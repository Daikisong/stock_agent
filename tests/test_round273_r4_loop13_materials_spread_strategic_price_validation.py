from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round273_r4_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round273_r4_loop13_materials_spread_strategic_price_validation import (
    ROUND273_CASE_CANDIDATES,
    ROUND273_GREEN_FORBIDDEN_PATTERNS,
    ROUND273_GREEN_REQUIRED_FIELDS,
    ROUND273_HARD_4C_GATES,
    ROUND273_LARGE_SECTOR,
    ROUND273_PRICE_VALIDATION_FIELDS,
    ROUND273_REQUIRED_TARGET_ALIASES,
    ROUND273_SCORE_ADJUSTMENTS,
    ROUND273_SHADOW_WEIGHT_ROWS,
    ROUND273_STAGE4B_WATCH_TRIGGERS,
    render_round273_green_gate_review_markdown,
    render_round273_stage4b_4c_review_markdown,
    round273_audit_payload,
    round273_case_records,
    round273_case_rows,
    round273_deep_sub_archetype_rows,
    round273_shadow_weight_rows,
    round273_summary,
    write_round273_r4_loop13_reports,
)


class Round273R4Loop13MaterialsSpreadStrategicPriceValidationTests(unittest.TestCase):
    def test_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND273_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND273_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND273_REQUIRED_TARGET_ALIASES["CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION"],
            E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION.value,
        )
        self.assertEqual(
            ROUND273_REQUIRED_TARGET_ALIASES["GRAPHITE_LITHIUM_POLICY_PRICE_EVENT"],
            E2RArchetype.GRAPHITE_LITHIUM_POLICY_PRICE_EVENT.value,
        )
        self.assertEqual(
            ROUND273_REQUIRED_TARGET_ALIASES["PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE"],
            E2RArchetype.PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE.value,
        )

    def test_archetype_definitions_encode_r4_loop13_gates(self) -> None:
        zinc = archetype_definition(E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION)
        graphite = archetype_definition(E2RArchetype.GRAPHITE_LITHIUM_POLICY_PRICE_EVENT)
        steel = archetype_definition(E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK)
        capex = archetype_definition(E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE)
        petchem = archetype_definition(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING)
        overseas = archetype_definition(E2RArchetype.PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE)
        defense_metals = archetype_definition(E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY)
        copper = archetype_definition(E2RArchetype.COPPER_COMMODITY_OVERHEAT_4B)

        self.assertIn("offtake, margin, FCF, funding quality, and dilution/governance control confirmed", zinc.stage3_high_conviction_signals)
        self.assertIn("tariff relief treated as margin", graphite.false_positive_patterns)
        self.assertIn("domestic tariff relief counted without export risk", steel.false_positive_patterns)
        self.assertIn("not from CAPEX headline alone; funding clarity, margin, FCF, and demand conversion required", capex.stage3_high_conviction_signals)
        self.assertIn("capacity cut without spread recovery", petchem.false_positive_patterns)
        self.assertIn("ethylene or PTA spread, utilization, working capital, ROIC, and FCF confirmed", overseas.stage3_high_conviction_signals)
        self.assertIn("M&A rumor treated as Green", defense_metals.false_positive_patterns)
        self.assertIn("copper spot rally treated as structural FCF", copper.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round273_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND273_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_invent_price_or_stage_dates", record.green_guardrails)

        summary = round273_summary()
        self.assertEqual(summary["round_id"], "round_201")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["event_premium_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["four_b_watch_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["price_data_unavailable_count"], 4)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertEqual(summary["false_positive_score_count"], 1)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["hard_4c_confirmed"])

    def test_zinc_graphite_steel_and_hyundai_cases_capture_price_anchors(self) -> None:
        by_id = {case.case_id: case for case in ROUND273_CASE_CANDIDATES}
        zinc = by_id["r4_loop13_korea_zinc_control_premium_dilution_watch"]
        posco_futurem = by_id["r4_loop13_posco_futurem_graphite_lithium_event"]
        steel = by_id["r4_loop13_steel_tariff_two_sided_posco_hyundai_seah"]
        hyundai = by_id["r4_loop13_hyundai_steel_us_plant_policy_capex_false_positive"]

        self.assertEqual(zinc.primary_archetype, E2RArchetype.CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION)
        self.assertEqual(zinc.stage2_price_anchor, 660000.0)
        self.assertEqual(zinc.stage4b_price_anchor, 690000.0)
        self.assertEqual(zinc.extra_price_metrics["event_mfe_pct"], 24.0)
        self.assertEqual(zinc.extra_price_metrics["injunction_event_mae_pct"], -13.0)
        self.assertEqual(zinc.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(posco_futurem.primary_archetype, E2RArchetype.GRAPHITE_LITHIUM_POLICY_PRICE_EVENT)
        self.assertEqual(posco_futurem.extra_price_metrics["graphite_tariff_event_mfe_pct"], 20.0)
        self.assertEqual(posco_futurem.extra_price_metrics["catl_lithium_event_mfe_pct"], 8.3)
        self.assertFalse(posco_futurem.extra_price_metrics["actual_graphite_supply_contract_confirmed"])
        self.assertFalse(posco_futurem.extra_price_metrics["margin_confirmed"])

        self.assertEqual(steel.primary_archetype, E2RArchetype.STEEL_TARIFF_TWO_SIDED_RELIEF_RISK)
        self.assertEqual(steel.extra_price_metrics["hyundai_steel_antidumping_mfe_pct"], 5.8)
        self.assertEqual(steel.extra_price_metrics["seah_steel_50pct_tariff_mae_pct"], -8.0)
        self.assertEqual(steel.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(hyundai.primary_archetype, E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE)
        self.assertEqual(hyundai.extra_price_metrics["plant_investment_usd_bn"], 5.8)
        self.assertEqual(hyundai.extra_price_metrics["annual_capacity_mn_tonnes"], 2.7)
        self.assertEqual(hyundai.extra_price_metrics["post_announcement_drawdown_pct"], -21.2)
        self.assertEqual(hyundai.score_price_alignment, "false_positive_score")

    def test_petchem_lotte_and_poongsan_cases_do_not_force_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND273_CASE_CANDIDATES}
        yncc = by_id["r4_loop13_lgchem_hanwha_dl_yncc_petchem_credit_watch"]
        lotte_hd = by_id["r4_loop13_lotte_hd_hyundai_petchem_restructuring_relief"]
        lotte_overseas = by_id["r4_loop13_lotte_chemical_overseas_portfolio_spread_gate"]
        poongsan = by_id["r4_loop13_poongsan_defense_metals_mna_rumor"]

        self.assertEqual(yncc.primary_archetype, E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING)
        self.assertEqual(yncc.extra_price_metrics["yncc_debt_to_equity_1h2025_pct"], 249.0)
        self.assertEqual(yncc.extra_price_metrics["capacity_cut_equivalent_pct"], 25.0)
        self.assertIn("restructuring_plan_undisclosed", yncc.red_flag_fields)

        self.assertEqual(lotte_hd.primary_archetype, E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING)
        self.assertEqual(lotte_hd.extra_price_metrics["daesan_ncc_shutdown_capacity_mn_tpy"], 1.1)
        self.assertEqual(lotte_hd.extra_price_metrics["capital_increase_krw_trn"], 1.2)
        self.assertEqual(lotte_hd.stage_failure_type, "stage2_watch_success")

        self.assertEqual(lotte_overseas.primary_archetype, E2RArchetype.PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE)
        self.assertEqual(lotte_overseas.extra_price_metrics["indonesia_project_value_usd_bn"], 4.0)
        self.assertEqual(lotte_overseas.extra_price_metrics["pakistan_stake_sold_pct"], 75.0)
        self.assertFalse(lotte_overseas.extra_price_metrics["utilization_confirmed"])

        self.assertEqual(poongsan.primary_archetype, E2RArchetype.DEFENSE_METALS_AMMUNITION_OPTIONALITY)
        self.assertEqual(poongsan.extra_price_metrics["reported_deal_value_krw_trn"], 1.5)
        self.assertIn("Hanwha dropped review", poongsan.extra_price_metrics["transaction_status"])
        self.assertIn("M&A_rumor_only", poongsan.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND273_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND273_GREEN_FORBIDDEN_PATTERNS)
        review = render_round273_green_gate_review_markdown()
        stage_review = render_round273_stage4b_4c_review_markdown()
        fields = set(ROUND273_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND273_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round273_shadow_weight_rows()}
        deep_rows = round273_deep_sub_archetype_rows()

        self.assertIn("product_spread_visibility_confirmed", required)
        self.assertIn("governance_dilution_risk_cleared", required)
        self.assertIn("export_control_or_tariff_risk_cleared", required)
        self.assertIn("control_premium_only", forbidden)
        self.assertIn("policy_capex_only", forbidden)
        self.assertIn("capacity_shutdown_only", forbidden)
        self.assertIn("product_spread_visibility", axes)
        self.assertIn("export_tariff_exposure", axes)
        self.assertIn("governance_dilution_anchor", fields)
        self.assertIn("policy_capex_before_funding_roi", ROUND273_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("export_tariff_destroying_margin", ROUND273_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("hard 4C", stage_review)
        self.assertEqual(len(ROUND273_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION"]["governance_dilution_control"], "+5")
        self.assertEqual(shadow_rows["POLICY_CAPEX_FALSE_POSITIVE"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["PETROCHEMICAL_CAPACITY_RESTRUCTURING"]["policy_relief_to_margin_bridge"], "+5")
        self.assertTrue(any("Korea Zinc" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Poongsan" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hyundai Steel" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round273_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_273.md")
        self.assertEqual(audit["round_id"], "round_201")
        self.assertEqual(audit["large_sector"], ROUND273_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertFalse(audit["summary"]["hard_4c_confirmed"])
        self.assertEqual(len(audit["shadow_weights"]), 8)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 8)
        self.assertIn("do_not_use_round273_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round273_r4_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round273_case_rows()
            self.assertEqual(len(records), len(ROUND273_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND273_CASE_CANDIDATES))
            self.assertIn("Korea Zinc", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("POSCO Future M", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Poongsan", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("product_spread_visibility", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Hyundai Steel", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["event_high_price_krw"], 690000.0)


if __name__ == "__main__":
    unittest.main()
