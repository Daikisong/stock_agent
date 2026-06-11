"""Guarded LLM theme route agent."""

from __future__ import annotations

from e2r.llm.theme_provider import ThemeRouteProvider
from e2r.llm.theme_schemas import ThemeRouteInput, ThemeRouteOutput, validate_theme_route_output


class LLMThemeRebalanceAgent:
    """Ask an LLM provider for a route, then strip unsafe fields."""

    def __init__(self, provider: ThemeRouteProvider) -> None:
        self._provider = provider

    def route(self, inputs: ThemeRouteInput) -> ThemeRouteOutput:
        try:
            raw = self._provider.route(inputs)
        except Exception as exc:  # pragma: no cover - provider-specific failures
            return ThemeRouteOutput(status="provider_error", blocked_reason=str(exc)[:200])
        return validate_theme_route_output(raw)


__all__ = ["LLMThemeRebalanceAgent"]
