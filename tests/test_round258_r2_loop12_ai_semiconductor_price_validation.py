from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round258_r2_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round258_r2_loop12_ai_semiconductor_price_validation import (
    ROUND258_CASE_CANDIDATES,
    ROUND258_GREEN_FORBIDDEN_PATTERNS,
    ROUND258_GREEN_REQUIRED_FIELDS,
    ROUND258_HARD_4C_GATES,
    ROUND258_LARGE_SECTOR,
    ROUND258_PRICE_VALIDATION_FIELDS,
    ROUND258_REQUIRED_TARGET_ALIASES,
    ROUND258_SCORE_ADJUSTMENTS,
    ROUND258_SHADOW_WEIGHT_ROWS,
    ROUND258_STAGE4B_WATCH_TRIGGERS,
    render_round258_green_gate_review_markdown,
    render_round258_stage4b_4c_review_markdown,
    round258_audit_payload,
    round258_case_records,
    round258_case_rows,
    round258_deep_sub_archetype_rows,
    round258_shadow_weight_rows,
    round258_summary,
    write_round258_r2_loop12_reports,
)


class Round258R2Loop12AISemiconductorPriceValidationTests(unittest.TestCase):
    def test_round258_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND258_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND258_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND258_REQUIRED_TARGET_ALIASES["MEMORY_HBM4_CAPACITY_LEADER"],
            E2RArchetype.MEMORY_HBM4_CAPACITY_LEADER.value,
        )
        self.assertEqual(
            ROUND258_REQUIRED_TARGET_ALIASES["HBM_CATCHUP_FOUNDRY_TURNAROUND"],
            E2RArchetype.HBM_CATCHUP_FOUNDRY_TURNAROUND.value,
        )
        self.assertEqual(
            ROUND258_REQUIRED_TARGET_ALIASES["AI_DEVICE_COMPONENT_OPTIONALITY"],
            E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY.value,
        )
        self.assertEqual(
            ROUND258_REQUIRED_TARGET_ALIASES["GEOPOLITICAL_EXPORT_CONTROL_OVERLAY"],
            E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY.value,
        )

    def test_round258_archetype_definitions_are_available(self) -> None:
        leader = archetype_definition(E2RArchetype.MEMORY_HBM4_CAPACITY_LEADER)
        catchup = archetype_definition(E2RArchetype.HBM_CATCHUP_FOUNDRY_TURNAROUND)
        bonder = archetype_definition(E2RArchetype.HBM_BONDER_EQUIPMENT_ORDER)
        device = archetype_definition(E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY)
        display = archetype_definition(E2RArchetype.DISPLAY_LCD_EXIT_OLED_TURNAROUND)
        export = archetype_definition(E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY)

        self.assertIn("record OP", leader.stage3_high_conviction_signals)
        self.assertIn("HBM4 volume visibility", leader.stage3_high_conviction_signals)
        self.assertIn("labor disruption", catchup.stage4c_thesis_break_signals)
        self.assertIn("unconfirmed media report treated as order", bonder.false_positive_patterns)
        self.assertIn("actual device volume", device.stage3_high_conviction_signals)
        self.assertIn("sustained OLED profit", display.stage3_high_conviction_signals)
        self.assertIn("equipment authorization loss", export.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round258_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND258_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round258_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 5)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["price_data_unavailable_count"], 2)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_sk_hynix_samsung_and_hanmi_paths_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND258_CASE_CANDIDATES}
        skh = by_id["r2_loop12_sk_hynix_hbm4_structural_success_4b"]
        samsung = by_id["r2_loop12_samsung_hbm4_foundry_labor_export_watch"]
        hanmi = by_id["r2_loop12_hanmi_hbm_bonder_order_rumor_4b"]

        self.assertEqual(skh.primary_archetype, E2RArchetype.MEMORY_HBM4_CAPACITY_LEADER)
        self.assertEqual(skh.stage3_date.isoformat(), "2025-10-29")
        self.assertEqual(skh.stage4b_date.isoformat(), "2026-05-14")
        self.assertEqual(skh.extra_price_metrics["market_cap_mfe_from_under_100b_pct"], 842.0)
        self.assertEqual(skh.extra_price_metrics["q3_2025_op_krw_trn"], 11.4)
        self.assertEqual(skh.stage_failure_type, "green_success")
        self.assertIn("market_cap_milestone_942bn_usd", skh.red_flag_fields)

        self.assertEqual(samsung.primary_archetype, E2RArchetype.HBM_CATCHUP_FOUNDRY_TURNAROUND)
        self.assertEqual(samsung.stage2_date.isoformat(), "2026-01-25")
        self.assertEqual(samsung.stage4c_date.isoformat(), "2025-09-01")
        self.assertEqual(samsung.extra_price_metrics["nvidia_tieup_price_anchor_krw"], 196800.0)
        self.assertEqual(samsung.extra_price_metrics["relative_outperformance_kospi7000_pp"], 7.95)
        self.assertIn("labor_strike_risk_45000_workers", samsung.red_flag_fields)
        self.assertEqual(samsung.score_price_alignment, "unknown")

        self.assertEqual(hanmi.primary_archetype, E2RArchetype.HBM_BONDER_EQUIPMENT_ORDER)
        self.assertEqual(hanmi.stage4b_date.isoformat(), "2024-03-28")
        self.assertEqual(hanmi.stage4b_price_anchor, 139100.0)
        self.assertEqual(hanmi.extra_price_metrics["micron_rumor_event_mfe_pct"], 22.0)
        self.assertIn("micron_deal_unconfirmed_media_report", hanmi.red_flag_fields)

    def test_design_device_display_cxmt_and_export_cases_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND258_CASE_CANDIDATES}
        gaon = by_id["r2_loop12_gaonchips_pfn_ai_design_house"]
        innotek = by_id["r2_loop12_lg_innotek_apple_ai_aeva_lidar"]
        display = by_id["r2_loop12_lg_display_lcd_exit_oled_turnaround"]
        cxmt = by_id["r2_loop12_jusung_mirae_cxmt_relief_watch"]
        export = by_id["r2_loop12_export_control_overlay_samsung_skh_hana_hanmi"]

        self.assertEqual(gaon.primary_archetype, E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER)
        self.assertEqual(gaon.price_validation_status, "price_data_unavailable_after_deep_search")
        self.assertEqual(gaon.extra_price_metrics["order_size"], "not_disclosed")
        self.assertEqual(gaon.round_stage_failure_label, "design_win_not_revenue")

        self.assertEqual(innotek.primary_archetype, E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY)
        self.assertEqual(innotek.extra_price_metrics["apple_ai_event_mfe_pct"], 19.0)
        self.assertEqual(innotek.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("lidar_optionality_without_volume", innotek.red_flag_fields)

        self.assertEqual(display.primary_archetype, E2RArchetype.DISPLAY_LCD_EXIT_OLED_TURNAROUND)
        self.assertEqual(display.extra_price_metrics["loss_surprise_vs_expected_pct"], 69.5)
        self.assertEqual(display.extra_price_metrics["guangzhou_lcd_sale_usd_bn"], 1.54)
        self.assertEqual(display.price_validation_status, "price_data_unavailable_after_deep_search")

        self.assertEqual(cxmt.primary_archetype, E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF)
        self.assertEqual(cxmt.extra_price_metrics["mirae_cxmt_revenue_share_1h2024_pct"], 15.0)
        self.assertEqual(cxmt.stage4c_date.isoformat(), "2024-12-03")
        self.assertEqual(cxmt.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(export.primary_archetype, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY)
        self.assertEqual(export.stage4c_date.isoformat(), "2025-09-01")
        self.assertFalse(export.hard_4c_confirmed)
        self.assertEqual(export.extra_price_metrics["sk_hynix_event_mae_pct"], -4.4)
        self.assertEqual(export.extra_price_metrics["veu_revocation_effective_delay_days"], 120)
        self.assertEqual(export.rerating_result, "thesis_break")
        self.assertEqual(export.round_alignment_label, "thesis_break_watch")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND258_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND258_GREEN_FORBIDDEN_PATTERNS)
        review = render_round258_green_gate_review_markdown()
        stage_review = render_round258_stage4b_4c_review_markdown()
        fields = set(ROUND258_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND258_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round258_shadow_weight_rows()}
        deep_rows = round258_deep_sub_archetype_rows()

        self.assertIn("revenue_recognition_path", required)
        self.assertIn("customer_concentration_china_labor_export_control_risk_passed", required)
        self.assertIn("unconfirmed_customer_rumor", forbidden)
        self.assertIn("export_control_risk_unresolved", forbidden)
        self.assertIn("hbm_customer_rumor_plus_20pct", ROUND258_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("china_fab_license_denial", ROUND258_HARD_4C_GATES)
        self.assertIn("labor_export_control_anchor", fields)
        self.assertIn("HBM_generation_transition", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("Hard 4C needs confirmed license denial", stage_review)
        self.assertEqual(len(ROUND258_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["MEMORY_HBM4_CAPACITY_LEADER"]["confirmed_customer_order"], "+5")
        self.assertEqual(shadow_rows["HBM_CATCHUP_FOUNDRY_TURNAROUND"]["china_labor_export_redteam"], "+5")
        self.assertEqual(shadow_rows["GEOPOLITICAL_EXPORT_CONTROL_OVERLAY"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("SK Hynix" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Aeva lidar" in row["terms"] for row in deep_rows))
        self.assertTrue(any("MATCH Act" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round258_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_258.md")
        self.assertEqual(audit["round_id"], "round_186")
        self.assertEqual(audit["large_sector"], ROUND258_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round258_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round258_r2_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round258_case_rows()
            self.assertEqual(len(records), len(ROUND258_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND258_CASE_CANDIDATES))
            self.assertIn("SK Hynix", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("unconfirmed_customer_rumor", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("GEOPOLITICAL_EXPORT_CONTROL_OVERLAY", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("MATCH Act", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["market_cap_mfe_from_under_100b_pct"], 842.0)


if __name__ == "__main__":
    unittest.main()
