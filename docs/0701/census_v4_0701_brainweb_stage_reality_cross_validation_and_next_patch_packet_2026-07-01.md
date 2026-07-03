# Census v4 Brain/Web Stage Reality Cross Validation And Next Patch Packet - 2026-07-01

이 문서는 다음 에이전트가 빡세게 리뷰할 수 있게 만든 교차검증 패킷이다.

기준 실행:

```text
/tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch
```

P1 패치 후 최신 실행:

```text
/tmp/census_v4_enabled_provider_probe_after_rejected_feedback_patch_v2
```

P1 이후 추가 결론:

```text
rejected mapping trace가 planner feedback으로 되돌아가는 루프는 생겼다.
feedback_retry planner run 2개와 follow-up source task execution 4개가 실제로 생겼다.
web search task는 4개에서 9개, fetched document는 8개에서 16개, LLM extractor run은 8개에서 16개로 늘었다.
하지만 Brain/Web accepted claim은 여전히 0개라 Stage 승격도 0개이고 NOT_READY가 맞다.
```

자세한 P1 결과는 아래 문서를 우선한다.

```text
census_v4_0701_rejected_mapping_feedback_retry_patch_2026-07-01.md
```

기준 질문:

```text
1. Stage가 있는 종목이 있긴 한가?
2. 그 Stage가 실제 운영 full thesis Stage인가?
3. Brain/Web/LLM이 실제로 자료를 가져오고 읽었는가?
4. 읽은 자료가 왜 점수와 Stage로 승격되지 않았는가?
5. 다음 패치는 어디를 고쳐야 하고, 어디를 건드리면 안 되는가?
```

## 최종 판정

현재 상태는 다음이 정확하다.

```text
Stage label은 있다.
하지만 전부 CENSUS_EVENT_BOARD 상태판이고, full thesis operating Stage는 0개다.

Brain/Web 검색, fetch, LLM extraction은 실제로 실행됐다.
하지만 Brain/Web accepted claim, Brain/Web score contribution, Brain/Web StageCourt trace,
그리고 대표 census_stage_status 승격 row는 모두 0개다.
```

쉬운 예:

```text
전교생 출석부에는 "출석", "상담 필요", "자료 확인 필요" 같은 상태가 붙었다.
하지만 기말고사 답안지를 채점해서 최종 성적을 낸 학생은 아직 없다.
```

따라서 지금 시스템은 "완성된 운영 채점 파이프라인"이 아니다. 다만 예전처럼 틀린 자료를 억지로 점수에 넣어 Stage를 만드는 상태도 아니다. 현재 guard는 위험한 입력을 막고 있고, 다음 패치는 막힌 이유를 planner에게 되돌려 다시 조사하게 만드는 쪽이어야 한다.

## 재현 명령

enabled smoke 실행 명령:

```bash
rm -rf /tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch

PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root /tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch \
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

예상 결과:

```text
NOT_READY
```

이 `NOT_READY`는 실패 은폐가 아니라 정직한 차단이다. 현재 Brain/Web 결과가 점수/Stage로 들어갈 자격을 아직 못 얻었기 때문이다.

최신 전체 테스트 기록:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 4959 tests in 156.646s
OK
```

주의:

```text
테스트 4959개 OK는 현재 guard와 기존 회귀 방어가 통과했다는 뜻이다.
Brain/Web accepted claim이 생겼다는 뜻은 아니다.
```

빠른 재검산 명령:

```bash
python - <<'PY'
import json
from pathlib import Path
from collections import Counter

root = Path('/tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch')

def rows(name):
    path = root / name
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

for name in [
    'planner_runs.jsonl',
    'source_task_executions.jsonl',
    'web_search_tasks.jsonl',
    'web_search_results.jsonl',
    'web_fetched_documents.jsonl',
    'claim_extractor_runs.jsonl',
    'raw_assertions.jsonl',
    'adjudicated_claims.jsonl',
    'brain_claim_mapping_trace.jsonl',
    'accepted_claims.jsonl',
    'score_contributions.jsonl',
    'stagecourt_traces.jsonl',
    'brain_to_claim_trace.jsonl',
    'census_stage_status.jsonl',
]:
    print(name, len(rows(name)))

stage_rows = rows('census_stage_status.jsonl')
mapping_rows = rows('brain_claim_mapping_trace.jsonl')

print('stage_scope', Counter(row.get('stage_scope') for row in stage_rows))
print('full_thesis_stage', Counter(row.get('full_thesis_stage') for row in stage_rows))
print('canonical_stage', Counter(row.get('canonical_stage') for row in stage_rows))
print('brain_trace_status', Counter(row.get('trace_status') for row in mapping_rows))
print('brain_mapping_status', Counter(row.get('mapping_status') for row in mapping_rows))
print('brain_rejection_reason', Counter(row.get('rejection_reason') for row in mapping_rows))
PY
```

## 산출물 교차검증

핵심 row count:

```text
planner_runs.jsonl:              22
source_task_executions.jsonl:    106
web_search_tasks.jsonl:            4
web_search_results.jsonl:         40
web_fetched_documents.jsonl:       8
web_rejected_documents.jsonl:      3
claim_extractor_runs.jsonl:        8
raw_assertions.jsonl:            146
adjudicated_claims.jsonl:        146
brain_claim_mapping_trace.jsonl:  54
accepted_claims.jsonl:            92
score_contributions.jsonl:        92
stagecourt_traces.jsonl:          92
brain_to_claim_trace.jsonl:        0
census_stage_status.jsonl:      3391
```

중요한 분리:

```text
accepted_claims 92개
= 기존 OpenDART event-board 경로
!= Brain/Web accepted claim

stagecourt_traces 92개
= 기존 event-board partial score trace
!= Brain/Web StageCourt trace
```

Brain/Web attempt만 따로 보면:

```text
Brain/Web raw assertion:       54
Brain/Web mapping trace:       54
Brain/Web accepted claim:       0
Brain/Web score contribution:   0
Brain/Web StageCourt trace:     0
Brain/Web promoted stage row:   0
```

즉 "자료를 가져오고 LLM이 읽은 것"과 "점수에 들어간 것"이 명확히 분리되어 있다.

## Stage 존재 여부

`census_stage_status.jsonl` 기준:

```text
stage_scope:
  CENSUS_EVENT_BOARD: 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

canonical_stage:
  0:      3306
  1:        54
  2:        30
  3-Red:     1

score_scope:
  NO_SCORE:                3324
  EVENT_WEIGHTED_PARTIAL:    67

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

operator_score_use:
  NOT_FULL_E2R_SCORE: 3391
```

정확한 답:

```text
Stage가 있는 애들은 있다.
하지만 그 Stage는 운영 full thesis Stage가 아니라 daily census event-board 상태다.
```

쉬운 예:

```text
Stage1 = "좋은 투자논리 1단계"가 아니라,
현재 산출물에서는 "오늘 확인할 이벤트가 잡힌 상태"에 가깝다.
```

## 삼성전자 / SK하이닉스 현재 의미

enabled smoke의 두 row:

```text
SK하이닉스 000660:
  canonical_stage: 1
  base_stage_display: EVENT_BOARD_STAGE1
  stage_scope: CENSUS_EVENT_BOARD
  full_thesis_stage: FULL_THESIS_NOT_RUN
  score_scope: EVENT_WEIGHTED_PARTIAL
  operator_stage_use: NOT_FULL_THESIS_STAGE
  operator_score_use: NOT_FULL_E2R_SCORE

삼성전자 005930:
  canonical_stage: 1
  base_stage_display: EVENT_BOARD_STAGE1
  stage_scope: CENSUS_EVENT_BOARD
  full_thesis_stage: FULL_THESIS_NOT_RUN
  score_scope: EVENT_WEIGHTED_PARTIAL
  operator_stage_use: NOT_FULL_THESIS_STAGE
  operator_score_use: NOT_FULL_E2R_SCORE
```

이것은 HBM/C06 full thesis Stage가 아니다.

`samsung_hynix_full_thesis_smoke.json` 기준:

```text
full_thesis_status: PENDING_FULL_THESIS_REFRESH
daily_event_and_full_thesis_separated: true
blocking_reason: full_thesis_source_tasks_planned_but_not_executed
```

공통 missing full thesis primitives:

```text
named_customer_or_customer_quality
qualification_status
capacity_allocation_or_pre_sold
hbm_shipment_or_revenue_mix
cash_or_revision_conversion
repeat_evidence_family
source_quorum
```

쉬운 예:

```text
삼성전자/하이닉스는 "출석부에 올라와 있음"이지,
"HBM 투자논리 채점이 끝남"이 아니다.
```

## Brain/Web 결과가 왜 accepted 0개인가

`brain_claim_mapping_trace.jsonl` 54줄의 판정:

```text
trace_status:
  REJECTED_BEFORE_SCORE: 54

accepted:
  False: 54

score_eligible:
  False: 54

mapping_status:
  REJECTED: 54

primitive_gap:
  volume_growth_visible:              50
  official_disclosure_status_current:  4

source_provider:
  Naver web:  35
  Naver news: 11
  OpenDART:    8

target_scope_status:
  UNRELATED: 35
  DIRECT:    19

rejection_reason:
  target_scope_not_direct:UNRELATED;mapping_not_accepted:REJECTED: 35
  mapping_not_accepted:REJECTED:                                  19
```

해석:

```text
35개는 대상 회사 직접 claim이 아니라서 차단됐다.
19개는 대상 회사 직접 claim이긴 하지만 해당 primitive 점수 칸에 들어갈 의미가 아니라서 차단됐다.
```

쉬운 예:

```text
네이버 검색으로 "대웅"을 찾았는데 여러 회사 이름이 섞인 기사라면,
대웅 점수에 넣으면 안 된다.

대웅 공시가 직접 공시라도,
"시설투자 종료일 연장 정정"이면 volume growth visible 점수로 바로 넣으면 안 된다.
```

이 rejection 자체는 대체로 올바른 방향이다. 문제는 rejection 이후에 멈춘다는 점이다.

## 현재 코드 병목

확인한 코드 위치:

```text
src/e2r/research_brain/v4_production_orchestrator.py
  _evidence_context_by_event
  _evidence_summary
  _retry_planner_for_missing_external_web_plan

src/e2r/research_brain/v4_planner_runtime.py
  build_v4_planner_prompt_payload
  planner prompt rules
```

현재 이미 있는 retry:

```text
LLM planner가 query_intents를 비워 둠
또는 external web source task를 안 냄
→ planner_feedback으로 다시 묻는다.
```

현재 없는 retry:

```text
문서를 가져옴
LLM extractor가 raw assertion을 만듦
adjudication/mapping에서 전부 rejected 됨
→ 그 rejection 사유를 planner에게 되돌려 다른 source/task를 계획하게 함
```

즉 지금 파이프라인은 여기서 끊긴다.

```text
SourceTask
  -> search/fetch
  -> EvidenceDocument/Anchor
  -> LLM raw assertion
  -> adjudicated rejected claim
  -> brain_claim_mapping_trace
  -> 끝
```

목표는 이 다음 루프다.

```text
rejected mapping trace
  -> planner feedback
  -> 다른 source/task/query 계획
  -> 다시 bounded acquisition
  -> accepted claim 또는 material pending/exhausted
```

## 다음 패치 P1

P1의 목적:

```text
accepted claim을 억지로 늘리는 것이 아니라,
rejected claim trace를 LLM planner에게 되돌려 더 나은 source/task를 계획하게 만든다.
```

구현 방향:

```text
1. _rejected_claim_feedback_from_bundle(...) 추가
2. _evidence_context_by_event(...)에 rejected_claim_feedback_by_event_id 추가
3. _evidence_summary(...)에 rejected_claim_feedback 구조화 필드 추가
4. planner prompt rule에 rejected feedback 사용 규칙 추가
5. source acquisition 후 rejected feedback retry 1회 추가
6. follow-up bundle을 기존 bundle과 append-only merge
7. follow-up planner run/source task/execution도 artifact에 남김
8. 대표 row 승격은 strict 조건을 그대로 유지
```

피드백 구조 예:

```json
{
  "source_task_id": "TASK-...",
  "primitive_gap": "volume_growth_visible",
  "source_url": "https://dart.fss.or.kr/...",
  "source_provider": "OpenDART",
  "claim_id": "CLM-...",
  "target_scope_status": "DIRECT",
  "directness": "DIRECT",
  "semantic_status": "PASS",
  "temporal_status": "CURRENT",
  "mapping_status": "REJECTED",
  "eligibility_reasons": ["mapping_not_accepted:REJECTED"],
  "rejection_summary": "direct current filing, but correction/extension wording did not establish volume growth"
}
```

LLM planner에게 주는 의미:

```text
이 문서는 이미 봤고, 이 이유로 점수 칸에 못 들어갔다.
같은 문서/같은 패턴을 반복하지 말고,
이 primitive를 직접 증명할 다른 source task를 계획하라.
단 score/stage/eligibility는 출력하지 마라.
```

## P1에서 절대 하면 안 되는 것

금지:

```text
1. mapping guard를 느슨하게 해서 accepted claim을 늘리기
2. "시설투자 정정"을 volume growth로 강제 인정하기
3. "검색 결과에 회사명이 있다"를 direct target claim으로 인정하기
4. deterministic 코드가 새 query template을 만들어내기
5. ticker, 종목명, C06/HBM 같은 예외 조건으로 우회하기
6. rejected claim을 조용히 삭제하거나 기존 ledger를 덮어쓰기
7. Brain/Web StageCourt trace 없이 census_stage_status를 승격하기
8. event-board Stage를 full thesis Stage처럼 출력하기
```

쉬운 예:

```text
오답 노트를 보고 다시 공부하게 해야지,
오답을 정답 처리하면 안 된다.
```

## P1 완료 기준

P1은 아래 둘 중 하나를 만들어야 한다.

성공 경로:

```text
rejected_claim_feedback이 planner prompt에 들어감
follow-up planner run이 생김
follow-up source task가 중복 없이 생김
새 source/fetch/extraction이 실행됨
accepted Brain/Web claim이 1개 이상 생김
그 accepted claim이 ScoreContribution과 StageCourt trace까지 연결됨
strict promotion 조건을 만족할 때만 census_stage_status 대표 row로 승격됨
```

정직한 pending 경로:

```text
rejected_claim_feedback이 planner prompt에 들어감
follow-up planner run이 생김
bounded source acquisition이 재시도됨
그래도 accepted claim이 없으면 NOT_READY 유지
왜 exhausted인지 source_task_execution/rejected trace에 남음
낮은 점수나 Red/4C로 확정하지 않음
```

P1 후 기대 가능한 count 변화:

```text
planner_runs.jsonl: 22보다 증가 가능
source_task_executions.jsonl: 106보다 증가 가능
brain_claim_mapping_trace.jsonl: 54보다 증가 가능

accepted_claims.jsonl:
  OpenDART event-board 92개는 그대로 유지
  Brain/Web accepted가 생기면 별도 origin/ref로 식별되어야 함

brain_to_claim_trace.jsonl:
  Brain/Web accepted가 생기면 0보다 커져야 함
```

P1 후에도 허용되는 상태:

```text
NOT_READY
```

단, 이 경우에는 "재시도도 했지만 source-backed accepted claim을 못 만들었다"는 장부가 있어야 한다.

## P1 테스트 요구

최소 테스트:

```text
1. _evidence_context_by_event가 rejected_claim_feedback을 existing_evidence_summary에 넣는다.
2. fake/spy planner provider가 retry 호출에서 rejected_claim_feedback을 실제로 받는다.
3. rejected feedback retry는 retry_max=1이면 실행되지 않는다.
4. rejected feedback retry는 provider 없음/fake/none 모드에서는 실행되지 않는다.
5. retry가 같은 source_task_id를 중복 생성하지 않는다.
6. follow-up bundle merge 후 기존 accepted claim/trace가 사라지지 않는다.
7. follow-up에서도 accepted claim 0개면 score/stage 승격은 0개로 유지된다.
8. prompt rule에는 score/stage/eligibility 출력 금지가 유지된다.
```

권장 실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_provider_failure_pending \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  -v
```

최종:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

그리고 enabled smoke를 다시 돌려야 한다.

## 다음 에이전트 공격 질문

다음 에이전트는 아래를 먼저 공격해야 한다.

```text
1. brain_claim_mapping_trace 54개가 진짜 rejected claim 단위인가, task 단위 요약인가?
2. DIRECT인데 mapping rejected 된 19개는 왜 rejected가 맞는가?
3. UNRELATED 35개가 혹시 실제 target claim인데 entity resolver가 과차단한 것은 아닌가?
4. rejected feedback을 planner에게 줄 때 score gap/Green 목표로 extraction을 오염시키지 않는가?
5. planner retry가 deterministic query template으로 변질되지 않는가?
6. follow-up retry가 unbounded crawling으로 변하지 않는가?
7. retry 후 accepted claim이 생겨도 Stage 승격 조건이 너무 쉽게 풀리지 않는가?
8. event-board OpenDART 92개와 Brain/Web accepted claim이 artifact에서 명확히 분리되는가?
9. 삼성전자/하이닉스 Stage1 표시가 UI나 downstream에서 full thesis Stage로 오해되지 않는가?
10. NOT_READY를 실패로 숨기지 않고 운영 pending으로 정확히 전달하는가?
```

## 최종 방향

궁극 목표는 아래 구조다.

```text
CensusAssessmentEvent
  -> CandidateEvent
  -> LLM planner source task
  -> bounded official/web acquisition
  -> EvidenceDocument/Anchor
  -> contract-blind raw assertion
  -> target/temporal/semantic adjudication
  -> primitive mapping
  -> accepted claim or rejected feedback
  -> retry if material and bounded
  -> ScoreContribution
  -> StageCourt
  -> promoted operating stage only if strict chain closes
```

핵심 원칙:

```text
트리거는 조사를 여는 문이고,
claim만 점수를 여는 열쇠다.
```

지금은 "문을 열고, 자료를 가져오고, 오답 노트까지 만들었다"까지 왔다.
다음 패치는 "오답 노트를 planner에게 되돌려 다시 찾게 하는 것"이다.
