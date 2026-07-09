"""Canonical command status before a reconstruction phase is implemented."""

from __future__ import annotations

from typing import Any


def reconstruction_pending_payload(
    *,
    command: str,
    required_phase: int,
    inputs: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": "e2r_reconstruction_command_status_v1",
        "command": command,
        "status": "RECONSTRUCTION_COMPONENT_NOT_READY",
        "required_phase": required_phase,
        "canonical_readiness_eligible": False,
        "inputs": dict(inputs or {}),
    }


__all__ = ["reconstruction_pending_payload"]
