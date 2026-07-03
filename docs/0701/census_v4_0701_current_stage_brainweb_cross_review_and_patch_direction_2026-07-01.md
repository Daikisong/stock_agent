# Census v4 Current Stage / Brain-Web Cross Review And Patch Direction - 2026-07-01

작성 목적:

```text
사용자 질문:
  뭔가 잘못되고 있는 거 맞지?
  stage가 있는 애들이 있긴 해?

다음 에이전트 리뷰 목적:
  현재 산출물이 무엇을 통과했고,
  무엇을 아직 통과하지 못했으며,
  어느 코드 배관을 다음 패치 대상으로 봐야 하는지
  한 문서에서 공격 가능하게 고정한다.
```

이 문서는 결론을 좋게 포장하지 않는다.
현재 `output/census_v4/2026-07-01` 기준으로 통과한 것은
`ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS`이고,
아직 통과하지 못한 것은 `MEANINGFUL_OPERATIONAL_STAGE_PASS`,
`BRAIN_WEB_EVIDENCE_PASS`, `FULL_THESIS_SMOKE_PASS`다.

쉬운 예:

```text
지금은 전교생 출석부와 일부 쪽지시험 채점지가 조작 없이 붙어 있는지 확인한 상태다.
아직 전교생 기말고사 100점 만점 최종 성적표를 만든 상태가 아니다.
```

## 1. 짧은 결론

질문 1:

```text
뭔가 잘못되고 있는 거 맞지?
```

답:

```text
현재 결과를 "event-board 상태판"으로 부르면 맞다.
현재 결과를 "전 종목 full thesis 운영 Stage/점수"로 부르면 틀리다.
```

질문 2:

```text
Stage가 있는 애들이 있긴 해?
```

답:

```text
있다.
하지만 그 Stage는 full thesis 운영 Stage가 아니라 Census event-board label이다.
```

현재 Stage label:

```text
Stage0:       3306
Stage1:         54
Stage2-Watch:   30
Red:             1
```

현재 full thesis Stage:

```text
FULL_THESIS_NOT_RUN: 3391
```

따라서 다음 표현은 맞다.

```text
85개 종목에는 Stage0이 아닌 event-board label이 있다.
67개 종목에는 EVENT_WEIGHTED_PARTIAL 부분 이벤트 점수가 있다.
```

다음 표현은 틀리다.

```text
85개 종목의 full E2R thesis Stage가 끝났다.
67개 종목의 100점 만점 운영 점수가 끝났다.
삼성전자/하이닉스 HBM thesis 점수가 나왔다.
```

쉬운 예:

```text
Stage1은 "진료 접수됨"에 가깝다.
Stage2-Watch는 "추가 검사 필요"에 가깝다.
Green/Yellow/4B/4C 같은 최종 진단서가 아니다.
```

## 2. 기준 산출물

기준 경로:

```text
output/census_v4/2026-07-01
```

핵심 파일:

```text
census_stage_status.jsonl
readiness_verdict.json
goal_completion_audit.json
brain_web_attempt_audit.json
brain_web_readiness_gate_audit.json
brain_stage_promotion_audit.json
web_naver_acquisition_audit.json
samsung_hynix_full_thesis_smoke_audit.json
test_result_evidence_audit.json
```

현재 테스트 증거:

```text
test_result_evidence_audit.json:
  verdict: MACHINE_READABLE_TEST_ARTIFACT_PASS
  artifact_test_count: 4942
  artifact_status: OK
  artifact_duration_seconds: 170.2478
  artifact_log_sha256: aa894a5be988f1837df72bf33fa52b2ac452ee32e409b3b1c89fddfad77bf300
```

주의:

```text
4942 tests OK
!= goal.md 전체 완료
!= Brain/Web 운영 증거 pass
!= full thesis Stage pass
```

## 3. 산출물 1차 교차검증

`census_stage_status.jsonl` 3391행 기준:

```text
base_stage:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

canonical_stage:
  0:       3306
  1:         54
  2:         30
  3-Red:      1

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

stage_scope:
  CENSUS_EVENT_BOARD: 3391

score_scale:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

operator_score_use:
  NOT_FULL_E2R_SCORE: 3391
```

점수 필드:

```text
event_evidence_score_present:       67
verified_score_present:              0
full_e2r_verified_score_present:     0
is_full_thesis_stage_true:           0
accepted_claim_ids_present:          67
score_contribution_ids_present:      67
stagecourt_trace_id_present:         74
```

해석:

```text
event_evidence_score는 daily/census event-board 부분 점수다.
verified_score와 full_e2r_verified_score는 현재 0개다.
```

쉬운 예:

```text
event_evidence_score 4.0은 "이번 이벤트 점검에서 4점짜리 신호가 있다"는 뜻이다.
full_e2r_verified_score 90은 "전체 thesis를 100점 기준으로 다 채점했다"는 뜻인데,
현재 그런 row는 0개다.
```

## 4. Stage label 샘플

현재 non-Stage0 샘플:

```text
000660 SK하이닉스:
  base_stage: Stage1
  canonical_stage: 1
  event_evidence_score: 4.0
  score_scale: EVENT_WEIGHTED_PARTIAL
  full_thesis_stage: FULL_THESIS_NOT_RUN
  stage_signal: OFFICIAL_EVENT_WATCH
  stage_decision_status: FINAL

005930 삼성전자:
  base_stage: Stage1
  canonical_stage: 1
  score_scale: EVENT_WEIGHTED_PARTIAL
  full_thesis_stage: FULL_THESIS_NOT_RUN

001470 삼부토건:
  base_stage: Stage2-Watch
  canonical_stage: 2
  event_evidence_score: 4.4
  score_scale: EVENT_WEIGHTED_PARTIAL
  full_thesis_stage: FULL_THESIS_NOT_RUN
  stage_signal: MATERIAL_CLAIM_WATCH
  stage_decision_status: PENDING_MATERIAL_GAPS

003090 대웅:
  base_stage: Stage1
  canonical_stage: 1
  score_scale: NO_SCORE
  full_thesis_stage: FULL_THESIS_NOT_RUN
  stage_signal: EVIDENCE_INSUFFICIENT
  stage_decision_status: SOURCE_PENDING
```

위 샘플에서 가장 중요한 점:

```text
Stage1 / Stage2-Watch / Red label은 있다.
하지만 모든 샘플의 full_thesis_stage는 FULL_THESIS_NOT_RUN이다.
```

## 5. Readiness / Goal 2차 교차검증

`readiness_verdict.json`:

```text
verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
brain_web_mode: disabled
brain_web_evidence_pass: false
meaningful_operational_stage_pass: false
full_thesis_smoke_pass: false
blockers: []
```

`goal_completion_audit.json`:

```text
goal_completion_ready: false
blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending
brain_web_evidence_pass_allowed: false
full_thesis_status: PENDING_FULL_THESIS_REFRESH
```

해석:

```text
anti-fake gate는 통과했다.
goal completion은 실패가 정상이다.
```

쉬운 예:

```text
"가짜 성적표 방지 검사 통과"와 "최종 성적표 완성"은 다르다.
현재는 전자다.
```

## 6. Brain/Web 3차 교차검증

현재 canonical run은 Brain/Web disabled다.

행 수:

```text
planner_runs.jsonl:             0
web_search_tasks.jsonl:         0
web_search_results.jsonl:       0
web_fetched_documents.jsonl:    0
claim_extractor_runs.jsonl:     0

accepted_claims.jsonl:          92
score_contributions.jsonl:      92
stagecourt_traces.jsonl:        92
source_task_executions.jsonl:   92
```

주의:

```text
accepted_claims 92개는 Brain/Web live claims가 아니다.
현재 canonical run의 planner/web/extractor rows는 0개다.
```

`brain_web_attempt_audit.json`:

```text
verdict: NOT_REQUESTED
real_provider_success_count: 0
source_task_execution_count: 0
accepted_claim_count: 0
```

`brain_web_readiness_gate_audit.json`:

```text
verdict: NOT_REQUESTED
brain_web_mode: disabled
brain_web_evidence_pass_allowed: false
minimum_gate_applies: false
web_search_task_count: 0
web_fetched_document_count: 0
llm_claim_extractor_attempt_count: 0
source_task_execution_count: 0
brain_promoted_stage_row_count: 0
```

`web_naver_acquisition_audit.json`:

```text
verdict: DISABLED_HONESTY_PASS
pass_scope: disabled_honesty
web_search_task_count: 0
web_fetched_document_count: 0
```

해석:

```text
Brain/Web은 실행 성공이 아니라 "실행하지 않았고, 실행했다고 거짓말하지 않았다"가 현재 pass 범위다.
```

쉬운 예:

```text
"수술 안 했음"이라고 정확히 기록한 것은 좋은 장부다.
하지만 수술 성공은 아니다.
```

## 7. Source acquisition 코드 경로 분석

검토 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/census/census_runner_v4.py
src/e2r/research_brain/v4_schemas.py
```

현재 `SourceAcquisitionModeV4`:

```text
LIVE_OFFICIAL_FIRST
FROZEN_REAL_SOURCE_SNAPSHOT
LIVE_OFFICIAL_ONLY
LIVE_FULL_BOUNDED
TEST_FAKE
```

문제의 핵심:

```text
LIVE_FULL_BOUNDED라는 enum은 있다.
하지만 SourceAcquisitionRunnerV4.acquire()의 실제 흐름은:

1. live_official_first / live_official_only / live_full_bounded이면
   _acquire_live_official_sources()를 먼저 호출한다.

2. live official이 PARSED이면 반환한다.

3. live_official_only면 실패/무증거라도 반환한다.

4. 그 외에는 stored snapshot fallback으로 내려간다.
```

즉 현재 코드에서 보이는 실제 acquisition 배관은:

```text
official connector
또는 stored snapshot fallback
```

이고,
`web_search_tasks.jsonl`, `web_search_results.jsonl`,
`web_fetched_documents.jsonl`을 채우는 live web/Naver full-source acquisition 배관은
현재 canonical artifact 기준 0행이다.

쉬운 예:

```text
메뉴판에는 "풀코스"라고 써 있지만,
현재 주방 배관은 공식자료 한 접시를 먼저 내고,
안 되면 냉장고의 저장 반찬을 꺼내는 흐름이다.
웹/뉴스/Naver를 실제로 주문하고 가져오는 별도 접시는 아직 완성되지 않았다.
```

## 8. Brain/Web readiness gate가 요구하는 것

`_brain_web_readiness_gate_audit()`는 enabled/full live 모드에서 아래를 요구한다.

```text
real planner success > 0
source_task_executions rows > 0
non-snapshot real evidence_documents rows > 0
web/news search/fetch rows
LLM claim extractor attempt 또는 accepted Brain/Web claim
accepted claim > 0
brain_to_claim_trace rows
claim-backed score_contributions
StageCourt traces
strict promotion into census_stage_status
snapshot/fake/snippet/provider-failure score leakage 0
```

특히 `run_mode in {"BRAIN_AND_WEB_ACQUISITION_ENABLED", "FULL_LIVE_BRAIN_CENSUS"}`이면:

```text
web_search_tasks.jsonl row > 0
web_fetched_documents.jsonl row > 0
```

가 필요하다.

따라서 accepted claim이 하나 생겨도,
웹/뉴스 acquisition이 0행이면 full Brain/Web pass가 아니다.

쉬운 예:

```text
의사가 한 명 의견을 냈어도,
필수 검사 결과지가 없으면 "정밀검사 완료" 도장을 찍으면 안 된다.
```

## 9. 현재 상태가 "잘못"인지 판정

정상인 부분:

```text
1. full thesis를 안 돌렸으면 FULL_THESIS_NOT_RUN으로 남긴다.
2. Brain/Web을 안 돌렸으면 NOT_REQUESTED로 남긴다.
3. claim 없는 종목은 0점 Red가 아니라 Stage0 / NoCurrentCatalyst로 남긴다.
4. provider/source pending은 낮은 점수 확정이 아니라 SOURCE_PENDING/PENDING_MATERIAL_GAPS로 남긴다.
5. event-board partial score와 full E2R score를 분리한다.
```

문제인 부분:

```text
1. 사람이 Stage1/Stage2-Watch를 full thesis Stage처럼 읽을 여지가 아직 크다.
2. LIVE_FULL_BOUNDED 이름과 실제 웹/Naver acquisition 구현 사이에 간극이 있다.
3. 삼성전자/하이닉스 C06/HBM full thesis는 planning task만 있고 아직 실행/채점이 아니다.
4. Brain/Web enabled smoke가 안정적으로 accepted claim -> score -> StageCourt -> promoted row까지 닫히지 않는다.
5. 전 아키타입 Evidence Contract replay parity는 아직 완료되지 않았다.
```

따라서 정확한 결론:

```text
장부 정직성은 개선됐다.
운영 채점 엔진은 아직 미완성이다.
```

## 10. 다음 패치 방향

### Patch 1. UI/report overclaim 차단

목표:

```text
사용자 화면과 문서에서 Stage1/Stage2-Watch/Red를 full thesis Stage처럼 보이지 않게 한다.
```

필수 조건:

```text
stage_scope=CENSUS_EVENT_BOARD이면:
  label 앞에 Event Board / Census Status를 붙인다.

operator_stage_use=NOT_FULL_THESIS_STAGE이면:
  "운영 Stage 확정" 문구를 금지한다.

full_thesis_stage=FULL_THESIS_NOT_RUN이면:
  Green/Yellow/4B/4C와 비교하지 않는다.
```

쉬운 예:

```text
나쁜 출력:
  SK하이닉스 Stage1 4점

좋은 출력:
  SK하이닉스 Census Event Board Stage1, partial event score 4.0,
  full thesis not run
```

### Patch 2. LIVE_FULL_BOUNDED를 이름값 하게 만들기

목표:

```text
live_full_bounded가 실제 bounded web/news/Naver acquisition 산출물을 만든다.
```

필수 산출물:

```text
web_search_tasks.jsonl
web_search_results.jsonl
web_fetched_documents.jsonl
web_rejected_documents.jsonl
claim_extractor_runs.jsonl
```

정책:

```text
official-first
bounded budget
dedupe-before-fetch
stop-on-resolution
snippet-only score 금지
provider failure는 낮은 점수 확정 금지
```

테스트 기대:

```text
BRAIN_AND_WEB_ACQUISITION_ENABLED에서
web_search_tasks=0인데 Brain/Web pass면 실패.

web_fetched_documents=0인데 Brain/Web pass면 실패.

provider unavailable이면:
  NOT_READY 또는 PROVIDER/SOURCE_PENDING
  낮은 점수 FINAL 금지.
```

### Patch 3. Brain/Web accepted claim 안정화

목표:

```text
enabled smoke가 매번 같은 의미로 닫힌다.
```

필수 chain:

```text
planner_runs
-> source_tasks
-> source_task_executions
-> evidence_documents
-> evidence_anchors
-> raw_assertions
-> adjudicated_claims
-> accepted_claims
-> primitive_states
-> score_contributions
-> stagecourt_traces
-> brain_to_claim_trace
-> census_stage_status promoted row
```

모든 ID는 같은 claim을 가리켜야 한다.

쉬운 예:

```text
증거 문서 A에서 claim C를 뽑았으면,
점수 contribution도 C를 지원해야 하고,
StageCourt trace도 C를 들고 있어야 한다.
중간에 claim D로 바뀌면 count가 맞아도 실패다.
```

### Patch 4. 삼성전자/하이닉스 C06 full thesis smoke 실행

현재:

```text
samsung_hynix_full_thesis_smoke_audit.json:
  verdict: PENDING_FULL_THESIS_REFRESH
  full_thesis_status: PENDING_FULL_THESIS_REFRESH
```

필요:

```text
2개 종목 x 7개 C06/HBM primitive task 실행
source-backed accepted claim
primitive state
score contribution
StageCourt trace
full_thesis_stage 또는 material pending
```

주의:

```text
full_thesis_smoke_tasks.jsonl은 task 계획서다.
그 자체는 점수 근거가 아니다.
```

### Patch 5. 전 아키타입 replay parity

목표:

```text
모든 아키타입에서 과거 연구자료가 만든 positive/guard 경계를
Evidence Contract v2와 replay fixture로 검증한다.
```

원칙:

```text
직접 URL 있는 연구자료:
  golden replay fixture 가능

source_proxy_only / evidence_url_pending:
  ontology/contract 참고만 가능
  운영 점수 정답으로 사용 금지
```

쉬운 예:

```text
연구 MD에 "이건 Green"이라고 적혀 있어도,
원문 URL과 as_of_date 기준 claim anchor가 없으면 운영 점수 정답이 아니다.
```

## 11. 다음 에이전트 공격 질문

다음 에이전트는 아래 질문을 먼저 때려야 한다.

```text
1. full_thesis_stage가 FULL_THESIS_NOT_RUN이 아닌 row가 있는가?
   있다면 full thesis accepted claim/score/StageCourt trace가 실제로 있는가?

2. stage_scope=CENSUS_EVENT_BOARD인데 UI/report가 "운영 Stage"라고 말하는가?

3. EVENT_WEIGHTED_PARTIAL score를 FULL_E2R_100 score처럼 합산하거나 비교하는가?

4. Brain/Web enabled run에서 web_search_tasks와 web_fetched_documents가 0인데 pass가 나는가?

5. accepted claim count만 맞고 brain_to_claim_trace / score_contribution / StageCourt ID가 어긋나는가?

6. live_full_bounded가 실제 웹/Naver provider를 호출하지 않고 snapshot fallback만으로 pass하는가?

7. provider failure 또는 source pending row가 낮은 점수 FINAL로 확정되는가?

8. 삼성전자/하이닉스 C06 full thesis가 daily event-board Stage1과 섞여 출력되는가?

9. source_proxy_only 연구자료가 운영 점수로 들어가는가?

10. as_of_date 이후 자료가 accepted claim이나 score contribution으로 들어가는가?
```

## 12. 다음 에이전트 재검산 명령

```bash
python - <<'PY'
import json
from collections import Counter
from pathlib import Path

root = Path("output/census_v4/2026-07-01")
rows = [
    json.loads(line)
    for line in (root / "census_stage_status.jsonl").read_text().splitlines()
    if line.strip()
]

print("rows", len(rows))
for field in [
    "base_stage",
    "canonical_stage",
    "full_thesis_stage",
    "stage_scope",
    "score_scale",
    "operator_stage_use",
    "operator_score_use",
    "stage_signal",
    "stage_decision_status",
    "score_valid_status",
    "investigation_status",
]:
    print(field, dict(Counter(str(row.get(field)) for row in rows)))

print("event_evidence_score_present", sum(row.get("event_evidence_score") is not None for row in rows))
print("verified_score_present", sum(row.get("verified_score") is not None for row in rows))
print("full_e2r_verified_score_present", sum(row.get("full_e2r_verified_score") is not None for row in rows))
print("is_full_thesis_stage_true", sum(bool(row.get("is_full_thesis_stage")) for row in rows))
print("accepted_claim_ids_present", sum(bool(row.get("accepted_claim_ids")) for row in rows))
print("score_contribution_ids_present", sum(bool(row.get("score_contribution_ids")) for row in rows))
print("stagecourt_trace_id_present", sum(bool(row.get("stagecourt_trace_id")) for row in rows))

for name in [
    "readiness_verdict.json",
    "goal_completion_audit.json",
    "brain_web_readiness_gate_audit.json",
    "brain_web_attempt_audit.json",
    "web_naver_acquisition_audit.json",
    "brain_stage_promotion_audit.json",
    "samsung_hynix_full_thesis_smoke_audit.json",
    "test_result_evidence_audit.json",
]:
    payload = json.loads((root / name).read_text())
    print("\\n#", name)
    for key in [
        "verdict",
        "goal_completion_ready",
        "blockers",
        "brain_web_mode",
        "brain_web_evidence_pass",
        "meaningful_operational_stage_pass",
        "full_thesis_smoke_pass",
        "brain_web_evidence_pass_allowed",
        "full_thesis_status",
        "minimum_gate_applies",
        "pass_scope",
        "web_search_task_count",
        "web_fetched_document_count",
        "llm_claim_extractor_attempt_count",
        "real_provider_success_count",
        "source_task_execution_count",
        "accepted_claim_count",
        "brain_promoted_stage_row_count",
        "artifact_test_count",
        "artifact_status",
    ]:
        if key in payload:
            print(key, payload[key])
PY
```

현재 기대값:

```text
rows 3391
full_thesis_stage {'FULL_THESIS_NOT_RUN': 3391}
stage_scope {'CENSUS_EVENT_BOARD': 3391}
operator_stage_use {'NOT_FULL_THESIS_STAGE': 3391}
operator_score_use {'NOT_FULL_E2R_SCORE': 3391}
event_evidence_score_present 67
verified_score_present 0
full_e2r_verified_score_present 0
is_full_thesis_stage_true 0

readiness verdict:
  ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS

goal_completion_ready:
  false

goal blockers:
  brain_web_evidence_pass_false
  full_thesis_smoke_pending

brain_web_readiness_gate:
  NOT_REQUESTED
  brain_web_evidence_pass_allowed false

web_naver_acquisition:
  DISABLED_HONESTY_PASS
  pass_scope disabled_honesty
  web_search_task_count 0
  web_fetched_document_count 0

samsung_hynix_full_thesis_smoke:
  PENDING_FULL_THESIS_REFRESH

test_result_evidence:
  artifact_test_count 4942
  artifact_status OK
```

## 13. 최종 리뷰 판정

현재 상태를 한 문장으로 쓰면:

```text
Census v4는 가짜 full-universe Stage/점수 완료 선언을 막는 상태판으로는 통과했지만,
LLM Brain/Web과 full thesis 운영 채점 파이프라인은 아직 통과하지 못했다.
```

따라서 다음 작업은 "점수표를 다시 조정"하는 것이 아니다.

정확한 다음 작업:

```text
1. Event-board 출력과 full-thesis 출력이 UI/report에서 절대 섞이지 않게 한다.
2. live_full_bounded에 실제 bounded web/news/Naver acquisition 산출물을 만든다.
3. web/full-source 문서에서 Evidence OS claim extraction을 실제 실행한다.
4. accepted claim -> primitive -> score -> StageCourt -> promoted row ID chain을 닫는다.
5. 삼성전자/하이닉스 C06 smoke를 daily event와 분리해 full thesis로 실행한다.
6. 전 아키타입 replay parity를 source-backed fixture로 검증한다.
```

완료라고 말할 수 있는 기준:

```text
goal_completion_ready=true
meaningful_operational_stage_pass=true
brain_web_evidence_pass=true
full_thesis_smoke_pass=true
test_result_evidence_audit PASS
known_bad_regression PASS
web_search/fetch/extractor rows > 0
full_thesis_stage가 실제 claim-backed trace와 함께 존재
```

그 전까지는:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

만 말해야 한다.
