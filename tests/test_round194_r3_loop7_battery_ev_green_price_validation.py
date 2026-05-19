import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round194_r3_loop7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round194_r3_loop7_battery_ev_green_price_validation import (
    ROUND194_CASE_CANDIDATES,
    ROUND194_GREEN_FORBIDDEN_PATTERNS,
    ROUND194_GREEN_REQUIRED_FIELDS,
    ROUND194_HARD_4C_GATES,
    ROUND194_PRICE_BACKFILL_FIELDS,
    ROUND194_REQUIRED_TARGET_ALIASES,
    ROUND194_SCORE_ADJUSTMENTS,
    render_round194_green_gate_review_markdown,
    render_round194_stage4b_4c_review_markdown,
    round194_audit_payload,
    round194_case_records,
    round194_case_rows,
    round194_price_backfill_field_rows,
    round194_score_adjustment_rows,
    round194_summary,
    write_round194_r3_loop7_reports,
)


class Round194R3Loop7BatteryEVGreenPriceValidationTests(unittest.TestCase):
    def test_round194_targets_are_existing_canonical_archetypes(self):
        self.assertGreaterEqual(len(ROUND194_REQUIRED_TARGET_ALIASES), 16)
        self.assertEqual(
            ROUND194_REQUIRED_TARGET_ALIASES["EVENT_LITHIUM_PRICE_RALLY"],
            E2RArchetype.EVENT_LITHIUM_PRICE_RALLY.value,
        )
        for canonical in ROUND194_REQUIRED_TARGET_ALIASES.values():
            self.assertIsInstance(E2RArchetype(canonical), E2RArchetype)

    def test_case_records_validate_and_remain_shadow_only(self):
        records = {record.case_id: record for record in round194_case_records()}

        self.assertEqual(len(records), 7)
        self.assertEqual(
            records["lg_energy_solution_ess_lfp_stage2_ev_contract_4c_watch"].case_type,
            "success_candidate",
        )
        self.assertEqual(records["lnf_tesla_cathode_contract_value_reduction_hard_4c"].case_type, "4c_thesis_break")
        self.assertEqual(records["posco_future_m_lithium_event_and_ford_shock_false_green_guard"].case_type, "overheat")
        self.assertEqual(records["ecopro_materials_precursor_ipo_theme_overheat_guard"].case_type, "overheat")
        for record in records.values():
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertEqual(record.price_validation.price_validation_status, "needs_ohlc_backfill")

    def test_ess_stage2_and_ev_4c_watch_are_separated(self):
        rows = {row["case_id"]: row for row in round194_case_rows()}
        lg = rows["lg_energy_solution_ess_lfp_stage2_ev_contract_4c_watch"]
        samsung = rows["samsung_sdi_tesla_ess_unconfirmed_stage1_only"]

        self.assertEqual(lg["stage2_date"], "2025-07-30")
        self.assertEqual(lg["stage3_date"], "")
        self.assertEqual(lg["stage4c_date"], "2025-12-26")
        self.assertEqual(lg["hard_4c_confirmed"], "false")
        self.assertEqual(samsung["stage2_date"], "")
        self.assertIn("forbidden_unconfirmed_media_report", samsung["stage3_decision"])

    def test_contract_value_reduction_is_hard_4c_but_not_green(self):
        rows = {row["case_id"]: row for row in round194_case_rows()}
        lnf = rows["lnf_tesla_cathode_contract_value_reduction_hard_4c"]

        self.assertEqual(lnf["stage3_date"], "")
        self.assertEqual(lnf["stage4c_date"], "2025-12-29")
        self.assertEqual(lnf["hard_4c_confirmed"], "true")
        self.assertEqual(lnf["rerating_result"], "thesis_break")
        self.assertIn("contract_value_reduction_hard_4c", lnf["red_flag_fields"])

    def test_green_gate_requires_operating_conversion_and_blocks_theme(self):
        required = set(ROUND194_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND194_GREEN_FORBIDDEN_PATTERNS)
        adjustments = {row["axis"]: row for row in round194_score_adjustment_rows()}
        markdown = render_round194_green_gate_review_markdown()

        self.assertIn("gwh_or_tonnage_volume", required)
        self.assertIn("customer_calloff_or_shipment", required)
        self.assertIn("fcf_after_capex", required)
        self.assertIn("ev_theme", forbidden)
        self.assertIn("unconfirmed_media_report", forbidden)
        self.assertIn("contract_value_without_actual_order", forbidden)
        self.assertEqual(adjustments["contract_binding_quality"]["points"], "4")
        self.assertEqual(adjustments["ev_theme"]["points"], "-5")
        self.assertIn("Do not apply these weights to production scoring yet", markdown)

    def test_price_backfill_fields_include_battery_specific_operating_fields(self):
        fields = {row["field"] for row in round194_price_backfill_field_rows()}

        self.assertGreaterEqual(len(ROUND194_PRICE_BACKFILL_FIELDS), 45)
        for field in (
            "gwh_volume_visibility",
            "customer_order_calloff",
            "utilization_rate",
            "opm_margin_visibility",
            "fcf_after_capex",
            "ampc_dependency",
            "operating_profit_ex_ampc",
            "lithium_price_event_flag",
            "hard_4c_confirmed",
        ):
            self.assertIn(field, fields)

    def test_stage4b_4c_review_contains_price_only_watch_and_hard_gates(self):
        review = render_round194_stage4b_4c_review_markdown()

        self.assertIn("contract_value_reduction", ROUND194_HARD_4C_GATES)
        self.assertIn("operating_loss_ex_ampc", ROUND194_HARD_4C_GATES)
        self.assertIn("4B Status Definitions", review)
        self.assertIn("lnf_tesla_cathode_contract_value_reduction_hard_4c", review)

    def test_summary_and_audit_payload_are_calibration_only(self):
        summary = round194_summary()
        payload = round194_audit_payload()

        self.assertEqual(summary["case_candidate_count"], len(ROUND194_CASE_CANDIDATES))
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertIn("do_not_use_round194_cases_as_candidate_generation_input", payload["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self):
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_round194_r3_loop7_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(records), 7)
            self.assertIn("Stage 3-Green", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("gwh_volume_visibility", paths["score_adjustments"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
