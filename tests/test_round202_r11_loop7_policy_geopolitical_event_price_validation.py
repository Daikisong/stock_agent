from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round202_r11_loop7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round202_r11_loop7_policy_geopolitical_event_price_validation import (
    ROUND202_CASE_CANDIDATES,
    ROUND202_GREEN_FORBIDDEN_PATTERNS,
    ROUND202_GREEN_REQUIRED_FIELDS,
    ROUND202_HARD_4C_GATES,
    ROUND202_PRICE_BACKFILL_FIELDS,
    ROUND202_REQUIRED_TARGET_ALIASES,
    render_round202_green_gate_review_markdown,
    render_round202_stage4b_4c_review_markdown,
    round202_audit_payload,
    round202_case_records,
    round202_summary,
    write_round202_r11_loop7_reports,
)


class Round202R11Loop7PolicyGeopoliticalEventPriceValidationTests(unittest.TestCase):
    def test_round202_targets_are_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertGreaterEqual(len(ROUND202_REQUIRED_TARGET_ALIASES), 17)
        self.assertTrue(set(ROUND202_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND202_REQUIRED_TARGET_ALIASES["DOMESTIC_RESOURCE_DISCOVERY_EVENT"],
            E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT.value,
        )
        self.assertEqual(
            ROUND202_REQUIRED_TARGET_ALIASES["POLICY_MARKET_SHOCK_EVENT"],
            E2RArchetype.POLICY_MARKET_SHOCK_EVENT.value,
        )

    def test_case_records_validate_and_keep_r11_conservative_bias(self) -> None:
        records = round202_case_records()
        for record in records:
            record.validate()
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("r11_default_stage3_bias_conservative", record.green_guardrails)
            self.assertIsNone(record.stage3_date)

        summary = round202_summary()
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["r11_default_stage3_bias"], "conservative")
        self.assertFalse(summary["production_scoring_changed"])

    def test_resource_discovery_is_price_moved_without_evidence(self) -> None:
        kogas = next(case for case in ROUND202_CASE_CANDIDATES if case.case_id == "kogas_east_sea_resource_discovery_event_premium")

        self.assertEqual(kogas.primary_archetype, E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT)
        self.assertEqual(kogas.case_type, "event_premium")
        self.assertEqual(kogas.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("resource_estimate_without_drilling", kogas.red_flag_fields)
        self.assertIsNone(kogas.stage3_date)
        self.assertEqual(kogas.stage4b_status, "watch")

    def test_policy_to_contract_cases_are_stage2_watch_until_orders(self) -> None:
        by_id = {case.case_id: case for case in ROUND202_CASE_CANDIDATES}
        doosan = by_id["doosan_enerbility_nuclear_smr_policy_to_contract_watch"]
        shipbuilding = by_id["hdhyundai_samsungheavy_us_shipbuilding_policy_mou_watch"]
        short_selling = by_id["short_selling_msci_market_structure_stage2_watch"]

        self.assertEqual(doosan.case_type, "success_candidate")
        self.assertIsNotNone(doosan.stage2_date)
        self.assertIn(E2RArchetype.NUCLEAR_SMR_GRID_POLICY, doosan.secondary_archetypes)
        self.assertIn("equipment_backlog_unverified", doosan.red_flag_fields)

        self.assertIn("mou_only", shipbuilding.red_flag_fields)
        self.assertIsNone(shipbuilding.stage3_date)

        self.assertEqual(short_selling.primary_archetype, E2RArchetype.MARKET_STRUCTURE_SHORT_SELLING_POLICY)
        self.assertIsNotNone(short_selling.stage2_date)
        self.assertIn("market_structure_reform_without_earnings", short_selling.red_flag_fields)

    def test_disease_and_science_events_do_not_create_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND202_CASE_CANDIDATES}
        poultry = by_id["poultry_basket_brazil_bird_flu_import_ban_event_fade"]
        lk99 = by_id["lk99_superconductor_speculative_science_thesis_break"]

        self.assertEqual(poultry.case_type, "event_premium")
        self.assertIn("disease_import_ban_only", poultry.red_flag_fields)
        self.assertEqual(poultry.stage4c_date.isoformat(), "2025-06-23")
        self.assertFalse(poultry.hard_4c_confirmed)

        self.assertEqual(lk99.case_type, "overheat")
        self.assertTrue(lk99.hard_4c_confirmed)
        self.assertEqual(lk99.rerating_result, "thesis_break")
        self.assertIn("independent_replication_failure", lk99.red_flag_fields)

    def test_macro_policy_shock_is_overlay_not_company_green(self) -> None:
        shock = next(case for case in ROUND202_CASE_CANDIDATES if case.case_id == "korea_martial_law_policy_market_shock_overlay")

        self.assertEqual(shock.primary_archetype, E2RArchetype.POLICY_MARKET_SHOCK_EVENT)
        self.assertIn(E2RArchetype.POLITICAL_SYSTEM_SHOCK_KOREA, shock.secondary_archetypes)
        self.assertEqual(shock.case_type, "4b_watch")
        self.assertIsNone(shock.stage3_date)
        self.assertEqual(shock.stage4c_date.isoformat(), "2024-12-04")
        self.assertFalse(shock.hard_4c_confirmed)

    def test_green_gate_requires_contract_budget_financing_revenue_and_revision(self) -> None:
        required = set(ROUND202_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND202_GREEN_FORBIDDEN_PATTERNS)
        markdown = render_round202_green_gate_review_markdown()

        self.assertIn("company_level_contract_confirmed", required)
        self.assertIn("budget_or_contract_amount_confirmed", required)
        self.assertIn("financing_secured", required)
        self.assertIn("revenue_conversion_confirmed", required)
        self.assertIn("policy_news_only", forbidden)
        self.assertIn("mou_only", forbidden)
        self.assertIn("preprint_or_science_claim_only", forbidden)
        self.assertIn("Do not apply these weights to production scoring yet.", markdown)

    def test_price_backfill_fields_include_short_window_event_inputs(self) -> None:
        fields = set(ROUND202_PRICE_BACKFILL_FIELDS)

        self.assertIn("MFE_5D", fields)
        self.assertIn("MFE_20D", fields)
        self.assertIn("event_volume_spike", fields)
        self.assertIn("contract_amount", fields)
        self.assertIn("drilling_result", fields)
        self.assertIn("replication_result", fields)
        self.assertIn("macro_fx_shock", fields)

    def test_stage4b_4c_review_contains_r11_hard_gates(self) -> None:
        review = render_round202_stage4b_4c_review_markdown()

        self.assertIn("drilling_failure", ROUND202_HARD_4C_GATES)
        self.assertIn("independent_replication_failure", ROUND202_HARD_4C_GATES)
        self.assertIn("political_system_shock", ROUND202_HARD_4C_GATES)
        self.assertIn("event premium", review.lower())
        self.assertIn("macro overlay", review)

    def test_summary_and_audit_payload_are_calibration_only(self) -> None:
        audit = round202_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_202.md")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round202_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round202_r11_loop7_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            self.assertEqual(len(records), len(ROUND202_CASE_CANDIDATES))
            self.assertIn("policy_news_only", paths["score_adjustments"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
