"""Static authority audit for the Phase 83 question-contract demotion."""

from __future__ import annotations

import ast
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.dossier.scoring_pipeline import (
    V5_FINAL_STAGE_AUTHORITY,
    V5_PRODUCTION_SCORE_AUTHORITY,
)

from .research_question_seed_catalog import load_research_question_seed_catalog


QUESTION_AUTHORITY_PASS = "RESEARCH_QUESTION_SEED_AUTHORITY_PASS"


def audit_research_question_seed_authority(
    *, repo_root: str | Path = "."
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    catalog = load_research_question_seed_catalog(
        root / "configs/e2r_question_impact_contracts_v1.json"
    )
    future_root = root / "src/e2r/research_brain/researcher_mode"
    closure_imports = []
    closure_calls = []
    for path in sorted(future_root.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == "compile_question_closures_v2":
                        closure_imports.append(
                            {"path": path.relative_to(root).as_posix(), "line": node.lineno}
                        )
            elif isinstance(node, ast.Call):
                name = _call_name(node.func)
                if name.endswith("compile_question_closures_v2"):
                    closure_calls.append(
                        {"path": path.relative_to(root).as_posix(), "line": node.lineno}
                    )
    seed_rows = catalog.seeds
    critical = {
        "keyword_positive_scoring_authority_count": sum(
            row.production_score_authority for row in seed_rows
        ),
        "keyword_absence_authority_count": sum(row.absence_authority for row in seed_rows),
        "question_closure_required_for_component_score_count": len(closure_imports)
        + len(closure_calls),
        "question_seed_component_completion_authority_count": sum(
            row.component_completion_authority for row in seed_rows
        ),
        "question_seed_final_stage_authority_count": sum(
            row.final_stage_authority for row in seed_rows
        ),
        "legacy_dossier_production_authority_count": int(
            V5_PRODUCTION_SCORE_AUTHORITY
        ),
        "legacy_dossier_final_stage_authority_count": int(V5_FINAL_STAGE_AUTHORITY),
        "seed_catalog_missing_count": int(not seed_rows),
    }
    return {
        "schema_version": "e2r_v5_research_question_seed_authority_audit_v1",
        "status": QUESTION_AUTHORITY_PASS if sum(critical.values()) == 0 else "RESEARCH_QUESTION_SEED_AUTHORITY_FAIL",
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
        "seed_count": len(seed_rows),
        "archetype_count": len({row.archetype_id for row in seed_rows}),
        "future_namespace_question_closure_imports": closure_imports,
        "future_namespace_question_closure_calls": closure_calls,
        "catalog": catalog.to_dict(),
        "legacy_compatibility": {
            "QuestionImpactContract": {
                "production_score_authority": False,
                "component_completion_authority": False,
                "absence_authority": False,
                "final_stage_authority": False,
            },
            "dossier_scoring_pipeline": {
                "production_score_authority": V5_PRODUCTION_SCORE_AUTHORITY,
                "final_stage_authority": V5_FINAL_STAGE_AUTHORITY,
            },
        },
    }


def _call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_call_name(node.value)}.{node.attr}".lstrip(".")
    return ""


__all__ = ["QUESTION_AUTHORITY_PASS", "audit_research_question_seed_authority"]
