너는 Daikisong/stock_agent 레포의 E2R Research Brain v3 / True Production Shadow Run을 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 READY 상태로 유지되어야 한다.
- Research Brain v1/v2는 구현되어 있다.
- 그러나 v2는 아직 실제 production 운영이 아니라 shadow scaffold다.
- v2 report의 READY_FOR_SHADOW_DAILY_RUN은 PRODUCTION_READY가 아니다.
- 이번 작업은 실제 daily 운영 플로우를 따라 “시장 이벤트 → LLM/Research Brain 라우팅 → SourceTask 실제 실행 → Evidence OS accepted claim → deterministic scorer/stage → daily watchlist”를 닫는 것이다.

최종 목표:
Research Brain이 과거 연구 MemoryCard를 참고해 현재 CandidateEvent의 아키타입과 조사계획을 만들고,
SourceTask가 실제 source acquisition을 수행하며,
Evidence OS v2가 실제 EvidenceDocument/EvidenceAnchor/AdmissibleClaim을 생성하고,
기존 deterministic scorer와 StageCourt가 claim-backed score/stage를 산출하는 production shadow daily pipeline을 완성하라.

절대 원칙:
1. Research Brain은 score/stage를 직접 계산하지 않는다.
2. Research Brain output은 FeatureInput, ScoreContribution, risk field를 직접 mutate하지 않는다.
3. Evidence OS accepted claim 없이 verified_score 상승 금지.
4. Watchlist score는 cheap_scan_total_score가 아니라 deterministic scorer 결과여야 한다.
5. SourceTask execution은 local evidence id를 accepted claim으로 가정하면 안 된다.
6. A2 source quality는 실제 URL/snapshot/anchor/date/entity/primitive replay를 통과해야 한다.
7. CandidateEvent dry run은 특정 캐시 파일/삼성전자 샘플에 의존하면 안 된다.
8. LLM Planner가 실제로 event semantics와 MemoryCard를 읽어 top-k archetype을 제안해야 한다.
9. deterministic router는 fallback/safety rail이고, 운영 primary brain이 아니다.
10. AGENTS.md의 research-mode 넓은 수집과 production-mode bounded 수집을 분리하라.

================================================================================
1. 현재 v2 한계 명시 및 재라벨링
================================================================================

다음 상태를 문서화하라.

- Research Brain v2는 READY_FOR_SHADOW_DAILY_RUN이지 PRODUCTION_READY가 아니다.
- v2 acceptance의 candidate_event_count 60은 sector coverage가 L2 59 / L6 1로 치우쳐 있다.
- v2 source execution accepted claims는 local evidence handoff 기반이며, 실제 Evidence OS full acceptance path가 아니다.
- v2 watchlist verified_score는 cheap_scan_total_score 기반 preview이며 deterministic E2R score가 아니다.
- v2 A2 source-quality sample은 실제 200개 URL replay를 완전히 의미하지 않는다.
- v2 LLM planner는 schema/payload validation hook이며 real provider planning run이 아니다.
- v2 router fixtures는 archetype id가 포함된 fixture이므로 raw market event routing 검증이 부족하다.

생성:
docs/operational/research_brain_v2_shadow_limitations.md

이 문서는 기존 v2 report를 부정하는 게 아니라, “v2가 어디까지 검증했고 어디서부터 v3가 필요한지”를 명확히 해야 한다.

================================================================================
2. Real LLM Planner integration
================================================================================

현재 v2_llm_planner.py는 schema validation 중심이다.
실제 PlannerProvider를 구현하라.

추가/수정:
src/e2r/research_brain/v3_llm_planner_provider.py

필수 인터페이스:

class ResearchBrainPlannerProvider:
    def plan(
        self,
        event: CandidateEventV2,
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_summary: Mapping[str, Any] | None = None,
    ) -> LLMPlannerOutputV2:
        ...

구현:
- Codex/OpenAI provider adapter 또는 기존 LLM provider infrastructure 재사용
- Fake provider는 tests 전용
- production/shadow run에서 fake provider 사용 여부를 명확히 기록
- provider_error는 candidate investigation_status=PROVIDER_FAILED/PENDING으로 처리
- provider가 없는데 deterministic router로 몰래 대체하고 READY를 주지 마라

LLM Planner prompt:
입력:
- CandidateEventV2
- top relevant ArchetypeMemoryCards
- source route policy
- forbidden output keys
- current as_of_date
- source gap warnings

금지 입력:
- future MFE/MAE
- outcome label
- expected stage
- score threshold
- “Green을 열어야 한다” 같은 목적성 문장

출력:
- top_k_archetype_hypotheses
- positive_thesis
- counter_thesis
- must_verify_primitives
- red_team_checks
- source_task_drafts
- query_intents
- do_not_promote_reasons
- planner_self_check

금지 출력:
- score
- stage
- hard_break final
- current_score_eligible
- verified final

검증:
- LLM output schema validation
- score/stage keys 발견 시 reject
- unknown archetype reject
- R13 primary는 explicit red-team event일 때만 허용
- LLM이 source task에 budget을 안 주면 validator가 보완 또는 reject
- FCF/DART-solvable gap을 general web으로 보내면 reject

필수 테스트:
tests/test_research_brain_v3_real_planner_provider.py
tests/test_research_brain_v3_planner_provider_failure.py
tests/test_research_brain_v3_no_fake_provider_production_ready.py

================================================================================
3. Raw Market Event Routing Fixtures
================================================================================

기존 v2 router fixtures는 정답 archetype id가 event에 들어가 있어 과하게 쉬웠다.
새 raw fixture set을 만들어라.

생성:
fixtures/research_brain_v3/raw_event_routing/*.jsonl

각 fixture는 실제 운영형 사건 문장만 포함한다.
정답 archetype id는 expected field에만 있고, event_summary/raw_reason_codes에는 넣지 않는다.

필수 raw fixture:
- C06 HBM:
  “HBM 매출 비중 확대, capacity sold out, customer allocation”
- C08 test socket:
  “삼성전자향 테스트소켓 공급, VIP 고객 매출 비중, 제품 profile only”
- C15 material spread:
  “인쇄용지 판가 15% 인상, 펄프가격 상승, pass-through”
- C17 chemical spread:
  “BD spread 개선, 제품 ASP, OPM 개선”
- C24 bio:
  “임상 2상 endpoint 발표, CRL, partner/funding runway”
- C28 software/security:
  “보안관제 계약, ARR/RPO/renewal, security theme only”
- C03 defense/export:
  “방산 수출계약, 납기, backlog”
- C10 orderbook:
  “수주잔고 급증, 매출인식 schedule”
- R13 explicit:
  “cross-archetype false positive review”
- wrong route adversarial:
  HBM substrate sympathy should not route as direct C06 capacity
  security keyword only should not route as C28 Actionable
  raw commodity headline should not route as C15 Actionable without pass-through

Acceptance:
- raw fixture top1 accuracy >= 85%
- raw fixture top3 accuracy >= 98%
- mandatory C06/C08/C15/C17/C24/C28 top1 exact
- R13 overroute = 0
- R13 overlay allowed but not primary unless explicit R13
- low confidence emits ARCTYPE_PENDING_DISAMBIGUATION

생성:
docs/operational/research_brain_v3_raw_event_router_matrix.json

================================================================================
4. Real SourceTask Execution
================================================================================

현재 execute_source_tasks_from_local_evidence는 initial_evidence_document_ids가 있으면 accepted claim을 가정한다.
이것을 production shadow mode에서 금지하라.

새 경로:
SourceTask
→ SourceAcquisitionRunner
→ EvidenceDocument
→ EvidenceAnchor
→ Evidence OS v2 workflow
→ accepted AdmissibleClaim
→ SourceTaskExecution

필수 구현:
src/e2r/research_brain/v3_source_acquisition_runner.py
src/e2r/research_brain/v3_evidence_os_execution_bridge.py

지원 source:
- DART/OpenDART detail/document
- KIND/KRX
- CompanyGuide/revision if available
- existing OfficialFollowUpSourceProvider
- IR/report snapshot store
- trusted news only as fallback
- general web only when source task allows it

SourceTaskExecutionV3:
{
  "task_id": "...",
  "source_task": {...},
  "status": "FETCHED|PARSED|EVIDENCE_OS_ACCEPTED|NO_EVIDENCE_FOUND|PROVIDER_FAILED|BUDGET_EXHAUSTED|REJECTED_BY_POLICY",
  "fetched_document_ids": [],
  "evidence_anchor_ids": [],
  "raw_assertion_ids": [],
  "adjudicated_claim_ids": [],
  "accepted_claim_ids": [],
  "rejected_claim_ids": [],
  "not_eligible_reasons": [],
  "provider_errors": [],
  "budget_used": {},
  "stop_reason": "..."
}

금지:
- initial_evidence_document_ids만으로 accepted_claim 생성
- deterministic_claim_id_v2로 fake accepted claim 생성
- source_task_to_score_contribution_count를 항상 0으로 두는 audit
- source task planning만으로 executed 처리
- local handoff accepted status를 Evidence OS accepted로 표현

Acceptance:
- SourceTaskExecutionV3 accepted claim은 Evidence OS ledger에 실제 존재해야 한다.
- accepted claim마다 source_url 또는 API/table anchor가 있어야 한다.
- source task accepted_claim_count와 Evidence OS accepted_claim_count가 일치해야 한다.
- accepted claim 0개면 score contribution 0.
- provider failure material gap이면 score_valid=PENDING/PROVIDER_FAILED.

테스트:
tests/test_research_brain_v3_real_source_task_execution.py
tests/test_research_brain_v3_source_task_to_evidence_os_ledger.py
tests/test_research_brain_v3_no_local_handoff_fake_claims.py

================================================================================
5. Watchlist score를 real scorer로 연결
================================================================================

현재 DailyWatchlistItem의 verified_score는 cheap_scan_total_score preview다.
이것을 제거하거나 preview_score로 분리하라.

새 구분:
- trigger_priority_score: cheap_scan / candidate triage용
- provisional_score: 미검증 claim 포함 investigation priority용
- verified_score: deterministic scorer가 Evidence OS accepted claims로 계산한 점수
- score_interval: unresolved material gaps 반영
- score_valid_status

Watchlist에 들어갈 Stage는 반드시 StageCourt 결과여야 한다.

Flow:
accepted_claims
→ PrimitiveState
→ ScoreContributionLedger
→ DeterministicScorer
→ StageCourt
→ DailyWatchlistItem

금지:
- cheap_scan_total_score를 verified_score로 사용
- `_base_stage(score >= 85 / 55 / 20)` 같은 임시 stage mapping을 production shadow report에 사용
- accepted_claim_ids가 있다는 이유만으로 score를 숫자로 채움

필수 출력:
DailyWatchlistItem:
- trigger_priority_score
- verified_score
- provisional_score
- score_interval_lower/upper
- score_valid_status
- base_stage
- investigation_status
- transition_overlay
- accepted_claim_ids
- score_contribution_ids
- failed_stage_gates
- green_blockers
- red_team_checks
- source_task_status_summary
- follow_up_tasks

테스트:
tests/test_research_brain_v3_watchlist_uses_real_scorer.py
tests/test_research_brain_v3_cheap_scan_score_not_verified_score.py
tests/test_research_brain_v3_stagecourt_integration.py

================================================================================
6. Production Discovery를 실제 daily scan으로 실행
================================================================================

현재 v2 default candidates path는 특정 output cache에 의존한다.
v3는 실제 daily scan / morning pipeline / report radar / official scan을 실행해야 한다.

새 entrypoint:
src/e2r/cli/run_research_brain_v3_daily_shadow.py

입력:
--as-of-date
--universe-limit optional
--sector-min-events 3
--candidate-event-min-count 30
--output-dir
--fixture-mode / --live-mode / --frozen-mode
--planner-provider real|fake|none
--source-acquisition live|snapshot|frozen

Flow:
1. KRX universe
2. cheap_scan official sources
3. report_radar
4. CompanyGuide/revision if available
5. DART/KIND/KRX events
6. price/volume anomaly
7. CandidateEventV2 생성
8. CandidateCluster 생성
9. LLM Planner + deterministic router comparison
10. SourceTask 생성
11. SourceTask actual execution
12. Evidence OS accepted claims
13. Deterministic score/stage
14. Daily watchlist

Acceptance:
- targeted_smoke_only=False
- hardcoded candidate cache path 사용 금지
- candidate_event_count >= 30 or explicit provider/market gap
- each large sector >= 3 attempts or explicit source gap
- at least 20 events routed
- at least 10 events with executed source tasks
- at least 5 events with Evidence OS accepted claims
- at least 3 events with real deterministic score/stage
- report records source/provider gaps honestly

테스트:
tests/test_research_brain_v3_daily_shadow_entrypoint.py
tests/test_research_brain_v3_no_default_cached_candidates.py
tests/test_research_brain_v3_sector_coverage_requirements.py

================================================================================
7. Source quality A2 실제 검증
================================================================================

현재 A2는 sample count와 Evidence OS ready flag로 생성된다.
v3에서는 A2가 실제 URL/snapshot/anchor/Evidence OS replay를 통과해야 한다.

A2 promotion pipeline:
A1/A0/B queue
→ fetch or use snapshot
→ source date verify
→ EvidenceAnchor generate
→ target directness verify
→ primitive mapping accepted
→ Evidence OS replay pass
→ A2 promotion

필수:
- A2 promotion records include source_url/document_id/anchor_id/claim_id
- A2 failed rows include failure reason
- A2 sample pass is not derived from evidence_os_ready flag
- repair queue persists unresolved URLs
- source_proxy_only cannot enter A2

Run requirement:
- at least 500 A1/A0/B rows attempted
- at least 100 actual A2 promotions or honest source/provider gap
- C06/C08/C15 URL-backed rows prioritized
- C24/C28/C17 source_proxy rows remain C unless URL repaired

Reports:
docs/operational/research_brain_v3_source_quality_promotion_report.json
docs/operational/research_brain_v3_url_repair_failures.json
docs/operational/research_brain_v3_a2_promoted_claims_sample.json

================================================================================
8. MemoryCard 자동증류 강화
================================================================================

현재 일부 MemoryCard는 semantic override에 의존한다.
v3에서는 override를 seed로만 쓰고, 실제 memory record 기반 distillation 결과를 별도로 생성하라.

ArchetypeMemoryCardV3:
- seed_rules
- data_distilled_rules
- conflict_summary
- source_quality_weighted_patterns
- URL-backed supporting records
- source_proxy supporting records
- price-path-only warning records
- source_gap
- confidence
- last_compiled_at
- compile_input_hash

Distillation:
- URL-backed A2/A1 rows weighted high
- source_proxy ontology rows weighted low and tagged
- price-path-only rows can create guard warning but not positive unlock
- repeated pattern frequency and diversity recorded
- representative examples include grade and reason
- MemoryCard prompt payload must mark proxy/price-only as non-evidence

Reports:
docs/operational/research_brain_v3_memory_card_distillation_report.json
docs/operational/research_brain_v3_memory_card_conflicts.json

Acceptance:
- all C01-C36 have V3 card
- card shows data_distilled_rules, not only seed overrides
- conflicts/gaps shown
- source_proxy-derived positive unlocks are not allowed without URL-backed support

================================================================================
9. AGENTS.md 운영 모드 분리
================================================================================

AGENTS.md를 업데이트하라.

분리:
A. Research/backfill mode
- 넓은 검색 가능
- max_results_per_query=100/top_results=None 허용 가능
- 목적: source repair / memory backfill / research audit

B. Production daily mode
- SourceTask budget 필수
- top_results=None 금지
- retry_max=None 금지
- general web fallback 제한
- official-first
- stop-on-resolution
- no unbounded page fetch
- provider failure는 pending

C. Test mode
- fake provider 허용
- bounded fixture만 사용
- production readiness 금지

필수:
- KoreaLiveLiteConfig / ResearchBrain daily CLI가 mode별 preset을 사용
- production daily preset에서 unbounded config 발견 시 실행 실패

테스트:
tests/test_operational_modes_no_unbounded_production.py
tests/test_agents_policy_sync.py

================================================================================
10. Full static / logical audit
================================================================================

새 감사 CLI:
src/e2r/cli/audit_research_brain_v3_operational_readiness.py

검사 항목:
- Research Brain direct score/stage key path count
- cheap_scan_total_score used as verified_score count
- deterministic fake accepted claim count
- local handoff accepted claim count
- SourceTask without execution count
- SourceTask without budget count
- general web before official count
- FCF gap sent to news count
- DART-solvable gap sent to web count
- v2/v3 reports claiming READY despite provider_status real_provider_available=False
- raw routing fixture leakage count
- fixture expected archetype in event text count
- source_proxy_to_A2 count
- source_proxy_to_score count
- future outcome in planner/extractor prompt count
- watchlist item without StageCourt result count
- production daily run from cached candidate path count
- R13 primary without explicit red-team event count
- real LLM provider exercised count
- frozen daily run count
- Evidence OS accepted claim linked to source task count

Report:
docs/operational/research_brain_v3_static_logic_audit.json

Acceptance:
all critical counts = 0
warnings may remain only with documented source gap

================================================================================
11. Multi-day frozen shadow runs
================================================================================

PRODUCTION_READY는 한 번의 dry run으로 선언 금지.

실행:
- 최소 5개 as_of_date
- 가능한 서로 다른 시장 상태
- frozen/snapshot source corpus
- same config/model/schema
- real planner provider 또는 provider failure explicitly pending
- deterministic repeat 3회 for each frozen day

Reports:
docs/operational/research_brain_v3_frozen_daily_runs.json
docs/operational/research_brain_v3_stability_audit.json

Acceptance:
- 5 days completed
- each day candidate_event_count >= 30 or provider/market gap
- no score/stage variance across repeated frozen run
- no source_proxy_to_score
- no fake accepted claim
- no R13 overroute
- every watchlist item has source task/execution/StageCourt trace
- unresolved provider failures become Provider/Source Pending

================================================================================
12. Final Production Readiness Labels
================================================================================

상태 라벨:
- IMPLEMENTATION_MERGED
- REAL_PLANNER_INTEGRATED
- RAW_ROUTER_REPLAY_PASS
- REAL_SOURCE_TASK_EXECUTION_PASS
- REAL_SCORER_WATCHLIST_PASS
- DAILY_SHADOW_RUN_PASS
- FIVE_DAY_FROZEN_SHADOW_PASS
- PRODUCTION_READY

Goal 완료라고 말하려면 최소:
DAILY_SHADOW_RUN_PASS

PRODUCTION_READY라고 말하려면:
FIVE_DAY_FROZEN_SHADOW_PASS + real planner provider exercised + no critical audit findings

================================================================================
13. 필수 테스트
================================================================================

추가 또는 강화:

tests/test_research_brain_v3_real_planner_provider.py
tests/test_research_brain_v3_raw_event_routing.py
tests/test_research_brain_v3_no_fixture_label_leakage.py
tests/test_research_brain_v3_real_source_task_execution.py
tests/test_research_brain_v3_no_local_handoff_fake_claims.py
tests/test_research_brain_v3_watchlist_uses_real_scorer.py
tests/test_research_brain_v3_stagecourt_integration.py
tests/test_research_brain_v3_daily_shadow_entrypoint.py
tests/test_research_brain_v3_no_default_cached_candidates.py
tests/test_research_brain_v3_source_quality_actual_a2_promotion.py
tests/test_research_brain_v3_operational_mode_policy.py
tests/test_research_brain_v3_static_logic_audit.py
tests/test_research_brain_v3_frozen_daily_runs.py

전체 테스트:
PYTHONPATH=src python -m unittest discover -s tests -v

================================================================================
14. 최종 산출물
================================================================================

생성:

docs/operational/research_brain_v2_shadow_limitations.md
docs/operational/research_brain_v3_acceptance_report.md
docs/operational/research_brain_v3_raw_event_router_matrix.json
docs/operational/research_brain_v3_real_planner_provider_report.json
docs/operational/research_brain_v3_source_task_execution_audit.json
docs/operational/research_brain_v3_daily_shadow_report.md
docs/operational/research_brain_v3_daily_watchlist_sample.json
docs/operational/research_brain_v3_source_quality_promotion_report.json
docs/operational/research_brain_v3_memory_card_distillation_report.json
docs/operational/research_brain_v3_static_logic_audit.json
docs/operational/research_brain_v3_frozen_daily_runs.json
docs/operational/research_brain_v3_stability_audit.json
docs/operational/research_brain_v3_production_readiness_verdict.md

output/daily_watchlist/YYYY-MM-DD/e2r_daily_watchlist.json
output/daily_watchlist/YYYY-MM-DD/e2r_daily_watchlist.md

================================================================================
15. 최종 보고 형식
================================================================================

완료 후 다음 형식으로만 보고하라.

1. 최종 상태
- IMPLEMENTATION_MERGED / REAL_PLANNER_INTEGRATED / RAW_ROUTER_REPLAY_PASS / REAL_SOURCE_TASK_EXECUTION_PASS / REAL_SCORER_WATCHLIST_PASS / DAILY_SHADOW_RUN_PASS / FIVE_DAY_FROZEN_SHADOW_PASS / PRODUCTION_READY

2. 커밋
- SHA
- message
- push status
- working tree clean

3. 테스트
- command
- pass/fail/skip

4. Evidence OS regression
- READY 유지 여부
- orphan score count
- source_proxy_to_score count
- legacy direct path count

5. Planner
- real provider exercised 여부
- fake provider used 여부
- provider failure count
- raw routing top1/top3
- R13 overroute count

6. SourceTask execution
- planned/executed/fetched/parsed/Evidence OS accepted count
- local handoff fake claim count
- provider failure
- budget exhausted material gaps

7. Scoring/Stage
- watchlist item count
- real deterministic scorer used count
- cheap_scan_total_score_as_verified_score count
- StageCourt trace count

8. Discovery
- candidate_event_count
- sector coverage
- event type breakdown
- source family breakdown
- cached candidate path used 여부

9. Source quality
- A2 actual promoted count
- A1/A0/B repair queue count
- source_proxy_to_A2 count
- A2 failure reasons

10. Multi-day shadow
- frozen daily run count
- repeat variance
- unresolved blockers

11. Production verdict
- READY / NOT_READY
- blockers
- exact next step

================================================================================
16. 금지사항
================================================================================

- v2 report 숫자만 업데이트하고 v3 완료 주장 금지
- local evidence id를 accepted claim으로 가정 금지
- cheap_scan_total_score를 verified_score로 사용 금지
- deterministic router만 쓰고 LLM planner integration 완료 주장 금지
- 정답 archetype id가 event text에 포함된 fixture로 router accuracy 주장 금지
- source_quality A2를 sample size만으로 pass 처리 금지
- 특정 cached candidates path로 production discovery 주장 금지
- fake provider로 PRODUCTION_READY 주장 금지
- top_results=None production daily 실행 금지
- source_proxy_only를 score/replay-ready로 승격 금지
- score/stage threshold 변경 금지

================================================================================
17. 한 줄 목표
================================================================================

Research Brain v3의 목표는:

“좋은 리포트를 만드는 것”이 아니라,
실제 daily 운영에서 새 사건이 생긴 종목을 잡고,
LLM Planner가 과거 연구 MemoryCard로 무엇을 검증해야 하는지 판단하고,
SourceTask가 실제 source를 가져오고,
Evidence OS가 accepted claim을 만들고,
deterministic scorer와 StageCourt가 진짜 watchlist를 내는 것이다.