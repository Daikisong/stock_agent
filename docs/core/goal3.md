확인했어. 최신 `main`은 **Research Brain v1까지 실제로 들어간 상태**가 맞아. 커밋 히스토리상 최신 커밋은 `f5829a4 Research Brain v1 전체 메모리 재컴파일 보강`이고, 그 직전에 `d4cce0b Research Brain v1 운영 두뇌 계층 구현`, `3f30fe2 전 아키타입 증거 OS 운영 검증 완료`가 이어져 있어. 즉 Evidence OS → Research Brain 순서로 큰 구조는 실제 반영됐다. ([GitHub][1])

그런데 정적 감사 기준으로 보면 **아직 “운영 두뇌 완성”이라고 보기엔 치명적인 빈틈이 남아 있어.** 특히 Research Brain v1 리포트는 `READY`라고 쓰고 있지만, 내부 지표를 보면 “실제 종목 선정 두뇌”라기보다 **대량 메모리 인덱스 + 규칙형 플래너 + 제한된 dry-run**에 가깝다.

---

# 현재 상태 요약

좋은 점부터 보면, 레포에는 이제 `src/e2r/research_brain` 폴더가 생겼고, `memory_compiler.py`, `memory_store.py`, `hypothesis_builder.py`, `investigation_planner.py`, `runtime_planner.py`, `evidence_os_bridge.py`, `source_task_bridge.py`, `memory_leakage_audit.py`, `reports.py` 같은 핵심 파일이 들어가 있다. 구조 자체는 우리가 말한 Research Brain 계층을 제대로 만들려고 한 흔적이 분명하다. ([GitHub][2])

운영 리포트도 생겼다. `research_brain_v1_acceptance_report.md`에는 테스트 `4543 passed / 0 failed / 0 skipped`, Evidence OS regression `READY`, memory record `1,555,954`, C01~C36 profile coverage `36/36`, leakage audit 통과, source router audit 통과, verdict `READY`가 적혀 있다. ([GitHub][3])

하지만 바로 다음 지표가 문제야.

`planner_replay_results`를 보면 C06, C08, C15, C17 replay의 `primary_archetype_hypothesis`가 각각 원래 아키타입이 아니라 **`R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`**로 잡혀 있는데도 `result: pass`로 처리돼 있다. C24도 `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`로 잡혔고, C28만 제대로 C28로 잡혔다. ([GitHub][4])

이건 꽤 중요해. 왜냐하면 Research Brain의 핵심은:

```text
이 사건은 어느 아키타입인가?
→ 그 아키타입에서 무엇을 검증해야 하는가?
```

인데, replay에서조차 C06/HBM, C08/test socket, C15/spread, C17/chemical spread를 전부 R13 red-team류로 보내면서 pass가 나오면, 지금 acceptance test가 **“뇌가 맞게 생각했는지”가 아니라 “뭔가 source task를 만들었는지”만 보고 있는 것**에 가깝다.

---

# 내가 보는 핵심 부족점

## 1. 아키타입 추론이 아직 두뇌가 아니라 토큰 점수기다

현재 `infer_archetype_hypothesis()`는 후보 이벤트의 `event_type`, `candidate_reason`, `source_family` 문자열을 합친 뒤, profile의 primitive/source route token이 들어 있는지와 memory record count로 점수를 올린다. 추가로 `contract`, `facility`, `earnings`, `risk` 같은 단어가 있으면 관련 토큰을 가진 archetype을 boost한다. ([GitHub][5])

이 구조는 빠르지만, 우리가 말한 “연구 기억을 바탕으로 사고하는 LLM 두뇌”는 아니야.

예를 들어 C06 replay가 HBM/customer-capacity 사고를 해야 하는데 R13 false-positive review로 가는 건, 실제 아키타입 의미보다 **메모리량·토큰 중첩·red-team류 일반어**가 더 세게 작동했다는 뜻으로 보인다.

---

## 2. replay test가 잘못 통과하고 있다

C06 replay에서 primary hypothesis가 C06이 아니면, 그 replay는 실패해야 맞다.

지금은:

```text
target archetype: C06
primary hypothesis: R13
source_task_count: 6
result: pass
```

이런 식이야. ([GitHub][4])

이건 acceptance 기준이 너무 헐겁다. 최소한 replay에서는 아래를 요구해야 해.

```text
primary_archetype_hypothesis == expected_archetype
또는
expected_archetype in top_3_hypotheses
AND primary mismatch reason is explicit
```

지금은 “뭔가 조사 계획을 만들었다”는 이유로 통과하는 모양인데, 이러면 실제 운영에서 좋은 C06 후보가 들어와도 R13 쪽 guard task만 잔뜩 만들고, C06 특유의 `capacity sold-out / customer allocation / HBM revenue mix / FCF bridge`를 놓칠 수 있어.

---

## 3. Source quality A등급이 너무 쉽게 부여될 가능성이 있다

`source_quality_classifier.py`를 보면 `source_proxy_only`나 `evidence_url_pending`이면 C등급으로 보내는 건 좋다. 그런데 그 외에는 `has_url`과 `has_anchor_hint`가 있으면 바로 `A_URL_BACKED_REPLAY_READY`가 된다. ([GitHub][6])

이건 아직 약해.

진짜 A등급 replay-ready는 단순히 URL 문자열과 `source_url`/`evidence_url` 힌트가 있는 게 아니라:

```text
URL fetch 성공
source date 검증
exact quote 또는 table/API anchor 검증
target entity 직접성 검증
as-of date 이전 자료
primitive mapping 가능
Evidence OS accepted claim으로 재현 가능
```

까지 통과해야 해.

지금 리포트에는 `A_URL_BACKED_REPLAY_READY`가 202,547개, `production_fixture_count`가 56,042개로 크게 늘어났는데, 이 숫자가 실제 원문 fetch/anchor 검증까지 통과한 수인지, 아니면 URL 문자열이 있는 연구 row를 넓게 잡은 수인지는 더 엄격히 검증해야 한다. ([GitHub][7])

---

## 4. Memory가 너무 크고, 아직 “압축된 판례 카드”가 약하다

메모리 레코드가 155만 개까지 늘었다. 그중 `C_SOURCE_PROXY_ONTOLOGY_ONLY`가 860,101개, `D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK`가 361,665개다. ([GitHub][3])

원료가 많은 건 좋은데, 운영 두뇌가 매번 이 원료를 그대로 뒤지면 안 돼.

최종적으로는 raw memory가 아니라:

```text
C06 ArchetypeMemoryCard
C08 ArchetypeMemoryCard
C15 ArchetypeMemoryCard
...
```

처럼 압축돼야 해.

예:

```text
C06:
HBM 단어만으로 승격 금지.
Stage2-Actionable unlock:
- capacity sold-out
- customer allocation
- qualification pass
- HBM revenue mix

Green blocker:
- cashflow bridge
- repeat evidence family

False positive:
- package substrate sympathy
- qualification lag with reopen path
```

현재 memory는 많이 들어갔지만, `runtime_planner.py`는 결국 profile의 `required_primitives_observed`, `green_blockers`, `source_routes`를 뽑아 source task를 만드는 수준이다. `plan_candidate_events()`도 candidate events를 받아 `build_research_brain_plan()`을 호출하는 얇은 entrypoint다. ([GitHub][8])

---

## 5. Discovery dry run은 아직 운영 dry run이라고 보기엔 약하다

Research Brain acceptance report의 discovery dry run은 `candidate_event_count: 8`, `candidate_event_requirement_status: provider_or_source_gap_recorded`, Evidence OS accepted claim count `5`다. ([GitHub][3])

Evidence OS 쪽 sector matrix도 production discovery candidate count가 8이고, candidate source path가 `official_cheap_scan` 하나다. source call count를 보면 naver search query 32개가 있고, OpenDART detail fetch, OpenDART financial statement, CompanyGuide call은 0으로 되어 있다. ([GitHub][9])

이건 “전 시장 운영으로 후보를 넓게 잡고, 공식 소스 중심으로 검증하는 일일 파이프라인”이라기보다는 **fixture/dry-run에 가까운 후보 생성 확인**이야.

Research Brain이 진짜 운영 두뇌가 되려면 최소한:

```text
30개 이상 CandidateEvent
각 large sector별 3개 이상
source route 실행
Evidence OS accepted claim 생성
Stage output 생성
follow-up task 생성
```

까지 가야 한다.

---

## 6. general search 비율이 여전히 높다

source route audit에서 official source task ratio는 1.0으로 좋게 찍혔지만, general search task ratio도 0.520833이다. 즉 전체 source task 중 절반가량은 general search 허용이다. ([GitHub][10])

이 자체가 무조건 나쁜 건 아니지만, 최종 운영 목표는:

```text
DART/KIND/IR/CompanyGuide로 해결 가능한 gap
→ general search 금지

general search
→ trusted source/unknown repair/fallback only
```

였지.

따라서 단순히 “general_search_allowed=True인 task가 있어도 budget이 있으니 pass”가 아니라, **primitive별로 왜 general search가 허용됐는지**가 audit되어야 해.

---

# 내 판정

현재 상태는 이렇게 보는 게 정확해.

```text
Evidence OS v2:
운영 READY에 가까움

Research Brain v1:
메모리 인덱스와 기본 플래너 구현은 완료

하지만:
아키타입 추론 정확도, replay acceptance, source quality 실제 검증,
discovery dry run 규모, 압축 memory card, production orchestration은 아직 부족
```

따라서 다음 Goal은 “Research Brain v1에 또 파일 더 추가”가 아니라:

> **Research Brain v2 — Archetype Routing Correctness + Production Discovery Orchestrator + Memory Distillation**

로 가는 게 맞다.

---

# 다음 패치용 완성 Goal 프롬프트

아래 그대로 코딩 에이전트에게 주면 돼.

```text
너는 Daikisong/stock_agent 레포의 E2R Research Brain v2와 Production Discovery Orchestrator를 구현하는 coding agent다.

현재 전제:
- Evidence OS v2는 READY 상태다.
- Research Brain v1은 구현되어 있고, 연구 메모리 compile/report/acceptance 산출물도 존재한다.
- 하지만 Research Brain v1 acceptance는 아직 운영 두뇌 정확도를 충분히 검증하지 못한다.
- 특히 planner replay에서 C06/C08/C15/C17/C24가 expected archetype이 아니라 R13 계열로 라우팅돼도 pass 처리되는 문제가 있다.
- 이번 작업의 목표는 단순히 테스트 숫자를 늘리는 것이 아니라, Research Brain이 실제 운영에서 “새 사건 → 올바른 아키타입 → 올바른 primitive/source task → Evidence OS accepted claim → deterministic Stage”로 이어지게 만드는 것이다.

이번 작업의 이름:
Research Brain v2 — Archetype Routing Correctness + Production Discovery Orchestrator + Memory Distillation

절대 원칙:
1. Evidence OS v2를 우회하지 마라.
2. Research Brain은 score/stage를 직접 계산하지 않는다.
3. Research Brain은 FeatureInput, ScoreContribution, risk field를 직접 mutate하지 않는다.
4. scoring weight와 Stage threshold는 바꾸지 않는다.
5. source_proxy_only / evidence_url_pending / price_path_only memory는 현재 점수 evidence가 아니다.
6. 과거 MFE/MAE/outcome label은 current extraction prompt에 들어가면 안 된다.
7. 종목명 하드코딩, 특정 URL 예외, 특정 키워드 예외 금지.
8. general search는 fallback이다. official source로 해결 가능한 primitive에는 general search를 허용하지 않는다.
9. replay에서 expected archetype을 틀리면 실패다.
10. candidate discovery가 8개로 끝나는데 READY라고 말하면 안 된다. source gap이면 NOT_READY 또는 PARTIAL_READY로 표시한다.

================================================================================
1. 현재 Research Brain v1 결함을 명시적으로 deprecated 처리
================================================================================

다음 상태를 운영 READY 근거로 쓰지 마라.

- research_brain_v1_planner_replay_results.json에서:
  - C06 expected인데 primary = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  - C08 expected인데 primary = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  - C15 expected인데 primary = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  - C17 expected인데 primary = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  - C24 expected인데 primary = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - result가 pass로 되어 있는 상태

이 결과는 “planner task generation smoke pass”일 수는 있지만 “archetype routing pass”가 아니다.

새 문서 생성:
docs/operational/research_brain_v1_deprecated_acceptance_notes.md

내용:
- v1 acceptance가 무엇을 검증했는지
- 무엇을 검증하지 못했는지
- 왜 v2가 필요한지
- v1 report의 READY를 production-ready가 아니라 IMPLEMENTATION_READY로 재라벨링

================================================================================
2. Archetype Routing Correctness 재설계
================================================================================

현재 infer_archetype_hypothesis의 token/memory-count 기반 점수기를 교체하거나 보조로 낮춰라.

새 구조:

A. Candidate Event Understanding
입력:
- CandidateEvent
- event_type
- source_family
- source payload
- reason_codes
- structured fields
- price context
- disclosure text if available
- report/IR metadata if available

출력:
- event_semantics
- involved_entities
- economic_mechanism
- likely_evidence_family
- directness_to_issuer
- event_strength
- event_freshness
- candidate_archetype_distribution

B. Research Memory Retrieval
입력:
- event_semantics
- large_sector candidate
- candidate_archetype_distribution
- available source families

출력:
- top_k_archetype_memory_cards
- positive patterns
- false-positive patterns
- green blockers
- red-team patterns
- source route patterns
- query success/failure patterns

C. Archetype Router
출력:
{
  "primary_archetype": "...",
  "top_k_archetypes": [
    {"archetype_id": "...", "probability_or_score": 0.0, "reason": "..."}
  ],
  "router_confidence": "HIGH|MEDIUM|LOW",
  "why_not_other_top_archetypes": [],
  "required_disambiguation_tasks": []
}

규칙:
- R13 red-team/cross-archetype archetype는 default primary가 되면 안 된다.
- R13은 overlay/secondary/red-team route로 붙는 것이 기본이다.
- primary가 R13이 되려면 candidate event 자체가 cross-archetype false-positive review 또는 red-team review event라는 강한 증거가 있어야 한다.
- expected archetype replay에서 primary mismatch는 실패다.
- LOW confidence이면 score/stage로 넘어가지 말고 `ARCTYPE_PENDING_DISAMBIGUATION` 상태를 출력한다.

필수 테스트:
- C06 HBM event replay → primary C06
- C08 test socket customer/order replay → primary C08
- C15 material spread pass-through replay → primary C15
- C17 chemical spread replay → primary C17
- C24 bio data/regulatory event replay → primary C24
- C28 software/security retention replay → primary C28
- R13 generic false-positive review event → primary R13 가능
- C06 event + red-team concern → primary C06, secondary/overlay R13
- C15 raw commodity headline → primary C15, stage cap/false-positive memory attached, not R13 primary

Acceptance:
- C01-C36 archetype routing fixture 전체에서 top1 accuracy >= 90%
- top3 accuracy = 100%
- C06/C08/C15/C17/C24/C28 six mandatory replays top1 exact match
- R13 over-routing count = 0 except explicit R13 fixtures

================================================================================
3. ArchetypeMemoryCard 도입
================================================================================

현재 155만 개 ResearchMemoryRecord를 runtime planner가 직접 보는 구조를 줄여라.

새 객체:
ArchetypeMemoryCard

{
  "archetype_id": "...",
  "large_sector_id": "...",
  "version": "v2",
  "generated_from_record_count": 0,
  "quality_breakdown": {},
  "canonical_mechanism": "...",
  "stage2_unlocks": [],
  "yellow_unlocks": [],
  "green_unlocks": [],
  "green_blockers": [],
  "stage2_caps": [],
  "false_positive_patterns": [],
  "4b_watch_patterns": [],
  "4c_hard_break_patterns": [],
  "required_primitives": [],
  "alternative_primitives": [],
  "source_route_by_primitive": {},
  "source_quorum_by_primitive": {},
  "do_not_promote_rules": [],
  "lifecycle_rules": [],
  "query_intent_patterns": [],
  "bad_query_patterns": [],
  "representative_url_backed_fixture_ids": [],
  "representative_source_proxy_ontology_ids": [],
  "source_gaps": [],
  "confidence": "HIGH|MEDIUM|LOW",
  "runtime_usage_policy": "READY|PLANNING_ONLY|SOURCE_GAP|UNSUPPORTED"
}

카드는 raw memory를 그대로 복사하지 말고 압축해야 한다.

예시:
C06 card:
- HBM keyword alone is not enough.
- Stage2-Actionable unlocks: capacity sold-out, customer allocation, qualification pass, HBM revenue mix, shipment visibility.
- Green blockers: cashflow bridge, repeat evidence family, conventional memory drag.
- False positives: package substrate sympathy, qualification lag with reopen path.
- Hard 4C: confirmed permanent customer loss or cancellation, not mere qualification delay.

C28 card:
- software/security keyword is a signboard.
- Stage2-Actionable requires ARR/RPO/renewal/retention/churn/contract backlog.
- Security theme spike without retention bridge is false positive.
- Green requires recurring revenue plus margin/cash durability.

필수:
- C01-C36 전체 ArchetypeMemoryCard 생성
- card별 source_quality breakdown
- card별 representative memory ids
- card별 source gap
- card 생성 과정 deterministic
- raw memory record 155만 개를 planner prompt에 직접 넣지 않음

출력:
docs/operational/research_brain_v2_memory_cards.json
docs/operational/research_brain_v2_memory_card_matrix.json

================================================================================
4. Source Quality 재검증: A등급을 실제 Anchor-ready로 강화
================================================================================

현재 A_URL_BACKED_REPLAY_READY는 URL + anchor hint만으로 과대분류될 수 있다.
A등급을 다음처럼 세분화하라.

A2_EVIDENCE_OS_REPLAY_VERIFIED
- URL fetch 또는 snapshot 있음
- EvidenceAnchor 생성 성공
- source date verified
- exact quote/table/API locator verified
- target entity directness verified
- primitive mapping accepted
- Evidence OS replay 통과

A1_URL_BACKED_ANCHOR_PENDING
- URL 있음
- source date 또는 quote/anchor 검증 미완
- replay fixture 후보지만 production replay 전 repair 필요

A0_URL_STRING_ONLY
- URL 문자열은 있지만 fetch/anchor/date 검증 없음
- query/source route memory로만 사용

B_URL_REPAIR_NEEDED
- URL 있음, 원문 접근 실패 또는 format repair 필요

C_SOURCE_PROXY_ONTOLOGY_ONLY
- source_proxy_only/evidence_url_pending
- ontology/source route/false-positive memory만 허용

D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK
- outcome/price-path 중심
- current extraction 금지

E_INVALID_OR_DUPLICATE
- 사용 금지

수정할 것:
- source_quality_classifier.py
- memory_record schema
- memory compiler
- replay fixture selector
- acceptance report

필수 audit:
- 기존 A_URL_BACKED_REPLAY_READY 202,547개를 A2/A1/A0로 재분류
- A2만 production replay fixture 가능
- A1/A0는 repair queue로 이동
- A2 샘플 200개를 Evidence OS replay로 검증
- C_SOURCE_PROXY_ONTOLOGY_ONLY가 score/replay fixture로 승격되는 count 0

출력:
docs/operational/research_brain_v2_source_quality_reclassification.json
docs/operational/research_brain_v2_url_anchor_repair_queue.json
docs/operational/research_brain_v2_a2_replay_sample_audit.json

================================================================================
5. CandidateEvent v2: 종목 row가 아니라 사건 단위로 분리
================================================================================

현재 CheapScanCandidate는 종목 단위 후보에 가깝다.
Research Brain v2는 사건 단위 CandidateEvent를 사용해야 한다.

CandidateEventV2:

{
  "candidate_event_id": "...",
  "symbol": "...",
  "company_name": "...",
  "event_date": "...",
  "detected_at": "...",
  "source_family": "DART|KIND|KRX|CompanyGuide|IR|ReportRadar|Price|TrustedNews|Manual",
  "source_id": "...",
  "event_type": "...",
  "raw_reason_codes": [],
  "primary_disclosure_type": "...",
  "event_title": "...",
  "event_summary": "...",
  "magnitude": {
    "contract_to_sales_pct": null,
    "facility_to_marketcap_pct": null,
    "eps_revision_pct": null,
    "opm_change_pctp": null,
    "fcf_change": null,
    "relative_strength_rank": null,
    "volume_spike_ratio": null
  },
  "event_freshness_days": 0,
  "issuer_directness": "DIRECT|INDIRECT|UNKNOWN",
  "initial_evidence_document_ids": [],
  "structured_payload": {},
  "price_context": {},
  "research_brain_eligible": true
}

한 종목에서 여러 사건이 있으면 여러 CandidateEvent를 만들어라.

예:
- A사 공급계약 공시
- A사 신규시설투자
- A사 실적 턴어라운드
- A사 리포트 EPS 상향
- A사 거래대금 급증

이 다섯 개는 하나의 종목 후보가 아니라 다섯 개의 event다.
나중에 CandidateCluster에서 합쳐라.

필수:
- daily_scan / korea_live_lite / report_radar output을 CandidateEventV2로 변환
- event_id deterministic
- event source anchor 보존
- event freshness 계산
- event magnitude normalization
- event-level dedupe
- event cluster by symbol/date/source family

출력:
docs/operational/research_brain_v2_candidate_event_schema.md
docs/operational/research_brain_v2_candidate_event_dry_run.json

================================================================================
6. Production Discovery Orchestrator
================================================================================

지금 discovery dry run은 candidate_event_count 8에서 provider/source gap을 기록했는데 verdict READY로 남아 있다.
v2에서는 운영 준비 판단을 엄격히 바꿔라.

새 Orchestrator flow:

1. Universe build
   - KRX listed universe
   - active watchlist optional
   - exclude ETF/SPAC/REIT/preferred if configured

2. Structured trigger scan
   - DART/KIND/KRX
   - financial actuals
   - CompanyGuide/reports
   - IR/report radar
   - price/volume/relative strength

3. CandidateEventV2 generation
   - event-level rows

4. Candidate clustering
   - symbol/date/event-family cluster
   - event priority score
   - source strength score
   - freshness score

5. Research Brain v2 archetype routing
   - top-k archetypes
   - card retrieval
   - disambiguation tasks

6. SourceTask plan
   - official-first
   - primitive-level
   - budgeted
   - stop-on-resolution

7. Source acquisition execution
   - actual fetch/parse
   - EvidenceDocument / EvidenceAnchor

8. Evidence OS v2
   - accepted claims
   - primitive state
   - score contribution

9. Deterministic score/stage
   - verified score
   - provisional score
   - score interval
   - base stage
   - investigation status
   - transition overlay

10. Daily Watchlist output
   - Green
   - Yellow-Pending
   - Stage2-Actionable
   - Stage2-Watch
   - 4B-watch
   - Reject/Red
   - follow-up tasks

Production readiness rules:
- candidate_event_count >= 30 required for READY unless explicit market-holiday/provider outage label.
- each large_sector_id must have >=3 event attempts or explicit provider/source gap.
- at least 20 events must complete Research Brain routing.
- at least 10 events must execute source tasks.
- at least 5 events must produce Evidence OS accepted claims.
- at least 3 events must produce deterministic score/stage output.
- if these are not met, verdict is NOT_READY or PARTIAL_READY, not READY.

출력:
docs/operational/research_brain_v2_production_discovery_report.md
docs/operational/research_brain_v2_daily_watchlist_sample.json
docs/operational/research_brain_v2_candidate_cluster_report.json

================================================================================
7. SourceTask 실행성 강화
================================================================================

지금 source task는 계획 단위다.
v2에서는 SourceTask가 실제 실행 결과와 연결돼야 한다.

SourceTaskExecution:

{
  "task_id": "...",
  "status": "NOT_STARTED|FETCHED|PARSED|EVIDENCE_OS_ACCEPTED|NO_EVIDENCE_FOUND|PROVIDER_FAILED|BUDGET_EXHAUSTED",
  "attempted_sources": [],
  "fetched_document_ids": [],
  "parsed_anchor_count": 0,
  "accepted_claim_ids": [],
  "rejected_claim_ids": [],
  "stop_reason": "...",
  "provider_error": null,
  "budget_used": {}
}

규칙:
- SourceTask가 accepted claim 0개이면 그 primitive는 UNKNOWN 또는 NOT_OBSERVED다.
- accepted claim 0개인데 score 상승하면 실패.
- provider failure이면 score_valid가 pending/provider_failed로 가야 한다.
- budget exhausted인데 material gap이면 pending.
- source task execution 없이 planning만으로 READY 금지.

필수 audit:
- source_task_count
- executed_source_task_count
- accepted_claim_source_task_count
- source_task_to_score_contribution_count
- planned_but_not_executed_task_count
- provider_failed_material_task_count

출력:
docs/operational/research_brain_v2_source_task_execution_audit.json

================================================================================
8. LLM Planner 통합
================================================================================

Research Brain v2는 deterministic token router만으로 끝나면 안 된다.

LLM Planner 역할:
- CandidateEventV2를 읽음
- ArchetypeMemoryCard를 읽음
- top-k archetype 후보와 이유 제시
- positive thesis / counter thesis 작성
- must-verify primitive 선정
- red-team primitive 선정
- SourceTask 초안 작성
- suggested query intent 작성

금지:
- score 출력
- stage 출력
- hard_break final 출력
- current_score_eligible 출력
- FeatureInput 수정
- ScoreContribution 수정

LLM Planner output schema:

{
  "top_k_archetype_hypotheses": [
    {
      "archetype_id": "...",
      "rank": 1,
      "confidence": "HIGH|MEDIUM|LOW",
      "reason": "...",
      "supporting_event_fields": [],
      "disambiguation_needed": false
    }
  ],
  "positive_thesis": "...",
  "counter_thesis": "...",
  "must_verify_primitives": [],
  "green_blockers_to_close": [],
  "red_team_checks": [],
  "source_task_drafts": [],
  "query_intents": [],
  "do_not_promote_reasons": [],
  "planner_self_check": {
    "score_keys_present": false,
    "stage_keys_present": false,
    "future_outcome_used": false
  }
}

Deterministic validator:
- schema validation
- allowed archetype ids
- no score/stage keys
- no future outcome leakage
- source task budget enforced
- official-first rule enforced
- disallowed general search for DART-solvable gaps
- if LLM fails, status = PLANNER_PROVIDER_FAILED and candidate is pending, not fake-planned.

Fake/mock LLM:
- tests only
- production report must say whether real provider or fake provider was used
- fake provider results cannot be PRODUCTION_READY

================================================================================
9. Acceptance tests 강화
================================================================================

새 테스트 파일 또는 동등 테스트를 추가하라.

tests/test_research_brain_v2_archetype_router.py
tests/test_research_brain_v2_r13_overrouting.py
tests/test_research_brain_v2_memory_cards.py
tests/test_research_brain_v2_source_quality_reclassification.py
tests/test_research_brain_v2_candidate_event_v2.py
tests/test_research_brain_v2_production_orchestrator.py
tests/test_research_brain_v2_source_task_execution.py
tests/test_research_brain_v2_llm_planner_schema.py
tests/test_research_brain_v2_evidence_os_integration.py
tests/test_research_brain_v2_daily_watchlist.py
tests/test_research_brain_v2_readiness_verdict.py

필수 assertions:

1. C06 replay primary == C06.
2. C08 replay primary == C08.
3. C15 replay primary == C15.
4. C17 replay primary == C17.
5. C24 replay primary == C24.
6. C28 replay primary == C28.
7. R13 is not primary unless fixture is explicit R13.
8. top3 archetype contains expected archetype for all C01-C36 fixtures.
9. router confidence LOW causes ARCTYPE_PENDING_DISAMBIGUATION.
10. SourceQuality A2 requires Evidence OS anchor replay.
11. URL string only is not A2.
12. source_proxy_only never becomes replay fixture.
13. CandidateEventV2 splits multiple events for same symbol.
14. production discovery count < 30 cannot be READY unless explicit market/provider outage.
15. source task planning without execution cannot be PRODUCTION_READY.
16. planned task accepted_claim_count=0 cannot increase score.
17. Research Brain output contains no score/stage keys.
18. fake LLM provider cannot mark production readiness READY.
19. general search ratio above configured max triggers warning or failure unless justified.
20. DART-solvable gap sent to general search count = 0.
21. FCF gap sent to news count = 0.
22. source task execution audit has no unbounded task.
23. daily watchlist sample includes event, archetype, claims, blockers, follow-up tasks.
24. Evidence OS v2 regression remains READY.
25. full unittest suite passes.

================================================================================
10. 운영 리포트 강화
================================================================================

새 report 생성:

docs/operational/research_brain_v2_acceptance_report.md
docs/operational/research_brain_v2_archetype_router_confusion_matrix.json
docs/operational/research_brain_v2_memory_cards.json
docs/operational/research_brain_v2_source_quality_reclassification.json
docs/operational/research_brain_v2_candidate_event_dry_run.json
docs/operational/research_brain_v2_production_discovery_report.md
docs/operational/research_brain_v2_source_task_execution_audit.json
docs/operational/research_brain_v2_daily_watchlist_sample.json
docs/operational/research_brain_v2_readiness_verdict.md
docs/operational/research_brain_v2_known_regressions.md

Acceptance report 필수 항목:

- commit SHA
- test command and pass/fail/skip
- Evidence OS v2 regression status
- memory card count
- A2/A1/A0/B/C/D/E source quality counts
- router top1/top3 accuracy
- R13 overroute count
- CandidateEventV2 count
- sector coverage
- source task planned/executed/accepted claim count
- official/general source ratio
- Evidence OS accepted claim count
- deterministic score/stage output count
- watchlist sample count
- provider error count
- fake provider used 여부
- production verdict:
  - NOT_READY
  - PARTIAL_READY
  - READY_FOR_SHADOW_DAILY_RUN
  - PRODUCTION_READY

READY_FOR_SHADOW_DAILY_RUN 조건:
- Evidence OS READY
- Research Brain v2 router pass
- CandidateEvent >= 30 or documented market/provider gap
- SourceTask execution audit pass
- watchlist sample generated

PRODUCTION_READY 조건:
- 최소 5개 날짜 또는 5회 frozen daily run
- 각 run CandidateEvent >= 30 or provider gap
- 각 run source task execution 완료
- score/stage output reproducible
- no R13 overroute
- no source_proxy_to_score
- no fake provider

================================================================================
11. Daily Watchlist Output
================================================================================

최종 출력은 추천이 아니라 상태판이다.

DailyWatchlistItem:

{
  "symbol": "...",
  "company_name": "...",
  "candidate_event_id": "...",
  "event_type": "...",
  "event_summary": "...",
  "primary_archetype": "...",
  "secondary_archetypes": [],
  "research_memory_cards_used": [],
  "verified_score": null,
  "provisional_score": null,
  "score_valid_status": "...",
  "base_stage": "...",
  "investigation_status": "...",
  "transition_overlay": "...",
  "accepted_claim_ids": [],
  "top_supporting_claims": [],
  "green_blockers": [],
  "red_team_checks": [],
  "source_task_status_summary": {},
  "follow_up_tasks": [],
  "do_not_promote_reasons": [],
  "operator_notes": "..."
}

섹션:
- Stage3-Green
- Stage3-Yellow-Pending
- Stage2-Actionable
- Stage2-Watch
- 4B-watch
- Reject/Red
- Provider/Source Pending

출력 파일:
output/daily_watchlist/YYYY-MM-DD/e2r_daily_watchlist.json
output/daily_watchlist/YYYY-MM-DD/e2r_daily_watchlist.md

================================================================================
12. 완료 조건
================================================================================

Goal 완료 조건:

1. Evidence OS v2 remains READY.
2. Research Brain v1 deprecated notes created.
3. Archetype router top1/top3 confusion matrix created.
4. C06/C08/C15/C17/C24/C28 mandatory replay top1 exact match.
5. C01-C36 top3 accuracy 100%.
6. R13 overroute count 0 except explicit R13 fixtures.
7. ArchetypeMemoryCard generated for C01-C36.
8. SourceQuality reclassified into A2/A1/A0/B/C/D/E.
9. A2 sample Evidence OS replay audit passes.
10. CandidateEventV2 implemented.
11. Multiple events per symbol split correctly.
12. Production Discovery Orchestrator runs targeted_smoke_only=false.
13. CandidateEvent count >=30 or verdict is not READY.
14. SourceTaskExecution audit exists.
15. Planned-only tasks do not count as executed.
16. Evidence OS accepted claims are produced from executed tasks.
17. Deterministic score/stage outputs are produced for at least 3 events in dry run.
18. DailyWatchlist sample generated.
19. general search fallback is justified and bounded.
20. DART/IR/CompanyGuide-solvable gaps do not go to general search.
21. Research Brain output has score/stage direct key count 0.
22. source_proxy_to_score count 0.
23. future leakage in extraction prompt count 0.
24. full unittest suite passes.
25. working tree clean.
26. 한글 커밋 메시지로 commit/push.
27. final report states exact readiness label.

최종 상태 라벨:
- IMPLEMENTATION_MERGED
- ROUTER_REPLAY_PASS
- MEMORY_CARD_PASS
- SOURCE_QUALITY_RECLASSIFICATION_PASS
- DISCOVERY_ORCHESTRATOR_PASS
- SOURCE_TASK_EXECUTION_PASS
- WATCHLIST_SAMPLE_PASS
- READY_FOR_SHADOW_DAILY_RUN
- PRODUCTION_READY

Goal 완료라고 말하려면 최소:
READY_FOR_SHADOW_DAILY_RUN

PRODUCTION_READY라고 말하려면:
5회 이상 daily shadow run 또는 frozen daily replay까지 통과해야 한다.

================================================================================
13. 최종 답변 형식
================================================================================

작업 완료 후 다음 형식으로만 보고하라.

1. 최종 상태
- IMPLEMENTATION_MERGED / ROUTER_REPLAY_PASS / MEMORY_CARD_PASS / SOURCE_QUALITY_RECLASSIFICATION_PASS / DISCOVERY_ORCHESTRATOR_PASS / SOURCE_TASK_EXECUTION_PASS / WATCHLIST_SAMPLE_PASS / READY_FOR_SHADOW_DAILY_RUN / PRODUCTION_READY

2. 커밋
- SHA
- message
- push status
- working tree status

3. 테스트
- command
- passed/failed/skipped

4. Evidence OS regression
- READY 유지 여부
- orphan score count
- legacy direct path count
- source_proxy_to_score count

5. Archetype router
- top1 accuracy
- top3 accuracy
- C06/C08/C15/C17/C24/C28 mandatory replay result
- R13 overroute count

6. Memory cards
- C01-C36 card count
- source quality breakdown
- source gap count

7. Source quality
- A2/A1/A0/B/C/D/E counts
- A2 replay sample pass count
- repair queue count

8. Candidate discovery
- candidate_event_count
- sector coverage
- event type breakdown
- targeted_smoke_only 여부

9. Source task execution
- planned/executed/fetched/parsed/accepted counts
- provider failures
- budget exhausted material gaps
- general search ratio

10. Daily watchlist
- Green count
- Yellow-Pending count
- Stage2-Actionable count
- Stage2-Watch count
- 4B-watch count
- Reject/Red count
- Provider pending count

11. Production verdict
- READY_FOR_SHADOW_DAILY_RUN / PRODUCTION_READY / NOT_READY
- blockers
- exact next step
```

---

# 한 줄 결론

지금 레포는 **Evidence OS는 잘 닫혔고, Research Brain도 뼈대와 메모리 import는 크게 들어갔다.**
하지만 최신 산출물에서 C06/C08/C15/C17 replay가 R13으로 라우팅되는데도 pass 처리되는 걸 보면, 아직 “연구 기억으로 아키타입을 제대로 판정하는 두뇌”는 완성됐다고 보면 안 된다. ([GitHub][4])

다음 Goal은 바로 이거야.

> **Research Brain v2에서 아키타입 라우팅 정확도, 메모리 카드 압축, source quality 실제 검증, CandidateEvent v2, SourceTask 실행 감사, Daily Watchlist까지 묶어서 “실제 일일 운영 상태판”으로 만드는 것.**
