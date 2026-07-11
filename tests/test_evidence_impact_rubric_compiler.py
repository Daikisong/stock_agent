from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
    audit_evidence_impact_rubrics,
    compile_evidence_impact_rubrics,
)


class EvidenceImpactRubricCompilerTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_c06_distinguishes_positive_partial_counter_and_unsupported_meaning(self) -> None:
        catalog = compile_evidence_impact_rubrics("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        audit = audit_evidence_impact_rubrics(catalog)
        self.assertEqual(audit["status"], "RESEARCH_CALIBRATED_IMPACT_RUBRIC_PASS")
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertGreaterEqual(len(catalog.rubrics), 14)
        required = {"hbm_product_profile", "qualification_state", "shipment_or_revenue_mix", "actual_earnings_conversion", "margin_fcf_conversion", "conventional_memory_drag", "capacity_supply_response", "package_substrate_sympathy"}
        self.assertTrue(required <= set(catalog.by_primitive()))

    def test_actual_earnings_does_not_overmap_customer_allocation(self) -> None:
        rubric = compile_evidence_impact_rubrics("C06_HBM_MEMORY_CUSTOMER_CAPACITY").by_primitive()["actual_earnings_conversion"]
        self.assertIn("customer allocation", " ".join(rubric.unsupported_predicates))
        self.assertNotIn("bottleneck_pricing", rubric.allowed_component_ids)

    def test_product_profile_and_package_sympathy_are_capped_to_information(self) -> None:
        rubrics = compile_evidence_impact_rubrics("C06_HBM_MEMORY_CUSTOMER_CAPACITY").by_primitive()
        self.assertEqual(rubrics["hbm_product_profile"].allowed_component_ids, ("information_confidence",))
        self.assertEqual(rubrics["package_substrate_sympathy"].allowed_component_ids, ("information_confidence",))

    def test_historical_examples_hide_outcome_fields(self) -> None:
        catalog = compile_evidence_impact_rubrics("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(
            sum(len(rubric.source_backed_examples) for rubric in catalog.rubrics),
            2,
        )
        for rubric in catalog.rubrics:
            for example in rubric.source_backed_examples:
                self.assertNotIn("stage_after", example)
                self.assertNotIn("mfe", example)
                self.assertNotIn("mae", example)
        self.assertFalse(catalog.policies["source_proxy_current_score_allowed"])

    def test_operational_audit_matches_recompiled_rubric(self) -> None:
        catalog = compile_evidence_impact_rubrics("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        recomputed = audit_evidence_impact_rubrics(catalog)
        artifact = json.loads(
            (self.ROOT / "docs/operational/e2r_evidence_impact_rubric_audit.json").read_text()
        )
        for key in ("status", "rubric_count", "source_backed_example_count", "config_hash", "critical_counts"):
            self.assertEqual(artifact[key], recomputed[key])


if __name__ == "__main__":
    unittest.main()
