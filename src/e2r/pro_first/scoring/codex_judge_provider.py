"""Codex-backed evidence-only Judge provider for Pro-first operation."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping, Protocol

from e2r.research_brain.planning.provider_transport import (
    CodexStructuredProviderTransport,
)


_JUDGE_SCHEMA: Mapping[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "proposed_points",
        "allowed_range",
        "rationale",
        "support_fact_ids",
        "counter_fact_ids",
        "nearest_anchor_ids",
        "anchor_comparisons",
        "disagreements",
        "why_not_higher",
        "why_not_lower",
    ],
    "properties": {
        "proposed_points": {"type": "number", "minimum": 0},
        "allowed_range": {
            "type": "array",
            "minItems": 2,
            "maxItems": 2,
            "items": {"type": "number", "minimum": 0},
        },
        "rationale": {"type": "string", "minLength": 1},
        "support_fact_ids": {
            "type": "array",
            "items": {"type": "string"},
        },
        "counter_fact_ids": {
            "type": "array",
            "items": {"type": "string"},
        },
        "nearest_anchor_ids": {
            "type": "array",
            "items": {"type": "string"},
        },
        "anchor_comparisons": {
            "type": "array",
            "items": {"type": "string"},
        },
        "disagreements": {
            "type": "array",
            "items": {"type": "string"},
        },
        "why_not_higher": {"type": "string", "minLength": 1},
        "why_not_lower": {"type": "string", "minLength": 1},
    },
}


class StructuredJudgeTransport(Protocol):
    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
        schema_name: str,
    ) -> Any: ...


@dataclass
class CodexEvidenceOnlyJudgeProvider:
    """Run one no-search component Judge pass through isolated Codex CLI."""

    transport: StructuredJudgeTransport
    provider_name: str = "CODEX_STRUCTURED_EVIDENCE_ONLY_JUDGE"

    @classmethod
    def default(
        cls,
        *,
        working_directory: str | Path | None = None,
        timeout_seconds: float = 180.0,
    ) -> "CodexEvidenceOnlyJudgeProvider":
        return cls(
            CodexStructuredProviderTransport(
                working_directory=working_directory or Path.cwd(),
                timeout_seconds=timeout_seconds,
            )
        )

    def judge(self, request: Mapping[str, Any]) -> Mapping[str, Any]:
        if request.get("mode") != "EVIDENCE_ONLY_NO_SEARCH":
            raise ValueError("Codex Judge requires evidence-only no-search mode")
        prompt = "\n".join(
            (
                "You are one E2R component Judge.",
                "Use only the supplied verified facts, component memo, historical anchors, and deterministic gap dispositions.",
                "Never browse, fetch a source, calculate a total score, choose a canonical Stage, or treat a Pro-proposed score range as authority.",
                "Cite only fact IDs and anchor IDs present in the request. Keep points and the two-value allowed range within component_memo.component_max_points.",
                "The ANALYST states the strongest source-backed case, the SKEPTIC applies counter evidence and missing bridges, and the CALIBRATION_JUDGE gives the bounded evidence-only calibration.",
                "Return exactly one JSON object matching the schema.",
                json.dumps(request, ensure_ascii=False, sort_keys=True),
            )
        )
        response = self.transport.complete(
            prompt=prompt,
            output_schema=_JUDGE_SCHEMA,
            schema_name="e2r_pro_evidence_only_judge",
        )
        payload = getattr(response, "payload", response)
        if not isinstance(payload, Mapping):
            raise ValueError("Codex Judge transport returned a non-object")
        return dict(payload)


__all__ = ["CodexEvidenceOnlyJudgeProvider", "StructuredJudgeTransport"]
