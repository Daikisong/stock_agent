from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.scoring.scoring_readiness import (
    NOT_READY,
    READY,
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


class FinalReadinessRequiresValidScoreTests(unittest.TestCase):
    def test_missing_dossiers_are_explicit_not_ready(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audit = root / "audit.json"
            audit.write_text(json.dumps({"status":"PASS","critical_count_sum":0}))
            config = {
                "schema_version":"e2r_meaningful_scoring_readiness_v2",
                "as_of_date":"2026-07-11",
                "required_component_ids":list(COMPONENTS),
                "mandatory_targets":[
                    {"target_id":target_id,"company_name":target_id,"archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","dossier_root":str(root/target_id)}
                    for target_id in ("005930","000660")
                ],
                "required_global_audits":[{"audit_id":"live_materialization","path":str(audit),"accepted_statuses":["PASS"]}],
            }
            config_path=root/"config.json"
            config_path.write_text(json.dumps(config))
            verdict = compile_meaningful_scoring_readiness(config_path=config_path)
            self.assertEqual(verdict["status"], NOT_READY)
            self.assertGreater(verdict["critical_count_sum"], 0)
            self.assertEqual(verdict["counts"]["organic_accepted_claim_count"], 0)
            self.assertEqual(verdict["counts"]["full_score_valid_canary_count"], 0)

    def test_organic_claim_without_validated_impact_cannot_pass(self) -> None:
        verdict = self._compile(impact=False, full_score=True)
        self.assertEqual(verdict["status"], NOT_READY)
        self.assertEqual(verdict["counts"]["organic_accepted_claim_count"], 2)
        self.assertEqual(verdict["counts"]["organic_validated_impact_count"], 0)

    def test_no_score_decision_cannot_pass_even_with_organic_claim(self) -> None:
        verdict = self._compile(impact=True, full_score=False)
        self.assertEqual(verdict["status"], NOT_READY)
        self.assertEqual(verdict["counts"]["no_score_only_target_count"], 2)
        self.assertGreater(
            verdict["target_results"][0]["critical_counts"]["full_score_invalid"], 0
        )

    def test_complete_leaf_chain_is_the_only_ready_shape(self) -> None:
        verdict = self._compile(impact=True, full_score=True)
        self.assertEqual(verdict["status"], READY)
        self.assertEqual(verdict["critical_count_sum"], 0)
        self.assertEqual(verdict["counts"]["full_score_valid_canary_count"], 2)
        self.assertTrue(
            verdict["intermediate_labels"]["C06_CANONICAL_LIVE_CUTOVER_PASS"]
        )

    def _compile(self, *, impact: bool, full_score: bool):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for target_id in ("005930", "000660"):
                self._write_dossier(
                    root / target_id, target_id, impact=impact, full_score=full_score
                )
            audit = root / "audit.json"
            audit.write_text(
                json.dumps({"status": "PASS", "critical_count_sum": 0}),
                encoding="utf-8",
            )
            config = {
                "schema_version": "e2r_meaningful_scoring_readiness_v2",
                "as_of_date": "2026-07-11",
                "required_component_ids": list(COMPONENTS),
                "mandatory_targets": [
                    {
                        "target_id": target_id,
                        "company_name": target_id,
                        "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "expected_profile_id": "e2r_2_2_archetype_weight_runtime",
                        "success_label": f"TARGET_{target_id}_PASS",
                        "dossier_root": str(root / target_id),
                    }
                    for target_id in ("005930", "000660")
                ],
                "required_global_audits": [
                    {
                        "audit_id": "live_materialization",
                        "path": str(audit),
                        "accepted_statuses": ["PASS"],
                    }
                ],
            }
            config_path = root / "config.json"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            return compile_meaningful_scoring_readiness(config_path=config_path)

    def _write_dossier(
        self, root: Path, target_id: str, *, impact: bool, full_score: bool
    ) -> None:
        root.mkdir(parents=True)
        claim_id = f"CLM-{target_id}"
        impact_id = f"IMP-{target_id}"
        decision_id = f"DEC-{target_id}"
        trace_id = f"TRACE-{target_id}"
        assessment_ids = [f"ASM-{target_id}-{index}" for index in range(len(COMPONENTS))]
        (root / "accepted_current_claims.jsonl").write_text(
            json.dumps(
                {
                    "claim_id": claim_id,
                    "evidence_origin": "ORGANIC_LIVE",
                    "fetched": True,
                    "source_proxy_only": False,
                    "source_url": "https://issuer.example/official",
                    "published_date": "2026-07-10",
                }
            )
            + "\n",
            encoding="utf-8",
        )
        impact_rows = (
            [{"impact_id": impact_id, "claim_id": claim_id, "validated_credit_fraction": 0.5}]
            if impact
            else []
        )
        (root / "claim_impacts_validated.jsonl").write_text(
            "".join(json.dumps(row) + "\n" for row in impact_rows), encoding="utf-8"
        )
        assessments = [
            {
                "assessment_id": assessment_id,
                "component_id": component,
                "status": "VERIFIED_ABSENT_AFTER_SEARCH" if index else "VERIFIED_PARTIAL_SUPPORT",
            }
            for index, (assessment_id, component) in enumerate(
                zip(assessment_ids, COMPONENTS)
            )
        ]
        (root / "component_assessments.jsonl").write_text(
            "".join(json.dumps(row) + "\n" for row in assessments),
            encoding="utf-8",
        )
        score_type = "FULL_E2R_100" if full_score else "NO_SCORE"
        score = {
            "profile_id": "e2r_2_2_archetype_weight_runtime",
            "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "contract_hash": "a" * 64,
            "component_score_vector": {
                component: 1.0 if index == 0 else 0.0
                for index, component in enumerate(COMPONENTS)
            },
            "verified_supported_score": 1.0,
            "full_e2r_score": 1.0 if full_score else None,
            "full_score_valid": full_score,
            "score_type": score_type,
        }
        (root / "component_score_vector.json").write_text(
            json.dumps(score), encoding="utf-8"
        )
        decision = {
            "decision_id": decision_id,
            "target_id": target_id,
            "as_of_date": "2026-07-11",
            "trace_id": trace_id,
            "accepted_claim_ids": [claim_id],
            "claim_impact_ids": [impact_id] if impact else [],
            "component_assessment_ids": assessment_ids,
            "full_score_valid": full_score,
            "score_type": score_type,
            "canonical_stage": "0",
            "decision_status": "FINAL" if full_score else "PENDING_MATERIAL_COMPONENTS",
        }
        (root / "atomic_stage_decision.json").write_text(
            json.dumps(decision), encoding="utf-8"
        )
        (root / "stagecourt_trace.json").write_text(
            json.dumps(
                {"trace_id": trace_id, "decision_id": decision_id, "target_id": target_id}
            ),
            encoding="utf-8",
        )


if __name__ == "__main__":
    unittest.main()
