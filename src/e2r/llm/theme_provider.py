"""Provider abstraction for LLM-assisted theme route detection."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Mapping, Protocol

from e2r.llm.prompts import E2R_THEME_ROUTE_SYSTEM_PROMPT
from e2r.llm.theme_schemas import ThemeRouteInput, ThemeRouteOutput


class ThemeRouteProvider(Protocol):
    """Provider contract for route detection and expansion-query suggestions."""

    def route(self, inputs: ThemeRouteInput) -> ThemeRouteOutput | Mapping[str, object]:
        """Return a structured theme route output."""


@dataclass
class FakeThemeRouteProvider:
    """Deterministic provider for tests and fixture-driven runs."""

    output: ThemeRouteOutput | Mapping[str, object] | None = None
    outputs: list[ThemeRouteOutput | Mapping[str, object]] = field(default_factory=list)
    calls: list[ThemeRouteInput] = field(default_factory=list)

    def route(self, inputs: ThemeRouteInput) -> ThemeRouteOutput | Mapping[str, object]:
        self.calls.append(inputs)
        if self.outputs:
            return self.outputs.pop(0)
        if self.output is not None:
            return self.output
        return ThemeRouteOutput(status="no_transition")


def build_theme_route_messages(inputs: ThemeRouteInput) -> tuple[Mapping[str, str], Mapping[str, str]]:
    """Build guarded chat-style messages for a real theme route LLM provider."""

    payload = asdict(inputs)
    payload["as_of_date"] = inputs.as_of_date.isoformat()
    return (
        {"role": "system", "content": E2R_THEME_ROUTE_SYSTEM_PROMPT},
        {"role": "user", "content": json.dumps(payload, ensure_ascii=False, sort_keys=True)},
    )


__all__ = ["FakeThemeRouteProvider", "ThemeRouteProvider", "build_theme_route_messages"]
