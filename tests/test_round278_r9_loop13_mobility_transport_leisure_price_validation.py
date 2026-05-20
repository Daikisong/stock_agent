from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round278_r9_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round278_r9_loop13_mobility_transport_leisure_price_validation import (
    ROUND278_CASE_CANDIDATES,
    ROUND278_GREEN_FORBIDDEN_PATTERNS,
    ROUND278_GREEN_REQUIRED_FIELDS,
    ROUND278_HARD_4C_GATES,
    ROUND278_LARGE_SECTOR,
    ROUND278_PRICE_VALIDATION_FIELDS,
    ROUND278_REQUIRED_TARGET_ALIASES,
    ROUND278_SHADOW_WEIGHT_ROWS,
    ROUND278_STAGE4B_WATCH_TRIGGERS,
    render_round278_green_gate_review_markdown,
    render_round278_stage4b_4c_review_markdown,
    round278_audit_payload,
    round278_case_records,
    round278_case_rows,
    round278_deep_sub_archetype_rows,
    round278_shadow_weight_rows,
    round278_summary,
    write_round278_r9_loop13_reports,
)


class Round278R9Loop13MobilityTransportLeisurePriceValidationTests(unittest.TestCase):
    def test_round278_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND278_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND278_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND278_REQUIRED_TARGET_ALIASES["HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2"],
            E2RArchetype.HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2.value,
        )
        self.assertEqual(
            ROUND278_REQUIRED_TARGET_ALIASES["AVIATION_SAFETY_HARD_4C"],
            E2RArchetype.AVIATION_SAFETY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND278_REQUIRED_TARGET_ALIASES["CHINA_TOURISM_LEISURE_EVENT_PREMIUM"],
            E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM.value,
        )

    def test_round278_archetype_definitions_capture_r9_loop13_gates(self) -> None:
        hyundai = archetype_definition(E2RArchetype.HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2)
        tariff = archetype_definition(E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH)
        india = archetype_definition(E2RArchetype.INDIA_AUTO_IPO_CAPITAL_RECYCLING)
        airline = archetype_definition(E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2)
        safety = archetype_definition(E2RArchetype.AVIATION_SAFETY_HARD_4C)
        mobis = archetype_definition(E2RArchetype.AUTO_PARTS_PORTFOLIO_RECYCLING)
        red_sea = archetype_definition(E2RArchetype.RED_SEA_FREIGHT_CYCLE_4B_4C)
        tourism = archetype_definition(E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM)

        self.assertIn("OP margin after tariff", hyundai.stage3_high_conviction_signals)
        self.assertIn("unit sales treated as Green while tariff cost crushes OP", tariff.false_positive_patterns)
        self.assertIn("IPO valuation treated as parent Green without proceeds use", india.false_positive_patterns)
        self.assertIn("fleet capex ROI", airline.stage3_high_conviction_signals)
        self.assertIn("fatal aviation accident", safety.stage4c_thesis_break_signals)
        self.assertIn("exploratory sale treated as ROIC improvement", mobis.false_positive_patterns)
        self.assertIn("freight-rate spike treated as structural Green", red_sea.false_positive_patterns)
        self.assertIn("tourist-flow headline treated as booking margin", tourism.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round278_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND278_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round278_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round278_summary()
        self.assertEqual(summary["round_id"], "round_206")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["cyclical_success_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 5)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_mobility_cases_keep_margin_roi_safety_and_booking_separate(self) -> None:
        by_id = {case.case_id: case for case in ROUND278_CASE_CANDIDATES}
        hyundai = by_id["r9_loop13_hyundai_motor_hybrid_shareholder_return_tariff_watch"]
        kia = by_id["r9_loop13_kia_us_tariff_margin_break"]
        india = by_id["r9_loop13_hyundai_motor_india_ipo_capital_recycling"]
        korean_air = by_id["r9_loop13_korean_air_asiana_consolidation_fleet_capex_watch"]
        jeju = by_id["r9_loop13_jeju_air_fatal_crash_aviation_safety_hard_4c"]
        tourism = by_id["r9_loop13_china_tourism_leisure_event_premium"]

        self.assertEqual(hyundai.primary_archetype, E2RArchetype.HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2)
        self.assertEqual(hyundai.extra_price_metrics["hyundai_event_intraday_mfe_pct"], 5.0)
        self.assertEqual(hyundai.extra_price_metrics["buyback_2025_2027_krw_trn"], 4.0)
        self.assertIn("tariff_exposure_unhedged", hyundai.red_flag_fields)

        self.assertEqual(kia.primary_archetype, E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH)
        self.assertEqual(kia.extra_price_metrics["q2_tariff_hit_krw_bn"], 786)
        self.assertEqual(kia.extra_price_metrics["q2_op_decline_pct"], -24)
        self.assertEqual(kia.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(india.primary_archetype, E2RArchetype.INDIA_AUTO_IPO_CAPITAL_RECYCLING)
        self.assertEqual(india.extra_price_metrics["debut_mae_pct"], -6.0)
        self.assertEqual(india.stage4c_price_anchor, 1882.10)

        self.assertEqual(korean_air.primary_archetype, E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2)
        self.assertEqual(korean_air.extra_price_metrics["boeing_aircraft_order_units"], 103)
        self.assertIn("fleet_order_without_ROI", korean_air.red_flag_fields)

        self.assertEqual(jeju.primary_archetype, E2RArchetype.AVIATION_SAFETY_HARD_4C)
        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179)
        self.assertEqual(jeju.rerating_result, "thesis_break")

        self.assertEqual(tourism.primary_archetype, E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM)
        self.assertEqual(tourism.extra_price_metrics["yellow_balloon_rerouting_mfe_pct"], 24)
        self.assertFalse(tourism.extra_price_metrics["actual_booking_margin_confirmed"])

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND278_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND278_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND278_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round278_shadow_weight_rows()}
        deep_rows = round278_deep_sub_archetype_rows()
        green_markdown = render_round278_green_gate_review_markdown()
        stage_markdown = render_round278_stage4b_4c_review_markdown()

        self.assertIn("OP_margin_after_tariff_confirmed", required)
        self.assertIn("aviation_safety_trust_confirmed", required)
        self.assertIn("unit_sales_without_margin", forbidden)
        self.assertIn("fatal_safety_event", forbidden)
        self.assertIn("hybrid_shareholder_return_event_plus_5pct_before_margin", ROUND278_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_crash_or_safety_inspection", ROUND278_HARD_4C_GATES)
        self.assertIn("tariff_margin_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Jeju Air", stage_markdown)
        self.assertIn("hard 4C", stage_markdown)
        self.assertEqual(len(ROUND278_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["AUTO_TARIFF_MARGIN_4C_WATCH"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["AVIATION_SAFETY_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Hyundai Motor" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Lotte Tour" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round278_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_278.md")
        self.assertEqual(audit["round_id"], "round_206")
        self.assertEqual(audit["large_sector"], ROUND278_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round278_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round278_r9_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round278_case_rows()
            self.assertEqual(len(records), len(ROUND278_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND278_CASE_CANDIDATES))
            self.assertIn("Hyundai Motor", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("OP_margin_after_tariff_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("RED_SEA_FREIGHT_CYCLE_4B_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("tariff_margin_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["q2_tariff_hit_krw_bn"], 786)


if __name__ == "__main__":
    unittest.main()
