"""Convert search result snippets into low-confidence news evidence."""

from __future__ import annotations

import html
import re
from datetime import date, datetime
from typing import Any, Sequence

from e2r.evidence_ids import stable_news_evidence_id
from e2r.models import Market, NewsItem, SourceTier
from e2r.research.financial_text_fields import extract_reported_financial_fields
from e2r.research.search_provider import SearchResult
from e2r.sources.naver_news import parse_news_event


AI_INFRA_THEME_ID = "AI_INFRA_PLATFORM_DATACENTER"

_AI_THEME_TOKENS = (
    "인공지능",
    "하이퍼클로바",
    "hyperclova",
    "클로바",
    "clova",
    "엔비디아",
    "nvidia",
    "gpu",
    "데이터센터",
    "data center",
    "datacenter",
    "llm",
    "초거대",
    "소버린",
    "sovereign",
)
_BUSINESS_EVIDENCE_TOKENS = (
    "매출",
    "revenue",
    "수주",
    "계약",
    "rpo",
    "backlog",
    "capex",
    "투자",
    "증설",
    "mou",
    "파트너십",
    "partnership",
    "공급",
)


def news_item_from_search_snippet(
    result: SearchResult,
    *,
    company_name: str,
    symbol: str,
    sector: str | None,
    market: Market,
    as_of_date: date,
    company_aliases: Sequence[str] = (),
) -> NewsItem | None:
    """Build a snippet-only ``NewsItem`` when a search hit is company-relevant.

    스니펫 증거는 본문을 확인하지 못한 상태라 낮은 신뢰로만 사용한다.
    날짜가 없으면 as_of_date 08:00으로 합성하고 Green 해제 근거에서는 제외한다.
    """

    del market
    title = _clean_text(result.title)
    snippet = _clean_text(result.snippet or "")
    if not title:
        return None
    if result.published_at is not None and result.published_at.date() > as_of_date:
        return None
    haystack = f"{title}\n{snippet}\n{result.url}".lower()
    aliases = _aliases(company_name=company_name, symbol=symbol, company_aliases=company_aliases)
    if not _is_company_relevant(haystack=haystack, aliases=aliases):
        return None
    if not any(alias in title.lower() for alias in aliases):
        return None
    if _looks_like_other_company_report_hit(title=title, url=result.url, aliases=aliases):
        return None
    if not _has_research_signal(haystack):
        return None

    date_verified = bool(result.date_verified) if result.date_verified is not None else result.published_at is not None
    green_allowed = bool(result.green_allowed_by_date) if result.green_allowed_by_date is not None else date_verified
    published = result.published_at or datetime(as_of_date.year, as_of_date.month, as_of_date.day, 8, 0)
    parsed = _snippet_parsed_fields(
        title=title,
        snippet=snippet,
        result=result,
        as_of_date=as_of_date,
        date_verified=date_verified,
        green_allowed=green_allowed,
    )
    parsed["evidence_id"] = stable_news_evidence_id(
        symbol=symbol,
        published_date=published.date(),
        source=result.source or "search-snippet",
        source_url=result.url,
        title=title,
    )
    body = snippet or title
    return NewsItem(
        symbol=symbol,
        sector=sector,
        published_at=published,
        source=result.source or "search-snippet",
        title=title,
        as_of_date=as_of_date,
        body=body,
        source_tier=SourceTier.TIER_3,
        theme_tags=(AI_INFRA_THEME_ID,) if parsed.get("emerging_theme_ai_infra_platform_datacenter") else (),
        parsed_fields=parsed,
    )


def is_search_snippet_only(fields: Any) -> bool:
    return bool(getattr(fields, "get", lambda key, default=None: default)("search_snippet_only", False))


def _snippet_parsed_fields(
    *,
    title: str,
    snippet: str,
    result: SearchResult,
    as_of_date: date,
    date_verified: bool,
    green_allowed: bool,
) -> dict[str, Any]:
    text = f"{title}\n{snippet}"
    parsed = dict(parse_news_event(title=title, body=snippet))
    for key, value in extract_reported_financial_fields(text).items():
        parsed.setdefault(key, value)
    lowered = text.lower()
    ai_theme = _has_ai_infra_theme(lowered)
    business_link = any(token in lowered for token in _BUSINESS_EVIDENCE_TOKENS)
    parsed.update(
        {
            "search_snippet_only": True,
            "source_url": result.url,
            "source_query": result.query,
            "source_title": title,
            "source_published_at": result.published_at.isoformat() if result.published_at else None,
            "date_verified": date_verified,
            "search_snippet_date_unverified": not date_verified,
            "green_allowed_by_date": green_allowed,
            "confidence": 0.35 if date_verified else 0.25,
            "parser_confidence": 0.35 if date_verified else 0.25,
            "as_of_date": as_of_date.isoformat(),
        }
    )
    if ai_theme:
        parsed["emerging_theme_id"] = AI_INFRA_THEME_ID
        parsed["emerging_theme_active"] = True
        parsed["emerging_theme_ai_infra_platform_datacenter"] = True
        parsed["theme_transition_detected"] = True
        parsed["market_frame_shift"] = True
    if ai_theme and business_link:
        parsed["theme_business_link_mentioned"] = True
    if any(token in lowered for token in ("nvidia", "엔비디아")):
        parsed["nvidia_momentum_mentioned"] = True
    if any(token in lowered for token in ("gpu", "데이터센터", "data center", "datacenter")):
        parsed["ai_infra_capacity_or_gpu_mentioned"] = True
    if any(token in lowered for token in ("클라우드 매출", "cloud revenue", "gpu 매출", "ai 매출")):
        parsed["gpu_cloud_revenue_visible"] = True
    return {key: value for key, value in parsed.items() if value is not None}


def _aliases(*, company_name: str, symbol: str, company_aliases: Sequence[str]) -> tuple[str, ...]:
    aliases = [company_name, symbol, *company_aliases]
    clean = tuple(dict.fromkeys(alias.strip().lower() for alias in aliases if alias and alias.strip()))
    return clean


def _is_company_relevant(*, haystack: str, aliases: Sequence[str]) -> bool:
    if not aliases:
        return False
    return any(alias in haystack for alias in aliases)


def _looks_like_other_company_report_hit(*, title: str, url: str, aliases: Sequence[str]) -> bool:
    lowered_title = title.lower()
    if any(alias in lowered_title for alias in aliases):
        return False
    lowered_url = (url or "").lower()
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
    return any(token in lowered_title or token in lowered_url for token in report_tokens)


def _has_research_signal(haystack: str) -> bool:
    return _has_ai_infra_theme(haystack) or any(token in haystack for token in _BUSINESS_EVIDENCE_TOKENS)


def _has_ai_infra_theme(lowered: str) -> bool:
    strong_tokens = (
        *_AI_THEME_TOKENS,
        "클라우드 매출",
        "cloud revenue",
        "gpu cloud",
        "gpu 클라우드",
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


def _clean_text(value: str) -> str:
    text = html.unescape(value or "")
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


__all__ = ["AI_INFRA_THEME_ID", "is_search_snippet_only", "news_item_from_search_snippet"]
