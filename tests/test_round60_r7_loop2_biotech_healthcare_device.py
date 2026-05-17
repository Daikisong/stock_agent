import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round60_r7_loop2_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round60_r7_loop2_biotech_healthcare_device import (
    ROUND60_CASE_CANDIDATES,
    ROUND60_PRICE_FIELDS,
    ROUND60_SCORE_TARGETS,
    render_round60_green_guardrail_markdown,
    render_round60_price_validation_plan_markdown,
    render_round60_risk_overlay_markdown,
    render_round60_summary_markdown,
    round60_case_candidate_rows,
    round60_case_records,
    round60_price_field_rows,
    round60_score_profile_rows,
    round60_stage_date_rows,
    round60_summary,
    target_for,
    write_round60_r7_loop2_reports,
)


class Round60R7Loop2BiotechHealthcareDeviceTests(unittest.TestCase):
    def test_round60_targets_cover_r7_loop2_archetypes(self):
        labels = {target.target_id for target in ROUND60_SCORE_TARGETS}

        self.assertEqual(len(labels), 16)
        for label in (
            "CDMO_HEALTHCARE_CONTRACT",
            "CRO_CLINICAL_SERVICE",
            "BIOSIMILAR_COMMERCIALIZATION",
            "BIOSIMILAR_ORIGINATOR_DEFENSE",
            "OBESITY_GLP1_COMMERCIALIZATION",
            "GENE_THERAPY_RARE_DISEASE",
            "AI_DRUG_DISCOVERY_PLATFORM",
            "DIGITAL_HEALTHCARE_AI",
            "DIGITAL_HEALTHCARE_REMOTE_MEDICINE",
            "TELEHEALTH_BEHAVIORAL_HEALTH",
            "PHARMA_CHANNEL_AND_PRIVACY_RISK",
            "MEDICAL_DEVICE_HEALTHCARE_EXPORT",
            "MEDICAL_DEVICE_DENTAL_IMPLANT",
            "BOTULINUM_AESTHETIC_REGULATED",
            "DIAGNOSTICS_INFECTIOUS_DISEASE",
            "ANIMAL_HEALTH_BIOSECURITY",
        ):
            self.assertIn(label, labels)
        for target in ROUND60_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE)
            self.assertFalse(target.production_scoring_changed)

    def test_cdmo_glp1_and_devices_are_green_possible_but_guardrailed(self):
        cdmo = target_for("CDMO_HEALTHCARE_CONTRACT")
        glp1 = target_for("OBESITY_GLP1_COMMERCIALIZATION")
        device = target_for("MEDICAL_DEVICE_HEALTHCARE_EXPORT")
        implant = target_for("MEDICAL_DEVICE_DENTAL_IMPLANT")

        for target in (cdmo, glp1, device, implant):
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        assert cdmo is not None
        assert glp1 is not None
        assert device is not None
        assert implant is not None
        self.assertIn("capacity_utilization", cdmo.green_conditions)
        self.assertIn("underutilization", cdmo.red_flags)
        self.assertIn("prescription_volume", glp1.green_conditions)
        self.assertIn("compounded_alternative", glp1.red_flags)
        self.assertIn("consumable_repeat_revenue", device.green_conditions)
        self.assertIn("vbp_price_control", implant.red_flags)

    def test_pre_revenue_ai_telehealth_and_diagnostics_are_redteam_first(self):
        for target_id in (
            "GENE_THERAPY_RARE_DISEASE",
            "AI_DRUG_DISCOVERY_PLATFORM",
            "TELEHEALTH_BEHAVIORAL_HEALTH",
            "DIAGNOSTICS_INFECTIOUS_DISEASE",
        ):
            target = target_for(target_id)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)

        gene = target_for("GENE_THERAPY_RARE_DISEASE")
        ai_drug = target_for("AI_DRUG_DISCOVERY_PLATFORM")
        diagnostics = target_for("DIAGNOSTICS_INFECTIOUS_DISEASE")
        telehealth = target_for("TELEHEALTH_BEHAVIORAL_HEALTH")
        assert gene is not None
        assert ai_drug is not None
        assert diagnostics is not None
        assert telehealth is not None
        self.assertIn("cash_burn", gene.red_flags)
        self.assertIn("no_approved_drug", ai_drug.red_flags)
        self.assertIn("one_off_demand", diagnostics.red_flags)
        self.assertIn("impairment", telehealth.red_flags)

    def test_pharma_channel_is_gate_only_overlay(self):
        pharma = target_for("PHARMA_CHANNEL_AND_PRIVACY_RISK")

        assert pharma is not None
        self.assertEqual(pharma.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertTrue(pharma.gate_only)
        self.assertEqual(pharma.score_weight.eps_fcf, "gate")
        self.assertIn("fda_ftc_scrutiny", pharma.stage4c_conditions)
        self.assertIn("illegal_copycat_drug", pharma.red_flags)

    def test_required_round60_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round60_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND60_CASE_CANDIDATES))
        self.assertEqual(rows["samsung_biologics_gsk_us_facility_case"]["stage2_date"], "2025-12-22")
        self.assertEqual(rows["samsung_biologics_cdmo_capacity_reference"]["stage2_date"], "")
        self.assertEqual(rows["straumann_dental_implant_vbp_case"]["stage2_date"], "2026-02-18")
        self.assertEqual(rows["lilly_foundayo_fda_approval_case"]["stage2_date"], "2026-04-01")
        self.assertEqual(rows["lilly_foundayo_prescription_uptake_case"]["stage2_date"], "2026-05-08")
        self.assertEqual(rows["lilly_foundayo_switch_maintenance_case"]["stage2_date"], "2026-05-12")
        self.assertEqual(rows["biosimilar_access_slow_uptake_case"]["stage2_date"], "2024-05-01")
        self.assertEqual(rows["novo_glp1_price_pressure_case"]["stage4c_date"], "2026-02-04")
        self.assertEqual(rows["hims_branded_glp1_pivot_loss_case"]["stage4c_date"], "2026-05-12")
        self.assertEqual(rows["hims_novo_partnership_case"]["stage2_date"], "2026-03-09")
        self.assertEqual(rows["hims_compounded_glp1_crackdown_case"]["stage4c_date"], "2026-02-07")
        self.assertEqual(rows["bluebird_gene_therapy_cash_crunch_case"]["stage4c_date"], "2025-02-21")
        self.assertEqual(rows["charles_river_cro_funding_crunch_case"]["stage4c_date"], "2024-08-07")
        self.assertEqual(rows["teladoc_betterhelp_impairment_case"]["stage4c_date"], "2024-08-01")
        self.assertEqual(rows["recursion_exscientia_ai_drug_case"]["stage2_date"], "2024-08-08")
        self.assertEqual(rows["lunit_dbt_subgroup_validation_case"]["stage2_date"], "2025-03-17")
        self.assertEqual(rows["botox_counterfeit_fda_warning_case"]["stage4c_date"], "2025-11-05")

    def test_case_records_validate_and_keep_round60_guardrails(self):
        records = round60_case_records()

        self.assertEqual(len(records), len(ROUND60_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("approval_or_clinical_news_is_not_revenue", record.green_guardrails)
            self.assertIn("commercialization_reimbursement_fcf_required_for_green", record.green_guardrails)
            self.assertIn("capacity_without_utilization_is_not_stage3", record.green_guardrails)
            self.assertIn("do_not_invent_prescriptions_reimbursement_capacity_uptake_cash_runway_hospital_adoption_or_stage_prices", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["samsung_biologics_cdmo_capacity_reference"].score_price_alignment, "aligned")
        self.assertEqual(by_id["hims_novo_partnership_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["novo_glp1_price_pressure_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["bluebird_gene_therapy_cash_crunch_case"].score_price_alignment, "false_positive_score")
        self.assertEqual(by_id["lunit_dbt_subgroup_validation_case"].score_price_alignment, "unknown")

    def test_score_profile_rows_match_round60_weight_table(self):
        rows = {row["target_id"]: row for row in round60_score_profile_rows()}

        self.assertEqual(rows["CDMO_HEALTHCARE_CONTRACT"]["structural_visibility"], "24")
        self.assertEqual(rows["CRO_CLINICAL_SERVICE"]["eps_fcf"], "17")
        self.assertEqual(rows["BIOSIMILAR_COMMERCIALIZATION"]["market_mispricing"], "12")
        self.assertEqual(rows["OBESITY_GLP1_COMMERCIALIZATION"]["valuation"], "11")
        self.assertEqual(rows["GENE_THERAPY_RARE_DISEASE"]["eps_fcf"], "7")
        self.assertEqual(rows["DIGITAL_HEALTHCARE_AI"]["information_confidence"], "7")
        self.assertEqual(rows["TELEHEALTH_BEHAVIORAL_HEALTH"]["valuation"], "8")
        self.assertEqual(rows["PHARMA_CHANNEL_AND_PRIVACY_RISK"]["gate_only"], "true")
        self.assertEqual(rows["PHARMA_CHANNEL_AND_PRIVACY_RISK"]["eps_fcf"], "gate")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round60_stage_date_rows()}
        fields = {row["field"] for row in round60_price_field_rows()}

        self.assertIn("capacity_utilization", rows["CDMO_HEALTHCARE_CONTRACT"]["stage2"])
        self.assertIn("weekly_scripts", rows["OBESITY_GLP1_COMMERCIALIZATION"]["stage2"])
        self.assertIn("subgroup_performance_issue", rows["DIGITAL_HEALTHCARE_AI"]["stage4c"])
        self.assertIn("fda_ftc_scrutiny", rows["PHARMA_CHANNEL_AND_PRIVACY_RISK"]["stage4c"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "capacity_liters",
            "capacity_utilization",
            "us_operating_cost",
            "weekly_scripts",
            "insurance_coverage",
            "pbm_listing_flag",
            "prescription_conversion_rate",
            "cash_runway_months",
            "hospital_adoption_count",
            "paid_workflow_flag",
            "ai_model_auc",
            "subgroup_performance_risk",
            "vbp_price_control_flag",
            "asp_drop_flag",
            "fda_ftc_scrutiny_flag",
            "compounded_quality_issue_flag",
            "impairment_charge",
            "forecast_withdrawal_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND60_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r7_loop2_guardrails(self):
        summary = round60_summary()
        summary_md = render_round60_summary_markdown()
        guardrails = render_round60_green_guardrail_markdown()
        overlays = render_round60_risk_overlay_markdown()
        price_plan = render_round60_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 16)
        self.assertEqual(summary["case_candidate_count"], 17)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 8)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["stage4c_case_count"], 7)
        self.assertEqual(summary["green_possible_count"], 4)
        self.assertEqual(summary["watch_yellow_first_count"], 7)
        self.assertEqual(summary["redteam_first_count"], 5)
        self.assertEqual(summary["gate_only_target_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R7 Loop 2", summary_md)
        self.assertIn("Do not apply R7 Loop-2 v2.0 weights", guardrails)
        self.assertIn("APPROVAL_WITHOUT_UPTAKE", overlays)
        self.assertIn("lilly_foundayo_prescription_uptake_case", price_plan)
        self.assertIn("bluebird_gene_therapy_cash_crunch_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round60_r7_loop2_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r7_loop2_round60.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round60_r7_loop2_v2.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND60_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round60_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round60_r7_loop2_biotech_healthcare_device", text)


if __name__ == "__main__":
    unittest.main()
