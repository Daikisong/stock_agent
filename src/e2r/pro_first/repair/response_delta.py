"""Derive the internal repair delta from a captured full ResearchDossierV2."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from .models import REPAIR_ACTIONS, VerifierRejectionPacket


_FACT_COLLECTIONS = ("material_facts", "counterfacts", "resolution_facts")


def derive_repair_delta_from_dossier_response(
    *,
    original_dossier: Mapping[str, Any],
    response_dossier: Mapping[str, Any],
    rejection_packets: Sequence[VerifierRejectionPacket],
    response_hash: str,
) -> Mapping[str, Any]:
    if response_dossier.get("schema_version") != "e2r_pro_research_dossier_v2":
        raise ValueError("repair response must be a full ResearchDossierV2")
    for key in ("job_id", "conversation_id"):
        if response_dossier.get(key) != original_dossier.get(key):
            raise ValueError(f"repair response {key} mismatch")
    if response_dossier.get("score_authority") is not False:
        raise ValueError("repair response must have score_authority=false")
    if response_dossier.get("stage_authority") is not False:
        raise ValueError("repair response must have stage_authority=false")
    if len(response_hash) != 64:
        raise ValueError("repair response hash must be sha256")
    pass_id = str(response_dossier.get("research_pass_id") or "")
    parent_pass_id = str(response_dossier.get("parent_pass_id") or "")
    if not pass_id or not parent_pass_id:
        raise ValueError("repair response lacks pass lineage")

    packets = {row.candidate_id: row for row in rejection_packets}
    original_facts = {
        str(row.get("dossier_fact_id") or ""): row
        for collection in _FACT_COLLECTIONS
        for row in original_dossier.get(collection) or ()
    }
    response_facts = {
        str(row.get("dossier_fact_id") or ""): row
        for collection in _FACT_COLLECTIONS
        for row in response_dossier.get(collection) or ()
    }
    if len(response_facts) != sum(
        len(tuple(response_dossier.get(collection) or ()))
        for collection in _FACT_COLLECTIONS
    ):
        raise ValueError("repair response contains duplicate candidate ids")
    new_facts = {
        candidate_id: row
        for candidate_id, row in response_facts.items()
        if candidate_id not in original_facts
    }
    replacement_by_original: dict[str, list[Mapping[str, Any]]] = {}
    for row in new_facts.values():
        repair_of = str(row.get("repair_of_candidate_id") or "")
        if not repair_of or repair_of not in packets:
            raise ValueError("repair response invented an unscoped new fact")
        replacement_by_original.setdefault(repair_of, []).append(row)

    register_by_candidate: dict[str, list[Mapping[str, Any]]] = {}
    for row in response_dossier.get("verification_repair_register") or ():
        candidate_id = str(row.get("candidate_id") or "")
        if candidate_id in packets:
            register_by_candidate.setdefault(candidate_id, []).append(row)
    original_lineage_ids = {
        str(row.get("source_lineage_id") or "")
        for row in original_dossier.get("source_lineages") or ()
    }
    response_lineages = {
        str(row.get("source_lineage_id") or ""): row
        for row in response_dossier.get("source_lineages") or ()
    }
    original_route_ids = {
        str(row.get("route_receipt_id") or "")
        for row in original_dossier.get("search_route_receipts") or ()
    }
    new_routes = tuple(
        row
        for row in response_dossier.get("search_route_receipts") or ()
        if str(row.get("route_receipt_id") or "") not in original_route_ids
    )
    if len({str(row.get("route_receipt_id") or "") for row in new_routes}) != len(
        new_routes
    ):
        raise ValueError("repair response contains duplicate new route receipts")
    actions: list[Mapping[str, Any]] = []
    for candidate_id, packet in packets.items():
        register_rows = register_by_candidate.get(candidate_id) or []
        if not register_rows:
            continue
        action_values = {str(row.get("status") or "") for row in register_rows}
        if len(action_values) != 1 or not action_values.issubset(REPAIR_ACTIONS):
            raise ValueError("repair register has conflicting or invalid actions")
        action = next(iter(action_values))
        pro_declared_question_ids = tuple(
            dict.fromkeys(
                str(row.get("question_family_id") or "") for row in register_rows
            )
        )
        packet_question_ids = tuple(packet.question_family_ids)
        if (
            not pro_declared_question_ids
            or not set(pro_declared_question_ids).issubset(packet_question_ids)
        ):
            raise ValueError("repair register escapes the rejection packet question scope")
        replacements = replacement_by_original.get(candidate_id) or []
        if action == "WITHDRAWN":
            if replacements:
                raise ValueError("WITHDRAWN repair response contains a replacement fact")
            corrected = None
        else:
            if len(replacements) != 1:
                raise ValueError("repair action requires exactly one scoped replacement")
            corrected = dict(replacements[0])
            replacement_question_ids = tuple(
                dict.fromkeys(
                    str(value)
                    for value in corrected.get("question_family_ids") or ()
                    if str(value)
                )
            )
            if (
                not replacement_question_ids
                or not set(replacement_question_ids).issubset(
                    packet_question_ids
                )
            ):
                raise ValueError(
                    "replacement fact escapes its declared packet question scope"
                )
            # A repair action targets one rejected candidate, while the schema
            # records one question per register row.  Pro may emit only a
            # representative in-packet question.  Restore the immutable
            # packet roster solely as the deterministic reverification scope;
            # this does not accept the fact or grant score/Stage authority.
            corrected["question_family_ids"] = list(packet_question_ids)
        action_row: dict[str, Any] = {
            "packet_id": packet.packet_id,
            "candidate_id": candidate_id,
            "question_family_ids": list(packet_question_ids),
            "pro_declared_question_family_ids": list(
                pro_declared_question_ids
            ),
            "pro_reported_replacement_question_family_ids": (
                list(replacement_question_ids) if corrected is not None else []
            ),
            "question_scope_binding": (
                "EXACT_PACKET_SCOPE"
                if set(pro_declared_question_ids) == set(packet_question_ids)
                and (
                    corrected is None
                    or set(replacement_question_ids) == set(packet_question_ids)
                )
                else "PACKET_SCOPE_RESTORED_FOR_DETERMINISTIC_REVERIFICATION"
            ),
            "action": action,
            "corrected_fact": corrected,
        }
        if corrected is not None:
            lineage_id = str(corrected.get("source_lineage_id") or "")
            if lineage_id not in original_lineage_ids:
                lineage = response_lineages.get(lineage_id)
                if lineage is None:
                    raise ValueError("replacement fact lacks a source lineage receipt")
                action_row["new_source_lineage"] = lineage
            replacement_id = str(corrected.get("dossier_fact_id") or "")
            scoped_routes = tuple(
                row
                for row in new_routes
                if row.get("pass_id") == pass_id
                and str(row.get("question_family_id") or "")
                in set(packet_question_ids)
                and replacement_id
                in {
                    str(value) for value in row.get("accepted_fact_ids") or ()
                }
            )
            if not scoped_routes:
                raise ValueError(
                    "replacement fact lacks a current-pass accepted route receipt"
                )
            action_row["new_route_receipts"] = list(scoped_routes)
        actions.append(action_row)
    return {
        "schema_version": "e2r_pro_verifier_repair_delta_v1",
        "job_id": original_dossier.get("job_id"),
        "conversation_id": original_dossier.get("conversation_id"),
        "research_pass_id": pass_id,
        "parent_pass_id": parent_pass_id,
        "response_hash": response_hash,
        "actions": actions,
        "score_authority": False,
        "stage_authority": False,
    }


__all__ = ["derive_repair_delta_from_dossier_response"]
