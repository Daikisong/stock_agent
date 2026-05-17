import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round99_r7_loop5_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round99_r7_loop5_biotech_healthcare_device import (
    ROUND99_CASE_CANDIDATES,
    ROUND99_PRICE_FIELDS,
    ROUND99_SCORE_TARGETS,
    render_round99_green_guardrail_markdown,
    render_round99_price_validation_plan_markdown,
    render_round99_risk_overlay_markdown,
    render_round99_summary_markdown,
    round99_case_candidate_rows,
    round99_case_records,
    round99_price_field_rows,
    round99_score_profile_rows,
    round99_stage_date_rows,
    round99_summary,
    round99_target_for,
    write_round99_r7_loop5_reports,
)


class Round99R7Loop5BiotechHealthcareDeviceTests(unittest.TestCase):
    def test_round99_targets_cover_r7_loop5_archetypes(self):
        labels = {target.target_id for target in ROUND99_SCORE_TARGETS}

        self.assertEqual(len(labels), 27)
        for label in (
            "CDMO_HEALTHCARE_CONTRACT",
            "CDMO_US_TARIFF_HEDGE_CAPACITY",
            "CDMO_ADC_CELL_GENE_CAPABILITY",
            "CRO_CLINICAL_SERVICE",
            "BIOSIMILAR_COMMERCIALIZATION",
            "BIOSIMILAR_ACCESS_CASH_PAY",
            "BIOSIMILAR_PATENT_LITIGATION",
            "OBESITY_GLP1_COMMERCIALIZATION",
            "ORAL_GLP1_MAINTENANCE_THERAPY",
            "GLP1_PRICE_WAR_OVERLAY",
            "GLP1_TELEHEALTH_CHANNEL",
            "COMPOUNDED_GLP1_REGULATORY_RISK",
            "GENE_THERAPY_RARE_DISEASE",
            "AI_DRUG_DISCOVERY_PLATFORM",
            "DIGITAL_HEALTHCARE_AI",
            "MEDICAL_AI_EXTERNAL_VALIDATION",
            "DIGITAL_HEALTHCARE_REMOTE_MEDICINE",
            "TELEHEALTH_BEHAVIORAL_HEALTH",
            "MEDICAL_DEVICE_HEALTHCARE_EXPORT",
            "MEDICAL_DEVICE_DENTAL_IMPLANT",
            "SURGICAL_ROBOT_INSTALLED_BASE",
            "BOTULINUM_AESTHETIC_REGULATED",
            "DIAGNOSTICS_INFECTIOUS_DISEASE",
            "COMMERCIALIZATION_FAILURE_OVERLAY",
            "REIMBURSEMENT_ACCESS_OVERLAY",
            "DEVICE_SAFETY_COUNTERFEIT_OVERLAY",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND99_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE)
            self.assertFalse(target.production_scoring_changed)
        self.assertEqual(E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY.value, "CDMO_US_TARIFF_HEDGE_CAPACITY")
        self.assertEqual(E2RArchetype.CDMO_ADC_CELL_GENE_CAPABILITY.value, "CDMO_ADC_CELL_GENE_CAPABILITY")
        self.assertEqual(E2RArchetype.BIOSIMILAR_ACCESS_CASH_PAY.value, "BIOSIMILAR_ACCESS_CASH_PAY")
        self.assertEqual(E2RArchetype.ORAL_GLP1_MAINTENANCE_THERAPY.value, "ORAL_GLP1_MAINTENANCE_THERAPY")
        self.assertEqual(E2RArchetype.GLP1_PRICE_WAR_OVERLAY.value, "GLP1_PRICE_WAR_OVERLAY")
        self.assertEqual(E2RArchetype.COMPOUNDED_GLP1_REGULATORY_RISK.value, "COMPOUNDED_GLP1_REGULATORY_RISK")
        self.assertEqual(E2RArchetype.DISCLOSURE_CONFIDENCE_CAP.value, "DISCLOSURE_CONFIDENCE_CAP")

    def test_cdmo_glp1_and_devices_are_green_possible_but_guardrailed(self):
        cdmo = round99_target_for("CDMO_HEALTHCARE_CONTRACT")
        glp1 = round99_target_for("OBESITY_GLP1_COMMERCIALIZATION")
        device = round99_target_for("MEDICAL_DEVICE_HEALTHCARE_EXPORT")
        implant = round99_target_for("MEDICAL_DEVICE_DENTAL_IMPLANT")
        robot = round99_target_for("SURGICAL_ROBOT_INSTALLED_BASE")

        for target in (cdmo, glp1, device, implant, robot):
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.GREEN_POSSIBLE)
        assert cdmo is not None
        assert glp1 is not None
        assert device is not None
        assert implant is not None
        assert robot is not None
        self.assertIn("capacity_utilization", cdmo.green_conditions)
        self.assertIn("underutilization", cdmo.red_flags)
        self.assertIn("prescription_volume", glp1.green_conditions)
        self.assertIn("compounded_alternative", glp1.red_flags)
        self.assertIn("consumable_repeat_revenue", device.green_conditions)
        self.assertIn("vbp_price_control", implant.red_flags)
        self.assertIn("instruments_accessories_revenue", robot.green_conditions)
        self.assertIn("hospital_capex", robot.red_flags)

    def test_pre_revenue_ai_telehealth_and_diagnostics_are_redteam_first(self):
        for target_id in (
            "BIOSIMILAR_PATENT_LITIGATION",
            "GLP1_PRICE_WAR_OVERLAY",
            "COMPOUNDED_GLP1_REGULATORY_RISK",
            "GENE_THERAPY_RARE_DISEASE",
            "AI_DRUG_DISCOVERY_PLATFORM",
            "TELEHEALTH_BEHAVIORAL_HEALTH",
            "DIAGNOSTICS_INFECTIOUS_DISEASE",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            target = round99_target_for(target_id)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)

        gene = round99_target_for("GENE_THERAPY_RARE_DISEASE")
        ai_drug = round99_target_for("AI_DRUG_DISCOVERY_PLATFORM")
        diagnostics = round99_target_for("DIAGNOSTICS_INFECTIOUS_DISEASE")
        telehealth = round99_target_for("TELEHEALTH_BEHAVIORAL_HEALTH")
        glp1_channel = round99_target_for("GLP1_TELEHEALTH_CHANNEL")
        assert gene is not None
        assert ai_drug is not None
        assert diagnostics is not None
        assert telehealth is not None
        assert glp1_channel is not None
        self.assertEqual(glp1_channel.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("cash_burn", gene.red_flags)
        self.assertIn("no_approved_drug", ai_drug.red_flags)
        self.assertIn("one_off_demand", diagnostics.red_flags)
        self.assertIn("impairment", telehealth.red_flags)
        self.assertIn("revenue_recognition", glp1_channel.red_flags)

    def test_redteam_overlays_are_gate_only(self):
        for target_id in (
            "BIOSIMILAR_PATENT_LITIGATION",
            "GLP1_PRICE_WAR_OVERLAY",
            "COMPOUNDED_GLP1_REGULATORY_RISK",
            "COMMERCIALIZATION_FAILURE_OVERLAY",
            "REIMBURSEMENT_ACCESS_OVERLAY",
            "DEVICE_SAFETY_COUNTERFEIT_OVERLAY",
        ):
            target = round99_target_for(target_id)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertTrue(target.gate_only)
            self.assertEqual(target.score_weight.eps_fcf, "gate")
        compounded = round99_target_for("COMPOUNDED_GLP1_REGULATORY_RISK")
        price_war = round99_target_for("GLP1_PRICE_WAR_OVERLAY")
        patent = round99_target_for("BIOSIMILAR_PATENT_LITIGATION")
        device = round99_target_for("DEVICE_SAFETY_COUNTERFEIT_OVERLAY")
        assert compounded is not None
        assert price_war is not None
        assert patent is not None
        assert device is not None
        self.assertIn("fda_crackdown", compounded.stage4c_conditions)
        self.assertIn("gross_to_net_pressure", price_war.red_flags)
        self.assertIn("unapproved_copycat", "|".join(compounded.red_flags))
        self.assertIn("launch_delay", patent.red_flags)
        self.assertIn("counterfeit_product", device.red_flags)

    def test_disclosure_confidence_cap_is_cap_only_not_gate_only(self):
        cap = round99_target_for("DISCLOSURE_CONFIDENCE_CAP")

        assert cap is not None
        self.assertEqual(cap.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertFalse(cap.gate_only)
        self.assertEqual(cap.score_weight.eps_fcf, "cap")
        self.assertEqual(cap.score_weight.information_confidence, "+")
        self.assertIn("disclosure_confidence_low", cap.red_flags)
        self.assertIn("stage3_cap_until_key_fields_verified", cap.stage3_conditions)

    def test_required_round99_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round99_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND99_CASE_CANDIDATES))
        self.assertEqual(rows["samsung_biologics_gsk_us_facility_case"]["stage2_date"], "2025-12-22")
        self.assertEqual(rows["samsung_biologics_cdmo_capacity_reference"]["stage2_date"], "")
        self.assertEqual(rows["samsung_biologics_gsk_us_facility_case"]["target_id"], "CDMO_US_TARIFF_HEDGE_CAPACITY")
        self.assertEqual(rows["intuitive_surgical_q1_2026_procedure_growth_case"]["stage2_date"], "2026-04-22")
        self.assertEqual(rows["straumann_dental_implant_vbp_case"]["stage2_date"], "2026-02-18")
        self.assertEqual(rows["lilly_foundayo_fda_approval_case"]["target_id"], "ORAL_GLP1_MAINTENANCE_THERAPY")
        self.assertEqual(rows["lilly_foundayo_fda_approval_case"]["stage2_date"], "2026-04-01")
        self.assertEqual(rows["lilly_foundayo_switch_maintenance_case"]["stage2_date"], "2026-05-12")
        self.assertEqual(rows["boehringer_goodrx_humira_biosimilar_case"]["target_id"], "BIOSIMILAR_ACCESS_CASH_PAY")
        self.assertEqual(rows["boehringer_goodrx_humira_biosimilar_case"]["stage2_date"], "2024-07-18")
        self.assertEqual(rows["novo_glp1_price_pressure_case"]["target_id"], "GLP1_PRICE_WAR_OVERLAY")
        self.assertEqual(rows["novo_glp1_price_pressure_case"]["stage4c_date"], "2026-02-03")
        self.assertEqual(rows["hims_branded_glp1_pivot_loss_case"]["stage4c_date"], "2026-05-12")
        self.assertEqual(rows["hims_compounded_glp1_crackdown_case"]["target_id"], "COMPOUNDED_GLP1_REGULATORY_RISK")
        self.assertEqual(rows["hims_compounded_glp1_crackdown_case"]["stage4c_date"], "2026-02-07")
        self.assertEqual(rows["bluebird_gene_therapy_cash_crunch_case"]["stage4c_date"], "2025-02-21")
        self.assertEqual(rows["charles_river_cro_funding_crunch_case"]["stage4c_date"], "2024-08-07")
        self.assertEqual(rows["teladoc_betterhelp_impairment_case"]["stage4c_date"], "2024-08-01")
        self.assertEqual(rows["recursion_exscientia_ai_drug_case"]["stage2_date"], "2024-08-08")
        self.assertEqual(rows["lunit_dbt_subgroup_validation_case"]["target_id"], "MEDICAL_AI_EXTERNAL_VALIDATION")
        self.assertEqual(rows["lunit_dbt_subgroup_validation_case"]["stage2_date"], "2025-03-17")
        self.assertEqual(rows["amgen_samsung_bioepis_biosimilar_litigation_case"]["target_id"], "BIOSIMILAR_PATENT_LITIGATION")
        self.assertEqual(rows["amgen_samsung_bioepis_biosimilar_litigation_case"]["stage4c_date"], "2024-08-13")
        self.assertEqual(rows["botox_counterfeit_fda_warning_case"]["stage4c_date"], "2025-11-05")

    def test_case_records_validate_and_keep_round99_guardrails(self):
        records = round99_case_records()

        self.assertEqual(len(records), len(ROUND99_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("approval_or_clinical_news_is_not_revenue", record.green_guardrails)
            self.assertIn("commercialization_reimbursement_fcf_required_for_green", record.green_guardrails)
            self.assertIn("capacity_without_utilization_is_not_stage3", record.green_guardrails)
            self.assertIn("compounded_glp1_channel_is_redteam_gate", record.green_guardrails)
            self.assertIn("external_validation_is_not_paid_deployment", record.green_guardrails)
            self.assertIn("do_not_invent_prescriptions_reimbursement_capacity_uptake_cash_runway_hospital_adoption_external_validation_or_stage_prices", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["samsung_biologics_cdmo_capacity_reference"].score_price_alignment, "aligned")
        self.assertEqual(by_id["intuitive_surgical_q1_2026_procedure_growth_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["boehringer_goodrx_humira_biosimilar_case"].primary_archetype.value, "BIOSIMILAR_ACCESS_CASH_PAY")
        self.assertEqual(by_id["novo_glp1_price_pressure_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["novo_glp1_price_pressure_case"].primary_archetype.value, "GLP1_PRICE_WAR_OVERLAY")
        self.assertEqual(by_id["bluebird_gene_therapy_cash_crunch_case"].score_price_alignment, "false_positive_score")
        self.assertEqual(by_id["lunit_dbt_subgroup_validation_case"].score_price_alignment, "unknown")
        self.assertEqual(by_id["lunit_dbt_subgroup_validation_case"].primary_archetype.value, "MEDICAL_AI_EXTERNAL_VALIDATION")
        self.assertEqual(by_id["amgen_samsung_bioepis_biosimilar_litigation_case"].primary_archetype.value, "BIOSIMILAR_PATENT_LITIGATION")
        self.assertEqual(by_id["botox_counterfeit_fda_warning_case"].primary_archetype.value, "DEVICE_SAFETY_COUNTERFEIT_OVERLAY")

    def test_score_profile_rows_match_round99_weight_table(self):
        rows = {row["target_id"]: row for row in round99_score_profile_rows()}

        self.assertEqual(rows["CDMO_HEALTHCARE_CONTRACT"]["structural_visibility"], "24")
        self.assertEqual(rows["CDMO_US_TARIFF_HEDGE_CAPACITY"]["structural_visibility"], "21")
        self.assertEqual(rows["CDMO_ADC_CELL_GENE_CAPABILITY"]["bottleneck_pricing"], "11")
        self.assertEqual(rows["CRO_CLINICAL_SERVICE"]["eps_fcf"], "16")
        self.assertEqual(rows["BIOSIMILAR_COMMERCIALIZATION"]["market_mispricing"], "12")
        self.assertEqual(rows["BIOSIMILAR_ACCESS_CASH_PAY"]["structural_visibility"], "15")
        self.assertEqual(rows["BIOSIMILAR_PATENT_LITIGATION"]["gate_only"], "true")
        self.assertEqual(rows["OBESITY_GLP1_COMMERCIALIZATION"]["valuation"], "8")
        self.assertEqual(rows["ORAL_GLP1_MAINTENANCE_THERAPY"]["eps_fcf"], "21")
        self.assertEqual(rows["ORAL_GLP1_MAINTENANCE_THERAPY"]["valuation"], "9")
        self.assertEqual(rows["GLP1_PRICE_WAR_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["GLP1_TELEHEALTH_CHANNEL"]["structural_visibility"], "15")
        self.assertEqual(rows["GLP1_TELEHEALTH_CHANNEL"]["valuation"], "7")
        self.assertEqual(rows["COMPOUNDED_GLP1_REGULATORY_RISK"]["gate_only"], "true")
        self.assertEqual(rows["GENE_THERAPY_RARE_DISEASE"]["eps_fcf"], "7")
        self.assertEqual(rows["MEDICAL_AI_EXTERNAL_VALIDATION"]["information_confidence"], "7")
        self.assertEqual(rows["DIGITAL_HEALTHCARE_AI"]["information_confidence"], "7")
        self.assertEqual(rows["TELEHEALTH_BEHAVIORAL_HEALTH"]["valuation"], "8")
        self.assertEqual(rows["SURGICAL_ROBOT_INSTALLED_BASE"]["eps_fcf"], "21")
        self.assertEqual(rows["DEVICE_SAFETY_COUNTERFEIT_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["information_confidence"], "+")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["gate_only"], "false")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round99_stage_date_rows()}
        fields = {row["field"] for row in round99_price_field_rows()}

        self.assertIn("capacity_utilization", rows["CDMO_HEALTHCARE_CONTRACT"]["stage2"])
        self.assertIn("technology_transfer", rows["CDMO_US_TARIFF_HEDGE_CAPACITY"]["stage2"])
        self.assertIn("regulatory_tech_transfer", rows["CDMO_ADC_CELL_GENE_CAPABILITY"]["stage2"])
        self.assertIn("prescription_conversion", rows["BIOSIMILAR_ACCESS_CASH_PAY"]["stage2"])
        self.assertIn("weekly_scripts", rows["OBESITY_GLP1_COMMERCIALIZATION"]["stage2"])
        self.assertIn("weekly_scripts", rows["ORAL_GLP1_MAINTENANCE_THERAPY"]["stage3"])
        self.assertIn("gross_to_net_pressure", rows["GLP1_PRICE_WAR_OVERLAY"]["stage4c"])
        self.assertIn("revenue_recognition_shock", rows["GLP1_TELEHEALTH_CHANNEL"]["stage4c"])
        self.assertIn("fda_crackdown", rows["COMPOUNDED_GLP1_REGULATORY_RISK"]["stage4c"])
        self.assertIn("stage3_cap_until_key_fields_verified", rows["DISCLOSURE_CONFIDENCE_CAP"]["stage3"])
        self.assertIn("subgroup_performance_issue", rows["DIGITAL_HEALTHCARE_AI"]["stage4c"])
        self.assertIn("external_validation", rows["MEDICAL_AI_EXTERNAL_VALIDATION"]["stage2"])
        self.assertIn("instruments_accessories_revenue", rows["SURGICAL_ROBOT_INSTALLED_BASE"]["stage2"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "contract_duration_months",
            "customer_name",
            "facility_location",
            "us_manufacturing_site_flag",
            "tariff_hedge_flag",
            "technology_transfer_flag",
            "capacity_liters",
            "capacity_utilization",
            "adc_capability_flag",
            "cell_gene_capability_flag",
            "us_operating_cost",
            "weekly_scripts",
            "prescriber_count",
            "new_prescriber_ratio",
            "script_growth_rate",
            "insurance_coverage",
            "pbm_listing_flag",
            "pbm_coverage_flag",
            "biosimilar_approval_flag",
            "interchangeable_flag",
            "pbm_exclusion_flag",
            "patent_litigation_flag",
            "prescription_conversion_rate",
            "biosimilar_prescription_volume",
            "price_discount_pct",
            "margin_compression_flag",
            "price_war_flag",
            "generic_competition_flag",
            "telehealth_channel_flag",
            "oral_glp1_flag",
            "maintenance_therapy_flag",
            "injection_to_pill_switch_flag",
            "self_pay_price",
            "boxed_warning_flag",
            "real_world_adherence_signal",
            "compounded_drug_flag",
            "fda_crackdown_flag",
            "doj_referral_flag",
            "unapproved_copycat_flag",
            "legal_cost",
            "restructuring_cost",
            "launch_date",
            "commercial_revenue",
            "milestone_payment",
            "big_pharma_partner",
            "pipeline_count",
            "ai_platform_flag",
            "approved_drug_count",
            "cash_runway_months",
            "cash_runway_years",
            "dilution_flag",
            "take_private_flag",
            "discounted_take_private_flag",
            "branded_drug_attach_rate",
            "revenue_recognition_issue_flag",
            "hospital_adoption_count",
            "paid_workflow_flag",
            "ai_model_auc",
            "external_validation_flag",
            "workflow_integration_flag",
            "subgroup_performance_risk",
            "surgical_robot_installed_base",
            "system_placements",
            "installed_base",
            "instruments_accessories_revenue",
            "hospital_capex_risk",
            "procedure_mix_risk",
            "glp1_bariatric_slowdown_flag",
            "bariatric_slowdown_flag",
            "vbp_price_control_flag",
            "asp_change",
            "fda_warning_flag",
            "licensed_channel_flag",
            "asp_drop_flag",
            "fda_ftc_scrutiny_flag",
            "compounded_quality_issue_flag",
            "advertising_cost_change",
            "impairment_charge",
            "forecast_withdrawal_flag",
            "opendart_rcept_no",
            "opendart_detail_fetched_flag",
            "disclosure_confidence_score",
            "detail_parser_confidence",
            "disclosure_signal_class",
            "routine_disclosure_flag",
            "risk_disclosure_flag",
            "high_signal_disclosure_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND99_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r7_loop5_guardrails(self):
        summary = round99_summary()
        summary_md = render_round99_summary_markdown()
        guardrails = render_round99_green_guardrail_markdown()
        overlays = render_round99_risk_overlay_markdown()
        price_plan = render_round99_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 27)
        self.assertEqual(summary["case_candidate_count"], 17)
        self.assertEqual(summary["structural_success_count"], 2)
        self.assertEqual(summary["success_candidate_count"], 7)
        self.assertEqual(summary["event_premium_count"], 0)
        self.assertEqual(summary["stage4c_case_count"], 8)
        self.assertEqual(summary["green_possible_count"], 5)
        self.assertEqual(summary["watch_yellow_first_count"], 11)
        self.assertEqual(summary["redteam_first_count"], 11)
        self.assertEqual(summary["gate_only_target_count"], 6)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("R7 Loop 5", summary_md)
        self.assertIn("Do not apply R7 Loop-5 v5.0 weights", guardrails)
        self.assertIn("APPROVAL_WITHOUT_UPTAKE", overlays)
        self.assertIn("US_CAPACITY_TARIFF_HEDGE_BUT_DELAYED_PRICE", overlays)
        self.assertIn("COMPOUNDED_GLP1_REGULATORY_BREAK", overlays)
        self.assertIn("MEDICAL_AI_EXTERNAL_VALIDATION", overlays)
        self.assertIn("BIOSIMILAR_PATENT_LITIGATION", overlays)
        self.assertIn("BIOSIMILAR_ACCESS_WITHOUT_UPTAKE", overlays)
        self.assertIn("GLP1_PRICE_WAR_4C", overlays)
        self.assertIn("DISCLOSURE_CONFIDENCE_CAP", overlays)
        self.assertIn("SURGICAL_ROBOT_RECURRING_CONSUMABLE_SUCCESS", overlays)
        self.assertIn("lilly_foundayo_switch_maintenance_case", price_plan)
        self.assertIn("hims_branded_glp1_pivot_loss_case", price_plan)
        self.assertIn("intuitive_surgical_q1_2026_procedure_growth_case", price_plan)
        self.assertIn("bluebird_gene_therapy_cash_crunch_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round99_r7_loop5_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r7_loop5_round99.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round99_r7_loop5_v5.csv",
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
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND99_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round99_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round99_r7_loop5_biotech_healthcare_device", text)


if __name__ == "__main__":
    unittest.main()
