# Census v4 v93 - Follow-up Seed CLI Entrypoint Patch / Cross Validation

작성일: 2026-07-03

이 문서는 v92 이후 남아 있던 다음 단절을 기록한다.

```text
v92:
  full_thesis_blocker_follow_up_seed_events.jsonl 생성
  Research Brain 내부 config에는 candidate_event_seed_path 존재

남은 문제:
  run_research_brain_v4_production_shadow CLI에는
  --candidate-event-seed-path 옵션이 없었다.
```

## 1. 결론

v93는 점수나 Stage를 바꾸지 않는다.

하는 일은 하나다.

```text
Census v4가 만든 blocker follow-up seed JSONL
-> Research Brain v4 CLI의 --candidate-event-seed-path
-> ProductionShadowV4Config.candidate_event_seed_path
-> run_research_brain_v4_production_shadow()
```

즉 v92에서 만든 다음-run seed를 사람이 실제 명령줄에서 Brain에 넣을 수 있게 했다.

쉬운 예:

```text
v92 = 보충문제 파일을 만들었다.
v93 = 선생님에게 그 보충문제 파일을 제출할 입력창을 만들었다.
```

## 2. 패치 내용

수정 파일:

```text
src/e2r/cli/run_research_brain_v4_production_shadow.py
tests/test_research_brain_v4_operational_modes.py
docs/0701/README.md
```

새 CLI 옵션:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_brain_v4_production_shadow \
  --as-of-date 2026-07-01 \
  --planner-provider real \
  --source-acquisition live_full_bounded \
  --candidate-event-seed-path output/census_v4/<run>/full_thesis_blocker_follow_up_seed_events.jsonl \
  --output-dir docs/operational \
  --skip-multi-day
```

이 옵션은 그대로 아래 config로 전달된다.

```text
ProductionShadowV4Config.candidate_event_seed_path
```

## 3. 왜 필요한가

v92 문서에는 다음 절차를 적었다.

```text
full_thesis_blocker_follow_up_seed_events.jsonl을 candidate_event_seed_path로 Brain에 투입
```

하지만 CLI에 해당 인자가 없으면 실제 운영자는 Python 내부 API를 직접 호출해야 했다.

그 상태에서는 다음 에이전트가 아래처럼 공격할 수 있다.

```text
"seed를 만든 건 맞는데 운영 명령으로 어떻게 넣지?"
```

v93는 이 공격을 닫는다.

## 4. 하지 않은 것

v93도 아래를 하지 않는다.

```text
FULL_THESIS 승격
FULL_E2R_100 점수 생성
LLM planner query 생성 보장
source fetch 성공 보장
accepted_claim closure 보장
```

즉 이 패치는 “입력창”이다. “답안 채점 완료”가 아니다.

운영 준비가 되려면 다음이 추가로 증명되어야 한다.

```text
1. v92/v93 코드로 live bounded Census run 재실행
2. live output에 full_thesis_blocker_follow_up_seed_events.jsonl 생성
3. 그 seed 파일을 --candidate-event-seed-path로 Brain CLI에 투입
4. planner_runs.jsonl에 seed event 우선 planner run 생성
5. LLM planner가 score/stage 없는 context에서 bounded source task 생성
6. source acquisition이 official-first/fallback 정책대로 fetch
7. Evidence OS accepted_claim이 missing primitive를 닫음
8. StageCourt가 같은 atomic trace에서 FULL_THESIS 여부 재판정
```

## 5. 테스트

추가 테스트:

```text
tests.test_research_brain_v4_operational_modes
  .ResearchBrainV4OperationalModesTests
  .test_cli_passes_candidate_event_seed_path_to_production_shadow_config
```

검증 내용:

```text
--candidate-event-seed-path <path>
-> CLI argparse
-> ProductionShadowV4Config.candidate_event_seed_path
-> run_research_brain_v4_production_shadow(config=...)
```

실행 결과:

```text
PYTHONPATH=src python -m py_compile \
  src/e2r/cli/run_research_brain_v4_production_shadow.py

PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_cli_passes_candidate_event_seed_path_to_production_shadow_config \
  -v

result = OK
```

## 6. 다음 에이전트 공격 포인트

v93 이후에도 남은 공격 포인트는 명확하다.

```text
1. CLI가 seed path를 받는 것은 확인됐다.
2. 하지만 live seed file을 실제로 넣어 live planner/source/claim closure까지 닫은 증거는 아직 없다.
3. 그러므로 production ready는 아니다.
```

다음 검증은 “CLI 인자 전달”이 아니라 “실제 seed 소비 실행”이어야 한다.

특히 아래 산출물을 봐야 한다.

```text
planner_runs.jsonl
source_tasks.jsonl
web_search_tasks.jsonl
source_task_executions.jsonl
evidence_documents.jsonl
accepted_claims.jsonl
primitive_states.jsonl
stagecourt_traces.jsonl
```

그리고 여전히 지켜야 할 원칙:

```text
seed/context는 score/stage를 주입하지 않는다.
LLM은 query/source task를 계획한다.
점수와 Stage는 source-backed claim 이후 deterministic engine이 계산한다.
```

## 7. 한 줄 요약

```text
v92는 follow-up seed 파일을 만들었다.
v93는 그 seed 파일을 Research Brain CLI에 넣는 공식 입력 경로를 만들었다.
하지만 아직 live source fetch와 claim closure가 증명되지 않았으므로 NOT_READY다.
```
