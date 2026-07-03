# Census v4 0701 Brain/Web Operational Minimum Gate Patch

작성 시각: 2026-07-02 KST

## 한 줄 결론

운영 Brain/Web pass에 최소 수량 gate를 추가했다.

이제 production Brain/Web 모드에서는 claim 1개짜리 작은 연결 fixture가 `BRAIN_WEB_EVIDENCE_PASS`를 대신할 수 없다.

쉽게 말하면:

```text
나쁜 상태:
  planner 1개
  web task 1개
  fetched doc 1개
  accepted claim 1개
  → Brain/Web pass처럼 보일 수 있음

패치 후:
  운영 모드에서는 아래 최소 수량을 못 채우면 BLOCKED
```

## 추가한 운영 최소 수량

파일:

```text
src/e2r/census/census_runner_v4.py
```

상수:

```text
BRAIN_WEB_MIN_PLANNER_CALLS = 30
BRAIN_WEB_MIN_WEB_SEARCH_TASKS = 20
BRAIN_WEB_MIN_WEB_SEARCH_CALLS = 20
BRAIN_WEB_MIN_FETCHED_DOCUMENTS = 10
BRAIN_WEB_MIN_EXTRACTOR_ATTEMPTS = 10
BRAIN_WEB_MIN_ACCEPTED_CLAIMS = 3
```

gate 출력:

```text
operational_minimum_count_gate_applies
minimum_required_counts
```

적용되는 모드:

```text
BRAIN_AND_WEB_ACQUISITION_ENABLED
FULL_LIVE_BRAIN_CENSUS
HYBRID_CENSUS + brain_web_mode=enabled
target_gate=brain_web/meaningful 이면서 web acquisition을 요청한 경우
```

## 왜 필요한가

`goal3.md`에는 Brain/Web 최소 수량이 명시되어 있다.

```text
selected_deep_symbol_count >= 30
llm_planner_call_count >= 30
web_search_task_count >= 20
web/news search calls >= 20
web_fetched_document_count >= 10
llm_claim_extractor_attempt_count >= 10
web_or_llm_accepted_claim_count >= 3
```

이 패치는 그 요구를 `brain_web_readiness_gate_audit.json`의 pass 조건으로 끌어올린다.

주의:

```text
이 패치는 실제 provider를 돌린 것이 아니다.
실제 provider/source/extractor leaf가 없으면 여전히 pass하지 못하게 막는 장치다.
```

## 테스트

추가 테스트:

```text
tests/test_census_v4_brain_web_readiness_gate.py

test_production_brain_web_mode_blocks_below_operational_minimum_counts
test_production_brain_web_mode_can_pass_when_operational_minimum_counts_are_met
```

의미:

```text
1개짜리 connected fixture:
  run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
  → BLOCKED
  → planner 1/30, web task 1/20, search call 1/20, fetch 1/10, extractor 1/10, claim 1/3 blocker 확인

최소량 충족 synthetic fixture:
  planner 30
  web task/search call 20
  fetched document 10
  extractor 10
  accepted claim 3
  claim → contribution → stagecourt → stage row 연결
  → READY_FOR_BRAIN_WEB_EVIDENCE_PASS
```

검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 30 tests
OK
```

V4 전체:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
```

결과:

```text
Ran 111 tests in 61.428s
OK
```

Full repo:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
exit_code = 0
test_count = 4992
failed_count = 0
error_count = 0
duration_seconds = 184.878
log_sha256 = 2207625b90762539d78da558bdcfb16a129f50d493375d3f3e8bf4485f5a4043
```

## 재생성한 output

```text
output/test_census_v4_verified_full_tests
output/test_census_v4_verified_full_tests_smoke
output/census_v4/2026-07-01
docs/operational/census_mode_v4_*
```

Canonical output:

```text
run_mode = LEDGER_REFRESH_CENSUS
brain_web_mode = disabled

brain_web_readiness_gate_audit:
  verdict = NOT_REQUESTED
  minimum_gate_applies = false
  operational_minimum_count_gate_applies = false
  brain_web_evidence_pass_allowed = false
  minimum_required_counts =
    llm_planner_call_count: 30
    web_search_task_count: 20
    web_search_call_count: 20
    web_fetched_document_count: 10
    llm_claim_extractor_attempt_count: 10
    web_or_llm_accepted_claim_count: 3
```

즉 canonical ledger-refresh run은 여전히 Brain/Web을 돌린 것이 아니다. 다만 이제 운영 Brain/Web 모드에서 작은 fixture가 pass를 대신하지 못한다.

## 남은 blocker

아직 goal 완료가 아니다.

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
controlled_semantic_replay_pending
```

다음 실질 작업:

```text
1. 실제 BRAIN_AND_WEB_ACQUISITION_ENABLED 또는 HYBRID_CENSUS run에서 provider/source/extractor leaf 생성
2. accepted Brain/Web claim 3개 이상을 score contribution과 StageCourt trace로 연결
3. 최소량 gate를 synthetic fixture가 아니라 production output으로 통과
4. production FULL_THESIS row를 controlled smoke가 아니라 live/source-backed chain으로 만들기
```

## 다음 에이전트 공격 질문

1. 운영 Brain/Web 모드에서 planner 1개짜리 fixture가 pass하지 못하는가?
2. 최소량 충족 기준이 readiness leaf에 machine-readable로 남는가?
3. canonical ledger refresh가 최소량 gate를 우회해서 Brain/Web pass를 claim하지 않는가?
4. `BRAIN_TRIAGE_ENABLED`와 `BRAIN_AND_WEB_ACQUISITION_ENABLED`가 필요한 최소 조건을 다르게 적용하는가?
5. 실제 production output에서 이 minimum count를 만족하는 row가 아직 없다는 사실을 숨기지 않는가?
