import unittest

from e2r.calibration.v12_research_green_runtime_gap_matrix import (
    build_v12_research_green_runtime_gap_matrix,
    render_v12_research_green_runtime_gap_matrix,
)


class V12ResearchGreenRuntimeGapMatrixTests(unittest.TestCase):
    def test_matrix_joins_research_green_shape_to_runtime_gap(self) -> None:
        representative_rows = [
            {
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_type": "Stage3-Green",
                "case_id": "C06_GREEN",
                "trigger_id": "T1",
                "symbol": "000660",
                "trigger_date": "2024-04-25",
                "entry_date": "2024-04-25",
                "MFE_180D_pct": 39.76,
                "MAE_180D_pct": -18.62,
                "fine_archetype_id": "HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE",
                "current_profile_verdict": "current_profile_correct",
                "evidence_available_at_that_date": "HBM capacity sold out and customer allocation visible.",
                "evidence_source": "fixture source",
                "source_file": "fixture.md",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                "trigger_type": "Stage3-Green",
                "case_id": "C21_GREEN",
                "trigger_id": "T2",
                "symbol": "000810",
                "trigger_date": "2024-05-16",
                "entry_date": "2024-05-16",
                "MFE_180D_pct": 62.0,
                "MAE_180D_pct": -9.0,
                "fine_archetype_id": "ROE_PBR_CAPITAL_RETURN_EXECUTION",
                "current_profile_verdict": "current_profile_correct",
                "evidence_available_at_that_date": "Buyback cancellation and ROE/PBR rerating visible.",
                "evidence_source": "fixture source",
                "source_file": "fixture.md",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                "trigger_type": "Stage3-Green",
                "case_id": "C01_GREEN",
                "trigger_id": "T1B",
                "symbol": "001440",
                "trigger_date": "2026-02-01",
                "entry_date": "2026-02-01",
                "MFE_180D_pct": 55.0,
                "MAE_180D_pct": -8.0,
                "fine_archetype_id": "ORDER_BACKLOG_MARGIN_BRIDGE",
                "current_profile_verdict": "current_profile_correct",
                "evidence_available_at_that_date": "Order backlog, customer contract and margin conversion visible.",
                "evidence_source": "fixture source",
                "source_file": "fixture.md",
                "source_proxy_only": False,
                "evidence_url_pending": False,
            },
            {
                "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
                "trigger_type": "Stage3-Green",
                "case_id": "C04_PROXY",
                "trigger_id": "T3",
                "symbol": "000000",
                "trigger_date": "2024-01-02",
                "entry_date": "2024-01-02",
                "fine_archetype_id": "POLICY_HEADLINE_ONLY",
                "evidence_available_at_that_date": "source proxy only",
                "evidence_source": "source_proxy_only",
                "source_file": "fixture.md",
                "source_proxy_only": True,
                "evidence_url_pending": False,
            },
        ]
        spec_payload = {
            "rows": [
                {
                    "role": "green",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "candidate": {"case_id": "C06_GREEN", "symbol": "000660", "as_of_date": "2024-04-25"},
                },
                {
                    "role": "guard",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "candidate": {"case_id": "C06_GUARD", "symbol": "356860", "as_of_date": "2024-03-06"},
                },
                {
                    "role": "green",
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "candidate": {"case_id": "C21_GREEN", "symbol": "000810", "as_of_date": "2024-05-16"},
                },
                {
                    "role": "green",
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "candidate": {"case_id": "C01_GREEN", "symbol": "001440", "as_of_date": "2026-02-01"},
                },
            ]
        }
        coverage_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "runtime_gap_status": "not_in_current_benchmark",
                    "runtime_candidate_count": 0,
                    "missing_required_bridge_axes": ["capital_return"],
                },
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "runtime_gap_status": "runtime_input_evidence_missing",
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 0,
                    "missing_required_bridge_axes": ["margin", "backlog", "contract", "customer"],
                },
                {
                    "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
                    "runtime_gap_status": "fixture_not_ready",
                    "runtime_candidate_count": 0,
                    "missing_required_bridge_axes": ["contract"],
                },
            ]
        }

        payload = build_v12_research_green_runtime_gap_matrix(
            representative_rows=representative_rows,
            spec_payload=spec_payload,
            coverage_payload=coverage_payload,
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["rows"]}

        self.assertEqual(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["research_clean_green_count"], 1)
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["root_cause"],
            "research_green_axes_not_structured_into_runtime_fields",
        )
        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["root_cause"],
            "research_green_fixture_not_exercised_by_current_runtime_benchmark",
        )
        self.assertEqual(
            by_arch["C01_ORDER_BACKLOG_MARGIN_BRIDGE"]["root_cause"],
            "runtime_candidate_has_insufficient_source_backed_inputs",
        )
        self.assertEqual(
            by_arch["C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY"]["root_cause"],
            "research_green_not_source_backed_enough_for_fixture",
        )
        report = render_v12_research_green_runtime_gap_matrix(payload)

        self.assertIn("Research Green Runtime Gap Matrix", report)
        self.assertIn("HBM_CUSTOMER_APPROVAL_CAPACITY_MIX_BRIDGE", report)
        self.assertIn("capital_return", report)


if __name__ == "__main__":
    unittest.main()
