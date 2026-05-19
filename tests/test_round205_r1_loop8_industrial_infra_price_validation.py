from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round205_r1_loop8_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round205_r1_loop8_industrial_infra_price_validation import (
    ROUND205_CASE_CANDIDATES,
    ROUND205_GREEN_FORBIDDEN_PATTERNS,
    ROUND205_GREEN_REQUIRED_FIELDS,
    ROUND205_HARD_4C_GATES,
    ROUND205_PRICE_VALIDATION_FIELDS,
    ROUND205_REQUIRED_TARGET_ALIASES,
    ROUND205_STAGE4B_WATCH_TRIGGERS,
    render_round205_green_gate_review_markdown,
    render_round205_stage4b_4c_review_markdown,
    round205_audit_payload,
    round205_case_records,
    round205_summary,
    write_round205_r1_loop8_reports,
)


class Round205R1Loop8IndustrialInfraPriceValidationTests(unittest.TestCase):
    def test_round205_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND205_REQUIRED_TARGET_ALIASES), 11)
        self.assertTrue(set(ROUND205_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND205_REQUIRED_TARGET_ALIASES["CROWDING_4B_WATCH"],
            E2RArchetype.CROWDED_RERATING_4B_WATCH.value,
        )
        self.assertEqual(
            ROUND205_REQUIRED_TARGET_ALIASES["DEFENSE_LOCAL_PRODUCTION_PLATFORM"],
            E2RArchetype.DEFENSE_LOCAL_PRODUCTION_PLATFORM.value,
        )

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round205_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.INDUSTRIAL_ORDERS_INFRA.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)

        summary = round205_summary()
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["structural_success_count"], 2)
        self.assertEqual(summary["stage3_case_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_defense_structural_success_cases_have_reported_price_alignment(self) -> None:
        by_id = {case.case_id: case for case in ROUND205_CASE_CANDIDATES}
        rotem = by_id["r1_loop8_hyundai_rotem_k2_aligned"]
        hanwha = by_id["r1_loop8_hanwha_aerospace_mfe_4b"]

        self.assertEqual(rotem.primary_archetype, E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG)
        self.assertEqual(rotem.stage3_date.isoformat(), "2024-04-09")
        self.assertEqual(rotem.stage3_price_anchor, 41300.0)
        self.assertEqual(rotem.reported_mfe_minimum_pct, 500.0)
        self.assertEqual(rotem.score_price_alignment, "aligned")
        self.assertEqual(rotem.rerating_result, "true_rerating")

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH)
        self.assertEqual(hanwha.reported_mfe_minimum_pct, 665.3)
        self.assertEqual(hanwha.mae_1d, -13.0)
        self.assertFalse(hanwha.hard_4c_confirmed)

    def test_stage2_watch_cases_do_not_force_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND205_CASE_CANDIDATES}
        lig = by_id["r1_loop8_lig_nex1_cheongung_watch"]
        kai = by_id["r1_loop8_kai_fa50_stage2"]

        self.assertIsNone(lig.stage3_date)
        self.assertEqual(lig.stage_failure_type, "stage2_watch_success")
        self.assertEqual(lig.mfe_1d, 3.6)
        self.assertEqual(lig.reported_mfe_minimum_pct, 47.0)

        self.assertIsNone(kai.stage3_date)
        self.assertEqual(kai.reported_mfe_minimum_pct, 200.0)
        self.assertIn("margin_visibility_needed", kai.red_flag_fields)

    def test_ipo_policy_and_sanction_events_are_not_green_evidence(self) -> None:
        by_id = {case.case_id: case for case in ROUND205_CASE_CANDIDATES}
        marine = by_id["r1_loop8_hd_hyundai_marine_ipo_premium"]
        sanction = by_id["r1_loop8_hanwha_ocean_china_sanction"]
        merger = by_id["r1_loop8_hd_hyundai_heavy_mipo_merger_4b"]

        self.assertEqual(marine.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(marine.rerating_result, "event_premium")
        self.assertEqual(marine.mfe_1d, 96.5)
        self.assertIn("ipo_first_day_rally", marine.red_flag_fields)

        self.assertFalse(sanction.hard_4c_confirmed)
        self.assertEqual(sanction.mae_1d, -5.8)
        self.assertEqual(sanction.stage4c_date.isoformat(), "2025-10-14")
        self.assertEqual(sanction.rerating_result, "no_rerating")

        self.assertEqual(merger.mfe_1d, 11.3)
        self.assertEqual(merger.mfe_1d_secondary, 14.6)
        self.assertEqual(merger.rerating_result, "policy_event_rerating")
        self.assertIn("record_high_on_policy_event", merger.red_flag_fields)

    def test_green_gate_and_stage4b_4c_rules_are_explicit(self) -> None:
        required = set(ROUND205_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND205_GREEN_FORBIDDEN_PATTERNS)
        triggers = set(ROUND205_STAGE4B_WATCH_TRIGGERS)
        review = render_round205_green_gate_review_markdown()
        stage_review = render_round205_stage4b_4c_review_markdown()

        self.assertIn("actual_delivery_or_revenue_recognition_confirmed", required)
        self.assertIn("opm_or_eps_revision_confirmed", required)
        self.assertIn("ipo_first_day_rally", forbidden)
        self.assertIn("record_high_on_policy_event", forbidden)
        self.assertIn("ipo_first_day_50_to_100pct_rally", triggers)
        self.assertIn("sanction_revenue_disruption", ROUND205_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("4C-watch", stage_review)

    def test_price_validation_fields_include_reported_anchor_and_secondary_mfe(self) -> None:
        fields = set(ROUND205_PRICE_VALIDATION_FIELDS)

        self.assertIn("reported_price_anchor", fields)
        self.assertIn("reported_return_anchor", fields)
        self.assertIn("mfe_1d", fields)
        self.assertIn("mfe_1d_secondary", fields)
        self.assertIn("full_ohlc_available", fields)

    def test_summary_and_audit_payload_keep_non_production_guardrails(self) -> None:
        audit = round205_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_205.md")
        self.assertEqual(audit["large_sector"], Round10LargeSector.INDUSTRIAL_ORDERS_INFRA.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round205_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round205_r1_loop8_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND205_CASE_CANDIDATES))
            self.assertIn("order_to_revenue_conversion", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("IPO", paths["summary"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
