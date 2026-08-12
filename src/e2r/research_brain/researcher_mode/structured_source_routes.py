"""Adapters that donate existing structured connectors to Researcher Mode.

No adapter performs live scraping by itself.  Network/cache policy remains in
the existing connector or loader supplied by the caller; these adapters only
normalize typed rows and preserve route-attempt lineage.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
import hashlib
import json
from typing import Any, Callable, Mapping, Protocol, Sequence

from e2r.models import (
    ConsensusRevision,
    ConsensusSnapshot,
    FinancialActual,
    PriceBar,
    ResearchReport,
)
from e2r.sources.company_guide import CompanyGuideConnector
from e2r.sources.opendart import OpenDARTConnector

from .structured_data_researcher import StructuredMetricRecord
from .structured_financial_engine import (
    ForwardGuidanceObservation,
    PeerValuationObservation,
    SegmentFinancialObservation,
    StructuredSourcePayload,
)


class FinancialActualConnector(Protocol):
    def get_financial_actuals(
        self, symbol: str, as_of_date: date
    ) -> tuple[FinancialActual, ...]:
        ...


class ConsensusHistoryConnector(Protocol):
    def get_consensus(
        self, symbol: str, as_of_date: date
    ) -> tuple[ConsensusSnapshot, ...]:
        ...

    def get_consensus_revisions(
        self, symbol: str, as_of_date: date
    ) -> tuple[ConsensusRevision, ...]:
        ...


class PriceHistoryConnector(Protocol):
    def get_price_bars(
        self,
        symbol: str,
        start: date,
        end: date,
        as_of_date: date,
    ) -> tuple[PriceBar, ...]:
        ...


@dataclass(frozen=True)
class InMemoryStructuredSourceRoute:
    """Deterministic route for checkpoints, fixtures, and upstream collectors."""

    route_name: str
    payload: StructuredSourcePayload
    provider_error: str | None = None

    def __post_init__(self) -> None:
        if self.payload.route_name != self.route_name:
            raise ValueError("in-memory payload route mismatch")

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del target_id, symbol, company_name, as_of_date
        if self.provider_error:
            raise RuntimeError(self.provider_error)
        return self.payload


@dataclass(frozen=True)
class UnavailableStructuredSourceRoute:
    route_name: str
    reason: str = "structured_provider_not_configured"

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del target_id, symbol, company_name, as_of_date
        raise RuntimeError(self.reason)


@dataclass(frozen=True)
class OpenDARTActualsStructuredRoute:
    connector: FinancialActualConnector
    single_account_payloads: tuple[Mapping[str, Any], ...] = ()
    route_name: str = field(
        default="DART_ACTUALS_DETERMINISTIC_SCENARIO", init=False
    )

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del company_name
        actuals = list(self.connector.get_financial_actuals(symbol, as_of_date))
        balance_records: list[StructuredMetricRecord] = []
        raw_source_ids: list[str] = []
        for row in self.single_account_payloads:
            payload = row.get("payload")
            if not isinstance(payload, Mapping):
                continue
            reported_at = _date_value(row.get("reported_at") or as_of_date)
            if reported_at > as_of_date:
                continue
            raw_source_id = _content_source_id(self.route_name, payload)
            raw_source_ids.append(raw_source_id)
            actuals.extend(
                OpenDARTConnector.normalize_single_account_actuals(
                    payload,
                    symbol=symbol,
                    fiscal_year=int(row["fiscal_year"]),
                    as_of_date=as_of_date,
                    reported_at=reported_at,
                    fiscal_quarter=(
                        int(row["fiscal_quarter"])
                        if row.get("fiscal_quarter") not in (None, "")
                        else None
                    ),
                    period_end=(
                        _date_value(row["period_end"])
                        if row.get("period_end")
                        else None
                    ),
                )
            )
            balance_records.extend(
                _opendart_balance_sheet_records(
                    payload=payload,
                    target_id=target_id,
                    as_of_date=as_of_date,
                    fiscal_year=int(row["fiscal_year"]),
                    fiscal_quarter=(
                        int(row["fiscal_quarter"])
                        if row.get("fiscal_quarter") not in (None, "")
                        else None
                    ),
                    reported_at=reported_at,
                    source_id=raw_source_id,
                    source_route=self.route_name,
                )
            )
        by_period = {
            (
                int(row["fiscal_year"]),
                (
                    int(row["fiscal_quarter"])
                    if row.get("fiscal_quarter") not in (None, "")
                    else None
                ),
            ): row
            for row in self.single_account_payloads
            if isinstance(row.get("payload"), Mapping)
        }
        for (fiscal_year, quarter), annual_row in tuple(by_period.items()):
            if quarter is not None:
                continue
            q3_row = by_period.get((fiscal_year, 3))
            if q3_row is None:
                continue
            reported_at = _date_value(annual_row.get("reported_at") or as_of_date)
            if reported_at > as_of_date:
                continue
            actuals.extend(
                OpenDARTConnector.normalize_derived_q4_actuals(
                    annual_row["payload"],
                    q3_row["payload"],
                    symbol=symbol,
                    fiscal_year=fiscal_year,
                    as_of_date=as_of_date,
                    reported_at=reported_at,
                )
            )
        compiled = tuple(
            sorted(
                {
                    (
                        item.fiscal_year,
                        item.fiscal_quarter,
                        item.period_end,
                        item.reported_at,
                        item.source,
                    ): item
                    for item in actuals
                    if item.symbol == symbol
                    and item.reported_at.date() <= as_of_date
                    and item.as_of_date <= as_of_date
                }.values(),
                key=lambda item: (item.period_end, item.reported_at, item.source),
            )
        )
        connector_source_ids = (
            _source_id(
                    self.route_name,
                    symbol,
                    as_of_date.isoformat(),
                    tuple(
                        (
                            item.fiscal_year,
                            item.fiscal_quarter,
                            item.period_end.isoformat(),
                            item.source,
                        )
                        for item in compiled
                    ),
                )
            if compiled
            else None
        )
        source_ids = tuple(
            dict.fromkeys(
                (
                    *((connector_source_ids,) if connector_source_ids else ()),
                    *raw_source_ids,
                    *(
                        source_id
                        for record in balance_records
                        for source_id in record.source_ids
                    ),
                )
            )
        )
        return StructuredSourcePayload(
            route_name=self.route_name,
            source_ids=source_ids,
            financial_actuals=compiled,
            structured_records=tuple(balance_records),
            diagnostics={
                "connector_class": type(self.connector).__name__,
                "single_account_payload_count": len(self.single_account_payloads),
                "direct_fcf_parser_required": False,
            },
        )


@dataclass(frozen=True)
class ConsensusConnectorStructuredRoute:
    connector: ConsensusHistoryConnector
    route_name: str = "CONSENSUS_CSV"

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del target_id, company_name
        snapshots = tuple(self.connector.get_consensus(symbol, as_of_date))
        revisions = tuple(self.connector.get_consensus_revisions(symbol, as_of_date))
        source_ids = (
            (
                _source_id(
                    self.route_name,
                    symbol,
                    as_of_date.isoformat(),
                    tuple((row.date.isoformat(), row.fiscal_year, row.source) for row in snapshots),
                    tuple((row.date.isoformat(), row.fiscal_year, row.source) for row in revisions),
                ),
            )
            if snapshots or revisions
            else ()
        )
        return StructuredSourcePayload(
            route_name=self.route_name,
            source_ids=source_ids,
            consensus_snapshots=snapshots,
            consensus_revisions=revisions,
            diagnostics={"connector_class": type(self.connector).__name__},
        )


@dataclass(frozen=True)
class KRXPriceMarketCapStructuredRoute:
    connector: PriceHistoryConnector
    benchmark_symbols: tuple[str, ...] = ()
    lookback_days: int = 1_825
    route_name: str = field(default="KRX_PRICE_MARKET_CAP", init=False)

    def __post_init__(self) -> None:
        if self.lookback_days <= 0:
            raise ValueError("structured price lookback must be positive")

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del target_id, company_name
        start = as_of_date - timedelta(days=self.lookback_days)
        symbols = tuple(dict.fromkeys((symbol, *self.benchmark_symbols)))
        bars = tuple(
            sorted(
                (
                    bar
                    for item_symbol in symbols
                    for bar in self.connector.get_price_bars(
                        item_symbol, start, as_of_date, as_of_date
                    )
                    if bar.date <= as_of_date and bar.as_of_date <= as_of_date
                ),
                key=lambda row: (row.symbol, row.date),
            )
        )
        source_ids = (
            (
                _source_id(
                    self.route_name,
                    symbols,
                    start.isoformat(),
                    as_of_date.isoformat(),
                    len(bars),
                ),
            )
            if bars
            else ()
        )
        return StructuredSourcePayload(
            route_name=self.route_name,
            source_ids=source_ids,
            price_bars=bars,
            diagnostics={
                "connector_class": type(self.connector).__name__,
                "requested_symbols": list(symbols),
                "lookback_days": self.lookback_days,
            },
        )


@dataclass(frozen=True)
class CompanyGuideStructuredRoute:
    snapshot_loader: Callable[[str, date], str | None] | None = None
    recent_reports_loader: Callable[[str, date], str | Mapping[str, Any] | None] | None = None
    connector: CompanyGuideConnector = field(
        default_factory=lambda: CompanyGuideConnector(fixture_mode=True)
    )
    route_name: str = field(default="COMPANYGUIDE", init=False)

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del target_id, company_name
        snapshots: list[ConsensusSnapshot] = []
        revisions: list[ConsensusRevision] = []
        reports: list[ResearchReport] = []
        source_ids: list[str] = []
        errors: list[str] = []
        if self.snapshot_loader is not None:
            html_text = self.snapshot_loader(symbol, as_of_date)
            if html_text:
                source_ids.append(_content_source_id(self.route_name, html_text))
                try:
                    parsed = self.connector.parse_consensus_snapshot_html(
                        html_text, symbol=symbol, as_of_date=as_of_date
                    )
                    snapshots.append(parsed.consensus)
                    revisions.extend(
                        _target_price_revisions(
                            parsed.broker_targets,
                            symbol=symbol,
                            as_of_date=as_of_date,
                        )
                    )
                except (TypeError, ValueError) as exc:
                    errors.append(f"snapshot_parse:{type(exc).__name__}:{exc}")
                    try:
                        targets = self.connector.parse_broker_targets_html(
                            html_text, symbol=symbol, as_of_date=as_of_date
                        )
                        revisions.extend(
                            _target_price_revisions(
                                targets, symbol=symbol, as_of_date=as_of_date
                            )
                        )
                    except (TypeError, ValueError) as target_exc:
                        errors.append(
                            f"target_parse:{type(target_exc).__name__}:{target_exc}"
                        )
        if self.recent_reports_loader is not None:
            payload = self.recent_reports_loader(symbol, as_of_date)
            if payload not in (None, "", {}):
                source_ids.append(_content_source_id(self.route_name, payload))
                try:
                    reports.extend(
                        self.connector.parse_recent_reports_payload(
                            payload, symbol=symbol, as_of_date=as_of_date
                        )
                    )
                except (TypeError, ValueError, json.JSONDecodeError) as exc:
                    errors.append(f"reports_parse:{type(exc).__name__}:{exc}")
        if not (snapshots or revisions or reports) and errors:
            raise ValueError(";".join(errors))
        return StructuredSourcePayload(
            route_name=self.route_name,
            source_ids=tuple(dict.fromkeys(source_ids)) if snapshots or revisions or reports else (),
            consensus_snapshots=tuple(snapshots),
            consensus_revisions=tuple(revisions),
            research_reports=tuple(reports),
            diagnostics={"parse_errors": errors},
        )


@dataclass(frozen=True)
class PublicBrokerReportStructuredRoute:
    reports: tuple[ResearchReport, ...]
    source_ids: tuple[str, ...]
    route_name: str = field(default="PUBLIC_BROKER_REPORT", init=False)

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del target_id, company_name
        rows = tuple(
            report
            for report in self.reports
            if report.symbol == symbol and report.publish_date <= as_of_date
        )
        return StructuredSourcePayload(
            route_name=self.route_name,
            source_ids=self.source_ids if rows else (),
            research_reports=rows,
        )


@dataclass(frozen=True)
class IssuerGuidanceStructuredRoute:
    records: tuple[StructuredMetricRecord, ...] = ()
    source_ids: tuple[str, ...] = ()
    segment_observations: tuple[SegmentFinancialObservation, ...] = ()
    guidance_observations: tuple[ForwardGuidanceObservation, ...] = ()
    route_name: str = field(default="ISSUER_GUIDANCE", init=False)

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del symbol, company_name
        rows = tuple(
            row
            for row in self.records
            if row.target_id == target_id
            and row.as_of_date == as_of_date.isoformat()
            and row.source_route == self.route_name
        )
        segment_rows = tuple(
            row
            for row in self.segment_observations
            if row.target_id == target_id
            and row.as_of_date == as_of_date.isoformat()
            and row.source_route == self.route_name
        )
        guidance_rows = tuple(
            row
            for row in self.guidance_observations
            if row.target_id == target_id
            and row.as_of_date == as_of_date.isoformat()
            and row.source_route == self.route_name
        )
        has_rows = bool(rows or segment_rows or guidance_rows)
        return StructuredSourcePayload(
            route_name=self.route_name,
            source_ids=self.source_ids if has_rows else (),
            structured_records=rows,
            segment_observations=segment_rows,
            guidance_observations=guidance_rows,
        )


@dataclass(frozen=True)
class PeerStructuredValuationRoute:
    observations: tuple[PeerValuationObservation, ...]
    source_ids: tuple[str, ...]
    route_name: str = "PEER_STRUCTURED"

    def fetch(
        self,
        *,
        target_id: str,
        symbol: str,
        company_name: str,
        as_of_date: date,
    ) -> StructuredSourcePayload:
        del target_id, symbol, company_name
        rows = tuple(
            row
            for row in self.observations
            if row.as_of_date == as_of_date.isoformat()
            and row.source_route == self.route_name
        )
        return StructuredSourcePayload(
            route_name=self.route_name,
            source_ids=self.source_ids if rows else (),
            peer_valuations=rows,
        )


def build_structured_source_routes(
    *,
    opendart_connector: FinancialActualConnector | None = None,
    krx_connector: PriceHistoryConnector | None = None,
    consensus_connector: ConsensusHistoryConnector | None = None,
    companyguide_route: CompanyGuideStructuredRoute | None = None,
    broker_route: PublicBrokerReportStructuredRoute | None = None,
    issuer_route: IssuerGuidanceStructuredRoute | None = None,
    benchmark_symbols: Sequence[str] = (),
) -> tuple[Any, ...]:
    """Build all canonical fallbacks, preserving unavailable routes as failures."""

    routes: list[Any] = [
        companyguide_route
        or UnavailableStructuredSourceRoute("COMPANYGUIDE"),
        broker_route
        or UnavailableStructuredSourceRoute("PUBLIC_BROKER_REPORT"),
        issuer_route or UnavailableStructuredSourceRoute("ISSUER_GUIDANCE"),
        (
            OpenDARTActualsStructuredRoute(opendart_connector)
            if opendart_connector is not None
            else UnavailableStructuredSourceRoute(
                "DART_ACTUALS_DETERMINISTIC_SCENARIO"
            )
        ),
        (
            KRXPriceMarketCapStructuredRoute(
                krx_connector, benchmark_symbols=tuple(benchmark_symbols)
            )
            if krx_connector is not None
            else UnavailableStructuredSourceRoute("KRX_PRICE_MARKET_CAP")
        ),
    ]
    if consensus_connector is not None:
        routes.append(ConsensusConnectorStructuredRoute(consensus_connector))
    return tuple(routes)


def _opendart_balance_sheet_records(
    *,
    payload: Mapping[str, Any],
    target_id: str,
    as_of_date: date,
    fiscal_year: int,
    fiscal_quarter: int | None,
    reported_at: date,
    source_id: str,
    source_route: str,
) -> tuple[StructuredMetricRecord, ...]:
    rows = payload.get("list") or payload.get("items") or payload.get("data") or ()
    if not isinstance(rows, (list, tuple)):
        return ()
    cash_candidates: dict[int, tuple[float, str]] = {}
    aggregate_debt: dict[int, tuple[float, str]] = {}
    debt_leaves: dict[int, dict[str, float]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        statement = str(row.get("sj_div") or row.get("statement") or "")
        if statement and statement != "BS":
            continue
        account_name = str(
            row.get("account_nm") or row.get("account_name") or ""
        ).replace(" ", "")
        amount = _dart_amount(
            row.get("thstrm_amount")
            if row.get("thstrm_amount") not in (None, "")
            else row.get("amount")
        )
        if not account_name or amount is None:
            continue
        priority = _dart_row_priority(row)
        if account_name in {
            "현금및현금성자산",
            "현금및현금성자산등",
            "현금성자산",
            "CashAndCashEquivalents",
        }:
            if amount < 0:
                continue
            current = cash_candidates.get(priority)
            if current is None or abs(amount) > abs(current[0]):
                cash_candidates[priority] = (amount, account_name)
            continue
        if account_name in {
            "총차입금",
            "차입금및사채",
            "차입금및사채총계",
            "이자발생부채",
            "이자부부채",
        }:
            current = aggregate_debt.get(priority)
            if current is None or abs(amount) > abs(current[0]):
                aggregate_debt[priority] = (abs(amount), account_name)
            continue
        if _is_debt_leaf(account_name):
            key = str(row.get("account_id") or account_name)
            debt_leaves.setdefault(priority, {})[key] = abs(amount)
    values: list[tuple[str, float, str, Mapping[str, Any]]] = []
    if cash_candidates:
        priority = max(cash_candidates)
        amount, account_name = cash_candidates[priority]
        values.append(
            (
                "cash_and_equivalents",
                amount,
                "BALANCE_SHEET_CASH",
                {"account_names": [account_name], "dart_priority": priority},
            )
        )
    if aggregate_debt:
        priority = max(aggregate_debt)
        amount, account_name = aggregate_debt[priority]
        values.append(
            (
                "total_debt",
                amount,
                "BALANCE_SHEET_DEBT",
                {
                    "account_names": [account_name],
                    "dart_priority": priority,
                    "debt_method": "reported_aggregate",
                },
            )
        )
    elif debt_leaves:
        priority = max(debt_leaves)
        leaves = debt_leaves[priority]
        values.append(
            (
                "total_debt",
                sum(leaves.values()),
                "BALANCE_SHEET_DEBT",
                {
                    "account_names": sorted(leaves),
                    "dart_priority": priority,
                    "debt_method": "sum_distinct_interest_bearing_leaf_accounts",
                },
            )
        )
    output = []
    period = (
        f"FY{fiscal_year}Q{fiscal_quarter}"
        if fiscal_quarter is not None
        else f"FY{fiscal_year}"
    )
    for metric_id, value, role, metadata in values:
        output.append(
            StructuredMetricRecord(
                record_id=_source_id(
                    "STRUCTURED-DART-BALANCE",
                    target_id,
                    fiscal_year,
                    fiscal_quarter,
                    metric_id,
                    value,
                    source_id,
                ),
                target_id=target_id,
                as_of_date=as_of_date.isoformat(),
                metric_id=metric_id,
                value=value,
                unit="KRW",
                period=period,
                evidence_roles=(role,),
                source_ids=(source_id,),
                source_route=source_route,
                observed_at=reported_at.isoformat(),
                available_at=reported_at.isoformat(),
                record_kind="FINANCIAL_BALANCE_SHEET",
                confidence=0.98,
                dataset="FINANCIAL",
                provenance="STRUCTURED_EXTRACTED",
                metadata={
                    **dict(metadata),
                    "structured_source": True,
                    "source_family": "OpenDART_single_account_all",
                    "fiscal_quarter": fiscal_quarter,
                },
            )
        )
    return tuple(output)


def _is_debt_leaf(account_name: str) -> bool:
    exact = {
        "단기차입금",
        "장기차입금",
        "유동성장기차입금",
        "유동성장기부채",
        "유동사채",
        "사채",
        "전환사채",
        "신주인수권부사채",
        "리스부채",
        "유동리스부채",
        "비유동리스부채",
    }
    return account_name in exact


def _dart_row_priority(row: Mapping[str, Any]) -> int:
    priority = 0
    if str(row.get("fs_div") or "") == "CFS" or "연결" in str(
        row.get("fs_nm") or ""
    ):
        priority += 10
    if str(row.get("sj_div") or "") == "BS":
        priority += 1
    return priority


def _dart_amount(value: Any) -> float | None:
    text = str(value or "").strip().replace(",", "")
    if not text or text in {"-", "nan", "NaN"}:
        return None
    negative = text.startswith("(") and text.endswith(")")
    if negative:
        text = text[1:-1]
    try:
        parsed = float(text)
    except ValueError:
        return None
    return -parsed if negative else parsed


def _target_price_revisions(
    rows: Sequence[Any], *, symbol: str, as_of_date: date
) -> tuple[ConsensusRevision, ...]:
    usable = [
        row
        for row in rows
        if row.symbol == symbol
        and row.date <= as_of_date
        and (as_of_date - row.date).days <= 31
        and row.target_price_revision_pct is not None
    ]
    if not usable:
        return ()
    values = [float(row.target_price_revision_pct) for row in usable]
    return (
        ConsensusRevision(
            symbol=symbol,
            date=max(row.date for row in usable),
            fiscal_year=as_of_date.year,
            as_of_date=as_of_date,
            target_price_revision_1m=round(sum(values) / len(values), 6),
            analyst_count_change=len(values),
            source="company_guide_snapshot",
            parsed_fields={
                "structured_consensus_revision_source": True,
                "revision_family": "TARGET_PRICE",
                "target_price_only": True,
                "earnings_revision": False,
                "broker_target_revision_count": len(values),
            },
        ),
    )


def _date_value(value: Any) -> date:
    if type(value) is date:
        return value
    return date.fromisoformat(str(value)[:10])


def _source_id(prefix: str, *parts: Any) -> str:
    payload = json.dumps(parts, ensure_ascii=False, sort_keys=True, default=str)
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]
    return f"SRC-{prefix}-{digest}"


def _content_source_id(prefix: str, payload: Any) -> str:
    if isinstance(payload, str):
        text = payload
    else:
        text = json.dumps(payload, ensure_ascii=False, sort_keys=True, default=str)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]
    return f"SRC-{prefix}-{digest}"


__all__ = [
    "CompanyGuideStructuredRoute",
    "ConsensusConnectorStructuredRoute",
    "FinancialActualConnector",
    "InMemoryStructuredSourceRoute",
    "IssuerGuidanceStructuredRoute",
    "KRXPriceMarketCapStructuredRoute",
    "OpenDARTActualsStructuredRoute",
    "PeerStructuredValuationRoute",
    "PriceHistoryConnector",
    "PublicBrokerReportStructuredRoute",
    "UnavailableStructuredSourceRoute",
    "build_structured_source_routes",
]
