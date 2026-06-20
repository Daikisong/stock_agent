import unittest

from e2r.calibration.v12_runtime_first_repair_input_gap_manifest import (
    build_v12_runtime_first_repair_input_gap_manifest,
    render_v12_runtime_first_repair_input_gap_manifest,
)


class V12RuntimeFirstRepairInputGapManifestTests(unittest.TestCase):
    def test_manifest_separates_archive_missing_strict_pit_and_ready_rows(self) -> None:
        first_slice = {
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "implementation_lane": "01_fixture_archive_and_candidate_funnel",
                    "acceptance_status_current": "blocked",
                    "runtime_candidate_count": 0,
                    "runtime_max_score": None,
                    "missing_required_bridge_axes": ["capital_return"],
                    "missing_feature_parser_contract_primitives": [],
                    "acceptance_tests_to_add": ["test_c21_fixture"],
                },
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "implementation_lane": "02_parser_feature_bridge_contract",
                    "acceptance_status_current": "blocked",
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                    "missing_feature_parser_contract_primitives": [],
                    "acceptance_tests_to_add": ["test_c06_bridge"],
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "implementation_lane": "03_weighted_gate_validation_after_fields",
                    "acceptance_status_current": "blocked",
                    "runtime_candidate_count": 44,
                    "runtime_max_score": 72.9,
                    "missing_required_bridge_axes": [],
                    "missing_feature_parser_contract_primitives": [],
                    "acceptance_tests_to_add": ["test_c02_gate"],
                },
                {
                    "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
                    "implementation_lane": "01_fixture_archive_and_candidate_funnel",
                    "acceptance_status_current": "blocked",
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 55.0,
                    "missing_required_bridge_axes": ["consumer_sell_through"],
                    "missing_feature_parser_contract_primitives": [],
                    "acceptance_tests_to_add": ["test_c18_fixture"],
                },
            ]
        }
        readiness = {
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "role": "green",
                    "candidate": {"symbol": "000810", "as_of_date": "2024-05-16"},
                    "retrospective_readiness_status": "missing_official_and_research_inputs",
                    "strict_pit_readiness_status": "missing_official_and_research_inputs",
                    "retrospective_missing_inputs": ["official_universe", "price_history_370d"],
                    "strict_pit_missing_inputs": ["official_universe", "price_history_370d"],
                },
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "role": "green",
                    "candidate": {"symbol": "000660", "as_of_date": "2024-04-25"},
                    "retrospective_readiness_status": "ready_retrospective_exact_replay",
                    "strict_pit_readiness_status": "missing_research_snapshot_inputs",
                    "retrospective_missing_inputs": [],
                    "strict_pit_missing_inputs": ["pit_search_snapshot"],
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "role": "green",
                    "candidate": {"symbol": "267260", "as_of_date": "2024-02-16"},
                    "retrospective_readiness_status": "ready_retrospective_exact_replay",
                    "strict_pit_readiness_status": "ready_strict_pit_exact_replay",
                    "retrospective_missing_inputs": [],
                    "strict_pit_missing_inputs": [],
                },
                {
                    "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
                    "role": "green",
                    "candidate": {"symbol": "003230", "as_of_date": "2024-05-16"},
                    "retrospective_readiness_status": "missing_research_snapshot_inputs",
                    "strict_pit_readiness_status": "missing_research_snapshot_inputs",
                    "retrospective_missing_inputs": ["evidence_source_search_snapshot"],
                    "strict_pit_missing_inputs": ["pit_evidence_source_search_snapshot"],
                },
            ]
        }
        funnel = {
            "rows": [
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "role": "green",
                    "candidate": {"symbol": "000810", "as_of_date": "2024-05-16"},
                    "fixture_funnel_status": "symbol_never_reached_current_runtime",
                    "funnel_root_cause": "benchmark_universe_or_official_cheap_scan_funnel_gap",
                    "runtime_symbol_dates": [],
                },
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "role": "green",
                    "candidate": {"symbol": "000660", "as_of_date": "2024-04-25"},
                    "fixture_funnel_status": "symbol_reached_runtime_but_not_fixture_date",
                    "funnel_root_cause": "monthly_schedule_or_fixture_date_mismatch",
                    "runtime_symbol_dates": ["2024-04-01", "2024-05-01"],
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "role": "green",
                    "candidate": {"symbol": "267260", "as_of_date": "2024-02-16"},
                    "fixture_funnel_status": "exact_symbol_date_candidate_reached_runtime",
                    "funnel_root_cause": "exact_candidate_reached",
                    "runtime_symbol_dates": ["2024-02-16"],
                },
                {
                    "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
                    "role": "green",
                    "candidate": {"symbol": "003230", "as_of_date": "2024-05-16"},
                    "fixture_funnel_status": "exact_symbol_date_candidate_reached_runtime",
                    "funnel_root_cause": "exact_candidate_reached",
                    "runtime_symbol_dates": ["2024-05-16"],
                },
            ]
        }

        payload = build_v12_runtime_first_repair_input_gap_manifest(
            first_slice_payload=first_slice,
            readiness_payload=readiness,
            funnel_payload=funnel,
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["rows"]}

        self.assertEqual(
            by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["role_gap_classes"],
            ["archive_or_candidate_funnel_missing"],
        )
        self.assertEqual(
            by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["role_gap_classes"],
            ["strict_pit_research_snapshot_missing"],
        )
        self.assertEqual(by_arch["C02_POWER_GRID_DATACENTER_CAPEX"]["role_gap_classes"], ["exact_replay_ready"])
        self.assertEqual(
            by_arch["C18_CONSUMER_EXPORT_CHANNEL_REORDER"]["role_gap_classes"],
            ["exact_candidate_reached_but_research_snapshot_missing"],
        )
        self.assertEqual(payload["summary"]["role_gap_class_counts"]["exact_replay_ready"], 1)
        self.assertEqual(
            payload["summary"]["role_gap_class_counts"]["exact_candidate_reached_but_research_snapshot_missing"],
            1,
        )
        self.assertEqual(payload["summary"]["missing_input_counts"]["strict:pit_search_snapshot"], 1)
        self.assertEqual(payload["summary"]["selected_hbm_or_samsung_related_count"], 1)
        self.assertEqual(payload["summary"]["selected_non_hbm_count"], 3)
        self.assertIn("삼전/하닉은 전체 아키타입", payload["summary"]["generalization_guard"])

        report = render_v12_runtime_first_repair_input_gap_manifest(payload)
        self.assertIn("C21/C23/C26은 점수식이 낮은 게 아니라", report)
        self.assertIn("strict PIT search snapshot", report)
        self.assertIn("하닉/삼전만 좋아지는 패치는 실패", report)


if __name__ == "__main__":
    unittest.main()
