import unittest

from e2r.calibration.v12_runtime_replay_spec import (
    build_v12_runtime_replay_spec,
    render_v12_runtime_replay_spec,
)


class V12RuntimeReplaySpecTests(unittest.TestCase):
    def test_replay_spec_materializes_green_and_guard_rows_with_current_gap(self) -> None:
        fixture_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                    "runtime_bridge_group": "semiconductor_customer_capacity_bridge",
                    "fixture_status": "ready_for_runtime_replay_fixture",
                    "expected_runtime_primitives": ["customer_preorder_or_allocation", "hbm_capacity_constraint"],
                    "green_fixture_candidate": {
                        "case_id": "C06_GREEN",
                        "symbol": "000660",
                        "trigger_date": "2024-04-25",
                        "trigger_type": "Stage3-Green",
                    },
                    "guard_fixture_candidate": {
                        "case_id": "C06_GUARD",
                        "symbol": "005930",
                        "trigger_date": "2024-04-05",
                        "trigger_type": "Stage3-Yellow",
                    },
                },
                {
                    "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
                    "fixture_status": "needs_green_row",
                },
                {
                    "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
                    "fixture_status": "needs_green_row",
                    "guard_fixture_candidate": {
                        "case_id": "R13_GUARD",
                        "symbol": "003550",
                        "trigger_date": "2024-02-26",
                        "trigger_type": "Stage4B",
                    },
                },
            ]
        }
        coverage_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "required_bridge_axes": ["customer", "backlog", "contract"],
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "runtime_candidate_count": 2,
                    "runtime_stage_distribution": {"3-Yellow": 2},
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                    "top_failed_gates": [{"gate": "failed_stage3_bottleneck", "count": 2}],
                }
            ]
        }

        payload = build_v12_runtime_replay_spec(
            fixture_payload=fixture_payload,
            coverage_payload=coverage_payload,
        )

        self.assertEqual(payload["spec_row_count"], 3)
        self.assertEqual(payload["ready_archetype_count"], 1)
        self.assertEqual(payload["covered_archetype_count"], 2)
        self.assertEqual(payload["role_counts"], {"green": 1, "guard": 2})
        self.assertEqual(payload["current_runtime_gap_status_counts"], {None: 1, "runtime_bridge_axes_missing": 2})
        self.assertEqual(payload["skipped_archetypes"][0]["canonical_archetype_id"], "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY")
        self.assertEqual(payload["skipped_archetypes"][1]["included_roles"], ["guard"])
        green = next(row for row in payload["rows"] if row["role"] == "green")
        self.assertEqual(green["expected_outcome"], "green_candidate_should_reach_stage3_green_or_emit_field_level_deficit")
        self.assertEqual(green["current_missing_required_bridge_axes"], ["backlog", "contract"])
        self.assertEqual(green["candidate"]["case_id"], "C06_GREEN")

        report = render_v12_runtime_replay_spec(payload)
        self.assertIn("C06_HBM_MEMORY_CUSTOMER_CAPACITY", report)
        self.assertIn("runtime_bridge_axes_missing", report)

    def test_replay_spec_does_not_turn_yellow_candidate_into_green_row(self) -> None:
        fixture_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
                    "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
                    "runtime_bridge_group": "battery_mobility_contract_bridge",
                    "fixture_status": "ready_for_runtime_replay_fixture",
                    "expected_runtime_primitives": ["customer_contract", "volume_visibility"],
                    "green_fixture_candidate": {
                        "case_id": "C12_YELLOW",
                        "symbol": "348370",
                        "trigger_date": "2024-01-25",
                        "trigger_type": "Stage3-Yellow",
                    },
                    "guard_fixture_candidate": {
                        "case_id": "C12_GUARD",
                        "symbol": "093370",
                        "trigger_date": "2023-04-17",
                        "trigger_type": "Stage4C",
                    },
                }
            ]
        }

        payload = build_v12_runtime_replay_spec(
            fixture_payload=fixture_payload,
            coverage_payload={"archetypes": []},
        )

        self.assertEqual(payload["role_counts"], {"guard": 1})
        self.assertEqual(payload["rows"][0]["role"], "guard")
        self.assertEqual(
            payload["skipped_archetypes"][0]["skip_reason"],
            "green_replay_role_requires_raw_stage3_green_trigger",
        )


if __name__ == "__main__":
    unittest.main()
