from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round281_r12_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round281_r12_loop13_agriculture_life_service_other_price_validation import (
    ROUND281_CASE_CANDIDATES,
    ROUND281_GREEN_FORBIDDEN_PATTERNS,
    ROUND281_GREEN_REQUIRED_FIELDS,
    ROUND281_HARD_4C_GATES,
    ROUND281_LARGE_SECTOR,
    ROUND281_PRICE_VALIDATION_FIELDS,
    ROUND281_REQUIRED_TARGET_ALIASES,
    ROUND281_SHADOW_WEIGHT_ROWS,
    ROUND281_STAGE4B_WATCH_TRIGGERS,
    render_round281_green_gate_review_markdown,
    render_round281_stage4b_4c_review_markdown,
    round281_audit_payload,
    round281_case_records,
    round281_case_rows,
    round281_deep_sub_archetype_rows,
    round281_shadow_weight_rows,
    round281_summary,
    write_round281_r12_loop13_reports,
)


class Round281R12Loop13AgricultureLifeServiceOtherPriceValidationTests(unittest.TestCase):
    def test_round281_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND281_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND281_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND281_REQUIRED_TARGET_ALIASES["FOOD_INFLATION_CLIMATE_INPUT_4C"],
            E2RArchetype.FOOD_INFLATION_CLIMATE_INPUT_4C.value,
        )
        self.assertEqual(
            ROUND281_REQUIRED_TARGET_ALIASES["ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE"],
            E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE.value,
        )
        self.assertEqual(
            ROUND281_REQUIRED_TARGET_ALIASES["OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE"],
            E2RArchetype.OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE.value,
        )

    def test_round281_archetype_definitions_capture_r12_loop13_gates(self) -> None:
        food = archetype_definition(E2RArchetype.FOOD_INFLATION_CLIMATE_INPUT_4C)
        feed = archetype_definition(E2RArchetype.ANIMAL_FEED_GRAIN_COST_4C)
        poultry = archetype_definition(E2RArchetype.POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK)
        machinery = archetype_definition(E2RArchetype.AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY)
        logistics = archetype_definition(E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2)
        trust = archetype_definition(E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE)
        waste = archetype_definition(E2RArchetype.WASTE_RECYCLING_INFRA_PLATFORM_STAGE2)
        demographic = archetype_definition(E2RArchetype.DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT)
        ipo = archetype_definition(E2RArchetype.OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE)

        self.assertIn("food inflation headline treated as food-company Green", food.false_positive_patterns)
        self.assertIn("feed tender failure", feed.stage4c_thesis_break_signals)
        self.assertIn("disease supply shock treated only as benefit", poultry.false_positive_patterns)
        self.assertIn("aging-farm theme treated as order backlog", machinery.false_positive_patterns)
        self.assertIn("logistics revenue uplift treated as Green without margin", logistics.false_positive_patterns)
        self.assertIn("data breach", trust.stage4c_thesis_break_signals)
        self.assertIn("recycling policy treated as company Green without tipping fee", waste.false_positive_patterns)
        self.assertIn("birthrate headline treated as childcare or education Green", demographic.false_positive_patterns)
        self.assertIn("IPO size treated as quality proof", ipo.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round281_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND281_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_true_for_life_service_trust_reference", record.green_guardrails)
            self.assertIn("direct_listed_hard_4c_confirmed_false", record.green_guardrails)
            self.assertIn("do_not_use_round281_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round281_summary()
        self.assertEqual(summary["round_id"], "round_209")
        self.assertEqual(summary["large_sector"], "AGRICULTURE_LIFE_SERVICE_OTHER")
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_reference_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 3)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["direct_listed_hard_4c_case_count"], 0)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])
        self.assertFalse(summary["direct_listed_hard_4c_confirmed"])

    def test_round281_cases_keep_input_service_trust_and_ipo_anchors_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND281_CASE_CANDIDATES}
        cabbage = by_id["r12_loop13_kimchi_cabbage_climate_food_input_cost"]
        feed = by_id["r12_loop13_feed_wheat_tender_livestock_cost_watch"]
        poultry = by_id["r12_loop13_poultry_egg_birdflu_supply_shock"]
        machinery = by_id["r12_loop13_daedong_tym_agri_machinery_labor_substitution"]
        logistics = by_id["r12_loop13_cj_logistics_shinsegae_alliance_unit_economics"]
        coupang = by_id["r12_loop13_coupang_life_service_trust_break_reference"]
        waste = by_id["r12_loop13_waste_recycling_food_waste_rfid_platform"]
        birthrate = by_id["r12_loop13_birthrate_rebound_childcare_education_event"]
        ipo = by_id["r12_loop13_dn_solutions_other_manufacturing_tools_ipo"]

        self.assertEqual(cabbage.primary_archetype, E2RArchetype.FOOD_INFLATION_CLIMATE_INPUT_4C)
        self.assertEqual(cabbage.extra_price_metrics["government_cabbage_stock_release_tonnes"], 24000)
        self.assertEqual(cabbage.extra_price_metrics["wholesale_price_per_cabbage_krw_september"], 9537)
        self.assertFalse(cabbage.extra_price_metrics["selling_price_pass_through_confirmed"])

        self.assertEqual(feed.primary_archetype, E2RArchetype.ANIMAL_FEED_GRAIN_COST_4C)
        self.assertEqual(feed.extra_price_metrics["tender_volume_tonnes"], 65000)
        self.assertEqual(feed.extra_price_metrics["effective_lowest_offer_usd_per_tonne"], 300.5)
        self.assertTrue(feed.extra_price_metrics["black_sea_russia_ukraine_loading_ports_prohibited"])

        self.assertEqual(poultry.primary_archetype, E2RArchetype.POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK)
        self.assertEqual(poultry.extra_price_metrics["brazil_commercial_flock_no_new_outbreak_period_days"], 28)
        self.assertEqual(poultry.extra_price_metrics["us_south_korea_egg_import_tariff_risk_pct"], 26)
        self.assertEqual(poultry.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(machinery.primary_archetype, E2RArchetype.AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY)
        self.assertEqual(machinery.extra_price_metrics["daedong_north_america_brand"], "Kioti")
        self.assertFalse(machinery.extra_price_metrics["actual_order_backlog_confirmed"])
        self.assertFalse(machinery.extra_price_metrics["north_america_sellthrough_confirmed"])

        self.assertEqual(logistics.primary_archetype, E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2)
        self.assertEqual(logistics.extra_price_metrics["annual_revenue_uplift_estimate_krw_bn"], 300)
        self.assertEqual(logistics.extra_price_metrics["event_price_krw"], 99100)
        self.assertEqual(logistics.extra_price_metrics["event_mae_pct"], -0.2)
        self.assertEqual(logistics.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(coupang.primary_archetype, E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE)
        self.assertEqual(coupang.extra_price_metrics["affected_users_mn"], 34)
        self.assertEqual(coupang.extra_price_metrics["coupang_share_decline_since_disclosure_pct"], -34)
        self.assertEqual(coupang.extra_price_metrics["naver_mobile_users_change_pct"], 23)
        self.assertTrue(coupang.hard_4c_confirmed)
        self.assertFalse(coupang.direct_listed_hard_4c_confirmed)

        self.assertEqual(waste.primary_archetype, E2RArchetype.WASTE_RECYCLING_INFRA_PLATFORM_STAGE2)
        self.assertEqual(waste.extra_price_metrics["food_waste_recycling_rate_2023_pct"], 96.8)
        self.assertEqual(waste.extra_price_metrics["national_rfid_units"], 150738)
        self.assertEqual(waste.extra_price_metrics["national_apartment_households_served_mn"], 8.54)

        self.assertEqual(birthrate.primary_archetype, E2RArchetype.DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT)
        self.assertEqual(birthrate.extra_price_metrics["fertility_rate_2025"], 0.80)
        self.assertEqual(birthrate.extra_price_metrics["births_2025_growth_pct"], 6.8)
        self.assertFalse(birthrate.extra_price_metrics["company_enrolment_ARPU_confirmed"])

        self.assertEqual(ipo.primary_archetype, E2RArchetype.OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE)
        self.assertEqual(ipo.extra_price_metrics["ipo_raise_max_krw_trn"], 1.6)
        self.assertEqual(ipo.extra_price_metrics["price_range_krw"], "65000-89700")
        self.assertTrue(ipo.extra_price_metrics["tariff_short_term_risk_acknowledged"])

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND281_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND281_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND281_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round281_shadow_weight_rows()}
        deep_rows = round281_deep_sub_archetype_rows()
        green_markdown = render_round281_green_gate_review_markdown()
        stage_markdown = render_round281_stage4b_4c_review_markdown()

        self.assertIn("input_cost_pass_through_confirmed", required)
        self.assertIn("logistics_unit_economics_confirmed", required)
        self.assertIn("data_trust_service_continuity_confirmed", required)
        self.assertIn("enrolment_arpu_retention_confirmed", required)
        self.assertIn("food_inflation_headline_only", forbidden)
        self.assertIn("IPO_size_without_aftermarket_demand", forbidden)
        self.assertIn("coupang_breach_competitor_benefit_overpriced", ROUND281_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("data_breach_or_service_trust_failure", ROUND281_HARD_4C_GATES)
        self.assertIn("service_trust_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Coupang", stage_markdown)
        self.assertIn("hard-4C", stage_markdown)
        self.assertEqual(len(ROUND281_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["FOOD_INFLATION_CLIMATE_INPUT_4C"]["input_cost_pass_through"], "+5")
        self.assertEqual(shadow_rows["ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE"]["event_penalty"], "-5")
        self.assertTrue(any("24,000 tonnes stock release" in row["terms"] for row in deep_rows))
        self.assertTrue(any("DN Solutions" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round281_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_281.md")
        self.assertEqual(audit["round_id"], "round_209")
        self.assertEqual(audit["large_sector"], ROUND281_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertFalse(audit["summary"]["direct_listed_hard_4c_confirmed"])
        self.assertIn("do_not_use_round281_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round281_r12_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round281_case_rows()
            self.assertEqual(len(records), len(ROUND281_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND281_CASE_CANDIDATES))
            self.assertIn("Coupang", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("input_cost_pass_through_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("service_trust_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[4]["extra_price_metrics"])["event_price_krw"], 99100)


if __name__ == "__main__":
    unittest.main()
