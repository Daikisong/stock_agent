import unittest

from e2r.cli.run_e2r_census_v3_until_pass import main as v3_main
from e2r.cli.run_e2r_census_mode import main


class CensusV4LegacyRunnerLockoutTests(unittest.TestCase):
    def test_legacy_v1_cli_requires_explicit_fixture_flag(self):
        code = main(
            [
                "--as-of-date",
                "2026-07-01",
                "--output-root",
                "output/test_legacy_cli_lockout",
            ]
        )
        self.assertNotEqual(code, 0)

    def test_legacy_v3_cli_requires_explicit_fixture_flag(self):
        code = v3_main(
            [
                "--as-of-date",
                "2026-07-01",
                "--output-root",
                "output/test_legacy_v3_cli_lockout",
            ]
        )
        self.assertNotEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
