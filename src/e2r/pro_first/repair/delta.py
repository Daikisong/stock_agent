"""Validate and apply append-only Pro repair deltas without trusting them."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash
from .models import (
    REPAIR_ACTIONS,
    RepairActionDecision,
    RepairApplication,
    VerifierRejectionPacket,
)


_FACT_COLLECTIONS = ("material_facts", "counterfacts", "resolution_facts")
_FORBIDDEN_AUTHORITY_FIELDS = frozenset(
    {"final_score", "final_stage", "canonical_stage", "score_value", "stage_decision"}
)


def apply_repair_delta(
    *,
    dossier: Mapping[str, Any],
    rejection_packets: Sequence[VerifierRejectionPacket],
    repair_delta: Mapping[str, Any],
    prior_accepted_candidate_ids: Sequence[str],
) -> RepairApplication:
    if repair_delta.get("schema_version") != "e2r_pro_verifier_repair_delta_v1":
        raise ValueError("unsupported verifier repair delta schema")
    for key, expected in (
        ("job_id", dossier.get("job_id")),
        ("conversation_id", dossier.get("conversation_id")),
    ):
        if repair_delta.get(key) != expected:
            raise ValueError(f"repair delta {key} mismatch")
    if repair_delta.get("score_authority") is not False:
        raise ValueError("repair delta must have score_authority=false")
    if repair_delta.get("stage_authority") is not False:
        raise ValueError("repair delta must have stage_authority=false")
    forbidden = _find_forbidden_fields(repair_delta)
    if forbidden:
        raise ValueError(f"repair delta contains forbidden authority fields: {forbidden}")
    pass_id = str(repair_delta.get("research_pass_id") or "")
    parent_pass_id = str(repair_delta.get("parent_pass_id") or "")
    if not pass_id or not parent_pass_id:
        raise ValueError("repair delta requires pass and parent lineage")

    packets = {row.packet_id: row for row in rejection_packets}
    if len(packets) != len(tuple(rejection_packets)):
        raise ValueError("duplicate rejection packet ids are forbidden")
    packet_by_candidate = {row.candidate_id: row for row in rejection_packets}
    if len(packet_by_candidate) != len(packets):
        raise ValueError("one candidate cannot have multiple repair packets")
    original_facts = {
        str(row.get("dossier_fact_id") or ""): row
        for collection in _FACT_COLLECTIONS
        for row in dossier.get(collection) or ()
    }
    prior_accepted = tuple(
        dict.fromkeys(str(value) for value in prior_accepted_candidate_ids)
    )
    if not set(prior_accepted).issubset(original_facts):
        raise ValueError("prior accepted roster references an unknown dossier candidate")

    raw_actions = tuple(repair_delta.get("actions") or ())
    seen_packets: set[str] = set()
    seen_candidates: set[str] = set()
    replacement_ids: set[str] = set()
    decisions: list[RepairActionDecision] = []
    action_rows: list[tuple[Mapping[str, Any], VerifierRejectionPacket]] = []
    for action_row in raw_actions:
        packet_id = str(action_row.get("packet_id") or "")
        candidate_id = str(action_row.get("candidate_id") or "")
        packet = packets.get(packet_id)
        if packet is None or packet.candidate_id != candidate_id:
            raise ValueError("repair action escapes its rejection packet")
        if packet_id in seen_packets or candidate_id in seen_candidates:
            raise ValueError("one rejected candidate may have only one repair action")
        seen_packets.add(packet_id)
        seen_candidates.add(candidate_id)
        if candidate_id in set(prior_accepted):
            raise ValueError("repair action cannot target an accepted fact")
        action = str(action_row.get("action") or "")
        if action not in REPAIR_ACTIONS:
            raise ValueError("repair action is not allowed")
        question_ids = tuple(
            dict.fromkeys(
                str(value) for value in action_row.get("question_family_ids") or ()
            )
        )
        if set(question_ids) != set(packet.question_family_ids):
            raise ValueError("repair action question scope differs from the packet")
        corrected = action_row.get("corrected_fact")
        replacement_id = None
        if action == "WITHDRAWN":
            if corrected is not None:
                raise ValueError("WITHDRAWN cannot carry a corrected fact")
        else:
            if not isinstance(corrected, Mapping):
                raise ValueError("non-withdrawn repair requires a corrected fact")
            replacement_id = str(corrected.get("dossier_fact_id") or "")
            if (
                not replacement_id
                or replacement_id in original_facts
                or replacement_id in replacement_ids
            ):
                raise ValueError("corrected fact requires a new unique candidate id")
            replacement_ids.add(replacement_id)
            if corrected.get("repair_of_candidate_id") != candidate_id:
                raise ValueError("corrected fact lacks exact repair lineage")
            if corrected.get("research_pass_id") != pass_id:
                raise ValueError("corrected fact belongs to another research pass")
            if str(corrected.get("target_id") or "") != str(
                (dossier.get("target") or {}).get("target_id")
                or (dossier.get("target") or {}).get("symbol")
                or ""
            ):
                raise ValueError("corrected fact changed the target")
            if set(str(value) for value in corrected.get("question_family_ids") or ()) != set(
                packet.question_family_ids
            ):
                raise ValueError("corrected fact changed its question-family scope")
        action_hash = canonical_hash(action_row)
        decisions.append(
            RepairActionDecision(
                packet_id=packet_id,
                candidate_id=candidate_id,
                question_family_ids=question_ids,
                action=action,
                replacement_candidate_id=replacement_id,
                action_hash=action_hash,
            )
        )
        action_rows.append((action_row, packet))

    effective = deepcopy(dict(dossier))
    accepted_before = {
        candidate_id: canonical_hash(original_facts[candidate_id])
        for candidate_id in prior_accepted
    }
    for action_row, packet in action_rows:
        _remove_candidate(effective, packet.candidate_id)
        action = str(action_row["action"])
        corrected = action_row.get("corrected_fact")
        if action != "WITHDRAWN":
            collection = _candidate_collection(dossier, packet.candidate_id)
            effective.setdefault(collection, []).append(deepcopy(dict(corrected)))
            _replace_source_lineage_reference(
                effective,
                old_candidate_id=packet.candidate_id,
                replacement_fact=corrected,
                proposed_new_lineage=action_row.get("new_source_lineage"),
            )
            _replace_question_fact_reference(
                effective,
                old_candidate_id=packet.candidate_id,
                replacement_candidate_id=str(corrected["dossier_fact_id"]),
            )
            _append_repair_route_receipts(
                effective,
                routes=action_row.get("new_route_receipts") or (),
                pass_id=pass_id,
                question_family_ids=packet.question_family_ids,
                replacement_candidate_id=str(corrected["dossier_fact_id"]),
            )
        else:
            _replace_source_lineage_reference(
                effective,
                old_candidate_id=packet.candidate_id,
                replacement_fact=None,
                proposed_new_lineage=None,
            )
            _replace_question_fact_reference(
                effective,
                old_candidate_id=packet.candidate_id,
                replacement_candidate_id=None,
            )
            _mark_questions_public_after_withdrawal(
                effective,
                question_family_ids=packet.question_family_ids,
            )
        for question_id in packet.question_family_ids:
            effective.setdefault("verification_repair_register", []).append(
                {
                    "packet_id": packet.packet_id,
                    "candidate_id": packet.candidate_id,
                    "question_family_id": question_id,
                    "rejection_category": packet.rejection_category,
                    "status": action,
                    "replacement_candidate_id": (
                        str(corrected["dossier_fact_id"])
                        if corrected is not None
                        else None
                    ),
                    "original_candidate_hash": packet.original_candidate_hash,
                    "repair_action_hash": canonical_hash(action_row),
                    "research_pass_id": pass_id,
                    "parent_pass_id": parent_pass_id,
                    "score_authority": False,
                    "stage_authority": False,
                }
            )
    unhandled = tuple(
        packet_id for packet_id in packets if packet_id not in seen_packets
    )
    for packet_id in unhandled:
        packet = packets[packet_id]
        for question_id in packet.question_family_ids:
            effective.setdefault("verification_repair_register", []).append(
                {
                    "packet_id": packet.packet_id,
                    "candidate_id": packet.candidate_id,
                    "question_family_id": question_id,
                    "rejection_category": packet.rejection_category,
                    "status": "REPAIR_REQUIRED",
                    "replacement_candidate_id": None,
                    "original_candidate_hash": packet.original_candidate_hash,
                    "repair_action_hash": None,
                    "research_pass_id": pass_id,
                    "parent_pass_id": parent_pass_id,
                    "score_authority": False,
                    "stage_authority": False,
                }
            )
        _mark_questions_repair_required(
            effective,
            question_family_ids=packet.question_family_ids,
        )
    effective["research_pass_id"] = pass_id
    effective["parent_pass_id"] = parent_pass_id
    if unhandled or any(row.action != "WITHDRAWN" for row in decisions):
        effective["research_status"] = "NEEDS_VERIFIER_REPAIR"
    elif decisions:
        effective["research_status"] = "NEEDS_PUBLIC_GAP_CLOSURE"

    effective_facts = {
        str(row.get("dossier_fact_id") or ""): row
        for collection in _FACT_COLLECTIONS
        for row in effective.get(collection) or ()
    }
    accepted_after = tuple(
        candidate_id
        for candidate_id in prior_accepted
        if candidate_id in effective_facts
        and canonical_hash(effective_facts[candidate_id]) == accepted_before[candidate_id]
    )
    if set(accepted_after) != set(prior_accepted):
        raise ValueError("repair delta changed or deleted an accepted fact")
    return RepairApplication(
        effective_dossier=effective,
        actions=tuple(decisions),
        unhandled_packet_ids=unhandled,
        accepted_candidate_ids_preserved=accepted_after,
        delta_hash=canonical_hash(repair_delta),
    )


def _candidate_collection(dossier: Mapping[str, Any], candidate_id: str) -> str:
    matches = [
        collection
        for collection in _FACT_COLLECTIONS
        if any(
            str(row.get("dossier_fact_id") or "") == candidate_id
            for row in dossier.get(collection) or ()
        )
    ]
    if len(matches) != 1:
        raise ValueError("repair candidate must occur in exactly one fact collection")
    return matches[0]


def _remove_candidate(dossier: dict[str, Any], candidate_id: str) -> None:
    for collection in _FACT_COLLECTIONS:
        dossier[collection] = [
            row
            for row in dossier.get(collection) or ()
            if str(row.get("dossier_fact_id") or "") != candidate_id
        ]


def _replace_question_fact_reference(
    dossier: dict[str, Any],
    *,
    old_candidate_id: str,
    replacement_candidate_id: str | None,
) -> None:
    for question in dossier.get("question_family_results") or ():
        for key in ("support_fact_ids", "counter_fact_ids", "resolution_fact_ids"):
            values = [str(value) for value in question.get(key) or ()]
            if old_candidate_id not in values:
                continue
            question[key] = [
                replacement_candidate_id if value == old_candidate_id else value
                for value in values
                if value != old_candidate_id or replacement_candidate_id is not None
            ]


def _append_repair_route_receipts(
    dossier: dict[str, Any],
    *,
    routes: Sequence[Mapping[str, Any]],
    pass_id: str,
    question_family_ids: Sequence[str],
    replacement_candidate_id: str,
) -> None:
    if not routes:
        # Lower-level hand-authored repair deltas used by isolated unit tests
        # remain supported. Captured full-dossier responses enforce this route
        # in ``derive_repair_delta_from_dossier_response``.
        return
    allowed_questions = set(str(value) for value in question_family_ids)
    existing = {
        str(row.get("route_receipt_id") or "")
        for row in dossier.get("search_route_receipts") or ()
    }
    new_ids: list[str] = []
    role_by_question: dict[str, set[str]] = {}
    for route in routes:
        route_id = str(route.get("route_receipt_id") or "")
        question_id = str(route.get("question_family_id") or "")
        accepted = {
            str(value) for value in route.get("accepted_fact_ids") or ()
        }
        if (
            not route_id
            or route_id in existing
            or str(route.get("pass_id") or "") != pass_id
            or question_id not in allowed_questions
            or accepted != {replacement_candidate_id}
        ):
            raise ValueError("repair route receipt escapes its replacement fact scope")
        dossier.setdefault("search_route_receipts", []).append(deepcopy(dict(route)))
        existing.add(route_id)
        new_ids.append(route_id)
        role_by_question.setdefault(question_id, set()).add(
            str(route.get("source_role_id") or "")
        )
    for question in dossier.get("question_family_results") or ():
        question_id = str(question.get("question_family_id") or "")
        if question_id not in role_by_question:
            continue
        question["search_route_receipt_ids"] = list(
            dict.fromkeys(
                (
                    *(str(value) for value in question.get("search_route_receipt_ids") or ()),
                    *(
                        route_id
                        for route_id in new_ids
                        if any(
                            str(route.get("route_receipt_id") or "") == route_id
                            and str(route.get("question_family_id") or "") == question_id
                            for route in routes
                        )
                    ),
                )
            )
        )
        question["attempted_source_role_ids"] = list(
            dict.fromkeys(
                (
                    *(str(value) for value in question.get("attempted_source_role_ids") or ()),
                    *sorted(role_by_question[question_id]),
                )
            )
        )


def _mark_questions_public_after_withdrawal(
    dossier: dict[str, Any], *, question_family_ids: Sequence[str]
) -> None:
    affected = set(question_family_ids)
    for question in dossier.get("question_family_results") or ():
        if str(question.get("question_family_id") or "") not in affected:
            continue
        question["status"] = "PUBLIC_SEARCHABLE"
        question["availability_class"] = "PUBLIC_SEARCHABLE"
        question["adequate_search_proven"] = False
        question["closure_reason"] = (
            "deterministic verifier rejection was withdrawn; public evidence gap reopened"
        )


def _mark_questions_repair_required(
    dossier: dict[str, Any], *, question_family_ids: Sequence[str]
) -> None:
    affected = set(question_family_ids)
    for question in dossier.get("question_family_results") or ():
        if str(question.get("question_family_id") or "") not in affected:
            continue
        question["status"] = "VERIFIER_REPAIR_REQUIRED"
        question["closure_reason"] = (
            "material verifier rejection remains unresolved after repair pass"
        )


def _replace_source_lineage_reference(
    dossier: dict[str, Any],
    *,
    old_candidate_id: str,
    replacement_fact: Mapping[str, Any] | None,
    proposed_new_lineage: Any,
) -> None:
    replacement_id = (
        str(replacement_fact.get("dossier_fact_id") or "")
        if replacement_fact is not None
        else None
    )
    replacement_lineage_id = (
        str(replacement_fact.get("source_lineage_id") or "")
        if replacement_fact is not None
        else ""
    )
    lineages = dossier.setdefault("source_lineages", [])
    by_id = {
        str(row.get("source_lineage_id") or ""): row for row in lineages
    }
    for row in lineages:
        row["fact_ids"] = [
            str(value)
            for value in row.get("fact_ids") or ()
            if str(value) != old_candidate_id
        ]
    if replacement_fact is None:
        return
    if not replacement_lineage_id:
        raise ValueError("corrected fact requires source_lineage_id")
    lineage = by_id.get(replacement_lineage_id)
    if lineage is None:
        if not isinstance(proposed_new_lineage, Mapping):
            raise ValueError("new repair source lineage requires an explicit receipt")
        if proposed_new_lineage.get("source_lineage_id") != replacement_lineage_id:
            raise ValueError("new source lineage identity differs from corrected fact")
        source_url = str(replacement_fact.get("source_url") or "")
        if source_url not in set(
            str(value) for value in proposed_new_lineage.get("source_urls") or ()
        ):
            raise ValueError("new source lineage does not contain corrected source URL")
        lineage = deepcopy(dict(proposed_new_lineage))
        lineage["fact_ids"] = []
        lineages.append(lineage)
    elif proposed_new_lineage is not None:
        raise ValueError("existing source lineage cannot be overwritten by repair delta")
    source_url = str(replacement_fact.get("source_url") or "")
    if source_url not in set(str(value) for value in lineage.get("source_urls") or ()):
        raise ValueError(
            "corrected source URL requires a matching existing or new source lineage"
        )
    values = [str(value) for value in lineage.get("fact_ids") or ()]
    lineage["fact_ids"] = list(dict.fromkeys((*values, replacement_id)))


def _find_forbidden_fields(value: Any, path: str = "$") -> tuple[str, ...]:
    found: list[str] = []
    if isinstance(value, Mapping):
        for key, child in value.items():
            next_path = f"{path}.{key}"
            if str(key).lower() in _FORBIDDEN_AUTHORITY_FIELDS:
                found.append(next_path)
            found.extend(_find_forbidden_fields(child, next_path))
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            found.extend(_find_forbidden_fields(child, f"{path}[{index}]"))
    return tuple(found)


__all__ = ["apply_repair_delta"]
