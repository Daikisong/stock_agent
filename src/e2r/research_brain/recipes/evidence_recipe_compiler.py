"""Compile explicit semantic EvidenceRecipe records from contracts and cases."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.agentic.evidence_os import EvidenceContractV2
from e2r.production.metadata import stable_hash, write_json, write_jsonl, write_text
from e2r.research_brain.intelligence_schema import (
    AcceptedClaimPredicate,
    EvidenceRecipe,
    EvidenceRecipeRole,
    HistoricalResearchCase,
    HistoricalSourceState,
    HistoricalSourceVerification,
    UnsupportedEvidenceRecipe,
    stable_intelligence_id,
)


EVIDENCE_RECIPE_SEMANTICS_SCHEMA_VERSION = "e2r_evidence_recipe_semantics_v1"
DEFAULT_EVIDENCE_RECIPE_SEMANTICS_PATH = (
    Path(__file__).resolve().parents[4] / "configs" / "e2r_evidence_recipe_semantics_v1.json"
)
RECIPE_ROUTING_STRATEGY = "EXACT_ARCHETYPE_PRIMITIVE_SEMANTIC_DEFINITION_LOOKUP"


@dataclass(frozen=True)
class EvidenceRecipeCompilationResult:
    recipes: tuple[EvidenceRecipe, ...]
    unsupported: tuple[UnsupportedEvidenceRecipe, ...]
    manifest: Mapping[str, Any]


def load_evidence_recipe_semantics(
    path: str | Path = DEFAULT_EVIDENCE_RECIPE_SEMANTICS_PATH,
) -> Mapping[str, Any]:
    source = Path(path)
    payload = json.loads(source.read_text(encoding="utf-8", errors="strict"))
    if payload.get("schema_version") != EVIDENCE_RECIPE_SEMANTICS_SCHEMA_VERSION:
        raise ValueError("unsupported EvidenceRecipe semantics schema_version")
    profiles = payload.get("profiles")
    definitions = payload.get("primitive_definitions")
    if not isinstance(profiles, Mapping) or not isinstance(definitions, list):
        raise ValueError("EvidenceRecipe semantics requires profiles and primitive_definitions")
    seen: set[tuple[str, str]] = set()
    for index, definition in enumerate(definitions):
        if not isinstance(definition, Mapping):
            raise ValueError(f"primitive definition must be an object: index={index}")
        key = (str(definition.get("archetype_id") or ""), str(definition.get("primitive_id") or ""))
        if not all(key):
            raise ValueError(f"primitive definition identity missing: index={index}")
        if key in seen:
            raise ValueError(f"duplicate primitive semantic definition: {key}")
        seen.add(key)
    return payload


def compile_evidence_recipe_os(
    cases: Iterable[HistoricalResearchCase],
    *,
    source_verifications: Sequence[HistoricalSourceVerification] = (),
    contracts: Mapping[str, EvidenceContractV2] | None = None,
    semantics_path: str | Path = DEFAULT_EVIDENCE_RECIPE_SEMANTICS_PATH,
    required_url_backed_case_ids: Iterable[str] = (),
    required_source_proxy_case_ids: Iterable[str] = (),
) -> EvidenceRecipeCompilationResult:
    contract_map = dict(
        contracts
        if contracts is not None
        else load_evidence_contracts_v2(require_all_archetypes=True)
    )
    semantics = load_evidence_recipe_semantics(semantics_path)
    profiles = {str(key): value for key, value in semantics["profiles"].items()}
    definitions = {
        (str(row["archetype_id"]), str(row["primitive_id"])): row
        for row in semantics["primitive_definitions"]
    }
    required_pairs = {
        (archetype_id, primitive_id)
        for archetype_id, contract in contract_map.items()
        for primitive_id in contract.required_primitives
    }
    extra_definitions = set(definitions) - required_pairs
    if extra_definitions:
        raise ValueError(
            f"semantic definitions reference non-required contract pairs: {sorted(extra_definitions)}"
        )

    ordered_cases = tuple(sorted(cases, key=lambda item: item.case_id))
    cases_by_archetype: dict[str, list[HistoricalResearchCase]] = {}
    for case in ordered_cases:
        cases_by_archetype.setdefault(case.canonical_archetype_id, []).append(case)
    verifications_by_case: dict[str, list[HistoricalSourceVerification]] = {}
    for verification in source_verifications:
        verifications_by_case.setdefault(verification.case_id, []).append(verification)

    recipes: list[EvidenceRecipe] = []
    unsupported: list[UnsupportedEvidenceRecipe] = []
    for archetype_id, primitive_id in sorted(required_pairs):
        contract = contract_map[archetype_id]
        profile = profiles.get(archetype_id)
        definition = definitions.get((archetype_id, primitive_id))
        archetype_cases = tuple(cases_by_archetype.get(archetype_id, ()))
        if not isinstance(profile, Mapping) or not isinstance(definition, Mapping):
            unsupported.append(
                _unsupported(
                    archetype_id,
                    primitive_id,
                    reason_code="UNSUPPORTED_PENDING_SEMANTIC_RECIPE",
                    reason_detail=(
                        "Evidence Contract exists, but no reviewed archetype profile and "
                        "primitive semantic definition are registered. A generic route is forbidden."
                    ),
                )
            )
            continue
        supporting_cases = _supporting_cases(archetype_cases, primitive_id)
        if not supporting_cases:
            unsupported.append(
                _unsupported(
                    archetype_id,
                    primitive_id,
                    reason_code="UNSUPPORTED_NO_SUPPORTING_CASE_IN_INPUT",
                    reason_detail=(
                        "An explicit semantic definition exists, but this compile input has no "
                        "historical case for the archetype. Supporting case IDs may not be fabricated."
                    ),
                )
            )
            continue
        recipes.append(
            _compile_recipe(
                contract=contract,
                primitive_id=primitive_id,
                profile=profile,
                definition=definition,
                supporting_cases=supporting_cases,
                verifications_by_case=verifications_by_case,
            )
        )

    manifest = _build_recipe_manifest(
        contracts=contract_map,
        required_pairs=required_pairs,
        cases=ordered_cases,
        recipes=recipes,
        unsupported=unsupported,
        required_url_backed_case_ids=set(required_url_backed_case_ids),
        required_source_proxy_case_ids=set(required_source_proxy_case_ids),
    )
    return EvidenceRecipeCompilationResult(
        recipes=tuple(recipes),
        unsupported=tuple(unsupported),
        manifest=manifest,
    )


def write_evidence_recipe_os(
    result: EvidenceRecipeCompilationResult,
    *,
    output_root: str | Path,
) -> Mapping[str, Path]:
    root = Path(output_root) / "recipes"
    paths = {
        "recipes": root / "evidence_recipes.jsonl",
        "unsupported": root / "unsupported_evidence_recipes.jsonl",
        "manifest": root / "evidence_recipe_manifest.json",
        "report": root / "evidence_recipe_report.md",
    }
    write_jsonl(paths["recipes"], (item.to_dict() for item in result.recipes))
    write_jsonl(paths["unsupported"], (item.to_dict() for item in result.unsupported))
    write_json(paths["manifest"], dict(result.manifest))
    write_text(paths["report"], render_evidence_recipe_report(result.manifest))
    return paths


def render_evidence_recipe_report(manifest: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# E2R Executable EvidenceRecipe OS",
            "",
            f"- status: {manifest['status']}",
            f"- required_primitive_pair_count: {manifest['required_primitive_pair_count']}",
            f"- executable_recipe_count: {manifest['executable_recipe_count']}",
            f"- explicit_unsupported_count: {manifest['explicit_unsupported_count']}",
            f"- pair_coverage_rate: {manifest['pair_coverage_rate']}",
            f"- executable_recipe_coverage_rate: {manifest['executable_recipe_coverage_rate']}",
            f"- critical_count_sum: {manifest['critical_count_sum']}",
            "",
            "Unsupported pairs remain planning-only; they are not replaced by generic primitive-name queries.",
        ]
    ) + "\n"


def _compile_recipe(
    *,
    contract: EvidenceContractV2,
    primitive_id: str,
    profile: Mapping[str, Any],
    definition: Mapping[str, Any],
    supporting_cases: Sequence[HistoricalResearchCase],
    verifications_by_case: Mapping[str, Sequence[HistoricalSourceVerification]],
) -> EvidenceRecipe:
    role = _recipe_role(contract, primitive_id)
    freshness = contract.freshness.get(primitive_id)
    required_entities = _strings(definition.get("required_entities"))
    required_values = _strings(definition.get("required_values"))
    required_units = _strings(definition.get("required_units"))
    required_time_scope = _strings(profile.get("required_time_scope"))
    predicates = tuple(
        AcceptedClaimPredicate(
            predicate_id=stable_intelligence_id(
                "RCPRED",
                {
                    "archetype_id": contract.archetype_id,
                    "primitive_id": primitive_id,
                    "semantic_test": semantic_test,
                },
            ),
            semantic_test=semantic_test,
            required_subject_relation="target-direct or explicitly permitted target subsidiary/customer relation",
            required_fields=tuple(
                dict.fromkeys(
                    (
                        "source_id",
                        "exact_anchor",
                        "subject_entity",
                        "target_entity",
                        "published_date",
                        "effective_period",
                        *required_entities,
                        *required_values,
                        *required_units,
                    )
                )
            ),
            allowed_polarities=("POSITIVE", "NEGATIVE"),
            temporal_test=(
                "published/available/effective dates must be on or before as_of_date and "
                "within the contract freshness policy"
            ),
            lifecycle_test="claim must be current OPEN or the latest effective unsuperseded assertion",
        )
        for semantic_test in _strings(definition.get("semantic_tests"))
    )
    supporting_case_ids = tuple(case.case_id for case in supporting_cases)
    related_verifications = tuple(
        verification
        for case_id in supporting_case_ids
        for verification in verifications_by_case.get(case_id, ())
    )
    successful = tuple(
        item.verification_id for item in related_verifications if item.historical_replay_ready
    )
    failed = tuple(
        item.verification_id for item in related_verifications if not item.historical_replay_ready
    )
    proxy_cases = tuple(
        case.case_id
        for case in supporting_cases
        if str(case.declared_source_quality or "").upper()
        in {
            HistoricalSourceState.SOURCE_PROXY_ONLY.value,
            HistoricalSourceState.EVIDENCE_URL_PENDING.value,
        }
    )
    return EvidenceRecipe(
        recipe_id=stable_intelligence_id(
            "ERECIPE",
            {"archetype_id": contract.archetype_id, "primitive_id": primitive_id},
        ),
        archetype_id=contract.archetype_id,
        primitive_id=primitive_id,
        role=role.value,
        economic_mechanism=str(profile["economic_mechanism"]),
        question_to_answer=str(definition["question_to_answer"]),
        accepted_claim_predicates=predicates,
        required_entities=required_entities,
        required_values=required_values,
        required_units=required_units,
        required_time_scope=required_time_scope,
        required_target_directness=_strings(profile.get("required_target_directness")),
        required_current_lifecycle=_strings(profile.get("required_current_lifecycle")),
        preferred_source_families=_strings(profile.get("preferred_source_families")),
        preferred_document_types=_strings(profile.get("preferred_document_types")),
        preferred_sections=_strings(profile.get("preferred_sections")),
        discovery_sources=_strings(profile.get("discovery_sources")),
        forbidden_score_sources=_strings(profile.get("forbidden_score_sources")),
        positive_examples=_strings(definition.get("positive_examples")),
        counterexamples=_strings(definition.get("counterexamples")),
        wrong_subject_examples=_strings(profile.get("wrong_subject_examples")),
        source_success_examples=_strings(profile.get("source_success_examples")),
        source_failure_examples=_strings(profile.get("source_failure_examples")),
        rejection_conditions=_strings(definition.get("rejection_conditions")),
        counter_questions=_strings(definition.get("counter_questions")),
        supersession_questions=_strings(profile.get("supersession_questions")),
        query_intent_constraints=_strings(profile.get("query_intent_constraints")),
        stop_conditions=_strings(profile.get("stop_conditions")),
        source_exhaustion_conditions=_strings(profile.get("source_exhaustion_conditions")),
        supporting_case_ids=supporting_case_ids,
        supporting_source_verification_ids=successful,
        supporting_source_failure_verification_ids=failed,
        planning_only_source_proxy_case_ids=proxy_cases,
        freshness_max_age_days=freshness.max_age_days if freshness else None,
        freshness_supersession_rule=freshness.supersession_rule if freshness else None,
        literal_queries=(),
    )


def _supporting_cases(
    cases: Sequence[HistoricalResearchCase],
    primitive_id: str,
) -> tuple[HistoricalResearchCase, ...]:
    exact = tuple(
        case
        for case in cases
        if primitive_id
        in {
            *case.positive_evidence_fields,
            *case.missing_evidence_fields,
            *case.counter_evidence_fields,
            *case.hard_breaks,
        }
    )
    return exact or tuple(cases)


def _recipe_role(
    contract: EvidenceContractV2,
    primitive_id: str,
) -> EvidenceRecipeRole:
    guard_mode = contract.guard_modes.get(primitive_id)
    if guard_mode == "hard_break_if_current_and_quorum":
        return EvidenceRecipeRole.HARD_BREAK
    if guard_mode:
        return EvidenceRecipeRole.GUARD
    return EvidenceRecipeRole.POSITIVE


def _unsupported(
    archetype_id: str,
    primitive_id: str,
    *,
    reason_code: str,
    reason_detail: str,
) -> UnsupportedEvidenceRecipe:
    return UnsupportedEvidenceRecipe(
        unsupported_id=stable_intelligence_id(
            "ERUNSUPPORTED",
            {"archetype_id": archetype_id, "primitive_id": primitive_id, "reason": reason_code},
        ),
        archetype_id=archetype_id,
        primitive_id=primitive_id,
        reason_code=reason_code,
        reason_detail=reason_detail,
        required_next_input=(
            "reviewed economic mechanism",
            "accepted claim predicate with entities/values/time",
            "positive, counter, wrong-subject, and source success/failure examples",
            "rejection, lifecycle, counter, and supersession rules",
        ),
    )


def _build_recipe_manifest(
    *,
    contracts: Mapping[str, EvidenceContractV2],
    required_pairs: set[tuple[str, str]],
    cases: Sequence[HistoricalResearchCase],
    recipes: Sequence[EvidenceRecipe],
    unsupported: Sequence[UnsupportedEvidenceRecipe],
    required_url_backed_case_ids: set[str],
    required_source_proxy_case_ids: set[str],
) -> Mapping[str, Any]:
    recipe_pairs = {(item.archetype_id, item.primitive_id) for item in recipes}
    unsupported_pairs = {(item.archetype_id, item.primitive_id) for item in unsupported}
    covered_pairs = recipe_pairs | unsupported_pairs
    case_by_id = {case.case_id: case for case in cases}
    recipes_by_archetype: dict[str, list[EvidenceRecipe]] = {}
    for recipe in recipes:
        recipes_by_archetype.setdefault(recipe.archetype_id, []).append(recipe)

    url_example_missing = sum(
        case_id not in case_by_id
        or not any(
            case_id in recipe.supporting_case_ids
            and recipe.positive_examples
            and recipe.source_success_examples
            and recipe.source_failure_examples
            for recipe in recipes_by_archetype.get(
                case_by_id[case_id].canonical_archetype_id,
                (),
            )
        )
        for case_id in required_url_backed_case_ids
    )
    proxy_not_planning = sum(
        case_id not in case_by_id
        or not any(
            case_id in recipe.planning_only_source_proxy_case_ids
            for recipe in recipes_by_archetype.get(
                case_by_id[case_id].canonical_archetype_id,
                (),
            )
        )
        for case_id in required_source_proxy_case_ids
    )
    lifecycle_missing = sum(
        not recipe.required_current_lifecycle or not recipe.supersession_questions
        for recipe in recipes
    )
    acceptance_missing = sum(
        not recipe.accepted_claim_predicates or not recipe.rejection_conditions
        for recipe in recipes
    )
    counter_missing = sum(
        not recipe.counterexamples or not recipe.counter_questions for recipe in recipes
    )
    generic_query_only = sum(
        bool(recipe.literal_queries)
        or not recipe.economic_mechanism
        or not recipe.accepted_claim_predicates
        or not recipe.preferred_sections
        for recipe in recipes
    )
    critical = {
        "required_pair_without_recipe_or_unsupported_reason": len(required_pairs - covered_pairs),
        "unknown_recipe_or_unsupported_pair": len(covered_pairs - required_pairs),
        "url_backed_case_recipe_example_missing": url_example_missing,
        "source_proxy_example_not_planning_only": proxy_not_planning,
        "generic_query_only_recipe": generic_query_only,
        "primitive_substring_production_routing": 0,
        "acceptance_or_rejection_missing": acceptance_missing,
        "counter_question_or_example_missing": counter_missing,
        "lifecycle_or_supersession_missing": lifecycle_missing,
        "literal_query_in_recipe": sum(bool(recipe.literal_queries) for recipe in recipes),
        "recipe_runtime_score_eligible": sum(recipe.runtime_score_eligible for recipe in recipes),
        "unsupported_runtime_route_available": sum(
            item.runtime_route_available for item in unsupported
        ),
    }
    supported_archetypes = sorted({recipe.archetype_id for recipe in recipes})
    return {
        "schema_version": "e2r_evidence_recipe_os_manifest_v1",
        "status": (
            "EVIDENCE_RECIPE_OS_COMPILER_PASS"
            if required_pairs and sum(critical.values()) == 0
            else "EVIDENCE_RECIPE_OS_COMPILER_FAIL"
        ),
        "routing_strategy": RECIPE_ROUTING_STRATEGY,
        "contract_count": len(contracts),
        "required_primitive_pair_count": len(required_pairs),
        "executable_recipe_count": len(recipes),
        "explicit_unsupported_count": len(unsupported),
        "covered_pair_count": len(covered_pairs),
        "pair_coverage_rate": round(len(covered_pairs) / len(required_pairs), 6),
        "executable_recipe_coverage_rate": round(len(recipes) / len(required_pairs), 6),
        "supported_archetype_count": len(supported_archetypes),
        "supported_archetypes": supported_archetypes,
        "recipe_count_by_archetype": dict(
            sorted(Counter(recipe.archetype_id for recipe in recipes).items())
        ),
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "recipe_hash": stable_hash([recipe.to_dict() for recipe in recipes]),
        "unsupported_hash": stable_hash([item.to_dict() for item in unsupported]),
        "production_runtime_ready": False,
    }


def _strings(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    values = value if isinstance(value, (list, tuple)) and not isinstance(value, (str, bytes)) else (value,)
    return tuple(dict.fromkeys(str(item).strip() for item in values if str(item).strip()))


__all__ = [
    "DEFAULT_EVIDENCE_RECIPE_SEMANTICS_PATH",
    "EVIDENCE_RECIPE_SEMANTICS_SCHEMA_VERSION",
    "EvidenceRecipeCompilationResult",
    "RECIPE_ROUTING_STRATEGY",
    "compile_evidence_recipe_os",
    "load_evidence_recipe_semantics",
    "render_evidence_recipe_report",
    "write_evidence_recipe_os",
]
