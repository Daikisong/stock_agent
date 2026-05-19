from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round219_r2_loop9_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round219_r2_loop9_ai_semiconductor_price_validation import (
    ROUND219_CASE_CANDIDATES,
    ROUND219_GREEN_FORBIDDEN_PATTERNS,
    ROUND219_GREEN_REQUIRED_FIELDS,
    ROUND219_HARD_4C_GATES,
    ROUND219_PRICE_VALIDATION_FIELDS,
    ROUND219_REQUIRED_TARGET_ALIASES,
    ROUND219_SHADOW_WEIGHT_ROWS,
    ROUND219_STAGE4B_WATCH_TRIGGERS,
    render_round219_green_gate_review_markdown,
    render_round219_stage4b_4c_review_markdown,
    round219_audit_payload,
    round219_case_records,
    round219_shadow_weight_rows,
    round219_summary,
    write_round219_r2_loop9_reports,
)


class Round219R2Loop9AISemiconductorPriceValidationTests(unittest.TestCase):
    def test_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND219_REQUIRED_TARGET_ALIASES), 12)
        self.assertTrue(set(ROUND219_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND219_REQUIRED_TARGET_ALIASES["MEMORY_HBM4_FIRST_MOVER"],
            E2RArchetype.MEMORY_HBM4_FIRST_MOVER.value,
        )
        self.assertEqual(
            ROUND219_REQUIRED_TARGET_ALIASES["OPENAI_STARGATE_AI_CAPEX_EVENT"],
            E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT.value,
        )
        self.assertEqual(
            ROUND219_REQUIRED_TARGET_ALIASES["GEOPOLITICAL_EXPORT_CONTROL_OVERLAY"],
            E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY.value,
        )

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round219_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round219_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["watch_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_sk_hynix_hbm4_case_has_large_mfe_and_4b_elevated(self) -> None:
        case = _case("r2_loop9_sk_hynix_hbm4_stage3_4b")

        self.assertEqual(case.primary_archetype, E2RArchetype.MEMORY_HBM4_FIRST_MOVER)
        self.assertEqual(case.stage3_date.isoformat(), "2024-06-25")
        self.assertEqual(case.stage3_price_anchor, 222000.0)
        self.assertEqual(case.stage4b_price_anchor, 1447000.0)
        self.assertEqual(case.reported_mfe_pct, 551.8)
        self.assertEqual(case.reported_market_cap_mfe_minimum_pct, 842.0)
        self.assertEqual(case.reported_compounded_return_minimum_pct, 1022.0)
        self.assertEqual(case.stage4b_status, "elevated")
        self.assertIn(E2RArchetype.MEMORY_SUPERCYCLE_AI_CAPEX, case.secondary_archetypes)

    def test_samsung_is_stage2_watch_with_labor_4c_watch_not_green(self) -> None:
        case = _case("r2_loop9_samsung_hbm_catchup_labor_watch")

        self.assertEqual(case.primary_archetype, E2RArchetype.HBM_CATCHUP_EXECUTION)
        self.assertIn(E2RArchetype.LABOR_SUPPLY_CHAIN_4C_WATCH, case.secondary_archetypes)
        self.assertIsNone(case.stage3_date)
        self.assertEqual(case.case_type, "success_candidate")
        self.assertEqual(case.stage4c_date.isoformat(), "2026-05-15")
        self.assertEqual(case.mae_1d, -9.3)
        self.assertEqual(case.extra_price_metrics["q3_2025_op_krw_trn"], 12.2)
        self.assertIn("labor_strike_risk", case.red_flag_fields)

    def test_hanmi_splits_confirmed_order_from_unconfirmed_customer_rumor(self) -> None:
        case = _case("r2_loop9_hanmi_hbm_bonder_confirmed_vs_rumor")

        self.assertEqual(case.primary_archetype, E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA)
        self.assertEqual(case.stage4b_price_anchor, 139100.0)
        self.assertEqual(case.mfe_1d, 22.0)
        self.assertEqual(case.extra_price_metrics["confirmed_sk_hynix_contract_krw_bn"], 21.48)
        self.assertEqual(case.extra_price_metrics["relative_outperformance_pp"], 22.3)
        self.assertIn("unconfirmed_micron_media_report", case.red_flag_fields)
        self.assertIsNone(case.stage3_date)

    def test_design_win_policy_foundry_and_openai_do_not_force_green(self) -> None:
        gaon = _case("r2_loop9_gaonchips_pfn_design_win")
        db = _case("r2_loop9_db_hitek_policy_foundry")
        openai = _case("r2_loop9_openai_stargate_memory_4b")

        self.assertEqual(gaon.score_price_alignment, "unknown")
        self.assertIn("design_win_without_revenue", gaon.red_flag_fields)
        self.assertIsNone(gaon.stage3_date)

        self.assertEqual(db.case_type, "event_premium")
        self.assertEqual(db.rerating_result, "policy_event_rerating")
        self.assertIn("policy_foundry_without_order", db.red_flag_fields)

        self.assertEqual(openai.case_type, "4b_watch")
        self.assertEqual(openai.primary_archetype, E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT)
        self.assertEqual(openai.mfe_1d, 12.0)
        self.assertEqual(openai.mfe_1d_secondary, 4.7)
        self.assertIn("laggard_green_forbidden", openai.red_flag_fields)

    def test_export_control_is_4c_watch_not_hard_4c(self) -> None:
        case = _case("r2_loop9_export_control_china_fab_watch")

        self.assertEqual(case.primary_archetype, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY)
        self.assertEqual(case.case_type, "failed_rerating")
        self.assertEqual(case.stage4c_date.isoformat(), "2025-09-01")
        self.assertEqual(case.mae_1d, -4.4)
        self.assertEqual(case.mae_1d_secondary, -1.7)
        self.assertFalse(case.hard_4c_confirmed)
        self.assertIn("hard_4c_not_confirmed", case.red_flag_fields)

    def test_green_gate_and_stage4_rules_are_explicit(self) -> None:
        required = set(ROUND219_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND219_GREEN_FORBIDDEN_PATTERNS)
        green_markdown = render_round219_green_gate_review_markdown()
        stage_review = render_round219_stage4b_4c_review_markdown()

        self.assertIn("eps_fcf_revision_confirmed", required)
        self.assertIn("export_control_china_fab_labor_accounting_trust_passed", required)
        self.assertIn("design_win_without_revenue", forbidden)
        self.assertIn("policy_foundry_without_order", forbidden)
        self.assertIn("market_cap_milestone_headline", ROUND219_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("china_fab_export_control_disruption", ROUND219_HARD_4C_GATES)
        self.assertIn("labor_strike_or_production_halt", ROUND219_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("r2_loop9_export_control_china_fab_watch", stage_review)

    def test_shadow_weights_cover_ai_semiconductor_archetypes(self) -> None:
        shadow_text = "\n".join(str(row) for row in round219_shadow_weight_rows())

        self.assertEqual(len(ROUND219_SHADOW_WEIGHT_ROWS), 8)
        self.assertIn("MEMORY_HBM4_FIRST_MOVER", shadow_text)
        self.assertIn("HBM_CATCHUP_EXECUTION", shadow_text)
        self.assertIn("HBM_BONDER_EQUIPMENT_KOREA", shadow_text)
        self.assertIn("SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER", shadow_text)
        self.assertIn("POLICY_FOUNDRY_EVENT", shadow_text)
        self.assertIn("OPENAI_STARGATE_AI_CAPEX_EVENT", shadow_text)
        self.assertIn("GEOPOLITICAL_EXPORT_CONTROL_OVERLAY", shadow_text)

    def test_price_validation_fields_include_round219_anchor_fields(self) -> None:
        fields = set(ROUND219_PRICE_VALIDATION_FIELDS)

        self.assertIn("reported_market_cap_mfe_minimum_pct", fields)
        self.assertIn("reported_compounded_return_minimum_pct", fields)
        self.assertIn("hbm4_event_mfe_intraday_pct", fields)
        self.assertIn("relative_outperformance_pp", fields)
        self.assertIn("project_size_krw_trn", fields)

    def test_summary_and_audit_payload_are_calibration_only(self) -> None:
        audit = round219_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_219.md")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round219_cases_as_candidate_generation_input", audit["what_not_to_change"])
        self.assertIn("do_not_lower_stage3_green_thresholds", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round219_r2_loop9_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND219_CASE_CANDIDATES))
            self.assertIn("SK하이닉스", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("hbm4_first_mover", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("OPENAI_STARGATE_AI_CAPEX_EVENT", paths["shadow_weights"].read_text(encoding="utf-8"))


def _case(case_id: str):
    return next(case for case in ROUND219_CASE_CANDIDATES if case.case_id == case_id)


if __name__ == "__main__":
    unittest.main()
