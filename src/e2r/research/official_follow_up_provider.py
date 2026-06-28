"""Official connector backed follow-up search provider."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.models import ConsensusRevision, ConsensusSnapshot, DisclosureEvent, FinancialActual, Market, NewsItem, ResearchReport
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_provider import SearchResult
from e2r.sources.kind import KINDRiskRecord


@dataclass
class CompositeFollowUpSourceProvider:
    """Merge multiple scoped follow-up providers without broadening queries."""

    providers: Sequence[Any]

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        rows: list[SearchResult] = []
        for provider in self.providers:
            if provider is None or not hasattr(provider, "search"):
                continue
            try:
                rows.extend(provider.search(query, as_of_date, max_results))
            except Exception:
                continue
        deduped: dict[str, SearchResult] = {}
        for item in rows:
            deduped.setdefault(item.url, item)
        selected = sorted(
            deduped.values(),
            key=lambda item: (-(item.confidence or 0.0), item.rank or 9999, item.url),
        )[:max_results]
        return tuple(
            SearchResult(
                title=item.title,
                url=item.url,
                snippet=item.snippet,
                source=item.source,
                published_at=item.published_at,
                query=query,
                rank=index,
                is_pdf=item.is_pdf,
                is_report_domain=item.is_report_domain,
                is_news=item.is_news,
                is_disclosure=item.is_disclosure,
                confidence=item.confidence,
                date_verified=item.date_verified,
                green_allowed_by_date=item.green_allowed_by_date,
            )
            for index, item in enumerate(selected, start=1)
        )

    def fixture_text_by_url(self) -> Mapping[str, str | Path]:
        merged: dict[str, str | Path] = {}
        for provider in self.providers:
            if provider is None or not hasattr(provider, "fixture_text_by_url"):
                continue
            value = getattr(provider, "fixture_text_by_url")
            if not callable(value):
                continue
            try:
                mapping = value()
            except Exception:
                continue
            if isinstance(mapping, Mapping):
                merged.update({str(url): text for url, text in mapping.items() if str(url).strip()})
        return merged


@dataclass
class FeatureInputFollowUpSourceProvider:
    """Expose already collected FeatureEngineeringInput evidence as sources."""

    feature_input: Any
    market: Market = Market.KR
    _fixture_text_by_url: dict[str, str | Path] = field(default_factory=dict, init=False, repr=False)

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        if max_results <= 0:
            return ()
        rows = [row for row in self._rows(query=query, as_of_date=as_of_date) if row[1].date() <= as_of_date]
        rows.sort(key=lambda item: (-item[0], -item[1].timestamp(), item[2].rank, item[2].url))
        selected: list[SearchResult] = []
        for index, (_, _, result, text) in enumerate(rows[:max_results], start=1):
            ranked = SearchResult(
                title=result.title,
                url=result.url,
                snippet=result.snippet,
                source=result.source,
                published_at=result.published_at,
                query=query,
                rank=index,
                is_pdf=result.is_pdf,
                is_report_domain=result.is_report_domain,
                is_news=result.is_news,
                is_disclosure=result.is_disclosure,
                confidence=result.confidence,
                date_verified=True,
                green_allowed_by_date=True,
            )
            self._fixture_text_by_url[ranked.url] = text
            selected.append(ranked)
        return tuple(selected)

    def fixture_text_by_url(self) -> Mapping[str, str | Path]:
        return dict(self._fixture_text_by_url)

    def _rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str], ...]:
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        rows.extend(self._financial_actual_rows(query=query, as_of_date=as_of_date))
        rows.extend(self._consensus_rows(query=query, as_of_date=as_of_date))
        rows.extend(self._consensus_revision_rows(query=query, as_of_date=as_of_date))
        rows.extend(self._disclosure_rows(query=query, as_of_date=as_of_date))
        rows.extend(self._research_report_rows(query=query, as_of_date=as_of_date))
        rows.extend(self._news_rows(query=query, as_of_date=as_of_date))
        return tuple(rows)

    def _financial_actual_rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str], ...]:
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        for index, item in enumerate(tuple(getattr(self.feature_input, "financial_actuals", ())), start=1):
            if not isinstance(item, FinancialActual) or item.reported_at.date() > as_of_date:
                continue
            url = f"feature://{item.symbol}/financial_actual/{item.period_end.isoformat()}"
            text = _financial_actual_text(item)
            rows.append((_query_overlap(query, f"{url} {text}"), item.reported_at, _feature_result(
                title=f"{item.source} financial actual {item.period_end.isoformat()}",
                url=url,
                text=text,
                source=item.source,
                published_at=item.reported_at,
                query=query,
                rank=index,
                is_disclosure=True,
            ), text))
        return tuple(rows)

    def _consensus_rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str], ...]:
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        for index, item in enumerate(tuple(getattr(self.feature_input, "consensus", ())), start=1):
            if not isinstance(item, ConsensusSnapshot) or item.date > as_of_date:
                continue
            url = f"feature://{item.symbol}/consensus/{item.date.isoformat()}/{item.fiscal_year}"
            text = _consensus_text(item)
            published = _day_start(item.date)
            rows.append((_query_overlap(query, f"{url} {text}"), published, _feature_result(
                title=f"{item.source} consensus FY{item.fiscal_year}",
                url=url,
                text=text,
                source=item.source,
                published_at=published,
                query=query,
                rank=index,
                is_report_domain=True,
            ), text))
        return tuple(rows)

    def _consensus_revision_rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str], ...]:
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        for index, item in enumerate(tuple(getattr(self.feature_input, "consensus_revisions", ())), start=1):
            if not isinstance(item, ConsensusRevision) or item.date > as_of_date:
                continue
            url = f"feature://{item.symbol}/consensus_revision/{item.date.isoformat()}/{item.fiscal_year}"
            text = _consensus_revision_text(item)
            published = _day_start(item.date)
            rows.append((_query_overlap(query, f"{url} {text}"), published, _feature_result(
                title=f"{item.source} consensus revision FY{item.fiscal_year}",
                url=url,
                text=text,
                source=item.source,
                published_at=published,
                query=query,
                rank=index,
                is_report_domain=True,
            ), text))
        return tuple(rows)

    def _disclosure_rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str], ...]:
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        for index, item in enumerate(tuple(getattr(self.feature_input, "disclosures", ())), start=1):
            if not isinstance(item, DisclosureEvent) or item.available_at.date() > as_of_date:
                continue
            url = f"feature://{item.symbol}/disclosure/{item.rcept_no or item.published_at.date().isoformat()}"
            text = _disclosure_text(item)
            rows.append((_query_overlap(query, f"{url} {text}"), item.published_at, _feature_result(
                title=item.title,
                url=url,
                text=text,
                source=item.source,
                published_at=item.published_at,
                query=query,
                rank=index,
                is_disclosure=True,
            ), text))
        return tuple(rows)

    def _research_report_rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str], ...]:
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        for index, item in enumerate(tuple(getattr(self.feature_input, "research_reports", ())), start=1):
            if not isinstance(item, ResearchReport) or item.publish_date > as_of_date:
                continue
            url = f"feature://{item.symbol}/research_report/{item.broker}/{item.publish_date.isoformat()}/{index}"
            text = _research_report_text(item)
            published = _day_start(item.publish_date)
            rows.append((_query_overlap(query, f"{url} {text}"), published, _feature_result(
                title=item.title,
                url=url,
                text=text,
                source=item.broker,
                published_at=published,
                query=query,
                rank=index,
                is_report_domain=True,
                confidence=0.9,
            ), text))
        return tuple(rows)

    def _news_rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str], ...]:
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        for index, item in enumerate(tuple(getattr(self.feature_input, "news_items", ())), start=1):
            if not isinstance(item, NewsItem) or item.published_at.date() > as_of_date:
                continue
            symbol = item.symbol or getattr(self.feature_input, "symbol", "unknown")
            url = f"feature://{symbol}/news/{item.source}/{item.published_at.date().isoformat()}/{index}"
            text = _news_text(item)
            rows.append((_query_overlap(query, f"{url} {text}"), item.published_at, _feature_result(
                title=item.title,
                url=url,
                text=text,
                source=item.source,
                published_at=item.published_at,
                query=query,
                rank=index,
                is_news=True,
                confidence=0.82,
            ), text))
        return tuple(rows)


@dataclass
class OpenDARTDetailFollowUpSourceProvider:
    """Expose already fetched OpenDART document.xml detail bodies.

    Detail fetching remains owned by the live pipeline budget. This adapter
    only makes the bounded, already fetched full-document rows available to
    the agentic follow-up loop before it falls back to broad web search.
    """

    symbol: str
    company_name: str
    detail_disclosures: Sequence[DisclosureEvent]
    market: Market = Market.KR
    _fixture_text_by_url: dict[str, str | Path] = field(default_factory=dict, init=False, repr=False)

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        if max_results <= 0:
            return ()
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        for index, item in enumerate(self.detail_disclosures, start=1):
            if not isinstance(item, DisclosureEvent) or item.symbol != self.symbol:
                continue
            if not _is_opendart_detail_event(item) or item.available_at.date() > as_of_date:
                continue
            text = _disclosure_text(item)
            result = SearchResult(
                title=item.title,
                url=_disclosure_source_url(self.symbol, item),
                snippet=text[:240],
                source=item.source,
                published_at=item.published_at,
                query=query,
                rank=index,
                is_disclosure=True,
                confidence=0.98,
                date_verified=True,
                green_allowed_by_date=True,
            )
            rows.append((_query_overlap(query, f"{result.title} {text}"), item.published_at, result, text))
        rows.sort(key=lambda item: (-item[0], -item[1].timestamp(), item[2].rank, item[2].url))
        selected: list[SearchResult] = []
        for index, (_, _, result, text) in enumerate(rows[:max_results], start=1):
            ranked = SearchResult(
                title=result.title,
                url=result.url,
                snippet=result.snippet,
                source=result.source,
                published_at=result.published_at,
                query=query,
                rank=index,
                is_pdf=result.is_pdf,
                is_report_domain=result.is_report_domain,
                is_news=result.is_news,
                is_disclosure=result.is_disclosure,
                confidence=result.confidence,
                date_verified=True,
                green_allowed_by_date=True,
            )
            self._fixture_text_by_url[ranked.url] = text
            selected.append(ranked)
        return tuple(selected)

    def fixture_text_by_url(self) -> Mapping[str, str | Path]:
        return dict(self._fixture_text_by_url)


@dataclass
class ReportDocumentFollowUpSourceProvider:
    """Expose point-in-time report/IR document text as follow-up sources."""

    symbol: str
    company_name: str
    market: Market = Market.KR
    snapshot_store: Any | None = None
    report_connectors: Sequence[Any] = ()
    _fixture_text_by_url: dict[str, str | Path] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        if self.snapshot_store is None:
            self.snapshot_store = ReportSnapshotStore()
        object.__setattr__(self, "report_connectors", tuple(self.report_connectors))

    def has_sources(self, as_of_date: date) -> bool:
        return bool(self._snapshot_rows(query="", as_of_date=as_of_date) or self._connector_rows(query="", as_of_date=as_of_date))

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        if max_results <= 0:
            return ()
        rows = list(self._snapshot_rows(query=query, as_of_date=as_of_date))
        rows.extend(self._connector_rows(query=query, as_of_date=as_of_date))
        rows.sort(key=lambda item: (-item[0], -item[1].timestamp(), item[2].rank, item[2].url))
        selected: list[SearchResult] = []
        for index, (_, _, result, text) in enumerate(rows[:max_results], start=1):
            ranked = SearchResult(
                title=result.title,
                url=result.url,
                snippet=result.snippet,
                source=result.source,
                published_at=result.published_at,
                query=query,
                rank=index,
                is_pdf=result.is_pdf,
                is_report_domain=result.is_report_domain,
                is_news=result.is_news,
                is_disclosure=result.is_disclosure,
                confidence=result.confidence,
                date_verified=result.date_verified,
                green_allowed_by_date=result.green_allowed_by_date,
            )
            if text:
                self._fixture_text_by_url[ranked.url] = text
            selected.append(ranked)
        return tuple(selected)

    def fixture_text_by_url(self) -> Mapping[str, str | Path]:
        return dict(self._fixture_text_by_url)

    def _snapshot_rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str | Path], ...]:
        store = self.snapshot_store
        if store is None or not hasattr(store, "load_snapshots"):
            return ()
        try:
            snapshots = tuple(store.load_snapshots(as_of_date=as_of_date, symbol=self.symbol))
            snapshots += tuple(store.load_snapshots(as_of_date=as_of_date, company_name=self.company_name))
        except Exception:
            return ()
        by_url: dict[str, Any] = {}
        for item in snapshots:
            if item.as_of_date > as_of_date:
                continue
            if item.symbol not in (None, self.symbol) and item.company_name not in (None, self.company_name):
                continue
            by_url.setdefault(str(item.url), item)
        rows: list[tuple[int, datetime, SearchResult, str | Path]] = []
        for index, item in enumerate(by_url.values(), start=1):
            text_ref = _snapshot_text_reference(store, item)
            if text_ref is None:
                continue
            published = _day_start(item.as_of_date)
            title = str(item.title or item.url)
            result = SearchResult(
                title=title,
                url=str(item.url),
                snippet=title,
                source=str(item.source_type or "report_snapshot"),
                published_at=published,
                query=query,
                rank=index,
                is_pdf=str(item.url).lower().split("?")[0].endswith(".pdf"),
                is_report_domain=True,
                confidence=0.92,
                date_verified=True,
                green_allowed_by_date=True,
            )
            haystack = f"{title} {item.url}"
            rows.append((_query_overlap(query, haystack), published, result, text_ref))
        return tuple(rows)

    def _connector_rows(self, *, query: str, as_of_date: date) -> tuple[tuple[int, datetime, SearchResult, str | Path], ...]:
        rows: list[tuple[int, datetime, SearchResult, str | Path]] = []
        for connector in self.report_connectors:
            if connector is None or not hasattr(connector, "search_reports"):
                continue
            try:
                reports = tuple(connector.search_reports(self.company_name, as_of_date))
            except Exception:
                continue
            for index, item in enumerate(reports, start=1):
                publish_date = getattr(item, "publish_date", None)
                if publish_date is not None and publish_date > as_of_date:
                    continue
                text = _download_report_text(connector, item)
                published = _day_start(publish_date or as_of_date)
                title = str(getattr(item, "title", "") or getattr(item, "url", "report"))
                url = str(getattr(item, "url", ""))
                if not url:
                    continue
                result = SearchResult(
                    title=title,
                    url=url,
                    snippet=str(getattr(item, "snippet", "") or title)[:240],
                    source=str(getattr(item, "source", "") or "report_search"),
                    published_at=published,
                    query=query,
                    rank=index,
                    is_pdf=bool(getattr(item, "is_pdf", False)),
                    is_report_domain=bool(getattr(item, "is_recognized_report_domain", False)),
                    confidence=0.86 if text else 0.72,
                    date_verified=publish_date is not None,
                    green_allowed_by_date=publish_date is not None,
                )
                haystack = f"{title} {url} {getattr(item, 'snippet', '')}"
                rows.append((_query_overlap(query, haystack), published, result, text or ""))
        return tuple(rows)


@dataclass
class KoreaOfficialFollowUpSourceProvider:
    """Expose DART/KIND official connector rows as bounded follow-up sources.

    The provider does not synthesize queries. It only responds to an LLM-created
    follow-up query by returning official records for the scoped symbol that
    were available by the requested as-of date.
    """

    symbol: str
    company_name: str
    market: Market = Market.KR
    opendart: Any | None = None
    kind: Any | None = None
    lookback_days: int = 756
    _fixture_text_by_url: dict[str, str | Path] = field(default_factory=dict, init=False, repr=False)

    def search(self, query: str, as_of_date: date, max_results: int = 100) -> tuple[SearchResult, ...]:
        if max_results <= 0:
            return ()
        rows: list[tuple[int, datetime, SearchResult, str]] = []
        for result, text in self._disclosure_results(query=query, as_of_date=as_of_date):
            rows.append((_query_overlap(query, f"{result.title} {text}"), result.published_at or _day_start(as_of_date), result, text))
        for result, text in self._financial_actual_results(query=query, as_of_date=as_of_date):
            rows.append((_query_overlap(query, f"{result.title} {text}"), result.published_at or _day_start(as_of_date), result, text))
        for result, text in self._kind_results(query=query, as_of_date=as_of_date):
            rows.append((_query_overlap(query, f"{result.title} {text}"), result.published_at or _day_start(as_of_date), result, text))

        rows.sort(key=lambda item: (-item[0], -item[1].timestamp(), item[2].rank, item[2].url))
        selected: list[SearchResult] = []
        for index, (_, _, result, text) in enumerate(rows[:max_results], start=1):
            ranked = SearchResult(
                title=result.title,
                url=result.url,
                snippet=result.snippet,
                source=result.source,
                published_at=result.published_at,
                query=query,
                rank=index,
                is_pdf=result.is_pdf,
                is_report_domain=result.is_report_domain,
                is_news=result.is_news,
                is_disclosure=result.is_disclosure,
                confidence=result.confidence,
                date_verified=True,
                green_allowed_by_date=True,
            )
            self._fixture_text_by_url[ranked.url] = text
            selected.append(ranked)
        return tuple(selected)

    def fixture_text_by_url(self) -> Mapping[str, str | Path]:
        return dict(self._fixture_text_by_url)

    def _disclosure_results(self, *, query: str, as_of_date: date) -> tuple[tuple[SearchResult, str], ...]:
        if self.opendart is None or not hasattr(self.opendart, "get_disclosures"):
            return ()
        start = as_of_date - timedelta(days=max(self.lookback_days, 0))
        try:
            disclosures = tuple(self.opendart.get_disclosures(self.symbol, start, as_of_date, as_of_date))
        except Exception:
            return ()
        rows: list[tuple[SearchResult, str]] = []
        for index, item in enumerate(disclosures, start=1):
            if item.available_at.date() > as_of_date:
                continue
            if _is_follow_up_disclosure_noise(item):
                continue
            url = _disclosure_source_url(self.symbol, item)
            text = _disclosure_text(item)
            rows.append(
                (
                    SearchResult(
                        title=item.title,
                        url=url,
                        snippet=text[:240],
                        source=item.source,
                        published_at=item.published_at,
                        query=query,
                        rank=index,
                        is_disclosure=True,
                        confidence=0.98 if _is_opendart_detail_event(item) else 0.95,
                        date_verified=True,
                        green_allowed_by_date=True,
                    ),
                    text,
                )
            )
        return tuple(rows)

    def _financial_actual_results(self, *, query: str, as_of_date: date) -> tuple[tuple[SearchResult, str], ...]:
        if self.opendart is None or not hasattr(self.opendart, "get_financial_actuals"):
            return ()
        try:
            actuals = tuple(self.opendart.get_financial_actuals(self.symbol, as_of_date))
        except Exception:
            return ()
        rows: list[tuple[SearchResult, str]] = []
        for index, item in enumerate(actuals, start=1):
            if item.reported_at.date() > as_of_date:
                continue
            url = f"opendart://{self.symbol}/financial_actual/{item.period_end.isoformat()}"
            text = _financial_actual_text(item)
            rows.append(
                (
                    SearchResult(
                        title=f"OpenDART financial actual {item.period_end.isoformat()}",
                        url=url,
                        snippet=text[:240],
                        source=item.source,
                        published_at=item.reported_at,
                        query=query,
                        rank=index,
                        is_disclosure=True,
                        confidence=0.95,
                        date_verified=True,
                        green_allowed_by_date=True,
                    ),
                    text,
                )
            )
        return tuple(rows)

    def _kind_results(self, *, query: str, as_of_date: date) -> tuple[tuple[SearchResult, str], ...]:
        if self.kind is None or not hasattr(self.kind, "get_risk_records"):
            return ()
        try:
            records = tuple(self.kind.get_risk_records(self.symbol, as_of_date))
        except Exception:
            return ()
        rows: list[tuple[SearchResult, str]] = []
        for index, item in enumerate(records, start=1):
            if item.as_of_date > as_of_date:
                continue
            published = item.published_at if isinstance(item.published_at, datetime) else _day_start(item.as_of_date)
            url = f"kind://{self.symbol}/risk_status/{item.as_of_date.isoformat()}"
            text = _kind_text(item)
            rows.append(
                (
                    SearchResult(
                        title=item.title,
                        url=url,
                        snippet=text[:240],
                        source=item.source,
                        published_at=published,
                        query=query,
                        rank=index,
                        is_disclosure=True,
                        confidence=0.95,
                        date_verified=True,
                        green_allowed_by_date=True,
                    ),
                    text,
                )
            )
        return tuple(rows)


def _disclosure_text(item: DisclosureEvent) -> str:
    parts = [item.title, item.report_type, item.raw_text or ""]
    parts.extend(
        f"{key}: {value}"
        for key, value in sorted((item.parsed_fields or {}).items())
        if value not in (None, "") and key not in _DISCLOSURE_TEXT_EXCLUDED_FIELDS
    )
    return "\n".join(str(part).strip() for part in parts if str(part).strip())


_DISCLOSURE_TEXT_EXCLUDED_FIELDS = frozenset(
    {
        "opendart_corp_code",
        "opendart_corp_name",
        "opendart_corp_class",
        "watch_type",
        "signal_class",
        "parser_confidence",
        "raw_document_format",
    }
)


_FOLLOW_UP_DISCLOSURE_NOISE_TOKENS = (
    "임원ㆍ주요주주",
    "임원·주요주주",
    "주식등의대량보유",
    "대량보유상황보고서",
    "특정증권등소유상황보고서",
)


def _is_follow_up_disclosure_noise(item: DisclosureEvent) -> bool:
    haystack = f"{item.title} {item.report_type}".strip()
    return any(token in haystack for token in _FOLLOW_UP_DISCLOSURE_NOISE_TOKENS)


def _is_opendart_detail_event(item: DisclosureEvent) -> bool:
    return str(item.source).strip().lower() == "opendart detail" or bool((item.parsed_fields or {}).get("detail_fetched"))


def _disclosure_source_url(symbol: str, item: DisclosureEvent) -> str:
    scheme = "opendart-detail" if _is_opendart_detail_event(item) else "opendart"
    receipt = item.rcept_no or item.published_at.date().isoformat()
    return f"{scheme}://{symbol}/{receipt}"


def _snapshot_text_reference(store: Any, snapshot: Any) -> str | Path | None:
    extracted_path = getattr(snapshot, "extracted_text_path", None)
    if not extracted_path:
        return None
    path = Path(extracted_path)
    if not path.is_absolute():
        path = Path(getattr(store, "root", ".")) / path
    return path if path.exists() else None


def _download_report_text(connector: Any, item: Any) -> str | None:
    if not hasattr(connector, "download_report_text"):
        return None
    try:
        text = connector.download_report_text(item)
    except Exception:
        return None
    return str(text) if text else None


def _financial_actual_text(item: FinancialActual) -> str:
    fields = {
        "cashflow_from_operations": item.cashflow_from_operations,
        "capex": item.capex,
        "fcf": item.fcf,
        "sales": item.sales,
        "operating_profit": item.operating_profit,
        "net_income": item.net_income,
        "eps": item.eps,
        "period_end": item.period_end.isoformat(),
        "reported_at": item.reported_at.date().isoformat(),
    }
    return "\n".join(f"{key}: {value}" for key, value in fields.items() if value not in (None, ""))


def _consensus_text(item: ConsensusSnapshot) -> str:
    fields = {
        "sales_e": item.sales_e,
        "op_e": item.op_e,
        "net_income_e": item.net_income_e,
        "eps_e": item.eps_e,
        "fcf_e": item.fcf_e,
        "roe_e": item.roe_e,
        "per_e": item.per_e,
        "pbr_e": item.pbr_e,
        "analyst_count": item.analyst_count,
        "target_price": item.target_price,
        "date": item.date.isoformat(),
        "fiscal_year": item.fiscal_year,
        **dict(item.parsed_fields or {}),
    }
    return "\n".join(f"{key}: {value}" for key, value in fields.items() if value not in (None, ""))


def _consensus_revision_text(item: ConsensusRevision) -> str:
    fields = {
        "eps_revision_1w": item.eps_revision_1w,
        "eps_revision_1m": item.eps_revision_1m,
        "eps_revision_3m": item.eps_revision_3m,
        "op_revision_1w": item.op_revision_1w,
        "op_revision_1m": item.op_revision_1m,
        "op_revision_3m": item.op_revision_3m,
        "fcf_revision_1m": item.fcf_revision_1m,
        "target_price_revision_1m": item.target_price_revision_1m,
        "analyst_count_change": item.analyst_count_change,
        "date": item.date.isoformat(),
        "fiscal_year": item.fiscal_year,
        **dict(item.parsed_fields or {}),
    }
    return "\n".join(f"{key}: {value}" for key, value in fields.items() if value not in (None, ""))


def _research_report_text(item: ResearchReport) -> str:
    fields = {
        "title": item.title,
        "broker": item.broker,
        "analyst": item.analyst,
        "target_price": item.target_price,
        "rating": item.rating,
        "target_revision_pct": item.target_revision_pct,
        "fy1_sales": item.fy1_sales,
        "fy1_op": item.fy1_op,
        "fy1_eps": item.fy1_eps,
        "fy2_sales": item.fy2_sales,
        "fy2_op": item.fy2_op,
        "fy2_eps": item.fy2_eps,
        "est_per": item.est_per,
        "est_pbr": item.est_pbr,
        "roe": item.roe,
        "opm": item.opm,
        "backlog": item.backlog,
        "new_orders": item.new_orders,
        "order_backlog_to_sales": item.order_backlog_to_sales,
        "investment_points": " | ".join(item.investment_points),
        "risk_points": " | ".join(item.risk_points),
        "raw_text": item.raw_text,
        **dict(item.parsed_fields or {}),
    }
    return "\n".join(f"{key}: {value}" for key, value in fields.items() if value not in (None, ""))


def _news_text(item: NewsItem) -> str:
    fields = {
        "title": item.title,
        "source": item.source,
        "sector": item.sector,
        "published_at": item.published_at.date().isoformat(),
        "body": item.body,
        "theme_tags": " | ".join(item.theme_tags),
        "sentiment": item.sentiment,
        **dict(item.parsed_fields or {}),
    }
    return "\n".join(f"{key}: {value}" for key, value in fields.items() if value not in (None, ""))


def _kind_text(item: KINDRiskRecord) -> str:
    fields = {
        "managed_issue": item.managed_issue,
        "investment_warning": item.investment_warning,
        "trading_halt": item.trading_halt,
        "unfaithful_disclosure": item.unfaithful_disclosure,
        "delisting_risk": item.delisting_risk,
        "investor_caution": item.investor_caution,
        **dict(item.parsed_fields or {}),
    }
    return "\n".join(f"{key}: {value}" for key, value in fields.items() if value not in (None, ""))


def _query_overlap(query: str, text: str) -> int:
    query_tokens = set(_tokens(query))
    if not query_tokens:
        return 0
    text_tokens = set(_tokens(text))
    return len(query_tokens & text_tokens)


def _tokens(text: str) -> tuple[str, ...]:
    return tuple(token for token in "".join(char.lower() if char.isalnum() else " " for char in text).split() if len(token) >= 2)


def _day_start(value: date) -> datetime:
    return datetime(value.year, value.month, value.day, 8, 0)


def _feature_result(
    *,
    title: str,
    url: str,
    text: str,
    source: str,
    published_at: datetime,
    query: str,
    rank: int,
    is_report_domain: bool = False,
    is_news: bool = False,
    is_disclosure: bool = False,
    confidence: float = 0.9,
) -> SearchResult:
    return SearchResult(
        title=title,
        url=url,
        snippet=text[:240],
        source=source,
        published_at=published_at,
        query=query,
        rank=rank,
        is_report_domain=is_report_domain,
        is_news=is_news,
        is_disclosure=is_disclosure,
        confidence=confidence,
        date_verified=True,
        green_allowed_by_date=True,
    )


__all__ = [
    "CompositeFollowUpSourceProvider",
    "FeatureInputFollowUpSourceProvider",
    "KoreaOfficialFollowUpSourceProvider",
    "OpenDARTDetailFollowUpSourceProvider",
    "ReportDocumentFollowUpSourceProvider",
]
