import json
from pathlib import Path
import tempfile
import unittest

from e2r.calibration.v12_research_ledger_operational_parity import (
    build_archive_coverage_from_spec,
    build_v12_research_ledger_operational_parity_audit,
    render_v12_research_ledger_operational_parity_audit,
    write_v12_research_ledger_operational_parity_audit,
)


class V12ResearchLedgerOperationalParityTests(unittest.TestCase):
    def test_audit_classifies_candidate_funnel_and_score_gap(self) -> None:
        spec_payload = {
            "rows": [
                _spec_row("green", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "000660", "2024-04-25"),
                _spec_row("green", "C02_POWER_GRID_DATACENTER_CAPEX", "267260", "2024-02-16"),
                _spec_row("green", "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "010140", "2025-02-06"),
                _spec_row("guard", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "005930", "2024-07-11"),
                _spec_row("guard", "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "080580", "2024-01-23"),
            ]
        }
        operational = [
            {
                **_candidate("000660", "2024-04-25", "official_cheap_scan", "3-Green", 90.0),
                "evidence_contract_coverage_pct": 100.0,
                "evidence_contract_positive_coverage_pct": 100.0,
                "evidence_contract_positive_missing_primitive_count": 0.0,
                "evidence_contract_guard_present_primitive_count": 0.0,
                "evidence_contract_guard_missing_primitive_count": 1.0,
                "evidence_contract_positive_missing_primitives": "",
                "evidence_contract_guard_present_primitives": "",
                "evidence_contract_guard_missing_primitives": "cost_overrun",
            },
            _candidate("267260", "2024-02-16", "official_cheap_scan", "2", 72.0),
            _candidate("005930", "2024-07-11", "official_cheap_scan", "3-Yellow", 84.0),
            _candidate("080580", "2024-01-23", "official_cheap_scan", "3-Green", 89.0),
        ]
        ledger = [
            _fixture("000660", "2024-04-25", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "3-Green", 97.5),
            _fixture("267260", "2024-02-16", "C02_POWER_GRID_DATACENTER_CAPEX", "3-Green", 95.0),
            _fixture("010140", "2025-02-06", "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "3-Green", 97.0),
            _fixture("005930", "2024-07-11", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "1", 49.0, role="guard"),
            _fixture("080580", "2024-01-23", "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "1", 12.0, role="guard"),
            _fixture(
                "000660",
                "2024-04-30",
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "3-Green",
                98.0,
                carried=True,
            ),
        ]

        payload = build_v12_research_ledger_operational_parity_audit(
            spec_payload=spec_payload,
            operational_candidates=operational,
            ledger_candidates=ledger,
            archive_coverage=[
                {
                    "symbol": "010140",
                    "as_of_date": "2025-02-06",
                    "universe_present": False,
                    "price_count": 0,
                    "financial_count": 0,
                    "disclosure_count": 0,
                }
            ],
            near_score_tolerance=5.0,
        )

        self.assertEqual(payload["summary"]["green_case_count"], 3)
        self.assertEqual(
            payload["summary"]["green_bucket_counts"],
            {
                "ledger_only_green": 1,
                "operational_green_score_gap": 1,
                "operational_missing": 1,
            },
        )
        self.assertEqual(payload["summary"]["green_missing_lane_counts"], {"archive_universe_missing": 1})
        self.assertEqual(payload["summary"]["guard_bucket_counts"], {"guard_fail_false_green": 1, "guard_pass": 1})
        self.assertEqual(payload["summary"]["carried_fixture_count"], 1)
        self.assertEqual(payload["carried_summary"][0]["fixture_green"], 1)
        first_green = next(row for row in payload["green_rows"] if row["symbol"] == "000660")
        self.assertEqual(first_green["operational_contract_positive_coverage_pct"], 100.0)
        self.assertEqual(first_green["operational_contract_positive_missing_primitive_count"], 0.0)
        self.assertEqual(first_green["operational_contract_guard_missing_primitive_count"], 1.0)
        self.assertEqual(first_green["operational_contract_guard_missing_primitives"], "cost_overrun")

        report = render_v12_research_ledger_operational_parity_audit(payload)
        self.assertIn("operational_missing", report)
        self.assertIn("ledger_only_green", report)
        self.assertIn("operational_green_score_gap", report)
        self.assertIn("pos_cov=100.0", report)
        self.assertIn("guard_missing=1.0", report)

    def test_writer_outputs_json_and_markdown(self) -> None:
        spec_payload = {"rows": [_spec_row("green", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "000660", "2024-04-25")]}
        operational = [_candidate("000660", "2024-04-25", "official_cheap_scan", "3-Green", 90.0)]
        ledger = [_fixture("000660", "2024-04-25", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "3-Green", 97.5)]

        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            spec_path = root_path / "spec.json"
            op_path = root_path / "op.json"
            ledger_path = root_path / "ledger.json"
            spec_path.write_text(json.dumps(spec_payload), encoding="utf-8")
            op_path.write_text(json.dumps(operational), encoding="utf-8")
            ledger_path.write_text(json.dumps(ledger), encoding="utf-8")

            paths = write_v12_research_ledger_operational_parity_audit(
                spec_path=spec_path,
                operational_candidates_path=op_path,
                ledger_candidates_path=ledger_path,
                output_json_path=root_path / "audit.json",
                output_markdown_path=root_path / "audit.md",
            )

            payload = json.loads(paths["json"].read_text(encoding="utf-8"))
            markdown = paths["markdown"].read_text(encoding="utf-8")

        self.assertEqual(payload["summary"]["green_bucket_counts"], {"operational_green_score_gap": 1})
        self.assertIn("V12 Research-Ledger Operational Parity Audit", markdown)

    def test_r13_green_can_match_source_archetype_fixture(self) -> None:
        spec_payload = {
            "rows": [
                _spec_row("green", "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "000100", "2024-08-20"),
                _spec_row("guard", "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "003230", "2024-06-18"),
            ]
        }
        operational = [
            _candidate("000100", "2024-08-20", "report_radar", "3-Green", 92.25),
            _candidate("003230", "2024-06-18", "report_radar", "1", 48.0),
        ]
        ledger = [
            _fixture("000100", "2024-08-20", "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "3-Green", 91.17),
            _fixture("003230", "2024-06-18", "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "3-Green", 93.0),
        ]

        payload = build_v12_research_ledger_operational_parity_audit(
            spec_payload=spec_payload,
            operational_candidates=operational,
            ledger_candidates=ledger,
            near_score_tolerance=5.0,
        )

        green = payload["green_rows"][0]
        guard = payload["guard_rows"][0]
        self.assertEqual(green["bucket"], "near_parity_green")
        self.assertEqual(green["ledger_match_mode"], "source_archetype_fallback")
        self.assertEqual(green["ledger_matched_archetype"], "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION")
        self.assertEqual(guard["bucket"], "guard_pass")
        self.assertIsNone(guard["ledger_match_mode"])

    def test_operational_green_must_match_non_r13_archetype_when_available(self) -> None:
        spec_payload = {"rows": [_spec_row("green", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "000660", "2024-04-25")]}
        operational = [
            {
                **_candidate("000660", "2024-04-25", "report_radar", "3-Green", 97.4),
                "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
            }
        ]
        ledger = [_fixture("000660", "2024-04-25", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "3-Green", 97.5)]

        payload = build_v12_research_ledger_operational_parity_audit(
            spec_payload=spec_payload,
            operational_candidates=operational,
            ledger_candidates=ledger,
            near_score_tolerance=5.0,
        )

        row = payload["green_rows"][0]
        self.assertEqual(row["bucket"], "operational_archetype_mismatch")
        self.assertEqual(row["operational_matched_archetype"], "C02_POWER_GRID_DATACENTER_CAPEX")
        self.assertFalse(row["operational_archetype_match"])

    def test_carried_forward_fixture_is_not_counted_as_exact_green_parity(self) -> None:
        spec_payload = {"rows": [_spec_row("green", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "000660", "2024-04-30")]}
        operational = [_candidate("000660", "2024-04-30", "report_radar", "3-Green", 98.2804)]
        ledger = [
            _fixture(
                "000660",
                "2024-04-30",
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "3-Green",
                97.9877,
                carried=True,
            )
        ]

        payload = build_v12_research_ledger_operational_parity_audit(
            spec_payload=spec_payload,
            operational_candidates=operational,
            ledger_candidates=ledger,
            near_score_tolerance=5.0,
        )

        row = payload["green_rows"][0]
        self.assertEqual(row["bucket"], "fixture_missing")
        self.assertEqual(row["operational_stage"], "3-Green")
        self.assertEqual(row["operational_score"], 98.2804)
        self.assertEqual(row["ledger_stage"], "missing")
        self.assertEqual(payload["summary"]["carried_fixture_count"], 1)
        self.assertEqual(payload["carried_summary"][0]["fixture_green"], 1)
        self.assertEqual(payload["carried_summary"][0]["operational_green"], 1)

    def test_archive_coverage_from_spec_marks_universe_and_price_gaps(self) -> None:
        spec_payload = {
            "rows": [
                _spec_row("green", "C02_POWER_GRID_DATACENTER_CAPEX", "267260", "2024-02-16"),
                _spec_row("green", "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "010140", "2025-02-06"),
            ]
        }
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            (root_path / "universe").mkdir(parents=True)
            (root_path / "universe" / "universe.csv").write_text(
                "symbol,name,market,exchange,listed_date\n"
                "267260,HD현대일렉트릭,KR,KRX,2017-05-10\n",
                encoding="utf-8",
            )

            rows = build_archive_coverage_from_spec(spec_payload, official_root=root_path)

        by_symbol = {row["symbol"]: row for row in rows}
        self.assertTrue(by_symbol["267260"]["universe_present"])
        self.assertEqual(by_symbol["267260"]["price_count"], 0)
        self.assertFalse(by_symbol["010140"]["universe_present"])


def _spec_row(role: str, archetype: str, symbol: str, as_of_date: str) -> dict:
    return {
        "role": role,
        "canonical_archetype_id": archetype,
        "candidate": {"symbol": symbol, "as_of_date": as_of_date},
    }


def _candidate(symbol: str, as_of_date: str, source: str, stage: str, score: float) -> dict:
    return {
        "symbol": symbol,
        "as_of_date": as_of_date,
        "candidate_source_path": source,
        "stage": stage,
        "score": score,
    }


def _fixture(
    symbol: str,
    as_of_date: str,
    archetype: str,
    stage: str,
    score: float,
    *,
    role: str = "green",
    carried: bool = False,
) -> dict:
    codes = ["V12_RUNTIME_FIXTURE_SPEC", archetype, f"fixture_role:{role}", f"fixture_source_date:{as_of_date}"]
    if carried:
        codes.append("fixture_carried_forward")
    return {
        "symbol": symbol,
        "as_of_date": as_of_date,
        "candidate_source_path": "runtime_fixture_spec",
        "reason_codes": codes,
        "stage": stage,
        "score": score,
    }


if __name__ == "__main__":
    unittest.main()
