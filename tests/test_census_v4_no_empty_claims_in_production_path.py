import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.census_v4_auditor import (
    _empty_claims_stage_builder_production_count,
    _legacy_runner_production_reachable_count,
    _legacy_v3_runner_production_reachable_count,
    _official_cli_not_v4_runner_count,
)
from tests.census_v4_test_helpers import census_v4_artifacts


class CensusV4NoEmptyClaimsInProductionPathTests(unittest.TestCase):
    def test_production_path_static_audit_blocks_empty_claim_tuple_wiring(self):
        critical = census_v4_artifacts()["leaf_audit"]["critical_counts"]
        self.assertEqual(critical["empty_claims_stage_builder_production_count"], 0)
        self.assertEqual(critical["legacy_runner_production_reachable_count"], 0)
        self.assertEqual(critical["legacy_v3_runner_production_reachable_count"], 0)
        self.assertEqual(critical["old_cli_can_claim_pass_count"], 0)
        self.assertEqual(critical["official_cli_not_v4_runner_count"], 0)

    def test_static_audit_detects_fake_legacy_and_empty_claim_paths(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "src" / "e2r" / "cli").mkdir(parents=True)
            (root / "src" / "e2r" / "census").mkdir(parents=True)
            (root / "tests").mkdir()
            (root / "src" / "e2r" / "cli" / "run_e2r_census_mode.py").write_text(
                "from e2r.census.census_runner import run_census_mode\n"
                "def main():\n"
                "    # --allow-legacy-v1 return 2 strings in comments must not satisfy the guard\n"
                "    return run_census_mode()\n",
                encoding="utf-8",
            )
            (root / "src" / "e2r" / "cli" / "run_e2r_census_v3_until_pass.py").write_text(
                "from e2r.census.census_runner_v3 import run_census_mode_v3\n"
                "def main():\n"
                "    return 0 if run_census_mode_v3().readiness_verdict['verdict'] == 'FULL_UNIVERSE_STAGE_MAP_PASS' else 1\n",
                encoding="utf-8",
            )
            (root / "src" / "e2r" / "cli" / "run_e2r_census_v4_until_pass.py").write_text(
                "def main():\n"
                "    # run_census_mode_v4 CensusV4RunConfig strings in comments must not satisfy the gate\n"
                "    return 0\n",
                encoding="utf-8",
            )
            (root / "src" / "e2r" / "census" / "census_runner_v4.py").write_text(
                "def build():\n"
                "    empty=[]\n"
                "    return build_atomic_stage_decisions(accepted_claims=empty, score_contributions=tuple())\n",
                encoding="utf-8",
            )
            self.assertEqual(_legacy_runner_production_reachable_count(root), 1)
            self.assertEqual(_legacy_v3_runner_production_reachable_count(root), 1)
            self.assertGreaterEqual(_empty_claims_stage_builder_production_count(root), 2)
            self.assertEqual(_official_cli_not_v4_runner_count(root), 1)


if __name__ == "__main__":
    unittest.main()
