from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round284_r2_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round284_r2_loop14_ai_semiconductor_electronics_price_validation import (
    ROUND284_CASE_CANDIDATES,
    ROUND284_GREEN_FORBIDDEN_PATTERNS,
    ROUND284_GREEN_REQUIRED_FIELDS,
    ROUND284_HARD_4C_GATES,
    ROUND284_LARGE_SECTOR,
    ROUND284_PRICE_VALIDATION_FIELDS,
    ROUND284_REQUIRED_TARGET_ALIASES,
    ROUND284_SHADOW_WEIGHT_ROWS,
    ROUND284_STAGE4B_WATCH_TRIGGERS,
    render_round284_green_gate_review_markdown,
    render_round284_stage4b_4c_review_markdown,
    round284_audit_payload,
    round284_case_records,
    round284_case_rows,
    round284_deep_sub_archetype_rows,
    round284_shadow_weight_rows,
    round284_summary,
    write_round284_r2_loop14_reports,
)


class Round284R2Loop14AISemiconductorElectronicsPriceValidationTests(unittest.TestCase):
    def test_round284_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND284_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND284_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND284_REQUIRED_TARGET_ALIASES["HBM_DOMINANCE_STAGE3_AND_4B"],
            E2RArchetype.HBM_DOMINANCE_STAGE3_AND_4B.value,
        )
        self.assertEqual(
            ROUND284_REQUIRED_TARGET_ALIASES["AI_INFRA_MEMORY_SUPPLY_MOU_4B"],
            E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B.value,
        )
        self.assertEqual(
            ROUND284_REQUIRED_TARGET_ALIASES["CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH"],
            E2RArchetype.CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH.value,
        )

    def test_round284_archetype_definitions_capture_r2_loop14_gates(self) -> None:
        hynix = archetype_definition(E2RArchetype.HBM_DOMINANCE_STAGE3_AND_4B)
        samsung = archetype_definition(E2RArchetype.SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH)
        hanmi = archetype_definition(E2RArchetype.TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM)
        innotek = archetype_definition(E2RArchetype.ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2)
        display = archetype_definition(E2RArchetype.OLED_PORTFOLIO_RESTRUCTURING_STAGE2)
        fabless = archetype_definition(E2RArchetype.KOREAN_AI_CHIP_FABLESS_STAGE2)
        stargate = archetype_definition(E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B)
        lg = archetype_definition(E2RArchetype.CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH)

        self.assertIn("actual HBM allocation", str(hynix.stage3_high_conviction_signals))
        self.assertIn("strike or shutdown disrupting memory supply", samsung.stage4c_thesis_break_signals)
        self.assertIn("rumored customer PO", hanmi.false_positive_patterns)
        self.assertIn("on-device AI expectation only", innotek.false_positive_patterns)
        self.assertIn("capacity capex without utilization", display.false_positive_patterns)
        self.assertIn("unlisted AI chip readthrough", fabless.false_positive_patterns)
        self.assertIn("LOI or MOU without binding contract", stargate.false_positive_patterns)
        self.assertIn("AI memory shortage treated as positive for OEM", lg.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round284_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND284_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)
            self.assertIn("hard_4c_watch_confirmed_true", record.green_guardrails)
            self.assertIn("do_not_use_round284_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round284_summary()
        self.assertEqual(summary["round_id"], "round_212")
        self.assertEqual(summary["large_sector"], "AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["event_premium_or_result_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["overheat_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["hard_4c_watch_case_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["stage4c_watch_count"], 2)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["false_positive_score_count"], 1)
        self.assertEqual(summary["unknown_alignment_count"], 3)
        self.assertEqual(summary["aligned_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["hard_4c_confirmed"])
        self.assertTrue(summary["hard_4c_watch_confirmed"])

    def test_round284_cases_keep_ai_semiconductor_anchors_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND284_CASE_CANDIDATES}
        hynix = by_id["r2_loop14_sk_hynix_hbm_dominance_stage3_4b"]
        samsung = by_id["r2_loop14_samsung_hbm_catchup_labor_4c_watch"]
        hanmi = by_id["r2_loop14_hanmi_tc_bonder_hbm_equipment_4b"]
        innotek = by_id["r2_loop14_lg_innotek_ai_iphone_component_price_failed"]
        display = by_id["r2_loop14_lg_display_oled_restructuring_stage2"]
        reb = by_id["r2_loop14_rebellions_sapeon_korean_ai_chip_stage2"]
        stargate = by_id["r2_loop14_samsung_sk_openai_stargate_memory_mou_4b"]
        lg = by_id["r2_loop14_lg_electronics_component_cost_4c_watch"]

        self.assertEqual(hynix.primary_archetype, E2RArchetype.HBM_DOMINANCE_STAGE3_AND_4B)
        self.assertEqual(hynix.extra_price_metrics["q2_2024_op_krw_trn"], 5.47)
        self.assertEqual(hynix.extra_price_metrics["q4_2025_op_krw_trn"], 19.2)
        self.assertEqual(hynix.extra_price_metrics["hbm_market_share_q4_2025_pct"], 61)
        self.assertEqual(hynix.extra_price_metrics["market_cap_may_2026_usd_bn"], 942)
        self.assertEqual(hynix.score_price_alignment, "aligned")

        self.assertEqual(samsung.primary_archetype, E2RArchetype.SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH)
        self.assertEqual(samsung.extra_price_metrics["hbm_china_customer_share_context_pct"], 20)
        self.assertEqual(samsung.extra_price_metrics["kospi_7000_session_samsung_mfe_pct"], 14.4)
        self.assertEqual(samsung.extra_price_metrics["strike_threat_workers"], 50000)
        self.assertTrue(samsung.hard_4c_watch_confirmed)

        self.assertEqual(hanmi.primary_archetype, E2RArchetype.TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM)
        self.assertEqual(hanmi.extra_price_metrics["sk_hynix_supply_deal_krw_bn"], 21.48)
        self.assertEqual(hanmi.extra_price_metrics["micron_rumor_event_high_price_krw"], 139100)
        self.assertFalse(hanmi.extra_price_metrics["micron_deal_confirmed_at_source_date"])
        self.assertEqual(hanmi.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(innotek.primary_archetype, E2RArchetype.ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2)
        self.assertEqual(innotek.stage2_price_anchor, 272000)
        self.assertEqual(innotek.extra_price_metrics["q2_op_estimate_krw_bn"], 106.4)
        self.assertEqual(innotek.extra_price_metrics["op_estimate_above_consensus_pct"], 31.2)
        self.assertEqual(innotek.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(display.primary_archetype, E2RArchetype.OLED_PORTFOLIO_RESTRUCTURING_STAGE2)
        self.assertEqual(display.extra_price_metrics["guangzhou_lcd_sale_usd_bn"], 1.54)
        self.assertEqual(display.extra_price_metrics["oled_infrastructure_investment_krw_trn"], 1.1)
        self.assertFalse(display.extra_price_metrics["oled_utilization_confirmed"])

        self.assertEqual(reb.primary_archetype, E2RArchetype.KOREAN_AI_CHIP_FABLESS_STAGE2)
        self.assertEqual(reb.extra_price_metrics["waed_ventures_investment_usd_mn"], 15)
        self.assertEqual(reb.extra_price_metrics["total_funding_usd_mn"], 225)
        self.assertFalse(reb.extra_price_metrics["listed_stock_direct_revenue_confirmed"])

        self.assertEqual(stargate.primary_archetype, E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B)
        self.assertEqual(stargate.extra_price_metrics["sk_hynix_close_mfe_pct"], 10.0)
        self.assertEqual(stargate.extra_price_metrics["openai_dram_wafer_demand_per_month"], 900000)
        self.assertFalse(stargate.extra_price_metrics["binding_take_or_pay_contract_confirmed"])

        self.assertEqual(lg.primary_archetype, E2RArchetype.CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH)
        self.assertEqual(lg.extra_price_metrics["q4_2025_net_loss_krw_bn"], 725.90)
        self.assertEqual(lg.extra_price_metrics["q4_2025_operating_loss_krw_bn"], 109.00)
        self.assertTrue(lg.hard_4c_watch_confirmed)
        self.assertEqual(lg.score_price_alignment, "false_positive_score")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND284_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND284_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND284_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round284_shadow_weight_rows()}
        deep_rows = round284_deep_sub_archetype_rows()
        green_markdown = render_round284_green_gate_review_markdown()
        stage_markdown = render_round284_stage4b_4c_review_markdown()

        self.assertIn("actual_hbm_allocation_confirmed", required)
        self.assertIn("equipment_PO_to_revenue_confirmed", required)
        self.assertIn("labor_supply_continuity_confirmed", required)
        self.assertIn("LOI_or_MOU_without_binding_contract", forbidden)
        self.assertIn("unlisted_AI_chip_readthrough", forbidden)
        self.assertIn("AI_memory_MOU_LOI_10pct_plus_rally", ROUND284_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("component_cost_spike_crushing_OEM_margins", ROUND284_HARD_4C_GATES)
        self.assertIn("strike_export_control_risk_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Strong Watch Gates", stage_markdown)
        self.assertEqual(len(ROUND284_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["HBM_DOMINANCE_STAGE3_AND_4B"]["actual_hbm_allocation"], "+5")
        self.assertEqual(shadow_rows["TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH"]["hard_4c_sensitivity"], "+4")
        self.assertTrue(any("SK Hynix" in row["terms"] for row in deep_rows))
        self.assertTrue(any("OpenAI Stargate" in row["terms"] for row in deep_rows))
        self.assertTrue(any("LG Electronics" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round284_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_284.md")
        self.assertEqual(audit["round_id"], "round_212")
        self.assertEqual(audit["large_sector"], ROUND284_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertFalse(audit["summary"]["hard_4c_confirmed"])
        self.assertTrue(audit["summary"]["hard_4c_watch_confirmed"])
        self.assertIn("do_not_use_round284_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round284_r2_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round284_case_rows()
            self.assertEqual(len(records), len(ROUND284_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND284_CASE_CANDIDATES))
            self.assertIn("SK Hynix", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_hbm_allocation_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("AI_INFRA_MEMORY_SUPPLY_MOU_4B", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("strike_export_control_risk_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["q2_2024_op_krw_trn"], 5.47)


if __name__ == "__main__":
    unittest.main()
