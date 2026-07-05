import json
import unittest
from pathlib import Path


class FullThesisTargetArchetypeProvenanceTests(unittest.TestCase):
    def test_unknown_target_and_source_primary_context_promotion_are_not_current_blockers(self) -> None:
        parity = json.loads(Path("docs/operational/research_to_runtime_parity_matrix_2026-07-05.json").read_text())
        selection = json.loads(Path("docs/operational/full_thesis_candidate_selection_audit_v2.json").read_text())
        self.assertEqual(parity["target_archetype_unknown_promoted_count"], 0)
        self.assertEqual(parity["source_primary_context_promoted_count"], 0)
        self.assertNotIn("target_archetype_unknown_promoted", selection["blockers"])
        self.assertNotIn("source_primary_context_promoted", selection["blockers"])


if __name__ == "__main__":
    unittest.main()
