from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from e2r.research_brain.runtime.live_materialization import (
    BaselineBulkSnapshot,
    BaselineLane,
    BaselineLaneStatus,
    BaselineMaterializerConfig,
    BulkSnapshotStatus,
    CurrentBaselineMaterializer,
    CurrentStateBootstrapper,
    LiveUniverseRow,
    load_current_state_store,
    write_baseline_materialization,
    write_current_state_bootstrap,
)


def _universe_row(symbol: str, name: str, market: str) -> LiveUniverseRow:
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
        source_request_id="KRX-REQUEST-20260709",
        source_mode="LIVE_OFFICIAL_API",
        eligible=True,
        exclusion_reason=None,
        raw_fields={},
    )


def _snapshot(
    provider: str,
    source_class: str,
    rows,
    *,
    status: str = BulkSnapshotStatus.FETCHED.value,
    error: str | None = None,
) -> BaselineBulkSnapshot:
    raw = json.dumps(rows, ensure_ascii=False, sort_keys=True).encode("utf-8")
    if provider == "KRX":
        endpoint = "stk_bydd_trd" if source_class.endswith("KOSPI") else "ksq_bydd_trd"
        url = f"https://data-dbg.krx.co.kr/svc/apis/sto/{endpoint}"
        effective_date = "2026-07-09"
    else:
        url = "https://opendart.fss.or.kr/api/list.json"
        effective_date = "2026-07-10"
    return BaselineBulkSnapshot(
        provider_name=provider,
        source_class=source_class,
        effective_date=effective_date,
        canonical_url=url,
        request_id=f"REQUEST-{provider}-{source_class}",
        provider_request_id=f"PROVIDER-{provider}-{source_class}",
        fetched_at="2026-07-11T00:00:00+00:00",
        content_hash=hashlib.sha256(raw).hexdigest(),
        rows=tuple(rows),
        status=status,
        error_category=error,
    )


class _FixtureBaselineTransport:
    def __init__(self, *, krx_by_market, dart):
        self.krx_by_market = krx_by_market
        self.dart = dart
        self.calls = []

    def fetch_krx_price(
        self, *, market, effective_date, credential, timeout_seconds
    ):
        self.calls.append(("KRX", market, effective_date.isoformat()))
        return self.krx_by_market[market]

    def fetch_opendart_index(
        self,
        *,
        start_date,
        end_date,
        credential,
        page_count,
        max_pages,
        timeout_seconds,
    ):
        self.calls.append(("OpenDART", start_date.isoformat(), end_date.isoformat()))
        return self.dart


def _price(symbol: str, *, segment: str = "") -> dict[str, str]:
    return {
        "BAS_DD": "20260709",
        "ISU_CD": symbol,
        "ISU_NM": symbol,
        "SECT_TP_NM": segment,
        "TDD_CLSPRC": "10000",
        "CMPPREVDD_PRC": "500",
        "FLUC_RT": "5.26",
        "ACC_TRDVOL": "100000",
        "ACC_TRDVAL": "1000000000",
        "MKTCAP": "100000000000",
    }


class LiveBaselineLaneMaterializerTests(unittest.TestCase):
    def setUp(self):
        self.universe = (
            _universe_row("005930", "삼성전자", "KOSPI"),
            _universe_row("000660", "SK하이닉스", "KOSDAQ"),
        )
        self.transport = _FixtureBaselineTransport(
            krx_by_market={
                "KOSPI": _snapshot("KRX", "PRICE_KOSPI", (_price("005930"),)),
                "KOSDAQ": _snapshot("KRX", "PRICE_KOSDAQ", (_price("000660"),)),
            },
            dart=_snapshot(
                "OpenDART",
                "DISCLOSURE_INDEX",
                (
                    {
                        "stock_code": "005930",
                        "corp_code": "00126380",
                        "rcept_no": "20260710000001",
                        "rcept_dt": "20260710",
                        "report_nm": "분기보고서",
                    },
                    {
                        "stock_code": "000660",
                        "corp_code": "00164779",
                        "rcept_no": "20260710900001",
                        "rcept_dt": "20260710",
                        "report_nm": "매매거래정지",
                    },
                ),
            ),
        )

    def _materialize(self, *, prior_state=()):
        return CurrentBaselineMaterializer(self.transport).materialize(
            BaselineMaterializerConfig(as_of_date="2026-07-10", test_mode=True),
            universe=self.universe,
            prior_state=prior_state,
            krx_credential="fixture-krx-key",
            opendart_credential="fixture-dart-key",
            env_file=None,
        )

    def test_live_operational_audit_records_complete_four_lane_coverage(self):
        audit = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "docs/operational/e2r_live_baseline_lane_audit.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(audit["status"], "CURRENT_BASELINE_LANES_PASS")
        self.assertGreater(audit["eligible_universe_count"], 1000)
        self.assertEqual(
            audit["baseline_lane_count"], audit["eligible_universe_count"] * 4
        )
        self.assertEqual(audit["missing_required_baseline_lane_count"], 0)
        self.assertEqual(
            audit["baseline_lane_provider_failure_without_error_count"], 0
        )
        self.assertEqual(audit["observed_lane_without_source_id_count"], 0)
        self.assertEqual(audit["price_lane_to_score_count"], 0)
        self.assertEqual(audit["generic_portal_observed_lane_count"], 0)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertTrue(audit["hard_acceptance_pass"])

    def test_every_symbol_gets_exactly_four_required_lanes(self):
        result = self._materialize()

        self.assertEqual(result.status, "CURRENT_BASELINE_LANES_PASS")
        self.assertEqual(len(result.lanes), len(self.universe) * 4)
        for symbol in ("005930", "000660"):
            self.assertEqual(
                {lane.lane for lane in result.lanes if lane.target_id == symbol},
                {item.value for item in BaselineLane},
            )
        self.assertEqual(result.audit["missing_required_baseline_lane_count"], 0)
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_price_is_real_bulk_baseline_but_never_score_evidence(self):
        result = self._materialize()
        price_lanes = [lane for lane in result.lanes if lane.lane == BaselineLane.PRICE.value]

        self.assertTrue(
            all(lane.status == BaselineLaneStatus.OBSERVED.value for lane in price_lanes)
        )
        self.assertTrue(all(lane.values["close"] == 10000 for lane in price_lanes))
        self.assertTrue(all(not lane.score_evidence_eligible for lane in price_lanes))
        self.assertEqual(result.audit["price_lane_to_score_count"], 0)

    def test_risk_requires_symbol_specific_official_row_and_stays_lifecycle_pending(self):
        result = self._materialize()
        risks = {
            lane.target_id: lane
            for lane in result.lanes
            if lane.lane == BaselineLane.RISK.value
        }

        self.assertEqual(risks["005930"].status, BaselineLaneStatus.NO_RESULT.value)
        self.assertEqual(risks["000660"].status, BaselineLaneStatus.OBSERVED.value)
        self.assertEqual(risks["000660"].values["risk_event_count"], 1)
        self.assertEqual(
            risks["000660"].values["risk_lifecycle_status"],
            "OPEN_CANDIDATE_REQUIRES_LIFECYCLE_REFRESH",
        )

    def test_risk_resolution_is_observed_but_never_kept_as_current_open_risk(self):
        self.transport.dart = _snapshot(
            "OpenDART",
            "DISCLOSURE_INDEX",
            (
                {
                    "stock_code": "000660",
                    "corp_code": "00164779",
                    "rcept_no": "20260710900002",
                    "rcept_dt": "20260710",
                    "report_nm": "주권매매거래정지 해제",
                },
            ),
        )

        result = self._materialize()
        risk = next(
            lane
            for lane in result.lanes
            if lane.target_id == "000660" and lane.lane == BaselineLane.RISK.value
        )

        self.assertEqual(risk.status, BaselineLaneStatus.OBSERVED.value)
        self.assertFalse(risk.values["current_risk_confirmed"])
        self.assertEqual(
            risk.values["risk_lifecycle_status"],
            "RESOLVED_IN_BOUNDED_DAILY_OFFICIAL_SCAN",
        )
        self.assertFalse(risk.score_evidence_eligible)

    def test_missing_prior_ledger_is_explicit_and_not_an_empty_observation(self):
        result = self._materialize()
        ledger_lanes = [
            lane for lane in result.lanes if lane.lane == BaselineLane.EXISTING_LEDGER.value
        ]

        self.assertTrue(
            all(lane.status == BaselineLaneStatus.NO_PRIOR_LEDGER.value for lane in ledger_lanes)
        )
        self.assertTrue(all(lane.source_ids for lane in ledger_lanes))

    def test_one_market_provider_failure_does_not_poison_other_market_price_lane(self):
        self.transport.krx_by_market["KOSPI"] = _snapshot(
            "KRX",
            "PRICE_KOSPI",
            (),
            status=BulkSnapshotStatus.PROVIDER_FAILED.value,
            error="PROVIDER_NETWORK_FAILURE",
        )

        result = self._materialize()
        price = {
            lane.target_id: lane
            for lane in result.lanes
            if lane.lane == BaselineLane.PRICE.value
        }

        self.assertEqual(price["005930"].status, BaselineLaneStatus.PROVIDER_FAILED.value)
        self.assertEqual(price["005930"].provider_error_category, "PROVIDER_NETWORK_FAILURE")
        self.assertEqual(price["000660"].status, BaselineLaneStatus.OBSERVED.value)
        self.assertEqual(
            result.audit["baseline_lane_provider_failure_without_error_count"], 0
        )

    def test_generic_krx_homepage_cannot_be_constructed_as_bulk_source(self):
        with self.assertRaises(ValueError):
            BaselineBulkSnapshot(
                provider_name="KRX",
                source_class="PRICE_KOSPI",
                effective_date="2026-07-09",
                canonical_url="https://data.krx.co.kr/",
                request_id="GENERIC",
                provider_request_id="GENERIC",
                fetched_at="2026-07-11T00:00:00+00:00",
                content_hash="a" * 64,
                rows=(),
            )

    def test_current_state_store_roundtrip_preserves_nested_schema(self):
        bootstrap = CurrentStateBootstrapper().bootstrap(
            as_of_date="2026-07-10",
            universe=self.universe,
        )
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_current_state_bootstrap(bootstrap, output_root=tmp)
            loaded = load_current_state_store(paths["store"])
        self.assertEqual(
            [record.to_dict() for record in loaded],
            [record.to_dict() for record in bootstrap.records],
        )

    def test_writer_emits_lane_source_and_audit_files(self):
        result = self._materialize()
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_baseline_materialization(result, output_root=tmp)
            self.assertEqual(
                {path.name for path in paths.values()},
                {
                    "baseline_lanes.jsonl",
                    "baseline_source_snapshots.jsonl",
                    "baseline_lane_audit.json",
                },
            )
            self.assertTrue(all(Path(path).is_file() for path in paths.values()))


if __name__ == "__main__":
    unittest.main()
