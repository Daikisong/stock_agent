from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round271_r2_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round271_r2_loop13_ai_semiconductor_electronics_price_validation import (
    ROUND271_CASE_CANDIDATES,
    ROUND271_GREEN_FORBIDDEN_PATTERNS,
    ROUND271_GREEN_REQUIRED_FIELDS,
    ROUND271_HARD_4C_GATES,
    ROUND271_LARGE_SECTOR,
    ROUND271_PRICE_VALIDATION_FIELDS,
    ROUND271_REQUIRED_TARGET_ALIASES,
    ROUND271_SCORE_ADJUSTMENTS,
    ROUND271_SHADOW_WEIGHT_ROWS,
    ROUND271_STAGE4B_WATCH_TRIGGERS,
    render_round271_green_gate_review_markdown,
    render_round271_stage4b_4c_review_markdown,
    round271_audit_payload,
    round271_case_records,
    round271_case_rows,
    round271_deep_sub_archetype_rows,
    round271_shadow_weight_rows,
    round271_summary,
    write_round271_r2_loop13_reports,
)


class Round271R2Loop13AISemiconductorElectronicsPriceValidationTests(unittest.TestCase):
    def test_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND271_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND271_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND271_REQUIRED_TARGET_ALIASES["HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B"],
            E2RArchetype.HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B.value,
        )
        self.assertEqual(
            ROUND271_REQUIRED_TARGET_ALIASES["SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C"],
            E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C.value,
        )
        self.assertEqual(
            ROUND271_REQUIRED_TARGET_ALIASES["CHINA_FAB_EXPORT_CONTROL_4C_WATCH"],
            E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH.value,
        )

    def test_archetype_definitions_encode_r2_loop13_gates(self) -> None:
        hynix = archetype_definition(E2RArchetype.HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B)
        samsung = archetype_definition(E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C)
        carveout = archetype_definition(E2RArchetype.HBM_EQUIPMENT_CARVEOUT_NOT_GREEN)
        ai_chip = archetype_definition(E2RArchetype.AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2)
        ipo = archetype_definition(E2RArchetype.SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT)
        policy = archetype_definition(E2RArchetype.STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN)
        blackwell = archetype_definition(E2RArchetype.NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2)
        china = archetype_definition(E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH)

        self.assertIn("HBM volume, customer qualification, OP revision, margin and price path align", hynix.stage3_high_conviction_signals)
        self.assertIn("labor strike", samsung.stage4c_thesis_break_signals)
        self.assertIn("actual HBM equipment orders", carveout.stage3_high_conviction_signals)
        self.assertIn("unlisted AI chip merger treated as listed-stock EPS", ai_chip.false_positive_patterns)
        self.assertIn("100x-600x oversubscription", ipo.stage4b_graduation_overheat_signals)
        self.assertIn("operator, customer contracts, utilization, margin and capex ROI confirmed", policy.stage3_high_conviction_signals)
        self.assertIn("buying Nvidia chips treated as Korean listed-company EPS", blackwell.false_positive_patterns)
        self.assertIn("not a Green source; China fab exposure must clear for affected names", china.stage3_high_conviction_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round271_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND271_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_invent_price_or_stage_dates", record.green_guardrails)

        summary = round271_summary()
        self.assertEqual(summary["round_id"], "round_199")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 2)
        self.assertEqual(summary["price_data_unavailable_count"], 1)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertEqual(summary["aligned_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["hard_4c_confirmed"])

    def test_hbm_success_samsung_watch_and_carveout_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND271_CASE_CANDIDATES}
        hynix = by_id["r2_loop13_sk_hynix_hbm_success_now_4b"]
        samsung = by_id["r2_loop13_samsung_hbm_lag_labor_4c_watch"]
        hanwha = by_id["r2_loop13_hanwha_precision_hbm_equipment_carveout"]

        self.assertEqual(hynix.primary_archetype, E2RArchetype.HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B)
        self.assertEqual(hynix.stage3_date.isoformat(), "2024-07-24")
        self.assertEqual(hynix.extra_price_metrics["q2_2024_op_krw_trn"], 5.47)
        self.assertEqual(hynix.extra_price_metrics["reported_return_2025_pct"], 274.0)
        self.assertEqual(hynix.extra_price_metrics["market_cap_2026_may_usd_bn"], 942.0)
        self.assertEqual(hynix.peak_return_from_stage3_pct, 842.0)
        self.assertEqual(hynix.score_price_alignment, "aligned")

        self.assertEqual(samsung.primary_archetype, E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C)
        self.assertEqual(samsung.extra_price_metrics["q2_2024_op_growth_multiple"], 15.52)
        self.assertEqual(samsung.extra_price_metrics["q2_2025_op_decline_pct"], -55.0)
        self.assertEqual(samsung.extra_price_metrics["chip_division_profit_decline_pct"], -93.8)
        self.assertEqual(samsung.extra_price_metrics["strike_duration_days"], 18.0)
        self.assertIn("labor_strike_unresolved", samsung.red_flag_fields)

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.HBM_EQUIPMENT_CARVEOUT_NOT_GREEN)
        self.assertEqual(hanwha.event_mfe_pct, 15.0)
        self.assertEqual(hanwha.event_mae_pct, -8.0)
        self.assertTrue(hanwha.extra_price_metrics["hbm_equipment_development_confirmed"])
        self.assertFalse(hanwha.extra_price_metrics["actual_hbm_equipment_order_revenue_confirmed"])
        self.assertEqual(hanwha.score_price_alignment, "price_moved_without_evidence")

    def test_ai_chip_ipo_foundry_blackwell_and_china_cases_do_not_force_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND271_CASE_CANDIDATES}
        reb = by_id["r2_loop13_rebellions_sapeon_ai_chip_merger"]
        tera = by_id["r2_loop13_teraview_kosdaq_semiconductor_inspection_ipo"]
        foundry = by_id["r2_loop13_korea_state_foundry_policy"]
        blackwell = by_id["r2_loop13_nvidia_blackwell_korea_ai_infra"]
        china = by_id["r2_loop13_china_fab_export_control_basket"]

        self.assertEqual(reb.primary_archetype, E2RArchetype.AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2)
        self.assertEqual(reb.extra_price_metrics["total_funding_rebellions_usd_mn"], 225.0)
        self.assertIn("unlisted_merger_only", reb.red_flag_fields)

        self.assertEqual(tera.primary_archetype, E2RArchetype.SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT)
        self.assertEqual(tera.extra_price_metrics["oversubscription_multiple"], 600.0)
        self.assertEqual(tera.stage2_price_anchor, 8000.0)
        self.assertEqual(tera.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(foundry.primary_archetype, E2RArchetype.STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN)
        self.assertEqual(foundry.extra_price_metrics["proposed_foundry_investment_krw_trn"], 4.5)
        self.assertFalse(foundry.extra_price_metrics["operator_confirmed"])
        self.assertIn("foundry_policy_only", foundry.red_flag_fields)

        self.assertEqual(blackwell.primary_archetype, E2RArchetype.NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2)
        self.assertEqual(blackwell.extra_price_metrics["total_blackwell_chips_to_korea"], 260000.0)
        self.assertFalse(blackwell.extra_price_metrics["direct_supplier_revenue_to_korean_listed_companies"])
        self.assertEqual(blackwell.price_validation_status, "price_data_unavailable_after_deep_search")

        self.assertEqual(china.primary_archetype, E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH)
        self.assertEqual(china.stage4c_date.isoformat(), "2025-09-01")
        self.assertFalse(china.hard_4c_confirmed)
        self.assertEqual(china.event_mae_pct, -4.4)
        self.assertEqual(china.extra_price_metrics["sk_hynix_relative_underperformance_pp"], -3.7)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND271_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND271_GREEN_FORBIDDEN_PATTERNS)
        review = render_round271_green_gate_review_markdown()
        stage_review = render_round271_stage4b_4c_review_markdown()
        fields = set(ROUND271_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND271_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round271_shadow_weight_rows()}
        deep_rows = round271_deep_sub_archetype_rows()

        self.assertIn("customer_qualification_confirmed", required)
        self.assertIn("china_fab_export_control_risk_passed", required)
        self.assertIn("labor_production_disruption_risk_passed", required)
        self.assertIn("ai_keyword_only", forbidden)
        self.assertIn("blackwell_chip_consumption_only", forbidden)
        self.assertIn("labor_strike_unresolved", forbidden)
        self.assertIn("HBM_volume_certification", axes)
        self.assertIn("China_fab_exposure", axes)
        self.assertIn("event_mae_pct", fields)
        self.assertIn("ipo_oversubscription_100x_to_600x", ROUND271_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("china_fab_equipment_license_denial", ROUND271_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("hard 4C", stage_review)
        self.assertEqual(len(ROUND271_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B"]["4b_watch_sensitivity"], "+5")
        self.assertEqual(shadow_rows["SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CHINA_FAB_EXPORT_CONTROL_4C_WATCH"]["china_fab_export_control_clearance"], "+5")
        self.assertTrue(any("SK Hynix" in row["terms"] for row in deep_rows))
        self.assertTrue(any("TeraView" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Nvidia Blackwell" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round271_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_271.md")
        self.assertEqual(audit["round_id"], "round_199")
        self.assertEqual(audit["large_sector"], ROUND271_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertFalse(audit["summary"]["hard_4c_confirmed"])
        self.assertEqual(len(audit["shadow_weights"]), 8)
        self.assertEqual(len(audit["deep_sub_archetypes"]), 8)
        self.assertIn("do_not_use_round271_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round271_r2_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round271_case_rows()
            self.assertEqual(len(records), len(ROUND271_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND271_CASE_CANDIDATES))
            self.assertIn("SK Hynix", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Samsung Electronics", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Nvidia Blackwell", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("HBM_volume_certification", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("CHINA_FAB_EXPORT_CONTROL_4C_WATCH", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("Rebellions", paths["deep_sub_archetypes"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["market_cap_2026_may_usd_bn"], 942.0)


if __name__ == "__main__":
    unittest.main()
