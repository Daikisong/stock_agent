"""Compile all registered research rows into the v5 Judgment Atlas."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_jsonl
from e2r.research_brain.compiler.semantic_case_compiler import (
    SemanticCompilationResult,
    compile_research_intelligence,
    discover_historical_research_paths,
)
from e2r.research_brain.corpus.research_case_linker import row_type_of
from e2r.research_brain.intelligence_schema import (
    HistoricalResearchCase,
    ParsedResearchRow,
    stable_intelligence_id,
)

from .schemas import (
    AnchorConfidence,
    HistoricalResearchJudgment,
    HistoricalScoreSchemaType,
)


ATLAS_SCHEMA_VERSION = "e2r_historical_research_judgment_atlas_v1"
ATLAS_PASS = "HISTORICAL_RESEARCH_JUDGMENT_ATLAS_PASS"
ATLAS_OUTPUT_FILES = {
    "judgments": "historical_judgments.jsonl",
    "fact_signatures": "fact_signatures.jsonl",
    "score_anchors": "score_anchors.jsonl",
    "quarantine": "quarantine.jsonl",
    "manifest": "atlas_manifest.json",
}

COMPONENT_ALIASES = {
    "eps_fcf_explosion": "eps_fcf_explosion",
    "eps_fcf": "eps_fcf_explosion",
    "earnings_visibility": "earnings_visibility",
    "visibility_quality": "earnings_visibility",
    "visibility": "earnings_visibility",
    "bottleneck_pricing": "bottleneck_pricing",
    "bottleneck_pricing_power": "bottleneck_pricing",
    "market_mispricing": "market_mispricing",
    "valuation_rerating": "valuation_rerating",
    "valuation_rerating_runway": "valuation_rerating",
    "capital_allocation": "capital_allocation",
    "information_confidence": "information_confidence",
}

SCORE_CONTAINER_KEYS = {
    "raw_component_score_breakdown",
    "component_score_breakdown",
    "component_scores",
    "component_proxy",
    "component_proxies",
    "component_ratings",
    "normalized_component_ratings",
    "normalized_component_vector",
    "score_components",
}

TOTAL_KEYS = (
    "total",
    "total_score",
    "score_total",
    "reported_total_proxy",
    "component_proxy_total",
)

FUTURE_KEY_RE = re.compile(
    r"(?:^|_)(?:mfe|mae|future|outcome|drawdown|peak_price|return)(?:_|$)",
    re.IGNORECASE,
)
URL_RE = re.compile(r"https?://[^\s)>\]\"']+")


@dataclass(frozen=True)
class HistoricalJudgmentAtlasResult:
    judgments: tuple[HistoricalResearchJudgment, ...]
    fact_signatures: tuple[Mapping[str, Any], ...]
    score_anchors: tuple[Mapping[str, Any], ...]
    quarantine: tuple[Mapping[str, Any], ...]
    audit: Mapping[str, Any]


@dataclass(frozen=True)
class _ScoreCandidate:
    row_id: str
    schema_type: str
    vector: Mapping[str, float]
    total: float | None
    mapping_confidence: str
    source_path: str


def compile_historical_judgment_atlas(
    paths: Iterable[str | Path] | None = None,
    *,
    repo_root: str | Path = ".",
    registry_contract_path: str | Path = "configs/e2r_agentic_evidence_contracts_v2.json",
    component_weight_path: str | Path = "configs/e2r_archetype_weight_profile_v2_2.json",
) -> HistoricalJudgmentAtlasResult:
    root = Path(repo_root).resolve()
    source_paths = (
        tuple(Path(path) for path in paths)
        if paths is not None
        else discover_historical_research_paths(root)
    )
    semantic = compile_research_intelligence(source_paths, repo_root=root)
    return compile_historical_judgment_atlas_from_semantic(
        semantic,
        repo_root=root,
        registry_contract_path=registry_contract_path,
        component_weight_path=component_weight_path,
    )


def compile_historical_judgment_atlas_from_semantic(
    semantic: SemanticCompilationResult,
    *,
    repo_root: str | Path = ".",
    registry_contract_path: str | Path = "configs/e2r_agentic_evidence_contracts_v2.json",
    component_weight_path: str | Path = "configs/e2r_archetype_weight_profile_v2_2.json",
) -> HistoricalJudgmentAtlasResult:
    root = Path(repo_root).resolve()
    registry_ids = _load_registry_ids(root, registry_contract_path)
    maxima = _load_component_maxima(root, component_weight_path)
    rows_by_id = {row.row_id: row for row in semantic.structured_rows}
    fact_rows: list[Mapping[str, Any]] = []
    anchor_rows: list[Mapping[str, Any]] = []
    atlas_quarantine: list[Mapping[str, Any]] = []
    judgments: list[HistoricalResearchJudgment] = []
    score_component_source_count = 0
    component_mapping_loss_count = 0

    for case in semantic.cases:
        case_rows = tuple(
            rows_by_id[row_id]
            for row_id in case.source_row_ids
            if row_id in rows_by_id
        )
        positive_signatures, counter_signatures = _compile_fact_signatures(
            case=case,
            rows=case_rows,
        )
        fact_rows.extend((*positive_signatures, *counter_signatures))
        candidates = _score_candidates(
            case=case,
            rows=case_rows,
            component_maxima=maxima[case.canonical_archetype_id],
        )
        score_component_source_count += sum(bool(row.vector) for row in candidates)
        selected, conflict = _select_score_candidate(candidates)
        if selected is None:
            schema_type = (
                HistoricalScoreSchemaType.RULE_ONLY.value
                if case.shadow_rule_refs or case.transition_refs
                else HistoricalScoreSchemaType.NO_SCORE.value
            )
            vector: Mapping[str, float] = {}
            total = None
            score_row_ids: tuple[str, ...] = ()
            mapping_confidence = "NONE"
        else:
            schema_type = selected.schema_type
            vector = dict(selected.vector)
            total = selected.total
            score_row_ids = tuple(dict.fromkeys(row.row_id for row in candidates))
            mapping_confidence = selected.mapping_confidence
            if candidates and any(row.vector for row in candidates) and not vector:
                component_mapping_loss_count += 1
        source_quality, anchor_confidence = _source_quality(case, case_rows)
        exact = bool(
            source_quality == "SOURCE_BACKED_HIGH"
            and schema_type
            in {
                HistoricalScoreSchemaType.DIRECT_COMPONENT_POINTS.value,
                HistoricalScoreSchemaType.NORMALIZED_COMPONENT_RATINGS.value,
            }
            and vector
            and not conflict
        )
        ordinal = bool(
            vector
            or total is not None
            or schema_type == HistoricalScoreSchemaType.RULE_ONLY.value
        )
        positive_ids = tuple(row["fact_signature_id"] for row in positive_signatures)
        counter_ids = tuple(row["fact_signature_id"] for row in counter_signatures)
        judgment = HistoricalResearchJudgment(
            judgment_id=stable_intelligence_id(
                "HJDG",
                {
                    "case_id": case.case_id,
                    "schema_type": schema_type,
                    "vector": vector,
                    "score_rows": score_row_ids,
                },
            ),
            research_case_id=case.case_id,
            archetype_id=case.canonical_archetype_id,
            as_of_date=case.trigger_date or case.entry_date,
            source_quality=source_quality,
            fact_signatures=positive_ids,
            counter_fact_signatures=counter_ids,
            score_schema_type=schema_type,
            normalized_component_vector=vector,
            component_max_points=maxima[case.canonical_archetype_id],
            reported_total_proxy=total,
            reported_stage=case.trigger_type,
            future_outcome_ref=case.price_metrics_ref,
            usable_as_exact_anchor=exact,
            usable_as_ordinal_anchor=ordinal,
            anchor_confidence=(
                AnchorConfidence.HIGH.value if exact else anchor_confidence
            ),
            company_name=case.company_name,
            symbol=case.symbol,
            source_file=case.source_file,
            source_row_ids=case.source_row_ids,
            score_source_row_ids=score_row_ids,
            score_mapping_confidence=mapping_confidence,
            score_conflict=conflict,
        )
        judgments.append(judgment)
        anchor_rows.extend(_score_anchor_rows(judgment, case))
        if conflict:
            atlas_quarantine.append(
                {
                    "quarantine_id": stable_intelligence_id(
                        "HJQ", {"case_id": case.case_id, "reason": "CONFLICTING_SCORE_ROWS"}
                    ),
                    "reason": "CONFLICTING_SCORE_ROWS",
                    "research_case_id": case.case_id,
                    "source_file": case.source_file,
                    "score_candidates": [_candidate_dict(row) for row in candidates],
                    "exact_anchor_allowed": False,
                }
            )

    accounting, preserved_rows = _structured_row_accounting(semantic)
    atlas_quarantine.extend(preserved_rows)
    atlas_quarantine.extend(
        {
            "quarantine_id": row.quarantine_id,
            "reason": row.reason,
            "source_file": row.source_file,
            "source_line_range": row.source_line_range.to_dict(),
            "source_row_id": row.row_id,
            "details": dict(row.details),
            "compiler_quarantine": True,
        }
        for row in semantic.quarantine
    )

    judgments = sorted(judgments, key=lambda row: (row.archetype_id, row.research_case_id))
    fact_rows = sorted(
        _dedupe_mapping_rows(fact_rows, "fact_signature_id"),
        key=lambda row: str(row["fact_signature_id"]),
    )
    anchor_rows = sorted(
        _dedupe_mapping_rows(anchor_rows, "anchor_id"),
        key=lambda row: str(row["anchor_id"]),
    )
    atlas_quarantine = sorted(
        _dedupe_mapping_rows(atlas_quarantine, "quarantine_id"),
        key=lambda row: str(row["quarantine_id"]),
    )
    judgment_archetypes = {row.archetype_id for row in judgments}
    schema_counts = Counter(row.score_schema_type for row in judgments)
    source_counts = Counter(row.source_quality for row in judgments)
    source_proxy_exact_count = sum(
        row.usable_as_exact_anchor and row.source_quality == "SOURCE_PROXY_ONLY"
        for row in judgments
    )
    runtime_payload_future_exposure_count = sum(
        _has_future_key(row.to_runtime_anchor()) for row in judgments
    )
    critical = {
        "structured_row_preservation_failure_count": int(
            accounting["structured_row_preservation_rate"] != 1.0
        ),
        "present_company_name_loss_count": int(
            semantic.manifest["quality"]["present_company_name_loss_count"]
        ),
        "present_trigger_date_loss_count": int(
            semantic.manifest["quality"]["present_trigger_date_loss_count"]
        ),
        "component_mapping_loss_count": component_mapping_loss_count,
        "schema_type_unknown_without_quarantine_count": 0,
        "source_proxy_exact_anchor_promotion_count": source_proxy_exact_count,
        "future_outcome_current_prompt_exposure_count": runtime_payload_future_exposure_count,
        "registry_archetype_coverage_gap_count": len(registry_ids - judgment_archetypes),
        "unregistered_judgment_archetype_count": len(judgment_archetypes - registry_ids),
    }
    audit = {
        "schema_version": ATLAS_SCHEMA_VERSION,
        "status": ATLAS_PASS if sum(critical.values()) == 0 else "HISTORICAL_RESEARCH_JUDGMENT_ATLAS_FAIL",
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "source_compile_status": semantic.manifest["status"],
        "source_corpus_hash": semantic.manifest["corpus_hash"],
        "registered_artifact_count": len(semantic.artifacts),
        "structured_row_count": len(semantic.structured_rows),
        "historical_case_count": len(semantic.cases),
        "judgment_count": len(judgments),
        "fact_signature_count": len(fact_rows),
        "score_anchor_count": len(anchor_rows),
        "atlas_quarantine_count": len(atlas_quarantine),
        "score_component_source_count": score_component_source_count,
        "score_schema_type_counts": dict(sorted(schema_counts.items())),
        "source_quality_counts": dict(sorted(source_counts.items())),
        "exact_anchor_count": sum(row.usable_as_exact_anchor for row in judgments),
        "ordinal_anchor_count": sum(row.usable_as_ordinal_anchor for row in judgments),
        "registry_archetype_count": len(registry_ids),
        "covered_registry_archetype_count": len(registry_ids & judgment_archetypes),
        "registry_archetype_coverage_rate": round(
            len(registry_ids & judgment_archetypes) / len(registry_ids), 6
        ),
        "structured_row_accounting": accounting,
        "runtime_outcome_payload_allowed": False,
        "future_outcome_evaluator_only": True,
        "judgment_hash": stable_hash([row.to_dict() for row in judgments]),
        "fact_signature_hash": stable_hash(fact_rows),
        "score_anchor_hash": stable_hash(anchor_rows),
    }
    return HistoricalJudgmentAtlasResult(
        judgments=tuple(judgments),
        fact_signatures=tuple(fact_rows),
        score_anchors=tuple(anchor_rows),
        quarantine=tuple(atlas_quarantine),
        audit=audit,
    )


def write_historical_judgment_atlas(
    result: HistoricalJudgmentAtlasResult,
    *,
    output_root: str | Path = "output/researcher_parity/judgment_atlas",
    audit_path: str | Path = "docs/operational/e2r_v5_historical_judgment_atlas_audit.json",
) -> Mapping[str, Path]:
    root = Path(output_root)
    paths = {key: root / value for key, value in ATLAS_OUTPUT_FILES.items()}
    write_jsonl(paths["judgments"], (row.to_dict() for row in result.judgments))
    write_jsonl(paths["fact_signatures"], result.fact_signatures)
    write_jsonl(paths["score_anchors"], result.score_anchors)
    write_jsonl(paths["quarantine"], result.quarantine)
    write_json(paths["manifest"], dict(result.audit))
    audit_output = Path(audit_path)
    write_json(audit_output, dict(result.audit))
    return {**paths, "audit": audit_output}


def _load_registry_ids(root: Path, path: str | Path) -> set[str]:
    source = Path(path)
    source = source if source.is_absolute() else root / source
    payload = json.loads(source.read_text(encoding="utf-8"))
    ids = {
        str(row.get("archetype_id") or "")
        for row in payload.get("contracts") or ()
        if str(row.get("archetype_id") or "")
    }
    if not ids or int(payload.get("contract_count") or 0) != len(ids):
        raise ValueError("current archetype registry is empty or inconsistent")
    return ids


def _load_component_maxima(root: Path, path: str | Path) -> Mapping[str, Mapping[str, float]]:
    source = Path(path)
    source = source if source.is_absolute() else root / source
    payload = json.loads(source.read_text(encoding="utf-8"))
    rows = payload.get("archetype_weights") or {}
    result = {
        str(archetype_id): {
            str(component_id): float(value)
            for component_id, value in row["weights"].items()
        }
        for archetype_id, row in rows.items()
    }
    if any(abs(sum(values.values()) - 100.0) > 1e-6 for values in result.values()):
        raise ValueError("archetype component maxima must sum to 100")
    return result


def _score_candidates(
    *,
    case: HistoricalResearchCase,
    rows: Sequence[ParsedResearchRow],
    component_maxima: Mapping[str, float],
) -> tuple[_ScoreCandidate, ...]:
    result: list[_ScoreCandidate] = []
    for row in rows:
        mappings = _candidate_mappings(row.data, case.case_id)
        for source_path, mapping, container_hint in mappings:
            vector_raw = _canonical_vector(mapping)
            total = _first_numeric(mapping, TOTAL_KEYS)
            if not vector_raw and total is None:
                continue
            schema_type = _classify_score_schema(
                vector=vector_raw,
                mapping=mapping,
                container_hint=container_hint,
                row_type=row_type_of(row),
                component_maxima=component_maxima,
            )
            vector = _normalize_vector(
                vector_raw,
                schema_type=schema_type,
                component_maxima=component_maxima,
            )
            if total is None and vector:
                total = round(sum(vector.values()), 6)
            result.append(
                _ScoreCandidate(
                    row_id=row.row_id,
                    schema_type=schema_type,
                    vector=vector,
                    total=total,
                    mapping_confidence=(
                        "HIGH"
                        if schema_type
                        in {
                            HistoricalScoreSchemaType.DIRECT_COMPONENT_POINTS.value,
                            HistoricalScoreSchemaType.NORMALIZED_COMPONENT_RATINGS.value,
                        }
                        else "MEDIUM"
                        if schema_type == HistoricalScoreSchemaType.CUSTOM_ARCHETYPE_POINTS.value
                        else "LOW"
                    ),
                    source_path=source_path,
                )
            )
    return tuple(_dedupe_score_candidates(result))


def _candidate_mappings(
    data: Mapping[str, Any], case_id: str
) -> tuple[tuple[str, Mapping[str, Any], str], ...]:
    found: list[tuple[str, Mapping[str, Any], str]] = []

    def visit(value: Any, path: str, hint: str, depth: int) -> None:
        if depth > 4 or not isinstance(value, Mapping):
            return
        if _canonical_vector(value) or _first_numeric(value, TOTAL_KEYS) is not None:
            found.append((path or "$", value, hint))
        if case_id in value and isinstance(value[case_id], Mapping):
            visit(value[case_id], f"{path}.{case_id}", hint, depth + 1)
        for key, nested in value.items():
            normalized = str(key).lower()
            if normalized in SCORE_CONTAINER_KEYS and isinstance(nested, Mapping):
                visit(nested, f"{path}.{key}", normalized, depth + 1)

    visit(data, "$", "", 0)
    return tuple(found)


def _classify_score_schema(
    *,
    vector: Mapping[str, float],
    mapping: Mapping[str, Any],
    container_hint: str,
    row_type: str | None,
    component_maxima: Mapping[str, float],
) -> str:
    if vector:
        normalized_hint = any(
            token in container_hint for token in ("normalized", "rating", "proxy")
        )
        above_direct_max = any(
            float(value) > float(component_maxima[component_id]) + 1e-9
            for component_id, value in vector.items()
        )
        if normalized_hint or above_direct_max:
            return HistoricalScoreSchemaType.NORMALIZED_COMPONENT_RATINGS.value
        if len(vector) >= 2:
            return HistoricalScoreSchemaType.DIRECT_COMPONENT_POINTS.value
        return HistoricalScoreSchemaType.CUSTOM_ARCHETYPE_POINTS.value
    if _first_numeric(mapping, TOTAL_KEYS) is not None:
        return HistoricalScoreSchemaType.TOTAL_ONLY_PROXY.value
    if row_type and ("rule" in row_type or "weight" in row_type):
        return HistoricalScoreSchemaType.RULE_ONLY.value
    return HistoricalScoreSchemaType.NO_SCORE.value


def _normalize_vector(
    vector: Mapping[str, float],
    *,
    schema_type: str,
    component_maxima: Mapping[str, float],
) -> Mapping[str, float]:
    result = {}
    for component_id, value in vector.items():
        maximum = float(component_maxima[component_id])
        if schema_type == HistoricalScoreSchemaType.NORMALIZED_COMPONENT_RATINGS.value:
            points = (max(0.0, min(100.0, float(value))) / 100.0) * maximum
        else:
            points = max(0.0, min(maximum, float(value)))
        result[component_id] = round(points, 6)
    return result


def _canonical_vector(mapping: Mapping[str, Any]) -> Mapping[str, float]:
    result = {}
    for key, value in mapping.items():
        component_id = COMPONENT_ALIASES.get(str(key).strip().lower())
        numeric = _number(value)
        if component_id and numeric is not None:
            result[component_id] = numeric
    return result


def _select_score_candidate(
    candidates: Sequence[_ScoreCandidate],
) -> tuple[_ScoreCandidate | None, bool]:
    if not candidates:
        return None, False
    rank = {
        HistoricalScoreSchemaType.DIRECT_COMPONENT_POINTS.value: 5,
        HistoricalScoreSchemaType.NORMALIZED_COMPONENT_RATINGS.value: 4,
        HistoricalScoreSchemaType.CUSTOM_ARCHETYPE_POINTS.value: 3,
        HistoricalScoreSchemaType.TOTAL_ONLY_PROXY.value: 2,
        HistoricalScoreSchemaType.RULE_ONLY.value: 1,
        HistoricalScoreSchemaType.NO_SCORE.value: 0,
    }
    ordered = sorted(
        candidates,
        key=lambda row: (
            rank[row.schema_type],
            len(row.vector),
            row.mapping_confidence,
            row.row_id,
        ),
        reverse=True,
    )
    selected = ordered[0]
    comparable = {
        stable_hash(
            {
                "schema_type": row.schema_type,
                "vector": dict(row.vector),
                "total": row.total,
            }
        )
        for row in ordered
        if rank[row.schema_type] == rank[selected.schema_type]
    }
    return selected, len(comparable) > 1


def _compile_fact_signatures(
    *, case: HistoricalResearchCase, rows: Sequence[ParsedResearchRow]
) -> tuple[tuple[Mapping[str, Any], ...], tuple[Mapping[str, Any], ...]]:
    positive_values = list(case.positive_evidence_fields) + list(case.evidence_families)
    counter_values = (
        list(case.counter_evidence_fields)
        + list(case.false_positive_patterns)
        + list(case.hard_breaks)
        + list(case.missing_evidence_fields)
    )
    for row in rows:
        positive_values.extend(
            _field_values(
                row.data,
                (
                    "evidence_family",
                    "positive_evidence_fields",
                    "stage2_evidence_fields",
                    "stage3_evidence_fields",
                ),
            )
        )
        counter_values.extend(
            _field_values(
                row.data,
                (
                    "counter_evidence_fields",
                    "missing_evidence_fields",
                    "stage4b_evidence_fields",
                    "stage4c_evidence_fields",
                    "false_positive_patterns",
                    "hard_breaks",
                ),
            )
        )
    if case.classification.lower() in {"counterexample", "negative", "risk"}:
        counter_values.extend(positive_values)
        positive_values = []
    if not positive_values and not counter_values:
        fallback = case.case_role or case.classification
        (counter_values if "counter" in fallback.lower() else positive_values).append(fallback)
    positive = _signature_rows(case, positive_values, "POSITIVE")
    counter = _signature_rows(case, counter_values, "COUNTER")
    return positive, counter


def _signature_rows(
    case: HistoricalResearchCase, values: Sequence[Any], role: str
) -> tuple[Mapping[str, Any], ...]:
    rows = []
    for value in values:
        text = str(value or "").strip()
        if not text or FUTURE_KEY_RE.search(text):
            continue
        normalized = _normalize_fact_text(text, case)
        if not normalized:
            continue
        rows.append(
            {
                "fact_signature_id": stable_intelligence_id(
                    "HFACT",
                    {
                        "case_id": case.case_id,
                        "role": role,
                        "signature": normalized,
                    },
                ),
                "research_case_id": case.case_id,
                "archetype_id": case.canonical_archetype_id,
                "role": role,
                "economic_fact_pattern": normalized,
                "source_text": text,
                "company_name_exposed_to_matcher": False,
                "symbol_exposed_to_matcher": False,
            }
        )
    return tuple(_dedupe_mapping_rows(rows, "fact_signature_id"))


def _source_quality(
    case: HistoricalResearchCase, rows: Sequence[ParsedResearchRow]
) -> tuple[str, str]:
    declared = " ".join(
        value
        for value in (
            case.declared_source_quality or "",
            *(str(row.data.get("declared_source_quality") or "") for row in rows),
        )
        if value
    ).lower()
    proxy = any(
        _truthy(row.data.get("source_proxy_only"))
        or _truthy(row.data.get("evidence_url_pending"))
        for row in rows
    ) or any(token in declared for token in ("proxy", "pending", "price_path_only"))
    urls = tuple(ref.url for ref in case.evidence_references if ref.url)
    if proxy:
        return "SOURCE_PROXY_ONLY", AnchorConfidence.LOW.value
    if urls:
        direct = any(
            token in declared
            for token in ("official", "direct", "dart", "kind", "research_report", "issuer")
        )
        return (
            "SOURCE_BACKED_HIGH" if direct else "SOURCE_BACKED_MEDIUM",
            AnchorConfidence.HIGH.value if direct else AnchorConfidence.MEDIUM.value,
        )
    return "SHADOW_OR_UNVERIFIED", AnchorConfidence.LOW.value


def _score_anchor_rows(
    judgment: HistoricalResearchJudgment, case: HistoricalResearchCase
) -> tuple[Mapping[str, Any], ...]:
    role = (
        "COUNTER"
        if case.classification.lower() in {"counterexample", "negative", "risk"}
        or any(token in (case.trigger_type or "").lower() for token in ("4b", "4c", "red"))
        else "POSITIVE"
    )
    rows = []
    for component_id, points in judgment.normalized_component_vector.items():
        maximum = float(judgment.component_max_points[component_id])
        ratio = round(float(points) / maximum if maximum else 0.0, 6)
        band = "STRONG" if ratio >= 0.7 else "MEDIUM" if ratio >= 0.4 else "WEAK" if ratio > 0 else "ZERO"
        rows.append(
            {
                "anchor_id": stable_intelligence_id(
                    "HANCH",
                    {
                        "judgment_id": judgment.judgment_id,
                        "component_id": component_id,
                    },
                ),
                "judgment_id": judgment.judgment_id,
                "research_case_id": judgment.research_case_id,
                "archetype_id": judgment.archetype_id,
                "component_id": component_id,
                "role": role,
                "points": float(points),
                "max_points": maximum,
                "normalized_ratio": ratio,
                "score_band": band,
                "source_quality": judgment.source_quality,
                "usable_as_exact_anchor": judgment.usable_as_exact_anchor,
                "usable_as_ordinal_anchor": judgment.usable_as_ordinal_anchor,
                "anchor_confidence": judgment.anchor_confidence,
                "fact_signature_ids": list(
                    judgment.counter_fact_signatures if role == "COUNTER" else judgment.fact_signatures
                ),
            }
        )
    return tuple(rows)


def _structured_row_accounting(
    semantic: SemanticCompilationResult,
) -> tuple[Mapping[str, Any], tuple[Mapping[str, Any], ...]]:
    case_ids = {
        row_id for case in semantic.cases for row_id in case.source_row_ids
    }
    outcome_ids = {row.source_row_id for row in semantic.outcomes}
    rule_ids = {row.source_row_id for row in semantic.rules}
    counts: Counter[str] = Counter()
    preserved = []
    for row in semantic.structured_rows:
        if row.row_id in case_ids:
            role = "CASE_JUDGMENT_LINEAGE"
        elif row.row_id in outcome_ids:
            role = "EVALUATOR_ONLY_OUTCOME"
        elif row.row_id in rule_ids:
            role = "RULE_ONLY"
        else:
            role = "PRESERVED_NON_JUDGMENT_ROW"
        counts[role] += 1
        if role != "CASE_JUDGMENT_LINEAGE":
            preserved.append(
                {
                    "quarantine_id": stable_intelligence_id(
                        "HJQ", {"row_id": row.row_id, "role": role}
                    ),
                    "reason": role,
                    "source_row_id": row.row_id,
                    "source_file": row.source_file,
                    "source_line_range": row.source_line_range.to_dict(),
                    "row_type": row_type_of(row),
                    "row_kind": row.row_kind,
                    "data_sha256": hashlib.sha256(
                        json.dumps(
                            row.data,
                            ensure_ascii=False,
                            sort_keys=True,
                            default=str,
                        ).encode("utf-8")
                    ).hexdigest(),
                    "preserved_in_source_corpus": True,
                    "runtime_anchor_allowed": False,
                }
            )
    total = len(semantic.structured_rows)
    accounted = sum(counts.values())
    return (
        {
            "structured_row_count": total,
            "accounted_structured_row_count": accounted,
            "structured_row_preservation_rate": round(accounted / total if total else 1.0, 6),
            "accounting_role_counts": dict(sorted(counts.items())),
        },
        tuple(preserved),
    )


def _candidate_dict(row: _ScoreCandidate) -> Mapping[str, Any]:
    return {
        "row_id": row.row_id,
        "schema_type": row.schema_type,
        "vector": dict(row.vector),
        "total": row.total,
        "mapping_confidence": row.mapping_confidence,
        "source_path": row.source_path,
    }


def _field_values(data: Mapping[str, Any], keys: Sequence[str]) -> list[Any]:
    result = []
    for key in keys:
        value = data.get(key)
        if isinstance(value, (list, tuple, set)):
            result.extend(value)
        elif value not in (None, ""):
            result.append(value)
    return result


def _normalize_fact_text(text: str, case: HistoricalResearchCase) -> str:
    value = URL_RE.sub(" ", text.casefold())
    for target_specific in (case.company_name.casefold(), case.symbol.casefold()):
        if target_specific:
            value = value.replace(target_specific, " ")
    value = re.sub(r"[^0-9a-z가-힣]+", "_", value).strip("_")
    return value[:500]


def _first_numeric(mapping: Mapping[str, Any], keys: Sequence[str]) -> float | None:
    for key in keys:
        value = _number(mapping.get(key))
        if value is not None:
            return value
    return None


def _number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        cleaned = value.strip().replace(",", "").rstrip("%")
        try:
            return float(cleaned)
        except ValueError:
            return None
    return None


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    return str(value or "").strip().lower() in {"true", "1", "yes", "y"}


def _dedupe_score_candidates(
    rows: Sequence[_ScoreCandidate],
) -> tuple[_ScoreCandidate, ...]:
    result = {}
    for row in rows:
        key = stable_hash(_candidate_dict(row))
        result[key] = row
    return tuple(result[key] for key in sorted(result))


def _dedupe_mapping_rows(
    rows: Iterable[Mapping[str, Any]], key: str
) -> list[Mapping[str, Any]]:
    result = {}
    for row in rows:
        identity = str(row.get(key) or stable_hash(row))
        result.setdefault(identity, row)
    return list(result.values())


def _has_future_key(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(
            FUTURE_KEY_RE.search(str(key)) or _has_future_key(item)
            for key, item in value.items()
        )
    if isinstance(value, (list, tuple)):
        return any(_has_future_key(item) for item in value)
    return False


__all__ = [
    "ATLAS_OUTPUT_FILES",
    "ATLAS_PASS",
    "ATLAS_SCHEMA_VERSION",
    "HistoricalJudgmentAtlasResult",
    "compile_historical_judgment_atlas",
    "compile_historical_judgment_atlas_from_semantic",
    "write_historical_judgment_atlas",
]
