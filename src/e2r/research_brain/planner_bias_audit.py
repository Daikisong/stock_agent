"""Planner archetype routing bias audit for Research Brain runs."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any, Mapping


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _short(value: str | None) -> str | None:
    if not value:
        return None
    return value.split("_", 1)[0]


def _resolve_output_root(repo_root: Path, docs_dir: Path, explicit_output_root: str | Path | None) -> Path:
    if explicit_output_root:
        path = Path(explicit_output_root)
        return path if path.is_absolute() else repo_root / path
    manifest = _read_json(docs_dir / "census_mode_v4_artifact_manifest.json")
    output_root = manifest.get("output_root")
    if not output_root:
        raise FileNotFoundError("Cannot resolve output root from census_mode_v4_artifact_manifest.json")
    path = Path(output_root)
    return path if path.is_absolute() else repo_root / path


def build_planner_bias_audit(
    *,
    repo_root: str | Path = ".",
    output_root: str | Path | None = None,
    docs_dir: str | Path = "docs/operational",
    parity_audit: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    repo_root = Path(repo_root).resolve()
    docs_path = Path(docs_dir)
    docs_path = docs_path if docs_path.is_absolute() else repo_root / docs_path
    output_path = _resolve_output_root(repo_root, docs_path, output_root)

    top1_counts: Counter[str] = Counter()
    topk_counts: Counter[str] = Counter()
    top1_symbols: dict[str, set[str]] = {}
    hypothesis_run_count = 0
    real_success_hypothesis_count = 0
    planner_run_count = 0
    real_provider_success_count = 0
    invalid_score_stage_key_count = 0

    for row in _read_jsonl(output_path / "planner_runs.jsonl"):
        planner_run_count += 1
        if row.get("real_provider_success"):
            real_provider_success_count += 1
        output = row.get("output") or {}
        invalid_score_stage_key_count += int(row.get("planner_output_score_stage_key_count") or 0)
        hypotheses = output.get("top_k_archetype_hypotheses") or output.get("archetype_hypotheses") or []
        normalized: list[str] = []
        for hypothesis in hypotheses:
            if isinstance(hypothesis, Mapping):
                value = hypothesis.get("archetype_id") or hypothesis.get("canonical_archetype_id") or hypothesis.get("id")
            else:
                value = str(hypothesis)
            short = _short(str(value)) if value else None
            if short:
                normalized.append(short)
        if not normalized:
            continue
        hypothesis_run_count += 1
        if row.get("real_provider_success"):
            real_success_hypothesis_count += 1
        top1 = normalized[0]
        top1_counts[top1] += 1
        symbol = ((row.get("event") or {}).get("symbol") or "").strip()
        if symbol:
            top1_symbols.setdefault(top1, set()).add(symbol)
        for short in normalized:
            topk_counts[short] += 1

    c05_top1_count = top1_counts.get("C05", 0)
    c05_top1_share = c05_top1_count / hypothesis_run_count if hypothesis_run_count else 0.0
    distinct_top1_count = len(top1_counts)

    blockers: list[str] = []
    if c05_top1_share > 0.35:
        blockers.append("planner_top1_c05_share_over_limit")
    if distinct_top1_count < 6:
        blockers.append("planner_top1_distinct_archetype_count_below_minimum")
    if parity_audit:
        if parity_audit.get("target_archetype_unknown_promoted_count", 0):
            blockers.append("target_unknown_rows_promoted_after_planner")
        if parity_audit.get("source_primary_context_promoted_count", 0):
            blockers.append("source_primary_context_survived_into_promotion")
        if parity_audit.get("mandatory_archetype_attempt_count", 0) < len(parity_audit.get("mandatory_archetypes", [])):
            blockers.append("mandatory_archetypes_not_planner_attempted")

    return {
        "schema_version": "e2r_research_brain_planner_bias_audit_v1",
        "status": "PLANNER_ARCHETYPE_ROUTING_BIAS_PASS" if not blockers else "PLANNER_ARCHETYPE_ROUTING_BIAS_NOT_READY",
        "planner_run_count": planner_run_count,
        "real_provider_success_count": real_provider_success_count,
        "hypothesis_run_count": hypothesis_run_count,
        "real_success_hypothesis_count": real_success_hypothesis_count,
        "distinct_top1_archetype_count": distinct_top1_count,
        "top1_archetype_counts": dict(sorted(top1_counts.items())),
        "topk_archetype_counts": dict(sorted(topk_counts.items())),
        "top1_symbol_samples": {key: sorted(value)[:20] for key, value in sorted(top1_symbols.items())},
        "c05_top1_count": c05_top1_count,
        "c05_top1_share": round(c05_top1_share, 6),
        "planner_output_score_stage_key_count": invalid_score_stage_key_count,
        "blockers": blockers,
        "bias_rule": "Production full-thesis routing is not balanced if C05 top1 share exceeds 35% or fewer than 6 archetypes receive top1 planner coverage.",
    }


def render_planner_bias_markdown(audit: Mapping[str, Any]) -> str:
    lines = [
        "# Planner Bias And Archetype Routing Audit - 2026-07-05",
        "",
        "이 문서는 Research Brain planner가 어떤 아키타입을 1순위로 골랐는지 본다.",
        "",
        "쉬운 예: 선생님이 모든 과목 시험을 봐야 하는데, 채점할 때마다 건설 계약형(C05) 답안지만 먼저 꺼내면 전체 시험 검증이 아니다.",
        "",
        "## Summary",
        "",
        f"- status: `{audit['status']}`",
        f"- planner_run_count: `{audit['planner_run_count']}`",
        f"- hypothesis_run_count: `{audit['hypothesis_run_count']}`",
        f"- distinct_top1_archetype_count: `{audit['distinct_top1_archetype_count']}`",
        f"- c05_top1_share: `{audit['c05_top1_share']}`",
        f"- planner_output_score_stage_key_count: `{audit['planner_output_score_stage_key_count']}`",
        "",
        "## Top1 Counts",
        "",
    ]
    for key, value in audit.get("top1_archetype_counts", {}).items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Blockers", ""])
    for blocker in audit.get("blockers", []):
        lines.append(f"- `{blocker}`")
    lines.append("")
    return "\n".join(lines)


def write_planner_bias_audit(
    *,
    repo_root: str | Path = ".",
    output_root: str | Path | None = None,
    docs_dir: str | Path = "docs/operational",
    parity_audit: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    docs_path = Path(docs_dir)
    audit = build_planner_bias_audit(
        repo_root=repo_root,
        output_root=output_root,
        docs_dir=docs_path,
        parity_audit=parity_audit,
    )
    docs_path.mkdir(parents=True, exist_ok=True)
    json_path = docs_path / "planner_bias_and_archetype_routing_audit_2026-07-05.json"
    md_path = docs_path / "planner_bias_and_archetype_routing_audit_2026-07-05.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_planner_bias_markdown(audit), encoding="utf-8")
    return audit


__all__ = [
    "build_planner_bias_audit",
    "render_planner_bias_markdown",
    "write_planner_bias_audit",
]
