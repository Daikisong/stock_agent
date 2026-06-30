"""Census claim reuse and lightweight ledger helpers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class ClaimReuseResult:
    claim_id: str
    reuse_status: str
    reason: str
    followup_task_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "claim_id": self.claim_id,
            "reuse_status": self.reuse_status,
            "reason": self.reason,
            "followup_task_id": self.followup_task_id,
        }


def evaluate_claim_reuse(
    claim: Mapping[str, Any],
    *,
    symbol: str,
    as_of_date: str,
    max_age_days: int = 365,
) -> ClaimReuseResult:
    claim_id = str(claim.get("claim_id") or claim.get("id") or "")
    if str(claim.get("symbol") or claim.get("target_symbol") or "") != symbol:
        return ClaimReuseResult(claim_id=claim_id, reuse_status="REJECTED_SCOPE", reason="symbol_mismatch")
    if str(claim.get("lifecycle") or claim.get("temporal_status") or "CURRENT").upper() not in {"CURRENT", "OPEN"}:
        return ClaimReuseResult(claim_id=claim_id, reuse_status="STALE_NEEDS_REFRESH", reason="not_current_lifecycle")
    if bool(claim.get("superseded")):
        return ClaimReuseResult(claim_id=claim_id, reuse_status="SUPERSEDED", reason="claim_superseded")
    if bool(claim.get("contradicted")):
        return ClaimReuseResult(claim_id=claim_id, reuse_status="CONTRADICTED", reason="claim_contradicted")
    if str(claim.get("polarity") or "").upper() == "NEGATIVE" and not bool(claim.get("current_open_followup")):
        return ClaimReuseResult(
            claim_id=claim_id,
            reuse_status="STALE_NEEDS_REFRESH",
            reason="old_risk_requires_current_open_followup",
        )
    published = str(claim.get("as_of_date") or claim.get("published_at") or "")
    if published and _age_days(published, as_of_date) > max_age_days:
        return ClaimReuseResult(claim_id=claim_id, reuse_status="STALE_NEEDS_REFRESH", reason="freshness_expired")
    return ClaimReuseResult(claim_id=claim_id, reuse_status="REUSED_CURRENT", reason="current_lifecycle_valid")


def reusable_claims(
    claims: Sequence[Mapping[str, Any]],
    *,
    symbol: str,
    as_of_date: str,
    max_age_days: int = 365,
) -> tuple[Mapping[str, Any], tuple[ClaimReuseResult, ...]]:
    results = tuple(evaluate_claim_reuse(claim, symbol=symbol, as_of_date=as_of_date, max_age_days=max_age_days) for claim in claims)
    reusable_ids = {row.claim_id for row in results if row.reuse_status == "REUSED_CURRENT"}
    return tuple(claim for claim in claims if str(claim.get("claim_id") or claim.get("id") or "") in reusable_ids), results


def _age_days(start: str, end: str) -> int:
    try:
        return (date.fromisoformat(end[:10]) - date.fromisoformat(start[:10])).days
    except ValueError:
        return 10**9


__all__ = ["ClaimReuseResult", "evaluate_claim_reuse", "reusable_claims"]
