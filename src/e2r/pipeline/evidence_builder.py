"""Evidence builders for pipeline-collected raw data."""

from __future__ import annotations

from datetime import date, datetime
from typing import Iterable

from e2r.agentic import claim_backed_parsed_fields
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
from e2r.evidence_ids import stable_consensus_evidence_id, stable_news_evidence_id, stable_revision_evidence_id
from e2r.estimate_quality import consensus_source_quality


def _estimate_source_tier_and_confidence(source: str, parsed_fields) -> tuple[SourceTier, float]:
    quality = consensus_source_quality(source, parsed_fields)
    if quality >= 90:
        return SourceTier.TIER_2, 0.85
    if quality >= 75:
        return SourceTier.TIER_2, 0.75
    if quality >= 60:
        return SourceTier.TIER_3, 0.65
    if quality >= 35:
        return SourceTier.TIER_4, 0.45
    return SourceTier.TIER_5, 0.25


def evidence_from_financial_actual(item: FinancialActual, market: Market) -> Evidence:
    evidence_id = f"actual:{item.symbol}:{item.period_end.isoformat()}"
    parsed_fields = {
        "sales": item.sales,
        "operating_profit": item.operating_profit,
        "net_income": item.net_income,
        "eps": item.eps,
        "bps": item.bps,
        "equity": item.equity,
        "cashflow_from_operations": item.cashflow_from_operations,
        "capex": item.capex,
        "fcf": item.fcf,
    }
    return Evidence(
        evidence_id=evidence_id,
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
        parsed_fields=_claim_backed_fields(
            evidence_id=evidence_id,
            symbol=item.symbol,
            as_of_date=item.as_of_date,
            parsed_fields=parsed_fields,
            subject=item.symbol,
            quote_text=f"Reported financials {item.period_end.isoformat()}",
            source_tier=SourceTier.TIER_0,
            confidence=1.0,
        ),
        confidence=1.0,
    )


def evidence_from_consensus(item: ConsensusSnapshot, market: Market) -> Evidence:
    timestamp = datetime(item.date.year, item.date.month, item.date.day, 8, 0)
    evidence_id = stable_consensus_evidence_id(
        symbol=item.symbol,
        estimate_date=item.date,
        fiscal_year=item.fiscal_year,
        source=item.source,
    )
    source_tier, confidence = _estimate_source_tier_and_confidence(item.source, item.parsed_fields)
    parsed_fields = {
        **item.parsed_fields,
        "legacy_evidence_id": f"consensus:{item.symbol}:{item.date.isoformat()}:{item.fiscal_year}",
        "sales_e": item.sales_e,
        "op_e": item.op_e,
        "eps_e": item.eps_e,
        "fcf_e": item.fcf_e,
        "target_price": item.target_price,
    }
    return Evidence(
        evidence_id=evidence_id,
        source_type="consensus",
        source_name=item.source,
        source_tier=source_tier,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=item.as_of_date,
        market=market,
        symbol=item.symbol,
        title=f"Consensus FY{item.fiscal_year}",
        parsed_fields=_claim_backed_fields(
            evidence_id=evidence_id,
            symbol=item.symbol,
            as_of_date=item.as_of_date,
            parsed_fields=parsed_fields,
            subject=item.symbol,
            quote_text=f"Consensus FY{item.fiscal_year}",
            source_tier=source_tier,
            confidence=confidence,
        ),
        confidence=confidence,
    )


def evidence_from_consensus_revision(item: ConsensusRevision, market: Market) -> Evidence:
    timestamp = datetime(item.date.year, item.date.month, item.date.day, 8, 0)
    evidence_id = stable_revision_evidence_id(
        symbol=item.symbol,
        estimate_date=item.date,
        fiscal_year=item.fiscal_year,
        source=item.source,
    )
    source_tier, confidence = _estimate_source_tier_and_confidence(item.source, item.parsed_fields)
    parsed_fields = {
        **item.parsed_fields,
        "legacy_evidence_id": f"revision:{item.symbol}:{item.date.isoformat()}:{item.fiscal_year}",
        "eps_revision_1m": item.eps_revision_1m,
        "op_revision_1m": item.op_revision_1m,
        "fcf_revision_1m": item.fcf_revision_1m,
        "target_price_revision_1m": item.target_price_revision_1m,
        "street_high_eps_revision_1m": item.street_high_eps_revision_1m,
        "street_low_eps_revision_1m": item.street_low_eps_revision_1m,
    }
    return Evidence(
        evidence_id=evidence_id,
        source_type="consensus_revision",
        source_name=item.source,
        source_tier=source_tier,
        published_at=timestamp,
        observed_at=timestamp,
        available_at=timestamp,
        as_of_date=item.as_of_date,
        market=market,
        symbol=item.symbol,
        title=f"Consensus revision FY{item.fiscal_year}",
        parsed_fields=_claim_backed_fields(
            evidence_id=evidence_id,
            symbol=item.symbol,
            as_of_date=item.as_of_date,
            parsed_fields=parsed_fields,
            subject=item.symbol,
            quote_text=f"Consensus revision FY{item.fiscal_year}",
            source_tier=source_tier,
            confidence=confidence,
        ),
        confidence=confidence,
    )


def evidence_from_disclosure(item: DisclosureEvent, market: Market) -> Evidence:
    evidence_id = f"disclosure:{item.symbol}:{item.published_at.date().isoformat()}:{item.report_type}"
    confidence = float(item.parsed_fields.get("parser_confidence", 0.8))
    return Evidence(
        evidence_id=evidence_id,
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
        parsed_fields=_claim_backed_fields(
            evidence_id=evidence_id,
            symbol=item.symbol,
            as_of_date=item.as_of_date,
            parsed_fields=item.parsed_fields,
            subject=item.symbol,
            quote_text=item.raw_text[:1_000] if item.raw_text else item.title,
            source_url=item.rcept_no,
            source_tier=SourceTier.TIER_0,
            confidence=confidence,
        ),
        confidence=confidence,
    )


def evidence_from_research_report(item: ResearchReport, market: Market) -> Evidence:
    timestamp = datetime(item.publish_date.year, item.publish_date.month, item.publish_date.day, 8, 0)
    evidence_id = f"research:{item.symbol}:{item.publish_date.isoformat()}:{item.broker}"
    confidence = float(item.parsed_fields.get("parser_confidence", 0.8))
    return Evidence(
        evidence_id=evidence_id,
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
        parsed_fields=_claim_backed_fields(
            evidence_id=evidence_id,
            symbol=item.symbol,
            as_of_date=item.as_of_date,
            parsed_fields=item.parsed_fields,
            subject=item.symbol,
            quote_text=item.raw_text[:1_000] if item.raw_text else item.title,
            source_tier=SourceTier.TIER_1,
            confidence=confidence,
        ),
        confidence=confidence,
    )


def evidence_from_news_item(item: NewsItem, market: Market, fallback_symbol: str) -> Evidence:
    symbol = item.symbol or fallback_symbol
    source_url = str(item.parsed_fields.get("source_url") or item.parsed_fields.get("url") or "").strip() or None
    evidence_id = str(item.parsed_fields.get("evidence_id") or "").strip() or stable_news_evidence_id(
        symbol=symbol,
        published_date=item.published_at.date(),
        source=item.source,
        source_url=source_url,
        title=item.title,
    )
    confidence = float(item.parsed_fields.get("confidence", 0.7))
    return Evidence(
        evidence_id=evidence_id,
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
        url_or_identifier=source_url,
        excerpt_or_value=item.body[:240] if item.body else None,
        parsed_fields=_claim_backed_fields(
            evidence_id=evidence_id,
            symbol=symbol,
            as_of_date=item.as_of_date,
            parsed_fields=item.parsed_fields,
            subject=symbol,
            quote_text=item.body[:1_000] if item.body else item.title,
            source_url=source_url,
            source_tier=item.source_tier,
            confidence=confidence,
        ),
        confidence=confidence,
    )


def _claim_backed_fields(
    *,
    evidence_id: str,
    symbol: str,
    as_of_date: date,
    parsed_fields,
    subject: str,
    quote_text: str,
    source_tier: SourceTier,
    confidence: float,
    source_url: str | None = None,
):
    return claim_backed_parsed_fields(
        evidence_id=evidence_id,
        symbol=symbol,
        as_of_date=as_of_date,
        parsed_fields=parsed_fields,
        subject=subject,
        quote_text=quote_text,
        source_url=source_url,
        source_tier=int(source_tier),
        confidence=confidence,
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
