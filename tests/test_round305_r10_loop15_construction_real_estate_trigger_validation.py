from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round305_r10_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round305_r10_loop15_construction_real_estate_trigger_validation import (
    ROUND305_CASE_CANDIDATES,
    ROUND305_GREEN_BLOCKERS,
    ROUND305_HARD_4C_GATES,
    ROUND305_LARGE_SECTOR,
    ROUND305_REQUIRED_TARGET_ALIASES,
    ROUND305_SCORE_DOWN_AXES,
    ROUND305_SCORE_UP_AXES,
    ROUND305_SHADOW_WEIGHT_ROWS,
    ROUND305_STAGE2_ACTIONABLE_RULES,
    ROUND305_STAGE3_GREEN_RULES,
    ROUND305_STAGE3_YELLOW_RULES,
    ROUND305_STAGE4B_WATCH_TRIGGERS,
    ROUND305_TRIGGER_RECORDS,
    render_round305_stage_rules_markdown,
    render_round305_stage4b_4c_review_markdown,
    render_round305_trigger_grid_markdown,
    round305_audit_payload,
    round305_case_records,
    round305_case_rows,
    round305_shadow_weight_rows,
    round305_summary,
    round305_trigger_rows,
    write_round305_r10_loop15_reports,
)


class Round305R10Loop15ConstructionRealEstateTriggerValidationTests(unittest.TestCase):
    def test_round305_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND305_REQUIRED_TARGET_ALIASES), 7)
        self.assertTrue(set(ROUND305_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND305_REQUIRED_TARGET_ALIASES["OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE"],
            E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND305_REQUIRED_TARGET_ALIASES["CONSTRUCTION_QUALITY_SAFETY_HARD_4C"],
            E2RArchetype.CONSTRUCTION_QUALITY_SAFETY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND305_REQUIRED_TARGET_ALIASES["BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH"],
            E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH.value,
        )

    def test_archetype_definitions_capture_r10_loop15_rules(self) -> None:
        epc = archetype_definition(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE)
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B)
        pf = archetype_definition(E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH)
        housing = archetype_definition(E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY)
        safety = archetype_definition(E2RArchetype.CONSTRUCTION_QUALITY_SAFETY_HARD_4C)
        material = archetype_definition(E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING)
        liquidity = archetype_definition(E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH)

        self.assertIn("cash collection schedule", " ".join(epc.stage3_high_conviction_signals))
        self.assertIn("legal appeal clearance", " ".join(nuclear.stage3_high_conviction_signals))
        self.assertIn("impairment cleanup", " ".join(pf.stage3_high_conviction_signals))
        self.assertIn("presale rate", " ".join(housing.stage3_high_conviction_signals))
        self.assertIn("substandard building materials", " ".join(safety.stage4c_thesis_break_signals))
        self.assertIn("rebar price decline", " ".join(material.stage4c_thesis_break_signals))
        self.assertIn("survival liquidity", " ".join(liquidity.false_positive_patterns))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round305_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND305_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round305_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_construction_policy_or_order_headline_as_green", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r10_loop15_samsung_ea_fadhili"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r10_loop15_hdc_gwangju_quality_hard_4c"].green_guardrails)

        summary = round305_summary()
        self.assertEqual(summary["round_id"], "round_233")
        self.assertEqual(summary["large_sector"], ROUND305_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 2)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 3)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_epc_policy_pf_and_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND305_CASE_CANDIDATES}
        samsung = by_id["r10_loop15_samsung_ea_fadhili"]
        gsenc = by_id["r10_loop15_gsenc_fadhili_overlay"]
        nuclear = by_id["r10_loop15_czech_nuclear_construction_basket"]
        taeyoung = by_id["r10_loop15_taeyoung_pf_restructuring"]
        housing = by_id["r10_loop15_seoul_housing_supply_reconstruction"]
        hdc = by_id["r10_loop15_hdc_gwangju_quality_hard_4c"]
        steel = by_id["r10_loop15_hyundai_steel_rebar_weak_construction_demand"]
        support = by_id["r10_loop15_builder_liquidity_support_false_positive_watch"]

        self.assertEqual(samsung.primary_archetype, E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE)
        self.assertEqual(samsung.event_mfe_pct, 8.5)
        self.assertEqual(samsung.extra_price_metrics["market_relative_return_pp"], 9.9)
        self.assertIn("cash_collection_schedule_missing", samsung.red_flag_fields)

        self.assertEqual(gsenc.round_alignment_label, "Stage2_evidence_but_not_actionable_without_company_price")
        self.assertIn("event_return_missing", gsenc.red_flag_fields)

        self.assertEqual(nuclear.primary_archetype, E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B)
        self.assertEqual(nuclear.extra_price_metrics["signed_contract_value_usd_bn"], 18.7)
        self.assertIn("legal_appeal_resolution_needed", nuclear.red_flag_fields)

        self.assertEqual(taeyoung.primary_archetype, E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH)
        self.assertEqual(taeyoung.extra_price_metrics["pf_delinquency_end_2023_pct"], 2.70)

        self.assertEqual(housing.primary_archetype, E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY)
        self.assertEqual(housing.extra_price_metrics["planned_homes_over_6y"], 400000)

        self.assertEqual(hdc.primary_archetype, E2RArchetype.CONSTRUCTION_QUALITY_SAFETY_HARD_4C)
        self.assertTrue(hdc.hard_4c_confirmed)
        self.assertEqual(hdc.extra_price_metrics["fatalities"], 6)

        self.assertEqual(steel.primary_archetype, E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING)
        self.assertEqual(steel.event_mae_pct, -1.2)
        self.assertEqual(steel.extra_price_metrics["net_profit_estimate_cut_pct"], -73)

        self.assertEqual(support.primary_archetype, E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH)
        self.assertEqual(support.score_price_alignment, "false_positive_score")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round305_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round305_shadow_weight_rows()}
        rules_md = render_round305_stage_rules_markdown()
        trigger_md = render_round305_trigger_grid_markdown()
        stage_md = render_round305_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND305_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r10l15_samsungea_fadhili_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r10l15_hdc_gwangju_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r10l15_czech_nuclear_T3"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND305_SHADOW_WEIGHT_ROWS), 7)
        self.assertEqual(shadow_rows["OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE"]["contract_value_vs_annual_backlog"], "+5")
        self.assertEqual(shadow_rows["NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B"]["preferred_bidder_without_final_contract_penalty"], "-5")
        self.assertEqual(shadow_rows["HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY"]["housing_starts_presale_rate"], "+5")
        self.assertIn("contract_value_is_meaningful_vs_annual_wins_or_backlog", ROUND305_STAGE2_ACTIONABLE_RULES)
        self.assertIn("PF_restructuring_terms_visible_but_impairment_or_cashflow_pending", ROUND305_STAGE3_YELLOW_RULES)
        self.assertIn("PF_cleanup_refinancing_and_impairment_resolution_visible", ROUND305_STAGE3_GREEN_RULES)
        self.assertIn("construction_quality_or_safety_hard_gate_active", ROUND305_GREEN_BLOCKERS)
        self.assertIn("contract_value_vs_annual_backlog", ROUND305_SCORE_UP_AXES)
        self.assertIn("policy_support_without_project_cashflow", ROUND305_SCORE_DOWN_AXES)
        self.assertIn("preferred_bidder_basket_rerating_before_final_contract", ROUND305_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_construction_quality_or_safety_event", ROUND305_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r10_loop15_czech_nuclear_construction_basket", trigger_md)
        self.assertIn("HDC Gwangju Hwajeong I-Park collapse", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round305_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_305.md")
        self.assertEqual(audit["round_id"], "round_233")
        self.assertEqual(audit["large_sector"], ROUND305_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_construction_policy_or_order_headline_as_green", audit["what_not_to_change"])

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
            paths = write_round305_r10_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round305_case_rows()
            self.assertEqual(len(records), len(ROUND305_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND305_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND305_TRIGGER_RECORDS))
            self.assertIn("Samsung E&A / Fadhili", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage3-Green", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r10l15_hdc_gwangju_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["contract_value_usd_bn"], 6.0)


if __name__ == "__main__":
    unittest.main()
