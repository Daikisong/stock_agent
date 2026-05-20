from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round247_r4_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round247_r4_loop11_materials_spread_strategic_price_validation import (
    ROUND247_CASE_CANDIDATES,
    ROUND247_GREEN_FORBIDDEN_PATTERNS,
    ROUND247_GREEN_REQUIRED_FIELDS,
    ROUND247_HARD_4C_GATES,
    ROUND247_LARGE_SECTOR,
    ROUND247_PRICE_VALIDATION_FIELDS,
    ROUND247_REQUIRED_TARGET_ALIASES,
    ROUND247_SCORE_ADJUSTMENTS,
    ROUND247_SHADOW_WEIGHT_ROWS,
    ROUND247_STAGE4B_WATCH_TRIGGERS,
    render_round247_green_gate_review_markdown,
    render_round247_stage4b_4c_review_markdown,
    round247_audit_payload,
    round247_case_records,
    round247_case_rows,
    round247_deep_sub_archetype_rows,
    round247_shadow_weight_rows,
    round247_summary,
    write_round247_r4_loop11_reports,
)


class Round247R4Loop11MaterialsSpreadStrategicPriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND247_REQUIRED_TARGET_ALIASES), 11)
        self.assertTrue(set(ROUND247_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND247_REQUIRED_TARGET_ALIASES["CRITICAL_MINERALS_SUPPLY_CHAIN"],
            E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN.value,
        )
        self.assertEqual(
            ROUND247_REQUIRED_TARGET_ALIASES["CATHODE_SUPPLY_CHAIN_DERISKING"],
            E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING.value,
        )
        self.assertEqual(
            ROUND247_REQUIRED_TARGET_ALIASES["BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK"],
            E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK.value,
        )

    def test_archetype_definitions_capture_round247_gates(self) -> None:
        critical = archetype_definition(E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN)
        ncc = archetype_definition(E2RArchetype.STANDALONE_NCC_CREDIT_BREAK)
        steel = archetype_definition(E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF)
        cathode = archetype_definition(E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING)
        polysilicon = archetype_definition(E2RArchetype.NON_CHINA_POLYSILICON_OPTIONALITY)
        break_case = archetype_definition(E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK)

        self.assertIn("offtake or price floor", critical.stage3_high_conviction_signals)
        self.assertIn("standalone cracker credit break", ncc.stage4c_thesis_break_signals)
        self.assertIn("actual plate spread", steel.stage3_high_conviction_signals)
        self.assertIn("confirmed cathode volume", cathode.stage3_high_conviction_signals)
        self.assertIn("unconfirmed customer media report rally", polysilicon.stage4b_graduation_overheat_signals)
        self.assertIn("contract value collapse", break_case.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round247_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND247_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_commodity_strategic_mineral_policy_restructuring_or_unconfirmed_media_as_green", record.green_guardrails)

        summary = round247_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["watch_4c_count"], 4)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 2)
        self.assertEqual(summary["price_moved_without_evidence_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_strategic_minerals_and_petrochemical_cases_keep_green_blocked(self) -> None:
        by_id = {case.case_id: case for case in ROUND247_CASE_CANDIDATES}
        korea_zinc = by_id["r4_loop11_korea_zinc_critical_minerals_governance"]
        lotte = by_id["r4_loop11_lotte_hd_petrochemical_restructuring"]
        yncc = by_id["r4_loop11_yncc_standalone_ncc_credit_watch"]

        self.assertEqual(korea_zinc.primary_archetype, E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN)
        self.assertIn(E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE, korea_zinc.secondary_archetypes)
        self.assertEqual(korea_zinc.stage2_date.isoformat(), "2026-03-12")
        self.assertEqual(korea_zinc.stage4c_date.isoformat(), "2025-12-16")
        self.assertEqual(korea_zinc.mae_1d, -13.0)
        self.assertEqual(korea_zinc.extra_price_metrics["share_issue_vs_project_value_pct"], 26.2)
        self.assertIsNone(korea_zinc.stage3_date)

        self.assertEqual(lotte.primary_archetype, E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING)
        self.assertEqual(lotte.extra_price_metrics["daesan_ncc_capacity_mn_tpy"], 1.1)
        self.assertEqual(lotte.extra_price_metrics["industry_capacity_cut_goal_pct"], 25.0)
        self.assertIsNone(lotte.stage3_date)

        self.assertEqual(yncc.primary_archetype, E2RArchetype.STANDALONE_NCC_CREDIT_BREAK)
        self.assertEqual(yncc.stage4c_date.isoformat(), "2025-08-27")
        self.assertEqual(yncc.extra_price_metrics["yncc_debt_to_equity_1h2025_pct"], 249.0)
        self.assertEqual(yncc.stage_failure_type, "should_have_been_red")

    def test_steel_cathode_lithium_polysilicon_and_lnf_are_classified(self) -> None:
        by_id = {case.case_id: case for case in ROUND247_CASE_CANDIDATES}
        steel = by_id["r4_loop11_hyundai_posco_steel_tariff_two_sided"]
        lg = by_id["r4_loop11_lg_chem_toyota_cathode_derisking"]
        posco = by_id["r4_loop11_posco_minres_lithium_resource_security"]
        oci = by_id["r4_loop11_oci_non_china_polysilicon_spacex_watch"]
        lnf = by_id["r4_loop11_lnf_tesla_cathode_contract_hard_4c"]

        self.assertEqual(steel.primary_archetype, E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF)
        self.assertIn(E2RArchetype.STEEL_TARIFF_EXPORT_RISK, steel.secondary_archetypes)
        self.assertEqual(steel.mfe_1d, 5.8)
        self.assertEqual(steel.mae_1d, -5.1)
        self.assertEqual(steel.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(lg.primary_archetype, E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING)
        self.assertEqual(lg.extra_price_metrics["huayou_stake_reduction_relative_pct"], -51.0)
        self.assertIsNone(lg.stage3_date)

        self.assertEqual(posco.primary_archetype, E2RArchetype.LITHIUM_RESOURCE_SECURITY)
        self.assertEqual(posco.extra_price_metrics["spodumene_drawdown_peak_to_low_pct"], -89.8)

        self.assertEqual(oci.primary_archetype, E2RArchetype.NON_CHINA_POLYSILICON_OPTIONALITY)
        self.assertEqual(oci.stage4b_date.isoformat(), "2026-04-14")
        self.assertEqual(oci.extra_price_metrics["spacex_contract_status"], "unconfirmed_media_report")

        self.assertEqual(lnf.primary_archetype, E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK)
        self.assertTrue(lnf.hard_4c_confirmed)
        self.assertEqual(lnf.stage4c_date.isoformat(), "2025-12-29")
        self.assertEqual(lnf.extra_price_metrics["contract_value_drawdown_pct"], -99.999745)
        self.assertEqual(lnf.rerating_result, "thesis_break")

    def test_green_gate_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND247_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND247_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND247_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND247_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round247_shadow_weight_rows()}
        deep_rows = round247_deep_sub_archetype_rows()
        green_markdown = render_round247_green_gate_review_markdown()
        stage_markdown = render_round247_stage4b_4c_review_markdown()

        self.assertIn("offtake_price_floor_or_take_or_pay", required)
        self.assertIn("fcf_after_working_capital", required)
        self.assertIn("unconfirmed_media_report", forbidden)
        self.assertIn("resource_deal_without_offtake", forbidden)
        self.assertIn("unconfirmed_customer_media_report_rally", ROUND247_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("standalone_cracker_credit_break", ROUND247_HARD_4C_GATES)
        self.assertIn("project_or_contract_value_anchor", fields)
        self.assertIn("customer_name_without_volume", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Tesla customer name", green_markdown)
        self.assertIn("r4_loop11_lnf_tesla_cathode_contract_hard_4c", stage_markdown)
        self.assertEqual(len(ROUND247_SHADOW_WEIGHT_ROWS), 10)
        self.assertEqual(shadow_rows["CRITICAL_MINERALS_SUPPLY_CHAIN"]["offtake_quality"], "+5")
        self.assertEqual(shadow_rows["BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Korea Zinc" in row["terms"] for row in deep_rows))
        self.assertTrue(any("SpaceX" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round247_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_247.md")
        self.assertEqual(audit["round_id"], "round_175")
        self.assertEqual(audit["large_sector"], ROUND247_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round247_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round247_r4_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round247_case_rows()
            self.assertEqual(len(records), len(ROUND247_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND247_CASE_CANDIDATES))
            self.assertIn("Korea Zinc", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("product_spread_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("YNCC", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["share_issue_vs_project_value_pct"], 26.2)


if __name__ == "__main__":
    unittest.main()
