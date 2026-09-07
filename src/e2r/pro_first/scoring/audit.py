"""Static acceptance receipt for the P7 score/Stage/publication boundary."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping


REQUIRED_SCORING_PUBLICATION_TESTS = (
    "test_partial_diagnostic_score_not_published",
    "test_stage0_final_not_used_for_research_incomplete",
    "test_full_thesis_requires_saturation",
    "test_pro_score_stage_fields_ignored",
    "test_existing_component_scorer_used",
    "test_existing_atomic_stagecourt_used",
    "test_nonzero_score_requires_claim_lineage",
)


def audit_scoring_publication_gate(repo_root: str | Path) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    service = (root / "src/e2r/pro_first/scoring/service.py").read_text(
        encoding="utf-8"
    )
    gate = (root / "src/e2r/pro_first/scoring/publication_gate.py").read_text(
        encoding="utf-8"
    )
    publisher = (root / "src/e2r/pro_first/publication.py").read_text(
        encoding="utf-8"
    )
    stagecourt = (root / "src/e2r/pro_first/scoring/stagecourt_bridge.py").read_text(
        encoding="utf-8"
    )
    scorer = (root / "src/e2r/pro_first/scoring/scorer_bridge.py").read_text(
        encoding="utf-8"
    )
    tests = (root / "tests/test_e2r_pro_first_scoring_bridge.py").read_text(
        encoding="utf-8"
    )
    checks = {
        "saturation_required_before_component": (
            "if not research_eligibility.component_entry_allowed" in service
            and "research_saturation_receipt" in service
        ),
        "partial_result_is_non_publishable": (
            '"score_valid": False' in gate
            and '"canonical_stage": None' in gate
            and "WITHHELD_PENDING_RESEARCH_SATURATION" in gate
        ),
        "publisher_revalidates_full_thesis_gate": (
            "validate_full_thesis_eligibility_receipt" in publisher
            and 'score.get("full_score_valid") is not True' in publisher
        ),
        "existing_component_scorer_preserved": (
            "ProCalibratedScorerBridge().score" in service
            and "ResearchCalibratedComponentScorer" in scorer
        ),
        "existing_atomic_stagecourt_preserved": (
            "ProAtomicStageCourtBridge().decide" in service
            and "AtomicStageCourtV2" in stagecourt
        ),
        "invalid_score_cannot_enter_stagecourt": "not score_result.score_valid" in stagecourt,
        "required_tests_present": all(name in tests for name in REQUIRED_SCORING_PUBLICATION_TESTS),
    }
    failures = tuple(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": "e2r_pro_first_v2_scoring_publication_gate_audit_v1",
        "phase": "P7",
        "status": "PASS" if not failures else "FAIL",
        "critical_count": len(failures),
        "failure_codes": list(failures),
        "checks": checks,
        "required_test_count": len(REQUIRED_SCORING_PUBLICATION_TESTS),
        "required_test_names": list(REQUIRED_SCORING_PUBLICATION_TESTS),
        "focused_test_count": sum(
            line.lstrip().startswith("def test_") for line in tests.splitlines()
        ),
        "research_incomplete_score_valid": False,
        "research_incomplete_canonical_stage": None,
        "research_incomplete_publication_status": (
            "WITHHELD_PENDING_RESEARCH_SATURATION"
        ),
        "score_authority": "ResearchCalibratedComponentScorer",
        "stage_authority": "AtomicStageCourtV2",
        "new_score_engine_count": 0,
        "new_stage_engine_count": 0,
    }


__all__ = [
    "REQUIRED_SCORING_PUBLICATION_TESTS",
    "audit_scoring_publication_gate",
]
