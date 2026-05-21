from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round303_r8_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round303_r8_loop15_platform_content_sw_security_trigger_validation import (
    ROUND303_CASE_CANDIDATES,
    ROUND303_GREEN_BLOCKERS,
    ROUND303_HARD_4C_GATES,
    ROUND303_LARGE_SECTOR,
    ROUND303_REQUIRED_TARGET_ALIASES,
    ROUND303_SCORE_DOWN_AXES,
    ROUND303_SCORE_UP_AXES,
    ROUND303_SHADOW_WEIGHT_ROWS,
    ROUND303_STAGE2_ACTIONABLE_RULES,
    ROUND303_STAGE3_GREEN_RULES,
    ROUND303_STAGE3_YELLOW_RULES,
    ROUND303_STAGE4B_WATCH_TRIGGERS,
    ROUND303_TRIGGER_RECORDS,
    render_round303_stage_rules_markdown,
    render_round303_stage4b_4c_review_markdown,
    render_round303_trigger_grid_markdown,
    round303_audit_payload,
    round303_case_records,
    round303_case_rows,
    round303_shadow_weight_rows,
    round303_summary,
    round303_trigger_rows,
    write_round303_r8_loop15_reports,
)


class Round303R8Loop15PlatformContentSWSecurityTriggerValidationTests(unittest.TestCase):
    def test_round303_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND303_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND303_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND303_REQUIRED_TARGET_ALIASES["AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE"],
            E2RArchetype.AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE.value,
        )
        self.assertEqual(
            ROUND303_REQUIRED_TARGET_ALIASES["AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B"],
            E2RArchetype.AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B.value,
        )
        self.assertEqual(
            ROUND303_REQUIRED_TARGET_ALIASES["CYBERSECURITY_DATA_BREACH_HARD_4C"],
            E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C.value,
        )

    def test_archetype_definitions_capture_r8_loop15_rules(self) -> None:
        ai_msg = archetype_definition(E2RArchetype.AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE)
        webtoon = archetype_definition(E2RArchetype.WEBTOON_IPO_CONTENT_PLATFORM_STAGE2)
        cloud = archetype_definition(E2RArchetype.CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED)
        cb = archetype_definition(E2RArchetype.AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B)
        game = archetype_definition(E2RArchetype.GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE)
        kpop = archetype_definition(E2RArchetype.KPOP_ARTIST_GOVERNANCE_4C_WATCH)
        cyber = archetype_definition(E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C)
        content_ma = archetype_definition(E2RArchetype.CONTENT_MA_IP_EXPANSION_STAGE2)

        self.assertIn("paid AI usage", " ".join(ai_msg.stage3_high_conviction_signals))
        self.assertIn("parent value capture", " ".join(webtoon.stage3_high_conviction_signals))
        self.assertIn("weak IPO debut", " ".join(cloud.stage4c_thesis_break_signals))
        self.assertIn("dilution absorption", " ".join(cb.stage3_high_conviction_signals))
        self.assertIn("live-service retention", " ".join(game.stage3_high_conviction_signals))
        self.assertIn("court injunction", " ".join(kpop.stage4c_thesis_break_signals))
        self.assertIn("revenue forecast cut", " ".join(cyber.stage4c_thesis_break_signals))
        self.assertIn("new IP revenue", " ".join(content_ma.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round303_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND303_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round303_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_ai_partnership_ipo_cb_ip_or_security_capex_headline_as_green", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r8_loop15_kakao_openai_ai_messaging"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r8_loop15_skt_data_breach_security_4c"].green_guardrails)

        summary = round303_summary()
        self.assertEqual(summary["round_id"], "round_231")
        self.assertEqual(summary["large_sector"], ROUND303_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 10)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 5)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_headline_monetization_and_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND303_CASE_CANDIDATES}
        kakao = by_id["r8_loop15_kakao_openai_ai_messaging"]
        naver = by_id["r8_loop15_naver_webtoon_nvidia_ai_infra"]
        lgcns = by_id["r8_loop15_lg_cns_cloud_ai_ipo"]
        sds = by_id["r8_loop15_samsung_sds_kkr_cb_ai"]
        krafton = by_id["r8_loop15_krafton_adk_india_ip_expansion"]
        shiftup = by_id["r8_loop15_shiftup_ipo_stellarblade_nikke"]
        hybe = by_id["r8_loop15_hybe_newjeans_sm_tencent_kpop_governance"]
        skt = by_id["r8_loop15_skt_data_breach_security_4c"]

        self.assertEqual(kakao.primary_archetype, E2RArchetype.AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE)
        self.assertEqual(kakao.event_mfe_pct, 9.0)
        self.assertEqual(kakao.event_mae_pct, -2.0)
        self.assertIn("paid_AI_usage_missing", kakao.red_flag_fields)

        self.assertEqual(naver.extra_price_metrics["webtoon_maus_mn"], 170)
        self.assertEqual(naver.extra_price_metrics["naver_blackwell_chip_purchase_units"], 60000)

        self.assertEqual(lgcns.score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(lgcns.extra_price_metrics["debut_return_vs_issue_pct"], -3.55)

        self.assertEqual(sds.primary_archetype, E2RArchetype.AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B)
        self.assertEqual(sds.extra_price_metrics["convertible_bond_value_usd_mn"], 820)
        self.assertIn("CB_dilution_absorption_missing", sds.red_flag_fields)

        self.assertEqual(krafton.primary_archetype, E2RArchetype.CONTENT_MA_IP_EXPANSION_STAGE2)
        self.assertEqual(krafton.extra_price_metrics["bgmi_downloads_mn"], 240)

        self.assertEqual(shiftup.primary_archetype, E2RArchetype.GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE)
        self.assertEqual(shiftup.extra_price_metrics["nikke_sales_krw_bn"], 255)

        self.assertEqual(hybe.primary_archetype, E2RArchetype.KPOP_ARTIST_GOVERNANCE_4C_WATCH)
        self.assertEqual(hybe.stage_failure_type, "should_have_been_red")

        self.assertEqual(skt.primary_archetype, E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C)
        self.assertTrue(skt.hard_4c_confirmed)
        self.assertEqual(skt.extra_price_metrics["revenue_forecast_cut_2025_krw_bn"], 800)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round303_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round303_shadow_weight_rows()}
        rules_md = render_round303_stage_rules_markdown()
        trigger_md = render_round303_trigger_grid_markdown()
        stage_md = render_round303_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND303_TRIGGER_RECORDS), 10)
        self.assertEqual(trigger_rows["r8l15_kakao_openai_T1"]["promote_to"], "Stage2-Actionable_only")
        self.assertEqual(trigger_rows["r8l15_samsungsds_kkr_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r8l15_skt_breach_T0"]["promote_to"], "4C")
        self.assertEqual(len(ROUND303_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE"]["paid_ai_usage_conversion"], "+5")
        self.assertEqual(shadow_rows["AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B"]["cb_capital_without_backlog_penalty"], "-4")
        self.assertEqual(shadow_rows["CYBERSECURITY_DATA_BREACH_HARD_4C"]["platform_user_data_security"], "+5")
        self.assertIn("event_day_market_relative_price_reaction_exceeds_5pp", ROUND303_STAGE2_ACTIONABLE_RULES)
        self.assertIn("enterprise_order_backlog_or_cloud_margin_visible_but_durability_pending", ROUND303_STAGE3_YELLOW_RULES)
        self.assertIn("paid_ai_usage_api_revenue_or_ad_uplift_is_visible", ROUND303_STAGE3_GREEN_RULES)
        self.assertIn("security_capex_after_breach_as_positive", ROUND303_GREEN_BLOCKERS)
        self.assertIn("paid_AI_usage_conversion", ROUND303_SCORE_UP_AXES)
        self.assertIn("AI_partnership_headline_only", ROUND303_SCORE_DOWN_AXES)
        self.assertIn("cb_or_strategic_capital_price_pop_before_order_backlog", ROUND303_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("data_breach_or_customer_data_leak", ROUND303_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r8_loop15_samsung_sds_kkr_cb_ai", trigger_md)
        self.assertIn("SK Telecom data breach", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round303_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_303.md")
        self.assertEqual(audit["round_id"], "round_231")
        self.assertEqual(audit["large_sector"], ROUND303_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_ai_partnership_ipo_cb_ip_or_security_capex_headline_as_green", audit["what_not_to_change"])

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
            paths = write_round303_r8_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round303_case_rows()
            self.assertEqual(len(records), len(ROUND303_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND303_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND303_TRIGGER_RECORDS))
            self.assertIn("Kakao/OpenAI", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage3-Green", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r8l15_skt_breach_T1", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("CYBERSECURITY_DATA_BREACH_HARD_4C", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["kakaotalk_domestic_share_pct"], 97)


if __name__ == "__main__":
    unittest.main()
