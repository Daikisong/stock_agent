import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.baseline_scanner import BaselineScanInputs, BaselineScanner
from e2r.census.census_runner import CensusRunConfig, official_provider_gap_errors, run_census_mode
from e2r.census.depth_policy import CensusDepthPolicyConfig, decide_depths
from e2r.census.stage_status_builder import build_stage_status
from tests.census_test_helpers import write_universe_csv
from tests.census_test_helpers import instrument


class CensusProviderFailurePendingTests(unittest.TestCase):
    def test_provider_failure_becomes_pending_not_low_score(self):
        inst = instrument()
        scan = BaselineScanner(BaselineScanInputs(provider_failed_symbols={inst.symbol: ["KRX"]})).scan(inst, as_of_date="2026-07-01")
        decision = decide_depths([inst], [scan], config=CensusDepthPolicyConfig(sector_sample_quota=0))[0]
        status = build_stage_status(instrument=inst, as_of_date="2026-07-01", scan=scan, depth_decision=decision)
        self.assertEqual(status.census_status.value, "PENDING_PROVIDER")
        self.assertEqual(status.verified_score, None)
        self.assertNotIn(status.base_stage.value, {"Reject", "Red"})

    def test_live_official_gap_is_pending_not_stage0(self):
        errors = official_provider_gap_errors(
            source_mode="live_official_first",
            universe_file=None,
            env={"KRX_OPENAPI_KEY": "", "OPENDART_API_KEY": ""},
            official_baseline_connector_wired=False,
        )
        self.assertIn("KRX_OPENAPI_KEY_missing", errors)
        self.assertIn("OPENDART_API_KEY_missing", errors)
        self.assertIn("official_baseline_connector_unwired", errors)

        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            universe = write_universe_csv(root / "universe.csv", count=3)
            output = root / "out"
            result = run_census_mode(
                CensusRunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output),
                    universe_file=None,
                    max_symbols=3,
                    fail_on_critical_audit=True,
                    write_operational_docs=False,
                    source_mode="live_official_first",
                )
            )
            self.assertEqual(result.stage_summary["provider_pending_count"], result.stage_summary["scanned_symbol_count"])
            self.assertEqual(result.stage_summary["stage0_count"], 0)

    def test_fixture_universe_does_not_inject_live_provider_gap(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            universe = write_universe_csv(root / "universe.csv", count=3)
            output = root / "out"
            result = run_census_mode(
                CensusRunConfig(
                    as_of_date="2026-07-01",
                    output_root=str(output),
                    universe_file=str(universe),
                    max_symbols=0,
                    fail_on_critical_audit=True,
                    write_operational_docs=False,
                    source_mode="live_official_first",
                )
            )
            self.assertEqual(result.stage_summary["provider_pending_count"], 0)


if __name__ == "__main__":
    unittest.main()
