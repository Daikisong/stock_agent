from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import subprocess
import sys
from typing import Sequence

from e2r.production.metadata import write_json
from e2r.research_brain.researcher_mode.independent_acceptance import (
    DEFAULT_FULL_TEST_EVIDENCE_PATH,
    verification_tree_hash,
)


_COUNT_RE = re.compile(r"Ran\s+(\d+)\s+tests?\s+in\s+([0-9.]+)s")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run full unittest discovery and write tree-bound evidence."
    )
    parser.add_argument("--workspace-root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=DEFAULT_FULL_TEST_EVIDENCE_PATH)
    parser.add_argument(
        "--log-output",
        type=Path,
        default=Path("docs/operational/e2r_v5_full_test_result.log"),
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.workspace_root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    log_path = args.log_output if args.log_output.is_absolute() else root / args.log_output
    log_path.parent.mkdir(parents=True, exist_ok=True)
    running_log_path = log_path.with_name(f".{log_path.name}.running")
    tree_before = verification_tree_hash(root)
    command = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        "tests",
        "-v",
    ]
    started = datetime.now(timezone.utc)
    with running_log_path.open("w", encoding="utf-8") as handle:
        process = subprocess.Popen(
            command,
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert process.stdout is not None
        for line in process.stdout:
            print(line, end="", flush=True)
            handle.write(line)
        exit_code = process.wait()
    finished = datetime.now(timezone.utc)
    tree_after = verification_tree_hash(root)
    raw = running_log_path.read_text(encoding="utf-8")
    running_log_path.replace(log_path)
    matches = tuple(_COUNT_RE.finditer(raw))
    test_count = int(matches[-1].group(1)) if matches else 0
    unittest_runtime = float(matches[-1].group(2)) if matches else None
    stable_tree = tree_before == tree_after
    passed = bool(exit_code == 0 and test_count > 0 and stable_tree)
    payload = {
        "schema_version": "e2r_v5_full_test_evidence_v1",
        "status": "PASS" if passed else "FAIL",
        "full_discovery": True,
        "command": command,
        "exit_code": exit_code,
        "test_count": test_count,
        "unittest_runtime_seconds": unittest_runtime,
        "wall_runtime_seconds": round((finished - started).total_seconds(), 6),
        "started_at": started.isoformat(),
        "finished_at": finished.isoformat(),
        "verification_tree_hash": tree_after,
        "verification_tree_stable_during_run": stable_tree,
        "log_path": str(log_path.relative_to(root)),
        "log_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
    }
    write_json(output, payload)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
