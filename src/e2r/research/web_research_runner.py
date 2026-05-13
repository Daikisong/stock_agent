"""Fixture-first web research runner for E2R manual workflow replication."""

from __future__ import annotations

import re
from dataclasses import dataclass, field, replace
from datetime import date, datetime
from typing import Any, Mapping, Sequence

from e2r.models import DisclosureEvent, Evidence, Market, NewsItem, RedTeamFinding, ResearchReport, SourceTier
from e2r.pipeline.evidence_builder import evidence_from_feature_domains
from e2r.research.page_fetcher import FetchResult, PageFetcher
from e2r.research.pdf_text_extractor import PDFTextExtractor
from e2r.research.query_planner import QueryPlan, QueryPlanner, QuerySpec
from e2r.research.report_parser import parse_research_report_text
from e2r.research.search_provider import EmptySearchProvider, SearchProvider, SearchResult
from e2r.research.search_result_ranker import RankedSearchResult, SearchResultRanker
from e2r.sources.naver_news import NaverNewsConnector, parse_news_event
from e2r.sources.opendart import OpenDARTConnector


@dataclass(frozen=True)
class WebResearchInput:
    """One company web research request."""

    company_name: str
    symbol: str
    sector: str | None
    market: Market
    as_of_date: date
    stage_context: str | None = None
    max_results_per_query: int = 5
    top_results: int = 8


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
                dropped.append(DroppedSearchResult(result=result, reason=fetch.reason or "fetch_unavailable"))
                continue
            kind = classify_search_result(result)
            if kind == "report":
                parsed = self._parse_report(inputs, result, fetch.text)
                parsed_reports.append(parsed)
            elif kind == "disclosure":
                parsed_disclosures.append(self._parse_disclosure(inputs, result, fetch.text))
            elif kind == "news":
                news = self._parse_news(inputs, result, fetch.text)
                parsed_news.append(news)
                finding = NaverNewsConnector.to_red_team_finding(news)
                if finding is not None:
                    findings.append(finding)
            else:
                dropped.append(DroppedSearchResult(result=result, reason="unknown_document_type"))

        evidence = evidence_from_feature_domains(
            market=inputs.market,
            fallback_symbol=inputs.symbol,
            disclosures=parsed_disclosures,
            research_reports=parsed_reports,
            news_items=parsed_news,
        )
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
        top_results: int,
    ) -> tuple[list[RankedSearchResult], list[DroppedSearchResult]]:
        selected: list[RankedSearchResult] = []
        dropped: list[DroppedSearchResult] = []
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
            if len(selected) >= top_results:
                dropped.append(DroppedSearchResult(result=item.result, reason="not_selected"))
                continue
            selected.append(item)
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
        parsed = parse_research_report_text(
            symbol=inputs.symbol,
            market=inputs.market,
            text=text,
            metadata={
                "title": result.title,
                "broker": result.source,
                "publish_date": published,
                "as_of_date": inputs.as_of_date,
                "url": result.url,
                "market": inputs.market.value,
            },
        )
        merged_fields = dict(parsed.report.parsed_fields)
        merged_fields.update({key: value for key, value in extract_e2r_text_fields(text).items() if value not in (None, "")})
        merged_fields.setdefault("source_url", result.url)
        merged_fields.setdefault("parser_confidence", parsed.parsed_fields.get("parser_confidence", 0.65))
        return replace(parsed.report, parsed_fields=merged_fields, raw_text=text)

    @staticmethod
    def _parse_disclosure(inputs: WebResearchInput, result: SearchResult, text: str) -> DisclosureEvent:
        published = result.published_at or datetime(inputs.as_of_date.year, inputs.as_of_date.month, inputs.as_of_date.day, 8, 0)
        parsed_fields = extract_e2r_text_fields(text)
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
        parsed_fields.update(extract_e2r_text_fields(f"{result.title}\n{text}"))
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


def classify_search_result(result: SearchResult) -> str:
    """Classify a result as report, disclosure, news, or unknown."""

    haystack = f"{result.title} {result.snippet or ''} {result.url}"
    if result.is_report_domain or result.is_pdf or any(token in haystack for token in ("Review", "리포트", "목표주가", "PDF", "OPM")):
        return "report"
    if result.is_disclosure or any(token in haystack for token in ("단일판매", "공급계약", "신규시설투자", "감사의견", "공시")):
        return "disclosure"
    if result.is_news or any(token in haystack for token in ("뉴스", "보도", "기사", "news")):
        return "news"
    return "unknown"


def extract_e2r_text_fields(text: str) -> dict[str, Any]:
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
        ("op_delta_to_market_cap", ("OP 증가분/시총", "영업이익 증가분/시총")),
        ("capex_to_sales", ("CAPEX/매출", "투자/매출")),
        ("target_multiple_delta", ("멀티플 상향폭", "multiple expansion")),
        ("return_since_stage3", ("return_since_stage3", "return since Stage 3", "Stage 3 이후 수익률")),
        ("return_12_24m", ("return_12_24m", "12~24개월 수익률", "12-24m return")),
    ):
        value = _number_after(text, labels)
        if value is not None:
            fields[key] = value

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
    if "해지 불가" in text or "취소 불가" in text or "take-or-pay" in lowered:
        fields["non_cancellable"] = True
    if "사상 최대 수주잔고" in text or "record backlog" in lowered:
        fields["record_backlog"] = True
    if "capa 부족" in lowered or "생산능력 부족" in text or "capacity constraint" in lowered:
        fields["capacity_constraint"] = True
    if "판가 전가" in text or "가격 전가" in text or "pricing power" in lowered:
        fields["pricing_power_confirmed"] = True
    if "멀티플 상향" in text or "리레이팅" in text or "rerating" in lowered:
        fields["market_frame_shift"] = True
        fields["target_multiple_rerating"] = True
    if "구조적 공급부족" in text or "structural shortage" in lowered:
        fields["shortage_type"] = "structural"
    if any(token in lowered for token in ("pandemic", "temporary", "one-off")) or any(token in text for token in ("팬데믹", "코로나", "일회성", "진단키트")):
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
    return fields


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
