"""Compile and audit verifier-ready Initial Prompt V3 for all 36 contracts."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Mapping

from e2r.pro_first.ids import canonical_hash

from .loader import CROSS_GUARD_IDS, load_all_research_contracts
from .prompt_compiler_v3 import (
    MAX_INITIAL_PROMPT_CHARS,
    ProResearchPromptCompilerV3,
    VERIFIER_PREFLIGHT_FALSE_FIELDS,
    VERIFIER_PREFLIGHT_TRUE_FIELDS,
)


ATOMIC_EVIDENCE_REQUIREMENT_MARKERS = (
    "한 fact에는 하나의 atomic predicate만 둔다",
    "하나의 source_document_id와 하나의 exact supporting excerpt",
    "서로 다른 두 문장 또는 두 source를 합쳐",
    "statement의 의미 범위는 exact excerpt보다 넓을 수 없다",
    "exact excerpt에 직접 없는 고객명",
    "실제로 연 canonical 원문 URL",
    "utm/tracking URL을 canonical URL로 쓰지 않는다",
    "publication_date와 availability_date를 실제 문서에서 확인",
    "HTML은 heading/section/paragraph locator",
    "question_family_ids와 source_role_ids를 처음부터 연결",
    "source document 하나 아래 서로 다른 atomic fact",
    "derived_metrics에 원천 fact IDs와 계산식",
    "unresolved gap으로 남긴다",
    "동일 lineage의 재인용을 독립 source로 세지 않는다",
    "verifier_preflight 9개 true 항목",
    "accepted material fact로 제출하지 않는다",
)
FORCED_COMPLETE_MARKERS = (
    "research_status`는 `COMPLETE`",
    "research_status는 COMPLETE로 고정",
    "반드시 COMPLETE로",
    "무조건 COMPLETE로",
)
ANSWER_LEAKAGE_MARKERS = (
    "expected_score",
    "expected_stage",
    "gold_score",
    "gold_stage",
    "gold_answer",
    "future_outcome",
    "forward_return",
    '"score_authority": true',
    '"stage_authority": true',
    "score_authority: `true`",
    "stage_authority: `true`",
)


def compile_initial_prompt_v3_snapshot_audit(
    repo_root: str | Path,
    *,
    output_root: str | Path | None = None,
) -> Mapping[str, Any]:
    """Regenerate tracked snapshots and return deterministic audit counters."""

    root = Path(repo_root).resolve()
    destination = (
        Path(output_root).resolve()
        if output_root
        else root
        / "docs/operational/e2r_pro_first_v2_1/prompt_snapshots_v3"
    )
    destination.mkdir(parents=True, exist_ok=True)
    contracts = load_all_research_contracts()
    contract_by_id = {str(row["archetype_id"]): row for row in contracts}
    all_question_ids = {
        str(question["question_family_id"])
        for contract in contracts
        for question in contract["question_families"]
    }
    compiler = ProResearchPromptCompilerV3()
    rows: list[Mapping[str, Any]] = []
    counters = {
        "compile_failure_count": 0,
        "mandatory_question_missing_count": 0,
        "atomic_contract_missing_snapshot_count": 0,
        "verifier_preflight_missing_snapshot_count": 0,
        "derived_metric_separation_missing_snapshot_count": 0,
        "forced_complete_snapshot_count": 0,
        "score_stage_leakage_snapshot_count": 0,
        "cross_archetype_question_pollution_count": 0,
        "source_role_policy_missing_snapshot_count": 0,
        "output_v3_schema_missing_snapshot_count": 0,
        "prompt_over_limit_count": 0,
    }
    for contract in contracts:
        archetype_id = str(contract["archetype_id"])
        failures: list[str] = []
        try:
            compiled = compiler.compile_contract_snapshot(
                packet=_example_packet(archetype_id),
                archetype_id=archetype_id,
            )
        except Exception as exc:  # pragma: no cover - audit retains the exact error
            counters["compile_failure_count"] += 1
            rows.append(
                {
                    "archetype_id": archetype_id,
                    "contract_role": contract["contract_role"],
                    "failure_codes": ["COMPILE_FAILURE"],
                    "compile_error": f"{type(exc).__name__}: {exc}",
                }
            )
            continue
        prompt = compiled.prompt_text
        snapshot_path = destination / f"{archetype_id}.md"
        _write_text_atomic(snapshot_path, prompt)

        expected_contract_ids = set(compiled.contract_ids)
        expected_question_ids = {
            str(question["question_family_id"])
            for expected_id in expected_contract_ids
            for question in contract_by_id[expected_id]["question_families"]
        }
        expected_mandatory_ids = {
            str(question["question_family_id"])
            for expected_id in expected_contract_ids
            for question in contract_by_id[expected_id]["question_families"]
            if question["mandatory_for_full_thesis"] is True
        }
        present_question_ids = {
            question_id
            for question_id in all_question_ids
            if f"`{question_id}`" in prompt
        }
        missing_mandatory = sorted(expected_mandatory_ids - present_question_ids)
        polluted_question_ids = sorted(present_question_ids - expected_question_ids)
        if missing_mandatory:
            failures.append("MANDATORY_QUESTION_MISSING")
            counters["mandatory_question_missing_count"] += len(missing_mandatory)
        if polluted_question_ids:
            failures.append("CROSS_ARCHETYPE_QUESTION_POLLUTION")
            counters["cross_archetype_question_pollution_count"] += len(
                polluted_question_ids
            )

        missing_atomic_markers = [
            marker
            for marker in ATOMIC_EVIDENCE_REQUIREMENT_MARKERS
            if marker not in prompt
        ]
        if missing_atomic_markers:
            failures.append("ATOMIC_EVIDENCE_CONTRACT_MISSING")
            counters["atomic_contract_missing_snapshot_count"] += 1

        missing_preflight_fields = [
            field
            for field in (
                *VERIFIER_PREFLIGHT_TRUE_FIELDS,
                *VERIFIER_PREFLIGHT_FALSE_FIELDS,
            )
            if f'"{field}"' not in prompt or f"`{field}`" not in prompt
        ]
        if missing_preflight_fields:
            failures.append("VERIFIER_PREFLIGHT_FIELD_MISSING")
            counters["verifier_preflight_missing_snapshot_count"] += 1

        derived_separation_present = all(
            marker in prompt
            for marker in (
                "DerivedMetricV3",
                "`input_fact_ids`",
                "`formula`",
                "quoted atomic fact에 계산 결과를 섞지 않는다",
                '"derived_calculation_mixed_into_fact"',
                '"const": false',
            )
        )
        if not derived_separation_present:
            failures.append("DERIVED_METRIC_SEPARATION_MISSING")
            counters["derived_metric_separation_missing_snapshot_count"] += 1

        forced_complete = [
            marker for marker in FORCED_COMPLETE_MARKERS if marker in prompt
        ]
        if forced_complete or "특정 COMPLETE 상태를 형식적으로 강제하지 않는다" not in prompt:
            failures.append("FORCED_COMPLETE")
            counters["forced_complete_snapshot_count"] += 1

        lowered = prompt.casefold()
        leakage = [
            marker for marker in ANSWER_LEAKAGE_MARKERS if marker in lowered
        ]
        if (
            leakage
            or "score_authority: `false`" not in prompt
            or "stage_authority: `false`" not in prompt
        ):
            failures.append("SCORE_STAGE_AUTHORITY_LEAKAGE")
            counters["score_stage_leakage_snapshot_count"] += 1

        source_role_policy_missing = any(
            str(role) not in prompt
            for expected_id in expected_contract_ids
            for role in contract_by_id[expected_id]["source_role_policy"][
                "recommended_routes"
            ]
        )
        if source_role_policy_missing:
            failures.append("SOURCE_ROLE_POLICY_MISSING")
            counters["source_role_policy_missing_snapshot_count"] += 1

        output_schema_present = all(
            marker in prompt
            for marker in (
                '"const": "e2r_pro_research_dossier_v3"',
                '"source_documents"',
                '"material_facts"',
                '"counterfacts"',
                '"resolution_facts"',
                '"derived_metrics"',
                '"question_family_results"',
                '"search_route_receipts"',
                "E2R_RESEARCH_DOSSIER_JSON_BEGIN",
                "E2R_RESEARCH_DOSSIER_JSON_END",
            )
        )
        if not output_schema_present:
            failures.append("OUTPUT_V3_SCHEMA_MISSING")
            counters["output_v3_schema_missing_snapshot_count"] += 1
        if len(prompt) > MAX_INITIAL_PROMPT_CHARS:
            failures.append("PROMPT_CHAR_LIMIT_EXCEEDED")
            counters["prompt_over_limit_count"] += 1

        rows.append(
            {
                "archetype_id": archetype_id,
                "contract_role": contract["contract_role"],
                "snapshot_path": str(snapshot_path.relative_to(root)),
                "prompt_hash": compiled.prompt_hash,
                "dossier_schema_hash": compiled.dossier_schema_hash,
                "prompt_char_count": len(prompt),
                "attached_contract_ids": list(compiled.contract_ids),
                "mandatory_question_count": len(expected_mandatory_ids),
                "missing_mandatory_question_ids": missing_mandatory,
                "polluted_question_ids": polluted_question_ids,
                "missing_atomic_markers": missing_atomic_markers,
                "missing_preflight_fields": missing_preflight_fields,
                "failure_codes": failures,
            }
        )

    existing = {path.stem for path in destination.glob("*.md")}
    expected = set(contract_by_id)
    missing_snapshot_ids = sorted(expected - existing)
    extra_snapshot_ids = sorted(existing - expected)
    critical_count = (
        sum(counters.values())
        + len(missing_snapshot_ids)
        + len(extra_snapshot_ids)
    )
    payload = {
        "schema_version": "e2r_pro_first_v2_1_initial_prompt_v3_audit_v1",
        "status": "PASS" if critical_count == 0 else "FAIL",
        "critical_count": critical_count,
        "canonical_contract_count": len(contracts),
        "prompt_snapshot_count": len(rows),
        "primary_prompt_snapshot_count": sum(
            row["contract_role"] == "PRIMARY" for row in contracts
        ),
        "cross_guard_prompt_snapshot_count": sum(
            row["contract_role"] != "PRIMARY" for row in contracts
        ),
        "r13_cross_guard_ids": list(CROSS_GUARD_IDS),
        "missing_snapshot_ids": missing_snapshot_ids,
        "extra_snapshot_ids": extra_snapshot_ids,
        "counters": counters,
        "snapshots": rows,
    }
    return {**payload, "audit_hash": canonical_hash(payload)}


def render_initial_prompt_v3_audit_markdown(payload: Mapping[str, Any]) -> str:
    counters = payload["counters"]
    rows = [
        "# Initial Prompt V3 36-contract 감사",
        "",
        f"판정: **{payload['status']}**",
        "",
        "이 감사는 fresh Pro 전송 전 단계다. 실제 ChatGPT 응답 품질이나 운영 완료를 주장하지 않고, 모든 canonical contract에 같은 verifier-ready 계약이 붙는지만 검증한다.",
        "",
        "```text",
        f"36/36 compile                        {payload['prompt_snapshot_count']}/{payload['canonical_contract_count']}",
        f"mandatory question missing           {counters['mandatory_question_missing_count']}",
        f"atomic contract missing              {counters['atomic_contract_missing_snapshot_count']}",
        f"verifier preflight missing           {counters['verifier_preflight_missing_snapshot_count']}",
        f"derived separation missing           {counters['derived_metric_separation_missing_snapshot_count']}",
        f"forced COMPLETE                      {counters['forced_complete_snapshot_count']}",
        f"score/Stage leakage                  {counters['score_stage_leakage_snapshot_count']}",
        f"other-archetype question pollution   {counters['cross_archetype_question_pollution_count']}",
        f"source role policy missing           {counters['source_role_policy_missing_snapshot_count']}",
        f"output V3 schema missing             {counters['output_v3_schema_missing_snapshot_count']}",
        f"prompt over 100k                     {counters['prompt_over_limit_count']}",
        "```",
        "",
        "쉬운 예: C06 snapshot에는 C06 질문과 모든 job 공통 R13 질문만 있다. C17 질문이 섞이면 pollution으로 즉시 실패한다. 반대로 source URL은 document registry에 한 번만 두고, 그 문서의 여러 주장은 각각 다른 atomic fact로 나누라는 공통 규칙은 36개 모두에 들어간다.",
        "",
        "## Snapshot roster",
        "",
        "| contract | role | chars | mandatory | failure |",
        "|---|---:|---:|---:|---|",
    ]
    for row in payload["snapshots"]:
        rows.append(
            "| {id} | {role} | {chars} | {mandatory} | {failure} |".format(
                id=row["archetype_id"],
                role=row["contract_role"],
                chars=row.get("prompt_char_count", "-"),
                mandatory=row.get("mandatory_question_count", "-"),
                failure=", ".join(row["failure_codes"]) or "PASS",
            )
        )
    rows.extend(["", f"audit_hash: `{payload['audit_hash']}`", ""])
    return "\n".join(rows)


def _example_packet(archetype_id: str) -> Mapping[str, Any]:
    return {
        "schema_version": "e2r_pro_research_packet_v3",
        "job_id": f"PROMPT-V3-SNAPSHOT-{archetype_id}",
        "run_id": f"PROMPT-V3-SNAPSHOT-RUN-{archetype_id}",
        "target": {
            "target_id": "BLIND-SAMPLE",
            "symbol": "BLIND-SAMPLE",
            "company_name": "블라인드 예시 대상",
            "aliases": [],
        },
        "as_of_date": "2026-08-22",
        "research_mode": "FULL_RESEARCH",
        "candidate_archetypes": [archetype_id],
        "selected_archetypes": [archetype_id],
        "trigger_summary": [],
        "business_snapshot": {},
        "structured_financial_snapshot": {},
        "revision_valuation_snapshot": {},
        "known_positive_facts": [],
        "known_counterfacts": [],
        "score_authority": False,
        "stage_authority": False,
    }


def _write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


__all__ = [
    "ATOMIC_EVIDENCE_REQUIREMENT_MARKERS",
    "compile_initial_prompt_v3_snapshot_audit",
    "render_initial_prompt_v3_audit_markdown",
]
