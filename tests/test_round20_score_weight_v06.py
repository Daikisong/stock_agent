import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round20_score_weight_report import build_parser
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round20_score_weight_v06 import (
    ROUND20_SCORE_WEIGHT_TARGETS,
    render_round20_summary_markdown,
    round20_policy_groups,
    round20_target_rows,
    round20_theme_tag_rows,
    target_for,
    write_round20_score_weight_reports,
)


class Round20ScoreWeightV06Tests(unittest.TestCase):
    def test_round20_targets_include_thin_sub_archetypes(self):
        labels = {target.sub_archetype for target in ROUND20_SCORE_WEIGHT_TARGETS}

        self.assertIn("RAIL_INFRASTRUCTURE", labels)
        self.assertIn("AI_DATA_CENTER_COOLING", labels)
        self.assertIn("WASTE_RECYCLING_ENVIRONMENT", labels)
        self.assertIn("SECURITY_IDENTITY_DEEPFAKE", labels)
        self.assertIn("CLOUD_AI_SOFTWARE_INFRA", labels)
        self.assertIn("CRO_CLINICAL_SERVICE", labels)

    def test_theme_tags_are_search_routing_not_score_inputs(self):
        for row in round20_theme_tag_rows():
            self.assertEqual(row["theme_is_score_input"], "false")

    def test_ai_cooling_requires_real_orders_not_theme_only(self):
        target = target_for("AI_DATA_CENTER_COOLING")

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("confirmed_customer_order", target.must_have_evidence)
        self.assertIn("cooling_theme_only", target.red_flags)
        self.assertGreaterEqual(target.score_weight.as_dict()["bottleneck_pricing"], 22)

    def test_security_has_operational_trust_4c_guardrail(self):
        target = target_for("SECURITY_IDENTITY_DEEPFAKE")

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("large_outage", target.red_flags)
        self.assertIn("large_outage", target.stage4c_conditions)

    def test_education_and_apparel_stay_watch_first(self):
        education = target_for("EDUCATION_SPECIALTY_SERVICES")
        apparel = target_for("APPAREL_BRAND_OEM")

        self.assertIsNotNone(education)
        self.assertIsNotNone(apparel)
        assert education is not None
        assert apparel is not None
        self.assertEqual(education.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("birthrate_decline", education.red_flags)
        self.assertEqual(apparel.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("inventory_build", apparel.red_flags)

    def test_policy_groups_split_green_and_watch(self):
        groups = round20_policy_groups()

        self.assertIn("AI_DATA_CENTER_COOLING", groups[Round10ThemePosture.GREEN_POSSIBLE.value])
        self.assertIn("CLOUD_AI_SOFTWARE_INFRA", groups[Round10ThemePosture.GREEN_POSSIBLE.value])
        self.assertIn("RAIL_INFRASTRUCTURE", groups[Round10ThemePosture.WATCH_YELLOW_FIRST.value])
        self.assertEqual(groups[Round10ThemePosture.REDTEAM_FIRST.value], ())

    def test_target_rows_mark_no_production_scoring_change(self):
        for row in round20_target_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_report_writer_outputs_round20_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round20_score_weight_reports(
                output_directory=Path(tmp) / "out",
                score_profile_path=Path(tmp) / "score_weight_profiles_round20_v06.csv",
                theme_map_path=Path(tmp) / "theme_tag_map_round20_v06.csv",
            )

            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["theme_map"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["target_matrix"].exists())
            self.assertTrue(paths["theme_policy"].exists())
            self.assertTrue(paths["case_candidate_plan"].exists())
            self.assertTrue(paths["next_plan"].exists())
            self.assertIn("production_scoring_changed: false", paths["summary"].read_text(encoding="utf-8"))

    def test_summary_says_not_production_score_change(self):
        markdown = render_round20_summary_markdown()

        self.assertIn("theme_tags_are_score_input: false", markdown)
        self.assertIn("not a production score change", markdown)
        self.assertIn("액침냉각", markdown)

    def test_cli_argument_parser_supports_paths(self):
        args = build_parser().parse_args(
            [
                "--output-directory",
                "out",
                "--score-profiles",
                "scores.csv",
                "--theme-map",
                "themes.csv",
            ]
        )

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.score_profiles, "scores.csv")
        self.assertEqual(args.theme_map, "themes.csv")

    def test_production_scoring_modules_do_not_import_round20_matrix(self):
        paths = [
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ]
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round20_score_weight_v06", text)


if __name__ == "__main__":
    unittest.main()
