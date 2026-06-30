"""Lifecycle policy helpers for Census v2."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping


DEFAULT_LIFECYCLE_POLICY_PATH = Path("configs/e2r_census_lifecycle_policy_v1.json")


@dataclass(frozen=True)
class LifecycleDecision:
    temporal_status: str
    score_eligible: bool
    followup_required: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "temporal_status": self.temporal_status,
            "score_eligible": self.score_eligible,
            "followup_required": self.followup_required,
            "reason": self.reason,
        }


def load_lifecycle_policy(path: str | Path = DEFAULT_LIFECYCLE_POLICY_PATH) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return _default_policy()
    payload = json.loads(p.read_text(encoding="utf-8"))
    return {**_default_policy(), **payload}


def adjudicate_lifecycle(
    *,
    event: Mapping[str, Any],
    as_of_date: str,
    policy: Mapping[str, Any] | None = None,
) -> LifecycleDecision:
    policy = dict(policy or _default_policy())
    if event.get("score_evidence_eligible") is True:
        return LifecycleDecision(
            temporal_status="CURRENT",
            score_eligible=True,
            followup_required=False,
            reason="accepted claim ledger event already passed current lifecycle refresh",
        )
    source_family = str(event.get("source_family") or "")
    event_date = str(event.get("published_at") or event.get("event_date") or event.get("to_date") or "")
    max_age = int((policy.get("stored_source_max_age_days_by_family") or {}).get(source_family, policy.get("default_stored_source_max_age_days", 365)))
    age = _age_days(event_date=event_date, as_of_date=as_of_date)
    if age is None:
        return LifecycleDecision(
            temporal_status="UNKNOWN",
            score_eligible=False,
            followup_required=True,
            reason="event date is missing or unparsable",
        )
    if age > max_age:
        return LifecycleDecision(
            temporal_status="HISTORICAL",
            score_eligible=False,
            followup_required=True,
            reason=f"stored source is {age} days old; requires current lifecycle refresh before scoring",
        )
    return LifecycleDecision(
        temporal_status="RECENT_UNVERIFIED",
        score_eligible=False,
        followup_required=True,
        reason="recent candidate/source event still needs accepted claim extraction before scoring",
    )


def _age_days(*, event_date: str, as_of_date: str) -> int | None:
    try:
        return (date.fromisoformat(as_of_date[:10]) - date.fromisoformat(event_date[:10])).days
    except (TypeError, ValueError):
        return None


def _default_policy() -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_lifecycle_policy_v1",
        "default_stored_source_max_age_days": 365,
        "stored_source_max_age_days_by_family": {
            "ReportRadar": 365,
            "TrustedNews": 90,
            "CompanyGuide": 120,
            "IR": 365,
            "OpenDART": 730,
            "KRXPrice": 30,
        },
        "score_policy": "accepted_current_claims_only",
        "unknown_policy": "unknown_is_not_present_and_not_absent",
    }


__all__ = ["DEFAULT_LIFECYCLE_POLICY_PATH", "LifecycleDecision", "adjudicate_lifecycle", "load_lifecycle_policy"]
