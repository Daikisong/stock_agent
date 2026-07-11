from __future__ import annotations

import unittest
from pathlib import Path

from e2r.research_brain.scoring.scoring_readiness import (
    READY,
    RESEARCH_NOT_VERIFIED,
    SEMANTIC_NOT_READY,
    compile_meaningful_scoring_readiness,
)


class ReadinessV2DeprecatedUntilV3Tests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_v2_shape_pass_cannot_activate_legacy_ready_alias(self) -> None:
        verdict = compile_meaningful_scoring_readiness(
            config_path=self.ROOT
            / "configs/e2r_meaningful_scoring_readiness_v2.json"
        )
        self.assertEqual(verdict["status"], READY)
        self.assertEqual(verdict["exact_final_verdict"], SEMANTIC_NOT_READY)
        self.assertEqual(
            verdict["research_grade_acquisition_status"],
            RESEARCH_NOT_VERIFIED,
        )
        self.assertFalse(verdict["legacy_ready_alias_active"])
        self.assertTrue(verdict["readiness_v3_required"])
        self.assertNotEqual(verdict["status"], "MEANINGFUL_E2R_SCORING_READY")


if __name__ == "__main__":
    unittest.main()
