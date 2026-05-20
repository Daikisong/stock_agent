from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round243_r13_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round243_r13_loop10_cross_archetype_redteam_price_validation import (
    ROUND243_CASE_CANDIDATES,
    ROUND243_DEFAULT_STAGE3_BIAS,
    ROUND243_GREEN_FORBIDDEN_PATTERNS,
    ROUND243_GREEN_REQUIRED_FIELDS,
    ROUND243_HARD_4C_GATES,
    ROUND243_LARGE_SECTOR,
    ROUND243_PRICE_VALIDATION_FIELDS,
    ROUND243_REQUIRED_TARGET_ALIASES,
    ROUND243_SCORE_ADJUSTMENTS,
    ROUND243_SHADOW_WEIGHT_ROWS,
    ROUND243_STAGE4B_WATCH_TRIGGERS,
    render_round243_green_gate_review_markdown,
    render_round243_stage4b_4c_review_markdown,
    round243_audit_payload,
    round243_case_records,
    round243_case_rows,
    round243_deep_sub_archetype_rows,
    round243_shadow_weight_rows,
    round243_summary,
    write_round243_r13_loop10_reports,
)


class Round243R13Loop10CrossArchetypeRedTeamPriceValidationTests(unittest.TestCase):
    def test_round243_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND243_REQUIRED_TARGET_ALIASES), 11)
        self.assertTrue(set(ROUND243_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND243_REQUIRED_TARGET_ALIASES["AI_CAPITAL_ALLOCATION_EVENT_PREMIUM"],
            E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM.value,
        )
        self.assertEqual(
            ROUND243_REQUIRED_TARGET_ALIASES["CONTRACT_QUALITY_HARD_4C"],
            E2RArchetype.CONTRACT_QUALITY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND243_REQUIRED_TARGET_ALIASES["MACRO_GEOPOLITICAL_HARD_4C"],
            E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C.value,
        )
        self.assertEqual(
            ROUND243_REQUIRED_TARGET_ALIASES["PRICE_MOVED_WITHOUT_EVIDENCE"],
            E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE.value,
        )

    def test_new_round243_archetype_definitions_are_available(self) -> None:
        ai_event = archetype_definition(E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM)
        capex = archetype_definition(E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE)
        contract = archetype_definition(E2RArchetype.CONTRACT_QUALITY_HARD_4C)
        macro = archetype_definition(E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C)
        digital = archetype_definition(E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT)

        self.assertIn("stock jumps 20-30% before recurring AI revenue evidence", ai_event.stage4b_graduation_overheat_signals)
        self.assertIn("financing failure", capex.stage4c_thesis_break_signals)
        self.assertIn("contract value collapse", contract.stage4c_thesis_break_signals)
        self.assertIn("geopolitical energy chokepoint shock", macro.stage4c_thesis_break_signals)
        self.assertIn("stablecoin basket rallies 2-3x before regulated revenue evidence", digital.stage4b_graduation_overheat_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round243_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND243_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("r13_default_stage3_bias_redteam_first_after_price_validation", record.green_guardrails)

        summary = round243_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 2)
        self.assertEqual(summary["success_candidate_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 2)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["r13_default_stage3_bias"], ROUND243_DEFAULT_STAGE3_BIAS)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_sk_hynix_and_apr_validate_structural_success_but_need_4b_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND243_CASE_CANDIDATES}
        hynix = by_id["r13_loop10_sk_hynix_hbm_stage3_4b"]
        apr = by_id["r13_loop10_apr_medicube_structural_4b"]

        self.assertEqual(hynix.primary_archetype, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH)
        self.assertEqual(hynix.stage3_date.isoformat(), "2024-06-25")
        self.assertEqual(hynix.stage3_price_anchor, 222000.0)
        self.assertEqual(hynix.peak_price_anchor, 1447000.0)
        self.assertEqual(hynix.peak_return_from_stage3_pct, 551.8)
        self.assertEqual(hynix.extra_price_metrics["market_cap_2026_usd_bn"], 942.0)
        self.assertEqual(hynix.rerating_result, "true_rerating")
        self.assertIn("market_cap_milestone_headline", hynix.red_flag_fields)

        self.assertEqual(apr.primary_archetype, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH)
        self.assertEqual(apr.stage2_price_anchor, 158300.0)
        self.assertEqual(apr.extra_price_metrics["q4_2025_revenue_growth_pct"], 124.0)
        self.assertEqual(apr.extra_price_metrics["q4_2025_overseas_growth_pct"], 203.0)
        self.assertEqual(apr.extra_price_metrics["medicube_revenue_share_pct"], 91.7)
        self.assertEqual(apr.extra_price_metrics["tiktok_shop_revenue_usd_mn_min"], 102.9)
        self.assertIn("single_brand_device_concentration", apr.red_flag_fields)

    def test_samsung_sds_and_hyundai_steel_are_stage2_or_false_positive_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND243_CASE_CANDIDATES}
        sds = by_id["r13_loop10_samsung_sds_kkr_ai_event_4b"]
        steel = by_id["r13_loop10_hyundai_steel_policy_capex_failure"]

        self.assertEqual(sds.primary_archetype, E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM)
        self.assertEqual(sds.stage2_date.isoformat(), "2026-04-15")
        self.assertEqual(sds.mfe_1d, 20.8)
        self.assertEqual(sds.extra_price_metrics["relative_intraday_outperformance_vs_kospi_pp"], 17.8)
        self.assertEqual(sds.extra_price_metrics["combined_cash_plus_cb_krw_trn"], 7.607)
        self.assertIn("ai_capital_allocation_without_revenue", sds.red_flag_fields)
        self.assertEqual(sds.round_stage_failure_label, "should_not_be_green_yet")

        self.assertEqual(steel.primary_archetype, E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE)
        self.assertEqual(steel.stage2_date.isoformat(), "2025-03-25")
        self.assertEqual(steel.stage4b_date.isoformat(), "2025-03-25")
        self.assertEqual(steel.mfe_1d, 5.0)
        self.assertEqual(steel.mae_1d, -21.2)
        self.assertEqual(steel.extra_price_metrics["relative_underperformance_vs_benchmark_pp"], -15.7)
        self.assertEqual(steel.extra_price_metrics["net_profit_forecast_cut_pct"], -73.0)
        self.assertIn("capex_without_funding_or_margin", steel.red_flag_fields)
        self.assertEqual(steel.round_alignment_label, "false_positive_score_prevention")

    def test_contract_safety_and_macro_cases_are_hard_4c_gates(self) -> None:
        by_id = {case.case_id: case for case in ROUND243_CASE_CANDIDATES}
        contract = by_id["r13_loop10_lnf_tesla_cathode_contract_hard_4c"]
        jeju = by_id["r13_loop10_jeju_air_operational_safety_hard_4c"]
        hormuz = by_id["r13_loop10_hormuz_iran_macro_hard_4c"]

        self.assertTrue(contract.hard_4c_confirmed)
        self.assertEqual(contract.primary_archetype, E2RArchetype.CONTRACT_QUALITY_HARD_4C)
        self.assertEqual(contract.stage4c_date.isoformat(), "2025-12-29")
        self.assertEqual(contract.extra_price_metrics["initial_contract_value_usd_bn"], 2.9)
        self.assertEqual(contract.extra_price_metrics["revised_contract_value_usd"], 7386.0)
        self.assertEqual(contract.extra_price_metrics["contract_value_drawdown_pct"], -99.999745)
        self.assertIn("contract_value_collapse", contract.red_flag_fields)

        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.primary_archetype, E2RArchetype.OPERATIONAL_SAFETY_HARD_4C)
        self.assertEqual(jeju.mae_1d, -15.7)
        self.assertEqual(jeju.stage4c_price_anchor, 6920.0)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179.0)
        self.assertIn("fatal_safety_accident", jeju.red_flag_fields)

        self.assertTrue(hormuz.hard_4c_confirmed)
        self.assertEqual(hormuz.primary_archetype, E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C)
        self.assertEqual(hormuz.stage4c_date.isoformat(), "2026-05-18")
        self.assertEqual(hormuz.extra_price_metrics["global_company_cost_usd_bn"], 25.0)
        self.assertEqual(hormuz.extra_price_metrics["iea_supply_shortfall_2026_mn_bpd"], 1.78)
        self.assertEqual(hormuz.extra_price_metrics["iea_q2_deficit_mn_bpd"], 6.0)
        self.assertIn("geopolitical_energy_chokepoint_shock", hormuz.red_flag_fields)

    def test_stablecoin_cluster_is_price_moved_without_evidence(self) -> None:
        by_id = {case.case_id: case for case in ROUND243_CASE_CANDIDATES}
        cluster = by_id["r13_loop10_stablecoin_policy_theme_overheat"]

        self.assertEqual(cluster.primary_archetype, E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT)
        self.assertEqual(cluster.stage4b_date.isoformat(), "2025-06-01")
        self.assertEqual(cluster.extra_price_metrics["kakao_pay_mfe_month_pct_min"], 100.0)
        self.assertEqual(cluster.extra_price_metrics["lg_cns_mfe_month_pct"], 70.0)
        self.assertEqual(cluster.extra_price_metrics["aton_mfe_month_pct"], 80.0)
        self.assertEqual(cluster.extra_price_metrics["me2on_mfe_month_pct"], 200.0)
        self.assertFalse(cluster.extra_price_metrics["regulated_revenue_confirmed"])
        self.assertFalse(cluster.extra_price_metrics["issuer_license_confirmed"])
        self.assertEqual(cluster.score_price_alignment, "price_moved_without_evidence")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND243_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND243_GREEN_FORBIDDEN_PATTERNS)
        review = render_round243_green_gate_review_markdown()
        stage_review = render_round243_stage4b_4c_review_markdown()
        fields = set(ROUND243_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND243_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round243_shadow_weight_rows()}
        deep_rows = round243_deep_sub_archetype_rows()

        self.assertIn("price_path_after_evidence", required)
        self.assertIn("stage3_to_large_mfe_confirmation", required)
        self.assertIn("contract_operational_governance_security_trust_passed", required)
        self.assertIn("stablecoin_policy_theme_only", forbidden)
        self.assertIn("ai_capital_allocation_without_revenue", forbidden)
        self.assertIn("macro_geopolitical_chokepoint_ignored", forbidden)
        self.assertIn("macro_risk_overlay", axes)
        self.assertIn("hard_4c_early_warning", axes)
        self.assertIn("macro_cost_anchor", fields)
        self.assertIn("geopolitical_energy_chokepoint_shock", ROUND243_HARD_4C_GATES)
        self.assertIn("market_cap_milestone_headline", ROUND243_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("4C is about thesis break", stage_review)
        self.assertEqual(len(ROUND243_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["STRUCTURAL_SUCCESS_BUT_4B_WATCH"]["4b_watch_sensitivity"], "+5")
        self.assertEqual(shadow_rows["DIGITAL_ASSET_POLICY_OVERHEAT"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["MACRO_GEOPOLITICAL_HARD_4C"]["macro_risk_overlay"], "+5")
        self.assertTrue(any("SK Hynix HBM" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hormuz" in row["terms"] for row in deep_rows))
        self.assertTrue(any("KRW stablecoin" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round243_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_243.md")
        self.assertEqual(audit["large_sector"], ROUND243_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertEqual(audit["summary"]["r13_default_stage3_bias"], "redteam_first_after_price_validation")
        self.assertEqual(len(audit["shadow_weights"]), 8)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 8)
        self.assertIn("do_not_use_round243_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round243_r13_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round243_case_rows()
            self.assertEqual(len(records), len(ROUND243_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND243_CASE_CANDIDATES))
            self.assertIn("SK하이닉스", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Hormuz/Iran", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("macro_risk_overlay", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("MACRO_GEOPOLITICAL_HARD_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("KRW stablecoin", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["market_cap_2026_usd_bn"], 942.0)


if __name__ == "__main__":
    unittest.main()
