from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round218_r1_loop9_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round218_r1_loop9_industrial_infra_price_validation import (
    ROUND218_CASE_CANDIDATES,
    ROUND218_GREEN_FORBIDDEN_PATTERNS,
    ROUND218_GREEN_REQUIRED_FIELDS,
    ROUND218_HARD_4C_GATES,
    ROUND218_PRICE_VALIDATION_FIELDS,
    ROUND218_REQUIRED_TARGET_ALIASES,
    ROUND218_SHADOW_WEIGHT_ROWS,
    ROUND218_STAGE4B_WATCH_TRIGGERS,
    render_round218_green_gate_review_markdown,
    render_round218_stage4b_4c_review_markdown,
    round218_audit_payload,
    round218_case_records,
    round218_shadow_weight_rows,
    round218_summary,
    write_round218_r1_loop9_reports,
)


class Round218R1Loop9IndustrialInfraPriceValidationTests(unittest.TestCase):
    def test_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND218_REQUIRED_TARGET_ALIASES), 13)
        self.assertTrue(set(ROUND218_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND218_REQUIRED_TARGET_ALIASES["POWER_EQUIPMENT_EXPORT_US_GRID"],
            E2RArchetype.POWER_EQUIPMENT_EXPORT_US_GRID.value,
        )
        self.assertEqual(
            ROUND218_REQUIRED_TARGET_ALIASES["SHIPBUILDING_US_POLICY_MASGA"],
            E2RArchetype.SHIPBUILDING_US_POLICY_MASGA.value,
        )
        self.assertEqual(
            ROUND218_REQUIRED_TARGET_ALIASES["IPO_EVENT_PREMIUM"],
            E2RArchetype.IPO_EVENT_PREMIUM.value,
        )

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round218_case_records()
        for record in records:
            record.validate()
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round218_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["watch_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_ls_electric_is_evidence_good_but_price_failed(self) -> None:
        case = _case("r1_loop9_ls_electric_us_grid_watch")

        self.assertEqual(case.primary_archetype, E2RArchetype.POWER_EQUIPMENT_EXPORT_US_GRID)
        self.assertEqual(case.stage2_date.isoformat(), "2024-07-01")
        self.assertEqual(case.stage2_price_anchor, 208500.0)
        self.assertEqual(case.mae_1d, -5.4)
        self.assertEqual(case.extra_price_metrics["target_price"], 280000.0)
        self.assertEqual(case.extra_price_metrics["target_upside_pct"], 34.3)
        self.assertEqual(case.score_price_alignment, "evidence_good_but_price_failed")
        self.assertIsNone(case.stage3_date)

    def test_transformer_basket_is_stage2_not_green_without_company_price_path(self) -> None:
        case = _case("r1_loop9_k_transformer_bottleneck_basket")

        self.assertEqual(case.primary_archetype, E2RArchetype.TRANSFORMER_CAPACITY_BOTTLENECK)
        self.assertEqual(case.stage2_date.isoformat(), "2026-05-11")
        self.assertEqual(case.extra_price_metrics["gsu_transformer_demand_growth_pct"], 274.0)
        self.assertEqual(case.extra_price_metrics["transformer_price_increase_5y_pct"], 80.0)
        self.assertEqual(case.price_validation_status, "price_data_unavailable_after_deep_search")
        self.assertIn("sector_data_without_company_order", case.red_flag_fields)
        self.assertIsNone(case.stage3_date)

    def test_epc_and_nuclear_cases_are_stage2_watch_before_margin_and_equipment_backlog(self) -> None:
        samsung = _case("r1_loop9_samsung_ea_fadhili_epc")
        doosan = _case("r1_loop9_doosan_czech_nuclear_policy_to_contract")

        self.assertEqual(samsung.primary_archetype, E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG)
        self.assertEqual(samsung.stage2_price_anchor, 26750.0)
        self.assertEqual(samsung.mfe_1d, 8.5)
        self.assertEqual(samsung.extra_price_metrics["relative_outperformance_pp"], 9.9)
        self.assertEqual(samsung.score_price_alignment, "aligned")
        self.assertIn("epc_margin_unconfirmed", samsung.red_flag_fields)

        self.assertEqual(doosan.primary_archetype, E2RArchetype.NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG)
        self.assertEqual(doosan.reported_mfe_pct, 48.0)
        self.assertEqual(doosan.extra_price_metrics["signed_contract_value_koruna_bn"], 407.0)
        self.assertEqual(doosan.rerating_result, "policy_event_rerating")
        self.assertIn("equipment_backlog_unconfirmed", doosan.red_flag_fields)

    def test_masga_and_ipo_events_are_4b_watch_not_stage3_green(self) -> None:
        masga = _case("r1_loop9_hd_hyundai_heavy_mipo_masga_event")
        ipo = _case("r1_loop9_hd_hyundai_marine_solution_ipo_premium")

        self.assertEqual(masga.case_type, "4b_watch")
        self.assertEqual(masga.primary_archetype, E2RArchetype.SHIPBUILDING_US_POLICY_MASGA)
        self.assertEqual(masga.mfe_1d, 14.6)
        self.assertTrue(masga.extra_price_metrics["record_high_status"])
        self.assertEqual(masga.score_price_alignment, "price_moved_without_evidence")
        self.assertIsNone(masga.stage3_date)

        self.assertEqual(ipo.case_type, "overheat")
        self.assertEqual(ipo.primary_archetype, E2RArchetype.SHIP_MRO_RECURRING_PLATFORM)
        self.assertEqual(ipo.stage2_price_anchor, 83400.0)
        self.assertEqual(ipo.stage4b_price_anchor, 163900.0)
        self.assertEqual(ipo.mfe_1d, 96.5)
        self.assertEqual(ipo.extra_price_metrics["market_cap_mfe_1d_pct"], 98.5)
        self.assertIn("ipo_first_day_rally", ipo.red_flag_fields)

    def test_hanwha_ocean_is_4c_watch_not_hard_4c(self) -> None:
        case = _case("r1_loop9_hanwha_ocean_china_sanction_watch")

        self.assertEqual(case.primary_archetype, E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION)
        self.assertEqual(case.case_type, "failed_rerating")
        self.assertEqual(case.stage4c_date.isoformat(), "2025-10-14")
        self.assertEqual(case.mae_1d, -5.8)
        self.assertEqual(case.extra_price_metrics["hanwha_ocean_intraday_mae_pct"], -8.0)
        self.assertFalse(case.hard_4c_confirmed)
        self.assertIn("hard_4c_not_confirmed", case.red_flag_fields)

    def test_green_gate_and_stage4_rules_are_explicit(self) -> None:
        required = set(ROUND218_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND218_GREEN_FORBIDDEN_PATTERNS)
        green_markdown = render_round218_green_gate_review_markdown()
        stage_review = render_round218_stage4b_4c_review_markdown()

        self.assertIn("price_path_after_evidence_confirmed", required)
        self.assertIn("no_hard_redteam", required)
        self.assertIn("ipo_event_premium_only", forbidden)
        self.assertIn("policy_or_merger_event_record_high", ROUND218_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("ipo_first_day_50_to_100pct_rally", ROUND218_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("sanction_trade_restriction", ROUND218_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("r1_loop9_hanwha_ocean_china_sanction_watch", stage_review)

    def test_shadow_weights_cover_grid_epc_nuclear_shipbuilding_and_ipo(self) -> None:
        shadow_text = "\n".join(str(row) for row in round218_shadow_weight_rows())

        self.assertEqual(len(ROUND218_SHADOW_WEIGHT_ROWS), 8)
        self.assertIn("POWER_EQUIPMENT_EXPORT_US_GRID", shadow_text)
        self.assertIn("TRANSFORMER_CAPACITY_BOTTLENECK", shadow_text)
        self.assertIn("OVERSEAS_EPC_CONTRACT_BACKLOG", shadow_text)
        self.assertIn("NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG", shadow_text)
        self.assertIn("SHIPBUILDING_US_POLICY_MASGA", shadow_text)
        self.assertIn("IPO_EVENT_PREMIUM", shadow_text)

    def test_price_validation_fields_include_reported_anchor_fields(self) -> None:
        fields = set(ROUND218_PRICE_VALIDATION_FIELDS)

        self.assertIn("target_upside_pct", fields)
        self.assertIn("relative_outperformance_pp", fields)
        self.assertIn("ipo_first_day_return_pct", fields)
        self.assertIn("policy_contract_value", fields)
        self.assertIn("price_validation_status", fields)

    def test_summary_and_audit_payload_are_calibration_only(self) -> None:
        audit = round218_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_218.md")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round218_cases_as_candidate_generation_input", audit["what_not_to_change"])
        self.assertIn("do_not_lower_stage3_green_thresholds", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round218_r1_loop9_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND218_CASE_CANDIDATES))
            self.assertIn("LS ELECTRIC", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("confirmed_contract_amount", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("IPO_EVENT_PREMIUM", paths["shadow_weights"].read_text(encoding="utf-8"))


def _case(case_id: str):
    return next(case for case in ROUND218_CASE_CANDIDATES if case.case_id == case_id)


if __name__ == "__main__":
    unittest.main()
