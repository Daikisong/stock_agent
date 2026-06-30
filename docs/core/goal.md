너는 Daikisong/stock_agent 레포의 E2R Census Mode v2를 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 구현되어 있다.
- Production Cutover v3는 CUTOVER_READY 상태다.
- Census v1은 전체 KRX universe row 생성과 safety audit skeleton은 통과했지만, 실제 Census Stage 지도는 실패했다.
- Census v1 최종 산출물:
  - raw universe: 3940
  - eligible: 3391
  - stage distribution: Unknown 3391
  - provider pending: 3391
  - accepted claim: 0
  - score contribution: 0
  - orphan score: 0
  - critical audit count: 0
  - verdict: READY_FOR_DEEP_BACKFILL_DESIGN
- 이 결과는 “전 종목에 억지 점수를 주지 않았다”는 안전성만 통과한 것이지, 전 종목 현재 Stage 지도는 아니다.
- 실패 원인은 census_runner._baseline_inputs_for_mode()가 빈 BaselineScanInputs()를 반환하고, 실제 OpenDART/KIND/KRX/CompanyGuide/ReportRadar/IR/News/price/existing claim ledger를 Census Baseline에 연결하지 않은 것이다.
- 이번 Goal은 실패하면 끝나는 것이 아니라, 실패 원인을 찾아 수리하고 성공 기준을 통과할 때까지 반복하는 작업이다.

이번 Goal 이름:
E2R Census Mode v2 — Real Baseline Source Wiring + Last Effective Thesis Stage Map + Self-Repair Until Pass

최종 목표:
전체 KRX eligible universe에 대해,
최근 공시 유무가 아니라,
각 종목의 마지막 유효 event / claim / thesis / risk / financial state를 찾아
as_of_date 현재 살아 있는 E2R 상태를 Stage 지도에 반영한다.

즉:

전체 KRX universe
→ CensusAssessmentEvent
→ 실제 baseline source wiring
→ 각 symbol별 Source Timeline 생성
→ LastEffectiveThesisState 판정
→ OfficialEvent / InfoEvent / MarketEvent / RiskEvent / ExistingClaim / LastValidFinancialState 수집
→ Research Brain triage
→ 필요한 종목만 SourceTask + Evidence OS
→ accepted claim 기반 deterministic score/stage
→ Stage0 / Stage1 / Stage2-Watch / Stage2-Actionable / Yellow-Pending / Green / ProviderPending / EvidenceInsufficient / RiskReview / Reject 분포 생성
→ watchlist seed + deep backfill plan 생성

절대 원칙:
1. “최근 공시 없음”이라는 이유만으로 모든 종목을 보류하지 않는다.
2. 최근 lookback window는 refresh 우선순위일 뿐 Stage cutoff가 아니다.
3. 한 달 전, 일 년 전, 그 이전의 event라도 아직 supersede/expire/resolved되지 않았으면 현재 thesis로 살아 있을 수 있다.
4. 상장사의 마지막 유효 정기보고서, 마지막 주요 공시, 마지막 risk 상태, 마지막 accepted claim, 마지막 Research Brain thesis를 확인한다.
5. 공시만 트리거가 아니다. IR, 실적자료, 리포트, 뉴스, 가격/거래량, 리스크 이벤트, 기존 claim ledger, Research Memory 모두 trigger source가 될 수 있다.
6. 단, trigger는 조사를 여는 문이고 accepted claim만 점수를 여는 열쇠다.
7. CensusAssessmentEvent는 전 종목 평가 시작 스탬프이지 score evidence가 아니다.
8. market anomaly는 score evidence가 아니라 investigation trigger다.
9. 뉴스 headline/snippet은 score evidence가 아니라 source task 또는 follow-up query hint다.
10. 뉴스로만 나온 사건도 full article/source/date/target scope가 검증되면 InfoEvent/CandidateEvent가 될 수 있다.
11. provider failure는 낮은 점수나 Red가 아니라 ProviderPending이다.
12. source를 실제로 봤지만 현재 thesis가 없으면 Stage0 / NoKnownE2RThesis / NoCurrentCatalyst가 가능하다.
13. source를 못 봤으면 NoCurrentCatalyst가 아니라 ProviderPending 또는 SourcePending이다.
14. source_proxy_only, evidence_url_pending, price_path_only memory는 current production score evidence가 아니다.
15. historical research memory는 현재 claim이 아니라 source route / false-positive / bridge requirement memory로만 사용한다.
16. scoring weight와 Stage threshold는 변경하지 않는다.
17. 특정 종목명, 특정 URL, 특정 키워드 예외 처리 금지.
18. FULL_UNIVERSE_STAGE_MAP_PASS는 전 종목 Unknown/ProviderPending/Stage0 100% 상태에서는 절대 선언하지 않는다.
19. 완료는 한 번 실행으로 끝내지 말고, 실패 원인 분석 → 패치 → 재실행 → 지표 개선 → acceptance pass까지 반복한다.
20. 외부 API 키/계약/네트워크 장애처럼 코드로 고칠 수 없는 blocker만 EXTERNAL_BLOCKER_NOT_READY로 남길 수 있다. 코드 wiring 실패는 반드시 고친다.

================================================================================
0. Self-Repair Until Pass 프로토콜
================================================================================

이번 Goal의 핵심은 “실패하면 보고”가 아니라 “실패하면 고치고 다시 실행”이다.

반드시 다음 루프를 구현하고 실제 작업에서 따르라.

SelfRepairLoop:

1. Run Census
2. Validate metrics
3. If failure:
   a. classify failure
   b. locate root cause
   c. patch code/config
   d. rerun same command
   e. compare before/after metrics
4. Repeat until acceptance pass
5. If external blocker:
   a. mark exact provider/key/network blocker
   b. do not claim pass
   c. output EXTERNAL_BLOCKER_NOT_READY

Failure classes:
- BASELINE_INPUT_EMPTY
- ALL_UNKNOWN
- ALL_PROVIDER_PENDING
- ALL_STAGE0_NO_SOURCE
- NO_RECENT_OR_HISTORICAL_EVENT_TIMELINE
- NO_EXISTING_LEDGER_WIRING
- NO_PROVIDER_REGISTRY_WIRING
- NO_SOURCE_TASKS_IN_SELECTIVE_DEEP
- NO_ACCEPTED_CLAIMS_IN_SELECTIVE_DEEP
- NO_SCORE_CONTRIBUTIONS_IN_SELECTIVE_DEEP
- PROVIDER_FAILURE_MISCLASSIFIED_AS_NO_EVENT
- NEWS_IR_REPORT_NOT_WIRED
- PRICE_ANOMALY_NOT_WIRED
- RISK_SOURCE_NOT_WIRED
- LAST_EFFECTIVE_THESIS_NOT_BUILT
- STALE_CLAIM_REUSED_WITHOUT_LIFECYCLE
- RECENT_LOOKBACK_USED_AS_STAGE_CUTOFF
- FULL_MAP_LABEL_WITH_EMPTY_EVIDENCE
- REPORT_LABEL_OVERCLAIM
- EXTERNAL_PROVIDER_BLOCKER

For every failure:
{
  "iteration": 1,
  "failure_class": "...",
  "root_cause_file": "...",
  "root_cause_function": "...",
  "before_metrics": {},
  "patch_summary": "...",
  "rerun_command": "...",
  "after_metrics": {},
  "resolved": true_or_false
}

Reports:
docs/operational/census_mode_v2_self_repair_log.json
docs/operational/census_mode_v2_self_repair_summary.md

Acceptance:
- self_repair_log exists.
- If first run fails, at least one patch/rerun iteration is recorded.
- Same failure cannot appear unresolved in final pass.
- Any external blocker prevents FULL_UNIVERSE_STAGE_MAP_PASS unless it is explicitly nonblocking.
- “Goal completed” is forbidden until final acceptance pass.

================================================================================
1. Census v1 실패 재분류
================================================================================

먼저 Census v1 결과를 정확히 재라벨링하라.

생성/수정:
docs/operational/census_mode_v1_reclassification.md

내용:
- Census v1은 CENSUS_SKELETON_PASS다.
- Census v1은 FULL_UNIVERSE_STAGE_MAP_PASS가 아니다.
- Census v1은 READY_FOR_DAILY_TRIGGER_INTEGRATION이 아니다.
- Census v1은 전체 universe row generation과 no-false-score safety는 통과했다.
- 그러나 baseline source wiring이 비어 있어 모든 종목이 Unknown/ProviderPending이 되었다.
- accepted_claim_count=0, score_contribution_count=0, source_task_count=0이면 실제 Stage 지도라고 부를 수 없다.
- _baseline_inputs_for_mode()가 빈 BaselineScanInputs()를 반환하는 동안 Census 완료 선언 금지.

Acceptance:
- v1 산출물의 라벨을 CENSUS_SKELETON_PASS로 낮춘다.
- FULL_UNIVERSE_STAGE_MAP_PASS, READY_FOR_DAILY_TRIGGER_INTEGRATION 라벨은 v2 성공 전까지 금지한다.
- docs/operational/census_mode_v1_reclassification.md에 실패 원인과 v2 목표를 명시한다.

================================================================================
2. 빈 BaselineScanInputs 제거
================================================================================

현재 문제의 핵심은 census_runner._baseline_inputs_for_mode()가 빈 입력을 반환한다는 점이다.

금지:
- return BaselineScanInputs() 단독 반환
- provider registry 없이 전 종목을 Unknown/ProviderPending으로 만드는 실행
- accepted_claims=() / score_contributions=()를 모든 symbol에 일괄 전달
- source task 없이 READY 라벨 부여
- deep count 0인데 FULL_UNIVERSE_STAGE_MAP_PASS 선언

구현:
src/e2r/census/baseline_input_collector.py

CensusBaselineInputCollector:

class CensusBaselineInputCollector:
    def collect(
        self,
        instruments: Sequence[UniverseInstrument],
        as_of_date: date,
        mode: str,
        provider_registry: SourceProviderRegistry,
        existing_ledger_paths: Sequence[Path],
        production_cutover_paths: Sequence[Path],
        price_provider: Optional[PriceProvider],
        report_radar_provider: Optional[ReportRadarProvider],
        research_memory_store: Optional[ResearchMemoryStore],
    ) -> BaselineScanInputs:
        ...

BaselineScanInputs must include:
- provider_failed_symbols
- provider_failure_by_symbol
- price_anomaly_symbols
- price_anomaly_by_symbol
- recent_official_events
- historical_official_events
- last_material_official_event_by_symbol
- risk_events_by_symbol
- companyguide_revision_events_by_symbol
- report_radar_events_by_symbol
- issuer_ir_events_by_symbol
- trusted_news_events_by_symbol
- existing_claim_counts
- existing_claim_refs_by_symbol
- existing_stage
- previous_watchlist_state
- last_effective_thesis_by_symbol
- source_gap_by_symbol
- no_data_reason_by_symbol

Important:
- Do not use “recent official events” as the only source.
- Build both recent and historical/last-effective event state.
- If a symbol has no fresh event but has a still-active old contract/thesis, it must not become NoCurrentCatalyst.
- If a provider fails, mark ProviderPending only for affected symbols/source families, not the whole universe.

Acceptance:
- _baseline_inputs_for_mode() removed or converted into a real collector call.
- BaselineScanInputs is non-empty in production census.
- At least 5 different baseline fields are populated in the output report.
- recent_official_events may be zero on quiet days, but last_effective_thesis / latest_filing / price / risk / ledger fields must still be populated.
- provider_pending 100% is failure unless every provider truly failed and EXTERNAL_PROVIDER_BLOCKER is declared.

Tests:
tests/test_census_v2_baseline_input_collector.py
tests/test_census_v2_no_empty_baseline_inputs.py
tests/test_census_v2_provider_pending_not_global_default.py

================================================================================
3. Source Timeline / Last Effective Thesis
================================================================================

Census는 “최근 이벤트”가 아니라 “마지막 유효 thesis”를 봐야 한다.

구현:
src/e2r/census/source_timeline.py
src/e2r/census/last_effective_thesis.py

SourceTimeline per symbol:

{
  "symbol": "...",
  "as_of_date": "...",
  "official_events": [],
  "risk_events": [],
  "financial_events": [],
  "revision_events": [],
  "ir_events": [],
  "trusted_news_events": [],
  "market_events": [],
  "existing_claim_events": [],
  "research_memory_hints": [],
  "latest_regular_report": null,
  "latest_material_disclosure": null,
  "latest_risk_status": null,
  "latest_price_context": null
}

LastEffectiveThesisState:

{
  "symbol": "...",
  "status": "ACTIVE_THESIS|HISTORICAL_ONLY|NO_KNOWN_THESIS|PROVIDER_PENDING|SOURCE_PENDING|CONTRADICTED|SUPERSEDED|EXPIRED|NEEDS_REFRESH",
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

Lifecycle examples:
- Supply contract:
  active until contract_end unless cancelled/superseded.
- Facility investment:
  active until completed/cancelled/converted to revenue/capacity.
- Regular report:
  supersedes prior regular report for financial actual state.
- Risk event:
  active until resolved/superseded/cleared by official source.
- News/IR thesis:
  active only if full source/date/issuer scope verified and not contradicted by later official data.
- Price anomaly:
  expires quickly as investigation trigger; never a score thesis by itself.
- Research memory:
  planning memory only, not current thesis unless revalidated by source-backed claim.

Rules:
- No arbitrary 30/90/365-day cutoff for Stage.
- Source-specific expiry/supersession rules must drive current status.
- A one-year-old active contract may remain current.
- A two-year-old unresolved risk may remain current if OPEN.
- A two-year-old resolved risk must not score.
- A one-day-old price spike with no claim is not a score thesis.

Acceptance:
- Every eligible symbol gets SourceTimeline.
- Every eligible symbol gets LastEffectiveThesisState.
- last_effective_thesis missing count = 0.
- NoCurrentCatalyst can only be assigned after SourceTimeline was built.
- ProviderPending can only be assigned if source timeline has provider failure.
- “recent lookback expired” cannot be the reason for dropping an active thesis.

Tests:
tests/test_census_v2_source_timeline.py
tests/test_census_v2_last_effective_thesis.py
tests/test_census_v2_old_active_contract_still_current.py
tests/test_census_v2_old_resolved_risk_not_current.py
tests/test_census_v2_recent_lookback_not_stage_cutoff.py

================================================================================
4. Baseline Source Families
================================================================================

Census baseline must not be 공시-only.

Wire the following source families.

A. OpenDART / DART
- latest regular report
- latest quarterly/semiannual/annual financial state
- supply contract disclosures
- facility investment
- earnings preannouncement
- correction disclosures
- risk-relevant disclosures
- contract cancellation / revision

B. KIND / KRX
- trading halt
- administrative issue
- delisting risk
- market warning
- disclosure violation
- investment warning/caution
- listing status

C. CompanyGuide / Report / Consensus
- EPS revision
- operating profit revision
- target price/report metadata
- report radar hit
- consensus trend
- if connector unavailable, mark provider gap; do not ignore

D. Issuer IR / Newsroom
- investor presentation
- earnings release
- conference call
- company newsroom
- product roadmap
- capacity / contract / revenue mix
- if not globally crawlable, use report_radar/source task on prioritized symbols

E. Trusted News / Industry Media
- only full article/source/date/title/issuer scope can become InfoEvent
- headline/snippet can only create follow-up task
- news-only event must not be ignored; it must be routed to verification

F. Price / Volume / Relative Strength
- volume spike
- relative strength
- breakout/gap
- sector momentum
- price is trigger only, not score evidence

G. Existing Evidence Ledger
- accepted claims from prior production runs
- existing StageStatus
- pending source tasks
- previous watchlist
- must lifecycle refresh before reuse

H. Research Memory
- MemoryCard / archetype hints
- false-positive patterns
- source route hints
- no direct score evidence

Acceptance:
- At least OpenDART + KRX/KIND + price + existing ledger path + one of CompanyGuide/Report/IR/News must be wired.
- If a source family is unavailable, it must appear in provider_gap_report with exact reason.
- No source family failure may silently turn into NoCurrentCatalyst.
- report/news-only events are represented as InfoEvent/SourceTask, not ignored.

Tests:
tests/test_census_v2_source_family_wiring.py
tests/test_census_v2_news_ir_report_not_ignored.py
tests/test_census_v2_price_trigger_not_score.py
tests/test_census_v2_provider_gap_reported.py

================================================================================
5. Event Taxonomy for Census
================================================================================

Create a unified event model.

CensusEvent types:
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

Event fields:
{
  "event_id": "...",
  "symbol": "...",
  "company_name": "...",
  "event_type": "...",
  "event_category": "official|financial|revision|report|ir|news|market|risk|ledger|memory|assessment",
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
- CensusAssessmentEvent score_evidence_allowed=false.
- MarketAnomalyEvent score_evidence_allowed=false.
- TrustedNewsEvent score_evidence_allowed=false unless full source+anchor+issuer scope verified through Evidence OS.
- ResearchMemoryHintEvent score_evidence_allowed=false.
- ExistingClaimEvent score_evidence_allowed=true only after lifecycle refresh.
- OfficialEvent may become score evidence only through Evidence OS accepted claim.

Acceptance:
- Every event has event_category and score_evidence_allowed.
- market/news/memory assessment events never directly create score.
- existing claims go through lifecycle refresh.
- no event type hardcoded to positive score.

Tests:
tests/test_census_v2_event_taxonomy.py
tests/test_census_v2_event_score_eligibility_policy.py

================================================================================
6. Actual Baseline Scan Flow
================================================================================

Replace empty flow with actual flow:

1. Build KRX eligible universe.
2. For every eligible symbol:
   - create CensusAssessmentEvent
   - fetch/lookup source timeline
   - collect official/financial/risk/revision/price/ledger/memory events
   - build LastEffectiveThesisState
   - run BaselineScanner with real BaselineScanInputs
   - produce BaselineScanResult
   - apply DepthPolicy
   - produce initial CensusStageStatus

3. For selected deep symbols:
   - Research Brain triage
   - SourceTask generation
   - SourceTask execution
   - Evidence OS extraction
   - PrimitiveState
   - ScoreContributionLedger
   - DeterministicScorer
   - StageCourt
   - update CensusStageStatus

4. For non-deep symbols:
   - Stage0 / Stage1 / ProviderPending / RiskReview / NoKnownThesis based on source timeline and baseline.

Acceptance:
- baseline_scan_results count equals eligible_symbol_count.
- SourceTimeline count equals eligible_symbol_count.
- LastEffectiveThesisState count equals eligible_symbol_count.
- stage_status count equals eligible_symbol_count.
- Unknown count <= 5% unless external blocker.
- ProviderPending count < 30% unless provider outage documented.
- NoCurrentCatalyst / NoKnownThesis count is allowed, but only after source timeline exists.
- stage distribution cannot be a single bucket.
- at least 4 distinct census statuses appear in production census.
- at least 3 distinct base_stage values appear.
- selective_deep mode must produce source_task_count > 0 and accepted_claim_count > 0.
- if accepted_claim_count remains 0, self-repair loop must patch source wiring or label EXTERNAL_BLOCKER_NOT_READY.

Tests:
tests/test_census_v2_actual_baseline_flow.py
tests/test_census_v2_no_single_bucket_stage_map.py
tests/test_census_v2_selective_deep_produces_claims.py

================================================================================
7. Depth Policy v2
================================================================================

DepthPolicy must not use recent-only logic.

Inputs:
- LastEffectiveThesisState
- official event strength
- risk event strength
- revision/report/IR/news event strength
- market anomaly strength
- existing claim count
- existing stage
- provider/source gap
- sector quota
- random audit quota
- previous pending state

Depth outputs:
- L0_UNIVERSE_ONLY
- L1_BASELINE_ONLY
- L2_OFFICIAL_LIGHT
- L3_RESEARCH_BRAIN_TRIAGE
- L4_DEEP_DOSSIER
- L5_VERIFIED_STAGE

Rules:
- Active thesis → at least L2.
- Active thesis + missing bridge → L3/L4.
- Existing accepted claim → lifecycle refresh; if current, L3/L4 as needed.
- Official material event → L3/L4.
- Risk event → L3/L4 risk review.
- News/IR/report event → L3 if full source or verification task exists.
- Market-only anomaly → L2/L3 investigation only.
- NoKnownThesis → L1 and Stage0.
- Provider gap → ProviderPending, not NoKnownThesis.
- Sector quota ensures every large sector has some deep/audit sample.

Acceptance:
- deep_count > 0.
- research_brain_plan_count > 0 in selective_deep.
- source_task_count > 0 in selective_deep.
- no deep LLM for all symbols by default.
- sector audit sample exists.
- symbols with active thesis are not left at Stage0 solely due age.

Tests:
tests/test_census_v2_depth_policy_last_thesis.py
tests/test_census_v2_active_old_thesis_deepened.py
tests/test_census_v2_sector_audit_quota.py

================================================================================
8. Existing Claim Ledger Reuse
================================================================================

Wire existing accepted claims and previous StageStatus.

Inputs:
- output/production_cutover_v3 accepted_claims
- output/daily_watchlist
- previous census output
- evidence claim ledger jsonl
- score contribution ledger
- stagecourt traces

Implement:
src/e2r/census/existing_ledger_loader.py
src/e2r/census/lifecycle_refresh.py

Rules:
- Existing claim can be reused only after lifecycle refresh.
- Old positive claim must check effective_end/supersession.
- Old risk claim needs current OPEN confirmation.
- Previous stage cannot be copied blindly.
- Existing claim can open active thesis, but must be refreshed if stale.

Acceptance:
- existing_ledger_loaded_count > 0 if prior ledger exists.
- reused_current_claim_count reported.
- stale_needs_refresh_count reported.
- stale_claim_reused_as_current_count = 0.
- previous_stage_blind_copy_count = 0.

Tests:
tests/test_census_v2_existing_ledger_loader.py
tests/test_census_v2_lifecycle_refresh.py
tests/test_census_v2_no_blind_stage_copy.py

================================================================================
9. Report / News / IR Handling
================================================================================

공시 컷 금지. 공시가 아닌 source도 Census에 들어와야 한다.

Implement:
- ReportRadar ingestion for Census
- IssuerIR/Newsroom event ingestion where provider available
- TrustedNews event ingestion or explicit provider gap
- News/IR/Report source task generation for verification

Rules:
- report/news/IR headline can create InfoEvent and SourceTask.
- report/news/IR cannot score unless Evidence OS accepted claim.
- snippet-only count reported.
- full source missing → SourcePending/VerificationPending, not ignored.
- news-only event can trigger Research Brain triage if source quality sufficient.

Acceptance:
- report_event_count > 0 or provider_gap documented.
- trusted_news_event_count > 0 or provider_gap documented.
- issuer_ir_event_count > 0 or provider_gap documented.
- snippet_to_score_count = 0.
- news_event_to_source_task_count > 0 in selective_deep if news events exist.

Tests:
tests/test_census_v2_report_news_ir_ingestion.py
tests/test_census_v2_news_only_event_verification.py
tests/test_census_v2_snippet_never_scores.py

================================================================================
10. Selective Deep Evidence Path
================================================================================

Census v2 must prove that deep path works inside Census.

For selected deep symbols:
- Create ResearchBrainPlan.
- Create SourceTasks.
- Execute SourceTasks through production source connectors.
- Run Evidence OS.
- Generate accepted claims.
- Generate ScoreContributions.
- Run StageCourt.
- Update CensusStageStatus.

Minimum selective_deep acceptance:
- research_brain_plan_count >= 30 OR source/provider gap with NOT_READY.
- source_task_count >= 50 OR source/provider gap with NOT_READY.
- source_task_executed_count >= 30 OR source/provider gap with NOT_READY.
- accepted_claim_count >= 10 OR source/provider gap with NOT_READY.
- score_contribution_count >= 5 OR source/provider gap with NOT_READY.
- deterministic_stage_output_count >= 5 OR source/provider gap with NOT_READY.
- If any minimum fails due code wiring, patch and rerun.
- If any minimum fails due external provider, mark EXTERNAL_BLOCKER_NOT_READY.

Tests:
tests/test_census_v2_selective_deep_path.py
tests/test_census_v2_source_task_to_evidence_os.py
tests/test_census_v2_score_stage_update.py

================================================================================
11. Stage Map Success Criteria
================================================================================

Census v2 is successful only if the stage map is not empty and not a single default bucket.

Minimum status distribution:
- Unknown <= 5%
- ProviderPending < 30% unless provider outage
- At least 4 census_status buckets
- At least 3 base_stage buckets
- NoCurrentCatalyst/NoKnownThesis present
- Stage1 or Stage2-Watch present
- ProviderPending or SourcePending present only where actual provider/source gap exists
- At least one of Stage2-Actionable / Yellow-Pending / RiskReview / Reject present, either live or controlled regression slice
- accepted_claim_count > 0
- score_contribution_count > 0
- source_task_count > 0
- orphan_score_count = 0
- claimless nonzero score count = 0

If production day is genuinely low-signal:
- still must show NoKnownThesis / MarketAnomaly / ProviderPending / RiskReview / Stage1 split.
- cannot be Unknown 100%.
- cannot be ProviderPending 100%.
- cannot be Stage0 100% unless all source families verified no events and no existing thesis, which is unrealistic for full KRX universe; if this happens, classify as BASELINE_WIRING_FAILURE and repair.

Tests:
tests/test_census_v2_stage_map_success_criteria.py
tests/test_census_v2_all_unknown_fails.py
tests/test_census_v2_all_provider_pending_fails.py
tests/test_census_v2_all_stage0_fails_without_source_proof.py

================================================================================
12. Source Lifecycle and “Recent” Policy
================================================================================

Create policy file:
configs/e2r_census_lifecycle_policy_v1.json
docs/operational/census_mode_v2_lifecycle_and_recency_policy.md

Policy:
- recent_refresh_window_days:
  used only for prioritizing fresh source fetch.
- material_event_history_window:
  source-specific and can be long.
- active_contract_lifecycle:
  from contract_start to contract_end unless cancelled/superseded.
- facility_investment_lifecycle:
  active until completion/cancellation/revenue conversion.
- risk_lifecycle:
  active until resolved/superseded/cleared.
- regular_report_lifecycle:
  latest report supersedes prior financial actual state.
- revision_lifecycle:
  active until newer consensus/revision/report supersedes.
- news_ir_lifecycle:
  requires source-backed claim and must be checked against later official data.
- market_anomaly_lifecycle:
  short-lived investigation trigger only.
- research_memory_lifecycle:
  planning memory only; never current claim.

Acceptance:
- No code uses fixed recent window as stage cutoff.
- Every event type has lifecycle policy.
- Old active event fixture remains active.
- Old expired event fixture becomes historical.
- Latest regular report supersedes old report.

Tests:
tests/test_census_v2_lifecycle_policy.py
tests/test_census_v2_no_fixed_recent_stage_cutoff.py

================================================================================
13. Static Logic Audit v2
================================================================================

Implement:
src/e2r/cli/audit_e2r_census_v2.py

Critical counts:
- empty_baseline_inputs_count
- all_unknown_stage_map_count
- all_provider_pending_count
- all_stage0_without_source_proof_count
- baseline_source_family_wired_count_below_min
- source_timeline_missing_count
- last_effective_thesis_missing_count
- recent_lookback_used_as_stage_cutoff_count
- census_assessment_event_to_score_count
- no_claim_nonzero_score_count
- source_proxy_to_score_count
- evidence_url_pending_to_score_count
- price_path_only_to_score_count
- market_anomaly_to_score_count
- news_snippet_to_score_count
- provider_failed_final_score_count
- old_risk_without_current_open_to_score_count
- stale_claim_reused_current_count
- cheap_scan_score_as_verified_score_count
- research_brain_stage_direct_output_count
- research_brain_score_direct_output_count
- no_current_event_marked_red_count
- source_pending_marked_red_count
- source_task_count_zero_in_selective_deep
- accepted_claim_count_zero_in_selective_deep
- score_contribution_count_zero_in_selective_deep
- report_overclaims_full_map_count
- one_line_large_report_count
- unbounded_fetch_config_count

All critical counts must be 0.

Reports:
docs/operational/census_mode_v2_static_logic_audit.json

================================================================================
14. SLA / Sharding / Resume
================================================================================

Full universe Census must be resumable and must not hang.

Implement/strengthen:
- shard planner
- checkpoint store
- resume
- partial run report
- provider circuit breaker
- per-source budgets
- per-symbol budgets
- per-sector quotas

Rules:
- If source budget exhausted, mark RuntimeBudgetPending.
- RuntimeBudgetPending is not Red.
- If shard fails, repair and rerun failed shard.
- Same source snapshot + same config rerun must be deterministic.
- No hidden background work.
- No unbounded fetch.

Acceptance:
- shard_count configurable.
- full eligible universe can run in shards.
- failed shard can resume.
- same shard rerun idempotent.
- no duplicate symbol rows after merge.
- runtime budget exhausted rows reported.

Tests:
tests/test_census_v2_shard_resume.py
tests/test_census_v2_idempotency.py
tests/test_census_v2_sla_budget.py

================================================================================
15. Output Artifacts
================================================================================

Output directory:

output/census_v2/YYYY-MM-DD/
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
  census_stage_summary.json
  sector_stage_distribution.json
  provider_gap_report.json
  source_gap_report.json
  watchlist_seed_candidates.json
  deep_backfill_plan.json
  operator_digest.md
  audit_summary.json

Docs:
docs/operational/census_mode_v2_acceptance_report.md
docs/operational/census_mode_v2_stage_map_summary.md
docs/operational/census_mode_v2_universe_coverage.json
docs/operational/census_mode_v2_sector_stage_distribution.json
docs/operational/census_mode_v2_provider_gap_report.json
docs/operational/census_mode_v2_source_gap_report.json
docs/operational/census_mode_v2_watchlist_seed_report.md
docs/operational/census_mode_v2_deep_backfill_plan.md
docs/operational/census_mode_v2_self_repair_summary.md
docs/operational/census_mode_v2_static_logic_audit.json
docs/operational/census_mode_v2_readiness_verdict.md

================================================================================
16. Readiness Labels
================================================================================

Allowed labels:
- IMPLEMENTATION_MERGED
- CENSUS_V1_RECLASSIFIED
- BASELINE_SOURCE_WIRED_PASS
- SOURCE_TIMELINE_PASS
- LAST_EFFECTIVE_THESIS_PASS
- CENSUS_LIGHT_PASS
- CENSUS_SELECTIVE_DEEP_PASS
- FULL_UNIVERSE_STAGE_MAP_PASS
- WATCHLIST_SEED_PASS
- SELF_REPAIR_LOOP_PASS
- READY_FOR_DAILY_TRIGGER_INTEGRATION
- READY_FOR_DEEP_BACKFILL_DESIGN
- EXTERNAL_BLOCKER_NOT_READY

Minimum Goal completion:
- CENSUS_V1_RECLASSIFIED
- BASELINE_SOURCE_WIRED_PASS
- SOURCE_TIMELINE_PASS
- LAST_EFFECTIVE_THESIS_PASS
- CENSUS_LIGHT_PASS
- CENSUS_SELECTIVE_DEEP_PASS
- FULL_UNIVERSE_STAGE_MAP_PASS
- SELF_REPAIR_LOOP_PASS
- static critical count 0
- full tests pass

FULL_UNIVERSE_STAGE_MAP_PASS requires:
- every eligible symbol represented exactly once
- Unknown <= 5%
- ProviderPending < 30% unless external outage
- at least 4 census_status buckets
- at least 3 base_stage buckets
- accepted_claim_count > 0
- source_task_count > 0
- score_contribution_count > 0
- no claimless nonzero score
- no source_proxy_to_score
- no provider_failed_final_score
- no recent-lookback cutoff misuse

If any required metric fails:
- run self-repair loop.
- patch root cause.
- rerun.
- do not claim completion until pass.

If impossible due external provider:
- label EXTERNAL_BLOCKER_NOT_READY.
- report exact external blocker.
- do not claim FULL_UNIVERSE_STAGE_MAP_PASS.

================================================================================
17. Required Tests
================================================================================

Add or strengthen:

tests/test_census_v2_baseline_input_collector.py
tests/test_census_v2_no_empty_baseline_inputs.py
tests/test_census_v2_source_timeline.py
tests/test_census_v2_last_effective_thesis.py
tests/test_census_v2_source_family_wiring.py
tests/test_census_v2_event_taxonomy.py
tests/test_census_v2_actual_baseline_flow.py
tests/test_census_v2_depth_policy_last_thesis.py
tests/test_census_v2_existing_ledger_loader.py
tests/test_census_v2_lifecycle_refresh.py
tests/test_census_v2_report_news_ir_ingestion.py
tests/test_census_v2_selective_deep_path.py
tests/test_census_v2_stage_map_success_criteria.py
tests/test_census_v2_lifecycle_policy.py
tests/test_census_v2_no_fixed_recent_stage_cutoff.py
tests/test_census_v2_static_logic_audit.py
tests/test_census_v2_shard_resume.py
tests/test_census_v2_self_repair_loop.py
tests/test_census_v2_no_goal_complete_on_failed_metrics.py

Full command:
PYTHONPATH=src python -m unittest discover -s tests -v

No skipped Census v2 tests allowed unless explicitly marked future deep-backfill-only.
Skipped tests cannot be required for Goal completion.

================================================================================
18. Acceptance Report Format
================================================================================

docs/operational/census_mode_v2_acceptance_report.md must include:

1. Final status
2. Commit SHA / message / push status / working tree
3. Test command and pass/fail/skip
4. Census v1 reclassification
5. Self-repair iteration count
6. Self-repair resolved failure classes
7. Universe coverage
8. Baseline source wiring metrics
9. Source timeline count
10. Last effective thesis count
11. Event taxonomy counts
12. Recent vs historical/last-effective event counts
13. Provider/source gap summary
14. Stage distribution
15. Census status distribution
16. Depth distribution
17. Research Brain plan count
18. Source task count
19. Source task execution count
20. Accepted claim count
21. Score contribution count
22. Orphan score count
23. Source_proxy_to_score count
24. Provider_failed_final_score count
25. Claimless nonzero score count
26. Unknown count
27. ProviderPending count
28. NoKnownThesis / NoCurrentCatalyst count
29. Watchlist seed count
30. Deep backfill plan status
31. Static audit critical counts
32. Final verdict
33. Remaining blockers

================================================================================
19. Final Response Format
================================================================================

After completion, report only:

1. Final status
- IMPLEMENTATION_MERGED / CENSUS_V1_RECLASSIFIED / BASELINE_SOURCE_WIRED_PASS / SOURCE_TIMELINE_PASS / LAST_EFFECTIVE_THESIS_PASS / CENSUS_LIGHT_PASS / CENSUS_SELECTIVE_DEEP_PASS / FULL_UNIVERSE_STAGE_MAP_PASS / WATCHLIST_SEED_PASS / SELF_REPAIR_LOOP_PASS / READY_FOR_DAILY_TRIGGER_INTEGRATION / READY_FOR_DEEP_BACKFILL_DESIGN / EXTERNAL_BLOCKER_NOT_READY

2. Commit
- SHA
- message
- push status
- working tree clean

3. Tests
- command
- passed / failed / skipped

4. Self-repair
- iteration count
- failure classes found
- patches made
- final unresolved blockers

5. Universe
- raw universe
- eligible
- excluded counts
- missing/duplicate symbol count

6. Baseline wiring
- source families wired
- official event count
- historical/last-effective event count
- report/news/IR event count
- market anomaly count
- risk event count
- existing ledger count

7. Source timeline
- timeline count
- last effective thesis count
- active thesis
- no known thesis
- provider pending
- stale needs refresh

8. Stage map
- stage distribution
- census status distribution
- depth distribution
- Unknown count
- ProviderPending count

9. Evidence / score
- source task count
- accepted claim count
- score contribution count
- orphan score
- claimless nonzero score
- source_proxy_to_score

10. Watchlist / backfill
- watchlist seed count
- deep backfill plan generated
- top source gaps

11. Verdict
- FULL_UNIVERSE_STAGE_MAP_PASS or not
- READY_FOR_DAILY_TRIGGER_INTEGRATION or not
- blockers
- exact next step

================================================================================
20. Prohibitions
================================================================================

- Do not stop at failure without repair.
- Do not claim Goal complete if all symbols are Unknown.
- Do not claim Goal complete if all symbols are ProviderPending.
- Do not claim Goal complete if accepted_claim_count = 0 in selective_deep.
- Do not claim Goal complete if source_task_count = 0 in selective_deep.
- Do not use fixed recent lookback as Stage cutoff.
- Do not ignore old active contracts/theses.
- Do not ignore news/IR/report-only events.
- Do not use news snippet as score evidence.
- Do not score CensusAssessmentEvent.
- Do not score market anomaly.
- Do not score source_proxy_only/evidence_url_pending/price_path_only memory.
- Do not finalize low score on provider failure.
- Do not mark no-event symbols as Red.
- Do not mark source pending symbols as Red.
- Do not use cheap_scan_total_score as verified_score.
- Do not hardcode symbol/company/url exceptions.
- Do not change scoring weights or Stage thresholds.
- Do not output one-line huge reports.
- Do not hide source gaps.
- Do not pretend external provider blocker is success.

================================================================================
21. One-line goal
================================================================================

Census Mode v2의 목적은:

“최근 공시가 있는 종목만 보는 것”도 아니고,
“모든 티커에 억지 점수를 주는 것”도 아니다.

목적은:

전체 KRX universe에 대해
각 종목의 마지막 유효 event / claim / thesis / risk / financial state를 찾아
as_of_date 현재 살아 있는 E2R 상태를 붙이는 것이다.

즉:

전체 종목
→ 실제 source timeline
→ last effective thesis
→ 필요한 종목만 deep evidence
→ Evidence OS accepted claim
→ deterministic Stage
→ 전 시장 Stage 지도

이 경로가 성공할 때까지
실패 원인을 찾아 수리하고 재실행하라.