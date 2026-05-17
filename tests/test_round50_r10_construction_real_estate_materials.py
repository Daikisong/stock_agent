import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round50_r10_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10ThemePosture
from e2r.sector.round50_r10_construction_real_estate_materials import (
    ROUND50_CASE_CANDIDATES,
    ROUND50_SCORE_TARGETS,
    render_round50_credit_asset_cap_markdown,
    render_round50_green_guardrail_markdown,
    render_round50_price_validation_plan_markdown,
    render_round50_summary_markdown,
    round50_case_candidate_rows,
    round50_case_records,
    round50_price_field_rows,
    round50_score_profile_rows,
    round50_stage_date_rows,
    round50_summary,
    target_for,
    write_round50_r10_reports,
)


class Round50R10ConstructionRealEstateMaterialsTests(unittest.TestCase):
    def test_round50_targets_cover_r10_archetypes(self):
        labels = {target.target_id for target in ROUND50_SCORE_TARGETS}

        self.assertEqual(len(labels), 10)
        for label in (
            "CONSTRUCTION_REAL_ESTATE_CREDIT",
            "REIT_DEVELOPMENT_TRUST",
            "BUILDING_MATERIALS_CYCLE",
            "DATA_CENTER_REIT_INFRASTRUCTURE",
            "COLD_CHAIN_REIT_LOGISTICS",
            "INFRA_RECONSTRUCTION_POLICY",
            "DISASTER_REBUILD_EVENT",
            "COMMERCIAL_REAL_ESTATE_CREDIT",
            "RESIDENTIAL_HOUSING_CYCLE",
            "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT",
        ):
            self.assertIn(label, labels)

    def test_new_r10_canonical_archetypes_exist(self):
        expected = (
            E2RArchetype.REIT_DEVELOPMENT_TRUST,
            E2RArchetype.BUILDING_MATERIALS_CYCLE,
            E2RArchetype.DATA_CENTER_REIT_INFRASTRUCTURE,
            E2RArchetype.COLD_CHAIN_REIT_LOGISTICS,
            E2RArchetype.INFRA_RECONSTRUCTION_POLICY,
            E2RArchetype.DISASTER_REBUILD_EVENT,
            E2RArchetype.COMMERCIAL_REAL_ESTATE_CREDIT,
            E2RArchetype.RESIDENTIAL_HOUSING_CYCLE,
            E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,
        )

        for archetype in expected:
            self.assertIsInstance(archetype.value, str)

    def test_construction_and_cre_are_redteam_first(self):
        construction = target_for("CONSTRUCTION_REAL_ESTATE_CREDIT")
        cre = target_for("COMMERCIAL_REAL_ESTATE_CREDIT")
        data_center = target_for("DATA_CENTER_REIT_INFRASTRUCTURE")
        cold_chain = target_for("COLD_CHAIN_REIT_LOGISTICS")

        self.assertIsNotNone(construction)
        self.assertIsNotNone(cre)
        self.assertIsNotNone(data_center)
        self.assertIsNotNone(cold_chain)
        assert construction is not None
        assert cre is not None
        assert data_center is not None
        assert cold_chain is not None
        self.assertEqual(construction.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("pf_exposure", construction.red_flags)
        self.assertEqual(cre.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("dividend_cut", cre.red_flags)
        self.assertEqual(data_center.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("hyperscale_tenant", data_center.green_conditions)
        self.assertEqual(cold_chain.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("noi_affo", cold_chain.green_conditions)

    def test_policy_reconstruction_and_disaster_are_event_capped(self):
        infra = target_for("INFRA_RECONSTRUCTION_POLICY")
        disaster = target_for("DISASTER_REBUILD_EVENT")
        cap_text = render_round50_credit_asset_cap_markdown()

        self.assertIsNotNone(infra)
        self.assertIsNotNone(disaster)
        assert infra is not None
        assert disaster is not None
        self.assertEqual(infra.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertEqual(disaster.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("funded orders", cap_text)
        self.assertIn("refinancing_success_flag", cap_text)

    def test_required_round50_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round50_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND50_CASE_CANDIDATES))
        self.assertEqual(rows["korea_pf_delinquency_restructuring_case"]["stage4c_date"], "2024-05-13")
        self.assertEqual(rows["korea_builder_support_relief_case"]["stage4b_date"], "2024-03-27")
        self.assertEqual(rows["blackstone_mortgage_trust_dividend_cut_case"]["case_type"], "4c_thesis_break")
        self.assertEqual(rows["blackstone_data_center_reit_flat_debut_case"]["case_type"], "failed_rerating")
        self.assertEqual(rows["fermi_ai_data_center_reit_case"]["stage4b_date"], "2025-09-30")
        self.assertEqual(rows["heidelberg_materials_price_cost_case"]["stage2_date"], "2025-11-06")

    def test_case_records_validate_and_keep_price_backfill_open(self):
        records = round50_case_records()

        self.assertEqual(len(records), len(ROUND50_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertEqual(record.price_validation.price_validation_status, "needs_price_backfill")
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("theme_label_is_not_score_evidence", record.green_guardrails)
            self.assertIn("pf_support_or_rate_cut_is_not_green_evidence_alone", record.green_guardrails)

    def test_score_profile_rows_mark_no_production_change(self):
        rows = round50_score_profile_rows()

        self.assertEqual(len(rows), len(ROUND50_SCORE_TARGETS))
        for row in rows:
            self.assertEqual(row["production_scoring_changed"], "false")
        by_target = {row["target_id"]: row for row in rows}
        self.assertEqual(by_target["CONSTRUCTION_REAL_ESTATE_CREDIT"]["posture"], "REDTEAM_FIRST")
        self.assertEqual(by_target["DATA_CENTER_REIT_INFRASTRUCTURE"]["posture"], "GREEN_POSSIBLE")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        stage_rows = {row["target_id"]: row for row in round50_stage_date_rows()}
        price_fields = {row["field"] for row in round50_price_field_rows()}

        self.assertIn("pf_delinquency_increase", stage_rows["CONSTRUCTION_REAL_ESTATE_CREDIT"]["stage4c"])
        self.assertIn("asset_acquisition", stage_rows["DATA_CENTER_REIT_INFRASTRUCTURE"]["stage2"])
        self.assertIn("pf_delinquency_rate", price_fields)
        self.assertIn("noi_growth", price_fields)
        self.assertIn("data_center_asset_acquired_flag", price_fields)
        self.assertIn("hyperscale_tenant_flag", price_fields)

    def test_summary_and_markdown_explain_r10_guardrails(self):
        summary = round50_summary()
        summary_md = render_round50_summary_markdown()
        guardrails = render_round50_green_guardrail_markdown()
        price_plan = render_round50_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 10)
        self.assertEqual(summary["case_candidate_count"], 12)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 3)
        self.assertEqual(summary["stage4b_case_count"], 1)
        self.assertEqual(summary["stage4c_case_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("production_scoring_changed: false", summary_md)
        self.assertIn("Do not apply these R10 v1.0 weights", guardrails)
        self.assertIn("theme_without_asset", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round50_r10_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r10_round50.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round50_r10_v1.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["credit_asset_caps"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND50_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round50_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round50_r10_construction_real_estate_materials", text)


if __name__ == "__main__":
    unittest.main()
