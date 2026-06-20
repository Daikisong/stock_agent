import unittest

from e2r.calibration.v12_runtime_first_repair_slice import (
    build_v12_runtime_first_repair_slice,
    render_v12_runtime_first_repair_slice,
)


def acceptance_row(archetype: str, lane: str, priority: float, candidates: int) -> dict:
    return {
        "canonical_archetype_id": archetype,
        "implementation_lane": lane,
        "acceptance_status_current": "blocked",
        "priority_score": priority,
        "runtime_candidate_count": candidates,
        "runtime_max_score": None,
        "missing_required_bridge_axes": ["contract"] if "C06" in archetype else [],
        "missing_feature_parser_contract_primitives": ["field_gap"] if "C26" in archetype else [],
        "required_proof_artifacts": ["proof"],
        "acceptance_tests_to_add": [f"test_{archetype.lower()}"],
        "do_not_accept": "do not use shortcut",
    }


class V12RuntimeFirstRepairSliceTests(unittest.TestCase):
    def test_slice_includes_hbm_samsung_and_non_hbm_representatives(self) -> None:
        acceptance = {
            "rows": [
                acceptance_row(
                    "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "01_fixture_archive_and_candidate_funnel",
                    101.8,
                    0,
                ),
                acceptance_row(
                    "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
                    "01_fixture_archive_and_candidate_funnel",
                    69.0,
                    0,
                ),
                acceptance_row(
                    "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
                    "01_fixture_archive_and_candidate_funnel",
                    66.6,
                    0,
                ),
                acceptance_row(
                    "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
                    "02_parser_feature_bridge_contract",
                    104.2,
                    22,
                ),
                acceptance_row(
                    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "02_parser_feature_bridge_contract",
                    56.6,
                    19,
                ),
                acceptance_row(
                    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
                    "02_parser_feature_bridge_contract",
                    54.6,
                    1,
                ),
                acceptance_row(
                    "C02_POWER_GRID_DATACENTER_CAPEX",
                    "03_weighted_gate_validation_after_fields",
                    41.0,
                    44,
                ),
            ]
        }
        replay = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "role": "green",
                    "expected_outcome": "green",
                    "candidate": {"symbol": "000660", "as_of_date": "2024-04-30", "case_id": "hbm"},
                    "current_runtime_gap_status": "runtime_bridge_axes_missing",
                }
            ]
        }
        payload = build_v12_runtime_first_repair_slice(
            acceptance_spec_payload=acceptance,
            replay_spec_payload=replay,
        )
        selected = {row["canonical_archetype_id"] for row in payload["rows"]}

        self.assertIn("C06_HBM_MEMORY_CUSTOMER_CAPACITY", selected)
        self.assertIn("C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", selected)
        self.assertIn("C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", selected)
        self.assertIn("C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", selected)
        self.assertIn("C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", selected)
        self.assertIn("C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", selected)
        self.assertIn("C02_POWER_GRID_DATACENTER_CAPEX", selected)
        self.assertEqual(payload["summary"]["selected_hbm_or_samsung_related_count"], 2)
        self.assertGreaterEqual(payload["summary"]["selected_non_hbm_count"], 5)

        report = render_v12_runtime_first_repair_slice(payload)
        self.assertIn("첫 패치가 하닉만 Green으로 올리면 실패", report)
        self.assertIn("C21/C23/C26", report)


if __name__ == "__main__":
    unittest.main()
