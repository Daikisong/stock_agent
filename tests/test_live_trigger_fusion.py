from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    BaselineLane,
    BaselineLaneRecord,
    BaselineLaneStatus,
    CurrentStateBootstrapper,
    CurrentStateEvent,
    CurrentTriggerFusion,
    EventLifecycleStatus,
    LiveUniverseRow,
    TriggerFusionConfig,
    TriggerSignal,
    TriggerType,
    load_candidate_events,
    load_trigger_signals,
    write_trigger_fusion,
)


def _universe(symbol: str, name: str, market: str) -> LiveUniverseRow:
    endpoint = "stk_isu_base_info" if market == "KOSPI" else "ksq_isu_base_info"
    return LiveUniverseRow(
        symbol=symbol,
        company_name=name,
        market=market,
        security_group="주권",
        stock_certificate_type="보통주",
        sector_type="",
        listing_date="2020-01-01",
        listing_status="LISTED",
        source_effective_date="2026-07-09",
        source_url=f"https://data-dbg.krx.co.kr/svc/apis/sto/{endpoint}",
        source_document_id=f"KRX-UNIVERSE-{symbol}",
        source_content_hash="a" * 64,
        source_request_id="KRX-REQUEST",
        source_mode="LIVE_OFFICIAL_API",
        eligible=True,
        exclusion_reason=None,
        raw_fields={},
    )


def _lane(
    symbol: str,
    name: str,
    market: str,
    lane: BaselineLane,
    *,
    status: BaselineLaneStatus = BaselineLaneStatus.NO_RESULT,
    values=None,
) -> BaselineLaneRecord:
    return BaselineLaneRecord(
        lane_id=f"LANE-{symbol}-{lane.value}",
        target_id=symbol,
        target_name=name,
        market=market,
        lane=lane.value,
        status=status.value,
        observed_date="2026-07-10",
        provider_names=(
            ("KRX", "OpenDART")
            if lane == BaselineLane.RISK
            else ("KRX",)
            if lane == BaselineLane.PRICE
            else ("OpenDART",)
            if lane == BaselineLane.OFFICIAL
            else ("ExistingLedger",)
        ),
        source_ids=(f"SOURCE-{symbol}-{lane.value}",),
        values=values or {},
    )


def _lanes():
    return (
        _lane(
            "005930",
            "삼성전자",
            "KOSPI",
            BaselineLane.OFFICIAL,
            status=BaselineLaneStatus.PARTIAL_HISTORY_PENDING,
            values={
                "latest_material_event": {
                    "rcept_no": "20260710000001",
                    "rcept_date": "2026-07-10",
                    "report_name": "단일판매ㆍ공급계약체결",
                    "corp_code": "00126380",
                }
            },
        ),
        _lane(
            "005930",
            "삼성전자",
            "KOSPI",
            BaselineLane.PRICE,
            status=BaselineLaneStatus.OBSERVED,
            values={
                "price_date": "2026-07-09",
                "return_pct": 2.0,
                "trading_value": 5_000_000_000,
            },
        ),
        _lane("005930", "삼성전자", "KOSPI", BaselineLane.RISK),
        _lane(
            "005930",
            "삼성전자",
            "KOSPI",
            BaselineLane.EXISTING_LEDGER,
            status=BaselineLaneStatus.OBSERVED,
            values={"accepted_current_claim_ids": ["CLAIM-005930"]},
        ),
        _lane("000660", "SK하이닉스", "KOSDAQ", BaselineLane.OFFICIAL),
        _lane(
            "000660",
            "SK하이닉스",
            "KOSDAQ",
            BaselineLane.PRICE,
            status=BaselineLaneStatus.OBSERVED,
            values={
                "price_date": "2026-07-09",
                "return_pct": 15.0,
                "trading_value": 2_000_000_000,
            },
        ),
        _lane(
            "000660",
            "SK하이닉스",
            "KOSDAQ",
            BaselineLane.RISK,
            status=BaselineLaneStatus.OBSERVED,
            values={
                "risk_events": [
                    {
                        "rcept_no": "20260710900001",
                        "rcept_date": "2026-07-10",
                        "report_name": "주권매매거래정지 해제",
                        "corp_code": "00164779",
                        "lifecycle": "RESOLVED",
                    }
                ],
                "risk_lifecycle_status": "RESOLVED_IN_BOUNDED_DAILY_OFFICIAL_SCAN",
            },
        ),
        _lane("000660", "SK하이닉스", "KOSDAQ", BaselineLane.EXISTING_LEDGER),
    )


class LiveTriggerFusionTests(unittest.TestCase):
    def setUp(self):
        self.universe = (
            _universe("005930", "삼성전자", "KOSPI"),
            _universe("000660", "SK하이닉스", "KOSDAQ"),
        )

    def _fuse(self, *, lanes=None, current_state=()):
        return CurrentTriggerFusion().fuse(
            TriggerFusionConfig(as_of_date="2026-07-10", test_mode=True),
            universe=self.universe,
            baseline_lanes=_lanes() if lanes is None else lanes,
            current_state=current_state,
        )

    def test_live_operational_audit_records_nonempty_safe_trigger_pool(self):
        audit = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "docs/operational/e2r_live_trigger_fusion_audit.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(audit["status"], "CURRENT_TRIGGER_FUSION_PASS")
        self.assertGreater(audit["eligible_universe_count"], 1000)
        self.assertTrue(audit["full_universe_trigger_scan_attempted"])
        self.assertGreater(audit["trigger_signal_count"], 0)
        self.assertGreater(audit["candidate_event_count"], 0)
        self.assertEqual(audit["market_trigger_to_score_count"], 0)
        self.assertEqual(audit["news_snippet_to_score_count"], 0)
        self.assertEqual(audit["wrong_subject_trigger_count"], 0)
        self.assertEqual(audit["trigger_without_source_ref_count"], 0)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(audit["hard_acceptance_pass"])

    def test_official_market_risk_and_existing_ledger_are_investigation_only(self):
        result = self._fuse()

        self.assertEqual(result.status, "CURRENT_TRIGGER_FUSION_PASS")
        self.assertEqual(
            {signal.trigger_type for signal in result.trigger_signals},
            {
                TriggerType.OFFICIAL.value,
                TriggerType.MARKET.value,
                TriggerType.RISK.value,
                TriggerType.EXISTING_LEDGER.value,
            },
        )
        self.assertTrue(all(signal.investigation_required for signal in result.trigger_signals))
        self.assertTrue(
            all(not signal.score_evidence_eligible for signal in result.trigger_signals)
        )
        self.assertEqual(result.audit["market_trigger_to_score_count"], 0)
        self.assertEqual(result.audit["trigger_without_source_ref_count"], 0)

    def test_resolved_risk_opens_review_but_is_not_reopened_as_current_risk(self):
        result = self._fuse()
        risk = next(
            signal
            for signal in result.trigger_signals
            if signal.target_id == "000660" and signal.trigger_type == TriggerType.RISK.value
        )

        self.assertEqual(risk.lifecycle_status, "RESOLVED")
        self.assertFalse(risk.score_evidence_eligible)

    def test_active_old_contract_stays_in_trigger_pool(self):
        old_contract = CurrentStateEvent(
            event_id="OLD-ACTIVE-CONTRACT",
            target_id="005930",
            event_type="SUPPLY_CONTRACT",
            effective_date="2024-01-01",
            lifecycle_status=EventLifecycleStatus.OPEN.value,
            source_ids=("DART-RCEPT-20240101000001",),
            end_date="2027-12-31",
            score_eligible=True,
        )
        state = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=self.universe,
            discovered_events=(old_contract,),
        ).records

        result = self._fuse(current_state=state)

        old = next(
            signal
            for signal in result.trigger_signals
            if signal.source_event_id == "OLD-ACTIVE-CONTRACT"
        )
        self.assertEqual(old.effective_date, "2024-01-01")
        self.assertEqual(old.lifecycle_status, EventLifecycleStatus.OPEN.value)
        self.assertTrue(old.payload["active_old_event_preserved"])

    def test_same_source_event_and_date_are_deduped(self):
        lanes = list(_lanes())
        lanes[4] = _lane(
            "000660",
            "SK하이닉스",
            "KOSDAQ",
            BaselineLane.OFFICIAL,
            status=BaselineLaneStatus.PARTIAL_HISTORY_PENDING,
            values={
                "latest_material_event": {
                    "rcept_no": "20260710900001",
                    "rcept_date": "2026-07-10",
                    "report_name": "주권매매거래정지 해제",
                    "corp_code": "00164779",
                }
            },
        )

        result = self._fuse(lanes=tuple(lanes))

        same = [
            signal
            for signal in result.trigger_signals
            if signal.source_event_id == "DART-RCEPT-20260710900001"
        ]
        self.assertEqual(len(same), 1)
        self.assertEqual(same[0].trigger_type, TriggerType.RISK.value)
        self.assertEqual(result.dedupe_report["duplicate_trigger_count"], 1)

    def test_missing_baseline_lane_fails_full_universe_scan_gate(self):
        result = self._fuse(lanes=_lanes()[:-1])

        self.assertEqual(result.status, "CURRENT_TRIGGER_FUSION_FAIL")
        self.assertEqual(
            result.audit["critical_counts"][
                "symbol_without_required_baseline_for_trigger_scan"
            ],
            1,
        )

    def test_trigger_signal_without_source_lineage_is_rejected(self):
        with self.assertRaises(ValueError):
            TriggerSignal(
                trigger_signal_id="TRIG-BAD",
                target_id="005930",
                target_name="삼성전자",
                trigger_type=TriggerType.NEWS.value,
                source_event_id="NEWS-BAD",
                effective_date="2026-07-10",
                detected_at="2026-07-10",
                source_refs=(),
                provider_names=("NaverSearch",),
                subject_direct=True,
                lifecycle_status="DISCOVERY_ONLY",
                investigation_required=True,
                score_evidence_eligible=False,
                headline_or_snippet_only=True,
                payload={},
            )

    def test_writer_and_loaders_preserve_leaf_rows(self):
        result = self._fuse()
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_trigger_fusion(result, output_root=tmp)
            signals = load_trigger_signals(paths["signals"])
            candidates = load_candidate_events(paths["candidates"])
            self.assertEqual(
                [row.to_dict() for row in signals],
                [row.to_dict() for row in result.trigger_signals],
            )
            self.assertEqual(
                [row.to_dict() for row in candidates],
                [row.to_dict() for row in result.candidate_events],
            )
            self.assertTrue(all(Path(path).is_file() for path in paths.values()))


if __name__ == "__main__":
    unittest.main()
