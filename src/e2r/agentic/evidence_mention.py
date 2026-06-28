"""Quarantine layer for legacy parser outputs.

EvidenceMention is deliberately weaker than RawAssertion or AdjudicatedClaim.
It records that an upstream parser noticed a field, but it is never score
admissible by itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
from typing import Any, Mapping


EVIDENCE_MENTION_SCHEMA_VERSION = "e2r-evidence-mention-v1"
V2_SCORE_ELIGIBLE_CLAIMS_KEY = "evidence_os_v2_score_eligible_claim_ids_by_primitive"
V2_HARD_BREAK_SOURCE_QUORUM_KEY = "evidence_os_v2_hard_break_source_quorum_by_primitive"

MENTION_METADATA_KEYS = frozenset(
    {
        "agent_extracted_field_source",
        "claim_ledger_version",
        "compiled_claim_ids",
        "compiled_claim_ids_by_primitive",
        "compiled_primitive_states",
        V2_HARD_BREAK_SOURCE_QUORUM_KEY,
        V2_SCORE_ELIGIBLE_CLAIMS_KEY,
    }
)


class MentionSourceKind(str, Enum):
    LEGACY_PARSER_FIELD = "LEGACY_PARSER_FIELD"
    LEGACY_AGENT_FIELD = "LEGACY_AGENT_FIELD"
    STRUCTURED_CONNECTOR_FIELD = "STRUCTURED_CONNECTOR_FIELD"
    SEARCH_SNIPPET = "SEARCH_SNIPPET"


@dataclass(frozen=True)
class EvidenceMention:
    """A non-scoring observation from a parser or connector."""

    mention_id: str
    evidence_id: str
    source_kind: MentionSourceKind
    field_name: str
    raw_value: Any
    document_id: str | None = None
    source_url: str | None = None
    text_hint: str = ""
    subject_hint: str | None = None
    schema_version: str = EVIDENCE_MENTION_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if not self.mention_id.strip():
            raise ValueError("mention_id must be non-empty")
        if not self.evidence_id.strip():
            raise ValueError("evidence_id must be non-empty")
        if not self.field_name.strip():
            raise ValueError("field_name must be non-empty")

    def score_admissible(self) -> bool:
        """Mentions are never direct score inputs."""

        return False


def mentions_from_parsed_fields(
    *,
    evidence_id: str,
    parsed_fields: Mapping[str, Any],
    source_kind: MentionSourceKind | str = MentionSourceKind.LEGACY_PARSER_FIELD,
    document_id: str | None = None,
    source_url: str | None = None,
    subject_hint: str | None = None,
    text_hint: str = "",
    max_mentions: int = 80,
) -> tuple[EvidenceMention, ...]:
    """Convert parser fields to quarantined mentions.

    This function intentionally does not create RawAssertion, AdjudicatedClaim,
    primitive mappings, or ScoreContribution objects.
    """

    if not evidence_id.strip():
        raise ValueError("evidence_id must be non-empty")
    if max_mentions <= 0:
        raise ValueError("max_mentions must be positive")
    kind = MentionSourceKind(source_kind)
    mentions: list[EvidenceMention] = []
    for key in sorted(parsed_fields):
        if len(mentions) >= max_mentions:
            break
        field_name = str(key).strip()
        if not field_name or _is_metadata_key(field_name):
            continue
        value = parsed_fields.get(key)
        if not _has_mention_value(value):
            continue
        mention_id = _stable_mention_id(
            evidence_id=evidence_id,
            source_kind=kind,
            field_name=field_name,
            raw_value=value,
            schema_version=EVIDENCE_MENTION_SCHEMA_VERSION,
        )
        mentions.append(
            EvidenceMention(
                mention_id=mention_id,
                evidence_id=evidence_id,
                source_kind=kind,
                field_name=field_name,
                raw_value=value,
                document_id=document_id,
                source_url=source_url,
                text_hint=text_hint.strip(),
                subject_hint=subject_hint.strip() if subject_hint else None,
            )
        )
    return tuple(mentions)


def _is_metadata_key(field_name: str) -> bool:
    return (
        field_name in MENTION_METADATA_KEYS
        or field_name.startswith("compiled_")
        or field_name.startswith("claim_")
    )


def _has_mention_value(value: Any) -> bool:
    if value is None or value == "":
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def _stable_mention_id(
    *,
    evidence_id: str,
    source_kind: MentionSourceKind,
    field_name: str,
    raw_value: Any,
    schema_version: str,
) -> str:
    payload = "|".join(
        (
            schema_version,
            evidence_id,
            source_kind.value,
            field_name,
            _normalise_value(raw_value),
        )
    )
    return f"MEN-{hashlib.sha1(payload.encode('utf-8')).hexdigest()[:20]}"


def _normalise_value(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.10g}"
    if isinstance(value, Mapping):
        items = sorted((str(key), _normalise_value(raw)) for key, raw in value.items())
        return "{" + ",".join(f"{key}:{raw}" for key, raw in items) + "}"
    if isinstance(value, (list, tuple, set)):
        return "[" + ",".join(_normalise_value(item) for item in value) + "]"
    return " ".join(str(value).strip().lower().split())


__all__ = [
    "EVIDENCE_MENTION_SCHEMA_VERSION",
    "EvidenceMention",
    "MentionSourceKind",
    "mentions_from_parsed_fields",
]
