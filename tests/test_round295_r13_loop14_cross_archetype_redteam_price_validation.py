from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round295_r13_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round295_r13_loop14_cross_archetype_redteam_price_validation import (
    ROUND295_CASE_CANDIDATES,
    ROUND295_GREEN_FORBIDDEN_PATTERNS,
    ROUND295_GREEN_REQUIRED_FIELDS,
    ROUND295_HARD_4C_GATES,
    ROUND295_LARGE_SECTOR,
    ROUND295_REQUIRED_TARGET_ALIASES,
    ROUND295_SHADOW_WEIGHT_ROWS,
    ROUND295_STAGE4B_WATCH_TRIGGERS,
    render_round295_green_gate_review_markdown,
    render_round295_stage4b_4c_review_markdown,
    round295_audit_payload,
    round295_case_records,
    round295_case_rows,
    round295_deep_sub_archetype_rows,
    round295_shadow_weight_rows,
    round295_summary,
    write_round295_r13_loop14_reports,
)


class Round295R13Loop14CrossArchetypeRedTeamTests(unittest.TestCase):
    def test_round295_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND295_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND295_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND295_REQUIRED_TARGET_ALIASES["SIGNED_CONTRACT_COLLAPSE_HARD_4C"],
            E2RArchetype.SIGNED_CONTRACT_COLLAPSE_HARD_4C.value,
        )
        self.assertEqual(
            ROUND295_REQUIRED_TARGET_ALIASES["DATA_TRUST_HARD_4C"],
            E2RArchetype.DATA_TRUST_HARD_4C.value,
        )

    def test_archetype_definitions_capture_cross_arch_redteam_gates(self) -> None:
        defense = archetype_definition(E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B)
        contract = archetype_definition(E2RArchetype.SIGNED_CONTRACT_COLLAPSE_HARD_4C)
        resource = archetype_definition(E2RArchetype.RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE)
        ipo = archetype_definition(E2RArchetype.AI_CLOUD_IPO_FALSE_POSITIVE)
        valueup = archetype_definition(E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE)
        trust = archetype_definition(E2RArchetype.DATA_TRUST_HARD_4C)
        capex = archetype_definition(E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE)
        control = archetype_definition(E2RArchetype.CONTROL_PREMIUM_4B_GOVERNANCE_WATCH)

        self.assertIn("capital raising filing revision", defense.stage4c_thesis_break_signals)
        self.assertIn("contract value collapse", contract.stage4c_thesis_break_signals)
        self.assertIn("resource estimate without drilling", resource.false_positive_patterns)
        self.assertIn("IPO oversubscription treated as aftermarket validation", ipo.false_positive_patterns)
        self.assertIn("activist proposal fails", valueup.stage4c_thesis_break_signals)
        self.assertIn("data breach", trust.stage4c_thesis_break_signals)
        self.assertIn("funding plan unclear", capex.stage4c_thesis_break_signals)
        self.assertIn("tender control premium", control.stage4b_graduation_overheat_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round295_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND295_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("do_not_use_round295_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_lower_stage3_green_thresholds", record.green_guardrails)

        summary = round295_summary()
        self.assertEqual(summary["round_id"], "round_223")
        self.assertEqual(summary["large_sector"], ROUND295_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 0)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["watch_counterexample_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["stage4c_watch_count"], 5)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["false_positive_score_count"], 5)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_round295_cases_keep_headlines_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND295_CASE_CANDIDATES}
        hanwha = by_id["r13_loop14_hanwha_aerospace_backlog_dilution_4b"]
        lnf = by_id["r13_loop14_lnf_tesla_signed_contract_collapse_hard_4c"]
        kogas = by_id["r13_loop14_kogas_blue_whale_resource_event_premium"]
        lgcns = by_id["r13_loop14_lg_cns_ai_cloud_ipo_false_positive"]
        samsung = by_id["r13_loop14_samsung_ct_valueup_proposal_failure"]
        skt = by_id["r13_loop14_skt_data_trust_hard_4c"]
        hyundai = by_id["r13_loop14_hyundai_steel_us_localization_capex_false_positive"]
        zinc = by_id["r13_loop14_korea_zinc_control_premium_4b"]

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B)
        self.assertEqual(hanwha.extra_price_metrics["share_sale_krw_trn"], 3.6)
        self.assertEqual(hanwha.extra_price_metrics["event_mae_pct"], -13)
        self.assertTrue(hanwha.extra_price_metrics["fss_revision_order"])

        self.assertEqual(lnf.primary_archetype, E2RArchetype.SIGNED_CONTRACT_COLLAPSE_HARD_4C)
        self.assertEqual(lnf.extra_price_metrics["initial_contract_value_usd_bn"], 2.9)
        self.assertEqual(lnf.extra_price_metrics["revised_contract_value_usd"], 7386)
        self.assertTrue(lnf.hard_4c_confirmed)

        self.assertEqual(kogas.primary_archetype, E2RArchetype.RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE)
        self.assertEqual(kogas.extra_price_metrics["korea_gas_event_mfe_pct"], 30)
        self.assertFalse(kogas.extra_price_metrics["economic_viability_confirmed"])
        self.assertEqual(kogas.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(lgcns.primary_archetype, E2RArchetype.AI_CLOUD_IPO_FALSE_POSITIVE)
        self.assertEqual(lgcns.extra_price_metrics["ipo_price_krw"], 61900)
        self.assertEqual(lgcns.extra_price_metrics["morning_trading_price_krw"], 59700)
        self.assertFalse(lgcns.extra_price_metrics["aftermarket_demand_confirmed"])

        self.assertEqual(samsung.primary_archetype, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE)
        self.assertFalse(samsung.extra_price_metrics["proposal_passed"])
        self.assertEqual(samsung.extra_price_metrics["nps_vote"], "sided_with_management")

        self.assertEqual(skt.primary_archetype, E2RArchetype.DATA_TRUST_HARD_4C)
        self.assertEqual(skt.extra_price_metrics["revenue_forecast_cut_krw_bn"], 800)
        self.assertEqual(skt.extra_price_metrics["consumer_agency_possible_total_compensation_krw_trn"], 2.3)
        self.assertTrue(skt.hard_4c_confirmed)

        self.assertEqual(hyundai.primary_archetype, E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE)
        self.assertEqual(hyundai.extra_price_metrics["hyundai_steel_stock_decline_since_announcement_pct"], -21.2)
        self.assertFalse(hyundai.extra_price_metrics["full_funding_plan_disclosed"])

        self.assertEqual(zinc.primary_archetype, E2RArchetype.CONTROL_PREMIUM_4B_GOVERNANCE_WATCH)
        self.assertEqual(zinc.extra_price_metrics["korea_zinc_event_mfe_pct"], 19.8)
        self.assertFalse(zinc.extra_price_metrics["operating_cashflow_improvement_confirmed"])

    def test_green_gate_stage_review_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND295_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND295_GREEN_FORBIDDEN_PATTERNS)
        shadow_rows = {row["archetype"]: row for row in round295_shadow_weight_rows()}
        deep_rows = round295_deep_sub_archetype_rows()
        green_markdown = render_round295_green_gate_review_markdown()
        stage_markdown = render_round295_stage4b_4c_review_markdown()

        self.assertIn("actual_calloff_vs_signed_contract", required)
        self.assertIn("dilution_adjusted_EPS", required)
        self.assertIn("resource_economic_viability", required)
        self.assertIn("large_customer_name_only", forbidden)
        self.assertIn("data_breach_treated_as_oneoff", forbidden)
        self.assertIn("IPO_oversubscription_high_but_debut_below_IPO", ROUND295_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("signed_contract_value_collapse", ROUND295_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("hard 4C", stage_markdown)
        self.assertEqual(len(ROUND295_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["SIGNED_CONTRACT_COLLAPSE_HARD_4C"]["actual_calloff_vs_signed_contract"], "+5")
        self.assertEqual(shadow_rows["AI_CLOUD_IPO_FALSE_POSITIVE"]["aftermarket_price_validation"], "+5")
        self.assertEqual(shadow_rows["RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE"]["event_penalty"], "-5")
        self.assertTrue(any("SK Telecom" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hyundai Steel" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round295_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_295.md")
        self.assertEqual(audit["round_id"], "round_223")
        self.assertEqual(audit["large_sector"], ROUND295_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round295_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round295_r13_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round295_case_rows()
            self.assertEqual(len(records), len(ROUND295_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND295_CASE_CANDIDATES))
            self.assertIn("Hanwha Aerospace", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_calloff_vs_signed_contract", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("DATA_TRUST_HARD_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("contract_value_collapse_anchor", paths["price_validation_fields"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["contract_value_collapse_pct"], -99.9997)


if __name__ == "__main__":
    unittest.main()

