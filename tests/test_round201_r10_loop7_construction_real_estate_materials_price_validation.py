from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round201_r10_loop7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round201_r10_loop7_construction_real_estate_materials_price_validation import (
    ROUND201_CASE_CANDIDATES,
    ROUND201_GREEN_FORBIDDEN_PATTERNS,
    ROUND201_GREEN_REQUIRED_FIELDS,
    ROUND201_HARD_4C_GATES,
    ROUND201_PRICE_BACKFILL_FIELDS,
    ROUND201_REQUIRED_TARGET_ALIASES,
    render_round201_green_gate_review_markdown,
    render_round201_stage4b_4c_review_markdown,
    round201_audit_payload,
    round201_case_records,
    round201_summary,
    write_round201_r10_loop7_reports,
)


class Round201R10Loop7ConstructionRealEstatePriceValidationTests(unittest.TestCase):
    def test_round201_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND201_REQUIRED_TARGET_ALIASES), 15)
        self.assertTrue(set(ROUND201_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND201_REQUIRED_TARGET_ALIASES["CONSTRUCTION_REAL_ESTATE_CREDIT"],
            E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT.value,
        )
        self.assertEqual(
            ROUND201_REQUIRED_TARGET_ALIASES["AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT"],
            E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT.value,
        )

    def test_case_records_validate_and_remain_shadow_only(self) -> None:
        records = round201_case_records()
        for record in records:
            record.validate()
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIsNone(record.stage3_date)

        summary = round201_summary()
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["production_scoring_changed"])

    def test_epc_cases_are_stage2_until_margin_and_cash_flow_are_visible(self) -> None:
        by_id = {case.case_id: case for case in ROUND201_CASE_CANDIDATES}
        samsung = by_id["samsung_ea_fadhili_epc_backlog_stage2_watch"]
        hyundai = by_id["hyundai_ec_jafurah_gas_infra_stage2_watch"]
        daewoo = by_id["daewoo_ec_grand_faw_handover_stage2_watch"]

        for case in (samsung, hyundai, daewoo):
            self.assertEqual(case.case_type, "success_candidate")
            self.assertIsNotNone(case.stage2_date)
            self.assertIsNone(case.stage3_date)
            self.assertIn(case.stage4b_status, {"watch", "none"})
            self.assertTrue(any("margin" in field or "cash" in field for field in case.red_flag_fields))

        self.assertIn("epc_backlog_without_margin", samsung.red_flag_fields)
        self.assertIn("handover", "|".join(daewoo.evidence_fields))

    def test_pf_and_apartment_safety_cases_are_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND201_CASE_CANDIDATES}
        taeyoung = by_id["taeyoung_pf_workout_credit_hard_4c"]
        hdc = by_id["hdc_hyundai_development_apartment_collapse_hard_4c"]

        self.assertTrue(taeyoung.hard_4c_confirmed)
        self.assertTrue(hdc.hard_4c_confirmed)
        self.assertEqual(taeyoung.rerating_result, "thesis_break")
        self.assertEqual(hdc.rerating_result, "thesis_break")
        self.assertIn("pf_workout_or_debt_reschedule", taeyoung.red_flag_fields)
        self.assertIn("apartment_collapse_or_quality_accident", hdc.red_flag_fields)

    def test_data_center_real_asset_is_blocked_without_tenant_and_noi_affo(self) -> None:
        data_center = next(
            case for case in ROUND201_CASE_CANDIDATES if case.case_id == "sk_aws_ulsan_ai_data_center_real_asset_insufficient_evidence"
        )

        self.assertEqual(data_center.primary_archetype, E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT)
        self.assertIn(E2RArchetype.AI_DATA_CENTER_NO_REVENUE_NO_TENANT, data_center.secondary_archetypes)
        self.assertIsNone(data_center.stage3_date)
        self.assertIn("data_center_theme_without_tenant", data_center.red_flag_fields)
        self.assertIn("asset_headline_without_noi_affo", data_center.red_flag_fields)

    def test_green_gate_requires_cash_flow_affo_pf_and_safety(self) -> None:
        required = set(ROUND201_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND201_GREEN_FORBIDDEN_PATTERNS)
        markdown = render_round201_green_gate_review_markdown()

        self.assertIn("cash_flow_after_working_capital_confirmed", required)
        self.assertIn("epc_margin_or_noi_affo_confirmed", required)
        self.assertIn("pf_and_funding_cost_risk_passed", required)
        self.assertIn("safety_quality_trust_passed", required)
        self.assertIn("contract_headline_only", forbidden)
        self.assertIn("pf_relief_policy_only", forbidden)
        self.assertIn("data_center_theme_without_tenant", forbidden)
        self.assertIn("Do not apply these weights to production scoring yet.", markdown)

    def test_price_backfill_fields_include_r10_cashflow_pf_and_affo_inputs(self) -> None:
        fields = set(ROUND201_PRICE_BACKFILL_FIELDS)

        self.assertIn("working_capital", fields)
        self.assertIn("pf_exposure", fields)
        self.assertIn("tenant_contract_quality", fields)
        self.assertIn("noi_affo", fields)
        self.assertIn("power_water_permitting", fields)
        self.assertIn("safety_quality_incident_flag", fields)

    def test_stage4b_4c_review_contains_r10_hard_gates(self) -> None:
        review = render_round201_stage4b_4c_review_markdown()

        self.assertIn("pf_workout_or_debt_reschedule", ROUND201_HARD_4C_GATES)
        self.assertIn("apartment_collapse_or_quality_accident", ROUND201_HARD_4C_GATES)
        self.assertIn("tenant_absent_or_no_binding_lease", ROUND201_HARD_4C_GATES)
        self.assertIn("AFFO", review)
        self.assertIn("Apartment collapse", review)

    def test_summary_and_audit_payload_are_calibration_only(self) -> None:
        audit = round201_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_201.md")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round201_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round201_r10_loop7_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND201_CASE_CANDIDATES))
            self.assertIn("cash_flow_after_working_capital", paths["score_adjustments"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
