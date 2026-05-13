"""KIND market-risk status connector."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping

from e2r.models import Evidence, Instrument, Market, RedTeamFinding, SourceTier
from e2r.sources.source_errors import (
    SourceRequest,
    bool_value,
    date_value,
    datetime_value,
    float_or_none,
    load_fixture_records,
    market_value,
    parsed_fields_from_record,
    source_tier_value,
    text_or_none,
)


KIND_BASE_URL = "https://kind.krx.co.kr"

KIND_RISK_FIELDS: tuple[str, ...] = (
    "managed_issue",
    "investment_warning",
    "trading_halt",
    "unfaithful_disclosure",
    "delisting_risk",
    "investor_caution",
)


@dataclass(frozen=True)
class KINDRiskRecord:
    """Normalized KIND risk/status row."""

    symbol: str
    company_name: str
    as_of_date: date
    market: Market = Market.KR
    managed_issue: bool = False
    investment_warning: bool = False
    trading_halt: bool = False
    unfaithful_disclosure: bool = False
    delisting_risk: bool = False
    investor_caution: bool = False
    title: str = "KIND risk status"
    source: str = "KIND"
    published_at: Any = None
    parsed_fields: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class KINDConnector:
    """Fixture-first KIND connector for listing and market caution flags."""

    fixture_root: str | Path | None = "data/raw/kind"
    fixture_mode: bool = True
    base_url: str = KIND_BASE_URL

    def build_status_request(self, market: Market, as_of_date: date) -> SourceRequest:
        return SourceRequest(
            method="GET",
            url=f"{self.base_url}/corpgeneral/corpList.do",
            params={"method": "loadInitPage", "marketType": market.value, "date": as_of_date.isoformat()},
            fixture_mode=self.fixture_mode,
        )

    def get_risk_records(self, symbol: str | None = None, as_of_date: date | None = None) -> tuple[KINDRiskRecord, ...]:
        records = tuple(self.normalize_risk_record(row) for row in load_fixture_records(self.fixture_root, "risk_flags"))
        if symbol is not None:
            records = tuple(record for record in records if record.symbol == symbol)
        if as_of_date is not None:
            records = tuple(record for record in records if record.as_of_date <= as_of_date)
        return tuple(sorted(records, key=lambda item: (item.symbol, item.as_of_date)))

    def list_instruments(self, market: Market, as_of_date: date) -> tuple[Instrument, ...]:
        instruments: list[Instrument] = []
        for record in self.get_risk_records(as_of_date=as_of_date):
            if record.market != market:
                continue
            instruments.append(
                Instrument(
                    symbol=record.symbol,
                    name=record.company_name,
                    market=record.market,
                    exchange="KRX",
                    is_managed=record.managed_issue,
                    is_invest_warning=record.investment_warning or record.investor_caution,
                    is_trading_halt=record.trading_halt,
                )
            )
        return tuple(sorted(instruments, key=lambda item: item.symbol))

    @staticmethod
    def normalize_risk_record(row: Mapping[str, Any]) -> KINDRiskRecord:
        known = {
            "symbol",
            "company_name",
            "name",
            "market",
            "as_of_date",
            "title",
            "source",
            "published_at",
            "parsed_fields",
            *KIND_RISK_FIELDS,
        }
        parsed = parsed_fields_from_record(row, known)
        for field in KIND_RISK_FIELDS:
            if row.get(field) not in (None, ""):
                parsed[field] = bool_value(row.get(field))
        as_of = date_value(row.get("as_of_date") or row.get("published_at") or date.today())
        return KINDRiskRecord(
            symbol=str(row["symbol"]),
            company_name=str(row.get("company_name") or row.get("name") or row["symbol"]),
            market=market_value(row.get("market")),
            as_of_date=as_of,
            managed_issue=bool_value(row.get("managed_issue")),
            investment_warning=bool_value(row.get("investment_warning")),
            trading_halt=bool_value(row.get("trading_halt")),
            unfaithful_disclosure=bool_value(row.get("unfaithful_disclosure")),
            delisting_risk=bool_value(row.get("delisting_risk")),
            investor_caution=bool_value(row.get("investor_caution")),
            title=str(row.get("title") or "KIND risk status"),
            source=str(row.get("source") or "KIND"),
            published_at=datetime_value(row.get("published_at") or as_of),
            parsed_fields=parsed,
        )

    @staticmethod
    def to_evidence(record: KINDRiskRecord) -> Evidence:
        published = datetime_value(record.published_at or record.as_of_date)
        parsed = dict(record.parsed_fields or {})
        return Evidence(
            evidence_id=f"kind:{record.symbol}:{record.as_of_date.isoformat()}",
            source_type="exchange_risk",
            source_name=record.source,
            source_tier=source_tier_value(parsed.get("source_tier"), SourceTier.TIER_0),
            published_at=published,
            observed_at=published,
            available_at=published,
            as_of_date=record.as_of_date,
            market=record.market,
            symbol=record.symbol,
            title=record.title,
            parsed_fields=parsed,
            confidence=float_or_none(parsed.get("confidence")) or 1.0,
        )

    @staticmethod
    def to_red_team_finding(record: KINDRiskRecord) -> RedTeamFinding | None:
        flags = {
            "trading_halt": record.trading_halt,
            "unfaithful_disclosure": record.unfaithful_disclosure,
            "delisting_risk": record.delisting_risk,
            "managed_issue": record.managed_issue,
            "investment_warning": record.investment_warning or record.investor_caution,
        }
        active = [key for key, enabled in flags.items() if enabled]
        if not active:
            return None
        severity_by_key = {
            "delisting_risk": 95.0,
            "trading_halt": 80.0,
            "unfaithful_disclosure": 70.0,
            "managed_issue": 65.0,
            "investment_warning": 45.0,
        }
        top = max(active, key=lambda key: severity_by_key[key])
        return RedTeamFinding(
            symbol=record.symbol,
            as_of_date=record.as_of_date,
            risk_type=top,
            severity=severity_by_key[top],
            is_hard_break=top in {"delisting_risk", "trading_halt", "unfaithful_disclosure"},
            description=f"KIND status flag: {top}",
            evidence_ids=(f"kind:{record.symbol}:{record.as_of_date.isoformat()}",),
        )

    def get_evidence(self, symbol: str, as_of_date: date) -> tuple[Evidence, ...]:
        return tuple(self.to_evidence(record) for record in self.get_risk_records(symbol, as_of_date))

    def get_red_team_candidates(self, symbol: str, as_of_date: date) -> tuple[RedTeamFinding, ...]:
        findings = [self.to_red_team_finding(record) for record in self.get_risk_records(symbol, as_of_date)]
        return tuple(finding for finding in findings if finding is not None)
