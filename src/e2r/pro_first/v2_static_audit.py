"""Requirement-level static acceptance audit for the Pro-first V2 goal."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Mapping

from .generalization import compile_generalization_acceptance
from .ids import canonical_hash
from .repair import compile_verifier_repair_contract_audit
from .research_contracts import (
    compile_contract_totality_audit,
    compile_prompt_snapshot_audit,
)
from .scoring.audit import audit_scoring_publication_gate
from .static_audit import compile_pro_first_static_audit


REQUIRED_V2_STATIC_COUNTER_KEYS = (
    "canonical_contract_missing_count",
    "research_contract_missing_count",
    "required_primitive_unmapped_count",
    "green_gate_unmapped_count",
    "guard_unmapped_count",
    "generic_filler_contract_count",
    "prompt_snapshot_missing_count",
    "prompt_forced_complete_count",
    "prompt_gold_leakage_count",
    "component_count_used_as_adequacy_count",
    "public_gap_downgraded_to_corroboration_count",
    "material_gap_without_followup_count",
    "verifier_repair_skipped_count",
    "partial_score_published_count",
    "research_incomplete_stage_final_count",
    "pro_score_authority_count",
    "pro_stage_authority_count",
    "future_leakage_count",
    "symbol_specific_branch_count",
    "deterministic_query_template_count",
)


def compile_pro_first_v2_static_audit(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    root = Path(repo_root).expanduser().resolve()
    contract = compile_contract_totality_audit(root)
    with TemporaryDirectory(prefix=".e2r-pro-v2-audit-", dir=root) as temporary:
        prompt = compile_prompt_snapshot_audit(root, output_root=temporary)
        prompt_texts = tuple(
            path.read_text(encoding="utf-8")
            for path in sorted(Path(temporary).glob("*.md"))
        )
    static = compile_pro_first_static_audit(root)
    scoring = audit_scoring_publication_gate(root)
    repair = compile_verifier_repair_contract_audit()
    generalization = compile_generalization_acceptance(root)
    contract_counts = dict(contract.get("counters") or {})
    prompt_failures = tuple(
        str(code)
        for row in prompt.get("snapshots") or ()
        for code in row.get("failure_codes") or ()
    )
    expected_snapshot_ids = {
        str(row.get("archetype_id") or "")
        for row in prompt.get("snapshots") or ()
    }
    tracked_snapshot_root = (
        root / "docs/operational/e2r_pro_first_v2/prompt_snapshots"
    )
    tracked_snapshot_ids = {
        path.stem for path in tracked_snapshot_root.glob("*.md")
    }
    behavior = _behavior_counters_from_sources(
        live_source=(root / "src/e2r/pro_first/canary/live_v2.py").read_text(
            encoding="utf-8"
        ),
        question_source=(
            root / "src/e2r/pro_first/saturation/question_closure.py"
        ).read_text(encoding="utf-8"),
        saturation_sources=tuple(
            path.read_text(encoding="utf-8")
            for path in sorted((root / "src/e2r/pro_first/saturation").glob("*.py"))
            if path.name != "audit.py"
        ),
    )
    scoring_checks = dict(scoring.get("checks") or {})
    static_counts = dict(static.get("critical_counts") or {})
    forbidden_gold_literals = (
        "23.202275",
        "70.2",
        "000660",
        "SK하이닉스",
        "first_pass_diagnostic_score",
        "expected_score",
        "expected_stage",
    )
    prompt_gold_leakage = sum(
        literal in text
        for text in prompt_texts
        for literal in forbidden_gold_literals
    )
    production_sources = tuple(
        path.read_text(encoding="utf-8")
        for path in sorted((root / "src/e2r/pro_first").rglob("*.py"))
        if "__pycache__" not in path.parts and path.name != "v2_static_audit.py"
    )
    symbol_specific = sum(
        literal in text
        for text in production_sources
        for literal in ("000660", "SK하이닉스")
    )
    future_guard_missing = int(
        "FUTURE_SOURCE_GUARD_MISSING" in prompt_failures
        or "FUTURE_SOURCE" not in set(repair.get("rejection_categories") or ())
        or int(
            (generalization.get("critical_counts") or {}).get(
                "golden_replay_failure_count", 0
            )
        )
        > 0
    )
    counters = {
        "canonical_contract_missing_count": max(
            0, 36 - int(contract_counts.get("canonical_contract_count") or 0)
        ),
        "research_contract_missing_count": int(
            contract_counts.get("missing_contract_count") or 0
        ),
        "required_primitive_unmapped_count": int(
            contract_counts.get("required_primitive_unmapped_count") or 0
        ),
        "green_gate_unmapped_count": int(
            contract_counts.get("green_gate_primitive_unmapped_count") or 0
        ),
        "guard_unmapped_count": int(
            contract_counts.get("guard_primitive_unmapped_count") or 0
        ),
        "generic_filler_contract_count": int(
            contract_counts.get("generic_filler_contract_count") or 0
        ),
        "prompt_snapshot_missing_count": len(
            expected_snapshot_ids - tracked_snapshot_ids
        ),
        "prompt_forced_complete_count": prompt_failures.count(
            "FORCED_COMPLETE_LITERAL"
        ),
        "prompt_gold_leakage_count": int(prompt_gold_leakage),
        "component_count_used_as_adequacy_count": behavior[
            "component_count_used_as_adequacy_count"
        ],
        "public_gap_downgraded_to_corroboration_count": behavior[
            "public_gap_downgraded_to_corroboration_count"
        ],
        "material_gap_without_followup_count": behavior[
            "material_gap_without_followup_count"
        ],
        "verifier_repair_skipped_count": behavior[
            "verifier_repair_skipped_count"
        ],
        "partial_score_published_count": int(
            not scoring_checks.get("partial_result_is_non_publishable", False)
            or not scoring_checks.get(
                "publisher_revalidates_full_thesis_gate", False
            )
        ),
        "research_incomplete_stage_final_count": int(
            scoring.get("research_incomplete_canonical_stage") is not None
            or scoring.get("research_incomplete_score_valid") is not False
        ),
        "pro_score_authority_count": int(
            static_counts.get("pro_score_authority_count") or 0
        ),
        "pro_stage_authority_count": int(
            static_counts.get("pro_stage_authority_count") or 0
        ),
        "future_leakage_count": future_guard_missing,
        "symbol_specific_branch_count": int(symbol_specific),
        "deterministic_query_template_count": int(
            static_counts.get("deterministic_query_template_count") or 0
        ),
    }
    if tuple(counters) != REQUIRED_V2_STATIC_COUNTER_KEYS:
        raise RuntimeError("V2 static audit counter roster drifted")
    critical_count = sum(counters.values())
    payload = {
        "schema_version": "e2r_pro_first_v2_static_audit_v1",
        "status": "PASS" if critical_count == 0 else "FAIL",
        "counters": counters,
        "critical_count": critical_count,
        "contract_audit_status": contract.get("status"),
        "contract_audit_hash": canonical_hash(contract),
        "prompt_audit_status": prompt.get("status"),
        "prompt_audit_hash": prompt.get("audit_hash"),
        "production_static_audit_status": static.get("status"),
        "production_static_audit_hash": canonical_hash(static),
        "scoring_publication_audit_status": scoring.get("status"),
        "scoring_publication_audit_hash": canonical_hash(scoring),
        "verifier_repair_audit_status": repair.get("status"),
        "verifier_repair_audit_hash": canonical_hash(repair),
        "generalization_audit_status": generalization.get("status"),
        "generalization_audit_hash": generalization.get("audit_hash"),
    }
    return {**payload, "audit_hash": canonical_hash(payload)}


def _behavior_counters_from_sources(
    *,
    live_source: str,
    question_source: str,
    saturation_sources: tuple[str, ...],
) -> Mapping[str, int]:
    public_position = question_source.find("elif public_material:")
    corroboration_position = question_source.find("elif missing_corroboration:")
    repair_position = live_source.find("await self._run_repairs(")
    scoring_position = live_source.find("ProScoringPipelineService(")
    return {
        "component_count_used_as_adequacy_count": sum(
            "component_fact_count" in source for source in saturation_sources
        ),
        "public_gap_downgraded_to_corroboration_count": int(
            public_position < 0
            or corroboration_position < 0
            or public_position > corroboration_position
        ),
        "material_gap_without_followup_count": int(
            "public_material_gap_question_ids" not in live_source
            or live_source.count("await self._close_public_gaps(") < 2
        ),
        "verifier_repair_skipped_count": int(
            repair_position < 0
            or scoring_position < 0
            or repair_position > scoring_position
        ),
    }


__all__ = [
    "REQUIRED_V2_STATIC_COUNTER_KEYS",
    "compile_pro_first_v2_static_audit",
]
