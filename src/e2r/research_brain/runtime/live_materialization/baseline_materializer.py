"""Bulk-first OFFICIAL/PRICE/RISK/EXISTING_LEDGER baseline materialization."""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

import requests

from e2r.env import load_project_env
from e2r.production.metadata import stable_hash, write_json, write_jsonl

from .current_state_store import CurrentStateRecord
from .universe_materializer import LiveUniverseRow


BASELINE_LANE_SCHEMA_VERSION = "e2r_live_baseline_lane_v1"
_KRX_PRICE_BASE = "https://data-dbg.krx.co.kr/svc/apis/sto"
_KRX_PRICE_ENDPOINTS = {"KOSPI": "stk_bydd_trd", "KOSDAQ": "ksq_bydd_trd"}
_OPENDART_LIST_URL = "https://opendart.fss.or.kr/api/list.json"
_REGULAR_REPORT_TOKENS = ("사업보고서", "반기보고서", "분기보고서")
_RISK_TOKENS = (
    "관리종목",
    "상장폐지",
    "매매거래정지",
    "거래정지",
    "투자주의",
    "투자경고",
    "투자위험",
    "불성실공시",
    "감사의견",
    "회생절차",
)
_RISK_RESOLUTION_TOKENS = (
    "해제",
    "지정해제",
    "해소",
    "철회",
    "종료",
)


class BaselineLane(str, Enum):
    OFFICIAL = "OFFICIAL"
    PRICE = "PRICE"
    RISK = "RISK"
    EXISTING_LEDGER = "EXISTING_LEDGER"


class BaselineLaneStatus(str, Enum):
    OBSERVED = "OBSERVED"
    NO_RESULT = "NO_RESULT"
    NO_PRIOR_LEDGER = "NO_PRIOR_LEDGER"
    PARTIAL_HISTORY_PENDING = "PARTIAL_HISTORY_PENDING"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    AUTH_FAILED = "AUTH_FAILED"
    RATE_LIMITED = "RATE_LIMITED"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"


class BulkSnapshotStatus(str, Enum):
    FETCHED = "FETCHED"
    PROVIDER_FAILED = "PROVIDER_FAILED"
    AUTH_FAILED = "AUTH_FAILED"
    RATE_LIMITED = "RATE_LIMITED"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"


@dataclass(frozen=True)
class BaselineMaterializerConfig:
    as_of_date: str
    price_effective_date: str | None = None
    dart_index_start_date: str | None = None
    dart_page_count: int = 100
    dart_max_pages: int = 20
    request_timeout_seconds: float = 30.0
    test_mode: bool = False

    def __post_init__(self) -> None:
        as_of = date.fromisoformat(self.as_of_date)
        if self.price_effective_date and date.fromisoformat(self.price_effective_date) > as_of:
            raise ValueError("future KRX price date is forbidden")
        if self.dart_index_start_date and date.fromisoformat(self.dart_index_start_date) > as_of:
            raise ValueError("future OpenDART start date is forbidden")
        if self.dart_page_count <= 0 or self.dart_page_count > 100:
            raise ValueError("OpenDART page_count must be bounded by the provider maximum")
        if self.dart_max_pages <= 0 or self.dart_max_pages > 100:
            raise ValueError("OpenDART max pages must be explicitly bounded")
        if self.request_timeout_seconds <= 0 or self.request_timeout_seconds > 120:
            raise ValueError("baseline request timeout must be bounded")


@dataclass(frozen=True)
class BaselineBulkSnapshot:
    provider_name: str
    source_class: str
    effective_date: str
    canonical_url: str
    request_id: str
    provider_request_id: str
    fetched_at: str
    content_hash: str
    rows: tuple[Mapping[str, Any], ...]
    status: str = BulkSnapshotStatus.FETCHED.value
    error_category: str | None = None
    page_count: int = 1

    def __post_init__(self) -> None:
        BulkSnapshotStatus(self.status)
        date.fromisoformat(self.effective_date)
        if self.provider_name == "KRX" and not self.canonical_url.startswith(
            _KRX_PRICE_BASE + "/"
        ):
            raise ValueError("KRX baseline snapshot must use a structured OpenAPI endpoint")
        if self.provider_name == "OpenDART" and self.canonical_url != _OPENDART_LIST_URL:
            raise ValueError("OpenDART baseline snapshot must use list.json, not a portal page")
        if not all((self.source_class.strip(), self.request_id.strip())):
            raise ValueError("baseline snapshot identity required")
        if not _is_sha256(self.content_hash):
            raise ValueError("baseline snapshot content hash invalid")
        if self.status == BulkSnapshotStatus.FETCHED.value and self.error_category:
            raise ValueError("successful baseline snapshot cannot carry provider error")
        if self.status != BulkSnapshotStatus.FETCHED.value and not self.error_category:
            raise ValueError("failed baseline snapshot requires provider error category")
        if self.page_count <= 0:
            raise ValueError("baseline snapshot page count must be positive")

    @property
    def source_document_id(self) -> str:
        return "BASESRC-" + stable_hash(
            {
                "provider": self.provider_name,
                "source_class": self.source_class,
                "effective_date": self.effective_date,
                "request_id": self.request_id,
                "content_hash": self.content_hash,
            }
        )[:24]

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["rows"] = [dict(row) for row in self.rows]
        payload["source_document_id"] = self.source_document_id
        return payload


@dataclass(frozen=True)
class BaselineLaneRecord:
    lane_id: str
    target_id: str
    target_name: str
    market: str
    lane: str
    status: str
    observed_date: str
    provider_names: tuple[str, ...]
    source_ids: tuple[str, ...]
    values: Mapping[str, Any]
    provider_error_category: str | None = None
    score_evidence_eligible: bool = False
    generic_portal_source: bool = False
    schema_version: str = BASELINE_LANE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        BaselineLane(self.lane)
        BaselineLaneStatus(self.status)
        date.fromisoformat(self.observed_date)
        if not all((self.lane_id.strip(), self.target_id.strip(), self.target_name.strip())):
            raise ValueError("baseline lane identity required")
        if not self.provider_names:
            raise ValueError("baseline lane provider lineage required")
        if self.status == BaselineLaneStatus.OBSERVED.value and not self.source_ids:
            raise ValueError("observed baseline lane requires source ID")
        if self.status in {
            BaselineLaneStatus.PROVIDER_FAILED.value,
            BaselineLaneStatus.AUTH_FAILED.value,
            BaselineLaneStatus.RATE_LIMITED.value,
            BaselineLaneStatus.BUDGET_EXHAUSTED.value,
        } and not self.provider_error_category:
            raise ValueError("baseline provider failure requires exact error category")
        if self.lane == BaselineLane.PRICE.value and self.score_evidence_eligible:
            raise ValueError("price baseline cannot be score evidence")
        if self.generic_portal_source:
            raise ValueError("generic portal cannot count as a baseline lane source")

    def to_dict(self) -> dict[str, Any]:
        return {
            **asdict(self),
            "provider_names": list(self.provider_names),
            "source_ids": list(self.source_ids),
            "values": dict(self.values),
        }


@dataclass(frozen=True)
class BaselineMaterializationResult:
    as_of_date: str
    status: str
    lanes: tuple[BaselineLaneRecord, ...]
    source_snapshots: tuple[BaselineBulkSnapshot, ...]
    source_corpus_hash: str
    audit: Mapping[str, Any]

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)


class BaselineBulkTransport(Protocol):
    def fetch_krx_price(
        self,
        *,
        market: str,
        effective_date: date,
        credential: str,
        timeout_seconds: float,
    ) -> BaselineBulkSnapshot:
        ...

    def fetch_opendart_index(
        self,
        *,
        start_date: date,
        end_date: date,
        credential: str,
        page_count: int,
        max_pages: int,
        timeout_seconds: float,
    ) -> BaselineBulkSnapshot:
        ...


class RequestsBaselineBulkTransport:
    def fetch_krx_price(
        self,
        *,
        market: str,
        effective_date: date,
        credential: str,
        timeout_seconds: float,
    ) -> BaselineBulkSnapshot:
        endpoint = _KRX_PRICE_ENDPOINTS[market]
        url = f"{_KRX_PRICE_BASE}/{endpoint}"
        request_id = "KRXBASE-" + stable_hash(
            {"market": market, "date": effective_date.isoformat(), "endpoint": endpoint}
        )[:24]
        fetched_at = _utc_now()
        try:
            response = requests.get(
                url,
                headers={"AUTH_KEY": credential},
                params={"basDd": effective_date.strftime("%Y%m%d")},
                timeout=(5.0, timeout_seconds),
            )
            content_hash = hashlib.sha256(response.content).hexdigest()
            failure = _http_failure(response.status_code)
            if failure:
                return _failed_snapshot(
                    provider_name="KRX",
                    source_class=f"PRICE_{market}",
                    effective_date=effective_date,
                    canonical_url=url,
                    request_id=request_id,
                    fetched_at=fetched_at,
                    content_hash=content_hash,
                    error_category=failure,
                )
            response.raise_for_status()
            payload = response.json()
            rows = payload.get("OutBlock_1")
            if not isinstance(rows, list):
                return _failed_snapshot(
                    provider_name="KRX",
                    source_class=f"PRICE_{market}",
                    effective_date=effective_date,
                    canonical_url=url,
                    request_id=request_id,
                    fetched_at=fetched_at,
                    content_hash=content_hash,
                    error_category="PROVIDER_SCHEMA_CHANGED",
                )
            return BaselineBulkSnapshot(
                provider_name="KRX",
                source_class=f"PRICE_{market}",
                effective_date=effective_date.isoformat(),
                canonical_url=url,
                request_id=request_id,
                provider_request_id=response.headers.get("X-Request-ID") or request_id,
                fetched_at=fetched_at,
                content_hash=content_hash,
                rows=tuple(dict(row) for row in rows if isinstance(row, Mapping)),
            )
        except requests.RequestException:
            return _failed_snapshot(
                provider_name="KRX",
                source_class=f"PRICE_{market}",
                effective_date=effective_date,
                canonical_url=url,
                request_id=request_id,
                fetched_at=fetched_at,
                content_hash=hashlib.sha256(b"").hexdigest(),
                error_category="PROVIDER_NETWORK_FAILURE",
            )
        except (TypeError, ValueError, json.JSONDecodeError):
            return _failed_snapshot(
                provider_name="KRX",
                source_class=f"PRICE_{market}",
                effective_date=effective_date,
                canonical_url=url,
                request_id=request_id,
                fetched_at=fetched_at,
                content_hash=hashlib.sha256(b"").hexdigest(),
                error_category="PROVIDER_SCHEMA_CHANGED",
            )

    def fetch_opendart_index(
        self,
        *,
        start_date: date,
        end_date: date,
        credential: str,
        page_count: int,
        max_pages: int,
        timeout_seconds: float,
    ) -> BaselineBulkSnapshot:
        request_id = "DARTBASE-" + stable_hash(
            {
                "start": start_date.isoformat(),
                "end": end_date.isoformat(),
                "page_count": page_count,
                "max_pages": max_pages,
            }
        )[:24]
        fetched_at = _utc_now()
        rows: list[Mapping[str, Any]] = []
        raw_pages: list[bytes] = []
        provider_request_id = request_id
        for page_no in range(1, max_pages + 1):
            try:
                response = requests.get(
                    _OPENDART_LIST_URL,
                    params={
                        "crtfc_key": credential,
                        "bgn_de": start_date.strftime("%Y%m%d"),
                        "end_de": end_date.strftime("%Y%m%d"),
                        "page_no": page_no,
                        "page_count": page_count,
                    },
                    timeout=(5.0, timeout_seconds),
                )
                raw_pages.append(response.content)
                provider_request_id = response.headers.get("X-Request-ID") or provider_request_id
                failure = _http_failure(response.status_code)
                if failure:
                    return _failed_snapshot(
                        provider_name="OpenDART",
                        source_class="DISCLOSURE_INDEX",
                        effective_date=end_date,
                        canonical_url=_OPENDART_LIST_URL,
                        request_id=request_id,
                        fetched_at=fetched_at,
                        content_hash=_combined_hash(raw_pages),
                        error_category=failure,
                        page_count=page_no,
                    )
                response.raise_for_status()
                payload = response.json()
                provider_status = str(payload.get("status") or "")
                if provider_status == "013":
                    break
                if provider_status != "000" or not isinstance(payload.get("list"), list):
                    return _failed_snapshot(
                        provider_name="OpenDART",
                        source_class="DISCLOSURE_INDEX",
                        effective_date=end_date,
                        canonical_url=_OPENDART_LIST_URL,
                        request_id=request_id,
                        fetched_at=fetched_at,
                        content_hash=_combined_hash(raw_pages),
                        error_category=(
                            "PROVIDER_AUTH_FAILURE"
                            if provider_status in {"010", "011", "012"}
                            else "PROVIDER_SCHEMA_CHANGED"
                        ),
                        page_count=page_no,
                    )
                rows.extend(dict(row) for row in payload["list"] if isinstance(row, Mapping))
                total_page = _int(payload.get("total_page"), default=page_no)
                if page_no >= total_page:
                    break
                if page_no == max_pages:
                    return _failed_snapshot(
                        provider_name="OpenDART",
                        source_class="DISCLOSURE_INDEX",
                        effective_date=end_date,
                        canonical_url=_OPENDART_LIST_URL,
                        request_id=request_id,
                        fetched_at=fetched_at,
                        content_hash=_combined_hash(raw_pages),
                        error_category="RUNTIME_BUDGET_EXHAUSTED",
                        page_count=page_no,
                    )
            except requests.RequestException:
                return _failed_snapshot(
                    provider_name="OpenDART",
                    source_class="DISCLOSURE_INDEX",
                    effective_date=end_date,
                    canonical_url=_OPENDART_LIST_URL,
                    request_id=request_id,
                    fetched_at=fetched_at,
                    content_hash=_combined_hash(raw_pages),
                    error_category="PROVIDER_NETWORK_FAILURE",
                    page_count=page_no,
                )
            except (TypeError, ValueError, json.JSONDecodeError):
                return _failed_snapshot(
                    provider_name="OpenDART",
                    source_class="DISCLOSURE_INDEX",
                    effective_date=end_date,
                    canonical_url=_OPENDART_LIST_URL,
                    request_id=request_id,
                    fetched_at=fetched_at,
                    content_hash=_combined_hash(raw_pages),
                    error_category="PROVIDER_SCHEMA_CHANGED",
                    page_count=page_no,
                )
        return BaselineBulkSnapshot(
            provider_name="OpenDART",
            source_class="DISCLOSURE_INDEX",
            effective_date=end_date.isoformat(),
            canonical_url=_OPENDART_LIST_URL,
            request_id=request_id,
            provider_request_id=provider_request_id,
            fetched_at=fetched_at,
            content_hash=_combined_hash(raw_pages),
            rows=tuple(rows),
            page_count=max(1, len(raw_pages)),
        )


class CurrentBaselineMaterializer:
    def __init__(self, transport: BaselineBulkTransport | None = None) -> None:
        self.transport = transport or RequestsBaselineBulkTransport()

    def materialize(
        self,
        config: BaselineMaterializerConfig,
        *,
        universe: Sequence[LiveUniverseRow],
        prior_state: Sequence[CurrentStateRecord] = (),
        krx_credential: str | None = None,
        opendart_credential: str | None = None,
        env_file: str | Path | None = ".env",
        load_environment: bool = True,
    ) -> BaselineMaterializationResult:
        if load_environment:
            load_project_env(env_file, override=False)
        eligible = tuple(row for row in universe if row.eligible)
        if not eligible:
            raise ValueError("baseline materializer requires eligible universe")
        universe_by_symbol = _unique_universe(eligible)
        prior_by_symbol = {record.target_id: record for record in prior_state}
        if len(prior_by_symbol) != len(prior_state):
            raise ValueError("duplicate prior current-state target")
        as_of = date.fromisoformat(config.as_of_date)
        price_date = _resolve_price_date(config=config, universe=eligible)
        dart_start = date.fromisoformat(config.dart_index_start_date or config.as_of_date)
        krx_key = krx_credential or (
            os.environ.get("KRX_OPENAPI_KEY") if load_environment else None
        )
        dart_key = (
            opendart_credential
            or (os.environ.get("OPENDART_API_KEY") if load_environment else None)
            or (os.environ.get("OPEN_DART_API_KEY") if load_environment else None)
        )
        snapshots: list[BaselineBulkSnapshot] = []
        for market in sorted(_KRX_PRICE_ENDPOINTS):
            snapshots.append(
                self.transport.fetch_krx_price(
                    market=market,
                    effective_date=price_date,
                    credential=krx_key,
                    timeout_seconds=config.request_timeout_seconds,
                )
                if krx_key
                else _missing_credential_snapshot(
                    provider_name="KRX",
                    source_class=f"PRICE_{market}",
                    effective_date=price_date,
                    canonical_url=f"{_KRX_PRICE_BASE}/{_KRX_PRICE_ENDPOINTS[market]}",
                )
            )
        snapshots.append(
            self.transport.fetch_opendart_index(
                start_date=dart_start,
                end_date=as_of,
                credential=dart_key,
                page_count=config.dart_page_count,
                max_pages=config.dart_max_pages,
                timeout_seconds=config.request_timeout_seconds,
            )
            if dart_key
            else _missing_credential_snapshot(
                provider_name="OpenDART",
                source_class="DISCLOSURE_INDEX",
                effective_date=as_of,
                canonical_url=_OPENDART_LIST_URL,
            )
        )
        price_snapshots = {
            snapshot.source_class.removeprefix("PRICE_"): snapshot
            for snapshot in snapshots
            if snapshot.provider_name == "KRX"
        }
        dart_snapshot = next(
            snapshot for snapshot in snapshots if snapshot.provider_name == "OpenDART"
        )
        price_by_symbol = {
            str(row.get("ISU_CD") or "").strip(): dict(row)
            for snapshot in price_snapshots.values()
            if snapshot.status == BulkSnapshotStatus.FETCHED.value
            for row in snapshot.rows
            if str(row.get("ISU_CD") or "").strip()
        }
        dart_by_symbol: dict[str, list[Mapping[str, Any]]] = {}
        if dart_snapshot.status == BulkSnapshotStatus.FETCHED.value:
            for row in dart_snapshot.rows:
                symbol = str(row.get("stock_code") or "").strip()
                if symbol in universe_by_symbol and _dart_row_as_of_safe(row, as_of=as_of):
                    dart_by_symbol.setdefault(symbol, []).append(row)
        lanes: list[BaselineLaneRecord] = []
        for symbol, member in sorted(universe_by_symbol.items()):
            filings = tuple(
                sorted(
                    dart_by_symbol.get(symbol, ()),
                    key=lambda row: (str(row.get("rcept_dt") or ""), str(row.get("rcept_no") or "")),
                )
            )
            price_snapshot = price_snapshots[member.market]
            price_row = price_by_symbol.get(symbol)
            prior = prior_by_symbol.get(symbol)
            lanes.extend(
                (
                    _official_lane(
                        member=member,
                        filings=filings,
                        snapshot=dart_snapshot,
                        prior=prior,
                        as_of_date=config.as_of_date,
                    ),
                    _price_lane(
                        member=member,
                        price_row=price_row,
                        snapshot=price_snapshot,
                        as_of_date=config.as_of_date,
                    ),
                    _risk_lane(
                        member=member,
                        filings=filings,
                        dart_snapshot=dart_snapshot,
                        price_row=price_row,
                        price_snapshot=price_snapshot,
                        as_of_date=config.as_of_date,
                    ),
                    _ledger_lane(
                        member=member,
                        prior=prior,
                        as_of_date=config.as_of_date,
                    ),
                )
            )
        audit = _audit_baseline(
            as_of_date=config.as_of_date,
            universe=eligible,
            lanes=tuple(lanes),
            snapshots=tuple(snapshots),
        )
        return BaselineMaterializationResult(
            as_of_date=config.as_of_date,
            status=(
                "CURRENT_BASELINE_LANES_PASS"
                if audit["hard_acceptance_pass"]
                else "CURRENT_BASELINE_LANES_FAIL"
            ),
            lanes=tuple(lanes),
            source_snapshots=tuple(snapshots),
            source_corpus_hash=stable_hash(
                [snapshot.source_document_id for snapshot in snapshots]
            ),
            audit=audit,
        )


def write_baseline_materialization(
    result: BaselineMaterializationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "lanes": root / "baseline_lanes.jsonl",
        "sources": root / "baseline_source_snapshots.jsonl",
        "audit": root / "baseline_lane_audit.json",
    }
    write_jsonl(paths["lanes"], (lane.to_dict() for lane in result.lanes))
    write_jsonl(paths["sources"], (item.to_dict() for item in result.source_snapshots))
    write_json(
        paths["audit"],
        {
            **dict(result.audit),
            "status": result.status,
            "source_corpus_hash": result.source_corpus_hash,
        },
    )
    return paths


def load_baseline_lanes(path: str | Path) -> tuple[BaselineLaneRecord, ...]:
    source = Path(path)
    if not source.is_file():
        return ()
    lanes: list[BaselineLaneRecord] = []
    with source.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
                provider_names = tuple(payload.pop("provider_names"))
                source_ids = tuple(payload.pop("source_ids"))
                lanes.append(
                    BaselineLaneRecord(
                        **payload,
                        provider_names=provider_names,
                        source_ids=source_ids,
                    )
                )
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"invalid baseline lane row at line {line_number}: {exc}"
                ) from exc
    identities = {(lane.target_id, lane.lane) for lane in lanes}
    if len(identities) != len(lanes):
        raise ValueError("duplicate target/lane in baseline file")
    return tuple(lanes)


def _official_lane(
    *,
    member: LiveUniverseRow,
    filings: Sequence[Mapping[str, Any]],
    snapshot: BaselineBulkSnapshot,
    prior: CurrentStateRecord | None,
    as_of_date: str,
) -> BaselineLaneRecord:
    regular = tuple(row for row in filings if _contains_any(_report_name(row), _REGULAR_REPORT_TOKENS))
    material = tuple(row for row in filings if row not in regular)
    source_ids = _filing_source_ids(filings) or (snapshot.source_document_id,)
    if snapshot.status != BulkSnapshotStatus.FETCHED.value:
        return _lane(
            member=member,
            lane=BaselineLane.OFFICIAL,
            status=_lane_failure_status(snapshot),
            providers=("OpenDART",),
            source_ids=(),
            values={"latest_regular_report_checked": False, "latest_material_event_checked": False},
            as_of_date=as_of_date,
            provider_error=snapshot.error_category,
        )
    history_complete = bool(
        prior and prior.bootstrap_completeness == "COMPLETE"
    )
    return _lane(
        member=member,
        lane=BaselineLane.OFFICIAL,
        status=(
            BaselineLaneStatus.OBSERVED
            if filings and history_complete
            else BaselineLaneStatus.PARTIAL_HISTORY_PENDING
        ),
        providers=("OpenDART",),
        source_ids=source_ids,
        values={
            "recent_disclosure_count": len(filings),
            "latest_regular_report_checked": bool(regular) or history_complete,
            "latest_regular_report": _filing_ref(regular[-1]) if regular else None,
            "latest_material_event_checked": True,
            "latest_material_event": _filing_ref(material[-1]) if material else None,
            "history_complete": history_complete,
            "index_scope_start": snapshot.effective_date,
        },
        as_of_date=as_of_date,
    )


def _price_lane(
    *,
    member: LiveUniverseRow,
    price_row: Mapping[str, Any] | None,
    snapshot: BaselineBulkSnapshot,
    as_of_date: str,
) -> BaselineLaneRecord:
    if snapshot.status != BulkSnapshotStatus.FETCHED.value:
        return _lane(
            member=member,
            lane=BaselineLane.PRICE,
            status=_lane_failure_status(snapshot),
            providers=("KRX",),
            source_ids=(),
            values={},
            as_of_date=as_of_date,
            provider_error=snapshot.error_category,
        )
    return _lane(
        member=member,
        lane=BaselineLane.PRICE,
        status=(BaselineLaneStatus.OBSERVED if price_row else BaselineLaneStatus.NO_RESULT),
        providers=("KRX",),
        source_ids=(snapshot.source_document_id,),
        values=(
            {
                "price_date": _yyyymmdd_to_iso(price_row.get("BAS_DD")),
                "close": _number(price_row.get("TDD_CLSPRC")),
                "change": _number(price_row.get("CMPPREVDD_PRC")),
                "return_pct": _number(price_row.get("FLUC_RT")),
                "trading_volume": _number(price_row.get("ACC_TRDVOL")),
                "trading_value": _number(price_row.get("ACC_TRDVAL")),
                "market_cap": _number(price_row.get("MKTCAP")),
                "relative_strength_status": "NOT_COMPUTED_SINGLE_DAY_BASELINE",
                "score_usage": "TRIGGER_PRIORITY_ONLY",
            }
            if price_row
            else {"price_date": snapshot.effective_date, "score_usage": "TRIGGER_PRIORITY_ONLY"}
        ),
        as_of_date=as_of_date,
    )


def _risk_lane(
    *,
    member: LiveUniverseRow,
    filings: Sequence[Mapping[str, Any]],
    dart_snapshot: BaselineBulkSnapshot,
    price_row: Mapping[str, Any] | None,
    price_snapshot: BaselineBulkSnapshot,
    as_of_date: str,
) -> BaselineLaneRecord:
    failed = tuple(
        snapshot
        for snapshot in (dart_snapshot, price_snapshot)
        if snapshot.status != BulkSnapshotStatus.FETCHED.value
    )
    if failed:
        category = "+".join(sorted({str(item.error_category) for item in failed}))
        return _lane(
            member=member,
            lane=BaselineLane.RISK,
            status=BaselineLaneStatus.PROVIDER_FAILED,
            providers=("KRX", "OpenDART"),
            source_ids=tuple(
                item.source_document_id
                for item in (dart_snapshot, price_snapshot)
                if item.status == BulkSnapshotStatus.FETCHED.value
            ),
            values={"risk_lifecycle_complete": False},
            as_of_date=as_of_date,
            provider_error=category,
        )
    risk_filings = tuple(
        row for row in filings if _contains_any(_report_name(row), _RISK_TOKENS)
    )
    segment = str((price_row or {}).get("SECT_TP_NM") or "")
    segment_risk = _contains_any(segment, ("관리", "투자주의", "정리매매"))
    latest_risk_resolved = bool(
        risk_filings
        and _contains_any(_report_name(risk_filings[-1]), _RISK_RESOLUTION_TOKENS)
    )
    current_risk_confirmed = bool(segment_risk or (risk_filings and not latest_risk_resolved))
    risk_event_observed = bool(risk_filings or segment_risk)
    source_ids = tuple(
        dict.fromkeys(
            (
                price_snapshot.source_document_id,
                dart_snapshot.source_document_id,
                *_filing_source_ids(risk_filings),
            )
        )
    )
    return _lane(
        member=member,
        lane=BaselineLane.RISK,
        status=(
            BaselineLaneStatus.OBSERVED
            if risk_event_observed
            else BaselineLaneStatus.NO_RESULT
        ),
        providers=("KRX", "OpenDART"),
        source_ids=source_ids,
        values={
            "risk_event_count": len(risk_filings) + int(segment_risk),
            "risk_events": [
                {
                    **_filing_ref(row),
                    "lifecycle": (
                        "RESOLVED"
                        if _contains_any(_report_name(row), _RISK_RESOLUTION_TOKENS)
                        else "OPEN_CANDIDATE"
                    ),
                }
                for row in risk_filings
            ],
            "krx_segment": segment or None,
            "current_risk_confirmed": current_risk_confirmed,
            "risk_lifecycle_status": (
                "OPEN_CANDIDATE_REQUIRES_LIFECYCLE_REFRESH"
                if current_risk_confirmed
                else "RESOLVED_IN_BOUNDED_DAILY_OFFICIAL_SCAN"
                if latest_risk_resolved
                else "NO_RESULT_IN_BOUNDED_DAILY_OFFICIAL_SCAN"
            ),
            "risk_lifecycle_complete": False,
        },
        as_of_date=as_of_date,
    )


def _ledger_lane(
    *,
    member: LiveUniverseRow,
    prior: CurrentStateRecord | None,
    as_of_date: str,
) -> BaselineLaneRecord:
    claims = tuple(prior.accepted_current_claim_ids) if prior else ()
    source_ids = (
        ("CURRENTSTATE-" + prior.last_updated_source_corpus_hash[:24],)
        if prior
        else ("CURRENTSTATE-NO-PRIOR-" + stable_hash(member.symbol)[:16],)
    )
    return _lane(
        member=member,
        lane=BaselineLane.EXISTING_LEDGER,
        status=(BaselineLaneStatus.OBSERVED if claims else BaselineLaneStatus.NO_PRIOR_LEDGER),
        providers=("ExistingLedger",),
        source_ids=source_ids,
        values={
            "accepted_current_claim_ids": list(claims),
            "accepted_current_claim_count": len(claims),
            "historical_only_claim_ids": list(prior.historical_only_claim_ids) if prior else [],
            "stale_needs_refresh": bool(prior and claims),
            "superseded_or_contradicted_count": sum(
                event.lifecycle_status in {"RESOLVED", "SUPERSEDED"}
                for event in (prior.material_events if prior else ())
            ),
        },
        as_of_date=as_of_date,
    )


def _lane(
    *,
    member: LiveUniverseRow,
    lane: BaselineLane,
    status: BaselineLaneStatus,
    providers: tuple[str, ...],
    source_ids: tuple[str, ...],
    values: Mapping[str, Any],
    as_of_date: str,
    provider_error: str | None = None,
) -> BaselineLaneRecord:
    identity = {
        "target": member.symbol,
        "lane": lane.value,
        "as_of_date": as_of_date,
        "providers": providers,
    }
    return BaselineLaneRecord(
        lane_id="BASELANE-" + stable_hash(identity)[:24],
        target_id=str(member.symbol),
        target_name=str(member.company_name),
        market=member.market,
        lane=lane.value,
        status=status.value,
        observed_date=as_of_date,
        provider_names=providers,
        source_ids=source_ids,
        values=values,
        provider_error_category=provider_error,
        score_evidence_eligible=False,
    )


def _audit_baseline(
    *,
    as_of_date: str,
    universe: Sequence[LiveUniverseRow],
    lanes: Sequence[BaselineLaneRecord],
    snapshots: Sequence[BaselineBulkSnapshot],
) -> dict[str, Any]:
    required = {item.value for item in BaselineLane}
    by_symbol: dict[str, list[BaselineLaneRecord]] = {}
    for lane in lanes:
        by_symbol.setdefault(lane.target_id, []).append(lane)
    missing = sum(
        len(required - {lane.lane for lane in by_symbol.get(str(member.symbol), ())})
        for member in universe
    )
    provider_failure_without_error = sum(
        lane.status
        in {
            BaselineLaneStatus.PROVIDER_FAILED.value,
            BaselineLaneStatus.AUTH_FAILED.value,
            BaselineLaneStatus.RATE_LIMITED.value,
            BaselineLaneStatus.BUDGET_EXHAUSTED.value,
        }
        and not lane.provider_error_category
        for lane in lanes
    )
    observed_without_source = sum(
        lane.status == BaselineLaneStatus.OBSERVED.value and not lane.source_ids
        for lane in lanes
    )
    price_to_score = sum(
        lane.lane == BaselineLane.PRICE.value and lane.score_evidence_eligible
        for lane in lanes
    )
    generic_portal = sum(lane.generic_portal_source for lane in lanes)
    future_source = sum(
        date.fromisoformat(snapshot.effective_date) > date.fromisoformat(as_of_date)
        for snapshot in snapshots
    )
    lane_status_counts: dict[str, int] = {}
    for lane in lanes:
        lane_status_counts[lane.status] = lane_status_counts.get(lane.status, 0) + 1
    critical = {
        "baseline_lane_count_mismatch": int(len(lanes) != len(universe) * 4),
        "missing_required_baseline_lane": missing,
        "baseline_lane_provider_failure_without_error": provider_failure_without_error,
        "observed_lane_without_source_id": observed_without_source,
        "price_lane_to_score": price_to_score,
        "generic_portal_observed_lane": generic_portal,
        "future_baseline_source": future_source,
    }
    return {
        "schema_version": "e2r_live_baseline_lane_audit_v1",
        "as_of_date": as_of_date,
        "eligible_universe_count": len(universe),
        "baseline_lane_count": len(lanes),
        "expected_baseline_lane_count": len(universe) * 4,
        "missing_required_baseline_lane_count": missing,
        "baseline_lane_provider_failure_without_error_count": provider_failure_without_error,
        "observed_lane_without_source_id_count": observed_without_source,
        "price_lane_to_score_count": price_to_score,
        "generic_portal_observed_lane_count": generic_portal,
        "future_baseline_source_count": future_source,
        "source_snapshot_count": len(snapshots),
        "actual_provider_fetch_count": sum(
            snapshot.status == BulkSnapshotStatus.FETCHED.value for snapshot in snapshots
        ),
        "lane_status_counts": dict(sorted(lane_status_counts.items())),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "hard_acceptance_pass": sum(critical.values()) == 0,
    }


def _resolve_price_date(
    *,
    config: BaselineMaterializerConfig,
    universe: Sequence[LiveUniverseRow],
) -> date:
    if config.price_effective_date:
        return date.fromisoformat(config.price_effective_date)
    dates = {row.source_effective_date for row in universe}
    if len(dates) != 1:
        raise ValueError("baseline universe must have one deterministic effective date")
    return date.fromisoformat(next(iter(dates)))


def _unique_universe(rows: Sequence[LiveUniverseRow]) -> dict[str, LiveUniverseRow]:
    result: dict[str, LiveUniverseRow] = {}
    for row in rows:
        symbol = str(row.symbol or "")
        if not symbol or symbol in result:
            raise ValueError("eligible baseline universe has missing or duplicate symbol")
        if row.market not in _KRX_PRICE_ENDPOINTS:
            raise ValueError("unsupported baseline market")
        result[symbol] = row
    return result


def _failed_snapshot(
    *,
    provider_name: str,
    source_class: str,
    effective_date: date,
    canonical_url: str,
    request_id: str,
    fetched_at: str,
    content_hash: str,
    error_category: str,
    page_count: int = 1,
) -> BaselineBulkSnapshot:
    return BaselineBulkSnapshot(
        provider_name=provider_name,
        source_class=source_class,
        effective_date=effective_date.isoformat(),
        canonical_url=canonical_url,
        request_id=request_id,
        provider_request_id=request_id,
        fetched_at=fetched_at,
        content_hash=content_hash,
        rows=(),
        status=_snapshot_failure_status(error_category).value,
        error_category=error_category,
        page_count=page_count,
    )


def _missing_credential_snapshot(
    *,
    provider_name: str,
    source_class: str,
    effective_date: date,
    canonical_url: str,
) -> BaselineBulkSnapshot:
    request_id = "BASEMISS-" + stable_hash(
        {"provider": provider_name, "source": source_class, "date": effective_date.isoformat()}
    )[:24]
    return _failed_snapshot(
        provider_name=provider_name,
        source_class=source_class,
        effective_date=effective_date,
        canonical_url=canonical_url,
        request_id=request_id,
        fetched_at=_utc_now(),
        content_hash=hashlib.sha256(b"").hexdigest(),
        error_category="MISSING_CREDENTIAL",
    )


def _snapshot_failure_status(error: str) -> BulkSnapshotStatus:
    if error in {"MISSING_CREDENTIAL", "INVALID_CREDENTIAL", "PROVIDER_AUTH_FAILURE"}:
        return BulkSnapshotStatus.AUTH_FAILED
    if error == "PROVIDER_RATE_LIMIT":
        return BulkSnapshotStatus.RATE_LIMITED
    if error == "RUNTIME_BUDGET_EXHAUSTED":
        return BulkSnapshotStatus.BUDGET_EXHAUSTED
    return BulkSnapshotStatus.PROVIDER_FAILED


def _lane_failure_status(snapshot: BaselineBulkSnapshot) -> BaselineLaneStatus:
    return {
        BulkSnapshotStatus.AUTH_FAILED.value: BaselineLaneStatus.AUTH_FAILED,
        BulkSnapshotStatus.RATE_LIMITED.value: BaselineLaneStatus.RATE_LIMITED,
        BulkSnapshotStatus.BUDGET_EXHAUSTED.value: BaselineLaneStatus.BUDGET_EXHAUSTED,
    }.get(snapshot.status, BaselineLaneStatus.PROVIDER_FAILED)


def _http_failure(status_code: int) -> str | None:
    if status_code in {401, 403}:
        return "PROVIDER_AUTH_FAILURE"
    if status_code == 429:
        return "PROVIDER_RATE_LIMIT"
    if status_code >= 400:
        return "PROVIDER_NETWORK_FAILURE"
    return None


def _dart_row_as_of_safe(row: Mapping[str, Any], *, as_of: date) -> bool:
    raw = str(row.get("rcept_dt") or "")
    try:
        observed = datetime.strptime(raw, "%Y%m%d").date()
    except ValueError:
        return False
    return observed <= as_of


def _report_name(row: Mapping[str, Any]) -> str:
    return str(row.get("report_nm") or row.get("report_name") or "")


def _contains_any(value: str, tokens: Sequence[str]) -> bool:
    return any(token in value for token in tokens)


def _filing_source_ids(rows: Sequence[Mapping[str, Any]]) -> tuple[str, ...]:
    return tuple(
        "DART-RCEPT-" + str(row.get("rcept_no"))
        for row in rows
        if str(row.get("rcept_no") or "").strip()
    )


def _filing_ref(row: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "rcept_no": row.get("rcept_no"),
        "rcept_date": _yyyymmdd_to_iso(row.get("rcept_dt")),
        "report_name": _report_name(row),
        "corp_code": row.get("corp_code"),
    }


def _yyyymmdd_to_iso(value: Any) -> str | None:
    raw = str(value or "")
    try:
        return datetime.strptime(raw, "%Y%m%d").date().isoformat()
    except ValueError:
        return None


def _number(value: Any) -> int | float | None:
    raw = str(value or "").replace(",", "").strip()
    if not raw:
        return None
    try:
        number = float(raw)
    except ValueError:
        return None
    return int(number) if number.is_integer() else number


def _combined_hash(raw_pages: Sequence[bytes]) -> str:
    digest = hashlib.sha256()
    for raw in raw_pages:
        digest.update(raw)
    return digest.hexdigest()


def _int(value: Any, *, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _is_sha256(value: str) -> bool:
    return len(value) == 64 and all(character in "0123456789abcdef" for character in value)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


__all__ = [
    "BASELINE_LANE_SCHEMA_VERSION",
    "BaselineBulkSnapshot",
    "BaselineBulkTransport",
    "BaselineLane",
    "BaselineLaneRecord",
    "BaselineLaneStatus",
    "BaselineMaterializationResult",
    "BaselineMaterializerConfig",
    "BulkSnapshotStatus",
    "CurrentBaselineMaterializer",
    "RequestsBaselineBulkTransport",
    "load_baseline_lanes",
    "write_baseline_materialization",
]
