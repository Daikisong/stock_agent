import unittest

from e2r.calibration.v12_fixture_candidate_funnel_audit import (
    build_v12_fixture_candidate_funnel_audit,
    render_v12_fixture_candidate_funnel_audit,
)


class V12FixtureCandidateFunnelAuditTests(unittest.TestCase):
    def test_audit_accepts_fixture_candidate_archetype_payload(self) -> None:
        spec_payload = {
            "archetypes": [
                {
                    "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
                    "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
                    "runtime_bridge_group": "industrial_backlog_margin_bridge",
                    "fixture_status": "ready_for_runtime_replay_fixture",
                    "green_fixture_candidate": {
                        "case_id": "C01_GREEN",
                        "symbol": "010140",
                        "trigger_date": "2025-02-06",
                        "trigger_type": "Stage3-Green",
                    },
                    "guard_fixture_candidate": {
                        "case_id": "C01_GUARD",
                        "symbol": "097230",
                        "trigger_date": "2024-03-06",
                        "trigger_type": "Stage2",
                    },
                }
            ]
        }
        discovered_candidates = [
            {
                "symbol": "010140",
                "company_name": "삼성중공업",
                "as_of_date": "2025-02-06",
                "stage": "2",
                "score": 71.0,
                "candidate_source_path": "official_cheap_scan",
                "layer": "event_search",
            },
            {
                "symbol": "097230",
                "company_name": "HJ중공업",
                "as_of_date": "2024-04-01",
                "stage": "1",
                "score": 20.0,
                "candidate_source_path": "official_cheap_scan",
                "layer": "event_search",
            },
        ]

        payload = build_v12_fixture_candidate_funnel_audit(
            spec_payload=spec_payload,
            discovered_candidates=discovered_candidates,
            replay_summary={"config": {"frequency": "monthly"}},
        )
        by_role = {row["role"]: row for row in payload["rows"]}

        self.assertEqual(payload["spec_row_count"], 2)
        self.assertEqual(
            by_role["green"]["fixture_funnel_status"],
            "exact_symbol_date_candidate_reached_runtime",
        )
        self.assertEqual(
            by_role["guard"]["fixture_funnel_status"],
            "symbol_reached_runtime_but_not_fixture_date",
        )

    def test_audit_splits_exact_symbol_only_and_absent_fixture_rows(self) -> None:
        spec_payload = {
            "rows": [
                {
                    "role": "green",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "current_runtime_gap_status": "runtime_bridge_axes_missing",
                    "candidate": {"symbol": "000660", "as_of_date": "2024-04-25", "case_id": "C06_GREEN"},
                },
                {
                    "role": "green",
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "current_runtime_gap_status": "runtime_stage3_gate_blocked",
                    "candidate": {"symbol": "267260", "as_of_date": "2024-02-01", "case_id": "C02_GREEN"},
                },
                {
                    "role": "green",
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "current_runtime_gap_status": "not_in_current_benchmark",
                    "candidate": {"symbol": "000810", "as_of_date": "2024-05-16", "case_id": "C21_GREEN"},
                },
            ]
        }
        discovered_candidates = [
            {
                "symbol": "000660",
                "company_name": "SK하이닉스",
                "as_of_date": "2024-05-01",
                "stage": "3-Yellow",
                "score": 76.7,
                "candidate_source_path": "official_cheap_scan",
                "layer": "event_search",
            },
            {
                "symbol": "267260",
                "company_name": "HD현대일렉트릭",
                "as_of_date": "2024-02-01",
                "stage": "2",
                "score": 66.3,
                "candidate_source_path": "official_cheap_scan",
                "layer": "event_search",
            },
        ]
        replay_summary = {
            "config": {
                "frequency": "monthly",
                "fixture_search": True,
                "live_search": False,
                "allow_snapshot_derived_universe": False,
            },
            "snapshots": [{"universe_count": 12}, {"universe_count": 12}],
        }

        payload = build_v12_fixture_candidate_funnel_audit(
            spec_payload=spec_payload,
            discovered_candidates=discovered_candidates,
            replay_summary=replay_summary,
        )
        by_symbol = {row["candidate"]["symbol"]: row for row in payload["rows"]}

        self.assertEqual(
            by_symbol["267260"]["fixture_funnel_status"],
            "exact_symbol_date_candidate_reached_runtime",
        )
        self.assertEqual(
            by_symbol["000660"]["fixture_funnel_status"],
            "symbol_reached_runtime_but_not_fixture_date",
        )
        self.assertEqual(
            by_symbol["000810"]["fixture_funnel_status"],
            "symbol_never_reached_current_runtime",
        )
        self.assertEqual(payload["fixture_funnel_status_counts"]["symbol_never_reached_current_runtime"], 1)
        report = render_v12_fixture_candidate_funnel_audit(payload)

        self.assertIn("점수가 낮은 문제와 후보가 아예 없는 문제를 분리", report)
        self.assertIn("monthly_schedule_or_fixture_date_mismatch", report)
        self.assertIn("benchmark_universe_or_official_cheap_scan_funnel_gap", report)


if __name__ == "__main__":
    unittest.main()
