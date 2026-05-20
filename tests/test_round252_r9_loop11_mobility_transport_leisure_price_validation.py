from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round252_r9_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round252_r9_loop11_mobility_transport_leisure_price_validation import (
    ROUND252_CASE_CANDIDATES,
    ROUND252_DEEP_SUB_ARCHETYPES,
    ROUND252_GREEN_FORBIDDEN_PATTERNS,
    ROUND252_GREEN_REQUIRED_FIELDS,
    ROUND252_HARD_4C_GATES,
    ROUND252_LARGE_SECTOR,
    ROUND252_PRICE_VALIDATION_FIELDS,
    ROUND252_REQUIRED_TARGET_ALIASES,
    ROUND252_SCORE_ADJUSTMENTS,
    ROUND252_SHADOW_WEIGHT_ROWS,
    ROUND252_STAGE4B_WATCH_TRIGGERS,
    render_round252_green_gate_review_markdown,
    render_round252_stage4b_4c_review_markdown,
    round252_audit_payload,
    round252_case_records,
    round252_case_rows,
    round252_deep_sub_archetype_rows,
    round252_shadow_weight_rows,
    round252_summary,
    write_round252_r9_loop11_reports,
)


class Round252R9Loop11MobilityTransportLeisurePriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND252_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND252_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND252_REQUIRED_TARGET_ALIASES["AUTO_HYBRID_SHAREHOLDER_RETURN"],
            E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN.value,
        )
        self.assertEqual(
            ROUND252_REQUIRED_TARGET_ALIASES["AUTO_TARIFF_MARGIN_SHOCK"],
            E2RArchetype.AUTO_TARIFF_MARGIN_SHOCK.value,
        )
        self.assertEqual(
            ROUND252_REQUIRED_TARGET_ALIASES["AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION"],
            E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION.value,
        )
        self.assertEqual(
            ROUND252_REQUIRED_TARGET_ALIASES["AIRLINE_CONSOLIDATION_INTEGRATION"],
            E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION.value,
        )
        self.assertEqual(
            ROUND252_REQUIRED_TARGET_ALIASES["AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C"],
            E2RArchetype.AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C.value,
        )
        self.assertEqual(
            ROUND252_REQUIRED_TARGET_ALIASES["AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C"],
            E2RArchetype.AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND252_REQUIRED_TARGET_ALIASES["TOURISM_REDIRECT_POLICY_EVENT"],
            E2RArchetype.TOURISM_REDIRECT_POLICY_EVENT.value,
        )

    def test_archetype_definitions_capture_round252_gates(self) -> None:
        hybrid = archetype_definition(E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN)
        tariff = archetype_definition(E2RArchetype.AUTO_TARIFF_MARGIN_SHOCK)
        logistics = archetype_definition(E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION)
        airline = archetype_definition(E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION)
        tire = archetype_definition(E2RArchetype.AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C)
        supplier = archetype_definition(E2RArchetype.AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C)
        tourism = archetype_definition(E2RArchetype.TOURISM_REDIRECT_POLICY_EVENT)
        cyclical = archetype_definition(E2RArchetype.CYCLICAL_SUCCESS)

        self.assertIn("tariff-adjusted margin", hybrid.stage3_high_conviction_signals)
        self.assertIn("tariff cost causing OP collapse", tariff.stage4c_thesis_break_signals)
        self.assertIn("route closure", logistics.stage4c_thesis_break_signals)
        self.assertIn("load factor", airline.stage3_high_conviction_signals)
        self.assertIn("factory fire", tire.stage4c_thesis_break_signals)
        self.assertIn("fatal workplace accident", supplier.stage4c_thesis_break_signals)
        self.assertIn("tourist spend", tourism.stage3_high_conviction_signals)
        self.assertIn("cyclical earnings spike treated as structural E2R", cyclical.false_positive_patterns)

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round252_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.MOBILITY_TRANSPORT_LEISURE.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_strategy_day_shareholder_return_merger_tourism_policy_or_freight_spike_as_green", record.green_guardrails)

        summary = round252_summary()
        self.assertEqual(summary["analyst_round_id"], "round_180")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["stage4c_watch_count"], 2)
        self.assertEqual(summary["thesis_break_watch_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_auto_airline_shipping_and_tourism_cases_are_stage2_or_event_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND252_CASE_CANDIDATES}
        hyundai = by_id["r9_loop11_hyundai_hybrid_shareholder_return"]
        tariff = by_id["r9_loop11_hyundai_kia_us_tariff_margin_shock"]
        logistics = by_id["r9_loop11_hyundai_glovis_middle_east_logistics_disruption"]
        airline = by_id["r9_loop11_korean_air_asiana_consolidation"]
        pan_ocean = by_id["r9_loop11_pan_ocean_shipping_freight_cycle"]
        tourism = by_id["r9_loop11_lotte_tour_yellow_balloon_tourism_redirect"]

        self.assertEqual(hyundai.primary_archetype, E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN)
        self.assertEqual(hyundai.stage2_date.isoformat(), "2024-08-28")
        self.assertEqual(hyundai.mfe_1d, 5.0)
        self.assertEqual(hyundai.event_close_return, 4.7)
        self.assertEqual(hyundai.extra_price_metrics["buyback_program_krw_trn"], 4.0)
        self.assertIn("tariff_adjusted_margin_unverified", hyundai.red_flag_fields)

        self.assertEqual(tariff.primary_archetype, E2RArchetype.AUTO_TARIFF_MARGIN_SHOCK)
        self.assertEqual(tariff.stage4c_date.isoformat(), "2025-03-27")
        self.assertFalse(tariff.hard_4c_confirmed)
        self.assertEqual(tariff.extra_price_metrics["kia_q2_2025_tariff_hit_krw_bn"], 786.0)
        self.assertEqual(tariff.extra_price_metrics["kia_trade_deal_mae_pct"], -6.6)
        self.assertEqual(tariff.round_score_price_alignment, "thesis_break_watch")

        self.assertEqual(logistics.primary_archetype, E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION)
        self.assertEqual(logistics.stage4c_date.isoformat(), "2026-04-03")
        self.assertEqual(logistics.extra_price_metrics["hyundai_relative_underperformance_pp"], -3.9)
        self.assertEqual(logistics.extra_price_metrics["middle_east_shipments_decline_pct"], -49.0)
        self.assertIn("logistics_disruption", logistics.red_flag_fields)

        self.assertEqual(airline.primary_archetype, E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION)
        self.assertEqual(airline.stage2_date.isoformat(), "2024-12-12")
        self.assertEqual(airline.extra_price_metrics["korean_air_asiana_stake_pct"], 63.88)
        self.assertEqual(airline.extra_price_metrics["combined_lcc_aircraft"], 58.0)
        self.assertIn("load_factor_unverified", airline.red_flag_fields)

        self.assertEqual(pan_ocean.primary_archetype, E2RArchetype.SHIPPING_FREIGHT_CYCLE)
        self.assertEqual(pan_ocean.case_type, "cyclical_success")
        self.assertEqual(pan_ocean.stage2_price_anchor, 4615.0)
        self.assertEqual(pan_ocean.extra_price_metrics["target_upside_from_event_price_pct"], 45.2)
        self.assertEqual(pan_ocean.rerating_result, "cyclical_rerating")

        self.assertEqual(tourism.primary_archetype, E2RArchetype.TOURISM_REDIRECT_POLICY_EVENT)
        self.assertEqual(tourism.case_type, "event_premium")
        self.assertEqual(tourism.mfe_1d, 24.0)
        self.assertEqual(tourism.extra_price_metrics["yellow_balloon_redirect_mfe_pct"], 24.0)
        self.assertEqual(tourism.score_price_alignment, "price_moved_without_evidence")

    def test_hard_4c_cases_are_direct_or_sector_operational_breaks(self) -> None:
        by_id = {case.case_id: case for case in ROUND252_CASE_CANDIDATES}
        kumho = by_id["r9_loop11_kumho_tire_gwangju_factory_fire_hard_4c"]
        daejeon = by_id["r9_loop11_daejeon_auto_parts_supplier_fire_sector_hard_4c"]

        self.assertEqual(kumho.primary_archetype, E2RArchetype.AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C)
        self.assertTrue(kumho.hard_4c_confirmed)
        self.assertEqual(kumho.stage4c_date.isoformat(), "2025-05-17")
        self.assertEqual(kumho.mae_1d, -8.0)
        self.assertEqual(kumho.extra_price_metrics["annual_capacity_mn_tires"], 12.0)
        self.assertEqual(kumho.extra_price_metrics["share_of_global_capacity_pct"], 20.0)
        self.assertEqual(kumho.rerating_result, "thesis_break")

        self.assertEqual(daejeon.primary_archetype, E2RArchetype.AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C)
        self.assertTrue(daejeon.hard_4c_confirmed)
        self.assertEqual(daejeon.stage4c_date.isoformat(), "2026-03-20")
        self.assertEqual(daejeon.extra_price_metrics["fatalities"], 14.0)
        self.assertEqual(daejeon.extra_price_metrics["injuries"], 60.0)
        self.assertIn("direct_listed_mapping_unavailable", daejeon.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND252_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND252_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND252_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND252_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round252_shadow_weight_rows()}
        deep_rows = round252_deep_sub_archetype_rows()
        green_markdown = render_round252_green_gate_review_markdown()
        stage_markdown = render_round252_stage4b_4c_review_markdown()

        self.assertIn("tariff_adjusted_margin_confirmed", required)
        self.assertIn("fleet_utilization_confirmed", required)
        self.assertIn("tourism_policy_only", forbidden)
        self.assertIn("factory_fire_or_supply_disruption", forbidden)
        self.assertIn("tourism_policy_basket_rally_before_spend", ROUND252_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("factory_fire", ROUND252_HARD_4C_GATES)
        self.assertIn("fatal_workplace_accident", ROUND252_HARD_4C_GATES)
        self.assertIn("tariff_or_margin_anchor", fields)
        self.assertIn("safety_or_factory_risk_anchor", fields)
        self.assertIn("unit_economics", axes)
        self.assertIn("factory_fire_or_supply_disruption", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Factory fire", green_markdown)
        self.assertIn("r9_loop11_kumho_tire_gwangju_factory_fire_hard_4c", stage_markdown)
        self.assertEqual(len(ROUND252_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["AUTO_HYBRID_SHAREHOLDER_RETURN"]["hybrid_mix_profitability"], "+5")
        self.assertEqual(shadow_rows["TOURISM_REDIRECT_POLICY_EVENT"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Hyundai Glovis" in row["deep_sub_archetype"] for row in deep_rows))
        self.assertIn("Kumho Tire factory fire", ROUND252_DEEP_SUB_ARCHETYPES)

    def test_audit_payload_cli_and_writer_outputs(self) -> None:
        audit = round252_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_252.md")
        self.assertEqual(audit["analyst_round_id"], "round_180")
        self.assertEqual(audit["large_sector"], ROUND252_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round252_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round252_r9_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round252_case_rows()
            self.assertEqual(len(records), len(ROUND252_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND252_CASE_CANDIDATES))
            self.assertIn("Kumho Tire factory fire is hard 4C", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("tariff_adjusted_margin", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("AUTO_HYBRID_SHAREHOLDER_RETURN", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("fatal_workplace_accident", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[0]["round_case_type"], "success_candidate_hybrid_shareholder_return_stage2")
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["buyback_program_krw_trn"], 4.0)

    def test_production_modules_do_not_import_round252(self) -> None:
        forbidden = "round252_r9_loop11_mobility_transport_leisure_price_validation"
        for rel_path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(rel_path).read_text(encoding="utf-8")
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
