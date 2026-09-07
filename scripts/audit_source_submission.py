from __future__ import annotations

import argparse
import ast
import importlib
import json
import re
import sys
from collections import defaultdict, deque
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile

from docx import Document


NUMBERED_LINE = re.compile(r"^\s*(\d+)\s{2}(.*)$")
FILE_MARKER = re.compile(r"^(#|//|--|;)\s*File:\s*(.+?)(?:\s+\(lines .+\))?$")
DEFAULT_BANNED_TERMS = (
    "软件申请表",
    "软著",
    "第二件",
    "科研",
    "论文",
    "投稿",
    "材料合规",
    "设计核检",
    "soft-copyright",
    "registration-oriented",
    "export-materials-profile",
    "audit-design",
)
DEFAULT_EXCLUDED_PARTS = {
    "__pycache__",
    "tests",
    "test",
    "examples",
    "example",
    "docs",
    "doc",
    "materials",
    "quality",
    ".git",
    ".venv",
    "venv",
}


def extract_numbered_lines(docx_path: Path) -> list[str]:
    document = Document(str(docx_path))
    numbered: list[tuple[int, str]] = []
    for paragraph in document.paragraphs:
        match = NUMBERED_LINE.match(paragraph.text)
        if match:
            numbered.append((int(match.group(1)), match.group(2)))
    if not numbered:
        raise ValueError("No numbered code lines were found in the DOCX")
    numbers = [number for number, _ in numbered]
    expected = list(range(1, len(numbered) + 1))
    if numbers != expected:
        raise ValueError("DOCX line numbers are not continuous from 1")
    return [line for _, line in numbered]


def split_files(lines: list[str]) -> tuple[dict[str, list[str]], dict[str, str], list[str]]:
    files: dict[str, list[str]] = {}
    marker_styles: dict[str, str] = {}
    partial_markers: list[str] = []
    current: str | None = None
    for line in lines:
        marker = FILE_MARKER.match(line)
        if marker:
            style, path = marker.groups()
            if "(lines " in line:
                partial_markers.append(line)
            current = path
            if current in files:
                raise ValueError(f"Duplicate file marker: {current}")
            files[current] = []
            marker_styles[current] = style
            continue
        if current is None:
            raise ValueError("Material contains source before the first file marker")
        files[current].append(line)
    return files, marker_styles, partial_markers


def module_name(package: str, rel_path: str) -> str:
    parts = list(Path(rel_path).with_suffix("").parts)
    if parts and parts[-1] == "__init__":
        parts.pop()
    if parts and parts[0] == package:
        parts.pop(0)
    return ".".join((package, *parts)) if parts else package


def resolve_import(current: str, node: ast.ImportFrom) -> str | None:
    if node.level == 0:
        return node.module
    current_parts = current.split(".")[:-1]
    keep = max(0, len(current_parts) - node.level + 1)
    prefix = current_parts[:keep]
    if node.module:
        prefix.extend(node.module.split("."))
    return ".".join(prefix)


def imported_modules(package: str, rel_path: str, lines: list[str]) -> set[str]:
    tree = ast.parse("\n".join(lines), filename=rel_path)
    current = module_name(package, rel_path)
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            resolved = resolve_import(current, node)
            if resolved:
                imports.add(resolved)
    return imports


def package_target(imported: str, modules: set[str]) -> str | None:
    candidates = [name for name in modules if imported == name or imported.startswith(name + ".")]
    return max(candidates, key=len) if candidates else None


def zip_integrity(path: Path) -> bool:
    try:
        with ZipFile(path) as archive:
            return archive.testzip() is None and "word/document.xml" in archive.namelist()
    except Exception:
        return False


def source_candidates(project: Path, suffixes: set[str]) -> list[str]:
    candidates: list[str] = []
    for path in project.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        rel = path.relative_to(project)
        if any(part.casefold() in DEFAULT_EXCLUDED_PARTS for part in rel.parts):
            continue
        candidates.append(rel.as_posix())
    return sorted(candidates)


def write_markdown(report: dict[str, object], path: Path) -> None:
    lines = [
        "# Source Submission Audit",
        "",
        f"- DOCX: `{report['docx']}`",
        f"- Source files: {report['source_file_count']}",
        f"- Source lines: {report['source_line_count']}",
        f"- Material lines: {report['material_line_count']}",
        f"- Calculated pages: {report['calculated_pages']}",
        f"- Exact source match: {'yes' if report['exact_source_match'] else 'no'}",
        f"- Syntax check: {'passed' if not report['syntax_errors'] else 'failed'}",
        f"- Import check: {'passed' if not report['import_errors'] else 'failed'}",
        f"- Strict fidelity: {'passed' if report['strict_fidelity_passed'] else 'failed'}",
        "",
        "## Unreachable substantive modules",
        "",
    ]
    unreachable = report.get("unreachable_substantive_modules", [])
    lines.extend(f"- `{item}`" for item in unreachable)
    lines.extend(["", "## Unreferenced substantive modules", ""])
    lines.extend(f"- `{item}`" for item in report.get("unreferenced_substantive_modules", []))
    lines.extend(["", "## Unselected source candidates", ""])
    lines.extend(f"- `{item}`" for item in report.get("unselected_source_candidates", []))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit source-code DOCX fidelity and Python call graph")
    parser.add_argument("--docx", required=True, type=Path)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--output-json", required=True, type=Path)
    parser.add_argument("--output-md", required=True, type=Path)
    parser.add_argument("--package", help="Python package name for call/import audit")
    parser.add_argument("--entry", action="append", default=[], help="Python entry module; repeatable")
    parser.add_argument("--old-name", action="append", default=[])
    parser.add_argument("--ban", action="append", default=[])
    parser.add_argument("--import-check", action="store_true")
    args = parser.parse_args()

    docx_path = args.docx.resolve()
    project = args.project.resolve()
    lines = extract_numbered_lines(docx_path)
    files, marker_styles, partial_markers = split_files(lines)

    missing_sources: list[str] = []
    outside_project: list[str] = []
    source_mismatches: list[dict[str, object]] = []
    marker_style_errors: list[str] = []
    source_line_count = 0

    for rel_path, submitted_lines in files.items():
        source_line_count += len(submitted_lines)
        source_path = (project / rel_path).resolve()
        try:
            source_path.relative_to(project)
        except ValueError:
            outside_project.append(rel_path)
            continue
        if not source_path.exists():
            missing_sources.append(rel_path)
            continue
        actual_lines = source_path.read_text(encoding="utf-8").splitlines()
        if actual_lines != submitted_lines:
            source_mismatches.append(
                {
                    "path": rel_path,
                    "submitted_lines": len(submitted_lines),
                    "project_lines": len(actual_lines),
                    "submitted_sha256": sha256("\n".join(submitted_lines).encode("utf-8")).hexdigest(),
                    "project_sha256": sha256("\n".join(actual_lines).encode("utf-8")).hexdigest(),
                }
            )
        if source_path.suffix.lower() == ".py" and marker_styles[rel_path] != "#":
            marker_style_errors.append(rel_path)

    banned_terms = tuple(dict.fromkeys((*DEFAULT_BANNED_TERMS, *args.old_name, *args.ban)))
    joined = "\n".join(lines)
    banned_hits = [term for term in banned_terms if term and term.casefold() in joined.casefold()]

    syntax_errors: list[dict[str, str]] = []
    import_errors: list[dict[str, str]] = []
    reachable_modules: list[str] = []
    unreachable_paths: list[str] = []
    unreferenced_paths: list[str] = []

    if args.package:
        python_files = {path: payload for path, payload in files.items() if path.endswith(".py")}
        modules = {module_name(args.package, path) for path in python_files}
        module_to_path = {module_name(args.package, path): path for path in python_files}
        edges: dict[str, set[str]] = defaultdict(set)
        imported_by: dict[str, set[str]] = defaultdict(set)

        for rel_path, submitted_lines in python_files.items():
            current = module_name(args.package, rel_path)
            try:
                imports = imported_modules(args.package, rel_path, submitted_lines)
            except SyntaxError as exc:
                syntax_errors.append({"path": rel_path, "error": str(exc)})
                continue
            for imported in imports:
                target = package_target(imported, modules)
                if target and target != current:
                    edges[current].add(target)
                    imported_by[target].add(current)

        entries = args.entry or ([f"{args.package}.cli"] if f"{args.package}.cli" in modules else [])
        reachable: set[str] = set()
        queue = deque(entries)
        while queue:
            current = queue.popleft()
            if current in reachable:
                continue
            reachable.add(current)
            queue.extend(edges.get(current, ()))
        reachable_modules = sorted(reachable & modules)

        substantive = {
            module: path
            for module, path in module_to_path.items()
            if not path.endswith("/__init__.py") and path != "__init__.py"
        }
        unreachable_paths = sorted(path for module, path in substantive.items() if entries and module not in reachable)
        unreferenced_paths = sorted(
            path for module, path in substantive.items() if module not in entries and not imported_by.get(module)
        )

        if args.import_check:
            sys.path.insert(0, str(project.parent))
            for module in sorted(modules):
                try:
                    importlib.import_module(module)
                except Exception as exc:
                    import_errors.append({"module": module, "error": f"{type(exc).__name__}: {exc}"})

    suffixes = {Path(path).suffix.lower() for path in files if Path(path).suffix}
    candidates = source_candidates(project, suffixes)
    unselected_candidates = sorted(set(candidates) - set(files))

    report: dict[str, object] = {
        "docx": str(docx_path),
        "project": str(project),
        "zip_integrity": zip_integrity(docx_path),
        "source_file_count": len(files),
        "source_line_count": source_line_count,
        "file_marker_line_count": len(files),
        "material_line_count": len(lines),
        "calculated_pages": (len(lines) + 49) // 50,
        "line_numbers_continuous": True,
        "partial_file_markers": partial_markers,
        "marker_style_errors": marker_style_errors,
        "outside_project": outside_project,
        "missing_sources": missing_sources,
        "source_mismatches": source_mismatches,
        "exact_source_match": not (outside_project or missing_sources or source_mismatches),
        "syntax_errors": syntax_errors,
        "import_errors": import_errors,
        "banned_term_hits": banned_hits,
        "reachable_module_count": len(reachable_modules),
        "reachable_modules": reachable_modules,
        "unreachable_substantive_modules": unreachable_paths,
        "unreferenced_substantive_modules": unreferenced_paths,
        "unselected_source_candidates": unselected_candidates,
    }
    report["strict_fidelity_passed"] = all(
        (
            report["zip_integrity"],
            report["line_numbers_continuous"],
            report["exact_source_match"],
            not partial_markers,
            not marker_style_errors,
            not syntax_errors,
            not import_errors,
            not banned_hits,
        )
    )

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(report, args.output_md)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
