확인해봤어. 결론은 이거야.

**v3 패치는 꽤 많이 들어갔고, 이전보다 훨씬 진전됐어.**
근데 현재 레포 상태를 “실제 운영 투입 가능”이라고 부르면 아직 안 돼.

현재 정확한 라벨은:

```text
Research Brain v3 = DAILY_SHADOW_RUN_PASS
Production = NOT READY
```

레포의 `research_brain_v3_acceptance_report.md` 자체도 `final_status: DAILY_SHADOW_RUN_PASS`, `production_ready: False`로 되어 있고, 테스트는 `4596 tests passed`, raw routing top1/top3는 `0.916667 / 1.0`, SourceTask는 `120 / 120 / 120 / 120 / 66`, watchlist item은 40개, deterministic scorer 사용은 13개로 찍혀 있어. 하지만 **real_provider_exercised_count가 0이고 fake_provider_used_count가 40**이야. 즉 LLM 두뇌 운영이 아니라, 아직 fake/fixture 기반 shadow run이야. ([GitHub][1])

또 production readiness 문서도 그대로 말하고 있어. `verdict: DAILY_SHADOW_RUN_PASS`, `production_ready: False`, production blocker는 `fake planner provider used`, `real planner provider not exercised`야. ([GitHub][2])

그래서 지금 상태는 이렇게 보면 돼.

```text
Evidence OS:
상당히 안정화됨

Research Brain v3:
shadow daily flow까지는 닫힘

실제 운영:
아직 real planner / real source / real daily run 검증 전
```

---

# 지금 남은 진짜 핵심 문제

## 1. Real LLM Planner가 아직 운영에서 안 돌았다

`v3_llm_planner_provider.py`에는 `OpenAIPlannerProvider`가 들어가 있고, schema validation, R13 primary 제한, FCF/DART-solvable gap의 general web 차단 같은 검증은 들어가 있어. 구조는 좋아. 그런데 acceptance report에서는 real provider exercised가 0이고 fake provider가 40회 사용됐어. ([GitHub][3]) ([GitHub][1])

즉 지금 라우팅은 “LLM 두뇌가 실제 시장 event를 읽고 판단했다”가 아니라:

```text
Fixture/Fake Planner
+ deterministic router
+ schema guard
```

에 가까워.

이건 테스트용으로는 좋지만, 실제 운영 ready는 아니야.

---

## 2. Source acquisition이 아직 진짜 웹/API fetch가 아니다

`v3_source_acquisition_runner.py`를 보면 기본 구현은 “web scrape을 하지 않는다”고 명시하고, snapshot/event payload를 `EvidenceDocument`와 `EvidenceAnchor`로 바꿔 주는 구조야. `mode == live`이면 실제 live provider가 붙은 게 아니라 `live_source_acquisition_provider_not_configured`로 `PROVIDER_FAILED`를 반환해. ([GitHub][4])

즉 지금은:

```text
SourceTask
→ 실제 DART/IR/CompanyGuide/뉴스 fetch
→ 원문 parse
→ quote/date/entity 검증
```

이 아니라,

```text
SourceTask
→ CandidateEvent summary를 snapshot text로 포장
→ EvidenceDocument/Anchor 생성
```

에 가깝다.

이건 shadow run용으로는 괜찮지만, 실전 운영에서 “진짜 원문 증거를 찾았다”고 말하려면 부족해.

---

## 3. Evidence OS bridge가 여전히 synthetic assertion을 만든다

`v3_evidence_os_execution_bridge.py`는 SourceTask 결과 문서에서 claim을 만들 때, subject를 event company로 놓고, predicate를 `primitive_gap`, object를 `event_summary`, polarity를 positive, temporal status를 CURRENT로 만든다. 즉 원문에서 LLM이 실제 assertion을 추출한 게 아니라, SourceTask의 primitive gap과 event summary를 바탕으로 **결정론적 synthetic assertion**을 구성한다. ([GitHub][5])

이게 왜 중요하냐면, 우리가 원래 만들려던 최종 구조는:

```text
실제 문서 원문
→ LLM assertion extraction
→ target/temporal adjudication
→ primitive mapping
→ score
```

이었어. 기존 Evidence OS 목표문서도 문서 원문에서 “누가, 언제, 무엇을 주장했는가 → 평가 대상 회사에 직접 귀속되는가 → 현재 살아 있는가 → 어느 primitive인가 → 몇 점인가” 장부가 필요하다고 정의했어. 

지금 v3는 이 형식을 흉내 내지만, 아직 “실제 원문 독해”가 아니라 “event/task snapshot을 claim처럼 포장”하는 부분이 남아 있어.

---

## 4. A2 source quality promotion도 실제 URL 검증이라기엔 약하다

`v3_source_quality.py`는 source URL이 있는 memory row를 읽고, 그 URL 문자열과 memory record 내용을 써서 EvidenceDocument/Anchor/claim id를 만든다. 그런데 실제 URL fetch, 원문 날짜 검증, quote 검증까지 수행하는 구조는 아니다. ([GitHub][6])

즉:

```text
URL 있음
→ EvidenceDocument.from_text(...)
→ anchor_verified=True
```

에 가까워. 이건 “A2 실제 승격”이라는 이름치고는 아직 너무 관대해.

특히 과거 연구자료 중 C06, C08, C15 일부처럼 실제 URL이 있는 것은 좋은 fixture 원료가 될 수 있지만, C24/C28/C17의 source_proxy_only/evidence_url_pending 자료는 운영 score fixture가 아니라 ontology/source-gap으로 남겨야 해. C24 연구는 `source_proxy_only`, `evidence_url_pending`, `shadow_weight_only`임을 명시하고 production scoring을 바꾸지 말라고 적고 있고, C28/C17 자료도 source-proxy/URL repair 필요 상태를 분명히 적고 있어.   

---

## 5. AGENTS.md는 production/backfill mode 분리를 반영했지만, 실행 경로가 완전히 강제되는지 더 봐야 함

좋은 점도 있어. `AGENTS.md`에는 이제 Research/backfill mode와 Production daily mode가 분리되어 있고, production daily에서는 `top_results=None`, `retry_max=None`, 무제한 page fetch를 금지하며, DART/KIND/KRX/IR/CompanyGuide로 풀 수 있는 gap을 먼저 일반 웹으로 보내지 말라고 되어 있어. ([GitHub][7])

이건 우리가 원하던 방향이 맞아.

하지만 실제 v3 source runner가 아직 snapshot 중심이라, “bounded official-first real acquisition”이 실제로 닫힌 건 아니야.

---

# 현재 점수

내가 지금 레포를 실제 운영 기준으로 보면:

```text
Evidence OS 무결성:
85~90점

Research Brain v3 구조:
75~80점

실제 daily 운영 가능성:
55~60점

Production readiness:
아직 불가
```

가장 중요한 차이는 이거야.

```text
현재:
shadow daily run이 돌아감

목표:
real planner + real source acquisition + real Evidence OS extraction + real score/stage daily run
```

지금은 “뼈대가 좋고 테스트가 많은 상태”지, 아직 “시장 열리기 전에 돌려서 오늘 후보를 믿고 보는 상태판”은 아니야.

---

# 다음 패치 Goal — Research Brain v4 / Real Evidence Production Shadow

아래 그대로 주면 돼. 이번 Goal은 더 이상 “shadow scaffold”가 아니라 **real evidence production shadow**로 가야 해.

```text
너는 Daikisong/stock_agent 레포의 E2R Research Brain v4 / Real Evidence Production Shadow를 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 유지한다.
- Research Brain v3는 DAILY_SHADOW_RUN_PASS까지 도달했다.
- 그러나 v3는 PRODUCTION_READY가 아니다.
- v3 acceptance report에는 production_ready=False, real_provider_exercised_count=0, fake_provider_used_count=40이 기록되어 있다.
- v3 production readiness verdict도 fake planner provider used, real planner provider not exercised를 production blocker로 기록한다.
- v3 SourceAcquisitionRunner는 기본 snapshot mode이고, live mode는 provider not configured로 실패한다.
- v3 Evidence OS bridge는 실제 원문 assertion extraction이 아니라 CandidateEvent/SourceTask 기반 synthetic assertion을 생성한다.
- 이번 작업 목표는 shadow scaffold를 실제 운영 직전 단계로 끌어올리는 것이다.

이번 작업의 이름:
Research Brain v4 — Real Planner + Real Source Acquisition + Real Evidence Extraction Production Shadow

최종 목표:
실제 CandidateEvent를 생성하고,
실제 LLM Planner가 Research MemoryCard를 보고 아키타입/primitive/source task를 계획하고,
SourceTask가 실제 공시/IR/CompanyGuide/Report/News source에서 문서를 가져오고,
Evidence OS가 실제 원문에서 assertion/claim을 추출·검증하고,
기존 deterministic scorer와 StageCourt가 실제 claim-backed score/stage를 계산하며,
최종 Daily Watchlist가 운영자가 볼 수 있는 상태판으로 출력되게 하라.

절대 원칙:
1. Research Brain은 score/stage를 직접 계산하지 않는다.
2. Research Brain output은 FeatureInput, ScoreContribution, risk field를 직접 mutate하지 않는다.
3. SourceTask snapshot/event summary를 claim처럼 포장해서 score를 만들지 않는다.
4. 실제 원문 EvidenceDocument/EvidenceAnchor/RawAssertion/AdjudicatedClaim 경로를 통과한 claim만 score에 들어간다.
5. fake planner provider 사용 시 PRODUCTION_READY 금지.
6. real planner provider가 provider_error면 해당 후보는 pending/provider_failed로 남긴다.
7. live source provider가 없으면 source task는 provider_failed이며 score 상승 불가.
8. source_proxy_only/evidence_url_pending/price_path_only memory는 current score evidence가 아니다.
9. A2 source quality는 실제 URL/snapshot fetch + anchor/date/entity/primitive replay를 통과해야 한다.
10. production daily mode에서 top_results=None, retry_max=None, unbounded fetch 금지.
11. scoring weight와 Stage threshold는 변경하지 않는다.
12. 특정 종목명, 특정 기사 URL, 특정 키워드 예외 처리 금지.
13. 최종 상태를 PRODUCTION_READY라고 부르려면 real planner provider와 real source acquisition이 모두 실제로 exercised되어야 한다.

================================================================================
1. v3 상태를 명확히 재라벨링
================================================================================

다음 문서를 보강하라.

docs/operational/research_brain_v3_shadow_limitations.md
docs/operational/research_brain_v4_transition_plan.md

내용:
- v3는 DAILY_SHADOW_RUN_PASS이지 PRODUCTION_READY가 아니다.
- v3의 real_provider_exercised_count=0, fake_provider_used_count=40 문제를 명시한다.
- v3 SourceAcquisitionRunner는 snapshot/event payload 기반이고 live provider는 not configured임을 명시한다.
- v3 Evidence OS bridge는 synthetic assertion을 만든다는 한계를 명시한다.
- v4의 목표는 real planner + real acquisition + real extraction + real scorer/stage 연결임을 명시한다.

완료 조건:
- 기존 v3 리포트의 production_ready=False가 유지되어야 한다.
- v3를 production-ready로 재라벨링하지 않는다.

================================================================================
2. Real Planner Provider 운영 연결
================================================================================

현재 OpenAIPlannerProvider는 존재하지만 acceptance에서 real provider가 exercised되지 않았다.
v4에서는 실제 provider run을 운영 shadow acceptance에 포함하라.

구현:
src/e2r/research_brain/v4_planner_runtime.py

요구사항:
- 기존 OpenAIPlannerProvider 또는 프로젝트 LLM provider를 실제로 호출할 수 있는 runtime wrapper 구현
- planner provider mode:
  - real
  - fake
  - none
- fake는 tests 전용
- none은 provider_failed
- real provider에서 API key/model/endpoint를 명확히 보고서에 기록
- real provider 실패 시 candidate별 provider_failed/pending 처리
- real provider가 한 번도 성공하지 않았으면 PRODUCTION_READY 금지

LLM Planner 입력:
- CandidateEventV2
- relevant ArchetypeMemoryCardV3
- current evidence summary
- source route policy
- as_of_date
- forbidden output keys

LLM Planner 금지 입력:
- future MFE/MAE
- outcome label
- expected stage
- target score threshold
- “Green을 열어야 한다” 같은 목적성 문장

LLM Planner 출력:
- top_k_archetype_hypotheses
- positive_thesis
- counter_thesis
- must_verify_primitives
- green_blockers_to_close
- red_team_checks
- source_task_drafts
- query_intents
- do_not_promote_reasons
- planner_self_check

금지 출력:
- score
- stage
- hard_break final
- verified final
- current_score_eligible
- accepted claim final

Validator:
- unknown archetype reject
- R13 primary는 explicit red-team event일 때만 허용
- score/stage key 있으면 reject
- source task budget 없으면 reject
- FCF/cash/revision/backlog/contract gap을 general web/news로 보내면 reject
- future outcome leakage 있으면 reject

필수 리포트:
docs/operational/research_brain_v4_real_planner_report.json

필수 지표:
- real_provider_attempt_count
- real_provider_success_count
- real_provider_failure_count
- fake_provider_used_count
- provider_error_by_candidate
- rejected_by_validator_count
- planner_output_score_stage_key_count
- R13_invalid_primary_rejected_count

Acceptance:
- real_provider_success_count >= 10 in shadow run
- fake_provider_used_count == 0 for production-shadow acceptance
- provider failure candidates remain pending/provider_failed
- no planner output mutates score/stage directly

================================================================================
3. Real Source Acquisition Layer
================================================================================

현재 SourceAcquisitionRunnerV3는 snapshot payload를 EvidenceDocument로 바꾸고, live mode는 not configured를 반환한다.
v4에서는 실제 source connector를 붙여라.

구현:
src/e2r/research_brain/v4_source_acquisition_runner.py

Source classes:
1. DART/OpenDART
   - 단일판매공급계약
   - 신규시설투자
   - 사업보고서/분기보고서/반기보고서
   - 감사보고서
   - 주요사항보고서
   - 정정공시
   - 재무제표/XBRL/API records

2. KIND/KRX
   - 관리종목
   - 거래정지
   - 불성실공시
   - 투자주의/경고/위험
   - 상장폐지 관련 공시

3. CompanyGuide / consensus / report metadata
   - EPS revision
   - 영업이익 revision
   - 목표주가 변화
   - 리포트 title/snippet/PDF link where legally accessible

4. Issuer official
   - 회사 IR
   - 실적발표 자료
   - 컨퍼런스콜 자료
   - 회사 뉴스룸
   - 사업 업데이트

5. Domain official
   - 임상/규제 registry
   - 고객사 공식 발표
   - 정부/입찰/프로젝트 공고

6. Trusted news fallback
   - trusted news only when SourceTask allows fallback

금지:
- SourceTask가 FCF/cash/revision/backlog/contract gap인데 뉴스/general web 먼저 호출
- snapshot text만으로 EVIDENCE_OS_ACCEPTED 처리
- event_summary를 source document로 가장
- provider가 실패했는데 NO_EVIDENCE_FOUND로 위장
- accepted_claim_count를 synthetic하게 채움

SourceAcquisitionResultV4:
{
  "task_id": "...",
  "source_class": "...",
  "provider_name": "...",
  "status": "FETCHED|PARSED|NO_EVIDENCE_FOUND|PROVIDER_FAILED|REJECTED_BY_POLICY|BUDGET_EXHAUSTED",
  "fetched_document_ids": [],
  "document_urls": [],
  "document_hashes": [],
  "anchor_ids": [],
  "provider_errors": [],
  "budget_used": {},
  "stop_reason": "..."
}

Acceptance:
- live/source shadow run에서 at least 30 real documents fetched or honest provider/source gap
- DART/KIND/CompanyGuide/IR provider path exercised
- provider failure is represented as PROVIDER_FAILED, not accepted/no evidence
- source task execution without real document does not produce accepted claim
- source task accepted claim ids must correspond to Evidence OS ledger claim ids

================================================================================
4. Real Evidence Extraction Bridge
================================================================================

현재 v3 bridge는 RawAssertion을 event company + primitive_gap + event_summary로 구성한다.
v4에서는 실제 document text/anchor에서 assertion을 추출해야 한다.

구현:
src/e2r/research_brain/v4_evidence_extraction_bridge.py

Flow:
EvidenceDocument + EvidenceAnchor + document text
→ contract-blind EvidenceClaim/RawAssertion extractor
→ target/temporal adjudicator
→ primitive mapper
→ derive_score_eligibility
→ AppendOnlyEvidenceLedger

Extractor:
- 기본은 Evidence OS v2 workflow 재사용
- 가능하면 LLM Evidence Claim Extractor 사용
- LLM provider unavailable이면 rule-based extraction은 mention-only로 제한
- mention-only는 score 불가
- document text 안의 quote/span/table/API record anchor를 검증

금지:
- subject_entity_id를 무조건 target ticker로 설정
- polarity를 무조건 positive로 설정
- temporal_status를 무조건 CURRENT로 설정
- semantic_status를 무조건 PASS로 설정
- task.primitive_gap을 바로 accepted mapping으로 넣기
- event_summary를 exact_quote처럼 쓰기

필수 처리:
- subject/entity resolver
- target directness
- polarity
- event_date/source_date
- lifecycle/current status
- contradiction
- primitive mapping accepted/rejected
- source quorum
- quote/table/API anchor verification

Acceptance:
- accepted claim에는 real document_id + anchor_id + quote/API/table locator가 있다.
- wrong-subject fixture는 accepted score claim이 되지 않는다.
- old risk without current open confirmation is follow-up/pending, not risk score.
- source_proxy_only memory cannot become RawAssertion.
- LLM-only inference without anchor cannot become score contribution.

Reports:
docs/operational/research_brain_v4_evidence_extraction_audit.json

Metrics:
- real_document_to_raw_assertion_count
- raw_assertion_to_adjudicated_claim_count
- adjudicated_claim_to_accepted_claim_count
- mention_only_count
- synthetic_assertion_count
- forced_positive_polarity_count
- forced_current_temporal_count
- quote_anchor_missing_rejected_count
- wrong_subject_rejected_count

Critical:
synthetic_assertion_count must be 0 in production shadow acceptance.

================================================================================
5. Source Quality A2 실제 재검증
================================================================================

v3 A2 promotion은 memory row와 URL 문자열로 EvidenceDocument를 만들어 승격했다.
v4는 실제 URL/snapshot fetch/anchor/date/entity/claim replay를 요구한다.

구현:
src/e2r/research_brain/v4_source_quality_promotion.py

A2_REAL_REPLAY_VERIFIED 조건:
- source_url 또는 official API/snapshot URI 존재
- source fetch 또는 stored snapshot load 성공
- content_hash 생성
- published_at 또는 official filing date 검증
- EvidenceAnchor 생성
- quote/table/API locator 검증
- subject/target directness 판정
- primitive mapping accepted
- Evidence OS score eligibility 통과
- source_proxy_only=false
- evidence_url_pending=false

A1_URL_ANCHOR_PENDING:
- URL 있음
- fetch/date/anchor 중 일부 미완

A0_URL_STRING_ONLY:
- URL 문자열만 있음

C_SOURCE_PROXY_ONTOLOGY_ONLY:
- source_proxy_only 또는 evidence_url_pending

D_PRICE_PATH_ONLY:
- price outcome 중심

Run:
- C06/C08/C15 URL-backed rows 우선 500개 attempted
- at least 100 actual A2_REAL_REPLAY_VERIFIED or honest source/provider gap
- C24/C28/C17 source_proxy rows remain C unless actual URL repaired

Reports:
docs/operational/research_brain_v4_source_quality_promotion_report.json
docs/operational/research_brain_v4_a2_real_replay_claims_sample.json
docs/operational/research_brain_v4_url_repair_queue.json

Critical metrics:
- source_proxy_to_A2_count = 0
- A2_without_fetch_or_snapshot_count = 0
- A2_without_anchor_count = 0
- A2_without_claim_id_count = 0
- A2_without_source_date_count = 0

================================================================================
6. Candidate Discovery 실전화
================================================================================

현재 v3 shadow는 fixture/frozen 후보 중심이다.
v4에서는 실제 daily discovery를 production shadow mode로 실행하라.

구현:
src/e2r/cli/run_research_brain_v4_production_shadow.py

모드:
- frozen_real_source_snapshot
- live_official_only
- live_full_bounded
- test_fake

기본 production shadow:
- planner-provider=real
- source-acquisition=live_official_first
- targeted_smoke_only=false
- top_results=None 금지
- max_fetches/task 제한
- provider failure pending
- fake provider 금지

Flow:
1. KRX universe build
2. DART/KIND/KRX official events
3. CompanyGuide/revision/report radar
4. IR/report snapshot
5. price/volume anomaly
6. CandidateEventV2 generation
7. Candidate clustering
8. real LLM planner
9. SourceTask generation
10. real source acquisition
11. real evidence extraction
12. Evidence OS accepted claims
13. deterministic scorer/stage
14. Daily Watchlist output

Minimum shadow acceptance:
- candidate_event_count >= 30 or explicit provider/market gap
- each large_sector_id attempted >= 3 or explicit source gap
- real planner success >= 10
- source task executed >= 20
- real documents fetched >= 30
- Evidence OS accepted claims >= 10
- deterministic score/stage outputs >= 5
- fake provider used = 0
- source task without real document accepted = 0

Reports:
docs/operational/research_brain_v4_production_shadow_report.md
docs/operational/research_brain_v4_candidate_event_report.json
docs/operational/research_brain_v4_sector_coverage_report.json
docs/operational/research_brain_v4_source_provider_gap_report.json

================================================================================
7. Daily Watchlist V4
================================================================================

Watchlist는 “추천”이 아니라 상태판이다.

DailyWatchlistItemV4:
{
  "symbol": "...",
  "company_name": "...",
  "candidate_event_id": "...",
  "event_type": "...",
  "event_summary": "...",
  "event_source": "...",
  "primary_archetype": "...",
  "secondary_archetypes": [],
  "planner_provider": "...",
  "planner_real_provider": true,
  "research_memory_cards_used": [],
  "source_tasks": [],
  "source_task_executions": [],
  "accepted_claim_ids": [],
  "top_supporting_claims": [],
  "score_contribution_ids": [],
  "trigger_priority_score": null,
  "verified_score": null,
  "provisional_score": null,
  "score_interval_lower": null,
  "score_interval_upper": null,
  "score_valid_status": "...",
  "base_stage": "...",
  "investigation_status": "...",
  "transition_overlay": "...",
  "failed_stage_gates": [],
  "green_blockers": [],
  "red_team_checks": [],
  "do_not_promote_reasons": [],
  "follow_up_tasks": [],
  "operator_notes": "..."
}

Sections:
- Stage3-Green
- Stage3-Yellow-Pending
- Stage2-Actionable
- Stage2-Watch
- 4B-watch
- Reject/Red
- Provider/Source Pending
- Planner Pending

Rules:
- verified_score must come from deterministic scorer only.
- trigger_priority_score may come from cheap scan, but never as verified_score.
- item without accepted claim remains pending/watch, not scored.
- provider failure item goes Provider/Source Pending.
- fake provider output cannot appear in production shadow watchlist.

Output:
output/daily_watchlist_v4/YYYY-MM-DD/e2r_daily_watchlist.json
output/daily_watchlist_v4/YYYY-MM-DD/e2r_daily_watchlist.md

================================================================================
8. Static / Logical Audit V4
================================================================================

새 감사 CLI:
src/e2r/cli/audit_research_brain_v4_operational_readiness.py

검사 항목:
- fake_provider_used_in_production_shadow_count
- real_provider_exercised_count
- provider_failed_final_score_count
- source_task_accepted_without_real_document_count
- synthetic_assertion_count
- forced_target_subject_count
- forced_positive_polarity_count
- forced_current_temporal_count
- event_summary_used_as_exact_quote_count
- source_proxy_to_score_count
- source_proxy_to_A2_count
- A2_without_fetch_or_snapshot_count
- A2_without_anchor_count
- cheap_scan_score_as_verified_score_count
- watchlist_without_stagecourt_count
- score_contribution_without_claim_count
- R13_invalid_primary_count
- DART_solvable_gap_sent_to_general_web_count
- FCF_gap_sent_to_news_count
- unbounded_source_task_count
- top_results_none_in_production_count
- retry_max_none_in_production_count
- future_outcome_in_planner_prompt_count
- future_outcome_in_extraction_prompt_count
- production_ready_despite_blockers_count

Critical counts must be 0 except real_provider_exercised_count must be > 0.

Report:
docs/operational/research_brain_v4_static_logic_audit.json

================================================================================
9. Multi-day Real Shadow Validation
================================================================================

PRODUCTION_READY는 단일 run으로 금지한다.

Run:
- 최소 5개 as_of_date
- frozen source snapshot 또는 live official source
- real planner provider
- fake provider 금지
- 동일 source snapshot 반복 3회
- score/stage variance 0
- provider failures pending 처리
- each day daily watchlist 생성

Reports:
docs/operational/research_brain_v4_multi_day_shadow_runs.json
docs/operational/research_brain_v4_stability_audit.json

Acceptance:
- five_day_run_count >= 5
- real_provider_success_count_total >= 30
- real_document_fetched_total >= 100
- accepted_claim_total >= 30
- deterministic_stage_output_total >= 15
- repeated frozen run variance = 0
- fake_provider_used_total = 0
- production_ready_despite_provider_gap = 0

================================================================================
10. 기존 연구자료 사용 정책 재검증
================================================================================

과거 연구자료는 두뇌 원료이지 점수 정답지가 아니다.

다시 audit:
- C06/C08/C15 URL-backed rows:
  - source fetch/snapshot/anchor 가능 여부
  - A2_REAL_REPLAY_VERIFIED 승격 가능 여부

- C17/C24/C28 source_proxy rows:
  - ontology/source route/false-positive memory로만 사용
  - production score fixture로 승격 금지

- price_path_only rows:
  - current extraction prompt 금지
  - source route/guardrail summary만 허용

Reports:
docs/operational/research_brain_v4_research_memory_usage_audit.json

Critical:
- source_proxy_memory_to_score_count = 0
- price_outcome_to_extraction_prompt_count = 0
- C24/C28/C17 source_proxy promoted_to_A2_count = 0 unless URL repaired
- C06/C08/C15 A2 promoted count reported with real source evidence

참고:
C06 연구자료는 source_proxy_only_count=0, evidence_url_pending_count=0인 URL-backed row가 있어 golden replay 후보가 될 수 있다.
C08도 직접 URL을 가진 customer/order/profile fixture가 있다.
C15 일부는 direct URL이 있다.
반면 C24/C28/C17 상당수는 source_proxy_only/evidence_url_pending이므로 ontology-only로 남겨야 한다.

================================================================================
11. 필수 테스트
================================================================================

추가 또는 강화:

tests/test_research_brain_v4_real_planner_provider.py
tests/test_research_brain_v4_provider_failure_pending.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_research_brain_v4_no_snapshot_fake_claim.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
tests/test_research_brain_v4_no_synthetic_assertion.py
tests/test_research_brain_v4_source_quality_real_a2.py
tests/test_research_brain_v4_candidate_discovery_live_official.py
tests/test_research_brain_v4_daily_watchlist.py
tests/test_research_brain_v4_static_logic_audit.py
tests/test_research_brain_v4_multi_day_shadow.py
tests/test_research_brain_v4_memory_usage_policy.py
tests/test_research_brain_v4_operational_modes.py
tests/test_research_brain_v4_no_fake_provider_production_ready.py
tests/test_research_brain_v4_no_unbounded_production_fetch.py

필수 assertions:
- real planner provider exercised in production shadow.
- fake provider cannot pass PRODUCTION_READY.
- live source acquisition mode fetches real document or returns provider_failed.
- no SourceTask accepted claim without real document.
- no synthetic assertion in production shadow.
- no event_summary used as quote.
- no forced subject=target without entity adjudication.
- no forced polarity=positive.
- no forced temporal_status=CURRENT.
- accepted claim has real source anchor.
- source_proxy_only never scores.
- A2 requires real source replay.
- watchlist verified_score uses deterministic scorer.
- cheap_scan score never equals verified_score unless separately justified by scorer trace.
- provider failure cannot produce final low score.
- five-day shadow run required for PRODUCTION_READY.
- full unittest suite passes.

================================================================================
12. Final reports
================================================================================

생성:

docs/operational/research_brain_v4_acceptance_report.md
docs/operational/research_brain_v4_real_planner_report.json
docs/operational/research_brain_v4_source_acquisition_report.json
docs/operational/research_brain_v4_evidence_extraction_audit.json
docs/operational/research_brain_v4_source_quality_promotion_report.json
docs/operational/research_brain_v4_production_shadow_report.md
docs/operational/research_brain_v4_daily_watchlist_sample.json
docs/operational/research_brain_v4_static_logic_audit.json
docs/operational/research_brain_v4_multi_day_shadow_runs.json
docs/operational/research_brain_v4_stability_audit.json
docs/operational/research_brain_v4_research_memory_usage_audit.json
docs/operational/research_brain_v4_production_readiness_verdict.md

Acceptance report must include:
- commit SHA
- test command
- pass/fail/skip
- Evidence OS regression
- Research Brain v3 regression
- real planner provider metrics
- real source acquisition metrics
- real evidence extraction metrics
- score/stage metrics
- watchlist metrics
- static audit critical counts
- multi-day shadow metrics
- production verdict

================================================================================
13. 완료 상태 라벨
================================================================================

상태 라벨:
- IMPLEMENTATION_MERGED
- REAL_PLANNER_PASS
- REAL_SOURCE_ACQUISITION_PASS
- REAL_EVIDENCE_EXTRACTION_PASS
- REAL_SCORER_STAGE_PASS
- DAILY_WATCHLIST_PASS
- FIVE_DAY_REAL_SHADOW_PASS
- PRODUCTION_READY

Goal 완료라고 말하려면 최소:
DAILY_WATCHLIST_PASS

PRODUCTION_READY라고 말하려면:
- REAL_PLANNER_PASS
- REAL_SOURCE_ACQUISITION_PASS
- REAL_EVIDENCE_EXTRACTION_PASS
- REAL_SCORER_STAGE_PASS
- FIVE_DAY_REAL_SHADOW_PASS
- static critical count 0
- fake provider count 0
- provider failure final score count 0

================================================================================
14. 최종 답변 형식
================================================================================

작업 완료 후 다음 형식으로 보고하라.

1. 최종 상태
- IMPLEMENTATION_MERGED / REAL_PLANNER_PASS / REAL_SOURCE_ACQUISITION_PASS / REAL_EVIDENCE_EXTRACTION_PASS / REAL_SCORER_STAGE_PASS / DAILY_WATCHLIST_PASS / FIVE_DAY_REAL_SHADOW_PASS / PRODUCTION_READY

2. 커밋
- SHA
- message
- push status
- working tree clean

3. 테스트
- command
- pass/fail/skip

4. Planner
- real provider success/failure
- fake provider count
- R13 invalid primary rejected
- schema violations

5. Source acquisition
- source tasks
- real documents fetched
- provider failures
- budget exhausted
- unbounded count

6. Evidence extraction
- documents to assertions
- assertions to claims
- accepted claims
- synthetic assertion count
- forced current/positive/target count

7. Score/Stage
- deterministic scorer output count
- StageCourt trace count
- watchlist count
- score pending/provider pending count

8. A2 source quality
- attempted
- promoted
- failed
- source_proxy_to_A2
- repair queue

9. Multi-day shadow
- day count
- repeat variance
- accepted claims
- deterministic stage outputs

10. Production verdict
- READY / NOT_READY
- blockers
- next exact action

================================================================================
15. 금지사항
================================================================================

- fake provider로 PRODUCTION_READY 주장 금지
- snapshot/event summary를 accepted claim으로 포장 금지
- v3 report 숫자만 업데이트하고 v4 완료 주장 금지
- event_summary를 quote로 쓰기 금지
- source_proxy_only를 A2나 score로 승격 금지
- cheap_scan_total_score를 verified_score로 사용 금지
- live source provider missing인데 no_evidence로 처리 금지
- provider failure인데 낮은 점수 확정 금지
- score/stage threshold 변경 금지
- 종목명/URL/키워드 예외 패치 금지
```

---

# 최종 판단

방금 패치는 **v3 shadow daily run을 꽤 잘 만들었다**고 봐도 돼.
하지만 네가 원하는 최종 운영은 아직 한 겹 더 남았어.

남은 한 겹은 정확히 이거야.

```text
fake/snapshot shadow
→ real planner + real source + real extraction shadow
```

지금 레포의 리포트도 production blocker를 스스로 말하고 있어.

```text
fake planner provider used
real planner provider not exercised
```

그래서 다음 Goal은 “더 많은 테스트”가 아니라, **가짜 그림자를 실제 문서·실제 LLM·실제 Evidence OS claim으로 바꾸는 패치**가 되어야 해.
