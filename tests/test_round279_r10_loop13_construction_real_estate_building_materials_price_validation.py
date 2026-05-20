from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round279_r10_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round279_r10_loop13_construction_real_estate_building_materials_price_validation import (
    ROUND279_CASE_CANDIDATES,
    ROUND279_GREEN_FORBIDDEN_PATTERNS,
    ROUND279_GREEN_REQUIRED_FIELDS,
    ROUND279_HARD_4C_GATES,
    ROUND279_LARGE_SECTOR,
    ROUND279_PRICE_VALIDATION_FIELDS,
    ROUND279_REQUIRED_TARGET_ALIASES,
    ROUND279_SHADOW_WEIGHT_ROWS,
    ROUND279_STAGE4B_WATCH_TRIGGERS,
    render_round279_green_gate_review_markdown,
    render_round279_stage4b_4c_review_markdown,
    round279_audit_payload,
    round279_case_records,
    round279_case_rows,
    round279_deep_sub_archetype_rows,
    round279_shadow_weight_rows,
    round279_summary,
    write_round279_r10_loop13_reports,
)


class Round279R10Loop13ConstructionRealEstateBuildingMaterialsPriceValidationTests(unittest.TestCase):
    def test_round279_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND279_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND279_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND279_REQUIRED_TARGET_ALIASES["REAL_ESTATE_PF_LIQUIDITY_4C_WATCH"],
            E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND279_REQUIRED_TARGET_ALIASES["OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN"],
            E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN.value,
        )
        self.assertEqual(
            ROUND279_REQUIRED_TARGET_ALIASES["STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK"],
            E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK.value,
        )

    def test_round279_archetype_definitions_capture_r10_loop13_gates(self) -> None:
        pf = archetype_definition(E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH)
        epc = archetype_definition(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN)
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2)
        materials = archetype_definition(E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK)
        property_policy = archetype_definition(E2RArchetype.SEOUL_PROPERTY_POLICY_EVENT_PREMIUM)
        steel = archetype_definition(E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK)
        builder = archetype_definition(E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF)

        self.assertIn("government support treated as Green", pf.false_positive_patterns)
        self.assertIn("EPC margin", epc.stage3_high_conviction_signals)
        self.assertIn("preferred bidder treated as final contract", nuclear.false_positive_patterns)
        self.assertIn("construction demand collapse", materials.stage4c_thesis_break_signals)
        self.assertIn("rate-cut property expectation treated as Green", property_policy.false_positive_patterns)
        self.assertIn("tariff relief-only treated as Green", steel.false_positive_patterns)
        self.assertIn("PF support without profitability", builder.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round279_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND279_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("direct_listed_hard_4c_confirmed_false", record.green_guardrails)
            self.assertIn("do_not_use_round279_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round279_summary()
        self.assertEqual(summary["round_id"], "round_207")
        self.assertEqual(summary["large_sector"], "CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 3)
        self.assertEqual(summary["policy_relief_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["direct_listed_hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 6)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])
        self.assertFalse(summary["direct_listed_hard_4c_confirmed"])

    def test_construction_cases_keep_policy_order_and_cashflow_separate(self) -> None:
        by_id = {case.case_id: case for case in ROUND279_CASE_CANDIDATES}
        pf = by_id["r10_loop13_real_estate_pf_taeyoung_liquidity_watch"]
        epc = by_id["r10_loop13_samsung_ena_gs_fadhili_epc_order_stage2"]
        nuclear = by_id["r10_loop13_czech_nuclear_infra_preferred_bidder_legal_watch"]
        hyundai_steel = by_id["r10_loop13_hyundai_steel_construction_material_demand_break"]
        seoul = by_id["r10_loop13_seoul_property_policy_ratecut_macro_gate"]
        safety = by_id["r10_loop13_anseong_highway_construction_safety_reference"]
        builder = by_id["r10_loop13_builder_liquidity_package_policy_relief"]
        anti_dumping = by_id["r10_loop13_steel_plate_anti_dumping_construction_relief"]

        self.assertEqual(pf.primary_archetype, E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH)
        self.assertEqual(pf.extra_price_metrics["government_support_krw_trn"], 40.6)
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_end_2023_pct"], 2.70)
        self.assertIn("PF_support_without_profitability", pf.red_flag_fields)

        self.assertEqual(epc.primary_archetype, E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN)
        self.assertEqual(epc.extra_price_metrics["samsung_event_mfe_pct"], 8.5)
        self.assertEqual(epc.extra_price_metrics["samsung_contract_share_of_total_pct"], 77.9)
        self.assertEqual(epc.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(nuclear.primary_archetype, E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2)
        self.assertEqual(nuclear.extra_price_metrics["doosan_enerbility_3m_return_pct"], 48)
        self.assertFalse(nuclear.extra_price_metrics["final_contract_signed"])
        self.assertTrue(nuclear.extra_price_metrics["temporary_contract_block"])

        self.assertEqual(hyundai_steel.primary_archetype, E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK)
        self.assertEqual(hyundai_steel.extra_price_metrics["net_profit_estimate_cut_pct"], -73)
        self.assertEqual(hyundai_steel.extra_price_metrics["anti_dumping_event_mfe_pct"], 5.8)
        self.assertEqual(hyundai_steel.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(seoul.primary_archetype, E2RArchetype.SEOUL_PROPERTY_POLICY_EVENT_PREMIUM)
        self.assertEqual(seoul.extra_price_metrics["household_debt_2024_krw_trn"], 1927.3)
        self.assertIn("Gangnam", seoul.extra_price_metrics["land_transaction_permit_areas"])

        self.assertEqual(safety.primary_archetype, E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE)
        self.assertTrue(safety.hard_4c_confirmed)
        self.assertFalse(safety.direct_listed_hard_4c_confirmed)
        self.assertEqual(safety.extra_price_metrics["fatalities"], 3)

        self.assertEqual(builder.primary_archetype, E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF)
        self.assertIn("market stabilising fund", builder.extra_price_metrics["support_tools"])

        self.assertEqual(anti_dumping.primary_archetype, E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK)
        self.assertEqual(anti_dumping.extra_price_metrics["chinese_share_of_total_steel_imports_pct"], 49)
        self.assertTrue(anti_dumping.extra_price_metrics["u_s_tariff_export_risk"])

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND279_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND279_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND279_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round279_shadow_weight_rows()}
        deep_rows = round279_deep_sub_archetype_rows()
        green_markdown = render_round279_green_gate_review_markdown()
        stage_markdown = render_round279_stage4b_4c_review_markdown()

        self.assertIn("PF_refinancing_success_confirmed", required)
        self.assertIn("construction_safety_trust_confirmed", required)
        self.assertIn("policy_support_only", forbidden)
        self.assertIn("tariff_relief_only", forbidden)
        self.assertIn("nuclear_preferred_bidder_basket_plus_40pct_before_final_contract", ROUND279_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_construction_site_accident", ROUND279_HARD_4C_GATES)
        self.assertIn("PF_delinquency_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Anseong", stage_markdown)
        self.assertIn("hard 4C", stage_markdown)
        self.assertEqual(len(ROUND279_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CONSTRUCTION_SAFETY_HARD_REFERENCE"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Taeyoung E&C" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Anseong highway collapse" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round279_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_279.md")
        self.assertEqual(audit["round_id"], "round_207")
        self.assertEqual(audit["large_sector"], ROUND279_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertFalse(audit["summary"]["direct_listed_hard_4c_confirmed"])
        self.assertIn("do_not_use_round279_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round279_r10_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round279_case_rows()
            self.assertEqual(len(records), len(ROUND279_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND279_CASE_CANDIDATES))
            self.assertIn("Samsung E&A", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("PF_refinancing_success_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("REAL_ESTATE_PF_LIQUIDITY_4C_WATCH", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("PF_delinquency_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["samsung_event_mfe_pct"], 8.5)


if __name__ == "__main__":
    unittest.main()
