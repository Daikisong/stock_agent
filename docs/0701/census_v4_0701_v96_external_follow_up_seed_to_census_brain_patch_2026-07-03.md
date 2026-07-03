# Census v4 v96 - External Follow-up Seed to Census Brain Patch

작성일: 2026-07-03

## 1. 문제

v91~v93에서 다음 구조까지는 만들었다.

```text
v91:
  FULL_THESIS blocker follow-up source task shell 생성

v92:
  blocker follow-up source task를 planner_input_only seed event로 변환

v93:
  Research Brain 단독 CLI에 --candidate-event-seed-path 추가
```

하지만 Census v4 CLI 자체에는 이전 run의 follow-up seed를 다음 run의 Research Brain 입력으로 직접 넣는 옵션이 없었다.

쉬운 예:

```text
v92 = 보충문제 파일 생성
v93 = Research Brain 단독 실행에는 제출함 생김
남은 구멍 = Census 전체 실행에서 그 보충문제 파일을 제출할 방법이 부족함
```

이러면 운영 루프가 이렇게 끊긴다.

```text
Census run A
-> full_thesis_blocker_follow_up_seed_events.jsonl 생성
-> Census run B에서 이 파일을 Brain에 넣어야 함
-> CLI/config 입력 경로가 없음
```

## 2. 패치

`CensusV4RunConfig`에 새 필드를 추가했다.

```text
brain_candidate_event_seed_path: str | None
```

CLI에도 새 옵션을 추가했다.

```bash
--brain-candidate-event-seed-path <jsonl>
```

예시:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-follow-up \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-candidate-event-seed-path output/census_v4/<previous-run>/full_thesis_blocker_follow_up_seed_events.jsonl \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web
```

## 3. Auditable Used Seed Leaf

외부 seed를 그대로 외부 경로에서 읽기만 하면, 나중에 해당 run output만 보고 무엇을 Brain에 넣었는지 알기 어렵다.

그래서 v96은 실제로 Brain에 넘기는 seed를 항상 output에 복사한다.

```text
research_brain_candidate_seed_events_used.jsonl
```

기본 run에서는 이 파일이 내부 queue seed와 같다.

```text
research_brain_full_thesis_seed_events.jsonl
-> research_brain_candidate_seed_events_used.jsonl
```

외부 follow-up run에서는 이 파일이 외부 seed의 복사본이다.

```text
previous/full_thesis_blocker_follow_up_seed_events.jsonl
-> current/research_brain_candidate_seed_events_used.jsonl
```

즉 이 run의 source of truth는 항상 아래 파일이다.

```text
research_brain_candidate_seed_events_used.jsonl
```

## 4. Audit Fields

`brain_web_attempt`, `brain_web_readiness_gate`, `readiness_verdict` 요약에 seed 출처를 노출한다.

```text
full_thesis_seed_event_path
full_thesis_seed_source
full_thesis_seed_original_path
full_thesis_seed_event_count
```

가능한 `full_thesis_seed_source`:

```text
internal_full_thesis_refresh_queue
external_candidate_event_seed_path
external_candidate_event_seed_path_missing
```

해석:

```text
internal_full_thesis_refresh_queue
  이번 run이 자체 생성한 full thesis refresh queue seed를 Brain에 넣었다.

external_candidate_event_seed_path
  이전 run 등에서 만든 seed JSONL을 복사해서 Brain에 넣었다.

external_candidate_event_seed_path_missing
  외부 seed 경로가 지정됐지만 파일이 없었다. 점수/Stage 성공 근거가 아니다.
```

## 5. Materialization Trace 대상 변경

`full_thesis_seed_materialization_trace.jsonl`은 이제 “기본 queue seed”가 아니라 “실제 Brain에 투입된 seed”를 기준으로 작성된다.

기본 run:

```text
trace rows = internal queue seed rows
```

외부 follow-up seed run:

```text
trace rows = external follow-up seed rows copied into research_brain_candidate_seed_events_used.jsonl
```

이게 중요한 이유:

```text
외부 seed를 Brain에 넣었는데 trace가 내부 queue만 보면
실제 follow-up seed가 planner/source/claim으로 이어졌는지 감사할 수 없다.
```

## 6. 테스트

추가/보강 테스트:

```text
tests/test_census_v4_full_thesis_smoke_tasks.py
  test_external_brain_candidate_seed_path_is_copied_and_consumed

tests/test_census_v4_cli_uses_v4_runner.py
  --brain-candidate-event-seed-path 노출 확인
```

검증 내용:

```text
외부 full_thesis_blocker_follow_up_seed_events.jsonl 생성
-> CensusV4RunConfig.brain_candidate_event_seed_path로 전달
-> current output/research_brain_candidate_seed_events_used.jsonl로 복사
-> Brain planner row가 해당 seed event를 소비
-> full_thesis_seed_materialization_trace.jsonl이 해당 event를 추적
-> provider=none이면 PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS로 남음
```

중요한 점:

```text
이 테스트는 실제 FULL_THESIS 승급 테스트가 아니다.
외부 seed가 다음 Census Brain run에 들어가는 wiring 테스트다.
```

## 7. 현재 운영 상태

v96 이후에도 최신 운영 truth는 아직 바뀌지 않는다.

```text
FULL_THESIS row = 0
FULL_E2R_100 row = 0
actual_materialization_pass_allowed = false
NOT_READY
```

다만 이전보다 운영 루프가 한 칸 더 닫혔다.

```text
이전:
  follow-up seed 생성
  -> Research Brain 단독 CLI에는 넣을 수 있음
  -> Census 전체 실행에는 직접 넣기 어려움

v96:
  follow-up seed 생성
  -> 다음 Census v4 run의 --brain-candidate-event-seed-path로 투입 가능
  -> used seed leaf와 materialization trace로 감사 가능
```

## 8. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 공격해야 한다.

```text
1. --brain-candidate-event-seed-path가 실제 live run에서 쓰였는가?
2. research_brain_candidate_seed_events_used.jsonl이 외부 seed와 같은가?
3. full_thesis_seed_source가 external_candidate_event_seed_path로 남는가?
4. seed event가 planner_runs.jsonl에 실제 등장하는가?
5. planner가 source task를 만들었는가?
6. source task가 official-first/live bounded로 fetch됐는가?
7. accepted_claim이 생겼는가?
8. score_contribution과 StageCourt까지 닫혔는가?
9. actual_materialization_pass_allowed가 false인데 READY로 표시하지 않았는가?
```

## 9. 한 줄 결론

```text
v96은 이전 run의 follow-up seed를 다음 Census v4 Brain run에 직접 넣는 운영 입력 경로를 열었다.
아직 FULL_THESIS 성공은 아니지만, seed -> planner/source/claim closure를 실제로 재시도할 수 있는 Census-level wiring이 생겼다.
```
