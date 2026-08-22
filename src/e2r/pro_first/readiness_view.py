"""Append-only readiness projection for legacy Pro-first results.

The V1 live canary proved browser transport and deterministic downstream
plumbing.  It did not prove contract-driven research saturation.  This module
keeps the immutable V1 receipt available for audit while preventing its
diagnostic score and Stage from being exposed as a full-thesis result.
"""

from __future__ import annotations

from typing import Any, Mapping

from .ids import canonical_hash


TRANSPORT_CANARY_PASS = "PRO_FIRST_END_TO_END_TRANSPORT_CANARY_PASS"
PARTIAL_DIAGNOSTIC = "FIRST_PASS_PARTIAL_CORPUS_DIAGNOSTIC_ONLY"
NOT_OPERATIONAL_SCORE = "NOT_A_FULL_THESIS_OPERATIONAL_SCORE"
WITHHELD = "WITHHELD_PENDING_RESEARCH_SATURATION"


def project_full_thesis_readiness(
    legacy_result: Mapping[str, Any],
    *,
    saturation_receipt: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Return a non-mutating V2 view over a V1 result or acceptance receipt.

    A V1 ``PUBLISHED`` marker is historical transport/downstream evidence only.
    Full-thesis fields remain null until an explicit V2 saturation receipt says
    that every mandatory question is terminal and all material pending rosters
    are empty.
    """

    original = dict(legacy_result)
    ready = _is_full_thesis_ready(saturation_receipt)
    diagnostic_score = original.get("score", original.get("full_score"))
    diagnostic_stage = original.get(
        "canonical_stage",
        original.get("stage"),
    )
    view: dict[str, Any] = {
        "schema_version": "e2r_pro_first_readiness_view_v2",
        "job_id": original.get("job_id"),
        "target_id": original.get("target_id", original.get("symbol")),
        "as_of_date": original.get("as_of_date"),
        "transport_canary_status": TRANSPORT_CANARY_PASS,
        "first_pass_status": PARTIAL_DIAGNOSTIC,
        "operational_score_status": NOT_OPERATIONAL_SCORE,
        "first_pass_diagnostic_score": diagnostic_score,
        "first_pass_diagnostic_stage": diagnostic_stage,
        "full_thesis_score": None,
        "full_thesis_stage": None,
        "full_thesis_score_valid": False,
        "research_status": "RESEARCH_INCOMPLETE",
        "publication_status": WITHHELD,
        "legacy_publication_status": original.get("publication_status"),
        "legacy_result_hash": canonical_hash(original),
        "legacy_result_preserved": True,
        "score_authority": "ResearchCalibratedComponentScorer",
        "stage_authority": "AtomicStageCourtV2",
        "pro_score_authority": False,
        "pro_stage_authority": False,
        "withhold_reasons": [
            "V2_RESEARCH_CONTRACT_CLOSURE_NOT_PROVEN",
            "PUBLIC_MATERIAL_GAP_CLOSURE_NOT_PROVEN",
            "VERIFIER_REPAIR_CLOSURE_NOT_PROVEN",
        ],
    }
    if ready:
        assert saturation_receipt is not None
        view.update(
            {
                "operational_score_status": "FULL_THESIS_OPERATIONAL_SCORE",
                "full_thesis_score": saturation_receipt.get("full_thesis_score"),
                "full_thesis_stage": saturation_receipt.get("full_thesis_stage"),
                "full_thesis_score_valid": True,
                "research_status": "FULL_THESIS_READY",
                "publication_status": saturation_receipt.get(
                    "publication_status",
                    "FULL_THESIS_PUBLISHED",
                ),
                "withhold_reasons": [],
            }
        )
    return view


def _is_full_thesis_ready(
    saturation_receipt: Mapping[str, Any] | None,
) -> bool:
    if not saturation_receipt:
        return False
    return bool(
        saturation_receipt.get("status") == "FULL_THESIS_READY"
        and saturation_receipt.get("full_thesis_score_valid") is True
        and int(saturation_receipt.get("mandatory_nonterminal_count") or 0) == 0
        and int(saturation_receipt.get("public_searchable_material_gap_count") or 0)
        == 0
        and int(saturation_receipt.get("verifier_repair_pending_count") or 0) == 0
        and int(saturation_receipt.get("core_provider_parser_pending_count") or 0)
        == 0
    )


__all__ = [
    "NOT_OPERATIONAL_SCORE",
    "PARTIAL_DIAGNOSTIC",
    "TRANSPORT_CANARY_PASS",
    "WITHHELD",
    "project_full_thesis_readiness",
]
