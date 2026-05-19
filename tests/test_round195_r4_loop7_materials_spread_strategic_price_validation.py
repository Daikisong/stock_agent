import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round195_r4_loop7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round195_r4_loop7_materials_spread_strategic_price_validation import (
    ROUND195_CASE_CANDIDATES,
    ROUND195_GREEN_FORBIDDEN_PATTERNS,
    ROUND195_GREEN_REQUIRED_FIELDS,
    ROUND195_HARD_4C_GATES,
    ROUND195_PRICE_BACKFILL_FIELDS,
    ROUND195_REQUIRED_TARGET_ALIASES,
    render_round195_green_gate_review_markdown,
    render_round195_stage4b_4c_review_markdown,
    round195_audit_payload,
    round195_case_records,
    round195_case_rows,
    round195_price_backfill_field_rows,
    round195_score_adjustment_rows,
    round195_summary,
    write_round195_r4_loop7_reports,
)


class Round195R4Loop7MaterialsSpreadPriceValidationTests(unittest.TestCase):
    def test_round195_targets_are_existing_canonical_archetypes(self):
        self.assertGreaterEqual(len(ROUND195_REQUIRED_TARGET_ALIASES), 13)
        self.assertEqual(
            ROUND195_REQUIRED_TARGET_ALIASES["POLYSILICON_NON_CHINA_SUPPLY_OPTION"],
            E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION.value,
        )
        self.assertEqual(
            ROUND195_REQUIRED_TARGET_ALIASES["EVENT_PREMIUM_GOVERNANCE_OVERLAY"],
            E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY.value,
        )
        for canonical in ROUND195_REQUIRED_TARGET_ALIASES.values():
            self.assertIsInstance(E2RArchetype(canonical), E2RArchetype)

    def test_case_records_validate_and_remain_shadow_only(self):
        records = {record.case_id: record for record in round195_case_records()}

        self.assertEqual(len(records), 7)
        self.assertEqual(records["lotte_chemical_petrochemical_loss_restructuring_watch"].case_type, "4c_thesis_break")
        self.assertEqual(records["sk_innovation_refining_margin_cyclical_success_not_structural"].case_type, "cyclical_success")
        self.assertEqual(records["posco_holdings_lithium_resource_security_cycle_watch"].case_type, "success_candidate")
        self.assertEqual(records["poongsan_copper_defense_sale_rumor_event_break"].case_type, "event_premium")
        for record in records.values():
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertEqual(record.price_validation.price_validation_status, "needs_ohlc_backfill")

    def test_petrochemical_restructuring_is_stage2_watch_not_green(self):
        rows = {row["case_id"]: row for row in round195_case_rows()}
        lotte = rows["lotte_chemical_petrochemical_loss_restructuring_watch"]
        lg_chem = rows["lg_chem_petrochemical_spread_failed_rerating_watch"]

        self.assertEqual(lotte["stage2_date"], "2025-11-26")
        self.assertEqual(lotte["stage3_date"], "")
        self.assertEqual(lotte["stage4c_date"], "2025-02-07")
        self.assertEqual(lotte["hard_4c_confirmed"], "true")
        self.assertIn("deferred_until_spread", lotte["stage3_decision"])
        self.assertEqual(lg_chem["stage2_date"], "2025-12-19")
        self.assertIn("feedstock", lg_chem["stage3_decision"])

    def test_refining_margin_success_is_cyclical_not_structural_green(self):
        rows = {row["case_id"]: row for row in round195_case_rows()}
        sk = rows["sk_innovation_refining_margin_cyclical_success_not_structural"]

        self.assertEqual(sk["case_type"], "cyclical_success")
        self.assertEqual(sk["stage2_date"], "2026-05-13")
        self.assertEqual(sk["stage3_date"], "")
        self.assertEqual(sk["rerating_result"], "cyclical_rerating")
        self.assertIn("geopolitical_margin_spike_risk", sk["red_flag_fields"])

    def test_event_premium_and_strategic_material_stage2_are_separated(self):
        rows = {row["case_id"]: row for row in round195_case_rows()}
        korea_zinc = rows["korea_zinc_governance_event_vs_critical_minerals_stage2"]
        poongsan = rows["poongsan_copper_defense_sale_rumor_event_break"]

        self.assertEqual(korea_zinc["stage1_date"], "2024-09-13")
        self.assertEqual(korea_zinc["stage2_date"], "2025-12-15")
        self.assertEqual(korea_zinc["stage3_date"], "")
        self.assertEqual(korea_zinc["rerating_result"], "event_premium")
        self.assertEqual(poongsan["stage4c_date"], "2026-04-09")
        self.assertIn("poongsan_denied_sale_plan", poongsan["red_flag_fields"])

    def test_green_gate_requires_spread_fcf_and_blocks_event_premium(self):
        required = set(ROUND195_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND195_GREEN_FORBIDDEN_PATTERNS)
        adjustments = {row["axis"]: row for row in round195_score_adjustment_rows()}
        markdown = render_round195_green_gate_review_markdown()

        self.assertIn("actual_product_spread", required)
        self.assertIn("fcf_conversion_or_cashflow_improvement", required)
        self.assertIn("capex_and_dilution_risk_passed", required)
        self.assertIn("commodity_price_spike", forbidden)
        self.assertIn("tender_offer_premium", forbidden)
        self.assertIn("unconfirmed_media_report", forbidden)
        self.assertEqual(adjustments["actual_product_spread"]["points"], "4")
        self.assertEqual(adjustments["commodity_price_up_only"]["points"], "-5")
        self.assertIn("Do not apply these weights to production scoring yet", markdown)

    def test_price_backfill_fields_include_materials_specific_inputs(self):
        fields = {row["field"] for row in round195_price_backfill_field_rows()}

        self.assertGreaterEqual(len(ROUND195_PRICE_BACKFILL_FIELDS), 45)
        for field in (
            "actual_product_spread",
            "crack_spread",
            "naphtha_ethylene_spread",
            "operating_rate",
            "capacity_shutdown_confirmed",
            "working_capital_cashflow",
            "price_floor_or_offtake",
            "tender_offer_or_governance_premium_flag",
            "hard_4c_confirmed",
        ):
            self.assertIn(field, fields)

    def test_stage4b_4c_review_contains_event_failure_and_oversupply_gates(self):
        review = render_round195_stage4b_4c_review_markdown()

        self.assertIn("china_oversupply", ROUND195_HARD_4C_GATES)
        self.assertIn("contract_sale_tender_event_failure", ROUND195_HARD_4C_GATES)
        self.assertIn("large_share_issuance_or_dilution", ROUND195_HARD_4C_GATES)
        self.assertIn("poongsan_copper_defense_sale_rumor_event_break", review)

    def test_summary_and_audit_payload_are_calibration_only(self):
        summary = round195_summary()
        payload = round195_audit_payload()

        self.assertEqual(summary["case_candidate_count"], len(ROUND195_CASE_CANDIDATES))
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertIn("do_not_use_round195_cases_as_candidate_generation_input", payload["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self):
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_round195_r4_loop7_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(records), 7)
            self.assertIn("Stage 3-Green", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_product_spread", paths["score_adjustments"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
