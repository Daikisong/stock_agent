from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round239_r9_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round239_r9_loop10_mobility_transport_leisure_price_validation import (
    ROUND239_CASE_CANDIDATES,
    ROUND239_GREEN_FORBIDDEN_PATTERNS,
    ROUND239_GREEN_REQUIRED_FIELDS,
    ROUND239_HARD_4C_GATES,
    ROUND239_PRICE_VALIDATION_FIELDS,
    ROUND239_REQUIRED_TARGET_ALIASES,
    ROUND239_SCORE_ADJUSTMENTS,
    ROUND239_SHADOW_WEIGHT_ROWS,
    ROUND239_STAGE4B_WATCH_TRIGGERS,
    render_round239_green_gate_review_markdown,
    render_round239_stage4b_4c_review_markdown,
    round239_audit_payload,
    round239_case_records,
    round239_case_rows,
    round239_summary,
    write_round239_r9_loop10_reports,
)


class Round239R9Loop10MobilityTransportLeisurePriceValidationTests(unittest.TestCase):
    def test_round239_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND239_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND239_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND239_REQUIRED_TARGET_ALIASES["FUTURE_MOBILITY_AI_ROBOTICS_CAPEX"],
            E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX.value,
        )
        self.assertEqual(
            ROUND239_REQUIRED_TARGET_ALIASES["AIRLINE_SAFETY_OPERATIONAL_TRUST_4C"],
            E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C.value,
        )
        self.assertEqual(ROUND239_REQUIRED_TARGET_ALIASES["PRICE_ONLY_RALLY"], E2RArchetype.PRICE_ONLY_RALLY.value)

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round239_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.MOBILITY_TRANSPORT_LEISURE.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)

        summary = round239_summary()
        self.assertEqual(summary["analyst_round_id"], "round_167")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_new_mobility_archetype_definitions_are_available(self) -> None:
        future = archetype_definition(E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX)
        safety = archetype_definition(E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C)
        route = archetype_definition(E2RArchetype.LCC_LONG_HAUL_ROUTE_ALLOCATION)

        self.assertIn("robot shipments", future.stage3_high_conviction_signals)
        self.assertIn("FCF after capex", future.stage3_high_conviction_signals)
        self.assertIn("fatal safety accident", safety.stage4c_thesis_break_signals)
        self.assertIn("not a Green source; fatal accident is a hard 4C gate", safety.stage3_high_conviction_signals)
        self.assertIn("load factor", route.stage3_high_conviction_signals)
        self.assertIn("route rights treated as earnings before load factor/yield", route.false_positive_patterns)

    def test_hyundai_kia_future_mobility_case_is_4b_watch_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND239_CASE_CANDIDATES}
        case = by_id["r9_loop10_hyundai_kia_future_mobility_capex_4b"]

        self.assertEqual(case.primary_archetype, E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX)
        self.assertEqual(case.stage2_date.isoformat(), "2026-02-25")
        self.assertEqual(case.stage4b_date.isoformat(), "2026-02-25")
        self.assertEqual(case.stage4c_date.isoformat(), "2026-01-22")
        self.assertIsNone(case.stage3_date)
        self.assertFalse(case.hard_4c_confirmed)
        self.assertEqual(case.extra_price_metrics["hyundai_event_mfe_1d_pct"], 10.5)
        self.assertEqual(case.extra_price_metrics["kia_event_mfe_1d_pct"], 15.0)
        self.assertEqual(case.extra_price_metrics["hyundai_group_domestic_investment_2026_2030_krw_tn"], 125.2)
        self.assertEqual(case.extra_price_metrics["nvidia_ai_chip_allocation"], 50000.0)
        self.assertIn("fcf_after_capex_unverified", case.red_flag_fields)

    def test_hyundai_mobis_quality_recall_is_redteam_overlay(self) -> None:
        by_id = {case.case_id: case for case in ROUND239_CASE_CANDIDATES}
        case = by_id["r9_loop10_hyundai_mobis_iccu_quality_recall_watch"]

        self.assertEqual(case.primary_archetype, E2RArchetype.AUTO_PARTS_QUALITY_RECALL_4C)
        self.assertEqual(case.stage4c_date.isoformat(), "2024-05-01")
        self.assertFalse(case.hard_4c_confirmed)
        self.assertEqual(case.stage4c_price_anchor, 225500.0)
        self.assertEqual(case.mae_1d, -0.7)
        self.assertEqual(case.extra_price_metrics["target_cut_pct"], -12.0)
        self.assertEqual(case.extra_price_metrics["implied_prior_target_krw"], 301136.0)
        self.assertIn("quality_recall_issue", case.red_flag_fields)

    def test_rail_lcc_and_integration_cases_are_stage2_until_execution(self) -> None:
        by_id = {case.case_id: case for case in ROUND239_CASE_CANDIDATES}
        rotem = by_id["r9_loop10_hyundai_rotem_morocco_rail_order"]
        tway = by_id["r9_loop10_tway_europe_route_allocation"]
        integration = by_id["r9_loop10_jin_air_air_busan_air_seoul_integration"]

        self.assertEqual(rotem.primary_archetype, E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY)
        self.assertEqual(rotem.extra_price_metrics["hyundai_rotem_order_krw_tn"], 2.2)
        self.assertEqual(rotem.extra_price_metrics["hyundai_train_count"], 110.0)
        self.assertEqual(rotem.extra_price_metrics["hyundai_order_share_of_total_program_pct"], 53.1)
        self.assertIn("margin_unverified", rotem.red_flag_fields)

        self.assertEqual(tway.primary_archetype, E2RArchetype.LCC_LONG_HAUL_ROUTE_ALLOCATION)
        self.assertEqual(tway.extra_price_metrics["new_europe_route_count"], 4.0)
        self.assertEqual(tway.extra_price_metrics["korean_air_support_aircraft_count"], 5.0)
        self.assertEqual(tway.extra_price_metrics["korean_air_support_pilots"], 100.0)
        self.assertIn("route_allocation_without_yield", tway.red_flag_fields)

        self.assertEqual(integration.primary_archetype, E2RArchetype.LCC_CONSOLIDATION_INTEGRATION)
        self.assertEqual(integration.extra_price_metrics["combined_lcc_aircraft"], 58.0)
        self.assertEqual(integration.extra_price_metrics["combined_capacity_share_nov_2024_pct"], 8.0)
        self.assertEqual(integration.extra_price_metrics["combined_lcc_aircraft_advantage_vs_jeju_pct"], 38.1)
        self.assertEqual(integration.extra_price_metrics["combined_lcc_aircraft_advantage_vs_tway_pct"], 48.7)
        self.assertIn("fleet_count_without_margin", integration.red_flag_fields)

    def test_shipping_tourism_and_jeju_cases_preserve_price_alignment(self) -> None:
        by_id = {case.case_id: case for case in ROUND239_CASE_CANDIDATES}
        pan = by_id["r9_loop10_pan_ocean_dry_bulk_cycle"]
        tourism = by_id["r9_loop10_lotte_tour_yellow_balloon_china_japan_redirect"]
        jeju = by_id["r9_loop10_jeju_air_fatal_crash_hard_4c"]

        self.assertEqual(pan.case_type, "cyclical_success")
        self.assertEqual(pan.primary_archetype, E2RArchetype.SHIPPING_DRY_BULK_CYCLE)
        self.assertEqual(pan.stage2_price_anchor, 4615.0)
        self.assertEqual(pan.mae_1d, -0.2)
        self.assertEqual(pan.extra_price_metrics["target_upside_from_event_price_pct"], 45.2)
        self.assertEqual(pan.extra_price_metrics["op_forecast_2024_krw_bn"], 536.0)
        self.assertEqual(pan.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(tourism.case_type, "event_premium")
        self.assertEqual(tourism.primary_archetype, E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM)
        self.assertEqual(tourism.stage4b_date.isoformat(), "2025-11-21")
        self.assertEqual(tourism.extra_price_metrics["yellow_balloon_event_mfe_pct"], 24.0)
        self.assertEqual(tourism.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(jeju.primary_archetype, E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C)
        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.stage4c_date.isoformat(), "2024-12-30")
        self.assertEqual(jeju.stage4c_price_anchor, 6920.0)
        self.assertEqual(jeju.mae_1d, -15.7)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179.0)
        self.assertEqual(jeju.extra_price_metrics["market_cap_wipeout_krw_bn"], 95.7)
        self.assertEqual(jeju.round_score_price_alignment, "thesis_break")
        self.assertIn("fatal_safety_accident", jeju.red_flag_fields)

    def test_green_gate_4b_4c_and_shadow_weights_are_explicit(self) -> None:
        required = set(ROUND239_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND239_GREEN_FORBIDDEN_PATTERNS)
        review = render_round239_green_gate_review_markdown()
        stage_review = render_round239_stage4b_4c_review_markdown()
        weights = {row.archetype: row for row in ROUND239_SHADOW_WEIGHT_ROWS}

        self.assertIn("unit_economics", required)
        self.assertIn("fcf_after_capex", required)
        self.assertIn("fatal_safety_accident", forbidden)
        self.assertIn("route_allocation_without_yield", forbidden)
        self.assertIn("fatal_safety_accident", ROUND239_HARD_4C_GATES)
        self.assertIn("tourism_reroute_rally_before_spend", ROUND239_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("r9_loop10_jeju_air_fatal_crash_hard_4c", stage_review)
        self.assertEqual(weights[E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX].event_penalty, -5)
        self.assertEqual(weights[E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C].hard_4c_sensitivity, 5)

    def test_price_fields_and_score_axes_cover_r9_loop10(self) -> None:
        fields = set(ROUND239_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND239_SCORE_ADJUSTMENTS}

        self.assertIn("reported_price_anchor", fields)
        self.assertIn("tourism_or_safety_anchor", fields)
        self.assertIn("unit_economics", axes)
        self.assertIn("fcf_after_capex", axes)
        self.assertIn("freight_rate_floor", axes)
        self.assertIn("safety_trust_break", axes)

    def test_audit_payload_marks_non_production_round(self) -> None:
        audit = round239_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_239.md")
        self.assertEqual(audit["analyst_round_id"], "round_167")
        self.assertEqual(audit["large_sector"], Round10LargeSector.MOBILITY_TRANSPORT_LEISURE.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("keep_jeju_air_fatal_crash_as_hard_4c_reference_case", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round239_r9_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round239_case_rows()
            self.assertEqual(len(records), len(ROUND239_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND239_CASE_CANDIDATES))
            self.assertIn("제주항공", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("route_allocation_without_yield", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("FUTURE_MOBILITY_AI_ROBOTICS_CAPEX", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("fatal_safety_accident", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[7]["round_score_price_alignment"], "thesis_break")
            self.assertEqual(json.loads(rows[7]["extra_price_metrics"])["fatalities"], 179.0)


if __name__ == "__main__":
    unittest.main()
