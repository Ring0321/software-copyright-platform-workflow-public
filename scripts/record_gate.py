#!/usr/bin/env python3
"""Record workflow gates that are additional to the base copyright skill."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


STAGES = (
    "code-source-strategy",
    "cooperation-development",
    "registration-scope",
    "template",
    "final-submission",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Record an additional software-copyright workflow gate."
    )
    parser.add_argument("--workdir", required=True, help="Current isolated material package")
    parser.add_argument("--stage", required=True, choices=STAGES)
    parser.add_argument("--note", required=True, help="User-confirmed decision or evidence")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    workdir = Path(args.workdir).expanduser().resolve()
    workdir.mkdir(parents=True, exist_ok=True)
    output = workdir / "扩展门禁确认.json"

    if output.exists():
        payload = json.loads(output.read_text(encoding="utf-8"))
    else:
        payload = {"schema_version": 1, "current": {}, "history": []}

    now = datetime.now().astimezone().isoformat(timespec="seconds")
    record = {"stage": args.stage, "confirmed_at": now, "note": args.note.strip()}
    payload.setdefault("current", {})[args.stage] = record
    payload.setdefault("history", []).append(record)
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(output)


if __name__ == "__main__":
    main()
