from __future__ import annotations

import unittest

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.research_brain.scoring.generalization_canaries import (
    compile_evidence_to_score_generalization_audit,
)


class AllArchetypeRubricTotalityTests(unittest.TestCase):
    def test_all_36_archetypes_have_total_scoring_and_rubric_schema(self) -> None:
        audit = compile_evidence_to_score_generalization_audit()
        totality = audit["scoring_schema_totality"]

        self.assertEqual(len(CANONICAL_ARCHETYPE_IDS), 36)
        self.assertEqual(audit["all_archetype_rubric_count"], 36)
        self.assertEqual(set(audit["rubric_audits"]), set(CANONICAL_ARCHETYPE_IDS))
        self.assertTrue(
            all(
                row["critical_count_sum"] == 0
                for row in audit["rubric_audits"].values()
            )
        )
        self.assertEqual(totality["canonical_archetype_count"], 36)
        self.assertEqual(totality["total_schema_archetype_count"], 36)
        self.assertEqual(totality["incomplete_archetype_ids"], [])
        self.assertEqual(totality["critical_count_sum"], 0)
        self.assertEqual(audit["critical_count_sum"], 0)


if __name__ == "__main__":
    unittest.main()
