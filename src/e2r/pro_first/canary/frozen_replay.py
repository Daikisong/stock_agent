"""Hash-bound V2 replay of a legacy Pro V1 partial corpus.

The tracked fixture contains no article text, source quotes, or full report.  It
keeps only identity, hashes, counts, and the minimal structured unresolved-gap
semantics required to prove that the old one-pass report cannot enter
full-thesis scoring under V2.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from ..ids import canonical_hash
from ..readiness_view import project_full_thesis_readiness
from ..research_contracts import build_research_question_plan
from ..saturation import ResearchSaturationAdjudicator, compile_saturation_audit


FROZEN_PROJECTION_SCHEMA = "e2r_pro_first_v2_frozen_v1_projection_v1"
FROZEN_REPLAY_SCHEMA = "e2r_pro_first_v2_frozen_partial_replay_v1"

LIKELY_NONPUBLIC_CANDIDATE = "LIKELY_NONPUBLIC_CANDIDATE"
PUBLIC_SEARCHABLE_CANDIDATE = "PUBLIC_SEARCHABLE"
FUTURE_EVENT_ONLY_CANDIDATE = "FUTURE_EVENT_ONLY_CANDIDATE"

_FUTURE_SOURCE_TOKENS = (
    "_PROGRESS",
    "_COMPLETION",
    "_DECISION",
    "BOARD_APPROVAL",
)
_FUTURE_REASON_TOKENS = (
    "not yet",
    "no decision",
    "future",
    "미결정",
    "아직",
)
_EXPLICIT_UNAVAILABLE_TOKENS = (
    "not public",
    "not disclosed",
    "do not disclose",
    "remain unknown",
    "remains unknown",
    "unknown",
    " but not ",
    "비공개",
    "미공개",
)
_STRONG_PUBLIC_ROUTE_TOKENS = (
    "AUDITED_FINANCIAL",
    "AUDITED_CASH_FLOW",
    "CONSENSUS",
    "MARKET_DATA",
    "PEER_VALUATION",
    "INDUSTRY_BIT_SUPPLY",
    "REGULATORY_PROJECT_UPDATE",
)


def project_frozen_v1_dossier(
    dossier: Mapping[str, Any],
    *,
    source_report_sha256: str,
    source_report_byte_count: int,
    dossier_payload_hash: str | None = None,
    parser_operations: Sequence[str] = (),
    verified_fact_count: int,
    first_pass_diagnostic_score: float,
    first_pass_diagnostic_stage: str,
    legacy_publication_status: str,
) -> Mapping[str, Any]:
    """Create a copyright-safe replay projection from a parsed V1 dossier."""

    if dossier.get("schema_version") != "e2r_pro_research_dossier_v1":
        raise ValueError("frozen legacy replay requires ResearchDossierV1")
    if len(source_report_sha256) != 64 or source_report_byte_count <= 0:
        raise ValueError("frozen source report requires a SHA256 and byte count")
    target = dossier.get("target") or {}
    if not isinstance(target, Mapping):
        raise ValueError("legacy dossier target must be an object")
    primary_ids = tuple(
        str(row.get("archetype_id") or "")
        for row in dossier.get("candidate_archetypes") or ()
        if str(row.get("selection_status") or "").startswith("PRIMARY")
    )
    if not primary_ids:
        primary_ids = tuple(
            str(row.get("archetype_id") or "")
            for row in dossier.get("candidate_archetypes") or ()
            if row.get("archetype_id")
        )
    if not primary_ids:
        raise ValueError("legacy dossier has no selected primary archetype")
    source_rows = tuple(dossier.get("sources") or ())
    lineage_groups = {
        str(row.get("lineage_group_id") or "") for row in source_rows
        if row.get("lineage_group_id")
    }
    gap_rows = tuple(_redacted_gap(row) for row in dossier.get("unresolved_gaps") or ())
    payload: dict[str, Any] = {
        "schema_version": FROZEN_PROJECTION_SCHEMA,
        "source_report_sha256": source_report_sha256,
        "source_report_byte_count": int(source_report_byte_count),
        "dossier_payload_hash": dossier_payload_hash or canonical_hash(dossier),
        "parser_operations": list(parser_operations),
        "raw_report_tracked": False,
        "projection_contains_article_or_quote_text": False,
        "job_id": str(dossier.get("job_id") or ""),
        "run_id": str(dossier.get("run_id") or ""),
        "target": {
            "target_id": str(target.get("target_id") or target.get("symbol") or ""),
            "symbol": str(target.get("symbol") or target.get("target_id") or ""),
            "company_name": str(target.get("company_name") or ""),
        },
        "as_of_date": str(dossier.get("as_of_date") or ""),
        "primary_archetype_ids": list(dict.fromkeys(primary_ids)),
        "legacy_research_status": str(dossier.get("research_status") or ""),
        "material_fact_count": len(tuple(dossier.get("material_facts") or ())),
        "counterfact_count": len(tuple(dossier.get("counterfacts") or ())),
        "lineage_group_count": len(lineage_groups),
        "unresolved_gap_count": len(gap_rows),
        "verified_fact_count": int(verified_fact_count),
        "unresolved_gaps": list(gap_rows),
        "first_pass_diagnostic_score": float(first_pass_diagnostic_score),
        "first_pass_diagnostic_stage": str(first_pass_diagnostic_stage),
        "legacy_publication_status": str(legacy_publication_status),
        "score_authority": False,
        "stage_authority": False,
    }
    return {**payload, "projection_hash": canonical_hash(payload)}


def compile_frozen_partial_corpus_replay(
    projection: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Run the actual V2 saturation/readiness gates over a redacted V1 digest."""

    _validate_projection(projection)
    primary_ids = tuple(str(value) for value in projection["primary_archetype_ids"])
    question_plan = build_research_question_plan(primary_ids)
    results = [_open_question_result(row) for row in question_plan.mandatory_questions]
    v2_dossier = {
        "schema_version": "e2r_pro_research_dossier_v2",
        "job_id": projection["job_id"],
        "run_id": projection["run_id"],
        "conversation_id": "LEGACY_V1_NO_V2_CONVERSATION_SCOPE",
        "research_pass_id": "LEGACY_V1_ONE_PASS",
        "parent_pass_id": None,
        "target": projection["target"],
        "as_of_date": projection["as_of_date"],
        "candidate_archetypes": list(primary_ids),
        "selected_archetypes": list(primary_ids),
        "research_status": projection["legacy_research_status"],
        "material_facts": [],
        "counterfacts": [],
        "resolution_facts": [],
        "question_family_results": results,
        "source_lineages": [],
        "search_route_receipts": [],
        "verification_repair_register": [],
        "proposed_score_ranges": [],
        "score_authority": False,
        "stage_authority": False,
    }
    saturation = ResearchSaturationAdjudicator().adjudicate(
        dossier=v2_dossier,
        verified_fact_ids=(),
    )
    saturation_audit = compile_saturation_audit(saturation)
    gap_rows = [
        {
            "dossier_gap_id": str(row.get("dossier_gap_id") or ""),
            "availability_candidate": _classify_gap_candidate(row),
            "required_source_families": list(row.get("required_source_families") or ()),
            "proposed_missing_source_role": str(
                row.get("proposed_missing_source_role") or ""
            ),
        }
        for row in projection.get("unresolved_gaps") or ()
    ]
    class_counts = {
        label: sum(row["availability_candidate"] == label for row in gap_rows)
        for label in (
            LIKELY_NONPUBLIC_CANDIDATE,
            PUBLIC_SEARCHABLE_CANDIDATE,
            FUTURE_EVENT_ONLY_CANDIDATE,
        )
    }
    legacy_result = {
        "job_id": projection["job_id"],
        "target_id": (projection.get("target") or {}).get("target_id"),
        "as_of_date": projection["as_of_date"],
        "score": projection["first_pass_diagnostic_score"],
        "canonical_stage": projection["first_pass_diagnostic_stage"],
        "publication_status": projection["legacy_publication_status"],
    }
    readiness = project_full_thesis_readiness(
        legacy_result,
        saturation_receipt={
            "status": saturation.deterministic_research_status,
            "full_thesis_score_valid": False,
            "mandatory_nonterminal_count": len(
                saturation.nonterminal_mandatory_question_ids
            ),
            "public_searchable_material_gap_count": len(
                saturation.public_material_gap_question_ids
            ),
            "verifier_repair_pending_count": len(
                saturation.verifier_repair_pending_ids
            ),
            "core_provider_parser_pending_count": len(
                saturation.provider_parser_core_pending_question_ids
            ),
        },
    )
    critical_counts = {
        "legacy_count_contract_mismatch_count": int(
            (
                int(projection["material_fact_count"]),
                int(projection["counterfact_count"]),
                int(projection["lineage_group_count"]),
                int(projection["unresolved_gap_count"]),
            )
            != (20, 15, 15, 13)
        ),
        "gap_candidate_unclassified_count": sum(
            row["availability_candidate"]
            not in {
                LIKELY_NONPUBLIC_CANDIDATE,
                PUBLIC_SEARCHABLE_CANDIDATE,
                FUTURE_EVENT_ONLY_CANDIDATE,
            }
            for row in gap_rows
        ),
        "semantic_candidate_class_missing_count": sum(
            class_counts[value] == 0 for value in class_counts
        ),
        "v2_question_plan_count_mismatch_count": int(
            len(results) != len(question_plan.mandatory_question_ids)
        ),
        "public_material_gap_missing_count": int(
            not saturation.public_material_gap_question_ids
        ),
        "legacy_complete_not_diverged_count": int(not saturation.pro_status_diverged),
        "partial_corpus_marked_saturated_count": int(
            saturation.research_saturation_valid
        ),
        "component_entry_allowed_count": int(saturation.component_entry_allowed),
        "full_thesis_score_valid_count": int(
            readiness["full_thesis_score_valid"] is not False
        ),
        "stage_final_publication_count": int(
            readiness["full_thesis_stage"] is not None
            or readiness["publication_status"]
            != "WITHHELD_PENDING_RESEARCH_SATURATION"
        ),
        "question_fact_linkage_inferred_count": 0,
        "new_query_or_fetch_count": 0,
        "pro_score_stage_authority_count": int(
            projection.get("score_authority") is not False
        )
        + int(projection.get("stage_authority") is not False),
        "partial_saturation_audit_unexpectedly_clean_count": int(
            saturation_audit["critical_count_sum"] == 0
        ),
    }
    # A frozen partial corpus must make the normal full-thesis saturation audit
    # fail.  That failure is the replay's expected safety behavior, not a P9
    # acceptance failure.
    critical_sum = sum(critical_counts.values())
    payload: dict[str, Any] = {
        "schema_version": FROZEN_REPLAY_SCHEMA,
        "phase": "P9_FROZEN_MD_REPLAY",
        "status": (
            "PRO_FIRST_V2_PARTIAL_CORPUS_GUARD_PASS"
            if critical_sum == 0
            else "FAIL"
        ),
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "source_report_sha256": projection["source_report_sha256"],
        "source_report_byte_count": projection["source_report_byte_count"],
        "dossier_payload_hash": projection["dossier_payload_hash"],
        "projection_hash": projection["projection_hash"],
        "raw_report_tracked": False,
        "job_id": projection["job_id"],
        "run_id": projection["run_id"],
        "target_id": (projection.get("target") or {}).get("target_id"),
        "as_of_date": projection["as_of_date"],
        "primary_archetype_ids": list(primary_ids),
        "observed_first_pass": {
            "material_fact_count": projection["material_fact_count"],
            "counterfact_count": projection["counterfact_count"],
            "lineage_group_count": projection["lineage_group_count"],
            "unresolved_gap_count": projection["unresolved_gap_count"],
            "verified_fact_count": projection["verified_fact_count"],
            "legacy_research_status": projection["legacy_research_status"],
        },
        "gap_candidate_class_counts": class_counts,
        "gap_candidate_decisions": gap_rows,
        "expected_mandatory_question_count": len(question_plan.mandatory_question_ids),
        "nonterminal_mandatory_question_count": len(
            saturation.nonterminal_mandatory_question_ids
        ),
        "public_searchable_material_gap_count": len(
            saturation.public_material_gap_question_ids
        ),
        "v2_deterministic_research_status": saturation.deterministic_research_status,
        "legacy_complete_diverged": saturation.pro_status_diverged,
        "research_saturation_valid": saturation.research_saturation_valid,
        "component_entry_allowed": saturation.component_entry_allowed,
        "first_pass_diagnostic_score": readiness["first_pass_diagnostic_score"],
        "first_pass_diagnostic_stage": readiness["first_pass_diagnostic_stage"],
        "full_thesis_score": readiness["full_thesis_score"],
        "full_thesis_stage": readiness["full_thesis_stage"],
        "full_thesis_score_valid": readiness["full_thesis_score_valid"],
        "publication_status": readiness["publication_status"],
        "new_query_count": 0,
        "new_fetch_count": 0,
        "score_authority": "ResearchCalibratedComponentScorer",
        "stage_authority": "AtomicStageCourtV2",
        "pro_score_authority": False,
        "pro_stage_authority": False,
        "saturation_receipt_hash": saturation.receipt_hash,
        "production_runtime_ready": False,
        "fixture_only": True,
    }
    return {**payload, "replay_hash": canonical_hash(payload)}


def _redacted_gap(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "dossier_gap_id": str(row.get("dossier_gap_id") or ""),
        "economic_reason": str(row.get("economic_reason") or ""),
        "predicate_or_fact_need_id": str(row.get("predicate_or_fact_need_id") or ""),
        "proposed_missing_source_role": str(
            row.get("proposed_missing_source_role") or ""
        ),
        "required_source_families": [
            str(value) for value in row.get("required_source_families") or ()
        ],
        "affected_component_ids": [
            str(value) for value in row.get("affected_component_ids") or ()
        ],
        "proposed_could_change_score": row.get("proposed_could_change_score") is True,
        "proposed_could_change_stage": row.get("proposed_could_change_stage") is True,
        "proposed_could_change_hard_break": row.get(
            "proposed_could_change_hard_break"
        )
        is True,
    }


def _classify_gap_candidate(row: Mapping[str, Any]) -> str:
    families = tuple(
        str(value).strip().upper()
        for value in row.get("required_source_families") or ()
    )
    reason = f" {str(row.get('economic_reason') or '').casefold()} "
    monitoring_only = (
        str(row.get("proposed_missing_source_role") or "").upper()
        == "MONITORING_ONLY"
    )
    future_route = any(
        token in family for family in families for token in _FUTURE_SOURCE_TOKENS
    )
    future_reason = any(token in reason for token in _FUTURE_REASON_TOKENS)
    if monitoring_only or (future_route and future_reason):
        return FUTURE_EVENT_ONLY_CANDIDATE
    explicitly_unavailable = any(
        token in reason for token in _EXPLICIT_UNAVAILABLE_TOKENS
    )
    strong_public_route = any(
        token in family for family in families for token in _STRONG_PUBLIC_ROUTE_TOKENS
    )
    if explicitly_unavailable and not strong_public_route:
        return LIKELY_NONPUBLIC_CANDIDATE
    return PUBLIC_SEARCHABLE_CANDIDATE


def _open_question_result(planned: Any) -> Mapping[str, Any]:
    question = planned.question
    return {
        "archetype_id": planned.archetype_id,
        "question_family_id": planned.question_family_id,
        "status": "UNKNOWN_ROUTE_NOT_YET_TESTED",
        "support_fact_ids": [],
        "counter_fact_ids": [],
        "resolution_fact_ids": [],
        "attempted_source_role_ids": [],
        "search_route_receipt_ids": [],
        "required_source_roles_satisfied": [],
        "required_source_roles_missing": list(question["required_source_roles"]),
        "availability_class": "UNKNOWN_ROUTE_NOT_YET_TESTED",
        "affected_component_ids": list(question["affected_component_ids"]),
        "could_change_score": question.get("could_change_score") is True,
        "could_change_stage": question.get("could_change_stage") is True,
        "could_change_hard_break": question.get("could_change_hard_break") is True,
        "closure_reason": (
            "legacy V1에는 exact question/fact/route lineage가 없으므로 V2 closure를 "
            "추론하지 않는다."
        ),
        "adequate_search_proven": False,
    }


def _validate_projection(projection: Mapping[str, Any]) -> None:
    if projection.get("schema_version") != FROZEN_PROJECTION_SCHEMA:
        raise ValueError("unknown frozen V1 projection schema")
    expected = str(projection.get("projection_hash") or "")
    actual = canonical_hash(
        {key: value for key, value in projection.items() if key != "projection_hash"}
    )
    if not expected or expected != actual:
        raise ValueError("frozen V1 projection hash mismatch")
    if projection.get("raw_report_tracked") is not False:
        raise ValueError("raw Pro report must not be tracked in the clean-clone fixture")
    if projection.get("projection_contains_article_or_quote_text") is not False:
        raise ValueError("frozen projection must not contain article or quote text")
    if len(tuple(projection.get("unresolved_gaps") or ())) != int(
        projection.get("unresolved_gap_count") or 0
    ):
        raise ValueError("frozen unresolved-gap roster count mismatch")


__all__ = [
    "FROZEN_PROJECTION_SCHEMA",
    "FROZEN_REPLAY_SCHEMA",
    "FUTURE_EVENT_ONLY_CANDIDATE",
    "LIKELY_NONPUBLIC_CANDIDATE",
    "PUBLIC_SEARCHABLE_CANDIDATE",
    "compile_frozen_partial_corpus_replay",
    "project_frozen_v1_dossier",
]
