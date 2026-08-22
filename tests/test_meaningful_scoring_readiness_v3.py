from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.scoring.scoring_readiness import (
    MEANINGFUL_READY_V2,
    NOT_READY,
    SCORING_READINESS_SCHEMA_VERSION,
    V3_REQUIRED_CRITICAL_SOURCES,
    compile_meaningful_scoring_readiness,
)


COMPONENTS = (
    "eps_fcf_explosion",
    "earnings_visibility",
    "bottleneck_pricing",
    "market_mispricing",
    "valuation_rerating",
    "capital_allocation",
    "information_confidence",
)


class MeaningfulScoringReadinessV3Tests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_v3_pass_is_the_only_path_to_exact_final_label(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            config_path = self._write_bundle(Path(tmp))
            verdict = compile_meaningful_scoring_readiness(
                config_path=config_path
            )
        self.assertEqual(verdict["schema_version"], SCORING_READINESS_SCHEMA_VERSION)
        self.assertEqual(verdict["status"], MEANINGFUL_READY_V2)
        self.assertEqual(verdict["exact_final_verdict"], MEANINGFUL_READY_V2)
        self.assertEqual(verdict["critical_count_sum"], 0)
        self.assertEqual(
            set(verdict["semantic_critical_counts"]),
            set(V3_REQUIRED_CRITICAL_SOURCES),
        )
        self.assertEqual(verdict["semantic_critical_count_sum"], 0)
        self.assertFalse(verdict["legacy_ready_alias_active"])
        self.assertTrue(verdict["legacy_ready_alias_allowed"])

    def test_each_required_semantic_counter_blocks_report_only_pass(self) -> None:
        for critical_name, (audit_id, source_name) in (
            V3_REQUIRED_CRITICAL_SOURCES.items()
        ):
            with self.subTest(critical_name=critical_name):
                with tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    config_path = self._write_bundle(root)
                    audit_path = root / "audits" / f"{audit_id}.json"
                    audit = json.loads(audit_path.read_text(encoding="utf-8"))
                    audit["critical_counts"][source_name] = 1
                    # Summary counter를 거짓 PASS로 둬도 leaf counter가 막아야 한다.
                    audit["critical_count_sum"] = 0
                    audit_path.write_text(
                        json.dumps(audit), encoding="utf-8"
                    )
                    verdict = compile_meaningful_scoring_readiness(
                        config_path=config_path
                    )
                self.assertEqual(verdict["status"], NOT_READY)
                self.assertGreater(
                    verdict["semantic_critical_counts"][critical_name], 0
                )

    def test_operational_v3_is_ready_after_all_semantic_gates_exist(self) -> None:
        verdict = compile_meaningful_scoring_readiness(
            config_path=self.ROOT
            / "configs/e2r_meaningful_scoring_readiness_v3.json"
        )
        text = (
            self.ROOT
            / "docs/operational/e2r_meaningful_scoring_readiness_v3.md"
        ).read_text(encoding="utf-8")
        if verdict["status"] != MEANINGFUL_READY_V2:
            # Raw dossier leaves live under intentionally excluded output/**.
            # The clean checkout must fail closed; the tracked markdown is a
            # historical receipt rather than a current raw recomputation.
            self.assertEqual(verdict["status"], NOT_READY)
            self.assertFalse(verdict["hard_acceptance_pass"])
            self.assertGreater(verdict["critical_count_sum"], 0)
            self.assertTrue(verdict["blockers"])
            self.assertTrue(
                any(
                    "required_dossier_leaf_missing_count" in blocker
                    for blocker in verdict["blockers"]
                )
            )
            self.assertIn("MEANINGFUL_E2R_SCORING_READY_V2", text)
            return
        self.assertTrue(verdict["hard_acceptance_pass"])
        self.assertEqual(verdict["blockers"], [])
        self.assertEqual(verdict["critical_count_sum"], 0)
        self.assertIn("MEANINGFUL_E2R_SCORING_READY_V2", text)
        self.assertIn(
            "pass-only final label: MEANINGFUL_E2R_SCORING_READY_V2",
            text,
        )
        for critical_name in V3_REQUIRED_CRITICAL_SOURCES:
            self.assertIn(f"- {critical_name}:", text)

    def test_missing_or_negative_semantic_counter_is_fail_closed(self) -> None:
        audit_id, source_name = V3_REQUIRED_CRITICAL_SOURCES[
            "silent_zero_default_count"
        ]
        for mutation in ("missing", "negative"):
            with self.subTest(mutation=mutation):
                with tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    config_path = self._write_bundle(root)
                    audit_path = root / "audits" / f"{audit_id}.json"
                    audit = json.loads(audit_path.read_text(encoding="utf-8"))
                    if mutation == "missing":
                        audit["critical_counts"].pop(source_name)
                    else:
                        audit["critical_counts"][source_name] = -1
                    audit_path.write_text(json.dumps(audit), encoding="utf-8")
                    verdict = compile_meaningful_scoring_readiness(
                        config_path=config_path
                    )
                self.assertEqual(verdict["status"], NOT_READY)
                self.assertGreater(
                    verdict["semantic_critical_counts"][
                        "silent_zero_default_count"
                    ],
                    0,
                )

    def _write_bundle(self, root: Path) -> Path:
        dossier = root / "dossier"
        audits = root / "audits"
        dossier.mkdir(parents=True)
        audits.mkdir(parents=True)
        self._write_dossier(dossier)
        required_audits = {
            "live_materialization",
            *(
                audit_id
                for audit_id, _ in V3_REQUIRED_CRITICAL_SOURCES.values()
            ),
        }
        audit_configs = []
        for audit_id in sorted(required_audits):
            source_counts = {
                source_name: 0
                for _, (source_audit_id, source_name) in (
                    V3_REQUIRED_CRITICAL_SOURCES.items()
                )
                if source_audit_id == audit_id
            }
            path = audits / f"{audit_id}.json"
            path.write_text(
                json.dumps(
                    {
                        "schema_version": f"test-{audit_id}",
                        "status": "PASS",
                        "critical_counts": source_counts,
                        "critical_count_sum": 0,
                    }
                ),
                encoding="utf-8",
            )
            audit_configs.append(
                {
                    "audit_id": audit_id,
                    "path": str(path),
                    "accepted_statuses": ["PASS"],
                }
            )
        config = {
            "schema_version": SCORING_READINESS_SCHEMA_VERSION,
            "as_of_date": "2026-07-11",
            "required_component_ids": list(COMPONENTS),
            "mandatory_targets": [
                {
                    "target_id": "TARGET-V3",
                    "company_name": "임의회사",
                    "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "expected_profile_id": "e2r_2_2_archetype_weight_runtime",
                    "dossier_root": str(dossier),
                }
            ],
            "required_global_audits": audit_configs,
        }
        config_path = root / "readiness_v3.json"
        config_path.write_text(json.dumps(config), encoding="utf-8")
        return config_path

    def _write_dossier(self, root: Path) -> None:
        claim_id = "CLM-V3"
        impact_id = "IMPACT-V3"
        eligibility_id = "ELIG-V3"
        decision_id = "DEC-V3"
        trace_id = "TRACE-V3"
        validity_id = "FSVALID-V3"
        assessment_ids = [f"ASM-V3-{index}" for index in range(7)]
        self._jsonl(
            root / "accepted_current_claims.jsonl",
            [
                {
                    "claim_id": claim_id,
                    "evidence_origin": "ORGANIC_LIVE",
                    "fetched": True,
                    "source_proxy_only": False,
                    "published_date": "2026-07-10",
                }
            ],
        )
        self._jsonl(
            root / "claim_impacts_validated.jsonl",
            [
                {
                    "impact_id": impact_id,
                    "claim_id": claim_id,
                    "component_id": COMPONENTS[0],
                    "direction": "SUPPORT",
                    "validated_credit_fraction": 0.5,
                    "fact_cluster_id": "FACT-V3",
                    "document_cluster_id": "DOC-CLUSTER-V3",
                    "eligibility_decision_id": eligibility_id,
                    "corroboration_only": False,
                    "scope_validation": {"scope_match": True},
                }
            ],
        )
        self._jsonl(
            root / "component_assessments.jsonl",
            [
                {
                    "assessment_id": assessment_id,
                    "component_id": component_id,
                    "status": (
                        "VERIFIED_PARTIAL_SUPPORT"
                        if index == 0
                        else "NOT_APPLICABLE"
                    ),
                }
                for index, (assessment_id, component_id) in enumerate(
                    zip(assessment_ids, COMPONENTS)
                )
            ],
        )
        score = {
            "profile_id": "e2r_2_2_archetype_weight_runtime",
            "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "contract_hash": "a" * 64,
            "component_score_vector": {
                component_id: 1.0 if index == 0 else 0.0
                for index, component_id in enumerate(COMPONENTS)
            },
            "verified_supported_score": 1.0,
            "full_e2r_score": 1.0,
            "full_score_valid": True,
            "score_type": "FULL_E2R_100",
            "audit": {
                "full_score_validity": {"validity_id": validity_id}
            },
        }
        (root / "component_score_vector.json").write_text(
            json.dumps(score), encoding="utf-8"
        )
        decision = {
            "decision_id": decision_id,
            "target_id": "TARGET-V3",
            "as_of_date": "2026-07-11",
            "trace_id": trace_id,
            "accepted_claim_ids": [claim_id],
            "claim_impact_ids": [impact_id],
            "component_assessment_ids": assessment_ids,
            "full_score_valid": True,
            "score_type": "FULL_E2R_100",
            "canonical_stage": "0",
            "full_thesis_stage": "0",
            "decision_status": "FINAL",
            "event_overlay": {"canonical_stage_effect": "NONE"},
            "stage_reason": [],
        }
        (root / "atomic_stage_decision.json").write_text(
            json.dumps(decision), encoding="utf-8"
        )
        (root / "stagecourt_trace.json").write_text(
            json.dumps(
                {
                    "trace_id": trace_id,
                    "decision_id": decision_id,
                    "target_id": "TARGET-V3",
                }
            ),
            encoding="utf-8",
        )
        self._jsonl(
            root / "claim_eligibility_decisions.jsonl",
            [
                {
                    "eligibility_decision_id": eligibility_id,
                    "claim_id": claim_id,
                    "component_scoring_eligibility": True,
                }
            ],
        )
        self._jsonl(
            root / "question_component_reconciliation.jsonl",
            [
                {
                    "reconciliation_id": "RECON-V3",
                    "question_family_id": "question-v3",
                    "input_closure_status": "SUPPORTED_SCORING",
                    "reconciled_closure_status": "SUPPORTED_SCORING",
                    "positive_scoring_claim_ids": [claim_id],
                    "provider_failure": False,
                    "component_links": [
                        {
                            "claim_id": claim_id,
                            "impact_id": impact_id,
                            "component_id": COMPONENTS[0],
                        }
                    ],
                }
            ],
        )
        self._jsonl(root / "evidence_search_adequacy.jsonl", [])
        self._jsonl(
            root / "economic_fact_clusters.jsonl",
            [{"fact_cluster_id": "FACT-V3"}],
        )
        self._jsonl(
            root / "document_clusters.jsonl",
            [{"document_cluster_id": "DOC-CLUSTER-V3"}],
        )
        zero_impact_counts = {
            "positive_impact_zeroed_by_missing_cap_count": 0,
            "counter_impact_zeroed_by_missing_cap_count": 0,
            "same_fact_duplicate_credit_count": 0,
            "same_document_duplicate_credit_count": 0,
        }
        self._json(
            root / "impact_validation_audit.json",
            {"critical_counts": zero_impact_counts, "critical_count_sum": 0},
        )
        self._json(
            root / "component_assessment_audit.json",
            {
                "critical_counts": {"counter_impact_ignored_count": 0},
                "critical_count_sum": 0,
            },
        )
        self._json(
            root / "question_component_reconciliation_audit.json",
            {
                "critical_counts": {
                    "supported_question_absent_component_count": 0,
                    "positive_claim_absent_component_count": 0,
                    "absence_with_inadequate_search_count": 0,
                },
                "critical_count_sum": 0,
            },
        )
        self._json(
            root / "scoring_schema_totality_audit.json",
            {
                "critical_counts": {
                    "missing_scoring_key_count": 0,
                    "silent_zero_default_count": 0,
                },
                "critical_count_sum": 0,
            },
        )
        self._json(
            root / "full_score_validity_v2.json",
            {
                "validity_id": validity_id,
                "status": "FULL_SCORE_VALIDITY_V2_PASS",
                "full_score_valid": True,
                "critical_count_sum": 0,
            },
        )

    @staticmethod
    def _jsonl(path: Path, rows) -> None:
        path.write_text(
            "".join(json.dumps(row) + "\n" for row in rows),
            encoding="utf-8",
        )

    @staticmethod
    def _json(path: Path, payload) -> None:
        path.write_text(json.dumps(payload), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
