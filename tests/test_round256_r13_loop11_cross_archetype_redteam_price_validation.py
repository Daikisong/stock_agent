from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round256_r13_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round256_r13_loop11_cross_archetype_redteam_price_validation import (
    ROUND256_CASE_CANDIDATES,
    ROUND256_DEFAULT_STAGE3_BIAS,
    ROUND256_GREEN_FORBIDDEN_PATTERNS,
    ROUND256_GREEN_REQUIRED_FIELDS,
    ROUND256_HARD_4C_GATES,
    ROUND256_LARGE_SECTOR,
    ROUND256_PRICE_VALIDATION_FIELDS,
    ROUND256_REQUIRED_TARGET_ALIASES,
    ROUND256_SCORE_ADJUSTMENTS,
    ROUND256_SHADOW_WEIGHT_ROWS,
    ROUND256_STAGE4B_WATCH_TRIGGERS,
    render_round256_green_gate_review_markdown,
    render_round256_stage4b_4c_review_markdown,
    round256_audit_payload,
    round256_case_records,
    round256_case_rows,
    round256_deep_sub_archetype_rows,
    round256_shadow_weight_rows,
    round256_summary,
    write_round256_r13_loop11_reports,
)


class Round256R13Loop11CrossArchetypeRedTeamPriceValidationTests(unittest.TestCase):
    def test_round256_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND256_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND256_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND256_REQUIRED_TARGET_ALIASES["CONTRACT_HEADLINE_STAGE2_NOT_GREEN"],
            E2RArchetype.STAGE2_STRONG_NOT_GREEN.value,
        )
        self.assertEqual(
            ROUND256_REQUIRED_TARGET_ALIASES["AI_CAPITAL_ALLOCATION_EVENT_PREMIUM"],
            E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM.value,
        )
        self.assertEqual(
            ROUND256_REQUIRED_TARGET_ALIASES["POLICY_DIGITAL_ASSET_PRICE_ONLY"],
            E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT.value,
        )
        self.assertEqual(
            ROUND256_REQUIRED_TARGET_ALIASES["EVIDENCE_GOOD_BUT_PRICE_FAILED"],
            E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED.value,
        )
        self.assertEqual(
            ROUND256_REQUIRED_TARGET_ALIASES["CONTRACT_QUALITY_HARD_4C"],
            E2RArchetype.CONTRACT_QUALITY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND256_REQUIRED_TARGET_ALIASES["OPERATIONAL_TRUST_HARD_4C"],
            E2RArchetype.OPERATIONAL_TRUST_HARD_4C.value,
        )
        self.assertEqual(
            ROUND256_REQUIRED_TARGET_ALIASES["MACRO_GEOPOLITICAL_HARD_4C"],
            E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C.value,
        )

    def test_new_round256_archetype_definitions_are_available(self) -> None:
        ai_event = archetype_definition(E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM)
        contract = archetype_definition(E2RArchetype.CONTRACT_QUALITY_HARD_4C)
        macro = archetype_definition(E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C)
        digital = archetype_definition(E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT)

        self.assertIn("stock jumps 20-30% before recurring AI revenue evidence", ai_event.stage4b_graduation_overheat_signals)
        self.assertIn("contract value collapse", contract.stage4c_thesis_break_signals)
        self.assertIn("geopolitical energy chokepoint shock", macro.stage4c_thesis_break_signals)
        self.assertIn("stablecoin basket rallies 2-3x before regulated revenue evidence", digital.stage4b_graduation_overheat_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round256_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND256_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("r13_default_stage3_bias_redteam_first_after_price_validation", record.green_guardrails)

        summary = round256_summary()
        self.assertEqual(summary["analyst_round_id"], "round_184")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 2)
        self.assertEqual(summary["success_candidate_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 2)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["r13_default_stage3_bias"], ROUND256_DEFAULT_STAGE3_BIAS)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_sk_hynix_and_apr_validate_structural_success_but_need_4b_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND256_CASE_CANDIDATES}
        hynix = by_id["r13_loop11_sk_hynix_hbm_structural_success_4b_watch"]
        apr = by_id["r13_loop11_apr_medicube_structural_concentration_4b"]

        self.assertEqual(hynix.primary_archetype, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH)
        self.assertEqual(hynix.stage3_date.isoformat(), "2024-06-25")
        self.assertEqual(hynix.stage3_price_anchor, 222000.0)
        self.assertEqual(hynix.peak_price_anchor, 1447000.0)
        self.assertEqual(hynix.peak_return_from_stage3_pct, 551.8)
        self.assertEqual(hynix.mfe_1d, 5.7)
        self.assertEqual(hynix.extra_price_metrics["asml_euv_order_krw_tn"], 11.95)
        self.assertEqual(hynix.extra_price_metrics["market_cap_2026_usd_bn"], 942.0)
        self.assertEqual(hynix.rerating_result, "true_rerating")
        self.assertIn("market_cap_milestone_headline", hynix.red_flag_fields)

        self.assertEqual(apr.primary_archetype, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH)
        self.assertIsNone(apr.stage2_price_anchor)
        self.assertEqual(apr.extra_price_metrics["q4_2025_revenue_growth_pct"], 124.0)
        self.assertEqual(apr.extra_price_metrics["q4_2025_overseas_growth_pct"], 203.0)
        self.assertEqual(apr.extra_price_metrics["overseas_revenue_share_pct"], 87.0)
        self.assertEqual(apr.extra_price_metrics["medicube_revenue_share_pct"], 91.7)
        self.assertEqual(apr.extra_price_metrics["tiktok_shop_revenue_usd_mn"], 102.9)
        self.assertEqual(apr.extra_price_metrics["ulta_store_count_min"], 1400.0)
        self.assertIn("single_brand_device_concentration", apr.red_flag_fields)

    def test_samsung_ea_sds_and_stablecoin_are_stage2_or_4b_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND256_CASE_CANDIDATES}
        epc = by_id["r13_loop11_samsung_ea_fadhili_contract_stage2_4b"]
        digital = by_id["r13_loop11_samsung_sds_stablecoin_ai_digital_event_premium"]

        self.assertEqual(epc.primary_archetype, E2RArchetype.STAGE2_STRONG_NOT_GREEN)
        self.assertEqual(epc.stage2_date.isoformat(), "2024-04-03")
        self.assertEqual(epc.stage2_price_anchor, 26750.0)
        self.assertEqual(epc.mfe_1d, 8.5)
        self.assertEqual(epc.extra_price_metrics["contract_share_of_total_pct"], 77.9)
        self.assertEqual(epc.extra_price_metrics["target_upside_from_event_price_pct"], 30.8)
        self.assertIn("contract_headline_without_margin", epc.red_flag_fields)
        self.assertEqual(epc.round_rerating_label, "EPC_order_stage2_not_green")

        self.assertEqual(digital.primary_archetype, E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM)
        self.assertEqual(digital.stage2_date.isoformat(), "2026-04-15")
        self.assertEqual(digital.stage4b_status, "4B-elevated")
        self.assertEqual(digital.mfe_1d, 20.8)
        self.assertEqual(digital.extra_price_metrics["samsung_sds_relative_outperformance_pp"], 17.8)
        self.assertEqual(digital.extra_price_metrics["combined_cash_plus_cb_krw_trn"], 7.607)
        self.assertEqual(digital.extra_price_metrics["me2on_mfe_pct"], 200.0)
        self.assertFalse(digital.extra_price_metrics["issuer_license_confirmed"])
        self.assertFalse(digital.extra_price_metrics["fee_revenue_confirmed"])
        self.assertIn("stablecoin_policy_theme_only", digital.red_flag_fields)
        self.assertEqual(digital.score_price_alignment, "price_moved_without_evidence")

    def test_contract_safety_and_macro_cases_are_hard_4c_gates(self) -> None:
        by_id = {case.case_id: case for case in ROUND256_CASE_CANDIDATES}
        contract = by_id["r13_loop11_lges_lnf_contract_quality_hard_4c"]
        trust = by_id["r13_loop11_skt_kumho_operational_trust_hard_4c"]
        hormuz = by_id["r13_loop11_hormuz_iran_macro_hard_4c"]

        self.assertTrue(contract.hard_4c_confirmed)
        self.assertEqual(contract.primary_archetype, E2RArchetype.CONTRACT_QUALITY_HARD_4C)
        self.assertEqual(contract.stage4c_date.isoformat(), "2025-12-29")
        self.assertEqual(contract.extra_price_metrics["lges_total_lost_expected_revenue_krw_tn"], 13.5)
        self.assertEqual(contract.extra_price_metrics["lges_lost_revenue_vs_2024_revenue_pct"], 52.7)
        self.assertEqual(contract.extra_price_metrics["lnf_initial_contract_value_usd_bn"], 2.9)
        self.assertEqual(contract.extra_price_metrics["lnf_revised_contract_value_usd"], 7386.0)
        self.assertEqual(contract.extra_price_metrics["lnf_contract_value_collapse_pct"], 99.999745)
        self.assertIn("contract_value_collapse", contract.red_flag_fields)

        self.assertTrue(trust.hard_4c_confirmed)
        self.assertEqual(trust.primary_archetype, E2RArchetype.OPERATIONAL_TRUST_HARD_4C)
        self.assertEqual(trust.stage4c_date.isoformat(), "2025-04-28")
        self.assertEqual(trust.extra_price_metrics["skt_initial_close_mae_pct"], -6.7)
        self.assertEqual(trust.extra_price_metrics["skt_revenue_forecast_cut_krw_bn"], 800.0)
        self.assertEqual(trust.extra_price_metrics["skt_fine_krw_bn"], 134.0)
        self.assertEqual(trust.extra_price_metrics["kumho_share_of_global_capacity_pct"], 20.0)
        self.assertIn("data_breach_or_security_failure", trust.red_flag_fields)
        self.assertIn("factory_fire_or_supply_disruption", trust.red_flag_fields)

        self.assertTrue(hormuz.hard_4c_confirmed)
        self.assertEqual(hormuz.primary_archetype, E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C)
        self.assertEqual(hormuz.stage4c_date.isoformat(), "2026-03-04")
        self.assertEqual(hormuz.mae_1d, -12.06)
        self.assertEqual(hormuz.stage4c_price_anchor, 5093.54)
        self.assertEqual(hormuz.extra_price_metrics["market_cap_wipeout_2d_usd_bn"], 553.82)
        self.assertEqual(hormuz.extra_price_metrics["krw_intraday_low_per_usd"], 1505.8)
        self.assertEqual(hormuz.extra_price_metrics["hyundai_motor_mae_pct"], -15.8)
        self.assertEqual(hormuz.extra_price_metrics["sk_hynix_mae_pct"], -9.6)
        self.assertIn("geopolitical_energy_chokepoint_shock", hormuz.red_flag_fields)

    def test_lg_cns_and_samsung_bio_are_good_evidence_but_price_failed(self) -> None:
        by_id = {case.case_id: case for case in ROUND256_CASE_CANDIDATES}
        failed = by_id["r13_loop11_lg_cns_samsung_biologics_good_evidence_price_failed"]

        self.assertEqual(failed.primary_archetype, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED)
        self.assertEqual(failed.extra_price_metrics["lg_cns_debut_mae_pct"], -3.55)
        self.assertEqual(failed.extra_price_metrics["lg_cns_op_margin_pct"], 7.8)
        self.assertEqual(failed.extra_price_metrics["samsung_biologics_facility_capacity_l"], 60000.0)
        self.assertEqual(failed.extra_price_metrics["samsung_biologics_relative_underperformance_pp"], -2.4)
        self.assertEqual(failed.score_price_alignment, "evidence_good_but_price_failed")
        self.assertIn("good_news_but_price_failed", failed.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND256_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND256_GREEN_FORBIDDEN_PATTERNS)
        review = render_round256_green_gate_review_markdown()
        stage_review = render_round256_stage4b_4c_review_markdown()
        fields = set(ROUND256_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND256_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round256_shadow_weight_rows()}
        deep_rows = round256_deep_sub_archetype_rows()

        self.assertIn("price_path_after_evidence", required)
        self.assertIn("stage3_to_large_mfe_confirmation", required)
        self.assertIn("actual_calloff_margin_cash_collection_for_contracts", required)
        self.assertIn("no_macro_hard_overlay", required)
        self.assertIn("stablecoin_policy_theme_only", forbidden)
        self.assertIn("ai_capital_allocation_without_revenue", forbidden)
        self.assertIn("macro_energy_fx_shock_ignored", forbidden)
        self.assertIn("macro_risk_overlay", axes)
        self.assertIn("fresh_rerating_response", axes)
        self.assertIn("good_news_but_price_failed", axes)
        self.assertIn("macro_cost_anchor", fields)
        self.assertIn("geopolitical_energy_chokepoint_shock", ROUND256_HARD_4C_GATES)
        self.assertIn("market_cap_milestone_headline", ROUND256_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("stablecoin_policy_theme_two_to_three_x_move", ROUND256_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("4C is about thesis break", stage_review)
        self.assertEqual(len(ROUND256_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["STRUCTURAL_SUCCESS_BUT_4B_WATCH"]["4b_watch_sensitivity"], "+5")
        self.assertEqual(shadow_rows["DIGITAL_ASSET_POLICY_OVERHEAT"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["EVIDENCE_GOOD_BUT_PRICE_FAILED"]["event_penalty"], "-4")
        self.assertEqual(shadow_rows["OPERATIONAL_TRUST_HARD_4C"]["governance_security_redteam"], "+5")
        self.assertEqual(shadow_rows["MACRO_GEOPOLITICAL_HARD_4C"]["macro_risk_overlay"], "+5")
        self.assertTrue(any("SK Hynix HBM" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Samsung E&A" in row["terms"] for row in deep_rows))
        self.assertTrue(any("LG CNS IPO" in row["terms"] for row in deep_rows))
        self.assertTrue(any("SK Telecom data breach" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hormuz" in row["terms"] for row in deep_rows))
        self.assertTrue(any("KRW stablecoin" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round256_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_256.md")
        self.assertEqual(audit["analyst_round_id"], "round_184")
        self.assertEqual(audit["large_sector"], ROUND256_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertEqual(audit["summary"]["r13_default_stage3_bias"], "redteam_first_after_price_validation")
        self.assertEqual(len(audit["shadow_weights"]), 9)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 9)
        self.assertIn("do_not_use_round256_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round256_r13_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round256_case_rows()
            self.assertEqual(len(records), len(ROUND256_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND256_CASE_CANDIDATES))
            self.assertIn("SK하이닉스", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Samsung E&A", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Hormuz/Iran", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("macro_risk_overlay", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("MACRO_GEOPOLITICAL_HARD_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("KRW stablecoin", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertIn("SK Telecom data breach", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["market_cap_2026_usd_bn"], 942.0)


if __name__ == "__main__":
    unittest.main()
