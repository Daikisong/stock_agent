import io
import json
import unittest
from contextlib import redirect_stdout

from e2r.cli.research_brain_v2_report import main as brain_v2_main
from e2r.cli.run_e2r_census_v2 import main as census_v2_main
from e2r.cli.run_e2r_census_v3_until_pass import main as census_v3_main
from e2r.cli.run_research_brain_v3_daily_shadow import main as brain_v3_main
from e2r.cli.run_research_to_runtime_parity_until_pass import main as parity_main


class LegacyCliCannotClaimReadyTests(unittest.TestCase):
    def _assert_blocked(self, callable_, argv: list[str]) -> None:
        stream = io.StringIO()
        with redirect_stdout(stream):
            exit_code = callable_(argv)
        self.assertEqual(exit_code, 2)
        payload = json.loads(stream.getvalue())
        self.assertEqual(payload["status"], "LEGACY_DIAGNOSTIC_ONLY")
        self.assertFalse(payload["canonical_readiness_eligible"])
        self.assertFalse(payload["canonical_ready_label_allowed"])

    def test_census_v2_requires_explicit_legacy_opt_in(self) -> None:
        self._assert_blocked(census_v2_main, ["--as-of-date", "2026-07-05"])

    def test_census_v3_requires_explicit_legacy_opt_in(self) -> None:
        self._assert_blocked(
            census_v3_main,
            ["--as-of-date", "2026-07-05", "--output-root", "unused"],
        )

    def test_research_brain_v2_requires_explicit_legacy_opt_in(self) -> None:
        self._assert_blocked(brain_v2_main, [])

    def test_research_brain_v3_requires_explicit_legacy_opt_in(self) -> None:
        self._assert_blocked(brain_v3_main, [])

    def test_goal4_parity_cli_is_diagnostic_only_by_default(self) -> None:
        self._assert_blocked(parity_main, [])


if __name__ == "__main__":
    unittest.main()
