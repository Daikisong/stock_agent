# 2026-07-03 Goal 진행상황 상세 기록

작성 시각: 2026-07-03 20:38:44 KST

대상 문서:

- `docs/core/goal.md`
- `docs/core/goal2.md`
- `docs/core/goal3.md`

현재 결론:

**Goal은 아직 완료가 아니다.**  
다만 Census v4는 이전처럼 "report가 pass라고 말하는 상태"에서 한 단계 올라와, leaf artifact와 Brain/Web 실행 흔적을 남기는 구조까지는 왔다. 아직 운영 Stage로 쓸 수 있는 `FULL_THESIS` row가 0개라서, 최종 목표인 `MEANINGFUL_OPERATIONAL_STAGE_PASS`와 `FULL_THESIS_REFRESH_PASS`는 미완료다.

쉬운 예:

```text
접수표:
  전 종목이 Census 평가 대상에 올라왔는가?
  -> 예. 이건 많이 진행됐다.

검사결과:
  일부 종목에서 실제 문서, claim, score contribution이 생겼는가?
  -> 예. Brain/Web evidence 경로는 통과했다.

최종진단서:
  이 종목은 100점 full thesis 기준으로 Stage Green/Yellow/Red라고 말할 수 있는가?
  -> 아직 아니다. FULL_THESIS 운영 승격 row가 0개다.
```

즉 지금 결과를 "삼성전자 Stage 1", "하이닉스 Stage 2"처럼 운영 판단으로 말하면 안 된다. 더 정확한 표현은 "Census v4가 일부 source-backed partial claim을 찾았지만, FULL_THESIS 운영 Stage로 승격하지 못했다"이다.

## 1. 이번 Goal의 진짜 성공 조건

세 goal 문서가 요구하는 것은 단순한 전 종목 CSV 생성이 아니다.

핵심 성공 조건은 다음이다.

1. 구형 Census runner가 pass를 만들 수 없게 차단한다.
2. report 문구가 아니라 leaf artifact를 source of truth로 삼는다.
3. `stage`, `score`, `claim`, `score_contribution`, `stagecourt_trace`가 하나의 원자적 결정에서 나온다.
4. `verified_score`와 단일 이벤트 점수를 분리한다.
5. Stage2-Watch와 canonical Stage2를 섞지 않는다.
6. LLM Brain이 실제로 planner, source task, claim extraction에 참여했는지 trace로 증명한다.
7. Naver/Web/TrustedNews/IR/Report source는 snippet이 아니라 full source fetch와 anchor 검증을 통과해야 점수 재료가 된다.
8. 삼성전자, SK하이닉스 같은 고관심 종목은 daily DART event 점수와 C06/HBM full thesis 점수를 분리한다.
9. `FULL_THESIS` 운영 Stage는 Green gate primitive와 source-backed claim이 충분할 때만 승격한다.
10. 전체 아키타입 replay와 5개 독립 검증 에이전트 리뷰를 통과해야 최종 완료로 볼 수 있다.

## 2. 현재 v105 실행 기준 상태

최근 기준 output:

```text
output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry
```

전체 row:

```text
total rows = 3391
```

stage scope:

```text
CENSUS_EVENT_BOARD    3368
BRAIN_OFFICIAL_PARTIAL  19
BRAIN_WEB_PARTIAL        4
FULL_THESIS              0
```

score scale:

```text
NO_SCORE                3321
EVENT_WEIGHTED_PARTIAL    70
FULL_E2R_100               0
```

operator stage use:

```text
NOT_FULL_THESIS_STAGE 3391
```

canonical stage:

```text
0        3324
1          46
2          20
3-Red       1
```

가장 중요한 숫자는 `FULL_THESIS = 0`, `FULL_E2R_100 = 0`, `NOT_FULL_THESIS_STAGE = 3391`이다.

쉬운 예:

```text
70개 row에 점수가 조금 있어도, 그 점수는 "full E2R 100점 시험" 점수가 아니다.
그건 "공시/웹/부분 증거 이벤트 점수"에 가깝다.
그래서 운영자가 이 숫자를 Green/Yellow 투자 thesis로 읽으면 안 된다.
```

## 3. Brain/Web evidence 경로는 어디까지 왔나

v105 기준 Brain/Web leaf count:

```text
planner_runs              300
llm_prompts                35
llm_responses              35
source_tasks              327
source_task_executions     327
evidence_documents        171
evidence_anchors          258
web_search_tasks           70
web_search_results        997
web_fetched_documents      47
claim_extractor_runs       47
claim_extractor_success    47
accepted_claims           191
score_contributions       153
stagecourt_traces         115
brain_to_claim_trace       99
brain_claim_mapping_trace 1319
```

이 부분은 이전 v3와 다르다. v3가 "3.67초 report pass"처럼 보였던 것과 달리, v4는 실제로 planner, prompts, responses, source tasks, web search result, fetched documents, accepted claims를 leaf로 남긴다.

다만 이것은 `BRAIN_WEB_EVIDENCE_PASS`에 가까운 성과이고, `FULL_THESIS_REFRESH_PASS`는 아니다.

쉬운 예:

```text
도서관에서 관련 논문을 찾고, 몇 문장을 발췌하고, 근거 카드까지 만들었다.
하지만 아직 최종 논문 심사 통과는 아니다.
```

## 4. 삼성전자와 SK하이닉스 현재 해석

v105 기준:

```text
005930 삼성전자
  stage_scope: BRAIN_WEB_PARTIAL
  canonical_stage: 1
  partial score: 44.1667
  accepted_claim_count: 3
  operator_stage_use: NOT_FULL_THESIS

000660 SK하이닉스
  stage_scope: BRAIN_WEB_PARTIAL
  canonical_stage: 2
  partial score: 75.8333
  accepted_claim_count: 6
  operator_stage_use: NOT_FULL_THESIS
```

주의:

이 숫자는 C06/HBM full thesis 운영 점수가 아니다. 예전에 문제가 됐던 `90점대였다가 60점대로 바뀌는 문제`를 막기 위해, 현재 구조에서는 부분 점수와 full thesis 점수를 분리한다.

따라서 지금은 다음처럼 말해야 한다.

```text
나쁜 표현:
  삼성전자 Stage1, 하이닉스 Stage2로 확정됐다.

좋은 표현:
  삼성전자와 하이닉스는 Brain/Web partial evidence는 생겼지만,
  C06/HBM FULL_THESIS 운영 Stage로는 승격하지 못했다.
```

## 5. FULL_THESIS 생산 경로가 막힌 이유

v105 기준 FULL_THESIS production runner:

```text
candidate_row_count = 23
blocked_candidate_count = 23
promoted_full_thesis_row_count = 0
```

모든 후보가 막힌 직접 사유:

```text
missing_green_gate_primitives
```

누락 primitive count:

```text
margin_bridge_visible             19
contract_duration_months          17
contract_amount_to_prior_sales    13
hbm_capacity_constraint            2
customer_preorder_or_allocation    1
hbm_capacity_pre_sold              1
customer_contract                  1
order_backlog_to_sales             1
```

중요한 점:

이 blocker 자체는 나쁜 것이 아니다. 오히려 "증거가 부족한데 Green/Yellow로 억지 승격하지 않는다"는 보호장치다. 문제는 다음 단계에서 이 gap을 실제 source task로 다시 조사하고, 검증된 claim으로 채워야 한다는 점이다.

쉬운 예:

```text
운전면허 시험에서 필기는 통과했지만 도로주행 기록이 없다.
그러면 "면허 발급"이 아니라 "도로주행 재시험 필요"가 맞다.
```

## 6. 이번에 추가로 패치한 내용

최근 패치의 목적은 `FULL_THESIS` blocker가 생겼을 때 그것을 문서에만 남기지 않고, 다음 Brain/Web 시도에 실제 seed로 다시 넣는 것이다.

### 6.1 Follow-up seed top-level field 보강

파일:

```text
src/e2r/census/census_runner_v4.py
```

변경:

`blocked_candidate_follow_up_seed_events.jsonl` row에 다음 필드를 top-level로 추가했다.

```text
follow_up_task_id
follow_up_archetype_id
follow_up_primitive_gap
```

이유:

기존에는 이 값들이 `structured_payload` 안에만 있었기 때문에, 다른 auditor나 다음 실행 단계가 seed를 빠르게 추적하기 어려웠다. 이제 JSONL 한 줄만 봐도 "어느 후보의 어떤 primitive gap 때문에 follow-up이 생겼는지" 바로 알 수 있다.

### 6.2 Planner/prompt/response append-only 병합

변경:

`planner_runs.jsonl`, `research_brain_plans.jsonl`, `llm_prompts.jsonl`, `llm_responses.jsonl`을 재시도마다 덮어쓰지 않고 key 기준으로 병합하게 했다.

수정된 helper:

```text
_merge_jsonl_by_key
```

특히 key가 없는 새 row도 삭제되지 않도록 보강했다. 이 부분이 없으면 provider-none planner row처럼 key가 비어 있는 진단 row가 사라질 수 있었다.

쉬운 예:

```text
나쁜 방식:
  1차 검사 기록 위에 2차 검사 기록을 덮어써서 1차 기록이 사라짐.

좋은 방식:
  1차 검사 기록은 그대로 두고, 2차 검사 기록을 뒤에 붙임.
```

### 6.3 max_iterations 기반 FULL_THESIS follow-up loop

`run_census_mode_v4`에 follow-up 반복 경로를 추가했다.

조건:

```text
max_iterations > 1
brain_web enabled
strict promotion mode
production full thesis runner가 아직 승격하지 못함
blocked_candidate_follow_up_seed_events.jsonl 존재
```

동작:

```text
1. 초기 Brain/Web 실행
2. production FULL_THESIS runner 실행
3. blocker seed 생성
4. seed snapshot을 full_thesis_follow_up_iteration_<N>_seed_events.jsonl로 고정
5. 그 seed를 다음 Brain/Web attempt에 입력
6. promotion과 production full thesis runner 재실행
7. promoted row가 생기거나 seed가 사라지거나 max_iterations에 도달하면 종료
```

새 audit:

```text
full_thesis_follow_up_iterations_audit.json
```

새 helper:

```text
_should_run_full_thesis_follow_up_iteration
_full_thesis_production_runner_promoted
_full_thesis_follow_up_iteration_summary
_full_thesis_follow_up_iterations_audit
_aggregate_brain_web_attempts
_aggregate_brain_promotion_exports
```

### 6.4 Seed materialization trace 다중 seed 지원

`_write_full_thesis_seed_materialization_trace`가 여러 seed path를 받게 바뀌었다.

각 trace row에는 다음 필드가 들어간다.

```text
seed_source_path
seed_source_index
```

이유:

초기 seed와 follow-up iteration seed를 같은 trace 안에서 구분해야 한다. 그래야 "이 claim이 최초 후보에서 온 것인지, blocker 보강 loop에서 온 것인지" 추적할 수 있다.

## 7. 이번 패치가 하지 않은 것

이번 패치는 일부러 다음을 하지 않았다.

1. Green gate를 느슨하게 만들지 않았다.
2. `FULL_THESIS`가 아닌 partial row를 운영 Stage처럼 승격하지 않았다.
3. 삼성전자/하이닉스에 종목명 예외를 만들지 않았다.
4. 점수 weight나 Stage threshold를 바꾸지 않았다.
5. missing primitive를 코드 하드코딩 검색어로 해결하지 않았다.
6. snippet이나 source_proxy_only 자료를 score evidence로 승격하지 않았다.

쉬운 예:

```text
문제가 "서류가 부족하다"라면,
가짜 서류를 통과시키는 게 아니라
부족한 서류를 다시 요청하는 루프를 만든 것이다.
```

## 8. 테스트 상태

최근 패치 후 직접 통과한 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_bundle_export tests.test_census_v4_brain_stage_promotion_gate tests.test_census_v4_goal_required_audits tests.test_census_v4_full_thesis_smoke_tasks -v
```

결과:

```text
Ran 43 tests
OK
```

그 전에 관련 subset:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_bundle_export tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 27 tests
OK
```

또한 문법 확인:

```bash
python -m py_compile src/e2r/census/census_runner_v4.py
```

결과:

```text
OK
```

최신 패치 후 전체 suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5141 tests in 236.128s
OK
```

해석:

최신 follow-up iteration patch 이후에도 전체 테스트는 통과했다. 다만 이것은 코드 회귀가 없다는 뜻이지, `FULL_THESIS` 운영 승격이 완료됐다는 뜻은 아니다. 운영 승격은 다음 live/bounded 실행 산출물에서 `FULL_THESIS` row와 pending gate 감소를 다시 확인해야 한다.

## 9. Goal requirement matrix 현재 해석

v105 기준 goal matrix:

```text
pass    17
pending  4
fail     0
```

pending gate:

```text
FULL_THESIS_SMOKE_PASS
FULL_THESIS_PRODUCTION_PASS
FULL_THESIS_SEED_PROMOTION_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

해석:

`fail=0`은 좋은 신호지만 완료가 아니다. 남은 4개 pending이 전부 운영 Stage 신뢰성과 직접 연결된다.

쉬운 예:

```text
건물 안전점검에서 17개 항목은 통과했지만,
비상구, 소방, 전기, 내진이 pending이면 입주 완료라고 말할 수 없다.
```

## 10. 전체 아키타입 replay 상태

v105 기준:

```text
source-backed ready: 6 / 32
ready archetypes: C06, C08, C15, C17, C24, C28
source gap pending: 26 / 32
```

해석:

모든 아키타입에 Evidence Contract 구조를 붙이는 작업과, 모든 아키타입에서 source-backed replay를 통과시키는 작업은 다르다. 현재는 일부 핵심 아키타입의 replay가 준비됐지만, 전체 32개 기준 운영 replay는 아직 부족하다.

중요:

`source_proxy_only`, `evidence_url_pending`, `shadow_weight_only` 연구자료는 운영 점수 정답으로 쓰면 안 된다. 이런 자료는 "어떤 primitive가 필요한가"를 설계하는 데만 쓴다.

## 11. 지금까지 완료된 큰 묶음

### Bundle A: Runtime Proof / Anti-Fake Hardening

진행됨:

- v3 forensic review 작성
- legacy runner lockout 계층 추가
- leaf artifact manifest 생성 경로 추가
- report generated from leaf audit only 원칙 도입
- known-bad regression audit 도입
- sample bundle과 manifest 기반 검증 추가

상태:

```text
부분 통과. Anti-fake status board로는 많이 단단해졌다.
```

### Bundle B: Meaningful Stage Semantics

진행됨:

- `AtomicStageDecision` 도입
- score field split 도입
- stage scope와 operator stage use 분리
- partial score와 full thesis score 분리
- semantic primitive guard 도입
- official event counter audit 도입

상태:

```text
부분 통과. partial stage와 full thesis stage를 섞지 않는 방어는 들어갔다.
```

### Bundle C: Real Brain/Web Evidence Gate

진행됨:

- planner run trace 생성
- llm prompts/responses leaf 생성
- source tasks/source task executions 생성
- web search tasks/results/fetched documents 생성
- claim extractor run audit 생성
- accepted claims/score contributions 연결
- Brain/Web readiness gate 통과

상태:

```text
BRAIN_WEB_EVIDENCE_PASS 쪽은 통과권이다.
하지만 FULL_THESIS_REFRESH_PASS는 아직 아니다.
```

## 12. 다음 작업 순서

다음 작업은 "더 그럴듯한 report 작성"이 아니라, 남은 pending gate를 실제로 닫는 것이다.

우선순위:

1. `max_iterations=2` 이상으로 v107 live bounded 실행
2. `full_thesis_follow_up_iterations_audit.json` 확인
3. follow-up seed가 실제 second Brain/Web attempt로 들어갔는지 확인
4. 추가 accepted claim이 missing Green primitive를 채웠는지 확인
5. `FULL_THESIS_SEED_PROMOTION_PASS`가 false면 seed가 왜 claim으로 못 바뀌었는지 원인 파일/함수까지 추적
6. 삼성전자/하이닉스 C06/HBM smoke에서 partial과 full thesis가 계속 분리되는지 확인
7. C05처럼 systemic source-backed replay gap이 남은 아키타입부터 보강
8. 32개 전체 아키타입 source-backed replay matrix 재생성
9. 모든 pending gate가 닫힌 뒤 5개 subagent 교차검증 수행

## 13. 다음 실행에서 꼭 봐야 할 파일

새 실행 산출물에서 우선 확인할 파일:

```text
full_thesis_follow_up_iterations_audit.json
blocked_candidate_follow_up_seed_events.jsonl
full_thesis_follow_up_iteration_2_seed_events.jsonl
census_mode_v4_full_thesis_seed_materialization_trace.jsonl
planner_runs.jsonl
research_brain_plans.jsonl
llm_prompts.jsonl
llm_responses.jsonl
source_tasks.jsonl
source_task_executions.jsonl
accepted_claims.jsonl
primitive_states.jsonl
score_contributions.jsonl
stagecourt_traces.jsonl
census_stage_status.jsonl
census_mode_v4_goal_requirement_matrix_audit.json
```

판정 기준:

```text
follow-up seed만 생김
  -> 아직 부족. 검색 과제만 만든 상태다.

follow-up seed가 2차 Brain/Web attempt에 들어감
  -> 이번 패치 경로가 작동한 것이다.

2차 attempt에서 accepted claim이 늘어남
  -> source acquisition/extraction이 실제로 보강됐다.

missing Green primitive가 줄어듦
  -> full thesis 승격 가능성이 생긴다.

FULL_THESIS row가 생김
  -> 운영 Stage 후보로 볼 수 있다.
```

## 14. 아직 금지해야 할 잘못된 설명

아래 표현은 현재 상태에서 금지해야 한다.

```text
전 종목 운영 Stage 지도가 완성됐다.
삼성전자와 하이닉스의 full thesis score가 확정됐다.
Brain/Web이 돌았으니 FULL_THESIS도 통과한 것이다.
partial score가 70점대라서 운영 Stage2다.
follow-up seed가 생겼으니 missing primitive가 해결됐다.
```

대신 이렇게 말해야 한다.

```text
Census v4는 전 종목 상태판과 Brain/Web evidence leaf를 만들었다.
하지만 FULL_THESIS 운영 Stage row는 아직 0개다.
현재 점수는 partial/event weighted score이며 full E2R 100점이 아니다.
follow-up seed를 다음 Brain/Web attempt로 되먹이는 패치가 들어갔고,
다음 실행에서 그 seed가 실제 claim과 primitive 보강으로 이어지는지 검증해야 한다.
```

## 15. 최종 완료까지 남은 명확한 blocker

현재 최종 blocker:

```text
1. FULL_THESIS_SMOKE_PASS 미통과
2. FULL_THESIS_PRODUCTION_PASS 미통과
3. FULL_THESIS_SEED_PROMOTION_PASS 미통과
4. ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS 미통과
5. 5개 subagent 최종 교차검증 미수행
```

따라서 현재 상태는:

```text
Goal status: IN_PROGRESS
Operational use status: NOT READY FOR FULL_THESIS OPERATION
Safe claim: BRAIN_WEB_EVIDENCE_PATH PARTIALLY PROVEN
Unsafe claim: FULL OPERATIONAL STAGE MAP COMPLETE
```

## 16. 작업자가 다음에 이어서 할 일

다음 에이전트나 이어지는 작업자는 아래 순서로 진행하면 된다.

```text
1. 현재 워킹트리 커밋 이후 최신 main에서 전체 테스트를 다시 돌린다.
2. v107 또는 다음 run id로 max_iterations=2 이상 bounded live run을 돌린다.
3. follow-up iteration audit이 1회 이상 생겼는지 본다.
4. blocked seed가 second attempt planner/source task로 연결됐는지 본다.
5. source task가 full source fetch와 accepted claim을 만들었는지 본다.
6. primitive state가 missing에서 present/current로 바뀌었는지 본다.
7. FULL_THESIS runner가 promoted_full_thesis_row_count > 0을 만들었는지 본다.
8. 실패하면 "왜 못 찾았는지"를 provider/source/acquisition/extractor/mapper/green gate 중 하나로 분류한다.
9. 그 원인을 코드와 테스트로 고친다.
10. 같은 명령으로 재실행한다.
```

핵심은 "낮은 점수를 확정하는 것"이 아니라 "자료를 못 찾았으면 Pending 또는 Follow-up으로 남기고, 자료를 찾았으면 claim-backed score로만 올리는 것"이다.
