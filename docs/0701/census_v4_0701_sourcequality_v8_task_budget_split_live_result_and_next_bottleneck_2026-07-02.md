# Census v4 0701 Sourcequality v8 Task Budget Split Live Result / Next Bottleneck

작성 시점: 2026-07-02 KST

대상 실행:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v8
```

관련 패치:

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_planner_runtime.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/cli/run_research_brain_v4_production_shadow.py
src/e2r/cli/run_e2r_census_v4_until_pass.py
src/e2r/census/census_runner_v4.py
tests/test_research_brain_v4_operational_modes.py
```

## 결론

```text
v8도 READY가 아니다.
하지만 v7에서 보인 task truncation 문제는 고쳤다.
```

쉬운 예:

```text
v7:
  LLM이 "DART 원문, IR, 뉴스 원문을 각각 확인하라"고 했는데
  max_fetches_per_task=1 값 때문에 조사 경로 자체가 1개로 잘렸다.

v8:
  조사 경로는 여러 개 유지하고,
  각 경로에서 fetch할 문서 수만 1개로 제한했다.
```

즉 v8은 크롤링을 무제한으로 넓힌 게 아니다.

```text
source task 수 = 조사 경로 수
max_fetches_per_task = 각 조사 경로에서 가져올 문서 수
```

둘을 분리했다.

## v7 -> v8 핵심 변화

```text
metric                             v7      v8
verdict                            BLOCKED BLOCKED
brain_accepted_claim_count          0       0
official_accepted_claim_count       0       0
web_or_llm_accepted_claim_count     0       0
brain_stage_trace_count             0       0
brain_promoted_stage_row_count      0       0
source_task_execution_count         99      104
current attempt source tasks        7       12
web_search_task_count               7       4
web_search_result_count             50      31
web_fetched_document_count          9       2
web_rejected_document_count         24      21
llm_claim_extractor_attempt_count   9       2
raw_assertion_rejections            56      23
```

해석:

```text
v8에서는 retry planner가 만든 여러 source task가 보존됐다.
대웅 003090 기준 source task가 DART/KIND, IR/IssuerOfficial, cash/revision, TrustedNews로 분산됐다.

하지만 accepted claim은 여전히 0개다.
따라서 운영 FULL_THESIS Stage도 여전히 0개다.
```

## 이번 코드 패치가 닫은 것

### 1. source task count와 fetch budget 분리

기존 문제:

```text
source_tasks_from_planner_output_v4(..., max_tasks=config.max_fetches_per_task)
```

이 구조에서는 `--brain-max-fetches-per-task 1`이 다음처럼 잘못 작동했다.

```text
각 source task에서 문서 1개만 fetch
```

가 아니라:

```text
LLM이 만든 source task 자체를 1개만 실행
```

이 되어 버렸다.

패치 후:

```text
max_source_tasks_per_plan = source task 경로 수 제한
max_fetches_per_task = 각 task당 fetch 수 제한
```

### 2. CLI와 reproduction command에 새 budget 노출

추가:

```text
--max-source-tasks-per-plan
--brain-max-source-tasks-per-plan
```

따라서 v8 재현 명령은 다음 의미를 갖는다.

```text
--brain-max-source-tasks-per-plan 5
  LLM planner가 만든 조사 경로는 최대 5개까지 보존

--brain-max-fetches-per-task 1
  각 조사 경로에서 문서 fetch는 1개까지만 허용
```

## v8에서 실제로 실행된 대웅 source task

대웅 003090 기준 주요 task:

```text
volume_growth_visible:
  IR / IssuerOfficial / DART / KIND

cash_or_revision_conversion:
  DART / IR / CompanyGuide

operating_leverage_visible:
  TrustedNews / CompanyNewsroom / IndustryMedia

retry volume_growth_visible:
  DART / KIND detail

retry operating_leverage_visible:
  IR / IssuerOfficial

retry cash_or_revision_conversion:
  DART / IR / CompanyGuide

retry trusted original article:
  TrustedNews / CompanyNewsroom / BrokerReportPublicPDF / IndustryMedia
```

쉬운 예:

```text
v7은 "공장 관련 서류 하나만 봄"에 가까웠다.
v8은 "공시 원문, IR, 현금흐름 자료, 신뢰 기사 원문"으로 조사 경로를 나눴다.
```

## 그래도 READY가 아닌 이유

v8의 raw assertion rejection:

```text
raw_assertion_rejections = 23

rejection_reason:
  primitive_mapping_rejected = 20
  target_scope_or_directness_rejected = 3

mapped_primitive_id:
  volume_growth_visible = 10
  operating_leverage_visible = 7
  cash_or_revision_conversion = 4
  official_disclosure_status_current = 2
```

의미:

```text
원문을 더 넓게 읽었지만,
아직 "생산량 증가", "영업 레버리지", "현금/실적 전환"을 직접 증명하는 claim은 못 찾았다.
```

대웅 예시:

```text
"신규시설투자 종료일이 연장됐다"
  -> 일정/지연/official status 문장이다.

"생산능력이 얼마 늘고, 고객/수요/매출로 연결된다"
  -> volume_growth_visible 문장이다.

현재 v8에서 accepted claim으로 필요한 것은 뒤쪽이다.
```

따라서 여기서 mapper를 느슨하게 해서 일정 연장을 volume growth로 받아주면 안 된다.

## 다음 병목

v8 기준 다음 병목은 두 갈래다.

```text
P1. 후보 선택/계속 탐색 정책
    universe_limit=1, planner_success_limit=1 smoke에서는 약한 이벤트 하나가 걸리면 accepted claim 0으로 끝난다.
    운영형 진단은 accepted claim이 나올 때까지 더 많은 후보를 bounded로 시도하거나,
    accepted claim 0을 정직하게 SourcePending/NoFullThesis로 남겨야 한다.

P2. rejected claim feedback 이후 source routing 품질
    retry planner는 여러 경로를 냈지만,
    실제 fetched document가 2개뿐이고 accepted claim은 0개다.
    다음 패치는 "더 많은 fetch"가 아니라,
    issuer IR/report/company newsroom/provider source가 실제 full-source로 닫히는지 봐야 한다.
```

금지:

```text
일정 연장을 volume_growth_visible로 강제 수용
fetch 성공을 accepted claim으로 간주
official-only claim을 web/LLM accepted claim으로 승격
v8 NOT_READY를 READY처럼 표현
```

## 검증

타깃 테스트:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
Ran 24 tests / OK

PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_cli_uses_v4_runner -v
Ran 84 tests / OK
```

v8 live diagnostic:

```text
exit code = 1
stdout = NOT_READY
```

이 실패는 정상 차단이다.

## 최종 판정

```text
TASK_BUDGET_SPLIT = PASS
RETRY_SOURCE_TASKS_PRESERVED = IMPROVED
LIVE_V8_WEB_FETCH = PRESENT_BUT_LOW
LIVE_V8_LLM_EXTRACTION = PRESENT_BUT_LOW
LIVE_V8_ACCEPTED_BRAIN_CLAIM = FAIL
LIVE_V8_STAGE_PROMOTION = FAIL
READY = NO
```

한 문장:

```text
v8은 LLM 조사계획을 budget 이름 혼동으로 잘라먹는 문제를 고쳤지만,
아직 source-backed accepted claim과 FULL_THESIS Stage를 만들지는 못했다.
다음 패치는 점수 완화가 아니라 후보 계속 탐색과 source route 실효성을 검증하는 쪽이어야 한다.
```
