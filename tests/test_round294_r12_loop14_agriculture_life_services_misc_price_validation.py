from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round294_r12_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round294_r12_loop14_agriculture_life_services_misc_price_validation import (
    ROUND294_CASE_CANDIDATES,
    ROUND294_GREEN_FORBIDDEN_PATTERNS,
    ROUND294_GREEN_REQUIRED_FIELDS,
    ROUND294_HARD_4C_GATES,
    ROUND294_LARGE_SECTOR,
    ROUND294_REQUIRED_TARGET_ALIASES,
    ROUND294_SHADOW_WEIGHT_ROWS,
    ROUND294_STAGE4B_WATCH_TRIGGERS,
    render_round294_green_gate_review_markdown,
    render_round294_stage4b_4c_review_markdown,
    round294_audit_payload,
    round294_case_records,
    round294_case_rows,
    round294_deep_sub_archetype_rows,
    round294_shadow_weight_rows,
    round294_summary,
    write_round294_r12_loop14_reports,
)


class Round294R12Loop14AgricultureLifeServicesMiscPriceValidationTests(unittest.TestCase):
    def test_round294_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND294_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND294_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND294_REQUIRED_TARGET_ALIASES["FRIED_CHICKEN_MEME_EVENT_PREMIUM"],
            E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM.value,
        )
        self.assertEqual(
            ROUND294_REQUIRED_TARGET_ALIASES["PRIVATE_EDUCATION_HAGWON_STAGE2_4C"],
            E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C.value,
        )

    def test_round294_archetype_definitions_capture_loop14_gates(self) -> None:
        agri = archetype_definition(E2RArchetype.AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH)
        food = archetype_definition(E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH)
        chicken = archetype_definition(E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM)
        delivery = archetype_definition(E2RArchetype.FOOD_DELIVERY_CONSOLIDATION_STAGE2)
        labor = archetype_definition(E2RArchetype.DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE)
        waste = archetype_definition(E2RArchetype.WASTE_RECYCLING_INFRA_STAGE2)
        childcare = archetype_definition(E2RArchetype.DEMOGRAPHIC_CHILDCARE_STAGE2)
        hagwon = archetype_definition(E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C)

        self.assertIn("tractor sales decline", agri.stage4c_thesis_break_signals)
        self.assertIn("input-cost inflation treated as pricing power", food.false_positive_patterns)
        self.assertIn("celebrity chicken meme rally without restaurant economics", chicken.false_positive_patterns)
        self.assertIn("approval, take-rate, rider cost, merchant churn, integration economics and cash-flow bridge verified", delivery.stage3_high_conviction_signals)
        self.assertIn("delivery service halt", labor.stage4c_thesis_break_signals)
        self.assertIn("actual recycling yield far below official claim", waste.stage4c_thesis_break_signals)
        self.assertIn("birthrate headline only treated as childcare revenue", childcare.false_positive_patterns)
        self.assertIn("private education regulation", hagwon.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round294_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND294_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("direct_KRX_hard_4c_confirmed_false", record.green_guardrails)
            self.assertIn("sector_hard_reference_confirmed_true", record.green_guardrails)
            self.assertIn("do_not_use_round294_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round294_summary()
        self.assertEqual(summary["round_id"], "round_222")
        self.assertEqual(summary["large_sector"], "AGRICULTURE_LIFE_SERVICES_MISC")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["watch_counterexample_count"], 3)
        self.assertEqual(summary["hard_reference_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 2)
        self.assertEqual(summary["stage4c_watch_count"], 5)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["direct_listed_hard_4c_case_count"], 0)
        self.assertEqual(summary["sector_hard_reference_count"], 7)
        self.assertEqual(summary["price_moved_without_evidence_count"], 1)
        self.assertEqual(summary["false_positive_score_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["direct_KRX_hard_4c_confirmed"])
        self.assertTrue(summary["sector_hard_reference_confirmed"])

    def test_round294_cases_keep_headline_events_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND294_CASE_CANDIDATES}
        agri = by_id["r12_loop14_daedong_tym_agri_equipment_export_cycle"]
        food = by_id["r12_loop14_food_input_cost_inflation_basket"]
        chicken = by_id["r12_loop14_fried_chicken_jensen_huang_meme_rally"]
        baemin = by_id["r12_loop14_naver_uber_baemin_food_delivery_consolidation"]
        labor = by_id["r12_loop14_delivery_labor_service_continuity_reference"]
        waste = by_id["r12_loop14_waste_recycling_infra_stage2"]
        childcare = by_id["r12_loop14_birthrate_childcare_infant_goods_stage2"]
        hagwon = by_id["r12_loop14_private_education_hagwon_demand_stage2"]

        self.assertEqual(agri.primary_archetype, E2RArchetype.AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH)
        self.assertEqual(agri.extra_price_metrics["cnh_premarket_mae_pct"], -10)
        self.assertEqual(agri.extra_price_metrics["agco_event_mfe_pct"], 2.2)
        self.assertEqual(agri.score_price_alignment, "false_positive_score")

        self.assertEqual(food.primary_archetype, E2RArchetype.AGRI_FOOD_INPUT_COST_4C_WATCH)
        self.assertEqual(food.extra_price_metrics["rice_price_yoy_pct"], 18.6)
        self.assertEqual(food.extra_price_metrics["mandarin_price_yoy_pct"], 26.5)

        self.assertEqual(chicken.primary_archetype, E2RArchetype.FRIED_CHICKEN_MEME_EVENT_PREMIUM)
        self.assertEqual(chicken.extra_price_metrics["kyochon_event_mfe_pct"], 20)
        self.assertEqual(chicken.extra_price_metrics["cherrybro_event_mfe_pct"], 30)
        self.assertFalse(chicken.extra_price_metrics["kkanbu_listed"])
        self.assertFalse(chicken.extra_price_metrics["same_store_sales_confirmed"])
        self.assertEqual(chicken.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(baemin.primary_archetype, E2RArchetype.FOOD_DELIVERY_CONSOLIDATION_STAGE2)
        self.assertEqual(baemin.extra_price_metrics["baemin_bid_value_krw_trn"], 8)
        self.assertEqual(baemin.extra_price_metrics["uber_naver_consortium_split"], "80/20")
        self.assertFalse(baemin.extra_price_metrics["final_decision_confirmed"])

        self.assertEqual(labor.primary_archetype, E2RArchetype.DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE)
        self.assertEqual(labor.extra_price_metrics["coupang_rocket_delivery_first_pause_since"], 2014)
        self.assertIn("CJ Logistics", labor.extra_price_metrics["participating_companies"])
        self.assertFalse(labor.direct_listed_hard_4c_confirmed)

        self.assertEqual(waste.primary_archetype, E2RArchetype.WASTE_RECYCLING_INFRA_STAGE2)
        self.assertEqual(waste.extra_price_metrics["kj_environment_platform_ev_krw_trn_min"], 1.0)
        self.assertEqual(waste.extra_price_metrics["greenpeace_actual_recycling_estimate_pct"], 27)
        self.assertEqual(waste.extra_price_metrics["untreated_plastic_waste_tonnes"], 19000)

        self.assertEqual(childcare.primary_archetype, E2RArchetype.DEMOGRAPHIC_CHILDCARE_STAGE2)
        self.assertEqual(childcare.extra_price_metrics["fertility_rate_2025"], 0.80)
        self.assertEqual(childcare.extra_price_metrics["births_2025_growth_pct"], 6.8)
        self.assertTrue(childcare.extra_price_metrics["echo_boomer_effect_watch"])

        self.assertEqual(hagwon.primary_archetype, E2RArchetype.PRIVATE_EDUCATION_HAGWON_STAGE2_4C)
        self.assertEqual(hagwon.extra_price_metrics["under6_hagwon_enrolment_pct"], 47.6)
        self.assertEqual(hagwon.extra_price_metrics["english_kindergarten_monthly_tuition_avg_krw"], 1500000)

    def test_green_gate_stage_review_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND294_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND294_GREEN_FORBIDDEN_PATTERNS)
        shadow_rows = {row["archetype"]: row for row in round294_shadow_weight_rows()}
        deep_rows = round294_deep_sub_archetype_rows()
        green_markdown = render_round294_green_gate_review_markdown()
        stage_markdown = render_round294_stage4b_4c_review_markdown()

        self.assertIn("food_input_cost_pass_through_confirmed", required)
        self.assertIn("same_store_sales_franchise_fee_confirmed", required)
        self.assertIn("delivery_take_rate_unit_economics_confirmed", required)
        self.assertIn("childcare_customer_count_ARPU_margin_confirmed", required)
        self.assertIn("celebrity_AI_visit_without_restaurant_economics", forbidden)
        self.assertIn("waste_platform_EV_without_recycling_yield", forbidden)
        self.assertIn("celebrity_visit_photo_moves_food_service_peers", ROUND294_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("recycling_yield_failure_or_cleanup_liability", ROUND294_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("direct KRX hard 4C", stage_markdown)
        self.assertEqual(len(ROUND294_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["FOOD_DELIVERY_CONSOLIDATION_STAGE2"]["delivery_take_rate_unit_economics"], "+5")
        self.assertEqual(shadow_rows["FRIED_CHICKEN_MEME_EVENT_PREMIUM"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["WASTE_RECYCLING_INFRA_STAGE2"]["recycling_yield_gate_fee_margin"], "+5")
        self.assertTrue(any("Jensen Huang" in row["terms"] for row in deep_rows))
        self.assertTrue(any("under-6 hagwon 47.6%" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round294_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_294.md")
        self.assertEqual(audit["round_id"], "round_222")
        self.assertEqual(audit["large_sector"], ROUND294_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertFalse(audit["summary"]["direct_KRX_hard_4c_confirmed"])
        self.assertTrue(audit["summary"]["sector_hard_reference_confirmed"])
        self.assertIn("do_not_use_round294_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round294_r12_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round294_case_rows()
            self.assertEqual(len(records), len(ROUND294_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND294_CASE_CANDIDATES))
            self.assertIn("Jensen", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("same_store_sales_franchise_fee_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("FOOD_DELIVERY_CONSOLIDATION_STAGE2", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("waste_infra_anchor", paths["price_validation_fields"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[2]["extra_price_metrics"])["cherrybro_event_mfe_pct"], 30)


if __name__ == "__main__":
    unittest.main()
