"""Source collection connectors for E2R 2.0."""

from .consensus import ConsensusCSVConnector
from .http_client import HttpClient, HttpClientStats, HttpResult
from .kind import KINDConnector, KINDRiskRecord
from .krx import KRXConnector
from .naver_news import COMPANY_NEWS_QUERY_TEMPLATES, SECTOR_NEWS_QUERY_TEMPLATES, NaverNewsConnector
from .naver_webdoc import NaverWebDocConnector
from .opendart import DISCLOSURE_PARSED_FIELDS, DISCLOSURE_WATCH_TYPES, OpenDARTConnector
from .report_search import RECOGNIZED_REPORT_DOMAINS, REPORT_QUERY_TEMPLATES, ReportSearchConnector, ReportSearchResult
from .sec_edgar import SECEdgarConnector
from .source_errors import (
    MissingCredentialError,
    SourceConnectorError,
    SourceFixtureNotFoundError,
    SourceRequest,
    SourceResponseError,
)

__all__ = [
    "COMPANY_NEWS_QUERY_TEMPLATES",
    "ConsensusCSVConnector",
    "DISCLOSURE_PARSED_FIELDS",
    "DISCLOSURE_WATCH_TYPES",
    "HttpClient",
    "HttpClientStats",
    "HttpResult",
    "KINDConnector",
    "KINDRiskRecord",
    "KRXConnector",
    "MissingCredentialError",
    "NaverNewsConnector",
    "NaverWebDocConnector",
    "OpenDARTConnector",
    "RECOGNIZED_REPORT_DOMAINS",
    "REPORT_QUERY_TEMPLATES",
    "ReportSearchConnector",
    "ReportSearchResult",
    "SECEdgarConnector",
    "SECTOR_NEWS_QUERY_TEMPLATES",
    "SourceConnectorError",
    "SourceFixtureNotFoundError",
    "SourceRequest",
    "SourceResponseError",
]
