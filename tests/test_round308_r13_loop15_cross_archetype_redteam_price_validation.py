from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round308_r13_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round308_r13_loop15_cross_archetype_redteam_price_validation import (
    ROUND308_CASE_CANDIDATES,
    ROUND308_GREEN_BLOCKERS,
    ROUND308_HARD_4C_GATES,
    ROUND308_LARGE_SECTOR,
    ROUND308_REQUIRED_TARGET_ALIASES,
    ROUND308_ROW_SEPARATION_RULES,
    ROUND308_SCORE_DOWN_AXES,
    ROUND308_SCORE_UP_AXES,
    ROUND308_SHADOW_WEIGHT_ROWS,
    ROUND308_STAGE2_ACTIONABLE_RULES,
    ROUND308_STAGE3_GREEN_RULES,
    ROUND308_STAGE3_YELLOW_RULES,
    ROUND308_STAGE4B_WATCH_TRIGGERS,
    ROUND308_TRIGGER_RECORDS,
    render_round308_stage4b_4c_review_markdown,
    render_round308_stage_rules_markdown,
    render_round308_trigger_grid_markdown,
    round308_audit_payload,
    round308_case_records,
    round308_case_rows,
    round308_shadow_weight_rows,
    round308_summary,
    round308_trigger_rows,
    write_round308_r13_loop15_reports,
)


class Round308R13Loop15CrossArchetypeRedTeamValidationTests(unittest.TestCase):
    def test_round308_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND308_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND308_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND308_REQUIRED_TARGET_ALIASES["EARLY_EVIDENCE_MISSED_STRUCTURAL"],
            E2RArchetype.EARLY_EVIDENCE_MISSED_STRUCTURAL.value,
        )
        self.assertEqual(
            ROUND308_REQUIRED_TARGET_ALIASES["PLATFORM_SECURITY_HARD_4C"],
            E2RArchetype.PLATFORM_SECURITY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND308_REQUIRED_TARGET_ALIASES["OHLC_BACKFILL_SEPARATION_REQUIRED"],
            E2RArchetype.OHLC_BACKFILL_SEPARATION_REQUIRED.value,
        )

    def test_archetype_definitions_capture_r13_loop15_rules(self) -> None:
        early = archetype_definition(E2RArchetype.EARLY_EVIDENCE_MISSED_STRUCTURAL)
        delivery = archetype_definition(E2RArchetype.DELIVERY_TO_REVENUE_STAGE2_YELLOW)
        capital = archetype_definition(E2RArchetype.STRATEGIC_CAPITAL_WITH_DILUTION_4B)
        control = archetype_definition(E2RArchetype.CONTROL_BATTLE_GOVERNANCE_4B_4C)
        price_fail = archetype_definition(E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED)
        security = archetype_definition(E2RArchetype.PLATFORM_SECURITY_HARD_4C)
        policy = archetype_definition(E2RArchetype.POLICY_THEME_OVERHEAT_4B)
        ohlc = archetype_definition(E2RArchetype.OHLC_BACKFILL_SEPARATION_REQUIRED)

        self.assertIn("ASP increase", " ".join(early.stage1_radar_signals))
        self.assertIn("delivery count", " ".join(delivery.stage2_candidate_signals))
        self.assertIn("convertible bond", " ".join(capital.stage1_radar_signals))
        self.assertIn("regulator revision order", " ".join(control.stage4c_thesis_break_signals))
        self.assertIn("price rejects", " ".join(price_fail.false_positive_patterns))
        self.assertIn("revenue forecast cut", " ".join(security.stage4c_thesis_break_signals))
        self.assertIn("policy basket", " ".join(policy.stage4b_graduation_overheat_signals))
        self.assertIn("OHLC backfill row", " ".join(ohlc.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round308_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND308_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round308_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_headline_control_premium_cb_meme_security_or_safety_as_green", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r13_loop15_redteam_samsung_sds_kkr_cb"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r13_loop15_redteam_jeju_air_safety_4c"].green_guardrails)

        summary = round308_summary()
        self.assertEqual(summary["round_id"], "round_236")
        self.assertEqual(summary["large_sector"], ROUND308_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 10)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 2)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertTrue(summary["row_separation_required"])
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_missed_structural_4b_4c_and_meme(self) -> None:
        by_id = {case.case_id: case for case in ROUND308_CASE_CANDIDATES}
        samyang = by_id["r13_loop15_redteam_samyang_buldak_missed_structural"]
        rotem = by_id["r13_loop15_redteam_hyundai_rotem_k2_delivery"]
        sds = by_id["r13_loop15_redteam_samsung_sds_kkr_cb"]
        zinc = by_id["r13_loop15_redteam_korea_zinc_control_battle"]
        lgcns = by_id["r13_loop15_redteam_lg_cns_evidence_price_fail"]
        security = by_id["r13_loop15_redteam_platform_security_4c"]
        jeju = by_id["r13_loop15_redteam_jeju_air_safety_4c"]
        chicken = by_id["r13_loop15_redteam_jensen_chicken_meme"]

        self.assertEqual(samyang.primary_archetype, E2RArchetype.EARLY_EVIDENCE_MISSED_STRUCTURAL)
        self.assertEqual(samyang.extra_price_metrics["op_estimate_yoy_pct"], 84)
        self.assertEqual(samyang.stage1_price_anchor, 647000)
        self.assertEqual(samyang.score_price_alignment, "missed_due_to_score")

        self.assertEqual(rotem.extra_price_metrics["market_relative_return_pp"], 9.6)
        self.assertEqual(rotem.extra_price_metrics["k2_shipments_to_poland_count"], 18)

        self.assertEqual(sds.extra_price_metrics["convertible_bond_value_usd_mn"], 820)
        self.assertEqual(sds.event_mfe_pct, 20.8)
        self.assertIn("CB_dilution", sds.red_flag_fields)

        self.assertEqual(zinc.extra_price_metrics["tender_offer_price_krw"], 660000)
        self.assertEqual(zinc.event_mae_pct, -8.0)

        self.assertEqual(lgcns.score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(lgcns.extra_price_metrics["cloud_ai_sales_share_3q2024_pct"], 54)

        self.assertTrue(security.hard_4c_confirmed)
        self.assertEqual(security.extra_price_metrics["skt_event_return_pct"], -5.6)
        self.assertEqual(security.extra_price_metrics["coupang_affected_accounts_mn"], 33.7)

        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179)
        self.assertEqual(jeju.event_mae_pct, -15.7)

        self.assertEqual(chicken.score_price_alignment, "price_moved_without_evidence")
        self.assertFalse(chicken.extra_price_metrics["direct_revenue_link_confirmed"])
        self.assertFalse(chicken.extra_price_metrics["kkanbu_listed"])

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round308_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round308_shadow_weight_rows()}
        rules_md = render_round308_stage_rules_markdown()
        trigger_md = render_round308_trigger_grid_markdown()
        stage_md = render_round308_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND308_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r13_samyang_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r13_sds_T1"]["promote_to"], "Stage2-Actionable+4B")
        self.assertEqual(trigger_rows["r13_security_T1"]["promote_to"], "4C")
        self.assertEqual(len(ROUND308_SHADOW_WEIGHT_ROWS), 10)
        self.assertEqual(shadow_rows["EARLY_EVIDENCE_MISSED_STRUCTURAL"]["evidence_to_earnings_bridge"], "+5")
        self.assertEqual(shadow_rows["STRATEGIC_CAPITAL_WITH_DILUTION_4B"]["cb_capital_without_backlog_penalty"], "-5")
        self.assertEqual(shadow_rows["PRICE_MOVED_WITHOUT_EVIDENCE"]["celebrity_meme_event_penalty"], "-5")
        self.assertIn("OP_EPS_FCF_estimate_revision_exists", ROUND308_STAGE2_ACTIONABLE_RULES)
        self.assertIn("delivery_or_shipment_to_revenue_bridge_is_explicit", ROUND308_STAGE3_YELLOW_RULES)
        self.assertIn("actual_earnings_or_cashflow_confirms_the_bridge", ROUND308_STAGE3_GREEN_RULES)
        self.assertIn("celebrity_or_meme_event_without_direct_revenue", ROUND308_GREEN_BLOCKERS)
        self.assertIn("evidence_to_earnings_bridge", ROUND308_SCORE_UP_AXES)
        self.assertIn("control_premium_as_rerating", ROUND308_SCORE_DOWN_AXES)
        self.assertIn("control_premium_priced_as_operating_rerating", ROUND308_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("customer_data_breach_or_platform_security_failure", ROUND308_HARD_4C_GATES)
        self.assertIn("ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown", ROUND308_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r13_loop15_redteam_hyundai_rotem_k2_delivery", trigger_md)
        self.assertIn("r13_loop15_redteam_jeju_air_safety_4c", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round308_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_308.md")
        self.assertEqual(audit["round_id"], "round_236")
        self.assertEqual(audit["large_sector"], ROUND308_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_headline_control_premium_cb_meme_security_or_safety_as_green", audit["what_not_to_change"])

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
            paths = write_round308_r13_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round308_case_rows()
            self.assertEqual(len(records), len(ROUND308_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND308_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND308_TRIGGER_RECORDS))
            self.assertIn("case_library_row_describes_what_happened", paths["row_separation_plan"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
