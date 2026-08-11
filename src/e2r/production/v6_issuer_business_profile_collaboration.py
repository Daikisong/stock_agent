"""Codex Collaboration adapter for Phase-105 issuer profile classification.

The official profile materializer owns KRX/OpenDART fetching and deterministic
validation.  This adapter owns only the asynchronous Collaboration journal
boundary: the first call writes an exact request and returns the ordinary
``StructuredProviderUnavailable`` pending signal; a later replay consumes only
an imported, schema-validated response.

It deliberately exposes no score or Stage API and has no local-model fallback.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexSubagentTransport,
)

from .v6_issuer_business_profile import (
    CANONICAL_COMPATIBILITY_PROVIDER,
    CompatibilityProviderCompletion,
)


_SCHEMA_NAME = "e2r_v5_issuer_business_profile_compatibility"


@dataclass
class CollaborationIssuerBusinessCompatibilityProvider:
    """Journal-backed, score-blind compatibility provider.

    ``journal_root`` must be selected by the operational caller.  The canonical
    CLI pins it below the current live-materialization root; keeping the adapter
    path-agnostic also makes its request/replay contract testable without a live
    provider call.
    """

    journal_root: Path
    transport: CollaborationCodexSubagentTransport = field(
        default_factory=CollaborationCodexSubagentTransport
    )
    provider_name: str = CANONICAL_COMPATIBILITY_PROVIDER
    real_provider: bool = True
    fake_provider: bool = False

    def __post_init__(self) -> None:
        self.journal_root = Path(self.journal_root)
        self.transport.configure_journal_root(self.journal_root)

    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
    ) -> CompatibilityProviderCompletion:
        completion = self.transport.complete(
            prompt=prompt,
            output_schema=output_schema,
            schema_name=_SCHEMA_NAME,
        )
        return CompatibilityProviderCompletion(
            payload=dict(completion.payload),
            raw_response=str(completion.raw_response),
        )


__all__ = ["CollaborationIssuerBusinessCompatibilityProvider"]
