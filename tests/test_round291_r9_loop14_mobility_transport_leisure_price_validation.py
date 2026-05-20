from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round291_r9_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round291_r9_loop14_mobility_transport_leisure_price_validation import (
    ROUND291_CASE_CANDIDATES,
    ROUND291_GREEN_FORBIDDEN_PATTERNS,
    ROUND291_GREEN_REQUIRED_FIELDS,
    ROUND291_HARD_4C_GATES,
    ROUND291_LARGE_SECTOR,
    ROUND291_PRICE_VALIDATION_FIELDS,
    ROUND291_REQUIRED_TARGET_ALIASES,
    ROUND291_SHADOW_WEIGHT_ROWS,
    ROUND291_STAGE4B_WATCH_TRIGGERS,
    render_round291_green_gate_review_markdown,
    render_round291_stage4b_4c_review_markdown,
    round291_audit_payload,
    round291_case_records,
    round291_case_rows,
    round291_deep_sub_archetype_rows,
    round291_shadow_weight_rows,
    round291_summary,
    write_round291_r9_loop14_reports,
)


class Round291R9Loop14MobilityTransportLeisurePriceValidationTests(unittest.TestCase):
    def test_round291_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND291_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND291_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND291_REQUIRED_TARGET_ALIASES["AUTO_TARIFF_HYBRID_MIX_STAGE2"],
            E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2.value,
        )
        self.assertEqual(
            ROUND291_REQUIRED_TARGET_ALIASES["AIRLINE_REMEDY_ROUTE_CARGO_STAGE2"],
            E2RArchetype.AIRLINE_REMEDY_ROUTE_CARGO_STAGE2.value,
        )
        self.assertEqual(
            ROUND291_REQUIRED_TARGET_ALIASES["USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE"],
            E2RArchetype.USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE.value,
        )

    def test_round291_archetype_definitions_capture_loop14_gates(self) -> None:
        tariff = archetype_definition(E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2)
        logistics = archetype_definition(E2RArchetype.AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH)
        airline = archetype_definition(E2RArchetype.AIRLINE_REMEDY_ROUTE_CARGO_STAGE2)
        ipo = archetype_definition(E2RArchetype.OVERSEAS_AUTO_IPO_FAILED_RERATING)
        safety = archetype_definition(E2RArchetype.AVIATION_SAFETY_HARD_4C)
        shipping = archetype_definition(E2RArchetype.CONTAINER_SHIPPING_RATE_EVENT_PREMIUM)
        used_car = archetype_definition(E2RArchetype.USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE)

        self.assertIn("tariff pass-through", tariff.stage3_high_conviction_signals)
        self.assertIn("route disruption", logistics.stage4c_thesis_break_signals)
        self.assertIn("delivery delays", logistics.stage4c_thesis_break_signals)
        self.assertIn("load factor", airline.stage3_high_conviction_signals)
        self.assertIn("weak IPO debut", ipo.stage4c_thesis_break_signals)
        self.assertIn("fatal aviation accident", safety.stage4c_thesis_break_signals)
        self.assertIn("contract-rate mix", shipping.stage3_high_conviction_signals)
        self.assertIn("storage congestion", used_car.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round291_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND291_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round291_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round291_summary()
        self.assertEqual(summary["round_id"], "round_219")
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["watch_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 6)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["false_positive_score_count"], 2)
        self.assertEqual(summary["unknown_alignment_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_auto_airline_logistics_cases_capture_required_metrics(self) -> None:
        by_id = {case.case_id: case for case in ROUND291_CASE_CANDIDATES}
        tariff = by_id["r9_loop14_hyundai_kia_us_tariff_hybrid_mix"]
        logistics = by_id["r9_loop14_hyundai_glovis_middle_east_logistics_4c_watch"]
        korean_air = by_id["r9_loop14_korean_air_asiana_integration_stage2"]
        tway = by_id["r9_loop14_tway_air_incheon_airline_remedy_stage2"]

        self.assertEqual(tariff.primary_archetype, E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2)
        self.assertEqual(tariff.extra_price_metrics["q3_2025_tariff_cost_krw_trn"], 1.8)
        self.assertEqual(tariff.extra_price_metrics["us_hybrid_sales_share_pct"], 20)
        self.assertEqual(tariff.event_mae_pct, -6.6)
        self.assertIn("tariff_relief_headline_only", tariff.red_flag_fields)

        self.assertEqual(logistics.primary_archetype, E2RArchetype.AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH)
        self.assertEqual(logistics.extra_price_metrics["hyundai_relative_underperformance_pp"], -3.9)
        self.assertEqual(logistics.extra_price_metrics["q1_2026_op_yoy_pct"], -31)
        self.assertIn("route_disruption_blocks_high_margin_exports", logistics.red_flag_fields)

        self.assertEqual(korean_air.primary_archetype, E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2)
        self.assertEqual(korean_air.extra_price_metrics["asiana_stake_pct"], 63.88)
        self.assertEqual(korean_air.extra_price_metrics["revenue_2024_krw_trn"], 16)
        self.assertIn("merger_completion_only", korean_air.red_flag_fields)

        self.assertEqual(tway.primary_archetype, E2RArchetype.AIRLINE_REMEDY_ROUTE_CARGO_STAGE2)
        self.assertIn("Paris", tway.extra_price_metrics["tway_new_eu_routes"])
        self.assertEqual(tway.extra_price_metrics["asiana_cargo_sale_krw_bn"], 470)
        self.assertIn("route_rights_without_load_factor", tway.red_flag_fields)

    def test_safety_ipo_tourism_shipping_and_reference_cases_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND291_CASE_CANDIDATES}
        jeju = by_id["r9_loop14_jeju_air_safety_hard_4c"]
        india = by_id["r9_loop14_hyundai_india_ipo_failed_rerating"]
        tourism = by_id["r9_loop14_china_tourism_leisure_basket"]
        hmm = by_id["r9_loop14_hmm_red_sea_freight_rate_event_premium"]
        used_car = by_id["r9_loop14_korea_used_car_export_logistics_shock"]

        self.assertEqual(jeju.primary_archetype, E2RArchetype.AVIATION_SAFETY_HARD_4C)
        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179)
        self.assertEqual(jeju.stage4c_price_anchor, 6920.0)
        self.assertEqual(jeju.rerating_result, "thesis_break")

        self.assertEqual(india.primary_archetype, E2RArchetype.OVERSEAS_AUTO_IPO_FAILED_RERATING)
        self.assertEqual(india.stage4c_price_anchor, 1882.10)
        self.assertEqual(india.extra_price_metrics["q2_profit_decline_pct"], -16.5)
        self.assertEqual(india.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(tourism.primary_archetype, E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM)
        self.assertEqual(tourism.extra_price_metrics["hankook_cosmetics_event_mfe_pct"], 9.9)
        self.assertFalse(tourism.extra_price_metrics["tourist_spend_per_head_confirmed"])
        self.assertEqual(tourism.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(hmm.primary_archetype, E2RArchetype.CONTAINER_SHIPPING_RATE_EVENT_PREMIUM)
        self.assertEqual(hmm.extra_price_metrics["freightos_spot_index_6w_growth_pct"], 40)
        self.assertTrue(hmm.extra_price_metrics["rate_normalization_risk"])
        self.assertEqual(hmm.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(used_car.primary_archetype, E2RArchetype.USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE)
        self.assertEqual(used_car.extra_price_metrics["korea_used_car_exports_units"], 883000)
        self.assertTrue(used_car.extra_price_metrics["use_as_transport_logistics_4c_reference"])
        self.assertFalse(used_car.hard_4c_confirmed)
        self.assertEqual(used_car.case_type, "4c_thesis_break")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND291_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND291_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND291_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round291_shadow_weight_rows()}
        deep_rows = round291_deep_sub_archetype_rows()
        green_markdown = render_round291_green_gate_review_markdown()
        stage_markdown = render_round291_stage4b_4c_review_markdown()

        self.assertIn("tariff_pass_through_confirmed", required)
        self.assertIn("tourist_spend_per_head_confirmed", required)
        self.assertIn("tariff_relief_headline_only", forbidden)
        self.assertIn("freight_spot_rate_only", forbidden)
        self.assertIn("tariff_relief_headline_auto_rally", ROUND291_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_aviation_safety_event", ROUND291_HARD_4C_GATES)
        self.assertIn("market_cap_wipeout_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Jeju Air", stage_markdown)
        self.assertIn("hard 4C", stage_markdown)
        self.assertEqual(len(ROUND291_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["AUTO_TARIFF_HYBRID_MIX_STAGE2"]["tariff_pass_through"], "+5")
        self.assertEqual(shadow_rows["AVIATION_SAFETY_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Hyundai Motor" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Jeju Air" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round291_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_291.md")
        self.assertEqual(audit["round_id"], "round_219")
        self.assertEqual(audit["large_sector"], ROUND291_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round291_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round291_r9_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round291_case_rows()
            self.assertEqual(len(records), len(ROUND291_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND291_CASE_CANDIDATES))
            self.assertIn("Hyundai Motor", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("tariff_pass_through_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("AVIATION_SAFETY_HARD_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("market_cap_wipeout_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["q3_2025_tariff_cost_krw_trn"], 1.8)


if __name__ == "__main__":
    unittest.main()
