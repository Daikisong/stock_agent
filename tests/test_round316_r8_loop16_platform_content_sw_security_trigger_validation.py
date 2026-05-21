from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round316_r8_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round316_r8_loop16_platform_content_sw_security_trigger_validation import (
    ROUND316_4C_WATCH_GATES,
    ROUND316_CASE_CANDIDATES,
    ROUND316_GREEN_BLOCKERS,
    ROUND316_LARGE_SECTOR,
    ROUND316_REQUIRED_TARGET_ALIASES,
    ROUND316_ROW_SEPARATION_RULES,
    ROUND316_SCORE_DOWN_AXES,
    ROUND316_SCORE_UP_AXES,
    ROUND316_SHADOW_WEIGHT_ROWS,
    ROUND316_STAGE2_ACTIONABLE_RULES,
    ROUND316_STAGE3_GREEN_RULES,
    ROUND316_STAGE3_YELLOW_RULES,
    ROUND316_STAGE4B_WATCH_TRIGGERS,
    ROUND316_TRIGGER_RECORDS,
    render_round316_stage4b_4c_review_markdown,
    render_round316_stage_rules_markdown,
    render_round316_trigger_grid_markdown,
    round316_audit_payload,
    round316_case_records,
    round316_case_rows,
    round316_shadow_weight_rows,
    round316_summary,
    round316_trigger_rows,
    write_round316_r8_loop16_reports,
)


class Round316R8Loop16PlatformContentSecurityTests(unittest.TestCase):
    def test_round316_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND316_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND316_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND316_REQUIRED_TARGET_ALIASES["AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE"],
            E2RArchetype.AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND316_REQUIRED_TARGET_ALIASES["WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE"],
            E2RArchetype.WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND316_REQUIRED_TARGET_ALIASES["PLATFORM_FOUNDER_REGULATORY_4C_RELIEF"],
            E2RArchetype.PLATFORM_FOUNDER_REGULATORY_4C_RELIEF.value,
        )
        self.assertEqual(
            ROUND316_REQUIRED_TARGET_ALIASES["CYBERSECURITY_DATA_BREACH_HARD_4C"],
            E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C.value,
        )

    def test_archetype_definitions_capture_round316_platform_rules(self) -> None:
        ai_dc = archetype_definition(E2RArchetype.AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE)
        ai_ipo = archetype_definition(E2RArchetype.AI_CLOUD_IPO_PRICE_MUTED)
        webtoon = archetype_definition(E2RArchetype.WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE)
        game_global = archetype_definition(E2RArchetype.GAME_IP_GLOBAL_EXPANSION_STAGE2)
        game_ipo = archetype_definition(E2RArchetype.GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B)
        label = archetype_definition(E2RArchetype.CONTENT_LABEL_GOVERNANCE_4C_WATCH)
        founder = archetype_definition(E2RArchetype.PLATFORM_FOUNDER_REGULATORY_4C_RELIEF)
        cyber = archetype_definition(E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C)

        self.assertIn("cloud/SI contract backlog", " ".join(ai_dc.stage3_high_conviction_signals))
        self.assertIn("trades below issue price", " ".join(ai_ipo.stage4c_thesis_break_signals))
        self.assertIn("ARPU", " ".join(webtoon.stage3_high_conviction_signals))
        self.assertIn("fund ROI", " ".join(game_global.stage3_high_conviction_signals))
        self.assertIn("single-title premium", " ".join(game_ipo.stage4b_graduation_overheat_signals))
        self.assertIn("label control dispute", " ".join(label.stage4c_thesis_break_signals))
        self.assertIn("founder arrest", " ".join(founder.stage4c_thesis_break_signals))
        self.assertIn("revenue forecast cut", " ".join(cyber.stage4c_thesis_break_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round316_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND316_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round316_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn(
                "do_not_treat_AI_infra_IPO_MAU_game_hit_artist_IP_founder_relief_or_security_headline_as_Green_without_recurring_revenue_ARPU_profit_repeat_sales_governance_clearance_or_trust_recovery",
                record.green_guardrails,
            )

        summary = round316_summary()
        self.assertEqual(summary["round_id"], "round_244")
        self.assertEqual(summary["large_sector"], ROUND316_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 11)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 2)
        self.assertEqual(summary["stage2_candidate_count"], 5)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 1)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["evidence_good_but_price_failed_or_muted_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_ai_webtoon_game_governance_and_cybersecurity(self) -> None:
        by_id = {case.case_id: case for case in ROUND316_CASE_CANDIDATES}
        ai_dc = by_id["r8_loop16_kakao_lgcns_sk_aws_ai_datacenter"]
        lg_cns = by_id["r8_loop16_lg_cns_ipo_ai_cloud_price_muted"]
        webtoon = by_id["r8_loop16_webtoon_naver_ip_monetization"]
        krafton = by_id["r8_loop16_krafton_naver_mirae_india_fund"]
        shiftup = by_id["r8_loop16_shiftup_game_ip_ipo"]
        hybe = by_id["r8_loop16_hybe_content_label_governance"]
        kakao = by_id["r8_loop16_kakao_founder_regulatory_relief"]
        skt = by_id["r8_loop16_sk_telecom_cyber_breach"]

        self.assertEqual(ai_dc.extra_price_metrics["investment_krw_trn"], 7.0)
        self.assertEqual(ai_dc.extra_price_metrics["kakao_event_return_pct"], 11)
        self.assertIn("cloud_contract_backlog_missing", ai_dc.red_flag_fields)

        self.assertEqual(lg_cns.extra_price_metrics["issue_price_krw"], 61900)
        self.assertEqual(lg_cns.extra_price_metrics["debut_later_price_krw"], 59700)
        self.assertEqual(lg_cns.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(webtoon.extra_price_metrics["monthly_active_users_mn"], 170)
        self.assertEqual(webtoon.extra_price_metrics["disney_earnings_event_return_pct"], 62)
        self.assertEqual(webtoon.stage_failure_type, "yellow_success")

        self.assertEqual(krafton.extra_price_metrics["fund_total_usd_mn"], 666)
        self.assertEqual(krafton.extra_price_metrics["bgmi_downloads_mn"], ">240")

        self.assertEqual(shiftup.extra_price_metrics["op_2023_krw_bn"], 111)
        self.assertIn("title_concentration_4B", shiftup.red_flag_fields)

        self.assertEqual(hybe.extra_price_metrics["bang_warrant_event_return_pct"], -2.4)
        self.assertIn("content_IP_governance_4C_watch", hybe.red_flag_fields)

        self.assertEqual(kakao.extra_price_metrics["arrest_event_return_pct"], -3.4)
        self.assertEqual(kakao.rerating_result, "credit_relief_rally")

        self.assertTrue(skt.hard_4c_confirmed)
        self.assertEqual(skt.extra_price_metrics["fine_krw_bn"], 134)
        self.assertEqual(skt.extra_price_metrics["revenue_forecast_cut_krw_bn"], 800)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round316_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round316_shadow_weight_rows()}
        rules_md = render_round316_stage_rules_markdown()
        trigger_md = render_round316_trigger_grid_markdown()
        stage_md = render_round316_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND316_TRIGGER_RECORDS), 11)
        self.assertEqual(trigger_rows["r8l16_kakao_lgcns_ai_dc_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r8l16_webtoon_disney_T2"]["promote_to"], "Stage2-Actionable_to_Yellow_candidate")
        self.assertEqual(trigger_rows["r8l16_skt_breach_T0"]["promote_to"], "4C")
        self.assertEqual(len(ROUND316_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE"]["AI_compute_to_cloud_revenue"], "+5")
        self.assertEqual(shadow_rows["WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE"]["content_IP_license_revenue"], "+5")
        self.assertEqual(shadow_rows["CYBERSECURITY_DATA_BREACH_HARD_4C"]["cybersecurity_trust_cost"], "+5")
        self.assertIn("event_return_at_least_5pct_or_market_relative_return_at_least_5pp", ROUND316_STAGE2_ACTIONABLE_RULES)
        self.assertIn("one_of_monetization_margin_retention_legal_or_security_gate_remains_open", ROUND316_STAGE3_YELLOW_RULES)
        self.assertIn("cybersecurity_remediation_is_complete_and_revenue_guidance_recovers", ROUND316_STAGE3_GREEN_RULES)
        self.assertIn("MAU_without_ARPU_profit", ROUND316_GREEN_BLOCKERS)
        self.assertIn("content_IP_license_revenue", ROUND316_SCORE_UP_AXES)
        self.assertIn("security_incident_treated_as_one_off", ROUND316_SCORE_DOWN_AXES)
        self.assertIn("content_platform_rallies_on_IP_deal_after_large_drawdown", ROUND316_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("large_scale_customer_data_breach", ROUND316_4C_WATCH_GATES)
        self.assertIn("trigger_calibration_row_stores_event_anchor_AI_infra_IPO_MAU_IP_deal_game_governance_or_cybersecurity_metrics", ROUND316_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r8_loop16_webtoon_naver_ip_monetization", trigger_md)
        self.assertIn("r8_loop16_sk_telecom_cyber_breach", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round316_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_316.md")
        self.assertEqual(audit["round_id"], "round_244")
        self.assertEqual(audit["large_sector"], ROUND316_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_change_production_scoring", audit["what_not_to_change"])

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
            paths = write_round316_r8_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round316_case_rows()
            self.assertEqual(len(records), len(ROUND316_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND316_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND316_TRIGGER_RECORDS))
            self.assertIn("Webtoon", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r8l16_skt_breach_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("CYBERSECURITY_DATA_BREACH_HARD_4C", paths["weight_profiles"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
