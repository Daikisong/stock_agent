from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round206_r2_loop8_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round206_r2_loop8_ai_semiconductor_price_validation import (
    ROUND206_CASE_CANDIDATES,
    ROUND206_GREEN_FORBIDDEN_PATTERNS,
    ROUND206_GREEN_REQUIRED_FIELDS,
    ROUND206_HARD_4C_GATES,
    ROUND206_PRICE_VALIDATION_FIELDS,
    ROUND206_REQUIRED_TARGET_ALIASES,
    ROUND206_STAGE4B_WATCH_TRIGGERS,
    render_round206_green_gate_review_markdown,
    render_round206_stage4b_4c_review_markdown,
    round206_audit_payload,
    round206_case_records,
    round206_summary,
    write_round206_r2_loop8_reports,
)


class Round206R2Loop8AISemiconductorPriceValidationTests(unittest.TestCase):
    def test_round206_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND206_REQUIRED_TARGET_ALIASES), 14)
        self.assertTrue(set(ROUND206_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND206_REQUIRED_TARGET_ALIASES["GEOPOLITICAL_EXPORT_CONTROL_OVERLAY"],
            E2RArchetype.IP_LEAK_SUPPLY_CHAIN_REDTEAM.value,
        )
        self.assertEqual(
            ROUND206_REQUIRED_TARGET_ALIASES["AI_CAPEX_CROWDING_OVERLAY"],
            E2RArchetype.AI_CAPEX_CROWDING_OVERLAY.value,
        )

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round206_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round206_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["structural_success_count"], 2)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_sk_hynix_hbm_case_has_large_mfe_and_4b_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND206_CASE_CANDIDATES}
        hynix = by_id["r2_loop8_sk_hynix_hbm_aligned_4b"]

        self.assertEqual(hynix.primary_archetype, E2RArchetype.MEMORY_HBM_CAPACITY)
        self.assertEqual(hynix.stage3_date.isoformat(), "2024-06-25")
        self.assertEqual(hynix.stage3_price_anchor, 222000.0)
        self.assertEqual(hynix.peak_price_anchor, 1946000.0)
        self.assertEqual(hynix.reported_mfe_minimum_pct, 776.6)
        self.assertEqual(hynix.reported_market_cap_mfe_minimum_pct, 842.0)
        self.assertEqual(hynix.reported_compounded_return_minimum_pct, 1022.0)
        self.assertEqual(hynix.stage4b_status, "elevated")

    def test_hanmi_splits_confirmed_order_from_unconfirmed_customer_report(self) -> None:
        by_id = {case.case_id: case for case in ROUND206_CASE_CANDIDATES}
        hanmi = by_id["r2_loop8_hanmi_semiconductor_hbm_bonder_4b"]

        self.assertEqual(hanmi.primary_archetype, E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA)
        self.assertEqual(hanmi.mfe_1d, 16.0)
        self.assertEqual(hanmi.mfe_1d_secondary, 22.0)
        self.assertEqual(hanmi.stage4b_price_anchor, 139100.0)
        self.assertIn("unconfirmed_micron_media_report", hanmi.red_flag_fields)
        self.assertIn(E2RArchetype.DISCLOSURE_CONFIDENCE_CAP, hanmi.secondary_archetypes)

    def test_samsung_gaonchips_and_db_hitek_are_not_forced_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND206_CASE_CANDIDATES}
        samsung = by_id["r2_loop8_samsung_memory_recovery_hbm_watch"]
        gaon = by_id["r2_loop8_gaonchips_pfn_design_win"]
        db = by_id["r2_loop8_db_hitek_policy_foundry"]

        self.assertIsNone(samsung.stage3_date)
        self.assertEqual(samsung.case_type, "success_candidate")
        self.assertEqual(samsung.rerating_result, "cyclical_rerating")
        self.assertIn("hbm_lag_vs_sk_hynix", samsung.red_flag_fields)

        self.assertIsNone(gaon.stage3_date)
        self.assertEqual(gaon.score_price_alignment, "unknown")
        self.assertIn("design_win_without_revenue", gaon.red_flag_fields)

        self.assertEqual(db.case_type, "event_premium")
        self.assertEqual(db.rerating_result, "policy_event_rerating")
        self.assertIn("policy_foundry_without_order", db.red_flag_fields)

    def test_export_control_and_openai_events_are_watch_overlays_not_hard_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND206_CASE_CANDIDATES}
        export = by_id["r2_loop8_hana_micron_hanmi_export_control_watch"]
        openai = by_id["r2_loop8_openai_stargate_memory_4b"]

        self.assertEqual(export.primary_archetype, E2RArchetype.IP_LEAK_SUPPLY_CHAIN_REDTEAM)
        self.assertEqual(export.case_type, "4b_watch")
        self.assertFalse(export.hard_4c_confirmed)
        self.assertEqual(export.mae_1d, -1.7)
        self.assertEqual(export.mae_1d_secondary, -4.4)
        self.assertEqual(export.stage4c_date.isoformat(), "2025-09-01")

        self.assertEqual(openai.primary_archetype, E2RArchetype.AI_CAPEX_CROWDING_OVERLAY)
        self.assertEqual(openai.case_type, "4b_watch")
        self.assertEqual(openai.mfe_1d, 12.0)
        self.assertEqual(openai.mfe_1d_secondary, 3.5)
        self.assertEqual(openai.stage4b_status, "watch")

    def test_green_gate_and_stage4b_4c_rules_are_explicit(self) -> None:
        required = set(ROUND206_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND206_GREEN_FORBIDDEN_PATTERNS)
        triggers = set(ROUND206_STAGE4B_WATCH_TRIGGERS)
        review = render_round206_green_gate_review_markdown()
        stage_review = render_round206_stage4b_4c_review_markdown()

        self.assertIn("product_specific_exposure", required)
        self.assertIn("eps_fcf_revision_confirmed", required)
        self.assertIn("unconfirmed_customer_media_report", forbidden)
        self.assertIn("design_win_without_revenue", forbidden)
        self.assertIn("market_cap_milestone_headline", triggers)
        self.assertIn("china_fab_export_control_disruption", ROUND206_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("4C-watch", stage_review)

    def test_price_validation_fields_include_market_cap_and_compounded_return(self) -> None:
        fields = set(ROUND206_PRICE_VALIDATION_FIELDS)

        self.assertIn("reported_price_anchor", fields)
        self.assertIn("reported_market_cap_mfe_minimum_pct", fields)
        self.assertIn("reported_compounded_return_minimum_pct", fields)
        self.assertIn("mfe_1d_secondary", fields)
        self.assertIn("full_ohlc_available", fields)

    def test_summary_and_audit_payload_keep_non_production_guardrails(self) -> None:
        audit = round206_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_206.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round206_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round206_r2_loop8_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND206_CASE_CANDIDATES))
            self.assertIn("capacity_bottleneck", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("SK하이닉스", paths["summary"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
