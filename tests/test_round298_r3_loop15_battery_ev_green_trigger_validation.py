from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round298_r3_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round298_r3_loop15_battery_ev_green_trigger_validation import (
    ROUND298_CASE_CANDIDATES,
    ROUND298_GREEN_BLOCKERS,
    ROUND298_HARD_4C_GATES,
    ROUND298_LARGE_SECTOR,
    ROUND298_REQUIRED_TARGET_ALIASES,
    ROUND298_SCORE_DOWN_AXES,
    ROUND298_SCORE_UP_AXES,
    ROUND298_SHADOW_WEIGHT_ROWS,
    ROUND298_STAGE2_ACTIONABLE_RULES,
    ROUND298_STAGE3_GREEN_RULES,
    ROUND298_STAGE3_YELLOW_RULES,
    ROUND298_STAGE4B_WATCH_TRIGGERS,
    ROUND298_TRIGGER_RECORDS,
    render_round298_stage_rules_markdown,
    render_round298_stage4b_4c_review_markdown,
    render_round298_trigger_grid_markdown,
    round298_audit_payload,
    round298_case_records,
    round298_case_rows,
    round298_shadow_weight_rows,
    round298_summary,
    round298_trigger_rows,
    write_round298_r3_loop15_reports,
)


class Round298R3Loop15BatteryEVGreenTriggerValidationTests(unittest.TestCase):
    def test_round298_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND298_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND298_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND298_REQUIRED_TARGET_ALIASES["BATTERY_AMPC_PROFIT_STAGE2_YELLOW"],
            E2RArchetype.BATTERY_AMPC_PROFIT_STAGE2_YELLOW.value,
        )
        self.assertEqual(
            ROUND298_REQUIRED_TARGET_ALIASES["BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE"],
            E2RArchetype.BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE.value,
        )

    def test_archetype_definitions_capture_r3_loop15_rules(self) -> None:
        ampc = archetype_definition(E2RArchetype.BATTERY_AMPC_PROFIT_STAGE2_YELLOW)
        ess = archetype_definition(E2RArchetype.ESS_LFP_PIVOT_STAGE2_ACTIONABLE)
        cancellation = archetype_definition(E2RArchetype.EV_DEMAND_CONTRACT_CANCELLATION_4C)
        cathode = archetype_definition(E2RArchetype.SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C)
        lithium = archetype_definition(E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM)
        upstream = archetype_definition(E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2)
        feoc = archetype_definition(E2RArchetype.FEOC_CATHODE_OWNERSHIP_STAGE2)
        safety = archetype_definition(E2RArchetype.BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE)

        self.assertIn("only Yellow until ex-AMPC margin, utilization, customer call-off, and FCF are confirmed", ampc.stage3_high_conviction_signals)
        self.assertIn("contract value, customer/application, delivery schedule, and EV-to-ESS line conversion are visible", ess.stage2_candidate_signals)
        self.assertIn("battery JV dissolution", cancellation.stage4c_thesis_break_signals)
        self.assertIn("contract value collapse", cathode.stage4c_thesis_break_signals)
        self.assertIn("temporary lithium supply shock treated as structural E2R", lithium.false_positive_patterns)
        self.assertIn("resource stake treated as FCF without cost advantage", upstream.false_positive_patterns)
        self.assertIn("ownership derisking treated as cash flow", feoc.false_positive_patterns)
        self.assertIn("misleading supplier disclosure", safety.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round298_case_records()
        hard_cases = {case.case_id for case in ROUND298_CASE_CANDIDATES if case.hard_4c_confirmed}
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND298_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round298_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("battery_safety_and_contract_cancellation_are_hard_gates", record.green_guardrails)
            if record.case_id not in hard_cases:
                self.assertIn("hard_4c_confirmed_false", record.green_guardrails)

        summary = round298_summary()
        self.assertEqual(summary["round_id"], "round_226")
        self.assertEqual(summary["large_sector"], ROUND298_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 2)
        self.assertEqual(summary["stage3_green_candidate_count"], 0)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_keep_contract_quality_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND298_CASE_CANDIDATES}
        lges = by_id["r3_loop15_lges_ampc_profit_dealrisk"]
        sdi = by_id["r3_loop15_samsung_sdi_ess_lfp_pivot"]
        skon = by_id["r3_loop15_sk_on_ford_jv_termination"]
        lnf = by_id["r3_loop15_lnf_tesla_cathode_contract_collapse"]
        lithium = by_id["r3_loop15_catl_mine_lithium_price_event"]
        posco = by_id["r3_loop15_posco_minres_lithium_supply_security"]
        lgchem = by_id["r3_loop15_lg_chem_toyota_tsusho_cathode_feoc"]
        safety = by_id["r3_loop15_aricell_sconnect_battery_safety_hard_4c"]

        self.assertEqual(lges.primary_archetype, E2RArchetype.BATTERY_AMPC_PROFIT_STAGE2_YELLOW)
        self.assertEqual(lges.extra_price_metrics["op_ex_ampc_krw_bn"], 1.4)
        self.assertEqual(lges.extra_price_metrics["total_lost_expected_revenue_krw_trn"], 13.5)
        self.assertEqual(lges.stage_candidate, "Stage3-Yellow_candidate")

        self.assertEqual(sdi.primary_archetype, E2RArchetype.ESS_LFP_PIVOT_STAGE2_ACTIONABLE)
        self.assertEqual(sdi.extra_price_metrics["ess_contract_value_krw_trn"], 2.0)
        self.assertEqual(sdi.extra_price_metrics["market_relative_return_pp"], 6.2)

        self.assertEqual(skon.primary_archetype, E2RArchetype.EV_DEMAND_CONTRACT_CANCELLATION_4C)
        self.assertEqual(skon.extra_price_metrics["georgia_layoffs_workers"], 958)
        self.assertFalse(skon.hard_4c_confirmed)

        self.assertEqual(lnf.primary_archetype, E2RArchetype.SIGNED_CATHODE_CONTRACT_COLLAPSE_HARD_4C)
        self.assertEqual(lnf.extra_price_metrics["contract_value_collapse_pct"], -99.9997)
        self.assertTrue(lnf.hard_4c_confirmed)

        self.assertEqual(lithium.primary_archetype, E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM)
        self.assertEqual(lithium.extra_price_metrics["lnf_event_mfe_pct"], 10.0)
        self.assertEqual(lithium.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(posco.primary_archetype, E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2)
        self.assertEqual(posco.extra_price_metrics["minres_deal_value_usd_mn"], 765)
        self.assertEqual(lgchem.primary_archetype, E2RArchetype.FEOC_CATHODE_OWNERSHIP_STAGE2)
        self.assertEqual(lgchem.extra_price_metrics["huayou_stake_after_pct"], 24)
        self.assertEqual(safety.primary_archetype, E2RArchetype.BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE)
        self.assertEqual(safety.extra_price_metrics["fatalities"], 23)
        self.assertTrue(safety.hard_4c_confirmed)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round298_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round298_shadow_weight_rows()}
        rules_md = render_round298_stage_rules_markdown()
        trigger_md = render_round298_trigger_grid_markdown()
        stage_md = render_round298_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND298_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r3l15_lges_T1"]["promote_to"], "Stage3-Yellow")
        self.assertEqual(trigger_rows["r3l15_sdi_T2"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r3l15_lnf_T2"]["promote_to"], "4C")
        self.assertEqual(len(ROUND298_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["BATTERY_AMPC_PROFIT_STAGE2_YELLOW"]["ex_subsidy_operating_margin"], "+5")
        self.assertEqual(shadow_rows["ESS_LFP_PIVOT_STAGE2_ACTIONABLE"]["line_conversion_execution"], "+5")
        self.assertEqual(shadow_rows["BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE"]["battery_safety_disclosure_trust"], "+5")
        self.assertIn("contract_value_and_delivery_schedule_are_visible", ROUND298_STAGE2_ACTIONABLE_RULES)
        self.assertIn("delivery_calloff_subsidy_or_utilization_gate_still_pending", ROUND298_STAGE3_YELLOW_RULES)
        self.assertIn("actual_customer_calloff_or_shipment_converts_to_revenue", ROUND298_STAGE3_GREEN_RULES)
        self.assertIn("signed_contract_amount_without_actual_calloff", ROUND298_GREEN_BLOCKERS)
        self.assertIn("actual_customer_calloff", ROUND298_SCORE_UP_AXES)
        self.assertIn("signed_contract_amount_only", ROUND298_SCORE_DOWN_AXES)
        self.assertIn("lithium_event_rally_without_durable_price_or_margin", ROUND298_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("signed_contract_value_collapse", ROUND298_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("Samsung SDI", trigger_md)
        self.assertIn("Stage3-Green 확정이 없다", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round298_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_298.md")
        self.assertEqual(audit["round_id"], "round_226")
        self.assertEqual(audit["large_sector"], ROUND298_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_signed_contract_amount_as_actual_calloff", audit["what_not_to_change"])

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
            paths = write_round298_r3_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round298_case_rows()
            self.assertEqual(len(records), len(ROUND298_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND298_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND298_TRIGGER_RECORDS))
            self.assertIn("LGES AMPC", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r3l15_sdi_T2", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("ESS_LFP_PIVOT_STAGE2_ACTIONABLE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("BATTERY_SAFETY_TRUST_HARD_4C_REFERENCE", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["op_ex_ampc_krw_bn"], 1.4)


if __name__ == "__main__":
    unittest.main()
