import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverScoreMeaningAuditTests(unittest.TestCase):
    def test_score_outputs_have_claim_and_contribution_counts(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        summary = bundle["score_meaning_audit"]["summary"]
        self.assertEqual(summary["canonical_score_scale_min"], 0)
        self.assertEqual(summary["canonical_score_scale_max"], 100)
        self.assertIn("score_without_claim_count", summary)


if __name__ == "__main__":
    unittest.main()
