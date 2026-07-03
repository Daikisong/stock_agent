# Census v4 Planner Contract Primitive Filter Cross-Validation - 2026-07-01

이 문서는 P2 패치와 최신 enabled Brain/Web smoke를 다음 에이전트가 공격적으로 리뷰할 수 있게 남긴 기록이다.

기준 실행:

```text
/tmp/census_v4_enabled_provider_probe_after_planner_primitive_filter
```

## 한 줄 결론

```text
LLM planner가 아키타입 계약서에 없는 primitive를 source task로 실행하는 문제는 막았다.
하지만 Brain/Web accepted claim은 여전히 0개라 운영 Stage 승격은 아직 없다.
```

쉬운 예:

```text
이전:
  시험지에 없는 "implementation_timeline" 칸을 LLM이 만들어 냄
  -> 코드는 그 칸을 조사하러 감
  -> 문서는 가져왔지만 채점표에는 없는 칸이라 전부 rejected

패치 후:
  LLM이 만든 칸이 Evidence Contract에 실제 있는지 먼저 확인
  -> 없는 칸은 source task에서 격리
  -> 있는 칸만 조사
  -> 그래도 실제 claim이 점수칸 조건을 못 맞추면 점수 반영 0
```

이건 점수 완화 패치가 아니다. 오히려 LLM output을 아키타입별 Evidence Contract에 묶는 방어막이다.

## 왜 이 패치가 필요했나

P1 이후 `/tmp/census_v4_enabled_provider_probe_after_rejected_feedback_patch_v2`를 보면 rejected mapping feedback retry는 작동했다.

하지만 rejected trace를 샘플링하니 이상한 패턴이 있었다.

```text
symbol:
  069620 대웅제약
  003090 대웅

planner primary:
  C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE

LLM planner primitive:
  implementation_timeline
```

C29 Evidence Contract의 실제 required primitives:

```text
volume_growth_visible
mix_improvement
operating_leverage_visible
pricing_power_confirmed
fcf_quality_score
```

여기에 `implementation_timeline`은 없다.

즉 문제는 이랬다.

```text
LLM이 "시설투자 일정"이라는 조사 칸을 만들어 냄
코드는 그 칸이 C29 계약서에 있는지 확인하지 않음
SourceTask 실행
Evidence OS mapping 단계에서 결국 rejected
```

쉬운 예:

```text
C29 채점표는 "물량 증가", "믹스 개선", "영업 레버리지", "가격 결정력", "현금흐름"을 본다.
"종료일 연장" 또는 "GMP 승인 예정일"은 일정 정보일 수는 있지만,
그 자체로 "물량 증가"나 "영업 레버리지" 점수칸은 아니다.
```

따라서 `implementation_timeline`을 특정 종목 예외로 막는 것이 아니라, 전 아키타입 공통으로 "planner source task primitive는 Evidence Contract에 존재해야 한다"는 규칙을 넣었다.

## 코드 패치

변경 파일:

```text
src/e2r/research_brain/v4_planner_runtime.py
tests/test_research_brain_v4_real_planner_provider.py
```

핵심 코드 위치:

```text
src/e2r/research_brain/v4_planner_runtime.py:512
  planner prompt의 allowed_primitives를 Evidence Contract에서 생성

src/e2r/research_brain/v4_planner_runtime.py:579
  validate_llm_planner_output_v4에서 must_verify_primitives와 source_task_drafts를 contract primitive로 필터

src/e2r/research_brain/v4_planner_runtime.py:605
  _allowed_primitives_from_contract

tests/test_research_brain_v4_real_planner_provider.py:25
  allowed_primitives에 alias/score component가 섞이지 않는지 검증

tests/test_research_brain_v4_real_planner_provider.py:83
  implementation_timeline은 격리되고 volume_growth_visible만 통과하는지 검증
```

허용 primitive는 아래에서만 온다.

```text
contract.required_primitives
contract.green_gate.primitive_ids()
contract.alternative_primitives keys
contract.alternative_primitives values
contract.score_rubric values
contract.primitive_aliases keys
contract.freshness keys
```

의도적으로 제외한 것:

```text
contract.score_rubric keys
  예: eps_fcf_explosion, earnings_visibility, bottleneck_pricing

contract.primitive_aliases values
  예: ASP increase, CAPA 제약, HBM price
```

이 제외가 중요하다.

쉬운 예:

```text
source task primitive_gap에는 "hbm_capacity_pre_sold" 같은 점수 입력칸이 와야 한다.
"ASP increase"는 원문 표현 alias일 뿐이다.
"eps_fcf_explosion"은 최종 점수 component 이름이지 원문 claim primitive가 아니다.
```

## 왜 하드코딩이 아닌가

이 패치는 아래를 하지 않는다.

```text
if symbol == "003090": ...
if company == "대웅": ...
if text contains "종료일 연장": reject
if archetype == C29: implementation_timeline만 reject
```

대신 이렇게 한다.

```text
contract = EvidenceContractRegistry.get(primary_archetype)
allowed = contract-backed canonical primitive set
LLM source_task_draft.primitive_gap in allowed 인 것만 실행
```

즉 LLM은 계속 다음을 담당한다.

```text
무슨 아키타입이 맞는지 가설 세우기
어떤 primitive를 확인할지 고르기
어떤 공식/웹 source task를 만들지 고르기
query_intents 작성
```

코드는 다음만 담당한다.

```text
그 primitive가 해당 아키타입 계약서에 실제 존재하는가
무제한 검색을 요구하지 않는가
official-solvable gap을 웹으로 보내지 않는가
score/stage/current_score_eligible을 LLM이 직접 쓰지 않았는가
```

이게 프로젝트 원칙에 맞다.

```text
LLM은 조사 계획과 증거 추출을 한다.
점수/Stage는 deterministic rule engine이 계산한다.
```

## Smoke 실행 명령

```bash
rm -rf /tmp/census_v4_enabled_provider_probe_after_planner_primitive_filter

PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root /tmp/census_v4_enabled_provider_probe_after_planner_primitive_filter \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 8 \
  --brain-planner-success-limit 2 \
  --brain-planner-batch-size 2 \
  --brain-max-fetches-per-task 2 \
  --brain-claim-extractor-provider auto \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --fail-on-critical-audit true \
  --write-operational-docs false
```

결과:

```text
NOT_READY
exit code: 1
```

이 `NOT_READY`는 현재 정상이다.

이유:

```text
planner/search/fetch/extractor는 실행됨
Brain/Web mapping trace도 생성됨
하지만 accepted Brain/Web claim = 0
따라서 Brain/Web score contribution = 0
따라서 Brain/Web StageCourt trace = 0
따라서 promoted census row = 0
```

## Smoke 산출물 숫자

row count:

```text
planner_runs.jsonl:                  24
source_tasks.jsonl:                 110
source_task_executions.jsonl:       110
web_search_tasks.jsonl:              10
web_search_results.jsonl:            87
web_fetched_documents.jsonl:         14
web_rejected_documents.jsonl:        12
claim_extractor_runs.jsonl:          14
raw_assertions.jsonl:               173
adjudicated_claims.jsonl:           179
brain_claim_mapping_trace.jsonl:     93
accepted_claims.jsonl:               92
score_contributions.jsonl:           92
stagecourt_traces.jsonl:             92
brain_to_claim_trace.jsonl:           0
primitive_states.jsonl:              92
```

planner:

```text
planner_runs total: 24
  initial:        22
  feedback_retry: 2

real_provider_success: 4
not_attempted_after_real_planner_limit: 20
```

planner draft primitives after filter:

```text
volume_growth_visible:        4
cash_or_revision_conversion:  3
operating_leverage_visible:   3
mix_improvement:              2
fcf_quality_score:            1
```

중요 검산:

```text
implementation_timeline planner drafts: 0
implementation_timeline source tasks:   0
implementation_timeline mapping trace:  0
```

즉 P1에서 보였던 "계약서에 없는 primitive를 조사하러 가는 문제"는 최신 smoke에서는 사라졌다.

## Brain/Web trace 해석

`brain_claim_mapping_trace.jsonl`:

```text
total: 93

trace_status:
  REJECTED_BEFORE_SCORE: 93

accepted:
  true:  0
  false: 93

primitive_gap:
  mix_improvement:                   55
  operating_leverage_visible:        26
  volume_growth_visible:              8
  official_disclosure_status_current: 4

rejection:
  target_scope_not_direct:UNRELATED + mapping_not_accepted:REJECTED: 71
  mapping_not_accepted:REJECTED:                                  22
```

해석:

```text
71개는 target 직접 claim이 아니다.
22개는 target 직접 claim이지만 해당 primitive 점수칸으로 인정되지 않았다.
그래서 accepted claim 0개가 맞다.
```

쉬운 예:

```text
"대웅제약 신규시설투자 종료일 연장"은 대웅제약 직접 문서다.
하지만 이 문장만으로 "mix improvement"나 "operating leverage"가 생긴 것은 아니다.
그러면 accepted로 올리면 안 된다.
```

## Stage가 있긴 한가

있다. 하지만 Brain/Web full thesis Stage가 아니다.

`census_stage_status.jsonl`:

```text
rows: 3391

canonical_stage:
  0:      3306
  1:        54
  2:        30
  3-Red:     1

base_stage:
  Stage0:        3306
  Stage1:          54
  Stage2-Watch:    30
  Red:              1

assessment_depth:
  CHEAP_BASELINE: 3309
  VERIFIED_STAGE:  67
  OFFICIAL_LIGHT:  15
```

하지만:

```text
brain_stage_promotion_status: null for 3391 rows
brain_web_evidence_status:    null for 3391 rows
full_thesis_stage:            FULL_THESIS_NOT_RUN for Samsung/Hynix sample
```

정확한 표현:

```text
event-board Stage는 있다.
Brain/Web accepted claim 기반 Stage 승격은 없다.
full thesis 운영 Stage는 아직 실행되지 않았다.
```

쉬운 예:

```text
출석부와 일일 쪽지시험 점수는 있다.
하지만 기말고사 종합 성적표는 아직 안 나온 상태다.
```

## 삼성전자 / SK하이닉스 상태

최신 smoke 기준:

```text
005930 삼성전자
  canonical_stage: 1
  base_stage: Stage1
  assessment_depth: VERIFIED_STAGE
  event_evidence_score: 4.0
  accepted_claim_count: 1
  full_thesis_stage: FULL_THESIS_NOT_RUN
  full_thesis_score_valid_status: NOT_SCORED

000660 SK하이닉스
  canonical_stage: 1
  base_stage: Stage1
  assessment_depth: VERIFIED_STAGE
  event_evidence_score: 4.0
  accepted_claim_count: 1
  full_thesis_stage: FULL_THESIS_NOT_RUN
  full_thesis_score_valid_status: NOT_SCORED
```

따라서 이 숫자를 이렇게 읽으면 안 된다.

```text
삼성전자 HBM/C06 full thesis 점수 = 4점
SK하이닉스 HBM/C06 full thesis 점수 = 4점
```

정확한 해석:

```text
둘 다 현재 Census event-board에서 source-backed event claim 1개가 있어 Stage1로 표시됐다.
HBM/C06 full thesis 운영 점수와 Stage는 아직 실행되지 않았다.
```

## Readiness 감사 결과

`readiness_verdict.json`:

```text
verdict: NOT_READY
target_gate: brain_web

blockers:
  Brain/Web readiness gate blocked: web/LLM accepted claim count is zero
  Brain/Web readiness gate blocked: Brain/Web StageCourt traces are not promoted into census_stage_status
  Brain/Web readiness gate blocked: brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
```

`brain_web_readiness_gate_audit.json`:

```text
verdict: BLOCKED
blockers:
  web/LLM accepted claim count is zero
  Brain/Web StageCourt traces are not promoted into census_stage_status
  brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
```

`brain_stage_promotion_audit.json`:

```text
verdict: BLOCKED
blockers:
  accepted brain claim count is zero
  brain score contribution count is zero
  brain StageCourt trace count is zero
```

`brain_planner_audit.json`:

```text
verdict: PASS
```

`llm_claim_extraction_audit.json`:

```text
verdict: REAL_EXTRACTION_PASS
```

`web_naver_acquisition_audit.json`:

```text
verdict: REAL_ACQUISITION_PASS
```

정리:

```text
planner는 실제로 돌았다.
web/Naver acquisition은 실제로 돌았다.
LLM extraction도 실제로 돌았다.
하지만 accepted claim과 Stage promotion은 0개다.
따라서 NOT_READY가 맞다.
```

## 검증한 테스트

Targeted:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_planner_provider \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_static_logic_audit \
  -v
```

결과:

```text
Ran 18 tests in 0.160s
OK
```

Broader Brain/Web/Census target:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_planner_provider \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_provider_failure_pending \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_bundle_export \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  -v
```

결과:

```text
Ran 77 tests in 32.051s
OK
```

Full suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 4965 tests in 155.489s
OK

log: /tmp/stock_agent_full_tests_after_planner_primitive_filter.log
```

## 아직 남은 문제

### 1. Brain/Web accepted claim이 0개다

이건 지금 가장 큰 blocker다.

현재는 다음까지는 된다.

```text
planner
-> source task
-> web search/fetch
-> LLM raw assertion
-> adjudicated claim
-> mapping trace
```

하지만 여기서 멈춘다.

```text
accepted claim
-> primitive state
-> score contribution
-> StageCourt trace
-> promoted census row
```

이 뒤쪽 chain은 Brain/Web 기준으로 아직 0개다.

### 2. fetch 결과 품질이 낮다

이번 trace의 71개 rejection은 `target_scope_not_direct:UNRELATED`다.

즉 query는 회사명 scope를 포함했지만, 실제 fetched page가 다음처럼 어긋난 경우가 많다.

```text
다른 회사 여러 개를 나열한 주요공시 모음 기사
시장 요약 기사
대상 회사와 직접 관련 없는 검색 결과
```

다음 패치는 점수기를 만지는 것이 아니라 source acquisition ranker/relevance guard를 강화해야 한다.

필요한 방향:

```text
1. fetch 전 result title/snippet에 target entity direct mention 확인
2. fetch 후 full text에서 target entity density와 section-local directness 확인
3. "여러 회사 모음 기사"는 source task 목적과 직접 맞지 않으면 extraction 전 reject
4. search result lineage에 rejected reason을 남김
```

### 3. direct claim 22개도 primitive bridge를 못 넘었다

`mapping_not_accepted:REJECTED`만 있는 22개는 target 직접 claim이지만, 점수 primitive로 인정되지 않았다.

이건 나쁜 일이 아니다. 예를 들어 일정 연장 공시를 `volume_growth_visible`로 인정하지 않는 것은 맞다.

하지만 다음 planner feedback에는 더 구체적인 오답 노트가 필요하다.

```text
현재:
  mapping_not_accepted:REJECTED

필요:
  direct_but_only_timeline_change
  direct_but_no_volume_or_revenue_bridge
  direct_but_no_margin_or_fcf_bridge
  direct_but_only_capex_schedule
```

그래야 LLM planner가 다음 라운드에서 "일정 문서 말고 생산능력 수치, 제품명, 매출 전환, margin bridge를 찾아라"처럼 더 정확히 움직일 수 있다.

### 4. quarantined primitive audit가 아직 약하다

이번 패치로 invalid primitive는 필터링된다.

하지만 운영 감사 파일에 아래 수치가 명시적으로 나오지는 않는다.

```text
planner_invalid_primitive_draft_count
planner_quarantined_primitive_names
planner_sanitized_source_task_count
```

다음 에이전트는 이걸 `brain_planner_audit.json` 또는 별도 planner sanitizer audit에 추가하는 것을 검토해야 한다.

### 5. full thesis는 여전히 미실행이다

삼성전자/하이닉스가 Stage1로 보이는 것은 full thesis가 아니다.

다음 패치가 닫아야 할 것은 별도다.

```text
C06/HBM full thesis SourceTask
-> official-first bounded acquisition
-> LLM claim extraction
-> Evidence Contract primitive mapping
-> score contribution
-> StageCourt
-> full_thesis_stage / verified_score
```

이 chain이 없으면 삼성전자/하이닉스의 HBM 운영 점수를 말하면 안 된다.

## 다음 패치 방향

우선순위는 아래 순서가 맞다.

### P3-1. Source result relevance guard

목표:

```text
UNRELATED fetched document를 extraction 전에 줄인다.
```

예:

```text
대웅제약 source task인데 "한국카본, 테스, 셀트리온, 에이프로젠..." 같은 모음 기사가 잡히면
그 문서에서 claim extraction을 돌리기 전에 source relevance reject로 남긴다.
```

주의:

```text
회사명 문자열 하나만으로 pass시키면 안 된다.
문서의 subject section이 target 회사인지 봐야 한다.
```

### P3-2. Rejected mapping reason taxonomy

목표:

```text
mapping_not_accepted 하나로 뭉개지 말고,
왜 primitive bridge를 못 넘었는지 다음 planner가 이해할 수 있게 분류한다.
```

예:

```text
direct_but_timeline_only
direct_but_no_volume_bridge
direct_but_no_margin_bridge
direct_but_no_cash_or_revision_bridge
direct_but_only_capex_amount
```

### P3-3. Planner sanitizer audit

목표:

```text
LLM output에서 격리한 primitive/task를 산출물로 남긴다.
```

그래야 다음 smoke에서 이런 질문에 바로 답할 수 있다.

```text
LLM이 계약서 밖 primitive를 얼마나 냈나?
그중 몇 개를 필터했나?
필터 때문에 web acquisition이 줄었나?
아니면 유효 task는 유지됐나?
```

### P3-4. Brain/Web accepted claim 최소 positive fixture

목표:

```text
실제 live_full_bounded 경로에서 accepted Brain/Web claim 1개 이상을 source-backed로 닫는다.
```

단, guard를 완화하면 안 된다.

좋은 방향:

```text
명백한 target direct 공식 문서
명확한 primitive bridge
valid anchor
current temporal status
mapping ACCEPTED
score contribution 생성
StageCourt trace 생성
strict promotion row 생성
```

나쁜 방향:

```text
mapping guard 완화
일정 변경을 volume growth로 인정
뉴스 snippet만으로 점수 반영
LLM이 accepted=true라고 했으니 통과
```

## 다음 에이전트 공격 질문

다음 리뷰어는 아래를 먼저 공격하면 된다.

1. `allowed_primitives`가 정말 canonical primitive만 포함하는가?
2. `score_rubric` key와 alias value가 다시 source task primitive로 들어오지 않는가?
3. invalid primitive가 전부 filtered 되었을 때 real provider success를 fake pass로 세지 않는가?
4. invalid primitive를 filter했는데 유효 external web task까지 같이 사라지지 않는가?
5. `implementation_timeline`이 source_tasks 또는 brain_claim_mapping_trace에 다시 나타나지 않는가?
6. Brain/Web accepted claim 0개인데 readiness가 PASS로 바뀌지 않는가?
7. Stage1/Stage2 event-board row를 full thesis 운영 Stage로 오해할 여지가 남아 있지 않은가?
8. 삼성전자/하이닉스 Stage1이 HBM/C06 full thesis 점수처럼 출력되지 않는가?
9. source result relevance guard 없이 unrelated 문서를 계속 LLM extractor에 보내고 있지 않은가?
10. direct-but-not-bridge rejection이 다음 planner feedback에서 충분히 구체적인가?

## 현재 완료/미완료 판정

완료:

```text
planner primitive contract filter
canonical allowed_primitives prompt
alias/score component primitive 오염 차단
implementation_timeline 실행 차단
P1 rejected feedback retry 유지
Brain/Web NOT_READY 정직성 유지
```

미완료:

```text
Brain/Web accepted claim
Brain/Web score contribution
Brain/Web StageCourt trace
Brain/Web promoted census row
Samsung/Hynix full thesis C06/HBM score/stage
MEANINGFUL_OPERATIONAL_STAGE_PASS
```

최종 문장:

> 이번 패치는 "틀린 조사칸을 실행하지 않게 만든 것"이지, "운영 Stage를 완성한 것"이 아니다. 현재 올바른 상태는 `NOT_READY`이며, 다음 병목은 source relevance와 direct-but-no-bridge rejection을 더 세밀하게 planner feedback으로 되돌리는 것이다.
