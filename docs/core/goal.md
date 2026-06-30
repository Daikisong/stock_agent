너는 Daikisong/stock_agent 레포의 E2R Census Mode v3 / Anti-Fake Full Universe Stage Map을 구현하는 coding agent다.

이번 Goal의 목적은 “리포트 숫자를 예쁘게 만드는 것”이 아니다.

이번 Goal의 목적은 다음이다.

전체 KRX eligible universe에 대해,
각 종목의 현재 E2R 상태를 실제 source / existing ledger / last effective thesis / Evidence OS claim / deterministic StageCourt trace에 근거해 붙이는 것이다.

즉:

KRX 전체 universe
→ 전 종목 CensusAssessmentEvent
→ 전 종목 SourceTimeline
→ 전 종목 LastEffectiveThesisState
→ 전 종목 BaselineScanResult
→ 전 종목 DepthDecision
→ 필요한 종목 SourceTask / Evidence OS / StageCourt
→ 전 종목 CensusStageStatus
→ leaf artifacts로부터 독립 audit 재계산
→ FULL_UNIVERSE_STAGE_MAP_PASS

까지 닫혀야 한다.

이번에는 절대 “실패하면 NOT_READY로 보고 끝”이 아니다.

반드시:

실패 감지
→ 실패 유형 분류
→ root cause 파일/함수/설정 추적
→ 코드/설정 패치
→ 같은 명령 재실행
→ leaf artifact 기준 지표 재계산
→ 성공 기준 통과

까지 반복한다.

외부 API 키 부재, 유료 provider 미계약, 거래소/공식 API 장애처럼 코드로 해결 불가능한 경우만 EXTERNAL_BLOCKER_NOT_READY로 남길 수 있다.
그러나 코드 wiring 누락, 빈 baseline, accepted_claim 미전달, source task fake execution, report label 과장, summary 숫자 조작은 반드시 고쳐야 한다.

================================================================================
0. 이번 Goal에서 반드시 막아야 할 이전 실패/속임수 패턴
================================================================================

다음 패턴이 하나라도 남아 있으면 Goal 실패다.

A. Empty baseline
- _baseline_inputs_for_mode()가 빈 BaselineScanInputs()를 반환
- BaselineScanner에 실제 source/event/ledger input이 들어가지 않음

B. Summary-only pass
- docs/operational/*.md 또는 *_summary.json 숫자만 보고 pass
- leaf artifact를 재계산하지 않음

C. Claim-to-stage disconnect
- accepted_claim_count는 report에 있는데 CensusStageStatus row에는 accepted_claim_ids가 없음
- score_contribution_count는 report에 있는데 해당 score row에 score_contribution_ids가 없음
- build_stage_status(... accepted_claims=(), score_contributions=()) 같은 호출이 production/census path에 남아 있음

D. SourceTask fake execution
- source_task_executions가 PARSED/FETCHED처럼 보이지만 accepted_claim_ids=[]
- existing report replay를 실제 SourceTask execution으로 카운트
- SourceTaskExecution이 Evidence OS ledger claim으로 이어지지 않음

E. Provider failure masking
- provider_failed를 no_result 또는 no_current_event로 처리
- provider failure 종목을 Red/Reject/low score로 확정

F. Snapshot/report synthesis masquerading as live
- 기존 report/candidate_event_report를 읽어 Census 결과를 만든 뒤 real source run으로 표시
- snapshot:// 또는 fixture 경로를 live provider fetch로 계산

G. Recent-window cutoff misuse
- “최근 공시 없음”이라는 이유로 Stage0/Unknown/NoCurrentCatalyst 처리
- 한 달 전/일 년 전 event라도 아직 active일 수 있는데 무시
- latest effective thesis를 만들지 않음

H. Source-proxy contamination
- source_proxy_only / evidence_url_pending / price_path_only 연구 row가 current score evidence가 됨
- shadow_weight_only research row가 production score에 반영됨

I. Report label overclaim
- Unknown 100%, ProviderPending 100%, Stage0 100%, accepted_claim=0, source_task=0인데 FULL_UNIVERSE_STAGE_MAP_PASS 선언
- source task / claim / score trace 없이 READY_FOR_DAILY_TRIGGER_INTEGRATION 선언

J. Tests that only test reports
- tests가 leaf artifact가 아니라 acceptance report만 읽음
- report generator와 validator가 같은 함수/같은 summary object를 공유

================================================================================
1. 현재 Census v1/v2 재분류
================================================================================

먼저 기존 Census v1/v2 결과를 정확히 재라벨링하라.

생성/수정:
docs/operational/census_mode_v1_v2_reclassification.md

반드시 명시:
- Census v1은 CENSUS_SKELETON_PASS일 뿐 FULL_UNIVERSE_STAGE_MAP_PASS가 아니다.
- Census v1의 Unknown 3391 / ProviderPending 3391 / accepted_claim 0 / score_contribution 0은 안전한 빈 지도일 뿐 실제 Stage 지도 아님.
- Census v2가 22분 내 완료됐고 accepted claim/score 숫자를 만들었더라도, census_runner가 StageStatus에 accepted_claims=(), score_contributions=()를 넘기는 경로가 남아 있으면 진짜 Stage map이 아니다.
- 기존 report/candidate_event_report replay를 source task execution처럼 세면 안 된다.
- FULL_UNIVERSE_STAGE_MAP_PASS는 leaf artifact 재계산으로만 인정된다.

Acceptance:
- 기존 과장 라벨을 낮춘다.
- 기존 산출물은 삭제하지 않고 deprecated/limited scope로 보존한다.
- “왜 이전 산출물이 부족했는지” root cause 파일/함수까지 적는다.
- build_stage_status 호출부, BaselineInput 생성부, SourceTaskExecution 생성부의 현재 상태를 audit에 남긴다.

================================================================================
2. Anti-Fake Invariant: Leaf Artifact가 Source of Truth
================================================================================

이번 Goal의 가장 중요한 규칙:

최종 report 숫자는 source of truth가 아니다.
source of truth는 leaf artifact다.

Leaf artifacts:
- universe.jsonl
- census_assessment_events.jsonl
- source_timelines.jsonl
- last_effective_thesis_states.jsonl
- baseline_scan_results.jsonl
- census_events.jsonl
- depth_decisions.jsonl
- research_brain_plans.jsonl
- source_tasks.jsonl
- source_task_executions.jsonl
- evidence_documents.jsonl
- evidence_anchors.jsonl
- raw_assertions.jsonl
- adjudicated_claims.jsonl
- accepted_claims.jsonl
- primitive_states.jsonl
- score_contributions.jsonl
- stagecourt_traces.jsonl
- census_stage_status.jsonl
- census_stage_map.jsonl

반드시 구현:
src/e2r/census/leaf_artifact_auditor.py
src/e2r/cli/audit_e2r_census_leaf_artifacts.py

LeafArtifactAuditor는 report를 읽지 않고 leaf files만 읽어 다음을 재계산한다.

- eligible symbol count
- stage status count
- missing symbol count
- duplicate symbol count
- Unknown count
- ProviderPending count
- NoCurrentCatalyst count
- accepted claim count
- score contribution count
- source task count
- source task execution count
- source task with accepted claim count
- StageCourt trace count
- stage distribution
- census status distribution
- depth distribution
- provider failure count
- source gap count
- claimless nonzero score count
- source_proxy_to_score count
- score_without_claim count
- stage row with accepted claims count
- stage row with score contribution count
- stage row with StageCourt trace count

Final report must be generated from LeafArtifactAuditor output, not from in-memory counters.

Acceptance:
- Report numbers must exactly match independent leaf audit numbers.
- Any mismatch fails.
- One-line huge reports fail.
- Missing leaf artifact fails.
- Empty accepted_claims but nonzero score fails.
- accepted_claim_count in report cannot exceed accepted_claims.jsonl line count.
- score_contribution_count in report cannot exceed score_contributions.jsonl line count.
- Stage2/Yellow/Green/Reject rows must have StageCourt trace or explicit non-scored status reason.

Tests:
tests/test_census_v3_leaf_artifact_auditor.py
tests/test_census_v3_report_not_source_of_truth.py
tests/test_census_v3_report_leaf_count_mismatch_fails.py

================================================================================
3. Claim-to-Stage Trace Contract
================================================================================

모든 CensusStageStatus row는 trace contract를 가져야 한다.

CensusStageStatusTrace:

{
  "symbol": "...",
  "company_name": "...",
  "as_of_date": "...",

  "census_assessment_event_id": "...",
  "source_timeline_id": "...",
  "last_effective_thesis_id": "...",
  "baseline_scan_result_id": "...",
  "depth_decision_id": "...",

  "research_brain_plan_ids": [],
  "source_task_ids": [],
  "source_task_execution_ids": [],
  "evidence_document_ids": [],
  "evidence_anchor_ids": [],
  "raw_assertion_ids": [],
  "adjudicated_claim_ids": [],
  "accepted_claim_ids": [],
  "primitive_state_ids": [],
  "score_contribution_ids": [],
  "stagecourt_trace_id": null,

  "trace_status": "NO_EVIDENCE_NEEDED|LIGHT_ONLY|DEEP_TRACE_COMPLETE|PENDING_PROVIDER|PENDING_SOURCE|INVALID_TRACE",
  "trace_missing_reasons": []
}

Rules:
- verified_score != null → accepted_claim_ids not empty
- verified_score != null → score_contribution_ids not empty
- verified_score != null → stagecourt_trace_id not null
- base_stage in Stage2-Actionable/Yellow/Green/Reject/Red → stagecourt_trace_id required unless status is explicitly non-scored guard status
- ProviderPending → provider failure record required
- NoCurrentCatalyst → SourceTimeline and LastEffectiveThesisState required, with source families attempted or existing ledger checked
- MarketAnomaly only → no verified_score

Ban:
- build_stage_status(... accepted_claims=(), score_contributions=()) in any path that can produce non-light stage or non-null score
- stage row counted as claim-backed if accepted_claim_ids empty
- source task counted as claim-producing if accepted_claim_ids empty

Acceptance:
- 100% of eligible symbols have CensusStageStatusTrace.
- 100% of non-null verified_score rows have accepted_claim_ids, score_contribution_ids, and StageCourt trace.
- 100% of Stage2+ rows have either StageCourt trace or explicit pending/provider status.
- claim_to_stage_unlinked_count = 0.
- accepted_claim_unused_in_any_stage_or_backlog_count must be reported.
- score_contribution_unused_in_any_stage_count = 0.
- build_stage_status_empty_claims_for_scored_path_count = 0.

Tests:
tests/test_census_v3_claim_to_stage_trace.py
tests/test_census_v3_no_empty_claims_in_scored_stage.py
tests/test_census_v3_stage2_requires_trace.py

================================================================================
4. Real Baseline Source Wiring
================================================================================

Census runner must no longer generate empty baseline input.

Implement:
src/e2r/census/baseline_input_collector.py
src/e2r/census/source_family_collectors/
    opendart_census_collector.py
    kind_krx_census_collector.py
    companyguide_report_census_collector.py
    issuer_ir_news_census_collector.py
    price_volume_census_collector.py
    existing_ledger_census_collector.py
    research_memory_census_collector.py

CensusBaselineInputCollector must populate:

BaselineScanInputs:
- provider_failed_symbols
- provider_failure_by_symbol
- price_anomaly_symbols
- price_anomaly_by_symbol
- recent_official_events
- historical_official_events
- latest_regular_report_by_symbol
- latest_material_disclosure_by_symbol
- last_material_official_event_by_symbol
- risk_events_by_symbol
- companyguide_revision_events_by_symbol
- report_radar_events_by_symbol
- issuer_ir_events_by_symbol
- trusted_news_events_by_symbol
- market_anomaly_events_by_symbol
- existing_claim_counts
- existing_claim_refs_by_symbol
- existing_stage
- previous_watchlist_state
- last_effective_thesis_by_symbol
- research_memory_hints_by_symbol
- source_gap_by_symbol
- no_data_reason_by_symbol

Mandatory source families:
1. OpenDART / DART
2. KIND/KRX risk and listing state
3. Price/volume/relative strength
4. Existing evidence ledger / previous StageStatus
5. CompanyGuide/report radar OR explicit provider gap
6. IssuerIR/trusted news OR explicit provider gap
7. ResearchMemory hints as planning-only

Acceptance:
- empty_baseline_inputs_count = 0.
- baseline_source_family_wired_count >= 5.
- For every eligible symbol, at least one of:
  - latest official source checked
  - price/volume checked
  - existing ledger checked
  - provider failure recorded
- provider_pending cannot be global default.
- recent_official_events may be 0 on quiet days, but latest_regular_report / latest_material_disclosure / existing_ledger / price/risk checks must still be attempted.
- source family attempts are reported per symbol and per provider.
- if provider not available, exact provider gap is recorded; do not convert to NoCurrentCatalyst.

Tests:
tests/test_census_v3_baseline_input_collector_real.py
tests/test_census_v3_no_empty_baseline_inputs.py
tests/test_census_v3_provider_pending_not_global_default.py
tests/test_census_v3_source_family_attempts_per_symbol.py

================================================================================
5. SourceTimeline and LastEffectiveThesis Must Be Real
================================================================================

Census is not a “recent disclosure” scan.
It is an as_of_date current state map.

Implement/strengthen:
src/e2r/census/source_timeline.py
src/e2r/census/last_effective_thesis.py
src/e2r/census/lifecycle_policy.py

Every eligible symbol must have:

SourceTimeline:
{
  "symbol": "...",
  "as_of_date": "...",
  "timeline_id": "...",
  "source_family_attempts": [],
  "official_events": [],
  "regular_reports": [],
  "risk_events": [],
  "financial_events": [],
  "revision_events": [],
  "ir_events": [],
  "trusted_news_events": [],
  "market_events": [],
  "existing_claim_events": [],
  "research_memory_hints": [],
  "provider_failures": [],
  "source_gaps": [],
  "latest_regular_report": null,
  "latest_material_disclosure": null,
  "latest_risk_status": null,
  "latest_price_context": null
}

LastEffectiveThesisState:
{
  "symbol": "...",
  "as_of_date": "...",
  "state_id": "...",
  "status": "ACTIVE_THESIS|NO_KNOWN_THESIS|HISTORICAL_ONLY|PROVIDER_PENDING|SOURCE_PENDING|CONTRADICTED|SUPERSEDED|EXPIRED|NEEDS_REFRESH",
  "primary_archetype": null,
  "last_effective_event_date": null,
  "last_effective_event_type": null,
  "last_effective_source_family": null,
  "support_claim_ids": [],
  "support_event_ids": [],
  "needs_lifecycle_refresh": false,
  "needs_source_task": false,
  "reason": "..."
}

Lifecycle policy:
- active supply contract remains active until contract_end unless cancelled/superseded.
- facility investment remains active until completed/cancelled/converted.
- regular report supersedes prior regular financial state.
- risk event remains active until resolved/superseded/cleared.
- revision/report thesis remains active until newer revision/report supersedes.
- IR/news thesis requires full source/date/issuer scope and later official contradiction check.
- market anomaly expires quickly and cannot score.
- research memory is planning-only.

Ban:
- fixed 30/90/365-day cutoff as Stage cutoff.
- “recent 공시 없음” → NoCurrentCatalyst without checking latest effective state.
- old risk current penalty without current OPEN check.
- old positive thesis reused without lifecycle refresh.

Acceptance:
- source_timeline_count == eligible_symbol_count.
- last_effective_thesis_count == eligible_symbol_count.
- last_effective_thesis_missing_count = 0.
- recent_lookback_used_as_stage_cutoff_count = 0.
- active_old_contract_fixture stays active.
- old_resolved_risk fixture does not score.
- latest_regular_report supersedes older regular report.
- NoCurrentCatalyst only after source timeline exists and no active thesis found.
- ProviderPending only if provider failure/source gap exists.

Tests:
tests/test_census_v3_source_timeline_complete.py
tests/test_census_v3_last_effective_thesis_complete.py
tests/test_census_v3_no_recent_cutoff_stage_drop.py
tests/test_census_v3_active_old_contract_current.py
tests/test_census_v3_resolved_old_risk_zero.py

================================================================================
6. Event Taxonomy: 공시만 보지 마라
================================================================================

CensusEvent categories:

- CensusAssessmentEvent
- OfficialEvent
- FinancialEvent
- RevisionEvent
- ReportEvent
- IssuerIREvent
- TrustedNewsEvent
- MarketAnomalyEvent
- RiskEvent
- ExistingClaimEvent
- ResearchMemoryHintEvent

Every event:
{
  "event_id": "...",
  "symbol": "...",
  "event_category": "...",
  "event_type": "...",
  "source_family": "...",
  "source_id": "...",
  "event_date": "...",
  "detected_at": "...",
  "as_of_date": "...",
  "title": "...",
  "summary": "...",
  "has_full_source": true_or_false,
  "has_anchor": true_or_false,
  "score_evidence_allowed": true_or_false,
  "investigation_trigger_allowed": true_or_false,
  "requires_verification": true_or_false,
  "lifecycle_policy": "...",
  "raw_payload_ref": "..."
}

Rules:
- CensusAssessmentEvent: score_evidence_allowed=false.
- MarketAnomalyEvent: score_evidence_allowed=false.
- ResearchMemoryHintEvent: score_evidence_allowed=false.
- TrustedNewsEvent: score_evidence_allowed=false until full source/date/issuer scope verified by Evidence OS.
- ReportEvent can trigger investigation; can score only after Evidence OS accepted claim.
- ExistingClaimEvent can score only after lifecycle refresh.
- OfficialEvent can score only after Evidence OS accepted claim.
- News/IR/report-only events must not be ignored. They become InfoEvent/SourceTask if source quality allows.
- Snippet-only events cannot score.

Acceptance:
- event_taxonomy_count_by_category reported.
- at least official + market + ledger categories present OR exact source/provider gap.
- report/news/IR ingestion attempted OR explicit provider gap.
- market_anomaly_to_score_count = 0.
- news_snippet_to_score_count = 0.
- research_memory_hint_to_score_count = 0.
- source_proxy_memory_to_score_count = 0.

Tests:
tests/test_census_v3_event_taxonomy.py
tests/test_census_v3_news_ir_report_not_ignored.py
tests/test_census_v3_market_anomaly_not_score.py
tests/test_census_v3_memory_hint_never_score.py

================================================================================
7. Selective Deep Must Actually Produce Claims
================================================================================

Census has two levels:
- all symbols get baseline and stage status
- selected symbols get deep evidence path

For L3/L4/L5 depth symbols:
Flow must be:

ResearchBrainPlan
→ SourceTask
→ SourceTaskExecution
→ EvidenceDocument
→ EvidenceAnchor
→ RawAssertion
→ AdjudicatedClaim
→ AcceptedClaim
→ PrimitiveState
→ ScoreContribution
→ StageCourtTrace
→ CensusStageStatus update

Implement:
src/e2r/census/selective_deep_runner.py

Ban:
- source task count generated from replay-only report.
- accepted claim count generated from existing summary.
- source_task_execution status PARSED counted as accepted if accepted_claim_ids empty.
- accepted_claims=() in stage builder for deep symbols.
- score_contribution without accepted claim.

Minimum acceptance:
- research_brain_plan_count >= 30 OR EXTERNAL_BLOCKER_NOT_READY.
- source_task_count >= 50 OR EXTERNAL_BLOCKER_NOT_READY.
- source_task_executed_count >= 30 OR EXTERNAL_BLOCKER_NOT_READY.
- accepted_claim_count >= 10 OR EXTERNAL_BLOCKER_NOT_READY.
- score_contribution_count >= 5 OR EXTERNAL_BLOCKER_NOT_READY.
- deterministic_stage_output_count >= 5 OR EXTERNAL_BLOCKER_NOT_READY.
- At least 5 StageStatus rows must include accepted_claim_ids and score_contribution_ids.
- At least 5 StageCourt traces must link to CensusStageStatus rows.

If these fail due code wiring:
- self-repair loop must patch and rerun.

Tests:
tests/test_census_v3_selective_deep_real_path.py
tests/test_census_v3_source_task_execution_not_fake.py
tests/test_census_v3_deep_claims_reach_stage.py

================================================================================
8. Existing Ledger Reuse Must Be Explicit
================================================================================

Wire existing accepted claims and previous stage state.

Implement:
src/e2r/census/existing_ledger_loader.py
src/e2r/census/claim_lifecycle_refresh.py

Inputs:
- previous production_cutover accepted_claims
- previous daily_watchlist
- previous census outputs
- evidence claim ledger jsonl
- score contribution ledger
- stagecourt traces

ExistingClaimReuseResult:
{
  "claim_id": "...",
  "symbol": "...",
  "reuse_status": "REUSED_CURRENT|STALE_NEEDS_REFRESH|SUPERSEDED|CONTRADICTED|REJECTED_SCOPE|UNKNOWN",
  "reason": "...",
  "followup_task_id": null
}

Rules:
- accepted claim can be reused only after lifecycle refresh.
- previous Stage cannot be copied blindly.
- stale claim cannot score.
- old risk requires current OPEN confirmation.
- previous accepted claim can open active thesis but must be freshness/lifecycle checked.

Acceptance:
- existing_ledger_load_attempted = true.
- existing_ledger_loaded_count reported.
- reused_current_claim_count reported.
- stale_needs_refresh_count reported.
- stale_claim_reused_as_current_count = 0.
- previous_stage_blind_copy_count = 0.
- if no prior ledger exists, report explicit NO_PRIOR_LEDGER rather than silently 0.

Tests:
tests/test_census_v3_existing_ledger_loader.py
tests/test_census_v3_lifecycle_refresh_required.py
tests/test_census_v3_no_blind_stage_copy.py

================================================================================
9. Stage Map Success Criteria: Hard Gate
================================================================================

FULL_UNIVERSE_STAGE_MAP_PASS requires all of the following:

Universe:
- raw_universe_count > 1000
- eligible_symbol_count > 1000
- every eligible symbol appears exactly once in census_stage_status
- missing_symbol_count = 0
- duplicate_symbol_count = 0

Baseline:
- source_timeline_count == eligible_symbol_count
- last_effective_thesis_count == eligible_symbol_count
- baseline_scan_result_count == eligible_symbol_count
- empty_baseline_inputs_count = 0
- baseline_source_family_wired_count >= 5

Distribution:
- Unknown <= 5%
- ProviderPending < 30% unless EXTERNAL_PROVIDER_BLOCKER
- stage_distribution not single bucket
- census_status_distribution not single bucket
- at least 4 census_status buckets
- at least 3 base_stage buckets
- NoKnownThesis / NoCurrentCatalyst present
- Stage1 or Stage2-Watch present
- At least one of Stage2-Actionable / Yellow-Pending / RiskReview / Reject present either live or controlled regression slice
- all Stage0/NoCurrentCatalyst rows have source_timeline_id and last_effective_thesis_id

Evidence:
- source_task_count > 0
- source_task_executed_count > 0
- accepted_claim_count > 0
- score_contribution_count > 0
- deterministic_stage_output_count > 0
- claim_to_stage_unlinked_count = 0
- score_contribution_unused_count = 0

Safety:
- orphan_score_count = 0
- claimless_nonzero_score_count = 0
- source_proxy_to_score_count = 0
- evidence_url_pending_to_score_count = 0
- price_path_only_to_score_count = 0
- market_anomaly_to_score_count = 0
- news_snippet_to_score_count = 0
- provider_failed_final_score_count = 0
- old_risk_without_current_open_to_score_count = 0
- cheap_scan_score_as_verified_score_count = 0
- recent_lookback_used_as_stage_cutoff_count = 0

If any hard gate fails:
- DO NOT declare FULL_UNIVERSE_STAGE_MAP_PASS.
- Run self-repair loop.
- Patch root cause.
- Rerun.

Tests:
tests/test_census_v3_stage_map_hard_gate.py
tests/test_census_v3_all_unknown_fails.py
tests/test_census_v3_all_provider_pending_fails.py
tests/test_census_v3_all_stage0_fails_without_source_proof.py

================================================================================
10. Self-Repair Loop Must Be Enforced in Code and Report
================================================================================

Implement:
src/e2r/census/self_repair.py
src/e2r/cli/run_e2r_census_v3_until_pass.py

CLI:
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v3_until_pass \
  --as-of-date YYYY-MM-DD \
  --universe krx \
  --mode census_selective_deep \
  --max-iterations 10 \
  --output-root output/census_v3/YYYY-MM-DD \
  --fail-on-external-blocker true \
  --fail-on-report-overclaim true

SelfRepairIteration:
{
  "iteration": 1,
  "command": "...",
  "status_before": "...",
  "failure_classes": [],
  "root_causes": [
    {
      "failure_class": "...",
      "file": "...",
      "function": "...",
      "evidence": "..."
    }
  ],
  "patches_applied": [],
  "tests_run": [],
  "metrics_before": {},
  "metrics_after": {},
  "resolved_failures": [],
  "unresolved_failures": []
}

Failure classes:
- EMPTY_BASELINE_INPUTS
- ALL_UNKNOWN
- ALL_PROVIDER_PENDING
- ALL_STAGE0_WITHOUT_SOURCE_PROOF
- CLAIM_TO_STAGE_DISCONNECTED
- SOURCE_TASK_FAKE_EXECUTION
- ACCEPTED_CLAIM_SUMMARY_ONLY
- SCORE_CONTRIBUTION_SUMMARY_ONLY
- NO_SOURCE_TIMELINE
- NO_LAST_EFFECTIVE_THESIS
- RECENT_LOOKBACK_CUTOFF
- EXISTING_LEDGER_NOT_WIRED
- PROVIDER_REGISTRY_NOT_WIRED
- NEWS_IR_REPORT_NOT_WIRED
- PRICE_ANOMALY_NOT_WIRED
- RISK_SOURCE_NOT_WIRED
- REPORT_LABEL_OVERCLAIM
- LEAF_AUDIT_MISMATCH
- EXTERNAL_PROVIDER_BLOCKER

Rules:
- If first run fails, at least one repair iteration must exist.
- If same failure persists after patch, continue.
- If max_iterations reached without pass, final status = NOT_READY, not completed.
- External provider blocker must include provider name, API key/env status, request id, error sample, and affected symbols.
- Self-repair cannot patch by loosening acceptance thresholds.
- Self-repair cannot fake source/claim/stage artifacts.

Acceptance:
- self_repair_log.json exists.
- self_repair_summary.md exists.
- final report includes iteration count and resolved failures.
- completion forbidden if unresolved non-external failures remain.

Tests:
tests/test_census_v3_self_repair_loop.py
tests/test_census_v3_no_completion_with_unresolved_failures.py
tests/test_census_v3_repair_cannot_loosen_thresholds.py

================================================================================
11. Independent Reviewer Gate
================================================================================

Reviewer “99/100 pass” is not enough.

Implement three independent audits that read only leaf artifacts.

Reviewer A: Trace Auditor
- validates symbol → source timeline → claim → score → stage trace
- fails on claim-to-stage disconnect

Reviewer B: Source Auditor
- validates source family attempts, provider failures, source_proxy contamination, snapshot/live classification
- fails on fake source task execution

Reviewer C: Stage Auditor
- validates stage distribution, StageCourt traces, pending vs reject logic, no recent cutoff misuse

Each reviewer:
- must run as separate CLI or independent module.
- must not import report generator counters.
- must output machine-readable JSON.
- any FAIL blocks completion.
- 99/100 is not pass if the failed item is critical.
- reviewer pass requires critical_count=0.

Reports:
docs/operational/census_mode_v3_reviewer_A_trace_audit.json
docs/operational/census_mode_v3_reviewer_B_source_audit.json
docs/operational/census_mode_v3_reviewer_C_stage_audit.json

Acceptance:
- all three reviewers critical_count = 0.
- all three reviewers verdict = PASS.
- any critical FAIL blocks FULL_UNIVERSE_STAGE_MAP_PASS.
- reviewer audit files cite leaf artifact paths and row IDs.

Tests:
tests/test_census_v3_independent_reviewer_gate.py

================================================================================
12. Tests Must Attack Known Cheat Patterns
================================================================================

Add/strengthen tests:

tests/test_census_v3_detect_empty_baseline.py
tests/test_census_v3_detect_accepted_claims_not_passed_to_stage.py
tests/test_census_v3_detect_source_task_replay_as_execution.py
tests/test_census_v3_detect_report_only_pass.py
tests/test_census_v3_detect_all_unknown_fake_pass.py
tests/test_census_v3_detect_all_provider_pending_fake_pass.py
tests/test_census_v3_detect_recent_cutoff_misuse.py
tests/test_census_v3_detect_source_proxy_score.py
tests/test_census_v3_detect_news_snippet_score.py
tests/test_census_v3_detect_provider_failure_final_red.py
tests/test_census_v3_detect_stage_without_trace.py
tests/test_census_v3_detect_summary_leaf_mismatch.py
tests/test_census_v3_detect_threshold_loosening.py
tests/test_census_v3_detect_one_line_huge_report.py

Every test must fail against the known bad patterns:
- accepted_claim_count in summary but no accepted_claim_ids in stage rows
- score_contribution_count in summary but no score_contribution_ids in stage rows
- build_stage_status called with accepted_claims=() for scored row
- source task execution accepted count inferred from PARSED status
- report claims FULL_UNIVERSE_STAGE_MAP_PASS but stage_distribution single bucket
- report claims pass with accepted_claim_count=0
- report claims pass with source_task_count=0
- source_proxy_only used as score evidence
- recent lookback cutoff drops active old contract
- provider failure mapped to Red

Full test:
PYTHONPATH=src python -m unittest discover -s tests -v

No skipped Census v3 tests allowed.
No xfail for current known issue.
No “future TODO” tests counted as pass.

================================================================================
13. Output Artifacts
================================================================================

Required output directory:

output/census_v3/YYYY-MM-DD/
  run_metadata.json
  self_repair_log.json
  universe.jsonl
  census_assessment_events.jsonl
  source_timelines.jsonl
  last_effective_thesis_states.jsonl
  baseline_inputs_summary.json
  baseline_scan_results.jsonl
  census_events.jsonl
  depth_decisions.jsonl
  research_brain_plans.jsonl
  source_tasks.jsonl
  source_task_executions.jsonl
  evidence_documents.jsonl
  evidence_anchors.jsonl
  raw_assertions.jsonl
  adjudicated_claims.jsonl
  accepted_claims.jsonl
  primitive_states.jsonl
  score_contributions.jsonl
  stagecourt_traces.jsonl
  census_stage_status.jsonl
  census_stage_map.csv
  census_stage_map.jsonl
  claim_to_stage_trace.jsonl
  census_stage_summary.json
  sector_stage_distribution.json
  provider_gap_report.json
  source_gap_report.json
  watchlist_seed_candidates.json
  deep_backfill_plan.json
  operator_digest.md
  audit_summary.json
  leaf_artifact_audit.json
  reviewer_A_trace_audit.json
  reviewer_B_source_audit.json
  reviewer_C_stage_audit.json

Required docs:

docs/operational/census_mode_v3_acceptance_report.md
docs/operational/census_mode_v3_readiness_verdict.md
docs/operational/census_mode_v3_self_repair_summary.md
docs/operational/census_mode_v3_leaf_artifact_audit.json
docs/operational/census_mode_v3_static_logic_audit.json
docs/operational/census_mode_v3_stage_map_summary.md
docs/operational/census_mode_v3_provider_gap_report.json
docs/operational/census_mode_v3_source_gap_report.json
docs/operational/census_mode_v3_watchlist_seed_report.md
docs/operational/census_mode_v3_deep_backfill_plan.md
docs/operational/census_mode_v3_reviewer_A_trace_audit.json
docs/operational/census_mode_v3_reviewer_B_source_audit.json
docs/operational/census_mode_v3_reviewer_C_stage_audit.json

Reports must be pretty-printed.
One-line huge JSON/MD fails.

================================================================================
14. Acceptance Report Must Include
================================================================================

docs/operational/census_mode_v3_acceptance_report.md must include:

1. Final status
2. Commit SHA / message / push status / working tree
3. Test command and pass/fail/skip
4. Self-repair iteration count
5. Resolved failure classes
6. Unresolved blockers
7. Raw universe count
8. Eligible symbol count
9. StageStatus count
10. Missing/duplicate symbols
11. SourceTimeline count
12. LastEffectiveThesis count
13. Baseline source family wired count
14. Event taxonomy counts
15. Recent vs historical/last-effective event counts
16. Existing ledger load count
17. Research Brain plan count
18. Source task count
19. Source task execution count
20. Accepted claim count
21. Score contribution count
22. StageCourt trace count
23. Claim-to-stage trace count
24. Stage distribution
25. Census status distribution
26. Depth distribution
27. Provider pending count
28. Unknown count
29. NoKnownThesis / NoCurrentCatalyst count
30. Provider/source gap summary
31. Orphan score count
32. Claimless nonzero score count
33. Source_proxy_to_score count
34. Evidence_url_pending_to_score count
35. Market_anomaly_to_score count
36. News_snippet_to_score count
37. Provider_failed_final_score count
38. Recent_lookback_cutoff_misuse count
39. Leaf artifact audit verdict
40. Reviewer A/B/C verdicts
41. Watchlist seed count
42. Deep backfill plan generated
43. Final verdict
44. Exact next step

================================================================================
15. Readiness Labels
================================================================================

Allowed labels:

- IMPLEMENTATION_MERGED
- CENSUS_V1_V2_RECLASSIFIED
- BASELINE_SOURCE_WIRED_PASS
- SOURCE_TIMELINE_PASS
- LAST_EFFECTIVE_THESIS_PASS
- CLAIM_TO_STAGE_TRACE_PASS
- CENSUS_LIGHT_PASS
- CENSUS_SELECTIVE_DEEP_PASS
- FULL_UNIVERSE_STAGE_MAP_PASS
- WATCHLIST_SEED_PASS
- SELF_REPAIR_LOOP_PASS
- INDEPENDENT_REVIEWER_PASS
- READY_FOR_DAILY_TRIGGER_INTEGRATION
- READY_FOR_DEEP_BACKFILL_DESIGN
- EXTERNAL_BLOCKER_NOT_READY

FULL_UNIVERSE_STAGE_MAP_PASS requires:
- all hard gates in Section 9 pass.
- LeafArtifactAuditor pass.
- Reviewer A/B/C pass.
- self-repair loop pass.
- full tests pass.
- no unresolved non-external failures.

If not:
- final label must be EXTERNAL_BLOCKER_NOT_READY or NOT_READY.
- do not use FULL_UNIVERSE_STAGE_MAP_PASS.
- do not use READY_FOR_DAILY_TRIGGER_INTEGRATION.

================================================================================
16. Final Answer Format
================================================================================

After completion, report only this structure:

1. Final status
- one of allowed labels

2. Commit
- SHA
- message
- push status
- working tree clean

3. Tests
- command
- passed / failed / skipped
- failed test names if any

4. Self-repair
- iteration count
- failure classes found
- root causes patched
- unresolved blockers

5. Universe
- raw universe
- eligible
- excluded counts
- missing/duplicate symbols

6. Source wiring
- source families wired
- timeline count
- last effective thesis count
- event taxonomy counts
- provider gaps

7. Deep path
- research brain plans
- source tasks
- source executions
- accepted claims
- score contributions
- StageCourt traces

8. Stage map
- stage distribution
- census status distribution
- depth distribution
- Unknown count
- ProviderPending count
- NoKnownThesis count

9. Trace audit
- claim-to-stage trace count
- unlinked claim count
- score contribution unused count
- stage rows missing trace count

10. Safety audit
- orphan score
- claimless nonzero score
- source_proxy_to_score
- provider_failed_final_score
- recent cutoff misuse
- market/news snippet score

11. Independent reviewers
- Reviewer A verdict
- Reviewer B verdict
- Reviewer C verdict

12. Watchlist / backfill
- watchlist seed count
- deep backfill plan generated
- top source gaps

13. Final verdict
- FULL_UNIVERSE_STAGE_MAP_PASS or not
- READY_FOR_DAILY_TRIGGER_INTEGRATION or not
- exact blockers
- exact next step

================================================================================
17. Prohibitions
================================================================================

- Do not stop at failure without repair.
- Do not claim pass from summary reports.
- Do not claim pass if leaf artifact audit fails.
- Do not claim pass if reviewer A/B/C has any critical fail.
- Do not claim pass if all symbols are Unknown.
- Do not claim pass if all symbols are ProviderPending.
- Do not claim pass if all symbols are Stage0 without source proof.
- Do not claim pass if accepted_claim_count = 0.
- Do not claim pass if source_task_count = 0.
- Do not claim pass if score_contribution_count = 0 in selective deep.
- Do not claim pass if stage rows do not reference accepted_claim_ids / score_contribution_ids.
- Do not count PARSED source tasks as accepted claims.
- Do not count existing report replay as real source execution.
- Do not use fixed recent lookback as Stage cutoff.
- Do not ignore old active contracts/theses.
- Do not ignore report/news/IR-only events.
- Do not score news snippets.
- Do not score CensusAssessmentEvent.
- Do not score market anomaly.
- Do not score source_proxy_only/evidence_url_pending/price_path_only memory.
- Do not finalize low score on provider failure.
- Do not mark source pending symbols as Red.
- Do not use cheap_scan_total_score as verified_score.
- Do not hardcode symbol/company/url exceptions.
- Do not change scoring weights or Stage thresholds.
- Do not output one-line huge reports.
- Do not hide source gaps.
- Do not pretend external provider blocker is success.
- Do not loosen thresholds to pass.
- Do not patch by faking leaf artifacts.

================================================================================
18. One-line goal
================================================================================

Census Mode v3의 목적은:

전체 KRX universe에 대해
각 종목의 마지막 유효 event / claim / thesis / risk / financial state를 실제 source timeline으로 만들고,
필요한 종목은 Evidence OS accepted claim까지 연결해,
전 종목의 현재 E2R Stage 상태판을 만드는 것이다.

성공은 report 숫자가 아니라:

symbol
→ source_timeline
→ last_effective_thesis
→ baseline_scan
→ depth_decision
→ source_task
→ accepted_claim
→ score_contribution
→ StageCourt
→ census_stage_status

이 trace가 leaf artifact로 검증될 때만 인정한다.

실패하면 끝내지 말고,
원인을 찾아 패치하고,
같은 명령을 재실행하고,
FULL_UNIVERSE_STAGE_MAP_PASS가 될 때까지 반복하라.