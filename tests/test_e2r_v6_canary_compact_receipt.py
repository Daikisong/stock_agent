from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_compact_receipt import (
    COMPACT_RECEIPT_PASS,
    COMPACT_REVIEW_PASS,
    COMPACT_REVIEW_SCHEMA,
    REQUIRED_ARTIFACT_NAMES,
    build_selection_bound_canary_artifacts_from_output,
    _production_provider_accounting,
    build_selection_bound_canary_manifest,
    export_selection_bound_canary_bundle,
    validate_selection_bound_canary_artifacts,
    validate_selection_bound_canary_bundle,
    verify_selection_bound_canary_directory,
)
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    canary_output_tree_hash,
)
from e2r.production.v6_canary_selection import (
    NATURAL_SELECTION,
    REQUIRED_ARCHETYPES,
    SELECTION_PASS,
    SELECTION_RECEIPT_SCHEMA,
    SELECTION_SCHEMA,
)
from e2r.production.v6_canary_results import (
    CANARY_RESULT_PASS,
    CANARY_RESULT_SCHEMA,
    build_full_researcher_mode_canary_receipt,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER
from e2r.research_brain.researcher_mode.tracked_receipts import (
    _recompute_stage,
    _tracked_component_maxima,
    _tracked_historical_anchors,
)


AS_OF_DATE = "2026-07-12"
REPO_ROOT = Path(__file__).resolve().parents[1]


def _selection() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for index, archetype_id in enumerate(REQUIRED_ARCHETYPES, start=1):
        target_id = f"{index:06d}"
        pre_deep = hashlib.sha256(f"{archetype_id}:{target_id}".encode()).hexdigest()
        rows.append(
            {
                "schema_version": SELECTION_RECEIPT_SCHEMA,
                "selection_id": "SELREC-" + pre_deep[:24],
                "archetype_id": archetype_id,
                "target_id": target_id,
                "company_name": f"회사{index}",
                "selection_mode": NATURAL_SELECTION,
                "selection_as_of_date": AS_OF_DATE,
                "pre_deep_input_hash": pre_deep,
                "krx_effective_date": AS_OF_DATE,
                "krx_source_url": "https://data-dbg.krx.co.kr/svc/apis/sto/stk_isu_base_info",
                "krx_source_hash": hashlib.sha256(f"krx:{index}".encode()).hexdigest(),
                "krx_request_id": f"KRXREQ-{index:024x}",
                "candidate_event_hash": hashlib.sha256(f"event:{index}".encode()).hexdigest(),
                "depth_decision_hash": hashlib.sha256(f"depth:{index}".encode()).hexdigest(),
                "planner_run_id": f"LIVEPLAN-{index:024x}",
                "blind_input_id": f"BLIND-{index:024x}",
                "plan_hash": hashlib.sha256(f"plan:{index}".encode()).hexdigest(),
                "issuer_profile_hash": hashlib.sha256(f"issuer:{index}".encode()).hexdigest(),
                "business_profile_hash": hashlib.sha256(f"business:{index}".encode()).hexdigest(),
                "direct_current_supporting_fact_ids": [f"FACT-{index}"],
                "recipe_ids": [f"RECIPE-{index}"],
                "trigger_event_ids": [f"TRIGGER-{index}"],
                "available_source_families": ["OPENDART"],
                "selection_rationale": "current trigger fixture",
                "final_score_visible_at_selection": False,
                "final_stage_visible_at_selection": False,
                "production_daily_candidate": True,
                "score_or_stage_authority": False,
            }
        )
    payload: dict[str, object] = {
        "schema_version": SELECTION_SCHEMA,
        "status": SELECTION_PASS,
        "selection_as_of_date": AS_OF_DATE,
        "required_archetypes": list(REQUIRED_ARCHETYPES),
        "selections": rows,
        "selection_count": len(rows),
        "critical_counts": {
            "required_archetype_missing_count": 0,
            "invalid_candidate_lineage_count": 0,
            "post_score_target_selection_count": 0,
            "target_specific_code_branch_count": 0,
            "forced_canary_mislabeled_natural_count": 0,
            "duplicate_target_count": 0,
        },
        "critical_count_sum": 0,
        "failures": [],
        "score_or_stage_authority": False,
        # The current Phase-105 manifest carries this authority hash.  The
        # synthetic receipt has no forced-profile material, so its exact
        # fixture value is null; selection validation still requires the key.
        "issuer_business_profile_manifest_hash": None,
    }
    payload["selection_roster_hash"] = stable_hash(rows)
    return payload


def _classification_input() -> dict[str, object]:
    return {
        "diagnostic_scores": {},
        "red_team": {
            "soft_4b_score": 0.0,
            "soft_4b_status": "none",
            "thesis_break_score": 0.0,
            "risk_level": "low",
            "has_hard_break": False,
        },
        "previous_stage": None,
        "theme_regime_score": 0.0,
        "company_event_score": 0.0,
        "high_quality_company_event": False,
        "thesis_ongoing": True,
        "archive_requested": False,
        "coverage_impossible": False,
    }


def _artifacts(
    selection: dict[str, object], selection_index: int = 0
) -> dict[str, object]:
    selected = selection["selections"][selection_index]
    assert isinstance(selected, dict)
    target_id = str(selected["target_id"])
    archetype_id = str(selected["archetype_id"])
    selection_id = str(selected["selection_id"])
    maxima = dict(_tracked_component_maxima(repo_root=REPO_ROOT, archetype_id=archetype_id))
    vector = {component_id: round(float(maxima[component_id]) / 2.0, 6) for component_id in CANONICAL_COMPONENT_ORDER}
    tracked_anchors = _tracked_historical_anchors(repo_root=REPO_ROOT, archetype_id=archetype_id)
    anchor_for_component = {}
    for anchor in tracked_anchors:
        component_id = str(anchor["component_id"])
        if component_id not in anchor_for_component and float(anchor["max_points"]) == float(maxima[component_id]):
            anchor_for_component[component_id] = anchor
    assert set(anchor_for_component) == set(CANONICAL_COMPONENT_ORDER)

    components = []
    facts = []
    judges = []
    sources = []
    anchors = []
    provider_calls = []
    for component_index, component_id in enumerate(CANONICAL_COMPONENT_ORDER):
        fact_id = f"EFACT-{component_index:064x}"
        source_id = f"SGDOC-{component_index:064x}"
        quote = f"{component_id} current source-backed mechanism fact"
        quote_hash = hashlib.sha256(quote.encode()).hexdigest()
        document_hash = hashlib.sha256(f"document:{component_id}".encode()).hexdigest()
        fact_call_id = f"COLLABFACT-{component_index:02d}"
        fact_prompt_hash = hashlib.sha256(f"fact-prompt:{fact_id}".encode()).hexdigest()
        fact_response_hash = hashlib.sha256(f"fact-response:{fact_id}".encode()).hexdigest()
        fact = {
            "schema_version": "e2r_v6_canary_compact_fact_v1",
            "fact_id": fact_id,
            "target_id": target_id,
            "as_of_date": AS_OF_DATE,
            "component_ids": [component_id],
            "fact_roles": ["SUPPORT"],
            "subject_id": target_id,
            "business_segment": "TEST",
            "product_family": component_id,
            "economic_mechanism": component_id,
            "source_document_id": source_id,
            "document_content_hash": document_hash,
            "exact_quote": quote,
            "exact_quote_hash": quote_hash,
            "published_at": "2026-07-10",
            "available_at": "2026-07-10",
            "current_score_eligible": True,
            "extraction_provider_name": "COLLABORATION_CODEX",
            "provider_call_id": fact_call_id,
            "provider_prompt_hash": fact_prompt_hash,
            "provider_response_hash": fact_response_hash,
            "accepted_fact_record_hash": "",
        }
        fact["accepted_fact_record_hash"] = stable_hash(
            {key: value for key, value in fact.items() if key != "accepted_fact_record_hash"}
        )
        facts.append(fact)
        provider_calls.append(
            {
                "schema_version": "e2r_v6_canary_compact_provider_call_v1",
                "provider_call_id": fact_call_id,
                "provider_name": "COLLABORATION_CODEX",
                "call_scope": "FACT_EXTRACTION",
                "status": "COMPLETED",
                "prompt_hash": fact_prompt_hash,
                "response_hash": fact_response_hash,
                "judge_decision_ids": [],
                "fact_ids": [fact_id],
                "score_or_stage_authority": False,
            }
        )
        source = {
            "schema_version": "e2r_v6_canary_compact_source_v1",
            "source_document_id": source_id,
            "target_id": target_id,
            "as_of_date": AS_OF_DATE,
            "source_url": f"https://example.invalid/{source_id}",
            "source_title": f"source {component_id}",
            "source_publisher": "example.invalid",
            "source_tier": "TIER1",
            "source_family": "OPENDART",
            "published_at": "2026-07-10",
            "available_at": "2026-07-10",
            "document_content_hash": document_hash,
            "fact_ids": [fact_id],
            "fact_exact_quote_hashes": {fact_id: quote_hash},
            "accepted_source_record_hash": "",
        }
        source["accepted_source_record_hash"] = stable_hash(
            {key: value for key, value in source.items() if key != "accepted_source_record_hash"}
        )
        sources.append(source)
        tracked_anchor = anchor_for_component[component_id]
        anchor_id = str(tracked_anchor["anchor_id"])
        anchors.append(
            {
                "schema_version": "e2r_v6_canary_compact_anchor_v1",
                "anchor_id": anchor_id,
                "component_id": component_id,
                "archetype_id": archetype_id,
                "max_points": maxima[component_id],
                "normalized_anchor_payload": tracked_anchor,
                "anchor_payload_hash": stable_hash(tracked_anchor),
            }
        )
        judge_ids = []
        for role_index, role in enumerate(("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE")):
            judge_id = f"JUDGE-{component_index:02d}-{role_index}"
            call_id = f"COLLABCALL-{component_index:02d}-{role_index}"
            prompt_hash = hashlib.sha256(f"prompt:{judge_id}".encode()).hexdigest()
            response_hash = hashlib.sha256(f"response:{judge_id}".encode()).hexdigest()
            judge_ids.append(judge_id)
            judges.append(
                {
                    "schema_version": "e2r_v6_canary_compact_judge_v1",
                    "judge_decision_id": judge_id,
                    "component_id": component_id,
                    "role": role,
                    "proposed_points": vector[component_id],
                    "allowed_range": [0.0, maxima[component_id]],
                    "support_fact_ids": [fact_id],
                    "counter_fact_ids": [],
                    "anchor_ids": [anchor_id],
                    "provider_call_id": call_id,
                    "prompt_hash": prompt_hash,
                    "response_hash": response_hash,
                    "score_or_stage_authority": False,
                }
            )
            provider_calls.append(
                {
                    "schema_version": "e2r_v6_canary_compact_provider_call_v1",
                    "provider_call_id": call_id,
                    "provider_name": "COLLABORATION_CODEX",
                    "call_scope": "COMPONENT_JUDGE",
                    "status": "COMPLETED",
                    "prompt_hash": prompt_hash,
                    "response_hash": response_hash,
                    "judge_decision_ids": [judge_id],
                    "fact_ids": [],
                    "score_or_stage_authority": False,
                }
            )
        components.append(
            {
                "schema_version": "e2r_v6_canary_compact_component_v1",
                "component_id": component_id,
                "max_points": maxima[component_id],
                "support_points": vector[component_id],
                "counter_effect": 0.0,
                "final_points": vector[component_id],
                "confidence": 1.0,
                "proposal_median": vector[component_id],
                "consensus_band": [0.0, maxima[component_id]],
                "judge_proposals": {
                    "ANALYST": vector[component_id],
                    "SKEPTIC": vector[component_id],
                    "CALIBRATION_JUDGE": vector[component_id],
                },
                "aggregation_method": "MEDIAN_WITH_ALLOWED_RANGE_INTERSECTION",
                "aggregator_config_hash": hashlib.sha256(b"aggregator-config").hexdigest(),
                "support_fact_ids": [fact_id],
                "counter_fact_ids": [],
                "resolution_fact_ids": [],
                "anchor_ids": [anchor_id],
                "judge_decision_ids": judge_ids,
            }
        )

    total = round(sum(vector.values()), 6)
    source_by_id = {str(row["source_document_id"]): row for row in sources}
    blind_review_inventory = [
        {
            "fact_id": fact["fact_id"],
            "target_id": fact["target_id"],
            "as_of_date": fact["as_of_date"],
            "subject_id": fact["subject_id"],
            "business_segment": fact["business_segment"],
            "product_family": fact["product_family"],
            "economic_mechanism": fact["economic_mechanism"],
            "fact_roles": fact["fact_roles"],
            "source_document_id": fact["source_document_id"],
            "source_family": source_by_id[str(fact["source_document_id"])]["source_family"],
            "source_tier": source_by_id[str(fact["source_document_id"])]["source_tier"],
            "published_at": fact["published_at"],
            "available_at": fact["available_at"],
            "exact_quote_hash": fact["exact_quote_hash"],
            "current_score_eligible": fact["current_score_eligible"],
        }
        for fact in facts
    ]
    score = {
        "schema_version": "e2r_v6_canary_compact_score_v1",
        "target_id": target_id,
        "as_of_date": AS_OF_DATE,
        "selection_id": selection_id,
        "selection_roster_hash": selection["selection_roster_hash"],
        "score_valid": True,
        "research_complete": True,
        "component_score_vector": vector,
        "component_max_vector": maxima,
        "total_score": total,
        "canonical_stage": "0",
        "canary_result": {},
        "production_receipt": {},
        "blind_review_inventory": blind_review_inventory,
        "score_or_stage_authority": False,
    }
    stage = {
        "schema_version": "e2r_v6_canary_compact_stagecourt_v1",
        "target_id": target_id,
        "as_of_date": AS_OF_DATE,
        "score_receipt_hash": "",
        "component_score_vector_hash": stable_hash(vector),
        "total_score": total,
        "canonical_stage": "0",
        "decision_status": "FINAL",
        "score_valid": True,
        "stage_final": True,
        "classification_input": _classification_input(),
        "decision_trace_hash": "",
        "score_or_stage_authority": False,
    }
    stage_value = _recompute_stage(score, stage)
    score["canonical_stage"] = stage_value
    stage["canonical_stage"] = stage_value
    result_body = {
        "schema_version": CANARY_RESULT_SCHEMA,
        "status": CANARY_RESULT_PASS,
        "run_id": "RESEARCHRUN-" + target_id,
        "selection_id": selection_id,
        "selection_roster_hash": selection["selection_roster_hash"],
        "archetype_id": archetype_id,
        "target_id": target_id,
        "as_of_date": AS_OF_DATE,
        "production_research_status": "COMPLETE",
        "fact_extraction_status": "COMPLETE",
        "structured_materialization_status": "COMPLETE",
        "business_model_status": "COMPLETE",
        "component_research_status": "COMPLETE",
        "judge_status": "COMPLETE",
        "red_team_status": "COMPLETE",
        "synthesis_status": "COMPLETE",
        "supervisor_status": "COMPLETE",
        "semantic_saturation_status": "COMPLETE",
        "score_status": "COMPLETE",
        "stagecourt_status": "FINAL",
        "full_researcher_mode_complete": True,
        "component_score_vector": vector,
        "total_score": total,
        "canonical_stage": stage_value,
        "score_valid": True,
        "stage_final": True,
        "component_count": 7,
        "judge_decision_count": 21,
        "query_count": 1,
        "document_count": 7,
        "fact_count": 7,
        "counterfact_count": 1,
        "material_gap_count": 0,
        "source_count": 7,
        "output_tree_hash": hashlib.sha256(f"output:{target_id}".encode()).hexdigest(),
        "provider_call_counts": {"COLLABORATION_CODEX": 28},
        "provider_error_count": 0,
        "unauthorized_provider_call_count": 0,
        "local_provider_call_count": 0,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }
    canary_result = {
        **result_body,
        "result_id": "CANARYRUN-" + stable_hash(result_body)[:24],
    }
    production_receipt = build_full_researcher_mode_canary_receipt(
        canary_result,
        selection=selection,
        selection_row=selected,
    )
    score["canary_result"] = canary_result
    score["production_receipt"] = production_receipt
    stage["score_receipt_hash"] = stable_hash(score)
    stage["decision_trace_hash"] = stable_hash(
        {
            "score_receipt_hash": stage["score_receipt_hash"],
            "component_score_vector_hash": stage["component_score_vector_hash"],
            "total_score": stage["total_score"],
            "classification_input": stage["classification_input"],
            "canonical_stage": stage["canonical_stage"],
        }
    )
    return {
        "score_receipt.json": score,
        "component_decisions.jsonl": components,
        "scoring_facts.jsonl": facts,
        "judge_decisions.jsonl": judges,
        "source_manifest.jsonl": sources,
        "anchor_manifest.jsonl": anchors,
        "provider_calls.jsonl": provider_calls,
        "stagecourt_receipt.json": stage,
    }


def _reviews(manifest: dict[str, object], artifacts: dict[str, object]) -> list[dict[str, object]]:
    score = artifacts["score_receipt.json"]
    assert isinstance(score, dict)
    result = []
    for suffix in ("a", "b"):
        reviewer_id = f"/root/independent_{suffix}"
        call_id = f"COLLAB-REVIEW-{manifest['target_id']}-{suffix}"
        receipt_scope = str(manifest["receipt_payload_hash"])
        prompt_hash = hashlib.sha256(
            f"review-prompt:{suffix}:{receipt_scope}".encode()
        ).hexdigest()
        response_hash = hashlib.sha256(
            f"review-response:{suffix}:{receipt_scope}".encode()
        ).hexdigest()
        identity = {
            "reviewer_id": reviewer_id,
            "provider_call_id": call_id,
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
            "receipt_payload_hash": manifest["receipt_payload_hash"],
        }
        result.append(
            {
                "schema_version": COMPACT_REVIEW_SCHEMA,
                "status": COMPACT_REVIEW_PASS,
                "review_id": "CANREVIEW-" + stable_hash(identity)[:24],
                "reviewer_id": reviewer_id,
                "provider_name": "COLLABORATION_CODEX",
                "provider_call_id": call_id,
                "prompt_hash": prompt_hash,
                "response_hash": response_hash,
                "selection_id": manifest["selection_id"],
                "selection_roster_hash": manifest["selection_roster_hash"],
                "receipt_id": manifest["receipt_id"],
                "receipt_payload_hash": manifest["receipt_payload_hash"],
                "target_id": manifest["target_id"],
                "archetype_id": manifest["archetype_id"],
                "as_of_date": manifest["as_of_date"],
                "recomputed_component_score_vector": score["component_score_vector"],
                "recomputed_total_score": score["total_score"],
                "recomputed_canonical_stage": score["canonical_stage"],
                "all_eight_artifacts_verified": True,
                "full_score_lineage_verified": True,
                "independent_review": True,
                "review_complete": True,
                "critical_findings": [],
                "critical_count_sum": 0,
                "material_fact_omission_count": 0,
                "counterfact_omission_count": 0,
                "subject_or_segment_mismatch_count": 0,
                "currentness_failure_count": 0,
                "source_quality_failure_count": 0,
                "component_calibration_failure_count": 0,
                "historical_anchor_analogy_failure_count": 0,
                "score_or_stage_authority": False,
            }
        )
    return result


def _bundle() -> tuple[dict[str, object], dict[str, object], dict[str, object], list[dict[str, object]]]:
    selection = _selection()
    artifacts = _artifacts(selection)
    row = selection["selections"][0]
    assert isinstance(row, dict)
    manifest = dict(
        build_selection_bound_canary_manifest(
            selection=selection,
            selection_id=str(row["selection_id"]),
            artifacts=artifacts,
            repo_root=REPO_ROOT,
        )
    )
    return selection, artifacts, manifest, _reviews(manifest, artifacts)


def _write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def _write_terminal_output(root: Path, selection: dict[str, object]) -> Path:
    selected = selection["selections"][0]
    assert isinstance(selected, dict)
    target = root / str(selected["target_id"])
    target.mkdir()
    normalized = _artifacts(selection)
    components = normalized["component_decisions.jsonl"]
    judges = normalized["judge_decisions.jsonl"]
    facts = normalized["scoring_facts.jsonl"]
    sources = normalized["source_manifest.jsonl"]
    score = normalized["score_receipt.json"]
    assert all(isinstance(rows, list) for rows in (components, judges, facts, sources))
    assert isinstance(score, dict)

    raw_decisions = []
    raw_memos = []
    for component in components:
        component_id = str(component["component_id"])
        component_judges = [row for row in judges if row["component_id"] == component_id]
        raw_decisions.append(
            {
                "decision": {
                    "component_id": component_id,
                    "max_points": component["max_points"],
                    "support_points": component["support_points"],
                    "counter_effect": component["counter_effect"],
                    "final_points": component["final_points"],
                    "fact_ids": component["support_fact_ids"],
                    "counter_fact_ids": component["counter_fact_ids"],
                    "anchor_ids": component["anchor_ids"],
                    "judge_ids": component["judge_decision_ids"],
                    "confidence": component["confidence"],
                    "proposal_median": component["proposal_median"],
                    "consensus_band": component["consensus_band"],
                    "judge_proposals": component["judge_proposals"],
                    "prompt_hashes": [row["prompt_hash"] for row in component_judges],
                    "response_hashes": [row["response_hash"] for row in component_judges],
                    "judge_call_ids": [row["provider_call_id"] for row in component_judges],
                    "config_hash": component["aggregator_config_hash"],
                }
            }
        )
        raw_memos.append(
            {
                "component_id": component_id,
                "resolution_fact_ids": component["resolution_fact_ids"],
                "why_not_higher": "bounded by current evidence",
                "why_not_lower": "supported by accepted facts",
            }
        )
    _write_jsonl(target / "final_component_decisions.jsonl", raw_decisions)
    _write_jsonl(target / "component_research_memos.jsonl", raw_memos)
    _write_jsonl(
        target / "component_judge_decisions.jsonl",
        [
            {
                "judge_id": row["judge_decision_id"],
                "component_id": row["component_id"],
                "role": row["role"],
                "proposed_points": row["proposed_points"],
                "allowed_range": row["allowed_range"],
                "support_fact_ids": row["support_fact_ids"],
                "counter_fact_ids": row["counter_fact_ids"],
                "nearest_anchor_ids": row["anchor_ids"],
                "why_not_lower": "source-backed support",
                "why_not_higher": "bounded uncertainty",
                "prompt_hash": row["prompt_hash"],
                "response_hash": row["response_hash"],
                "judge_call_id": row["provider_call_id"],
                "provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
            }
            for row in judges
        ],
    )

    raw_facts = []
    claims = []
    documents = []
    source_by_id = {str(row["source_document_id"]): row for row in sources}
    for fact in facts:
        fact_id = str(fact["fact_id"])
        source_id = str(fact["source_document_id"])
        component_id = str(fact["component_ids"][0])
        claim_id = "RFC-" + hashlib.sha256(f"claim:{fact_id}".encode()).hexdigest()
        raw_facts.append(
            {
                "fact_id": fact_id,
                "claim_ids": [claim_id],
                "subject": str(selected["target_id"]),
                "business_segment": "TEST",
                "product_family": component_id,
                "economic_mechanism": component_id,
                "predicate": "CURRENT_MECHANISM",
                "direction": "POSITIVE",
                "value": "current",
                "unit": "NONE",
                "period": "2026",
                "current_lifecycle": "CURRENT",
                "source_independence_group": source_id,
            }
        )
        source = source_by_id[source_id]
        claims.append(
            {
                "claim_id": claim_id,
                "document_id": source_id,
                "canonical_url": source["source_url"],
                "exact_quote": fact["exact_quote"],
                "target_id": selected["target_id"],
                "allowed_component_ids": [component_id],
                "subject_id": selected["target_id"],
                "question_family_id": "CURRENT_MECHANISM",
                "predicate_family": "CURRENT_MECHANISM",
                "normalized_object": "current",
                "period": "2026",
                "mechanism_scope_id": component_id,
                "scope_business_segment": "TEST",
                "scope_product_family": component_id,
                "scope_technology_family": "TEST",
                "scope_transaction_type": "GENERIC_INFORMATION",
                "scope_economic_mechanism": "INFORMATION_ONLY",
                "scope_confidence": 1.0,
                "source_tier": "TIER1",
                "source_family": source["source_family"],
                "published_at": source["published_at"],
                "available_at": source["available_at"],
                "provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
                "provider_prompt_hash": hashlib.sha256(f"fact-prompt:{fact_id}".encode()).hexdigest(),
                "provider_response_hash": hashlib.sha256(f"fact-response:{fact_id}".encode()).hexdigest(),
                "source_independence_group": source_id,
            }
        )
        documents.append(
            {
                "document_id": source_id,
                "canonical_url": source["source_url"],
                "title": source["source_title"],
                "source_family": source["source_family"],
                "published_at": source["published_at"],
                "available_at": source["available_at"],
                "full_source_content_hash": source["document_content_hash"],
            }
        )
    context_fact_id = "EFACT-CONTEXT-ONLY"
    context_claim_id = "RFC-" + hashlib.sha256(b"context-only-claim").hexdigest()
    context_document_id = "SGDOC-CONTEXT-ONLY"
    context_quote = "Current counter context that is not selected for direct scoring"
    context_document_hash = hashlib.sha256(b"context-only-document").hexdigest()
    claims.append(
        {
            "claim_id": context_claim_id,
            "document_id": context_document_id,
            "canonical_url": "https://example.invalid/context-only",
            "exact_quote": context_quote,
            "target_id": selected["target_id"],
            "allowed_component_ids": list(CANONICAL_COMPONENT_ORDER),
            "subject_id": selected["target_id"],
            "question_family_id": "COUNTER_CONTEXT",
            "predicate_family": "COUNTER_CONTEXT",
            "normalized_object": "counter",
            "period": "2026",
            "mechanism_scope_id": "COUNTER_CONTEXT",
            "scope_business_segment": "TEST",
            "scope_product_family": "TEST",
            "scope_technology_family": "TEST",
            "scope_transaction_type": "GENERIC_INFORMATION",
            "scope_economic_mechanism": "INFORMATION_ONLY",
            "scope_confidence": 1.0,
            "source_tier": "TIER1",
            "source_family": "OPENDART",
            "published_at": "2026-07-10",
            "available_at": "2026-07-10",
            "provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
            "provider_prompt_hash": hashlib.sha256(b"context-prompt").hexdigest(),
            "provider_response_hash": hashlib.sha256(b"context-response").hexdigest(),
        }
    )
    documents.append(
        {
            "document_id": context_document_id,
            "canonical_url": "https://example.invalid/context-only",
            "title": "counter context source",
            "source_family": "OPENDART",
            "published_at": "2026-07-10",
            "available_at": "2026-07-10",
            "full_source_content_hash": context_document_hash,
        }
    )
    _write_jsonl(target / "evidence_facts.jsonl", raw_facts)
    _write_jsonl(
        target / "counterfacts.jsonl",
        [
            {
                "fact_id": context_fact_id,
                "claim_ids": [context_claim_id],
                "subject": selected["target_id"],
                "business_segment": "TEST",
                "product_family": "TEST",
                "economic_mechanism": "COUNTER_CONTEXT",
                "predicate": "COUNTER_CONTEXT",
                "direction": "NEGATIVE",
                "value": "counter",
                "unit": "NONE",
                "period": "2026",
                "current_lifecycle": "CURRENT",
            }
        ],
    )
    _write_jsonl(target / "material_fact_claims.jsonl", claims)
    _write_jsonl(target / "documents.jsonl", documents)
    _write_jsonl(target / "query_ledger.jsonl", [{"query_id": "QUERY-1"}])
    _write_json(
        target / "score_vector.json",
        {
            "target_id": selected["target_id"],
            "as_of_date": AS_OF_DATE,
            "status": "COMPLETE",
            "score_valid": True,
            "component_score_vector": score["component_score_vector"],
            "total_points": score["total_score"],
        },
    )
    _write_json(
        target / "atomic_stage_decision.json",
        {
            "target_id": selected["target_id"],
            "as_of_date": AS_OF_DATE,
            "archetype_id": selected["archetype_id"],
            "status": "FINAL",
            "score_valid": True,
            "canonical_stage": score["canonical_stage"],
        },
    )
    _write_json(
        target / "semantic_saturation_certificate.json",
        {"status": "CERTIFIED", "semantic_saturation_certified": True},
    )
    _write_json(
        target / "fact_extraction_audit.json",
        {"status": "FACT_EXTRACTION_AUDIT_PASS", "critical_count_sum": 0},
    )
    _write_json(
        target / "current_structured_materialization.json",
        {
            "status": "COMPLETE",
            "target_id": selected["target_id"],
            "as_of_date": AS_OF_DATE,
        },
    )
    _write_json(
        target / "business_model_memo.json",
        {
            "research_complete": True,
            "target_id": selected["target_id"],
            "as_of_date": AS_OF_DATE,
        },
    )
    _write_json(target / "red_team_research.json", {"status": "COMPLETE"})
    _write_json(
        target / "research_supervisor_review.json",
        {
            "status": "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
            "structured_data_complete": True,
        },
    )
    _write_json(
        target / "research_provider_response_cache_audit.json",
        {
            "status": "COLLABORATION_PROVIDER_JOURNAL_ACTIVE",
            "provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
            "logical_call_count": 21,
            "successful_call_count": 21,
            "provider_error_count": 0,
            "provider_output_rejected_count": 0,
            "prompt_transport_rejected_count": 0,
            "collaboration_journal": {
                "status": "COLLABORATION_JOURNAL_ACTIVE",
                "request_count": 21,
                "validated_request_count": 21,
                "invalid_request_count": 0,
                "response_file_count": 21,
                "validated_response_count": 21,
                "invalid_response_count": 0,
                "orphan_response_count": 0,
                "pending_response_count": 0,
                "quarantined_response_count": 0,
            },
        },
    )
    _write_json(
        target / "stagecourt_trace.json",
        {
            "decision": {
                "canonical_stage": score["canonical_stage"],
                "status": "FINAL",
                "score_valid": True,
                "event_overlay": {},
                "hard_break_claim_ids": [],
                "current_guard_primitives": [],
            },
            "audit": {
                "green_gate_satisfied": False,
                "blocking_green_guard_primitives": [],
                "revision_score": 0.0,
            },
        },
    )
    # Deliberately invalid evaluation-lane content.  Projection succeeds only
    # if the builder never opens it and the canonical output hash excludes it.
    (target / "post_run_gold_forbidden.json").write_text(
        "this is intentionally not json\n", encoding="utf-8"
    )
    output_hash = canary_output_tree_hash(target, include_post_run_gold=False)
    _write_json(
        target / "target_run_manifest.json",
        {
            "status": "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD",
            "target_id": selected["target_id"],
            "as_of_date": AS_OF_DATE,
            "archetype_id": selected["archetype_id"],
            "production_research_complete": True,
            "gold_visibility": False,
            "gold_comparison_timing": "POST_RUN_ONLY",
            "completion_based_on_fixed_rounds": False,
            "zero_search_result_treated_as_completion": False,
            "transport_budget_treated_as_completion": False,
            "output_tree_hash": output_hash,
        },
    )
    return target


class E2RV6CanaryCompactReceiptTests(unittest.TestCase):
    def test_terminal_provider_allows_only_valid_accounted_history(self) -> None:
        audit = {
            "status": "COLLABORATION_PROVIDER_JOURNAL_ACTIVE",
            "provider_name": (
                "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE"
            ),
            "logical_call_count": 24,
            "successful_call_count": 24,
            "provider_error_count": 0,
            "provider_output_rejected_count": 0,
            "prompt_transport_rejected_count": 0,
            "collaboration_journal": {
                "status": "COLLABORATION_JOURNAL_ACTIVE",
                "request_count": 148,
                "validated_request_count": 148,
                "invalid_request_count": 0,
                "response_file_count": 138,
                "validated_response_count": 138,
                "invalid_response_count": 0,
                "orphan_response_count": 0,
                "pending_response_count": 10,
                "quarantined_response_count": 1,
                "validated_quarantined_response_count": 1,
                "invalid_quarantined_response_count": 0,
                "unresolved_pending_response_count": 9,
            },
        }

        accounting = _production_provider_accounting(
            audit,
            terminal_output_complete=True,
        )
        self.assertEqual(accounting["provider_error_count"], 0)
        with self.assertRaises(ValueError):
            _production_provider_accounting(
                audit,
                terminal_output_complete=False,
            )
        broken = deepcopy(audit)
        broken["collaboration_journal"][
            "unresolved_pending_response_count"
        ] = 8
        with self.assertRaises(ValueError):
            _production_provider_accounting(
                broken,
                terminal_output_complete=True,
            )

    def test_terminal_projection_recounts_positive_rosters_and_zero_material_gap(
        self,
    ) -> None:
        selection = _selection()

        def rebind(target: Path) -> None:
            manifest_path = target / "target_run_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["output_tree_hash"] = canary_output_tree_hash(
                target, include_post_run_gold=False
            )
            _write_json(manifest_path, manifest)

        def mark_fixed_round_completion(target: Path) -> None:
            manifest_path = target / "target_run_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["completion_based_on_fixed_rounds"] = True
            _write_json(manifest_path, manifest)

        mutations = {
            "query": lambda target: _write_jsonl(target / "query_ledger.jsonl", []),
            "counterfact": lambda target: _write_jsonl(
                target / "counterfacts.jsonl", []
            ),
            "material_gap": lambda target: _write_json(
                target / "research_supervisor_review.json",
                {
                    "status": "READY_FOR_INDEPENDENT_SATURATION_REVIEW",
                    "structured_data_complete": True,
                    "unresolved_material_questions": ["contract quality unresolved"],
                },
            ),
            "provider_error": lambda target: _write_json(
                target / "research_provider_response_cache_audit.json",
                {
                    **json.loads(
                        (
                            target
                            / "research_provider_response_cache_audit.json"
                        ).read_text(encoding="utf-8")
                    ),
                    "provider_error_count": 1,
                },
            ),
            "fixed_round_completion": mark_fixed_round_completion,
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                target = _write_terminal_output(Path(temporary), selection)
                mutate(target)
                rebind(target)
                selected = selection["selections"][0]
                assert isinstance(selected, dict)
                with self.assertRaises(ValueError):
                    build_selection_bound_canary_artifacts_from_output(
                        repo_root=REPO_ROOT,
                        target_root=target,
                        selection=selection,
                        selection_row=selected,
                    )

    def test_terminal_current_output_projects_to_the_same_strong_roster(self) -> None:
        selection = _selection()
        selected = selection["selections"][0]
        assert isinstance(selected, dict)
        with tempfile.TemporaryDirectory() as temporary:
            target = _write_terminal_output(Path(temporary), selection)
            artifacts = build_selection_bound_canary_artifacts_from_output(
                repo_root=REPO_ROOT,
                target_root=target,
                selection=selection,
                selection_row=selected,
            )
            self.assertEqual(set(artifacts), set(REQUIRED_ARTIFACT_NAMES))
            score_receipt = artifacts["score_receipt.json"]
            assert isinstance(score_receipt, dict)
            self.assertEqual(len(score_receipt["blind_review_inventory"]), 8)
            self.assertEqual(score_receipt["canary_result"]["fact_count"], 8)
            verified = validate_selection_bound_canary_artifacts(
                selection=selection,
                selection_id=str(selected["selection_id"]),
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )
            self.assertEqual(verified["component_count"], 7)
            self.assertEqual(verified["judge_decision_count"], 21)
            (target / "red_team_research.json").unlink()
            with self.assertRaisesRegex(ValueError, "missing required leaf"):
                build_selection_bound_canary_artifacts_from_output(
                    repo_root=REPO_ROOT,
                    target_root=target,
                    selection=selection,
                    selection_row=selected,
                )

    def test_full_eight_artifact_lineage_exports_and_verifies_offline(self) -> None:
        selection, artifacts, manifest, reviews = _bundle()
        self.assertEqual(manifest["status"], COMPACT_RECEIPT_PASS)
        self.assertEqual(manifest["component_count"], 7)
        self.assertEqual(manifest["judge_decision_count"], 21)
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "one-canary-receipt"
            export_selection_bound_canary_bundle(
                output_directory=destination,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                reviews=reviews,
                repo_root=REPO_ROOT,
            )
            verified = verify_selection_bound_canary_directory(
                receipt_directory=destination,
                selection=selection,
                repo_root=REPO_ROOT,
            )
            self.assertEqual(verified["judge_decision_count"], 21)
            self.assertEqual(verified["canonical_stage"], manifest["canonical_stage"])

    def test_thin_summary_cannot_substitute_for_eight_artifacts(self) -> None:
        selection, artifacts, _, _ = _bundle()
        artifacts.pop("scoring_facts.jsonl")
        row = selection["selections"][0]
        assert isinstance(row, dict)
        with self.assertRaisesRegex(ValueError, "eight-artifact"):
            build_selection_bound_canary_manifest(
                selection=selection,
                selection_id=str(row["selection_id"]),
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )

    def test_cross_component_fact_swap_fails_even_when_record_hash_is_resealed(self) -> None:
        selection, artifacts, _, _ = _bundle()
        facts = artifacts["scoring_facts.jsonl"]
        assert isinstance(facts, list)
        facts[0]["component_ids"] = [CANONICAL_COMPONENT_ORDER[1]]
        facts[0]["accepted_fact_record_hash"] = stable_hash(
            {key: value for key, value in facts[0].items() if key != "accepted_fact_record_hash"}
        )
        row = selection["selections"][0]
        assert isinstance(row, dict)
        with self.assertRaisesRegex(ValueError, "role/component linkage"):
            validate_selection_bound_canary_artifacts(
                selection=selection,
                selection_id=str(row["selection_id"]),
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )

    def test_missing_judge_and_duplicate_reviews_fail_closed(self) -> None:
        selection, artifacts, manifest, reviews = _bundle()
        judges = artifacts["judge_decisions.jsonl"]
        assert isinstance(judges, list)
        judges.pop()
        row = selection["selections"][0]
        assert isinstance(row, dict)
        with self.assertRaisesRegex(ValueError, "twenty-one"):
            validate_selection_bound_canary_artifacts(
                selection=selection,
                selection_id=str(row["selection_id"]),
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )

        selection, artifacts, manifest, reviews = _bundle()
        reviews[1] = deepcopy(reviews[0])
        with self.assertRaisesRegex(ValueError, "not independent"):
            validate_selection_bound_canary_bundle(
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                reviews=reviews,
                repo_root=REPO_ROOT,
            )

        selection, artifacts, manifest, reviews = _bundle()
        reviews[0]["critical_count_sum"] = False
        with self.assertRaisesRegex(ValueError, "did not reproduce"):
            validate_selection_bound_canary_bundle(
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                reviews=reviews,
                repo_root=REPO_ROOT,
            )

    def test_tampered_quote_or_tracked_anchor_is_rejected(self) -> None:
        selection, artifacts, _, _ = _bundle()
        facts = artifacts["scoring_facts.jsonl"]
        assert isinstance(facts, list)
        facts[0]["exact_quote"] = "tampered quote"
        row = selection["selections"][0]
        assert isinstance(row, dict)
        with self.assertRaisesRegex(ValueError, "quote hash"):
            validate_selection_bound_canary_artifacts(
                selection=selection,
                selection_id=str(row["selection_id"]),
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )

        selection, artifacts, _, _ = _bundle()
        anchors = artifacts["anchor_manifest.jsonl"]
        assert isinstance(anchors, list)
        anchors[0]["normalized_anchor_payload"] = {
            **anchors[0]["normalized_anchor_payload"],
            "points_mid": 999.0,
        }
        anchors[0]["anchor_payload_hash"] = stable_hash(anchors[0]["normalized_anchor_payload"])
        row = selection["selections"][0]
        assert isinstance(row, dict)
        with self.assertRaisesRegex(ValueError, "tracked current config"):
            validate_selection_bound_canary_artifacts(
                selection=selection,
                selection_id=str(row["selection_id"]),
                artifacts=artifacts,
                repo_root=REPO_ROOT,
            )

    def test_directory_extra_file_and_one_review_fail(self) -> None:
        selection, artifacts, manifest, reviews = _bundle()
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "receipt"
            export_selection_bound_canary_bundle(
                output_directory=destination,
                selection=selection,
                manifest=manifest,
                artifacts=artifacts,
                reviews=reviews,
                repo_root=REPO_ROOT,
            )
            (destination / "thin_summary.json").write_text("{}\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unexpected or missing"):
                verify_selection_bound_canary_directory(
                    receipt_directory=destination,
                    selection=selection,
                    repo_root=REPO_ROOT,
                )


if __name__ == "__main__":
    unittest.main()
