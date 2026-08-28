"""Eight leaf-level independent reviewer gates for Pro-first V2.

Each reviewer executes its own focused test command and hashes the exact code,
configuration, and test leaves it reviewed.  A shared aggregate counter is
never accepted as reviewer evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Mapping, Sequence

from .ids import canonical_hash


@dataclass(frozen=True)
class ReviewerSpec:
    reviewer_id: str
    scope: str
    test_modules: tuple[str, ...]
    input_paths: tuple[str, ...]


REVIEWER_SPECS = (
    ReviewerSpec(
        "A",
        "36 contract totality / primitive coverage",
        ("tests.test_e2r_pro_first_v2_contract_totality",),
        (
            "configs/e2r_archetype_research_contracts_v2.json",
            "configs/e2r_archetype_research_blueprints_v2.json",
            "src/e2r/pro_first/research_contracts/loader.py",
            "src/e2r/pro_first/research_contracts/question_planner.py",
            "tests/test_e2r_pro_first_v2_contract_totality.py",
        ),
    ),
    ReviewerSpec(
        "B",
        "prompt compiler / archetype specificity / no gold leakage",
        ("tests.test_e2r_pro_first_v2_prompt_compiler",),
        (
            "configs/prompts/e2r_pro_v2_initial_full_research.md",
            "configs/prompts/e2r_pro_v2_delta_research.md",
            "src/e2r/pro_first/research_contracts/prompt_compiler.py",
            "tests/test_e2r_pro_first_v2_prompt_compiler.py",
        ),
    ),
    ReviewerSpec(
        "C",
        "multi-pass browser state / exactly-once follow-up",
        (
            "tests.test_e2r_pro_first_browser_adapter",
            "tests.test_e2r_pro_first_v2_multi_pass",
        ),
        (
            "src/e2r/pro_first/browser/chatgpt_adapter.py",
            "src/e2r/pro_first/multi_pass/ledger.py",
            "src/e2r/pro_first/multi_pass/orchestrator.py",
            "tests/test_e2r_pro_first_browser_adapter.py",
            "tests/test_e2r_pro_first_v2_multi_pass.py",
        ),
    ),
    ReviewerSpec(
        "D",
        "gap availability / adequate search / fixpoint",
        (
            "tests.test_e2r_pro_first_gap_adjudication",
            "tests.test_e2r_pro_first_v2_saturation",
        ),
        (
            "src/e2r/pro_first/gaps/adjudicator.py",
            "src/e2r/pro_first/gaps/source_family_policy.py",
            "src/e2r/pro_first/saturation/audit.py",
            "src/e2r/pro_first/saturation/fixpoint.py",
            "tests/test_e2r_pro_first_gap_adjudication.py",
            "tests/test_e2r_pro_first_v2_saturation.py",
        ),
    ),
    ReviewerSpec(
        "E",
        "source verifier / repair / lifecycle",
        (
            "tests.test_e2r_pro_first_source_verification",
            "tests.test_e2r_pro_first_v2_verifier_repair",
        ),
        (
            "src/e2r/pro_first/verification/source_verifier.py",
            "src/e2r/pro_first/verification/lifecycle_service.py",
            "src/e2r/pro_first/canary/live_v2.py",
            "tests/test_e2r_pro_first_source_verification.py",
            "tests/test_e2r_pro_first_v2_verifier_repair.py",
        ),
    ),
    ReviewerSpec(
        "F",
        "component/Judge/scoring/Stage publication gate",
        (
            "tests.test_e2r_pro_first_scoring_bridge",
            "tests.test_e2r_pro_first_v2_dossier_status",
            "tests.test_e2r_pro_first_v2_readiness_view",
        ),
        (
            "src/e2r/pro_first/scoring/service.py",
            "src/e2r/pro_first/publication.py",
            "src/e2r/pro_first/readiness_view.py",
            "tests/test_e2r_pro_first_scoring_bridge.py",
            "tests/test_e2r_pro_first_v2_dossier_status.py",
            "tests/test_e2r_pro_first_v2_readiness_view.py",
        ),
    ),
    ReviewerSpec(
        "G",
        "cross-archetype generalization / known-bad",
        (
            "tests.test_e2r_pro_first_v2_generalization",
            "tests.test_e2r_pro_first_v2_frozen_replay",
        ),
        (
            "tests/fixtures/pro_first_v2/known_bad_corpus.json",
            "src/e2r/pro_first/generalization/audit.py",
            "src/e2r/pro_first/generalization/known_bad.py",
            "src/e2r/pro_first/canary/frozen_replay.py",
            "tests/test_e2r_pro_first_v2_generalization.py",
            "tests/test_e2r_pro_first_v2_frozen_replay.py",
        ),
    ),
    ReviewerSpec(
        "H",
        "CI/security/performance/idempotency",
        (
            "tests.test_e2r_pro_first_v2_static_audit",
            "tests.test_e2r_pro_first_v2_1_fresh_efficiency_audit",
            "tests.test_e2r_pro_first_v2_live_runtime",
            "tests.test_e2r_pro_first_v2_independent_review",
        ),
        (
            ".github/workflows/e2r_pro_first_verify.yml",
            "src/e2r/pro_first/v2_static_audit.py",
            "src/e2r/pro_first/fresh_session/efficiency_audit.py",
            "src/e2r/pro_first/operations.py",
            "src/e2r/pro_first/packet.py",
            "src/e2r/pro_first/independent_review_v2.py",
            "tests/test_e2r_pro_first_v2_static_audit.py",
            "tests/test_e2r_pro_first_v2_1_fresh_efficiency_audit.py",
            "tests/test_e2r_pro_first_v2_live_runtime.py",
            "tests/test_e2r_pro_first_v2_independent_review.py",
        ),
    ),
)


def run_independent_reviewers(
    repo_root: str | Path,
    *,
    timeout_seconds: int = 1_200,
) -> Mapping[str, Any]:
    root = Path(repo_root).expanduser().resolve()
    if not (root / "src/e2r/pro_first").is_dir():
        raise ValueError("repo_root is not the E2R source tree")
    rows = tuple(
        _run_reviewer(root, spec, timeout_seconds=timeout_seconds)
        for spec in REVIEWER_SPECS
    )
    verdict = "PASS" if all(row["verdict"] == "PASS" for row in rows) else "FAIL"
    receipt: dict[str, Any] = {
        "schema_version": "e2r_pro_first_v2_independent_reviewer_gate_v1",
        "verdict": verdict,
        "reviewer_count": len(rows),
        "reviewers": list(rows),
        "shared_report_counter_used": False,
        "receipt_hash": "",
    }
    receipt["receipt_hash"] = canonical_hash(
        {key: value for key, value in receipt.items() if key != "receipt_hash"}
    )
    return receipt


def _run_reviewer(
    root: Path,
    spec: ReviewerSpec,
    *,
    timeout_seconds: int,
) -> Mapping[str, Any]:
    input_manifest = _input_manifest(root, spec.input_paths)
    command = "PYTHONPATH=src python -m unittest -v " + " ".join(spec.test_modules)
    env = dict(os.environ)
    env["PYTHONPATH"] = str(root / "src")
    timed_out = False
    try:
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "-v", *spec.test_modules],
            cwd=root,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout_seconds,
            check=False,
        )
        output = completed.stdout or b""
        exit_code = completed.returncode
    except subprocess.TimeoutExpired as error:
        timed_out = True
        output = error.stdout or b""
        if isinstance(output, str):
            output = output.encode("utf-8", errors="replace")
        exit_code = 124
    decoded = output.decode("utf-8", errors="replace")
    match = re.search(r"Ran (\d+) tests?", decoded)
    test_count = int(match.group(1)) if match else 0
    passed = exit_code == 0 and test_count > 0 and re.search(
        r"^OK(?:\s|$)", decoded, re.MULTILINE
    ) is not None
    return {
        "reviewer_id": spec.reviewer_id,
        "scope": spec.scope,
        "verdict": "PASS" if passed else "FAIL",
        "exact_command": command,
        "input_hash": canonical_hash(input_manifest),
        "input_manifest": input_manifest,
        "output_hash": hashlib.sha256(output).hexdigest(),
        "exit_code": exit_code,
        "timed_out": timed_out,
        "test_count": test_count,
        "finding": (
            f"{test_count} leaf-level tests passed for {spec.scope}."
            if passed
            else (
                f"Direct leaf review timed out for {spec.scope}."
                if timed_out
                else f"Direct leaf review failed for {spec.scope}."
            )
        ),
    }


def _input_manifest(root: Path, paths: Sequence[str]) -> list[Mapping[str, Any]]:
    rows: list[Mapping[str, Any]] = []
    for relative in paths:
        path = (root / relative).resolve()
        try:
            path.relative_to(root)
        except ValueError as error:
            raise ValueError(f"reviewer input escapes repo root: {relative}") from error
        if not path.is_file():
            raise FileNotFoundError(f"reviewer input is missing: {relative}")
        data = path.read_bytes()
        rows.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
            }
        )
    return rows


def write_independent_reviewer_receipt(
    receipt: Mapping[str, Any],
    output_path: str | Path,
) -> Path:
    destination = Path(output_path).expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return destination


__all__ = [
    "REVIEWER_SPECS",
    "ReviewerSpec",
    "run_independent_reviewers",
    "write_independent_reviewer_receipt",
]
