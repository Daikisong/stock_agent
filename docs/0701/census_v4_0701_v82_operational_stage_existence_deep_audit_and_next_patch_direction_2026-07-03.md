# Census v4 0701 v82 Operational Stage Existence Deep Audit / Next Patch Direction

작성일: 2026-07-03

대상 실행:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82
```

이 문서는 다음 에이전트가 빡세게 반박할 수 있도록 만든 최신 v82 감사 패킷이다. 결론부터 말하면:

```text
Stage row는 있다.
하지만 운영자가 써도 되는 FULL_THESIS Stage는 0개다.
운영 점수 FULL_E2R_100도 0개다.
```

쉬운 예:

```text
CENSUS_EVENT_BOARD = 출석부
BRAIN_WEB_PARTIAL = 몇 문제만 푼 쪽지시험
FULL_THESIS = 최종 성적표
```

v82에는 출석부 3,390개와 SK하이닉스 쪽지시험 1개가 있다. 최종 성적표는 없다.

## 1. 지금 Stage가 있는가

있다. 하지만 전부 운영용이 아니다.

`census_stage_status.jsonl` 기준:

| 구분 | count | 운영 해석 |
|---|---:|---|
| total stage rows | 3,391 | 상태판 행 전체 |
| `CENSUS_EVENT_BOARD` | 3,390 | Census 출석부/상태판 |
| `BRAIN_WEB_PARTIAL` | 1 | Brain/Web partial |
| `FULL_THESIS` | 0 | 운영 Stage 없음 |
| `operator_stage_use=NOT_FULL_THESIS_STAGE` | 3,391 | 모든 행 운영 Stage 사용 금지 |
| `operator_score_use=NOT_FULL_E2R_SCORE` | 3,391 | 모든 행 운영 점수 사용 금지 |
| `full_thesis_stage=FULL_THESIS_NOT_RUN` | 3,391 | full thesis 미실행 |

`canonical_stage` 분포:

| canonical_stage | count | 주의 |
|---|---:|---|
| `0` | 3,306 | 대부분 NoCurrentCatalyst 상태판 |
| `1` | 54 | event board 또는 partial |
| `2` | 30 | event board material watch |
| `3-Red` | 1 | event board risk review |

중요한 점:

```text
canonical_stage=1/2/3-Red가 있어도 stage_scope가 FULL_THESIS가 아니면 운영 Stage가 아니다.
```

예를 들어 `canonical_stage=2`는 "공시/이벤트가 있어 더 봐야 한다"는 상태판일 수 있다. 이것을 "운영 Stage2 종목"이라고 말하면 안 된다.

## 2. 최신 v82 readiness 결론

`readiness_verdict.json`:

```text
verdict = NOT_READY
operational_stage_use_allowed = false
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
```

blockers:

```text
Brain/Web operational minimum planner runs not met: 21/30
Brain/Web operational minimum web search tasks not met: 3/20
Brain/Web operational minimum web/news search calls not met: 3/20
Brain/Web operational minimum fetched documents not met: 1/10
Brain/Web operational minimum claim extractor attempts not met: 1/10
```

`goal_completion_audit.json` blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
source_backed_replay_parity_all_archetypes_pending
goal_requirement_matrix_pass_false
```

`goal_requirement_matrix_audit.json`도 같은 방향이다:

```text
full_thesis_smoke_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
brain_web_evidence_pass_false
source_backed_replay_parity_all_archetypes_pending
```

즉 현재 상태는 "테스트는 많이 통과했지만 목표 완료는 아니다"가 아니라, 더 정확히:

```text
leaf artifact 경로 일부는 통과했다.
하지만 운영 full thesis chain이 닫히지 않아 goal.md/goal2.md/goal3.md는 미완료다.
```

## 3. SK하이닉스 partial row의 정확한 의미

v82 유일한 `BRAIN_WEB_PARTIAL` 행:

```json
{
  "symbol": "000660",
  "company_name": "SK하이닉스",
  "canonical_stage": "1",
  "base_stage_display": "BRAIN_WEB_PARTIAL_1",
  "stage_scope": "BRAIN_WEB_PARTIAL",
  "operator_stage_use": "NOT_FULL_THESIS_STAGE",
  "operator_score_use": "NOT_FULL_E2R_SCORE",
  "event_evidence_score": 60.0,
  "verified_score": null,
  "accepted_claim_count": 3,
  "score_contribution_count": 6,
  "score_scope": "BRAIN_WEB_CLAIM_BACKED_PARTIAL",
  "score_scale": "EVENT_WEIGHTED_PARTIAL",
  "full_thesis_stage": "FULL_THESIS_NOT_RUN",
  "is_full_thesis_stage": false,
  "is_full_e2r_score": false
}
```

이 행은 다음을 증명한다.

```text
Research Brain이 실제 원문 하나를 fetch했다.
LLM contract-blind extractor가 claim을 만들었다.
accepted claim 일부가 primitive/score contribution/StageCourt trace로 연결됐다.
```

하지만 다음을 증명하지 못한다.

```text
SK하이닉스 운영 Stage
SK하이닉스 FULL_E2R_100 점수
SK하이닉스 C06 full thesis 완료
SK하이닉스 Green/Yellow/Red 확정
```

쉬운 예:

```text
"HBM 고객 배정 관련 문장 하나를 찾았다"는 것은 진전이다.
하지만 "HBM thesis 전체가 검증됐다"는 뜻은 아니다.
```

## 4. SK하이닉스 claim chain

SK하이닉스 Brain/Web accepted claim 5개 중 score support로 쓰인 핵심은 3개다.

| claim | primitive | quote 요약 | 직접 source task 만족 |
|---|---|---|---|
| `CLM-e64d9727aa00c5957cc2` | `customer_preorder_or_allocation` | 핵심 고객 중장기 물량 우선 배정 | yes |
| `CLM-4d0c4c8684dc9265e131` | `revenue_visibility_contract` | 주요 고객사 장기공급계약 요구 | no, rerouted |
| `CLM-08e5923d01572f6efdf8` | `medium_term_revision_visibility` | 적정주가/2026 P/B 문장 | no, rerouted |

같은 문서에서 추가 추출된 `medium_term_revision_visibility` 2개는 accepted이지만 StageCourt trace에는 `non_score_accepted_claim_ids`로 남았다.

원문:

```text
https://stock.pstatic.net/stock-research/company/17/20251031_company_162545000.pdf
```

이 URL은 v82 패치 후 `VerifiedReportOriginal` route whitelist를 통과한 리포트 원문이다. 하지만 이 문서 하나로 C06 full thesis가 닫히지 않는다.

## 5. SK하이닉스가 FULL_THESIS로 못 올라간 직접 이유

`stagecourt_traces.jsonl`의 SK Brain trace:

```text
stagecourt_trace_id = SCT-BRAIN-c8a68b504ac586681b20
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
score_interval = 60.0 ~ 60.0
score_status = FINAL
present_green_primitives =
  customer_preorder_or_allocation
  revenue_visibility_contract
missing_green_primitives =
  hbm_capacity_constraint
  hbm_capacity_pre_sold
base_stage = 1
```

`full_thesis_production_runner_audit.json`의 blocked candidate:

```text
symbol = 000660
candidate_source = brain_web_partial_stage_row
primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
blockers =
  missing_green_gate_primitives
missing_green_primitives =
  hbm_capacity_constraint
  hbm_capacity_pre_sold
present_primitives =
  customer_preorder_or_allocation
  medium_term_revision_visibility
  revenue_visibility_contract
```

즉 점수가 낮아서 막힌 것이 아니다. C06 full thesis에서 필요한 Green primitive coverage가 부족해서 막혔다.

쉬운 예:

```text
지원서에 고객 배정 증거는 있다.
하지만 생산능력 제약과 선판매/locked capacity 증거가 없다.
그래서 최종 합격증(FULL_THESIS)은 못 준다.
```

## 6. SK하이닉스 source task별 결과

`source_task_executions.jsonl`에서 SK seed event `CEV4-FTQUEUE-000660-9563b2a7a852fc0c`:

| task | primitive_gap | source_class | status | 결과 |
|---|---|---|---|---|
| `ST-000660-C06-IR-HBM-CAPA-001` | `hbm_capacity_pre_sold` | DART | `NO_EVIDENCE_FOUND` | `hbm_capacity_pre_sold` 미충족 |
| `ST-000660-C06-OFFICIAL-QUAL-002` | `qualification_status` | DART | `NO_EVIDENCE_FOUND` | `qualification_status` 미충족 |
| `ST-000660-C06-REPORT-ORIGINAL-004` | `customer_preorder_or_allocation` | BrokerReportPublicPDF | `EVIDENCE_OS_ACCEPTED` | 고객 배정 claim 통과 |
| `RSTASKV4CGSTATUS-*` | `official_report_snapshot_current` | CompanyGuide | `NO_EVIDENCE_FOUND` | as-of 이후/future 문제로 불채택 |
| `RSTASKV4DARTSTATUS-*` | `official_disclosure_status_current` | DART | `NO_EVIDENCE_FOUND` | 현재 상태 확인 미충족 |
| `RSTASKV4KIND-*` | `exchange_risk_status_current` | KIND | `NO_EVIDENCE_FOUND` | risk status 미충족 |
| `RSTASKV4KRX-*` | `listing_trading_status_current` | KRX | `NO_EVIDENCE_FOUND` | listing status 미충족 |
| `RSTASKV4IRSTATUS-*` | `issuer_official_update_current` | IR | `PROVIDER_FAILED` | matching IR snapshot 없음 |

두 provider gap이 중요하다.

```text
issuer_ir_discovery_not_configured; do not treat missing IR as no evidence
trusted_news_provider_not_configured; general search is not a score source
```

이 말은 "증거가 없다"가 아니라 "그 경로를 아직 운영형으로 못 열었다"에 가깝다.

## 7. 삼성전자는 왜 Stage/점수가 없는가

삼성전자 full thesis seed trace:

```text
symbol = 005930
materialization_status = PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
planner_run_count = 1
planner_real_provider_success_count = 0
source_task_execution_count = 0
accepted_claim_count = 0
stagecourt_trace_count = 0
final_stage_scope = CENSUS_EVENT_BOARD
final_score_scale = EVENT_WEIGHTED_PARTIAL
final_operator_stage_use = NOT_FULL_THESIS_STAGE
```

따라서 삼성전자에 대해서는:

```text
Brain/Web planner placeholder는 있다.
real provider success가 없다.
source task 실행이 없다.
accepted claim이 없다.
StageCourt trace가 없다.
```

말하면 안 되는 것:

```text
삼성전자 운영 Stage 1
삼성전자 운영 점수 N점
삼성전자 C06 full thesis 실패
```

정확한 표현:

```text
삼성전자는 v82에서 full thesis seed가 있었지만, Brain/Web real provider가 성공하지 못해 운영 평가가 시작되지 못했다.
```

쉬운 예:

```text
시험지를 배부할 후보 명단에는 들어갔다.
하지만 시험지를 실제로 풀지 않았다.
그래서 점수도 등급도 없다.
```

## 8. full thesis seed materialization 전체 상태

`full_thesis_seed_materialization_trace.jsonl`:

| materialization_status | count | 의미 |
|---|---:|---|
| `PLANNER_NOT_RUN` | 64 | seed는 있으나 planner row 없음 |
| `PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS` | 20 | planner placeholder는 있으나 real provider success 없음 |
| `STAGECOURT_READY_NOT_PROMOTED` | 1 | SK하이닉스 partial trace는 있으나 FULL_THESIS 승급 실패 |
| `FULL_THESIS_PROMOTED` | 0 | 운영 full thesis 승급 없음 |

`full_thesis_seed_materialization_audit.json` 자체는 `PASS`다. 이 PASS는 "거짓 승급을 막았다"는 뜻이지 "full thesis가 됐다"는 뜻이 아니다.

쉬운 예:

```text
감사 PASS = 출석부를 성적표라고 속이지 않았다.
감사 PASS != 성적표가 발급됐다.
```

## 9. 코드 게이트와 산출물 해석 대조

현재 코드의 주요 게이트:

| 코드 위치 | 조건 | v82와의 관계 |
|---|---|---|
| `src/e2r/census/census_runner_v4.py:5399` | `BRAIN_AND_WEB_ACQUISITION_ENABLED`도 production full thesis 요청으로 간주 | v82에서 production runner가 실행되는 이유 |
| `src/e2r/census/census_runner_v4.py:5889` | seed materialization 단계 구분 | SK는 `STAGECOURT_READY_NOT_PROMOTED`, 삼성은 `PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS` |
| `src/e2r/census/census_runner_v4.py:6332` | production full thesis 승급 함수 | `FULL_THESIS` row 생성 담당 |
| `src/e2r/census/census_runner_v4.py:6416` | accepted claim / score contribution / primitive state ids 필요 | SK는 ids가 있지만 다음 gate에서 막힘 |
| `src/e2r/census/census_runner_v4.py:6424` | contract green primitives 충족 필요 | SK 직접 blocker |
| `src/e2r/census/census_runner_v4.py:6441` | live Brain source task document execution 필요 | SK는 통과 |
| `src/e2r/census/census_runner_v4.py:6444` | score interval과 score_status 필요 | SK는 `FINAL`, 60~60으로 통과 |
| `src/e2r/census/census_runner_v4.py:6471` | 통과 시에만 `stage_scope=FULL_THESIS`로 변경 | v82에서는 아무 행도 여기까지 못 감 |
| `src/e2r/census/census_runner_v4.py:6578` | candidate는 Brain partial row 또는 Brain StageCourt trace에서만 생성 | queue row 자체는 승급 후보가 아님 |

이 코드 게이트는 v82 산출물 해석과 대체로 일치한다. 현재 문제는 "게이트가 없어서 가짜 Stage가 나왔다"가 아니라:

```text
게이트는 막고 있다.
하지만 운영 full thesis를 완성할 source acquisition / provider / seed execution 경로가 아직 부족하다.
```

## 10. 지금 하면 안 되는 패치

다음은 금지해야 한다.

```text
1. BRAIN_WEB_PARTIAL을 FULL_THESIS로 alias 처리
2. EVENT_WEIGHTED_PARTIAL을 FULL_E2R_100으로 이름만 바꾸기
3. missing_green_gate_primitives를 무시하고 승급
4. planner/web/fetch/extractor minimum threshold를 낮춰 NOT_READY를 READY로 만들기
5. 삼성전자 seed를 "Stage1"이라고 표현
6. SK하이닉스 60점을 운영 점수라고 표현
7. pstatic/Naver snippet만으로 점수 추가
8. source_proxy_only 연구자료를 replay 정답처럼 사용
9. 종목명 조건문으로 삼성/하이닉스만 예외 처리
```

예를 들어:

```text
나쁜 패치:
if symbol == "000660": missing_green_primitives 무시

좋은 패치:
IssuerIR/TrustedNews/ReportPDF source task가 실제 원문을 찾아
hbm_capacity_pre_sold와 hbm_capacity_constraint accepted claim을 만들고,
그 claim이 C06 contract green gate를 통과하게 한다.
```

## 11. 다음 패치 방향

### P0. full thesis seed executor를 운영형으로 닫기

현재 85개 seed 중 real provider success는 1개뿐이다.

필요한 것:

```text
full_thesis_refresh_queue
  -> real planner success
  -> bounded official-first source tasks
  -> accepted claims
  -> primitive states
  -> score contributions
  -> StageCourt trace
  -> FULL_THESIS candidate
```

현재는 이 사슬이 SK 1개에서만 partial로 닫혔고, 삼성 포함 나머지는 대부분 planner/provider 단계에서 멈췄다.

### P1. SK C06 missing green primitive source route 열기

SK에서 빠진 것:

```text
hbm_capacity_constraint
hbm_capacity_pre_sold
```

현재 실패 원인:

```text
IssuerIR discovery not configured
TrustedNews provider not configured
IR matching document 없음
DART만으로 HBM capacity/pre-sold claim을 못 찾음
```

패치 방향:

```text
1. LLM planner가 만든 source task를 유지한다.
2. deterministic hardcoded query를 추가하지 않는다.
3. IssuerIR / broker report original / trusted news route를 bounded official-first로 실제 실행한다.
4. 원문 fetch 실패와 provider failure는 낮은 점수 확정이 아니라 pending/source gap으로 남긴다.
```

### P2. claim 기준일 검증 강화

SK Brain/Web accepted claim 중 일부는 `event_date`는 있으나 row-level `as_of_date`가 null이다. v82에서는 Green primitive 부족 때문에 FULL_THESIS 승급이 막혔지만, 다음에는 이게 승급 전 blocker가 되어야 한다.

필요한 검사:

```text
document.published_at 또는 available_at <= run as_of_date
claim.event_date <= run as_of_date
claim anchor가 실제 document text/span/hash에 존재
source_url이 verified original route를 통과
```

예:

```text
as_of_date=2026-07-01이면 2026-07-02 리포트는 아무리 내용이 좋아도 점수에 쓰면 안 된다.
```

### P3. seed metadata와 Brain hypothesis 혼동 제거

SK seed trace의 `source_primary_archetype`은 기존 event-board row에서 온 값이고 `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`로 남아 있다. 하지만 Brain StageCourt trace는 `C06_HBM_MEMORY_CUSTOMER_CAPACITY`다.

현재 production runner는 StageCourt trace의 C06을 보고 blocker를 계산하므로 직접 승급 오류는 아니다. 하지만 문서/감사에서 혼동을 만든다.

패치 방향:

```text
full_thesis_seed_materialization_trace에
  source_event_board_archetype
  brain_hypothesized_archetype
  production_candidate_archetype
를 분리해서 기록한다.
```

### P4. all-archetype replay parity 확장

`all_archetype_replay_matrix.json`:

```text
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
source_proxy_leak_count = 0
```

status counts:

```text
SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY = 6
SOURCE_GAP_PENDING = 26
GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

이 상태에서 "전 아키타입 운영 가능"이라고 말하면 안 된다.

다음 패치는 C06 live 하나만 통과시키는 것과 별개로, 26개 missing archetype에 대해 다음 둘 중 하나를 명시해야 한다.

```text
source-backed replay ready
또는
unsupported/source-gap 상태
```

## 12. 다음 에이전트 공격 체크리스트

다음 에이전트는 최소 이 질문들을 공격해야 한다.

```text
1. v82에서 FULL_THESIS row가 정말 0인가?
2. operator_stage_use가 모든 row에서 NOT_FULL_THESIS_STAGE인가?
3. SK BRAIN_WEB_PARTIAL 60점이 FULL_E2R_100으로 새지 않는가?
4. 삼성전자 seed가 Stage/score로 잘못 표시되는 경로가 없는가?
5. production runner가 missing_green_gate_primitives를 정확히 막는가?
6. pstatic verified report route가 너무 좁아 false negative를 만들지는 않는가?
7. pstatic verified report route가 너무 넓어 spoof를 통과시키지는 않는가?
8. accepted claim의 `as_of_date=null`이 FULL_THESIS 승급 전에 막히는가?
9. source task `NO_EVIDENCE_FOUND`와 `PROVIDER_FAILED`가 낮은 점수 확정으로 바뀌지 않는가?
10. all-archetype missing 26개를 완료처럼 말하는 문서/리포트가 없는가?
```

## 13. 교차검증에서 확인된 코드 약점

두 개의 read-only 교차검증 결과, v82 산출물 해석과 코드 게이트 방향은 대체로 일치했다. 다만 다음 약점은 문서에 숨기면 안 된다.

### 13.1 live source execution gate가 후보 claim에 직접 묶여 있지 않다

현재 production full thesis runner는 live source execution을 확인할 때:

```text
brain origin source execution 중 fetched_document_ids가 하나라도 있는가?
```

를 본다.

문제는 이 조건이:

```text
이 FULL_THESIS 후보의 accepted_claim_ids를 만든 source task/document가 실제 fetch됐는가?
```

까지 직접 확인하지는 않는다는 점이다.

쉬운 예:

```text
A 문서가 실제 fetch됐다.
B claim이 점수에 쓰였다.
현재 gate는 "A 문서가 있으니 live source 있음"까지만 볼 위험이 있다.
정답은 "B claim이 나온 바로 그 document/anchor/source task가 live fetch됐는가"를 봐야 한다.
```

다음 패치 요구:

```text
accepted_claim_id
  -> document_id / anchor_id
  -> source_task_execution.fetched_document_ids
  -> same candidate_event_id
  -> same source_origin=research_brain_v4_attempt
```

이 연결이 닫히지 않으면 FULL_THESIS 승급을 막아야 한다.

### 13.2 score interval은 lower만 검사하고 upper는 약하다

현재 runner는 `score_interval.lower` 존재와 `score_status`만 강하게 본다. `upper`가 없거나 이상해도 같은 강도로 막지 않는다.

다음 패치 요구:

```text
score_interval.lower exists
score_interval.upper exists
lower <= upper
score_status in FINAL / FINAL_WITH_NONMATERIAL_GAPS
score_status가 FINAL이면 material unresolved gap 없음
```

예:

```text
lower=60, upper=null이면 "60점 확정"이라고 말하면 안 된다.
가능 점수 범위가 닫히지 않았기 때문이다.
```

### 13.3 production audit 단독으로 모든 조건을 재검증하지 않는다

현재 `_full_thesis_production_audit`는 만들어진 `FULL_THESIS` row에 대해 claim/score/stage trace ID 존재를 주로 본다. Green primitive coverage, live source linkage, primitive state linkage는 promotion runner와 다른 leaf audits를 신뢰하는 구조다.

문서 표현 주의:

```text
나쁜 표현:
production audit 단독으로 FULL_THESIS의 모든 증거 조건을 재검증한다.

좋은 표현:
promotion runner가 승급 조건을 적용하고, production audit은 생성된 FULL_THESIS row와 다른 leaf audits의 결과를 종합한다.
```

다음 패치 요구:

```text
production audit에도 promoted FULL_THESIS row별로
  accepted_claim_id -> document/anchor -> source_task_execution
  primitive_state_id -> primitive_id -> green gate
  score_contribution_id -> support_claim_ids
를 재요약하는 row-level proof bundle을 붙인다.
```

## 14. 교차검증 결과 요약

읽기 전용 교차검증 1: v82 artifact truth

```text
stage_status_count = 3391
stage_scope_distribution = CENSUS_EVENT_BOARD 3390, BRAIN_WEB_PARTIAL 1
operator_stage_use_distribution = NOT_FULL_THESIS_STAGE 3391
operator_score_use_distribution = NOT_FULL_E2R_SCORE 3391
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
Samsung materialization_status = PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
SK BRAIN_WEB_PARTIAL row = NOT_FULL_THESIS / NOT_FULL_E2R
readiness = NOT_READY
all_archetype_replay_pass = false
source_backed_ready_count = 6
missing_required_archetype_count = 26
```

읽기 전용 교차검증 2: code gate truth

```text
CENSUS_EVENT_BOARD/BRAIN_WEB_PARTIAL은 operator FULL_THESIS로 alias되지 않는다.
production full thesis는 Brain partial row 또는 Brain StageCourt trace에서만 후보가 된다.
seed/planner/source/claim/stagecourt/FULL_THESIS+FULL_E2R 전에는 promoted가 아니다.
v82 해석과 코드 방향은 맞다.
다만 live source linkage, score interval upper, production audit row-level revalidation은 더 강화해야 한다.
```

## 15. 검증 명령

관련 regression:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_sources \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_stage_signal_split \
  tests.test_census_v4_score_field_split \
  -v
```

전체 regression:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

v82 live smoke 재현 명령:

```bash
rm -rf output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 \
E2R_CODEX_EXTRACTOR_TIMEOUT_SECONDS=120 \
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-timeout-seconds 120 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

예상 결과:

```text
LIVE_RC=1
NOT_READY
```

`NOT_READY`가 정상이다. 현재 설정과 산출물에서 `READY`가 나오면 오히려 감사 대상이다.

## 16. 최종 판단

v82는 이전보다 좋아졌다.

좋아진 점:

```text
1. 가짜 report original spoof를 더 잘 막는다.
2. snippet-only score를 막는다.
3. SK에서 실제 원문 -> LLM claim -> primitive -> score contribution -> StageCourt partial 사슬이 한 번 닫혔다.
4. partial을 operator FULL_THESIS로 과장하지 않는다.
```

하지만 운영 가능 상태는 아니다.

남은 핵심:

```text
1. FULL_THESIS row = 0
2. FULL_E2R_100 row = 0
3. 삼성전자 full thesis source task 미실행
4. SK하이닉스 C06 Green/full-thesis primitive coverage 부족
5. Brain/Web operational minimum 미달
6. all-archetype source-backed replay 6/32, missing 26
```

따라서 다음 패치의 목표는 readiness 숫자를 좋게 보이게 만드는 것이 아니라:

```text
FULL_THESIS_REFRESH_TASK_PLANNED
  -> SOURCE_TASK_EXECUTED
  -> ACCEPTED_CLAIM
  -> PRIMITIVE_STATE
  -> SCORE_CONTRIBUTION
  -> STAGECOURT_TRACE
  -> FULL_THESIS row
```

이 사슬을 production mode에서 진짜 원문 기반으로 닫는 것이다.
