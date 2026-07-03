import unittest
from pathlib import Path

from tests.census_v4_test_helpers import census_v4_artifacts


class CensusV4CliUsesV4RunnerTests(unittest.TestCase):
    def test_official_cli_imports_and_calls_v4_runner(self):
        text = Path("src/e2r/cli/run_e2r_census_v4_until_pass.py").read_text(encoding="utf-8")
        self.assertIn("run_census_mode_v4", text)
        self.assertIn("CensusV4RunConfig", text)
        self.assertIn("--brain-candidate-event-seed-path", text)
        self.assertIn("brain_candidate_event_seed_path=args.brain_candidate_event_seed_path", text)
        self.assertNotIn("from e2r.census.census_runner import", text)
        self.assertEqual(census_v4_artifacts()["leaf_audit"]["critical_counts"]["official_cli_not_v4_runner_count"], 0)


if __name__ == "__main__":
    unittest.main()
