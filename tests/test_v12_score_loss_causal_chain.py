import unittest

from e2r.calibration.v12_score_loss_causal_chain import (
    build_v12_score_loss_causal_chain,
    render_v12_score_loss_causal_chain,
)


class V12ScoreLossCausalChainTests(unittest.TestCase):
    def test_chain_splits_hbm_bridge_candidate_and_gate_failures(self) -> None:
        hbm_signal = {
            "symbol_rows": [
                {
                    "symbol": "000660",
                    "company_label": "SK하이닉스",
                    "research_hbm_row_count": 10,
                    "research_raw_stage3_green_count": 2,
                    "research_positive_or_green_worthy_count": 4,
                    "positive_signal_counts": {"capacity_lock": 3, "order_or_contract": 2},
                    "gap_signals": ["capacity_lock", "order_or_contract"],
                    "runtime_best_row": {
                        "current_stage": "3-Yellow",
                        "current_score": "76.7",
                        "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "revision_score": "100",
                        "research_axis_bridge_margin": "100",
                        "research_axis_bridge_customer": "100",
                        "research_axis_bridge_backlog": "0",
                        "research_axis_bridge_contract": "0",
                        "capa_constraint": "0",
                        "green_gate_deficit_summary": "total:76.7/87.0(-10.3); bottleneck:-3.2",
                    },
                }
            ]
        }
        archetype_signal = {
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "research_clean_green_count": 2,
                    "research_raw_stage3_green_count": 3,
                    "runtime_gap_status": "runtime_bridge_axes_missing",
                    "runtime_candidate_count": 19,
                    "runtime_max_score": 76.7,
                    "missing_required_bridge_axes": ["backlog", "contract"],
                    "diagnosis": "research_signal_not_structured_into_runtime_fields",
                    "runtime_best_row": {
                        "current_stage": "3-Yellow",
                        "current_score": "76.7",
                        "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "research_axis_bridge_backlog": "0",
                        "research_axis_bridge_contract": "0",
                    },
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "research_clean_green_count": 5,
                    "research_raw_stage3_green_count": 6,
                    "runtime_gap_status": "not_in_current_benchmark",
                    "runtime_candidate_count": 0,
                    "missing_required_bridge_axes": ["capital_return"],
                    "diagnosis": "research_green_fixture_not_archived_for_runtime_replay",
                    "runtime_best_row": None,
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "research_clean_green_count": 1,
                    "research_raw_stage3_green_count": 1,
                    "runtime_gap_status": "runtime_stage3_gate_blocked",
                    "runtime_candidate_count": 4,
                    "runtime_max_score": 72.9,
                    "missing_required_bridge_axes": [],
                    "diagnosis": "weighted_stage3_gate_blocks_after_fields_present",
                    "runtime_best_row": {
                        "current_stage": "2",
                        "current_score": "72.9",
                        "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                        "research_axis_bridge_backlog": "100",
                        "research_axis_bridge_contract": "100",
                        "green_gate_deficit_summary": "total:72.9/87.0(-14.1)",
                    },
                },
            ]
        }
        weight_audit = {
            "rows": [
                {"canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "weight_support_row_count": 10},
                {"canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "weight_support_row_count": 20},
                {"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "weight_support_row_count": 30},
            ]
        }
        execution_path = {
            "summary": {
                "research_support_rows": 60,
                "research_positive_cases": 12,
                "research_counterexamples": 8,
                "archetype_weight_count": 3,
                "runtime_gap_status_counts": {"not_in_current_benchmark": 1},
            },
            "archetype_rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "stop_layer": "parser_feature_bridge",
                    "next_fix": "bridge fields",
                },
                {
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "stop_layer": "candidate_replay_archive",
                    "next_fix": "fixture archive",
                },
                {
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "stop_layer": "stage_gate",
                    "next_fix": "gate validation",
                },
            ],
        }
        input_manifest = {
            "summary": {"role_gap_class_counts": {"archive_or_candidate_funnel_missing": 1}},
            "rows": [
                {
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "role_gap_classes": ["strict_pit_research_snapshot_missing"],
                }
            ],
        }

        payload = build_v12_score_loss_causal_chain(
            hbm_signal_payload=hbm_signal,
            archetype_signal_payload=archetype_signal,
            weight_audit_payload=weight_audit,
            execution_path_payload=execution_path,
            input_gap_manifest_payload=input_manifest,
        )
        by_arch = {row["canonical_archetype_id"]: row for row in payload["focus_archetype_rows"]}

        self.assertEqual(by_arch["C06_HBM_MEMORY_CUSTOMER_CAPACITY"]["stop_layer"], "parser_feature_bridge")
        self.assertEqual(by_arch["C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN"]["stop_layer"], "candidate_replay_archive")
        self.assertEqual(by_arch["C02_POWER_GRID_DATACENTER_CAPEX"]["stop_layer"], "stage_gate")
        self.assertIn("research_axis_bridge_contract", payload["hbm_symbol_rows"][0]["runtime_zero_or_missing_bridge_fields"])
        self.assertIn("점수표가 누적 연구를 잊은 것이 아니다", payload["summary"]["plain_answer"])

        report = render_v12_score_loss_causal_chain(payload)
        self.assertIn("total/bottleneck gate", report)
        self.assertIn("시험지가 current replay에 없다", report)
        self.assertIn("하닉/삼전만 좋아지는 패치는 실패", report)


if __name__ == "__main__":
    unittest.main()
