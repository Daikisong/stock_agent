from __future__ import annotations

from pathlib import Path
import unittest

from e2r.pro_first.v2_static_audit import (
    REQUIRED_V2_STATIC_COUNTER_KEYS,
    _behavior_counters_from_sources,
    compile_pro_first_v2_static_audit,
)


ROOT = Path(__file__).resolve().parents[1]


class ProFirstV2StaticAuditTest(unittest.TestCase):
    def test_requirement_level_static_audit_has_all_zero_counters(self) -> None:
        audit = compile_pro_first_v2_static_audit(ROOT)

        self.assertEqual(tuple(audit["counters"]), REQUIRED_V2_STATIC_COUNTER_KEYS)
        self.assertEqual(audit["critical_count"], 0)
        self.assertEqual(audit["status"], "PASS")
        self.assertTrue(all(value == 0 for value in audit["counters"].values()))

    def test_static_audit_detects_skipped_repair_and_gap_downgrade_order(self) -> None:
        behavior = _behavior_counters_from_sources(
            live_source=(
                "await self._close_public_gaps(\n"
                "await self._close_public_gaps(\n"
                "public_material_gap_question_ids\n"
                "ProScoringPipelineService(\n"
            ),
            question_source="elif missing_corroboration:\nelif public_material:\n",
            saturation_sources=("component_fact_count",),
        )

        self.assertEqual(behavior["component_count_used_as_adequacy_count"], 1)
        self.assertEqual(
            behavior["public_gap_downgraded_to_corroboration_count"], 1
        )
        self.assertEqual(behavior["material_gap_without_followup_count"], 0)
        self.assertEqual(behavior["verifier_repair_skipped_count"], 1)


if __name__ == "__main__":
    unittest.main()
