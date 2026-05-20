from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round260_r4_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round260_r4_loop12_materials_spread_strategic_price_validation import (
    ROUND260_CASE_CANDIDATES,
    ROUND260_GREEN_FORBIDDEN_PATTERNS,
    ROUND260_GREEN_REQUIRED_FIELDS,
    ROUND260_HARD_4C_GATES,
    ROUND260_LARGE_SECTOR,
    ROUND260_PRICE_VALIDATION_FIELDS,
    ROUND260_REQUIRED_TARGET_ALIASES,
    ROUND260_SCORE_ADJUSTMENTS,
    ROUND260_SHADOW_WEIGHT_ROWS,
    ROUND260_STAGE4B_WATCH_TRIGGERS,
    render_round260_green_gate_review_markdown,
    render_round260_stage4b_4c_review_markdown,
    round260_audit_payload,
    round260_case_records,
    round260_case_rows,
    round260_deep_sub_archetype_rows,
    round260_shadow_weight_rows,
    round260_summary,
    write_round260_r4_loop12_reports,
)


class Round260R4Loop12MaterialsSpreadStrategicPriceValidationTests(unittest.TestCase):
    def test_round260_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND260_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND260_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND260_REQUIRED_TARGET_ALIASES["DEFENSE_METALS_AMMUNITION_OPTIONALITY"],
            E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY.value,
        )
        self.assertEqual(
            ROUND260_REQUIRED_TARGET_ALIASES["CRITICAL_MINERALS_RECYCLING_SMELTER"],
            E2RArchetype.CRITICAL_MINERALS_RECYCLING_SMELTER.value,
        )
        self.assertEqual(
            ROUND260_REQUIRED_TARGET_ALIASES["RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C"],
            E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C.value,
        )
        self.assertEqual(
            ROUND260_REQUIRED_TARGET_ALIASES["CRITICAL_MINERALS_POLICY_RELIEF"],
            E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF.value,
        )

    def test_round260_archetype_definitions_capture_green_guards(self) -> None:
        defense = archetype_definition(E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY)
        critical = archetype_definition(E2RArchetype.CRITICAL_MINERALS_RECYCLING_SMELTER)
        rare = archetype_definition(E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C)
        steel = archetype_definition(E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK)
        policy = archetype_definition(E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF)

        self.assertIn("confirmed transaction", defense.stage3_high_conviction_signals)
        self.assertIn("dilution and governance risk cleared", critical.stage3_high_conviction_signals)
        self.assertIn("China end-use sanction", rare.stage4c_thesis_break_signals)
        self.assertIn("export-margin resilience", steel.stage3_high_conviction_signals)
        self.assertIn("actual supply contract", policy.stage3_high_conviction_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round260_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND260_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_mna_policy_strategic_material_capex_restructuring_or_tariff_as_green_alone", record.green_guardrails)

        summary = round260_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["watch_case_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["watch_4c_count"], 4)
        self.assertEqual(summary["false_positive_score_count"], 1)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["reported_price_anchor_count"], 4)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["hard_4c_confirmed"])

    def test_poongsan_and_korea_zinc_separate_event_premium_from_stage2_project(self) -> None:
        by_id = {case.case_id: case for case in ROUND260_CASE_CANDIDATES}
        poongsan = by_id["r4_loop12_poongsan_defense_metals_mna_rumor"]
        zinc = by_id["r4_loop12_korea_zinc_critical_minerals_dilution_watch"]

        self.assertEqual(poongsan.primary_archetype, E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY)
        self.assertEqual(poongsan.case_type, "event_premium")
        self.assertEqual(poongsan.stage1_date.isoformat(), "2026-04-03")
        self.assertEqual(poongsan.stage4b_date.isoformat(), "2026-04-09")
        self.assertIn("hanwha_dropped_review", poongsan.red_flag_fields)
        self.assertEqual(poongsan.extra_price_metrics["reported_potential_deal_value_krw_trn"], 1.5)

        self.assertEqual(zinc.primary_archetype, E2RArchetype.CRITICAL_MINERALS_RECYCLING_SMELTER)
        self.assertIn(E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE, zinc.secondary_archetypes)
        self.assertEqual(zinc.stage2_date.isoformat(), "2026-03-12")
        self.assertEqual(zinc.extra_price_metrics["us_smelter_project_value_usd_bn"], 7.4)
        self.assertEqual(zinc.extra_price_metrics["share_issuance_vs_project_value_pct"], 26.2)
        self.assertIsNone(zinc.stage3_date)

    def test_rare_earth_steel_and_policy_capex_cases_are_guarded(self) -> None:
        by_id = {case.case_id: case for case in ROUND260_CASE_CANDIDATES}
        rare = by_id["r4_loop12_china_rare_earth_end_use_restriction_overlay"]
        steel = by_id["r4_loop12_posco_hyundai_seah_steel_tariff_two_sided"]
        capex = by_id["r4_loop12_hyundai_steel_us_capex_false_positive"]

        self.assertEqual(rare.primary_archetype, E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C)
        self.assertEqual(rare.stage4c_date.isoformat(), "2025-04-22")
        self.assertIn("sanction_warning", rare.red_flag_fields)
        self.assertEqual(rare.extra_price_metrics["affected_sectors"][0], "power transformers")

        self.assertEqual(steel.primary_archetype, E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK)
        self.assertEqual(steel.mfe_1d, 5.8)
        self.assertEqual(steel.mae_1d, -8.0)
        self.assertEqual(steel.extra_price_metrics["hyundai_relative_outperformance_pp"], 6.5)
        self.assertEqual(steel.extra_price_metrics["seah_steel_50pct_tariff_mae_pct"], -8.0)

        self.assertEqual(capex.primary_archetype, E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE)
        self.assertEqual(capex.score_price_alignment, "false_positive_score")
        self.assertEqual(capex.extra_price_metrics["plant_investment_usd_bn"], 5.8)
        self.assertEqual(capex.extra_price_metrics["post_announcement_drawdown_pct"], -21.2)
        self.assertEqual(capex.stage_failure_type, "false_green")

    def test_petrochemical_and_policy_relief_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND260_CASE_CANDIDATES}
        yncc = by_id["r4_loop12_lgchem_hanwha_dl_yncc_petrochemical_credit_watch"]
        lotte = by_id["r4_loop12_lotte_hd_hyundai_chemical_restructuring_relief"]
        policy = by_id["r4_loop12_korea_critical_minerals_policy_relief"]

        self.assertEqual(yncc.primary_archetype, E2RArchetype.STANDALONE_NCC_CREDIT_BREAK)
        self.assertEqual(yncc.stage4c_date.isoformat(), "2025-08-27")
        self.assertEqual(yncc.extra_price_metrics["yncc_debt_to_equity_1h2025_pct"], 249.0)
        self.assertIn("restructuring_plan_undisclosed", yncc.red_flag_fields)

        self.assertEqual(lotte.primary_archetype, E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING)
        self.assertEqual(lotte.stage2_date.isoformat(), "2026-02-24")
        self.assertEqual(lotte.extra_price_metrics["daesan_ncc_shutdown_capacity_mn_tpy"], 1.1)
        self.assertEqual(lotte.rerating_result, "credit_relief_rally")

        self.assertEqual(policy.primary_archetype, E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF)
        self.assertEqual(policy.stage2_date.isoformat(), "2026-02-05")
        self.assertEqual(policy.extra_price_metrics["critical_minerals_monitored"], 17)
        self.assertEqual(policy.extra_price_metrics["overseas_mining_support_krw_bn"], 250.0)
        self.assertIsNone(policy.stage3_date)

    def test_green_gate_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND260_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND260_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND260_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND260_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round260_shadow_weight_rows()}
        deep_rows = round260_deep_sub_archetype_rows()
        green_markdown = render_round260_green_gate_review_markdown()
        stage_markdown = render_round260_stage4b_4c_review_markdown()

        self.assertIn("product_spread_confirmed", required)
        self.assertIn("working_capital_stable", required)
        self.assertIn("mna_rumor_only", forbidden)
        self.assertIn("rare_earth_end_use_restriction_present", forbidden)
        self.assertIn("anti_dumping_tariff_relief_rally", ROUND260_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("china_end_use_sanction", ROUND260_HARD_4C_GATES)
        self.assertIn("tariff_or_export_control_anchor", fields)
        self.assertIn("US_CAPEX_without_ROI", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("M&A rumor", green_markdown)
        self.assertIn("r4_loop12_hyundai_steel_us_capex_false_positive", stage_markdown)
        self.assertEqual(len(ROUND260_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["CRITICAL_MINERALS_RECYCLING_SMELTER"]["offtake_quality"], "+5")
        self.assertEqual(shadow_rows["POLICY_CAPEX_FALSE_POSITIVE"]["event_penalty"], "-5")
        self.assertTrue(any("Korea Zinc" in row["terms"] for row in deep_rows))
        self.assertTrue(any("YNCC" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round260_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_260.md")
        self.assertEqual(audit["round_id"], "round_188")
        self.assertEqual(audit["large_sector"], ROUND260_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round260_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round260_r4_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round260_case_rows()
            self.assertEqual(len(records), len(ROUND260_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND260_CASE_CANDIDATES))
            self.assertIn("Poongsan", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("product_spread_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("STEEL_TARIFF_TWO_SIDED_RELIEF_RISK", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("critical-minerals", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["share_issuance_vs_project_value_pct"], 26.2)


if __name__ == "__main__":
    unittest.main()
