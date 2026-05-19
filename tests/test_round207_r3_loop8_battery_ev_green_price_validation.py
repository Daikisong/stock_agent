from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round207_r3_loop8_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round207_r3_loop8_battery_ev_green_price_validation import (
    ROUND207_CASE_CANDIDATES,
    ROUND207_GREEN_FORBIDDEN_PATTERNS,
    ROUND207_GREEN_REQUIRED_FIELDS,
    ROUND207_HARD_4C_GATES,
    ROUND207_PRICE_VALIDATION_FIELDS,
    ROUND207_REQUIRED_TARGET_ALIASES,
    ROUND207_SCORE_ADJUSTMENTS,
    ROUND207_STAGE4B_WATCH_TRIGGERS,
    render_round207_green_gate_review_markdown,
    render_round207_stage4b_4c_review_markdown,
    round207_audit_payload,
    round207_case_records,
    round207_case_rows,
    round207_summary,
    write_round207_r3_loop8_reports,
)


class Round207R3Loop8BatteryEVGreenPriceValidationTests(unittest.TestCase):
    def test_round207_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND207_REQUIRED_TARGET_ALIASES), 13)
        self.assertTrue(set(ROUND207_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND207_REQUIRED_TARGET_ALIASES["PRECURSOR_SUPPLY_CHAIN"],
            E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT.value,
        )
        self.assertEqual(
            ROUND207_REQUIRED_TARGET_ALIASES["LEVERAGE_FCF_BREAKDOWN"],
            E2RArchetype.LEVERAGE_FCF_BREAKDOWN.value,
        )

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round207_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.BATTERY_EV_GREEN.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round207_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["event_premium_or_overheat_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_lges_and_samsung_sdi_are_stage2_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND207_CASE_CANDIDATES}
        lges = by_id["r3_loop8_lges_ess_pivot_contract_break"]
        sdi = by_id["r3_loop8_samsung_sdi_ess_lfp_stage2"]

        self.assertEqual(lges.primary_archetype, E2RArchetype.ESS_LFP_GRID_STORAGE)
        self.assertEqual(lges.stage2_date.isoformat(), "2025-07-30")
        self.assertIsNone(lges.stage3_date)
        self.assertEqual(lges.stage4c_date.isoformat(), "2025-12-18")
        self.assertEqual(lges.mae_1d_secondary, -7.6)
        self.assertEqual(lges.extra_price_metrics["lost_revenue_vs_2024_revenue_pct"], 52.7)
        self.assertTrue(lges.hard_4c_confirmed)

        self.assertEqual(sdi.stage2_date.isoformat(), "2025-12-10")
        self.assertIsNone(sdi.stage3_date)
        self.assertEqual(sdi.mfe_1d, 6.1)
        self.assertEqual(sdi.extra_price_metrics["offering_price_reduction_pct"], -13.6)
        self.assertFalse(sdi.hard_4c_confirmed)

    def test_lnf_contract_value_collapse_is_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND207_CASE_CANDIDATES}
        lnf = by_id["r3_loop8_lnf_tesla_contract_collapse"]

        self.assertEqual(lnf.primary_archetype, E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C)
        self.assertEqual(lnf.case_type, "4c_thesis_break")
        self.assertTrue(lnf.hard_4c_confirmed)
        self.assertEqual(lnf.stage4c_date.isoformat(), "2025-12-29")
        self.assertAlmostEqual(float(lnf.extra_price_metrics["contract_value_drawdown_pct"]), -99.999745, places=6)
        self.assertIn("contract_value_collapse", lnf.red_flag_fields)

    def test_sk_on_and_skiet_are_failed_rerating_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND207_CASE_CANDIDATES}
        sk = by_id["r3_loop8_sk_innovation_skon_failed_rerating"]
        skiet = by_id["r3_loop8_skiet_separator_demand_break"]

        self.assertEqual(sk.case_type, "failed_rerating")
        self.assertEqual(sk.rerating_result, "credit_relief_rally")
        self.assertEqual(sk.extra_price_metrics["net_debt_increase_pct"], 437.9)
        self.assertTrue(sk.hard_4c_confirmed)
        self.assertIn("negative_fcf_or_debt_burden", {item.axis for item in ROUND207_SCORE_ADJUSTMENTS})

        self.assertEqual(skiet.primary_archetype, E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE)
        self.assertEqual(skiet.extra_price_metrics["sk_on_loss_worsening_pct"], 1684.9)
        self.assertFalse(skiet.hard_4c_confirmed)
        self.assertIn("sale_consideration", skiet.red_flag_fields)

    def test_posco_future_m_and_ecopro_materials_stay_event_or_overheat(self) -> None:
        by_id = {case.case_id: case for case in ROUND207_CASE_CANDIDATES}
        posco = by_id["r3_loop8_posco_future_m_lithium_event"]
        ecopro = by_id["r3_loop8_ecopro_materials_precursor_overheat"]

        self.assertEqual(posco.case_type, "event_premium")
        self.assertEqual(posco.mfe_1d, 8.3)
        self.assertEqual(posco.mae_1d, -8.2)
        self.assertEqual(posco.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(ecopro.case_type, "overheat")
        self.assertEqual(ecopro.mae_1d, -11.0)
        self.assertEqual(ecopro.stage4c_price_anchor, 119200.0)
        self.assertEqual(ecopro.rerating_result, "theme_overheat")

    def test_green_gate_and_4c_rules_are_explicit(self) -> None:
        required = set(ROUND207_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND207_GREEN_FORBIDDEN_PATTERNS)
        review = render_round207_green_gate_review_markdown()
        stage_review = render_round207_stage4b_4c_review_markdown()

        self.assertIn("actual_calloff", required)
        self.assertIn("fcf_after_capex", required)
        self.assertIn("subsidy_excluded_profit_quality", required)
        self.assertIn("customer_name_only", forbidden)
        self.assertIn("lithium_price_event_only", forbidden)
        self.assertIn("contract_value_collapse", ROUND207_HARD_4C_GATES)
        self.assertIn("ampc_included_earnings_surprise_only", ROUND207_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("contract_value_collapse", stage_review)

    def test_price_validation_fields_include_contract_and_debt_metrics(self) -> None:
        fields = set(ROUND207_PRICE_VALIDATION_FIELDS)

        self.assertIn("contract_value_drawdown_pct", fields)
        self.assertIn("lost_revenue_vs_prior_revenue_pct", fields)
        self.assertIn("net_debt_increase_pct", fields)
        self.assertIn("loss_worsening_pct", fields)
        self.assertIn("full_ohlc_available", fields)

    def test_summary_and_audit_payload_keep_non_production_guardrails(self) -> None:
        audit = round207_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_207.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.BATTERY_EV_GREEN.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round207_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round207_r3_loop8_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round207_case_rows()
            self.assertEqual(len(records), len(ROUND207_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND207_CASE_CANDIDATES))
            self.assertIn("binding_contract_quality", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("LG에너지솔루션", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("contract_value_drawdown_pct", paths["price_validation_fields"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["contract_value_revised_usd"], 7386.0)


if __name__ == "__main__":
    unittest.main()
