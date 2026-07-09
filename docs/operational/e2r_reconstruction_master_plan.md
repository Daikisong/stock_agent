# E2R Evidence Intelligence Reconstruction Master Plan

기준일: 2026-07-10

이 계획은 docs/core/goal.md의 Phase 0~16 전체를 구현하기 위한 내부 실행 계약이다. 각 Phase는 기존 scoring weight와 Stage threshold를 변경하지 않는다. Phase가 실패하면 report label을 바꾸지 않고 가장 큰 leaf failure cluster의 코드나 schema를 고친다.

## 공통 원칙

- src/e2r/research_brain이 유일한 intelligence source of truth다.
- historical outcome은 evaluator-only다.
- current score evidence는 현재 source-backed accepted claim뿐이다.
- LLM은 hypothesis, question, query intent, assertion을 만들 수 있지만 score/Stage를 만들 수 없다.
- query literal은 LLM이 만들고 deterministic code는 범위, 날짜, 중복, budget만 검증한다.
- leaf identity는 artifact_id, case_id, recipe_id, question_id, task_id, document_id, anchor_id, claim_id, primitive_id, contribution_id, stagecourt_trace_id로 이어진다.
- current operation은 아키타입 quota를 강제하지 않는다.
- historical replay와 current operation은 output root와 schema status를 분리한다.

## Phase 0 — 결과 재분류와 기준선

- 문제: 오래된 PASS 보고서, 최신 NOT_READY leaf, 고정 test expectation이 서로 다른 상태를 가리킨다.
- Root cause: docs/operational/census_mode_v4_artifact_manifest.json의 mutable output pointer, census/research_to_runtime_parity.py의 summary readback, 과거 report 중심 판정.
- 제거할 legacy path: 없음. Phase 0에서는 삭제하지 않고 분류만 한다.
- 새 schema/API: runtime_call_graph_before_v1, duplicate_brain_stack_inventory_v1, conversion_funnel_baseline_v1, legacy_artifact_classification_v1.
- Migration: 최신 leaf를 authoritative baseline으로 고정하고 과거 문서는 REPORT_OR_PLAN_ONLY로 낮춘다.
- 구현 파일: docs/operational/e2r_reconstruction_* 및 Phase 0 baseline test.
- 테스트: JSON parse, verdict, zero full-thesis, forbidden count promotion, required call graph edge.
- Runtime acceptance: current promoted full-thesis 0과 NOT_READY를 그대로 재현한다.
- Rollback point: 문서/JSON artifact만 되돌리면 된다.
- Commit message: Phase 0: E2R 중복 두뇌 경로와 기준선 감사

## Phase 1 — Research Brain 단일 Source of Truth

- 문제: research_brain, research_reverse, source_routing, production cutover에 중복 schema와 orchestration이 있다.
- Root cause: census/research_to_runtime_parity.py가 reverse/routing report writer를 직접 import하고, V4가 V2 card/router를 사용한다.
- 제거할 legacy path: canonical production entrypoint에서 research_reverse와 source_routing import를 제거한다. V2/V3 CLI의 canonical READY 라벨을 금지한다.
- 새 schema/API: research_brain/canonical.py facade, corpus/compiler/recipes/retrieval/planning/replay/runtime package, LegacyCompatibilityResult.
- Migration: legacy public function은 canonical facade로 forward하고 DeprecationWarning을 낸다. legacy schema를 새로 쓰지 않는다.
- 구현 파일: research_brain 하위 package, research_reverse adapter, source_routing adapter, CLI lockout.
- 테스트: test_research_brain_single_source_of_truth.py, test_legacy_research_reverse_not_production_reachable.py, test_legacy_source_route_not_production_reachable.py, test_legacy_cli_cannot_claim_ready.py.
- Runtime acceptance: canonical CLI import graph의 legacy reverse count 0, primitive-name route guesser count 0, schema source count 1.
- Rollback point: adapter 뒤의 기존 implementation을 한 Phase 동안 보존한다.
- Commit message: Phase 1: Research Brain 단일 실행 경로 통합

## Phase 2 — Research Corpus Semantic Compiler

- 문제: 한 파일의 여러 case와 structured row linkage가 파일-level record로 무너진다.
- Root cause: research_reverse/research_case_extractor.py의 text truncation, first-symbol extraction, substring classification.
- 제거할 legacy path: heuristic extractor를 canonical compile에서 호출하지 않는다.
- 새 schema/API: HistoricalResearchArtifact, HistoricalResearchCase, HistoricalOutcome, HistoricalRuleCandidate, LinkageError, QuarantineRecord; parse_artifact, link_rows, compile_cases.
- Migration: YAML, fenced JSON/JSONL/CSV, Markdown table을 structured-row-first로 읽는다. narrative-only는 provider가 있을 때 LLM_DERIVED_UNVERIFIED로 quarantine한다.
- 구현 파일: corpus/research_corpus_parser.py, corpus/research_case_linker.py, compiler/semantic_case_compiler.py, schemas.py, compile CLI.
- 테스트: golden C06/C08/C15/C17/C24/C28, multi-case file, line span, company/date preservation, no 24k truncation, handoff exclusion, duplicate conflict.
- Runtime acceptance: valid structured row preservation 100%, golden counts exact, first-symbol collapse 0.
- Rollback point: old corpus artifacts remain read-only; new output uses output/research_intelligence versioned root.
- Commit message: Phase 2: 연구 JSONL case 단위 의미 컴파일러 구현

## Phase 3 — Case-Level Source Verification

- 문제: file-level URL presence가 case-level A2처럼 취급된다.
- Root cause: research_reverse/source_quality_inferencer.py와 source quality reports가 URL string과 case anchor를 분리하지 못한다.
- 제거할 legacy path: URL_PRESENT만으로 replay-ready를 부여하는 경로.
- 새 schema/API: HistoricalSourceState, HistoricalSourceVerification, SourceRepairTask, verify_case_source.
- Migration: 기존 URL-backed row를 UNVERIFIED부터 재검증하고 source proxy/pending은 repair queue로 보낸다.
- 구현 파일: compiler/source_verification_compiler.py, corpus/source_locator.py, source repair output writer.
- 테스트: wrong subject, invalid date, fetch failure, no anchor, case mismatch, source proxy cannot become ready.
- Runtime acceptance: case association 없는 A2 0, URL string-only A2 0, golden case는 ready 또는 exact blocker.
- Rollback point: verification result는 append-only sidecar이며 원본 research MD를 변경하지 않는다.
- Commit message: Phase 3: 연구 case별 source anchor 검증 계층 구현

## Phase 4 — Executable Evidence Recipe OS

- 문제: generic “primitive를 확인하라”와 primitive substring route가 질문을 대체한다.
- Root cause: source_routing/research_source_route_recovery.py, v2_memory_cards.py의 uniform source route.
- 제거할 legacy path: primitive-name production routing, generic query-only recipe.
- 새 schema/API: EvidenceRecipe, AcceptedClaimPredicate, EntityValueRequirement, LifecycleRequirement, RejectionCondition, SourceStrategy.
- Migration: Evidence Contract required primitive와 verified historical source success/failure를 결합한다. unsupported primitive는 이유를 명시한다.
- 구현 파일: recipes/evidence_recipe_compiler.py, evidence_recipe_catalog.py, recipe schemas and audit.
- 테스트: registry required primitive coverage, six mandatory archetype detail, positive/counter/wrong-subject/source-failure example, no substring routing.
- Runtime acceptance: 모든 required primitive가 recipe 또는 explicit unsupported, generic recipe 0.
- Rollback point: recipe catalog는 versioned immutable JSONL로 남기고 prior catalog hash로 복귀 가능하다.
- Commit message: Phase 4: 실행 가능한 Evidence Recipe OS 구축

## Phase 5 — Semantic Memory Graph와 Retrieval

- 문제: first-N, token overlap, popularity가 retrieval을 지배하고 positive/guard/source failure 균형이 없다.
- Root cause: memory_retriever.py와 V2 router/card의 count/token 중심 선택.
- 제거할 legacy path: first-N-only canonical retrieval, historical outcome prompt field.
- 새 schema/API: ResearchMemoryGraph, MemoryNode, MemoryEdge, BalancedRetrievalRequest/Result.
- Migration: case, recipe, primitive, source를 stable ID로 graph에 적재하고 role별 quota가 아니라 role coverage를 만족시킨다.
- 구현 파일: retrieval/semantic_memory_index.py, balanced_case_retriever.py, graph serializer.
- 테스트: blind benchmark top-3/top-1, recipe hit, positive+guard pair, outcome leakage, popularity bias.
- Runtime acceptance: top-3 >=95%, recipe hit >=95%, positive+guard >=90%, future leakage 0.
- Rollback point: deterministic lexical fallback은 test/debug 전용으로 남기되 production planner에는 연결하지 않는다.
- Commit message: Phase 5: 균형형 semantic memory graph와 retrieval 구현

## Phase 6 — Two-Pass LLM Research Brain

- 문제: event text와 archetype label token matching이 hypothesis처럼 사용된다.
- Root cause: v2_archetype_router.py, archetype_classifier.py, V4 planner prompt에 source-primary/context leakage 가능성.
- 제거할 legacy path: source_primary copy, expected archetype fixture text, score/stage/outcome prompt fields.
- 새 schema/API: BlindHypothesisInput/Output, MemoryCritiqueInput/Output, PlannerPending, TwoPassPlan.
- Migration: Pass A는 current evidence만, Pass B는 balanced memory/recipe만 추가한다. provider가 없거나 실패하면 pending이다.
- 구현 파일: planning/two_pass_brain_planner.py, prompt contracts, provider adapter, sanitizer.
- 테스트: prompt field denylist, score/stage mutation rejection, blind routing benchmark, ambiguity abstention, hash preservation.
- Runtime acceptance: blind top-3 >=95%, top-1 >=85%, critical guard misroute 0.
- Rollback point: existing Codex provider transport는 유지하고 prompt/schema만 canonical wrapper로 교체한다.
- Commit message: Phase 6: blind two-pass LLM Research Brain 구현

## Phase 7 — Question-Centric SourceTask

- 문제: SourceTask가 primitive label과 generic query intent만 갖고 성공 의미가 불명확하다.
- Root cause: research_brain/schemas.py와 v4_schemas.py의 task schema 부족.
- 제거할 legacy path: empty question, empty predicate, generic verify-primitive task.
- 새 schema/API: QuestionSourceTask, QuestionAcceptanceContract, QueryIntent, SourceBudget, StopCondition.
- Migration: old SourceTask는 adapter가 recipe/question을 요구하며 누락 시 INVALID_LEGACY_TASK로 만든다.
- 구현 파일: planning/source_task.py, source_task_bridge.py adapter, validator.
- 테스트: field completeness, official-first, bounded budgets, LLM query validation, FCF/contract/backlog Naver-first rejection.
- Runtime acceptance: empty material fields 0, unbounded task 0, generic task 0.
- Rollback point: legacy task serialization reader를 유지하되 production execution은 금지한다.
- Commit message: Phase 7: 질문과 성공조건을 가진 SourceTask 도입

## Phase 8 — Source Acquisition와 Document Selection

- 문제: source mode가 혼재하고 result date가 없을 때 as_of로 보정될 수 있으며 recipe relevance가 약하다.
- Root cause: v4_source_acquisition_runner.py의 mode/date fallback, generic document ranking.
- 제거할 legacy path: undated document current promotion, snippet-as-document, snapshot-as-live.
- 새 schema/API: AcquisitionMode, AcquiredDocument, DocumentRejection, RecipeDocumentSelector.
- Migration: existing connector를 mode-aware adapter로 감싸고 published_at unknown은 UNKNOWN_DATE로 차단한다.
- 구현 파일: runtime/source_acquisition.py, runtime/document_selector.py, connector adapters.
- 테스트: no-date, stale broker PDF, full fetch requirement, original source, source class/document mismatch.
- Runtime acceptance: content hash 없는 fetched 0, Naver result는 full fetch 또는 rejection 100%.
- Rollback point: existing SourceAcquisitionRunnerV4 remains adapter implementation until current CLI cutover.
- Commit message: Phase 8: mode별 source acquisition과 recipe 문서 선택 통합

## Phase 9 — Contract-Blind Claim Compiler

- 문제: rerouted claim과 original task satisfaction이 분리되지 않고 guard가 여러 layer에 중복된다.
- Root cause: v4_evidence_extraction_bridge.py와 census promotion code의 서로 다른 ledger filtering.
- 제거할 legacy path: parser mention direct score, unstructured fallback score, rerouted closure.
- 새 schema/API: ClaimCompilationInput/Result, TaskSatisfactionStatus enum, ClaimLedgerEvent.
- Migration: existing Evidence OS entities를 재사용하고 task satisfaction을 별도 leaf로 append한다.
- 구현 파일: runtime/claim_compiler.py, runtime/task_satisfaction.py, Evidence OS adapter.
- 테스트: missing anchor/date/subject/target, wrong subject, stale risk, reroute, baseline reuse, counter claim.
- Runtime acceptance: original-gap false closure 0, recipe mapping 없는 score claim 0.
- Rollback point: raw/adjudicated legacy leaf를 보존하고 canonical ledger를 side-by-side 비교한다.
- Commit message: Phase 9: contract-blind claim compiler와 task satisfaction 분리

## Phase 10 — Adaptive Investigation Controller

- 문제: retry가 동일 query 재실행이거나 generic feedback으로 끝난다.
- Root cause: V4 feedback loop와 until_pass runtime retry가 failure taxonomy를 공유하지 않는다.
- 제거할 legacy path: reason 없는 retry, identical query retry, runtime retry를 self-repair로 부르는 label.
- 새 schema/API: InvestigationFailureReason, NextInvestigationAction, InvestigationRound, SystemicFailureCluster.
- Migration: task result를 failure reason으로 정규화하고 LLM에게 실패 사실만 되돌린다. query 생성은 LLM이 한다.
- 구현 파일: runtime/adaptive_investigation_controller.py, failure cluster writer.
- 테스트: each failure transition, duplicate query block, reroute feedback, budget pending, provider pending.
- Runtime acceptance: identical retry 0, unresolved material gap score_valid false 100%.
- Rollback point: round limit 1로 controller를 안전하게 비활성화할 수 있다.
- Commit message: Phase 10: 실패 이유 기반 adaptive evidence closure 구현

## Phase 11 — Historical Replay와 Current Operation 분리

- 문제: 전 아키타입 parity와 현재 시장 종목 materialization이 섞인다.
- Root cause: census_runner_v4 dedicated replay/smoke/current promotion의 단일 runner, all-archetype seed forcing.
- 제거할 legacy path: current archetype quota, placeholder target materialization, replay row current promotion.
- 새 schema/API: HistoricalReplayRun, CurrentOperationRun, RunEvidenceMode, immutable RunManifest.
- Migration: frozen replay corpus와 current candidate pool에 별도 CLI/output root를 부여한다.
- 구현 파일: replay/historical_replay_runner.py, runtime/current_operation_runner.py, 두 CLI.
- 테스트: output separation, outcome hidden, no current quota, proxy score 0, no replay contamination.
- Runtime acceptance: historical registry 100%와 current selective terminal state를 각각 충족한다.
- Rollback point: legacy V4 runner는 deprecated audit-only로 유지한다.
- Commit message: Phase 11: historical replay와 current operation 완전 분리

## Phase 12 — Deterministic Score/Stage 재검증

- 문제: event partial, full score, pending, promotion wrapper가 여러 경로에서 다르게 판정된다.
- Root cause: scoring.py, staging.py, stage_court.py, v4_scoring_stage.py, atomic_stage_decision.py의 중복 orchestration.
- 제거할 legacy path: claimless score, material-gap full score, event score full promotion, caller별 threshold default.
- 새 schema/API: CanonicalAtomicStageDecision, ScoreType, ScoreValidity, DecisionFingerprint.
- Migration: 기존 scorer/profile을 그대로 사용하고 StageCourt threshold를 active profile에서 명시적으로 전달한다.
- 구현 파일: census/atomic_stage_decision.py 확장 또는 canonical decision module, adapters.
- 테스트: score/stage/trace identity, hard break direct-current-open, delta explanation, fingerprint.
- Runtime acceptance: 모든 full score가 accepted claim/contribution/trace로 재계산 가능하다.
- Rollback point: score algorithm은 변경하지 않으므로 orchestration adapter만 되돌린다.
- Commit message: Phase 12: 단일 AtomicStageDecision으로 score와 Stage 통합

## Phase 13 — Census / Daily Operation

- 문제: 모든 종목 deep 조사와 lookback cutoff 위험, legacy runner 이름 혼선.
- Root cause: census runner 세대 중복과 current operation facade 부재.
- 제거할 legacy path: unbounded production config, recent cutoff stage deletion, all-symbol LLM/web.
- 새 schema/API: CensusDepthLevel L0~L5, CensusStageStatus, CurrentWatchlistItem.
- Migration: existing baseline collector, SourceTimeline, LastEffectiveThesis, DepthPolicy를 canonical current runner에 연결한다.
- 구현 파일: runtime/current_operation_runner.py, census canonical adapter, run_e2r_census_mode CLI migration.
- 테스트: full universe one status, selective deep, stage cutoff guard, watchlist safety language.
- Runtime acceptance: 모든 eligible symbol baseline, selected deep terminal state, production bounded validation.
- Rollback point: current runner can run official-only L0/L2 when Brain is unavailable.
- Commit message: Phase 13: bounded selective-deep Census와 daily operation 통합

## Phase 14 — Conversion Funnel Observability

- 문제: task/claim 총량은 많지만 direct original-gap closure를 계산할 수 없다.
- Root cause: candidate-question-recipe-task identity가 leaf 전체에 일관되지 않다.
- 제거할 legacy path: summary counter만으로 progress 또는 PASS 판정.
- 새 schema/API: ConversionFunnelEvent, FunnelCohort, FunnelMetrics, leaf-only auditor.
- Migration: 각 canonical component가 같은 correlation IDs를 기록한다.
- 구현 파일: runtime/observability.py, CLI audit_e2r_evidence_intelligence.
- 테스트: independent recomputation, summary mismatch, reroute count, cost/runtime.
- Runtime acceptance: candidate별 end-to-end trace와 direct closure rate가 leaf에서 재계산된다.
- Rollback point: observability는 append-only라 runtime behavior를 바꾸지 않고 비활성화 가능하다.
- Commit message: Phase 14: leaf 기반 conversion funnel observability 구축

## Phase 15 — Known-Bad Suite

- 문제: 과거 개별 bug test는 많지만 새 canonical chain 기준 통합 공격 bundle이 없다.
- Root cause: version별 test가 자기 artifact만 검사한다.
- 제거할 legacy path: 답안 archetype이 raw fixture text에 들어간 fixture.
- 새 schema/API: canonical known-bad case bundle과 expected rejection/terminal status.
- Migration: 기존 known-bad를 새 question/claim/decision API로 재작성하되 기존 test는 삭제하지 않는다.
- 구현 파일: tests/fixtures/e2r_reconstruction_known_bad, canonical known-bad tests.
- 테스트: goal.md Phase 15의 모든 named bad case.
- Runtime acceptance: critical fail 0, mutation을 넣으면 각 guard가 실제로 실패한다.
- Rollback point: test-only fixture 추가이므로 production rollback 불필요.
- Commit message: Phase 15: E2R reconstruction known-bad 공격 회귀 완성

## Phase 16 — Commands, Runtime Proof, Independent Review

- 문제: 필수 CLI가 없고 READY를 증명할 독립 reviewer leaf audit가 없다.
- Root cause: versioned legacy CLI와 report generator counter 공유.
- 제거할 legacy path: old CLI canonical PASS label, report-only READY.
- 새 schema/API: CompileRunManifest, ReplayRunManifest, CurrentRunManifest, ReviewerVerdict.
- Migration: 네 개 공식 CLI를 canonical facade에 연결한다.
- 구현 파일: compile_e2r_research_intelligence.py, run_e2r_historical_replay.py, run_e2r_current_operation.py, audit_e2r_evidence_intelligence.py, census CLI adapter.
- 테스트: command smoke, dirty/config/corpus/memory/recipe/prompt/source hashes, reviewer independence.
- Runtime acceptance: compile strict, frozen replay critical pass, current production bounded terminal states, Census selective deep, full unittest.
- Rollback point: each run output is immutable and includes previous compatible hashes.
- Commit message: Phase 16: 공식 CLI와 독립 감사로 E2R runtime 완성

## 주요 integration test 시점

1. Phase 2 후: corpus golden + 전체 parser/calibration tests
2. Phase 5 후: compile command + retrieval benchmark
3. Phase 9 후: source task to claim closure integration
4. Phase 12 후: full deterministic score/stage suite
5. Phase 13 후: frozen current Census run
6. Phase 16: 전체 5,305+ tests와 모든 공식 runtime command

## 최종 completion evidence

완료는 다음을 모두 증명할 때만 가능하다.

- UNIFIED_RESEARCH_BRAIN_ARCHITECTURE_PASS
- RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS
- CASE_LEVEL_SOURCE_VERIFICATION_PASS
- EVIDENCE_RECIPE_OS_PASS
- SEMANTIC_RESEARCH_BRAIN_PASS
- ADAPTIVE_EVIDENCE_CLOSURE_PASS
- HISTORICAL_REPLAY_PARITY_PASS
- CURRENT_OPERATIONAL_BRAIN_PASS
- Reviewer A~E critical count 0
- 최종 working tree clean
- 최종 label MEANINGFUL_E2R_RUNTIME_READY

외부 provider나 network만 실패하면 EXTERNAL_SOURCE_BLOCKER_NOT_READY로 분리하되, 내부 Phase 구현과 frozen replay 검증은 계속한다.
