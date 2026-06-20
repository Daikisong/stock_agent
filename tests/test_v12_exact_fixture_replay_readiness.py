import unittest

from e2r.calibration.v12_exact_fixture_replay_readiness import (
    build_v12_exact_fixture_replay_readiness,
    render_v12_exact_fixture_replay_readiness,
)


class V12ExactFixtureReplayReadinessTests(unittest.TestCase):
    def test_readiness_accepts_fixture_candidate_archetype_payload(self) -> None:
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
                },
                {
                    "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
                    "fixture_status": "needs_verified_green_source",
                    "green_fixture_candidate": {
                        "case_id": "C03_UNREADY",
                        "symbol": "012450",
                        "trigger_date": "2024-02-01",
                    },
                },
            ]
        }
        universe_rows = [
            {"symbol": "010140", "listed_date": "2000-01-01"},
            {"symbol": "097230", "listed_date": "2000-01-01"},
        ]
        price_rows = [
            {"symbol": "010140", "date": "2025-02-06", "as_of_date": "2025-02-06"},
            {"symbol": "097230", "date": "2024-03-06", "as_of_date": "2024-03-06"},
        ]
        search_snapshots = [
            {"symbol": "010140", "search_date": "2025-02-06", "published_at": "2025-02-06T08:00:00"},
            {"symbol": "097230", "search_date": "2024-03-06", "published_at": "2024-03-06T08:00:00"},
        ]
        report_snapshots = [
            {"symbol": "010140", "as_of_date": "2025-02-06"},
            {"symbol": "097230", "as_of_date": "2024-03-06"},
        ]

        payload = build_v12_exact_fixture_replay_readiness(
            spec_payload=spec_payload,
            universe_rows=universe_rows,
            price_rows=price_rows,
            financial_rows=[],
            disclosure_rows=[],
            search_snapshots=search_snapshots,
            report_snapshots=report_snapshots,
        )

        self.assertEqual(payload["spec_row_count"], 2)
        self.assertEqual(payload["archetype_pair_summary"]["archetype_count"], 1)
        self.assertEqual(payload["archetype_pair_summary"]["pair_retrospective_ready_count"], 1)
        self.assertEqual(payload["archetype_pair_summary"]["pair_strict_pit_ready_count"], 1)
        self.assertEqual({row["role"] for row in payload["rows"]}, {"green", "guard"})
        self.assertEqual({row["candidate"]["as_of_date"] for row in payload["rows"]}, {"2025-02-06", "2024-03-06"})

    def test_readiness_splits_retrospective_and_strict_pit_inputs(self) -> None:
        spec_payload = {
            "rows": [
                {
                    "role": "green",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "candidate": {
                        "case_id": "C06_GREEN",
                        "symbol": "000660",
                        "as_of_date": "2024-04-25",
                        "trigger_type": "Stage3-Green",
                    },
                },
                {
                    "role": "green",
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "candidate": {
                        "case_id": "C02_GREEN",
                        "symbol": "267260",
                        "as_of_date": "2024-02-16",
                        "trigger_type": "Stage3-Green",
                    },
                },
                {
                    "role": "guard",
                    "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
                    "candidate": {
                        "case_id": "C21_GUARD",
                        "symbol": "000810",
                        "as_of_date": "2024-05-16",
                        "trigger_type": "Stage2",
                    },
                },
            ]
        }
        universe_rows = [
            {"symbol": "000660", "listed_date": "1996-12-26"},
            {"symbol": "267260", "listed_date": "2017-05-10"},
        ]
        price_rows = [
            {"symbol": "000660", "date": "2024-03-15", "as_of_date": "2024-03-15"},
            {"symbol": "267260", "date": "2023-07-27", "as_of_date": "2023-07-27"},
            {"symbol": "267260", "date": "2024-02-16", "as_of_date": "2024-02-16"},
        ]
        search_snapshots = [
            {
                "symbol": "000660",
                "search_date": "2026-05-14",
                "published_at": "2024-04-01T08:00:00",
            },
            {
                "symbol": "267260",
                "search_date": "2023-07-27",
                "published_at": "2023-07-27T08:00:00",
            },
        ]
        report_snapshots = [
            {"symbol": "000660", "as_of_date": "2024-04-01"},
            {"symbol": "267260", "as_of_date": "2023-07-27"},
        ]

        payload = build_v12_exact_fixture_replay_readiness(
            spec_payload=spec_payload,
            universe_rows=universe_rows,
            price_rows=price_rows,
            financial_rows=[],
            disclosure_rows=[],
            search_snapshots=search_snapshots,
            report_snapshots=report_snapshots,
        )
        by_symbol = {row["candidate"]["symbol"]: row for row in payload["rows"]}

        self.assertEqual(
            by_symbol["000660"]["retrospective_readiness_status"],
            "ready_retrospective_exact_replay",
        )
        self.assertEqual(
            by_symbol["000660"]["strict_pit_readiness_status"],
            "missing_research_snapshot_inputs",
        )
        self.assertEqual(by_symbol["267260"]["strict_pit_readiness_status"], "ready_strict_pit_exact_replay")
        self.assertEqual(
            by_symbol["000810"]["retrospective_readiness_status"],
            "missing_official_and_research_inputs",
        )
        self.assertEqual(payload["retrospective_ready_count"], 2)
        self.assertEqual(payload["strict_pit_ready_count"], 1)
        self.assertEqual(payload["archetype_pair_summary"]["pair_retrospective_ready_count"], 0)

        report = render_v12_exact_fixture_replay_readiness(payload)
        self.assertIn("HBM 전용 보정이 아니라 전 아키타입", report)
        self.assertIn("ready_retrospective_exact_replay", report)
        self.assertIn("strict PIT discovery", report)

    def test_stale_price_history_does_not_count_as_exact_replay_ready(self) -> None:
        spec_payload = {
            "rows": [
                {
                    "role": "green",
                    "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
                    "candidate": {
                        "case_id": "C02_GREEN",
                        "symbol": "267260",
                        "as_of_date": "2024-02-16",
                        "trigger_type": "Stage3-Green",
                    },
                },
            ]
        }

        payload = build_v12_exact_fixture_replay_readiness(
            spec_payload=spec_payload,
            universe_rows=[{"symbol": "267260", "listed_date": "2017-05-10"}],
            price_rows=[{"symbol": "267260", "date": "2023-07-27", "as_of_date": "2023-07-27"}],
            financial_rows=[],
            disclosure_rows=[],
            search_snapshots=[
                {"symbol": "267260", "search_date": "2024-02-16", "published_at": "2024-02-16T08:00:00"}
            ],
            report_snapshots=[{"symbol": "267260", "as_of_date": "2024-02-16"}],
        )
        row = payload["rows"][0]

        self.assertEqual(row["retrospective_readiness_status"], "missing_candidate_generation_inputs")
        self.assertEqual(row["strict_pit_readiness_status"], "missing_candidate_generation_inputs")
        self.assertEqual(row["retrospective_missing_inputs"], ["recent_price_history_45d"])
        self.assertEqual(row["strict_pit_missing_inputs"], ["recent_price_history_45d"])

    def test_evidence_url_fixture_requires_matching_source_snapshots(self) -> None:
        spec_payload = {
            "rows": [
                {
                    "role": "green",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "candidate": {
                        "case_id": "C06_GREEN",
                        "symbol": "000660",
                        "as_of_date": "2024-04-25",
                        "trigger_type": "Stage3-Green",
                        "evidence_source": "https://reuters.example.com/sk-hynix-q1-profit",
                    },
                },
            ]
        }
        common_kwargs = {
            "spec_payload": spec_payload,
            "universe_rows": [{"symbol": "000660", "listed_date": "1996-12-26"}],
            "price_rows": [{"symbol": "000660", "date": "2024-04-25", "as_of_date": "2024-04-25"}],
            "financial_rows": [],
            "disclosure_rows": [],
        }
        mismatched = build_v12_exact_fixture_replay_readiness(
            **common_kwargs,
            search_snapshots=[
                {
                    "symbol": "000660",
                    "search_date": "2024-04-25",
                    "published_at": "2024-04-25T08:00:00",
                    "url": "https://broker.example.com/sk-hynix-memory.pdf",
                }
            ],
            report_snapshots=[
                {
                    "symbol": "000660",
                    "as_of_date": "2024-04-25",
                    "url": "https://broker.example.com/sk-hynix-memory.pdf",
                }
            ],
        )
        mismatched_row = mismatched["rows"][0]

        self.assertEqual(mismatched_row["retrospective_readiness_status"], "missing_research_snapshot_inputs")
        self.assertEqual(
            mismatched_row["retrospective_missing_inputs"],
            ["evidence_source_search_snapshot", "evidence_source_report_text_snapshot"],
        )
        self.assertEqual(mismatched_row["input_counts"]["symbol_search_snapshots"], 1)
        self.assertEqual(mismatched_row["input_counts"]["retrospective_search_snapshots"], 0)

        matched = build_v12_exact_fixture_replay_readiness(
            **common_kwargs,
            search_snapshots=[
                {
                    "symbol": "000660",
                    "search_date": "2024-04-25",
                    "published_at": "2024-04-25T08:00:00",
                    "url": "https://reuters.example.com/sk-hynix-q1-profit",
                }
            ],
            report_snapshots=[
                {
                    "symbol": "000660",
                    "as_of_date": "2024-04-25",
                    "url": "https://reuters.example.com/sk-hynix-q1-profit",
                }
            ],
        )
        self.assertEqual(matched["rows"][0]["retrospective_readiness_status"], "ready_retrospective_exact_replay")
        self.assertEqual(matched["rows"][0]["strict_pit_readiness_status"], "ready_strict_pit_exact_replay")


if __name__ == "__main__":
    unittest.main()
