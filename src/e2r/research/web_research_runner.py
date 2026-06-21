"""Fixture-first web research runner for E2R manual workflow replication."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, replace
from datetime import date, datetime
from typing import Any, Mapping, Sequence

from e2r.evidence_ids import stable_news_evidence_id
from e2r.models import DisclosureEvent, Evidence, Market, NewsItem, RedTeamFinding, ResearchReport, SourceTier
from e2r.pipeline.evidence_builder import evidence_from_feature_domains
from e2r.research.financial_text_fields import extract_reported_financial_fields, latest_reported_period_end
from e2r.research.one_off_context import has_one_off_shortage_context
from e2r.research.page_fetcher import FetchResult, PageFetcher
from e2r.research.pdf_text_extractor import PDFTextExtractor
from e2r.research.query_planner import QueryPlan, QueryPlanner, QuerySpec
from e2r.research.report_parser import parse_research_report_text
from e2r.research.search_snippet_evidence import news_item_from_search_snippet
from e2r.research.search_provider import EmptySearchProvider, SearchProvider, SearchResult
from e2r.research.search_result_ranker import RankedSearchResult, SearchResultRanker
from e2r.sources.naver_news import NaverNewsConnector, parse_news_event
from e2r.sources.opendart import OpenDARTConnector


_REPORT_NUMERIC_NO_OVERWRITE_FIELDS = {
    "target_revision_pct",
    "target_price_revision_pct",
    "target_price",
    "fy1_eps",
    "fy1_op",
    "fy1_sales",
    "fy2_eps",
    "fy2_op",
    "fy2_sales",
    "fy3_eps",
    "fy3_op",
    "fy3_sales",
    "est_per",
    "est_pbr",
}

_EXPLICIT_SOURCE_BACKED_FIELD_RE = re.compile(
    r"^\s*E2R_SOURCE_BACKED_FIELD\s+([A-Za-z][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$"
)
_EXPLICIT_FIELD_PREFIX_EXCLUDES = (
    "claim_",
    "compiled_",
    "raw_",
    "source_",
)


@dataclass(frozen=True)
class WebResearchInput:
    """One company web research request."""

    company_name: str
    symbol: str
    sector: str | None
    market: Market
    as_of_date: date
    stage_context: str | None = None
    company_aliases: tuple[str, ...] = field(default_factory=tuple)
    max_results_per_query: int = 100
    top_results: int | None = None


@dataclass(frozen=True)
class DroppedSearchResult:
    """Search result excluded from fetching or parsing."""

    result: SearchResult
    reason: str


@dataclass(frozen=True)
class WebResearchResult:
    """Output of one fixture-first web research run."""

    company_name: str
    symbol: str
    market: Market
    as_of_date: date
    query_plan: QueryPlan
    queries_run: tuple[str, ...]
    search_results: tuple[SearchResult, ...]
    ranked_results: tuple[RankedSearchResult, ...]
    selected_results: tuple[RankedSearchResult, ...]
    fetched_documents: tuple[FetchResult, ...]
    parsed_reports: tuple[ResearchReport, ...]
    parsed_news: tuple[NewsItem, ...]
    parsed_disclosures: tuple[DisclosureEvent, ...] = field(default_factory=tuple)
    evidence: tuple[Evidence, ...] = field(default_factory=tuple)
    red_team_findings: tuple[RedTeamFinding, ...] = field(default_factory=tuple)
    dropped_results: tuple[DroppedSearchResult, ...] = field(default_factory=tuple)


class WebResearchRunner:
    """Search, rank, fetch, parse, and emit E2R evidence for one company."""

    def __init__(
        self,
        *,
        query_planner: QueryPlanner | None = None,
        search_provider: SearchProvider | None = None,
        ranker: SearchResultRanker | None = None,
        page_fetcher: PageFetcher | None = None,
        pdf_text_extractor: PDFTextExtractor | None = None,
    ) -> None:
        self._planner = query_planner or QueryPlanner()
        self._provider = search_provider or EmptySearchProvider()
        self._ranker = ranker or SearchResultRanker()
        self._fetcher = page_fetcher or PageFetcher()
        self._pdf_extractor = pdf_text_extractor or PDFTextExtractor()

    def run(self, inputs: WebResearchInput) -> WebResearchResult:
        plan = self._planner.plan(
            company_name=inputs.company_name,
            symbol=inputs.symbol,
            sector=inputs.sector,
            market=inputs.market,
            as_of_date=inputs.as_of_date,
            stage_context=inputs.stage_context,
        )
        query_specs = plan.queries
        results = self._search(query_specs, inputs.as_of_date, inputs.max_results_per_query)
        ranked = self._ranker.rank(results, company_name=inputs.company_name, as_of_date=inputs.as_of_date)
        selected, dropped = self._select_results(ranked, inputs.top_results)

        fetched: list[FetchResult] = []
        parsed_reports: list[ResearchReport] = []
        parsed_news: list[NewsItem] = []
        parsed_disclosures: list[DisclosureEvent] = []
        findings: list[RedTeamFinding] = []

        for ranked_result in selected:
            result = ranked_result.result
            fetch = self._fetch(result, inputs.as_of_date)
            fetched.append(fetch)
            if not fetch.ok or not fetch.text:
                snippet_news = news_item_from_search_snippet(
                    result,
                    company_name=inputs.company_name,
                    symbol=inputs.symbol,
                    sector=inputs.sector,
                    market=inputs.market,
                    as_of_date=inputs.as_of_date,
                    company_aliases=inputs.company_aliases,
                )
                if snippet_news is not None:
                    parsed_news.append(snippet_news)
                    finding = NaverNewsConnector.to_red_team_finding(snippet_news)
                    if finding is not None:
                        findings.append(finding)
                    dropped.append(DroppedSearchResult(result=result, reason="fetch_unavailable_snippet_evidence_used"))
                    continue
                dropped.append(DroppedSearchResult(result=result, reason=fetch.reason or "fetch_unavailable"))
                continue
            if not _is_fetched_document_company_relevant(
                result=result,
                fetch_text=fetch.text,
                company_name=inputs.company_name,
                symbol=inputs.symbol,
                company_aliases=inputs.company_aliases,
            ):
                dropped.append(DroppedSearchResult(result=result, reason="company_not_found_in_fetched_document"))
                continue
            kind = classify_search_result(result)
            parse_text = fetch.text
            result_context = f"{result.title}\n{result.snippet or ''}\n{result.url}".lower()
            if kind == "disclosure" and _is_market_list_context(result_context):
                parse_text = _company_relevant_fetched_text(
                    result=result,
                    fetch_text=fetch.text,
                    company_name=inputs.company_name,
                    symbol=inputs.symbol,
                    company_aliases=inputs.company_aliases,
                )
                if not _has_target_company_disclosure_context(
                    text=parse_text,
                    company_name=inputs.company_name,
                    symbol=inputs.symbol,
                    company_aliases=inputs.company_aliases,
                ):
                    kind = "news"
            elif kind != "disclosure" and not _should_keep_full_report_text(
                result=result,
                company_name=inputs.company_name,
                symbol=inputs.symbol,
                company_aliases=inputs.company_aliases,
            ) and not _has_explicit_source_backed_field_block(fetch.text):
                parse_text = _company_relevant_fetched_text(
                    result=result,
                    fetch_text=fetch.text,
                    company_name=inputs.company_name,
                    symbol=inputs.symbol,
                    company_aliases=inputs.company_aliases,
            )
            if kind == "report":
                parsed = self._parse_report(inputs, result, parse_text)
                stale_reason = _stale_research_report_reason(
                    report=parsed,
                    result=result,
                    text=parse_text,
                    as_of_date=inputs.as_of_date,
                )
                if stale_reason is not None:
                    dropped.append(DroppedSearchResult(result=result, reason=stale_reason))
                    continue
                parsed_reports.append(parsed)
            elif kind == "disclosure":
                parsed_disclosures.append(self._parse_disclosure(inputs, result, parse_text))
            elif kind == "news":
                news = self._parse_news(inputs, result, parse_text)
                parsed_news.append(news)
                finding = NaverNewsConnector.to_red_team_finding(news)
                if finding is not None:
                    findings.append(finding)
            else:
                news = self._parse_news(inputs, result, parse_text)
                parsed_fields = dict(news.parsed_fields)
                parsed_fields.setdefault("document_type", "generic_fetched_web_text")
                parsed_fields.setdefault("document_type_inferred_from_fetched_text", True)
                news = replace(news, parsed_fields=parsed_fields)
                parsed_news.append(news)
                finding = NaverNewsConnector.to_red_team_finding(news)
                if finding is not None:
                    findings.append(finding)

        evidence = evidence_from_feature_domains(
            market=inputs.market,
            fallback_symbol=inputs.symbol,
            disclosures=parsed_disclosures,
            research_reports=parsed_reports,
            news_items=parsed_news,
        )
        parsed_disclosures = list(_claim_backed_disclosures(parsed_disclosures, evidence))
        parsed_reports = list(_claim_backed_reports(parsed_reports, evidence))
        parsed_news = list(_claim_backed_news(parsed_news, evidence, fallback_symbol=inputs.symbol))
        return WebResearchResult(
            company_name=inputs.company_name,
            symbol=inputs.symbol,
            market=inputs.market,
            as_of_date=inputs.as_of_date,
            query_plan=plan,
            queries_run=tuple(item.query for item in query_specs),
            search_results=results,
            ranked_results=ranked,
            selected_results=tuple(selected),
            fetched_documents=tuple(fetched),
            parsed_reports=tuple(parsed_reports),
            parsed_news=tuple(parsed_news),
            parsed_disclosures=tuple(parsed_disclosures),
            evidence=evidence,
            red_team_findings=tuple(findings),
            dropped_results=tuple(dropped),
        )

    def _search(
        self,
        query_specs: Sequence[QuerySpec],
        as_of_date: date,
        max_results: int,
    ) -> tuple[SearchResult, ...]:
        results: list[SearchResult] = []
        for query_spec in query_specs:
            for result in self._provider.search(query_spec.query, as_of_date, max_results=max_results):
                if result.published_at is not None and result.published_at.date() > as_of_date:
                    continue
                results.append(result)
        return tuple(results)

    @staticmethod
    def _select_results(
        ranked: Sequence[RankedSearchResult],
        top_results: int | None,
    ) -> tuple[list[RankedSearchResult], list[DroppedSearchResult]]:
        selected: list[RankedSearchResult] = []
        dropped: list[DroppedSearchResult] = []
        eligible: list[RankedSearchResult] = []
        for item in ranked:
            if "duplicate_url" in item.negative_reasons:
                dropped.append(DroppedSearchResult(result=item.result, reason="duplicate_url"))
                continue
            if "future_result" in item.negative_reasons:
                dropped.append(DroppedSearchResult(result=item.result, reason="future_result"))
                continue
            if item.score <= 0:
                dropped.append(DroppedSearchResult(result=item.result, reason="low_rank_score"))
                continue
            eligible.append(item)
        selected_ids: set[str] = set()
        covered_queries: set[str] = set()
        for item in eligible:
            if top_results is not None and len(selected) >= top_results:
                break
            query = (item.result.query or "").strip()
            if query and query in covered_queries:
                continue
            selected.append(item)
            selected_ids.add(item.result.url)
            if query:
                covered_queries.add(query)
        for item in eligible:
            if top_results is not None and len(selected) >= top_results:
                break
            if item.result.url in selected_ids:
                continue
            selected.append(item)
            selected_ids.add(item.result.url)
        for item in eligible:
            if item.result.url not in selected_ids:
                dropped.append(DroppedSearchResult(result=item.result, reason="not_selected"))
        return selected, dropped

    def _fetch(self, result: SearchResult, as_of_date: date) -> FetchResult:
        fetch = self._fetcher.fetch(result.url, as_of_date=as_of_date)
        if fetch.ok or not result.is_pdf:
            return fetch
        extraction = self._pdf_extractor.extract_text(result.url)
        if extraction.ok and extraction.text:
            fetched_at = datetime(as_of_date.year, as_of_date.month, as_of_date.day, 8, 0)
            return FetchResult(
                url=result.url,
                ok=True,
                text=extraction.text,
                content_type="text/plain",
                fetched_at=fetched_at,
                reason=None,
            )
        return fetch

    @staticmethod
    def _parse_report(inputs: WebResearchInput, result: SearchResult, text: str) -> ResearchReport:
        published = result.published_at.date() if result.published_at else inputs.as_of_date
        parse_context = "\n".join(part for part in (result.title, result.snippet or "", text) if part.strip())
        parsed = parse_research_report_text(
            symbol=inputs.symbol,
            market=inputs.market,
            text=text,
            metadata={
                "title": result.title,
                "snippet": result.snippet,
                "broker": result.source,
                "publish_date": published,
                "as_of_date": inputs.as_of_date,
                "url": result.url,
                "market": inputs.market.value,
            },
        )
        merged_fields = dict(parsed.report.parsed_fields)
        extracted_fields = extract_e2r_text_fields(parse_context, as_of_date=inputs.as_of_date)
        for key, value in extracted_fields.items():
            if value in (None, ""):
                continue
            if key in _REPORT_NUMERIC_NO_OVERWRITE_FIELDS and key in merged_fields:
                continue
            merged_fields[key] = value
        _clear_mitigated_risk_fields(merged_fields)
        merged_fields.setdefault("source_url", result.url)
        merged_fields.setdefault("parser_confidence", parsed.parsed_fields.get("parser_confidence", 0.65))
        _apply_result_date_fields(merged_fields, result)
        return replace(parsed.report, parsed_fields=merged_fields, raw_text=text)

    @staticmethod
    def _parse_disclosure(inputs: WebResearchInput, result: SearchResult, text: str) -> DisclosureEvent:
        published = result.published_at or datetime(inputs.as_of_date.year, inputs.as_of_date.month, inputs.as_of_date.day, 8, 0)
        parsed_fields = extract_e2r_text_fields(text, as_of_date=inputs.as_of_date)
        _apply_result_date_fields(parsed_fields, result)
        # OpenDART-style date ranges are more reliable than generic number
        # extraction for contract duration.
        parsed_fields.pop("contract_duration_months", None)
        row: dict[str, Any] = {
            "symbol": inputs.symbol,
            "source": result.source or "web-disclosure",
            "report_type": _disclosure_type(result.title, text),
            "title": result.title,
            "published_at": published,
            "observed_at": published,
            "available_at": published,
            "as_of_date": inputs.as_of_date,
            "raw_text": text,
            "rcept_no": result.url,
            "parsed_fields": parsed_fields,
        }
        return OpenDARTConnector.normalize_disclosure(row)

    @staticmethod
    def _parse_news(inputs: WebResearchInput, result: SearchResult, text: str) -> NewsItem:
        published = result.published_at or datetime(inputs.as_of_date.year, inputs.as_of_date.month, inputs.as_of_date.day, 8, 0)
        parsed_fields = parse_news_event(title=result.title, body=text)
        parsed_fields.update(extract_e2r_text_fields(f"{result.title}\n{text}", as_of_date=inputs.as_of_date))
        parsed_fields.setdefault("source_url", result.url)
        parsed_fields.setdefault("source_query", result.query)
        parsed_fields.setdefault("date_verified", _result_date_verified(result))
        parsed_fields.setdefault("search_snippet_only", False)
        parsed_fields.setdefault("search_snippet_date_unverified", False)
        parsed_fields.setdefault("green_allowed_by_date", _result_green_allowed_by_date(result))
        _apply_result_date_fields(parsed_fields, result)
        parsed_fields.setdefault(
            "evidence_id",
            stable_news_evidence_id(
                symbol=inputs.symbol,
                published_date=published.date(),
                source=result.source or "web-news",
                source_url=result.url,
                title=result.title,
            ),
        )
        parsed_fields.setdefault("confidence", min(1.0, 0.45 + len(parsed_fields) * 0.04))
        row = {
            "symbol": inputs.symbol,
            "sector": inputs.sector,
            "published_at": published,
            "source": result.source or "web-news",
            "title": result.title,
            "as_of_date": inputs.as_of_date,
            "body": text,
            "source_tier": int(SourceTier.TIER_2),
            "parsed_fields": parsed_fields,
            "market": inputs.market.value,
        }
        news = NaverNewsConnector.normalize_news_item(row)
        merged = dict(news.parsed_fields)
        merged.update(parsed_fields)
        return replace(news, parsed_fields=merged)


def _result_date_verified(result: SearchResult) -> bool:
    return True if result.date_verified is None else bool(result.date_verified)


def _result_green_allowed_by_date(result: SearchResult) -> bool:
    return True if result.green_allowed_by_date is None else bool(result.green_allowed_by_date)


def _apply_result_date_fields(parsed_fields: dict[str, Any], result: SearchResult) -> None:
    date_verified = _result_date_verified(result)
    green_allowed = _result_green_allowed_by_date(result)
    parsed_fields.setdefault("date_verified", date_verified)
    parsed_fields.setdefault("green_allowed_by_date", green_allowed)
    if not date_verified:
        parsed_fields.setdefault("date_unverified_document", True)
    if not green_allowed:
        parsed_fields.setdefault("date_verification_green_block", True)


def _clear_mitigated_risk_fields(parsed_fields: dict[str, Any]) -> None:
    repair_bridge = all(
        bool(parsed_fields.get(key))
        for key in ("pf_exposure_reduced", "balance_sheet_repair", "cash_collection_visible")
    )
    funding_risk_monitored = bool(parsed_fields.get("funding_cost_risk_monitored"))
    if not repair_bridge and not funding_risk_monitored:
        return
    parsed_fields["guard_risk_mitigated"] = True
    if funding_risk_monitored or repair_bridge:
        parsed_fields.pop("funding_cost_risk", None)
    if repair_bridge:
        parsed_fields.pop("liquidity_or_microcap_risk", None)


def _claim_backed_reports(
    reports: Sequence[ResearchReport],
    evidence: Sequence[Evidence],
) -> tuple[ResearchReport, ...]:
    evidence_by_id = {item.evidence_id: item for item in evidence}
    updated: list[ResearchReport] = []
    for report in reports:
        evidence_id = f"research:{report.symbol}:{report.publish_date.isoformat()}:{report.broker}"
        linked = evidence_by_id.get(evidence_id)
        updated.append(replace(report, parsed_fields=linked.parsed_fields) if linked is not None else report)
    return tuple(updated)


def _claim_backed_disclosures(
    disclosures: Sequence[DisclosureEvent],
    evidence: Sequence[Evidence],
) -> tuple[DisclosureEvent, ...]:
    evidence_by_id = {item.evidence_id: item for item in evidence}
    updated: list[DisclosureEvent] = []
    for disclosure in disclosures:
        evidence_id = f"disclosure:{disclosure.symbol}:{disclosure.published_at.date().isoformat()}:{disclosure.report_type}"
        linked = evidence_by_id.get(evidence_id)
        updated.append(replace(disclosure, parsed_fields=linked.parsed_fields) if linked is not None else disclosure)
    return tuple(updated)


def _claim_backed_news(
    news_items: Sequence[NewsItem],
    evidence: Sequence[Evidence],
    *,
    fallback_symbol: str,
) -> tuple[NewsItem, ...]:
    evidence_by_id = {item.evidence_id: item for item in evidence}
    updated: list[NewsItem] = []
    for item in news_items:
        symbol = item.symbol or fallback_symbol
        source_url = str(item.parsed_fields.get("source_url") or item.parsed_fields.get("url") or "").strip() or None
        evidence_id = str(item.parsed_fields.get("evidence_id") or "").strip() or stable_news_evidence_id(
            symbol=symbol,
            published_date=item.published_at.date(),
            source=item.source,
            source_url=source_url,
            title=item.title,
        )
        linked = evidence_by_id.get(evidence_id)
        updated.append(replace(item, parsed_fields=linked.parsed_fields) if linked is not None else item)
    return tuple(updated)


def classify_search_result(result: SearchResult) -> str:
    """Classify a result as report, disclosure, news, or unknown."""

    haystack = f"{result.title} {result.snippet or ''} {result.url}"
    if result.is_report_domain or result.is_pdf or _has_report_document_context(haystack):
        return "report"
    if _has_disclosure_document_context(haystack, result_is_disclosure=result.is_disclosure):
        return "disclosure"
    if result.is_news or any(token in haystack for token in ("뉴스", "보도", "기사", "news")):
        return "news"
    return "unknown"


def _has_report_document_context(text: str) -> bool:
    lowered = text.lower()
    return any(
        token in lowered
        for token in (
            "리포트",
            "기업분석",
            "종목분석",
            "company report",
            "company_read",
            "research/company",
            "review pdf",
            "initiating coverage",
        )
    )


def _has_disclosure_document_context(text: str, *, result_is_disclosure: bool = False) -> bool:
    lowered = text.lower()
    official_context = any(token in lowered for token in ("dart.fss", "opendart", "kind.krx", "kind.co.kr"))
    explicit_disclosure = "공시" in text or "disclosure" in lowered
    if official_context:
        return True
    if "주요공시" in text or "주요 공시" in text:
        return True
    if result_is_disclosure and explicit_disclosure:
        return True
    if explicit_disclosure and any(token in text for token in ("단일판매", "공급계약", "신규시설투자", "감사의견")):
        return True
    return False


def extract_e2r_text_fields(text: str, *, as_of_date: date | None = None) -> dict[str, Any]:
    """Extract E2R feature fields from already fetched text.

    This is intentionally conservative. Missing values stay missing; the
    parser only emits fields when explicit keywords or numbers appear.
    """

    fields: dict[str, Any] = {}
    for key, labels in (
        ("op_yoy_pct", ("영업이익 YoY", "OP YoY", "영업이익 증가율", "OP growth")),
        ("eps_yoy_pct", ("EPS YoY", "EPS 증가율")),
        ("fcf_growth_pct", ("FCF 증가율", "FCF growth")),
        ("eps_revision_pct", ("EPS 상향", "EPS 추정치 상향", "EPS revision")),
        ("op_revision_pct", ("영업이익 추정치 상향", "OP revision")),
        ("fcf_revision_pct", ("FCF 상향", "FCF revision")),
        ("fcf_quality_score", ("FCF quality score", "FCF 질 점수")),
        ("contract_duration_months", ("계약기간", "계약 기간", "duration months")),
        ("lead_time_months", ("리드타임", "lead time")),
        ("capa_utilization_pct", ("가동률", "CAPA utilization", "capacity utilization")),
        ("capa_locked_years", ("CAPA 선점", "CAPA locked", "capacity locked")),
        ("asp_yoy_pct", ("ASP YoY", "ASP 상승률", "판가 상승률")),
        ("price_increase_pct", ("가격 상승률",)),
        ("opm_expansion_pctp", ("OPM 개선폭", "마진 개선폭")),
        ("export_growth_pct", ("수출 증가율", "수출 성장률", "Export growth")),
        ("cloud_revenue_growth_pct", ("클라우드 매출 성장률", "Cloud revenue growth", "AI 매출 성장률")),
        ("op_delta_to_market_cap", ("OP 증가분/시총", "영업이익 증가분/시총")),
        ("capex_to_sales", ("CAPEX/매출", "투자/매출")),
        ("target_multiple_delta", ("멀티플 상향폭", "multiple expansion")),
        ("return_since_stage3", ("return_since_stage3", "return since Stage 3", "Stage 3 이후 수익률")),
        ("return_12_24m", ("return_12_24m", "12~24개월 수익률", "12-24m return")),
    ):
        value = _number_after(text, labels)
        if value is not None:
            fields[key] = value
    for key, value in extract_reported_financial_fields(text, as_of_date=as_of_date).items():
        fields.setdefault(key, value)

    contract_ratio = _percent_after(text, ("계약 매출액 대비", "장기계약 매출액 대비", "계약금액/매출", "매출액 대비"))
    if contract_ratio is not None:
        fields["contract_amount_to_prior_sales"] = contract_ratio / 100.0 if contract_ratio > 2 else contract_ratio
    backlog_ratio = _percent_after(text, ("수주잔고/매출", "order backlog to sales", "backlog to sales"))
    if backlog_ratio is not None:
        fields.setdefault("order_backlog_to_sales", backlog_ratio / 100.0 if backlog_ratio <= 2 else backlog_ratio)
    capa_expansion = _percent_after(text, ("CAPA 증가율", "CAPA 증설", "생산능력 증가"))
    if capa_expansion is not None:
        fields.setdefault("capa_expansion_pct", capa_expansion)
        fields.setdefault("capa_increase_pct", capa_expansion)

    lowered = text.lower()
    if "선수금" in text or "선급금" in text or "prepayment" in lowered:
        fields["prepayment_exists"] = True
        fields["customer_prepayment"] = True
    if any(token in text for token in ("고객사 확정", "확정 고객", "주요 고객", "고객사 배정", "확정 물량")) or any(
        token in lowered for token in ("confirmed customer", "named customer", "anchor customer", "customer allocation")
    ):
        fields["named_customer_quality"] = True
        fields["customer_preorder_or_allocation"] = True
    if any(token in text for token in ("브랜드 고객", "주요 고객 다변화", "고객 다변화", "앵커 고객")) or any(
        token in lowered for token in ("brand customer", "customer diversification", "anchor customer", "named customer")
    ):
        fields["brand_customer_diversification"] = True
        fields["named_customer_quality"] = True
    if any(token in text for token in ("공급계약", "납품계약", "프레임워크 계약", "마스터 공급계약")) or any(
        token in lowered
        for token in ("supply agreement", "supply contract", "customer contract", "framework agreement", "master supply agreement")
    ):
        fields["customer_contract_visible"] = True
        fields["supply_agreement_visible"] = True
    if any(token in text for token in ("최소 매출 보장", "최소매출 보장", "최소 물량 보장", "최소 구매 보장")) or any(
        token in lowered for token in ("minimum revenue guarantee", "minimum sales guarantee", "minimum purchase commitment")
    ):
        fields["minimum_revenue_guarantee"] = True
        fields["minimum_sales_guarantee"] = True
        fields["revenue_visibility_contract"] = True
    if "해지 불가" in text or "취소 불가" in text or "take-or-pay" in lowered or "take or pay" in lowered:
        fields["non_cancellable"] = True
    if any(token in text for token in ("최소 구매 보장", "최소 물량 보장", "의무 구매")) or any(
        token in lowered for token in ("take-or-pay", "take or pay", "minimum purchase commitment")
    ):
        fields["take_or_pay"] = True
        fields["customer_preorder_or_allocation"] = True
    if "사상 최대 수주잔고" in text or ("수주잔고" in text and "사상 최대" in text) or "record backlog" in lowered:
        fields["record_backlog"] = True
        fields["backlog_record_high"] = True
    if any(token in text for token in ("생산능력 배정", "생산 슬롯 확정", "생산 슬롯 예약", "물량 예약")) or any(
        token in lowered for token in ("capacity allocation", "capacity booked", "booked out", "slot reservation")
    ):
        fields["capacity_precommitted"] = True
        fields["booked_out_capacity"] = True
        fields["order_slot_locked"] = True
    if any(token in text for token in ("납기 일정", "인도 일정", "출하 일정")) or "delivery schedule" in lowered:
        fields["delivery_schedule"] = True
    if any(token in text for token in ("수주잔고 매출 전환", "수주 매출 전환", "매출 전환 경로", "출하 매출 전환")) or any(
        token in lowered for token in ("order-to-revenue", "order to revenue", "revenue recognition path", "call-off")
    ):
        fields["order_to_revenue_bridge"] = True
    if any(token in lowered for token in ("book-to-bill", "book to bill")):
        fields["book_to_bill_visible"] = True
    if any(token in text for token in ("장비 수주 회복", "장비 주문 회복", "수주 회복")) or "equipment order recovery" in lowered:
        fields["equipment_order_recovery"] = True
        fields["order_to_revenue_bridge"] = True
    if (
        "capa 부족" in lowered
        or "capa 제약" in lowered
        or "capa 병목" in lowered
        or "생산능력 부족" in text
        or "capacity constraint" in lowered
        or "capacity bottleneck" in lowered
    ):
        fields["capacity_constraint"] = True
        fields["capa_shortage"] = True
    if "리드타임 장기화" in text and ("공급부족" in text or "공급 부족" in text):
        fields["lead_time_extended"] = True
        fields["supply_shortage_mentioned"] = True
        fields["capacity_constraint"] = True
        fields["capa_shortage"] = True
    if any(token in text for token in ("ASP 상승", "판가 상승", "가격 상승", "ASP 개선", "판가 개선")):
        fields["pricing_power_confirmed"] = True
        fields["pricing_power_mentioned"] = True
        fields["asp_increase_mentioned"] = True
    if "판가 전가" in text or "가격 전가" in text or "pricing power" in lowered:
        fields["pricing_power_confirmed"] = True
        fields["pricing_power_mentioned"] = True
    if "멀티플 상향" in text or "리레이팅" in text or "rerating" in lowered:
        fields["market_frame_shift"] = True
        fields["target_multiple_rerating"] = True
    if "구조적 공급부족" in text or "structural shortage" in lowered:
        fields["shortage_type"] = "structural"
        fields["structural_shortage_mentioned"] = True
    if "공급부족" in text or "공급 부족" in text or "shortage" in lowered:
        fields["supply_shortage_mentioned"] = True
    if has_one_off_shortage_context(text):
        fields["shortage_type"] = "one_off"
        fields["one_off_shortage"] = True
        fields["pandemic_demand_spike"] = True
        fields["temporary_shortage"] = True
        fields["one_off_shortage_risk"] = max(float(fields.get("one_off_shortage_risk", 0.0)), 90.0)
    if "수주잔고 감소" in text or "backlog decline" in lowered:
        fields["backlog_or_rpo_decline"] = True
    if "수주 둔화" in text or "new orders slowdown" in lowered:
        fields["new_orders_slowdown"] = True
    if "계약 취소" in text or "계약 지연" in text or "contract cancelled" in lowered or "contract delayed" in lowered:
        fields["contract_cancelled_or_delayed"] = True
    if "opm 하락" in lowered or "영업이익률 하락" in text:
        fields["opm_decline"] = True
    if "asp 하락" in lowered or "판가 하락" in text:
        fields["asp_decline"] = True
    if "공급과잉" in text or "supply glut" in lowered:
        fields["supply_glut"] = True
    if "컨센서스 하향" in text or "revision down" in lowered:
        fields["eps_fcf_revision_down"] = True
    if "extreme forward valuation" in lowered or "극단적 밸류에이션" in text:
        fields["extreme_forward_valuation"] = True
    if "revision slowdown" in lowered or "추정치 둔화" in text:
        fields["revision_slowdown"] = True
    if "market crowding" in lowered or "과밀" in text:
        fields["market_crowding"] = True
    if "blowoff price pattern" in lowered or "급등 과열" in text:
        fields["blowoff_price_pattern"] = True
    if "회계 이슈" in text or "감사의견" in text or "accounting issue" in lowered:
        fields["accounting_or_trust_issue"] = True
        fields["risk_comment"] = _excerpt(text, ("회계 이슈", "감사의견", "accounting issue"))
    if any(token in text for token in ("주가만 상승", "가격만 상승", "테마만 부각")) or any(
        token in lowered for token in ("price-only", "price only", "theme hype")
    ):
        fields["price_only_blowoff"] = True
    if any(token in text for token in ("매출 연결 없음", "매출로 연결되지", "현금흐름 연결 없음")) or any(
        token in lowered for token in ("without revenue", "no revenue bridge", "missing cashflow bridge")
    ):
        fields["missing_cashflow_bridge"] = True
        fields["theme_hype_without_revenue"] = True
    if any(token in text for token in ("출처 불일치", "근거 상충", "자료 신뢰도 낮음")) or any(
        token in lowered for token in ("source conflict", "source quality conflict", "low source quality")
    ):
        fields["source_quality_conflict"] = True
        fields["evidence_source_quality_issue"] = True
    if any(token in text for token in ("고객 인증 지연", "퀄 지연", "인증 지연")) or any(
        token in lowered for token in ("qualification lag", "qualification delay")
    ):
        fields["qualification_lag_risk"] = True
    if any(token in text for token in ("정책 승인", "규제 승인", "인허가 확인", "정부 승인")) or any(
        token in lowered for token in ("policy confirmed", "regulatory confirmed", "regulatory approval confirmed")
    ):
        fields["policy_or_regulatory_confirmed"] = True
    if any(token in text for token in ("프로젝트 수주", "프로젝트 선정", "사업자 선정", "낙찰")) or any(
        token in lowered for token in ("project award", "project awarded", "selected bidder")
    ):
        fields["project_award_confirmed"] = True
    if any(token in text for token in ("회사 현금흐름 연결", "현금흐름 연결", "직접 매출 연결")) or any(
        token in lowered for token in ("direct company cash route", "company cash route", "direct revenue route")
    ):
        fields["direct_company_cash_route"] = True
        fields["policy_to_company_cash_route"] = True
    if any(token in text for token in ("스프레드 확대", "마진 스프레드 확대")) or "spread expansion" in lowered:
        fields["spread_expansion"] = True
        fields["margin_bridge_visible"] = True
    if any(token in text for token in ("ex-credit 마진", "세액공제 제외 마진")) or "ex-credit margin" in lowered:
        fields["ex_credit_margin"] = True
        fields["margin_bridge_visible"] = True
    if any(token in text for token in ("원재료 비용 리스크", "원재료 가격 부담")) or any(
        token in lowered for token in ("raw material cost risk", "raw material price risk")
    ):
        fields["raw_material_cost_risk"] = True
    if any(token in text for token in ("가동률 상승", "가동률 개선")) or "utilization rate" in lowered:
        fields["utilization_rate"] = True
    if "inventory cycle" in lowered or "재고 사이클" in text:
        fields["inventory_cycle"] = True
    if any(token in text for token in ("재고 급증", "재고 증가")) or "inventory spike" in lowered:
        fields["inventory_spike"] = True
        fields["receivables_inventory_spike"] = True
    if any(token in text for token in ("데이터센터 고객",)) or any(
        token in lowered for token in ("datacenter customer", "data center customer")
    ):
        fields["datacenter_customer"] = True
        fields["data_center_contract"] = True
    if "hbm customer order" in lowered or "HBM 고객 주문" in text or "HBM 고객 수주" in text:
        fields["hbm_customer_order"] = True
        fields["customer_preorder_or_allocation"] = True
    if "relative strength" in lowered or "상대강도" in text:
        fields["relative_strength_score"] = True
    if "qualification confirmed" in lowered or "고객 인증 완료" in text or "퀄 통과" in text:
        fields["qualification_confirmed"] = True
    if any(token in lowered for token in ("socket demand", "test socket demand")) or "테스트 소켓 수요" in text:
        fields["socket_or_test_demand_visible"] = True
    if "customer quality visible" in lowered or "고객 품질 확인" in text or "우량 고객" in text:
        fields["customer_quality_visible"] = True
    if "volume visibility" in lowered or "물량 가시성" in text:
        fields["volume_visibility"] = True
    if "volume growth" in lowered or "판매량 증가" in text or "출하량 증가" in text:
        fields["volume_growth_visible"] = True
    if "jv utilization" in lowered or "JV 가동률" in text or "합작공장 가동률" in text:
        fields["jv_utilization"] = True
    if "valuation overheat" in lowered or "밸류에이션 과열" in text:
        fields["valuation_overheat"] = True
    if "thesis break" in lowered or "논리 훼손 확인" in text or "투자논리 훼손" in text:
        fields["thesis_break_confirmed"] = True
    if "evidence source quality" in lowered or "증거 품질" in text or "출처 품질" in text:
        fields["evidence_source_quality"] = True
    if "restatement risk" in lowered or "재무제표 재작성" in text or "정정 리스크" in text:
        fields["restatement_risk"] = True
    if "event spread risk" in lowered or "이벤트 스프레드 리스크" in text:
        fields["event_spread_risk"] = True
    if "offtake contract" in lowered or "오프테이크 계약" in text:
        fields["offtake_contract"] = True
        fields["customer_contract_visible"] = True
    if "supply shortage" in lowered or "공급 부족" in text or "공급부족" in text:
        fields["supply_shortage"] = True
    if "policy supply support" in lowered or "정책 공급 지원" in text:
        fields["policy_supply_support"] = True
    if "permit status" in lowered or "허가 상태" in text:
        fields["permit_status"] = True
    if "subsidy capture" in lowered or "세액공제 수혜" in text or "AMPC" in text:
        fields["ampc_or_subsidy_capture"] = True
        fields["subsidy_capture_visible"] = True
    if "implementation timeline" in lowered or "이행 일정" in text or "실행 일정" in text:
        fields["implementation_timeline"] = True
    if "gross margin bridge" in lowered or "매출총이익률 브릿지" in text:
        fields["gross_margin_bridge"] = True
        fields["margin_bridge_visible"] = True
    if any(token in text for token in ("자사주 소각", "자기주식 소각")) or any(
        token in lowered for token in ("treasury share cancellation", "share cancellation")
    ):
        fields["treasury_share_cancellation"] = True
        fields["buyback_executed"] = True
        fields["capital_return_execution"] = True
    if any(token in text for token in ("자사주 매입", "자사주 취득")) or "buyback" in lowered:
        fields["buyback_announced"] = True
    if any(token in text for token in ("배당 확대", "배당성향 확대", "주주환원 확대")) or any(
        token in lowered for token in ("shareholder return", "dividend growth")
    ):
        fields["dividend_visibility"] = True
        fields["shareholder_return_execution"] = True
    if any(token in text for token in ("신용비용 안정", "NPL 안정", "부실채권 안정")) or "credit cost" in lowered:
        fields["credit_cost_quality"] = True
    if any(token in text for token in ("CSM 증가", "CSM 성장", "계약서비스마진 증가", "계약서비스마진 성장")):
        fields["csm_growth_visible"] = True
    if any(token in text for token in ("준비금 안정", "준비금 충분")) or any(
        token in lowered for token in ("reserve quality", "reserve adequacy")
    ):
        fields["reserve_quality_visible"] = True
    if any(token in text for token in ("손해율 개선", "손해율 안정")) or any(
        token in lowered for token in ("loss ratio improvement", "loss ratio stable")
    ):
        fields["loss_ratio_quality"] = True
    if any(token in text for token in ("FDA 승인", "품목허가", "허가 승인")) or any(
        token in lowered for token in ("regulatory approval", "approved by fda")
    ):
        fields["regulatory_approval_confirmed"] = True
    if fields.get("regulatory_approval_confirmed") and (
        any(token in text for token in ("상업화", "출시", "매출 전환"))
        or any(token in lowered for token in ("approval-to-revenue", "approval to revenue"))
    ):
        fields["approval_to_revenue_bridge"] = True
    if any(token in text for token in ("로열티", "마일스톤")) or any(token in lowered for token in ("royalty", "milestone payment")):
        fields["royalty_route"] = True
        fields["partner_economics_visible"] = True
    if any(token in text for token in ("보험급여", "급여 등재")) or "reimbursement" in lowered:
        fields["reimbursement_confirmed"] = True
    if any(token in text for token in ("ARR 증가", "ARR 성장")) or any(
        token in lowered for token in ("arr growth", "recurring revenue growth")
    ):
        fields["arr_growth_visible"] = True
    if any(token in text for token in ("갱신율", "churn 감소")) or any(token in lowered for token in ("renewal", "retention", "nrr", "churn low")):
        fields["retention_or_renewal"] = True
        fields["contract_renewal_visible"] = True
    if any(token in text for token in ("좌석 확장", "사용자 확장")) or "seat expansion" in lowered:
        fields["seat_expansion_visible"] = True
    if any(token in text for token in ("PF 익스포저 축소", "재무구조 개선", "현금 회수 가시성")) or any(
        token in lowered for token in ("pf exposure reduced", "balance sheet repair", "cash collection visible")
    ):
        if "pf" in lowered or "PF" in text:
            fields["pf_exposure_reduced"] = True
        if "재무구조 개선" in text or "balance sheet repair" in lowered:
            fields["balance_sheet_repair"] = True
        if "현금 회수 가시성" in text or "cash collection visible" in lowered:
            fields["cash_collection_visible"] = True
    _add_qualitative_e2r_fields(text, lowered, fields)
    fields.update(_explicit_source_backed_fields(text))
    return fields


def _explicit_source_backed_fields(text: str) -> dict[str, Any]:
    fields: dict[str, Any] = {}
    for line in text.splitlines():
        match = _EXPLICIT_SOURCE_BACKED_FIELD_RE.match(line)
        if not match:
            continue
        key = match.group(1).strip()
        if not _safe_explicit_source_backed_field_key(key):
            continue
        value = _parse_explicit_source_backed_value(match.group(2).strip())
        if value is not None:
            fields[key] = value
    return fields


def _has_explicit_source_backed_field_block(text: str) -> bool:
    return any(_EXPLICIT_SOURCE_BACKED_FIELD_RE.match(line) for line in text.splitlines())


def _safe_explicit_source_backed_field_key(key: str) -> bool:
    if not key or any(key.startswith(prefix) for prefix in _EXPLICIT_FIELD_PREFIX_EXCLUDES):
        return False
    return bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{1,80}", key))


def _parse_explicit_source_backed_value(raw: str) -> Any:
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        lowered = raw.lower()
        if lowered == "true":
            return True
        if lowered == "false":
            return False
        try:
            number = float(raw.replace(",", ""))
        except ValueError:
            return raw[:300]
        return int(number) if number.is_integer() else number


def _add_qualitative_e2r_fields(text: str, lowered: str, fields: dict[str, Any]) -> None:
    ai_theme = _has_ai_infra_theme(lowered)
    hbm_context = "hbm" in lowered or "고대역폭메모리" in text
    if hbm_context:
        fields["hbm_context_mentioned"] = True
    if ai_theme:
        fields["emerging_theme_id"] = "AI_INFRA_PLATFORM_DATACENTER"
        fields["emerging_theme_active"] = True
        fields["emerging_theme_ai_infra_platform_datacenter"] = True
        fields["theme_transition_detected"] = True
        fields["market_frame_shift"] = True
    if ai_theme and any(token in lowered for token in ("매출", "revenue", "수주", "계약", "rpo", "backlog", "mou", "파트너십")):
        fields["theme_business_link_mentioned"] = True
    if any(token in lowered for token in ("엔비디아", "nvidia")):
        fields["nvidia_momentum_mentioned"] = True
    if any(token in lowered for token in ("gpu", "데이터센터", "data center", "datacenter")):
        fields["ai_infra_capacity_or_gpu_mentioned"] = True
    if any(token in lowered for token in ("gpu 할당", "gpu allocation", "gpu 공급", "gpu supply")):
        fields["gpu_allocation_mentioned"] = True
    if any(token in lowered for token in ("데이터센터 용량", "datacenter capacity", "전력 용량", "power capacity")):
        fields["datacenter_capacity_constraint"] = True
    if any(token in lowered for token in ("전력 부족", "power shortage", "전력망", "grid capacity")):
        fields["power_capacity_constraint"] = True
    if any(token in lowered for token in ("클라우드 매출", "cloud revenue", "gpu 매출", "ai 매출")):
        fields["gpu_cloud_revenue_visible"] = True
        fields["cloud_revenue_growth_visible"] = True
    if fields.get("cloud_revenue_growth_pct") not in (None, ""):
        fields["gpu_cloud_revenue_visible"] = True
        fields["cloud_revenue_growth_visible"] = True
    if any(token in lowered for token in ("rpo", "수주잔고", "backlog")) and ai_theme:
        fields["ai_infra_backlog_or_rpo"] = True
    if any(token in lowered for token in ("하이퍼스케일", "hyperscaler", "빅테크", "big tech")):
        fields["hyperscaler_customer"] = True
    if any(token in lowered for token in ("데이터센터 계약", "datacenter contract", "data center contract")):
        fields["data_center_contract"] = True
    if any(token in lowered for token in ("capex 부담", "투자 부담", "capex burden")):
        fields["capex_burden_risk"] = True
    if ai_theme and not fields.get("theme_business_link_mentioned"):
        fields["ai_theme_hype_without_revenue"] = True

    if any(token in text for token in ("수출 비중 확대", "수출 확대", "수출 증가", "해외 매출 확대")):
        fields["export_channel_expansion"] = True
        fields["export_growth_mentioned"] = True
    if any(token in text for token in ("해외 채널 확대", "해외 채널 확장", "북미 채널", "미국 채널")):
        fields["overseas_channel_expansion"] = True
        fields["channel_expansion"] = True
        fields["brand_channel_expansion"] = True
    if any(
        token in text
        for token in (
            "글로벌 유통망 확대",
            "글로벌 유통 확대",
            "플랫폼 유통 확대",
            "대형 유통 채널",
            "대형 리테일 채널",
            "입점 확대",
        )
    ) or any(
        token in lowered
        for token in (
            "global distribution",
            "distribution scale",
            "platform distribution",
            "retail channel expansion",
            "major retail channel",
        )
    ):
        fields["platform_distribution_scale"] = True
        fields["brand_channel_expansion"] = True
        fields["channel_expansion"] = True
    if any(token in text for token in ("반복 수요", "재구매", "리오더")) or any(
        token in lowered for token in ("recurring demand", "repeat purchase")
    ):
        fields["recurring_consumer_demand"] = True
    if any(token in text for token in ("재주문", "리오더")) or any(token in lowered for token in ("repeat order", "reorder")):
        fields["repeat_order_confirmed"] = True
        fields["channel_reorder_confirmed"] = True
        fields["recurring_consumer_demand"] = True
    if any(token in text for token in ("셀스루", "판매 회전", "재고 소진")) or any(
        token in lowered for token in ("sell-through", "sell through")
    ):
        fields["sell_through_confirmed"] = True
        fields["recurring_consumer_demand"] = True
    if "불닭" in text and any(token in text for token in ("수출", "채널", "미국", "해외")):
        fields["recurring_consumer_demand"] = True
        fields["export_channel_expansion"] = True
    if any(token in text for token in ("고마진 믹스", "믹스 개선", "수익성 높은", "OPM 개선", "마진 개선")):
        fields["high_margin_mix_improvement"] = True
    if hbm_context and (
        any(token in text for token in ("수요 증가", "수요 확대", "수요 강세", "수요 폭증", "수요 우위", "주문 확대", "고객 수요"))
        or any(token in lowered for token in ("demand growth", "strong demand", "customer demand"))
    ):
        fields["hbm_demand_mentioned"] = True
    if any(token in text for token in ("메모리 가격 상승", "DRAM 가격 상승", "D램 가격 상승", "NAND 가격 상승", "낸드 가격 상승")):
        fields["memory_price_increase_mentioned"] = True
        fields["pricing_power_mentioned"] = True
    if hbm_context and (
        any(token in text for token in ("HBM 가격 상승", "HBM 가격 인상", "가격 인상", "가격 상승", "ASP 상승", "평균판매가격"))
        or any(token in lowered for token in ("hbm price", "asp"))
    ):
        fields["memory_price_increase_mentioned"] = True
        fields["pricing_power_mentioned"] = True
        fields["asp_increase_mentioned"] = True
    if any(token in text for token in ("공급조절", "감산")) or "supply discipline" in lowered:
        fields["supply_discipline_mentioned"] = True
    semiconductor_cycle_context = hbm_context or any(
        token in lowered for token in ("memory", "dram", "nand", "semiconductor", "advanced packaging")
    ) or any(token in text for token in ("메모리", "반도체", "D램", "디램", "낸드", "패키징"))
    demand_cycle_visible = any(
        token in text
        for token in (
            "수요 증가",
            "수요 확대",
            "수요 강세",
            "수요 회복",
            "업황 개선",
            "주문 회복",
        )
    ) or any(token in lowered for token in ("demand growth", "strong demand", "demand recovery", "cycle recovery"))
    price_cycle_visible = bool(fields.get("memory_price_increase_mentioned") or fields.get("pricing_power_mentioned"))
    supply_cycle_visible = bool(fields.get("supply_discipline_mentioned")) or any(
        token in lowered for token in ("supply discipline", "capacity constraint", "bottleneck")
    )
    if semiconductor_cycle_context and demand_cycle_visible and (price_cycle_visible or supply_cycle_visible):
        fields["cycle_demand_visibility"] = True
        fields["end_market_demand_visibility"] = True
    if semiconductor_cycle_context and demand_cycle_visible and price_cycle_visible and supply_cycle_visible:
        fields["supply_demand_tightness"] = True
    if fields.get("cycle_demand_visibility") and any(
        token in text for token in ("추정치 상향", "목표주가 상향", "EPS 상향", "영업이익 상향")
    ):
        fields["cycle_to_revenue_bridge"] = True
    if any(token in text for token in ("선주문", "우선 배정", "최소 물량 보장", "최소 구매 보장")) or any(token in lowered for token in ("preorder", "allocation", "minimum purchase commitment")):
        fields["customer_preorder_or_allocation"] = True
    if hbm_context and (
        any(
            token in text
            for token in (
                "완판",
                "전량 판매",
                "전량판매",
                "물량 확보",
                "물량 선점",
                "물량 배정",
                "고객 수요 대비 공급",
                "공급 충족률",
                "공급 부족",
                "공급부족",
                "중장기 물량 확보",
                "장기 물량 확보",
            )
        )
        or any(token in lowered for token in ("sold out", "pre-sold", "sold-out", "capacity allocation", "supply allocation"))
    ):
        fields["customer_preorder_or_allocation"] = True
        fields["capacity_precommitted"] = True
        fields["hbm_capacity_pre_sold"] = True
    if hbm_context and (
        any(
            token in text
            for token in (
                "공급 부족",
                "공급부족",
                "공급이 제한",
                "공급 확대가 제한",
                "공급 충족률",
                "수요 대비 공급",
                "타이트",
                "신규 팹 증설에 시간",
                "단기간 내 공급 확대",
                "생산능력 부족",
            )
        )
        or any(token in lowered for token in ("supply shortage", "tight supply", "capacity constraint"))
    ):
        fields["supply_shortage_mentioned"] = True
        fields["capacity_constraint"] = True
        fields["capa_shortage"] = True
        fields["hbm_capacity_constraint"] = True
    if hbm_context and (
        any(token in text for token in ("CAPA 제약", "CAPA 병목", "패키징 병목", "첨단 패키징 병목"))
        or any(token in lowered for token in ("advanced packaging bottleneck", "packaging bottleneck"))
    ):
        fields["capacity_constraint"] = True
        fields["hbm_capacity_constraint"] = True
        fields["advanced_packaging_bottleneck"] = True
        fields["supply_demand_tightness"] = True
    if _has_defense_contract_context(text):
        fields["government_customer"] = True
    if any(token in text for token in ("장기계약", "장기 공급계약", "장기공급계약", "다년 계약")) or any(token in lowered for token in ("multi-year", "lta", "long-term agreement")):
        fields["multi_year_contract"] = True
        if hbm_context and fields.get("customer_preorder_or_allocation"):
            fields["revenue_visibility_contract"] = True
    if any(token in text for token in ("사상 최대 수주잔고", "최대 수주잔고")):
        fields["backlog_record_high"] = True


def _has_ai_infra_theme(lowered: str) -> bool:
    strong_tokens = (
        "인공지능",
        "하이퍼클로바",
        "hyperclova",
        "엔비디아",
        "nvidia",
        "gpu",
        "데이터센터",
        "data center",
        "datacenter",
        "클라우드 매출",
        "cloud revenue",
        "gpu cloud",
        "gpu 클라우드",
        "llm",
        "소버린 ai",
        "sovereign ai",
        "ai 반도체",
        "ai반도체",
        "ai 서버",
        "ai서버",
        "ai 인프라",
        "ai인프라",
        "ai 데이터센터",
        "ai데이터센터",
        "ai 매출",
        "ai매출",
        "ai 수요",
        "ai수요",
        "ai capex",
        "ai 투자",
        "ai투자",
    )
    if any(token in lowered for token in strong_tokens):
        return True
    if not re.search(r"(?<![a-z0-9가-힣])ai(?![a-z0-9가-힣])", lowered):
        return False
    context_tokens = (
        "반도체",
        "서버",
        "인프라",
        "데이터센터",
        "클라우드",
        "gpu",
        "매출",
        "수주",
        "계약",
        "capex",
        "엔비디아",
        "nvidia",
        "검색",
        "광고",
        "llm",
        "모델",
    )
    return any(token in lowered for token in context_tokens)


def _is_fetched_document_company_relevant(
    *,
    result: SearchResult,
    fetch_text: str,
    company_name: str,
    symbol: str,
    company_aliases: Sequence[str],
) -> bool:
    aliases = tuple(
        dict.fromkeys(
            alias.strip().lower()
            for alias in (company_name, symbol, *company_aliases)
            if alias and alias.strip()
        )
    )
    if not aliases:
        return False
    if _looks_like_other_company_report_hit(result=result, aliases=aliases):
        return False
    result_context = f"{result.title}\n{result.snippet or ''}\n{result.url}".lower()
    title_context = result.title.lower()
    stripped = _strip_common_news_boilerplate(fetch_text)
    if _has_explicit_source_backed_field_block(fetch_text) and (
        any(alias in result_context for alias in aliases)
        or any(alias in stripped[:1_500].lower() for alias in aliases)
    ):
        return True
    lead_body_context = _has_direct_company_context(stripped[:900], aliases)
    direct_body_context = _has_direct_company_context(stripped, aliases)
    if any(alias in title_context for alias in aliases):
        if _is_market_list_context(result_context) and not _has_direct_company_context(fetch_text, aliases):
            return False
        return True
    if any(alias in result_context for alias in aliases):
        return direct_body_context and lead_body_context
    return direct_body_context and lead_body_context


def _company_relevant_fetched_text(
    *,
    result: SearchResult,
    fetch_text: str,
    company_name: str,
    symbol: str,
    company_aliases: Sequence[str],
    max_chars: int = 12_000,
) -> str:
    aliases = _company_aliases(company_name=company_name, symbol=symbol, company_aliases=company_aliases)
    stripped = _strip_common_news_boilerplate(fetch_text)
    result_context = f"{result.title}\n{result.snippet or ''}\n{result.url}".lower()
    if _is_market_list_context(result_context):
        sentence_body = _company_relevant_sentence_text(stripped, aliases)
        if sentence_body:
            return sentence_body.strip()[:max_chars]
    lines = [line.strip() for line in stripped.splitlines() if line.strip()]
    lines = [line for line in lines if not _is_low_signal_site_line(line)]
    lowered_lines = [line.lower() for line in lines]
    selected_indexes: set[int] = set()
    for index, line in enumerate(lowered_lines):
        if any(alias in line for alias in aliases):
            if _is_market_list_context(line) and not _has_strong_company_specific_context(line):
                continue
            selected_indexes.update(range(max(0, index - 4), min(len(lines), index + 9)))

    if selected_indexes:
        body = "\n".join(lines[index] for index in sorted(selected_indexes))
    else:
        body = _company_relevant_sentence_text(stripped, aliases) or ""
    if _is_market_list_context(result_context):
        header = _company_relevant_sentence_text(
            "\n".join(part for part in (result.title, result.snippet or "") if part),
            aliases,
            max_chars=1_000,
        )
    else:
        header = "\n".join(part for part in (result.title, result.snippet or "") if part)
    return f"{header}\n{body}".strip()[:max_chars]


def _company_relevant_sentence_text(text: str, aliases: Sequence[str], *, max_chars: int = 6_000) -> str:
    if not text.strip():
        return ""
    chunks = tuple(
        re.sub(r"\s+", " ", part).strip()
        for part in re.split(r"(?<=[.!?。！？])\s+|\n+", text)
        if part.strip()
    )
    selected: list[str] = []
    for chunk in chunks:
        lowered = chunk.lower()
        if any(alias in lowered for alias in aliases):
            if _is_market_list_context(lowered) and not _has_strong_company_specific_context(lowered):
                continue
            selected.append(chunk)
    return "\n".join(dict.fromkeys(selected))[:max_chars]


def _should_keep_full_report_text(
    *,
    result: SearchResult,
    company_name: str,
    symbol: str,
    company_aliases: Sequence[str],
) -> bool:
    if classify_search_result(result) != "report":
        return False
    if not (result.is_pdf or result.is_report_domain):
        return False
    aliases = _company_aliases(company_name=company_name, symbol=symbol, company_aliases=company_aliases)
    title_haystack = result.title.lower()
    return any(alias in title_haystack for alias in aliases)


def _looks_like_other_company_report_hit(*, result: SearchResult, aliases: Sequence[str]) -> bool:
    title = result.title.lower()
    if any(alias in title for alias in aliases):
        return False
    url = result.url.lower()
    report_tokens = (
        "종목분석",
        "기업분석",
        "목표주가",
        "투자의견",
        "company_read",
        "research/company",
        "리포트",
        "review",
    )
    if not any(token in title or token in url for token in report_tokens):
        return False
    return bool(result.is_report_domain or "company_read" in url or "research/company" in url)


_CURRENT_REPORT_MAX_AGE_DAYS = 548


def _stale_research_report_reason(
    *,
    report: ResearchReport,
    result: SearchResult,
    text: str,
    as_of_date: date,
) -> str | None:
    if (as_of_date - report.publish_date).days > _CURRENT_REPORT_MAX_AGE_DAYS:
        return "stale_research_report_publish_date"
    context = f"{result.title}\n{result.snippet or ''}\n{text}"
    period_end = latest_reported_period_end(context)
    if period_end is None:
        return None
    if (as_of_date - period_end).days <= _CURRENT_REPORT_MAX_AGE_DAYS:
        return None
    if _has_current_forward_estimate_context(context, as_of_date):
        return None
    return "stale_research_report_inferred_period"


def _has_current_forward_estimate_context(text: str, as_of_date: date) -> bool:
    years = range(as_of_date.year, as_of_date.year + 3)
    return any(
        re.search(rf"\b{year}\s*e\b|{year}\s*년\s*(?:예상|전망|가이던스)", text, re.IGNORECASE)
        for year in years
    )


def _strip_common_news_boilerplate(text: str) -> str:
    markers = (
        "많이 본 기사",
        "오늘의 주요뉴스",
        "헤드라인 뉴스",
        "관련기사",
        "관련 기사",
        "인기뉴스",
        "인기 뉴스",
        "추천뉴스",
        "추천 뉴스",
        "이 시각",
        "투데이 컴퍼니",
        "리얼시승기",
        "most read",
        "popular news",
        "related articles",
    )
    lowered = text.lower()
    cut_at = len(text)
    for marker in markers:
        index = lowered.find(marker.lower())
        if index >= 80:
            cut_at = min(cut_at, index)
    return text[:cut_at]


def _company_aliases(*, company_name: str, symbol: str, company_aliases: Sequence[str]) -> tuple[str, ...]:
    aliases = []
    for alias in (company_name, symbol, *company_aliases):
        cleaned = alias.strip().lower() if alias else ""
        if len(cleaned) < 2:
            continue
        aliases.append(cleaned)
    return tuple(dict.fromkeys(aliases))


def _is_market_list_context(text: str) -> bool:
    return any(
        token in text
        for token in (
            "코스피",
            "코스닥",
            "증시",
            "시황",
            "마감",
            "장중",
            "순매수",
            "매수 상위",
            "주식고수",
            "시총 상위",
            "주요공시",
            "주요 공시",
            "외",
            "프리마켓",
            "마켓시그",
            "주목할 종목",
            "관심종목",
            "오늘의 종목",
            "특징주",
            "k반도체",
            "k-반도체",
            "업계동향",
            "관련주",
        )
    )


def _has_direct_company_context(text: str, aliases: Sequence[str]) -> bool:
    lowered = text.lower()
    for alias in aliases:
        starts = [match.start() for match in re.finditer(re.escape(alias), lowered)]
        for start in starts:
            excerpt = lowered[max(0, start - 180) : start + len(alias) + 260]
            if _is_market_list_context(excerpt) and not _has_strong_company_specific_context(excerpt):
                continue
            if _has_company_business_context(excerpt):
                return True
    return False


def _has_strong_company_specific_context(excerpt: str) -> bool:
    return any(
        token in excerpt
        for token in (
            "영업이익",
            "순이익",
            "매출",
            "실적",
            "컨센서스",
            "목표주가",
            "투자의견",
            "단일판매",
            "공급계약",
            "계약금액",
            "계약상대방",
            "신규시설투자",
            "주식교환",
            "지분가치",
            "자회사",
            "주주환원",
            "자사주",
            "논리",
            "훼손",
            "밸류에이션",
            "과열",
            "회계",
            "신뢰",
            "현금흐름",
            "임상",
            "허가",
            "승인",
            "기술이전",
            "로열티",
            "사업",
            "earnings",
            "revenue",
            "profit",
            "revision",
            "valuation",
            "thesis",
            "cashflow",
        )
    )


def _has_company_business_context(excerpt: str) -> bool:
    return any(
        token in excerpt
        for token in (
            "영업이익",
            "순이익",
            "매출",
            "실적",
            "컨센서스",
            "수주",
            "계약",
            "수주잔고",
            "rpo",
            "backlog",
            "목표주가",
            "투자의견",
            "지분가치",
            "자회사",
            "주주환원",
            "자사주",
            "임상",
            "허가",
            "승인",
            "기술이전",
            "로열티",
            "마진",
            "수익성",
            "opm",
            "asp",
            "논리",
            "훼손",
            "밸류에이션",
            "과열",
            "회계",
            "신뢰",
            "현금흐름",
            "판매",
            "출하",
            "신제품",
            "사업",
            "capa",
            "증설",
            "capacity",
            "revenue",
            "margin",
            "earnings",
            "profit",
            "revision",
            "valuation",
            "thesis",
            "cashflow",
            "price-only",
            "price only",
        )
    )


def _has_target_company_disclosure_context(
    *,
    text: str,
    company_name: str,
    symbol: str,
    company_aliases: Sequence[str],
) -> bool:
    aliases = _company_aliases(company_name=company_name, symbol=symbol, company_aliases=company_aliases)
    if not aliases:
        return False
    lowered = text.lower()
    disclosure_terms = (
        "단일판매",
        "공급계약",
        "신규시설투자",
        "계약금액",
        "계약상대방",
        "계약기간",
        "주식교환",
        "주식교환·이전",
        "유상증자",
        "전환사채",
        "감사의견",
        "감사보고서",
        "single sales",
        "supply contract",
        "facility investment",
        "share exchange",
    )
    for alias in aliases:
        starts = [match.start() for match in re.finditer(re.escape(alias), lowered)]
        for start in starts:
            excerpt = lowered[max(0, start - 140) : start + len(alias) + 360]
            if any(term in excerpt for term in disclosure_terms):
                return True
    return False


def _is_low_signal_site_line(line: str) -> bool:
    normalized = re.sub(r"\s+", "", line).lower()
    low_signal = (
        "기사검색",
        "검색버튼",
        "통합검색",
        "상세검색",
        "광고문의",
        "광고안내",
        "제휴문의",
        "구독신청",
        "회원가입",
        "로그인",
        "로그아웃",
        "본문내용바로가기",
        "메인메뉴로바로가기",
    )
    if normalized in low_signal:
        return True
    return len(normalized) <= 24 and any(token in normalized for token in low_signal)


def _has_defense_contract_context(text: str) -> bool:
    lowered = text.lower()
    defense_tokens = ("방산", "방위산업", "defense", "defence", "military", "k9", "k2", "천무", "fa-50", "kf-21")
    visibility_tokens = (
        "수출",
        "계약",
        "수주",
        "수주잔고",
        "납품",
        "인도",
        "폴란드",
        "루마니아",
        "정부",
        "방위사업청",
        "export",
        "contract",
        "backlog",
        "delivery",
        "government",
    )
    for left in defense_tokens:
        start = lowered.find(left)
        while start >= 0:
            excerpt = lowered[max(0, start - 180) : start + len(left) + 180]
            if any(right in excerpt for right in visibility_tokens):
                return True
            start = lowered.find(left, start + len(left))
    return False


def _number_after(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        match = re.search(
            rf"{re.escape(label)}[^0-9\-]*(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>%|개월|년|배|x)?",
            text,
            re.IGNORECASE,
        )
        if match:
            value = float(match.group("number").replace(",", ""))
            unit = match.group("unit")
            if unit == "년":
                return value
            return value
    return None


def _percent_after(text: str, labels: tuple[str, ...]) -> float | None:
    for label in labels:
        match = re.search(rf"{re.escape(label)}[^0-9\-]*(?P<number>-?[0-9][0-9,]*(?:\.[0-9]+)?)\s*%", text, re.IGNORECASE)
        if match:
            return float(match.group("number").replace(",", ""))
    return None


def _excerpt(text: str, labels: tuple[str, ...]) -> str:
    for label in labels:
        index = text.lower().find(label.lower())
        if index >= 0:
            return text[max(0, index - 40) : min(len(text), index + 120)].replace("\n", " ").strip()
    return text[:160]


def _disclosure_type(title: str, text: str) -> str:
    haystack = f"{title}\n{text}"
    if "신규시설투자" in haystack:
        return "신규시설투자"
    if "감사의견" in haystack:
        return "감사의견"
    if "단일판매" in haystack or "공급계약" in haystack:
        return "단일판매·공급계약체결"
    return "web-disclosure"


__all__ = [
    "DroppedSearchResult",
    "WebResearchInput",
    "WebResearchResult",
    "WebResearchRunner",
    "classify_search_result",
    "extract_e2r_text_fields",
]
