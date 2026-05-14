from datetime import date
import tempfile
import unittest

from e2r.cli.run_korea_shadow_validation import build_arg_parser, run_shadow_validation


AS_OF = date(2024, 5, 21)


class KoreaShadowValidationTests(unittest.TestCase):
    def test_fixture_shadow_validation_runs_tiny_smoke_and_small(self):
        with tempfile.TemporaryDirectory() as output_dir:
            summary = run_shadow_validation(
                as_of_date=AS_OF,
                output_directory=output_dir,
                fixture_mode=True,
                live_enabled=False,
            )

            self.assertTrue(summary.summary_path.exists())
            step_names = [item.name for item in summary.steps]
            self.assertEqual(step_names, ["tiny", "targeted_smoke", "small"])
            self.assertTrue(summary.passed)
            self.assertFalse(summary.standard_shadow_ran)
            self.assertTrue(all(item.result.candidates_path.exists() for item in summary.steps))
            self.assertTrue(all(item.result.calibration_json_path.exists() for item in summary.steps))

    def test_targeted_smoke_is_excluded_from_production_candidates(self):
        with tempfile.TemporaryDirectory() as output_dir:
            summary = run_shadow_validation(
                as_of_date=AS_OF,
                output_directory=output_dir,
                fixture_mode=True,
                live_enabled=False,
                targeted_smoke_company="스모크테스트",
                targeted_smoke_symbol="009999",
                targeted_smoke_queries=("스모크테스트 수주잔고",),
            )

        smoke_step = next(item for item in summary.steps if item.name == "targeted_smoke")
        self.assertTrue(smoke_step.gate.passed)
        self.assertTrue(smoke_step.result.run_log.targeted_smoke_results)
        self.assertFalse(any(item.candidate_source_path == "targeted_smoke" for item in smoke_step.result.candidates))

    def test_standard_shadow_runs_only_when_requested_and_gates_pass(self):
        with tempfile.TemporaryDirectory() as output_dir:
            summary = run_shadow_validation(
                as_of_date=AS_OF,
                output_directory=output_dir,
                fixture_mode=True,
                live_enabled=False,
                run_standard_shadow=True,
            )

        self.assertTrue(summary.standard_shadow_ran)
        self.assertEqual(summary.steps[-1].name, "standard_shadow")
        self.assertTrue(summary.steps[-1].gate.passed)

    def test_cli_argument_parser_supports_live_and_standard_shadow(self):
        args = build_arg_parser().parse_args(
            [
                "--date",
                "2024-05-21",
                "--live",
                "--standard-shadow",
                "--targeted-smoke-symbol",
                "005930",
                "--targeted-smoke-company",
                "삼성전자",
                "--targeted-smoke-query",
                "삼성전자 수주잔고",
            ]
        )

        self.assertTrue(args.live)
        self.assertTrue(args.standard_shadow)
        self.assertEqual(args.targeted_smoke_symbol, "005930")
        self.assertEqual(args.targeted_smoke_query, ["삼성전자 수주잔고"])


if __name__ == "__main__":
    unittest.main()
