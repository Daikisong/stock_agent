import unittest

from e2r.calibration.v12_archetype_signal_runtime_translation_audit import (
    build_v12_archetype_signal_runtime_translation_audit,
    render_v12_archetype_signal_runtime_translation_audit,
)


class V12ArchetypeSignalRuntimeTranslationAuditTests(unittest.TestCase):
    def test_audit_splits_funnel_archive_field_and_gate_failures(self) -> None:
        representative_rows = [
            {
                "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                "symbol": "000810",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-05-16",
                "MFE_180D_pct": 17.5,
                "evidence_available_at_that_date": "ROE, low-PBR value-up and capital return execution with buyback cancellation.",
            },
            {
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "symbol": "000660",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-04-25",
                "MFE_180D_pct": 39.7,
                "evidence_available_at_that_date": "HBM capacity sold out and Nvidia customer allocation order bridge.",
            },
            {
                "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                "symbol": "267260",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2024-02-16",
                "MFE_180D_pct": 256.7,
                "evidence_available_at_that_date": "AI datacenter customer backlog and long-term contract margin bridge.",
            },
            {
                "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                "symbol": "001440",
                "trigger_type": "Stage3-Green",
                "trigger_date": "2026-02-01",
                "MFE_180D_pct": 55.0,
                "evidence_available_at_that_date": "Order backlog, customer contract and margin conversion visible.",
            },
        ]
        gap_matrix_payload = {
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "large_sector_id": "L6",
                    "required_bridge_axes": ["capital_return", "valuation_repricing", "guard_risk"],
                    "runtime_gap_status": "not_in_current_benchmark",
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return"],
                    "root_cause": "research_green_fixture_not_exercised_by_current_runtime_benchmark",
                },
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "large_sector_id": "L2",
                    "required_bridge_axes": ["customer", "backlog", "contract"],
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "runtime_candidate_count": 2,
                    "runtime_max_score": 76.0,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                    "root_cause": "research_green_axes_not_structured_into_runtime_fields",
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "large_sector_id": "L1",
                    "required_bridge_axes": ["customer", "backlog", "contract"],
                    "runtime_gap_status": "runtime_stage3_gate_blocked",
                    "runtime_candidate_count": 3,
                    "runtime_max_score": 72.9,
                    "missing_required_bridge_axes": [],
                    "root_cause": "runtime_fields_present_but_weighted_green_gate_still_blocks",
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "large_sector_id": "L1",
                    "required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                    "runtime_gap_status": "runtime_input_evidence_missing",
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 0,
                    "missing_required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                    "root_cause": "runtime_candidate_has_insufficient_source_backed_inputs",
                },
            ]
        }
        readiness_payload = {
            "archetype_pair_rows": [
                {"canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "green_retrospective_ready": False},
                {"canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "green_retrospective_ready": True},
                {"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "green_retrospective_ready": True},
                {"canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "green_retrospective_ready": True},
            ]
        }
        runtime_score_rows = [
            {
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "symbol": "000660",
                "as_of_date": "2024-04-25",
                "current_stage": "3-Yellow",
                "current_score": "76.0",
                "research_axis_bridge_customer": "100",
                "research_axis_bridge_backlog": "0",
                "research_axis_bridge_contract": "0",
                "backlog_rpo_visibility": "0",
                "contract_quality": "0",
            },
            {
                "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                "symbol": "267260",
                "as_of_date": "2024-02-16",
                "current_stage": "2",
                "current_score": "72.9",
                "research_axis_bridge_customer": "100",
                "research_axis_bridge_backlog": "100",
                "research_axis_bridge_contract": "80",
            },
        ]
        payload = build_v12_archetype_signal_runtime_translation_audit(
            representative_rows=representative_rows,
            gap_matrix_payload=gap_matrix_payload,
            readiness_payload=readiness_payload,
            runtime_score_rows=runtime_score_rows,
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["rows"]}

        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["diagnosis"],
            "research_green_fixture_not_archived_for_runtime_replay",
        )
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["diagnosis"],
            "research_signal_not_structured_into_runtime_fields",
        )
        self.assertEqual(
            by_arch["C02_POWER_GRID_DATACENTER_CAPEX"]["diagnosis"],
            "weighted_stage3_gate_blocks_after_fields_present",
        )
        self.assertEqual(
            by_arch["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]["diagnosis"],
            "runtime_candidate_input_evidence_missing_for_bridge",
        )
        self.assertIn("capital_return", payload["research_axis_signal_counts"])
        self.assertIn("backlog", payload["untranslated_axis_counts"])

        report = render_v12_archetype_signal_runtime_translation_audit(payload)
        self.assertIn("C21 금융", report)
        self.assertIn("research_signal_not_structured_into_runtime_fields", report)
        self.assertIn("weighted_stage3_gate_blocks_after_fields_present", report)


if __name__ == "__main__":
    unittest.main()
