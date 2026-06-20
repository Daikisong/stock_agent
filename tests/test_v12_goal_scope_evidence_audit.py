import unittest

from e2r.calibration.v12_goal_scope_evidence_audit import (
    build_v12_goal_scope_evidence_audit,
    render_v12_goal_scope_evidence_audit,
)


class V12GoalScopeEvidenceAuditTests(unittest.TestCase):
    def test_audit_maps_original_questions_to_existing_evidence(self) -> None:
        component_payload = {
            "summary": {
                "candidate_row_count": 3,
                "runtime_exercised_archetype_count": 2,
                "runtime_unexercised_archetype_count": 34,
                "stage3_green_count": 0,
                "global_average_component_losses": [
                    {"component": "bottleneck_pricing", "avg_loss_points": 10.2},
                    {"component": "earnings_visibility", "avg_loss_points": 9.5},
                    {"component": "information_confidence", "avg_loss_points": 6.2},
                ],
            },
            "focus_rows": [
                {
                    "symbol": "000660",
                    "green_shortfall_to_87": 10.2361,
                    "components": [
                        {"component": "eps_fcf_explosion", "loss_points": 0.0},
                        {"component": "bottleneck_pricing", "loss_points": 7.9478},
                    ],
                },
                {
                    "symbol": "005930",
                    "green_shortfall_to_87": 18.3248,
                    "components": [
                        {"component": "eps_fcf_explosion", "loss_points": 0.0},
                        {"component": "information_confidence", "loss_points": 7.6},
                    ],
                },
            ],
        }
        historical_payload = {
            "summary": {
                "score_simulation_row_count": 9052,
                "historical_stage3_green_after_case_count": 331,
                "historical_green_archetype_count": 30,
            }
        }
        current_census_payload = {
            "summary": {
                "runtime_exercised_archetype_count": 8,
                "runtime_unexercised_archetype_count": 28,
                "stage3_green_count": 0,
            }
        }
        weight_payload = {
            "summary": {
                "total_archetype_support_rows": 12471,
                "total_archetype_positive_cases": 1495,
                "total_archetype_counterexamples": 2628,
                "archetype_weight_count": 36,
            }
        }
        execution_payload = {
            "summary": {
                "stop_layer_counts": {
                    "candidate_replay_archive": 26,
                    "parser_feature_bridge": 6,
                    "stage_gate": 1,
                }
            }
        }
        cross_trace_payload = {
            "loss_layer_counts_by_archetype": {
                "candidate_funnel_or_replay_coverage": 24,
                "research_axis_to_runtime_field_translation": 6,
                "weighted_component_or_stage3_gate": 1,
            }
        }
        axis_contract_payload = {
            "summary": {
                "top40_contract_status_counts": {
                    "requires_axis_bridge_to_runtime_primitives": 30,
                    "missing_axis_bridge_contract": 9,
                    "exact_derived_metric_only": 1,
                }
            }
        }
        acceptance_payload = {
            "summary": {
                "acceptance_status_counts": {
                    "blocked_missing_exact_fixture_archive_or_candidate_funnel": 26,
                    "blocked_missing_parser_feature_or_gate_axis_contract": 6,
                    "blocked_weighted_gate_after_fields_present": 1,
                }
            }
        }

        payload = build_v12_goal_scope_evidence_audit(
            component_payload=component_payload,
            historical_payload=historical_payload,
            current_census_payload=current_census_payload,
            weight_payload=weight_payload,
            execution_payload=execution_payload,
            cross_trace_payload=cross_trace_payload,
            axis_contract_payload=axis_contract_payload,
            acceptance_payload=acceptance_payload,
        )

        self.assertEqual(payload["summary"]["requirement_count"], 8)
        self.assertEqual(payload["summary"]["current_stage3_green_count"], 0)
        self.assertEqual(payload["summary"]["historical_stage3_green_after_case_count"], 331)
        self.assertEqual(payload["summary"]["research_support_rows"], 12471)
        self.assertEqual(
            payload["summary"]["investigation_completion_status"],
            "complete_for_root_cause_investigation",
        )
        self.assertEqual(
            payload["summary"]["implementation_repair_status"],
            "not_complete_and_tracked_as_acceptance_blockers",
        )
        self.assertIn("proved", payload["summary"]["requirement_status_counts"])
        self.assertIn("proved_but_weight_layer_only", payload["summary"]["requirement_status_counts"])

        rows = {row["requirement_id"]: row for row in payload["requirement_rows"]}
        self.assertIn("10.2361", rows["R1_samsung_hynix_score_cut_location"]["plain_answer"])
        self.assertIn("weight는 배점표", rows["R3_research_accumulated_into_weights"]["remaining_work"])
        self.assertIn("수리 자체는 아직 완료가 아니다", rows["R6_systemic_failure_layers"]["remaining_work"])

        report = render_v12_goal_scope_evidence_audit(payload)
        self.assertIn("원래 질문을 요구사항으로", report)
        self.assertIn("HBM 보너스가 아니라", report)
        self.assertIn("원인 조사는 완료", report)
        self.assertIn("exact replay archive", report)


if __name__ == "__main__":
    unittest.main()
