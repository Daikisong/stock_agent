import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverOperatorDigestTests(unittest.TestCase):
    def test_every_digest_row_has_next_action(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        rows = bundle["operator_digest"]["rows"]
        self.assertTrue(rows)
        self.assertTrue(all(row.get("next_action") for row in rows))


if __name__ == "__main__":
    unittest.main()
