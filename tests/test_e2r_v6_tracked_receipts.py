from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from e2r.production.metadata import stable_hash
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER
from e2r.research_brain.researcher_mode.tracked_receipts import (
    PROVIDER_ROUTE,
    RECEIPT_MANIFEST_SCHEMA,
    SCORE_RECEIPT_SCHEMA,
    STAGECOURT_RECEIPT_SCHEMA,
    VERIFICATION_FAIL,
    VERIFICATION_PASS,
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
        "eps_fcf_explosion": 20.0,
        "earnings_visibility": 20.0,
        "bottleneck_pricing": 20.0,
        "market_mispricing": 15.0,
        "valuation_rerating": 15.0,
        "capital_allocation": 5.0,
        "information_confidence": 5.0,
    }

    def _write_json(self, path: Path, payload: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
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

    def _fixture(self, base: Path, *, target_id: str = "TEST001") -> Path:
        target = base / target_id
        components: list[dict[str, object]] = []
        judges: list[dict[str, object]] = []
        facts: list[dict[str, object]] = []
        sources: list[dict[str, object]] = []
        anchors: list[dict[str, object]] = []
        for component_index, component_id in enumerate(CANONICAL_COMPONENT_ORDER):
            fact_id = f"FACT-{component_index}"
            source_id = f"SOURCE-{component_index}"
            anchor_id = f"ANCHOR-{component_index}"
            quote = f"{component_id} current source-backed fact"
            quote_hash = hashlib.sha256(quote.encode("utf-8")).hexdigest()
            document_hash = hashlib.sha256(source_id.encode("utf-8")).hexdigest()
            judge_ids = [f"JUDGE-{component_index}-{role}" for role in ("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE")]
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
                    "prompt_hashes": ["1" * 64, "2" * 64, "3" * 64],
                    "response_hashes": ["4" * 64, "5" * 64, "6" * 64],
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
                        "prompt_hash": hashlib.sha256(judge_id.encode()).hexdigest(),
                        "response_hash": hashlib.sha256((judge_id + "response").encode()).hexdigest(),
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
                    "business_segment": "TEST",
                    "product_family": "TEST",
                    "economic_mechanism": "test mechanism",
                    "predicate_family": "TEST_PREDICATE",
                    "normalized_object": "test",
                    "value": "test",
                    "unit": "none",
                    "period": "2026",
                    "temporal_status": "CURRENT",
                    "claim_ids": [f"CLAIM-{component_index}"],
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
                    "provider_prompt_hash": "8" * 64,
                    "provider_response_hash": "9" * 64,
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
            anchor_payload = {
                "anchor_id": anchor_id,
                "component_id": component_id,
                "archetype_id": "TEST_ARCHETYPE",
                "points_lower": 0.0,
                "points_mid": 0.0,
                "points_upper": 0.0,
                "max_points": self.MAXIMA[component_id],
            }
            anchors.append(
                {
                    "schema_version": "e2r_v6_anchor_manifest_row_v1",
                    "anchor_id": anchor_id,
                    "component_id": component_id,
                    "archetype_id": "TEST_ARCHETYPE",
                    "normalized_anchor_payload": anchor_payload,
                    "anchor_payload_hash": stable_hash(anchor_payload),
                }
            )

        score = {
            "schema_version": SCORE_RECEIPT_SCHEMA,
            "receipt_id": "V6RECEIPT-TEST",
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
            "gold_post_run_metrics": {
                "all_material_fact_recall": 1.0,
                "critical_material_fact_recall": 1.0,
            },
            "gold_leakage_count": 0,
        }
        stage = {
            "schema_version": STAGECOURT_RECEIPT_SCHEMA,
            "target_id": target_id,
            "score_receipt_id": "V6RECEIPT-TEST",
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
        self._write_json(target / "score_receipt.json", score)
        self._write_jsonl(target / "component_decisions.jsonl", components)
        self._write_jsonl(target / "scoring_facts.jsonl", facts)
        self._write_jsonl(target / "judge_decisions.jsonl", judges)
        self._write_jsonl(target / "source_manifest.jsonl", sources)
        self._write_jsonl(target / "anchor_manifest.jsonl", anchors)
        self._write_jsonl(target / "provider_calls.jsonl", [])
        self._write_json(target / "stagecourt_receipt.json", stage)
        manifest = {
            "schema_version": RECEIPT_MANIFEST_SCHEMA,
            "receipt_id": "V6RECEIPT-TEST",
            "target_id": target_id,
            "company_name": "테스트회사",
            "as_of_date": "2026-07-12",
            "latest_trading_snapshot_date": "2026-07-10",
            "archetype_id": "TEST_ARCHETYPE",
            "run_commit_sha": "b" * 40,
            "verification_commit_sha": "b" * 40,
            "config_hash": runtime_config_hash(),
            "prompt_hashes": {},
            "provider_identity_hash": "c" * 64,
            "source_corpus_hash": stable_hash(sources),
            "output_tree_hash": "d" * 64,
            "tracked_receipt_tree_hash": receipt_content_tree_hash(target),
            "tracked_receipt_content_index": list(receipt_content_index(target)),
            "tracked_receipt_hash_scope": "ALL_TARGET_RECEIPT_FILES_EXCEPT_RECEIPT_MANIFEST_JSON",
            "gold_visible_during_production": False,
            "provider_selected_explicitly": True,
            "provider_route": PROVIDER_ROUTE,
            "qwen_call_count": 0,
            "ollama_call_count": 0,
            "provider_call_counts": {},
            "scored_fact_provider_lineage_counts": {"COLLABORATION_CODEX": 7},
            "inherited_qwen_scored_fact_count": 0,
            "inherited_ollama_scored_fact_count": 0,
            "current_invocation_provider_name": "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE",
            "score_or_stage_authority": False,
        }
        self._write_json(target / "receipt_manifest.json", manifest)
        return target

    def _failure_codes(self, result: dict[str, object]) -> set[str]:
        return {str(row["code"]) for row in result["failures"]}  # type: ignore[index]

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
            self._fixture(root, target_id="A")
            self._fixture(root, target_id="B")
            result = verify_receipts(root)
        self.assertEqual(result["status"], VERIFICATION_PASS)
        self.assertEqual(result["target_count"], 2)

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

    def test_absolute_runtime_identity_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = self._fixture(Path(directory) / "receipts")
            path = target / "judge_decisions.jsonl"
            rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            rows[0]["provider_call_id"] = "/root/reviewer-a"
            self._write_jsonl(path, rows)
            result = verify_target_receipt(target)
        self.assertIn("ABSOLUTE_PATH_IDENTITY_PRESENT", self._failure_codes(result))


if __name__ == "__main__":
    unittest.main()
