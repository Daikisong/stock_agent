"""SEC EDGAR connector for US filings and companyfacts fixtures."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.evidence_ids import stable_news_evidence_id
from e2r.models import DisclosureEvent, Evidence, FinancialActual, Market, NewsItem, SourceTier
from e2r.sources.source_errors import (
    SourceRequest,
    date_value,
    datetime_value,
    float_or_none,
    load_fixture_records,
    parsed_fields_from_record,
    require_credential,
    text_or_none,
)


SEC_SUBMISSIONS_BASE_URL = "https://data.sec.gov/submissions"
SEC_COMPANYFACTS_BASE_URL = "https://data.sec.gov/api/xbrl/companyfacts"


@dataclass(frozen=True)
class SECEdgarConnector:
    """SEC EDGAR fixture connector and live request builder."""

    user_agent: str | None = None
    fixture_root: str | Path | None = "data/raw/sec_edgar"
    fixture_mode: bool = True

    def build_submissions_request(self, cik: str) -> SourceRequest:
        cik_text = _normalize_cik(cik)
        return SourceRequest(
            method="GET",
            url=f"{SEC_SUBMISSIONS_BASE_URL}/CIK{cik_text}.json",
            headers={"User-Agent": self.user_agent} if self.user_agent else {},
            fixture_mode=self.fixture_mode,
            credential_name="SEC_USER_AGENT",
        )

    def build_companyfacts_request(self, cik: str) -> SourceRequest:
        cik_text = _normalize_cik(cik)
        return SourceRequest(
            method="GET",
            url=f"{SEC_COMPANYFACTS_BASE_URL}/CIK{cik_text}.json",
            headers={"User-Agent": self.user_agent} if self.user_agent else {},
            fixture_mode=self.fixture_mode,
            credential_name="SEC_USER_AGENT",
        )

    def require_live_credentials(self) -> str:
        return require_credential(self.user_agent, "SEC_USER_AGENT")

    def get_financial_actuals(self, symbol: str, as_of_date: date) -> tuple[FinancialActual, ...]:
        actuals: list[FinancialActual] = []
        for row in load_fixture_records(self.fixture_root, "financial_actuals"):
            if str(row.get("symbol")) == symbol:
                actuals.append(self.normalize_financial_actual(row))
        for payload in load_fixture_records(self.fixture_root, "companyfacts"):
            if str(payload.get("symbol") or payload.get("ticker") or "") == symbol:
                actuals.extend(self.normalize_companyfacts_payload(symbol, payload, as_of_date))
        return tuple(
            sorted(
                (
                    item
                    for item in actuals
                    if item.symbol == symbol
                    and item.reported_at.date() <= as_of_date
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: (item.period_end, item.reported_at),
            )
        )

    def get_disclosures(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[DisclosureEvent, ...]:
        disclosures = tuple(self.normalize_disclosure(row) for row in load_fixture_records(self.fixture_root, "disclosures"))
        return tuple(
            sorted(
                (
                    item
                    for item in disclosures
                    if item.symbol == symbol
                    and start <= item.published_at.date() <= end
                    and item.available_at.date() <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )

    def get_news(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[NewsItem, ...]:
        items = tuple(self.normalize_filing_news(row) for row in load_fixture_records(self.fixture_root, "filings"))
        return tuple(
            sorted(
                (
                    item
                    for item in items
                    if item.symbol == symbol
                    and start <= item.published_at.date() <= end
                    and item.published_at.date() <= as_of_date
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )

    @staticmethod
    def normalize_financial_actual(row: Mapping[str, Any]) -> FinancialActual:
        cfo = float_or_none(row.get("cashflow_from_operations") or row.get("cfo"))
        capex = float_or_none(row.get("capex"))
        fcf = float_or_none(row.get("fcf"))
        if fcf is None and cfo is not None and capex is not None:
            fcf = cfo - abs(capex)
        return FinancialActual(
            symbol=str(row["symbol"]),
            fiscal_year=int(float(row["fiscal_year"])),
            fiscal_quarter=_quarter_value(row.get("fiscal_quarter") or row.get("fp")),
            period_end=date_value(row["period_end"]),
            reported_at=datetime_value(row["reported_at"]),
            as_of_date=date_value(row.get("as_of_date") or row["reported_at"]),
            source=str(row.get("source") or "SEC EDGAR"),
            sales=float_or_none(row.get("sales") or row.get("revenue")),
            operating_profit=float_or_none(row.get("operating_profit") or row.get("operating_income")),
            net_income=float_or_none(row.get("net_income")),
            eps=float_or_none(row.get("eps") or row.get("eps_diluted")),
            equity=float_or_none(row.get("equity") or row.get("stockholders_equity") or row.get("total_equity")),
            cashflow_from_operations=cfo,
            capex=capex,
            fcf=fcf,
            receivables=float_or_none(row.get("receivables")),
            inventory=float_or_none(row.get("inventory")),
        )

    @classmethod
    def normalize_companyfacts_payload(
        cls,
        symbol: str,
        payload: Mapping[str, Any],
        as_of_date: date,
    ) -> tuple[FinancialActual, ...]:
        facts = payload.get("facts")
        if not isinstance(facts, Mapping):
            return ()
        concepts = facts.get("us-gaap", {})
        if not isinstance(concepts, Mapping):
            return ()
        rows_by_period: dict[tuple[int, int | None, date], dict[str, Any]] = {}
        field_map = {
            "sales": ("Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"),
            "operating_profit": ("OperatingIncomeLoss",),
            "net_income": ("NetIncomeLoss", "ProfitLoss"),
            "eps": ("EarningsPerShareDiluted",),
            "cashflow_from_operations": ("NetCashProvidedByUsedInOperatingActivities",),
            "capex": ("PaymentsToAcquirePropertyPlantAndEquipment",),
            "equity": ("StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"),
            "inventory": ("InventoryNet",),
            "receivables": ("AccountsReceivableNetCurrent",),
        }
        reported_by_period: dict[tuple[int, int | None, date], datetime] = {}
        for output_key, concept_names in field_map.items():
            for fact in _concept_facts(concepts, concept_names):
                filed = date_value(fact.get("filed"))
                if filed > as_of_date:
                    continue
                fiscal_year = int(fact.get("fy"))
                fiscal_quarter = _quarter_value(fact.get("fp"))
                period_end = date_value(fact.get("end"))
                key = (fiscal_year, fiscal_quarter, period_end)
                value = float_or_none(fact.get("val"))
                if value is None:
                    continue
                if output_key == "capex":
                    value = abs(value)
                rows_by_period.setdefault(key, {})[output_key] = value
                reported = datetime(filed.year, filed.month, filed.day, 16, 0)
                reported_by_period[key] = max(reported_by_period.get(key, reported), reported)
        actuals: list[FinancialActual] = []
        for (fiscal_year, fiscal_quarter, period_end), values in rows_by_period.items():
            cfo = values.get("cashflow_from_operations")
            capex = values.get("capex")
            fcf = cfo - capex if cfo is not None and capex is not None else None
            actuals.append(
                FinancialActual(
                    symbol=symbol,
                    fiscal_year=fiscal_year,
                    fiscal_quarter=fiscal_quarter,
                    period_end=period_end,
                    reported_at=reported_by_period[(fiscal_year, fiscal_quarter, period_end)],
                    as_of_date=reported_by_period[(fiscal_year, fiscal_quarter, period_end)].date(),
                    source="SEC EDGAR companyfacts",
                    sales=values.get("sales"),
                    operating_profit=values.get("operating_profit"),
                    net_income=values.get("net_income"),
                    eps=values.get("eps"),
                    equity=values.get("equity"),
                    cashflow_from_operations=cfo,
                    capex=capex,
                    fcf=fcf,
                    receivables=values.get("receivables"),
                    inventory=values.get("inventory"),
                )
            )
        return tuple(actuals)

    @staticmethod
    def normalize_disclosure(row: Mapping[str, Any]) -> DisclosureEvent:
        known = {
            "symbol",
            "source",
            "report_type",
            "form",
            "title",
            "published_at",
            "filed",
            "observed_at",
            "available_at",
            "as_of_date",
            "accession_no",
            "rcept_no",
            "raw_text",
            "parsed_fields",
        }
        published = datetime_value(row.get("published_at") or row.get("filed"))
        raw_text = text_or_none(row.get("raw_text"))
        parsed = parsed_fields_from_record(row, known)
        if raw_text:
            parsed.update(_sec_keyword_fields(raw_text))
        return DisclosureEvent(
            symbol=str(row["symbol"]),
            source=str(row.get("source") or "SEC EDGAR"),
            report_type=str(row.get("report_type") or row.get("form") or "SEC filing"),
            title=str(row.get("title") or row.get("form") or "SEC filing"),
            published_at=published,
            observed_at=datetime_value(row.get("observed_at") or published),
            available_at=datetime_value(row.get("available_at") or published),
            as_of_date=date_value(row.get("as_of_date") or published.date()),
            rcept_no=text_or_none(row.get("accession_no") or row.get("rcept_no")),
            raw_text=raw_text,
            parsed_fields=parsed,
        )

    @staticmethod
    def normalize_filing_news(row: Mapping[str, Any]) -> NewsItem:
        published = datetime_value(row.get("published_at") or row.get("filed"))
        raw_text = text_or_none(row.get("raw_text") or row.get("body"))
        fields = parsed_fields_from_record(row, {"symbol", "source", "title", "published_at", "filed", "body", "raw_text", "as_of_date", "parsed_fields"})
        if raw_text:
            fields.update(_sec_keyword_fields(raw_text))
        title = str(row.get("title") or row.get("form") or "SEC filing")
        source = str(row.get("source") or "SEC EDGAR")
        source_url = text_or_none(row.get("source_url") or row.get("url"))
        fields.setdefault("source_url", source_url)
        fields.setdefault(
            "evidence_id",
            stable_news_evidence_id(
                symbol=str(row["symbol"]),
                published_date=published.date(),
                source=source,
                source_url=source_url,
                title=title,
                prefix="sec-news",
            ),
        )
        return NewsItem(
            symbol=str(row["symbol"]),
            sector=text_or_none(row.get("sector")),
            published_at=published,
            source=source,
            title=title,
            as_of_date=date_value(row.get("as_of_date") or published.date()),
            body=raw_text,
            source_tier=SourceTier.TIER_0,
            parsed_fields=fields,
        )

    @staticmethod
    def to_evidence(event: DisclosureEvent | NewsItem, market: Market = Market.US) -> Evidence:
        if isinstance(event, DisclosureEvent):
            return Evidence(
                evidence_id=f"sec:{event.symbol}:{event.rcept_no or event.published_at.date().isoformat()}",
                source_type="sec_filing",
                source_name=event.source,
                source_tier=SourceTier.TIER_0,
                published_at=event.published_at,
                observed_at=event.observed_at,
                available_at=event.available_at,
                as_of_date=event.as_of_date,
                market=market,
                symbol=event.symbol,
                title=event.title,
                url_or_identifier=event.rcept_no,
                excerpt_or_value=event.raw_text[:240] if event.raw_text else None,
                parsed_fields=event.parsed_fields,
                confidence=0.8,
            )
        source_url = str(event.parsed_fields.get("source_url") or event.parsed_fields.get("url") or "").strip() or None
        evidence_id = str(event.parsed_fields.get("evidence_id") or "").strip() or stable_news_evidence_id(
            symbol=event.symbol or "UNKNOWN",
            published_date=event.published_at.date(),
            source=event.source,
            source_url=source_url,
            title=event.title,
            prefix="sec-news",
        )
        return Evidence(
            evidence_id=evidence_id,
            source_type="sec_filing_news",
            source_name=event.source,
            source_tier=event.source_tier,
            published_at=event.published_at,
            observed_at=event.published_at,
            available_at=event.published_at,
            as_of_date=event.as_of_date,
            market=market,
            symbol=event.symbol or "UNKNOWN",
            title=event.title,
            url_or_identifier=source_url,
            excerpt_or_value=event.body[:240] if event.body else None,
            parsed_fields=event.parsed_fields,
            confidence=0.8,
        )


def _normalize_cik(cik: str) -> str:
    return str(cik).strip().lstrip("0").zfill(10)


def _quarter_value(value: Any) -> int | None:
    if value in (None, "", "FY"):
        return None
    text = str(value).strip().upper()
    if text.startswith("Q") and text[1:].isdigit():
        return int(text[1:])
    if text.isdigit():
        quarter = int(text)
        return quarter if quarter in (1, 2, 3, 4) else None
    return None


def _concept_facts(concepts: Mapping[str, Any], names: Sequence[str]) -> tuple[Mapping[str, Any], ...]:
    facts: list[Mapping[str, Any]] = []
    for name in names:
        concept = concepts.get(name)
        if not isinstance(concept, Mapping):
            continue
        units = concept.get("units", {})
        if not isinstance(units, Mapping):
            continue
        for unit_rows in units.values():
            if isinstance(unit_rows, list):
                facts.extend(row for row in unit_rows if isinstance(row, Mapping) and row.get("fy") and row.get("end") and row.get("filed"))
    return tuple(facts)


def _sec_keyword_fields(text: str) -> dict[str, Any]:
    lowered = text.lower()
    fields: dict[str, Any] = {}
    if "remaining performance obligation" in lowered or "rpo" in lowered:
        fields["rpo_mentioned"] = True
    if "deferred revenue" in lowered:
        fields["deferred_revenue_mentioned"] = True
    if "backlog" in lowered:
        fields["backlog_mentioned"] = True
    if "inventory" in lowered and ("increase" in lowered or "higher" in lowered):
        fields["receivables_inventory_spike"] = True
    if "material weakness" in lowered or "accounting" in lowered:
        fields["accounting_or_trust_issue"] = True
    return fields
