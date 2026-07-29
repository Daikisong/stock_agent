"""Phase 100 independent reviewers and final hard-gate truth.

Each reviewer executes its own detector suite and recomputes its own leaf
checks.  A single critical count makes that reviewer fail, and a single failed
reviewer makes the combined gate fail.  The module can therefore publish a
useful NOT_READY packet while live canary research is still pending, but it
cannot manufacture the final readiness label.
"""

from __future__ import annotations

import hashlib
import io
import json
import re
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from e2r.production.metadata import stable_hash, write_json, write_text

from .canary_leaf_contract import (
    CANARY_MASTER_LEAF_FILES,
    canary_output_tree_hash,
)
from .full_thesis_gold_benchmark import PHASE93_POST_RUN_PASS


SCHEMA_VERSION = "e2r_v5_phase100_independent_acceptance_v1"
REVIEWER_GATE_PASS = "E2R_V5_INDEPENDENT_REVIEWER_GATE_PASS"
REVIEWER_GATE_FAIL = "E2R_V5_INDEPENDENT_REVIEWER_GATE_FAIL"
FINAL_READY_LABEL = "MEANINGFUL_E2R_RESEARCHER_PARITY_READY"
FINAL_NOT_READY_LABEL = "MEANINGFUL_E2R_RESEARCHER_PARITY_NOT_READY"

DEFAULT_REVIEWER_GATE_PATH = Path("docs/operational/e2r_v5_reviewer_gate.json")
DEFAULT_FINAL_READINESS_PATH = Path("docs/operational/e2r_v5_final_readiness.md")
DEFAULT_COMPONENT_CALIBRATION_PATH = Path(
    "docs/operational/e2r_v5_component_score_calibration.json"
)
DEFAULT_STAGECOURT_AUDIT_PATH = Path(
    "docs/operational/e2r_v5_stagecourt_audit.json"
)
DEFAULT_FULL_TEST_EVIDENCE_PATH = Path(
    "docs/operational/e2r_v5_full_test_result.json"
)
_FULL_TEST_COUNT_RE = re.compile(r"^Ran\s+(\d+)\s+tests?\s+in\s+[0-9.]+s$", re.MULTILINE)
_FULL_TEST_OK_RE = re.compile(r"^OK(?:\s+\(.+\))?$", re.MULTILINE)
_FULL_TEST_FAILED_RE = re.compile(r"^FAILED(?:\s+\(.+\))?$", re.MULTILINE)


@dataclass(frozen=True)
class IndependentReviewerSpec:
    reviewer_id: str
    title: str
    scope: str
    detector_ids: tuple[str, ...]
    required_leaf_paths: tuple[str, ...]

    def __post_init__(self) -> None:
        if self.reviewer_id not in tuple("ABCDEFGHIJ"):
            raise ValueError("Phase 100 reviewer id must be A through J")
        if not all((self.title, self.scope, self.detector_ids)):
            raise ValueError("Phase 100 reviewer requires title, scope, and detectors")


REVIEWER_SPECS = (
    IndependentReviewerSpec(
        "A",
        "Historical Corpus Fidelity",
        "research rows / score schemas / anchors",
        (
            "tests.test_e2r_v5_historical_judgment_atlas.E2RV5HistoricalJudgmentAtlasTests.test_operational_full_corpus_atlas_is_committed_pass",
            "tests.test_e2r_v5_component_anchor_atlas.E2RV5ComponentAnchorAtlasTests.test_exact_anchors_are_source_backed_and_proxy_rows_are_guard_only",
            "tests.test_e2r_v5_historical_blind_replay.E2RV5HistoricalBlindReplayTests.test_phase91_audit_is_reproducible_and_passes_every_threshold",
        ),
        (
            "docs/operational/e2r_v5_historical_judgment_atlas_audit.json",
            "docs/operational/e2r_v5_component_anchor_atlas.json",
            "docs/operational/e2r_v5_historical_blind_replay.json",
        ),
    ),
    IndependentReviewerSpec(
        "B",
        "Research Aperture",
        "queries / source families / documents / material fact recall",
        (
            "tests.test_e2r_v5_legacy_retrieval_aperture.E2RV5LegacyRetrievalApertureTests.test_acceptance_recall_is_above_threshold",
            "tests.test_e2r_v5_source_graph_acquisition.E2RV5SourceGraphAcquisitionTests.test_graph_keeps_official_structured_independent_and_reference_expansion",
            "tests.test_e2r_v5_full_thesis_gold_benchmark.E2RV5FullThesisGoldBenchmarkTests.test_all_ten_public_source_families_exist_for_each_target",
        ),
        (
            "docs/operational/e2r_v5_legacy_retrieval_parity.json",
            "docs/operational/e2r_v5_source_graph_acquisition_audit.json",
            "docs/operational/e2r_v5_gold_research_recall.json",
        ),
    ),
    IndependentReviewerSpec(
        "C",
        "Evidence Fact Graph",
        "scope / currentness / dedupe / utilization",
        (
            "tests.test_e2r_v5_evidence_fact_graph.E2RV5EvidenceFactGraphTests.test_all_material_claims_end_in_exact_utilization_roster",
            "tests.test_e2r_v5_evidence_fact_graph.E2RV5EvidenceFactGraphTests.test_same_economic_fact_gets_one_fact_and_independent_confidence_gain",
        ),
        (
            "docs/operational/e2r_v5_evidence_fact_graph_claim_utilization_audit.json",
        ),
    ),
    IndependentReviewerSpec(
        "D",
        "Component Research Memos",
        "positive / counter / why higher / why lower",
        (
            "tests.test_e2r_v5_researcher_mode.E2RV5ResearcherModeTests.test_phase84_modules_and_ten_roles_are_committed_and_audited",
            "tests.test_e2r_v5_component_scoring_memos.E2RV5ComponentScoringMemoTests.test_each_judge_memo_has_exact_phase89_output_and_lineage",
        ),
        (
            "docs/operational/e2r_v5_researcher_mode_architecture_audit.json",
            "docs/operational/e2r_v5_component_scoring_memos_audit.json",
        ),
    ),
    IndependentReviewerSpec(
        "E",
        "Score Calibration",
        "historical parity / dynamic range / monotonicity",
        (
            "tests.test_e2r_v5_historical_blind_replay.E2RV5HistoricalBlindReplayTests.test_dynamic_range_canary_contains_historical_high_mid_and_low",
            "tests.test_e2r_v5_historical_blind_replay.E2RV5HistoricalBlindReplayTests.test_critical_positive_counter_ordering_and_guards_are_perfect",
            "tests.test_e2r_v5_deterministic_score_aggregator.E2RV5DeterministicScoreAggregatorTests.test_strong_high_anchor_equivalent_evidence_does_not_collapse_to_one_to_three_points",
        ),
        (
            "docs/operational/e2r_v5_historical_blind_replay.json",
            "docs/operational/e2r_v5_deterministic_score_aggregator_audit.json",
        ),
    ),
    IndependentReviewerSpec(
        "F",
        "Live Canary Dossiers",
        "full seven-component dossier and current evidence for mandatory targets",
        (
            "tests.test_e2r_v5_phase94_runner_contract.E2RV5Phase94RunnerContractTests.test_pending_checkpoint_writes_honest_full_dossier_without_gold",
            "tests.test_e2r_v5_phase94_runner_contract.E2RV5Phase94RunnerContractTests.test_target_registry_resolves_master_canaries_without_runner_branch",
        ),
        ("configs/e2r_targeted_live_smoke_v1.json",),
    ),
    IndependentReviewerSpec(
        "G",
        "StageCourt",
        "score / Stage / risk / event separation",
        (
            "tests.test_e2r_v5_stagecourt.E2RV5StageCourtTests.test_daily_event_overlay_cannot_change_canonical_stage",
            "tests.test_e2r_v5_stagecourt.E2RV5StageCourtTests.test_hard_break_requires_open_official_target_mechanism_claim",
        ),
        (),
    ),
    IndependentReviewerSpec(
        "H",
        "Generalization",
        "all archetypes and no target branches",
        (
            "tests.test_e2r_v5_all_archetype_generalization.E2RV5AllArchetypeGeneralizationTests.test_complete_registry_enters_the_same_seven_component_path",
            "tests.test_e2r_v5_full_thesis_gold_benchmark.E2RV5FullThesisGoldBenchmarkTests.test_generic_validator_contains_no_canary_target_branch",
        ),
        ("docs/operational/e2r_v5_all_archetype_generalization.json",),
    ),
    IndependentReviewerSpec(
        "I",
        "Daily and Census",
        "selective deep / dossier reuse / delta refresh",
        (
            "tests.test_e2r_v5_daily_census_integration.E2RV5DailyCensusIntegrationTests.test_every_universe_member_gets_assessment_but_deep_is_selective",
            "tests.test_e2r_v5_daily_census_integration.E2RV5DailyCensusIntegrationTests.test_unchanged_full_thesis_is_reused_without_daily_deep_research",
            "tests.test_e2r_v5_daily_census_integration.E2RV5DailyCensusIntegrationTests.test_completed_delta_computes_score_change_only_after_deterministic_update",
        ),
        ("docs/operational/e2r_v5_daily_census_integration.json",),
    ),
    IndependentReviewerSpec(
        "J",
        "Runtime Honesty",
        "actual LLM / query / fetch / provider / checkpoint / hash",
        (
            "tests.test_e2r_v5_source_graph_acquisition.E2RV5SourceGraphAcquisitionTests.test_checkpoint_resume_fetches_every_material_candidate_without_research_completion",
            "tests.test_e2r_v5_researcher_mode.E2RV5ResearcherModeTests.test_provider_outage_is_research_pending_without_score_or_stage",
        ),
        (
            "docs/operational/e2r_v5_self_repair_audit.json",
            "docs/operational/e2r_v5_capability_known_bad_audit.json",
        ),
    ),
)


class _RecordingResult(unittest.TextTestResult):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.passed_ids: set[str] = set()

    def addSuccess(self, test: unittest.case.TestCase) -> None:  # noqa: N802
        super().addSuccess(test)
        self.passed_ids.add(test.id())


def _run_reviewer_detectors(
    detector_ids: Sequence[str],
) -> tuple[_RecordingResult, str]:
    suite = unittest.TestSuite(
        unittest.TestLoader().loadTestsFromName(test_id) for test_id in detector_ids
    )
    stream = io.StringIO()
    result = unittest.TextTestRunner(
        stream=stream,
        verbosity=0,
        resultclass=_RecordingResult,
    ).run(suite)
    return result, stream.getvalue()


def compile_phase100_acceptance_bundle(
    workspace_root: str | Path = ".",
) -> Mapping[str, Any]:
    root = Path(workspace_root)
    context = _acceptance_context(root)
    reviewers = []
    for spec in REVIEWER_SPECS:
        result, output = _run_reviewer_detectors(spec.detector_ids)
        leaf_rows = tuple(_leaf_row(root, path) for path in spec.required_leaf_paths)
        custom = _REVIEWER_CHECKS[spec.reviewer_id](context, root)
        critical_counts = {
            "detector_failure_count": len(result.failures),
            "detector_error_count": len(result.errors),
            "detector_run_count_mismatch": abs(
                result.testsRun - len(spec.detector_ids)
            ),
            "missing_required_leaf_count": sum(
                not row["exists"] for row in leaf_rows
            ),
            **custom["critical_counts"],
        }
        critical_sum = sum(critical_counts.values())
        reviewers.append(
            {
                "reviewer_id": spec.reviewer_id,
                "title": spec.title,
                "scope": spec.scope,
                "status": "PASS" if critical_sum == 0 else "FAIL",
                "detector_ids": list(spec.detector_ids),
                "detector_run_count": result.testsRun,
                "detector_pass_count": len(result.passed_ids),
                "required_leaves": list(leaf_rows),
                "recomputed_metrics": custom["metrics"],
                "blockers": custom["blockers"],
                "critical_counts": critical_counts,
                "critical_count_sum": critical_sum,
                "runner_output": output if critical_sum and (result.failures or result.errors) else "",
            }
        )

    failed_reviewers = [row["reviewer_id"] for row in reviewers if row["status"] == "FAIL"]
    reviewer_critical_sum = sum(row["critical_count_sum"] for row in reviewers)
    blockers = tuple(
        dict.fromkeys(
            blocker
            for row in reviewers
            for blocker in row["blockers"]
        )
    )
    gate = {
        "schema_version": SCHEMA_VERSION,
        "status": REVIEWER_GATE_PASS if reviewer_critical_sum == 0 else REVIEWER_GATE_FAIL,
        "reviewer_count": len(reviewers),
        "reviewer_roster": [row["reviewer_id"] for row in reviewers],
        "reviewers": reviewers,
        "failed_reviewers": failed_reviewers,
        "critical_count_sum": reviewer_critical_sum,
        "blockers": list(blockers),
        "all_reviewers_independently_recomputed": True,
        "one_critical_forces_failure": True,
        "production_readiness_authority": reviewer_critical_sum == 0,
        "exact_verdict": (
            FINAL_READY_LABEL if reviewer_critical_sum == 0 else FINAL_NOT_READY_LABEL
        ),
    }
    calibration = _component_calibration_artifact(context)
    stagecourt = _stagecourt_audit_artifact(context)
    dossiers = {
        row["target_id"]: _render_canary_dossier(row)
        for row in context["canary_rows"]
    }
    readiness = _render_final_readiness(
        gate=gate,
        context=context,
        calibration=calibration,
        stagecourt=stagecourt,
    )
    return {
        "reviewer_gate": gate,
        "component_score_calibration": calibration,
        "stagecourt_audit": stagecourt,
        "dossiers": dossiers,
        "final_readiness": readiness,
    }


def write_phase100_acceptance_artifacts(
    *,
    workspace_root: str | Path = ".",
) -> Mapping[str, Path]:
    root = Path(workspace_root)
    bundle = compile_phase100_acceptance_bundle(root)
    paths: dict[str, Path] = {
        "reviewer_gate": root / DEFAULT_REVIEWER_GATE_PATH,
        "component_score_calibration": root / DEFAULT_COMPONENT_CALIBRATION_PATH,
        "stagecourt_audit": root / DEFAULT_STAGECOURT_AUDIT_PATH,
        "final_readiness": root / DEFAULT_FINAL_READINESS_PATH,
    }
    write_json(paths["reviewer_gate"], bundle["reviewer_gate"])
    write_json(
        paths["component_score_calibration"],
        bundle["component_score_calibration"],
    )
    write_json(paths["stagecourt_audit"], bundle["stagecourt_audit"])
    write_text(paths["final_readiness"], bundle["final_readiness"])

    target_specs = _target_specs(root)
    dossier_by_target = bundle["dossiers"]
    for index, spec in enumerate(target_specs):
        target_id = str(spec.get("symbol") or "")
        suffix = "samsung" if index == 0 else "hynix" if index == 1 else target_id
        key = f"dossier_{target_id}"
        paths[key] = root / f"docs/operational/e2r_v5_{suffix}_researcher_dossier.md"
        write_text(paths[key], dossier_by_target[target_id])
    return paths


def verification_tree_hash(workspace_root: str | Path = ".") -> str:
    """Hash executable source/tests/configs without self-referential result files."""

    root = Path(workspace_root)
    paths = sorted(
        (
            *root.glob("src/**/*.py"),
            *root.glob("tests/**/*.py"),
            *root.glob("configs/**/*.json"),
            *root.glob("configs/**/*.yaml"),
            *root.glob("configs/**/*.yml"),
        ),
        key=lambda path: str(path.relative_to(root)),
    )
    digest = hashlib.sha256()
    for path in paths:
        if not path.is_file():
            continue
        relative = str(path.relative_to(root)).replace("\\", "/")
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def validate_full_test_evidence(
    workspace_root: str | Path,
    evidence: Mapping[str, Any],
    *,
    expected_tree_hash: str,
) -> Mapping[str, Any]:
    """Validate the full-test receipt against its immutable source log."""

    root = Path(workspace_root).resolve()
    raw_log_path = evidence.get("log_path")
    log_path_safe = isinstance(raw_log_path, str) and bool(raw_log_path.strip())
    log_path: Path | None = None
    if log_path_safe:
        candidate = (root / raw_log_path).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            log_path_safe = False
        else:
            log_path = candidate
    log_exists = bool(log_path_safe and log_path and log_path.is_file())
    log_bytes = log_path.read_bytes() if log_exists and log_path else b""
    try:
        log_text = log_bytes.decode("utf-8")
    except UnicodeDecodeError:
        log_text = ""
    count_matches = tuple(_FULL_TEST_COUNT_RE.finditer(log_text))
    logged_test_count = int(count_matches[-1].group(1)) if count_matches else 0
    reported_test_count = evidence.get("test_count")
    test_count_is_integer = (
        isinstance(reported_test_count, int)
        and not isinstance(reported_test_count, bool)
        and reported_test_count > 0
    )
    command = evidence.get("command")
    command_is_full_discovery = bool(
        isinstance(command, list)
        and len(command) >= 7
        and command[-6:] == ["-m", "unittest", "discover", "-s", "tests", "-v"]
    )
    checks = {
        "status_pass": evidence.get("status") == "PASS",
        "full_discovery_true": evidence.get("full_discovery") is True,
        "exit_code_zero": evidence.get("exit_code") == 0
        and not isinstance(evidence.get("exit_code"), bool),
        "verification_tree_stable": evidence.get("verification_tree_stable_during_run")
        is True,
        "verification_tree_hash_matches": evidence.get("verification_tree_hash")
        == expected_tree_hash,
        "test_count_positive_integer": test_count_is_integer,
        "command_is_full_discovery": command_is_full_discovery,
        "log_path_safe": log_path_safe,
        "log_exists": log_exists,
        "log_sha256_matches": bool(
            log_exists
            and hashlib.sha256(log_bytes).hexdigest() == evidence.get("log_sha256")
        ),
        "log_test_count_matches": bool(
            test_count_is_integer and logged_test_count == reported_test_count
        ),
        "log_reports_ok": bool(
            _FULL_TEST_OK_RE.search(log_text)
            and not _FULL_TEST_FAILED_RE.search(log_text)
        ),
    }
    return {
        "valid": all(checks.values()),
        "checks": checks,
        "logged_test_count": logged_test_count,
        "reported_test_count": reported_test_count,
        "log_sha256": (
            hashlib.sha256(log_bytes).hexdigest() if log_exists else None
        ),
    }


def _acceptance_context(root: Path) -> Mapping[str, Any]:
    documents = {
        "atlas": _read_json(root / "docs/operational/e2r_v5_historical_judgment_atlas_audit.json"),
        "anchors": _read_json(root / "docs/operational/e2r_v5_component_anchor_atlas.json"),
        "blind": _read_json(root / "docs/operational/e2r_v5_historical_blind_replay.json"),
        "legacy": _read_json(root / "docs/operational/e2r_v5_legacy_retrieval_parity.json"),
        "gold": _read_json(root / "docs/operational/e2r_v5_gold_research_recall.json"),
        "source_graph": _read_json(root / "docs/operational/e2r_v5_source_graph_acquisition_audit.json"),
        "fact_graph": _read_json(root / "docs/operational/e2r_v5_evidence_fact_graph_claim_utilization_audit.json"),
        "researcher": _read_json(root / "docs/operational/e2r_v5_researcher_mode_architecture_audit.json"),
        "memos": _read_json(root / "docs/operational/e2r_v5_component_scoring_memos_audit.json"),
        "aggregator": _read_json(root / "docs/operational/e2r_v5_deterministic_score_aggregator_audit.json"),
        "generalization": _read_json(root / "docs/operational/e2r_v5_all_archetype_generalization.json"),
        "daily": _read_json(root / "docs/operational/e2r_v5_daily_census_integration.json"),
        "phase98": _read_json(root / "docs/operational/e2r_v5_capability_known_bad_audit.json"),
        "phase99": _read_json(root / "docs/operational/e2r_v5_self_repair_audit.json"),
        "full_test": _read_json(root / DEFAULT_FULL_TEST_EVIDENCE_PATH),
    }
    canary_rows = _canary_rows(root)
    return {
        "documents": documents,
        "canary_rows": canary_rows,
        "verification_tree_hash": verification_tree_hash(root),
    }


def _canary_rows(root: Path) -> tuple[Mapping[str, Any], ...]:
    rows = []
    for spec in _target_specs(root):
        target_id = str(spec.get("symbol") or "")
        manifests = sorted(
            root.glob(f"output/researcher_mode/**/{target_id}/target_run_manifest.json"),
            key=lambda path: str(path),
        )
        manifest_path = manifests[-1] if manifests else None
        manifest = _read_json(manifest_path) if manifest_path else {}
        output_root = manifest_path.parent if manifest_path else None
        cache = manifest.get("provider_response_cache") or {}
        leaf_names = tuple(CANARY_MASTER_LEAF_FILES.values())
        leaf_presence = {
            name: bool(output_root and (output_root / name).is_file())
            for name in leaf_names
        }
        manifest_output_tree_hash = str(manifest.get("output_tree_hash") or "")
        actual_output_tree_hash = (
            canary_output_tree_hash(output_root) if output_root else ""
        )
        leaf_contract = (
            _read_json(output_root / "canary_leaf_contract_audit.json")
            if output_root
            else {}
        )
        rows.append(
            {
                "target_id": target_id,
                "company_name": str(spec.get("company_name") or "UNKNOWN"),
                "manifest_path": (
                    str(manifest_path.relative_to(root)) if manifest_path else None
                ),
                "output_root": (
                    str(output_root.relative_to(root)) if output_root else None
                ),
                "status": str(manifest.get("status") or "LIVE_RESEARCH_NOT_STARTED"),
                "production_research_complete": manifest.get("production_research_complete") is True,
                "document_count": int(manifest.get("document_count") or 0),
                "fact_count": int(manifest.get("fact_count") or 0),
                "counterfact_count": int(manifest.get("counterfact_count") or 0),
                "component_memo_count": int(manifest.get("component_memo_count") or 0),
                "query_count": int(manifest.get("query_count") or 0),
                "output_tree_hash": manifest_output_tree_hash,
                "actual_output_tree_hash": actual_output_tree_hash,
                "output_tree_hash_matches": bool(
                    manifest_output_tree_hash
                    and manifest_output_tree_hash == actual_output_tree_hash
                ),
                "canary_leaf_contract_status": leaf_contract.get("status"),
                "canary_leaf_contract_critical_count": int(
                    leaf_contract.get("critical_count_sum") or 0
                )
                if leaf_contract
                else 1,
                "provider_logical_call_count": int(cache.get("logical_call_count") or 0),
                "provider_successful_call_count": int(cache.get("successful_call_count") or 0),
                "provider_error_count": int(cache.get("provider_error_count") or 0),
                "leaf_presence": leaf_presence,
                "score_valid": _canary_score_valid(output_root),
                "stage_final": _canary_stage_final(output_root),
            }
        )
    return tuple(rows)


def _target_specs(root: Path) -> tuple[Mapping[str, Any], ...]:
    payload = _read_json(root / "configs/e2r_targeted_live_smoke_v1.json")
    return tuple(payload.get("mandatory_targets") or ())


def _canary_score_valid(output_root: Path | None) -> bool:
    if output_root is None:
        return False
    score = _read_json(output_root / CANARY_MASTER_LEAF_FILES["score_vector"])
    return bool(
        score.get("status") == "COMPLETE"
        and score.get("score_valid") is True
        and isinstance(score.get("component_score_vector"), Mapping)
    )


def _canary_stage_final(output_root: Path | None) -> bool:
    if output_root is None:
        return False
    decision = _read_json(output_root / "atomic_stage_decision.json")
    trace = _read_json(output_root / "stagecourt_trace.json")
    return bool(
        decision.get("status") == "FINAL"
        and decision.get("score_valid") is True
        and decision.get("canonical_stage")
        and trace
    )


def _base_document_critical(document: Mapping[str, Any]) -> int:
    value = document.get("critical_count_sum")
    return int(value) if isinstance(value, int) and not isinstance(value, bool) else 1


def _review_a(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    docs = context["documents"]
    blind = docs["blind"]
    metrics = blind.get("metric_values") or {}
    coverage = float(docs["atlas"].get("registry_archetype_coverage_rate") or 0.0)
    critical = {
        "atlas_critical_count": _base_document_critical(docs["atlas"]),
        "anchor_critical_count": _base_document_critical(docs["anchors"]),
        "blind_replay_critical_count": _base_document_critical(blind),
        "registry_coverage_failure_count": int(coverage < 1.0),
        "future_leakage_count": int(
            not blind.get("future_outcomes_hidden_from_researcher", False)
        ),
    }
    return _custom_result(critical, {"registry_coverage": coverage, **metrics})


def _review_b(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    docs = context["documents"]
    gold_comparison = docs["gold"].get("post_run_comparison") or {}
    recall_thresholds = gold_comparison.get("thresholds") or {
        "critical_material_fact_recall_min": 1.0,
        "counter_supersession_recall_min": 1.0,
        "all_material_fact_recall_min": 0.95,
        "component_research_topic_coverage_min": 1.0,
    }
    legacy_recall = float(
        (docs["legacy"].get("metric_values") or {}).get(
            "legacy_valid_material_fact_recall", 0.0
        )
    )
    comparison_complete = gold_comparison.get("status") in {
        "PASS",
        "COMPLETE",
        PHASE93_POST_RUN_PASS,
    }
    critical = {
        "legacy_retrieval_critical_count": _base_document_critical(docs["legacy"]),
        "source_graph_critical_count": _base_document_critical(docs["source_graph"]),
        "gold_benchmark_critical_count": _base_document_critical(docs["gold"]),
        "legacy_recall_threshold_failure_count": int(legacy_recall < 0.95),
        "current_material_fact_recall_missing_count": int(not comparison_complete),
        **{
            f"{metric_name}_threshold_failure_count": _threshold_failure(
                gold_comparison.get(metric_name),
                recall_thresholds.get(f"{metric_name}_min"),
            )
            for metric_name in (
                "critical_material_fact_recall",
                "counter_supersession_recall",
                "all_material_fact_recall",
                "component_research_topic_coverage",
            )
        },
    }
    blockers = (
        ("PHASE94_CLEAN_GOLD_RECALL_COMPARISON_PENDING",)
        if not comparison_complete
        else ()
    )
    return _custom_result(
        critical,
        {
            "legacy_valid_material_fact_recall": legacy_recall,
            "current_gold_comparison_status": gold_comparison.get("status"),
            "all_material_fact_recall": gold_comparison.get("all_material_fact_recall"),
            "critical_material_fact_recall": gold_comparison.get("critical_material_fact_recall"),
            "counter_supersession_recall": gold_comparison.get("counter_supersession_recall"),
            "component_research_topic_coverage": gold_comparison.get(
                "component_research_topic_coverage"
            ),
            "thresholds": dict(recall_thresholds),
        },
        blockers,
    )


def _review_c(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    fact_graph = context["documents"]["fact_graph"]
    return _custom_result(
        {"fact_graph_critical_count": _base_document_critical(fact_graph)},
        {
            "status": fact_graph.get("status"),
            "material_claim_lost_count": (fact_graph.get("critical_counts") or {}).get(
                "material_claim_lost_count", 0
            ),
        },
    )


def _review_d(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    docs = context["documents"]
    return _custom_result(
        {
            "researcher_architecture_critical_count": _base_document_critical(docs["researcher"]),
            "component_memo_critical_count": _base_document_critical(docs["memos"]),
        },
        {
            "researcher_status": docs["researcher"].get("status"),
            "component_memo_status": docs["memos"].get("status"),
        },
    )


def _review_e(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    docs = context["documents"]
    metrics = docs["blind"].get("metric_values") or {}
    critical = {
        "historical_parity_critical_count": _base_document_critical(docs["blind"]),
        "aggregator_critical_count": _base_document_critical(docs["aggregator"]),
        "component_mae_threshold_failure_count": int(
            float(metrics.get("component_normalized_mae") or 999) > 0.12
        ),
        "total_mae_threshold_failure_count": int(
            float(metrics.get("total_proxy_mae") or 999) > 8.0
        ),
        "rank_threshold_failure_count": int(
            float(metrics.get("spearman_rank_correlation") or 0) < 0.85
        ),
        "stage_accuracy_failure_count": int(
            float(metrics.get("stage_band_accuracy") or 0) < 0.90
        ),
        "critical_guard_accuracy_failure_count": int(
            float(metrics.get("critical_positive_counter_ordering") or 0) < 1.0
        ),
        "false_positive_guard_accuracy_failure_count": int(
            float(metrics.get("false_positive_guard_accuracy") or 0) < 1.0
        ),
        "dynamic_range_collapse_count": int(
            ((docs["blind"].get("metrics") or {}).get("dynamic_range_audit") or {}).get(
                "collapsed_to_zero_twenty"
            )
            is True
        ),
        "strong_anchor_equivalent_undercredit_count": int(
            not bool(docs["aggregator"].get("strong_component_points"))
        ),
    }
    return _custom_result(critical, metrics)


def _review_f(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    rows = context["canary_rows"]
    critical = {
        "missing_target_manifest_count": sum(not row["manifest_path"] for row in rows),
        "incomplete_production_research_count": sum(
            not row["production_research_complete"] for row in rows
        ),
        "seven_component_memo_incomplete_count": sum(
            row["component_memo_count"] != 7 for row in rows
        ),
        "current_evidence_missing_count": sum(
            row["document_count"] <= 0 or row["fact_count"] <= 0 for row in rows
        ),
        "final_component_decision_missing_count": sum(
            not row["leaf_presence"].get("final_component_decisions.jsonl")
            for row in rows
        ),
        "master_leaf_contract_critical_count": sum(
            row["canary_leaf_contract_critical_count"] for row in rows
        ),
    }
    blockers = [
        f"LIVE_CANARY_DOSSIER_INCOMPLETE:{row['target_id']}"
        for row in rows
        if not row["production_research_complete"]
    ]
    blockers.extend(
        f"CANARY_LEAF_CONTRACT_PENDING:{row['target_id']}"
        for row in rows
        if row["canary_leaf_contract_critical_count"] > 0
    )
    return _custom_result(critical, {"targets": list(rows)}, blockers)


def _review_g(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    rows = context["canary_rows"]
    missing = sum(
        not row["leaf_presence"].get("atomic_stage_decision.json")
        or not row["leaf_presence"].get("stagecourt_trace.json")
        for row in rows
    )
    critical = {
        "canary_final_stagecourt_missing_count": missing,
        "canary_score_valid_missing_count": sum(not row["score_valid"] for row in rows),
    }
    blockers = tuple(
        f"FINAL_STAGECOURT_PENDING:{row['target_id']}"
        for row in rows
        if not row["stage_final"]
    )
    return _custom_result(critical, {"targets": list(rows)}, blockers)


def _review_h(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    generalization = context["documents"]["generalization"]
    return _custom_result(
        {"generalization_critical_count": _base_document_critical(generalization)},
        {
            "status": generalization.get("status"),
            "registry_archetype_count": generalization.get("registry_archetype_count"),
            "target_branch_scan": generalization.get("production_conditioned_branch_scan"),
        },
    )


def _review_i(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    daily = context["documents"]["daily"]
    return _custom_result(
        {"daily_census_critical_count": _base_document_critical(daily)},
        {
            "status": daily.get("status"),
            "operational_model": daily.get("operational_model"),
        },
    )


def _review_j(context: Mapping[str, Any], root: Path) -> Mapping[str, Any]:
    rows = context["canary_rows"]
    full_test = context["documents"]["full_test"]
    expected_tree_hash = context["verification_tree_hash"]
    full_test_validation = validate_full_test_evidence(
        root,
        full_test,
        expected_tree_hash=expected_tree_hash,
    )
    full_test_valid = bool(full_test_validation["valid"])
    critical = {
        "runtime_manifest_missing_count": sum(not row["manifest_path"] for row in rows),
        "actual_query_missing_count": sum(row["query_count"] <= 0 for row in rows),
        "actual_fetch_missing_count": sum(row["document_count"] <= 0 for row in rows),
        "provider_success_missing_count": sum(
            row["provider_successful_call_count"] <= 0 for row in rows
        ),
        "checkpoint_missing_count": sum(
            not row["leaf_presence"].get("research_epochs.jsonl") for row in rows
        ),
        "output_hash_missing_count": sum(not row["output_tree_hash"] for row in rows),
        "output_hash_mismatch_count": sum(
            not row["output_tree_hash_matches"] for row in rows
        ),
        "master_leaf_contract_critical_count": sum(
            row["canary_leaf_contract_critical_count"] for row in rows
        ),
        "current_full_test_evidence_missing_count": int(not full_test_valid),
        "capability_regression_critical_count": _base_document_critical(
            context["documents"]["phase98"]
        ),
        "self_repair_critical_count": _base_document_critical(
            context["documents"]["phase99"]
        ),
        "same_replay_variance_count": int(
            ((context["documents"]["phase99"].get("clean_rerun") or {}).get(
                "same_evidence_replay_variance"
            ))
            != 0
        ),
    }
    blockers = [
        f"RUNTIME_NOT_COMPLETE:{row['target_id']}"
        for row in rows
        if not row["production_research_complete"]
    ]
    blockers.extend(
        str(blocker)
        for blocker in context["documents"]["phase99"].get(
            "canary_completion_blockers"
        )
        or ()
        if str(blocker).strip()
    )
    if not full_test_valid:
        blockers.append("CURRENT_FULL_TEST_EVIDENCE_MISSING_OR_STALE")
    return _custom_result(
        critical,
        {
            "targets": list(rows),
            "full_test_evidence": full_test,
            "expected_verification_tree_hash": expected_tree_hash,
            "full_test_evidence_valid": full_test_valid,
            "full_test_evidence_validation": full_test_validation,
            "capability_regression_status": context["documents"]["phase98"].get(
                "status"
            ),
            "self_repair_status": context["documents"]["phase99"].get("status"),
        },
        blockers,
    )


_REVIEWER_CHECKS: Mapping[
    str, Callable[[Mapping[str, Any], Path], Mapping[str, Any]]
] = {
    "A": _review_a,
    "B": _review_b,
    "C": _review_c,
    "D": _review_d,
    "E": _review_e,
    "F": _review_f,
    "G": _review_g,
    "H": _review_h,
    "I": _review_i,
    "J": _review_j,
}


def _custom_result(
    critical_counts: Mapping[str, int],
    metrics: Mapping[str, Any],
    blockers: Sequence[str] = (),
) -> Mapping[str, Any]:
    return {
        "critical_counts": dict(critical_counts),
        "metrics": dict(metrics),
        "blockers": list(blockers),
    }


def _threshold_failure(value: Any, threshold: Any) -> int:
    if (
        not isinstance(value, (int, float))
        or isinstance(value, bool)
        or not isinstance(threshold, (int, float))
        or isinstance(threshold, bool)
    ):
        return 1
    return int(float(value) < float(threshold))


def _component_calibration_artifact(context: Mapping[str, Any]) -> Mapping[str, Any]:
    docs = context["documents"]
    metrics = docs["blind"].get("metric_values") or {}
    dynamic = (docs["blind"].get("metrics") or {}).get("dynamic_range_audit") or {}
    critical_counts = {
        "historical_replay_critical_count": _base_document_critical(docs["blind"]),
        "aggregator_critical_count": _base_document_critical(docs["aggregator"]),
        "dynamic_range_collapse_count": int(dynamic.get("collapsed_to_zero_twenty") is True),
        "strong_anchor_equivalent_undercredit_count": int(
            not bool(docs["aggregator"].get("strong_component_points"))
        ),
    }
    critical_sum = sum(critical_counts.values())
    return {
        "schema_version": "e2r_v5_component_score_calibration_v1",
        "status": "COMPONENT_SCORE_CALIBRATION_PASS" if critical_sum == 0 else "COMPONENT_SCORE_CALIBRATION_FAIL",
        "historical_parity_metrics": dict(metrics),
        "thresholds": dict(docs["blind"].get("thresholds") or {}),
        "dynamic_range": dict(dynamic),
        "strong_anchor_equivalent_undercredit_count": critical_counts[
            "strong_anchor_equivalent_undercredit_count"
        ],
        "production_current_score_authority": False,
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
    }


def _stagecourt_audit_artifact(context: Mapping[str, Any]) -> Mapping[str, Any]:
    rows = context["canary_rows"]
    critical_counts = {
        "canary_score_vector_missing_count": sum(not row["score_valid"] for row in rows),
        "canary_final_stage_missing_count": sum(not row["stage_final"] for row in rows),
    }
    critical_sum = sum(critical_counts.values())
    return {
        "schema_version": "e2r_v5_stagecourt_acceptance_audit_v1",
        "status": "FINAL_STAGECOURT_PASS" if critical_sum == 0 else "FINAL_STAGECOURT_PENDING",
        "canonical_stage_enum": [
            "0",
            "1",
            "2",
            "3-Green",
            "3-Yellow",
            "3-Red",
            "4A",
            "4B",
            "4C",
            "5",
        ],
        "llm_stage_authority": False,
        "event_overlay_can_change_canonical_stage": False,
        "targets": list(rows),
        "critical_counts": critical_counts,
        "critical_count_sum": critical_sum,
    }


def _render_canary_dossier(row: Mapping[str, Any]) -> str:
    lines = [
        f"# {row['company_name']} E2R v5 Researcher Dossier",
        "",
        f"- target_id: `{row['target_id']}`",
        f"- status: `{row['status']}`",
        f"- production research complete: `{str(row['production_research_complete']).lower()}`",
        f"- documents: `{row['document_count']}`",
        f"- evidence facts: `{row['fact_count']}`",
        f"- counterfacts: `{row['counterfact_count']}`",
        f"- complete component memos: `{row['component_memo_count']}` / `7`",
        f"- score valid: `{str(row['score_valid']).lower()}`",
        f"- FINAL StageCourt: `{str(row['stage_final']).lower()}`",
        "",
        "현재 dossier는 live checkpoint 진실을 기록한 것이며, 미완료 상태에서는 점수나 Stage를 확정하지 않는다.",
        "직접적인 투자 행동 지시를 포함하지 않는다.",
        "",
        "## Leaf presence",
        "",
    ]
    lines.extend(
        f"- `{name}`: `{'present' if present else 'missing'}`"
        for name, present in row["leaf_presence"].items()
    )
    lines.append("")
    return "\n".join(lines)


def _render_final_readiness(
    *,
    gate: Mapping[str, Any],
    context: Mapping[str, Any],
    calibration: Mapping[str, Any],
    stagecourt: Mapping[str, Any],
) -> str:
    blind_metrics = calibration["historical_parity_metrics"]
    legacy_recall = (
        context["documents"]["legacy"].get("metric_values") or {}
    ).get("legacy_valid_material_fact_recall")
    gold = context["documents"]["gold"].get("post_run_comparison") or {}
    full_test = context["documents"]["full_test"]
    lines = [
        "# E2R v5 Final Readiness",
        "",
        f"- exact verdict: `{gate['exact_verdict']}`",
        f"- reviewer gate: `{gate['status']}`",
        f"- reviewer critical sum: `{gate['critical_count_sum']}`",
        f"- failed reviewers: `{', '.join(gate['failed_reviewers'])}`",
        "",
        "## Historical parity",
        "",
        f"- component normalized MAE: `{blind_metrics.get('component_normalized_mae')}` (max `0.12`)",
        f"- total proxy MAE: `{blind_metrics.get('total_proxy_mae')}` (max `8`)",
        f"- rank correlation: `{blind_metrics.get('spearman_rank_correlation')}` (min `0.85`)",
        f"- Stage band accuracy: `{blind_metrics.get('stage_band_accuracy')}` (min `0.90`)",
        f"- legacy valid retrieval recall: `{legacy_recall}` (min `0.95`)",
        "",
        "## Current research quality",
        "",
        f"- Phase 94 Gold comparison: `{gold.get('status')}`",
        f"- critical material fact recall: `{gold.get('critical_material_fact_recall')}`",
        f"- counter/supersession recall: `{gold.get('counter_supersession_recall')}`",
        f"- all material fact recall: `{gold.get('all_material_fact_recall')}`",
        f"- component research topic coverage: `{gold.get('component_research_topic_coverage')}`",
        "",
        "## Current decisions",
        "",
    ]
    for row in context["canary_rows"]:
        lines.extend(
            [
                f"- {row['company_name']} ({row['target_id']}): memos `{row['component_memo_count']}/7`, score valid `{str(row['score_valid']).lower()}`, FINAL StageCourt `{str(row['stage_final']).lower()}`",
            ]
        )
    lines.extend(
        [
            "",
            "## Runtime",
            "",
            f"- current full-test evidence: `{full_test.get('status') or 'MISSING'}`",
            f"- full-test count: `{full_test.get('test_count')}`",
            f"- positive/known-bad capability audit: `{context['documents']['phase98'].get('status')}`",
            f"- self-repair audit: `{context['documents']['phase99'].get('status')}`",
            f"- StageCourt acceptance: `{stagecourt['status']}`",
            f"- same-evidence replay variance: `{((context['documents']['phase99'].get('clean_rerun') or {}).get('same_evidence_replay_variance'))}`",
            "",
            "## Blockers",
            "",
        ]
    )
    lines.extend(f"- `{blocker}`" for blocker in gate["blockers"])
    lines.extend(
        [
            "",
            f"`{FINAL_READY_LABEL}`는 reviewer A~J가 전부 PASS이고 blocker가 0일 때만 선언한다.",
            "현재 문서는 투자 권고가 아니라 연구 시스템 readiness 감사다.",
            "",
        ]
    )
    return "\n".join(lines)


def _leaf_row(root: Path, relative: str) -> Mapping[str, Any]:
    path = root / relative
    if not path.is_file():
        return {"path": relative, "exists": False, "sha256": None}
    return {
        "path": relative,
        "exists": True,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def _read_json(path: Path | None) -> Mapping[str, Any]:
    if path is None:
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, Mapping) else {}


__all__ = [
    "DEFAULT_COMPONENT_CALIBRATION_PATH",
    "DEFAULT_FINAL_READINESS_PATH",
    "DEFAULT_FULL_TEST_EVIDENCE_PATH",
    "DEFAULT_REVIEWER_GATE_PATH",
    "DEFAULT_STAGECOURT_AUDIT_PATH",
    "FINAL_NOT_READY_LABEL",
    "FINAL_READY_LABEL",
    "REVIEWER_GATE_FAIL",
    "REVIEWER_GATE_PASS",
    "REVIEWER_SPECS",
    "SCHEMA_VERSION",
    "IndependentReviewerSpec",
    "compile_phase100_acceptance_bundle",
    "validate_full_test_evidence",
    "verification_tree_hash",
    "write_phase100_acceptance_artifacts",
]
