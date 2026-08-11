"""Bulk-first current KRX universe materialization with strict provenance."""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

import requests

from e2r.env import load_project_env
from e2r.production.metadata import stable_hash, write_json, write_jsonl


KRX_UNIVERSE_SCHEMA_VERSION = "e2r_live_krx_universe_v1"
_KRX_OPENAPI_BASE = "https://data-dbg.krx.co.kr/svc/apis/sto"
_MARKET_ENDPOINTS = {
    "KOSPI": "stk_isu_base_info",
    "KOSDAQ": "ksq_isu_base_info",
}
_SYMBOL_RE = re.compile(r"^[0-9A-Z]{6}$")


@dataclass(frozen=True)
class UniverseMaterializerConfig:
    as_of_date: str
    max_trading_day_lookback: int = 7
    excluded_instrument_types: tuple[str, ...] = (
        "ETF",
        "ETN",
        "SPAC",
        "PREFERRED",
        "REIT",
        "INVESTMENT_COMPANY",
        "DR",
    )
    request_timeout_seconds: float = 30.0
    test_mode: bool = False

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if self.max_trading_day_lookback < 0 or self.max_trading_day_lookback > 31:
            raise ValueError("KRX universe trading-day lookback must be bounded by 31")
        if self.request_timeout_seconds <= 0 or self.request_timeout_seconds > 120:
            raise ValueError("KRX universe request timeout must be bounded")
        if not self.excluded_instrument_types:
            raise ValueError("KRX universe exclusion policy required")


@dataclass(frozen=True)
class KrxBulkResponse:
    market: str
    effective_date: str
    request_id: str
    canonical_url: str
    provider_request_id: str
    fetched_at: str
    content_hash: str
    rows: tuple[Mapping[str, Any], ...]
    status: str = "FETCHED"
    error_category: str | None = None

    def __post_init__(self) -> None:
        if self.market not in _MARKET_ENDPOINTS:
            raise ValueError("unsupported KRX universe market")
        date.fromisoformat(self.effective_date)
        if not self.canonical_url.startswith(_KRX_OPENAPI_BASE):
            raise ValueError("KRX universe response must use official OpenAPI endpoint")
        if not re.fullmatch(r"[0-9a-f]{64}", self.content_hash):
            raise ValueError("KRX universe response content hash invalid")
        if self.status == "FETCHED" and self.error_category:
            raise ValueError("fetched KRX response cannot carry error category")

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["rows"] = [dict(row) for row in self.rows]
        return payload


class KrxUniverseTransport(Protocol):
    def fetch_market(
        self,
        *,
        market: str,
        effective_date: date,
        credential: str,
        timeout_seconds: float,
    ) -> KrxBulkResponse:
        ...


class RequestsKrxUniverseTransport:
    def fetch_market(
        self,
        *,
        market: str,
        effective_date: date,
        credential: str,
        timeout_seconds: float,
    ) -> KrxBulkResponse:
        endpoint = _MARKET_ENDPOINTS[market]
        url = f"{_KRX_OPENAPI_BASE}/{endpoint}"
        request_id = "KRXREQ-" + stable_hash(
            {"market": market, "effective_date": effective_date.isoformat(), "endpoint": endpoint}
        )[:24]
        fetched_at = _utc_now()
        try:
            response = requests.get(
                url,
                headers={"AUTH_KEY": credential},
                params={"basDd": effective_date.strftime("%Y%m%d")},
                timeout=(5.0, timeout_seconds),
            )
            raw = response.content
            content_hash = hashlib.sha256(raw).hexdigest()
            if response.status_code in {401, 403}:
                return _error_response(
                    market=market,
                    effective_date=effective_date,
                    request_id=request_id,
                    url=url,
                    fetched_at=fetched_at,
                    content_hash=content_hash,
                    error_category="PROVIDER_AUTH_FAILURE",
                )
            response.raise_for_status()
            payload = response.json()
            rows = payload.get("OutBlock_1")
            if not isinstance(rows, list):
                return _error_response(
                    market=market,
                    effective_date=effective_date,
                    request_id=request_id,
                    url=url,
                    fetched_at=fetched_at,
                    content_hash=content_hash,
                    error_category="PROVIDER_SCHEMA_CHANGED",
                )
            return KrxBulkResponse(
                market=market,
                effective_date=effective_date.isoformat(),
                request_id=request_id,
                canonical_url=str(response.url),
                provider_request_id=(
                    response.headers.get("X-Request-ID") or request_id
                ),
                fetched_at=fetched_at,
                content_hash=content_hash,
                rows=tuple(dict(row) for row in rows if isinstance(row, Mapping)),
            )
        except requests.RequestException as exc:
            return _error_response(
                market=market,
                effective_date=effective_date,
                request_id=request_id,
                url=url,
                fetched_at=fetched_at,
                content_hash=hashlib.sha256(b"").hexdigest(),
                error_category=(
                    "PROVIDER_RATE_LIMIT"
                    if getattr(exc.response, "status_code", None) == 429
                    else "PROVIDER_NETWORK_FAILURE"
                ),
            )
        except (TypeError, ValueError, json.JSONDecodeError):
            return _error_response(
                market=market,
                effective_date=effective_date,
                request_id=request_id,
                url=url,
                fetched_at=fetched_at,
                content_hash=hashlib.sha256(b"").hexdigest(),
                error_category="PROVIDER_SCHEMA_CHANGED",
            )


@dataclass(frozen=True)
class LiveUniverseRow:
    symbol: str | None
    company_name: str | None
    market: str
    security_group: str
    stock_certificate_type: str
    sector_type: str
    listing_date: str | None
    listing_status: str
    source_effective_date: str
    source_url: str
    source_document_id: str
    source_content_hash: str
    source_request_id: str
    source_mode: str
    eligible: bool
    exclusion_reason: str | None
    raw_fields: Mapping[str, Any]
    schema_version: str = KRX_UNIVERSE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        date.fromisoformat(self.source_effective_date)
        if self.symbol is not None and not _SYMBOL_RE.fullmatch(self.symbol):
            raise ValueError("KRX universe symbol must be a six-character KRX short code")
        if self.eligible and (
            not self.symbol or not self.company_name or self.exclusion_reason
        ):
            raise ValueError("eligible KRX universe row identity/exclusion mismatch")
        if not self.eligible and not self.exclusion_reason:
            raise ValueError("excluded KRX universe row requires reason")
        if not self.source_url.startswith(_KRX_OPENAPI_BASE):
            raise ValueError("KRX universe row must retain official source URL")
        if not re.fullmatch(r"[0-9a-f]{64}", self.source_content_hash):
            raise ValueError("KRX universe row source hash invalid")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class UniverseMaterializationResult:
    as_of_date: str
    source_effective_date: str | None
    status: str
    raw_rows: tuple[LiveUniverseRow, ...]
    eligible_rows: tuple[LiveUniverseRow, ...]
    excluded_rows: tuple[LiveUniverseRow, ...]
    request_attempts: tuple[KrxBulkResponse, ...]
    blockers: tuple[str, ...]
    audit: Mapping[str, Any]

    def __post_init__(self) -> None:
        date.fromisoformat(self.as_of_date)
        if self.source_effective_date:
            if date.fromisoformat(self.source_effective_date) > date.fromisoformat(self.as_of_date):
                raise ValueError("future KRX source date entered universe result")
        if len(self.raw_rows) != len(self.eligible_rows) + len(self.excluded_rows):
            raise ValueError("KRX universe partition mismatch")


class CurrentKrxUniverseMaterializer:
    def __init__(self, transport: KrxUniverseTransport | None = None) -> None:
        self.transport = transport or RequestsKrxUniverseTransport()

    def materialize(
        self,
        config: UniverseMaterializerConfig,
        *,
        credential: str | None = None,
        env_file: str | Path | None = ".env",
    ) -> UniverseMaterializationResult:
        if credential is None and not config.test_mode:
            load_project_env(env_file, override=False)
            credential = os.environ.get("KRX_OPENAPI_KEY")
        if not str(credential or "").strip():
            return _empty_result(
                config,
                status="PROVIDER_PENDING",
                blockers=("MISSING_CREDENTIAL:KRX_OPENAPI_KEY",),
            )
        as_of = date.fromisoformat(config.as_of_date)
        attempts: list[KrxBulkResponse] = []
        selected: tuple[KrxBulkResponse, ...] | None = None
        for days_back in range(config.max_trading_day_lookback + 1):
            effective = as_of - timedelta(days=days_back)
            responses = tuple(
                self.transport.fetch_market(
                    market=market,
                    effective_date=effective,
                    credential=str(credential),
                    timeout_seconds=config.request_timeout_seconds,
                )
                for market in _MARKET_ENDPOINTS
            )
            attempts.extend(responses)
            errors = tuple(
                response.error_category for response in responses if response.error_category
            )
            if errors:
                return _empty_result(
                    config,
                    status="PROVIDER_PENDING",
                    blockers=tuple(dict.fromkeys(errors)),
                    attempts=tuple(attempts),
                )
            if all(response.rows for response in responses):
                selected = responses
                break
        if selected is None:
            return _empty_result(
                config,
                status="SOURCE_GAP",
                blockers=("UNIVERSE_FETCH_FAILURE:NO_NONEMPTY_TRADING_DAY",),
                attempts=tuple(attempts),
            )
        rows = _normalize_rows(selected, config=config)
        eligible = tuple(row for row in rows if row.eligible)
        excluded = tuple(row for row in rows if not row.eligible)
        audit = _audit_universe(
            config=config,
            rows=rows,
            eligible=eligible,
            attempts=tuple(attempts),
        )
        status = (
            "CURRENT_UNIVERSE_MATERIALIZATION_PASS"
            if audit["hard_acceptance_pass"]
            else "CURRENT_UNIVERSE_MATERIALIZATION_FAIL"
        )
        blockers = () if audit["hard_acceptance_pass"] else tuple(audit["blockers"])
        return UniverseMaterializationResult(
            as_of_date=config.as_of_date,
            source_effective_date=selected[0].effective_date,
            status=status,
            raw_rows=rows,
            eligible_rows=eligible,
            excluded_rows=excluded,
            request_attempts=tuple(attempts),
            blockers=blockers,
            audit=audit,
        )


def write_universe_materialization(
    result: UniverseMaterializationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {
        "raw": root / "universe_raw.jsonl",
        "eligible": root / "universe_eligible.jsonl",
        "excluded": root / "universe_excluded.jsonl",
        "provenance": root / "universe_provenance.json",
        "audit": root / "universe_audit.json",
    }
    write_jsonl(paths["raw"], (row.to_dict() for row in result.raw_rows))
    write_jsonl(paths["eligible"], (row.to_dict() for row in result.eligible_rows))
    write_jsonl(paths["excluded"], (row.to_dict() for row in result.excluded_rows))
    write_json(
        paths["provenance"],
        {
            "schema_version": "e2r_live_krx_universe_provenance_v1",
            "as_of_date": result.as_of_date,
            "source_effective_date": result.source_effective_date,
            "status": result.status,
            "blockers": list(result.blockers),
            "request_attempts": [
                {
                    **response.to_dict(),
                    "rows": None,
                    "row_count": len(response.rows),
                }
                for response in result.request_attempts
            ],
            "raw_universe_hash": stable_hash([row.to_dict() for row in result.raw_rows]),
            "eligible_universe_hash": stable_hash(
                [row.to_dict() for row in result.eligible_rows]
            ),
        },
    )
    write_json(paths["audit"], dict(result.audit))
    return paths


def load_universe_rows(path: str | Path) -> tuple[LiveUniverseRow, ...]:
    """Load a normalized universe leaf while preserving its schema checks."""

    source = Path(path)
    if not source.is_file():
        return ()
    rows: list[LiveUniverseRow] = []
    with source.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
                rows.append(
                    LiveUniverseRow(
                        **{
                            **payload,
                            "raw_fields": dict(payload.get("raw_fields") or {}),
                        }
                    )
                )
            except (TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"invalid normalized universe row at line {line_number}: {exc}"
                ) from exc
    symbols = [row.symbol for row in rows if row.eligible]
    if len(symbols) != len(set(symbols)):
        raise ValueError("duplicate eligible symbol in normalized universe leaf")
    return tuple(rows)


def _normalize_rows(
    responses: Sequence[KrxBulkResponse],
    *,
    config: UniverseMaterializerConfig,
) -> tuple[LiveUniverseRow, ...]:
    drafts: list[dict[str, Any]] = []
    source_mode = "TEST_FIXTURE" if config.test_mode else "LIVE"
    for response in responses:
        for raw in response.rows:
            symbol = _symbol(raw)
            company_name = _text(raw, "ISU_ABBRV", "ISU_NM", "ITMS_NM")
            security_group = _text(raw, "SECUGRP_NM") or ""
            certificate_type = _text(raw, "KIND_STKCERT_TP_NM") or ""
            sector_type = _text(raw, "SECT_TP_NM") or ""
            listing_date = _krx_date(_text(raw, "LIST_DD"))
            reason = _exclusion_reason(
                symbol=symbol,
                company_name=company_name,
                security_group=security_group,
                certificate_type=certificate_type,
                sector_type=sector_type,
                excluded_types=set(config.excluded_instrument_types),
            )
            drafts.append(
                {
                    "symbol": symbol,
                    "company_name": company_name,
                    "market": response.market,
                    "security_group": security_group,
                    "stock_certificate_type": certificate_type,
                    "sector_type": sector_type,
                    "listing_date": listing_date,
                    "listing_status": "LISTED",
                    "source_effective_date": response.effective_date,
                    "source_url": response.canonical_url,
                    "source_document_id": f"krx:{response.market}:{response.effective_date}",
                    "source_content_hash": response.content_hash,
                    # Use the deterministic request identity in every row.
                    # The provider's optional X-Request-ID remains preserved in
                    # the provenance snapshot, but must not change row identity.
                    "source_request_id": response.request_id,
                    "source_mode": source_mode,
                    "exclusion_reason": reason,
                    "raw_fields": dict(raw),
                }
            )
    symbol_counts: dict[str, int] = {}
    for row in drafts:
        if row["symbol"]:
            symbol_counts[row["symbol"]] = symbol_counts.get(row["symbol"], 0) + 1
    normalized = []
    for row in sorted(drafts, key=lambda item: (str(item["symbol"] or ""), item["market"])):
        reason = row["exclusion_reason"]
        if row["symbol"] and symbol_counts[row["symbol"]] > 1:
            reason = "DUPLICATE_SYMBOL"
        normalized.append(
            LiveUniverseRow(
                **{**row, "eligible": reason is None, "exclusion_reason": reason}
            )
        )
    return tuple(normalized)


def _exclusion_reason(
    *,
    symbol: str | None,
    company_name: str | None,
    security_group: str,
    certificate_type: str,
    sector_type: str,
    excluded_types: set[str],
) -> str | None:
    if not symbol:
        return "MISSING_OR_INVALID_SYMBOL"
    if not company_name:
        return "MISSING_COMPANY_NAME"
    combined = " ".join((company_name, security_group, certificate_type, sector_type)).upper()
    if "SPAC" in excluded_types and ("SPAC" in combined or "스팩" in combined):
        return "SPAC"
    if "PREFERRED" in excluded_types and certificate_type != "보통주":
        return "PREFERRED_OR_CLASS_SHARE"
    if "REIT" in excluded_types and (
        security_group == "부동산투자회사" or "리츠" in company_name.upper()
    ):
        return "REIT"
    if "INVESTMENT_COMPANY" in excluded_types and security_group in {
        "투자회사",
        "사회간접자본투융자회사",
    }:
        return "INVESTMENT_COMPANY"
    if "DR" in excluded_types and security_group == "주식예탁증권":
        return "DR"
    if "ETF" in excluded_types and "ETF" in combined:
        return "ETF"
    if "ETN" in excluded_types and "ETN" in combined:
        return "ETN"
    if security_group not in {"주권", "외국주권"}:
        return "NON_COMMON_STOCK_SECURITY_GROUP"
    return None


def _audit_universe(
    *,
    config: UniverseMaterializerConfig,
    rows: Sequence[LiveUniverseRow],
    eligible: Sequence[LiveUniverseRow],
    attempts: Sequence[KrxBulkResponse],
) -> dict[str, Any]:
    symbols = [row.symbol for row in eligible if row.symbol]
    as_of = date.fromisoformat(config.as_of_date)
    critical = {
        "raw_universe_below_1000": int(len(rows) <= 1000),
        "eligible_universe_below_1000": int(len(eligible) <= 1000),
        "missing_symbol": sum(not row.symbol for row in rows),
        "missing_company_name": sum(not row.company_name for row in rows),
        "duplicate_eligible_symbol": len(symbols) - len(set(symbols)),
        "fixture_symbol": sum(row.source_mode != "LIVE" for row in rows),
        "generic_portal_counted_as_universe": sum(
            "data.krx.co.kr/contents/MDC/MAIN" in row.source_url for row in rows
        ),
        "future_universe_data": sum(
            date.fromisoformat(row.source_effective_date) > as_of for row in rows
        ),
    }
    blockers = [key.upper() for key, value in critical.items() if value]
    exclusion_counts: dict[str, int] = {}
    for row in rows:
        if row.exclusion_reason:
            exclusion_counts[row.exclusion_reason] = exclusion_counts.get(row.exclusion_reason, 0) + 1
    return {
        "schema_version": "e2r_live_universe_audit_v1",
        "as_of_date": config.as_of_date,
        "source_effective_date": rows[0].source_effective_date if rows else None,
        "raw_universe_count": len(rows),
        "eligible_universe_count": len(eligible),
        "excluded_universe_count": len(rows) - len(eligible),
        "missing_symbol_count": critical["missing_symbol"],
        "missing_company_name_count": critical["missing_company_name"],
        "duplicate_eligible_symbol_count": critical["duplicate_eligible_symbol"],
        "fixture_symbol_count": critical["fixture_symbol"],
        "generic_portal_counted_as_universe_count": critical[
            "generic_portal_counted_as_universe"
        ],
        "future_universe_data_count": critical["future_universe_data"],
        "provider_request_count": len(attempts),
        "selected_market_count": len({row.market for row in rows}),
        "exclusion_reason_counts": dict(sorted(exclusion_counts.items())),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "blockers": blockers,
        "hard_acceptance_pass": sum(critical.values()) == 0,
    }


def _empty_result(
    config: UniverseMaterializerConfig,
    *,
    status: str,
    blockers: tuple[str, ...],
    attempts: tuple[KrxBulkResponse, ...] = (),
) -> UniverseMaterializationResult:
    audit = {
        "schema_version": "e2r_live_universe_audit_v1",
        "as_of_date": config.as_of_date,
        "source_effective_date": None,
        "raw_universe_count": 0,
        "eligible_universe_count": 0,
        "excluded_universe_count": 0,
        "missing_symbol_count": 0,
        "missing_company_name_count": 0,
        "duplicate_eligible_symbol_count": 0,
        "fixture_symbol_count": 0,
        "generic_portal_counted_as_universe_count": 0,
        "future_universe_data_count": 0,
        "provider_request_count": len(attempts),
        "selected_market_count": 0,
        "exclusion_reason_counts": {},
        "critical_counts": {"universe_not_materialized": 1},
        "critical_count_sum": 1,
        "blockers": list(blockers),
        "hard_acceptance_pass": False,
    }
    return UniverseMaterializationResult(
        as_of_date=config.as_of_date,
        source_effective_date=None,
        status=status,
        raw_rows=(),
        eligible_rows=(),
        excluded_rows=(),
        request_attempts=attempts,
        blockers=blockers,
        audit=audit,
    )


def _error_response(
    *,
    market: str,
    effective_date: date,
    request_id: str,
    url: str,
    fetched_at: str,
    content_hash: str,
    error_category: str,
) -> KrxBulkResponse:
    return KrxBulkResponse(
        market=market,
        effective_date=effective_date.isoformat(),
        request_id=request_id,
        canonical_url=url,
        provider_request_id=request_id,
        fetched_at=fetched_at,
        content_hash=content_hash,
        rows=(),
        status="PROVIDER_FAILED",
        error_category=error_category,
    )


def _symbol(row: Mapping[str, Any]) -> str | None:
    for key in ("ISU_SRT_CD", "SHORT_CODE", "SRT_CD", "srtnCd", "symbol"):
        value = str(row.get(key) or "").strip()
        if _SYMBOL_RE.fullmatch(value):
            return value
    return None


def _text(row: Mapping[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = str(row.get(key) or "").strip()
        if value:
            return value
    return None


def _krx_date(value: str | None) -> str | None:
    if not value:
        return None
    clean = value.replace("/", "").replace("-", "")
    if re.fullmatch(r"[0-9]{8}", clean):
        return date(int(clean[:4]), int(clean[4:6]), int(clean[6:8])).isoformat()
    return None


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


__all__ = [
    "KRX_UNIVERSE_SCHEMA_VERSION",
    "CurrentKrxUniverseMaterializer",
    "KrxBulkResponse",
    "KrxUniverseTransport",
    "LiveUniverseRow",
    "RequestsKrxUniverseTransport",
    "UniverseMaterializationResult",
    "UniverseMaterializerConfig",
    "write_universe_materialization",
]
