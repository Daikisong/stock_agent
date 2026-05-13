"""Evidence builders for pipeline-collected raw data."""

from __future__ import annotations

from datetime import datetime
from typing import Iterable

from e2r.models import (
    ConsensusRevision,
    ConsensusSnapshot,
    DisclosureEvent,
    Evidence,
    FinancialActual,
    Market,
    NewsItem,
    ResearchReport,
    SourceTier,
)


def evidence_from_financial_actual(item: FinancialActual, market: Market) -> Evidence:
    return Evidence(
        evidence_id=f"actual:{item.symbol}:{item.period_end.isoformat()}",
        source_type="financial_actual",
        source_name=item.source,
        source_tier=SourceTier.TIER_0,
        published_at=item.reported_at,
        observed_at=item.reported_at,
        available_at=item.reported_at,
        as_of_date=item.as_of_date,
        market=market,
        symbol=item.symbol,
        title=f"Reported financials {item.period_end.isoformat()}",
        parsed_fields={
            "sales": item.sales,
            "operating_profit": item.operating_profit,
            "net_income": item.net_income,
            "eps": item.eps,
            "fcf": item.fcf,
        },
        confidence=1.0,
    )


def evidence_from_consensus(item: ConsensusSnapshot, market: Market) -> Evidence:
    timestamp = datetime(item.date.year, item.date.month, item.date.day, 8, 0)
    return Evidence(
        evidence_id=f"consensus:{item.symbol}:{item.date.isoformat()}:{item.fiscal_year}",
        source_type="consensus",
        source_name=item.source,
        source_tier=SourceTier.TIER_3,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=item.as_of_date,
        market=market,
        symbol=item.symbol,
        title=f"Consensus FY{item.fiscal_year}",
        parsed_fields={
            "sales_e": item.sales_e,
            "op_e": item.op_e,
            "eps_e": item.eps_e,
            "fcf_e": item.fcf_e,
            "target_price": item.target_price,
        },
        confidence=0.7,
    )


def evidence_from_consensus_revision(item: ConsensusRevision, market: Market) -> Evidence:
    timestamp = datetime(item.date.year, item.date.month, item.date.day, 8, 0)
    return Evidence(
        evidence_id=f"revision:{item.symbol}:{item.date.isoformat()}:{item.fiscal_year}",
        source_type="consensus_revision",
        source_name="ConsensusRevision",
        source_tier=SourceTier.TIER_3,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=item.as_of_date,
        market=market,
        symbol=item.symbol,
        title=f"Consensus revision FY{item.fiscal_year}",
        parsed_fields={
            "eps_revision_1m": item.eps_revision_1m,
            "op_revision_1m": item.op_revision_1m,
            "fcf_revision_1m": item.fcf_revision_1m,
            "target_price_revision_1m": item.target_price_revision_1m,
            "street_high_eps_revision_1m": item.street_high_eps_revision_1m,
            "street_low_eps_revision_1m": item.street_low_eps_revision_1m,
        },
        confidence=0.7,
    )


def evidence_from_disclosure(item: DisclosureEvent, market: Market) -> Evidence:
    return Evidence(
        evidence_id=f"disclosure:{item.symbol}:{item.published_at.date().isoformat()}:{item.report_type}",
        source_type="disclosure",
        source_name=item.source,
        source_tier=SourceTier.TIER_0,
        published_at=item.published_at,
        observed_at=item.observed_at,
        available_at=item.available_at,
        as_of_date=item.as_of_date,
        market=market,
        symbol=item.symbol,
        title=item.title,
        url_or_identifier=item.rcept_no,
        excerpt_or_value=item.raw_text[:240] if item.raw_text else None,
        parsed_fields=item.parsed_fields,
        confidence=float(item.parsed_fields.get("parser_confidence", 0.8)),
    )


def evidence_from_research_report(item: ResearchReport, market: Market) -> Evidence:
    timestamp = datetime(item.publish_date.year, item.publish_date.month, item.publish_date.day, 8, 0)
    return Evidence(
        evidence_id=f"research:{item.symbol}:{item.publish_date.isoformat()}:{item.broker}",
        source_type="research_report",
        source_name=item.broker,
        source_tier=SourceTier.TIER_1,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=item.as_of_date,
        market=market,
        symbol=item.symbol,
        title=item.title,
        excerpt_or_value=item.raw_text[:240] if item.raw_text else None,
        parsed_fields=item.parsed_fields,
        confidence=float(item.parsed_fields.get("parser_confidence", 0.8)),
    )


def evidence_from_news_item(item: NewsItem, market: Market, fallback_symbol: str) -> Evidence:
    symbol = item.symbol or fallback_symbol
    return Evidence(
        evidence_id=f"news:{symbol}:{item.published_at.date().isoformat()}:{item.source}",
        source_type="news",
        source_name=item.source,
        source_tier=item.source_tier,
        published_at=item.published_at,
        observed_at=item.published_at,
        available_at=item.published_at,
        as_of_date=item.as_of_date,
        market=market,
        symbol=symbol,
        title=item.title,
        excerpt_or_value=item.body[:240] if item.body else None,
        parsed_fields=item.parsed_fields,
        confidence=float(item.parsed_fields.get("confidence", 0.7)),
    )


def evidence_from_feature_domains(
    *,
    market: Market,
    fallback_symbol: str,
    financial_actuals: Iterable[FinancialActual] = (),
    consensus: Iterable[ConsensusSnapshot] = (),
    consensus_revisions: Iterable[ConsensusRevision] = (),
    disclosures: Iterable[DisclosureEvent] = (),
    research_reports: Iterable[ResearchReport] = (),
    news_items: Iterable[NewsItem] = (),
) -> tuple[Evidence, ...]:
    evidence: list[Evidence] = []
    evidence.extend(evidence_from_financial_actual(item, market) for item in financial_actuals)
    evidence.extend(evidence_from_consensus(item, market) for item in consensus)
    evidence.extend(evidence_from_consensus_revision(item, market) for item in consensus_revisions)
    evidence.extend(evidence_from_disclosure(item, market) for item in disclosures)
    evidence.extend(evidence_from_research_report(item, market) for item in research_reports)
    evidence.extend(evidence_from_news_item(item, market, fallback_symbol) for item in news_items)

    unique: dict[str, Evidence] = {}
    for item in evidence:
        unique.setdefault(item.evidence_id, item)
    return tuple(unique.values())
