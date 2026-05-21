from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round331_r10_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round331_r10_loop17_construction_real_estate_building_materials_trigger_validation import (
    ROUND331_CASE_CANDIDATES,
    ROUND331_GREEN_BLOCKERS,
    ROUND331_HARD_4C_GATES,
    ROUND331_LARGE_SECTOR,
    ROUND331_REQUIRED_TARGET_ALIASES,
    ROUND331_ROW_SEPARATION_RULES,
    ROUND331_SCORE_DOWN_AXES,
    ROUND331_SCORE_UP_AXES,
    ROUND331_SHADOW_WEIGHT_ROWS,
    ROUND331_STAGE2_ACTIONABLE_RULES,
    ROUND331_STAGE3_GREEN_RULES,
    ROUND331_STAGE3_YELLOW_RULES,
    ROUND331_STAGE4B_WATCH_TRIGGERS,
    ROUND331_TRIGGER_RECORDS,
    render_round331_stage4b_4c_review_markdown,
    render_round331_stage_rules_markdown,
    render_round331_trigger_grid_markdown,
    round331_audit_payload,
    round331_case_records,
    round331_case_rows,
    round331_shadow_weight_rows,
    round331_summary,
    round331_trigger_rows,
    write_round331_r10_loop17_reports,
)


class Round331R10Loop17ConstructionRealEstateTests(unittest.TestCase):
    def test_round331_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND331_REQUIRED_TARGET_ALIASES), 7)
        self.assertTrue(set(ROUND331_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND331_REQUIRED_TARGET_ALIASES["OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE"],
            E2RArchetype.OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND331_REQUIRED_TARGET_ALIASES["NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B"],
            E2RArchetype.NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B.value,
        )
        self.assertEqual(
            ROUND331_REQUIRED_TARGET_ALIASES["CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE"],
            E2RArchetype.CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE.value,
        )

    def test_archetype_definitions_capture_round331_rules(self) -> None:
        overseas = archetype_definition(E2RArchetype.OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE)
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B)
        housing = archetype_definition(E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE)
        pf = archetype_definition(E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4B)
        holdco = archetype_definition(E2RArchetype.CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING)
        safety = archetype_definition(E2RArchetype.CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE)
        liquidity = archetype_definition(E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF)

        self.assertIn("progress billing", " ".join(overseas.stage3_high_conviction_signals))
        self.assertIn("cost overrun", " ".join(overseas.stage4c_thesis_break_signals))
        self.assertIn("preferred nuclear bidder", " ".join(nuclear.stage1_radar_signals))
        self.assertIn("final contract signed", " ".join(nuclear.stage3_high_conviction_signals))
        self.assertIn("legal appeal", " ".join(nuclear.stage4b_graduation_overheat_signals))
        self.assertIn("permits", " ".join(housing.stage3_high_conviction_signals))
        self.assertIn("pre-sales", " ".join(housing.stage3_high_conviction_signals))
        self.assertIn("policy without builder price", " ".join(housing.stage4b_graduation_overheat_signals))
        self.assertIn("bad-project cleanup", " ".join(pf.stage3_high_conviction_signals))
        self.assertIn("PF rollover", " ".join(pf.stage3_high_conviction_signals))
        self.assertIn("liquidity support without loss cleanup", " ".join(pf.stage4b_graduation_overheat_signals))
        self.assertIn("board-approved capital return", " ".join(holdco.stage3_high_conviction_signals))
        self.assertIn("almost -10% event reaction", " ".join(holdco.stage4b_graduation_overheat_signals))
        self.assertIn("fatal construction collapse", " ".join(safety.stage4c_thesis_break_signals))
        self.assertIn("listed-stock price anchor unavailable", " ".join(safety.stage4b_graduation_overheat_signals))
        self.assertIn("rate-cut hope without refinancing", " ".join(liquidity.stage4b_graduation_overheat_signals))
        self.assertIn("pre-sale cash recovery", " ".join(liquidity.stage3_high_conviction_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round331_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND331_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round331_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", record.green_guardrails)

        summary = round331_summary()
        self.assertEqual(summary["round_id"], "round_259")
        self.assertEqual(summary["loop_name"], "R10 Loop 17")
        self.assertEqual(summary["large_sector"], ROUND331_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 7)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 1)
        self.assertEqual(summary["stage2_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["price_unavailable_count"], 3)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_epc_nuclear_policy_pf_valueup_safety_and_liquidity(self) -> None:
        by_id = {case.case_id: case for case in ROUND331_CASE_CANDIDATES}
        epc = by_id["r10_loop17_samsung_ena_fadhili_epc"]
        nuclear = by_id["r10_loop17_czech_nuclear_epc"]
        housing = by_id["r10_loop17_seoul_housing_supply_reconstruction"]
        pf = by_id["r10_loop17_real_estate_pf_restructuring"]
        holdco = by_id["r10_loop17_samsung_ct_valueup_failed"]
        safety = by_id["r10_loop17_highway_construction_collapse_safety"]
        liquidity = by_id["r10_loop17_builder_liquidity_rate_relief"]

        self.assertEqual(epc.extra_price_metrics["contract_value_usd_bn"], 6.0)
        self.assertEqual(epc.extra_price_metrics["event_return_pct"], 8.5)
        self.assertEqual(epc.extra_price_metrics["market_relative_return_pp"], 9.9)
        self.assertIn("EPC_margin_visibility_missing", epc.red_flag_fields)

        self.assertEqual(nuclear.extra_price_metrics["doosan_3m_return_pct"], 48)
        self.assertEqual(nuclear.extra_price_metrics["kepco_ec_3m_return_pct"], 41)
        self.assertIn("final_contract_not_signed_4B", nuclear.red_flag_fields)

        self.assertEqual(housing.extra_price_metrics["seoul_home_price_weekly_pct"], 0.76)
        self.assertEqual(housing.extra_price_metrics["ltv_after_pct"], 40)
        self.assertEqual(housing.score_price_alignment, "unknown")

        self.assertEqual(pf.extra_price_metrics["pf_delinquency_2024_pct"], 2.70)
        self.assertEqual(pf.extra_price_metrics["support_package_krw_trn"], 40.6)
        self.assertIn("bad_project_cleanup_missing_4B", pf.red_flag_fields)

        self.assertEqual(holdco.extra_price_metrics["event_return_label"], "almost_-10")
        self.assertEqual(holdco.score_price_alignment, "evidence_good_but_price_failed")

        self.assertTrue(safety.hard_4c_confirmed)
        self.assertEqual(safety.extra_price_metrics["fatalities_context"], "at_least_3_to_4")
        self.assertEqual(safety.extra_price_metrics["injured"], 6)

        self.assertEqual(liquidity.extra_price_metrics["support_package_krw_trn"], 40.6)
        self.assertEqual(liquidity.extra_price_metrics["BOK_policy_rate_pct"], 2.5)
        self.assertIn("PF_refinancing_missing_4B", liquidity.red_flag_fields)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round331_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round331_shadow_weight_rows()}
        rules_md = render_round331_stage_rules_markdown()
        trigger_md = render_round331_trigger_grid_markdown()
        stage_md = render_round331_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND331_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r10l17_samsung_ena_fadhili_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r10l17_czech_legal_T3"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r10l17_highway_collapse_T0"]["promote_to"], "4C_sector_watch")
        self.assertEqual(trigger_rows["r10l17_samsung_ct_valueup_T1"]["event_return_pct"], "almost_-10")
        self.assertEqual(len(ROUND331_SHADOW_WEIGHT_ROWS), 7)
        self.assertEqual(shadow_rows["OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE"]["overseas_EPC_contract_value"], "+5")
        self.assertEqual(shadow_rows["NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B"]["nuclear_infra_EPC_optionality"], "+5")
        self.assertEqual(shadow_rows["CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE"]["construction_safety_risk"], "+5")
        self.assertIn("event_return_at_least_5pct_or_market_relative_return_at_least_5pp", ROUND331_STAGE2_ACTIONABLE_RULES)
        self.assertIn("PF_restructuring_shows_bad_project_cleanup_and_refinancing", ROUND331_STAGE3_YELLOW_RULES)
        self.assertIn("full_window_adjusted_OHLC_MFE_MAE_is_available_and_supportive", ROUND331_STAGE3_GREEN_RULES)
        self.assertIn("preferred_bidder_without_final_contract", ROUND331_GREEN_BLOCKERS)
        self.assertIn("PF_restructuring_recognition", ROUND331_SCORE_UP_AXES)
        self.assertIn("liquidity_support_without_loss_cleanup_penalty", ROUND331_SCORE_DOWN_AXES)
        self.assertIn("preferred_bidder_premium_before_final_contract", ROUND331_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_construction_collapse", ROUND331_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND331_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r10_loop17_samsung_ena_fadhili_epc", trigger_md)
        self.assertIn("r10_loop17_highway_construction_collapse_safety", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round331_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_331.md")
        self.assertEqual(audit["round_id"], "round_259")
        self.assertEqual(audit["large_sector"], ROUND331_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_change_production_scoring", audit["what_not_to_change"])
        self.assertIn("do_not_use_round331_cases_as_candidate_generation_input", audit["what_not_to_change"])

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
            paths = write_round331_r10_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round331_case_rows()
            self.assertEqual(len(records), len(ROUND331_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND331_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND331_TRIGGER_RECORDS))
            self.assertIn("Samsung E&A", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r10l17_highway_collapse_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("REAL_ESTATE_PF_RESTRUCTURING_4B", paths["weight_profile"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
