#!/usr/bin/env python3
"""Run reproducible Pro-first CI gates and emit one compact receipt."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Mapping, Sequence


def _run(
    command: Sequence[str], *, root: Path, environment: Mapping[str, str]
) -> dict:
    started = time.monotonic()
    completed = subprocess.run(
        list(command),
        cwd=root,
        env=dict(environment),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    output = completed.stdout
    match = re.search(r"Ran (\d+) tests?", output)
    return {
        "command": list(command),
        "returncode": completed.returncode,
        "status": "PASS" if completed.returncode == 0 else "FAIL",
        "tests_run": int(match.group(1)) if match else None,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "output_tail": output[-12_000:],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output", required=True)
    parser.add_argument("--full-regression", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.repo_root).expanduser().resolve()
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(root / "src")
    environment["E2R_RUN_LIVE_TESTS"] = "0"
    library_root = Path.home() / ".cache/e2r-playwright-libs/usr/lib/x86_64-linux-gnu"
    if library_root.is_dir():
        prior = environment.get("LD_LIBRARY_PATH")
        environment["LD_LIBRARY_PATH"] = f"{library_root}:{prior}" if prior else str(library_root)
    commands = [
        [sys.executable, "-m", "e2r.cli.verify_e2r_pro_first_readiness", "--repo-root", str(root)],
        [sys.executable, "-m", "e2r.cli.run_e2r_pro_first_offline_e2e"],
        [sys.executable, "-m", "e2r.cli.run_e2r_pro_first_browser_mock_e2e"],
        [sys.executable, "-m", "compileall", "-q", "src", "tests"],
        ["git", "diff", "--check"],
    ]
    if args.full_regression:
        commands.append(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]
        )
    rows = [_run(command, root=root, environment=environment) for command in commands]
    passed = all(row["returncode"] == 0 for row in rows)
    payload = {
        "schema_version": "e2r_pro_first_offline_ci_receipt_v1",
        "status": "PRO_FIRST_OFFLINE_CI_PASS" if passed else "PRO_FIRST_OFFLINE_CI_FAIL",
        "full_regression_requested": args.full_regression,
        "commands": rows,
        "recorded_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    destination = Path(args.output).expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(destination)
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
