너는 Daikisong/stock_agent 레포의 E2R Census Mode v1을 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 구현되어 있다.
- Research Brain / Production Cutover Gate v3는 CUTOVER_READY 상태다.
- 최신 cutover verdict는 production_verdict=CUTOVER_READY, static critical count=0, blockers=[] 상태다.
- Census readiness는 READY_FOR_CENSUS_DESIGN 상태다.
- 아직 PRODUCTION_READY는 아니다. 사용자 final cutover approval flag가 false이기 때문이다.
- 이번 Goal의 목적은 “실제 매수 추천”이 아니라, 전체 시장의 현재 E2R Stage 지도를 만드는 Census Mode를 구현하는 것이다.

이번 Goal 이름:
E2R Census Mode v1 — Full Universe Stage Map / Baseline Ledger / Incremental Update Foundation

최종 목표:
전체 KRX universe를 대상으로
트리거가 뜬 종목만 보는 daily mode가 아니라,
모든 종목에 대해 현재 E2R 상태를 부여하는 전 시장 Stage 지도를 만든다.

즉:

KRX 전체 유니버스
→ CensusAssessmentEvent 생성
→ cheap baseline scan
→ 공식 source / 기존 claim ledger / 최근 trigger 확인
→ Research Brain이 필요한 경우만 아키타입 가설과 source task 생성
→ Evidence OS accepted claim만 점수화
→ deterministic scorer / StageCourt
→ 전체 종목 Stage / confidence / source gap / next action 지도 출력

Census Mode는 모든 종목을 억지로 deep research하는 기능이 아니다.
Census Mode는 모든 종목에 “현재 판단 가능한 Stage 상태와 판단 깊이”를 붙이는 기능이다.

절대 원칙:
1. Census Mode는 Research Brain이나 LLM이 score/stage를 직접 만들지 않는다.
2. Census Mode는 Evidence OS를 우회하지 않는다.
3. Census Mode에서 비영점 score는 반드시 accepted current source-backed claim_id를 가진다.
4. 새 사건이 없는 종목은 억지로 Red가 아니라 NoCurrentCatalyst / Stage0 / Stage1 / CensusLightOnly가 될 수 있다.
5. provider failure는 낮은 점수 확정이 아니라 ProviderPending이다.
6. source가 부족한 종목은 SourcePending 또는 EvidenceInsufficient이지 3-Red 확정이 아니다.
7. market anomaly는 investigation trigger일 뿐 score evidence가 아니다.
8. news snippet, source_proxy_only, evidence_url_pending, price_path_only memory는 current production score evidence가 아니다.
9. full universe run은 bounded budget / shard / checkpoint 기반이어야 한다.
10. scoring weight와 Stage threshold는 변경하지 않는다.
11. 특정 종목명, 특정 URL, 특정 키워드 예외 처리 금지.
12. Census 결과는 buy/sell 추천이 아니라 운영 상태판이다.

================================================================================
0. Census Mode의 위치 정의
================================================================================

먼저 문서로 운영 모드를 분리하라.

생성:
docs/operational/census_mode_v1_design.md

내용:
- Daily Trigger Mode:
  새 공시/IR/리포트/가격 이상/리스크 이벤트가 생긴 종목만 깊게 본다.

- Census Mode:
  트리거 유무와 상관없이 전체 universe에 현재 Stage 상태를 붙인다.

- Deep Backfill Mode:
  전체 종목을 여러 shard로 나눠 장기간 deep evidence ledger를 구축한다.
  이번 Goal에서는 Deep Backfill 전체 구현은 하지 않는다. 단, 설계와 future backlog는 작성한다.

- Watchlist Update Mode:
  기존 Watchlist/Pending 종목만 재평가한다.

Census Mode의 목적:
1. 전체 시장 Stage 지도 생성
2. 놓친 후보 발견
3. source/provider gap 확인
4. 섹터별 Stage 분포 확인
5. 이후 daily trigger mode가 업데이트할 baseline ledger 생성

Census Mode의 금지:
- 모든 종목에 억지 점수 부여
- source 없는 종목을 3-Red로 확정
- cheap scan score를 verified score로 사용
- market-only event를 score evidence로 사용
- source_proxy research memory를 current claim으로 사용

================================================================================
1. 새 핵심 개념: CensusAssessmentEvent
================================================================================

트리거가 없는 종목도 Census 평가를 받아야 하므로 CandidateEvent와 별도로 CensusAssessmentEvent를 도입하라.

CensusAssessmentEvent:

{
  "assessment_event_id": "...",
  "symbol": "...",
  "company_name": "...",
  "as_of_date": "YYYY-MM-DD",
  "assessment_type": "baseline_census",
  "source_family": "FullUniverseCensus",
  "reason": "periodic full-universe E2R stage assessment",
  "universe_source": "KRX",
  "instrument_status": "ACTIVE|SUSPENDED|DELISTED|UNKNOWN",
  "market": "KOSPI|KOSDAQ|KONEX|OTHER",
  "large_sector_id": null,
  "existing_watchlist_status": null,
  "recent_candidate_events": [],
  "recent_claim_ledger_refs": [],
  "baseline_scan_refs": [],
  "eligible_for_deep_dossier": false
}

규칙:
- CensusAssessmentEvent는 score evidence가 아니다.
- CensusAssessmentEvent는 평가를 여는 행정 이벤트다.
- CensusAssessmentEvent만 있고 accepted claim이 없으면 Stage0/NoCurrentCatalyst 또는 Stage1/LightWatch로 남아야 한다.
- CensusAssessmentEvent 때문에 score가 올라가면 실패다.

테스트:
tests/test_census_assessment_event.py

필수 assertion:
- CensusAssessmentEvent alone produces no score contribution.
- CensusAssessmentEvent without evidence can produce Stage0_NO_CURRENT_CATALYST.
- CensusAssessmentEvent is not treated as positive trigger.

================================================================================
2. 새 핵심 출력: CensusStageStatus
================================================================================

Census에서는 Stage와 판단 깊이를 분리해야 한다.

CensusStageStatus:

{
  "symbol": "...",
  "company_name": "...",
  "as_of_date": "...",

  "census_status": "SCANNED|LIGHT_ONLY|DEEP_VERIFIED|PENDING_SOURCE|PENDING_PROVIDER|SKIPPED_INELIGIBLE|FAILED",
  "assessment_depth": "UNIVERSE_ONLY|CHEAP_BASELINE|OFFICIAL_LIGHT|RESEARCH_BRAIN_TRIAGE|DEEP_DOSSIER|VERIFIED_STAGE",
  "base_stage": "Stage0|Stage1|Stage2-Watch|Stage2-Actionable|Stage3-Yellow|Stage3-Green|Reject|Red|Unknown",
  "investigation_status": "COMPLETE|PENDING|EXHAUSTED|PROVIDER_FAILED|RUNTIME_BUDGET_EXHAUSTED|NO_CURRENT_CATALYST",
  "transition_overlay": "NONE|4A|4B|4C",

  "stage_confidence": "HIGH|MEDIUM|LOW|INSUFFICIENT_EVIDENCE",
  "score_valid_status": "FINAL|FINAL_WITH_NONMATERIAL_GAPS|PENDING_MATERIAL_GAPS|PROVIDER_FAILED|NO_CURRENT_EVENT|INVALID_EVIDENCE|NOT_SCORED",

  "trigger_priority_score": null,
  "verified_score": null,
  "provisional_score": null,
  "score_interval_lower": null,
  "score_interval_upper": null,

  "primary_archetype": null,
  "secondary_archetypes": [],
  "large_sector_id": null,

  "accepted_claim_count": 0,
  "score_contribution_count": 0,
  "claim_backed_score_ratio": 0.0,
  "orphan_score_count": 0,

  "recent_event_count": 0,
  "recent_official_event_count": 0,
  "market_anomaly_count": 0,
  "risk_event_count": 0,

  "missing_primitives": [],
  "failed_stage_gates": [],
  "provider_gaps": [],
  "source_gaps": [],
  "next_actions": []
}

Stage 의미:
- Stage0 / NoCurrentCatalyst:
  현재 새 사건, accepted claim, watchlist thesis가 없음.
- Stage1 / LightWatch:
  약한 official/price/revision 신호는 있으나 deep evidence 없음.
- Stage2-Watch:
  아키타입 가설은 있으나 core bridge claim 부족.
- Stage2-Actionable:
  accepted claim이 존재하고 아키타입상 조사/관찰 가치가 있음.
- Stage3-Yellow:
  높은 점수 또는 강한 bridge가 있으나 Green gate 일부 미충족.
- Stage3-Green:
  필수 primitive, source family, score gate, red-team gate 통과.
- ProviderPending:
  판단에 필요한 source가 provider failure.
- EvidenceInsufficient:
  source는 봤으나 claim 부족.
- Reject/Red:
  source-backed 부정 evidence 또는 guard에 의해 낮음.
- 4B/4C:
  기존 thesis 또는 current hard break 조건에 의해 transition overlay로 처리.

================================================================================
3. 새 모듈 구조
================================================================================

다음 모듈을 추가하라.

src/e2r/census/
    __init__.py
    schemas.py
    universe.py
    census_event.py
    baseline_scanner.py
    baseline_classifier.py
    triage.py
    depth_policy.py
    shard_planner.py
    checkpoint_store.py
    census_runner.py
    deep_dossier_scheduler.py
    stage_status_builder.py
    census_ledger.py
    census_reports.py
    census_audit.py
    census_sla.py
    census_backfill_plan.py
    watchlist_seed_exporter.py

CLI:
src/e2r/cli/run_e2r_census_mode.py
src/e2r/cli/run_e2r_census_shard.py
src/e2r/cli/audit_e2r_census_mode.py
src/e2r/cli/export_e2r_census_watchlist.py
src/e2r/cli/build_e2r_deep_backfill_plan.py

Configs:
configs/e2r_census_mode_v1.json
configs/e2r_census_depth_policy_v1.json
configs/e2r_census_stage_status_policy_v1.json
configs/e2r_census_sla_v1.json

Docs:
docs/operational/census_mode_v1_design.md
docs/operational/census_mode_v1_acceptance_report.md
docs/operational/census_mode_v1_stage_map_summary.md
docs/operational/census_mode_v1_universe_coverage.json
docs/operational/census_mode_v1_stage_distribution.json
docs/operational/census_mode_v1_source_gap_report.json
docs/operational/census_mode_v1_deep_backfill_plan.md
docs/operational/census_mode_v1_static_logic_audit.json
docs/operational/census_mode_v1_sla_report.json
docs/operational/census_mode_v1_watchlist_seed_report.md

================================================================================
4. Census 실행 모드
================================================================================

Census에는 네 가지 실행 모드를 둔다.

A. census_light
- 전체 universe cheap baseline scan
- LLM 최소 사용 또는 사용 없음
- official source / price / risk / existing ledger 중심
- 모든 종목에 Stage0/Stage1/ProviderPending/LightWatch 정도 부여
- 기본 전 시장 지도 생성

B. census_selective_deep
- census_light 결과에서 우선순위가 높은 종목만 Research Brain + SourceTask + Evidence OS deep 실행
- Stage2 이상 후보를 선별하기 위한 모드

C. census_full_deep_backfill_plan
- 실제 deep backfill 실행이 아니라 계획 생성
- 전체 universe를 sector/shard/budget으로 나눔
- 이번 Goal에서 full deep 실행은 금지
- 다음 Goal 후보로 남김

D. census_watchlist_update
- Census 결과에서 seed watchlist를 만든 뒤, daily trigger mode가 추적할 종목만 export

CLI 옵션:

PYTHONPATH=src python -m e2r.cli.run_e2r_census_mode \
  --as-of-date YYYY-MM-DD \
  --mode census_light|census_selective_deep \
  --universe krx \
  --output-root output/census/YYYY-MM-DD \
  --max-symbols 0 \
  --shard-count 1 \
  --shard-index 0 \
  --planner-provider real|none \
  --source-mode live_official_first \
  --depth-policy configs/e2r_census_depth_policy_v1.json \
  --fail-on-critical-audit true

규칙:
- --max-symbols 0 means full universe.
- production census mode에서 fixture symbol 금지.
- targeted_smoke_only 금지.
- top_results=None 금지.
- retry_max=None 금지.
- unbounded fetch 금지.
- source/provider failure는 Pending으로 남김.

================================================================================
5. Universe Builder
================================================================================

KRX universe를 안정적으로 만든다.

UniverseInstrument:

{
  "symbol": "...",
  "company_name": "...",
  "market": "KOSPI|KOSDAQ|KONEX",
  "instrument_type": "COMMON|PREFERRED|SPAC|ETF|REIT|ETN|OTHER",
  "is_active": true,
  "listing_status": "...",
  "large_sector_id": null,
  "sector_source": "KRX|internal_sector_map|unknown",
  "eligible_for_census": true,
  "exclusion_reason": null
}

기본 제외:
- ETF
- ETN
- SPAC
- REIT
- preferred shares
- delisted/inactive
- instruments without valid symbol/company mapping

단, excluded instrument도 count report에는 남긴다.

Reports:
docs/operational/census_mode_v1_universe_coverage.json

필수 지표:
- raw_universe_count
- eligible_common_stock_count
- excluded_etf_count
- excluded_spac_count
- excluded_reit_count
- excluded_preferred_count
- missing_sector_count
- active_market_breakdown
- sector_coverage_breakdown

Acceptance:
- actual KRX universe count > 1000
- eligible_common_stock_count > 1000
- fixture-like symbol count = 0
- missing company name count = 0 or explicitly reported
- every included symbol has market and eligibility status

Tests:
tests/test_census_universe_builder.py
tests/test_census_excludes_non_common_equity.py
tests/test_census_no_fixture_symbols.py

================================================================================
6. Baseline Scanner
================================================================================

모든 eligible symbol에 대해 cheap/light scan을 수행한다.

Input:
- UniverseInstrument
- as_of_date
- provider registry
- existing evidence ledger optional
- previous watchlist optional

Baseline sources:
1. KRX price / volume / relative strength
2. OpenDART recent disclosures
3. KIND/KRX risk flags
4. CompanyGuide / report/revision source if available
5. existing claim ledger and watchlist state
6. recent production trigger logs

BaselineScanResult:

{
  "symbol": "...",
  "as_of_date": "...",
  "scan_status": "SCANNED|PROVIDER_FAILED|PARTIAL|SKIPPED",
  "recent_disclosure_count": 0,
  "recent_supply_contract_count": 0,
  "recent_facility_investment_count": 0,
  "recent_earnings_event_count": 0,
  "recent_risk_event_count": 0,
  "revision_signal_count": 0,
  "price_anomaly_count": 0,
  "relative_strength_rank": null,
  "trading_value_rank": null,
  "existing_claim_count": 0,
  "existing_stage": null,
  "provider_errors": [],
  "reason_codes": [],
  "trigger_priority_score": 0.0
}

Rules:
- BaselineScanResult is not score evidence.
- Price anomaly only opens investigation.
- Recent official disclosure can create CandidateEvent but not score by itself until Evidence OS accepted.
- Existing claim ledger can be reused only if as_of_date/current lifecycle remains valid.

Acceptance:
- baseline scan attempts all eligible symbols.
- provider failures are counted per provider.
- no provider failure creates final low score.
- market anomaly does not create score contribution.
- reason_codes are traceable.

Tests:
tests/test_census_baseline_scanner.py
tests/test_census_market_anomaly_investigation_only.py
tests/test_census_provider_failure_pending.py

================================================================================
7. Depth Policy
================================================================================

전체 종목을 같은 깊이로 deep research하지 않는다.
DepthPolicy가 평가 깊이를 정한다.

Depth levels:
- L0_UNIVERSE_ONLY
  symbol/company/sector만 확인.
- L1_CHEAP_BASELINE
  price/risk/recent disclosure scan.
- L2_OFFICIAL_LIGHT
  recent official documents summary.
- L3_RESEARCH_BRAIN_TRIAGE
  Research Brain이 아키타입 후보와 missing primitive를 판단.
- L4_DEEP_DOSSIER
  SourceTask execution + Evidence OS accepted claims.
- L5_VERIFIED_STAGE
  deterministic scorer/stage court 완료.

DepthPolicy inputs:
- trigger_priority_score
- recent official event
- existing watchlist state
- existing accepted claim count
- source gap
- sector priority
- risk flag
- market anomaly
- previous pending state
- random audit sample quota

DepthPolicy output:
{
  "symbol": "...",
  "recommended_depth": "L1_CHEAP_BASELINE|L2_OFFICIAL_LIGHT|L3_RESEARCH_BRAIN_TRIAGE|L4_DEEP_DOSSIER|L5_VERIFIED_STAGE",
  "reason": "...",
  "expected_runtime_cost": "...",
  "source_task_budget": {},
  "llm_budget": {},
  "must_not_deepen_reason": null
}

Default:
- Most symbols end at L1/L2.
- Top priority symbols go to L3/L4.
- Existing watchlist/Pending symbols may go to L4/L5.
- High-risk flags go to L3/L4 risk review.
- Random sample per sector goes to L3/L4 for audit coverage.

Acceptance:
- every symbol has depth decision.
- total deep count is bounded.
- depth policy has sector quota.
- high-risk source flags are not ignored.
- low-signal symbols can be Stage0/NoCurrentCatalyst.

Tests:
tests/test_census_depth_policy.py
tests/test_census_deep_budget_bounded.py
tests/test_census_sector_sample_quota.py

================================================================================
8. Census Stage Classification Policy
================================================================================

Census stage는 Evidence OS StageCourt와 Census-specific status를 결합한다.

Rules:

1. No evidence / no current event:
   - base_stage = Stage0
   - investigation_status = NO_CURRENT_CATALYST
   - score_valid_status = NO_CURRENT_EVENT
   - verified_score = null

2. Cheap/market-only signal:
   - base_stage = Stage1 or Stage2-Watch depending on policy
   - score evidence 없음
   - trigger_priority_score만 있음
   - verified_score = null

3. Official single claim but no bridge:
   - base_stage = Stage1 or Stage2-Watch
   - verified_score may be low if deterministic scorer supports it
   - missing primitives explicit

4. Strong accepted claim + bridge:
   - Stage2-Actionable or higher via deterministic scorer / StageCourt

5. Score high but Green primitive missing:
   - Stage3-Yellow-Pending
   - failed green gates explicit

6. Provider failure on material source:
   - ProviderPending
   - final low score 금지

7. Existing hard break current OPEN:
   - Reject/Red or 4C overlay only if current direct source-backed hard break claim exists

8. Historical risk only:
   - historical/follow-up
   - no current penalty

9. Source exhausted:
   - EvidenceInsufficient or FINAL_WITH_NONMATERIAL_GAPS depending materiality

Acceptance:
- no accepted claim => no nonzero verified_score.
- no current event => Stage0 allowed.
- provider failure => ProviderPending.
- market anomaly only => no verified_score.
- CensusStageStatus always has assessment_depth and stage_confidence.

Tests:
tests/test_census_stage_policy.py
tests/test_census_no_event_stage0.py
tests/test_census_no_claim_no_score.py
tests/test_census_provider_pending_not_red.py

================================================================================
9. Research Brain Triage in Census
================================================================================

Research Brain은 모든 종목에 full LLM planning을 하지 않는다.
DepthPolicy가 L3 이상으로 올린 종목만 Research Brain을 호출한다.

Research Brain input:
- CensusAssessmentEvent
- BaselineScanResult
- recent CandidateEvents
- existing claims
- sector profile
- ArchetypeMemoryCards
- trigger taxonomy

Research Brain output:
- top_k_archetype_hypotheses
- positive thesis
- counter thesis
- must_verify_primitives
- red_team_checks
- SourceTask drafts
- do_not_promote_reasons
- confidence

금지:
- score output
- stage output
- hard_break final
- current_score_eligible
- FeatureInput mutation
- ScoreContribution mutation

Census-specific:
- If no recent event and no existing claim, Research Brain may return:
  “No current E2R thesis; keep Stage0.”
- If market anomaly only, Research Brain returns investigation tasks, not score.
- If existing watchlist thesis exists, Research Brain can create follow-up tasks.

Acceptance:
- Research Brain called only within budget.
- Research Brain output score/stage key count = 0.
- Research Brain no-current-thesis path supported.
- R13 overroute count tracked.
- Low confidence becomes ArchetypePending, not false Stage.

Tests:
tests/test_census_research_brain_triage.py
tests/test_census_research_brain_budget.py
tests/test_census_no_current_thesis_path.py

================================================================================
10. SourceTask in Census
================================================================================

Census SourceTask는 depth와 materiality에 따라 제한된다.

SourceTask classes:
- official_light_task
- deep_dossier_task
- risk_followup_task
- provider_repair_task
- existing_claim_lifecycle_task
- green_closure_task
- random_audit_task

Rules:
- FCF/cash/revision/contract/backlog gaps use official/structured source first.
- general web is off by default.
- TrustedNews fallback only when SourceTask explicitly allows.
- IssuerIR optional; failure becomes ProviderPending or SourceGap, not final score.
- No task without budget.
- stop-on-resolution.

Census SourceTaskExecution:
{
  "task_id": "...",
  "symbol": "...",
  "depth_level": "...",
  "source_class": "...",
  "status": "NOT_STARTED|FETCHED|PARSED|EVIDENCE_OS_ACCEPTED|NO_EVIDENCE_FOUND|PROVIDER_FAILED|BUDGET_EXHAUSTED|SKIPPED_BY_DEPTH_POLICY",
  "accepted_claim_ids": [],
  "provider_errors": [],
  "budget_used": {},
  "stop_reason": "..."
}

Acceptance:
- source_task_without_budget_count = 0
- source_task_executed_for_L1_only_count = 0 unless random audit
- accepted_claim_without_source_task_count = 0
- provider_failed_final_score_count = 0
- unbounded general search count = 0

Tests:
tests/test_census_source_tasks.py
tests/test_census_no_unbounded_source_task.py
tests/test_census_stop_on_resolution.py

================================================================================
11. Claim Ledger Reuse / Lifecycle Refresh
================================================================================

Census should reuse prior accepted claims only if they remain current.

ExistingClaimReusePolicy:
- accepted claim can be reused if:
  - same symbol/target
  - as_of_date within freshness policy
  - not superseded
  - not contradicted
  - lifecycle still CURRENT/OPEN as appropriate
  - source still valid
- stale claim becomes HistoricalOnly or NeedsRefresh.
- old risk claim needs current OPEN follow-up before scoring.
- existing watchlist stage must be refreshed, not blindly copied.

ClaimReuseResult:
{
  "claim_id": "...",
  "reuse_status": "REUSED_CURRENT|STALE_NEEDS_REFRESH|SUPERSEDED|CONTRADICTED|REJECTED_SCOPE|UNKNOWN",
  "reason": "...",
  "followup_task_id": null
}

Acceptance:
- stale claim reused as current count = 0
- old risk current penalty without follow-up count = 0
- reused claim has lifecycle trace
- previous Stage not blindly copied

Tests:
tests/test_census_claim_reuse_lifecycle.py
tests/test_census_old_risk_not_reused.py
tests/test_census_stage_not_blindly_copied.py

================================================================================
12. Sharding / Checkpoint / Resume
================================================================================

Full universe Census must be resumable.

Implement:
- shard planner
- checkpoint store
- per-shard output
- failed shard retry
- idempotent rerun
- deterministic result under same source snapshot

Shard key:
- symbol hash or sector/market partition

Checkpoint:
{
  "run_id": "...",
  "as_of_date": "...",
  "shard_count": 10,
  "shard_index": 0,
  "started_at": "...",
  "completed_at": "...",
  "processed_symbols": [],
  "failed_symbols": [],
  "pending_symbols": [],
  "source_corpus_hash": "...",
  "config_hash": "..."
}

Acceptance:
- interrupted run can resume.
- same shard rerun does not duplicate claims.
- shard outputs merge deterministically.
- full universe output can be built from shard outputs.
- checkpoint includes source/config hashes.

Tests:
tests/test_census_sharding.py
tests/test_census_checkpoint_resume.py
tests/test_census_idempotent_rerun.py
tests/test_census_shard_merge.py

================================================================================
13. Census Output Artifacts
================================================================================

Output directory:

output/census/YYYY-MM-DD/
  run_metadata.json
  universe.jsonl
  census_assessment_events.jsonl
  baseline_scan_results.jsonl
  depth_decisions.jsonl
  research_brain_plans.jsonl
  source_tasks.jsonl
  source_task_executions.jsonl
  evidence_documents.jsonl
  evidence_anchors.jsonl
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
  operator_digest.md
  audit_summary.json

Docs:
docs/operational/census_mode_v1_acceptance_report.md
docs/operational/census_mode_v1_stage_map_summary.md
docs/operational/census_mode_v1_universe_coverage.json
docs/operational/census_mode_v1_sector_stage_distribution.json
docs/operational/census_mode_v1_provider_gap_report.json
docs/operational/census_mode_v1_source_gap_report.json
docs/operational/census_mode_v1_watchlist_seed_report.md

census_stage_map.csv columns:
- symbol
- company_name
- market
- large_sector_id
- census_status
- assessment_depth
- base_stage
- investigation_status
- transition_overlay
- stage_confidence
- score_valid_status
- trigger_priority_score
- verified_score
- provisional_score
- score_interval_lower
- score_interval_upper
- accepted_claim_count
- score_contribution_count
- recent_event_count
- primary_archetype
- failed_stage_gates
- missing_primitives
- provider_gaps
- source_gaps
- next_actions

================================================================================
14. Stage Map Summary
================================================================================

Census summary must show:

Global:
- total_universe_count
- eligible_symbol_count
- scanned_symbol_count
- completed_symbol_count
- failed_symbol_count
- provider_pending_count
- runtime_pending_count
- no_current_catalyst_count
- stage0_count
- stage1_count
- stage2_watch_count
- stage2_actionable_count
- yellow_pending_count
- green_count
- reject_red_count
- risk_review_count
- verified_score_count
- no_score_count
- accepted_claim_total
- score_contribution_total
- orphan_score_count
- source_proxy_to_score_count

By sector:
- eligible count
- scanned count
- Stage distribution
- ProviderPending count
- SourceGap count
- DeepDossier count
- Stage2+ count
- accepted claim count

By provider:
- fetch success/failure
- provider pending
- source gap
- score claim contribution count

By depth:
- L0/L1/L2/L3/L4/L5 counts
- average runtime
- average source tasks
- accepted claim yield

Acceptance:
- every eligible symbol appears exactly once in census_stage_map.
- counts reconcile.
- no duplicate symbols.
- no missing StageStatus for eligible symbols.
- no orphan score.
- no source_proxy_to_score.

================================================================================
15. Watchlist Seed Export
================================================================================

Census 결과에서 daily 운영으로 넘길 seed watchlist를 생성한다.

WatchlistSeed categories:
- Green
- Yellow-Pending
- Stage2-Actionable
- Stage2-Watch with high priority
- ProviderPending high value
- RiskReview
- Random audit sample

WatchlistSeedItem:
{
  "symbol": "...",
  "company_name": "...",
  "as_of_date": "...",
  "seed_reason": "...",
  "base_stage": "...",
  "score_status": "...",
  "primary_archetype": "...",
  "accepted_claim_ids": [],
  "missing_primitives": [],
  "next_actions": [],
  "refresh_frequency": "daily|weekly|on_event",
  "source_followup_tasks": []
}

Rules:
- No buy/sell language.
- Green/Yellow/Stage2 seeds require supporting claim IDs or explicit pending reason.
- ProviderPending seeds require provider/source gap reason.
- Stage0 no-catalyst does not enter watchlist seed unless random audit.

Output:
output/census/YYYY-MM-DD/watchlist_seed_candidates.json
docs/operational/census_mode_v1_watchlist_seed_report.md

Tests:
tests/test_census_watchlist_seed_export.py

================================================================================
16. Census Static Logic Audit
================================================================================

Implement:
src/e2r/cli/audit_e2r_census_mode.py

Critical counts:
- eligible_symbol_missing_stage_status_count
- duplicate_symbol_stage_status_count
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
- stage_without_confidence_count
- no_current_event_marked_red_count
- source_pending_marked_red_count
- unbounded_fetch_config_count
- checkpoint_missing_hash_count
- shard_merge_duplicate_count
- report_head_sha_mismatch_count
- one_line_large_report_count

All critical counts must be 0.

Warnings:
- provider gap rate high
- accepted claim yield low
- too many Stage1 rows
- sector coverage missing
- LLM budget exhausted
- deep dossier count too low
- no Green/Yellow found
- too many NoCurrentCatalyst rows

Reports:
docs/operational/census_mode_v1_static_logic_audit.json

================================================================================
17. SLA / Budget
================================================================================

Census must finish.

Config:
configs/e2r_census_sla_v1.json

Required settings:
- max_total_runtime_seconds
- max_symbol_runtime_seconds
- max_deep_symbols
- max_llm_calls
- max_source_tasks_total
- max_source_tasks_per_symbol
- max_fetches_per_task
- max_provider_failures_before_circuit_breaker
- max_retry_count
- no top_results=None
- no retry_max=None

Runtime states:
- COMPLETE
- PARTIAL_WITH_PENDING
- RUNTIME_BUDGET_EXHAUSTED
- PROVIDER_CIRCUIT_OPEN

Rules:
- budget exhausted symbol becomes RuntimeBudgetPending.
- no final reject on runtime budget failure.
- partial run can still produce partial Census with status PARTIAL_WITH_PENDING.
- full acceptance requires configured coverage threshold.

Reports:
docs/operational/census_mode_v1_sla_report.json

Tests:
tests/test_census_sla_budget.py
tests/test_census_runtime_budget_pending.py
tests/test_census_provider_circuit_breaker.py

================================================================================
18. Full Universe Acceptance Levels
================================================================================

Define labels:

- IMPLEMENTATION_MERGED
- CENSUS_LIGHT_PASS
- CENSUS_SELECTIVE_DEEP_PASS
- FULL_UNIVERSE_STAGE_MAP_PASS
- WATCHLIST_SEED_PASS
- CENSUS_STATIC_AUDIT_PASS
- CENSUS_SLA_PASS
- READY_FOR_DEEP_BACKFILL_DESIGN
- READY_FOR_DAILY_TRIGGER_INTEGRATION

Goal completion minimum:
- CENSUS_LIGHT_PASS
- FULL_UNIVERSE_STAGE_MAP_PASS
- CENSUS_STATIC_AUDIT_PASS
- CENSUS_SLA_PASS
- WATCHLIST_SEED_PASS

CENSUS_LIGHT_PASS:
- actual eligible universe > 1000
- every eligible symbol has CensusStageStatus
- no duplicate/missing symbols
- no claimless nonzero score
- no provider failure final reject
- Stage0/NoCurrentCatalyst supported

CENSUS_SELECTIVE_DEEP_PASS:
- Research Brain called for bounded prioritized set
- source tasks executed for deep set
- Evidence OS accepted claims generated where available
- deterministic stage output generated for deep set
- pending/source gaps explicit

FULL_UNIVERSE_STAGE_MAP_PASS:
- census_stage_map.csv/jsonl generated
- all eligible symbols represented
- global/sector/provider/depth distributions generated
- stage confidence present for all rows
- source gaps and provider gaps visible

WATCHLIST_SEED_PASS:
- watchlist_seed_candidates.json generated
- daily trigger mode can consume seeds
- every seed has reason and next_action

READY_FOR_DEEP_BACKFILL_DESIGN:
- shard/backfill plan generated
- top source gaps identified
- deep backlog prioritized by sector/archetype/stage

READY_FOR_DAILY_TRIGGER_INTEGRATION:
- Census output can feed daily trigger watchlist
- previous StageStatus and claim ledger can be reused with lifecycle refresh

================================================================================
19. Required Tests
================================================================================

Add or strengthen:

tests/test_census_assessment_event.py
tests/test_census_universe_builder.py
tests/test_census_excludes_non_common_equity.py
tests/test_census_baseline_scanner.py
tests/test_census_depth_policy.py
tests/test_census_stage_policy.py
tests/test_census_research_brain_triage.py
tests/test_census_source_tasks.py
tests/test_census_claim_reuse_lifecycle.py
tests/test_census_sharding.py
tests/test_census_checkpoint_resume.py
tests/test_census_shard_merge.py
tests/test_census_watchlist_seed_export.py
tests/test_census_static_logic_audit.py
tests/test_census_sla_budget.py
tests/test_census_no_claim_no_score.py
tests/test_census_no_current_event_stage0.py
tests/test_census_provider_pending_not_red.py
tests/test_census_market_anomaly_not_score.py
tests/test_census_full_universe_stage_map.py

Full command:
PYTHONPATH=src python -m unittest discover -s tests -v

No skipped Census tests allowed unless explicitly marked as future Deep Backfill, and skipped tests cannot be required for Goal completion.

================================================================================
20. Required Reports
================================================================================

Generate:

docs/operational/census_mode_v1_design.md
docs/operational/census_mode_v1_acceptance_report.md
docs/operational/census_mode_v1_universe_coverage.json
docs/operational/census_mode_v1_stage_map_summary.md
docs/operational/census_mode_v1_sector_stage_distribution.json
docs/operational/census_mode_v1_provider_gap_report.json
docs/operational/census_mode_v1_source_gap_report.json
docs/operational/census_mode_v1_watchlist_seed_report.md
docs/operational/census_mode_v1_static_logic_audit.json
docs/operational/census_mode_v1_sla_report.json
docs/operational/census_mode_v1_deep_backfill_plan.md
docs/operational/census_mode_v1_readiness_verdict.md

Output:

output/census/YYYY-MM-DD/
  run_metadata.json
  universe.jsonl
  census_assessment_events.jsonl
  baseline_scan_results.jsonl
  depth_decisions.jsonl
  research_brain_plans.jsonl
  source_tasks.jsonl
  source_task_executions.jsonl
  evidence_documents.jsonl
  evidence_anchors.jsonl
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
  operator_digest.md
  audit_summary.json

================================================================================
21. Acceptance Report Format
================================================================================

docs/operational/census_mode_v1_acceptance_report.md must include:

1. Final status
2. Commit SHA / message / push status / working tree
3. Test command and pass/fail/skip
4. Production Cutover prerequisite status
5. Universe coverage
6. Census mode command
7. Config/source/candidate/evidence/scoring/stage hashes
8. Eligible symbol count
9. Scanned symbol count
10. CensusStageStatus count
11. Missing/duplicate symbol count
12. Stage distribution
13. Sector distribution
14. Depth distribution
15. Provider gap summary
16. Source gap summary
17. Accepted claim count
18. Score contribution count
19. Orphan score count
20. Source_proxy_to_score count
21. Provider_failed_final_score count
22. NoCurrentCatalyst count
23. Watchlist seed count
24. Runtime/SLA summary
25. Static audit critical counts
26. Census readiness verdict
27. Deep backfill readiness
28. Daily trigger integration readiness
29. Remaining blockers

================================================================================
22. Census Readiness Verdict
================================================================================

Create:
docs/operational/census_mode_v1_readiness_verdict.md

Possible verdicts:
- NOT_READY
- CENSUS_LIGHT_READY
- FULL_UNIVERSE_STAGE_MAP_READY
- READY_FOR_DEEP_BACKFILL_DESIGN
- READY_FOR_DAILY_TRIGGER_INTEGRATION

Rules:
- FULL_UNIVERSE_STAGE_MAP_READY requires every eligible symbol represented exactly once.
- READY_FOR_DAILY_TRIGGER_INTEGRATION requires watchlist seed export pass.
- READY_FOR_DEEP_BACKFILL_DESIGN requires deep backfill plan generated.
- If provider gap is high, verdict may still be FULL_UNIVERSE_STAGE_MAP_READY if ProviderPending rows are explicit and no false score is created.
- If missing symbols exist, verdict cannot exceed NOT_READY.
- If claimless nonzero scores exist, verdict NOT_READY.
- If provider failure became Red/Reject, verdict NOT_READY.

================================================================================
23. Deep Backfill Plan
================================================================================

Do not implement full deep backfill execution in this Goal.
Generate the plan.

DeepBackfillPlan:
- shard count
- sector priority
- archetype priority
- provider gap priority
- pending symbol list
- Stage2+ candidate list
- source-heavy candidate list
- expected runtime
- expected LLM calls
- expected provider calls
- checkpoint strategy
- resume strategy

Backfill priority:
1. Stage2-Actionable / Yellow-Pending with missing Green bridge
2. ProviderPending high trigger priority
3. source gap sectors
4. Stage2-Watch high market anomaly
5. random sector audit sample
6. C24/C28/C17 source-proxy ontology sectors where URL repair needed

Output:
docs/operational/census_mode_v1_deep_backfill_plan.md
output/census/YYYY-MM-DD/deep_backfill_plan.json

================================================================================
24. Operator Digest
================================================================================

Generate human-facing Census digest.

output/census/YYYY-MM-DD/operator_digest.md

Sections:
- 전체 요약
- Stage3-Green
- Stage3-Yellow-Pending
- Stage2-Actionable
- Stage2-Watch
- Provider/Source Pending
- RiskReview / Reject
- NoCurrentCatalyst summary
- Top source gaps
- Sector heatmap
- Watchlist seed
- Deep backfill candidates

No buy/sell language.

Each watch item must show:
- why it appears
- stage
- evidence depth
- accepted claims
- missing primitives
- next action

Next actions:
- WATCH
- INVESTIGATE
- RECHECK_SOURCE
- RISK_REVIEW
- IGNORE
- PROVIDER_WAIT
- DEEP_BACKFILL
- DAILY_TRIGGER_TRACK

================================================================================
25. Prohibitions
================================================================================

- Do not call this a recommendation engine.
- Do not output buy/sell language.
- Do not force score on every ticker.
- Do not mark no-event symbols as Red.
- Do not mark provider failure as Red.
- Do not use cheap_scan_total_score as verified_score.
- Do not score CensusAssessmentEvent.
- Do not score market anomaly.
- Do not score source_proxy_only/evidence_url_pending/price_path_only memory.
- Do not use future MFE/MAE in current Census scoring.
- Do not reuse old claim without lifecycle refresh.
- Do not run unbounded general web search for every ticker.
- Do not run deep LLM investigation for all tickers by default.
- Do not skip shard/checkpoint.
- Do not hide source gaps.
- Do not produce one-line huge reports.
- Do not change scoring weights or Stage thresholds.
- Do not hardcode symbol/company/url exceptions.

================================================================================
26. Final Answer Format
================================================================================

After completion, report only:

1. Final status
- IMPLEMENTATION_MERGED / CENSUS_LIGHT_PASS / CENSUS_SELECTIVE_DEEP_PASS / FULL_UNIVERSE_STAGE_MAP_PASS / WATCHLIST_SEED_PASS / CENSUS_STATIC_AUDIT_PASS / CENSUS_SLA_PASS / READY_FOR_DEEP_BACKFILL_DESIGN / READY_FOR_DAILY_TRIGGER_INTEGRATION

2. Commit
- SHA
- message
- push status
- working tree clean

3. Tests
- command
- passed / failed / skipped

4. Universe
- raw universe count
- eligible symbol count
- excluded counts
- missing sector count

5. Census coverage
- scanned count
- status count
- missing/duplicate count
- shard count

6. Stage distribution
- Stage0
- Stage1
- Stage2-Watch
- Stage2-Actionable
- Yellow-Pending
- Green
- Reject/Red
- ProviderPending
- NoCurrentCatalyst

7. Evidence / score
- accepted claim count
- score contribution count
- orphan score count
- source_proxy_to_score count
- claimless nonzero score count

8. Provider/source gaps
- provider pending count
- source gap count
- top blocker providers
- top blocker sectors

9. Watchlist seed
- seed count
- category counts
- next action counts

10. SLA
- total runtime
- deep count
- LLM calls
- source calls
- runtime pending count

11. Deep backfill plan
- generated yes/no
- shard count
- top sectors
- top source gaps

12. Final verdict
- NOT_READY / CENSUS_LIGHT_READY / FULL_UNIVERSE_STAGE_MAP_READY / READY_FOR_DEEP_BACKFILL_DESIGN / READY_FOR_DAILY_TRIGGER_INTEGRATION
- blockers
- exact next step

================================================================================
27. One-line goal
================================================================================

Census Mode v1의 목표는:

“모든 티커를 억지로 깊게 분석해 점수를 주는 것”이 아니라,
전체 KRX universe에 대해 현재 E2R 상태, 판단 깊이, source gap, 다음 action을 붙인 Stage 지도를 만드는 것이다.

즉:

전체 시장
→ CensusAssessmentEvent
→ cheap baseline
→ 필요한 종목만 Research Brain / Evidence OS deep
→ Stage0~Green / ProviderPending / NoCurrentCatalyst 분류
→ watchlist seed와 deep backfill plan 생성

이 경로를 완성하라.