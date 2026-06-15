"""Safe raw API probe runner for Korea live-lite schema discovery."""

from __future__ import annotations

import json
import os
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field, fields, is_dataclass
from datetime import date, datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.cheap_scan.korea_sources import DataGoKrFSCConnector
from e2r.env import load_project_env
from e2r.models import DisclosureEvent, FinancialActual, Instrument, Market, PriceBar
from e2r.probe.schema_profiler import SchemaProfile, profile_payload, render_schema_markdown, select_item_rows, find_list_candidates
from e2r.research.naver_search_provider import NAVER_SEARCH_ENDPOINTS, NaverFreeSearchProvider
from e2r.research.search_provider import SearchResult
from e2r.sources import KRXConnector, OpenDARTConnector
from e2r.sources.http_client import HttpClient, HttpClientStats, HttpResult
from e2r.sources.rate_limit import RateLimiter, SourceRateLimit
from e2r.sources.source_errors import SourceRequest, date_value, float_or_none, int_or_none


PROBE_QUERY = "삼성전자 수주잔고"
PROBE_COMPANY = "삼성전자"


@dataclass(frozen=True)
class APIProbeConfig:
    """Configuration for a tiny raw API probe run."""

    as_of_date: date
    output_directory: str | Path = "output/api_probe"
    live_enabled: bool = False
    fixture_mode: bool = True
    env_file: str | Path | None = ".env"
    max_requests_per_source: int = 3
    timeout_seconds: int = 10
    use_cache: bool = True
    sample_symbol: str = "005930"
    sample_company: str = PROBE_COMPANY
    sample_query: str = PROBE_QUERY
    sample_market: str = "KR"
    probe_data_go_kr: bool = True
    probe_krx: bool = True
    probe_opendart: bool = True
    probe_naver: bool = True
    save_raw: bool = True

    def __post_init__(self) -> None:
        if type(self.as_of_date) is not date:
            raise ValueError("as_of_date must be a date")
        if self.max_requests_per_source <= 0:
            raise ValueError("max_requests_per_source must be positive")
        if self.timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        if not self.sample_symbol.strip():
            raise ValueError("sample_symbol must be non-empty")
        if not self.sample_company.strip():
            raise ValueError("sample_company must be non-empty")
        if not self.sample_query.strip():
            raise ValueError("sample_query must be non-empty")


@dataclass(frozen=True)
class ProbeRawResponse:
    """Stored raw response metadata."""

    source_name: str
    path: Path
    ok: bool
    status_code: int | None = None
    error: str | None = None


@dataclass(frozen=True)
class NormalizerDryRun:
    """Result of attempting to normalize a raw response."""

    source_name: str
    normalizer_name: str
    rows_seen: int
    rows_normalized: int
    failures: int
    failure_examples: tuple[str, ...] = field(default_factory=tuple)
    missing_expected_fields: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class APIProbeRunLog:
    """Machine-readable probe audit log."""

    as_of_date: date
    fixture_mode: bool
    live_enabled: bool
    source_modes: Mapping[str, str]
    credentials_present: Mapping[str, bool]
    requests_attempted: int
    requests_succeeded: int
    requests_failed: int
    cache_hits: int
    cache_writes: int
    rate_limit_waits: int
    rate_limit_skips: int
    failed_sources: tuple[str, ...] = field(default_factory=tuple)
    skipped_sources: tuple[str, ...] = field(default_factory=tuple)
    fallback_reasons: Mapping[str, str] = field(default_factory=dict)
    warnings: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class APIProbeResult:
    """Output paths and summaries from one API probe."""

    as_of_date: date
    output_directory: Path
    raw_responses: tuple[ProbeRawResponse, ...]
    schema_profiles: tuple[SchemaProfile, ...]
    normalizer_reports: tuple[NormalizerDryRun, ...]
    schema_summary_json_path: Path
    schema_summary_md_path: Path
    normalizer_report_json_path: Path
    normalizer_report_md_path: Path
    run_log_path: Path
    run_log: APIProbeRunLog


@dataclass(frozen=True)
class ProbeTarget:
    source_name: str
    group_name: str
    raw_filename: str
    request: SourceRequest


class APIProbeRunner:
    """Run tiny source probes and write raw/schema/normalizer reports."""

    def __init__(
        self,
        *,
        http_client: HttpClient | None = None,
        fixture_payloads: Mapping[str, Any] | None = None,
    ) -> None:
        self.http_client = http_client
        payloads = dict(DEFAULT_FIXTURE_PAYLOADS)
        if fixture_payloads:
            payloads.update(fixture_payloads)
        self.fixture_payloads = payloads

    def run(self, config: APIProbeConfig) -> APIProbeResult:
        if config.live_enabled or not config.fixture_mode:
            load_project_env(config.env_file)
        output_dir = Path(config.output_directory) / config.as_of_date.isoformat()
        raw_dir = output_dir / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        http_client = self.http_client or HttpClient(
            timeout_seconds=config.timeout_seconds,
            rate_limiter=_probe_rate_limiter(config),
        )
        credentials = _credentials_present()
        targets, source_modes, skipped_sources, fallback_reasons = self._build_targets(config, credentials)
        raw_responses: list[ProbeRawResponse] = []
        payloads: dict[str, Any] = {}
        failed_sources: list[str] = []

        for target in targets:
            response, payload = self._collect_target(target, config=config, raw_dir=raw_dir, http_client=http_client)
            raw_responses.append(response)
            if not response.ok:
                failed_sources.append(target.source_name)
                continue
            try:
                payloads[target.source_name] = payload if payload is not None else _load_payload_from_raw(response.path)
            except ValueError as exc:
                failed_sources.append(target.source_name)
                raw_responses[-1] = ProbeRawResponse(
                    source_name=response.source_name,
                    path=response.path,
                    ok=False,
                    status_code=response.status_code,
                    error=str(exc),
                )

        schema_profiles = tuple(profile_payload(source_name, payload) for source_name, payload in payloads.items())
        normalizer_reports = tuple(_normalizer_dry_run(source_name, payload, config.as_of_date, config.sample_query) for source_name, payload in payloads.items())

        schema_json_path = output_dir / "schema_summary.json"
        schema_md_path = output_dir / "schema_summary.md"
        normalizer_json_path = output_dir / "normalizer_report.json"
        normalizer_md_path = output_dir / "normalizer_report.md"
        run_log_path = output_dir / "probe_run_log.json"

        schema_json_path.write_text(json.dumps(_jsonable(schema_profiles), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
        schema_md_path.write_text(render_schema_markdown(schema_profiles), encoding="utf-8")
        normalizer_json_path.write_text(json.dumps(_jsonable(normalizer_reports), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
        normalizer_md_path.write_text(_render_normalizer_markdown(normalizer_reports), encoding="utf-8")

        run_log = APIProbeRunLog(
            as_of_date=config.as_of_date,
            fixture_mode=config.fixture_mode,
            live_enabled=config.live_enabled,
            source_modes=source_modes,
            credentials_present=credentials,
            requests_attempted=len(targets),
            requests_succeeded=sum(1 for item in raw_responses if item.ok),
            requests_failed=sum(1 for item in raw_responses if not item.ok),
            cache_hits=http_client.stats.cache_hits,
            cache_writes=http_client.stats.cache_writes,
            rate_limit_waits=http_client.stats.rate_limit_waits,
            rate_limit_skips=http_client.stats.rate_limit_skips,
            failed_sources=tuple(failed_sources),
            skipped_sources=tuple(skipped_sources),
            fallback_reasons=fallback_reasons,
            warnings=_probe_warnings(schema_profiles, normalizer_reports),
        )
        run_log_path.write_text(json.dumps(_jsonable(run_log), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")

        return APIProbeResult(
            as_of_date=config.as_of_date,
            output_directory=output_dir,
            raw_responses=tuple(raw_responses),
            schema_profiles=schema_profiles,
            normalizer_reports=normalizer_reports,
            schema_summary_json_path=schema_json_path,
            schema_summary_md_path=schema_md_path,
            normalizer_report_json_path=normalizer_json_path,
            normalizer_report_md_path=normalizer_md_path,
            run_log_path=run_log_path,
            run_log=run_log,
        )

    def _build_targets(
        self,
        config: APIProbeConfig,
        credentials: Mapping[str, bool],
    ) -> tuple[tuple[ProbeTarget, ...], dict[str, str], list[str], dict[str, str]]:
        targets: list[ProbeTarget] = []
        source_modes: dict[str, str] = {}
        skipped_sources: list[str] = []
        fallback_reasons: dict[str, str] = {}

        def add(target: ProbeTarget, credential_key: str | None = None) -> None:
            if config.fixture_mode:
                source_modes[target.source_name] = "fixture"
                targets.append(target)
                return
            if not config.live_enabled:
                source_modes[target.source_name] = "request_only"
                skipped_sources.append(target.source_name)
                return
            if credential_key is not None and not credentials.get(credential_key, False):
                source_modes[target.source_name] = "fallback"
                skipped_sources.append(target.source_name)
                fallback_reasons[target.source_name] = f"missing_{credential_key}"
                return
            source_modes[target.source_name] = "live_executed"
            targets.append(target)

        as_of = config.as_of_date
        market = Market(config.sample_market)
        if config.probe_opendart:
            add(_opendart_target(as_of), "OPENDART_API_KEY")
        else:
            source_modes["opendart_list"] = "disabled_optional"
            skipped_sources.append("opendart_list")

        if config.probe_naver:
            for target in _naver_targets(as_of, config.sample_query):
                add(target, "NAVER_CLIENT_ID/NAVER_CLIENT_SECRET")
        else:
            for name in ("naver_news", "naver_web", "naver_doc"):
                source_modes[name] = "disabled_optional"
                skipped_sources.append(name)

        if config.probe_data_go_kr:
            for target in _data_go_kr_targets(config.sample_symbol, config.sample_company, market, as_of):
                add(target, "DATA_GO_KR_SERVICE_KEY")
        else:
            for name in (
                "data_go_kr_listed_items",
                "data_go_kr_stock_prices",
                "data_go_kr_corp_basic",
                "data_go_kr_financial_stat",
                "data_go_kr_disclosure_info",
            ):
                source_modes[name] = "disabled_optional"
                skipped_sources.append(name)

        if config.probe_krx:
            for target in _krx_targets(as_of):
                add(target, "KRX_OPENAPI_KEY")
        else:
            for name in (
                "krx_stk_bydd_trd",
                "krx_ksq_bydd_trd",
                "krx_stk_isu_base_info",
                "krx_ksq_isu_base_info",
                "krx_kospi_dd_trd",
                "krx_kosdaq_dd_trd",
            ):
                source_modes[name] = "disabled_optional"
                skipped_sources.append(name)
        return tuple(targets), source_modes, skipped_sources, fallback_reasons

    def _collect_target(
        self,
        target: ProbeTarget,
        *,
        config: APIProbeConfig,
        raw_dir: Path,
        http_client: HttpClient,
    ) -> tuple[ProbeRawResponse, Any | None]:
        raw_path = raw_dir / target.raw_filename
        if config.fixture_mode:
            payload = self.fixture_payloads.get(target.source_name, {})
            if config.save_raw:
                _write_raw_payload(raw_path, payload)
                return ProbeRawResponse(source_name=target.source_name, path=raw_path, ok=True, status_code=200), None
            return ProbeRawResponse(source_name=target.source_name, path=raw_path, ok=True, status_code=200), payload
        if config.use_cache and raw_path.exists():
            http_client.stats.cache_hits += 1
            return ProbeRawResponse(source_name=target.source_name, path=raw_path, ok=True, status_code=200), None
        result = http_client.get_text(target.request)
        if not result.ok or result.text is None:
            if config.save_raw:
                _write_failure_payload(raw_path, target, result)
            return ProbeRawResponse(source_name=target.source_name, path=raw_path, ok=False, status_code=result.status_code, error=result.error), None
        if config.save_raw:
            stored_path = _write_raw_text(raw_path, result.text)
            http_client.stats.cache_writes += 1
            return ProbeRawResponse(source_name=target.source_name, path=stored_path, ok=True, status_code=result.status_code), None
        try:
            return ProbeRawResponse(source_name=target.source_name, path=raw_path, ok=True, status_code=result.status_code), _payload_from_text(result.text)
        except ValueError as exc:
            return ProbeRawResponse(source_name=target.source_name, path=raw_path, ok=False, status_code=result.status_code, error=str(exc)), None


def _opendart_target(as_of_date: date) -> ProbeTarget:
    api_key = os.environ.get("OPENDART_API_KEY")
    params: dict[str, Any] = {
        "bgn_de": as_of_date.strftime("%Y%m%d"),
        "end_de": as_of_date.strftime("%Y%m%d"),
        "page_no": 1,
        "page_count": 10,
    }
    if api_key:
        params["crtfc_key"] = api_key
    request = SourceRequest(
        method="GET",
        url="https://opendart.fss.or.kr/api/list.json",
        params=params,
        fixture_mode=False,
        credential_name="OPENDART_API_KEY",
    )
    return ProbeTarget("opendart_list", "opendart", "opendart_list.json", request)


def _naver_targets(as_of_date: date, sample_query: str = PROBE_QUERY) -> tuple[ProbeTarget, ...]:
    client_id = os.environ.get("NAVER_CLIENT_ID")
    client_secret = os.environ.get("NAVER_CLIENT_SECRET")
    headers: dict[str, str] = {}
    if client_id:
        headers["X-Naver-Client-Id"] = client_id
    if client_secret:
        headers["X-Naver-Client-Secret"] = client_secret
    targets: list[ProbeTarget] = []
    for domain, url in NAVER_SEARCH_ENDPOINTS.items():
        request = SourceRequest(
            method="GET",
            url=url,
            params={
                "query": sample_query,
                "display": 3,
                "sort": "date",
                "as_of_date": as_of_date.isoformat(),
            },
            headers=headers,
            fixture_mode=False,
            credential_name="NAVER_CLIENT_ID/NAVER_CLIENT_SECRET",
        )
        source_name = f"naver_{domain}"
        targets.append(ProbeTarget(source_name, "naver", f"{source_name}.json", request))
    return tuple(targets)


def _data_go_kr_targets(sample_symbol: str, sample_company: str, market: Market, as_of_date: date) -> tuple[ProbeTarget, ...]:
    connector = DataGoKrFSCConnector(
        service_key=os.environ.get("DATA_GO_KR_SERVICE_KEY"),
        fixture_mode=False,
    )
    start = as_of_date - timedelta(days=7)
    market_date = _market_probe_date(as_of_date)
    return (
        ProbeTarget(
            "data_go_kr_listed_items",
            "data_go_kr",
            "data_go_kr_listed_items.json",
            connector.build_listed_items_page_request(market, market_date, page_no=1, num_rows=10),
        ),
        ProbeTarget(
            "data_go_kr_stock_prices",
            "data_go_kr",
            "data_go_kr_stock_prices.json",
            connector.build_stock_price_page_request(start, as_of_date, as_of_date, page_no=1, num_rows=10),
        ),
        ProbeTarget(
            "data_go_kr_corp_basic",
            "data_go_kr",
            "data_go_kr_corp_basic.json",
            connector.build_corp_basic_info_request(sample_symbol, as_of_date, company_name=sample_company),
        ),
        ProbeTarget(
            "data_go_kr_financial_stat",
            "data_go_kr",
            "data_go_kr_financial_stat.json",
            connector.build_financial_info_request(sample_symbol, as_of_date, company_name=sample_company, fiscal_year=as_of_date.year - 1),
        ),
        ProbeTarget(
            "data_go_kr_disclosure_info",
            "data_go_kr",
            "data_go_kr_disclosure_info.json",
            connector.build_disclosure_info_request(sample_symbol, as_of_date, as_of_date, as_of_date, company_name=sample_company, include_date=False),
        ),
    )


def _krx_targets(as_of_date: date) -> tuple[ProbeTarget, ...]:
    connector = KRXConnector(fixture_mode=False, openapi_key=os.environ.get("KRX_OPENAPI_KEY"))
    market_date = _market_probe_date(as_of_date)
    return (
        ProbeTarget("krx_stk_bydd_trd", "krx", "krx_stk_bydd_trd.json", connector.build_openapi_kospi_daily_trading_request(market_date)),
        ProbeTarget("krx_ksq_bydd_trd", "krx", "krx_ksq_bydd_trd.json", connector.build_openapi_kosdaq_daily_trading_request(market_date)),
        ProbeTarget("krx_stk_isu_base_info", "krx", "krx_stk_isu_base_info.json", connector.build_openapi_kospi_issue_base_info_request(market_date)),
        ProbeTarget("krx_ksq_isu_base_info", "krx", "krx_ksq_isu_base_info.json", connector.build_openapi_kosdaq_issue_base_info_request(market_date)),
        ProbeTarget("krx_kospi_dd_trd", "krx", "krx_kospi_dd_trd.json", connector.build_openapi_kospi_index_daily_trading_request(market_date)),
        ProbeTarget("krx_kosdaq_dd_trd", "krx", "krx_kosdaq_dd_trd.json", connector.build_openapi_kosdaq_index_daily_trading_request(market_date)),
    )


def _market_probe_date(as_of_date: date) -> date:
    """Use a settled market-data date for schema probes.

    Same-day KRX/data.go.kr files can be empty before the provider publishes
    the official close. The probe only needs response shape, so yesterday is a
    safer tiny call than repeatedly probing a not-yet-published date.
    """

    return as_of_date - timedelta(days=1)


def _normalizer_dry_run(source_name: str, payload: Any, as_of_date: date, sample_query: str = PROBE_QUERY) -> NormalizerDryRun:
    rows = _rows_for_payload(payload)
    failures: list[str] = []
    normalized = 0
    normalizer_name = _normalizer_name_for(source_name)
    missing = tuple(profile_payload(source_name, payload).expected_field_comparison.get("missing_expected_fields", ()))
    try:
        if source_name.startswith("naver_"):
            results = NaverFreeSearchProvider.normalize_response(payload if isinstance(payload, Mapping) else {}, query=sample_query, as_of_date=as_of_date, source=source_name)
            return NormalizerDryRun(source_name, "NaverFreeSearchProvider.normalize_response", len(payload.get("items", ())) if isinstance(payload, Mapping) else 0, len(results), 0, (), missing)
        for row in rows:
            if _skip_unpriced_probe_row(source_name, row):
                continue
            try:
                _normalize_row(source_name, row, as_of_date)
                normalized += 1
            except Exception as exc:
                failures.append(f"{type(exc).__name__}:{exc}")
    except Exception as exc:
        failures.append(f"{type(exc).__name__}:{exc}")
    return NormalizerDryRun(
        source_name=source_name,
        normalizer_name=normalizer_name,
        rows_seen=len(rows),
        rows_normalized=normalized,
        failures=len(failures),
        failure_examples=tuple(failures[:3]),
        missing_expected_fields=missing,
    )


def _normalize_row(source_name: str, row: Mapping[str, Any], as_of_date: date) -> Instrument | PriceBar | DisclosureEvent | SearchResult:
    connector = DataGoKrFSCConnector()
    if source_name == "data_go_kr_listed_items":
        return connector.normalize_instrument(row)
    if source_name == "data_go_kr_corp_basic":
        return Instrument(
            symbol=str(row.get("srtnCd") or row.get("crno") or row.get("isinCd")),
            name=str(row.get("corpNm") or row.get("itmsNm") or row.get("crno")),
            market=Market.KR,
            exchange="KRX",
            currency="KRW",
        )
    if source_name == "data_go_kr_stock_prices":
        return connector.normalize_price_bar(row)
    if source_name == "data_go_kr_financial_stat":
        return _data_go_kr_financial_actual(row, as_of_date)
    if source_name in {"opendart_list", "data_go_kr_disclosure_info"}:
        return OpenDARTConnector.normalize_disclosure(_disclosure_row(row, as_of_date))
    if source_name in {"krx_stk_bydd_trd", "krx_ksq_bydd_trd", "krx_kospi_dd_trd", "krx_kosdaq_dd_trd"}:
        return _krx_price_bar(row, as_of_date)
    if source_name in {"krx_stk_isu_base_info", "krx_ksq_isu_base_info"}:
        return _krx_instrument(row)
    raise ValueError(f"no normalizer configured for {source_name}")


def _normalizer_name_for(source_name: str) -> str:
    if source_name == "data_go_kr_listed_items":
        return "DataGoKrFSCConnector.normalize_instrument"
    if source_name == "data_go_kr_corp_basic":
        return "data.go.kr corp-basic metadata normalizer"
    if source_name == "data_go_kr_stock_prices":
        return "DataGoKrFSCConnector.normalize_price_bar"
    if source_name == "data_go_kr_financial_stat":
        return "data.go.kr financial-stat dry-run normalizer"
    if source_name in {"opendart_list", "data_go_kr_disclosure_info"}:
        return "OpenDARTConnector.normalize_disclosure"
    if source_name.startswith("naver_"):
        return "NaverFreeSearchProvider.normalize_response"
    if source_name.startswith("krx_"):
        return "KRX probe row normalizer"
    return "not_configured"


def _rows_for_payload(payload: Any) -> list[Mapping[str, Any]]:
    candidates = find_list_candidates(payload)
    path, rows = select_item_rows(payload, candidates)
    if path == "$" and candidates:
        return []
    return rows


def _disclosure_row(row: Mapping[str, Any], as_of_date: date) -> dict[str, Any]:
    return {
        "symbol": row.get("symbol") or row.get("stock_code") or row.get("srtnCd") or row.get("corp_code") or row.get("crno") or "UNKNOWN",
        "corp_code": row.get("corp_code") or row.get("crno"),
        "corp_name": row.get("corp_name") or row.get("corpNm"),
        "report_nm": row.get("report_nm") or row.get("reportNm") or row.get("diclTitl") or row.get("title") or "disclosure",
        "rcept_no": row.get("rcept_no") or row.get("rceptNo") or row.get("reportId"),
        "rcept_dt": row.get("rcept_dt") or row.get("rceptDt") or row.get("basDt") or as_of_date.strftime("%Y%m%d"),
        "as_of_date": as_of_date.isoformat(),
    }


def _data_go_kr_financial_actual(row: Mapping[str, Any], as_of_date: date) -> FinancialActual:
    period_end = date_value(row.get("basDt") or f"{row.get('bizYear') or as_of_date.year - 1}1231")
    return FinancialActual(
        symbol=str(row.get("srtnCd") or row.get("crno") or row.get("corpNm") or "UNKNOWN"),
        fiscal_year=int(float(str(row.get("bizYear") or period_end.year))),
        fiscal_quarter=None,
        period_end=period_end,
        reported_at=datetime(as_of_date.year, as_of_date.month, as_of_date.day),
        as_of_date=as_of_date,
        source="data.go.kr FSC financial-stat probe",
        sales=float_or_none(row.get("sales") or row.get("saleAmt") or row.get("enpSaleAmt")),
        operating_profit=float_or_none(row.get("operating_profit") or row.get("op") or row.get("enpBzopPft") or row.get("bzopPft")),
        net_income=float_or_none(row.get("net_income") or row.get("enpCrtmNpf") or row.get("crtmNpf")),
        debt_ratio=float_or_none(row.get("fnclDebtRto")),
    )


def _krx_price_bar(row: Mapping[str, Any], as_of_date: date) -> PriceBar:
    close = float_or_none(row.get("TDD_CLSPRC") or row.get("CLSPRC") or row.get("IDX_CLSPRC") or row.get("CLSPRC_IDX") or row.get("clpr")) or 0.0
    return PriceBar(
        symbol=str(row.get("ISU_SRT_CD") or row.get("ISU_CD") or row.get("IDX_CLSS") or row.get("IDX_NM") or "KRX_INDEX"),
        date=date_value(row.get("BAS_DD") or row.get("TRD_DD") or row.get("basDd") or as_of_date),
        open=float_or_none(row.get("TDD_OPNPRC") or row.get("OPNPRC") or row.get("OPNPRC_IDX") or row.get("mkp")) or close,
        high=float_or_none(row.get("TDD_HGPRC") or row.get("HGPRC") or row.get("HGPRC_IDX") or row.get("hipr")) or close,
        low=float_or_none(row.get("TDD_LWPRC") or row.get("LWPRC") or row.get("LWPRC_IDX") or row.get("lopr")) or close,
        close=close,
        adj_close=close,
        volume=int_or_none(row.get("ACC_TRDVOL") or row.get("trqu")) or 0,
        trading_value=float_or_none(row.get("ACC_TRDVAL") or row.get("trPrc")) or 0.0,
        market_cap=float_or_none(row.get("MKTCAP") or row.get("mrktTotAmt")),
        source="KRX Open API probe",
        as_of_date=as_of_date,
    )


def _krx_instrument(row: Mapping[str, Any]) -> Instrument:
    return Instrument(
        symbol=str(row.get("ISU_SRT_CD") or row.get("ISU_CD")),
        name=str(row.get("ISU_NM") or row.get("ISU_ABBRV") or row.get("ISU_ENG_NM") or row.get("ISU_CD")),
        market=Market.KR,
        exchange=str(row.get("MKT_NM") or row.get("MKT_TP_NM") or "KRX"),
        listed_date=date_value(row["LIST_DD"]) if row.get("LIST_DD") else None,
        currency="KRW",
    )


def _load_payload_from_raw(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    return _payload_from_text(text, path=path)


def _payload_from_text(text: str, *, path: Path | None = None) -> Any:
    if (path is not None and path.suffix == ".xml") or text.lstrip().startswith("<"):
        parsed = _xml_to_dict(text)
        if path is not None:
            parsed_path = path.with_suffix(".parsed.json")
            parsed_path.write_text(json.dumps(parsed, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
        return parsed
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"raw response is not JSON/XML: {exc}") from exc


def _write_raw_payload(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _write_raw_text(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if text.lstrip().startswith("<"):
        xml_path = path.with_suffix(".xml")
        xml_path.write_text(text, encoding="utf-8")
        try:
            parsed = _xml_to_dict(text)
            xml_path.with_suffix(".parsed.json").write_text(json.dumps(parsed, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
        except ValueError:
            pass
        return xml_path
    path.write_text(text, encoding="utf-8")
    return path


def _write_failure_payload(path: Path, target: ProbeTarget, result: HttpResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "ok": False,
        "source_name": target.source_name,
        "status_code": result.status_code,
        "error": result.error,
        "request": _jsonable(target.request),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _skip_unpriced_probe_row(source_name: str, row: Mapping[str, Any]) -> bool:
    if source_name not in {"krx_kospi_dd_trd", "krx_kosdaq_dd_trd"}:
        return False
    close = row.get("TDD_CLSPRC") or row.get("CLSPRC") or row.get("IDX_CLSPRC") or row.get("CLSPRC_IDX")
    return float_or_none(close) is None


def _xml_to_dict(text: str) -> dict[str, Any]:
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError(f"xml_parse_error:{exc}") from exc
    return {root.tag: _xml_element_to_value(root)}


def _xml_element_to_value(element: ET.Element) -> Any:
    children = list(element)
    if not children:
        return (element.text or "").strip()
    result: dict[str, Any] = {}
    for child in children:
        value = _xml_element_to_value(child)
        if child.tag in result:
            existing = result[child.tag]
            if not isinstance(existing, list):
                result[child.tag] = [existing]
            result[child.tag].append(value)
        else:
            result[child.tag] = value
    return result


def _credentials_present() -> dict[str, bool]:
    return {
        "OPENDART_API_KEY": bool(os.environ.get("OPENDART_API_KEY")),
        "NAVER_CLIENT_ID": bool(os.environ.get("NAVER_CLIENT_ID")),
        "NAVER_CLIENT_SECRET": bool(os.environ.get("NAVER_CLIENT_SECRET")),
        "NAVER_CLIENT_ID/NAVER_CLIENT_SECRET": bool(os.environ.get("NAVER_CLIENT_ID") and os.environ.get("NAVER_CLIENT_SECRET")),
        "DATA_GO_KR_SERVICE_KEY": bool(os.environ.get("DATA_GO_KR_SERVICE_KEY")),
        "KRX_OPENAPI_KEY": bool(os.environ.get("KRX_OPENAPI_KEY")),
    }


def _probe_rate_limiter(config: APIProbeConfig) -> RateLimiter:
    limit = max(config.max_requests_per_source, 10)
    return RateLimiter(
        (
            SourceRateLimit("opendart", max_requests_per_day=limit, max_concurrency=1, min_interval_seconds=0.1),
            SourceRateLimit("naver_search", max_requests_per_day=limit, max_concurrency=1, min_interval_seconds=0.1),
            SourceRateLimit("data_go_kr", max_requests_per_day=limit, max_concurrency=1, min_interval_seconds=0.1),
            SourceRateLimit("krx", max_requests_per_day=limit, max_concurrency=1, min_interval_seconds=0.1),
        )
    )


def _probe_warnings(schema_profiles: Sequence[SchemaProfile], reports: Sequence[NormalizerDryRun]) -> tuple[str, ...]:
    warnings: list[str] = []
    for profile in schema_profiles:
        missing = profile.expected_field_comparison.get("missing_expected_fields", ())
        if missing:
            warnings.append(f"{profile.source_name}: missing expected fields {', '.join(missing)}")
    for report in reports:
        if report.failures:
            warnings.append(f"{report.source_name}: normalizer failures {report.failures}")
    return tuple(warnings)


def _render_normalizer_markdown(reports: Sequence[NormalizerDryRun]) -> str:
    lines = [
        "# API Probe Normalizer Report",
        "",
        "| source | normalizer | rows_seen | rows_normalized | failures | missing_expected_fields |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    for report in reports:
        lines.append(
            f"| {report.source_name} | `{report.normalizer_name}` | {report.rows_seen} | {report.rows_normalized} | {report.failures} | {', '.join(report.missing_expected_fields) or '(none)'} |"
        )
        for example in report.failure_examples:
            lines.append(f"| {report.source_name} failure |  |  |  |  | `{example}` |")
    return "\n".join(lines).rstrip() + "\n"


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, SourceRequest):
        return {
            "method": value.method,
            "url": value.url,
            "params": _redacted_mapping(value.params),
            "headers": _redacted_mapping(value.headers),
            "fixture_mode": value.fixture_mode,
            "credential_name": value.credential_name,
        }
    if is_dataclass(value):
        return {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(item) for item in value]
    return value


def _redacted_mapping(value: Mapping[str, Any]) -> dict[str, Any]:
    redacted: dict[str, Any] = {}
    for key, item in value.items():
        lowered = str(key).lower()
        if any(token in lowered for token in ("key", "secret", "token", "client-id", "client_secret", "auth")):
            redacted[str(key)] = "<redacted>"
        else:
            redacted[str(key)] = _jsonable(item)
    return redacted


DEFAULT_FIXTURE_PAYLOADS: Mapping[str, Any] = {
    "opendart_list": {
        "status": "000",
        "message": "정상",
        "page_no": 1,
        "total_count": 1,
        "total_page": 1,
        "list": [
            {
                "corp_code": "00126380",
                "corp_name": "삼성전자",
                "stock_code": "005930",
                "report_nm": "단일판매·공급계약체결",
                "rcept_no": "202405140001",
                "rcept_dt": "20240514",
            }
        ],
    },
    "naver_news": {
        "items": [
            {
                "title": "삼성전자 수주잔고 관련 뉴스",
                "link": "https://news.example.com/samsung",
                "originallink": "https://news.example.com/samsung",
                "description": "삼성전자 수주잔고 점검",
                "pubDate": "Tue, 14 May 2024 08:00:00 +0900",
            }
        ]
    },
    "naver_web": {"items": [{"title": "삼성전자 수주잔고 웹문서", "link": "https://web.example.com/samsung", "description": "웹문서"}]},
    "naver_doc": {"items": [{"title": "삼성전자 리포트", "link": "https://doc.example.com/samsung.pdf", "description": "전문자료"}]},
    "data_go_kr_listed_items": {
        "response": {
            "body": {
                "items": {
                    "item": [
                        {
                            "basDt": "20240514",
                            "srtnCd": "005930",
                            "isinCd": "KR7005930003",
                            "itmsNm": "삼성전자",
                            "mrktCtg": "KOSPI",
                            "corpNm": "삼성전자",
                        }
                    ]
                },
                "totalCount": 1,
            }
        }
    },
    "data_go_kr_stock_prices": {
        "response": {
            "body": {
                "items": {
                    "item": [
                        {
                            "basDt": "20240514",
                            "srtnCd": "005930",
                            "isinCd": "KR7005930003",
                            "itmsNm": "삼성전자",
                            "mrktCtg": "KOSPI",
                            "clpr": "78000",
                            "mkp": "77000",
                            "hipr": "79000",
                            "lopr": "76000",
                            "trqu": "1000000",
                            "trPrc": "78000000000",
                            "mrktTotAmt": "465000000000000",
                        }
                    ]
                },
                "totalCount": 1,
            }
        }
    },
    "data_go_kr_corp_basic": {"response": {"body": {"items": {"item": [{"corpNm": "삼성전자", "crno": "1301110006246", "enpBsadr": "경기도 수원시"}]}}}},
    "data_go_kr_financial_stat": {"response": {"body": {"items": {"item": [{"basDt": "20240514", "corpNm": "삼성전자", "enpBsadr": "경기도 수원시", "sales": "1000"}]}}}},
    "data_go_kr_disclosure_info": {"response": {"body": {"items": {"item": [{"basDt": "20240514", "corpNm": "삼성전자", "diclTitl": "유상증자 결정", "rceptNo": "D202405140001"}]}}}},
    "krx_stk_bydd_trd": {"OutBlock_1": [{"BAS_DD": "20240514", "ISU_CD": "KR7005930003", "ISU_SRT_CD": "005930", "ISU_NM": "삼성전자", "TDD_CLSPRC": "78000", "ACC_TRDVOL": "1000000", "ACC_TRDVAL": "78000000000", "MKTCAP": "465000000000000"}]},
    "krx_ksq_bydd_trd": {"OutBlock_1": [{"BAS_DD": "20240514", "ISU_CD": "KR7123450000", "ISU_SRT_CD": "123450", "ISU_NM": "코스닥샘플", "TDD_CLSPRC": "10000", "ACC_TRDVOL": "1000", "ACC_TRDVAL": "10000000"}]},
    "krx_stk_isu_base_info": {"OutBlock_1": [{"ISU_CD": "KR7005930003", "ISU_SRT_CD": "005930", "ISU_NM": "삼성전자", "MKT_NM": "KOSPI", "LIST_DD": "19750611"}]},
    "krx_ksq_isu_base_info": {"OutBlock_1": [{"ISU_CD": "KR7123450000", "ISU_SRT_CD": "123450", "ISU_NM": "코스닥샘플", "MKT_NM": "KOSDAQ", "LIST_DD": "20200101"}]},
    "krx_kospi_dd_trd": {"OutBlock_1": [{"BAS_DD": "20240514", "IDX_NM": "KOSPI", "TDD_CLSPRC": "2700", "ACC_TRDVOL": "100000", "ACC_TRDVAL": "100000000"}]},
    "krx_kosdaq_dd_trd": {"OutBlock_1": [{"BAS_DD": "20240514", "IDX_NM": "KOSDAQ", "TDD_CLSPRC": "850", "ACC_TRDVOL": "100000", "ACC_TRDVAL": "100000000"}]},
}


__all__ = [
    "APIProbeConfig",
    "APIProbeResult",
    "APIProbeRunLog",
    "APIProbeRunner",
    "NormalizerDryRun",
    "ProbeRawResponse",
    "ProbeTarget",
]
