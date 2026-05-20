from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round237_r7_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round237_r7_loop10_biotech_healthcare_device_price_validation import (
    ROUND237_CASE_CANDIDATES,
    ROUND237_DEEP_SUB_ARCHETYPES,
    ROUND237_GREEN_FORBIDDEN_PATTERNS,
    ROUND237_GREEN_REQUIRED_FIELDS,
    ROUND237_HARD_4C_GATES,
    ROUND237_PRICE_VALIDATION_FIELDS,
    ROUND237_REQUIRED_TARGET_ALIASES,
    ROUND237_SCORE_ADJUSTMENTS,
    ROUND237_SHADOW_WEIGHT_ROWS,
    ROUND237_STAGE4B_WATCH_TRIGGERS,
    render_round237_green_gate_review_markdown,
    render_round237_stage4b_4c_review_markdown,
    round237_audit_payload,
    round237_case_records,
    round237_case_rows,
    round237_deep_sub_archetype_rows,
    round237_shadow_weight_rows,
    round237_summary,
    write_round237_r7_loop10_reports,
)


class Round237R7Loop10BiotechHealthcareDevicePriceValidationTests(unittest.TestCase):
    def test_round237_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND237_REQUIRED_TARGET_ALIASES), 12)
        self.assertTrue(set(ROUND237_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND237_REQUIRED_TARGET_ALIASES["MEDICAL_AESTHETIC_DEVICE_GLOBALIZATION"],
            E2RArchetype.AESTHETIC_DEVICE_EXPORT_KOREA.value,
        )
        self.assertEqual(
            ROUND237_REQUIRED_TARGET_ALIASES["AUTOIMMUNE_PARTNER_TRIAL_FAILURE"],
            E2RArchetype.THESIS_BREAK_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND237_REQUIRED_TARGET_ALIASES["EVIDENCE_GOOD_BUT_PRICE_FAILED"],
            E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED.value,
        )

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round237_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)

        summary = round237_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4c_watch_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_aesthetic_botulinum_and_medical_ai_cases_do_not_skip_commercialization_gate(self) -> None:
        by_id = {case.case_id: case for case in ROUND237_CASE_CANDIDATES}
        jeisys = by_id["r7_loop10_jeisys_aesthetic_device_take_private"]
        hugel = by_id["r7_loop10_hugel_letybo_us_launch"]
        lunit = by_id["r7_loop10_lunit_medical_ai_external_validation"]

        self.assertEqual(jeisys.primary_archetype, E2RArchetype.AESTHETIC_DEVICE_EXPORT_KOREA)
        self.assertEqual(jeisys.stage2_date.isoformat(), "2024-09-11")
        self.assertIsNone(jeisys.stage3_date)
        self.assertEqual(jeisys.stage2_price_anchor, 12860.0)
        self.assertEqual(jeisys.extra_price_metrics["adjusted_pretax_margin_pct"], 29.0)
        self.assertIn("take_private_premium_only", jeisys.red_flag_fields)

        self.assertEqual(hugel.primary_archetype, E2RArchetype.BOTULINUM_US_MARKET_ENTRY)
        self.assertEqual(hugel.extra_price_metrics["low_end_discount_pct"], -25.0)
        self.assertEqual(hugel.extra_price_metrics["high_end_discount_pct"], -33.3)
        self.assertIn("us_sales_unverified", hugel.red_flag_fields)

        self.assertEqual(lunit.case_type, "failed_rerating")
        self.assertEqual(lunit.extra_price_metrics["exam_count"], 163449.0)
        self.assertEqual(lunit.extra_price_metrics["overall_auc"], 0.91)
        self.assertEqual(lunit.extra_price_metrics["precision"], 0.08)
        self.assertIn("subgroup_performance_risk", lunit.red_flag_fields)

    def test_cdmo_mna_tariff_hedge_and_partner_failure_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND237_CASE_CANDIDATES}
        sk_bio = by_id["r7_loop10_sk_bioscience_idt_cmo_mna"]
        celltrion = by_id["r7_loop10_celltrion_us_manufacturing_tariff_hedge"]
        samsung_bio = by_id["r7_loop10_samsung_biologics_gsk_facility_price_failed"]
        hanall = by_id["r7_loop10_hanall_immunovant_batoclimab_ted_failure"]

        self.assertEqual(sk_bio.case_type, "event_premium")
        self.assertEqual(sk_bio.stage4b_date.isoformat(), "2024-06-27")
        self.assertEqual(sk_bio.mfe_1d, 11.7)
        self.assertEqual(sk_bio.extra_price_metrics["implied_idt_equity_value_krw_bn"], 565.0)
        self.assertIn("mna_without_utilization", sk_bio.red_flag_fields)

        self.assertEqual(celltrion.primary_archetype, E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING)
        self.assertEqual(celltrion.extra_price_metrics["imclone_acquisition_usd_mn"], 330.0)
        self.assertEqual(celltrion.extra_price_metrics["combined_acquisition_plus_expansion_krw_trn"], 1.183)
        self.assertIn("utilization_unverified", celltrion.red_flag_fields)

        self.assertEqual(samsung_bio.primary_archetype, E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY)
        self.assertEqual(samsung_bio.mae_1d, -0.4)
        self.assertEqual(samsung_bio.extra_price_metrics["relative_underperformance_pp"], -2.4)
        self.assertEqual(samsung_bio.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(hanall.primary_archetype, E2RArchetype.THESIS_BREAK_4C_WATCH)
        self.assertEqual(hanall.stage4c_date.isoformat(), "2026-04-02")
        self.assertFalse(hanall.hard_4c_confirmed)
        self.assertEqual(hanall.extra_price_metrics["immunovant_event_mae_pct"], -4.8)
        self.assertIn("partner_trial_failure", hanall.red_flag_fields)

    def test_green_gate_4b_4c_and_shadow_weights_are_explicit(self) -> None:
        required = set(ROUND237_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND237_GREEN_FORBIDDEN_PATTERNS)
        review = render_round237_green_gate_review_markdown()
        stage_review = render_round237_stage4b_4c_review_markdown()
        weights = {row.archetype: row for row in ROUND237_SHADOW_WEIGHT_ROWS}

        self.assertIn("commercial_revenue_or_royalty_recognition", required)
        self.assertIn("reimbursement_payer_access_or_asp_confirmed", required)
        self.assertIn("external_validation_without_revenue", forbidden)
        self.assertIn("take_private_premium_only", forbidden)
        self.assertIn("partner_trial_failure", ROUND237_HARD_4C_GATES)
        self.assertIn("take_private_premium_peer_readthrough", ROUND237_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("r7_loop10_hanall_immunovant_batoclimab_ted_failure", stage_review)
        self.assertEqual(weights[E2RArchetype.AESTHETIC_DEVICE_EXPORT_KOREA].channel_penetration, 5)
        self.assertEqual(weights[E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION].event_penalty, -4)

    def test_deep_sub_archetypes_and_price_fields_cover_round237(self) -> None:
        fields = set(ROUND237_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND237_SCORE_ADJUSTMENTS}
        deep_rows = round237_deep_sub_archetype_rows()
        shadow_text = "\n".join(str(row) for row in round237_shadow_weight_rows())

        self.assertIn("transaction_value_or_facility_capacity", fields)
        self.assertIn("launch_price_or_discount", fields)
        self.assertIn("commercialization_gate_status", fields)
        self.assertIn("prescription_or_procedure_volume", axes)
        self.assertIn("external_validation_without_revenue", axes)
        self.assertIn("mna_without_utilization", axes)
        self.assertIn("Lunit INSIGHT DBT", ROUND237_DEEP_SUB_ARCHETYPES)
        self.assertEqual(len(deep_rows), len(ROUND237_DEEP_SUB_ARCHETYPES))
        self.assertIn("BOTULINUM_US_MARKET_ENTRY", shadow_text)

    def test_audit_payload_marks_non_production_round(self) -> None:
        audit = round237_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_237.md")
        self.assertEqual(audit["analyst_round_id"], "round_165")
        self.assertEqual(audit["large_sector"], Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round237_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round237_r7_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round237_case_rows()
            self.assertEqual(len(records), len(ROUND237_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND237_CASE_CANDIDATES))
            self.assertIn("Jeisys", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("approval_news_only", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("BOTULINUM_US_MARKET_ENTRY", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("partner_trial_failure", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["deal_value_usd_mn"], 742.0)


if __name__ == "__main__":
    unittest.main()
