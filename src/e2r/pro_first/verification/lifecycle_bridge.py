"""Convert dossier lifecycle proposals into terminal verification dispositions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class LifecycleDisposition:
    status: str
    compile_as_evidence: bool
    direction: str | None
    current_lifecycle: str | None


class EvidenceLifecycleBridge:
    def classify(self, fact: Mapping[str, object]) -> LifecycleDisposition:
        lifecycle = str(fact.get("current_status") or "UNKNOWN").upper()
        direction = str(fact.get("direction") or "NEUTRAL").upper()
        if lifecycle == "SUPERSEDED":
            return LifecycleDisposition("SUPERSEDED", False, None, "SUPERSEDED")
        if lifecycle == "HISTORICAL":
            return LifecycleDisposition("HISTORICAL_ONLY", False, None, None)
        if lifecycle == "UNKNOWN":
            return LifecycleDisposition("UNVERIFIED_PENDING", False, None, None)
        if lifecycle == "RESOLVED":
            return LifecycleDisposition(
                "ACCEPTED_RESOLUTION", True, "RESOLUTION", "RESOLVED"
            )
        if lifecycle not in {"CURRENT", "OPEN"}:
            return LifecycleDisposition("UNVERIFIED_PENDING", False, None, None)
        if direction in {"COUNTER", "NEGATIVE"}:
            return LifecycleDisposition("ACCEPTED_COUNTER", True, "COUNTER", lifecycle)
        if direction in {"POSITIVE", "NEUTRAL", "RESOLUTION"}:
            return LifecycleDisposition("ACCEPTED_CURRENT", True, direction, lifecycle)
        return LifecycleDisposition("UNVERIFIED_PENDING", False, None, None)


__all__ = ["EvidenceLifecycleBridge", "LifecycleDisposition"]
