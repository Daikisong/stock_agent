"""Research parsing and fixture-first web research utilities."""

from .page_fetcher import FetchResult, PageFetcher
from .pdf_text_extractor import PDFTextExtractionResult, PDFTextExtractor
from .query_planner import QueryPlan, QueryPlanner, QuerySpec
from .report_parser import ReportParseResult, parse_research_report_file, parse_research_report_text
from .search_provider import EmptySearchProvider, FixtureSearchProvider, RequestOnlySearchProvider, SearchResult
from .search_result_ranker import RankedSearchResult, SearchResultRanker
from .web_research_runner import (
    DroppedSearchResult,
    WebResearchInput,
    WebResearchResult,
    WebResearchRunner,
    classify_search_result,
    extract_e2r_text_fields,
)

__all__ = [
    "DroppedSearchResult",
    "EmptySearchProvider",
    "FetchResult",
    "FixtureSearchProvider",
    "PDFTextExtractionResult",
    "PDFTextExtractor",
    "PageFetcher",
    "QueryPlan",
    "QueryPlanner",
    "QuerySpec",
    "RankedSearchResult",
    "ReportParseResult",
    "RequestOnlySearchProvider",
    "SearchResult",
    "SearchResultRanker",
    "WebResearchInput",
    "WebResearchResult",
    "WebResearchRunner",
    "classify_search_result",
    "extract_e2r_text_fields",
    "parse_research_report_file",
    "parse_research_report_text",
]
