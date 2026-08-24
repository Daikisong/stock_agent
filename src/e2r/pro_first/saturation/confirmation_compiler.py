"""Compile exact-gap fixpoint confirmations from audited V2 route receipts.

A route receipt is not allowed to inherit the *latest* fact/lineage snapshot.
It is bound to the earliest durable effective-dossier snapshot that contains
that route.  This prevents an old empty response from being relabelled as a
confirmation for a newer evidence state.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash, stable_id
from .fixpoint import NoNewRouteConfirmation
from .snapshots import compile_verified_research_snapshot


@dataclass(frozen=True)
class FixpointConfirmationCompilation:
    confirmations: tuple[NoNewRouteConfirmation, ...]
    fact_snapshot_hash: str
    accepted_lineage_roster_hash: str
    attempted_source_roles_hash_by_question: Mapping[str, str]
    skipped_route_receipt_ids: tuple[str, ...]

    def for_question(self, question_family_id: str) -> tuple[NoNewRouteConfirmation, ...]:
        return tuple(
            row
            for row in self.confirmations
            if row.question_family_id == question_family_id
        )


@dataclass(frozen=True)
class RouteSnapshotBindingCompilation:
    bindings_by_route_receipt_id: Mapping[str, Mapping[str, str]]
    bound_route_receipt_ids: tuple[str, ...]
    skipped_route_receipt_ids: tuple[str, ...]


def compile_route_snapshot_bindings(
    dossier_snapshots: Sequence[Mapping[str, Any]],
    *,
    verified_fact_ids: Sequence[str],
) -> RouteSnapshotBindingCompilation:
    """Bind every route to the first cumulative dossier snapshot containing it.

    ``dossier_snapshots`` must be in pass order.  The caller supplies the final
    deterministic accepted-candidate roster; each historical snapshot uses
    only accepted candidates that already existed at that pass.
    """

    snapshots = tuple(dossier_snapshots)
    if not snapshots:
        return RouteSnapshotBindingCompilation({}, (), ())
    job_ids = {str(row.get("job_id") or "") for row in snapshots}
    run_ids = {str(row.get("run_id") or "") for row in snapshots}
    conversations = {str(row.get("conversation_id") or "") for row in snapshots}
    if len(job_ids) != 1 or len(run_ids) != 1 or len(conversations) != 1:
        raise ValueError("route snapshot compilation requires one durable research scope")
    final_verified = frozenset(str(value) for value in verified_fact_ids)
    bindings: dict[str, Mapping[str, str]] = {}
    skipped: list[str] = []
    seen_routes: set[str] = set()
    for dossier in snapshots:
        snapshot_fact_ids = {
            str(fact.get("dossier_fact_id") or "")
            for collection in ("material_facts", "counterfacts", "resolution_facts")
            for fact in dossier.get(collection) or ()
        }
        historical_verified = tuple(sorted(final_verified.intersection(snapshot_fact_ids)))
        evidence_snapshot = compile_verified_research_snapshot(
            dossier,
            historical_verified,
        )
        questions = {
            str(row.get("question_family_id") or ""): row
            for row in dossier.get("question_family_results") or ()
        }
        target = dossier.get("target") or {}
        target_id = str(target.get("target_id") or target.get("symbol") or "")
        current_pass_id = str(dossier.get("research_pass_id") or "")
        for route in dossier.get("search_route_receipts") or ():
            receipt_id = str(route.get("route_receipt_id") or "")
            if not receipt_id or receipt_id in seen_routes:
                continue
            seen_routes.add(receipt_id)
            question_id = str(route.get("question_family_id") or "")
            archetype_id = str(route.get("archetype_id") or "")
            route_pass_id = str(route.get("pass_id") or "")
            question = questions.get(question_id)
            if (
                question is None
                or str(question.get("archetype_id") or "") != archetype_id
                or route_pass_id != current_pass_id
            ):
                skipped.append(receipt_id)
                continue
            requested_ids = {
                str(value)
                for value in question.get("search_route_receipt_ids") or ()
            }
            if receipt_id not in requested_ids:
                skipped.append(receipt_id)
                continue
            linked_routes = tuple(
                row
                for row in dossier.get("search_route_receipts") or ()
                if str(row.get("route_receipt_id") or "") in requested_ids
                and str(row.get("question_family_id") or "") == question_id
                and str(row.get("archetype_id") or "") == archetype_id
            )
            attempted_roles = sorted(
                {
                    str(value)
                    for value in question.get("attempted_source_role_ids") or ()
                }
                | {
                    str(row.get("source_role_id") or "")
                    for row in linked_routes
                }
            )
            stable_gap_key = stable_id(
                "PROGAP",
                {
                    "job_id": dossier.get("job_id"),
                    "target_id": target_id,
                    "as_of_date": dossier.get("as_of_date"),
                    "archetype_id": archetype_id,
                    "question_family_id": question_id,
                },
            )
            bindings[receipt_id] = {
                "route_receipt_id": receipt_id,
                "pass_id": route_pass_id,
                "question_family_id": question_id,
                "archetype_id": archetype_id,
                "stable_gap_key": stable_gap_key,
                "fact_snapshot_hash": evidence_snapshot.fact_snapshot_hash,
                "accepted_lineage_roster_hash": (
                    evidence_snapshot.accepted_lineage_roster_hash
                ),
                "attempted_source_roles_hash": canonical_hash(attempted_roles),
            }
    return RouteSnapshotBindingCompilation(
        bindings_by_route_receipt_id=dict(sorted(bindings.items())),
        bound_route_receipt_ids=tuple(sorted(bindings)),
        skipped_route_receipt_ids=tuple(dict.fromkeys(skipped)),
    )


def compile_fixpoint_confirmations(
    dossier: Mapping[str, Any],
    *,
    verified_fact_ids: Sequence[str],
    route_snapshot_bindings: Mapping[str, Mapping[str, Any]] | None = None,
) -> FixpointConfirmationCompilation:
    """Use question identity and exact pass snapshots, never current relabelling."""

    snapshot = compile_verified_research_snapshot(dossier, verified_fact_ids)
    routes = tuple(dossier.get("search_route_receipts") or ())
    route_by_id = {
        str(row.get("route_receipt_id") or ""): row for row in routes
    }
    if len(route_by_id) != len(routes):
        raise ValueError("duplicate route receipt ids are forbidden")
    target = dossier.get("target") or {}
    target_id = str(target.get("target_id") or target.get("symbol") or "")
    confirmations: list[NoNewRouteConfirmation] = []
    attempted_hashes: dict[str, str] = {}
    skipped: list[str] = []
    for result in dossier.get("question_family_results") or ():
        question_id = str(result.get("question_family_id") or "")
        archetype_id = str(result.get("archetype_id") or "")
        requested_ids = tuple(
            str(value) for value in result.get("search_route_receipt_ids") or ()
        )
        linked = []
        for receipt_id in requested_ids:
            route = route_by_id.get(receipt_id)
            if route is None:
                raise ValueError("question references an unknown route receipt")
            if (
                str(route.get("question_family_id") or "") != question_id
                or str(route.get("archetype_id") or "") != archetype_id
            ):
                raise ValueError("route receipt belongs to another question gap")
            linked.append(route)
        attempted_roles = sorted(
            {
                str(value)
                for value in result.get("attempted_source_role_ids") or ()
            }
            | {str(row.get("source_role_id") or "") for row in linked}
        )
        attempted_hash = canonical_hash(attempted_roles)
        attempted_hashes[question_id] = attempted_hash
        stable_gap_key = stable_id(
            "PROGAP",
            {
                "job_id": dossier.get("job_id"),
                "target_id": target_id,
                "as_of_date": dossier.get("as_of_date"),
                "archetype_id": archetype_id,
                "question_family_id": question_id,
            },
        )
        for route in linked:
            receipt_id = str(route.get("route_receipt_id") or "")
            if tuple(route.get("accepted_fact_ids") or ()) or not str(
                route.get("no_new_route_reason") or ""
            ).strip():
                skipped.append(receipt_id)
                continue
            binding = (route_snapshot_bindings or {}).get(receipt_id)
            if not isinstance(binding, Mapping):
                skipped.append(receipt_id)
                continue
            expected_binding = {
                "route_receipt_id": receipt_id,
                "pass_id": str(route.get("pass_id") or ""),
                "question_family_id": question_id,
                "archetype_id": archetype_id,
                "stable_gap_key": stable_gap_key,
            }
            if any(str(binding.get(key) or "") != value for key, value in expected_binding.items()):
                skipped.append(receipt_id)
                continue
            hashes = tuple(
                str(binding.get(key) or "")
                for key in (
                    "fact_snapshot_hash",
                    "accepted_lineage_roster_hash",
                    "attempted_source_roles_hash",
                )
            )
            if any(len(value) != 64 for value in hashes):
                skipped.append(receipt_id)
                continue
            confirmations.append(
                NoNewRouteConfirmation.from_route_receipt(
                    receipt=dict(route),
                    stable_gap_key=stable_gap_key,
                    fact_snapshot_hash=hashes[0],
                    accepted_lineage_roster_hash=hashes[1],
                    attempted_source_roles_hash=hashes[2],
                )
            )
    return FixpointConfirmationCompilation(
        confirmations=tuple(confirmations),
        fact_snapshot_hash=snapshot.fact_snapshot_hash,
        accepted_lineage_roster_hash=snapshot.accepted_lineage_roster_hash,
        attempted_source_roles_hash_by_question=dict(sorted(attempted_hashes.items())),
        skipped_route_receipt_ids=tuple(dict.fromkeys(skipped)),
    )


__all__ = [
    "FixpointConfirmationCompilation",
    "RouteSnapshotBindingCompilation",
    "compile_fixpoint_confirmations",
    "compile_route_snapshot_bindings",
]
