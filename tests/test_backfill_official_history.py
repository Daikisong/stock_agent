import json
import tempfile
import unittest

from e2r.cli.backfill_official_history import build_parser, main


class BackfillOfficialHistoryTests(unittest.TestCase):
    def test_cli_parses_and_writes_plan_without_network(self):
        args = build_parser().parse_args(
            [
                "--start-date",
                "2023-01-01",
                "--end-date",
                "2023-01-31",
                "--market",
                "KR",
            ]
        )
        self.assertEqual(args.market, "KR")

        with tempfile.TemporaryDirectory() as root:
            exit_code = main(
                [
                    "--start-date",
                    "2023-01-01",
                    "--end-date",
                    "2023-01-31",
                    "--output-directory",
                    root,
                ]
            )
            with open(f"{root}/backfill_plan.json", encoding="utf-8") as handle:
                plan = json.load(handle)

        self.assertEqual(exit_code, 0)
        self.assertFalse(plan["network_calls_executed"])
        self.assertFalse(plan["benchmark_labels_used"])
        self.assertFalse(plan["snapshot_derived_universe_used"])


if __name__ == "__main__":
    unittest.main()
