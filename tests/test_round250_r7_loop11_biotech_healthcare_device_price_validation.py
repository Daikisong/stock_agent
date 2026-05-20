from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round250_r7_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round250_r7_loop11_biotech_healthcare_device_price_validation import (
    ROUND250_CASE_CANDIDATES,
    ROUND250_DEEP_SUB_ARCHETYPES,
    ROUND250_GREEN_FORBIDDEN_PATTERNS,
    ROUND250_GREEN_REQUIRED_FIELDS,
    ROUND250_HARD_4C_GATES,
    ROUND250_LARGE_SECTOR,
    ROUND250_PRICE_VALIDATION_FIELDS,
    ROUND250_REQUIRED_TARGET_ALIASES,
    ROUND250_SCORE_ADJUSTMENTS,
    ROUND250_SHADOW_WEIGHT_ROWS,
    ROUND250_STAGE4B_WATCH_TRIGGERS,
    render_round250_green_gate_review_markdown,
    render_round250_stage4b_4c_review_markdown,
    round250_audit_payload,
    round250_case_records,
    round250_case_rows,
    round250_deep_sub_archetype_rows,
    round250_shadow_weight_rows,
    round250_summary,
    write_round250_r7_loop11_reports,
)


class Round250R7Loop11BiotechHealthcareDevicePriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND250_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND250_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND250_REQUIRED_TARGET_ALIASES["BIO_PLATFORM_ROYALTY_CONVERSION"],
            E2RArchetype.BIO_PLATFORM_ROYALTY_CONVERSION.value,
        )
        self.assertEqual(
            ROUND250_REQUIRED_TARGET_ALIASES["KOREAN_NEW_DRUG_GLOBAL_APPROVAL"],
            E2RArchetype.KOREAN_NEW_DRUG_GLOBAL_APPROVAL.value,
        )
        self.assertEqual(
            ROUND250_REQUIRED_TARGET_ALIASES["AUTOIMMUNE_PARTNER_TRIAL_FAILURE"],
            E2RArchetype.AUTOIMMUNE_PARTNER_TRIAL_FAILURE.value,
        )
        self.assertEqual(
            ROUND250_REQUIRED_TARGET_ALIASES["APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN"],
            E2RArchetype.APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN.value,
        )

    def test_archetype_definitions_capture_round250_gates(self) -> None:
        royalty = archetype_definition(E2RArchetype.BIO_PLATFORM_ROYALTY_CONVERSION)
        new_drug = archetype_definition(E2RArchetype.KOREAN_NEW_DRUG_GLOBAL_APPROVAL)
        cmo = archetype_definition(E2RArchetype.CMO_M_AND_A_TRANSITION)
        partner_failure = archetype_definition(E2RArchetype.AUTOIMMUNE_PARTNER_TRIAL_FAILURE)
        approval_only = archetype_definition(E2RArchetype.APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN)

        self.assertIn("royalty recognition", royalty.stage3_high_conviction_signals)
        self.assertIn("patent challenge loss", royalty.stage4c_thesis_break_signals)
        self.assertIn("prescription uptake", new_drug.stage3_high_conviction_signals)
        self.assertIn("utilization", cmo.stage3_high_conviction_signals)
        self.assertIn("partner trial failure", partner_failure.stage4c_thesis_break_signals)
        self.assertIn("FDA approval or AUC score treated as Stage 3-Green alone", approval_only.false_positive_patterns)

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round250_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)
            self.assertIn("do_not_treat_approval_clinical_validation_policy_mna_or_facility_headline_as_green", record.green_guardrails)

        summary = round250_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_platform_new_drug_cdmo_and_mna_cases_block_green_until_commercial_conversion(self) -> None:
        by_id = {case.case_id: case for case in ROUND250_CASE_CANDIDATES}
        alteogen = by_id["r7_loop11_alteogen_keytruda_sc_platform_royalty"]
        yuhan = by_id["r7_loop11_yuhan_lazertinib_global_approval"]
        samsung_bio = by_id["r7_loop11_samsung_biologics_gsk_facility_price_failed"]
        celltrion = by_id["r7_loop11_celltrion_us_tariff_hedge_factory"]
        sk_bio = by_id["r7_loop11_sk_bioscience_idt_cmo_mna"]

        self.assertEqual(alteogen.primary_archetype, E2RArchetype.BIO_PLATFORM_ROYALTY_CONVERSION)
        self.assertEqual(alteogen.stage2_date.isoformat(), "2025-03-27")
        self.assertEqual(alteogen.extra_price_metrics["keytruda_2024_sales_usd_bn"], 30.0)
        self.assertEqual(alteogen.extra_price_metrics["expected_sc_adoption_high_pct"], 40.0)
        self.assertIn("patent_challenge_possible", alteogen.red_flag_fields)

        self.assertEqual(yuhan.primary_archetype, E2RArchetype.KOREAN_NEW_DRUG_GLOBAL_APPROVAL)
        self.assertEqual(yuhan.stage4c_date.isoformat(), "2024-12-16")
        self.assertEqual(yuhan.extra_price_metrics["jj_peak_sales_expectation_usd_bn"], 5.0)
        self.assertIn("prescription_uptake_unconfirmed", yuhan.red_flag_fields)

        self.assertEqual(samsung_bio.primary_archetype, E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY)
        self.assertEqual(samsung_bio.score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(samsung_bio.mae_1d, -0.4)
        self.assertEqual(samsung_bio.extra_price_metrics["relative_underperformance_pp"], -2.4)

        self.assertEqual(celltrion.extra_price_metrics["combined_acquisition_plus_expansion_krw_trn"], 1.183)
        self.assertIn("utilization_unverified", celltrion.red_flag_fields)

        self.assertEqual(sk_bio.primary_archetype, E2RArchetype.CMO_M_AND_A_TRANSITION)
        self.assertEqual(sk_bio.stage4b_date.isoformat(), "2024-06-27")
        self.assertEqual(sk_bio.mfe_1d, 11.7)
        self.assertEqual(sk_bio.score_price_alignment, "price_moved_without_evidence")

    def test_partner_failure_medical_ai_and_policy_relief_are_redteam_or_event_premium(self) -> None:
        by_id = {case.case_id: case for case in ROUND250_CASE_CANDIDATES}
        hanall = by_id["r7_loop11_hanall_immunovant_batoclimab_ted_failure"]
        lunit = by_id["r7_loop11_lunit_medical_ai_external_validation"]
        policy = by_id["r7_loop11_biopharma_tariff_policy_relief_basket"]

        self.assertEqual(hanall.primary_archetype, E2RArchetype.AUTOIMMUNE_PARTNER_TRIAL_FAILURE)
        self.assertEqual(hanall.stage4c_date.isoformat(), "2026-04-02")
        self.assertFalse(hanall.hard_4c_confirmed)
        self.assertEqual(hanall.extra_price_metrics["immunovant_event_mae_pct"], -4.8)
        self.assertEqual(hanall.rerating_result, "thesis_break")

        self.assertEqual(lunit.primary_archetype, E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION)
        self.assertEqual(lunit.extra_price_metrics["exam_count"], 163449.0)
        self.assertEqual(lunit.extra_price_metrics["overall_auc"], 0.91)
        self.assertIn("subgroup_performance_risk", lunit.red_flag_fields)
        self.assertEqual(lunit.round_case_type, "insufficient_evidence")

        self.assertEqual(policy.primary_archetype, E2RArchetype.BIOPHARMA_POLICY_TARIFF_RELIEF)
        self.assertEqual(policy.case_type, "event_premium")
        self.assertEqual(policy.mfe_1d, 3.97)
        self.assertEqual(policy.extra_price_metrics["samsung_biologics_event_mfe_pct"], 6.23)
        self.assertEqual(policy.rerating_result, "policy_event_rerating")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND250_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND250_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND250_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND250_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round250_shadow_weight_rows()}
        deep_rows = round250_deep_sub_archetype_rows()
        green_markdown = render_round250_green_gate_review_markdown()
        stage_markdown = render_round250_stage4b_4c_review_markdown()

        self.assertIn("commercial_revenue_or_royalty_recognition", required)
        self.assertIn("reimbursement_payer_or_asp_confirmed", required)
        self.assertIn("fda_approval_only", forbidden)
        self.assertIn("medical_ai_auc_without_reimbursement", forbidden)
        self.assertIn("royalty_before_recognition_platform_rerating", ROUND250_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("partner_trial_failure", ROUND250_HARD_4C_GATES)
        self.assertIn("sales_base_or_peak_sales_expectation", fields)
        self.assertIn("royalty_revenue_visibility", axes)
        self.assertIn("external_validation_without_revenue", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("FDA approval", green_markdown)
        self.assertIn("r7_loop11_hanall_immunovant_batoclimab_ted_failure", stage_markdown)
        self.assertEqual(len(ROUND250_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["BIO_PLATFORM_ROYALTY_CONVERSION"]["royalty_visibility"], "+5")
        self.assertEqual(shadow_rows["BIOPHARMA_POLICY_TARIFF_RELIEF"]["event_penalty"], "-5")
        self.assertTrue(any("Keytruda" in row["deep_sub_archetype"] for row in deep_rows))
        self.assertIn("Lunit INSIGHT DBT external validation", ROUND250_DEEP_SUB_ARCHETYPES)

    def test_audit_payload_cli_and_writer_outputs(self) -> None:
        audit = round250_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_250.md")
        self.assertEqual(audit["analyst_round_id"], "round_178")
        self.assertEqual(audit["large_sector"], ROUND250_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round250_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round250_r7_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round250_case_rows()
            self.assertEqual(len(records), len(ROUND250_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND250_CASE_CANDIDATES))
            self.assertIn("Alteogen", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("royalty_revenue_visibility", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("BIO_PLATFORM_ROYALTY_CONVERSION", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("partner_trial_failure", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["expected_sc_adoption_high_pct"], 40.0)


if __name__ == "__main__":
    unittest.main()
