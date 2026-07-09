"""Shared guard for pre-reconstruction command-line entrypoints."""

from __future__ import annotations

import json
from typing import Any


LEGACY_DIAGNOSTIC_STATUS = "LEGACY_DIAGNOSTIC_ONLY"


def legacy_cli_block_payload(*, command: str, replacement: str) -> dict[str, Any]:
    return {
        "status": LEGACY_DIAGNOSTIC_STATUS,
        "command": command,
        "canonical_readiness_eligible": False,
        "canonical_ready_label_allowed": False,
        "replacement": replacement,
        "reason": "legacy command requires explicit diagnostic opt-in",
    }


def print_legacy_cli_block(*, command: str, replacement: str) -> None:
    print(
        json.dumps(
            legacy_cli_block_payload(command=command, replacement=replacement),
            ensure_ascii=False,
            sort_keys=True,
        )
    )


__all__ = [
    "LEGACY_DIAGNOSTIC_STATUS",
    "legacy_cli_block_payload",
    "print_legacy_cli_block",
]
