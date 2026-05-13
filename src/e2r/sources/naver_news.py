"""Naver News connector and event normalizer."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping

from e2r.models import Evidence, Market, NewsItem, RedTeamFinding, SourceTier
from e2r.sources.source_errors import (
    SourceRequest,
    datetime_value,
    float_or_none,
    load_fixture_records,
    market_value,
    parsed_fields_from_record,
    require_credential,
    source_tier_value,
    text_or_none,
    tuple_value,
)


NAVER_NEWS_BASE_URL = "https://openapi.naver.com/v1/search/news.json"

COMPANY_NEWS_QUERY_TEMPLATES: tuple[str, ...] = (
    "{company} 수주잔고",
    "{company} 장기공급계약",
    "{company} 단일판매 공급계약",
    "{company} 신규시설투자",
    "{company} CAPA 증설",
    "{company} 영업이익 컨센서스 상회",
    "{company} 목표주가 상향",
    "{company} 미국향 수주",
    "{company} 데이터센터 수주",
    "{company} 공급부족",
    "{company} ASP 상승",
    "{company} 판가 상승",
)

SECTOR_NEWS_QUERY_TEMPLATES: tuple[str, ...] = (
    "{sector} 공급 부족",
    "{sector} 리드타임",
    "{sector} 가격 상승",
    "{sector} 장기계약",
    "{sector} 선수금",
)

NEWS_PARSED_FIELDS: tuple[str, ...] = (
    "event_type",
    "mentioned_product",
    "mentioned_region",
    "customer_type",
    "contract_amount",
    "capex_amount",
    "backlog_amount",
    "margin_comment",
    "asp_comment",
    "capa_comment",
    "shortage_comment",
    "risk_comment",
    "source_tier",
    "confidence",
)


@dataclass(frozen=True)
class NaverNewsConnector:
    """Fixture-first Naver News connector.

    Live collection requires Naver API credentials and should be rate-limited by
    an external caller. This class only builds request metadata.
    """

    client_id: str | None = None
    client_secret: str | None = None
    fixture_root: str | Path | None = "data/raw/naver_news"
    fixture_mode: bool = True
    base_url: str = NAVER_NEWS_BASE_URL

    def build_company_search_requests(self, company: str, as_of_date: date) -> tuple[SourceRequest, ...]:
        return tuple(self._build_search_request(template.format(company=company), as_of_date) for template in COMPANY_NEWS_QUERY_TEMPLATES)

    def build_sector_search_requests(self, sector: str, as_of_date: date) -> tuple[SourceRequest, ...]:
        return tuple(self._build_search_request(template.format(sector=sector), as_of_date) for template in SECTOR_NEWS_QUERY_TEMPLATES)

    def require_live_credentials(self) -> tuple[str, str]:
        return (
            require_credential(self.client_id, "NAVER_CLIENT_ID"),
            require_credential(self.client_secret, "NAVER_CLIENT_SECRET"),
        )

    def get_news(self, symbol: str, start: date, end: date, as_of_date: date) -> tuple[NewsItem, ...]:
        items = tuple(self.normalize_news_item(row) for row in load_fixture_records(self.fixture_root, "news"))
        return tuple(
            sorted(
                (
                    item
                    for item in items
                    if item.symbol in (symbol, None)
                    and start <= item.published_at.date() <= end
                    and item.published_at.date() <= as_of_date
                    and item.as_of_date <= as_of_date
                ),
                key=lambda item: item.published_at,
            )
        )

    def _build_search_request(self, query: str, as_of_date: date) -> SourceRequest:
        headers = {}
        if self.client_id:
            headers["X-Naver-Client-Id"] = self.client_id
        if self.client_secret:
            headers["X-Naver-Client-Secret"] = self.client_secret
        return SourceRequest(
            method="GET",
            url=self.base_url,
            params={"query": query, "display": 20, "sort": "date", "as_of_date": as_of_date.isoformat()},
            headers=headers,
            fixture_mode=self.fixture_mode,
            credential_name="NAVER_CLIENT_ID/NAVER_CLIENT_SECRET",
        )

    @classmethod
    def normalize_news_item(cls, row: Mapping[str, Any]) -> NewsItem:
        known = {
            "symbol",
            "sector",
            "published_at",
            "pubDate",
            "source",
            "originallink",
            "link",
            "title",
            "as_of_date",
            "body",
            "description",
            "source_tier",
            "theme_tags",
            "sentiment",
            "parsed_fields",
            "market",
        }
        title = str(row.get("title") or "")
        body = text_or_none(row.get("body") or row.get("description"))
        published = datetime_value(row.get("published_at") or row.get("pubDate"))
        parsed = parsed_fields_from_record(row, known)
        parsed.update({key: row[key] for key in NEWS_PARSED_FIELDS if row.get(key) not in (None, "")})
        parsed = {key: _coerce_news_value(key, value) for key, value in parsed.items()}
        for key, value in parse_news_event(title=title, body=body or "").items():
            parsed.setdefault(key, value)
        parsed.setdefault("confidence", _news_confidence(parsed, body))
        parsed.setdefault("source_tier", int(source_tier_value(parsed.get("source_tier"), SourceTier.TIER_2)))
        return NewsItem(
            symbol=text_or_none(row.get("symbol")),
            sector=text_or_none(row.get("sector")),
            published_at=published,
            source=str(row.get("source") or "Naver News"),
            title=title,
            as_of_date=datetime_value(row.get("as_of_date") or published).date(),
            body=body,
            source_tier=source_tier_value(parsed.get("source_tier"), SourceTier.TIER_2),
            theme_tags=tuple_value(row.get("theme_tags")),
            sentiment=float_or_none(row.get("sentiment")),
            parsed_fields=parsed,
        )

    @staticmethod
    def to_evidence(news: NewsItem, market: Market = Market.KR) -> Evidence:
        parsed = dict(news.parsed_fields)
        confidence = float_or_none(parsed.get("confidence")) or 0.5
        return Evidence(
            evidence_id=f"naver-news:{news.symbol or news.sector or 'sector'}:{news.published_at.date().isoformat()}:{abs(hash(news.title))}",
            source_type="news",
            source_name=news.source,
            source_tier=news.source_tier,
            published_at=news.published_at,
            observed_at=news.published_at,
            available_at=news.published_at,
            as_of_date=news.as_of_date,
            market=market,
            symbol=news.symbol or news.sector or "SECTOR",
            title=news.title,
            excerpt_or_value=(news.body or "")[:240] if news.body else None,
            parsed_fields=parsed,
            confidence=confidence,
        )

    @staticmethod
    def to_red_team_finding(news: NewsItem) -> RedTeamFinding | None:
        parsed = news.parsed_fields
        risk_comment = str(parsed.get("risk_comment") or "")
        if not risk_comment and not any(parsed.get(key) for key in ("accounting_or_trust_issue", "contract_cancelled_or_delayed", "trading_halt")):
            return None
        risk_type = "accounting_or_trust_issue" if parsed.get("accounting_or_trust_issue") else "news_negative_event"
        severity = 80.0 if risk_type == "accounting_or_trust_issue" else 45.0
        return RedTeamFinding(
            symbol=news.symbol or "UNKNOWN",
            as_of_date=news.as_of_date,
            risk_type=risk_type,
            severity=severity,
            is_hard_break=risk_type == "accounting_or_trust_issue",
            description=risk_comment or "negative event surfaced in news",
            evidence_ids=(f"naver-news:{news.symbol or 'UNKNOWN'}:{news.published_at.date().isoformat()}",),
        )


def parse_news_event(*, title: str, body: str = "") -> dict[str, Any]:
    text = f"{title}\n{body}"
    parsed: dict[str, Any] = {}
    if "수주잔고" in text:
        parsed["event_type"] = "backlog"
        parsed["backlog_amount"] = _amount_near(text, "수주잔고")
    if "장기공급" in text or "장기 계약" in text or "장기계약" in text:
        parsed["event_type"] = parsed.get("event_type", "long_term_contract")
    if "단일판매" in text or "공급계약" in text:
        parsed["event_type"] = parsed.get("event_type", "supply_contract")
        amount = _amount_near(text, "계약")
        if amount is not None:
            parsed["contract_amount"] = amount
    if "신규시설투자" in text or "CAPA" in text or "증설" in text:
        parsed["event_type"] = parsed.get("event_type", "capacity_expansion")
        parsed["capa_comment"] = _short_excerpt(text, ("CAPA", "증설", "생산능력"))
        capex = _amount_near(text, "투자")
        if capex is not None:
            parsed["capex_amount"] = capex
    if "컨센서스" in text or "서프라이즈" in text:
        parsed["margin_comment"] = _short_excerpt(text, ("영업이익", "OPM", "마진", "컨센서스"))
    if "목표주가" in text and "상향" in text:
        parsed["event_type"] = parsed.get("event_type", "target_revision")
    if "미국향" in text or "북미" in text:
        parsed["mentioned_region"] = "US/North America"
    if "데이터센터" in text:
        parsed["customer_type"] = "datacenter"
    if "공급부족" in text or "공급 부족" in text:
        parsed["shortage_comment"] = _short_excerpt(text, ("공급부족", "공급 부족", "리드타임"))
    if "ASP" in text or "판가" in text or "가격 상승" in text:
        parsed["asp_comment"] = _short_excerpt(text, ("ASP", "판가", "가격 상승"))
    risk_tokens = ("감사의견", "거래정지", "상장폐지", "소송", "계약 취소", "계약 해지", "회계")
    if any(token in text for token in risk_tokens):
        parsed["risk_comment"] = _short_excerpt(text, risk_tokens)
    product_match = re.search(r"(변압기|전력기기|전선|라면|GPU|서버|진단키트|방산|항공우주)", text)
    if product_match:
        parsed["mentioned_product"] = product_match.group(1)
    return {key: value for key, value in parsed.items() if value is not None}


def _coerce_news_value(key: str, value: Any) -> Any:
    if key in {"contract_amount", "capex_amount", "backlog_amount", "confidence", "source_tier"}:
        return float_or_none(value)
    return value


def _news_confidence(parsed: Mapping[str, Any], body: str | None) -> float:
    field_count = len([key for key in NEWS_PARSED_FIELDS if key in parsed])
    return min(1.0, 0.35 + field_count * 0.06 + (0.15 if body else 0.0))


def _amount_near(text: str, label: str) -> float | None:
    match = re.search(rf"{label}[^\d]*(?P<number>[0-9][0-9,]*(?:\.[0-9]+)?)\s*(?P<unit>조원|억원|억|원|달러)?", text)
    if not match:
        return None
    value = float(match.group("number").replace(",", ""))
    unit = match.group("unit")
    if unit == "조원":
        return value * 1_000_000_000_000.0
    if unit in {"억원", "억"}:
        return value * 100_000_000.0
    return value


def _short_excerpt(text: str, labels: tuple[str, ...]) -> str | None:
    for label in labels:
        index = text.find(label)
        if index >= 0:
            start = max(0, index - 40)
            end = min(len(text), index + 100)
            return text[start:end].replace("\n", " ").strip()
    return None
