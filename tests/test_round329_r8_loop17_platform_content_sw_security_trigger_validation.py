from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round329_r8_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round329_r8_loop17_platform_content_sw_security_trigger_validation import (
    ROUND329_CASE_CANDIDATES,
    ROUND329_GREEN_BLOCKERS,
    ROUND329_HARD_4C_GATES,
    ROUND329_LARGE_SECTOR,
    ROUND329_REQUIRED_TARGET_ALIASES,
    ROUND329_ROW_SEPARATION_RULES,
    ROUND329_SCORE_DOWN_AXES,
    ROUND329_SCORE_UP_AXES,
    ROUND329_SHADOW_WEIGHT_ROWS,
    ROUND329_STAGE2_ACTIONABLE_RULES,
    ROUND329_STAGE3_GREEN_RULES,
    ROUND329_STAGE3_YELLOW_RULES,
    ROUND329_STAGE4B_WATCH_TRIGGERS,
    ROUND329_TRIGGER_RECORDS,
    render_round329_stage4b_4c_review_markdown,
    render_round329_stage_rules_markdown,
    render_round329_trigger_grid_markdown,
    round329_audit_payload,
    round329_case_records,
    round329_case_rows,
    round329_shadow_weight_rows,
    round329_summary,
    round329_trigger_rows,
    write_round329_r8_loop17_reports,
)


class Round329R8Loop17PlatformContentSecurityTests(unittest.TestCase):
    def test_round329_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND329_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND329_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND329_REQUIRED_TARGET_ALIASES["AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED"],
            E2RArchetype.AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED.value,
        )
        self.assertEqual(
            ROUND329_REQUIRED_TARGET_ALIASES["SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B"],
            E2RArchetype.SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B.value,
        )
        self.assertEqual(
            ROUND329_REQUIRED_TARGET_ALIASES["CYBER_BREACH_HARD_4C_SECURITY_CAPEX"],
            E2RArchetype.CYBER_BREACH_HARD_4C_SECURITY_CAPEX.value,
        )
        self.assertEqual(
            ROUND329_REQUIRED_TARGET_ALIASES["PLATFORM_GOVERNANCE_REGULATORY_4B"],
            E2RArchetype.PLATFORM_GOVERNANCE_REGULATORY_4B.value,
        )

    def test_archetype_definitions_capture_round329_rules(self) -> None:
        ai_chat = archetype_definition(E2RArchetype.AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED)
        sovereign = archetype_definition(E2RArchetype.SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B)
        webtoon = archetype_definition(E2RArchetype.WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT)
        gaming = archetype_definition(E2RArchetype.GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B)
        it_services = archetype_definition(E2RArchetype.IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED)
        cyber = archetype_definition(E2RArchetype.CYBER_BREACH_HARD_4C_SECURITY_CAPEX)
        kpop = archetype_definition(E2RArchetype.KPOP_LABEL_GOVERNANCE_4B)
        governance = archetype_definition(E2RArchetype.PLATFORM_GOVERNANCE_REGULATORY_4B)

        self.assertIn("MAU / ARPU", " ".join(ai_chat.stage3_high_conviction_signals))
        self.assertIn("enterprise/government contracts", " ".join(sovereign.stage3_high_conviction_signals))
        self.assertIn("holding-company discount", " ".join(webtoon.stage4b_graduation_overheat_signals))
        self.assertIn("live-service retention", " ".join(gaming.stage3_high_conviction_signals))
        self.assertIn("trades below issue price", " ".join(it_services.stage4b_graduation_overheat_signals))
        self.assertIn("revenue forecast cut", " ".join(cyber.stage4c_thesis_break_signals))
        self.assertIn("label/founder governance", " ".join(kpop.stage4b_graduation_overheat_signals))
        self.assertIn("KakaoBank control risk", " ".join(governance.stage4c_thesis_break_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round329_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND329_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round329_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", record.green_guardrails)

        summary = round329_summary()
        self.assertEqual(summary["round_id"], "round_257")
        self.assertEqual(summary["loop_name"], "R8 Loop 17")
        self.assertEqual(summary["large_sector"], ROUND329_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["trigger_count"], 12)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 1)
        self.assertEqual(summary["stage2_candidate_count"], 5)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 0)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 8)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["evidence_good_but_price_failed_or_muted_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_ai_content_game_governance_and_cyber(self) -> None:
        by_id = {case.case_id: case for case in ROUND329_CASE_CANDIDATES}
        kakao_ai = by_id["r8_loop17_kakao_openai_ai_partnership"]
        naver = by_id["r8_loop17_naver_sovereign_ai_blackwell"]
        webtoon = by_id["r8_loop17_webtoon_naver_content_platform"]
        shiftup = by_id["r8_loop17_shift_up_gaming_ip_ipo"]
        krafton = by_id["r8_loop17_krafton_subnautica_legal_4b"]
        lg_cns = by_id["r8_loop17_lg_cns_ai_cloud_ipo_price_failed"]
        skt = by_id["r8_loop17_sk_telecom_cyber_breach"]
        hybe = by_id["r8_loop17_hybe_ador_bang_governance_4b"]
        kakao_gov = by_id["r8_loop17_kakao_founder_legal_governance"]

        self.assertEqual(kakao_ai.extra_price_metrics["initial_event_return_pct"], 9)
        self.assertEqual(kakao_ai.extra_price_metrics["later_event_return_pct"], -2)
        self.assertEqual(kakao_ai.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(naver.extra_price_metrics["naver_chips"], 60000)
        self.assertIn("capex_ROI_4B", naver.red_flag_fields)

        self.assertEqual(webtoon.extra_price_metrics["disney_event_return_pct"], 62)
        self.assertEqual(webtoon.extra_price_metrics["holdco_discount_pct"], 50)

        self.assertEqual(shiftup.extra_price_metrics["nikke_revenue_krw_bn"], 255)
        self.assertIn("title_concentration_4B", shiftup.red_flag_fields)

        self.assertEqual(krafton.extra_price_metrics["earnout_usd_mn"], 250)
        self.assertIn("studio_governance_4B", krafton.red_flag_fields)

        self.assertEqual(lg_cns.extra_price_metrics["issue_price_krw"], 61900)
        self.assertEqual(lg_cns.extra_price_metrics["last_price_krw"], 59700)
        self.assertEqual(lg_cns.score_price_alignment, "evidence_good_but_price_failed")

        self.assertTrue(skt.hard_4c_confirmed)
        self.assertEqual(skt.extra_price_metrics["market_relative_pp"], -6.8)
        self.assertEqual(skt.extra_price_metrics["revenue_forecast_cut_krw_bn"], 800)

        self.assertEqual(hybe.extra_price_metrics["bang_warrant_event_return_pct"], -2.4)
        self.assertIn("ADOR_NewJeans_label_control_4B", hybe.red_flag_fields)

        self.assertEqual(kakao_gov.extra_price_metrics["arrest_event_return_pct"], -3.4)
        self.assertEqual(kakao_gov.rerating_result, "credit_relief_rally")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round329_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round329_shadow_weight_rows()}
        rules_md = render_round329_stage_rules_markdown()
        trigger_md = render_round329_trigger_grid_markdown()
        stage_md = render_round329_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND329_TRIGGER_RECORDS), 12)
        self.assertEqual(trigger_rows["r8l17_kakao_openai_T1"]["promote_to"], "Stage2_price_failed")
        self.assertEqual(trigger_rows["r8l17_webtoon_disney_T2"]["promote_to"], "Stage2-Actionable_candidate")
        self.assertEqual(trigger_rows["r8l17_skt_breach_T0"]["promote_to"], "4C")
        self.assertEqual(len(ROUND329_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED"]["AI_product_integration"], "+5")
        self.assertEqual(shadow_rows["SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B"]["cloud_AI_capex_to_contract"], "+5")
        self.assertEqual(shadow_rows["CYBER_BREACH_HARD_4C_SECURITY_CAPEX"]["cyber_trust_security"], "+5")
        self.assertIn("AI_product_or_sovereign_AI_infra_trigger_is_specific", ROUND329_STAGE2_ACTIONABLE_RULES)
        self.assertIn("monetization_or_utilization_path_exists_but_one_gate_remains_open", ROUND329_STAGE3_YELLOW_RULES)
        self.assertIn("AI_chat_partnership_converts_to_paid_usage_ARPU_and_margin", ROUND329_STAGE3_GREEN_RULES)
        self.assertIn("AI_partnership_without_monetization", ROUND329_GREEN_BLOCKERS)
        self.assertIn("governance_legal_risk", ROUND329_SCORE_UP_AXES)
        self.assertIn("security_breach_revenue_cut_penalty", ROUND329_SCORE_DOWN_AXES)
        self.assertIn("AI_cloud_IT_services_IPO_trades_below_issue_price", ROUND329_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("large_scale_customer_data_breach_with_revenue_forecast_cut", ROUND329_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND329_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r8_loop17_webtoon_naver_content_platform", trigger_md)
        self.assertIn("r8_loop17_sk_telecom_cyber_breach", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round329_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_329.md")
        self.assertEqual(audit["round_id"], "round_257")
        self.assertEqual(audit["large_sector"], ROUND329_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_change_production_scoring", audit["what_not_to_change"])
        self.assertIn("do_not_use_round329_cases_as_candidate_generation_input", audit["what_not_to_change"])

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
            paths = write_round329_r8_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round329_case_rows()
            self.assertEqual(len(records), len(ROUND329_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND329_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND329_TRIGGER_RECORDS))
            self.assertIn("Kakao", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r8l17_skt_breach_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("CYBER_BREACH_HARD_4C_SECURITY_CAPEX", paths["weight_profile"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
