from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round244_r1_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round244_r1_loop11_industrial_orders_infra_price_validation import (
    ROUND244_CASE_CANDIDATES,
    ROUND244_GREEN_FORBIDDEN_PATTERNS,
    ROUND244_GREEN_REQUIRED_FIELDS,
    ROUND244_HARD_4C_GATES,
    ROUND244_LARGE_SECTOR,
    ROUND244_PRICE_VALIDATION_FIELDS,
    ROUND244_REQUIRED_TARGET_ALIASES,
    ROUND244_SCORE_ADJUSTMENTS,
    ROUND244_SHADOW_WEIGHT_ROWS,
    ROUND244_STAGE4B_WATCH_TRIGGERS,
    render_round244_green_gate_review_markdown,
    render_round244_stage4b_4c_review_markdown,
    round244_audit_payload,
    round244_case_records,
    round244_case_rows,
    round244_deep_sub_archetype_rows,
    round244_shadow_weight_rows,
    round244_summary,
    write_round244_r1_loop11_reports,
)


class Round244R1Loop11IndustrialOrdersInfraPriceValidationTests(unittest.TestCase):
    def test_round244_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND244_REQUIRED_TARGET_ALIASES), 11)
        self.assertTrue(set(ROUND244_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND244_REQUIRED_TARGET_ALIASES["NUCLEAR_EPC_EXPORT_ORDER"],
            E2RArchetype.NUCLEAR_EPC_EXPORT_ORDER.value,
        )
        self.assertEqual(
            ROUND244_REQUIRED_TARGET_ALIASES["POWER_GRID_CABLE_TRANSFORMER_EXPORT"],
            E2RArchetype.POWER_GRID_CABLE_TRANSFORMER_EXPORT.value,
        )
        self.assertEqual(
            ROUND244_REQUIRED_TARGET_ALIASES["SHIPBUILDING_CONTRACT_CANCELLATION_4C"],
            E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C.value,
        )
        self.assertEqual(
            ROUND244_REQUIRED_TARGET_ALIASES["DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH"],
            E2RArchetype.DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH.value,
        )

    def test_new_round244_archetype_definitions_are_available(self) -> None:
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_EPC_EXPORT_ORDER)
        smr = archetype_definition(E2RArchetype.NUCLEAR_SMR_POLICY_MOU)
        grid = archetype_definition(E2RArchetype.POWER_GRID_CABLE_TRANSFORMER_EXPORT)
        mro = archetype_definition(E2RArchetype.MARINE_MRO_RECURRING_SERVICE)
        cancel = archetype_definition(E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C)
        sanction = archetype_definition(E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION)

        self.assertIn("listed supplier package", nuclear.stage3_high_conviction_signals)
        self.assertIn("MOU fails to convert", smr.stage4c_thesis_break_signals)
        self.assertIn("target-price raise treated as Stage 3 while event price fails", grid.false_positive_patterns)
        self.assertIn("IPO debut premium before post-listing FCF proof", mro.stage4b_graduation_overheat_signals)
        self.assertIn("contract cancellation", cancel.stage4c_thesis_break_signals)
        self.assertIn("transaction ban", sanction.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round244_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND244_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round244_summary()
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["success_candidate_count"], 7)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["target_archetype_count"], 11)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_nuclear_and_smr_cases_are_stage2_watch_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND244_CASE_CANDIDATES}
        czech = by_id["r1_loop11_czech_nuclear_doosan_kepco_stage2"]
        smr = by_id["r1_loop11_doosan_smr_ai_power_mou"]

        self.assertEqual(czech.primary_archetype, E2RArchetype.NUCLEAR_EPC_EXPORT_ORDER)
        self.assertEqual(czech.stage2_date.isoformat(), "2025-06-04")
        self.assertIsNone(czech.stage3_date)
        self.assertEqual(czech.stage4c_date.isoformat(), "2025-05-06")
        self.assertEqual(czech.extra_price_metrics["czech_contract_value_usd_bn"], 18.7)
        self.assertEqual(czech.extra_price_metrics["doosan_3m_mfe_pct"], 48.0)
        self.assertIn("edf_legal_challenge", czech.red_flag_fields)
        self.assertEqual(czech.round_stage_failure_label, "stage2_watch_success_not_green")

        self.assertEqual(smr.primary_archetype, E2RArchetype.NUCLEAR_SMR_POLICY_MOU)
        self.assertEqual(smr.stage2_date.isoformat(), "2025-08-26")
        self.assertFalse(smr.extra_price_metrics["funded_order_confirmed"])
        self.assertFalse(smr.extra_price_metrics["confirmed_revenue"])
        self.assertIn("mou_without_funded_order", smr.red_flag_fields)
        self.assertEqual(smr.score_price_alignment, "price_moved_without_evidence")

    def test_grid_mro_and_masga_are_watch_cases_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND244_CASE_CANDIDATES}
        ls = by_id["r1_loop11_ls_grid_cable_transformer_price_failed"]
        mro = by_id["r1_loop11_hd_hyundai_marine_solution_ipo_4b"]
        masga = by_id["r1_loop11_hd_hyundai_heavy_mipo_masga_merger"]

        self.assertEqual(ls.primary_archetype, E2RArchetype.POWER_GRID_CABLE_TRANSFORMER_EXPORT)
        self.assertEqual(ls.stage2_price_anchor, 208500.0)
        self.assertEqual(ls.mae_1d, -5.4)
        self.assertEqual(ls.extra_price_metrics["ls_power_cable_contract_krw_bn"], 282.13)
        self.assertEqual(ls.extra_price_metrics["target_raise_pct"], 86.7)
        self.assertEqual(ls.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(mro.primary_archetype, E2RArchetype.MARINE_MRO_RECURRING_SERVICE)
        self.assertEqual(mro.stage4b_date.isoformat(), "2024-05-08")
        self.assertEqual(mro.stage2_price_anchor, 83400.0)
        self.assertEqual(mro.stage4b_price_anchor, 163900.0)
        self.assertEqual(mro.extra_price_metrics["first_day_close_mfe_pct"], 96.5)
        self.assertEqual(mro.round_stage_failure_label, "IPO_event_not_green")

        self.assertEqual(masga.primary_archetype, E2RArchetype.SHIPBUILDING_US_POLICY_MASGA)
        self.assertEqual(masga.stage4b_date.isoformat(), "2025-08-27")
        self.assertTrue(masga.extra_price_metrics["record_high_status"])
        self.assertEqual(masga.extra_price_metrics["hd_hyundai_mipo_event_mfe_1d_pct"], 14.6)
        self.assertEqual(masga.score_price_alignment, "price_moved_without_evidence")

    def test_contract_cancellation_dilution_rail_and_sanction_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND244_CASE_CANDIDATES}
        cancel = by_id["r1_loop11_samsung_heavy_zvezda_contract_cancellation"]
        aero = by_id["r1_loop11_hanwha_aerospace_poland_jv_dilution_watch"]
        rail = by_id["r1_loop11_hyundai_rotem_morocco_rail_order"]
        ocean = by_id["r1_loop11_hanwha_ocean_china_sanction_watch"]

        self.assertEqual(cancel.primary_archetype, E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C)
        self.assertTrue(cancel.hard_4c_confirmed)
        self.assertEqual(cancel.stage4c_date.isoformat(), "2025-06-18")
        self.assertEqual(cancel.extra_price_metrics["cancelled_contract_value_usd_bn"], 3.54)
        self.assertEqual(cancel.extra_price_metrics["icebreaker_lng_carriers"], 10.0)
        self.assertIn("contract_cancellation", cancel.red_flag_fields)

        self.assertEqual(aero.primary_archetype, E2RArchetype.DEFENSE_LOCAL_PRODUCTION_DILUTION_WATCH)
        self.assertEqual(aero.mae_1d, -13.0)
        self.assertEqual(aero.extra_price_metrics["op_growth_vs_2024_guidance_pct"], 73.4)
        self.assertIn("dilution_after_rerating", aero.red_flag_fields)

        self.assertEqual(rail.primary_archetype, E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY)
        self.assertEqual(rail.stage2_date.isoformat(), "2025-02-26")
        self.assertEqual(rail.extra_price_metrics["hyundai_rotem_order_usd_bn"], 1.54)
        self.assertEqual(rail.extra_price_metrics["hyundai_order_share_of_total_program_pct"], 53.1)
        self.assertEqual(rail.round_stage_failure_label, "stage2_watch_success")

        self.assertEqual(ocean.primary_archetype, E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION)
        self.assertEqual(ocean.stage4c_date.isoformat(), "2025-10-14")
        self.assertFalse(ocean.hard_4c_confirmed)
        self.assertEqual(ocean.mae_1d, -5.8)
        self.assertEqual(ocean.round_stage_failure_label, "4C_watch_not_hard_4C")
        self.assertIn("actual_revenue_module_contract_disruption_unconfirmed", ocean.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND244_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND244_GREEN_FORBIDDEN_PATTERNS)
        review = render_round244_green_gate_review_markdown()
        stage_review = render_round244_stage4b_4c_review_markdown()
        fields = set(ROUND244_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND244_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round244_shadow_weight_rows()}
        deep_rows = round244_deep_sub_archetype_rows()

        self.assertIn("actual_delivery_or_revenue_recognition", required)
        self.assertIn("working_capital_cash_collection_stable", required)
        self.assertIn("mou_without_funded_order", forbidden)
        self.assertIn("ipo_first_day_surge_only", forbidden)
        self.assertIn("preferred_bidder_period_plus_40_to_50pct", ROUND244_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("contract_cancellation", ROUND244_HARD_4C_GATES)
        self.assertIn("legal_or_sanction_anchor", fields)
        self.assertIn("cash_collection_quality", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("4C-watch is not hard 4C", stage_review)
        self.assertEqual(len(ROUND244_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["NUCLEAR_EPC_EXPORT_ORDER"]["signed_contract"], "+5")
        self.assertEqual(shadow_rows["NUCLEAR_SMR_POLICY_MOU"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["SHIPBUILDING_CONTRACT_CANCELLATION_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Czech Dukovany" in row["terms"] for row in deep_rows))
        self.assertTrue(any("HD Hyundai Marine Solution" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hanwha Ocean" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round244_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_244.md")
        self.assertEqual(audit["round_id"], "round_172")
        self.assertEqual(audit["large_sector"], ROUND244_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round244_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round244_r1_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round244_case_rows()
            self.assertEqual(len(records), len(ROUND244_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND244_CASE_CANDIDATES))
            self.assertIn("Czech nuclear", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("mou_without_funded_order", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("SHIPBUILDING_CONTRACT_CANCELLATION_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Hanwha Ocean", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[2]["extra_price_metrics"])["target_raise_pct"], 86.7)


if __name__ == "__main__":
    unittest.main()
