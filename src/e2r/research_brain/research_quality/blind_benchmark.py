"""Gold 조사와 production 조사를 격리한 뒤 material fact recall을 비교한다.

Post-run independent adjudication compares the core economic event rather than
requiring the Gold and production lanes to use the same page, wording, numeric
surface form, or atomic row shape.  The adjudicators must still preserve the
target, time/currentness, subject and segment, economic direction, and business
mechanism boundaries.  This deliberately leaves semantic judgment with the
independent reviewers instead of adding keyword or Gold-specific auto-matching.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl


GOLD_FACT_FILE = "gold_material_facts.jsonl"
GOLD_SOURCE_FILE = "gold_source_map.jsonl"
GOLD_COVERAGE_FILE = "gold_question_coverage.json"
PRODUCTION_FACT_FILE = "production_material_facts.jsonl"
PRODUCTION_INPUT_FILE = "production_input_manifest.jsonl"
PRODUCTION_LANE_FILE = "production_lane_manifest.json"
POST_RUN_SEMANTIC_PRIMARY_FILE = "post_run_gold_semantic_primary.json"
POST_RUN_SEMANTIC_REVIEW_DIRECTORY = "post_run_gold_semantic_reviews"
POST_RUN_SEMANTIC_PRIMARY_SCHEMA_VERSION = (
    "e2r_v6_post_run_gold_semantic_primary_v2"
)
POST_RUN_SEMANTIC_REVIEW_SCHEMA_VERSION = (
    "e2r_v6_post_run_gold_semantic_review_v2"
)
MINIMUM_INDEPENDENT_SEMANTIC_REVIEW_COUNT = 2
POST_RUN_REVIEW_PROVIDER_ROUTE = "CODEX_COLLABORATION"

# This metadata makes the human/Codex adjudication contract machine-visible in
# the audit without changing the primary/review payload schemas.  In particular,
# a component-local fact_role label is not a literal identity key: the same
# dividend actual can be a capital-allocation COUNTER in one component and still
# support a Gold shareholder-return event.  Its economic direction and event
# must nevertheless remain compatible.
POST_RUN_SEMANTIC_MATCH_CONTRACT = {
    "contract_version": "CORE_ECONOMIC_EVENT_EQUIVALENCE_V1",
    "equivalence_basis": "CORE_ECONOMIC_EVENT",
    "literal_page_identity_required": False,
    "literal_numeric_text_identity_required": False,
    "canonical_numeric_meaning_required": True,
    "compound_atomic_fact_sets_allowed": True,
    "component_context_fact_role_identity_required": False,
    "economic_direction_compatibility_required": True,
    "source_quality_evaluated_separately": True,
    "required_boundaries": (
        "TARGET",
        "AS_OF_AND_CURRENTNESS",
        "SUBJECT",
        "SEGMENT",
        "CORE_ECONOMIC_EVENT",
        "BUSINESS_MECHANISM",
    ),
    "prohibited_substitutions": (
        "DIFFERENT_TARGET",
        "INDUSTRY_GENERAL_WITHOUT_TARGET_ATTRIBUTION",
        "WRONG_SEGMENT",
    ),
}


def build_post_run_reviewer_identity(
    *,
    role_id: str,
    provider_call_id: str,
    prompt_hash: str,
    response_hash: str,
) -> Mapping[str, str]:
    """Build one portable post-run reviewer identity.

    Filesystem task names such as ``/root/reviewer_a`` are deliberately not
    identities: they change across machines.  The role and provider-call
    binding below is portable and can be recomputed in a clean clone.
    """

    core = {
        "role_id": str(role_id).strip(),
        "provider_route": POST_RUN_REVIEW_PROVIDER_ROUTE,
        "provider_call_id": str(provider_call_id).strip(),
        "prompt_hash": str(prompt_hash).strip(),
        "response_hash": str(response_hash).strip(),
    }
    return {**core, "identity_hash": stable_hash(core)}


def _validated_post_run_reviewer_identity(
    value: Any,
    *,
    expected_role_id: str | None = None,
) -> Mapping[str, str]:
    if not isinstance(value, Mapping):
        raise ValueError("post-run semantic reviewer identity is missing")
    core = {
        key: str(value.get(key) or "").strip()
        for key in (
            "role_id",
            "provider_route",
            "provider_call_id",
            "prompt_hash",
            "response_hash",
        )
    }
    role_id = core["role_id"]
    provider_call_id = core["provider_call_id"]
    if expected_role_id is not None:
        role_valid = role_id == expected_role_id
    else:
        role_valid = role_id.startswith("CODEX_POST_RUN_REVIEWER_")
    portable_call_id = bool(provider_call_id) and all(
        character.isalnum() or character in "-_.:"
        for character in provider_call_id
    )
    lowercase_hex = set("0123456789abcdef")
    hashes_valid = all(
        len(core[key]) == 64
        and set(core[key]).issubset(lowercase_hex)
        for key in ("prompt_hash", "response_hash")
    )
    if (
        not role_valid
        or core["provider_route"] != POST_RUN_REVIEW_PROVIDER_ROUTE
        or not portable_call_id
        or not hashes_valid
        or str(value.get("identity_hash") or "") != stable_hash(core)
    ):
        raise ValueError("post-run semantic reviewer identity is invalid")
    return {**core, "identity_hash": stable_hash(core)}

REQUIRED_GOLD_ROUTES = {
    "official_filing",
    "issuer_ir_earnings",
    "issuer_newsroom",
    "customer_official",
    "trusted_independent",
    "financial_revision",
    "counter_supersession",
}
SOURCE_TIER_RANK = {
    "REGULATORY_OFFICIAL": 1,
    "ISSUER_OFFICIAL": 1,
    "CUSTOMER_OFFICIAL": 1,
    "TRUSTED_INDEPENDENT": 2,
    "FINANCIAL_REVISION": 2,
    "GENERAL_WEB": 3,
    "DISCOVERY_ONLY": 4,
}


@dataclass(frozen=True)
class MaterialFactComparison:
    question_family_id: str
    gold_fact_id: str
    production_fact_id: str | None
    semantic_match: bool
    source_quality_match: bool
    currentness_match: bool
    mechanism_scope_match: bool
    materiality: str
    miss_reason: str | None
    fact_role: str
    target_id: str
    production_fact_ids: tuple[str, ...]
    semantic_match_method: str

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class BlindResearchBenchmarkResult:
    status: str
    comparisons: tuple[MaterialFactComparison, ...]
    audit: Mapping[str, Any]


class BlindResearchQualityBenchmark:
    """Production 결과 생성이 끝난 뒤에만 gold leaf를 열어 비교한다."""

    def compare(
        self,
        *,
        gold_root: str | Path,
        production_root: str | Path,
        post_run_semantic_adjudication_root: str | Path | None = None,
    ) -> BlindResearchBenchmarkResult:
        gold = Path(gold_root).resolve()
        production = Path(production_root).resolve()
        _require_isolated_roots(gold, production)
        gold_facts = _read_jsonl(gold / GOLD_FACT_FILE)
        gold_sources = _read_jsonl(gold / GOLD_SOURCE_FILE)
        coverage = _read_json(gold / GOLD_COVERAGE_FILE)
        production_facts = _read_jsonl(production / PRODUCTION_FACT_FILE)
        production_inputs = _read_jsonl(production / PRODUCTION_INPUT_FILE)
        production_lane = _read_json(production / PRODUCTION_LANE_FILE)
        _validate_gold_lane(gold_facts, gold_sources, coverage)
        _validate_production_lane(production_facts, production_lane)
        semantic_adjudication = _load_post_run_semantic_adjudication(
            root=(
                Path(post_run_semantic_adjudication_root).resolve()
                if post_run_semantic_adjudication_root is not None
                else None
            ),
            gold_facts=gold_facts,
            production_facts=production_facts,
        )

        leakage = _audit_gold_leakage(
            gold_root=gold,
            gold_facts=gold_facts,
            gold_sources=gold_sources,
            production_inputs=production_inputs,
            production_lane=production_lane,
        )
        comparisons = _compare_material_facts(
            gold_facts,
            production_facts,
            semantic_adjudication=semantic_adjudication,
        )
        qualified = {
            row.gold_fact_id
            for row in comparisons
            if row.semantic_match
            and row.source_quality_match
            and row.currentness_match
            and row.mechanism_scope_match
        }
        critical_misses = sum(
            row.materiality == "CRITICAL" and row.gold_fact_id not in qualified
            for row in comparisons
        )
        counter_misses = sum(
            row.fact_role == "COUNTER" and row.gold_fact_id not in qualified
            for row in comparisons
        )
        supersession_misses = sum(
            row.fact_role == "SUPERSESSION"
            and row.gold_fact_id not in qualified
            for row in comparisons
        )
        noncritical = [
            row for row in comparisons if row.materiality == "NONCRITICAL"
        ]
        noncritical_recall = (
            sum(row.gold_fact_id in qualified for row in noncritical)
            / len(noncritical)
            if noncritical
            else 1.0
        )
        routes = {
            str(row.get("research_route") or "") for row in gold_sources
        }
        missing_routes = sorted(REQUIRED_GOLD_ROUTES - routes)
        critical_counts = {
            "critical_material_fact_miss_count": critical_misses,
            "material_counter_fact_miss_count": counter_misses,
            "material_supersession_fact_miss_count": supersession_misses,
            "gold_source_injected_into_production_count": leakage[
                "gold_source_injected_into_production_count"
            ],
            "gold_query_leaked_into_production_count": leakage[
                "gold_query_leaked_into_production_count"
            ],
            "gold_fact_leaked_into_production_prompt_count": leakage[
                "gold_fact_leaked_into_production_prompt_count"
            ],
            "gold_route_missing_count": len(missing_routes),
            "noncritical_recall_below_90_count": int(
                noncritical_recall < 0.9
            ),
        }
        critical_sum = sum(critical_counts.values())
        status = (
            "BLIND_RESEARCH_QUALITY_PASS"
            if critical_sum == 0
            else "BLIND_RESEARCH_QUALITY_FAIL"
        )
        audit = {
            "schema_version": "e2r_research_quality_gold_audit_v1",
            "status": status,
            "benchmark_mode": str(
                coverage.get("benchmark_mode")
                or "UNSPECIFIED_BLIND_BENCHMARK"
            ),
            "gold_lane_role": "PRIVATE_POST_RUN_EVALUATION",
            "production_lane_role": "CANONICAL_BLIND_RUN",
            "gold_fact_count": len(gold_facts),
            "production_fact_count": len(production_facts),
            "post_run_semantic_adjudication": (
                dict(semantic_adjudication["audit"])
                if semantic_adjudication is not None
                else {
                    "status": "NOT_PROVIDED_EXACT_CANONICAL_MATCH_ONLY",
                    "score_or_stage_authority": False,
                }
            ),
            "qualified_material_fact_match_count": len(qualified),
            "noncritical_fact_count": len(noncritical),
            "noncritical_fact_recall": round(noncritical_recall, 6),
            "required_gold_routes": sorted(REQUIRED_GOLD_ROUTES),
            "observed_gold_routes": sorted(routes),
            "missing_gold_routes": missing_routes,
            "lane_isolation": {
                "gold_root_hash": stable_hash(str(gold)),
                "production_root_hash": stable_hash(str(production)),
                "roots_are_disjoint": True,
                "gold_visibility_during_production": False,
                "comparison_timing": "POST_RUN_ONLY",
            },
            "leakage_audit": leakage,
            "comparisons": [row.to_dict() for row in comparisons],
            "critical_counts": critical_counts,
            "critical_count_sum": critical_sum,
        }
        return BlindResearchBenchmarkResult(
            status=status,
            comparisons=comparisons,
            audit=audit,
        )

    def write(
        self,
        *,
        result: BlindResearchBenchmarkResult,
        comparison_path: str | Path,
        audit_path: str | Path,
    ) -> None:
        write_jsonl(
            Path(comparison_path),
            (row.to_dict() for row in result.comparisons),
        )
        write_json(Path(audit_path), result.audit)

    def write_dossier_leaves(
        self,
        *,
        result: BlindResearchBenchmarkResult,
        gold_root: str | Path,
        production_root: str | Path,
        dossier_roots: Mapping[str, str | Path],
    ) -> Mapping[str, Mapping[str, Path]]:
        gold_facts = _read_jsonl(Path(gold_root) / GOLD_FACT_FILE)
        production_facts = _read_jsonl(
            Path(production_root) / PRODUCTION_FACT_FILE
        )
        paths: dict[str, Mapping[str, Path]] = {}
        for target_id, dossier_root in dossier_roots.items():
            root = Path(dossier_root)
            target_gold = tuple(
                row
                for row in gold_facts
                if str(row.get("target_id") or "") == str(target_id)
            )
            target_production = tuple(
                row
                for row in production_facts
                if str(row.get("target_id") or "") == str(target_id)
            )
            target_comparisons = tuple(
                row.to_dict()
                for row in result.comparisons
                if row.target_id == str(target_id)
            )
            if not target_gold or not target_production or not target_comparisons:
                raise ValueError(
                    f"dossier material-fact leaves are empty for target {target_id}"
                )
            target_paths = {
                "gold": root / GOLD_FACT_FILE,
                "production": root / PRODUCTION_FACT_FILE,
                "comparison": root / "material_fact_comparison.jsonl",
            }
            write_jsonl(target_paths["gold"], target_gold)
            write_jsonl(target_paths["production"], target_production)
            write_jsonl(target_paths["comparison"], target_comparisons)
            paths[str(target_id)] = target_paths
        return paths


def _compare_material_facts(
    gold_facts: Sequence[Mapping[str, Any]],
    production_facts: Sequence[Mapping[str, Any]],
    *,
    semantic_adjudication: Mapping[str, Any] | None = None,
) -> tuple[MaterialFactComparison, ...]:
    production_by_id = {
        str(row["fact_id"]): row for row in production_facts
    }
    production_by_key: dict[str, list[Mapping[str, Any]]] = {}
    for row in production_facts:
        production_by_key.setdefault(_semantic_fact_key(row), []).append(row)
    adjudication_by_gold_id = (
        dict(semantic_adjudication["rows"])
        if semantic_adjudication is not None
        else {}
    )
    used_production_ids: set[str] = set()
    comparisons = []
    for gold in gold_facts:
        gold_fact_id = str(gold["fact_id"])
        adjudicated = adjudication_by_gold_id.get(gold_fact_id)
        if adjudicated is None:
            candidates = [
                row
                for row in production_by_key.get(_semantic_fact_key(gold), ())
                if str(row["fact_id"]) not in used_production_ids
            ]
            production_rows = (
                (min(candidates, key=_candidate_rank),)
                if candidates
                else ()
            )
            semantic_match = bool(production_rows)
            mechanism_match = bool(
                production_rows
                and production_rows[0].get("mechanism_scope_id")
                == gold.get("mechanism_scope_id")
            )
            semantic_match_method = "EXACT_CANONICAL_SEMANTIC_KEY"
        else:
            production_fact_ids = tuple(adjudicated["production_fact_ids"])
            production_rows = tuple(
                production_by_id[production_fact_id]
                for production_fact_id in production_fact_ids
            )
            semantic_match = bool(adjudicated["semantic_match"])
            mechanism_match = bool(
                semantic_match and adjudicated["mechanism_scope_match"]
            )
            semantic_match_method = (
                "POST_RUN_INDEPENDENT_SEMANTIC_ADJUDICATION"
            )
        selected_production_ids = tuple(
            str(row["fact_id"]) for row in production_rows
        )
        if used_production_ids.intersection(selected_production_ids):
            raise ValueError(
                "post-run semantic adjudication reuses a production fact"
            )
        used_production_ids.update(selected_production_ids)
        production = production_rows[0] if production_rows else None
        source_match = bool(
            production_rows
            and all(
                _source_rank(str(row["source_tier"]))
                <= _source_rank(str(gold["source_tier"]))
                for row in production_rows
            )
        )
        currentness_match = bool(
            production_rows
            and all(
                row.get("temporal_status") == "CURRENT"
                and row.get("as_of_date") == gold.get("as_of_date")
                for row in production_rows
            )
        )
        comparisons.append(
            MaterialFactComparison(
                question_family_id=str(gold["question_family_id"]),
                gold_fact_id=str(gold["fact_id"]),
                production_fact_id=(
                    str(production["fact_id"])
                    if production is not None
                    else None
                ),
                semantic_match=semantic_match,
                source_quality_match=source_match,
                currentness_match=currentness_match,
                mechanism_scope_match=mechanism_match,
                materiality=str(gold["materiality"]),
                miss_reason=_miss_reason(
                    semantic=semantic_match,
                    source=source_match,
                    current=currentness_match,
                    mechanism=mechanism_match,
                ),
                fact_role=str(gold["fact_role"]),
                target_id=str(gold["target_id"]),
                production_fact_ids=selected_production_ids,
                semantic_match_method=semantic_match_method,
            )
        )
    return tuple(comparisons)


def _load_post_run_semantic_adjudication(
    *,
    root: Path | None,
    gold_facts: Sequence[Mapping[str, Any]],
    production_facts: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any] | None:
    if root is None:
        return None
    primary_path = root / POST_RUN_SEMANTIC_PRIMARY_FILE
    review_root = root / POST_RUN_SEMANTIC_REVIEW_DIRECTORY
    if not primary_path.is_file() and not review_root.exists():
        return None
    if not primary_path.is_file() or not review_root.is_dir():
        raise ValueError(
            "post-run semantic adjudication requires primary and review files"
        )
    primary = _read_json(primary_path)
    if (
        primary.get("schema_version")
        != POST_RUN_SEMANTIC_PRIMARY_SCHEMA_VERSION
        or primary.get("gold_visible_only_post_run") is not True
        or primary.get("score_or_stage_authority") is not False
        or primary.get("production_score_authority") is not False
    ):
        raise ValueError("post-run semantic primary contract is invalid")
    primary_reviewer_identity = _validated_post_run_reviewer_identity(
        primary.get("reviewer_identity"),
        expected_role_id="CODEX_POST_RUN_PRIMARY",
    )
    primary_reviewer_id = primary_reviewer_identity["role_id"]
    gold_ids = tuple(str(row["fact_id"]) for row in gold_facts)
    production_ids = tuple(str(row["fact_id"]) for row in production_facts)
    if primary.get("gold_fact_roster_hash") != stable_hash(sorted(gold_ids)):
        raise ValueError("post-run semantic Gold roster hash mismatch")
    if primary.get("production_fact_roster_hash") != stable_hash(
        sorted(production_ids)
    ):
        raise ValueError("post-run semantic production roster hash mismatch")
    primary_rows = primary.get("rows")
    if not isinstance(primary_rows, list):
        raise ValueError("post-run semantic primary rows are missing")
    _require_unique(primary_rows, "gold_fact_id")
    if {str(row["gold_fact_id"]) for row in primary_rows} != set(gold_ids):
        raise ValueError("post-run semantic primary Gold roster is inexact")
    gold_by_id = {str(row["fact_id"]): row for row in gold_facts}
    production_by_id = {
        str(row["fact_id"]): row for row in production_facts
    }
    used_production_ids: set[str] = set()
    normalized_rows: dict[str, Mapping[str, Any]] = {}
    for row in primary_rows:
        gold_fact_id = str(row["gold_fact_id"])
        production_fact_ids_raw = row.get("production_fact_ids")
        if not isinstance(production_fact_ids_raw, list):
            raise ValueError(
                "post-run semantic production fact ids must be a list"
            )
        production_fact_ids = tuple(
            str(value).strip() for value in production_fact_ids_raw
        )
        if (
            any(not value for value in production_fact_ids)
            or len(production_fact_ids) != len(set(production_fact_ids))
        ):
            raise ValueError(
                "post-run semantic production fact ids are invalid"
            )
        semantic_match = row.get("semantic_match")
        mechanism_scope_match = row.get("mechanism_scope_match")
        rationale = str(row.get("rationale") or "").strip()
        if (
            not isinstance(semantic_match, bool)
            or not isinstance(mechanism_scope_match, bool)
            or not rationale
        ):
            raise ValueError("post-run semantic primary row is invalid")
        if semantic_match != mechanism_scope_match:
            raise ValueError(
                "post-run semantic and mechanism decisions must agree"
            )
        if semantic_match != bool(production_fact_ids):
            raise ValueError(
                "post-run semantic match requires an exact production fact set"
            )
        gold = gold_by_id[gold_fact_id]
        for production_fact_id in production_fact_ids:
            production = production_by_id.get(production_fact_id)
            if production is None:
                raise ValueError(
                    "post-run semantic production fact id is unknown"
                )
            if str(production["target_id"]) != str(gold["target_id"]):
                raise ValueError(
                    "post-run semantic mapping crosses target boundaries"
                )
        if used_production_ids.intersection(production_fact_ids):
            raise ValueError(
                "post-run semantic primary reuses a production fact"
            )
        used_production_ids.update(production_fact_ids)
        normalized_rows[gold_fact_id] = {
            "production_fact_ids": production_fact_ids,
            "semantic_match": semantic_match,
            "mechanism_scope_match": mechanism_scope_match,
            "rationale": rationale,
        }
    primary_payload_hash = stable_hash(primary)
    review_paths = sorted(review_root.glob("*.json"))
    if len(review_paths) < MINIMUM_INDEPENDENT_SEMANTIC_REVIEW_COUNT:
        raise ValueError(
            "post-run semantic adjudication lacks independent reviews"
        )
    reviewer_ids: list[str] = []
    reviewer_identities: list[Mapping[str, str]] = []
    provider_call_ids = {primary_reviewer_identity["provider_call_id"]}
    identity_hashes = {primary_reviewer_identity["identity_hash"]}
    approval_by_gold_id = {gold_fact_id: 0 for gold_fact_id in gold_ids}
    for review_path in review_paths:
        review = _read_json(review_path)
        if (
            review.get("schema_version")
            != POST_RUN_SEMANTIC_REVIEW_SCHEMA_VERSION
            or review.get("primary_payload_hash") != primary_payload_hash
            or review.get("gold_visible_only_post_run") is not True
            or review.get("score_or_stage_authority") is not False
            or review.get("production_score_authority") is not False
        ):
            raise ValueError("post-run semantic review contract is invalid")
        reviewer_identity = _validated_post_run_reviewer_identity(
            review.get("reviewer_identity")
        )
        reviewer_id = reviewer_identity["role_id"]
        if (
            reviewer_id == primary_reviewer_id
            or reviewer_id in reviewer_ids
            or reviewer_identity["provider_call_id"] in provider_call_ids
            or reviewer_identity["identity_hash"] in identity_hashes
        ):
            raise ValueError("post-run semantic reviewer identity is invalid")
        reviewer_ids.append(reviewer_id)
        reviewer_identities.append(reviewer_identity)
        provider_call_ids.add(reviewer_identity["provider_call_id"])
        identity_hashes.add(reviewer_identity["identity_hash"])
        review_rows = review.get("rows")
        if not isinstance(review_rows, list):
            raise ValueError("post-run semantic review rows are missing")
        _require_unique(review_rows, "gold_fact_id")
        if {str(row["gold_fact_id"]) for row in review_rows} != set(gold_ids):
            raise ValueError("post-run semantic review Gold roster is inexact")
        for row in review_rows:
            if not isinstance(row.get("approve"), bool) or not str(
                row.get("rationale") or ""
            ).strip():
                raise ValueError("post-run semantic review row is invalid")
            if row["approve"]:
                approval_by_gold_id[str(row["gold_fact_id"])] += 1
    accepted_rows = {}
    for gold_fact_id, row in normalized_rows.items():
        accepted = (
            len(reviewer_ids)
            >= MINIMUM_INDEPENDENT_SEMANTIC_REVIEW_COUNT
            and approval_by_gold_id[gold_fact_id] == len(reviewer_ids)
        )
        accepted_rows[gold_fact_id] = {
            **row,
            "production_fact_ids": (
                row["production_fact_ids"]
                if accepted and row["semantic_match"]
                else ()
            ),
            "semantic_match": bool(accepted and row["semantic_match"]),
            "mechanism_scope_match": bool(
                accepted and row["mechanism_scope_match"]
            ),
        }
    return {
        "rows": accepted_rows,
        "audit": {
            "status": "POST_RUN_INDEPENDENT_SEMANTIC_ADJUDICATION_VALID",
            "semantic_match_contract": dict(
                POST_RUN_SEMANTIC_MATCH_CONTRACT
            ),
            "primary_reviewer_id": primary_reviewer_id,
            "primary_reviewer_identity": dict(primary_reviewer_identity),
            "independent_reviewer_ids": reviewer_ids,
            "independent_reviewer_identities": [
                dict(row) for row in reviewer_identities
            ],
            "independent_review_count": len(reviewer_ids),
            "minimum_independent_review_count": (
                MINIMUM_INDEPENDENT_SEMANTIC_REVIEW_COUNT
            ),
            "primary_payload_hash": primary_payload_hash,
            "gold_fact_roster_hash": primary["gold_fact_roster_hash"],
            "production_fact_roster_hash": (
                primary["production_fact_roster_hash"]
            ),
            "approved_gold_fact_count": sum(
                row["semantic_match"] for row in accepted_rows.values()
            ),
            "score_or_stage_authority": False,
            "gold_visible_only_post_run": True,
        },
    }


def _semantic_fact_key(row: Mapping[str, Any]) -> str:
    return stable_hash(
        {
            "target_id": str(row.get("target_id") or "").casefold(),
            "question_family_id": str(
                row.get("question_family_id") or ""
            ).casefold(),
            "subject_id": str(row.get("subject_id") or "").casefold(),
            "predicate_family": str(
                row.get("predicate_family") or ""
            ).casefold(),
            "normalized_object": str(
                row.get("normalized_object") or ""
            ).casefold(),
            "period": str(row.get("period") or "").casefold(),
        }
    )


def _candidate_rank(row: Mapping[str, Any]) -> tuple[int, int, str]:
    return (
        int(row.get("temporal_status") != "CURRENT"),
        _source_rank(str(row.get("source_tier") or "")),
        str(row.get("fact_id") or ""),
    )


def _source_rank(source_tier: str) -> int:
    if source_tier not in SOURCE_TIER_RANK:
        raise ValueError(f"unknown material fact source tier: {source_tier}")
    return SOURCE_TIER_RANK[source_tier]


def _miss_reason(
    *, semantic: bool, source: bool, current: bool, mechanism: bool
) -> str | None:
    if not semantic:
        return "MATERIAL_SEMANTIC_FACT_NOT_FOUND"
    if not mechanism:
        return "WRONG_BUSINESS_MECHANISM"
    if not current:
        return "STALE_OR_WRONG_AS_OF_DATE"
    if not source:
        return "SOURCE_QUALITY_BELOW_GOLD"
    return None


def _audit_gold_leakage(
    *,
    gold_root: Path,
    gold_facts: Sequence[Mapping[str, Any]],
    gold_sources: Sequence[Mapping[str, Any]],
    production_inputs: Sequence[Mapping[str, Any]],
    production_lane: Mapping[str, Any],
) -> Mapping[str, Any]:
    gold_urls = {
        str(row.get("source_url") or "")
        for row in gold_sources
        if row.get("source_url")
    }
    gold_queries = {
        str(row.get("research_query") or "").strip().casefold()
        for row in gold_sources
        if row.get("research_query")
    }
    gold_fact_ids = {str(row["fact_id"]) for row in gold_facts}
    source_injections = []
    query_leaks = []
    fact_leaks = []
    for row in production_inputs:
        input_type = str(row.get("input_type") or "").upper()
        value = str(row.get("value") or "")
        origin = str(row.get("origin") or "").upper()
        path_value = str(row.get("path") or "")
        path_in_gold = bool(
            path_value
            and _is_relative_to(Path(path_value).resolve(), gold_root)
        )
        if (
            path_in_gold
            or origin.startswith("GOLD")
            or (input_type == "SEED_URL" and value in gold_urls)
        ):
            source_injections.append(str(row.get("input_id") or ""))
        if input_type == "QUERY" and value.strip().casefold() in gold_queries:
            query_leaks.append(str(row.get("input_id") or ""))
        if input_type == "PROMPT_CONTEXT" and any(
            fact_id in value for fact_id in gold_fact_ids
        ):
            fact_leaks.append(str(row.get("input_id") or ""))
    if production_lane.get("gold_visibility") is not False:
        fact_leaks.append("PRODUCTION_LANE_GOLD_VISIBILITY_NOT_FALSE")
    return {
        "gold_source_injected_into_production_count": len(source_injections),
        "gold_query_leaked_into_production_count": len(query_leaks),
        "gold_fact_leaked_into_production_prompt_count": len(fact_leaks),
        "source_injection_input_ids": source_injections,
        "query_leak_input_ids": query_leaks,
        "fact_leak_input_ids": fact_leaks,
    }


def _validate_gold_lane(
    facts: Sequence[Mapping[str, Any]],
    sources: Sequence[Mapping[str, Any]],
    coverage: Mapping[str, Any],
) -> None:
    if not facts or not sources:
        raise ValueError("gold lane requires material facts and source map")
    _require_unique(facts, "fact_id")
    _require_unique(sources, "source_id")
    source_ids = {str(row["source_id"]) for row in sources}
    required = {
        "fact_id",
        "target_id",
        "question_family_id",
        "subject_id",
        "predicate_family",
        "normalized_object",
        "period",
        "mechanism_scope_id",
        "source_id",
        "source_tier",
        "temporal_status",
        "as_of_date",
        "materiality",
        "fact_role",
    }
    for row in facts:
        missing = required - set(row)
        if missing:
            raise ValueError(f"gold material fact fields missing: {sorted(missing)}")
        if str(row["source_id"]) not in source_ids:
            raise ValueError("gold fact source lineage is missing")
        _source_rank(str(row["source_tier"]))
        if row["materiality"] not in {"CRITICAL", "NONCRITICAL"}:
            raise ValueError("unknown materiality")
        if row["fact_role"] not in {"SUPPORT", "COUNTER", "SUPERSESSION"}:
            raise ValueError("unknown material fact role")
    questions = coverage.get("questions") or ()
    if not questions:
        raise ValueError("gold question coverage is empty")
    _require_unique(questions, "question_family_id")


def _validate_production_lane(
    facts: Sequence[Mapping[str, Any]], lane: Mapping[str, Any]
) -> None:
    if lane.get("lane_role") != "PRODUCTION" or lane.get("gold_visibility") is not False:
        raise ValueError("production lane is not contract-blind")
    _require_unique(facts, "fact_id")
    for row in facts:
        _source_rank(str(row.get("source_tier") or ""))
        if row.get("discovery_origin") not in {
            "CANONICAL_PLANNER",
            "CANONICAL_SOURCE_TASK",
        }:
            raise ValueError("production fact lacks independent discovery lineage")


def _require_isolated_roots(gold: Path, production: Path) -> None:
    if gold == production or _is_relative_to(gold, production) or _is_relative_to(
        production, gold
    ):
        raise ValueError("gold and production roots must be disjoint")


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _require_unique(rows: Sequence[Mapping[str, Any]], key: str) -> None:
    values = [str(row.get(key) or "") for row in rows]
    if any(not value for value in values) or len(values) != len(set(values)):
        raise ValueError(f"{key} must be present and unique")


def _read_jsonl(path: Path) -> list[Mapping[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _read_json(path: Path) -> Mapping[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


__all__ = [
    "BlindResearchBenchmarkResult",
    "BlindResearchQualityBenchmark",
    "MaterialFactComparison",
]
