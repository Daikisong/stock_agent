"""Strict identity, authority, closure, and URL checks for Dossier V1/V2."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import json
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker

from e2r.scoring import CANONICAL_SCORE_COMPONENTS

from ..research_contracts import select_contract_bundle
from .v2 import (
    DOSSIER_V2_SCHEMA_VERSION,
    validate_research_status,
    validate_route_bindings,
)


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
    conversation_id: str | None = None
    candidate_archetype_ids: tuple[str, ...] = ()
    research_pass_id: str | None = None
    parent_pass_id: str | None = None
    enforce_parent_pass_id: bool = False


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
    conversation_id: str | None = None
    research_pass_id: str | None = None
    selected_archetype_ids: tuple[str, ...] = ()
    question_family_ids: tuple[str, ...] = ()
    search_route_receipt_ids: tuple[str, ...] = ()
    research_status: str | None = None


class ResearchDossierValidator:
    def __init__(self, schema_path: str | Path | None = None) -> None:
        config_root = Path(__file__).resolve().parents[4] / "configs"
        paths = (
            (Path(schema_path),)
            if schema_path
            else (
                config_root / "e2r_pro_research_dossier_v1.schema.json",
                config_root / "e2r_pro_research_dossier_v2.schema.json",
            )
        )
        self.schemas: dict[str, Mapping[str, Any]] = {}
        self.validators: dict[str, Draft202012Validator] = {}
        for path in paths:
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            version = str(
                ((schema.get("properties") or {}).get("schema_version") or {}).get(
                    "const"
                )
                or ""
            )
            if not version:
                raise ValueError(f"dossier schema lacks a version const: {path}")
            self.schemas[version] = schema
            self.validators[version] = Draft202012Validator(
                schema,
                format_checker=FormatChecker(),
            )
        self.schema_path = paths[0]
        self.schema = self.schemas[next(iter(self.schemas))]
        self.validator = self.validators[next(iter(self.validators))]

    def validate(
        self, payload: Mapping[str, Any], context: DossierValidationContext
    ) -> DossierValidationReceipt:
        dossier_version = str(payload.get("schema_version") or "")
        validator = self.validators.get(dossier_version)
        if validator is None:
            raise DossierValidationError(
                f"unsupported ResearchDossier schema: {dossier_version!r}"
            )
        errors = sorted(validator.iter_errors(payload), key=lambda row: tuple(row.path))
        if errors:
            details = "; ".join(
                f"{'/'.join(str(item) for item in error.path) or '$'}: {error.message}"
                for error in errors
            )
            raise DossierValidationError(
                f"{dossier_version} schema validation failed: {details}"
            )
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
        if dossier_version == DOSSIER_SCHEMA_VERSION:
            return self._validate_v1(payload, context)
        return self._validate_v2(payload, context)

    def _validate_v1(
        self,
        payload: Mapping[str, Any],
        context: DossierValidationContext,
    ) -> DossierValidationReceipt:
        component_research = payload.get("component_research") or {}
        if set(component_research) != set(CANONICAL_COMPONENT_IDS):
            raise DossierValidationError("dossier must contain the exact seven component roster")
        facts = tuple(payload.get("material_facts") or ()) + tuple(payload.get("counterfacts") or ())
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

    def _validate_v2(
        self,
        payload: Mapping[str, Any],
        context: DossierValidationContext,
    ) -> DossierValidationReceipt:
        conversation_id = str(payload.get("conversation_id") or "")
        if context.conversation_id and conversation_id != context.conversation_id:
            raise DossierValidationError("dossier conversation_id mismatch")
        if (
            context.research_pass_id
            and str(payload.get("research_pass_id") or "")
            != context.research_pass_id
        ):
            raise DossierValidationError("dossier research_pass_id mismatch")
        if (
            context.enforce_parent_pass_id
            and payload.get("parent_pass_id") != context.parent_pass_id
        ):
            raise DossierValidationError("dossier parent_pass_id mismatch")
        candidate_ids = tuple(str(value) for value in payload["candidate_archetypes"])
        selected_ids = tuple(str(value) for value in payload["selected_archetypes"])
        if not set(selected_ids).issubset(candidate_ids):
            raise DossierValidationError("selected archetypes escape candidate roster")
        if context.candidate_archetype_ids and not set(candidate_ids).issubset(
            context.candidate_archetype_ids
        ):
            raise DossierValidationError("dossier candidate archetypes escape durable job")
        try:
            bundle = select_contract_bundle(selected_ids)
        except (KeyError, ValueError) as error:
            raise DossierValidationError(str(error)) from error
        allowed_contracts = set(bundle.contract_ids)
        component_research = payload.get("component_research") or {}
        if not set(component_research).issubset(CANONICAL_COMPONENT_IDS):
            raise DossierValidationError("V2 component research contains an unknown component")

        facts = tuple(
            row
            for collection in ("material_facts", "counterfacts", "resolution_facts")
            for row in payload.get(collection) or ()
        )
        fact_ids = tuple(str(row.get("dossier_fact_id") or "") for row in facts)
        if len(fact_ids) != len(set(fact_ids)):
            raise DossierValidationError("duplicate V2 dossier fact ids are forbidden")
        fact_id_set = set(fact_ids)
        cutoff = date.fromisoformat(context.as_of_date)
        source_urls: list[str] = []
        for fact in facts:
            if str(fact.get("target_id") or "") != context.target_id:
                raise DossierValidationError(
                    f"fact target mismatch: {fact.get('dossier_fact_id')}"
                )
            url = str(fact.get("source_url") or "")
            _validate_public_url(url)
            source_urls.append(url)
            _validate_source_date(fact.get("published_at"), cutoff)
            _validate_source_date(fact.get("event_date"), cutoff)

        pass_rows = tuple(payload.get("research_passes") or ())
        pass_ids = tuple(str(row.get("pass_id") or "") for row in pass_rows)
        if len(pass_ids) != len(set(pass_ids)):
            raise DossierValidationError("duplicate research pass ids are forbidden")
        if str(payload["research_pass_id"]) not in set(pass_ids):
            raise DossierValidationError("current research pass is absent from pass ledger")
        parent = payload.get("parent_pass_id")
        if parent is not None and str(parent) not in set(pass_ids):
            raise DossierValidationError("parent research pass is absent from pass ledger")

        question_rows = tuple(payload.get("question_family_results") or ())
        question_ids = tuple(
            str(row.get("question_family_id") or "") for row in question_rows
        )
        if len(question_ids) != len(set(question_ids)):
            raise DossierValidationError("duplicate question-family result ids are forbidden")
        contract_questions = {
            str(question["question_family_id"]): str(contract["archetype_id"])
            for contract in bundle.contracts
            for question in contract["question_families"]
        }
        unknown_questions = set(question_ids) - set(contract_questions)
        if unknown_questions:
            raise DossierValidationError(
                f"question results escape selected contracts: {sorted(unknown_questions)}"
            )
        for row in question_rows:
            question_id = str(row["question_family_id"])
            if str(row["archetype_id"]) != contract_questions[question_id]:
                raise DossierValidationError("question result archetype identity mismatch")
            fact_refs = {
                str(value)
                for key in ("support_fact_ids", "counter_fact_ids", "resolution_fact_ids")
                for value in row.get(key) or ()
            }
            if not fact_refs.issubset(fact_id_set):
                raise DossierValidationError("question result references an unknown fact")
            satisfied = set(row.get("required_source_roles_satisfied") or ())
            missing = set(row.get("required_source_roles_missing") or ())
            if satisfied.intersection(missing):
                raise DossierValidationError("source role cannot be both satisfied and missing")

        lineage_rows = tuple(payload.get("source_lineages") or ())
        lineage_ids = tuple(
            str(row.get("source_lineage_id") or "") for row in lineage_rows
        )
        if len(lineage_ids) != len(set(lineage_ids)):
            raise DossierValidationError("duplicate source lineage ids are forbidden")
        for row in lineage_rows:
            for url in row.get("source_urls") or ():
                _validate_public_url(str(url))
                source_urls.append(str(url))
            if not set(str(value) for value in row.get("fact_ids") or ()).issubset(
                fact_id_set
            ):
                raise DossierValidationError("source lineage references an unknown fact")
        if not {
            str(row.get("source_lineage_id") or "") for row in facts
        }.issubset(set(lineage_ids)):
            raise DossierValidationError("fact references an unknown source lineage")

        try:
            validate_route_bindings(payload)
            validate_research_status(payload)
        except ValueError as error:
            raise DossierValidationError(str(error)) from error
        if not set(
            str(row.get("archetype_id") or "") for row in question_rows
        ).issubset(allowed_contracts):
            raise DossierValidationError("question result contains an unselected contract")
        route_ids = tuple(
            str(row.get("route_receipt_id") or "")
            for row in payload.get("search_route_receipts") or ()
        )
        return DossierValidationReceipt(
            schema_version=DOSSIER_V2_SCHEMA_VERSION,
            job_id=context.job_id,
            run_id=context.run_id,
            target_id=context.target_id,
            as_of_date=context.as_of_date,
            component_ids=tuple(component_research),
            fact_ids=fact_ids,
            source_urls=tuple(source_urls),
            score_authority=False,
            stage_authority=False,
            conversation_id=conversation_id,
            research_pass_id=str(payload["research_pass_id"]),
            selected_archetype_ids=selected_ids,
            question_family_ids=question_ids,
            search_route_receipt_ids=route_ids,
            research_status=str(payload["research_status"]),
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


def _validate_source_date(value: Any, cutoff: date) -> None:
    if value is None or value == "":
        return
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00")).date()
    except ValueError:
        try:
            parsed = date.fromisoformat(str(value))
        except ValueError as error:
            raise DossierValidationError(
                f"invalid dossier source/event date: {value!r}"
            ) from error
    if parsed > cutoff:
        raise DossierValidationError("dossier contains a source/event after as_of_date")


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
