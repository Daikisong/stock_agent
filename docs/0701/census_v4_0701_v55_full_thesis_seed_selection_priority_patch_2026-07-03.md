# Census v4 0701 v55 Full-Thesis Seed Selection Priority Patch

작성일: 2026-07-03 KST

## 0. 한 줄 결론

v55에서는 `CensusFullThesisQueue` seed가 daily/cache 후보에 밀려 planner budget 밖으로 빠지는 문제를 줄였다.

이전 위험:

```text
full-thesis seed 85개 생성
-> candidate selection에서 seed 1개만 family-diversity 선점
-> 나머지는 CompanyGuide/Report/DART/IR/KRX 뒤로 밀림
-> bounded live planner run에서 seed 대부분이 PLANNER_NOT_RUN으로 남음
```

v55 이후:

```text
CensusFullThesisQueue seed를 selection budget 앞쪽에서 먼저 소비
-> full-thesis refresh 대기열이 실제 planner 후보로 먼저 들어감
-> provider가 none이면 승격 없이 PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS로 남음
```

쉬운 예:

```text
대기표 85장이 있는데, 예전에는 첫 대기표 1장만 보고
일반 방문자/홍보자료/캐시자료를 먼저 섞었다.

이제는 full-thesis 재진료 대기표를 먼저 진료실 후보로 올린다.
단, 의사가 없으면 진료 완료가 아니라 "의사 없음으로 대기"다.
```

## 1. 왜 이 패치가 필요한가

v54 기준 현재 가장 큰 운영 blocker:

```text
FULL_THESIS_SEED_PROMOTION_PASS = PENDING
FULL_THESIS_PRODUCTION_PASS = PENDING
production_full_thesis_row_count = 0
```

canonical disabled run:

```text
full_thesis_seed_event_count = 85
full_thesis_seed_planner_attempted_event_count = 0
full_thesis_seed_source_task_execution_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
```

Brain/Web diagnostic v28은 real planner를 일부 켰지만, 당시 산출물의 planner rows는 대부분 daily/cache 후보였고
`CensusFullThesisQueue` seed materialization에는 도달하지 못했다.

운영 목표는 아래다.

```text
event-board에서 full thesis refresh가 필요한 row
-> seed event
-> Research Brain planner
-> source task
-> Evidence OS claim
-> primitive state
-> score contribution
-> StageCourt
-> production FULL_THESIS row
```

이번 v55는 이 사슬의 첫 번째 병목을 고쳤다.

```text
seed event가 selection budget 안으로 먼저 들어오게 한다.
```

## 2. 코드 패치

변경 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
```

### 2.1 `_select_unique_candidate_events()`

이전 구조:

```text
preferred family에서 family당 첫 이벤트 1개 선택:
  CensusFullThesisQueue 1개
  DART 1개
  KIND 1개
  KRX 1개
  IR 1개
  CompanyGuide 1개
  ReportRadar 1개

그 다음 fill에서 CompanyGuide/Report/DART/IR/KRX/KIND를 먼저 채움.
나머지 CensusFullThesisQueue는 뒤로 밀림.
```

v55 구조:

```text
1. CensusFullThesisQueue seed를 selection budget 앞에서 먼저 채운다.
2. limit이 남으면 DART/KIND/KRX/IR/CompanyGuide/ReportRadar를 채운다.
```

중요:

```text
CensusFullThesisQueue seed는 score evidence가 아니다.
그냥 "이 row는 full thesis refresh를 실행해야 한다"는 작업 큐다.
```

즉 이번 패치는 점수를 만들지 않는다.
실행 순서만 바꾼다.

## 3. 새 테스트

추가 테스트:

```text
tests.test_research_brain_v4_operational_modes
  test_full_thesis_refresh_queue_consumes_selection_budget_before_daily_fill
```

테스트 시나리오:

```text
seed 4개:
  CensusFullThesisQueue

daily 후보 2개:
  DART
  CompanyGuide

limit = 3
```

기대값:

```text
selected = seed 3개
DART/CompanyGuide는 아직 선택되지 않음
```

이 테스트가 막는 회귀:

```text
full-thesis refresh queue가 있음에도 daily/cache 후보가 먼저 planner budget을 소비하는 문제
```

## 4. 검증 결과

### 4.1 관련 테스트

명령:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 49 tests in 3.315s
OK
```

명령:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks -v
```

결과:

```text
Ran 11 tests in 25.109s
OK
```

## 5. v55 diagnostic 실행

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-seed-priority-v55 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_TRIAGE_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider none \
  --brain-source-acquisition live_official_first \
  --brain-universe-limit 2 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-stage-promotion-mode strict \
  --target-gate anti_fake \
  --write-operational-docs false \
  --fail-on-critical-audit false \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

결과:

```text
NOT_READY
exit_code = 1
```

이 실패는 정상이다.

이 diagnostic은 provider를 `none`으로 둔 실행이다.
따라서 Brain/Web evidence pass나 full-thesis production pass를 주장하면 안 된다.

## 6. diagnostic에서 확인한 효과

파일:

```text
output/census_v4/2026-07-01-seed-priority-v55/planner_runs.jsonl
output/census_v4/2026-07-01-seed-priority-v55/brain_web_attempt_audit.json
output/census_v4/2026-07-01-seed-priority-v55/full_thesis_seed_materialization_audit.json
```

결과:

```text
planner rows = 21

planner row 0~20:
  source_family = CensusFullThesisQueue
  provider_name = none
  real_provider_success = false
  provider_error = planner_provider_not_configured
```

즉 selection budget 21개가 전부 full-thesis seed로 채워졌다.

before 방향:

```text
첫 seed 1개 이후 일반 DART/CompanyGuide/Report 후보가 섞일 수 있음
```

after 방향:

```text
full-thesis seed가 먼저 planner 후보로 들어감
```

## 7. materialization audit 변화

v55 diagnostic:

```text
full_thesis_seed_event_count = 85
full_thesis_seed_planner_attempted_event_count = 21
full_thesis_seed_planner_run_row_count = 21
full_thesis_seed_planner_run_count = 21
full_thesis_seed_real_provider_success_count = 0
full_thesis_seed_source_task_execution_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
```

status:

```text
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 21
PLANNER_NOT_RUN = 64
```

해석:

```text
패치 전 목표였던 "seed가 planner 후보로 먼저 들어오는가"는 확인됐다.
하지만 provider가 none이라 source task/claim/stage까지는 가지 않았다.
```

쉬운 예:

```text
대기표 21장이 진료실 문 앞까지 왔다.
하지만 의사가 없는 설정이라 진료는 시작되지 않았다.
남은 64장은 아직 대기실이다.
```

## 8. 아직 해결되지 않은 것

이번 패치가 해결하지 않는 것:

```text
1. real provider success
2. full-thesis seed source task execution
3. full-thesis seed accepted claim creation
4. full-thesis seed StageCourt trace creation
5. production FULL_THESIS row promotion
6. Brain/Web evidence pass
7. 26개 pending 아키타입 source-backed replay
```

현재 남은 작업:

```text
provider = codex_cli 또는 real
source_acquisition = live_full_bounded 또는 official-first + web fallback
seed planner success > 0
seed source task execution > 0
seed accepted claim > 0
seed stagecourt trace > 0
production_full_thesis_row_count > 0
```

단, 아래 조건 없이 승격하면 안 된다.

```text
valid anchor
direct/current target claim
accepted primitive mapping
score contribution
StageCourt trace
green gate primitive coverage
source quorum
```

## 9. 다음 패치 방향

다음 우선순위는 P1-b다.

```text
full-thesis seed가 real provider success 이후 source task까지 내려가는지 확인한다.
```

구체적으로 봐야 할 파일:

```text
src/e2r/research_brain/v4_planner_runtime.py
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/research_brain/v4_scoring_stage.py
src/e2r/census/census_runner_v4.py
```

다음 공격 질문:

```text
1. seed event prompt에는 full thesis context가 충분히 들어가는가?
2. seed event에서 primary archetype을 LLM이 고를 수 있는가?
3. seed event가 source_task_drafts를 만들면 deterministic validator가 불필요하게 버리지 않는가?
4. official-first source task가 seed context의 missing primitive를 실제로 닫는가?
5. source task execution이 accepted claim까지 만들었는데 StageCourt trace가 빠지는 경우는 없는가?
6. StageCourt trace가 있는데 production FULL_THESIS runner가 green primitive 부족으로 막는 이유가 정확히 leaf에 남는가?
```

## 10. 절대 하면 안 되는 shortcut

이번 패치 이후에도 아래는 금지다.

```text
1. provider none seed를 실행된 것으로 간주하기
2. PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS를 FULL_THESIS_PROMOTED로 바꾸기
3. source task 없이 accepted claim 만들기
4. accepted claim 없이 score contribution 만들기
5. controlled smoke row를 production row로 인정하기
6. CENSUS_EVENT_BOARD Stage를 FULL_THESIS_STAGE로 rename하기
7. threshold/weight를 낮춰 production row 만들기
```

쉬운 예:

```text
병원 문 앞까지 온 대기표는 진료 완료가 아니다.
의사 진료, 검사, 진단서가 모두 있어야 완료다.
```

## 11. 산출물 해시

```text
src/e2r/research_brain/v4_production_orchestrator.py
  bytes = 135780
  sha256 = baedaeeb76c40e848eb9d69b732e31ab857d5b34bde22ad42756c1ebe9f34e68

tests/test_research_brain_v4_operational_modes.py
  bytes = 140893
  sha256 = 14af0a972f57ccf0ce20d71ebf30503c726859b2715a25f06ab04e1af072e640

output/census_v4/2026-07-01-seed-priority-v55/brain_web_attempt_audit.json
  bytes = 2092
  sha256 = faaefd30aad13902b521d98a755944a56aab37198d0fcf90d1c06b2fdd52381a

output/census_v4/2026-07-01-seed-priority-v55/brain_web_readiness_gate_audit.json
  bytes = 4970
  sha256 = 0ace038cb31a13dcf20c43240d31f50c37a55415bc18809dae58ab9dbbb62c59

output/census_v4/2026-07-01-seed-priority-v55/full_thesis_seed_materialization_audit.json
  bytes = 2060
  sha256 = 42fbf42a62b89b9f2cad6a7f6a387c37d60fa729f0a9cbe2741aac83317dafc2

output/census_v4/2026-07-01-seed-priority-v55/planner_runs.jsonl
  bytes = 65627
  sha256 = f54210cdc59f5489e268185f52ef849ffe4d95dc7e11a05301ebd7c02f23d1b6

output/census_v4/2026-07-01-seed-priority-v55/full_thesis_seed_materialization_trace.jsonl
  bytes = 94610
  sha256 = c98ac96ff9b91d58a6e109960bf1069f1f60ee14f0a89fdf6310d3b3f9c013b3
```

## 12. 현재 판정

```text
FULL_THESIS seed selection priority:
  PATCHED

Seed planner candidate consumption:
  improved
  21 seed planner rows in v55 diagnostic

Seed materialization:
  still not complete
  provider none -> no real provider success

Production FULL_THESIS:
  still 0

BRAIN_WEB_EVIDENCE_PASS:
  still false

Goal completion:
  still false
```

한 문장으로:

```text
v55는 full-thesis 대기열을 실제 Research Brain 입구로 먼저 보내게 만든 패치다.
하지만 아직 의사/검사/진단서에 해당하는 real provider, source task, claim, StageCourt, production promotion은 닫히지 않았다.
```
