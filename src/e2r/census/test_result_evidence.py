"""Machine-readable test result evidence for Census v4 completion gates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping


TEST_RESULT_ARTIFACT_SCHEMA = "e2r_test_result_artifact_v1"


def validate_test_result_artifact(path: Path) -> dict[str, Any]:
    """Validate a machine-readable test result artifact.

    The artifact is completion evidence only if it proves a real command ran,
    exited successfully, and reported a positive test count. A random JSON file
    must not be enough to clear the goal-completion test blocker.
    """

    errors: list[str] = []
    artifact: Mapping[str, Any] | None = None
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    try:
        parsed = json.loads(raw.decode("utf-8"))
        if isinstance(parsed, dict):
            artifact = parsed
        else:
            errors.append("artifact root is not an object")
    except Exception as exc:  # pragma: no cover - exact JSON error text is not part of the contract
        errors.append(f"artifact is not valid JSON: {exc}")

    if artifact is None:
        return {
            "artifact_sha256": digest,
            "artifact_byte_size": len(raw),
            "artifact_valid": False,
            "artifact_validation_errors": errors,
        }

    if artifact.get("schema_version") != TEST_RESULT_ARTIFACT_SCHEMA:
        errors.append("schema_version must be e2r_test_result_artifact_v1")
    if not artifact.get("command"):
        errors.append("command is required")
    if artifact.get("exit_code") != 0:
        errors.append("exit_code must be 0")
    if artifact.get("status") != "OK":
        errors.append("status must be OK")
    test_count = artifact.get("test_count")
    if not isinstance(test_count, int) or test_count <= 0:
        errors.append("test_count must be a positive integer")
    if not artifact.get("started_at"):
        errors.append("started_at is required")
    if not artifact.get("finished_at"):
        errors.append("finished_at is required")
    if artifact.get("failed_count") not in (0, None):
        errors.append("failed_count must be 0 when present")
    if artifact.get("error_count") not in (0, None):
        errors.append("error_count must be 0 when present")

    log_path_value = artifact.get("log_path")
    log_sha256 = artifact.get("log_sha256")
    if log_path_value or log_sha256:
        if not log_path_value or not log_sha256:
            errors.append("log_path and log_sha256 must be provided together")
        else:
            log_path = Path(str(log_path_value)).expanduser()
            if not log_path.exists():
                errors.append("log_path does not exist")
            else:
                actual_log_sha256 = hashlib.sha256(log_path.read_bytes()).hexdigest()
                if actual_log_sha256 != log_sha256:
                    errors.append("log_sha256 does not match log_path content")

    return {
        "artifact_sha256": digest,
        "artifact_byte_size": len(raw),
        "artifact_valid": not errors,
        "artifact_validation_errors": errors,
        "artifact_schema_version": artifact.get("schema_version"),
        "artifact_command": artifact.get("command"),
        "artifact_exit_code": artifact.get("exit_code"),
        "artifact_status": artifact.get("status"),
        "artifact_test_count": artifact.get("test_count"),
        "artifact_failed_count": artifact.get("failed_count"),
        "artifact_error_count": artifact.get("error_count"),
        "artifact_started_at": artifact.get("started_at"),
        "artifact_finished_at": artifact.get("finished_at"),
        "artifact_duration_seconds": artifact.get("duration_seconds"),
        "artifact_log_path": artifact.get("log_path"),
        "artifact_log_sha256": artifact.get("log_sha256"),
    }


__all__ = ["TEST_RESULT_ARTIFACT_SCHEMA", "validate_test_result_artifact"]
