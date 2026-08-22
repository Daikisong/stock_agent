"""Strict identity, authority, roster, and URL checks for ResearchDossierV1."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker

from e2r.scoring import CANONICAL_SCORE_COMPONENTS


DOSSIER_SCHEMA_VERSION = "e2r_pro_research_dossier_v1"
CANONICAL_COMPONENT_IDS = tuple(row.key for row in CANONICAL_SCORE_COMPONENTS)
_FORBIDDEN_FINAL_FIELDS = frozenset(
    {"final_score", "final_stage", "canonical_stage", "score_value", "stage_decision"}
)


class DossierValidationError(ValueError):
    pass


@dataclass(frozen=True)
class DossierValidationContext:
    job_id: str
    run_id: str
    target_id: str
    as_of_date: str


@dataclass(frozen=True)
class DossierValidationReceipt:
    schema_version: str
    job_id: str
    run_id: str
    target_id: str
    as_of_date: str
    component_ids: tuple[str, ...]
    fact_ids: tuple[str, ...]
    source_urls: tuple[str, ...]
    score_authority: bool
    stage_authority: bool


class ResearchDossierValidator:
    def __init__(self, schema_path: str | Path | None = None) -> None:
        default = (
            Path(__file__).resolve().parents[4]
            / "configs/e2r_pro_research_dossier_v1.schema.json"
        )
        self.schema_path = Path(schema_path) if schema_path else default
        self.schema = json.loads(self.schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(self.schema)
        self.validator = Draft202012Validator(
            self.schema, format_checker=FormatChecker()
        )

    def validate(
        self, payload: Mapping[str, Any], context: DossierValidationContext
    ) -> DossierValidationReceipt:
        errors = sorted(self.validator.iter_errors(payload), key=lambda row: tuple(row.path))
        if errors:
            details = "; ".join(
                f"{'/'.join(str(item) for item in error.path) or '$'}: {error.message}"
                for error in errors
            )
            raise DossierValidationError(f"ResearchDossierV1 schema validation failed: {details}")
        for key, expected in (
            ("job_id", context.job_id),
            ("run_id", context.run_id),
            ("as_of_date", context.as_of_date),
        ):
            if payload.get(key) != expected:
                raise DossierValidationError(f"dossier {key} mismatch")
        target = payload.get("target") or {}
        actual_target = str(target.get("target_id") or target.get("symbol") or "")
        if actual_target != context.target_id:
            raise DossierValidationError("dossier target mismatch")
        if payload.get("score_authority") is not False:
            raise DossierValidationError("Pro dossier must have score_authority=false")
        if payload.get("stage_authority") is not False:
            raise DossierValidationError("Pro dossier must have stage_authority=false")
        forbidden = sorted(_find_forbidden_final_fields(payload))
        if forbidden:
            raise DossierValidationError(
                f"Pro dossier contains forbidden final score/Stage fields: {forbidden}"
            )
        component_research = payload.get("component_research") or {}
        if set(component_research) != set(CANONICAL_COMPONENT_IDS):
            raise DossierValidationError("dossier must contain the exact seven component roster")
        facts = tuple(payload.get("material_facts") or ()) + tuple(
            payload.get("counterfacts") or ()
        )
        fact_ids = tuple(str(row.get("dossier_fact_id") or "") for row in facts)
        if len(fact_ids) != len(set(fact_ids)):
            raise DossierValidationError("duplicate dossier fact ids are forbidden")
        source_urls: list[str] = []
        for fact in facts:
            if str(fact.get("target_id") or "") != context.target_id:
                raise DossierValidationError(
                    f"fact target mismatch: {fact.get('dossier_fact_id')}"
                )
            url = str(fact.get("source_url") or "")
            _validate_public_url(url)
            source_urls.append(url)
        for source in payload.get("sources") or ():
            url = str(source.get("source_url") or "")
            _validate_public_url(url)
            source_urls.append(url)
        return DossierValidationReceipt(
            schema_version=DOSSIER_SCHEMA_VERSION,
            job_id=context.job_id,
            run_id=context.run_id,
            target_id=context.target_id,
            as_of_date=context.as_of_date,
            component_ids=CANONICAL_COMPONENT_IDS,
            fact_ids=fact_ids,
            source_urls=tuple(source_urls),
            score_authority=False,
            stage_authority=False,
        )


def _validate_public_url(value: str) -> None:
    parsed = urlparse(value)
    if (
        parsed.scheme not in {"http", "https"}
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
    ):
        raise DossierValidationError(f"invalid public source URL: {value!r}")


def _find_forbidden_final_fields(value: Any, path: str = "$") -> tuple[str, ...]:
    found: list[str] = []
    if isinstance(value, Mapping):
        for key, child in value.items():
            next_path = f"{path}.{key}"
            if str(key).lower() in _FORBIDDEN_FINAL_FIELDS:
                found.append(next_path)
            found.extend(_find_forbidden_final_fields(child, next_path))
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            found.extend(_find_forbidden_final_fields(child, f"{path}[{index}]"))
    return tuple(found)


__all__ = [
    "CANONICAL_COMPONENT_IDS",
    "DOSSIER_SCHEMA_VERSION",
    "DossierValidationContext",
    "DossierValidationError",
    "DossierValidationReceipt",
    "ResearchDossierValidator",
]
