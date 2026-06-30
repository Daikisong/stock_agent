"""Existing ledger Census v3 source family attempt rows."""

from __future__ import annotations

from . import attempt_row


def collect_existing_ledger_attempt(symbol: str, *, accepted_claim_count: int = 0) -> dict:
    return attempt_row(
        symbol=symbol,
        source_family="ExistingEvidenceOSLedger",
        status="CURRENT_ACCEPTED_CLAIM_PRESENT" if accepted_claim_count else "LEDGER_CHECKED_NO_CURRENT_ACCEPTED_CLAIM",
        detail={"accepted_claim_count": accepted_claim_count},
    )


__all__ = ["collect_existing_ledger_attempt"]
