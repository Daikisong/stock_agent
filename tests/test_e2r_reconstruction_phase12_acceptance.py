from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.runtime import (
    ATOMIC_SCORE_STAGE_SCHEMA_VERSION,
    AtomicScoreType,
    CanonicalStage,
)


class E2RReconstructionPhase12AcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[1]
        cls.acceptance = json.loads(
            (cls.repo_root / "e2r_reconstruction_phase12_acceptance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_status_taxonomy_and_stage_enum_are_phase_scoped(self) -> None:
        self.assertEqual(self.acceptance["phase"], 12)
        self.assertEqual(
            self.acceptance["status"],
            "DETERMINISTIC_SCORE_STAGE_INTEGRITY_PASS",
        )
        self.assertFalse(self.acceptance["production_runtime_ready"])
        self.assertEqual(
            ATOMIC_SCORE_STAGE_SCHEMA_VERSION,
            "e2r_atomic_score_stage_v1",
        )
        self.assertEqual(
            set(self.acceptance["score_taxonomy"]),
            {item.value for item in AtomicScoreType},
        )
        self.assertEqual(
            set(self.acceptance["canonical_stage_enum"]),
            {item.value for item in CanonicalStage},
        )

    def test_atomic_full_event_and_pending_snapshots_are_frozen(self) -> None:
        frozen = self.acceptance["frozen_decisions"]
        full = frozen["full"]
        self.assertEqual(full["decision_id"], "ADEC-e5d977ecc906b6d1abddbb0d")
        self.assertEqual(full["score_type"], AtomicScoreType.FULL_E2R_100.value)
        self.assertEqual(full["score_value"], 100.0)
        self.assertEqual(full["canonical_stage"], CanonicalStage.STAGE_3_GREEN.value)
        self.assertEqual(full["material_gap_count"], 0)
        self.assertEqual(
            full["score_fingerprint"],
            "aa581be97cd88814ea18d8e4de7da6064fa3a949ea65dbfaffa8713c8d3d4f66",
        )

        event = frozen["event_partial"]
        self.assertEqual(
            event["score_type"],
            AtomicScoreType.EVENT_EVIDENCE_PARTIAL.value,
        )
        self.assertEqual(event["score_value"], 75.0)
        self.assertFalse(event["score_finalization_allowed"])

        pending = frozen["material_gap_pending"]
        self.assertEqual(pending["score_type"], AtomicScoreType.NO_SCORE.value)
        self.assertIsNone(pending["score_value"])
        self.assertEqual(pending["raw_reference_score"], 75.0)
        self.assertEqual(pending["canonical_stage"], CanonicalStage.STAGE_0.value)
        self.assertFalse(pending["score_valid"])

    def test_atomic_contract_requires_claim_mapping_gap_and_trace_lineage(self) -> None:
        contract = self.acceptance["atomic_decision_contract"]
        self.assertTrue(all(contract.values()))
        self.assertTrue(contract["full_score_requires_material_primitive_assessments"])
        self.assertTrue(
            contract["full_score_requires_accepted_current_source_backed_mapped_claims"]
        )
        self.assertTrue(contract["stage_court_trace_must_exactly_match_decision"])
        self.assertTrue(
            contract["stage_and_status_recomputed_from_score_rules_and_hard_break"]
        )

    def test_independent_integrity_audit_and_hard_acceptance_are_zero(self) -> None:
        audit = self.acceptance["integrity_audit"]
        self.assertEqual(
            audit["status"],
            "DETERMINISTIC_SCORE_STAGE_INTEGRITY_PASS",
        )
        self.assertEqual(audit["decision_count"], 3)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(all(value == 0 for value in audit["critical_counts"].values()))
        self.assertEqual(
            audit["result_hash"],
            "be5c0d66b45bee42d0e37285f5a96161672a4daf7c0e867c7d658090c3bf9dbe",
        )
        hard = self.acceptance["hard_acceptance"]
        self.assertTrue(all(value == 0 for value in hard.values()))

    def test_score_delta_requires_claim_or_config_change(self) -> None:
        delta = self.acceptance["score_delta_audit"]
        explained = delta["explained"]
        self.assertEqual(explained["status"], "ATOMIC_SCORE_DELTA_EXPLAINED")
        self.assertEqual(explained["score_delta"], -5.0)
        self.assertTrue(explained["claim_state_changed"])
        self.assertEqual(explained["unexplained_score_delta_count"], 0)
        self.assertEqual(
            explained["result_hash"],
            "66cd8f060745f9c87089788f87657e545d23c8dcb384d9d1a3eb1f845c911803",
        )

        known_bad = delta["known_bad_unexplained"]
        self.assertEqual(
            known_bad["status"],
            "ATOMIC_SCORE_DELTA_UNEXPLAINED",
        )
        self.assertEqual(known_bad["unexplained_score_delta_count"], 1)
        self.assertFalse(known_bad["claim_state_changed"])
        self.assertFalse(known_bad["config_changed"])

        hard_break = self.acceptance["hard_break_contract"]
        self.assertEqual(hard_break["invalid_condition_probe_count"], 8)
        self.assertEqual(hard_break["invalid_condition_probe_rejected_count"], 8)

    def test_report_explains_pending_hard_break_and_production_boundary(self) -> None:
        lineage = self.acceptance["claim_lineage_integration"]
        self.assertTrue(lineage["source_acquisition_document_used"])
        self.assertTrue(lineage["phase9_claim_ledger_event_used"])
        self.assertTrue(lineage["mapping_id_preserved_in_contribution"])
        self.assertTrue(lineage["same_fixture_is_not_production_score_eligible"])

        report = (
            self.repo_root
            / "docs"
            / "operational"
            / "e2r_reconstruction_phase12_deterministic_score_stage.md"
        ).read_text(encoding="utf-8")
        self.assertIn("DETERMINISTIC_SCORE_STAGE_INTEGRITY_PASS", report)
        self.assertIn("raw reference", report)
        self.assertIn("동시 위조", report)
        self.assertIn("current OPEN", report)
        self.assertIn("production_runtime_ready=false", report)
        self.assertIn("Phase 13", report)


if __name__ == "__main__":
    unittest.main()
