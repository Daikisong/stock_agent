"""Optional LLM analyst layer for E2R evidence review."""

from e2r.llm.codex_theme_provider import CodexCLIThemeRouteProvider, build_theme_route_provider_from_env
from e2r.llm.provider import FakeLLMProvider, LLMProvider
from e2r.llm.research_analyst import LLMResearchAnalyst
from e2r.llm.schemas import LLMAnalystInput, LLMAnalystOutput
from e2r.llm.theme_provider import FakeThemeRouteProvider, ThemeRouteProvider, build_theme_route_messages
from e2r.llm.theme_router import LLMThemeRebalanceAgent
from e2r.llm.theme_schemas import (
    EvidenceSlotStatus,
    ThemeRouteDocument,
    ThemeRouteInput,
    ThemeRouteOutput,
    ThemeRouteSearchResult,
    route_diagnostics,
    validate_theme_route_output,
)

__all__ = [
    "CodexCLIThemeRouteProvider",
    "EvidenceSlotStatus",
    "FakeLLMProvider",
    "FakeThemeRouteProvider",
    "LLMThemeRebalanceAgent",
    "LLMAnalystInput",
    "LLMAnalystOutput",
    "LLMProvider",
    "LLMResearchAnalyst",
    "ThemeRouteDocument",
    "ThemeRouteInput",
    "ThemeRouteOutput",
    "ThemeRouteProvider",
    "ThemeRouteSearchResult",
    "build_theme_route_provider_from_env",
    "build_theme_route_messages",
    "route_diagnostics",
    "validate_theme_route_output",
]
