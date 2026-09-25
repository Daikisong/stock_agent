"""Reproducible P8 all-archetype/generalization acceptance receipt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from ..ids import canonical_hash
from .golden import MANDATORY_MECHANISM_FAMILIES, run_mechanism_golden_replay
from .known_bad import REQUIRED_V2_KNOWN_BAD_CASE_IDS, audit_v2_known_bad_corpus


def compile_generalization_acceptance(
    repo_root: str | Path,
) -> Mapping[str, Any]:
    root = Path(repo_root).resolve()
    fixture_root = root / "tests/fixtures/pro_first_v2"
    golden_payload = _read_json(fixture_root / "mechanism_golden_cases.json")
    known_bad_payload = _read_json(fixture_root / "known_bad_corpus.json")
    prompt_audit = _read_json(
        root / "docs/operational/e2r_pro_first_v2/prompt_snapshot_audit.json"
    )
    cases = tuple(golden_payload.get("cases") or ())
    replays = []
    for case in cases:
        primary_id = str(case["primary_archetype_id"])
        prompt_path = (
            root
            / "docs/operational/e2r_pro_first_v2/prompt_snapshots"
            / f"{primary_id}.md"
        )
        replays.append(
            run_mechanism_golden_replay(
                case,
                prompt_snapshot=prompt_path.read_text(encoding="utf-8"),
            )
        )
    mechanism_ids = tuple(str(row.get("mechanism_family") or "") for row in cases)
    missing_mechanisms = [
        value for value in MANDATORY_MECHANISM_FAMILIES if value not in mechanism_ids
    ]
    extra_mechanisms = [
        value for value in mechanism_ids if value not in MANDATORY_MECHANISM_FAMILIES
    ]
    known_bad_audit = audit_v2_known_bad_corpus(known_bad_payload)
    critical_counts = {
        "mechanism_roster_mismatch_count": int(
            mechanism_ids != MANDATORY_MECHANISM_FAMILIES
        ),
        "mechanism_missing_count": len(missing_mechanisms),
        "mechanism_extra_count": len(extra_mechanisms),
        "golden_replay_failure_count": sum(row["status"] != "PASS" for row in replays),
        "prompt_snapshot_critical_count": int(prompt_audit.get("critical_count") or 0),
        "prompt_snapshot_count_mismatch_count": int(
            prompt_audit.get("prompt_snapshot_count") != 36
        ),
        "known_bad_critical_count": int(known_bad_audit["critical_count_sum"]),
        "known_bad_count_mismatch_count": int(
            known_bad_audit["observed_case_count"]
            != len(REQUIRED_V2_KNOWN_BAD_CASE_IDS)
        ),
        "offline_query_or_fetch_count": sum(
            int(row["query_count"]) + int(row["fetch_count"]) for row in replays
        ),
        "score_stage_authority_count": sum(
            int(row["score_authority"] is not False)
            + int(row["stage_authority"] is not False)
            for row in replays
        ),
    }
    critical_sum = sum(critical_counts.values())
    payload: dict[str, Any] = {
        "schema_version": "e2r_pro_first_v2_generalization_acceptance_v1",
        "phase": "P8",
        "status": "PASS" if critical_sum == 0 else "FAIL",
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
        "mandatory_mechanism_count": len(MANDATORY_MECHANISM_FAMILIES),
        "observed_mechanism_count": len(cases),
        "missing_mechanism_families": missing_mechanisms,
        "extra_mechanism_families": extra_mechanisms,
        "golden_replay_pass_count": sum(row["status"] == "PASS" for row in replays),
        "prompt_snapshot_count": int(prompt_audit.get("prompt_snapshot_count") or 0),
        "prompt_snapshot_audit_hash": str(prompt_audit.get("audit_hash") or ""),
        "known_bad_required_count": len(REQUIRED_V2_KNOWN_BAD_CASE_IDS),
        "known_bad_observed_count": int(known_bad_audit["observed_case_count"]),
        "known_bad_corpus_leaf_hash": str(known_bad_audit["corpus_leaf_hash"]),
        "acceptance_metrics": [
            "critical_question_recall",
            "material_positive_counter_recall",
            "source_role_coverage",
            "question_terminality",
            "public_gap_closure",
            "verifier_repair_completion",
            "no_future_leakage",
            "no_gold_injection",
        ],
        "golden_replays": replays,
        "known_bad_audit": known_bad_audit,
        "production_runtime_ready": False,
        "fixture_only": True,
    }
    return {**payload, "audit_hash": canonical_hash(payload)}


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return payload


__all__ = ["compile_generalization_acceptance"]
