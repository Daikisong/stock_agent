# Goal4 Seed Order Runtime Attempt Final Audit - 2026-07-08

작성 시점: 2026-07-08 KST

이 문서는 0705 Goal4 all-archetype runtime parity 작업 중, follow-up seed order 패치와 그 이후 bounded self-repair 실행 결과를 남긴다.

결론부터 말하면:

```text
시드 노출/순서 문제는 고쳤다.
전체 follow-up runtime은 끝까지 돌았다.
하지만 Goal4 meaningful runtime parity는 아직 통과가 아니다.
이번 산출물은 production readiness, score, Stage 근거로 쓰면 안 된다.
```

쉬운 예:

```text
전에는 시험지를 C01부터 C32까지 나눠 줬는데,
채점 대기열이 임의로 섞이면서 특정 유형이 먼저 계속 처리되는 문제가 있었다.

이번 패치는 "Goal4 전체 아키타입 follow-up 시험지"에 한해서
처음 나눠 준 순서 그대로 examiner에게 들어가게 만든 것이다.

다만 시험지를 순서대로 제출했다고 해서 합격은 아니다.
필수 증거 칸이 닫혀야 의미 있는 full thesis pass다.
```

## 패치 범위

수정 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
```

핵심 변경:

```text
_planner_candidate_order()가 Goal4 all-archetype follow-up seed event를 감지하면
evidence likelihood, freshness, candidate id 재정렬보다 입력 seed 순서를 먼저 보존한다.
```

감지 조건:

```text
source_family == AllArchetypeRuntimeParityFollowUp
or event_type == all_archetype_runtime_parity_follow_up_seed
or structured.follow_up_origin == all_archetype_runtime_status_matrix
or structured.source_task_origin == all_archetype_runtime_status_matrix
```

중요한 제한:

```text
일반 production 후보 정렬을 없앤 것이 아니다.
Goal4 all-archetype parity follow-up seed에만 순서 보존을 적용했다.
```

쉬운 예:

```text
일반 daily run에서는 "증거 가능성이 높은 후보를 먼저 조사"하는 정렬이 여전히 맞다.
하지만 Goal4 전 아키타입 검증에서는 C01, C02, C03 순서로 일부러 만든 seed가 의미가 있다.
그래서 이 특수 seed만 원래 순서를 유지한다.
```

## 회귀 테스트

추가 테스트:

```text
test_goal4_all_archetype_followup_seed_order_is_preserved_in_live_planner_order
```

검증 내용:

```text
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
를 실제 config로 읽은 뒤,
_planner_candidate_order()의 앞 30개 candidate_event_id가 원본 seed 앞 30개와 같은지 확인한다.

또한 C06은 ordered[15],
C08은 ordered[21] 위치에 남는지 확인한다.
```

실행한 targeted unittest:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_goal4_all_archetype_followup_seed_order_is_preserved_in_live_planner_order \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_planner_candidate_order_prioritizes_claim_likely_live_events_without_dropping_corrections \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_goal4_operational_seed_file_carries_source_task_failure_feedback_to_planner -v
```

결과:

```text
OK
```

## Runtime Attempt

실행 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass --as-of-date 2026-07-05 --max-iterations 2
```

주요 output directory:

```text
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260708T082837Z
```

실행 산출물 row count:

```text
source_task_executions.jsonl = 916 rows
accepted_claims.jsonl       = 179 rows
score_contributions.jsonl   = 115 rows
stagecourt_traces.jsonl     = 98 rows
```

runtime progress:

```text
status = COMPLETED
latest_phase = completed
llm prompt/response rows = 111 / 111
planner_runs.jsonl = 458 rows
source_task_executions.jsonl = 916 rows
accepted_claims.jsonl = 179 rows
```

하지만 wrapper 결과:

```text
child returncode = 1
partial_run_invalid.json verdict = INVALID_PARTIAL_OUTPUT
score_or_stage_evidence_allowed = false
readiness_evidence_allowed = false
full_thesis_promotion_allowed = false
```

partial output의 operator rule:

```text
This directory may contain partial leaf files, but it is not a completed census run.
Do not use it as readiness, score, or Stage evidence.
```

쉬운 예:

```text
기계는 끝까지 돌았지만,
감사관이 "이 결과는 아직 공식 성적표로 쓰면 안 된다"고 도장을 찍은 상태다.
```

## Stage가 있는 애들이 있나

있다. 단, 이것을 바로 운영 Stage로 읽으면 안 된다.

`stagecourt_traces.jsonl` 기준:

```text
base_stage 2     = 44 rows
base_stage 1     = 47 rows
base_stage 3-Red = 1 row
base_stage 0     = 6 rows
```

score status:

```text
PENDING_MATERIAL_GAPS       = 44 rows
FINAL_WITH_NONMATERIAL_GAPS = 48 rows
FINAL                       = 6 rows
```

그러나 representative promotion audit:

```text
verdict = FAIL_UNSAFE_PROMOTION
brain_promoted_stage_row_count = 1
unsafe_promoted_stage_row_count = 1
brain_claim_score_ineligible_count = 76
blocker = accepted brain claims are not score eligible by deterministic guard: 76
```

해석:

```text
StageCourt 내부 판단 흔적은 있다.
하지만 그 흔적을 Census 대표 Stage로 승격하는 게이트가 막혔다.
따라서 "Stage 1/2 row가 있으니 운영 가능"이 아니라
"Stage 후보 trace는 있으나 대표 Stage 승격은 실패"라고 봐야 한다.
```

쉬운 예:

```text
연습 채점표에는 1등급, 2등급이 적혀 있다.
그런데 감독관이 "이 답안지는 신분 확인과 증빙 확인이 덜 끝났다"고 막았다.
그러면 성적표에는 아직 올릴 수 없다.
```

## Full Thesis Production 상태

최신 audit:

```text
production_full_thesis_row_count = 1
production_symbols = 011170
production_full_thesis_row_with_required_positive_missing_primitives_count = 1
production_full_thesis_row_with_green_gap_primitives_count = 1
required_smoke_symbols_promoted_without_missing_primitives_count = 0
```

의미:

```text
이번 실행에서 production full thesis row는 1개뿐이다.
그 1개도 required positive primitive와 Green gap이 남아 있다.
따라서 meaningful full thesis pass가 아니다.
```

쉬운 예:

```text
논문 형식으로 제출된 종목이 1개 생겼지만,
필수 참고문헌과 핵심 실험 결과가 빠져 있어서 통과 논문은 아니다.
```

## 주요 아키타입 관찰

이번 순서 패치 덕분에 C06, C08, C15, C17, C24, C28이 runtime에서 실제로 노출됐다.

하지만 결과는 아직 아키타입별 thesis closure가 아니다.

관찰 요약:

```text
C06:
  삼성전자/하이닉스가 stagecourt trace에 나타난다.
  그러나 C06 full thesis production promotion은 닫히지 않았다.
  과거처럼 90점, 60점, 4C가 마음대로 튀는 운영 결과로 쓰면 안 된다.

C08:
  runtime에 노출됐지만 claim/primitive closure가 약하다.
  제품/고객/매출 bridge가 닫혀야 한다.

C15:
  source task는 돌았지만 material spread full thesis row가 meaningful하게 닫히지 않았다.
  원재료 가격 기사만으로는 pass-through, realized spread, margin, FCF bridge를 채울 수 없다.

C17:
  일부 spread 관련 accepted claim이 생겼지만 Stage는 운영 승격되지 않았다.
  "spread 문장 발견"과 "아키타입 thesis 완성"은 다르다.

C24:
  일부 binary event claim이 잡혀도 trial/regulatory/current lifecycle gate가 닫히지 않으면 pending이다.

C28:
  ARR, NRR, renewal, retention을 직접 닫는 accepted primitive가 아직 부족하다.
```

쉬운 예:

```text
C17에서 "원료 가격이 움직였다"는 문장은 찾을 수 있다.
하지만 점수표는 "원료 가격 -> 판가 전가 -> spread -> OPM -> FCF"까지 이어지는 다리를 요구한다.
첫 문장만 찾았다고 Green이나 Yellow가 되면 안 된다.
```

## 이번 실행에서 좋아진 점

좋아진 점:

```text
1. Goal4 all-archetype follow-up seed order가 보존된다.
2. planner/provider가 111개 seed에 대해 호출됐다.
3. source task와 claim extraction이 실제로 돌아갔다.
4. StageCourt trace가 생성되는 경로는 살아 있다.
5. unsafe promotion을 감사가 잡아냈다.
```

특히 5번이 중요하다.

```text
예전 같으면 잘못 승격된 stage row가 그대로 운영 결과처럼 보일 수 있었다.
이번에는 FAIL_UNSAFE_PROMOTION으로 막혔다.
```

## 아직 막힌 점

막힌 점:

```text
1. accepted brain claim 76개가 deterministic guard 기준 score-eligible이 아니다.
2. brain stage row 1개가 blocker가 있는데도 promoted되어 unsafe promotion으로 잡혔다.
3. production full thesis row는 1개뿐이고, 그 1개도 required positive와 green gap이 남았다.
4. StageCourt trace에는 Stage 1/2가 있지만 representative Census Stage로는 승격할 수 없다.
5. Goal4 completion audit은 여전히 false다.
```

가장 중요한 해석:

```text
지금 문제는 "Stage가 전혀 안 만들어진다"가 아니다.
Stage 후보는 만들어진다.

문제는 "Stage 후보를 운영 대표 Stage로 올려도 되는 증거 장부와 guard가 아직 맞지 않는다"이다.
```

## 다음 패치 우선순위

1. `FAIL_UNSAFE_PROMOTION`부터 고친다.

```text
blocker가 있는 stage row는 대표 stage로 올라가면 안 된다.
unsafe_promoted_stage_row_count가 0이 될 때까지 readiness 근거로 쓰지 않는다.
```

2. score-ineligible accepted claim 76개를 분해한다.

```text
accepted claim인데 왜 score eligible이 아닌지 축을 나눠야 한다.

예:
  target directness 실패
  current lifecycle 실패
  source anchor 실패
  primitive mapping 실패
  official-first guard 실패
```

3. C15, C24, C28을 production full thesis row로 다시 닫는다.

```text
아키타입별로 "문장 발견"이 아니라 "필수 primitive closure"를 기준으로 본다.
```

4. C06/C08은 과거 고점수 smoke와 production run을 섞지 않는다.

```text
삼성전자/하이닉스 bounded smoke, controlled smoke, production full thesis row는 서로 다른 실행물이다.
서로 다른 입력과 corpus를 같은 점수 변화처럼 비교하면 안 된다.
```

5. threshold를 낮추지 않는다.

```text
Goal4의 목적은 점수를 억지로 올리는 것이 아니다.
연구자료가 요구한 증거 칸을 runtime Evidence OS가 실제 문서 claim으로 닫는 것이다.
```

## 최종 판정

이번 패치 후 판정:

```text
seed order repair = PASS
targeted unit regression = PASS
bounded runtime executed = PASS
production readiness = FAIL
meaningful full thesis parity = FAIL
operator score/stage use = NOT ALLOWED
```

따라서 다음 에이전트는 이 문서를 기준으로 다음을 검증해야 한다.

```text
1. follow-up seed order 보존 패치가 맞는가
2. unsafe promotion이 왜 1개 생겼는가
3. score-ineligible accepted claim 76개가 어떤 guard에서 막혔는가
4. StageCourt trace의 Stage 1/2를 대표 Stage로 올리지 못하는 이유가 타당한가
5. C15/C24/C28 full thesis closure가 왜 여전히 안 닫혔는가
```

운영 결론:

```text
이 커밋은 Goal4 완료 커밋이 아니다.
0705 Goal4 runtime parity를 다음 단계로 밀어붙이기 위한 seed order repair와 실패 감사 문서화 커밋이다.
```
