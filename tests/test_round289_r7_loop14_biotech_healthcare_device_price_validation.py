from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round289_r7_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round289_r7_loop14_biotech_healthcare_device_price_validation import (
    ROUND289_CASE_CANDIDATES,
    ROUND289_GREEN_FORBIDDEN_PATTERNS,
    ROUND289_GREEN_REQUIRED_FIELDS,
    ROUND289_HARD_4C_GATES,
    ROUND289_LARGE_SECTOR,
    ROUND289_PRICE_VALIDATION_FIELDS,
    ROUND289_REQUIRED_TARGET_ALIASES,
    ROUND289_SHADOW_WEIGHT_ROWS,
    ROUND289_STAGE4B_WATCH_TRIGGERS,
    render_round289_green_gate_review_markdown,
    render_round289_stage4b_4c_review_markdown,
    round289_audit_payload,
    round289_case_records,
    round289_case_rows,
    round289_deep_sub_archetype_rows,
    round289_shadow_weight_rows,
    round289_summary,
    write_round289_r7_loop14_reports,
)


class Round289R7Loop14BiotechHealthcareDevicePriceValidationTests(unittest.TestCase):
    def test_round289_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND289_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND289_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND289_REQUIRED_TARGET_ALIASES["BIO_CMO_US_LOCALIZATION_STAGE2"],
            E2RArchetype.BIO_CMO_US_LOCALIZATION_STAGE2.value,
        )
        self.assertEqual(
            ROUND289_REQUIRED_TARGET_ALIASES["BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE"],
            E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE.value,
        )
        self.assertEqual(
            ROUND289_REQUIRED_TARGET_ALIASES["GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE"],
            E2RArchetype.GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE.value,
        )

    def test_round289_archetype_definitions_capture_loop14_gates(self) -> None:
        bio_cmo = archetype_definition(E2RArchetype.BIO_CMO_US_LOCALIZATION_STAGE2)
        biosimilar = archetype_definition(E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2)
        vaccine = archetype_definition(E2RArchetype.VACCINE_CDMO_MA_EVENT_PREMIUM)
        blockbuster = archetype_definition(E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE)
        oncology = archetype_definition(E2RArchetype.ONCOLOGY_LICENSE_ROYALTY_STAGE2)
        aesthetic = archetype_definition(E2RArchetype.AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2)
        tech_export = archetype_definition(E2RArchetype.KOREAN_BIOTECH_TECH_EXPORT_STAGE2)
        hard_ref = archetype_definition(E2RArchetype.GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE)

        self.assertIn("facility utilization", bio_cmo.stage3_high_conviction_signals)
        self.assertIn("FDA inspection / tech transfer", bio_cmo.stage3_high_conviction_signals)
        self.assertIn("tariff savings", biosimilar.stage3_high_conviction_signals)
        self.assertIn("M&A without utilization", vaccine.false_positive_patterns)
        self.assertIn("30-40% adoption", blockbuster.stage3_high_conviction_signals)
        self.assertIn("patent/IP freedom-to-operate", blockbuster.stage3_high_conviction_signals)
        self.assertIn("manufacturing inspection issue", oncology.stage4c_thesis_break_signals)
        self.assertIn("physician adoption", aesthetic.stage3_high_conviction_signals)
        self.assertIn("tech export upfront only", tech_export.false_positive_patterns)
        self.assertIn("clinical hold", hard_ref.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round289_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND289_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round289_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round289_summary()
        self.assertEqual(summary["round_id"], "round_217")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 7)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["sector_hard_4c_reference_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 8)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["price_moved_without_evidence_count"], 1)
        self.assertEqual(summary["unknown_alignment_count"], 5)
        self.assertEqual(summary["false_positive_score_count"], 1)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["direct_KRX_hard_4c_confirmed"])
        self.assertTrue(summary["sector_hard_4c_reference_confirmed"])

    def test_core_cases_capture_reported_price_and_execution_anchors(self) -> None:
        by_id = {case.case_id: case for case in ROUND289_CASE_CANDIDATES}
        samsung = by_id["r7_loop14_samsung_biologics_gsk_us_facility"]
        celltrion = by_id["r7_loop14_celltrion_us_factory_tariff_hedge"]
        sk = by_id["r7_loop14_sk_bioscience_idt_biologika_ma"]
        alteogen = by_id["r7_loop14_alteogen_keytruda_qlex_sc_formulation"]

        self.assertEqual(samsung.primary_archetype, E2RArchetype.BIO_CMO_US_LOCALIZATION_STAGE2)
        self.assertEqual(samsung.event_mae_pct, -0.4)
        self.assertEqual(samsung.extra_price_metrics["facility_capacity_liters"], 60000)
        self.assertEqual(samsung.extra_price_metrics["relative_underperformance_pp"], -2.4)
        self.assertEqual(samsung.score_price_alignment, "evidence_good_but_price_failed")
        self.assertFalse(samsung.extra_price_metrics["facility_utilization_confirmed"])

        self.assertEqual(celltrion.primary_archetype, E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2)
        self.assertEqual(celltrion.extra_price_metrics["factory_acquisition_value_usd_mn"], 330.0)
        self.assertEqual(celltrion.extra_price_metrics["additional_capacity_investment_krw_bn"], 700.0)
        self.assertFalse(celltrion.extra_price_metrics["product_transfer_confirmed"])

        self.assertEqual(sk.primary_archetype, E2RArchetype.VACCINE_CDMO_MA_EVENT_PREMIUM)
        self.assertEqual(sk.event_mfe_pct, 11.7)
        self.assertEqual(sk.extra_price_metrics["deal_value_krw_bn"], 339.0)
        self.assertEqual(sk.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(sk.rerating_result, "event_premium")

        self.assertEqual(alteogen.primary_archetype, E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE)
        self.assertEqual(alteogen.stage3_date.isoformat(), "2025-09-19")
        self.assertEqual(alteogen.extra_price_metrics["keytruda_2024_sales_usd_bn"], 30.0)
        self.assertEqual(alteogen.extra_price_metrics["target_peak_adoption_pct_range"], "30-40")
        self.assertTrue(alteogen.extra_price_metrics["patent_dispute_watch"])
        self.assertFalse(alteogen.extra_price_metrics["royalty_conversion_confirmed"])

    def test_yuhan_hugel_adel_and_global_hard_reference_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND289_CASE_CANDIDATES}
        yuhan = by_id["r7_loop14_yuhan_lazertinib_jnj_rybrevant_approval"]
        hugel = by_id["r7_loop14_hugel_letybo_us_aesthetic_launch"]
        adel = by_id["r7_loop14_adel_sanofi_alzheimers_tech_export_reference"]
        hard_ref = by_id["r7_loop14_global_clinical_fda_failure_hard_reference"]

        self.assertEqual(yuhan.primary_archetype, E2RArchetype.ONCOLOGY_LICENSE_ROYALTY_STAGE2)
        self.assertEqual(yuhan.extra_price_metrics["rybrevant_peak_sales_expectation_usd_bn"], 5.0)
        self.assertEqual(yuhan.extra_price_metrics["later_crl_related_to"], "pre-approval inspection at manufacturing facility")
        self.assertIn("manufacturing_inspection_CRL_watch", yuhan.red_flag_fields)

        self.assertEqual(hugel.primary_archetype, E2RArchetype.AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2)
        self.assertEqual(hugel.extra_price_metrics["product"], "Letybo / Botulax")
        self.assertTrue(hugel.extra_price_metrics["category_safety_watch"])
        self.assertFalse(hugel.extra_price_metrics["physician_adoption_confirmed"])

        self.assertEqual(adel.primary_archetype, E2RArchetype.KOREAN_BIOTECH_TECH_EXPORT_STAGE2)
        self.assertEqual(adel.symbol, "unlisted")
        self.assertEqual(adel.extra_price_metrics["deal_value_max_usd_bn"], 1.04)
        self.assertEqual(adel.extra_price_metrics["upfront_payment_usd_mn"], 80.0)
        self.assertFalse(adel.extra_price_metrics["listed_stock_readthrough_confirmed"])

        self.assertEqual(hard_ref.primary_archetype, E2RArchetype.GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE)
        self.assertEqual(hard_ref.case_type, "4c_thesis_break")
        self.assertFalse(hard_ref.hard_4c_confirmed)
        self.assertTrue(hard_ref.sector_hard_4c_reference_confirmed)
        self.assertEqual(hard_ref.extra_price_metrics["hillevax_event_mae_pct"], -87.6)
        self.assertEqual(hard_ref.extra_price_metrics["corcept_event_mae_pct"], -50.8)
        self.assertEqual(hard_ref.rerating_result, "thesis_break")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND289_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND289_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND289_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round289_shadow_weight_rows()}
        deep_rows = round289_deep_sub_archetype_rows()
        green_markdown = render_round289_green_gate_review_markdown()
        stage_markdown = render_round289_stage4b_4c_review_markdown()

        self.assertIn("facility_utilization_confirmed", required)
        self.assertIn("patent_ip_freedom_to_operate_confirmed", required)
        self.assertIn("facility_acquisition_only", forbidden)
        self.assertIn("clinical_hold_or_CRL", forbidden)
        self.assertIn("global_partner_name_rally_before_milestones", ROUND289_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("pivotal_trial_primary_endpoint_failure", ROUND289_HARD_4C_GATES)
        self.assertIn("clinical_failure_drawdown_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("HilleVax", stage_markdown)
        self.assertIn("sector hard 4C reference", stage_markdown)
        self.assertEqual(len(ROUND289_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["BIO_CMO_US_LOCALIZATION_STAGE2"]["facility_utilization"], "+5")
        self.assertEqual(shadow_rows["GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE"]["hard4c_sensitivity"], "+5")
        self.assertTrue(any("Keytruda Qlex" in row["terms"] for row in deep_rows))
        self.assertTrue(any("HilleVax" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round289_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_289.md")
        self.assertEqual(audit["round_id"], "round_217")
        self.assertEqual(audit["large_sector"], ROUND289_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertFalse(audit["summary"]["direct_KRX_hard_4c_confirmed"])
        self.assertTrue(audit["summary"]["sector_hard_4c_reference_confirmed"])
        self.assertIn("do_not_use_round289_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round289_r7_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round289_case_rows()
            self.assertEqual(len(records), len(ROUND289_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND289_CASE_CANDIDATES))
            self.assertIn("Alteogen", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("facility_utilization_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("clinical_failure_drawdown_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["facility_capacity_liters"], 60000)


if __name__ == "__main__":
    unittest.main()
