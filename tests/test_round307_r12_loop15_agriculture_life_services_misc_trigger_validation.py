from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round307_r12_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round307_r12_loop15_agriculture_life_services_misc_trigger_validation import (
    ROUND307_CASE_CANDIDATES,
    ROUND307_GREEN_BLOCKERS,
    ROUND307_HARD_4C_GATES,
    ROUND307_LARGE_SECTOR,
    ROUND307_REQUIRED_TARGET_ALIASES,
    ROUND307_SCORE_DOWN_AXES,
    ROUND307_SCORE_UP_AXES,
    ROUND307_SHADOW_WEIGHT_ROWS,
    ROUND307_STAGE2_ACTIONABLE_RULES,
    ROUND307_STAGE3_GREEN_RULES,
    ROUND307_STAGE3_YELLOW_RULES,
    ROUND307_STAGE4B_WATCH_TRIGGERS,
    ROUND307_TRIGGER_RECORDS,
    render_round307_stage4b_4c_review_markdown,
    render_round307_stage_rules_markdown,
    render_round307_trigger_grid_markdown,
    round307_audit_payload,
    round307_case_records,
    round307_case_rows,
    round307_shadow_weight_rows,
    round307_summary,
    round307_trigger_rows,
    write_round307_r12_loop15_reports,
)


class Round307R12Loop15AgricultureLifeServicesMiscTriggerValidationTests(unittest.TestCase):
    def test_round307_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND307_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND307_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND307_REQUIRED_TARGET_ALIASES["FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT"],
            E2RArchetype.FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT.value,
        )
        self.assertEqual(
            ROUND307_REQUIRED_TARGET_ALIASES["ECOMMERCE_DATA_BREACH_HARD_4C"],
            E2RArchetype.ECOMMERCE_DATA_BREACH_HARD_4C.value,
        )
        self.assertEqual(
            ROUND307_REQUIRED_TARGET_ALIASES["SHRINKFLATION_PRICE_REGULATION_4C_WATCH"],
            E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH.value,
        )

    def test_archetype_definitions_capture_r12_loop15_rules(self) -> None:
        fertilizer = archetype_definition(E2RArchetype.FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT)
        feed = archetype_definition(E2RArchetype.AGRI_FEED_PRICE_INPUT_COST_4C_WATCH)
        ai_textbook = archetype_definition(E2RArchetype.AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C)
        hagwon = archetype_definition(E2RArchetype.HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2)
        delivery = archetype_definition(E2RArchetype.FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B)
        breach = archetype_definition(E2RArchetype.ECOMMERCE_DATA_BREACH_HARD_4C)
        ip = archetype_definition(E2RArchetype.CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B)
        recycling = archetype_definition(E2RArchetype.PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE)
        shrink = archetype_definition(E2RArchetype.SHRINKFLATION_PRICE_REGULATION_4C_WATCH)

        self.assertIn("domestic ASP", " ".join(fertilizer.stage3_high_conviction_signals))
        self.assertIn("feed price pressure", " ".join(feed.stage3_high_conviction_signals))
        self.assertIn("official textbook status downgrade", " ".join(ai_textbook.stage4c_thesis_break_signals))
        self.assertIn("listed-company", " ".join(hagwon.stage3_high_conviction_signals))
        self.assertIn("binding offer", " ".join(delivery.stage3_high_conviction_signals))
        self.assertIn("large-scale personal-info exposure", " ".join(breach.stage4c_thesis_break_signals))
        self.assertIn("one-hit-wonder", " ".join(ip.stage4b_graduation_overheat_signals))
        self.assertIn("actual recycling yield", " ".join(recycling.stage2_candidate_signals))
        self.assertIn("price-control pressure", " ".join(shrink.stage1_radar_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round307_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND307_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round307_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_agriculture_life_service_policy_or_event_headline_as_green", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r12_loop15_pinkfong_babyshark_ipo"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r12_loop15_coupang_data_breach_life_service_4c"].green_guardrails)

        summary = round307_summary()
        self.assertEqual(summary["round_id"], "round_235")
        self.assertEqual(summary["large_sector"], ROUND307_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 10)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 1)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_policy_events_platform_4c_and_ip_4b(self) -> None:
        by_id = {case.case_id: case for case in ROUND307_CASE_CANDIDATES}
        fertilizer = by_id["r12_loop15_fertilizer_export_control_korea_basket"]
        feed = by_id["r12_loop15_feed_wheat_tender_input_cost"]
        ai_textbook = by_id["r12_loop15_ai_digital_textbook_policy_rollback"]
        hagwon = by_id["r12_loop15_hagwon_preschool_private_education"]
        baemin = by_id["r12_loop15_naver_uber_baemin_food_delivery_ma"]
        coupang = by_id["r12_loop15_coupang_data_breach_life_service_4c"]
        pinkfong = by_id["r12_loop15_pinkfong_babyshark_ipo"]
        recycling = by_id["r12_loop15_plastic_recycling_policy_false_positive"]

        self.assertEqual(fertilizer.primary_archetype, E2RArchetype.FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT)
        self.assertEqual(fertilizer.extra_price_metrics["international_urea_price_rise_from_prewar_pct"], 40)
        self.assertEqual(fertilizer.score_price_alignment, "false_positive_score")

        self.assertEqual(feed.primary_archetype, E2RArchetype.AGRI_FEED_PRICE_INPUT_COST_4C_WATCH)
        self.assertEqual(feed.extra_price_metrics["lowest_offer_cargill_usd_per_ton_cnf"], 298.5)

        self.assertEqual(ai_textbook.primary_archetype, E2RArchetype.AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C)
        self.assertIn("official_textbook_status_downgrade", ai_textbook.red_flag_fields)

        self.assertEqual(hagwon.extra_price_metrics["under_six_hagwon_enrollment_pct"], 47.6)
        self.assertIn("listed_company_margin_missing", hagwon.red_flag_fields)

        self.assertEqual(baemin.extra_price_metrics["reported_baemin_bid_krw_trn"], 8.0)
        self.assertEqual(baemin.event_mfe_pct, 5.6)

        self.assertTrue(coupang.hard_4c_confirmed)
        self.assertEqual(coupang.event_mae_pct, -4.4)
        self.assertEqual(coupang.event_mfe_pct, 9.0)

        self.assertEqual(pinkfong.primary_archetype, E2RArchetype.CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B)
        self.assertEqual(pinkfong.event_mfe_pct, 62.0)
        self.assertIn("one_hit_wonder_4b", pinkfong.red_flag_fields)

        self.assertEqual(recycling.extra_price_metrics["greenpeace_estimated_real_recycling_rate_pct"], 27)
        self.assertEqual(recycling.stage_candidate, "Stage2 policy only")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round307_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round307_shadow_weight_rows()}
        rules_md = render_round307_stage_rules_markdown()
        trigger_md = render_round307_trigger_grid_markdown()
        stage_md = render_round307_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND307_TRIGGER_RECORDS), 10)
        self.assertEqual(trigger_rows["r12l15_fertilizer_china_T1"]["promote_to"], "Stage2")
        self.assertEqual(trigger_rows["r12l15_coupang_breach_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r12l15_pinkfong_ipo_T2"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(len(ROUND307_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT"]["domestic_asp_margin_pass_through"], "+5")
        self.assertEqual(shadow_rows["AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C"]["school_contract_paid_adoption"], "+5")
        self.assertEqual(shadow_rows["ECOMMERCE_DATA_BREACH_HARD_4C"]["platform_scale_without_security_penalty"], "-5")
        self.assertIn("policy_or_supply_shock_closes_into_domestic_asp_margin_contract_or_paid_adoption", ROUND307_STAGE2_ACTIONABLE_RULES)
        self.assertIn("trigger_can_change_eps_op_fcf_path_but_one_core_gate_remains", ROUND307_STAGE3_YELLOW_RULES)
        self.assertIn("children_ip_has_recurring_franchise_revenue_not_one_hit_only", ROUND307_STAGE3_GREEN_RULES)
        self.assertIn("platform_scale_without_security", ROUND307_GREEN_BLOCKERS)
        self.assertIn("domestic_ASP_margin_pass_through", ROUND307_SCORE_UP_AXES)
        self.assertIn("viral_IP_without_next_franchise", ROUND307_SCORE_DOWN_AXES)
        self.assertIn("ma_teaser_is_priced_as_binding_acquisition", ROUND307_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("large_customer_data_breach", ROUND307_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r12_loop15_pinkfong_babyshark_ipo", trigger_md)
        self.assertIn("r12_loop15_coupang_data_breach_life_service_4c", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round307_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_307.md")
        self.assertEqual(audit["round_id"], "round_235")
        self.assertEqual(audit["large_sector"], ROUND307_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_policy_supply_shock_ma_teaser_or_viral_ip_as_green", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--triggers",
                "triggers.jsonl",
                "--audit",
                "audit.json",
                "--weight-profile",
                "weights.csv",
            ]
        )
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.triggers, "triggers.jsonl")
        self.assertEqual(args.audit, "audit.json")
        self.assertEqual(args.weight_profile, "weights.csv")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round307_r12_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round307_case_rows()
            self.assertEqual(len(records), len(ROUND307_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND307_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND307_TRIGGER_RECORDS))


if __name__ == "__main__":
    unittest.main()
