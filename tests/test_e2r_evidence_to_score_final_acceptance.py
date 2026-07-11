from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.scoring_readiness import (
    READY,
    compile_meaningful_scoring_readiness,
)


class E2REvidenceToScoreFinalAcceptanceTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_all_mandatory_operational_artifacts_exist(self) -> None:
        required = (
            "e2r_evidence_to_score_forensic_baseline.md",
            "e2r_canonical_scoring_contract_audit.json",
            "e2r_evidence_impact_rubric_audit.json",
            "e2r_claim_impact_ledger_audit.json",
            "e2r_component_assessment_audit.json",
            "e2r_research_calibrated_score_audit.json",
            "e2r_acceptance_probe_separation_audit.json",
            "e2r_c06_historical_component_replay.json",
            "e2r_samsung_full_thesis_acceptance.md",
            "e2r_sk_hynix_full_thesis_acceptance.md",
            "e2r_c06_live_cutover_acceptance.md",
            "e2r_evidence_to_score_self_repair_summary.md",
            "e2r_meaningful_scoring_readiness_verdict.md",
        )
        docs = self.ROOT / "docs/operational"
        self.assertEqual([name for name in required if not (docs / name).is_file()], [])

    def test_final_readiness_requires_every_goal_audit(self) -> None:
        verdict = compile_meaningful_scoring_readiness(
            config_path=self.ROOT / "configs/e2r_meaningful_scoring_readiness_v2.json"
        )
        self.assertEqual(verdict["status"], READY)
        self.assertEqual(verdict["critical_count_sum"], 0)
        self.assertEqual(verdict["blockers"], [])
        audit_ids = {row["audit_id"] for row in verdict["global_audits"]}
        self.assertTrue(
            {
                "evidence_impact_rubric",
                "claim_impact_ledger",
                "component_assessment",
                "research_calibrated_score",
                "c06_historical_component_replay",
                "evidence_to_score_generalization",
                "evidence_to_score_known_bad",
                "evidence_to_score_reviewer_gate",
            }
            <= audit_ids
        )

    def test_cutover_and_self_repair_exact_labels_are_present(self) -> None:
        docs = self.ROOT / "docs/operational"
        cutover = (docs / "e2r_c06_live_cutover_acceptance.md").read_text(encoding="utf-8")
        repair = (docs / "e2r_evidence_to_score_self_repair_summary.md").read_text(encoding="utf-8")
        self.assertIn("C06_CANONICAL_LIVE_CUTOVER_PASS", cutover)
        self.assertIn("SELF_REPAIR_RESOLVED", repair)
        reviewer = json.loads((docs / "e2r_evidence_to_score_reviewer_gate.json").read_text())
        self.assertEqual(reviewer["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
