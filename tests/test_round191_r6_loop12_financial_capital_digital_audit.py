from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round191_r6_loop12_audit_report import build_parser
from e2r.sector.round191_r6_loop12_financial_capital_digital_audit import (
    ROUND191_REQUIRED_CASES,
    ROUND191_REQUIRED_PRICE_FIELDS,
    ROUND191_REQUIRED_STAGE3_CHECKS,
    ROUND191_REQUIRED_STAGE4B_CHECKS,
    ROUND191_REQUIRED_STAGE4C_HARD_GATES,
    ROUND191_REQUIRED_TARGETS,
    render_round191_followup_backfill_markdown,
    render_round191_guardrail_review_markdown,
    render_round191_summary_markdown,
    round191_audit_checks,
    round191_audit_payload,
    round191_audit_rows,
    round191_audit_summary,
    write_round191_r6_loop12_audit_reports,
)


class Round191R6Loop12FinancialCapitalDigitalAuditTests(unittest.TestCase):
    def test_round191_audit_confirms_round190_target_case_and_price_coverage(self):
        summary = round191_audit_summary()
        self.assertEqual(summary["required_target_count"], 11)
        self.assertEqual(summary["required_case_count"], 13)
        self.assertEqual(summary["required_price_field_count"], len(ROUND191_REQUIRED_PRICE_FIELDS))
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["case_records_are_candidate_generation_input"])

        rows = {row["check_id"]: row for row in round191_audit_rows()}
        self.assertEqual(rows["required_targets_present"]["status"], "pass")
        self.assertEqual(rows["required_case_records_present"]["status"], "pass")
        self.assertEqual(rows["price_fields_present"]["status"], "pass")
        self.assertEqual(rows["hard_gate_target_count"]["actual_count"], "3")

    def test_stage_gate_audit_preserves_six_of_nine_four_of_six_and_hard_gates(self):
        rows = {row["check_id"]: row for row in round191_audit_rows()}
        self.assertEqual(rows["stage3_six_of_nine_checks_present"]["status"], "pass")
        self.assertEqual(rows["stage4b_four_of_six_checks_present"]["status"], "pass")
        self.assertEqual(rows["stage4c_hard_gates_present"]["status"], "pass")
        self.assertEqual(rows["stage3_six_of_nine_checks_present"]["expected_count"], str(len(ROUND191_REQUIRED_STAGE3_CHECKS)))
        self.assertEqual(rows["stage4b_four_of_six_checks_present"]["expected_count"], str(len(ROUND191_REQUIRED_STAGE4B_CHECKS)))
        self.assertEqual(rows["stage4c_hard_gates_present"]["expected_count"], str(len(ROUND191_REQUIRED_STAGE4C_HARD_GATES)))

    def test_required_lists_include_round191_examples(self):
        self.assertIn("INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE", ROUND191_REQUIRED_TARGETS)
        self.assertIn("KRW_STABLECOIN_POLICY_THEME", ROUND191_REQUIRED_TARGETS)
        self.assertIn("samsung_life_insurance_nav_valueup_stage23_case", ROUND191_REQUIRED_CASES)
        self.assertIn("krw_stablecoin_policy_theme_4b_watch_case", ROUND191_REQUIRED_CASES)
        self.assertIn("k_ics_ratio", ROUND191_REQUIRED_PRICE_FIELDS)
        self.assertIn("stablecoin_issuance_volume", ROUND191_REQUIRED_PRICE_FIELDS)
        self.assertIn("biometric_data_risk_flag", ROUND191_REQUIRED_PRICE_FIELDS)
        self.assertIn("tax_policy_shock_flag", ROUND191_REQUIRED_PRICE_FIELDS)

    def test_payload_and_markdown_explain_guardrails(self):
        payload = round191_audit_payload()
        self.assertEqual(payload["summary"]["failed_check_count"], 0)
        self.assertFalse(payload["production_scoring_changed"])

        summary_md = render_round191_summary_markdown()
        backfill_md = render_round191_followup_backfill_markdown()
        guardrail_md = render_round191_guardrail_review_markdown()
        self.assertIn("Round-191 R6 Loop-12", summary_md)
        self.assertIn("round190_r6_loop12_financial_capital_digital", summary_md)
        self.assertIn("production_scoring_changed: false", summary_md)
        self.assertIn("Do not lower Stage 3-Green thresholds", backfill_md)
        self.assertIn("스테이블코인 + 급등", guardrail_md)

    def test_writer_and_cli_parse_args(self):
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round191_r6_loop12_audit_reports(
                output_directory=Path(tmp) / "out",
                audit_path=Path(tmp) / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            self.assertIn("failed_check_count", paths["audit_json"].read_text(encoding="utf-8"))
            self.assertIn("required_targets_present", paths["coverage_matrix"].read_text(encoding="utf-8"))
            self.assertIn("Round191 confirms", paths["backfill_plan"].read_text(encoding="utf-8"))

    def test_production_scoring_modules_do_not_import_round191_audit(self):
        forbidden = "round191_r6_loop12_financial_capital_digital_audit"
        for relative in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
            "src/e2r/backtest/asof_research_replay.py",
        ):
            text = Path(relative).read_text(encoding="utf-8")
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
