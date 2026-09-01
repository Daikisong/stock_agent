"""Compile and audit one isolated prompt snapshot per primary archetype."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from e2r.pro_first.ids import canonical_hash

from .loader import load_all_research_contracts
from .prompt_compiler import ProResearchPromptCompilerV2


def compile_prompt_snapshot_audit(
    repo_root: str | Path,
    *,
    output_root: str | Path | None = None,
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    destination = (
        Path(output_root).resolve()
        if output_root
        else root / "docs/operational/e2r_pro_first_v2/prompt_snapshots"
    )
    destination.mkdir(parents=True, exist_ok=True)
    contracts = load_all_research_contracts()
    primary = tuple(row for row in contracts if row["contract_role"] == "PRIMARY")
    compiler = ProResearchPromptCompilerV2()
    rows = []
    critical_count = 0
    all_primary_questions = {
        str(contract["archetype_id"]): tuple(
            str(question["question_text"])
            for question in contract["question_families"]
        )
        for contract in primary
    }
    for contract in contracts:
        archetype_id = str(contract["archetype_id"])
        packet = _example_packet(archetype_id)
        compiled = compiler.compile_contract_snapshot(
            packet=packet,
            archetype_id=archetype_id,
        )
        snapshot_path = destination / f"{archetype_id}.md"
        snapshot_path.write_text(compiled.prompt_text, encoding="utf-8")
        mandatory = tuple(
            str(question["question_text"])
            for question in contract["question_families"]
            if question["mandatory_for_full_thesis"] is True
        )
        missing_questions = [text for text in mandatory if text not in compiled.prompt_text]
        polluted_by = sorted(
            other_id
            for other_id in all_primary_questions
            if other_id != archetype_id
            and f"`{other_id}_Q" in compiled.prompt_text
        )
        failures = []
        if archetype_id not in compiled.prompt_text:
            failures.append("ARCHETYPE_ID_MISSING")
        if str(contract["economic_mechanism"]) not in compiled.prompt_text:
            failures.append("ECONOMIC_MECHANISM_MISSING")
        if missing_questions:
            failures.append("MANDATORY_QUESTION_MISSING")
        if polluted_by:
            failures.append("CROSS_ARCHETYPE_QUESTION_POLLUTION")
        if str(contract["source_role_policy"]["recommended_routes"]) not in compiled.prompt_text:
            failures.append("SOURCE_ROLE_POLICY_MISSING")
        if str(contract["false_positive_guards"][0]) not in compiled.prompt_text:
            failures.append("FALSE_POSITIVE_GUARD_MISSING")
        if "score_authority: `false`" not in compiled.prompt_text:
            failures.append("SCORE_AUTHORITY_GUARD_MISSING")
        if "stage_authority: `false`" not in compiled.prompt_text:
            failures.append("STAGE_AUTHORITY_GUARD_MISSING")
        if "future_source_allowed: `false`" not in compiled.prompt_text:
            failures.append("FUTURE_SOURCE_GUARD_MISSING")
        if "모든 mandatory question family" not in compiled.prompt_text:
            failures.append("GENERIC_COMPONENT_ONLY_PROMPT")
        if "research_status`는 `COMPLETE" in compiled.prompt_text:
            failures.append("FORCED_COMPLETE_LITERAL")
        critical_count += len(failures)
        rows.append(
            {
                "archetype_id": archetype_id,
                "snapshot_path": str(snapshot_path.relative_to(root)),
                "prompt_hash": compiled.prompt_hash,
                "mandatory_question_count": len(mandatory),
                "missing_question_count": len(missing_questions),
                "polluted_by_archetype_ids": polluted_by,
                "failure_codes": failures,
            }
        )
    existing = {path.stem for path in destination.glob("*.md")}
    expected = {str(row["archetype_id"]) for row in contracts}
    extra_snapshots = sorted(existing - expected)
    missing_snapshots = sorted(expected - existing)
    critical_count += len(extra_snapshots) + len(missing_snapshots)
    payload = {
        "schema_version": "e2r_pro_first_v2_prompt_snapshot_audit_v1",
        "status": "PASS" if critical_count == 0 else "FAIL",
        "critical_count": critical_count,
        "canonical_contract_count": len(contracts),
        "prompt_snapshot_count": len(rows),
        "primary_prompt_snapshot_count": len(primary),
        "cross_guard_prompt_snapshot_count": len(contracts) - len(primary),
        "missing_snapshot_ids": missing_snapshots,
        "extra_snapshot_ids": extra_snapshots,
        "snapshots": rows,
    }
    return {**payload, "audit_hash": canonical_hash(payload)}


def _example_packet(archetype_id: str) -> Mapping[str, Any]:
    return {
        "schema_version": "e2r_pro_research_packet_v2_example",
        "job_id": f"PROMPT-SNAPSHOT-{archetype_id}",
        "run_id": f"PROMPT-SNAPSHOT-RUN-{archetype_id}",
        "target": {
            "symbol": "BLIND-SAMPLE",
            "company_name": "블라인드 예시 대상",
            "aliases": [],
        },
        "as_of_date": "2026-08-22",
        "research_mode": "FULL_RESEARCH",
        "candidate_archetypes": [archetype_id],
        "trigger_summary": [],
        "business_snapshot": {},
        "structured_financial_snapshot": {},
        "revision_valuation_snapshot": {},
        "known_positive_facts": [],
        "known_counterfacts": [],
        "score_authority": False,
        "stage_authority": False,
    }


__all__ = ["compile_prompt_snapshot_audit"]
