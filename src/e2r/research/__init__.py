"""Research parsing and fixture-first web research utilities."""

from .browser_search_provider import BrowserSearchProvider
from .free_web_research_runner import FreeWebResearchInput, FreeWebResearchRunner, SkippedQuery, WebResearchPipelineResult
from .manual_source_provider import ManualSource, ManualSourceProvider
from .naver_search_provider import NaverFreeSearchProvider
from .page_fetcher import FetchResult, PageFetcher
from .pdf_text_extractor import PDFTextExtractionResult, PDFTextExtractor
from .query_planner import QueryPlan, QueryPlanner, QuerySpec
from .report_parser import ReportParseResult, parse_research_report_file, parse_research_report_text
from .search_budget import ResearchLayer, SearchBudget, SearchBudgetDecision, SearchBudgetTracker
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
    "BrowserSearchProvider",
    "DroppedSearchResult",
    "EmptySearchProvider",
    "FetchResult",
    "FixtureSearchProvider",
    "FreeWebResearchInput",
    "FreeWebResearchRunner",
    "ManualSource",
    "ManualSourceProvider",
    "NaverFreeSearchProvider",
    "PDFTextExtractionResult",
    "PDFTextExtractor",
    "PageFetcher",
    "QueryPlan",
    "QueryPlanner",
    "QuerySpec",
    "RankedSearchResult",
    "ResearchLayer",
    "ReportParseResult",
    "RequestOnlySearchProvider",
    "SearchBudget",
    "SearchBudgetDecision",
    "SearchBudgetTracker",
    "SearchResult",
    "SearchResultRanker",
    "SkippedQuery",
    "WebResearchInput",
    "WebResearchPipelineResult",
    "WebResearchResult",
    "WebResearchRunner",
    "classify_search_result",
    "extract_e2r_text_fields",
    "parse_research_report_file",
    "parse_research_report_text",
]
