import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round33_score_weight_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round33_score_weight_v18 import (
    ROUND33_CASE_CANDIDATES,
    ROUND33_SCORE_TARGETS,
    render_round33_ai_ip_risk_markdown,
    render_round33_event_cycle_guardrail_markdown,
    render_round33_media_cycle_markdown,
    render_round33_summary_markdown,
    round33_case_records,
    round33_score_profile_rows,
    round33_summary,
    target_for,
    write_round33_score_weight_reports,
)


class Round33ScoreWeightV18Tests(unittest.TestCase):
    def test_round33_targets_include_v18_growth_theme_splits(self):
        labels = {target.target_id for target in ROUND33_SCORE_TARGETS}

        self.assertEqual(len(labels), 8)
        self.assertIn("MEDIA_AD_CONTENT_CYCLE", labels)
        self.assertIn("PAPER_PACKAGING_CYCLE", labels)
        self.assertIn("SMART_FARM_AGRI_TECH", labels)
        self.assertIn("CONSUMER_REGULATED_PRODUCT", labels)
        self.assertIn("APPAREL_FAST_FASHION", labels)
        self.assertIn("AI_SOFTWARE_APPLICATION", labels)
        self.assertIn("METAVERSE_NFT_THEME", labels)
        self.assertIn("FOOD_AGRI_LIVESTOCK_CYCLE", labels)

    def test_media_ad_is_watch_first_and_splits_streaming_platform_from_legacy_cycle(self):
        target = target_for("MEDIA_AD_CONTENT_CYCLE")
        records = {record.case_id: record for record in round33_case_records()}
        markdown = render_round33_media_cycle_markdown()

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("owned_ad_platform", target.green_conditions)
        self.assertIn("client_budget_cut", target.red_flags)
        self.assertEqual(records["netflix_ad_tier_growth_candidate"].case_type, "success_candidate")
        self.assertEqual(records["traditional_broadcast_ad_decline_counterexample"].case_type, "failed_rerating")
        self.assertIn("platform monetization", markdown)

    def test_packaging_and_food_agri_are_green_restricted_cycle_areas(self):
        packaging = target_for("PAPER_PACKAGING_CYCLE")
        food = target_for("FOOD_AGRI_LIVESTOCK_CYCLE")
        event_review = render_round33_event_cycle_guardrail_markdown()
        records = {record.case_id: record for record in round33_case_records()}

        self.assertIsNotNone(packaging)
        self.assertIsNotNone(food)
        assert packaging is not None
        assert food is not None
        self.assertEqual(packaging.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertEqual(food.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("overcapacity", packaging.red_flags)
        self.assertIn("disease_event", food.red_flags)
        self.assertEqual(records["pulp_cost_margin_4c"].case_type, "4c_thesis_break")
        self.assertEqual(records["egg_price_spike_event_case"].case_type, "one_off")
        self.assertIn("egg prices rise", event_review)

    def test_smart_farm_is_watch_to_green_but_subsidy_and_adoption_risks_apply(self):
        target = target_for("SMART_FARM_AGRI_TECH")
        records = {record.case_id: record for record in round33_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("recurring_service", target.green_conditions)
        self.assertIn("technical_barrier", target.red_flags)
        self.assertEqual(records["smart_farm_adoption_policy_candidate"].case_type, "success_candidate")
        self.assertEqual(records["smart_farm_financial_technical_barrier_counterexample"].case_type, "failed_rerating")

    def test_regulated_consumer_and_apparel_are_approval_channel_and_legal_risk_gated(self):
        regulated = target_for("CONSUMER_REGULATED_PRODUCT")
        apparel = target_for("APPAREL_FAST_FASHION")
        records = {record.case_id: record for record in round33_case_records()}

        self.assertIsNotNone(regulated)
        self.assertIsNotNone(apparel)
        assert regulated is not None
        assert apparel is not None
        self.assertEqual(regulated.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertEqual(apparel.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("legal_sales_permission", regulated.green_conditions)
        self.assertIn("public_health", regulated.red_flags)
        self.assertIn("ip_legal", apparel.red_flags)
        self.assertIn("product_safety", apparel.red_flags)
        self.assertEqual(records["cannabis_rescheduling_stage1_candidate"].case_type, "event_premium")
        self.assertEqual(records["shein_temu_ip_litigation_4c"].case_type, "4c_thesis_break")

    def test_ai_software_is_green_possible_but_ip_license_and_compute_are_hard_gates(self):
        target = target_for("AI_SOFTWARE_APPLICATION")
        markdown = render_round33_ai_ip_risk_markdown()
        records = {record.case_id: record for record in round33_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("recurring_subscription_or_api", target.green_conditions)
        self.assertIn("compute_cost", target.red_flags)
        self.assertIn("copyright", target.red_flags)
        self.assertEqual(records["b2b_ai_subscription_candidate"].case_type, "success_candidate")
        self.assertEqual(records["generative_ai_copyright_risk_4c"].case_type, "4c_thesis_break")
        self.assertIn("copyright, licensing, and compute cost", markdown)

    def test_metaverse_nft_is_redteam_first_and_green_blocked_by_default(self):
        target = target_for("METAVERSE_NFT_THEME")
        records = {record.case_id: record for record in round33_case_records()}

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertEqual(target.score_weight.eps_fcf, 5)
        self.assertEqual(target.score_weight.information_confidence, 3)
        self.assertIn("no_revenue", target.red_flags)
        self.assertEqual(records["nft_theme_rally_no_revenue_counterexample"].case_type, "overheat")
        self.assertEqual(records["nft_liquidity_collapse_4c"].case_type, "4c_thesis_break")

    def test_case_records_validate_and_keep_backfill_open(self):
        records = round33_case_records()

        self.assertEqual(len(records), len(ROUND33_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("theme_label_is_not_score_evidence", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        for row in round33_score_profile_rows():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_reports_v18_not_production_scoring(self):
        summary = round33_summary()
        markdown = render_round33_summary_markdown()

        self.assertEqual(summary["target_count"], 8)
        self.assertEqual(summary["case_candidate_count"], 32)
        self.assertEqual(summary["success_candidate_count"], 10)
        self.assertEqual(summary["stage4b_case_count"], 0)
        self.assertEqual(summary["stage4c_case_count"], 6)
        self.assertEqual(summary["green_possible_count"], 1)
        self.assertEqual(summary["watch_yellow_first_count"], 4)
        self.assertEqual(summary["redteam_first_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", markdown)
        self.assertIn("Theme names, case IDs, regulation headlines, app features, and price rallies are not score evidence", markdown)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round33_score_weight_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_v15_round33.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round33_v18.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["media_cycle"].exists())
            self.assertTrue(paths["ai_ip_risk"].exists())
            self.assertTrue(paths["event_cycle"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND33_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round33_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round33_score_weight_v18", text)


if __name__ == "__main__":
    unittest.main()
