# Census v4 0701 v29 Full Thesis Refresh Queue Patch Result

작성일: 2026-07-02 KST

## 0. 결론

이번 패치는 운영 `FULL_THESIS` Stage를 만든 패치가 아니다.

이번 패치가 만든 것은 이것이다.

```text
CENSUS_EVENT_BOARD 비 Stage0 상태판 행
-> 운영 Stage로 복사하지 않음
-> full_thesis_refresh_queue.jsonl에 심사 대기열로 기록
-> source-backed claim / score contribution / StageCourt trace가 닫힐 때만 이후 FULL_THESIS 승격 가능
```

쉽게 말하면:

```text
기존:
  "Stage1/Stage2-Watch가 보이는데 이걸 운영 Stage로 봐도 되나?"
  -> 아니지만, 다음에 뭘 해야 하는지 leaf artifact가 약했다.

변경:
  "Stage1/Stage2-Watch가 보이는 85개는 운영 Stage가 아니다.
   대신 FULL_THESIS refresh queue 85개로 들어갔다."
```

## 1. 코드 패치

변경 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_census_v4_goal_required_audits.py
tests/test_census_v4_artifact_manifest.py
tests/test_census_v4_manifest_counts_match_report.py
tests/test_census_v4_report_generated_from_leaf_audit.py
```

새 leaf artifacts:

```text
full_thesis_refresh_queue.jsonl
full_thesis_refresh_queue_audit.json
```

새 readiness label:

```text
FULL_THESIS_REFRESH_QUEUE_PRESENT
```

## 2. Queue 규칙

Queue 대상:

```text
stage_scope = CENSUS_EVENT_BOARD
base_stage != Stage0
```

Queue row는 반드시:

```text
task_type = full_thesis_refresh_task
task_status = PLANNING_REQUIRED
operator_stage_use = NOT_FULL_THESIS_STAGE
target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
score_allowed_before_execution = false
stage_promotion_allowed_before_execution = false
official_first_required = true
hardcoded_query_count = 0
```

그리고 bounded budget을 가진다.

```text
max_source_tasks = 5
max_queries_per_task = 3
max_candidates_per_query = 20
max_fetches_per_task = 3
```

쉬운 예:

```text
삼성전자가 상태판 Stage1로 보인다.
-> 운영 Stage1이라고 출력하지 않는다.
-> FULL_THESIS refresh queue에 넣는다.
-> LLM Brain이 아키타입 가설을 세우고,
   공식자료/IR/리포트/신뢰뉴스 원문에서 source-backed primitive를 닫아야 한다.
```

## 3. Queue 검증 산출물

검증 output:

```text
output/census_v4/2026-07-01-full-thesis-refresh-queue-v29
```

실행 결과:

```text
stdout = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

중요 수치:

```text
readiness.verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
target_gate_pass = true

event_board_non_stage0_count = 85
full_thesis_refresh_queue_candidate_count = 85
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
```

Queue audit:

```text
verdict = PASS
queue_candidate_count = 85
event_board_non_stage0_count = 85
full_thesis_stage_row_count = 0

critical_counts:
  queue_missing_event_board_count = 0
  score_allowed_before_execution_count = 0
  stage_promotion_allowed_before_execution_count = 0
  hardcoded_query_count = 0
  unbounded_budget_count = 0
  operator_stage_copy_count = 0
```

Queue priority 분포:

```text
P2_EVENT_WATCH_REFRESH = 36
P1_PENDING_MATERIAL_REFRESH = 18
P1_MATERIAL_STAGE_REFRESH = 30
P0_RISK_REVIEW_REFRESH = 1
```

Source base stage 분포:

```text
Stage1 = 54
Stage2-Watch = 30
Red = 1
```

## 4. Report / Manifest 교차검증

`census_stage_summary.json`, `leaf_artifact_audit.json`, `readiness_verdict.json`, `acceptance_report.md`, `artifact_manifest.json`이 같은 숫자를 본다.

```text
summary.full_thesis_refresh_queue_candidate_count = 85
leaf.metrics.full_thesis_refresh_queue_candidate_count = 85
readiness.full_thesis_refresh_queue_candidate_count = 85
acceptance_report full_thesis_refresh_queue_candidates = 85
artifact_manifest full_thesis_refresh_queue.jsonl row_count = 85
```

Manifest:

```text
full_thesis_refresh_queue.jsonl
  row_count = 85
  sha256 = 544ae1447cfbca9c37606199011fc351ef59fb507b57a47ab7cf4701c6616c7b

full_thesis_refresh_queue_audit.json
  sha256 = cf0036952ddf6b559da41f84695fa75049823d897c9ac54ff0dd4d25d264835b
```

## 5. Live v29 Brain/Web 시도는 폐기

별도로 아래 live diagnostic을 시도했다.

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v29
```

하지만 이 산출물은 최종 readiness 증거로 쓰면 안 된다.

이유:

```text
8분 이상 대기
planner/source leaf 일부만 생성
최종 readiness/report/manifest 생성 전 중단
KeyboardInterrupt로 종료
```

중단 traceback 핵심:

```text
_extract_unstructured_records
-> claim_extractor.extract_with_metadata
-> extractor_provider.extract
-> _run_codex_command
-> process.communicate(... timeout=...)
```

즉 대기 위치는 Census queue 코드가 아니라 LLM claim extractor provider 호출이었다.

정확한 판정:

```text
sourcequality-v29 live attempt = INVALID_PARTIAL_OUTPUT
원인 = codex_cli claim extractor provider stalled/interrupted
운영 점수/Stage 증거로 사용 금지
```

쉬운 예:

```text
시험을 채점하다가 답안지 일부만 쓰고 멈춘 파일이다.
그 파일로 점수나 합격 여부를 말하면 안 된다.
```

## 6. 테스트

Targeted:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_goal_required_audits -v

result:
  Ran 12 tests / OK
```

Expanded:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_manifest_counts_match_report \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_report_generated_from_leaf_audit \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_stage_signal_split -v

result:
  Ran 59 tests / OK
```

## 7. 아직 남은 문제

이 패치 이후에도 최종 목표는 완료가 아니다.

아직:

```text
FULL_THESIS production row = 0
FULL_E2R_100 verified score row = 0
Brain/Web accepted claim = 0
Meaningful operational Stage pass = false
```

이번 패치는 다음 단계의 입력을 만든 것이다.

```text
85개 queue
-> bounded Research Brain planner
-> official-first source tasks
-> Evidence OS accepted claims
-> score contribution
-> StageCourt
-> FULL_THESIS Stage
```

## 8. 다음 패치 방향

다음 패치는 둘 중 하나로 가야 한다.

```text
P0-G source route quality:
  Tistory/블로그/급등종목/텔레그램을 더 빨리 source failure로 처리하고,
  DART detail / IR / 리포트 PDF / 회사 newsroom / 신뢰 뉴스 원문 route를 강화한다.

P0-K provider timeout/failure handling:
  codex_cli claim extractor가 오래 대기하면 낮은 점수 확정이 아니라
  PROVIDER_PENDING / SOURCE_PENDING으로 안전하게 닫고,
  partial output을 readiness 증거로 쓰지 않게 한다.
```

우선순위는 P0-K가 더 높다.

이유:

```text
provider가 멈췄을 때 프로세스가 오래 대기하면 운영 daily가 막힌다.
그리고 중간 output을 잘못 쓰면 또 점수가 흔들린다.
```

## 9. 현재 판정

```text
Patch:
  FULL_THESIS refresh queue leaf added.

Verification:
  queue count = 85
  queue audit = PASS
  report/manifest/readiness count aligned
  expanded tests = 59 OK

Operational stage:
  still 0

Final goal:
  not complete
```

한 줄 결론:

```text
Stage처럼 보이는 85개를 이제 운영 Stage로 오해하지 않고,
FULL_THESIS refresh 대기열로 추적할 수 있게 됐다.
하지만 실제 운영 Stage를 만들려면 다음 패치에서 provider pending 처리와 source route quality를 더 잡아야 한다.
```
