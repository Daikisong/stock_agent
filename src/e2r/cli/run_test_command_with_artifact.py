"""Run a test command and write machine-readable evidence for Census gates."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from e2r.census.test_result_evidence import TEST_RESULT_ARTIFACT_SCHEMA


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", required=True, help="Path to write e2r_test_result_artifact_v1 JSON")
    parser.add_argument("--log", help="Path to write combined stdout/stderr log")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Command to run after --")
    args = parser.parse_args(argv)
    command = list(args.command)
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        parser.error("command is required after --")

    artifact_path = Path(args.artifact)
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    log_path = Path(args.log) if args.log else artifact_path.with_suffix(".log")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    started_at = datetime.now(timezone.utc)
    proc = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    finished_at = datetime.now(timezone.utc)
    combined_output = proc.stdout or ""
    log_path.write_text(combined_output, encoding="utf-8")
    log_sha256 = hashlib.sha256(log_path.read_bytes()).hexdigest()
    test_count = _parse_test_count(combined_output)
    failure_counts = _parse_failure_counts(combined_output)
    status = "OK" if proc.returncode == 0 and test_count > 0 and failure_counts == (0, 0) else "FAILED"
    artifact = {
        "schema_version": TEST_RESULT_ARTIFACT_SCHEMA,
        "command": command,
        "command_string": shlex.join(command),
        "started_at": started_at.isoformat(),
        "finished_at": finished_at.isoformat(),
        "duration_seconds": round((finished_at - started_at).total_seconds(), 4),
        "exit_code": proc.returncode,
        "status": status,
        "test_count": test_count,
        "failed_count": failure_counts[0],
        "error_count": failure_counts[1],
        "log_path": str(log_path),
        "log_sha256": log_sha256,
    }
    artifact_path.write_text(json.dumps(artifact, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return proc.returncode


def _parse_test_count(output: str) -> int:
    matches = re.findall(r"\bRan\s+(\d+)\s+tests?\b", output)
    if not matches:
        return 0
    return int(matches[-1])


def _parse_failure_counts(output: str) -> tuple[int, int]:
    if re.search(r"^\s*OK\s*$", output, flags=re.MULTILINE):
        return (0, 0)
    failed = 0
    errors = 0
    match = re.search(r"FAILED\s*\(([^)]*)\)", output)
    if match:
        parts = match.group(1).split(",")
        for part in parts:
            key_value = part.strip().split("=", 1)
            if len(key_value) != 2:
                continue
            key, value = key_value
            if key == "failures":
                failed = int(value)
            elif key == "errors":
                errors = int(value)
    return failed, errors


if __name__ == "__main__":
    raise SystemExit(main())
