from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round227_r10_loop9_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round227_r10_loop9_construction_real_estate_materials_price_validation import (
    ROUND227_CASE_CANDIDATES,
    ROUND227_GREEN_FORBIDDEN_PATTERNS,
    ROUND227_GREEN_REQUIRED_FIELDS,
    ROUND227_HARD_4C_GATES,
    ROUND227_PRICE_VALIDATION_FIELDS,
    ROUND227_REQUIRED_TARGET_ALIASES,
    ROUND227_SCORE_ADJUSTMENTS,
    ROUND227_SHADOW_WEIGHT_ROWS,
    ROUND227_STAGE4B_WATCH_TRIGGERS,
    render_round227_green_gate_review_markdown,
    render_round227_stage4b_4c_review_markdown,
    round227_audit_payload,
    round227_case_records,
    round227_case_rows,
    round227_summary,
    write_round227_r10_loop9_reports,
)


class Round227R10Loop9ConstructionRealEstateMaterialsPriceValidationTests(unittest.TestCase):
    def test_round227_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND227_REQUIRED_TARGET_ALIASES), 14)
        self.assertTrue(set(ROUND227_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND227_REQUIRED_TARGET_ALIASES["SAUDI_GAS_INFRA_BACKLOG"],
            E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA.value,
        )
        self.assertEqual(
            ROUND227_REQUIRED_TARGET_ALIASES["HOUSING_POLICY_SUPPLY_EVENT"],
            E2RArchetype.POLICY_LOCAL_REAL_ESTATE_THEME.value,
        )
        self.assertEqual(
            ROUND227_REQUIRED_TARGET_ALIASES["REBAR_CONSTRUCTION_DEMAND_4C_WATCH"],
            E2RArchetype.BUILDING_MATERIALS_VOLUME_FAILURE.value,
        )

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round227_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round227_summary()
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_epc_and_gas_infra_cases_are_stage2_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND227_CASE_CANDIDATES}
        samsung = by_id["r10_loop9_samsung_ea_gs_fadhili_epc"]
        hyundai = by_id["r10_loop9_hyundai_ec_jafurah_gas_infra"]

        self.assertEqual(samsung.primary_archetype, E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA)
        self.assertEqual(samsung.stage2_date.isoformat(), "2024-04-03")
        self.assertEqual(samsung.stage4b_date.isoformat(), "2024-04-03")
        self.assertIsNone(samsung.stage3_date)
        self.assertEqual(samsung.stage2_price_anchor, 26750.0)
        self.assertEqual(samsung.mfe_1d, 8.5)
        self.assertEqual(samsung.extra_price_metrics["relative_outperformance_pp"], 9.9)
        self.assertIn("epc_backlog_without_margin", samsung.red_flag_fields)

        self.assertEqual(hyundai.stage2_date.isoformat(), "2024-06-30")
        self.assertIsNone(hyundai.stage3_date)
        self.assertEqual(hyundai.extra_price_metrics["main_gas_network_added_pipeline_km"], 4000.0)
        self.assertEqual(hyundai.extra_price_metrics["target_2030_vs_first_phase_pct"], 344.4)
        self.assertIn("epc_margin_unverified", hyundai.red_flag_fields)

    def test_pf_safety_and_rebar_cases_are_redteam_or_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND227_CASE_CANDIDATES}
        pf = by_id["r10_loop9_taeyoung_pf_credit_hard_4c"]
        bridge = by_id["r10_loop9_hyundai_engineering_bridge_collapse_watch"]
        safety = by_id["r10_loop9_posco_ec_dl_construction_safety_regulation"]
        rebar = by_id["r10_loop9_hyundai_steel_rebar_construction_demand_watch"]

        self.assertTrue(pf.hard_4c_confirmed)
        self.assertEqual(pf.rerating_result, "thesis_break")
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_increase_2021_to_2023_pct"], 629.7)
        self.assertIn("pf_workout_or_debt_reschedule", pf.red_flag_fields)

        self.assertTrue(bridge.hard_4c_confirmed)
        self.assertEqual(bridge.extra_price_metrics["fatalities"], 4.0)
        self.assertIn("apartment_or_bridge_collapse", bridge.red_flag_fields)

        self.assertTrue(safety.hard_4c_confirmed)
        self.assertEqual(safety.extra_price_metrics["posco_ec_sites_halted"], 103.0)
        self.assertEqual(safety.extra_price_metrics["proposed_fine_pct_of_operating_profit"], 5.0)

        self.assertEqual(rebar.primary_archetype, E2RArchetype.BUILDING_MATERIALS_CYCLE)
        self.assertEqual(rebar.stage4c_price_anchor, 29000.0)
        self.assertEqual(rebar.mae_1d, -1.2)
        self.assertEqual(rebar.extra_price_metrics["net_profit_forecast_cut_pct"], -73.0)
        self.assertIn("building_material_demand_weakness", rebar.red_flag_fields)

    def test_policy_and_data_center_are_event_premium_or_stage2_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND227_CASE_CANDIDATES}
        policy = by_id["r10_loop9_seoul_housing_supply_policy_watch"]
        data_center = by_id["r10_loop9_ai_data_center_real_asset_event"]

        self.assertEqual(policy.case_type, "event_premium")
        self.assertEqual(policy.primary_archetype, E2RArchetype.POLICY_LOCAL_REAL_ESTATE_THEME)
        self.assertEqual(policy.extra_price_metrics["ltv_reduction_relative_pct"], -20.0)
        self.assertIn("housing_supply_policy_only", policy.red_flag_fields)

        self.assertEqual(data_center.primary_archetype, E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT)
        self.assertEqual(data_center.stage4b_date.isoformat(), "2025-06-20")
        self.assertEqual(data_center.mfe_1d, 11.0)
        self.assertEqual(data_center.extra_price_metrics["capacity_expansion_potential_multiple"], 10.0)
        self.assertIn("data_center_theme_without_tenant", data_center.red_flag_fields)
        self.assertIn("asset_headline_without_noi_affo", data_center.red_flag_fields)

    def test_green_gate_4b_4c_and_shadow_weights_are_explicit(self) -> None:
        required = set(ROUND227_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND227_GREEN_FORBIDDEN_PATTERNS)
        review = render_round227_green_gate_review_markdown()
        stage_review = render_round227_stage4b_4c_review_markdown()
        weights = {row.archetype: row for row in ROUND227_SHADOW_WEIGHT_ROWS}

        self.assertIn("cash_flow_after_working_capital_confirmed", required)
        self.assertIn("margin_or_noi_affo_confirmed", required)
        self.assertIn("safety_quality_trust_passed", required)
        self.assertIn("contract_headline_only", forbidden)
        self.assertIn("data_center_theme_without_tenant", forbidden)
        self.assertIn("large_overseas_epc_award_day_rally", ROUND227_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("pf_delinquency_spike", ROUND227_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("PF workout", stage_review)
        self.assertEqual(weights[E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA].epc_margin, 5)
        self.assertEqual(weights[E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY].hard_4c_sensitivity, 5)

    def test_price_fields_and_score_axes_cover_r10_loop9(self) -> None:
        fields = set(ROUND227_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND227_SCORE_ADJUSTMENTS}

        self.assertIn("pf_credit_anchor", fields)
        self.assertIn("tenant_noi_affo_anchor", fields)
        self.assertIn("building_material_demand_anchor", fields)
        self.assertIn("cash_flow_after_working_capital", axes)
        self.assertIn("epc_margin_visibility", axes)
        self.assertIn("workplace_fatality_repeated", axes)

    def test_audit_payload_marks_non_production_round(self) -> None:
        audit = round227_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_227.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round227_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round227_r10_loop9_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round227_case_rows()
            self.assertEqual(len(records), len(ROUND227_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND227_CASE_CANDIDATES))
            self.assertIn("삼성E&A", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("cash_flow_after_working_capital", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("pf_workout_or_debt_reschedule", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["samsung_share_of_total_project_pct"], 77.9)


if __name__ == "__main__":
    unittest.main()
