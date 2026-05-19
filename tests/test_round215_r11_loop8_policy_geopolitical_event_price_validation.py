from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round215_r11_loop8_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round215_r11_loop8_policy_geopolitical_event_price_validation import (
    ROUND215_CASE_CANDIDATES,
    ROUND215_DEFAULT_STAGE3_BIAS,
    ROUND215_GREEN_FORBIDDEN_PATTERNS,
    ROUND215_GREEN_REQUIRED_FIELDS,
    ROUND215_HARD_4C_GATES,
    ROUND215_PRICE_VALIDATION_FIELDS,
    ROUND215_REQUIRED_TARGET_ALIASES,
    ROUND215_SCORE_ADJUSTMENTS,
    ROUND215_STAGE4B_WATCH_TRIGGERS,
    render_round215_green_gate_review_markdown,
    render_round215_stage4b_4c_review_markdown,
    round215_audit_payload,
    round215_case_records,
    round215_case_rows,
    round215_summary,
    write_round215_r11_loop8_reports,
)


class Round215R11Loop8PolicyGeopoliticalEventPriceValidationTests(unittest.TestCase):
    def test_round215_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND215_REQUIRED_TARGET_ALIASES), 13)
        self.assertTrue(set(ROUND215_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND215_REQUIRED_TARGET_ALIASES["DOMESTIC_RESOURCE_DISCOVERY_EVENT"],
            E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT.value,
        )
        self.assertEqual(
            ROUND215_REQUIRED_TARGET_ALIASES["NUCLEAR_POLICY_TO_CONTRACT"],
            E2RArchetype.NUCLEAR_POLICY_TO_CONTRACT.value,
        )
        self.assertEqual(
            ROUND215_REQUIRED_TARGET_ALIASES["US_SHIPBUILDING_REBUILD_POLICY"],
            E2RArchetype.US_SHIPBUILDING_REBUILD_POLICY.value,
        )

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round215_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("r11_default_stage3_bias_very_conservative", record.green_guardrails)

        summary = round215_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["r11_default_stage3_bias"], ROUND215_DEFAULT_STAGE3_BIAS)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_resource_event_is_price_moved_without_evidence(self) -> None:
        by_id = {case.case_id: case for case in ROUND215_CASE_CANDIDATES}
        kogas = by_id["r11_loop8_kogas_east_sea_resource_event"]

        self.assertEqual(kogas.primary_archetype, E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT)
        self.assertEqual(kogas.stage1_date.isoformat(), "2024-06-03")
        self.assertEqual(kogas.stage4b_date.isoformat(), "2024-06-03")
        self.assertIsNone(kogas.stage3_date)
        self.assertEqual(kogas.stage1_price_anchor, 38700.0)
        self.assertEqual(kogas.mfe_1d, 30.0)
        self.assertEqual(kogas.extra_price_metrics["implied_pre_event_reference_price_krw"], 29769.0)
        self.assertEqual(kogas.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("resource_estimate_without_drilling", kogas.red_flag_fields)

    def test_nuclear_and_shipbuilding_policy_are_stage2_until_order_margin_revenue(self) -> None:
        by_id = {case.case_id: case for case in ROUND215_CASE_CANDIDATES}
        doosan = by_id["r11_loop8_doosan_nuclear_policy_to_contract"]
        hd = by_id["r11_loop8_hd_hyundai_masga_shipbuilding_event"]

        self.assertEqual(doosan.primary_archetype, E2RArchetype.NUCLEAR_POLICY_TO_CONTRACT)
        self.assertEqual(doosan.stage2_date.isoformat(), "2025-06-04")
        self.assertEqual(doosan.stage4c_date.isoformat(), "2025-05-06")
        self.assertEqual(doosan.mfe_90d, 48.0)
        self.assertEqual(doosan.extra_price_metrics["signed_contract_value_koruna_bn"], 407.0)
        self.assertEqual(doosan.extra_price_metrics["contract_value_per_reactor_koruna_bn"], 203.5)
        self.assertIn("equipment_backlog_unverified", doosan.red_flag_fields)

        self.assertEqual(hd.primary_archetype, E2RArchetype.US_SHIPBUILDING_REBUILD_POLICY)
        self.assertEqual(hd.stage2_date.isoformat(), "2025-08-27")
        self.assertEqual(hd.stage4b_date.isoformat(), "2025-08-27")
        self.assertEqual(hd.extra_price_metrics["hd_hyundai_heavy_event_mfe_1d_pct"], 11.3)
        self.assertEqual(hd.extra_price_metrics["hd_hyundai_mipo_event_mfe_1d_pct"], 14.6)
        self.assertTrue(hd.extra_price_metrics["record_high_status"])
        self.assertIn("funded_order_unverified", hd.red_flag_fields)

    def test_one_off_science_and_macro_events_do_not_create_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND215_CASE_CANDIDATES}
        poultry = by_id["r11_loop8_poultry_bird_flu_import_ban_event"]
        lk99 = by_id["r11_loop8_lk99_speculative_science_break"]
        macro = by_id["r11_loop8_martial_law_macro_market_shock"]

        self.assertEqual(poultry.case_type, "event_premium")
        self.assertEqual(poultry.stage4c_date.isoformat(), "2025-06-23")
        self.assertEqual(poultry.extra_price_metrics["event_duration_days"], 35.0)
        self.assertIn("import_restriction_eased", poultry.red_flag_fields)

        self.assertEqual(lk99.case_type, "overheat")
        self.assertTrue(lk99.hard_4c_confirmed)
        self.assertEqual(lk99.stage4c_date.isoformat(), "2023-08-07")
        self.assertEqual(lk99.extra_price_metrics["claim_to_negative_replication_days"], 16.0)
        self.assertIn("independent_replication_failure", lk99.red_flag_fields)

        self.assertEqual(macro.primary_archetype, E2RArchetype.POLICY_MARKET_SHOCK_EVENT)
        self.assertEqual(macro.case_type, "failed_rerating")
        self.assertEqual(macro.mae_1d, -2.0)
        self.assertEqual(macro.extra_price_metrics["market_stabilization_fund_krw_trn"], 10.0)
        self.assertIn("political_shock", macro.red_flag_fields)

    def test_market_structure_is_stage2_overlay_not_company_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND215_CASE_CANDIDATES}
        market_structure = by_id["r11_loop8_short_selling_msci_market_structure"]

        self.assertEqual(market_structure.primary_archetype, E2RArchetype.MARKET_STRUCTURE_SHORT_SELLING_POLICY)
        self.assertEqual(market_structure.stage1_date.isoformat(), "2025-03-01")
        self.assertEqual(market_structure.stage2_date.isoformat(), "2025-06-20")
        self.assertIsNone(market_structure.stage3_date)
        self.assertEqual(market_structure.extra_price_metrics["short_selling_ban_period_years"], 5.0)
        self.assertIn("market_structure_reform_without_earnings", market_structure.red_flag_fields)

    def test_green_gate_and_4c_rules_are_explicit(self) -> None:
        required = set(ROUND215_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND215_GREEN_FORBIDDEN_PATTERNS)
        review = render_round215_green_gate_review_markdown()
        stage_review = render_round215_stage4b_4c_review_markdown()

        self.assertIn("event_escalated_to_company_contract", required)
        self.assertIn("funded_budget_or_contract_amount", required)
        self.assertIn("revenue_conversion_visible", required)
        self.assertIn("policy_news_only", forbidden)
        self.assertIn("resource_estimate_without_drilling", forbidden)
        self.assertIn("preprint_or_science_claim_only", forbidden)
        self.assertIn("independent_replication_failure", ROUND215_HARD_4C_GATES)
        self.assertIn("same_day_limit_up_or_intraday_spike", ROUND215_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("r11_loop8_lk99_speculative_science_break", stage_review)

    def test_price_validation_fields_and_score_adjustments_cover_r11_axes(self) -> None:
        fields = set(ROUND215_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND215_SCORE_ADJUSTMENTS}

        self.assertIn("event_peak_price", fields)
        self.assertIn("reported_mfe_3m_pct", fields)
        self.assertIn("validation_or_replication_status", fields)
        self.assertIn("funded_budget", axes)
        self.assertIn("actual_contract", axes)
        self.assertIn("independent_replication_or_validation", axes)
        self.assertIn("event_fade_risk", axes)

    def test_summary_and_audit_payload_keep_non_production_guardrails(self) -> None:
        audit = round215_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_215.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.POLICY_GEOPOLITICAL_EVENT.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertEqual(audit["summary"]["r11_default_stage3_bias"], "very_conservative")
        self.assertIn("do_not_use_round215_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round215_r11_loop8_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round215_case_rows()
            self.assertEqual(len(records), len(ROUND215_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND215_CASE_CANDIDATES))
            self.assertIn("한국가스공사", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("funded_budget", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("independent_replication_failure", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["event_peak_price_krw"], 38700.0)


if __name__ == "__main__":
    unittest.main()
