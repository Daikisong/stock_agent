import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round21_case_expansion_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round21_cases_v04_expansion import (
    ROUND21_CASE_CANDIDATES,
    ROUND21_SCORE_TARGETS,
    render_round21_summary_markdown,
    round21_case_records,
    round21_score_profile_rows,
    round21_summary,
    target_for,
    write_round21_case_expansion_reports,
)


class Round21CasesV04ExpansionTests(unittest.TestCase):
    def test_round21_targets_include_cases_v04_thin_families(self):
        labels = {target.target_id for target in ROUND21_SCORE_TARGETS}

        self.assertIn("RAIL_INFRASTRUCTURE", labels)
        self.assertIn("AI_DATA_CENTER_COOLING", labels)
        self.assertIn("WASTE_RECYCLING_ENVIRONMENT", labels)
        self.assertIn("CDMO_HEALTHCARE_CONTRACT", labels)
        self.assertIn("RARE_METALS_STRATEGIC_MATERIALS", labels)

    def test_case_records_validate_and_keep_price_backfill_open(self):
        records = round21_case_records()

        self.assertEqual(len(records), len(ROUND21_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)

    def test_ai_cooling_and_cdmo_are_green_possible_but_need_evidence(self):
        cooling = target_for("AI_DATA_CENTER_COOLING")
        cdmo = target_for("CDMO_HEALTHCARE_CONTRACT")

        self.assertIsNotNone(cooling)
        self.assertIsNotNone(cdmo)
        assert cooling is not None
        assert cdmo is not None
        self.assertEqual(cooling.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("confirmed_order", cooling.green_conditions)
        self.assertIn("liquid_cooling_theme_only", cooling.red_flags)
        self.assertEqual(cdmo.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("capacity_utilization", cdmo.green_conditions)
        self.assertIn("underutilization", cdmo.red_flags)

    def test_rare_metals_separates_tender_event_from_structural_rerating(self):
        target = target_for("RARE_METALS_STRATEGIC_MATERIALS")
        records = {record.case_id: record for record in round21_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("event_premium_only", target.red_flags)
        self.assertEqual(records["korea_zinc_tender_event_premium"].rerating_result, "event_premium")
        self.assertEqual(records["korea_zinc_tender_event_premium"].case_type, "event_premium")

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round21_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_expansion_not_production_score_change(self):
        summary = round21_summary()
        markdown = render_round21_summary_markdown()

        self.assertEqual(summary["target_count"], 10)
        self.assertGreaterEqual(summary["case_candidate_count"], 30)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names and case IDs must never become score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round21_case_expansion_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v04_round21.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round21_v06.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            loaded = load_case_library(paths["cases"])
            self.assertEqual(len(loaded), len(ROUND21_CASE_CANDIDATES))

    def test_cli_argument_parser_supports_paths(self):
        args = build_parser().parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--score-profiles",
                "scores.csv",
            ]
        )

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.score_profiles, "scores.csv")

    def test_production_scoring_modules_do_not_import_round21_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round21_cases_v04_expansion", text)


if __name__ == "__main__":
    unittest.main()
