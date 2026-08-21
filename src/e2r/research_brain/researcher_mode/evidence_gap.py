"""Stable evidence-gap identity and audit lineage for Researcher Mode.

An evidence gap is an economic state, not a prompt.  Supervisor prose and
provider request hashes remain useful audit lineage, but changing that prose
must never create a fresh source-query lane for the same structured need.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import json
import re
from typing import Any, Mapping, Sequence

from e2r.research_brain.intelligence_schema import stable_intelligence_id


EVIDENCE_GAP_KEY_SCHEMA_VERSION = "e2r_evidence_gap_key_v1"
EVIDENCE_GAP_AUDIT_LINEAGE_SCHEMA_VERSION = (
    "e2r_evidence_gap_audit_lineage_v1"
)

_SHA256 = re.compile(r"[0-9a-f]{64}")
_STABLE_TOKEN = re.compile(r"[A-Za-z0-9_.:/,+\-\[\]]+")
_IDENTITY_FIELDS = (
    "target_id",
    "as_of_date",
    "archetype_id",
    "objective_identity",
    "affected_component_ids",
    "required_source_family",
    "economic_mechanism_id",
    "predicate_or_fact_need_id",
    "fact_snapshot_hash",
    "accepted_lineage_roster_hash",
)
_PROSE_OR_CALL_LINEAGE_FIELDS = frozenset(
    {
        "supervisor_text",
        "rationale",
        "query_text",
        "prompt_hash",
        "response_hash",
        "retry_count",
        "request_id",
    }
)


def _canonical_hash(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ).encode("utf-8")
    ).hexdigest()


def _required_text(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ValueError(f"{label} is required")
    return text


def _stable_token(value: Any, label: str) -> str:
    text = _required_text(value, label)
    if _STABLE_TOKEN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a stable symbolic id, not prose")
    return text


def _sha256(value: Any, label: str) -> str:
    text = _required_text(value, label).lower()
    if _SHA256.fullmatch(text) is None:
        raise ValueError(f"{label} must be a sha256 digest")
    return text


def canonical_source_family_requirement(
    source_families: str | Sequence[str],
) -> str:
    """Return one deterministic source-family requirement token.

    A gap can require one source family or a corroboration set.  The latter is
    represented as one sorted symbolic token so input order cannot split the
    identity.
    """

    raw_values = (
        (source_families,)
        if isinstance(source_families, str)
        else tuple(source_families)
    )
    values = tuple(
        sorted(
            {
                _stable_token(value, "required source family").upper()
                for value in raw_values
            }
        )
    )
    if not values:
        raise ValueError("at least one required source family is required")
    if len(values) == 1:
        return values[0]
    return "SOURCE_FAMILY_SET[" + ",".join(values) + "]"


def derive_objective_identity(
    *,
    stable_objective_id: str | None,
    affected_component_ids: Sequence[str],
    required_source_family: str | Sequence[str],
    economic_mechanism_id: str,
    predicate_or_fact_need_id: str,
) -> str:
    """Prefer a registry objective id, otherwise hash only stable structure."""

    if stable_objective_id is not None and str(stable_objective_id).strip():
        return _stable_token(stable_objective_id, "stable objective id")
    components = tuple(
        sorted(
            {
                _stable_token(value, "affected component id")
                for value in affected_component_ids
            }
        )
    )
    if not components:
        raise ValueError("affected component ids are required")
    payload = {
        "affected_component_ids": components,
        "required_source_family": canonical_source_family_requirement(
            required_source_family
        ),
        "economic_mechanism_id": _stable_token(
            economic_mechanism_id, "economic mechanism id"
        ),
        "predicate_or_fact_need_id": _stable_token(
            predicate_or_fact_need_id, "predicate or fact need id"
        ),
    }
    return stable_intelligence_id("EGAPOBJ", payload)


@dataclass(frozen=True)
class EvidenceGapKey:
    """Canonical identity for one evidence gap at one factual snapshot."""

    target_id: str
    as_of_date: str
    archetype_id: str
    objective_identity: str
    affected_component_ids: tuple[str, ...]
    required_source_family: str
    economic_mechanism_id: str
    predicate_or_fact_need_id: str
    fact_snapshot_hash: str
    accepted_lineage_roster_hash: str
    schema_version: str = EVIDENCE_GAP_KEY_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != EVIDENCE_GAP_KEY_SCHEMA_VERSION:
            raise ValueError("evidence gap key schema mismatch")
        object.__setattr__(self, "target_id", _stable_token(self.target_id, "target id"))
        try:
            date.fromisoformat(_required_text(self.as_of_date, "as_of_date"))
        except ValueError as error:
            raise ValueError("as_of_date must be ISO-8601") from error
        object.__setattr__(
            self, "archetype_id", _stable_token(self.archetype_id, "archetype id")
        )
        object.__setattr__(
            self,
            "objective_identity",
            _stable_token(self.objective_identity, "objective identity"),
        )
        components = tuple(
            sorted(
                {
                    _stable_token(value, "affected component id")
                    for value in self.affected_component_ids
                }
            )
        )
        if not components:
            raise ValueError("affected component ids are required")
        object.__setattr__(self, "affected_component_ids", components)
        object.__setattr__(
            self,
            "required_source_family",
            canonical_source_family_requirement(self.required_source_family),
        )
        object.__setattr__(
            self,
            "economic_mechanism_id",
            _stable_token(self.economic_mechanism_id, "economic mechanism id"),
        )
        object.__setattr__(
            self,
            "predicate_or_fact_need_id",
            _stable_token(
                self.predicate_or_fact_need_id,
                "predicate or fact need id",
            ),
        )
        object.__setattr__(
            self,
            "fact_snapshot_hash",
            _sha256(self.fact_snapshot_hash, "fact snapshot hash"),
        )
        object.__setattr__(
            self,
            "accepted_lineage_roster_hash",
            _sha256(
                self.accepted_lineage_roster_hash,
                "accepted lineage roster hash",
            ),
        )

    @classmethod
    def identity_field_names(cls) -> tuple[str, ...]:
        return _IDENTITY_FIELDS

    @classmethod
    def prohibited_prose_or_call_lineage_fields(cls) -> frozenset[str]:
        return _PROSE_OR_CALL_LINEAGE_FIELDS

    @property
    def semantic_gap_id(self) -> str:
        """Gap family identity excluding factual-state version hashes."""

        return stable_intelligence_id(
            "EGAPSEM",
            {
                key: value
                for key, value in self.identity_payload().items()
                if key
                not in {"fact_snapshot_hash", "accepted_lineage_roster_hash"}
            },
        )

    @property
    def gap_key(self) -> str:
        return stable_intelligence_id("EGAP", self.identity_payload())

    def identity_payload(self) -> Mapping[str, Any]:
        return {
            "target_id": self.target_id,
            "as_of_date": self.as_of_date,
            "archetype_id": self.archetype_id,
            "objective_identity": self.objective_identity,
            "affected_component_ids": list(self.affected_component_ids),
            "required_source_family": self.required_source_family,
            "economic_mechanism_id": self.economic_mechanism_id,
            "predicate_or_fact_need_id": self.predicate_or_fact_need_id,
            "fact_snapshot_hash": self.fact_snapshot_hash,
            "accepted_lineage_roster_hash": self.accepted_lineage_roster_hash,
        }

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "gap_key": self.gap_key,
            "semantic_gap_id": self.semantic_gap_id,
            **self.identity_payload(),
            "identity_payload_hash": _canonical_hash(self.identity_payload()),
            "prose_or_call_lineage_in_identity": False,
        }


@dataclass(frozen=True)
class EvidenceGapAuditLineage:
    """Non-authoritative prose and provider lineage kept outside the key."""

    request_id: str | None = None
    prompt_hash: str | None = None
    response_hash: str | None = None
    supervisor_text: str | None = None
    rationale: str | None = None
    schema_version: str = EVIDENCE_GAP_AUDIT_LINEAGE_SCHEMA_VERSION

    def __post_init__(self) -> None:
        if self.schema_version != EVIDENCE_GAP_AUDIT_LINEAGE_SCHEMA_VERSION:
            raise ValueError("evidence gap audit lineage schema mismatch")
        for field_name in ("request_id", "prompt_hash", "response_hash"):
            raw = getattr(self, field_name)
            if raw is not None and not str(raw).strip():
                raise ValueError(f"{field_name} cannot be blank")

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": self.schema_version,
            "request_id": self.request_id,
            "prompt_hash": self.prompt_hash,
            "response_hash": self.response_hash,
            "supervisor_text": self.supervisor_text,
            "rationale": self.rationale,
            "production_score_authority": False,
            "production_stage_authority": False,
        }

