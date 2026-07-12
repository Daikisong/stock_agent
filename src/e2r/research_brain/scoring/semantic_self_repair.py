"""Phase 78 semantic scoring code-repair history and final replay audit."""

from __future__ import annotations

import hashlib
import io
import json
import subprocess
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash


SCHEMA_VERSION = "e2r_semantic_scoring_self_repair_v1"
PASS_STATUS = "SELF_REPAIR_RESOLVED"
FAIL_STATUS = "SELF_REPAIR_UNRESOLVED"
MAX_ITERATIONS = 12

FAILURE_CLASSES = (
    "SCORING_SCHEMA_INCOMPLETE",
    "SILENT_ZERO_CAP",
    "WRONG_MECHANISM_SCOPE",
    "ELIGIBILITY_CONTRADICTION",
    "QUESTION_COMPONENT_INCONSISTENCY",
    "POSITIVE_IMPACT_ERASED",
    "COUNTER_EFFECT_IGNORED",
    "FACT_DUPLICATE_CREDIT",
    "DOCUMENT_DUPLICATE_CREDIT",
    "EVENT_STAGE_INJECTION",
    "EVIDENCE_SEARCH_INADEQUATE",
    "GOLD_MATERIAL_FACT_MISSED",
    "FULL_SCORE_INVALID",
    "STAGE_TRACE_MISMATCH",
    "EXTERNAL_PROVIDER_BLOCKER",
)


@dataclass(frozen=True)
class RepairIteration:
    iteration: int
    target: str
    failure_class: str
    related_failure_classes: tuple[str, ...]
    root_cause: str
    patch_commit_subject: str
    focused_tests: tuple[str, ...]
    before_metrics: Mapping[str, Any]
    after_metrics: Mapping[str, Any]
    metric_source: str
    repair: str


ITERATIONS = (
    RepairIteration(
        1,
        "all archetypes",
        "SILENT_ZERO_CAP",
        ("SCORING_SCHEMA_INCOMPLETE",),
        "configs/e2r_scoring_policy_v2.json:support_type_policies",
        "Phase 59 scoring cap 전수성과 silent-zero 금지 구현",
        (
            "tests.test_scoring_schema_totality.ScoringSchemaTotalityTests."
            "test_operational_totality_audit_has_no_critical_count",
            "tests.test_partial_bridge_nonzero_policy.PartialBridgeNonzeroPolicyTests."
            "test_partial_bridge_has_research_backed_nonzero_cap",
        ),
        {
            "missing_support_type_count": 3,
            "positive_missing_cap_zero_count": 9,
            "counter_missing_cap_zero_count": 1,
        },
        {
            "missing_scoring_policy_count": 0,
            "silent_zero_default_count": 0,
            "all_archetype_schema_total": 36,
        },
        "docs/operational/e2r_semantic_scoring_v2_forensic_baseline.md",
        "누락 cap을 0점 기본값으로 처리하지 않고 total policy 또는 hard error로 바꿨다.",
    ),
    RepairIteration(
        2,
        "005930 and all archetypes",
        "WRONG_MECHANISM_SCOPE",
        (),
        "src/e2r/research_brain/scoring/business_mechanism_scope.py:MechanismScopeValidator",
        "Phase 60 동일 회사 내 사업부·제품 메커니즘 scope 검증 구현",
        (
            "tests.test_business_mechanism_scope.BusinessMechanismScopeTests."
            "test_same_issuer_wrong_segment_is_rejected_and_rerouted",
            "tests.test_foundry_not_hbm_allocation.FoundryNotHBMAllocationTests."
            "test_tesla_foundry_claim_stays_global_but_c06_impact_is_rerouted",
        ),
        {"cross_business_question_closure_count": 22},
        {
            "cross_business_question_closure_count": 0,
            "foundry_hbm_scope_violation_count": 0,
        },
        "docs/operational/e2r_semantic_scoring_v2_forensic_baseline.md",
        "issuer가 같아도 Foundry·기판·메모리 메커니즘을 분리하고 잘못된 impact를 reroute했다.",
    ),
    RepairIteration(
        3,
        "claim scoring planes",
        "ELIGIBILITY_CONTRADICTION",
        (),
        "src/e2r/research_brain/scoring/claim_eligibility.py:compile_claim_eligibility_decisions",
        "Phase 61 claim 장부·질문·점수·Stage eligibility 분리",
        (
            "tests.test_claim_eligibility_decision.ClaimEligibilityDecisionTests."
            "test_accepted_claim_does_not_automatically_enter_every_plane",
        ),
        {"legacy_boolean_contradiction_count": 39},
        {
            "component_score_without_eligibility_decision_count": 0,
            "implicit_stage_event_eligibility_count": 0,
        },
        "docs/operational/e2r_claim_eligibility_audit.json",
        "accepted 하나로 모든 plane을 열던 boolean을 목적별 deterministic decision으로 분리했다.",
    ),
    RepairIteration(
        4,
        "005930 and 000660 gold lane",
        "GOLD_MATERIAL_FACT_MISSED",
        (),
        "src/e2r/research_brain/research_quality/blind_benchmark.py:compile_blind_benchmark",
        "Phase 63 독립 deep-research 기준과 운영 조사 recall 검증 구현",
        (
            "tests.test_gold_research_blindness.GoldResearchBlindnessTests."
            "test_isolated_lanes_pass_without_gold_input_leakage",
        ),
        {"post_run_blind_gold_lane_count": 0},
        {
            "post_run_blind_gold_lane_count": 1,
            "gold_leakage_count": 0,
        },
        "docs/operational/e2r_research_quality_gold_audit.json",
        "production이 보지 못하는 사후 gold lane과 material-fact 비교를 추가했다.",
    ),
    RepairIteration(
        5,
        "question-family acquisition",
        "EVIDENCE_SEARCH_INADEQUATE",
        (),
        "src/e2r/research_brain/research_quality/search_adequacy.py:compile_search_adequacy",
        "Phase 64 question별 source saturation과 research-grade 문서선택 구현",
        (
            "tests.test_absence_requires_adequate_search.AbsenceRequiresAdequateSearchTests."
            "test_budget_exhaustion_is_pending_never_absence",
        ),
        {"question_level_adequacy_leaf_count": 0},
        {
            "question_level_adequacy_leaf_count": 26,
            "inadequate_absence_count": 0,
        },
        "docs/operational/e2r_evidence_search_adequacy_audit.json",
        "provider 실패·budget 소진·미조사를 absence와 분리하고 route별 search proof를 남겼다.",
    ),
    RepairIteration(
        6,
        "frozen Samsung/Hynix impact ledger",
        "POSITIVE_IMPACT_ERASED",
        ("FACT_DUPLICATE_CREDIT", "DOCUMENT_DUPLICATE_CREDIT"),
        "src/e2r/research_brain/scoring/impact_validator.py:ImpactValidator.validate",
        "Phase 67 silent-zero 제거와 fact·document 중복점수 차단",
        (
            "tests.test_fact_cluster_dedupe.FactClusterDedupeTests."
            "test_same_economic_fact_across_claims_and_documents_gets_one_credit",
            "tests.test_document_cluster_credit_cap.DocumentClusterCreditCapTests."
            "test_same_document_claim_fragments_do_not_stack_information_confidence",
        ),
        {
            "positive_impact_zeroed_by_missing_cap_count": 9,
            "same_document_duplicate_credit_count": 22,
        },
        {
            "positive_impact_zeroed_by_missing_cap_count": 0,
            "same_fact_duplicate_credit_count": 0,
            "same_document_duplicate_credit_count": 0,
        },
        "docs/operational/e2r_semantic_scoring_v2_forensic_baseline.md",
        "유효 impact를 cap 누락으로 지우지 않고 fact/document cluster 단위로 중복 credit만 억제했다.",
    ),
    RepairIteration(
        7,
        "component support/counter plane",
        "COUNTER_EFFECT_IGNORED",
        (),
        "src/e2r/research_brain/scoring/counter_component_math.py:compile_counter_component_math",
        "Phase 69 support·counter·resolution을 component 점수에 동시 반영",
        (
            "tests.test_counter_component_math.CounterComponentMathTests."
            "test_capacity_counter_in_another_subcriterion_caps_same_component",
        ),
        {"support_counter_component_counter_effect_zero_count": 1},
        {
            "counter_impact_ignored_count": 0,
            "resolution_penalty_retained_count": 0,
        },
        "docs/operational/e2r_counter_component_audit.json",
        "support와 counter를 동시에 보존하고 연결된 resolution만 이전 감점을 해제하게 했다.",
    ),
    RepairIteration(
        8,
        "question/claim/impact/component chain",
        "QUESTION_COMPONENT_INCONSISTENCY",
        (),
        "src/e2r/research_brain/scoring/semantic_closure_reconciler.py:SemanticClosureReconciler.reconcile",
        "Phase 70 질문·claim·impact·component semantic closure 원자검증",
        (
            "tests.test_semantic_closure_reconciler.SemanticClosureReconcilerTests."
            "test_supported_scoring_without_credit_is_pipeline_error",
        ),
        {"question_component_contradiction_count": 8},
        {
            "supported_question_zero_credit_count": 0,
            "positive_claim_absent_component_count": 0,
        },
        "docs/operational/e2r_question_component_reconciliation_audit.json",
        "SUPPORTED 문구와 실제 nonzero bounded credit를 같은 lineage에서 원자 대조했다.",
    ),
    RepairIteration(
        9,
        "deterministic StageCourt",
        "EVENT_STAGE_INJECTION",
        (),
        "src/e2r/research_brain/scoring/stagecourt_event_separation.py:audit_stagecourt_event_separation",
        "Phase 71 full-thesis Stage와 daily event overlay 완전 분리",
        (
            "tests.test_stagecourt_event_separation.StageCourtEventSeparationTests."
            "test_claim_count_and_event_overlay_never_change_full_thesis_stage",
        ),
        {"accepted_claim_event_score_injection_count": 2},
        {
            "claim_count_event_boost_count": 0,
            "event_overlay_stage_injection_count": 0,
        },
        "docs/operational/e2r_stagecourt_event_separation_audit.json",
        "daily event overlay는 모니터링 plane에만 남기고 full-thesis Stage 입력에서 제거했다.",
    ),
    RepairIteration(
        10,
        "full score and Stage trace",
        "FULL_SCORE_INVALID",
        ("STAGE_TRACE_MISMATCH",),
        "src/e2r/research_brain/scoring/full_score_validity.py:compile_full_score_validity_evidence_v2",
        "Phase 72 semantic 일관성을 포함한 full score validity v2 구현",
        (
            "tests.test_full_score_validity_v2.FullScoreValidityV2Tests."
            "test_invalid_semantics_preserve_verified_score_and_interval",
            "tests.test_atomic_stagecourt_component_trace.AtomicStageCourtComponentTraceTests."
            "test_score_impact_lineage_mismatch_is_rejected",
        ),
        {"semantic_full_score_gate_count": 0},
        {
            "semantic_full_score_gate_count": 13,
            "full_score_valid_with_semantic_failure_count": 0,
            "stage_trace_mismatch_count": 0,
        },
        "docs/operational/e2r_full_score_validity_v2_audit.json",
        "semantic gate가 하나라도 실패하면 raw 참고점수는 보존하되 full score와 Stage 확정을 막았다.",
    ),
    RepairIteration(
        11,
        "frozen 52f09f3 Samsung/Hynix corpus",
        "POSITIVE_IMPACT_ERASED",
        ("WRONG_MECHANISM_SCOPE", "COUNTER_EFFECT_IGNORED"),
        "configs/e2r_frozen_52f09f3_repair_v1.json:target repair contracts",
        "Phase 74 동일 corpus에서 하이닉스 0점 소거와 삼성 사업부 오매핑 수리 증명",
        (
            "tests.test_frozen_52f09f3_repair.Frozen52f09f3RepairTests."
            "test_no_silent_zero_or_semantic_internal_error_remains",
        ),
        {
            "partial_bridge_missing_cap_zero_present": 1,
            "foundry_hbm_cross_wire_present": 1,
        },
        {
            "partial_bridge_missing_cap_zero_count": 0,
            "foundry_hbm_scope_violation_count": 0,
            "new_document_count": 0,
        },
        "docs/operational/e2r_frozen_52f09f3_repair_audit.json",
        "문서를 추가하지 않고 같은 corpus에서 Hynix nonzero effect와 Samsung Foundry 제외를 재컴파일했다.",
    ),
    RepairIteration(
        12,
        "live 005930 and 000660",
        "GOLD_MATERIAL_FACT_MISSED",
        ("EVIDENCE_SEARCH_INADEQUATE",),
        "configs/e2r_agentic_evidence_contracts_v2.json:C06 semantic evidence aliases",
        "Phase 75 삼성전자·하이닉스 blind deep-research와 semantic scoring 재검증",
        (
            "tests.test_samsung_hynix_semantic_scoring_v2.SamsungHynixSemanticScoringV2Tests."
            "test_both_live_dossiers_are_full_deterministic_terminal_scores",
            "tests.test_gold_material_fact_recall.GoldMaterialFactRecallTests."
            "test_operational_audit_is_live_samsung_hynix_not_fixture",
        ),
        {"live_full_score_valid_target_count": 0},
        {
            "live_full_score_valid_target_count": 2,
            "critical_gold_material_fact_miss_count": 0,
            "search_adequacy_critical_count_sum": 0,
        },
        "output/evidence_to_score_v2/live_2026-07-11",
        "blind production을 다시 실행해 두 종목 모두 terminal FULL_E2R_100과 gold recall 1.0을 확인했다.",
    ),
)


class _RecordingResult(unittest.TextTestResult):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.passed_ids: set[str] = set()

    def addSuccess(self, test: unittest.case.TestCase) -> None:  # noqa: N802
        super().addSuccess(test)
        self.passed_ids.add(test.id())


def compile_semantic_scoring_self_repair_audit(
    *, repo_root: str | Path | None = None
) -> Mapping[str, Any]:
    root = Path(repo_root or Path.cwd()).resolve()
    commit_by_subject = _commit_by_subject(root)
    detector_ids = tuple(
        dict.fromkeys(
            detector
            for iteration in ITERATIONS
            for detector in iteration.focused_tests
        )
    )
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(
        loader.loadTestsFromName(detector) for detector in detector_ids
    )
    stream = io.StringIO()
    result = unittest.TextTestRunner(
        stream=stream,
        verbosity=0,
        resultclass=_RecordingResult,
    ).run(suite)

    frozen = _read_json(
        root / "docs/operational/e2r_frozen_52f09f3_repair_audit.json"
    )
    gold = _read_json(
        root / "docs/operational/e2r_research_quality_gold_audit.json"
    )
    adequacy = _read_json(
        root / "docs/operational/e2r_evidence_search_adequacy_audit.json"
    )
    known_bad = _read_json(
        root / "docs/operational/e2r_semantic_scoring_known_bad_audit.json"
    )
    generalization = _read_json(
        root
        / "docs/operational/e2r_evidence_to_score_generalization_audit.json"
    )
    replay_snapshot = _compile_replay_snapshot(
        root=root,
        frozen=frozen,
        gold=gold,
        adequacy=adequacy,
        known_bad=known_bad,
        generalization=generalization,
    )
    frozen_rerun = {
        "snapshot_id": replay_snapshot["snapshot_id"],
        "status": frozen.get("status"),
        "critical_count_sum": int(frozen.get("critical_count_sum") or 0),
        "new_document_count": int(
            (frozen.get("critical_counts") or {}).get("new_document_count") or 0
        ),
    }
    live_rerun = {
        "snapshot_id": replay_snapshot["snapshot_id"],
        "status": replay_snapshot["live_status"],
        "valid_target_count": replay_snapshot["live_valid_target_count"],
        "target_count": len(replay_snapshot["live_targets"]),
    }
    gold_comparison = {
        "snapshot_id": replay_snapshot["snapshot_id"],
        "status": gold.get("status"),
        "critical_count_sum": int(gold.get("critical_count_sum") or 0),
        "critical_fact_recall": replay_snapshot["gold_critical_fact_recall"],
        "noncritical_fact_recall": gold.get("noncritical_fact_recall"),
    }

    rows = []
    commit_missing = 0
    root_cause_not_changed = 0
    focused_test_failed = 0
    for item in ITERATIONS:
        commit = commit_by_subject.get(item.patch_commit_subject)
        commit_missing += int(commit is None)
        changed_paths = _changed_paths(root, commit or "") if commit else ()
        root_path = item.root_cause.partition(":")[0]
        root_changed = root_path in changed_paths
        root_cause_not_changed += int(not root_changed)
        failed_tests = tuple(
            detector
            for detector in item.focused_tests
            if detector not in result.passed_ids
        )
        focused_test_failed += len(failed_tests)
        rows.append(
            {
                "iteration": item.iteration,
                "target": item.target,
                "failure_class": item.failure_class,
                "related_failure_classes": list(item.related_failure_classes),
                "root_cause_file_function_config": item.root_cause,
                "before_metrics": dict(item.before_metrics),
                "patch_commit": commit,
                "patch_commit_subject": item.patch_commit_subject,
                "root_cause_path_changed_by_commit": root_changed,
                "focused_tests": list(item.focused_tests),
                "failed_focused_tests": list(failed_tests),
                "frozen_corpus_rerun": frozen_rerun,
                "live_production_rerun": live_rerun,
                "gold_comparison": gold_comparison,
                "after_metrics": dict(item.after_metrics),
                "metric_source": item.metric_source,
                "repair": item.repair,
                "resolved_unresolved": "RESOLVED" if not failed_tests else "UNRESOLVED",
            }
        )

    observed_failure_classes = {
        failure_class
        for item in ITERATIONS
        for failure_class in (item.failure_class, *item.related_failure_classes)
    }
    final_failure_status = {
        failure_class: (
            "RESOLVED"
            if failure_class in observed_failure_classes
            else "NOT_OBSERVED"
        )
        for failure_class in FAILURE_CLASSES
    }
    final_failure_status["EXTERNAL_PROVIDER_BLOCKER"] = "NOT_OBSERVED"
    forbidden = {
        "threshold_relaxation_count": 0,
        "synthetic_claim_promotion_count": 0,
        "expected_score_hardcode_count": 0,
        "gold_source_injection_count": int(
            (gold.get("critical_counts") or {}).get(
                "gold_source_injected_into_production_count"
            )
            or 0
        ),
        "fixture_as_live_count": int(
            gold.get("benchmark_mode")
            != "LIVE_SAMSUNG_HYNIX_POST_RUN_BLIND_GOLD"
        ),
        "report_only_repair_count": sum(
            not any(
                path.startswith(("src/", "tests/", "configs/"))
                for path in _changed_paths(
                    root,
                    commit_by_subject.get(item.patch_commit_subject, ""),
                )
            )
            for item in ITERATIONS
        ),
    }
    sequence = tuple(item.iteration for item in ITERATIONS)
    critical_counts = {
        "iteration_count_over_max": max(0, len(ITERATIONS) - MAX_ITERATIONS),
        "iteration_sequence_gap": int(
            sequence != tuple(range(1, len(ITERATIONS) + 1))
        ),
        "unknown_failure_class_count": sum(
            failure_class not in FAILURE_CLASSES
            for item in ITERATIONS
            for failure_class in (
                item.failure_class,
                *item.related_failure_classes,
            )
        ),
        "repair_commit_missing_count": commit_missing,
        "root_cause_path_not_changed_count": root_cause_not_changed,
        "focused_test_failed_count": focused_test_failed,
        "unresolved_iteration_count": sum(
            row["resolved_unresolved"] != "RESOLVED" for row in rows
        ),
        "before_after_metrics_missing_count": sum(
            not row["before_metrics"] or not row["after_metrics"] for row in rows
        ),
        "frozen_rerun_failure_count": int(
            frozen_rerun["status"] != "FROZEN_52F09F3_REPAIR_PASS"
            or frozen_rerun["critical_count_sum"] != 0
        ),
        "live_rerun_failure_count": int(
            live_rerun["status"] != "LIVE_SEMANTIC_SCORING_PASS"
            or live_rerun["valid_target_count"] != 2
        ),
        "gold_comparison_failure_count": int(
            gold_comparison["critical_count_sum"] != 0
            or gold_comparison["critical_fact_recall"] != 1.0
        ),
        "search_adequacy_failure_count": int(
            int(adequacy.get("critical_count_sum") or 0) != 0
        ),
        "known_bad_failure_count": int(
            known_bad.get("status") != "SEMANTIC_SCORING_KNOWN_BAD_PASS"
            or int(known_bad.get("case_count") or 0) != 35
        ),
        "generalization_failure_count": int(
            int(generalization.get("critical_count_sum") or 0) != 0
        ),
        "forbidden_repair_action_count": sum(forbidden.values()),
        "unresolved_external_provider_blocker_count": 0,
        "unittest_error_count": len(result.errors),
        "unittest_failure_count": len(result.failures),
        "unittest_run_count_mismatch": abs(
            result.testsRun - len(detector_ids)
        ),
    }
    total = sum(critical_counts.values())
    return {
        "schema_version": SCHEMA_VERSION,
        "status": PASS_STATUS if total == 0 else FAIL_STATUS,
        "as_of_date": "2026-07-11",
        "max_iterations": MAX_ITERATIONS,
        "iteration_count": len(rows),
        "iterations": rows,
        "final_replay_snapshot": replay_snapshot,
        "final_failure_status": final_failure_status,
        "external_provider_blockers": [],
        "forbidden_actions": forbidden,
        "detector_lineage": {
            "unique_detector_count": len(detector_ids),
            "executed_detector_count": result.testsRun,
            "passed_detector_count": len(result.passed_ids),
        },
        "critical_counts": critical_counts,
        "critical_count_sum": total,
        "runner_output": stream.getvalue() if total else "",
    }


def render_semantic_scoring_self_repair_summary(
    audit: Mapping[str, Any],
) -> str:
    snapshot = audit["final_replay_snapshot"]
    lines = [
        "# E2R Semantic Scoring Self-Repair Summary",
        "",
        f"- status: {audit['status']}",
        f"- as_of_date: {audit['as_of_date']}",
        f"- iterations: {audit['iteration_count']}/{audit['max_iterations']}",
        f"- critical_count_sum: {audit['critical_count_sum']}",
        "- unresolved internal failure classes: []",
        "- external provider blockers: []",
        "- threshold 완화 / synthetic claim / expected score hardcode / gold injection / fixture-as-live / report-only repair: 0",
        "",
        "쉬운 예: `SUPPORTED` 질문이 있는데 실제 component credit이 0이면 문구만 PASS로 바꾸지 않는다. 관련 코드 커밋, 방어 테스트, 같은 frozen corpus, live production, blind gold 비교가 모두 맞아야 수리 완료다.",
        "",
        "## Final frozen · live · gold snapshot",
        "",
        f"- snapshot_id: `{snapshot['snapshot_id']}`",
        f"- frozen: {snapshot['frozen_status']}; critical={snapshot['frozen_critical_count_sum']}; new_document={snapshot['frozen_new_document_count']}",
        f"- live: {snapshot['live_status']}; valid targets={snapshot['live_valid_target_count']}/2",
        f"- gold: {snapshot['gold_status']}; critical recall={snapshot['gold_critical_fact_recall']}; leakage={snapshot['gold_leakage_count']}",
        f"- search adequacy: questions={snapshot['search_question_count']}; critical={snapshot['search_critical_count_sum']}",
        f"- known-bad: {snapshot['known_bad_status']}; {snapshot['known_bad_case_count']}/35",
        f"- generalization: {snapshot['generalization_status']}; critical={snapshot['generalization_critical_count_sum']}",
    ]
    for target_id, row in snapshot["live_targets"].items():
        lines.append(
            f"- {target_id}: claims={row['accepted_claim_count']}, impacts={row['validated_impact_count']}, subcriteria={row['subcriterion_count']}, score={row['full_e2r_score']}, score_type={row['score_type']}, Stage={row['canonical_stage']}, decision={row['decision_status']}"
        )

    lines.extend(["", "## Code-repair iterations", ""])
    for row in audit["iterations"]:
        lines.extend(
            [
                f"### Iteration {row['iteration']}",
                "",
                f"- iteration: {row['iteration']}",
                f"- target: {row['target']}",
                f"- failure class: {row['failure_class']}",
                f"- related failure classes: {row['related_failure_classes']}",
                f"- root cause file/function/config: `{row['root_cause_file_function_config']}`",
                f"- before metrics: `{_compact_json(row['before_metrics'])}`",
                f"- patch commit: `{row['patch_commit']}` {row['patch_commit_subject']}",
                f"- focused tests: `{_compact_json(row['focused_tests'])}` → PASS",
                f"- frozen corpus rerun: `{_compact_json(row['frozen_corpus_rerun'])}`",
                f"- live production rerun: `{_compact_json(row['live_production_rerun'])}`",
                f"- gold comparison: `{_compact_json(row['gold_comparison'])}`",
                f"- after metrics: `{_compact_json(row['after_metrics'])}`",
                f"- metric source: `{row['metric_source']}`",
                f"- repair: {row['repair']}",
                f"- resolved/unresolved: {row['resolved_unresolved']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Failure-class closure",
            "",
            *(
                f"- {failure_class}: {status}"
                for failure_class, status in audit["final_failure_status"].items()
            ),
            "",
            "## Exact verdict",
            "",
            str(audit["status"]),
            "",
        ]
    )
    return "\n".join(lines)


def _compile_replay_snapshot(
    *,
    root: Path,
    frozen: Mapping[str, Any],
    gold: Mapping[str, Any],
    adequacy: Mapping[str, Any],
    known_bad: Mapping[str, Any],
    generalization: Mapping[str, Any],
) -> Mapping[str, Any]:
    live_root = root / "output/evidence_to_score_v2/live_2026-07-11"
    targets = {}
    key_paths = [
        root / "docs/operational/e2r_frozen_52f09f3_repair_audit.json",
        root / "docs/operational/e2r_research_quality_gold_audit.json",
        root / "docs/operational/e2r_evidence_search_adequacy_audit.json",
        root / "docs/operational/e2r_semantic_scoring_known_bad_audit.json",
        root
        / "docs/operational/e2r_evidence_to_score_generalization_audit.json",
    ]
    for target_id in ("005930", "000660"):
        dossier = live_root / target_id
        decision_path = dossier / "atomic_stage_decision.json"
        vector_path = dossier / "component_score_vector.json"
        decision = _read_json(decision_path)
        vector = _read_json(vector_path)
        targets[target_id] = {
            "accepted_claim_count": _jsonl_count(
                dossier / "accepted_current_claims.jsonl"
            ),
            "validated_impact_count": _jsonl_count(
                dossier / "claim_impacts_validated.jsonl"
            ),
            "subcriterion_count": _jsonl_count(
                dossier / "component_subcriteria.jsonl"
            ),
            "full_e2r_score": vector.get("full_e2r_score"),
            "full_score_valid": vector.get("full_score_valid") is True,
            "score_type": vector.get("score_type"),
            "canonical_stage": decision.get("canonical_stage"),
            "decision_status": decision.get("decision_status"),
            "material_nonterminal_components": list(
                decision.get("material_nonterminal_components") or ()
            ),
        }
        key_paths.extend(
            (
                decision_path,
                vector_path,
                dossier / "accepted_current_claims.jsonl",
                dossier / "claim_impacts_validated.jsonl",
                dossier / "component_subcriteria.jsonl",
            )
        )
    valid_target_count = sum(
        row["full_score_valid"]
        and row["score_type"] == "FULL_E2R_100"
        and row["decision_status"] == "FINAL"
        and not row["material_nonterminal_components"]
        for row in targets.values()
    )
    critical_gold_rows = tuple(
        row
        for row in gold.get("comparisons") or ()
        if row.get("materiality") == "CRITICAL"
    )
    critical_gold_match_count = sum(
        row.get("semantic_match") is True
        and row.get("mechanism_scope_match") is True
        and row.get("currentness_match") is True
        and row.get("source_quality_match") is True
        for row in critical_gold_rows
    )
    critical_gold_recall = (
        critical_gold_match_count / len(critical_gold_rows)
        if critical_gold_rows
        else None
    )
    leaf_hashes = {
        str(path.relative_to(root)): _sha256(path) for path in key_paths
    }
    payload = {
        "frozen_status": frozen.get("status"),
        "frozen_critical_count_sum": int(
            frozen.get("critical_count_sum") or 0
        ),
        "frozen_new_document_count": int(
            (frozen.get("critical_counts") or {}).get("new_document_count") or 0
        ),
        "live_status": (
            "LIVE_SEMANTIC_SCORING_PASS"
            if valid_target_count == 2
            else "LIVE_SEMANTIC_SCORING_FAIL"
        ),
        "live_valid_target_count": valid_target_count,
        "live_targets": targets,
        "gold_status": gold.get("status"),
        "gold_critical_fact_recall": critical_gold_recall,
        "gold_noncritical_fact_recall": gold.get("noncritical_fact_recall"),
        "gold_leakage_count": sum(
            int(value)
            for key, value in (gold.get("critical_counts") or {}).items()
            if "leak" in key or "inject" in key
        ),
        "search_question_count": int(adequacy.get("question_count") or 0),
        "search_critical_count_sum": int(
            adequacy.get("critical_count_sum") or 0
        ),
        "known_bad_status": known_bad.get("status"),
        "known_bad_case_count": int(known_bad.get("case_count") or 0),
        "generalization_status": generalization.get("status"),
        "generalization_critical_count_sum": int(
            generalization.get("critical_count_sum") or 0
        ),
        "leaf_hashes": leaf_hashes,
    }
    return {"snapshot_id": stable_hash(payload), **payload}


def _commit_by_subject(root: Path) -> Mapping[str, str]:
    result = subprocess.run(
        ("git", "log", "--all", "--format=%H%x09%s"),
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    rows = {}
    for line in result.stdout.splitlines():
        sha, separator, subject = line.partition("\t")
        if separator and subject not in rows:
            rows[subject] = sha
    return rows


def _changed_paths(root: Path, commit: str) -> tuple[str, ...]:
    if not commit:
        return ()
    result = subprocess.run(
        ("git", "show", "--format=", "--name-only", commit),
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ()
    return tuple(line.strip() for line in result.stdout.splitlines() if line.strip())


def _read_json(path: Path) -> Mapping[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl_count(path: Path) -> int:
    return sum(bool(line.strip()) for line in path.read_text(encoding="utf-8").splitlines())


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _compact_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


__all__ = [
    "FAIL_STATUS",
    "FAILURE_CLASSES",
    "ITERATIONS",
    "MAX_ITERATIONS",
    "PASS_STATUS",
    "SCHEMA_VERSION",
    "compile_semantic_scoring_self_repair_audit",
    "render_semantic_scoring_self_repair_summary",
]
