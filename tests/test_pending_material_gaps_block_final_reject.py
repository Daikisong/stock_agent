import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class PendingMaterialGapsBlockFinalRejectTests(unittest.TestCase):
    def test_pending_rows_have_recheck_reason_and_low_scores_are_watch_only(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        rows = bundle["operator_digest"]["rows"]
        self.assertTrue(rows)
        pending = [row for row in rows if row["next_action"] == "RECHECK_SOURCE"]
        self.assertTrue(all(row.get("pending_reason") is not None for row in pending))
        self.assertTrue(all(row.get("next_action") in {"WATCH", "RECHECK_SOURCE"} for row in rows))
        self.assertFalse(
            any(
                row.get("section") in {"Stage3-Red", "4C", "Reject"}
                and row.get("score_stage_validity") == "FINAL_WITH_NONMATERIAL_GAPS"
                for row in rows
            )
        )


if __name__ == "__main__":
    unittest.main()
