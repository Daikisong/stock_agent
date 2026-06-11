"""Search result ranking for E2R manual research usefulness."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from typing import Sequence

from e2r.research.search_provider import SearchResult


REPORT_KEYWORDS: tuple[str, ...] = (
    "Review",
    "리뷰",
    "목표주가",
    "컨센서스",
    "실적",
    "영업이익",
    "매출",
    "전망치",
    "추정치",
    "어닝",
    "서프라이즈",
    "수주잔고",
    "CAPA",
    "장기공급계약",
    "ASP",
    "리드타임",
    "상향",
    "매출액 대비",
    "OPM",
    "HBM",
    "데이터센터",
    "PDF",
)

HIGH_TIER_SOURCE_TOKENS: tuple[str, ...] = (
    "hana",
    "samsung",
    "ibk",
    "nh",
    "shinhan",
    "mirae",
    "kiwoom",
    "sec",
    "opendart",
    "kind",
    "broker",
    "research",
    "reuters",
    "dart",
)

LOW_QUALITY_TOKENS: tuple[str, ...] = ("forum", "blog", "rumor", "dcinside", "fmkorea", "advert", "광고")
IRRELEVANT_TOKENS: tuple[str, ...] = ("채용", "중고", "쇼핑", "부동산", "광고", "맛집")


@dataclass(frozen=True)
class RankedSearchResult:
    """Ranked result with transparent scoring reasons."""

    result: SearchResult
    score: float
    positive_reasons: tuple[str, ...] = field(default_factory=tuple)
    negative_reasons: tuple[str, ...] = field(default_factory=tuple)


class SearchResultRanker:
    """Rank search results by expected E2R evidence value."""

    def rank(
        self,
        results: Sequence[SearchResult],
        *,
        company_name: str,
        as_of_date: date,
    ) -> tuple[RankedSearchResult, ...]:
        seen_urls: set[str] = set()
        ranked: list[RankedSearchResult] = []
        for result in results:
            is_duplicate = result.url in seen_urls
            seen_urls.add(result.url)
            ranked.append(self.score_result(result, company_name=company_name, as_of_date=as_of_date, is_duplicate=is_duplicate))
        return tuple(sorted(ranked, key=lambda item: (-item.score, item.result.rank or 9999, item.result.title)))

    def score_result(
        self,
        result: SearchResult,
        *,
        company_name: str,
        as_of_date: date,
        is_duplicate: bool = False,
    ) -> RankedSearchResult:
        score = 0.0
        positive: list[str] = []
        negative: list[str] = []
        haystack = f"{result.title} {result.snippet or ''}"
        lowered = f"{haystack} {result.source} {result.url}".lower()

        if result.is_report_domain:
            score += 18.0
            positive.append("recognized_report_domain")
        if result.is_pdf:
            score += 12.0
            positive.append("pdf")
        for keyword in REPORT_KEYWORDS:
            if keyword.lower() in lowered:
                score += 5.0
                positive.append(f"keyword:{keyword}")
        if any(token in lowered for token in HIGH_TIER_SOURCE_TOKENS):
            score += 8.0
            positive.append("high_tier_source")
        if company_name and company_name in haystack:
            score += 12.0
            positive.append("company_match")
        else:
            score -= 8.0
            negative.append("missing_company_name")
        query_terms = _query_terms(result.query, company_name=company_name)
        if query_terms:
            matched_terms = tuple(term for term in query_terms if term in lowered)
            if matched_terms:
                score += min(24.0, len(matched_terms) * 4.0)
                positive.append("query_intent_match")
            else:
                score -= 55.0 if _stale_asof_mismatch(result, as_of_date) else 10.0
                negative.append("query_intent_mismatch")
        if result.confidence:
            score += result.confidence * 10.0
            positive.append("provider_confidence")

        if result.published_at is not None:
            result_date = result.published_at.date()
            if result_date > as_of_date:
                score -= 100.0
                negative.append("future_result")
            else:
                age_days = (as_of_date - result_date).days
                if age_days <= 45:
                    score += 8.0
                    positive.append("fresh_result")
                elif age_days <= 180:
                    score += 4.0
                    positive.append("recent_result")
                elif age_days > 730:
                    score -= 10.0
                    negative.append("old_result")
        if any(token in lowered for token in LOW_QUALITY_TOKENS):
            score -= 20.0
            negative.append("forum_or_rumor_source")
        if any(token in lowered for token in IRRELEVANT_TOKENS):
            score -= 15.0
            negative.append("advertising_or_irrelevant")
        if is_duplicate:
            score -= 100.0
            negative.append("duplicate_url")
        return RankedSearchResult(
            result=result,
            score=round(score, 4),
            positive_reasons=tuple(dict.fromkeys(positive)),
            negative_reasons=tuple(dict.fromkeys(negative)),
        )


def _query_terms(query: str | None, *, company_name: str) -> tuple[str, ...]:
    if not query:
        return ()
    company_tokens = set(_tokens(company_name))
    ignored = company_tokens | {"site", "http", "https", "www", "com", "co", "kr", "pdf", "review"}
    return tuple(dict.fromkeys(token for token in _tokens(query) if token not in ignored and len(token) >= 2))


def _stale_asof_mismatch(result: SearchResult, as_of_date: date) -> bool:
    if result.published_at is None:
        return False
    return (as_of_date - result.published_at.date()).days > 730


def _tokens(text: str | None) -> tuple[str, ...]:
    if not text:
        return ()
    return tuple(token.lower() for token in re.findall(r"[0-9A-Za-z가-힣]+", text) if token.strip())


__all__ = ["RankedSearchResult", "SearchResultRanker"]
