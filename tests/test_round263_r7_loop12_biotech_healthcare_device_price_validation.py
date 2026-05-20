from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round263_r7_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round263_r7_loop12_biotech_healthcare_device_price_validation import (
    ROUND263_CASE_CANDIDATES,
    ROUND263_GREEN_FORBIDDEN_PATTERNS,
    ROUND263_GREEN_REQUIRED_FIELDS,
    ROUND263_HARD_4C_GATES,
    ROUND263_LARGE_SECTOR,
    ROUND263_PRICE_VALIDATION_FIELDS,
    ROUND263_REQUIRED_TARGET_ALIASES,
    ROUND263_SCORE_ADJUSTMENTS,
    ROUND263_SHADOW_WEIGHT_ROWS,
    ROUND263_STAGE4B_WATCH_TRIGGERS,
    render_round263_green_gate_review_markdown,
    render_round263_stage4b_4c_review_markdown,
    round263_audit_payload,
    round263_case_records,
    round263_case_rows,
    round263_deep_sub_archetype_rows,
    round263_shadow_weight_rows,
    round263_summary,
    write_round263_r7_loop12_reports,
)


class Round263R7Loop12BiotechHealthcareDevicePriceValidationTests(unittest.TestCase):
    def test_round263_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND263_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND263_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND263_REQUIRED_TARGET_ALIASES["AESTHETIC_EBD_GLOBAL_BUYOUT"],
            E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT.value,
        )
        self.assertEqual(
            ROUND263_REQUIRED_TARGET_ALIASES["BOTULINUM_TOXIN_US_LAUNCH"],
            E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH.value,
        )
        self.assertEqual(
            ROUND263_REQUIRED_TARGET_ALIASES["MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE"],
            E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE.value,
        )
        self.assertEqual(
            ROUND263_REQUIRED_TARGET_ALIASES["DENTAL_IMPLANT_GLOBAL_M_AND_A"],
            E2RArchetype.DENTAL_IMPLANT_GLOBAL_M_AND_A.value,
        )

    def test_round263_archetype_definitions_capture_green_guards(self) -> None:
        ebd = archetype_definition(E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT)
        toxin = archetype_definition(E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH)
        unsafe_toxin = archetype_definition(E2RArchetype.UNAPPROVED_TOXIN_SAFETY_TRUST_4C)
        ai = archetype_definition(E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE)
        dental = archetype_definition(E2RArchetype.DENTAL_IMPLANT_GLOBAL_M_AND_A)

        self.assertIn("listed-equity tracking remains open", ebd.stage3_high_conviction_signals)
        self.assertIn("repeat injection volume", toxin.stage3_high_conviction_signals)
        self.assertIn("unapproved distribution", unsafe_toxin.stage4c_thesis_break_signals)
        self.assertIn("reimbursement", ai.stage3_high_conviction_signals)
        self.assertIn("external validation or AUC score treated as Stage 3-Green alone", ai.false_positive_patterns)
        self.assertIn("M&A rumor or target rally treated as Korean listed Green", dental.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round263_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND263_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)
            self.assertIn("do_not_treat_fda_approval_mna_auc_k_aesthetic_ai_diagnosis_or_medical_policy_as_green_alone", record.green_guardrails)

        summary = round263_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["watch_case_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["price_moved_without_evidence_count"], 1)
        self.assertEqual(summary["reported_price_anchor_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_ebd_beauty_device_classys_and_hugel_cases_are_guarded(self) -> None:
        by_id = {case.case_id: case for case in ROUND263_CASE_CANDIDATES}
        jeisys = by_id["r7_loop12_jeisys_medical_ebd_global_buyout"]
        apr = by_id["r7_loop12_apr_medicube_device_crossover"]
        classys = by_id["r7_loop12_classys_aesthetic_device_export_platform"]
        hugel = by_id["r7_loop12_hugel_letybo_us_toxin_launch"]

        self.assertEqual(jeisys.primary_archetype, E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT)
        self.assertEqual(jeisys.stage2_price_anchor, 12860.0)
        self.assertEqual(jeisys.extra_price_metrics["deal_value_to_revenue_x"], 6.93)
        self.assertIn("delisting_tracking_gap", jeisys.red_flag_fields)

        self.assertEqual(apr.primary_archetype, E2RArchetype.BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER)
        self.assertEqual(apr.mfe_1d, 300.0)
        self.assertEqual(apr.extra_price_metrics["market_value_usd_bn"], 6.0)
        self.assertIn("single_device_concentration", apr.red_flag_fields)

        self.assertEqual(classys.primary_archetype, E2RArchetype.AESTHETIC_DEVICE_EXPORT_PLATFORM)
        self.assertEqual(classys.extra_price_metrics["bain_stake_pct"], 60.84)
        self.assertEqual(classys.extra_price_metrics["export_countries_min"], 60.0)
        self.assertEqual(classys.price_validation_status, "price_data_unavailable_after_deep_search")

        self.assertEqual(hugel.primary_archetype, E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH)
        self.assertEqual(hugel.extra_price_metrics["letybo_unit_price_low_usd"], 9.0)
        self.assertEqual(hugel.extra_price_metrics["relative_unit_price_discount_low_case_pct"], 33.3)
        self.assertIn("provider_adoption_unconfirmed", hugel.red_flag_fields)

    def test_safety_ai_policy_and_dental_event_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND263_CASE_CANDIDATES}
        medytox = by_id["r7_loop12_medytox_innotox_unauthorized_distribution"]
        lunit = by_id["r7_loop12_lunit_insight_dbt_validation_not_revenue"]
        quota = by_id["r7_loop12_medical_quota_doctors_strike_disruption"]
        dental = by_id["r7_loop12_osstem_zimvie_dental_mna_event"]

        self.assertEqual(medytox.primary_archetype, E2RArchetype.UNAPPROVED_TOXIN_SAFETY_TRUST_4C)
        self.assertEqual(medytox.stage4c_date.isoformat(), "2025-07-01")
        self.assertFalse(medytox.hard_4c_confirmed)
        self.assertIn("patient_safety_risk", medytox.red_flag_fields)

        self.assertEqual(lunit.primary_archetype, E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE)
        self.assertEqual(lunit.extra_price_metrics["exam_count"], 163449.0)
        self.assertEqual(lunit.extra_price_metrics["overall_auc"], 0.91)
        self.assertEqual(lunit.extra_price_metrics["calcification_auc"], 0.80)
        self.assertEqual(lunit.case_type, "failed_rerating")

        self.assertEqual(quota.primary_archetype, E2RArchetype.MEDICAL_SERVICE_DISRUPTION_POLICY_4C)
        self.assertEqual(quota.extra_price_metrics["trainee_doctor_resignation_share_pct"], 90.0)
        self.assertEqual(quota.extra_price_metrics["quota_2030_increase_pct"], 26.6)
        self.assertIn("procedure_volume_unconfirmed", quota.red_flag_fields)

        self.assertEqual(dental.primary_archetype, E2RArchetype.DENTAL_IMPLANT_GLOBAL_M_AND_A)
        self.assertEqual(dental.case_type, "event_premium")
        self.assertEqual(dental.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(dental.stage2_price_anchor, 21.31)
        self.assertEqual(dental.mfe_1d, 12.5)

    def test_green_gate_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND263_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND263_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND263_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND263_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round263_shadow_weight_rows()}
        deep_rows = round263_deep_sub_archetype_rows()
        green_markdown = render_round263_green_gate_review_markdown()
        stage_markdown = render_round263_stage4b_4c_review_markdown()

        self.assertIn("procedure_or_prescription_volume_confirmed", required)
        self.assertIn("safety_counterfeit_and_unauthorized_distribution_risk_passed", required)
        self.assertIn("fda_approval_only", forbidden)
        self.assertIn("external_validation_only", forbidden)
        self.assertIn("ai_validation_paper_before_reimbursement", ROUND263_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("counterfeit_or_unauthorized_distribution_regulatory_action", ROUND263_HARD_4C_GATES)
        self.assertIn("regulatory_safety_or_policy_gate", fields)
        self.assertIn("external_validation_without_revenue", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("AUC 0.91", green_markdown)
        self.assertIn("r7_loop12_medytox_innotox_unauthorized_distribution", stage_markdown)
        self.assertEqual(len(ROUND263_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["BOTULINUM_TOXIN_US_LAUNCH"]["provider_adoption"], "+5")
        self.assertEqual(shadow_rows["MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE"]["event_penalty"], "-5")
        self.assertTrue(any("Face" not in row["terms"] for row in deep_rows))
        self.assertTrue(any("Lunit" in row["terms"] for row in deep_rows))
        self.assertTrue(any("ZimVie" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round263_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_263.md")
        self.assertEqual(audit["round_id"], "round_191")
        self.assertEqual(audit["large_sector"], ROUND263_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round263_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round263_r7_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round263_case_rows()
            self.assertEqual(len(records), len(ROUND263_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND263_CASE_CANDIDATES))
            self.assertIn("Jeisys", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("procedure_or_prescription_volume_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("BOTULINUM_TOXIN_US_LAUNCH", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("regulatory_safety_or_policy_gate", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["deal_value_to_revenue_x"], 6.93)


if __name__ == "__main__":
    unittest.main()
