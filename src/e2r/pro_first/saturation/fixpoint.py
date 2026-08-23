"""Stable-gap semantic no-new-public-route fixpoint."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from ..ids import canonical_hash


@dataclass(frozen=True)
class NoNewRouteConfirmation:
    confirmation_id: str
    stable_gap_key: str
    question_family_id: str
    pass_id: str
    route_receipt_id: str
    route_signature: str
    fact_snapshot_hash: str
    accepted_lineage_roster_hash: str
    attempted_source_roles_hash: str
    provider_status: str
    parser_status: str
    new_accepted_fact_delta: int
    no_new_route_reason: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.confirmation_id, "confirmation_id"),
            (self.stable_gap_key, "stable_gap_key"),
            (self.question_family_id, "question_family_id"),
            (self.pass_id, "pass_id"),
            (self.route_receipt_id, "route_receipt_id"),
            (self.route_signature, "route_signature"),
            (self.no_new_route_reason, "no_new_route_reason"),
        ):
            if not value.strip():
                raise ValueError(f"{label} is required")
        for value in (
            self.fact_snapshot_hash,
            self.accepted_lineage_roster_hash,
            self.attempted_source_roles_hash,
        ):
            if len(value) != 64:
                raise ValueError("fixpoint snapshots must be sha256")
        if self.new_accepted_fact_delta < 0:
            raise ValueError("accepted fact delta must be nonnegative")

    @classmethod
    def from_route_receipt(
        cls,
        *,
        receipt: dict,
        stable_gap_key: str,
        fact_snapshot_hash: str,
        accepted_lineage_roster_hash: str,
        attempted_source_roles_hash: str,
    ) -> "NoNewRouteConfirmation":
        route_signature = canonical_hash(
            {
                "source_role_id": receipt.get("source_role_id"),
                "query_or_navigation_objective": receipt.get(
                    "query_or_navigation_objective"
                ),
                "query_text": receipt.get("query_text"),
                "opened_source_urls": sorted(receipt.get("opened_source_urls") or ()),
            }
        )
        receipt_id = str(receipt.get("route_receipt_id") or "")
        return cls(
            confirmation_id=canonical_hash(
                {
                    "stable_gap_key": stable_gap_key,
                    "route_receipt_id": receipt_id,
                    "fact_snapshot_hash": fact_snapshot_hash,
                    "accepted_lineage_roster_hash": accepted_lineage_roster_hash,
                    "attempted_source_roles_hash": attempted_source_roles_hash,
                }
            ),
            stable_gap_key=stable_gap_key,
            question_family_id=str(receipt.get("question_family_id") or ""),
            pass_id=str(receipt.get("pass_id") or ""),
            route_receipt_id=receipt_id,
            route_signature=route_signature,
            fact_snapshot_hash=fact_snapshot_hash,
            accepted_lineage_roster_hash=accepted_lineage_roster_hash,
            attempted_source_roles_hash=attempted_source_roles_hash,
            provider_status=str(receipt.get("provider_status") or ""),
            parser_status=str(receipt.get("parser_status") or "SUCCESS"),
            new_accepted_fact_delta=len(receipt.get("accepted_fact_ids") or ()),
            no_new_route_reason=str(receipt.get("no_new_route_reason") or ""),
        )


@dataclass(frozen=True)
class SemanticFixpointDecision:
    stable_gap_key: str
    question_family_id: str
    reached: bool
    disposition: str
    accepted_confirmation_ids: tuple[str, ...]
    failure_codes: tuple[str, ...]
    fact_snapshot_hash: str | None
    accepted_lineage_roster_hash: str | None
    attempted_source_roles_hash: str | None


def evaluate_semantic_no_new_route_fixpoint(
    confirmations: Sequence[NoNewRouteConfirmation],
    *,
    minimum_independent_confirmations: int = 2,
) -> SemanticFixpointDecision:
    rows = tuple(confirmations)
    if minimum_independent_confirmations < 2:
        raise ValueError("semantic fixpoint requires at least two confirmations")
    failures: list[str] = []
    if not rows:
        failures.append("NO_CONFIRMATION")
        return SemanticFixpointDecision(
            stable_gap_key="",
            question_family_id="",
            reached=False,
            disposition="PUBLIC_ROUTE_STILL_OPEN",
            accepted_confirmation_ids=(),
            failure_codes=tuple(failures),
            fact_snapshot_hash=None,
            accepted_lineage_roster_hash=None,
            attempted_source_roles_hash=None,
        )
    keys = {row.stable_gap_key for row in rows}
    questions = {row.question_family_id for row in rows}
    fact_hashes = {row.fact_snapshot_hash for row in rows}
    lineage_hashes = {row.accepted_lineage_roster_hash for row in rows}
    source_role_hashes = {row.attempted_source_roles_hash for row in rows}
    if len(keys) != 1:
        failures.append("STABLE_GAP_KEY_MISMATCH")
    if len(questions) != 1:
        failures.append("QUESTION_FAMILY_MISMATCH")
    if len(fact_hashes) != 1:
        failures.append("FACT_SNAPSHOT_MISMATCH")
    if len(lineage_hashes) != 1:
        failures.append("ACCEPTED_LINEAGE_ROSTER_MISMATCH")
    if len(source_role_hashes) != 1:
        failures.append("ATTEMPTED_SOURCE_ROLES_MISMATCH")
    if len({row.confirmation_id for row in rows}) != len(rows):
        failures.append("DUPLICATE_CONFIRMATION")
    if len({row.pass_id for row in rows}) < minimum_independent_confirmations:
        failures.append("INSUFFICIENT_INDEPENDENT_PASSES")
    if len({row.route_signature for row in rows}) < minimum_independent_confirmations:
        failures.append("INSUFFICIENT_INDEPENDENT_ROUTES")
    if any(row.provider_status != "SUCCESS" for row in rows):
        failures.append("PROVIDER_NOT_NORMAL")
    if any(row.parser_status != "SUCCESS" for row in rows):
        failures.append("PARSER_NOT_NORMAL")
    if any(row.new_accepted_fact_delta != 0 for row in rows):
        failures.append("NEW_ACCEPTED_FACT_DELTA_NONZERO")
    if any(not row.no_new_route_reason.strip() for row in rows):
        failures.append("NO_NEW_ROUTE_REASON_MISSING")
    if len(rows) < minimum_independent_confirmations:
        failures.append("INSUFFICIENT_CONFIRMATION_COUNT")
    reached = not failures
    return SemanticFixpointDecision(
        stable_gap_key=next(iter(keys)) if len(keys) == 1 else "",
        question_family_id=next(iter(questions)) if len(questions) == 1 else "",
        reached=reached,
        disposition=(
            "SEMANTIC_NO_NEW_PUBLIC_ROUTE_FIXPOINT"
            if reached
            else "PUBLIC_ROUTE_STILL_OPEN"
        ),
        accepted_confirmation_ids=(
            tuple(row.confirmation_id for row in rows) if reached else ()
        ),
        failure_codes=tuple(dict.fromkeys(failures)),
        fact_snapshot_hash=next(iter(fact_hashes)) if len(fact_hashes) == 1 else None,
        accepted_lineage_roster_hash=(
            next(iter(lineage_hashes)) if len(lineage_hashes) == 1 else None
        ),
        attempted_source_roles_hash=(
            next(iter(source_role_hashes)) if len(source_role_hashes) == 1 else None
        ),
    )


__all__ = [
    "NoNewRouteConfirmation",
    "SemanticFixpointDecision",
    "evaluate_semantic_no_new_route_fixpoint",
]
