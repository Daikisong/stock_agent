from __future__ import annotations

import base64
from copy import deepcopy
import hashlib
import json
import os
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest.mock import patch

from e2r.production.metadata import git_head_sha, stable_hash
from e2r.research_brain.intelligence_schema import stable_intelligence_id
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    _historical_anchors,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    COLLABORATION_REQUEST_SCHEMA_VERSION,
    COLLABORATION_RESPONSE_SCHEMA_VERSION,
    CollaborationCodexSubagentTransport,
    _canonical_hash,
    _request_id,
    _request_identity,
    _validate_agent_provenance,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER
from e2r.research_brain.researcher_mode.tracked_receipts import (
    GOLD_POST_RUN_PASS,
    GOLD_RECALL_METRIC_KEYS,
    PHASE101_TARGET_IDS,
    PROVIDER_ROUTE,
    RECEIPT_MANIFEST_SCHEMA,
    SCORE_RECEIPT_SCHEMA,
    STAGECOURT_RECEIPT_SCHEMA,
    VERIFICATION_FAIL,
    VERIFICATION_PASS,
    _decode_journal_envelope,
    _encode_journal_envelope,
    _fact_journal_provider_call_id,
    _fact_scope_attestation_payload,
    _fact_scope_attestation_hash,
    _provider_accounting,
    receipt_content_index,
    receipt_content_tree_hash,
    runtime_config_hash,
    stagecourt_rule_hash,
    verify_receipts,
    verify_target_receipt,
)


class E2RV6TrackedReceiptTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    MAXIMA = {
        "eps_fcf_explosion": 24.0,
        "earnings_visibility": 21.0,
        "bottleneck_pricing": 19.0,
        "market_mispricing": 15.0,
        "valuation_rerating": 12.0,
        "capital_allocation": 4.0,
        "information_confidence": 5.0,
    }

    def _write_json(self, path: Path, payload: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def test_embedded_journal_envelopes_reject_nonfinite_json(self) -> None:
        with self.assertRaises(ValueError):
            _encode_journal_envelope({"scope_confidence": float("nan")})
        malicious = base64.b64encode(
            zlib.compress(b'{"scope_confidence":NaN}')
        ).decode("ascii")
        with self.assertRaises(ValueError):
            _decode_journal_envelope(malicious)
        with self.assertRaises(ValueError):
            _canonical_hash({"scope_confidence": float("inf")})
        portable_payload = {"facts": [{"scope_confidence": 1.0}]}
        portable_raw = json.dumps(
            portable_payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
        alternate_compression = base64.b64encode(
            zlib.compress(portable_raw, level=1)
        ).decode("ascii")
        self.assertEqual(
            _decode_journal_envelope(alternate_compression),
            portable_payload,
        )

    def _write_jsonl(self, path: Path, rows: list[dict[str, object]]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "".join(
                json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
                for row in rows
            ),
            encoding="utf-8",
        )

    def _fixture(self, base: Path, *, target_id: str = "005930") -> Path:
        target = base / target_id
        components: list[dict[str, object]] = []
        judges: list[dict[str, object]] = []
        facts: list[dict[str, object]] = []
        sources: list[dict[str, object]] = []
        anchors: list[dict[str, object]] = []
        archetype_id = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
        fact_request_payload = {
            "target_id": target_id,
            "as_of_date": "2026-07-12",
            "fixture_scope": "TRACKED_RECEIPT_FACT_EXTRACTION",
        }
        fact_prompt_hash = stable_intelligence_id(
            "FACTPROMPT", fact_request_payload
        )
        fact_response_hash = "FACTRESP-PENDING"
        current_anchors = _historical_anchors(
            repo_root=self.ROOT,
            archetype_id=archetype_id,
        )
        anchor_by_component = {
            component_id: next(
                row
                for row in current_anchors
                if row["component_id"] == component_id
            )
            for component_id in CANONICAL_COMPONENT_ORDER
        }
        for component_index, component_id in enumerate(CANONICAL_COMPONENT_ORDER):
            fact_id = stable_intelligence_id(
                "EFACT",
                {
                    "target_id": target_id,
                    "as_of_date": "2026-07-12",
                    "subject": f"{target_id} {component_id}".casefold(),
                    "business_segment": "test",
                    "product_family": "test",
                    "economic_mechanism": "test mechanism",
                    "predicate": "test_predicate",
                    "value": "test",
                    "unit": "none",
                    "period": "2026",
                    "direction": "POSITIVE",
                    "current_lifecycle": "CURRENT",
                },
            )
            source_id = f"SOURCE-{component_index}"
            anchor_payload = dict(anchor_by_component[component_id])
            anchor_id = str(anchor_payload["anchor_id"])
            quote = f"{component_id} current source-backed fact"
            quote_hash = hashlib.sha256(quote.encode("utf-8")).hexdigest()
            document_hash = hashlib.sha256(source_id.encode("utf-8")).hexdigest()
            claim_identity = {
                "target_id": target_id,
                "as_of_date": "2026-07-12",
                "document_id": source_id,
                "question_family_id": "TEST_QUESTION",
                "subject_id": target_id,
                "predicate_family": "TEST_PREDICATE",
                "normalized_object": "test",
                "period": "2026",
                "mechanism_scope_id": "TEST_HBM_SCOPE",
                "exact_quote": quote,
            }
            claim_id = stable_intelligence_id("RFC", claim_identity)
            claim_scope_payload = {
                "primary_claim_id": claim_id,
                "allowed_component_ids": list(CANONICAL_COMPONENT_ORDER),
                "scope_business_segment": "MEMORY",
                "scope_product_family": "HBM",
                "scope_technology_family": "HBM",
                "scope_transaction_type": "GENERIC_INFORMATION",
                "scope_economic_mechanism": "INFORMATION_ONLY",
                "scope_confidence": 1.0,
            }
            judge_ids = [f"JUDGE-{component_index}-{role}" for role in ("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE")]
            judge_prompt_hashes = [
                hashlib.sha256(judge_id.encode()).hexdigest()
                for judge_id in judge_ids
            ]
            judge_response_hashes = [
                hashlib.sha256((judge_id + "response").encode()).hexdigest()
                for judge_id in judge_ids
            ]
            components.append(
                {
                    "schema_version": "e2r_v6_component_decision_receipt_v1",
                    "component_id": component_id,
                    "max_points": self.MAXIMA[component_id],
                    "support_points": 0.0,
                    "counter_effect": 0.0,
                    "final_points": 0.0,
                    "support_fact_ids": [fact_id],
                    "counter_fact_ids": [],
                    "resolution_fact_ids": [],
                    "resolution_fact_role": "MEMO_CONTEXT_ONLY_NOT_DIRECT_POINT_INPUT",
                    "historical_anchor_ids": [anchor_id],
                    "judge_decision_ids": judge_ids,
                    "why_not_higher": "current evidence does not support points",
                    "why_not_lower": "zero is the deterministic floor",
                    "confidence": 1.0,
                    "research_status": "RESEARCH_COMPLETE",
                    "aggregation_method": "MEDIAN_WITH_ALLOWED_RANGE_INTERSECTION",
                    "aggregation_trace_hash": "0" * 64,
                    "proposal_median": 0.0,
                    "consensus_band": [0.0, 0.0],
                    "judge_proposals": {
                        "ANALYST": 0.0,
                        "SKEPTIC": 0.0,
                        "CALIBRATION_JUDGE": 0.0,
                    },
                    "prompt_hashes": judge_prompt_hashes,
                    "response_hashes": judge_response_hashes,
                    "provider_call_ids": [f"CALL-{value}" for value in judge_ids],
                    "aggregator_config_hash": "7" * 64,
                }
            )
            for role, judge_id in zip(("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE"), judge_ids):
                judges.append(
                    {
                        "schema_version": "e2r_v6_judge_decision_receipt_v1",
                        "judge_decision_id": judge_id,
                        "component_id": component_id,
                        "role": role,
                        "proposed_points": 0.0,
                        "allowed_range": [0.0, 0.0],
                        "support_fact_ids": [fact_id],
                        "counter_fact_ids": [],
                        "anchor_ids": [anchor_id],
                        "why_higher": "",
                        "why_lower": "",
                        "prompt_hash": judge_prompt_hashes[
                            judge_ids.index(judge_id)
                        ],
                        "response_hash": judge_response_hashes[
                            judge_ids.index(judge_id)
                        ],
                        "provider_call_id": f"CALL-{judge_id}",
                        "provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
                        "provider_route": PROVIDER_ROUTE,
                        "score_or_stage_authority": False,
                    }
                )
            facts.append(
                {
                    "schema_version": "e2r_v6_scoring_fact_receipt_v1",
                    "fact_id": fact_id,
                    "target_id": target_id,
                    "component_ids": [component_id],
                    "fact_role": "SUPPORT",
                    "fact_roles": ["SUPPORT"],
                    "direct_point_input": True,
                    "subject_id": target_id,
                    "fact_identity_subject": f"{target_id} {component_id}",
                    "business_segment": "TEST",
                    "product_family": "TEST",
                    "economic_mechanism": "test mechanism",
                    "fact_identity_predicate": "TEST_PREDICATE",
                    "fact_identity_direction": "POSITIVE",
                    "predicate_family": "TEST_PREDICATE",
                    "normalized_object": "test",
                    "value": "test",
                    "unit": "none",
                    "period": "2026",
                    "temporal_status": "CURRENT",
                    "claim_ids": [claim_id],
                    "primary_claim_id": claim_id,
                    "question_family_id": "TEST_QUESTION",
                    "mechanism_scope_id": "TEST_HBM_SCOPE",
                    "allowed_component_ids": list(CANONICAL_COMPONENT_ORDER),
                    "scope_business_segment": "MEMORY",
                    "scope_product_family": "HBM",
                    "scope_technology_family": "HBM",
                    "scope_transaction_type": "GENERIC_INFORMATION",
                    "scope_economic_mechanism": "INFORMATION_ONLY",
                    "scope_confidence": 1.0,
                    "claim_scope_hash": stable_hash(claim_scope_payload),
                    "source_document_id": source_id,
                    "source_url": f"https://example.com/{component_index}",
                    "source_title": component_id,
                    "source_publisher": "example.com",
                    "source_publisher_derivation": "CANONICAL_URL_HOSTNAME_V1",
                    "source_tier": "ISSUER_OFFICIAL",
                    "source_family": "TEST_OFFICIAL",
                    "published_at": "2026-01-01",
                    "available_at": "2026-01-01",
                    "document_content_hash": document_hash,
                    "exact_quote": quote,
                    "exact_quote_hash": quote_hash,
                    "quote_excerpt": quote,
                    "quote_excerpt_hash": quote_hash,
                    "page_section_locator": "NOT_CAPTURED",
                    "issuer_scoped": True,
                    "issuer_scope_derivation": "CLAIM_TARGET_SCOPE_V1",
                    "current_score_eligible": True,
                    "current_score_eligibility_basis": "FINAL_DECISION_REFERENCE_AND_AS_OF_VALIDATED",
                    "source_independence_group": f"TEST:{component_index}",
                    "extraction_provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
                    "provider_prompt_hash": fact_prompt_hash,
                    "provider_response_hash": fact_response_hash,
                    "as_of_date": "2026-07-12",
                    "gold_fact": False,
                }
            )
            sources.append(
                {
                    "schema_version": "e2r_v6_source_manifest_row_v1",
                    "source_document_id": source_id,
                    "source_url": f"https://example.com/{component_index}",
                    "source_title": component_id,
                    "source_publisher": "example.com",
                    "source_tier": "ISSUER_OFFICIAL",
                    "source_family": "TEST_OFFICIAL",
                    "published_at": "2026-01-01",
                    "available_at": "2026-01-01",
                    "document_content_hash": document_hash,
                    "source_independence_group": f"TEST:{component_index}",
                    "fact_document_hashes": {fact_id: document_hash},
                    "fact_exact_quote_hashes": {fact_id: quote_hash},
                }
            )
            anchors.append(
                {
                    "schema_version": "e2r_v6_anchor_manifest_row_v1",
                    "anchor_id": anchor_id,
                    "component_id": component_id,
                    "archetype_id": archetype_id,
                    "normalized_anchor_payload": anchor_payload,
                    "anchor_payload_hash": stable_hash(anchor_payload),
                }
            )

        gold_metrics = {key: 1.0 for key in GOLD_RECALL_METRIC_KEYS}
        gold_thresholds = {
            f"{key}_min": 1.0 for key in GOLD_RECALL_METRIC_KEYS
        }
        gold_critical_counts = {
            f"{key}_below_threshold_count": 0
            for key in GOLD_RECALL_METRIC_KEYS
        }
        gold_critical_counts.update(
            {
                "gold_leakage_count": 0,
                "production_component_memo_incomplete_count": 0,
            }
        )
        gold_projection = {
            "schema_version": "e2r_v5_full_thesis_gold_research_recall_v1",
            "status": GOLD_POST_RUN_PASS,
            "as_of_date": "2026-07-12",
            "comparison_timing": "POST_RUN_ONLY",
            "gold_visibility_during_production": False,
            "metrics": gold_metrics,
            "thresholds": gold_thresholds,
            "critical_counts": gold_critical_counts,
            "critical_count_sum": 0,
            "gold_fact_count": 7,
            "qualified_material_fact_match_count": 7,
            "covered_target_component_count": 14,
            "required_target_component_count": 14,
        }
        gold_audit_hash = "e" * 64
        gold_projection_hash = stable_hash(gold_projection)
        output_tree_hash = "d" * 64
        receipt_id = "V6RECEIPT-" + stable_hash(
            {
                "target_id": target_id,
                "as_of_date": "2026-07-12",
                "output_tree_hash": output_tree_hash,
            }
        )[:24]
        score = {
            "schema_version": SCORE_RECEIPT_SCHEMA,
            "receipt_id": receipt_id,
            "target_id": target_id,
            "score_scale": "FULL_E2R_100",
            "score_valid": True,
            "component_score_vector": {key: 0.0 for key in CANONICAL_COMPONENT_ORDER},
            "component_max_vector": self.MAXIMA,
            "total_score": 0.0,
            "total_score_recomputed": 0.0,
            "component_sum_matches_total": True,
            "research_complete": True,
            "semantic_saturation_certified": True,
            "material_gap_count": 0,
            "provider_error_count": 0,
            "canonical_stage": "0",
            "stage_status": "FINAL",
            "risk_overlay": "LOW",
            "hard_break_fact_ids": [],
            "daily_event_overlay_can_change_canonical_stage": False,
            "production_research_status": "COMPLETE",
            "gold_evaluation_status": "PASS",
            "score_status": "COMPLETE",
            "stagecourt_status": "FINAL",
            "gold_post_run_metrics": gold_metrics,
            "gold_post_run_audit": gold_projection,
            "gold_audit_hash": gold_audit_hash,
            "gold_receipt_projection_hash": gold_projection_hash,
            "gold_leakage_count": 0,
        }
        stage = {
            "schema_version": STAGECOURT_RECEIPT_SCHEMA,
            "target_id": target_id,
            "score_receipt_id": receipt_id,
            "component_score_vector_hash": stable_hash(score["component_score_vector"]),
            "total_score": 0.0,
            "risk_fact_ids": [],
            "hard_break_fact_ids": [],
            "hard_break_claim_ids": [],
            "canonical_stage": "0",
            "decision_status": "FINAL",
            "score_valid": True,
            "event_overlay": {"canonical_stage_effect": "NONE", "status": "NO_EVENT_OVERLAY"},
            "event_overlay_changed_canonical_stage": False,
            "stagecourt_rule_hash": stagecourt_rule_hash(self.ROOT),
            "decision_trace_hash": "a" * 64,
            "classification_input": {
                "diagnostic_scores": {
                    "score_valid": 1.0,
                    "price_only_blowoff_score": 0.0,
                    "revision_score": 0.0,
                    "structural_visibility_quality": 0.0,
                    "contract_quality": 0.0,
                    "one_off_shortage_risk": 100.0,
                },
                "previous_stage": None,
                "thesis_ongoing": False,
                "theme_regime_score": 0.0,
                "company_event_score": 0.0,
                "high_quality_company_event": False,
                "archive_requested": False,
                "coverage_impossible": False,
                "red_team": {
                    "soft_4b_score": 0.0,
                    "soft_4b_status": "none",
                    "thesis_break_score": 0.0,
                    "risk_level": "low",
                    "has_hard_break": False,
                },
                "green_gate_satisfied": False,
                "blocking_green_guard_primitives": [],
                "revision_score": 0.0,
            },
        }
        fact_response_payload = {
            "facts": [
                dict(_fact_scope_attestation_payload(fact)) for fact in facts
            ]
        }
        fact_response_hash = stable_intelligence_id(
            "FACTRESP", fact_response_payload
        )
        for fact in facts:
            fact["provider_response_hash"] = fact_response_hash
        request_prompt = (
            "Extract fixture facts.\n"
            + json.dumps(
                fact_request_payload,
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        output_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": ["facts"],
            "properties": {
                "facts": {
                    "type": "array",
                    "items": {"type": "object"},
                }
            },
            "additionalProperties": False,
        }
        provider_identity = dict(
            CollaborationCodexSubagentTransport().provider_identity()
        )
        request_identity = _request_identity(
            pass_name="EVIDENCE_FACT_EXTRACTION",
            prompt_hash=hashlib.sha256(
                request_prompt.encode("utf-8")
            ).hexdigest(),
            output_schema_hash=_canonical_hash(output_schema),
            provider_identity_hash=_canonical_hash(provider_identity),
        )
        request_envelope = {
            "schema_version": COLLABORATION_REQUEST_SCHEMA_VERSION,
            "request_id": _request_id(request_identity),
            "request_identity": dict(request_identity),
            "provider_identity": provider_identity,
            "provider_identity_hash": request_identity[
                "provider_identity_hash"
            ],
            "schema_name": "e2r_v5_evidence_fact_extraction",
            "pass_name": "EVIDENCE_FACT_EXTRACTION",
            "prompt": request_prompt,
            "prompt_hash": request_identity["prompt_hash"],
            "output_schema": output_schema,
            "output_schema_hash": request_identity["output_schema_hash"],
            "score_or_stage_authority": False,
            "production_score_authority": False,
            "response_import_required": True,
        }
        provenance = _validate_agent_provenance(
            agent_id="fixture-agent",
            canonical_task_name="/root/fixture",
            agent_model="fixture-model",
        )
        payload_hash = _canonical_hash(fact_response_payload)
        response_envelope = {
            "schema_version": COLLABORATION_RESPONSE_SCHEMA_VERSION,
            "response_id": "COLLABRESP-"
            + _canonical_hash(
                {
                    "request_id": request_envelope["request_id"],
                    "payload_hash": payload_hash,
                    "provenance": provenance,
                }
            ),
            "request_id": request_envelope["request_id"],
            "prompt_hash": request_envelope["prompt_hash"],
            "output_schema_hash": request_envelope["output_schema_hash"],
            "provider_identity_hash": request_envelope[
                "provider_identity_hash"
            ],
            "payload_hash": payload_hash,
            "payload": fact_response_payload,
            "provenance": provenance,
            "validation": {
                "draft202012_schema_valid": True,
                "blind_research_output_valid": True,
                "request_hashes_valid": True,
                "downstream_semantic_validation_required": True,
            },
            "score_or_stage_authority": False,
            "production_score_authority": False,
        }
        self._write_json(target / "score_receipt.json", score)
        self._write_jsonl(target / "component_decisions.jsonl", components)
        self._write_jsonl(target / "scoring_facts.jsonl", facts)
        self._write_jsonl(target / "judge_decisions.jsonl", judges)
        self._write_jsonl(target / "source_manifest.jsonl", sources)
        self._write_jsonl(target / "anchor_manifest.jsonl", anchors)
        provider_calls = [
            {
                "schema_version": "e2r_v6_provider_call_receipt_v1",
                "provider_call_id": judge["provider_call_id"],
                "call_scope": "COMPONENT_JUDGE",
                "provider_name": judge["provider_name"],
                "provider_kind": "COLLABORATION_CODEX",
                "provider_attempt_count": 1,
                "prompt_hash": judge["prompt_hash"],
                "response_hash": judge["response_hash"],
                "status": "SUCCESS",
                "score_or_stage_authority": False,
            }
            for judge in judges
        ]
        fact_call = {
                "schema_version": "e2r_v6_provider_call_receipt_v1",
                "provider_call_id": "",
                "call_scope": "FACT_EXTRACTION",
                "provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
                "provider_kind": "COLLABORATION_CODEX",
                "provider_attempt_count": 1,
                "prompt_hash": fact_prompt_hash,
                "response_hash": fact_response_hash,
                "status": "SUCCESS",
                "score_or_stage_authority": False,
                "request_id": request_envelope["request_id"],
                "response_id": response_envelope["response_id"],
                "request_envelope_hash": stable_hash(request_envelope),
                "response_envelope_hash": stable_hash(response_envelope),
                "fact_scope_attestation_hashes": sorted(
                    _fact_scope_attestation_hash(fact) for fact in facts
                ),
                "request_envelope_zlib_b64": _encode_journal_envelope(
                    request_envelope
                ),
                "response_envelope_zlib_b64": _encode_journal_envelope(
                    response_envelope
                ),
            }
        fact_call["provider_call_id"] = _fact_journal_provider_call_id(
            fact_call
        )
        provider_calls.append(fact_call)
        provider_calls.append(
            {
                "schema_version": "e2r_v6_provider_call_receipt_v1",
                "provider_call_id": "RUNPROV-TEST",
                "call_scope": "FULL_RESEARCH_INVOCATION_AUDIT",
                "provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
                "provider_kind": "COLLABORATION_CODEX",
                "provider_attempt_count": 1,
                "successful_call_count": 1,
                "provider_error_count": 0,
                "transport_call_count": 1,
                "prompt_hash": None,
                "response_hash": "f" * 64,
                "status": "COLLABORATION_PROVIDER_JOURNAL_ACTIVE",
                "score_or_stage_authority": False,
            }
        )
        self._write_jsonl(target / "provider_calls.jsonl", provider_calls)
        self._write_json(target / "stagecourt_receipt.json", stage)
        manifest = {
            "schema_version": RECEIPT_MANIFEST_SCHEMA,
            "receipt_id": receipt_id,
            "target_id": target_id,
            "company_name": "테스트회사",
            "as_of_date": "2026-07-12",
            "latest_trading_snapshot_date": "2026-07-10",
            "archetype_id": archetype_id,
            "run_commit_sha": git_head_sha(self.ROOT),
            "verification_commit_sha": git_head_sha(self.ROOT),
            "commit_sha_hash_scope": "MANIFEST_EXCLUDED_FROM_IMMUTABLE_CONTENT_HASH",
            "config_hash": runtime_config_hash(),
            "prompt_hashes": {
                f"{judge['component_id']}:{judge['role']}": judge["prompt_hash"]
                for judge in judges
            },
            "provider_identity_hash": "c" * 64,
            "source_corpus_hash": stable_hash(sources),
            "output_tree_hash": output_tree_hash,
            "output_tree_hash_recomputed": output_tree_hash,
            "output_tree_hash_matches": True,
            "gold_audit_hash": gold_audit_hash,
            "gold_receipt_projection_hash": gold_projection_hash,
            "tracked_receipt_tree_hash": receipt_content_tree_hash(target),
            "tracked_receipt_content_index": list(receipt_content_index(target)),
            "tracked_receipt_hash_scope": "ALL_TARGET_RECEIPT_FILES_EXCEPT_RECEIPT_MANIFEST_JSON",
            "gold_visible_during_production": False,
            "provider_selected_explicitly": True,
            "provider_route": PROVIDER_ROUTE,
            "qwen_call_count": 0,
            "ollama_call_count": 0,
            "provider_call_counts": {"COLLABORATION_CODEX": 23},
            "scored_fact_provider_lineage_counts": {"COLLABORATION_CODEX": 7},
            "inherited_qwen_scored_fact_count": 0,
            "inherited_ollama_scored_fact_count": 0,
            "current_invocation_provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
            "current_invocation_logical_call_count": 1,
            "current_invocation_successful_call_count": 1,
            "current_invocation_provider_error_count": 0,
            "query_count": 1,
            "document_count": len(sources),
            "fact_count": len(facts),
            "counterfact_count": 0,
            "receipt_scoring_fact_count": len(facts),
            "receipt_source_count": len(sources),
            "receipt_anchor_count": len(anchors),
            "receipt_judge_count": len(judges),
            "receipt_component_count": len(components),
            "receipt_provider_call_count": len(provider_calls),
            "score_or_stage_authority": False,
        }
        named_payloads = {
            "score_receipt.json": score,
            "component_decisions.jsonl": components,
            "scoring_facts.jsonl": facts,
            "judge_decisions.jsonl": judges,
            "source_manifest.jsonl": sources,
            "anchor_manifest.jsonl": anchors,
            "provider_calls.jsonl": provider_calls,
            "stagecourt_receipt.json": stage,
        }
        manifest["provider_accounting"] = _provider_accounting(
            content_index=receipt_content_index(target),
            named_payloads=named_payloads,
        )
        self._write_json(target / "receipt_manifest.json", manifest)
        return target

    def _failure_codes(self, result: dict[str, object]) -> set[str]:
        return {str(row["code"]) for row in result["failures"]}  # type: ignore[index]

    def _reseal(self, target: Path) -> None:
        """Rebuild every self-reported hash after a synthetic semantic tamper."""

        manifest_path = target / "receipt_manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        named_payloads: dict[str, object] = {}
        for filename in (
            "score_receipt.json",
            "stagecourt_receipt.json",
        ):
            named_payloads[filename] = json.loads(
                (target / filename).read_text(encoding="utf-8")
            )
        for filename in (
            "component_decisions.jsonl",
            "scoring_facts.jsonl",
            "judge_decisions.jsonl",
            "source_manifest.jsonl",
            "anchor_manifest.jsonl",
            "provider_calls.jsonl",
        ):
            named_payloads[filename] = [
                json.loads(line)
                for line in (target / filename)
                .read_text(encoding="utf-8")
                .splitlines()
                if line.strip()
            ]
        index = receipt_content_index(target)
        manifest["tracked_receipt_tree_hash"] = receipt_content_tree_hash(target)
        manifest["tracked_receipt_content_index"] = list(index)
        manifest["provider_accounting"] = _provider_accounting(
            content_index=index,
            named_payloads=named_payloads,
        )
        self._write_json(manifest_path, manifest)

    def test_receipt_only_fixture_recomputes_score_and_stage(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            result = verify_target_receipt(target)
        self.assertEqual(result["status"], VERIFICATION_PASS)
        self.assertEqual(result["critical_count"], 0)
        self.assertEqual(result["metrics"]["total_score_recomputed"], 0.0)
        self.assertEqual(result["metrics"]["canonical_stage_recomputed"], "0")
        self.assertEqual(result["forbidden_runtime_inputs_read"], [])

    def test_receipt_root_aggregates_targets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "receipts"
            for target_id in PHASE101_TARGET_IDS:
                self._fixture(root, target_id=target_id)
            result = verify_receipts(root)
        self.assertEqual(result["status"], VERIFICATION_PASS)
        self.assertEqual(result["target_count"], 2)
        self.assertEqual(result["target_ids"], list(PHASE101_TARGET_IDS))

    def test_component_score_tamper_fails_even_when_json_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            score["component_score_vector"]["eps_fcf_explosion"] = 1.0
            self._write_json(score_path, score)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("RECEIPT_TREE_HASH_MISMATCH", codes)
        self.assertIn("COMPONENT_SUM_MISMATCH", codes)
        self.assertIn("SCORE_COMPONENT_DECISION_MISMATCH", codes)

    def test_orphan_fact_reference_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "component_decisions.jsonl"
            rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            rows[0]["support_fact_ids"].append("FACT-ORPHAN")
            self._write_jsonl(path, rows)
            result = verify_target_receipt(target)
        self.assertIn("ORPHAN_COMPONENT_FACT_ID", self._failure_codes(result))

    def test_stage_tamper_fails_deterministic_recompute(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "stagecourt_receipt.json"
            stage = json.loads(path.read_text(encoding="utf-8"))
            stage["canonical_stage"] = "2"
            self._write_json(path, stage)
            result = verify_target_receipt(target)
        self.assertIn("CANONICAL_STAGE_RECOMPUTE_MISMATCH", self._failure_codes(result))

    def test_ollama_call_and_inherited_lineage_are_both_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            self._write_jsonl(
                target / "provider_calls.jsonl",
                [
                    {
                        "provider_call_id": "CALL-OLLAMA",
                        "provider_name": "OLLAMA_STRUCTURED_RESEARCHER_MODE",
                        "provider_kind": "OLLAMA",
                        "provider_attempt_count": 1,
                    }
                ],
            )
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["provider_call_counts"] = {"OLLAMA": 1}
            manifest["ollama_call_count"] = 1
            manifest["inherited_ollama_scored_fact_count"] = 1
            manifest["tracked_receipt_tree_hash"] = receipt_content_tree_hash(target)
            manifest["tracked_receipt_content_index"] = list(receipt_content_index(target))
            self._write_json(manifest_path, manifest)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("OLLAMA_CALL_COUNT_NONZERO", codes)
        self.assertIn("INHERITED_OLLAMA_SCORED_FACT_LINEAGE_PRESENT", codes)

    def test_qwen_call_and_inherited_lineage_are_both_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            self._write_jsonl(
                target / "provider_calls.jsonl",
                [
                    {
                        "provider_call_id": "CALL-QWEN",
                        "provider_name": "QWEN_LOCAL_RESEARCHER",
                        "provider_kind": "QWEN",
                        "provider_attempt_count": 1,
                    }
                ],
            )
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["provider_call_counts"] = {"QWEN": 1}
            manifest["qwen_call_count"] = 1
            manifest["inherited_qwen_scored_fact_count"] = 1
            manifest["tracked_receipt_tree_hash"] = receipt_content_tree_hash(
                target
            )
            manifest["tracked_receipt_content_index"] = list(
                receipt_content_index(target)
            )
            self._write_json(manifest_path, manifest)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("QWEN_CALL_COUNT_NONZERO", codes)
        self.assertIn("INHERITED_QWEN_SCORED_FACT_LINEAGE_PRESENT", codes)

    def test_any_non_codex_call_or_scored_lineage_is_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            self._write_jsonl(
                target / "provider_calls.jsonl",
                [
                    {
                        "provider_call_id": "CALL-LOCAL",
                        "provider_name": "LLAMA_CPP_PROVIDER",
                        "provider_kind": "LLAMA_CPP",
                        "provider_attempt_count": 1,
                    }
                ],
            )
            fact_path = target / "scoring_facts.jsonl"
            facts = [
                json.loads(line)
                for line in fact_path.read_text(encoding="utf-8").splitlines()
            ]
            facts[0]["extraction_provider_name"] = "LOCALAI"
            self._write_jsonl(fact_path, facts)
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["provider_call_counts"] = {"LLAMA_CPP": 1}
            manifest["scored_fact_provider_lineage_counts"] = {
                "COLLABORATION_CODEX": 6,
                "LOCALAI": 1,
            }
            manifest["tracked_receipt_tree_hash"] = receipt_content_tree_hash(
                target
            )
            manifest["tracked_receipt_content_index"] = list(
                receipt_content_index(target)
            )
            self._write_json(manifest_path, manifest)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("UNAUTHORIZED_RESEARCH_PROVIDER_CALL_KIND", codes)
        self.assertIn("UNAUTHORIZED_SCORED_FACT_PROVIDER_LINEAGE", codes)

    def test_provider_names_containing_codex_cannot_bypass_allowlist(self) -> None:
        for provider_name in (
            "LOCALAI_CODEX",
            "NOT_CODEX",
            "LOCALAI_COLLABORATION",
        ):
            with self.subTest(provider_name=provider_name), tempfile.TemporaryDirectory() as directory:
                target = self._fixture(Path(directory) / "receipts")
                self._write_jsonl(
                    target / "provider_calls.jsonl",
                    [
                        {
                            "provider_call_id": "CALL-FORGED",
                            "provider_name": provider_name,
                            "provider_kind": "CODEX",
                            "provider_attempt_count": 1,
                        }
                    ],
                )
                manifest_path = target / "receipt_manifest.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                manifest["provider_call_counts"] = {provider_name: 1}
                manifest["tracked_receipt_tree_hash"] = receipt_content_tree_hash(
                    target
                )
                manifest["tracked_receipt_content_index"] = list(
                    receipt_content_index(target)
                )
                self._write_json(manifest_path, manifest)
                result = verify_target_receipt(target)
            self.assertIn(
                "UNAUTHORIZED_RESEARCH_PROVIDER_CALL_KIND",
                self._failure_codes(result),
            )

    def test_judge_and_current_invocation_provider_lineage_are_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            judges_path = target / "judge_decisions.jsonl"
            judges = [
                json.loads(line)
                for line in judges_path.read_text(encoding="utf-8").splitlines()
            ]
            judges[0]["provider_name"] = "OLLAMA_STRUCTURED_RESEARCHER_MODE"
            judges[1]["provider_route"] = "LOCAL_PROVIDER_ROUTE"
            self._write_jsonl(judges_path, judges)
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["current_invocation_provider_name"] = "LOCALAI_CODEX"
            manifest["tracked_receipt_tree_hash"] = receipt_content_tree_hash(
                target
            )
            manifest["tracked_receipt_content_index"] = list(
                receipt_content_index(target)
            )
            self._write_json(manifest_path, manifest)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("UNAUTHORIZED_CURRENT_INVOCATION_PROVIDER", codes)
        self.assertIn("UNAUTHORIZED_JUDGE_PROVIDER_LINEAGE", codes)
        self.assertIn("JUDGE_PROVIDER_ROUTE_MISMATCH", codes)

    def test_phase101_root_requires_exact_two_target_roster(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "receipts"
            self._fixture(root, target_id="005930")
            missing = verify_receipts(root)
            self.assertEqual(missing["status"], VERIFICATION_FAIL)
            self.assertEqual(
                missing["root_failures"][0]["code"],
                "EXACT_PHASE101_TARGET_ROOT_ROSTER_REQUIRED",
            )
            self._fixture(root, target_id="000660")
            self._fixture(root, target_id="UNEXPECTED")
            unexpected = verify_receipts(root)
        self.assertEqual(unexpected["status"], VERIFICATION_FAIL)
        self.assertEqual(
            unexpected["root_failures"][0]["code"],
            "EXACT_PHASE101_TARGET_ROOT_ROSTER_REQUIRED",
        )

    def test_receipt_root_rejects_every_unexpected_entry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "receipts"
            for target_id in PHASE101_TARGET_IDS:
                self._fixture(root, target_id=target_id)
            (root / "gold_facts.json").write_text(
                '{"future_outcome":"QWEN at ::1 /tmp/leak"}\n',
                encoding="utf-8",
            )
            result = verify_receipts(root)
        self.assertEqual(result["status"], VERIFICATION_FAIL)
        detail = result["root_failures"][0]["detail"]
        self.assertEqual(detail["unexpected_root_entries"], ["gold_facts.json"])

    def test_manifest_rejects_unexpected_gold_or_answer_fields_without_reseal(
        self,
    ) -> None:
        for key, value in (
            ("gold_facts", [{"future_outcome": "2026-12 actual EPS beat"}]),
            ("post_run_gold_answer_key", "future result"),
        ):
            with self.subTest(key=key), tempfile.TemporaryDirectory() as directory:
                target = self._fixture(Path(directory) / "receipts")
                path = target / "receipt_manifest.json"
                manifest = json.loads(path.read_text(encoding="utf-8"))
                manifest[key] = value
                self._write_json(path, manifest)
                result = verify_target_receipt(target)
            self.assertIn(
                "MANIFEST_EXACT_FIELD_ROSTER_REQUIRED",
                self._failure_codes(result),
            )

    def test_target_receipt_never_reads_symlinked_or_extra_leaf(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            target = self._fixture(base / "receipts")
            path = target / "scoring_facts.jsonl"
            external = base / "untracked_scoring_facts.jsonl"
            external.write_bytes(path.read_bytes())
            path.unlink()
            path.symlink_to(external)
            result = verify_target_receipt(target)
        self.assertEqual(result["status"], VERIFICATION_FAIL)
        self.assertIn(
            "EXACT_REGULAR_TARGET_RECEIPT_FILE_ROSTER_REQUIRED",
            self._failure_codes(result),
        )

    def test_symlinked_target_directory_is_rejected_before_external_listing(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            external = base / "private"
            external.mkdir()
            (external / "SECRET_CUSTOMER_LIST.txt").write_text(
                "private",
                encoding="utf-8",
            )
            root = base / "receipts"
            root.mkdir()
            self._fixture(root, target_id="000660")
            (root / "005930").symlink_to(external, target_is_directory=True)
            direct = verify_target_receipt(root / "005930")
            combined = verify_receipts(root)
        self.assertIn(
            "TARGET_RECEIPT_ROOT_SYMLINK_FORBIDDEN",
            self._failure_codes(direct),
        )
        self.assertNotIn("SECRET_CUSTOMER_LIST.txt", json.dumps(direct))
        self.assertNotIn("SECRET_CUSTOMER_LIST.txt", json.dumps(combined))

    def test_bidirectional_component_judge_fact_anchor_links_cannot_be_resealed(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            component_path = target / "component_decisions.jsonl"
            components = [
                json.loads(line)
                for line in component_path.read_text(encoding="utf-8").splitlines()
            ]
            components[0]["judge_decision_ids"] = components[0][
                "judge_decision_ids"
            ][1:]
            self._write_jsonl(component_path, components)
            fact_path = target / "scoring_facts.jsonl"
            facts = [
                json.loads(line)
                for line in fact_path.read_text(encoding="utf-8").splitlines()
            ]
            facts[0]["component_ids"] = [CANONICAL_COMPONENT_ORDER[1]]
            self._write_jsonl(fact_path, facts)
            anchor_path = target / "anchor_manifest.jsonl"
            anchors = [
                json.loads(line)
                for line in anchor_path.read_text(encoding="utf-8").splitlines()
            ]
            anchors[0]["component_id"] = CANONICAL_COMPONENT_ORDER[1]
            self._write_jsonl(anchor_path, anchors)
            self._reseal(target)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("COMPONENT_JUDGE_BIDIRECTIONAL_MISMATCH", codes)
        self.assertIn("FACT_COMPONENT_BIDIRECTIONAL_MISMATCH", codes)
        self.assertIn("ANCHOR_COMPONENT_BIDIRECTIONAL_MISMATCH", codes)

    def test_stage_target_receipt_vector_and_total_links_are_all_mandatory(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            stage_path = target / "stagecourt_receipt.json"
            stage = json.loads(stage_path.read_text(encoding="utf-8"))
            stage["target_id"] = "000660"
            stage["score_receipt_id"] = "V6RECEIPT-FOREIGN"
            stage["component_score_vector_hash"] = "0" * 64
            stage["total_score"] = 1.0
            self._write_json(stage_path, stage)
            self._reseal(target)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("TARGET_IDENTITY_LINKAGE_MISMATCH", codes)
        self.assertIn("RECEIPT_ID_LINKAGE_MISMATCH", codes)
        self.assertIn("STAGE_SCORE_VECTOR_HASH_MISMATCH", codes)
        self.assertIn("STAGE_TOTAL_SCORE_LINKAGE_MISMATCH", codes)

    def test_gold_hash_and_nonempty_accurate_recall_are_mandatory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            projection = score["gold_post_run_audit"]
            projection["metrics"]["critical_material_fact_recall"] = 0.0
            score["gold_post_run_metrics"] = dict(projection["metrics"])
            score["gold_receipt_projection_hash"] = stable_hash(projection)
            score["gold_audit_hash"] = "0" * 64
            self._write_json(score_path, score)
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["gold_receipt_projection_hash"] = stable_hash(projection)
            self._write_json(manifest_path, manifest)
            self._reseal(target)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("GOLD_AUDIT_HASH_LINKAGE_MISMATCH", codes)
        self.assertIn("GOLD_RECALL_METRIC_INVALID", codes)

    def test_general_absolute_paths_are_rejected_after_receipt_reseal(self) -> None:
        for path_value in (
            "/var/lib/e2r/reviewer",
            "D:/agent/cache/receipt",
            r"\\server\share\receipt",
            "~/private/receipt",
        ):
            with self.subTest(path_value=path_value), tempfile.TemporaryDirectory() as directory:
                target = self._fixture(Path(directory) / "receipts")
                path = target / "judge_decisions.jsonl"
                rows = [
                    json.loads(line)
                    for line in path.read_text(encoding="utf-8").splitlines()
                ]
                rows[0]["provider_call_id"] = path_value
                self._write_jsonl(path, rows)
                self._reseal(target)
                result = verify_target_receipt(target)
            self.assertIn(
                "ABSOLUTE_PATH_IDENTITY_PRESENT", self._failure_codes(result)
            )

    def test_exact_quote_hash_is_bound_to_literal_original_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "scoring_facts.jsonl"
            rows = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
            ]
            rows[0]["exact_quote"] = "different fabricated literal quote"
            self._write_jsonl(path, rows)
            self._reseal(target)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("FACT_EXACT_QUOTE_HASH_MISMATCH", codes)
        self.assertIn("FACT_QUOTE_EXCERPT_TEXT_MISMATCH", codes)

    def test_output_tree_match_flag_and_hash_equality_are_mandatory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["output_tree_hash_matches"] = False
            self._write_json(manifest_path, manifest)
            result = verify_target_receipt(target)
        self.assertIn(
            "OUTPUT_TREE_HASH_LINKAGE_MISMATCH", self._failure_codes(result)
        )

    def test_full_run_provider_accounting_cannot_hide_local_model_outside_fact_calls(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            score["fallback_model"] = "QWEN_LOCAL_MODEL"
            self._write_json(score_path, score)
            self._reseal(target)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("LOCAL_PROVIDER_MARKER_PRESENT_IN_CANONICAL_FILE", codes)

    def test_full_run_provider_audit_is_required_even_if_other_calls_are_clean(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "provider_calls.jsonl"
            rows = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
            ]
            rows = [
                row
                for row in rows
                if row["call_scope"] != "FULL_RESEARCH_INVOCATION_AUDIT"
            ]
            self._write_jsonl(path, rows)
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["receipt_provider_call_count"] = len(rows)
            manifest["provider_call_counts"] = {"COLLABORATION_CODEX": len(rows)}
            self._write_json(manifest_path, manifest)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "FULL_RUN_PROVIDER_AUDIT_RECEIPT_REQUIRED",
            self._failure_codes(result),
        )

    def test_file_uri_is_rejected_as_an_absolute_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            stage_path = target / "stagecourt_receipt.json"
            stage = json.loads(stage_path.read_text(encoding="utf-8"))
            stage["reviewer_identity"] = "file:///var/lib/e2r/reviewer.json"
            self._write_json(stage_path, stage)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "ABSOLUTE_PATH_IDENTITY_PRESENT", self._failure_codes(result)
        )

    def test_manifest_is_excluded_from_immutable_content_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            before = receipt_content_tree_hash(target)
            path = target / "receipt_manifest.json"
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["verification_commit_sha"] = "e" * 40
            self._write_json(path, manifest)
            after = receipt_content_tree_hash(target)
        self.assertEqual(before, after)

    def test_manifest_authority_hash_scopes_source_hash_and_commit_attestation_are_mandatory(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "receipt_manifest.json"
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["score_or_stage_authority"] = True
            manifest["commit_sha_hash_scope"] = "NONE"
            manifest["tracked_receipt_hash_scope"] = "NONE"
            manifest["source_corpus_hash"] = "0" * 64
            manifest["run_commit_sha"] = "not-a-commit"
            manifest["verification_commit_sha"] = "f" * 40
            self._write_json(path, manifest)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("MANIFEST_DIRECT_SCORE_OR_STAGE_AUTHORITY_PRESENT", codes)
        self.assertIn("COMMIT_SHA_HASH_SCOPE_MISMATCH", codes)
        self.assertIn("TRACKED_RECEIPT_HASH_SCOPE_MISMATCH", codes)
        self.assertIn("SOURCE_CORPUS_HASH_MISMATCH", codes)
        self.assertIn("COMMIT_SHA_ATTESTATION_MISMATCH", codes)

    def test_non_finite_numeric_values_are_rejected_before_score_comparison(
        self,
    ) -> None:
        for field, value in (
            ("final_points", float("nan")),
            ("support_points", float("inf")),
            ("counter_effect", float("-inf")),
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                target = self._fixture(Path(directory) / "receipts")
                path = target / "component_decisions.jsonl"
                rows = [
                    json.loads(line)
                    for line in path.read_text(encoding="utf-8").splitlines()
                ]
                rows[0][field] = value
                self._write_jsonl(path, rows)
                self._reseal(target)
                result = verify_target_receipt(target)
            self.assertIn(
                "NON_FINITE_NUMERIC_VALUE_PRESENT",
                self._failure_codes(result),
            )

    def test_offline_anchor_loading_never_falls_back_to_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory, patch(
            "e2r.research_brain.researcher_mode.current_researcher_mode."
            "compile_component_anchor_atlas_from_files"
        ) as compiler:
            with self.assertRaisesRegex(
                ValueError,
                "tracked historical anchor atlas is required",
            ):
                _historical_anchors(
                    repo_root=directory,
                    archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    allow_output_fallback=False,
                )
        compiler.assert_not_called()

    def test_absolute_runtime_identity_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "judge_decisions.jsonl"
            rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            rows[0]["provider_call_id"] = "/root/reviewer-a"
            self._write_jsonl(path, rows)
            result = verify_target_receipt(target)
        self.assertIn("ABSOLUTE_PATH_IDENTITY_PRESENT", self._failure_codes(result))

    def test_complete_cross_component_bundle_swap_cannot_be_resealed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            left_id, right_id = CANONICAL_COMPONENT_ORDER[:2]
            component_path = target / "component_decisions.jsonl"
            components = [
                json.loads(line)
                for line in component_path.read_text(encoding="utf-8").splitlines()
            ]
            left, right = dict(components[0]), dict(components[1])
            components[0] = {**right, "component_id": left_id}
            components[1] = {**left, "component_id": right_id}
            self._write_jsonl(component_path, components)
            for filename in ("judge_decisions.jsonl", "scoring_facts.jsonl"):
                path = target / filename
                rows = [
                    json.loads(line)
                    for line in path.read_text(encoding="utf-8").splitlines()
                ]
                for row in rows:
                    if filename.startswith("judge"):
                        if row["component_id"] == left_id:
                            row["component_id"] = right_id
                        elif row["component_id"] == right_id:
                            row["component_id"] = left_id
                    else:
                        row["component_ids"] = [
                            right_id
                            if value == left_id
                            else left_id
                            if value == right_id
                            else value
                            for value in row["component_ids"]
                        ]
                self._write_jsonl(path, rows)
            anchor_path = target / "anchor_manifest.jsonl"
            anchors = [
                json.loads(line)
                for line in anchor_path.read_text(encoding="utf-8").splitlines()
            ]
            for anchor in anchors:
                component_id = anchor["component_id"]
                if component_id not in {left_id, right_id}:
                    continue
                swapped = right_id if component_id == left_id else left_id
                anchor["component_id"] = swapped
                anchor["normalized_anchor_payload"]["component_id"] = swapped
                anchor["anchor_payload_hash"] = stable_hash(
                    anchor["normalized_anchor_payload"]
                )
            self._write_jsonl(anchor_path, anchors)
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            score["component_max_vector"][left_id], score["component_max_vector"][
                right_id
            ] = (
                score["component_max_vector"][right_id],
                score["component_max_vector"][left_id],
            )
            self._write_json(score_path, score)
            self._reseal(target)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("ANCHOR_NOT_BOUND_TO_CURRENT_TRACKED_CONFIG", codes)
        self.assertIn("COMPONENT_MAX_NOT_BOUND_TO_CURRENT_ANCHOR_CONFIG", codes)
        self.assertIn("MANIFEST_JUDGE_PROMPT_BINDING_MISMATCH", codes)

    def test_fact_target_as_of_and_issuer_scope_are_immutable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "scoring_facts.jsonl"
            rows = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
            ]
            rows[0]["target_id"] = "000660"
            rows[0]["subject_id"] = "000660"
            rows[0]["as_of_date"] = "2026-07-11"
            rows[0]["issuer_scoped"] = False
            self._write_jsonl(path, rows)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "SCORING_FACT_TARGET_SCOPE_MISMATCH", self._failure_codes(result)
        )

    def test_judge_prompt_and_response_hashes_bind_provider_call(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "judge_decisions.jsonl"
            rows = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
            ]
            rows[0]["prompt_hash"] = "a" * 64
            rows[0]["response_hash"] = "b" * 64
            self._write_jsonl(path, rows)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "JUDGE_PROVIDER_CALL_LINKAGE_MISMATCH", self._failure_codes(result)
        )

    def test_fact_prompt_and_response_hashes_bind_fact_extraction_call(self) -> None:
        for field, value in (
            ("provider_prompt_hash", "1" * 64),
            ("provider_response_hash", "2" * 64),
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                target = self._fixture(Path(directory) / "receipts")
                path = target / "scoring_facts.jsonl"
                facts = [
                    json.loads(line)
                    for line in path.read_text(encoding="utf-8").splitlines()
                ]
                facts[0][field] = value
                self._write_jsonl(path, facts)
                self._reseal(target)
                result = verify_target_receipt(target)
            self.assertIn(
                "FACT_EXTRACTION_PROVIDER_CALL_LINKAGE_MISMATCH",
                self._failure_codes(result),
            )

    def test_mechanism_scope_identity_blocks_product_relabelling(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "scoring_facts.jsonl"
            facts = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
            ]
            facts[0]["scope_product_family"] = "DRAM"
            scope_payload = {
                "primary_claim_id": facts[0]["primary_claim_id"],
                "allowed_component_ids": facts[0]["allowed_component_ids"],
                "scope_business_segment": facts[0]["scope_business_segment"],
                "scope_product_family": facts[0]["scope_product_family"],
                "scope_technology_family": facts[0]["scope_technology_family"],
                "scope_transaction_type": facts[0]["scope_transaction_type"],
                "scope_economic_mechanism": facts[0]["scope_economic_mechanism"],
                "scope_confidence": facts[0]["scope_confidence"],
            }
            facts[0]["claim_scope_hash"] = stable_hash(scope_payload)
            self._write_jsonl(path, facts)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "FACT_MECHANISM_SCOPE_IDENTITY_MISMATCH",
            self._failure_codes(result),
        )

    def test_full_claim_scope_is_bound_to_reviewed_fact_response(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "scoring_facts.jsonl"
            facts = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
            ]
            facts[0]["scope_confidence"] = 0.99
            scope_payload = {
                "primary_claim_id": facts[0]["primary_claim_id"],
                "allowed_component_ids": facts[0]["allowed_component_ids"],
                "scope_business_segment": facts[0]["scope_business_segment"],
                "scope_product_family": facts[0]["scope_product_family"],
                "scope_technology_family": facts[0]["scope_technology_family"],
                "scope_transaction_type": facts[0]["scope_transaction_type"],
                "scope_economic_mechanism": facts[0]["scope_economic_mechanism"],
                "scope_confidence": facts[0]["scope_confidence"],
            }
            facts[0]["claim_scope_hash"] = stable_hash(scope_payload)
            self._write_jsonl(path, facts)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "FACT_EXTRACTION_PROVIDER_CALL_LINKAGE_MISMATCH",
            self._failure_codes(result),
        )

    def test_fact_journal_identity_recomputes_prompt_and_response_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            fact_path = target / "scoring_facts.jsonl"
            facts = [
                json.loads(line)
                for line in fact_path.read_text(encoding="utf-8").splitlines()
            ]
            for fact in facts:
                fact["provider_prompt_hash"] = "FACTPROMPT-" + "1" * 24
                fact["provider_response_hash"] = "FACTRESP-" + "2" * 24
            self._write_jsonl(fact_path, facts)
            call_path = target / "provider_calls.jsonl"
            calls = [
                json.loads(line)
                for line in call_path.read_text(encoding="utf-8").splitlines()
            ]
            fact_call = next(
                row for row in calls if row["call_scope"] == "FACT_EXTRACTION"
            )
            fact_call["prompt_hash"] = "FACTPROMPT-" + "1" * 24
            fact_call["response_hash"] = "FACTRESP-" + "2" * 24
            fact_call["provider_call_id"] = _fact_journal_provider_call_id(
                fact_call
            )
            self._write_jsonl(call_path, calls)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "FACT_EXTRACTION_JOURNAL_IDENTITY_MISMATCH",
            self._failure_codes(result),
        )

    def test_fact_scope_and_call_attestation_cannot_be_jointly_resealed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            fact_path = target / "scoring_facts.jsonl"
            facts = [
                json.loads(line)
                for line in fact_path.read_text(encoding="utf-8").splitlines()
            ]
            old_attestation = _fact_scope_attestation_hash(facts[0])
            facts[0]["scope_confidence"] = 0.9
            scope_payload = {
                "primary_claim_id": facts[0]["primary_claim_id"],
                "allowed_component_ids": facts[0]["allowed_component_ids"],
                "scope_business_segment": facts[0]["scope_business_segment"],
                "scope_product_family": facts[0]["scope_product_family"],
                "scope_technology_family": facts[0]["scope_technology_family"],
                "scope_transaction_type": facts[0]["scope_transaction_type"],
                "scope_economic_mechanism": facts[0][
                    "scope_economic_mechanism"
                ],
                "scope_confidence": facts[0]["scope_confidence"],
            }
            facts[0]["claim_scope_hash"] = stable_hash(scope_payload)
            new_attestation = _fact_scope_attestation_hash(facts[0])
            self._write_jsonl(fact_path, facts)
            call_path = target / "provider_calls.jsonl"
            calls = [
                json.loads(line)
                for line in call_path.read_text(encoding="utf-8").splitlines()
            ]
            fact_call = next(
                row for row in calls if row["call_scope"] == "FACT_EXTRACTION"
            )
            fact_call["fact_scope_attestation_hashes"] = [
                new_attestation if value == old_attestation else value
                for value in fact_call["fact_scope_attestation_hashes"]
            ]
            fact_call["fact_scope_attestation_hashes"] = sorted(
                fact_call["fact_scope_attestation_hashes"]
            )
            fact_call["provider_call_id"] = _fact_journal_provider_call_id(
                fact_call
            )
            self._write_jsonl(call_path, calls)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "FACT_EXTRACTION_JOURNAL_IDENTITY_MISMATCH",
            self._failure_codes(result),
        )

    def test_risk_overlay_is_recomputed_from_stage_hard_break_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "score_receipt.json"
            score = json.loads(path.read_text(encoding="utf-8"))
            score["risk_overlay"] = "FABRICATED_RISK"
            self._write_json(path, score)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "RISK_OVERLAY_DETERMINISTIC_LINKAGE_MISMATCH",
            self._failure_codes(result),
        )

    def test_manifest_local_marker_ipv6_and_failed_full_run_are_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["fallback_model"] = "QWEN_LOCAL_MODEL"
            manifest["runtime_endpoint"] = "http://[::1]:11434"
            self._write_json(manifest_path, manifest)
            calls_path = target / "provider_calls.jsonl"
            calls = [
                json.loads(line)
                for line in calls_path.read_text(encoding="utf-8").splitlines()
            ]
            full_run = next(
                row
                for row in calls
                if row["call_scope"] == "FULL_RESEARCH_INVOCATION_AUDIT"
            )
            full_run["status"] = "FAIL"
            full_run["provider_error_count"] = 1
            self._write_jsonl(calls_path, calls)
            self._reseal(target)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("LOCAL_PROVIDER_MARKER_PRESENT_IN_RECEIPT_SET", codes)
        self.assertIn("FULL_RUN_PROVIDER_AUDIT_NOT_CLEAN_SUCCESS", codes)

    def test_truthy_local_provider_key_and_raw_ipv6_loopback_are_blocking(
        self,
    ) -> None:
        for field, value in (
            ("qwen_runtime_used", True),
            ("debug_endpoint", "::1:11434"),
            (
                "runtime_endpoint",
                "http://[0000:0000:0000:0000:0000:0000:0000:0001]:11434",
            ),
            ("runtime_endpoint", "http://[::ffff:7f00:1]:11434"),
            ("runtime_endpoint", "http://0x7f000001:11434"),
            ("runtime_endpoint", "http://0x7f.1:11434"),
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                target = self._fixture(Path(directory) / "receipts")
                manifest_path = target / "receipt_manifest.json"
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                manifest[field] = value
                self._write_json(manifest_path, manifest)
                self._reseal(target)
                result = verify_target_receipt(target)
            self.assertIn(
                "LOCAL_PROVIDER_MARKER_PRESENT_IN_RECEIPT_SET",
                self._failure_codes(result),
            )

    def test_gold_qualified_matches_cannot_exceed_gold_fact_count(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            projection = score["gold_post_run_audit"]
            projection["qualified_material_fact_match_count"] = 99
            score["gold_receipt_projection_hash"] = stable_hash(projection)
            self._write_json(score_path, score)
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["gold_receipt_projection_hash"] = stable_hash(projection)
            self._write_json(manifest_path, manifest)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "GOLD_QUALIFIED_MATCH_COUNT_EXCEEDS_GOLD_FACT_COUNT",
            self._failure_codes(result),
        )

    def test_quote_and_all_self_reported_hashes_still_bind_primary_claim(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            fact_path = target / "scoring_facts.jsonl"
            facts = [
                json.loads(line)
                for line in fact_path.read_text(encoding="utf-8").splitlines()
            ]
            fact = facts[0]
            quote = "fabricated replacement quote"
            quote_hash = hashlib.sha256(quote.encode("utf-8")).hexdigest()
            fact["exact_quote"] = quote
            fact["exact_quote_hash"] = quote_hash
            fact["quote_excerpt"] = quote
            fact["quote_excerpt_hash"] = quote_hash
            self._write_jsonl(fact_path, facts)
            source_path = target / "source_manifest.jsonl"
            sources = [
                json.loads(line)
                for line in source_path.read_text(encoding="utf-8").splitlines()
            ]
            sources[0]["fact_exact_quote_hashes"][fact["fact_id"]] = quote_hash
            self._write_jsonl(source_path, sources)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "FACT_PRIMARY_CLAIM_IDENTITY_MISMATCH", self._failure_codes(result)
        )

    def test_receipt_id_is_derived_from_target_date_and_output_hash(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            forged_id = "V6RECEIPT-FORGED"
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            score["receipt_id"] = forged_id
            self._write_json(score_path, score)
            stage_path = target / "stagecourt_receipt.json"
            stage = json.loads(stage_path.read_text(encoding="utf-8"))
            stage["score_receipt_id"] = forged_id
            self._write_json(stage_path, stage)
            manifest_path = target / "receipt_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["receipt_id"] = forged_id
            manifest["output_tree_hash"] = "f" * 64
            manifest["output_tree_hash_recomputed"] = "f" * 64
            self._write_json(manifest_path, manifest)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "RECEIPT_ID_IMMUTABLE_IDENTITY_MISMATCH",
            self._failure_codes(result),
        )

    def test_external_hardlink_receipt_leaf_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            target = self._fixture(base / "receipts")
            leaf = target / "scoring_facts.jsonl"
            outside = base / "untracked_scoring_facts.jsonl"
            outside.write_bytes(leaf.read_bytes())
            leaf.unlink()
            os.link(outside, leaf)
            result = verify_target_receipt(target)
        self.assertIn(
            "EXACT_REGULAR_TARGET_RECEIPT_FILE_ROSTER_REQUIRED",
            self._failure_codes(result),
        )

    def test_ipv4_shorthand_loopback_is_blocked_but_uppercase_https_is_portable(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            score["review_url"] = "http://127.1:11434"
            self._write_json(score_path, score)
            self._reseal(target)
            blocked = verify_target_receipt(target)
        self.assertIn(
            "LOCAL_PROVIDER_MARKER_PRESENT_IN_RECEIPT_SET",
            self._failure_codes(blocked),
        )
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            source_path = target / "source_manifest.jsonl"
            sources = [
                json.loads(line)
                for line in source_path.read_text(encoding="utf-8").splitlines()
            ]
            sources[0]["source_url"] = "HTTPS://example.com/report.pdf"
            self._write_jsonl(source_path, sources)
            self._reseal(target)
            portable = verify_target_receipt(target)
        self.assertNotIn(
            "ABSOLUTE_PATH_IDENTITY_PRESENT",
            self._failure_codes(portable),
        )

    def test_unknown_provider_backend_field_is_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            score["provider_backend"] = "ANTHROPIC"
            self._write_json(score_path, score)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "CANONICAL_RECEIPT_FIELD_ROSTER_MISMATCH",
            self._failure_codes(result),
        )

    def test_fact_economic_identity_and_claim_scope_are_immutable(self) -> None:
        for field, value, expected_code in (
            ("value", "fabricated", "FACT_ECONOMIC_IDENTITY_MISMATCH"),
            (
                "economic_mechanism",
                "fabricated mechanism",
                "FACT_ECONOMIC_IDENTITY_MISMATCH",
            ),
            ("scope_product_family", "DRAM", "FACT_CLAIM_SCOPE_HASH_MISMATCH"),
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                target = self._fixture(Path(directory) / "receipts")
                path = target / "scoring_facts.jsonl"
                facts = [
                    json.loads(line)
                    for line in path.read_text(encoding="utf-8").splitlines()
                ]
                facts[0][field] = value
                self._write_jsonl(path, facts)
                self._reseal(target)
                result = verify_target_receipt(target)
            self.assertIn(expected_code, self._failure_codes(result))

    def test_commit_attestation_must_name_a_real_ancestor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "receipt_manifest.json"
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["run_commit_sha"] = "e" * 40
            manifest["verification_commit_sha"] = "e" * 40
            self._write_json(path, manifest)
            result = verify_target_receipt(target)
        self.assertIn(
            "COMMIT_SHA_NOT_TRUSTED_GIT_ANCESTOR",
            self._failure_codes(result),
        )

    def test_fact_primary_role_directness_source_and_risk_links_are_exact(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            fact_path = target / "scoring_facts.jsonl"
            facts = [
                json.loads(line)
                for line in fact_path.read_text(encoding="utf-8").splitlines()
            ]
            facts[0]["fact_role"] = "RESOLUTION"
            facts[0]["direct_point_input"] = False
            facts[0]["source_tier"] = "SOCIAL_BLOG"
            self._write_jsonl(fact_path, facts)
            score_path = target / "score_receipt.json"
            score = json.loads(score_path.read_text(encoding="utf-8"))
            score["hard_break_fact_ids"] = ["FACT-NOT-EXISTS"]
            self._write_json(score_path, score)
            stage_path = target / "stagecourt_receipt.json"
            stage = json.loads(stage_path.read_text(encoding="utf-8"))
            stage["risk_fact_ids"] = ["FACT-NOT-EXISTS"]
            stage["hard_break_claim_ids"] = ["RFC-NOT-EXISTS"]
            self._write_json(stage_path, stage)
            self._reseal(target)
            result = verify_target_receipt(target)
        codes = self._failure_codes(result)
        self.assertIn("SCORING_FACT_PRIMARY_ROLE_MISMATCH", codes)
        self.assertIn("FACT_SOURCE_METADATA_LINKAGE_MISMATCH", codes)
        self.assertIn("RISK_OR_HARD_BREAK_FACT_LINKAGE_MISMATCH", codes)
        self.assertIn("HARD_BREAK_CLAIM_LINKAGE_MISMATCH", codes)

    def test_inverted_judge_ranges_cannot_close_a_component(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            judge_path = target / "judge_decisions.jsonl"
            judges = [
                json.loads(line)
                for line in judge_path.read_text(encoding="utf-8").splitlines()
            ]
            first_component = CANONICAL_COMPONENT_ORDER[0]
            for judge in judges:
                if judge["component_id"] == first_component:
                    judge["allowed_range"] = [1.0, 0.0]
            self._write_jsonl(judge_path, judges)
            component_path = target / "component_decisions.jsonl"
            components = [
                json.loads(line)
                for line in component_path.read_text(encoding="utf-8").splitlines()
            ]
            components[0]["consensus_band"] = [1.0, 0.0]
            self._write_jsonl(component_path, components)
            self._reseal(target)
            result = verify_target_receipt(target)
        self.assertIn(
            "JUDGE_ALLOWED_RANGE_CONTRACT_MISMATCH",
            self._failure_codes(result),
        )


if __name__ == "__main__":
    unittest.main()
