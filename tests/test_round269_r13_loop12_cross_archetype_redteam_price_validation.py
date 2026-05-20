from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round269_r13_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round269_r13_loop12_cross_archetype_redteam_price_validation import (
    ROUND269_CASE_CANDIDATES,
    ROUND269_DEFAULT_STAGE3_BIAS,
    ROUND269_GREEN_FORBIDDEN_PATTERNS,
    ROUND269_GREEN_REQUIRED_FIELDS,
    ROUND269_HARD_4C_GATES,
    ROUND269_LARGE_SECTOR,
    ROUND269_PRICE_VALIDATION_FIELDS,
    ROUND269_REQUIRED_TARGET_ALIASES,
    ROUND269_SCORE_ADJUSTMENTS,
    ROUND269_SHADOW_WEIGHT_ROWS,
    ROUND269_STAGE4B_WATCH_TRIGGERS,
    render_round269_green_gate_review_markdown,
    render_round269_stage4b_4c_review_markdown,
    round269_audit_payload,
    round269_case_records,
    round269_case_rows,
    round269_deep_sub_archetype_rows,
    round269_shadow_weight_rows,
    round269_summary,
    write_round269_r13_loop12_reports,
)


class Round269R13Loop12CrossArchetypeRedTeamPriceValidationTests(unittest.TestCase):
    def test_round269_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND269_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND269_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND269_REQUIRED_TARGET_ALIASES["TRUE_STRUCTURAL_RERATING"],
            E2RArchetype.TRUE_STRUCTURAL_RERATING.value,
        )
        self.assertEqual(
            ROUND269_REQUIRED_TARGET_ALIASES["STRUCTURAL_SUCCESS_NOW_4B"],
            E2RArchetype.STRUCTURAL_SUCCESS_NOW_4B.value,
        )
        self.assertEqual(
            ROUND269_REQUIRED_TARGET_ALIASES["CONTRACT_HEADLINE_STAGE2_NOT_GREEN"],
            E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN.value,
        )
        self.assertEqual(
            ROUND269_REQUIRED_TARGET_ALIASES["PLATFORM_TRUST_4C_WATCH"],
            E2RArchetype.PLATFORM_TRUST_4C_WATCH.value,
        )

    def test_round269_archetype_definitions_encode_r13_loop12_gates(self) -> None:
        true_structural = archetype_definition(E2RArchetype.TRUE_STRUCTURAL_RERATING)
        now_4b = archetype_definition(E2RArchetype.STRUCTURAL_SUCCESS_NOW_4B)
        contract = archetype_definition(E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN)
        digital = archetype_definition(E2RArchetype.DIGITAL_POLICY_PRICE_ONLY)
        platform = archetype_definition(E2RArchetype.PLATFORM_TRUST_4C_WATCH)
        combined = archetype_definition(E2RArchetype.OPERATIONAL_TRUST_AND_MACRO_HARD_4C)

        self.assertIn("revenue, EPS, FCF, price path and RedTeam all align after evidence", true_structural.stage3_high_conviction_signals)
        self.assertIn("3x-5x+ move", now_4b.stage4b_graduation_overheat_signals)
        self.assertIn("progress revenue, margin, working capital, and cash collection verified before Green", contract.stage3_high_conviction_signals)
        self.assertIn("stablecoin or digital-policy basket moves 2-3x before regulated revenue", digital.stage4b_graduation_overheat_signals)
        self.assertIn("abnormal withdrawal", platform.stage4c_thesis_break_signals)
        self.assertIn("safety, security, and macro hard gates override positive evidence", combined.stage3_high_conviction_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round269_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND269_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("r13_default_stage3_bias_redteam_first_after_price_validation", record.green_guardrails)
            self.assertIn("do_not_invent_price_or_stage_dates", record.green_guardrails)

        summary = round269_summary()
        self.assertEqual(summary["analyst_round_id"], "round_197")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 2)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_case_count"], 5)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertEqual(summary["aligned_count"], 2)
        self.assertEqual(summary["r13_default_stage3_bias"], ROUND269_DEFAULT_STAGE3_BIAS)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_sk_hynix_and_samyang_validate_success_but_keep_4b_watch_context(self) -> None:
        by_id = {case.case_id: case for case in ROUND269_CASE_CANDIDATES}
        hynix = by_id["r13_loop12_sk_hynix_true_stage3_now_4b"]
        samyang = by_id["r13_loop12_samyang_kfood_export_stage3_candidate"]

        self.assertEqual(hynix.primary_archetype, E2RArchetype.STRUCTURAL_SUCCESS_NOW_4B)
        self.assertEqual(hynix.stage3_date.isoformat(), "2024-06-25")
        self.assertEqual(hynix.stage3_price_anchor, 222000.0)
        self.assertEqual(hynix.extra_price_metrics["op_estimate_2025_krw_tn"], 53.0)
        self.assertEqual(hynix.extra_price_metrics["q2_2024_op_krw_tn"], 5.47)
        self.assertEqual(hynix.extra_price_metrics["market_cap_2026_usd_bn"], 942.0)
        self.assertEqual(hynix.peak_return_from_stage3_pct, 842.0)
        self.assertEqual(hynix.score_price_alignment, "aligned")
        self.assertIn("market_cap_milestone_942bn_usd", hynix.red_flag_fields)

        self.assertEqual(samyang.primary_archetype, E2RArchetype.TRUE_STRUCTURAL_RERATING)
        self.assertEqual(samyang.stage3_date.isoformat(), "2024-06-14")
        self.assertEqual(samyang.stage3_price_anchor, 647000.0)
        self.assertEqual(samyang.mfe_1d, 5.7)
        self.assertEqual(samyang.extra_price_metrics["implied_prior_close_krw"], 611921.0)
        self.assertEqual(samyang.extra_price_metrics["target_upside_pct"], 28.3)
        self.assertEqual(samyang.extra_price_metrics["op_growth_estimate_pct"], 84.0)
        self.assertIn("single_sku_concentration_watch", samyang.red_flag_fields)

    def test_contract_capex_stablecoin_and_platform_cases_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND269_CASE_CANDIDATES}
        epc = by_id["r13_loop12_samsung_ea_fadhili_contract_stage2"]
        steel = by_id["r13_loop12_hyundai_steel_us_capex_false_positive"]
        stablecoin = by_id["r13_loop12_stablecoin_policy_overheat"]
        naver = by_id["r13_loop12_naver_dunamu_platform_trust_watch"]

        self.assertEqual(epc.primary_archetype, E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN)
        self.assertEqual(epc.stage2_price_anchor, 26750.0)
        self.assertEqual(epc.mfe_1d, 8.5)
        self.assertEqual(epc.extra_price_metrics["relative_outperformance_pp"], 9.9)
        self.assertIn("cash_collection_unconfirmed", epc.red_flag_fields)

        self.assertEqual(steel.primary_archetype, E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE)
        self.assertEqual(steel.mae_1d, -21.2)
        self.assertEqual(steel.extra_price_metrics["relative_underperformance_vs_kospi_pp"], -15.7)
        self.assertTrue(steel.extra_price_metrics["remaining_funding_unclear"])
        self.assertEqual(steel.score_price_alignment, "false_positive_score")

        self.assertEqual(stablecoin.primary_archetype, E2RArchetype.DIGITAL_POLICY_PRICE_ONLY)
        self.assertEqual(stablecoin.extra_price_metrics["me2on_mfe_pct"], 200.0)
        self.assertEqual(stablecoin.extra_price_metrics["margin_loans_krw_tn"], 20.5)
        self.assertFalse(stablecoin.extra_price_metrics["issuer_license_confirmed"])
        self.assertEqual(stablecoin.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(naver.primary_archetype, E2RArchetype.PLATFORM_TRUST_4C_WATCH)
        self.assertEqual(naver.extra_price_metrics["deal_value_krw_tn"], 15.13)
        self.assertEqual(naver.extra_price_metrics["event_swing_pp"], -11.2)
        self.assertEqual(naver.extra_price_metrics["abnormal_withdrawal_krw_bn"], 54.0)
        self.assertIn("exchange_trust_gate_open", naver.red_flag_fields)

    def test_contract_quality_safety_security_and_macro_cases_are_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND269_CASE_CANDIDATES}
        lges = by_id["r13_loop12_lges_contract_quality_hard_4c"]
        hardpack = by_id["r13_loop12_hard_4c_reference_pack_jeju_skt_macro"]

        self.assertTrue(lges.hard_4c_confirmed)
        self.assertEqual(lges.primary_archetype, E2RArchetype.CONTRACT_QUALITY_HARD_4C)
        self.assertEqual(lges.stage4c_date.isoformat(), "2025-12-26")
        self.assertEqual(lges.extra_price_metrics["total_lost_expected_revenue_krw_tn"], 13.5)
        self.assertEqual(lges.extra_price_metrics["lost_revenue_vs_2024_revenue_pct"], 52.7)
        self.assertIn("contract_cancellation_or_value_collapse", lges.red_flag_fields)

        self.assertTrue(hardpack.hard_4c_confirmed)
        self.assertEqual(hardpack.primary_archetype, E2RArchetype.OPERATIONAL_TRUST_HARD_4C)
        self.assertEqual(hardpack.stage4c_date.isoformat(), "2024-12-30")
        self.assertEqual(hardpack.mae_1d, -15.7)
        self.assertEqual(hardpack.stage4c_price_anchor, 5093.54)
        self.assertEqual(hardpack.extra_price_metrics["jeju_intraday_mae_pct"], -15.7)
        self.assertEqual(hardpack.extra_price_metrics["skt_close_mae_pct"], -6.7)
        self.assertEqual(hardpack.extra_price_metrics["kospi_mae_pct"], -12.06)
        self.assertEqual(hardpack.extra_price_metrics["hyundai_motor_mae_pct"], -15.8)
        self.assertIn("macro_energy_chokepoint_shock", hardpack.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND269_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND269_GREEN_FORBIDDEN_PATTERNS)
        review = render_round269_green_gate_review_markdown()
        stage_review = render_round269_stage4b_4c_review_markdown()
        fields = set(ROUND269_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND269_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round269_shadow_weight_rows()}
        deep_rows = round269_deep_sub_archetype_rows()

        self.assertIn("revenue_eps_fcf_conversion_confirmed", required)
        self.assertIn("price_path_after_evidence", required)
        self.assertIn("platform_trust_and_security_cleared", required)
        self.assertIn("contract_headline_only", forbidden)
        self.assertIn("stablecoin_policy_theme_only", forbidden)
        self.assertIn("data_breach_or_safety_failure", forbidden)
        self.assertIn("stage3_evidence_to_price_alignment", axes)
        self.assertIn("M&A_without_trust_or_closing", axes)
        self.assertIn("hard_4c_before_price_damage", fields)
        self.assertIn("stage3_after_3x_to_5x_or_more_move", ROUND269_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("contract_cancellation_or_value_collapse", ROUND269_HARD_4C_GATES)
        self.assertIn("exchange_abnormal_withdrawal_or_hack", ROUND269_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("4C is about thesis break", stage_review)
        self.assertEqual(len(ROUND269_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["STRUCTURAL_SUCCESS_NOW_4B"]["4b_watch_sensitivity"], "+5")
        self.assertEqual(shadow_rows["DIGITAL_POLICY_PRICE_ONLY"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["PLATFORM_TRUST_4C_WATCH"]["platform_trust"], "+5")
        self.assertEqual(shadow_rows["MACRO_GEOPOLITICAL_HARD_4C"]["macro_energy_fx_overlay"], "+5")
        self.assertTrue(any("SK Hynix HBM" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Samyang Foods Buldak" in row["terms"] for row in deep_rows))
        self.assertTrue(any("NAVER Financial" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Jeju Air crash" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round269_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_269.md")
        self.assertEqual(audit["analyst_round_id"], "round_197")
        self.assertEqual(audit["large_sector"], ROUND269_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertEqual(audit["summary"]["r13_default_stage3_bias"], "redteam_first_after_price_validation")
        self.assertEqual(len(audit["shadow_weights"]), 9)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 9)
        self.assertIn("do_not_use_round269_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round269_r13_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round269_case_rows()
            self.assertEqual(len(records), len(ROUND269_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND269_CASE_CANDIDATES))
            self.assertIn("SK Hynix", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Samsung E&A", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Middle East/Iran", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("stage3_evidence_to_price_alignment", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("MACRO_GEOPOLITICAL_HARD_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("KRW stablecoin", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["market_cap_2026_usd_bn"], 942.0)


if __name__ == "__main__":
    unittest.main()
