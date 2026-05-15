import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round47_r7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round47_r7_biotech_healthcare_device import (
    ROUND47_CASE_CANDIDATES,
    ROUND47_PRICE_FIELDS,
    ROUND47_SCORE_TARGETS,
    render_round47_green_guardrail_markdown,
    render_round47_price_validation_plan_markdown,
    render_round47_summary_markdown,
    round47_case_candidate_rows,
    round47_case_records,
    round47_price_field_rows,
    round47_score_profile_rows,
    round47_stage_date_rows,
    round47_summary,
    target_for,
    write_round47_r7_reports,
)


class Round47R7BiotechHealthcareDeviceTests(unittest.TestCase):
    def test_round47_targets_cover_r7_archetypes(self):
        labels = {target.target_id for target in ROUND47_SCORE_TARGETS}

        self.assertEqual(len(labels), 16)
        self.assertIn("CDMO_HEALTHCARE_CONTRACT", labels)
        self.assertIn("CRO_CLINICAL_SERVICE", labels)
        self.assertIn("BIOSIMILAR_COMMERCIALIZATION", labels)
        self.assertIn("OBESITY_GLP1_COMMERCIALIZATION", labels)
        self.assertIn("GENE_THERAPY_RARE_DISEASE", labels)
        self.assertIn("AI_DRUG_DISCOVERY_PLATFORM", labels)
        self.assertIn("DIGITAL_HEALTHCARE_AI", labels)
        self.assertIn("TELEHEALTH_BEHAVIORAL_HEALTH", labels)
        self.assertIn("BOTULINUM_AESTHETIC_REGULATED", labels)
        self.assertIn("DIAGNOSTICS_INFECTIOUS_DISEASE", labels)
        for target in ROUND47_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE)
            self.assertFalse(target.production_scoring_changed)

    def test_new_r7_canonical_archetypes_exist(self):
        expected = {
            E2RArchetype.CRO_CLINICAL_SERVICE,
            E2RArchetype.BIOSIMILAR_COMMERCIALIZATION,
            E2RArchetype.BIOSIMILAR_ORIGINATOR_DEFENSE,
            E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION,
            E2RArchetype.GENE_THERAPY_RARE_DISEASE,
            E2RArchetype.AI_DRUG_DISCOVERY_PLATFORM,
            E2RArchetype.DIGITAL_HEALTHCARE_AI,
            E2RArchetype.DIGITAL_HEALTHCARE_REMOTE_MEDICINE,
            E2RArchetype.TELEHEALTH_BEHAVIORAL_HEALTH,
            E2RArchetype.PHARMA_CHANNEL_AND_PRIVACY_RISK,
            E2RArchetype.MEDICAL_DEVICE_DENTAL_IMPLANT,
            E2RArchetype.BOTULINUM_AESTHETIC_REGULATED,
            E2RArchetype.DIAGNOSTICS_INFECTIOUS_DISEASE,
            E2RArchetype.ANIMAL_HEALTH_BIOSECURITY,
        }

        self.assertTrue(expected.issubset(set(E2RArchetype)))

    def test_cdmo_glp1_and_medical_device_are_green_possible_but_guardrailed(self):
        cdmo = target_for("CDMO_HEALTHCARE_CONTRACT")
        glp1 = target_for("OBESITY_GLP1_COMMERCIALIZATION")
        implant = target_for("MEDICAL_DEVICE_DENTAL_IMPLANT")

        self.assertIsNotNone(cdmo)
        self.assertIsNotNone(glp1)
        self.assertIsNotNone(implant)
        assert cdmo is not None
        assert glp1 is not None
        assert implant is not None
        self.assertEqual(cdmo.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("capacity_utilization", cdmo.green_conditions)
        self.assertIn("underutilization", cdmo.red_flags)
        self.assertEqual(glp1.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("prescription_volume", glp1.green_conditions)
        self.assertIn("compounded_alternative", glp1.red_flags)
        self.assertEqual(implant.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("recurring_procedure_consumable", implant.green_conditions)
        self.assertIn("vbp_price_control", implant.red_flags)

    def test_pre_revenue_ai_diagnostics_and_telehealth_are_not_auto_green(self):
        gene = target_for("GENE_THERAPY_RARE_DISEASE")
        ai_drug = target_for("AI_DRUG_DISCOVERY_PLATFORM")
        diagnostics = target_for("DIAGNOSTICS_INFECTIOUS_DISEASE")
        telehealth = target_for("TELEHEALTH_BEHAVIORAL_HEALTH")

        for target in (gene, ai_drug, diagnostics, telehealth):
            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)

        assert gene is not None
        assert ai_drug is not None
        assert diagnostics is not None
        assert telehealth is not None
        self.assertIn("cash_burn", gene.red_flags)
        self.assertIn("no_approved_drug", ai_drug.red_flags)
        self.assertIn("one_off_demand", diagnostics.red_flags)
        self.assertIn("impairment", telehealth.red_flags)

    def test_case_records_validate_and_keep_price_backfill_open(self):
        records = round47_case_records()

        self.assertEqual(len(records), len(ROUND47_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("approval_or_clinical_news_is_not_revenue", record.green_guardrails)
            self.assertIn("commercialization_reimbursement_fcf_required_for_green", record.green_guardrails)

    def test_required_round47_cases_are_present_with_stage_dates(self):
        records = {record.case_id: record for record in round47_case_records()}

        self.assertEqual(str(records["samsung_biologics_gsk_us_facility_case"].stage2_date), "2025-12-22")
        self.assertEqual(records["samsung_biologics_cdmo_contract_reference"].case_type, "structural_success")
        self.assertEqual(str(records["straumann_dental_implant_growth_case"].stage2_date), "2026-02-18")
        self.assertEqual(str(records["botox_counterfeit_fda_warning_case"].stage4c_date), "2025-11-05")
        self.assertEqual(str(records["lunit_mammography_ai_subgroup_case"].stage2_date), "2025-03-17")
        self.assertEqual(str(records["lilly_oral_glp1_foundayo_case"].stage2_date), "2026-05-08")
        self.assertEqual(str(records["novo_wegovy_outlook_cut_case"].stage4c_date), "2025-05-07")
        self.assertEqual(str(records["hims_glp1_strategy_shift_case"].stage4c_date), "2026-05-11")
        self.assertEqual(str(records["bluebird_gene_therapy_cash_crunch_case"].stage4c_date), "2025-02-21")
        self.assertEqual(str(records["bluebird_revised_offer_event_premium_case"].stage2_date), "2025-05-14")
        self.assertEqual(str(records["charles_river_cro_funding_crunch_case"].stage4c_date), "2024-08-07")
        self.assertEqual(str(records["teladoc_betterhelp_impairment_case"].stage4c_date), "2024-08-01")
        self.assertEqual(str(records["recursion_exscientia_ai_drug_platform_case"].stage2_date), "2024-08-08")
        self.assertEqual(records["bluebird_revised_offer_event_premium_case"].case_type, "event_premium")

    def test_score_profile_rows_mark_no_production_change(self):
        rows = {row["target_id"]: row for row in round47_score_profile_rows()}

        self.assertEqual(rows["CDMO_HEALTHCARE_CONTRACT"]["large_sector"], "BIOTECH_HEALTHCARE_DEVICE")
        self.assertEqual(rows["CDMO_HEALTHCARE_CONTRACT"]["production_scoring_changed"], "false")
        self.assertEqual(rows["GENE_THERAPY_RARE_DISEASE"]["posture"], "REDTEAM_FIRST")
        self.assertIn("stage4c_conditions", rows["DIGITAL_HEALTHCARE_AI"])

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round47_stage_date_rows()}
        fields = {row["field"] for row in round47_price_field_rows()}

        self.assertIn("OBESITY_GLP1_COMMERCIALIZATION", rows)
        self.assertIn("weekly_scripts", rows["OBESITY_GLP1_COMMERCIALIZATION"]["stage2"])
        for field in (
            "stage2_price",
            "MFE_180D",
            "capacity_liters",
            "capacity_utilization",
            "weekly_scripts",
            "insurance_coverage",
            "cash_runway_months",
            "hospital_adoption_count",
            "ai_model_auc",
            "subgroup_performance_risk",
            "vbp_price_control_flag",
            "counterfeit_safety_flag",
            "impairment_charge",
            "forecast_withdrawal_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND47_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r7_guardrails(self):
        summary = round47_summary()
        summary_md = render_round47_summary_markdown()
        guardrails = render_round47_green_guardrail_markdown()
        price_plan = render_round47_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 16)
        self.assertEqual(summary["case_candidate_count"], len(ROUND47_CASE_CANDIDATES))
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("clinical, approval, AI", summary_md)
        self.assertIn("Do not apply these R7 v1.0 weights", guardrails)
        self.assertIn("approval, clinical success, AI model AUC", guardrails)
        self.assertIn("bluebird_gene_therapy_cash_crunch_case", price_plan)
        self.assertIn("recursion_exscientia_ai_drug_platform_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round47_r7_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r7_round47.jsonl",
                score_profile_path=Path(tmp) / "score_profiles.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND47_CASE_CANDIDATES))

    def test_case_matrix_records_are_not_production_inputs(self):
        rows = round47_case_candidate_rows()

        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(row["production_input"], "false")

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

    def test_production_scoring_modules_do_not_import_round47_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round47_r7_biotech_healthcare_device", text)


if __name__ == "__main__":
    unittest.main()
