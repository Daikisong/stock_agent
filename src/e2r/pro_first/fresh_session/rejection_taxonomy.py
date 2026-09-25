"""Reconstruct and classify every rejection from a frozen Pro V2 run.

The old runtime remains outside Git.  This module reduces its append-only
snapshot history to a copyright-safe diagnostic receipt: identifiers, root
causes, routing decisions, and aggregate counts only.  Statements and source
excerpts are deliberately not copied into the tracked report.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import re
from typing import Any, Mapping, Sequence
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from ..ids import canonical_hash, stable_id


INITIAL_PROMPT_OUTPUT_DEFECT = "INITIAL_PROMPT_OUTPUT_DEFECT"
LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT = (
    "LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT"
)
GENUINE_SEMANTIC_OR_SOURCE_DEFECT = "GENUINE_SEMANTIC_OR_SOURCE_DEFECT"

_FACT_COLLECTIONS = ("material_facts", "counterfacts", "resolution_facts")
_TRACKING_QUERY_KEYS = frozenset(
    {
        "fbclid",
        "gclid",
        "mc_cid",
        "mc_eid",
        "ref",
        "source",
    }
)


@dataclass(frozen=True)
class _RootCause:
    root_cause_class: str
    root_cause_code: str
    root_cause_detail: str
    could_be_fixed_locally: bool
    requires_new_public_search: bool
    requires_pro_semantic_repair: bool
    generic_fix_file: str
    generic_fix_function: str
    regression_test_id: str


def build_old_run_rejection_taxonomy(
    job_root: str | Path,
) -> Mapping[str, Any]:
    """Build one deterministic A/B/C audit from all durable dossier snapshots."""

    root = Path(job_root).resolve()
    snapshot_paths = _snapshot_paths(root)
    if not snapshot_paths:
        raise ValueError("old rejection audit requires durable dossier snapshots")

    register_history: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    fact_versions: dict[str, list[tuple[str, Mapping[str, Any]]]] = defaultdict(list)
    raw_register_row_count = 0
    for path in snapshot_paths:
        dossier = _load_object(path)
        for register_row in dossier.get("verification_repair_register") or ():
            candidate_id = str(register_row.get("candidate_id") or "")
            if not candidate_id:
                raise ValueError("verification repair row lacks candidate_id")
            register_history[candidate_id].append(dict(register_row))
            raw_register_row_count += 1
        for collection in _FACT_COLLECTIONS:
            for fact in dossier.get(collection) or ():
                candidate_id = str(fact.get("dossier_fact_id") or "")
                if candidate_id:
                    fact_versions[candidate_id].append((collection, dict(fact)))

    rows: list[dict[str, Any]] = []
    for candidate_id in sorted(register_history):
        history = register_history[candidate_id]
        categories = {
            str(item.get("rejection_category") or "") for item in history
        }
        if len(categories) != 1 or "" in categories:
            raise ValueError(
                f"candidate rejection category is not immutable: {candidate_id}"
            )
        original_hashes = {
            str(item.get("original_candidate_hash") or "") for item in history
        }
        if len(original_hashes) != 1 or "" in original_hashes:
            raise ValueError(
                f"candidate original hash is not immutable: {candidate_id}"
            )
        original_hash = next(iter(original_hashes))
        matching_facts = [
            (collection, fact)
            for collection, fact in fact_versions.get(candidate_id, ())
            if canonical_hash(fact) == original_hash
        ]
        if not matching_facts:
            raise ValueError(
                f"rejected candidate lacks its hash-bound original fact: {candidate_id}"
            )
        collections = {collection for collection, _ in matching_facts}
        if len(collections) != 1:
            raise ValueError(
                f"candidate changed fact collection across snapshots: {candidate_id}"
            )
        collection, fact = matching_facts[0]
        category = next(iter(categories))
        cause = _classify_root_cause(
            category=category,
            fact=fact,
            fact_collection=collection,
        )
        source_url = str(fact.get("source_url") or fact.get("url") or "")
        canonical_source_url = _canonical_source_url(source_url)
        source_document_id = stable_id(
            "OLDPRODOC", {"canonical_source_url": canonical_source_url}
        )
        question_family_ids = sorted(
            {
                str(value)
                for value in (
                    *(fact.get("question_family_ids") or ()),
                    *(
                        item.get("question_family_id")
                        for item in history
                    ),
                )
                if str(value or "").strip()
            }
        )
        first = history[0]
        latest = history[-1]
        row = {
            "candidate_id": candidate_id,
            "question_family_ids": question_family_ids,
            "rejection_category": category,
            "root_cause_class": cause.root_cause_class,
            "root_cause_code": cause.root_cause_code,
            "root_cause_detail": cause.root_cause_detail,
            "source_document_id": source_document_id,
            "could_be_fixed_locally": cause.could_be_fixed_locally,
            "requires_new_public_search": cause.requires_new_public_search,
            "requires_pro_semantic_repair": cause.requires_pro_semantic_repair,
            "generic_fix_file": cause.generic_fix_file,
            "generic_fix_function": cause.generic_fix_function,
            "regression_test_id": cause.regression_test_id,
            "fact_collection": collection,
            "source_lineage_id": str(fact.get("source_lineage_id") or ""),
            "canonical_source_url": canonical_source_url,
            "original_candidate_hash": original_hash,
            "first_repair_status": str(first.get("status") or ""),
            "latest_repair_status": str(latest.get("status") or ""),
            "replacement_candidate_ids": sorted(
                {
                    str(item.get("replacement_candidate_id") or "")
                    for item in history
                    if str(item.get("replacement_candidate_id") or "")
                }
            ),
            "history_row_count": len(history),
        }
        row["repair_group_key"] = canonical_hash(
            {
                "source_document_id": source_document_id,
                "root_cause_code": cause.root_cause_code,
                "question_family_ids": question_family_ids,
            }
        )
        rows.append(row)

    aggregates = _aggregate(rows)
    payload: dict[str, Any] = {
        "schema_version": "e2r_pro_old_rejection_taxonomy_v1",
        "source_job_id": _single_job_id(snapshot_paths),
        "source_snapshot_file_count": len(snapshot_paths),
        "raw_append_only_register_row_count": raw_register_row_count,
        "classification_policy": {
            "A": INITIAL_PROMPT_OUTPUT_DEFECT,
            "B": LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT,
            "C": GENUINE_SEMANTIC_OR_SOURCE_DEFECT,
            "candidate_identity": "candidate_id + original_candidate_hash",
            "source_document_identity": "canonical URL hash; source text excluded",
            "duplicate_mechanical_definition": (
                "B rows after the first row in the same source/root-cause group"
            ),
            "genuine_semantic_definition": "rows classified as C after A/B checks",
        },
        "aggregates": aggregates,
        "rows": rows,
        "score_authority": False,
        "stage_authority": False,
        "old_run_disposition": "DIAGNOSTIC_ONLY_FROZEN",
    }
    payload["audit_hash"] = canonical_hash(payload)
    return payload


def render_old_run_rejection_taxonomy_markdown(
    payload: Mapping[str, Any],
) -> str:
    aggregates = payload["aggregates"]
    class_counts = aggregates["root_cause_class_counts"]
    class_ratios = aggregates["root_cause_class_ratios"]
    lines = [
        "# Old Pro V2 반려 원인 전수 감사",
        "",
        "이 문서는 봉인된 repair-heavy 실행의 원문을 Git에 복사하지 않고, "
        "hash로 결박된 반려 후보의 원인과 수정 경로만 기록한다.",
        "",
        "## 결론",
        "",
        f"- 고유 반려 후보: **{aggregates['total_rejection_count']}개**",
        f"- A 최초 출력 계약 결함: **{class_counts[INITIAL_PROMPT_OUTPUT_DEFECT]}개 "
        f"({class_ratios[INITIAL_PROMPT_OUTPUT_DEFECT]:.2%})**",
        f"- B 로컬 정규화·검문 결함: **{class_counts[LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT]}개 "
        f"({class_ratios[LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT]:.2%})**",
        f"- C 실제 의미·source 결함: **{class_counts[GENUINE_SEMANTIC_OR_SOURCE_DEFECT]}개 "
        f"({class_ratios[GENUINE_SEMANTIC_OR_SOURCE_DEFECT]:.2%})**",
        f"- 같은 source가 반복된 반려 후보: **{aggregates['same_source_grouped_rejection_count']}개** "
        f"/ source group **{aggregates['same_source_group_count']}개**",
        f"- 중복 기계 반려: **{aggregates['duplicate_mechanical_rejection_count']}개**",
        f"- 실제 Pro 의미 수리 대상: **{aggregates['actual_genuine_semantic_repair_count']}개**",
        "",
        "쉬운 예: `resolution_facts`인데 lifecycle이 `UNKNOWN`이면 자료 부족으로 "
        "다시 검색할 문제가 아니다. V3 출력 계약이 terminal lifecycle을 반드시 "
        "요구해야 하는 A 결함이다. 반대로 peer fact가 `issuer_scoped=false`인데 "
        "한·영 subject label 차이로 거절되면 Pro에게 다시 묻지 않고 로컬 alias "
        "resolver가 처리해야 하는 B 결함이다.",
        "",
        "## 집계 정의",
        "",
        "- `total`: append-only register 302행을 candidate ID와 원본 hash로 "
        "중복 제거한 수다.",
        "- `same-source grouped`: 같은 canonical source document에서 반려가 둘 "
        "이상 발생한 경우 그 후보 전체 수다.",
        "- `duplicate mechanical`: B 후보를 source document + root cause + question "
        "roster와 무관하게 묶었을 때 첫 후보 뒤에 반복된 수다. question roster까지 "
        "포함한 실제 repair 압축 수치는 JSON의 `repair_group_*`에 별도로 둔다.",
        "- old run에서 A의 `requires_pro_semantic_repair=true`는 old 계약을 그대로 "
        "유지했다면 Pro correction이 필요했다는 반사실적 routing이다. 실제 old "
        "conversation은 봉인했으며, fresh run 전 Prompt/Dossier V3를 먼저 고친다.",
        "- fresh run에서는 A/B를 먼저 제거한 뒤 남는 C만 compact Pro semantic "
        "repair로 보낸다.",
        "- C가 0이라는 결과는 old 후보가 모두 의미적으로 옳다는 선언이 아니다. "
        "old verifier가 A/B 단계에서 먼저 막았으므로, A/B 수정 뒤의 fresh "
        "reverification이 실제 C를 새로 드러낼 수 있다.",
        "",
        "## 원인 코드 집계",
        "",
        "| 원인 코드 | A/B/C | 후보 수 |",
        "| --- | --- | ---: |",
    ]
    by_code = aggregates["root_cause_code_counts"]
    code_classes = {
        row["root_cause_code"]: row["root_cause_class"]
        for row in payload["rows"]
    }
    for code, count in sorted(by_code.items()):
        lines.append(f"| `{code}` | `{code_classes[code]}` | {count} |")
    lines.extend(
        [
            "",
            "## 후보별 판정",
            "",
            "원문 statement·quote는 runtime에만 보존한다. 이 표는 외부 검수가 "
            "가능한 식별자·원인·routing만 싣는다.",
            "",
            "| candidate | category | A/B/C | 원인 코드 | source document | local | Pro repair |",
            "| --- | --- | --- | --- | --- | ---: | ---: |",
        ]
    )
    for row in payload["rows"]:
        short_class = {
            INITIAL_PROMPT_OUTPUT_DEFECT: "A",
            LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT: "B",
            GENUINE_SEMANTIC_OR_SOURCE_DEFECT: "C",
        }[row["root_cause_class"]]
        lines.append(
            f"| `{row['candidate_id']}` | `{row['rejection_category']}` | {short_class} | "
            f"`{row['root_cause_code']}` | `{row['source_document_id']}` | "
            f"{str(row['could_be_fixed_locally']).lower()} | "
            f"{str(row['requires_pro_semantic_repair']).lower()} |"
        )
    lines.extend(
        [
            "",
            "## 다음 단계 결박",
            "",
            "- 이 감사 결과 없이 fresh conversation을 제출하지 않는다.",
            "- A의 regression은 Initial Prompt V3와 Dossier V3에 추가한다.",
            "- B의 regression은 provider 호출 없는 local preflight/verifier test로 추가한다.",
            "- old conversation에는 어떤 follow-up도 더 제출하지 않는다.",
            "- score와 Stage는 이 감사의 권한 밖이다.",
            "",
            f"Audit hash: `{payload['audit_hash']}`",
            "",
        ]
    )
    return "\n".join(lines)


def _classify_root_cause(
    *,
    category: str,
    fact: Mapping[str, Any],
    fact_collection: str,
) -> _RootCause:
    lifecycle = str(fact.get("current_status") or "UNKNOWN").upper()
    if category == "UNSUPPORTED_DERIVATION" and lifecycle == "UNKNOWN":
        return _a(
            "MISSING_TERMINAL_LIFECYCLE",
            "source가 아니라 fact lifecycle이 UNKNOWN이라 old verifier가 일괄 pending 처리했다.",
            "test_initial_v3_terminal_lifecycle_required",
        )
    if category == "WRONG_SUBJECT":
        if fact.get("issuer_scoped") is True:
            return _a(
                "INCORRECT_ISSUER_SCOPE_BINDING",
                "peer·auditor·industry 문맥 후보가 issuer-scoped fact로 출력됐다.",
                "test_initial_v3_nonissuer_scope_binding",
            )
        return _b(
            "NONISSUER_SUBJECT_ALIAS_NOT_RESOLVED",
            "비issuer fact의 구조화 subject label을 문서의 literal 회사명으로만 검사했다.",
            "src/e2r/pro_first/verification/subject_scope_verifier.py",
            "SubjectScopeVerifier.verify",
            "test_nonissuer_semantic_scope_alias_resolved_locally",
        )
    if category in {"WRONG_SEGMENT", "WRONG_PRODUCT"}:
        if not fact.get("business_segment") or not fact.get("product_family"):
            return _b(
                "REPAIR_SCOPE_FIELDS_NOT_INHERITED",
                "compact replacement에서 원본 segment/product scope가 로컬 병합 중 보존되지 않았다.",
                "src/e2r/pro_first/dossier/dialect_adapter.py",
                "_compact_source_fact",
                "test_repair_scope_fields_inherited_locally",
            )
    if category == "QUOTE_MISMATCH":
        quote = _normalized_text(str(fact.get("supporting_excerpt") or ""))
        if len(quote) < 8:
            return _a(
                "QUOTE_TOO_SHORT_FOR_LITERAL_VERIFICATION",
                "최초 excerpt가 literal verifier 최소 길이보다 짧아 statement를 검증할 수 없었다.",
                "test_initial_v3_minimum_literal_quote_span",
            )
        return _b(
            "SOURCE_REPRESENTATION_QUOTE_MISMATCH",
            "충분한 길이의 quote가 old fetched representation과 달라 alternate official representation 확인이 필요했다.",
            "src/e2r/pro_first/preflight/source_representation_resolver.py",
            "SourceRepresentationResolver.resolve",
            "test_same_source_alternate_representation",
        )
    if category == "SOURCE_UNAVAILABLE":
        source_url = str(fact.get("source_url") or fact.get("url") or "")
        if _looks_malformed_source_url(source_url):
            return _a(
                "MALFORMED_OR_TRUNCATED_SOURCE_URL",
                "최초 source URL이 불완전하거나 canonical document URL 계약을 만족하지 못했다.",
                "test_initial_v3_canonical_url",
            )
        return _b(
            "SOURCE_REPRESENTATION_UNAVAILABLE",
            "직접 URL fetch 실패를 alternate official representation으로 로컬 해소하지 못했다.",
            "src/e2r/pro_first/preflight/source_representation_resolver.py",
            "SourceRepresentationResolver.resolve",
            "test_source_unavailable_alternate_representation",
        )
    return _c(
        "SEMANTIC_OR_SOURCE_SUPPORT_REMAINS",
        f"{fact_collection} 후보가 A/B 규칙으로 해소되지 않아 실제 의미·source support 검토가 필요하다.",
        requires_new_public_search=category in {"SOURCE_UNAVAILABLE", "SNIPPET_ONLY"},
    )


def _a(code: str, detail: str, test_id: str) -> _RootCause:
    return _RootCause(
        root_cause_class=INITIAL_PROMPT_OUTPUT_DEFECT,
        root_cause_code=code,
        root_cause_detail=detail,
        could_be_fixed_locally=False,
        requires_new_public_search=False,
        requires_pro_semantic_repair=True,
        generic_fix_file="src/e2r/pro_first/research_contracts/prompt_compiler_v3.py",
        generic_fix_function="ProResearchPromptCompilerV3.compile",
        regression_test_id=test_id,
    )


def _b(
    code: str,
    detail: str,
    file_name: str,
    function_name: str,
    test_id: str,
) -> _RootCause:
    return _RootCause(
        root_cause_class=LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT,
        root_cause_code=code,
        root_cause_detail=detail,
        could_be_fixed_locally=True,
        requires_new_public_search=False,
        requires_pro_semantic_repair=False,
        generic_fix_file=file_name,
        generic_fix_function=function_name,
        regression_test_id=test_id,
    )


def _c(
    code: str,
    detail: str,
    *,
    requires_new_public_search: bool,
) -> _RootCause:
    return _RootCause(
        root_cause_class=GENUINE_SEMANTIC_OR_SOURCE_DEFECT,
        root_cause_code=code,
        root_cause_detail=detail,
        could_be_fixed_locally=False,
        requires_new_public_search=requires_new_public_search,
        requires_pro_semantic_repair=True,
        generic_fix_file="src/e2r/pro_first/repair/compact_delta_v3.py",
        generic_fix_function="CompactRepairDeltaV3Compiler.compile",
        regression_test_id="test_genuine_semantic_rejection_routes_to_compact_repair",
    )


def _aggregate(rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    total = len(rows)
    class_counts = Counter(str(row["root_cause_class"]) for row in rows)
    for value in (
        INITIAL_PROMPT_OUTPUT_DEFECT,
        LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT,
        GENUINE_SEMANTIC_OR_SOURCE_DEFECT,
    ):
        class_counts.setdefault(value, 0)
    source_counts = Counter(str(row["source_document_id"]) for row in rows)
    same_source_groups = {key: value for key, value in source_counts.items() if value > 1}
    mechanical_groups = Counter(
        (
            str(row["source_document_id"]),
            str(row["root_cause_code"]),
        )
        for row in rows
        if row["root_cause_class"] == LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT
    )
    all_repair_groups = Counter(str(row["repair_group_key"]) for row in rows)
    return {
        "total_rejection_count": total,
        "root_cause_class_counts": dict(sorted(class_counts.items())),
        "root_cause_class_ratios": {
            key: (value / total if total else 0.0)
            for key, value in sorted(class_counts.items())
        },
        "root_cause_code_counts": dict(
            sorted(Counter(str(row["root_cause_code"]) for row in rows).items())
        ),
        "source_document_count": len(source_counts),
        "same_source_group_count": len(same_source_groups),
        "same_source_grouped_rejection_count": sum(same_source_groups.values()),
        "same_source_group_compression_savings": sum(
            value - 1 for value in same_source_groups.values()
        ),
        "repair_group_count": len(all_repair_groups),
        "repair_group_compression_savings": sum(
            value - 1 for value in all_repair_groups.values()
        ),
        "duplicate_mechanical_rejection_count": sum(
            value - 1 for value in mechanical_groups.values()
        ),
        "actual_genuine_semantic_repair_count": class_counts[
            GENUINE_SEMANTIC_OR_SOURCE_DEFECT
        ],
    }


def _snapshot_paths(root: Path) -> tuple[Path, ...]:
    return tuple(
        sorted(
            root.glob("research_passes/[0-9][0-9]_*/effective_dossier*.json"),
            key=lambda path: path.as_posix(),
        )
    )


def _single_job_id(paths: Sequence[Path]) -> str:
    job_ids = {str(_load_object(path).get("job_id") or "") for path in paths}
    if len(job_ids) != 1 or "" in job_ids:
        raise ValueError("dossier snapshots do not share one non-empty job_id")
    return next(iter(job_ids))


def _load_object(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"dossier snapshot is not a JSON object: {path}")
    return payload


def _canonical_source_url(value: str) -> str:
    parsed = urlsplit(str(value or "").strip())
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
        return str(value or "").strip()
    query = [
        (key, item)
        for key, item in parse_qsl(parsed.query, keep_blank_values=True)
        if not key.lower().startswith("utm_")
        and key.lower() not in _TRACKING_QUERY_KEYS
    ]
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    return urlunsplit(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            path,
            urlencode(sorted(query)),
            "",
        )
    )


def _looks_malformed_source_url(value: str) -> bool:
    parsed = urlsplit(str(value or "").strip())
    return bool(
        parsed.scheme.lower() not in {"http", "https"}
        or not parsed.netloc
        or not parsed.path.strip("/")
        or parsed.path.rstrip("/").endswith("-")
    )


def _normalized_text(value: str) -> str:
    return " ".join(str(value or "").split())


__all__ = [
    "GENUINE_SEMANTIC_OR_SOURCE_DEFECT",
    "INITIAL_PROMPT_OUTPUT_DEFECT",
    "LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT",
    "build_old_run_rejection_taxonomy",
    "render_old_run_rejection_taxonomy_markdown",
]
