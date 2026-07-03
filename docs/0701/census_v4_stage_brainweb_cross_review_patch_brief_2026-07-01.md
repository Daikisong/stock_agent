# Census v4 Stage / Brain-Web Cross-Review Patch Brief - 2026-07-01

이 문서는 다음 에이전트가 빡세게 리뷰할 수 있도록 현재 `output/census_v4/2026-07-01` 산출물과 관련 코드 경로를 다시 대조한 기록이다.

핵심 질문은 두 개다.

```text
1. Stage가 있는 종목이 있긴 한가?
2. live_full_bounded / Brain-Web 경로가 실제 운영 증거 수집을 하고 있는가?
```

## 최종 판정

짧게 말하면:

```text
Stage label은 있다.
full thesis 운영 Stage는 없다.
Brain/Web live web/Naver acquisition은 아직 없다.
```

쉬운 예:

```text
현재 상태 = 출석부와 주의 표시판은 있다.
아직 상태 = 최종 진단서와 100점 만점 성적표는 없다.
```

따라서 지금 산출물을 이렇게 말하면 맞다.

```text
3391개 종목/row에 Census event-board 상태가 붙었다.
85개 row는 Stage0이 아닌 event-board label을 가진다.
67개 row에는 event-weighted partial score가 있다.
```

하지만 이렇게 말하면 틀린다.

```text
전체 KRX에 full E2R thesis Stage가 생겼다.
삼성전자/하이닉스 HBM/C06 운영 Stage가 계산됐다.
Brain/Web/Naver가 실제 원문을 가져와 claim-backed full thesis를 만들었다.
```

## Artifact Truth Table

기준 산출물:

```text
output/census_v4/2026-07-01
```

`census_stage_status.jsonl` 기준:

```text
rows: 3391

base_stage:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

canonical_stage:
  0:       3306
  1:         54
  2:         30
  3-Red:      1

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

stage_scope:
  CENSUS_EVENT_BOARD: 3391

score_scale:
  NO_SCORE:              3324
  EVENT_WEIGHTED_PARTIAL:  67

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

operator_score_use:
  NOT_FULL_E2R_SCORE: 3391

verified_score_present_count: 0
full_e2r_verified_score_count: 0
```

`stage_signal` / `stage_decision_status` 기준:

```text
stage_signal:
  NO_CURRENT_CATALYST: 3306
  OFFICIAL_EVENT_WATCH: 36
  MATERIAL_CLAIM_WATCH: 30
  EVIDENCE_INSUFFICIENT: 10
  SOURCE_PENDING: 8
  RISK_REVIEW: 1

stage_decision_status:
  NO_CURRENT_CATALYST: 3306
  FINAL: 36
  PENDING_MATERIAL_GAPS: 30
  SOURCE_PENDING: 18
  RISK_REVIEW: 1
```

이 숫자에서 중요한 점:

```text
Stage1 54개 + Stage2-Watch 30개 + Red 1개 = event-board non-Stage0 label 85개
full thesis Stage row = 0개
```

## 삼성전자 / 하이닉스 현재 의미

`census_stage_status.jsonl`에서 두 종목은 다음처럼 보인다.

```text
삼성전자 005930:
  base_stage: Stage1
  canonical_stage: 1
  full_thesis_stage: FULL_THESIS_NOT_RUN
  score_scale: EVENT_WEIGHTED_PARTIAL
  event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  operator_stage_use: NOT_FULL_THESIS_STAGE

SK하이닉스 000660:
  base_stage: Stage1
  canonical_stage: 1
  full_thesis_stage: FULL_THESIS_NOT_RUN
  score_scale: EVENT_WEIGHTED_PARTIAL
  event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  operator_stage_use: NOT_FULL_THESIS_STAGE
```

해석:

```text
이것은 HBM/C06 thesis 점수가 아니다.
이것은 daily/census event-board의 공식 이벤트 watch label이다.
```

쉬운 예:

```text
병원 접수표에 "검사 필요"라고 찍힌 상태다.
"암/완치/정상" 같은 최종 진단이 나온 상태가 아니다.
```

`samsung_hynix_full_thesis_smoke_audit.json`도 같은 말을 한다.

```text
full_thesis_status: PENDING_FULL_THESIS_REFRESH
full_thesis_claim_ids: []
full_thesis_score_contribution_ids: []
full_thesis_stagecourt_trace_ids: []
blocking_reason: full_thesis_source_tasks_planned_but_not_executed
```

따라서 삼성전자/하이닉스에 대해 지금 말할 수 있는 정확한 문장은 이것이다.

```text
둘 다 daily event-board Stage1이다.
둘 다 HBM/C06 full thesis Stage는 아직 미실행이다.
둘 다 운영 점수 90/60/Green/Yellow 같은 결론을 내면 안 된다.
```

## Brain/Web Artifact Truth

canonical output 기준 leaf row:

```text
planner_runs.jsonl: 0
claim_extractor_runs.jsonl: 0
web_search_tasks.jsonl: 0
web_search_results.jsonl: 0
web_fetched_documents.jsonl: 0

accepted_claims.jsonl: 92
score_contributions.jsonl: 92
stagecourt_traces.jsonl: 92
source_task_executions.jsonl: 92
```

여기서 92개 claim/contribution/trace는 Brain/Web live claim이 아니다.

현재 `readiness_verdict.json`은 다음처럼 말한다.

```text
verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
brain_web_mode: disabled
brain_web_evidence_pass: false
meaningful_operational_stage_pass: false
full_thesis_smoke_pass: false
remaining_operational_gaps:
  - full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt path not run
  - source-backed replay parity across all archetypes is not proven
  - Brain/Web/LLM acquisition artifacts are not produced in this disabled ledger-refresh run
```

`goal_completion_audit.json`도 완료 불가를 명시한다.

```text
goal_completion_ready: false
blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending
```

## Code Cross-Review: live_full_bounded

현재 enum은 있다.

```text
src/e2r/research_brain/v4_schemas.py
  SourceAcquisitionModeV4.LIVE_FULL_BOUNDED = "live_full_bounded"
```

하지만 실제 runner 경로는 이렇게 동작한다.

```text
SourceAcquisitionRunnerV4.acquire()
  if mode in live_official_first / live_official_only / live_full_bounded:
      _acquire_live_official_sources()
      if PARSED or live_official_only:
          return live_result

  snapshots = _candidate_snapshots(...)
```

즉 `live_full_bounded`는 현재:

```text
live official connector 먼저 시도
-> 실패하면 live web/Naver가 아니라 stored snapshot fallback
```

이다.

쉬운 예:

```text
간판은 "배달 포함 세트"인데,
실제로는 매장 재고만 보고 없으면 냉장고에 있던 어제 반찬을 꺼내는 상태다.
```

관련 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
```

중요한 세부:

```text
SourceAcquisitionResultV4에는 web_search_tasks/results/fetched/rejected 필드가 생겼다.
EvidenceOSExecutionBundleV4도 그 필드를 모을 수 있다.
하지만 SourceAcquisitionRunnerV4가 아직 그 필드를 채우지 않는다.
```

`TrustedNewsLiveConnector`도 현재는 live provider가 아니다.

```text
status: PROVIDER_FAILED if mode == "live"
provider_error: trusted_news_provider_not_configured; general search is not a score source
```

따라서 지금 `live_full_bounded`를 운영 web/news 수집이라고 부르면 안 된다.

## Code Cross-Review: Web Audit Risk

중앙 `brain_web_readiness_gate`는 비교적 강하다.

요구하는 연결:

```text
planner
-> source task execution
-> real document
-> accepted claim
-> score contribution
-> StageCourt trace
-> promoted census row
```

그래서 task 한 줄만으로 중앙 gate가 바로 pass될 가능성은 낮다.

하지만 보조 `_web_audit()`에는 약한 조건이 있다.

현재 구조:

```text
zero = claimed and not web_tasks and not web_results and not web_fetched
real_acquisition = claimed and bool(web_tasks or web_results or web_fetched)
verdict = REAL_ACQUISITION_PASS if real_acquisition
```

이 말은:

```text
web_search_tasks.jsonl 한 줄만 있어도 REAL_ACQUISITION_PASS처럼 보일 수 있다.
```

쉬운 예:

```text
택배 송장만 발급됐는데 물건이 도착한 것처럼 "배송 완료"라고 찍는 위험이다.
```

이건 다음 패치에서 반드시 바꿔야 한다.

## Code Cross-Review: Export Gap

`_export_brain_web_bundle_leafs()`는 현재 다음을 merge한다.

```text
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
brain_to_claim_trace.jsonl
```

하지만 아직 bundle의 web leaf는 output으로 merge하지 않는다.

필요한 출력:

```text
web_search_tasks.jsonl
web_search_results.jsonl
web_fetched_documents.jsonl
web_rejected_documents.jsonl
```

지금 bridge에 필드는 있어도 export까지 닫히지 않으면 나중에 감사가 못 본다.

## Existing Docs Corrections

이번 교차검증에서 문서 숫자 오타를 바로잡았다.

수정한 내용:

```text
docs/0701/census_v4_current_truth_table_2026-07-01.md
  EVENT_BOARD_STAGE2_WATCH: 35 -> 30

docs/0701/census_v4_latest_cross_validation_and_patch_map_2026-07-01.md
  EVENT_BOARD_STAGE2_WATCH: 35 -> 30

docs/0701/census_v4_stage_truth_final_cross_validation_packet_2026-07-01.md
  EVIDENCE_INSUFFICIENT: 5 -> 10
  SOURCE_PENDING: 13 -> 18
```

근거는 `output/census_v4/2026-07-01/census_stage_summary.json`이다.

## Patch Direction

### P0 - Overclaim Guard

먼저 말부터 못 바꾸게 해야 한다.

필수 변경:

```text
1. _web_audit()에서 task-only REAL_ACQUISITION_PASS 금지
2. web_fetched_documents가 0이면 real full-source acquisition pass 금지
3. task/result/fetched/rejected를 서로 다른 verdict로 분리
4. brain_web_mode=enabled라도 run_mode가 web acquisition을 요구하지 않으면 WEB_NAVER_PASS를 말하지 않기
```

권장 verdict:

```text
DISABLED_HONESTY_PASS
WEB_TASKS_ONLY_NOT_FETCHED
WEB_RESULTS_ONLY_NOT_FETCHED
WEB_FETCHED_NO_ACCEPTED_CLAIM
REAL_WEB_ACQUISITION_PASS
```

### P1 - live_full_bounded Real Web Leaf Wiring

`SourceAcquisitionRunnerV4`에 실제 bounded web acquisition을 붙인다.

단, deterministic query template을 늘리면 안 된다.

원칙:

```text
LLM query_intents가 검색어를 만든다.
코드는 회사명/티커/as_of_date/중복/예산만 검증한다.
```

필수 동작:

```text
1. task.query_intents가 비어 있으면 web 검색을 만들지 않는다.
2. query가 target company/ticker를 포함하지 않으면 rejected leaf로 남긴다.
3. max_queries / max_candidates / max_fetches를 지킨다.
4. Naver/Search result row를 web_search_results.jsonl에 남긴다.
5. 원문 fetch 성공분만 EvidenceDocument/Anchor로 넘긴다.
6. 원문 fetch 실패, 미래일자, target scope 불명확 문서는 web_rejected_documents.jsonl에 남긴다.
7. accepted claim이 없으면 낮은 점수 확정이 아니라 pending/blocker로 남긴다.
```

쉬운 예:

```text
나쁜 방식:
  코드가 "삼성전자 HBM 장기공급계약 선수금" 검색어를 고정 생성

좋은 방식:
  LLM이 "삼성전자 2026 HBM customer allocation qualification revenue mix"를 제안
  코드는 삼성전자/005930이 들어갔는지, as_of_date 이후 자료가 아닌지, fetch 예산 안인지 검사
```

### P2 - Web Leaf Export

`_export_brain_web_bundle_leafs()`가 bundle의 web leaf를 export해야 한다.

필수 merge key:

```text
web_search_tasks.jsonl: web_task_id
web_search_results.jsonl: web_result_id
web_fetched_documents.jsonl: web_fetch_id
web_rejected_documents.jsonl: web_rejected_id
```

각 row에 최소한 있어야 할 필드:

```text
candidate_event_id
symbol
company_name
task_id
query
provider_name
as_of_date
status
url
published_at
fetched_at
document_id or rejection_reason
```

### P3 - Brain Evidence Pass vs Web/Naver Pass 분리

Brain evidence pass와 Web/Naver pass는 다르다.

예:

```text
DART official source로 accepted claim이 생김
-> Brain source/evidence pass 후보
-> Web/Naver acquisition pass는 아님

Naver 검색과 원문 fetch가 됐지만 accepted claim이 없음
-> Web acquisition attempted
-> scoring/stage pass는 아님
```

따라서 audit label도 분리해야 한다.

```text
BRAIN_EVIDENCE_CHAIN_PASS
WEB_NAVER_ACQUISITION_PASS
FULL_THESIS_STAGE_PASS
MEANINGFUL_OPERATIONAL_STAGE_PASS
```

### P4 - Samsung/Hynix Full Thesis Smoke

두 종목은 daily event-board Stage1로 남겨야 한다.

별도로 full thesis smoke를 돌릴 때만:

```text
C06/HBM source tasks executed
-> accepted full thesis claims
-> primitive states
-> score contributions
-> StageCourt trace
-> promoted full_thesis_stage
```

가 가능하다.

필수 primitive:

```text
named_customer_or_customer_quality
qualification_status
capacity_allocation_or_pre_sold
hbm_shipment_or_revenue_mix
cash_or_revision_conversion
repeat_evidence_family
source_quorum
```

### P5 - All-Archetype Replay

full thesis smoke가 한두 종목에서 되는 것만으로 충분하지 않다.

최종 목표:

```text
모든 아키타입에서 과거 연구자료의 source-backed positive / guard replay를 통과
source_proxy_only 자료는 운영 정답 fixture로 쓰지 않음
UNKNOWN을 PRESENT/ABSENT로 바꾸지 않음
wrong-subject, old-risk, snippet-score, future leakage fixture 통과
```

## Required Tests

다음 테스트를 추가하거나 강화해야 한다.

```text
1. live_full_bounded with fixture search provider:
   query_intents 기반으로 web_search_task/result/fetched row가 생긴다.

2. unscoped query:
   "HBM customer allocation"처럼 회사명/티커 없는 query는 rejected row만 생긴다.

3. future document:
   as_of_date 이후 published_at 문서는 fetched가 아니라 rejected로 남는다.

4. task-only web audit:
   web_search_tasks만 있고 fetched document가 없으면 REAL_ACQUISITION_PASS가 아니다.

5. fetched-no-claim:
   원문 fetch는 됐지만 accepted claim이 없으면 score/stage pass가 아니다.

6. DART-only Brain evidence:
   official source claim pass가 Web/Naver pass로 둔갑하지 않는다.

7. Samsung/Hynix:
   daily event-board Stage1과 HBM/C06 full thesis Stage가 분리된다.
```

## Current Focused Verification

이번 문서화 직전 집중 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty -v

Ran 30 tests in 27.794s
OK
```

이 테스트는 현재 guard가 깨지지 않았다는 뜻이다.

하지만 이 테스트가 의미하는 것은 아래가 아니다.

```text
Brain/Web live acquisition pass
full thesis pass
Samsung/Hynix operating Stage pass
```

## Reviewer Attack Checklist

다음 에이전트는 아래 질문으로 공격하면 된다.

```text
1. 문서가 Stage1/Stage2-Watch를 full thesis Stage처럼 표현하는가?
2. full_thesis_stage가 하나라도 FULL_THESIS_NOT_RUN이 아닌가?
3. verified_score 또는 full_e2r_verified_score가 하나라도 있는가?
4. planner_runs/web_search/claim_extractor row가 0인데 Brain/Web pass라고 쓰는가?
5. web_search_tasks 한 줄만으로 REAL_ACQUISITION_PASS가 나오는가?
6. live_full_bounded가 실제로 Naver/Web 원문 fetch를 하는가?
7. snapshot:// 문서가 Brain/Web production cutover 증거로 쓰이는가?
8. 삼성전자/하이닉스 Stage1을 HBM/C06 full thesis Stage로 읽는 문장이 있는가?
9. source_proxy_only 연구자료가 운영 점수 fixture로 들어갔는가?
10. as_of_date 이후 자료가 current claim으로 들어갈 수 있는가?
```

## One-Line Next Patch

다음 패치의 한 줄 목표:

```text
live_full_bounded라는 이름을 실제 행동으로 맞춘다.
LLM query_intents -> bounded web/Naver search -> full source fetch -> rejected/fetched leaf -> EvidenceDocument/Anchor -> claim -> score/stage audit까지 닫고,
task-only나 official-only가 Web/Naver pass로 둔갑하지 못하게 한다.
```

완료 기준은 단순하다.

```text
web_search_tasks > 0
web_search_results > 0
web_fetched_documents > 0 또는 web_rejected_documents에 명확한 실패 사유
accepted Brain/Web claim 없으면 score/stage pass 금지
full thesis stage 없으면 full thesis 미실행으로 표기
```

이 조건 전까지 현재 정직한 상태명은 이것이다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
Brain/Web: NOT_REQUESTED 또는 NOT_READY
Full thesis: PENDING_FULL_THESIS_REFRESH
Meaningful operational stage: false
```
