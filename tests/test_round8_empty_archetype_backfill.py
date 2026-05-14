import tempfile
from pathlib import Path
import unittest

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import E2RCaseRecord, PriceValidation
from e2r.sector.round8_empty_archetype_backfill import (
    ROUND8_PRICE_PATTERN_VALUES,
    ROUND8_SUCCESS_CASE_REQUIREMENTS,
    Round8BackfillPriority,
    render_round8_price_pattern_contract_markdown,
    round8_backfill_rows,
    round8_case_gaps,
    round8_target_for,
    write_round8_empty_archetype_reports,
)


class Round8EmptyArchetypeBackfillTests(unittest.TestCase):
    def test_round8_price_pattern_adds_policy_contract_delay(self):
        self.assertIn("policy_contract_delay", ROUND8_PRICE_PATTERN_VALUES)
        self.assertIn("stage4b_or_stage4c_explainable_after_the_fact", ROUND8_SUCCESS_CASE_REQUIREMENTS)

        markdown = render_round8_price_pattern_contract_markdown()
        self.assertIn("credit_relief_rally", markdown)
        self.assertIn("cycle_boom_bust", markdown)

    def test_turnaround_target_requires_durable_opm_fcf_not_one_off_cost_cut(self):
        target = round8_target_for(E2RArchetype.TURNAROUND_COST_RESTRUCTURING)

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.priority, Round8BackfillPriority.HIGH)
        self.assertIn("fcf_improvement", target.required_alignment_fields)
        self.assertIn("일회성 비용절감 기업", target.counterexample_candidates)
        self.assertIn("one-time cost cuts", target.green_policy)

    def test_commodity_target_segments_refining_chemical_steel_and_rare_materials(self):
        target = round8_target_for(E2RArchetype.COMMODITY_SPREAD)

        self.assertIsNotNone(target)
        assert target is not None
        self.assertEqual(target.priority, Round8BackfillPriority.REDTEAM)
        self.assertIn("Refining", target.focus)
        self.assertIn("chemical_china_oversupply", target.counterexample_candidates)
        self.assertIn("spread_reversal", target.counterexample_candidates)

    def test_auto_targets_are_split_between_completed_vehicle_and_components(self):
        completed = round8_target_for(E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE)
        components = round8_target_for(E2RArchetype.AUTO_MOBILITY_COMPONENTS)

        self.assertIsNotNone(completed)
        self.assertIsNotNone(components)
        assert completed is not None
        assert components is not None
        self.assertIn("shareholder_return_execution", completed.required_alignment_fields)
        self.assertIn("customer_diversification", components.required_alignment_fields)
        self.assertIn("single_customer_dependency", components.counterexample_candidates)

    def test_financial_and_cdmo_targets_keep_green_strict(self):
        financial = round8_target_for(E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET)
        cdmo = round8_target_for(E2RArchetype.CDMO_HEALTHCARE_CONTRACT)

        self.assertIsNotNone(financial)
        self.assertIsNotNone(cdmo)
        assert financial is not None
        assert cdmo is not None
        self.assertIn("cet1_or_capital_ratio", financial.required_alignment_fields)
        self.assertIn("low_pbr_without_roe", financial.counterexample_candidates)
        self.assertIn("capacity_utilization", cdmo.required_alignment_fields)
        self.assertIn("patent_litigation", cdmo.counterexample_candidates)

    def test_memory_target_includes_success_and_4b_watch(self):
        target = round8_target_for(E2RArchetype.MEMORY_HBM_CAPACITY)

        self.assertIsNotNone(target)
        assert target is not None
        self.assertIn("SK_Hynix_stage3_success", target.success_case_candidates)
        self.assertIn("sk_hynix_4b_watch_after_large_run", target.counterexample_candidates)
        self.assertIn("one_to_two_year_price_surge", target.stage4b_signals)

    def test_gap_report_recommends_initial_records_for_empty_target(self):
        rows = round8_case_gaps(())
        by_archetype = {row["archetype"]: row for row in rows}

        self.assertEqual(
            by_archetype[E2RArchetype.TURNAROUND_COST_RESTRUCTURING.value]["recommended_action"],
            "add_initial_success_and_counterexample_records",
        )

    def test_gap_report_recommends_backfill_after_two_by_two_coverage(self):
        rows = round8_case_gaps(
            (
                _record("p1", "structural_success"),
                _record("p2", "success_candidate"),
                _record("c1", "failed_rerating"),
                _record("c2", "event_premium"),
            )
        )
        by_archetype = {row["archetype"]: row for row in rows}

        self.assertEqual(
            by_archetype[E2RArchetype.TURNAROUND_COST_RESTRUCTURING.value]["recommended_action"],
            "backfill_price_path",
        )

    def test_every_round8_target_has_matrix_row(self):
        rows = round8_backfill_rows()
        by_archetype = {row["archetype"]: row for row in rows}

        self.assertIn(E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE.value, by_archetype)
        self.assertIn(E2RArchetype.NUCLEAR_SMR_GRID_POLICY.value, by_archetype)
        self.assertIn("success_case_candidates", by_archetype[E2RArchetype.PLATFORM_SOFTWARE_INTERNET.value])

    def test_report_writer_outputs_round8_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round8_empty_archetype_reports(output_directory=tmp)

            self.assertTrue(paths["framework"].exists())
            self.assertTrue(paths["target_matrix"].exists())
            self.assertTrue(paths["gap_report"].exists())
            self.assertTrue(paths["price_pattern_contract"].exists())
            self.assertTrue(paths["next_plan"].exists())
            self.assertIn("Round-8 Empty-Archetype", paths["framework"].read_text(encoding="utf-8"))

    def test_production_scoring_modules_do_not_import_round8_framework(self):
        paths = [
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ]
        for path in paths:
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round8_empty_archetype_backfill", text)


def _record(case_id: str, case_type: str) -> E2RCaseRecord:
    return E2RCaseRecord(
        case_id=case_id,
        symbol=f"T{case_id}",
        company_name=f"테스트 {case_id}",
        market="KR",
        sector_raw="턴어라운드",
        primary_archetype=E2RArchetype.TURNAROUND_COST_RESTRUCTURING,
        expected_group=case_type,
        case_type=case_type,
        price_validation=PriceValidation(price_validation_status="needs_price_backfill"),
    )


if __name__ == "__main__":
    unittest.main()
