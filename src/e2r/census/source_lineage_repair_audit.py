"""Source-lineage repair audit for Goal4 runtime parity artifacts.

This audit separates "the claim looks semantically usable, but the source route
was not admitted as an original source" from generic primitive or semantic
failures.  It does not turn any rejected claim into score evidence.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit

from e2r.sources.report_search import is_verified_report_original_url


LINEAGE_REASON_PREFIXES = (
    "source_lineage_unverified_original",
    "source_provider_document_type_mismatch",
    "source_class_document_type_mismatch",
    "source_task_provider_error_score_block",
)

NON_ROUTE_REJECTION_PREFIXES = (
    "primitive_mapping_rejected",
    "mapping_not_accepted",
    "semantic_rejected",
    "target_scope_not_allowed",
    "target_not_direct",
    "target_scope_not_direct",
    "temporal_not_current",
    "anchor_validation",
)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows


def _reason_key(reason: str) -> str:
    return reason.split(":", 1)[0]


def _lineage_reasons(row: Mapping[str, Any]) -> list[str]:
    reasons = [str(reason) for reason in row.get("not_eligible_reasons") or [] if str(reason).strip()]
    if not reasons:
        return []
    return [
        reason
        for reason in reasons
        if any(reason.startswith(prefix) for prefix in LINEAGE_REASON_PREFIXES)
    ]


def _non_route_reasons(row: Mapping[str, Any]) -> list[str]:
    reasons = [str(reason) for reason in row.get("not_eligible_reasons") or [] if str(reason).strip()]
    return [
        reason
        for reason in reasons
        if any(reason.startswith(prefix) for prefix in NON_ROUTE_REJECTION_PREFIXES)
    ]


def _source_class_from_reasons(reasons: Sequence[str], fallback: Any = None) -> str:
    for reason in reasons:
        parts = reason.split(":")
        if len(parts) >= 2 and parts[0] in {
            "source_lineage_unverified_original",
            "source_provider_document_type_mismatch",
            "source_class_document_type_mismatch",
        }:
            return parts[1]
    return str(fallback or "UNKNOWN")


def _domain(url: Any) -> str:
    host = urlsplit(str(url or "")).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def _is_semantic_mapping_candidate(row: Mapping[str, Any]) -> bool:
    return (
        row.get("mapping_status") == "ACCEPTED"
        and row.get("semantic_status") == "PASS"
        and row.get("target_scope_status") == "DIRECT"
        and row.get("temporal_status") == "CURRENT"
    )


def _current_route_patch_status(*, source_class: str, source_url: str) -> str:
    if source_class in {"BrokerReportPublicPDF", "ReportPDF"} and is_verified_report_original_url(source_url):
        return "CURRENT_CODE_VERIFIES_BROKER_REPORT_ORIGINAL_RETRY_REQUIRED"
    return "ROUTE_RECOVERY_STILL_REQUIRED"


def _short(value: Any, *, max_chars: int = 180) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def _sample(row: Mapping[str, Any], *, reasons: Sequence[str], source_class: str) -> dict[str, Any]:
    source_url = str(row.get("source_url") or "")
    return {
        "archetype_id": row.get("archetype_id"),
        "symbol": row.get("symbol"),
        "company_name": row.get("company_name"),
        "source_task_id": row.get("source_task_id") or row.get("task_id"),
        "primitive_gap": row.get("source_task_primitive_gap") or row.get("primitive_gap"),
        "mapped_primitive_id": row.get("mapped_primitive_id") or row.get("primitive_id"),
        "mapping_status": row.get("mapping_status"),
        "semantic_status": row.get("semantic_status"),
        "target_scope_status": row.get("target_scope_status"),
        "temporal_status": row.get("temporal_status"),
        "source_provider": row.get("source_provider"),
        "source_class": source_class,
        "source_domain": _domain(source_url),
        "source_url": source_url,
        "lineage_reasons": list(reasons),
        "non_route_reasons": _non_route_reasons(row)[:6],
        "current_route_patch_status": _current_route_patch_status(source_class=source_class, source_url=source_url),
        "quote_excerpt": _short(row.get("quote_text") or row.get("exact_quote")),
    }


def build_source_lineage_repair_audit(
    *,
    output_root: str | Path,
    max_samples_per_archetype: int = 5,
) -> dict[str, Any]:
    output_path = Path(output_root)
    rejection_rows = _read_jsonl(output_path / "raw_assertion_rejections.jsonl")
    execution_rows = _read_jsonl(output_path / "source_task_executions.jsonl")

    lineage_rows = []
    route_only_rows = []
    patched_retry_rows = []
    archetype_rows: dict[str, dict[str, Any]] = {}
    reason_counts: Counter[str] = Counter()
    domain_counts: Counter[str] = Counter()
    source_class_counts: Counter[str] = Counter()

    for row in rejection_rows:
        reasons = _lineage_reasons(row)
        if not reasons:
            continue
        source_class = _source_class_from_reasons(reasons)
        source_url = str(row.get("source_url") or "")
        domain = _domain(source_url)
        archetype_id = str(row.get("archetype_id") or "UNKNOWN")
        route_only = _is_semantic_mapping_candidate(row) and not _non_route_reasons(row)
        patch_status = _current_route_patch_status(source_class=source_class, source_url=source_url)
        sample = _sample(row, reasons=reasons, source_class=source_class)

        lineage_rows.append(sample)
        if route_only:
            route_only_rows.append(sample)
        if patch_status == "CURRENT_CODE_VERIFIES_BROKER_REPORT_ORIGINAL_RETRY_REQUIRED":
            patched_retry_rows.append(sample)

        for reason in reasons:
            reason_counts[_reason_key(reason)] += 1
        if domain:
            domain_counts[domain] += 1
        source_class_counts[source_class] += 1

        entry = archetype_rows.setdefault(
            archetype_id,
            {
                "archetype_id": archetype_id,
                "lineage_rejection_count": 0,
                "route_only_candidate_count": 0,
                "current_code_verified_retry_candidate_count": 0,
                "reason_counts": Counter(),
                "source_class_counts": Counter(),
                "source_domain_counts": Counter(),
                "samples": [],
            },
        )
        entry["lineage_rejection_count"] += 1
        if route_only:
            entry["route_only_candidate_count"] += 1
        if patch_status == "CURRENT_CODE_VERIFIES_BROKER_REPORT_ORIGINAL_RETRY_REQUIRED":
            entry["current_code_verified_retry_candidate_count"] += 1
        for reason in reasons:
            entry["reason_counts"][_reason_key(reason)] += 1
        entry["source_class_counts"][source_class] += 1
        if domain:
            entry["source_domain_counts"][domain] += 1
        if len(entry["samples"]) < max_samples_per_archetype:
            entry["samples"].append(sample)

    source_lineage_feedback_retry_executions = [
        row
        for row in execution_rows
        if "feedback_retry:source_lineage_unverified_original"
        in str(row.get("reason_from_memory") or row.get("source_task") or row.get("stop_reason") or "")
    ]

    normalized_archetypes = []
    for archetype_id, row in sorted(archetype_rows.items()):
        normalized_archetypes.append(
            {
                "archetype_id": archetype_id,
                "lineage_rejection_count": row["lineage_rejection_count"],
                "route_only_candidate_count": row["route_only_candidate_count"],
                "current_code_verified_retry_candidate_count": row[
                    "current_code_verified_retry_candidate_count"
                ],
                "reason_counts": dict(sorted(row["reason_counts"].items())),
                "source_class_counts": dict(sorted(row["source_class_counts"].items())),
                "source_domain_counts": dict(sorted(row["source_domain_counts"].items())),
                "samples": row["samples"],
            }
        )

    return {
        "schema_version": "e2r_source_lineage_repair_audit_v1",
        "output_root": str(output_path),
        "raw_assertion_rejection_count": len(rejection_rows),
        "source_task_execution_count": len(execution_rows),
        "lineage_rejection_count": len(lineage_rows),
        "route_only_candidate_count": len(route_only_rows),
        "current_code_verified_retry_candidate_count": len(patched_retry_rows),
        "source_lineage_feedback_retry_execution_count": len(source_lineage_feedback_retry_executions),
        "reason_counts": dict(sorted(reason_counts.items())),
        "source_class_counts": dict(sorted(source_class_counts.items())),
        "source_domain_counts": dict(sorted(domain_counts.items())),
        "archetype_count": len(normalized_archetypes),
        "archetypes": normalized_archetypes,
        "top_retry_candidates": patched_retry_rows[:20],
        "score_evidence_allowed_from_rejected_rows": False,
        "operator_rule": (
            "Rows in this audit are repair candidates only. They become score evidence only after a fresh "
            "bounded runtime attempt creates accepted Evidence OS claims with verified anchors."
        ),
    }


def render_source_lineage_repair_audit_markdown(audit: Mapping[str, Any]) -> str:
    lines = [
        "# Source Lineage Repair Audit - 2026-07-05",
        "",
        "이 문서는 source route 때문에 버려진 claim 후보를 전수 집계한다.",
        "",
        "쉬운 예: 문장 자체는 `ARR 성장`처럼 맞게 뽑혔는데, URL이 검증된 증권사 원본 리포트로 인정되지 않아 점수 근거에서 탈락한 경우를 따로 모은다.",
        "",
        "## Summary",
        "",
        f"- raw_assertion_rejection_count: `{audit.get('raw_assertion_rejection_count')}`",
        f"- lineage_rejection_count: `{audit.get('lineage_rejection_count')}`",
        f"- route_only_candidate_count: `{audit.get('route_only_candidate_count')}`",
        f"- current_code_verified_retry_candidate_count: `{audit.get('current_code_verified_retry_candidate_count')}`",
        f"- source_lineage_feedback_retry_execution_count: `{audit.get('source_lineage_feedback_retry_execution_count')}`",
        f"- reason_counts: `{json.dumps(audit.get('reason_counts', {}), ensure_ascii=False, sort_keys=True)}`",
        f"- source_class_counts: `{json.dumps(audit.get('source_class_counts', {}), ensure_ascii=False, sort_keys=True)}`",
        "",
        "## Archetypes",
        "",
        "| archetype | lineage rejected | route-only candidates | current-code retry candidates | top domains |",
        "|---|---:|---:|---:|---|",
    ]
    for row in audit.get("archetypes", []):
        domains = ", ".join(
            f"{domain}:{count}" for domain, count in list((row.get("source_domain_counts") or {}).items())[:4]
        )
        lines.append(
            "| {archetype} | {lineage} | {route_only} | {retry} | {domains} |".format(
                archetype=row.get("archetype_id"),
                lineage=row.get("lineage_rejection_count"),
                route_only=row.get("route_only_candidate_count"),
                retry=row.get("current_code_verified_retry_candidate_count"),
                domains=domains or "-",
            )
        )
    lines.extend(
        [
            "",
            "## Safety",
            "",
            "이 audit의 row는 점수 근거가 아니다. 새 runtime attempt에서 source anchor, direct target, current temporal, accepted primitive mapping을 다시 통과해야 한다.",
            "",
        ]
    )
    return "\n".join(lines)


def write_source_lineage_repair_audit(
    *,
    output_root: str | Path,
    docs_dir: str | Path = "docs/operational",
) -> dict[str, Any]:
    docs_path = Path(docs_dir)
    docs_path.mkdir(parents=True, exist_ok=True)
    audit = build_source_lineage_repair_audit(output_root=output_root)
    json_path = docs_path / "source_lineage_repair_audit_2026-07-05.json"
    markdown_path = docs_path / "source_lineage_repair_audit_2026-07-05.md"
    json_text = json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    json_path.write_text(json_text, encoding="utf-8")
    (docs_path / "source_lineage_repair_audit.json").write_text(json_text, encoding="utf-8")
    markdown_path.write_text(render_source_lineage_repair_audit_markdown(audit), encoding="utf-8")
    return {
        "audit": audit,
        "json_path": json_path,
        "markdown_path": markdown_path,
    }


__all__ = [
    "build_source_lineage_repair_audit",
    "render_source_lineage_repair_audit_markdown",
    "write_source_lineage_repair_audit",
]
