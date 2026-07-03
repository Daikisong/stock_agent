# Census v4 0701 Stage Exists But Operational Stage Not Ready Cross Review

작성일: 2026-07-02 KST
repo: `/home/eorb915/projects/stock_agent`
as_of_date: `2026-07-01`

## 한 줄 결론

```text
Stage label은 있다.
하지만 현재 기본 production-style 산출물은 운영 FULL_THESIS Stage 지도가 아니다.
```

쉬운 예:

```text
현재 기본 실행:
전교생 3391명 출석부에 "결석 없음 / 관심 필요 / 추가 확인 필요" 같은 상태표는 붙었다.
하지만 각 학생의 정식 기말고사 100점 채점지는 아직 0명이다.

controlled smoke 실행:
삼성전자와 SK하이닉스 2명에게 모의 답안지를 흘려 배관은 확인했다.
하지만 그 모의 답안지는 LLM contract-blind extractor가 원문에서 다시 뽑은 source-backed semantic replay가 아니다.
```

따라서 사용자 질문인 "뭔가 잘못되고 있는 거 맞지? stage가 있는 애들이 있긴 해?"에 대한 답은 다음이다.

```text
1. Stage가 있는 행은 있다.
2. 기본 output 기준 stage_status_count = 3391이다.
3. 하지만 전부 CENSUS_EVENT_BOARD scope다.
4. 기본 output의 FULL_THESIS row는 0개다.
5. 기본 output의 full_e2r_verified_score_count도 0개다.
6. 그래서 "운영 확정 Stage/점수 지도"라고 부르면 안 된다.
```

## 교차검증 기준 산출물

이번 문서는 아래 세 산출물을 직접 비교했다.

```text
기본 production-style 검증 output:
output/test_census_v4_verified_full_tests

canonical operational docs copy source:
output/census_v4/2026-07-01

controlled smoke output:
output/test_census_v4_verified_full_tests_smoke
```

핵심 파일:

```text
census_stage_summary.json
census_stage_map.jsonl
census_stage_status.jsonl
atomic_stage_decisions.jsonl
goal_completion_audit.json
readiness_verdict.json
brain_web_readiness_gate_audit.json
full_thesis_production_audit.json
all_archetype_replay_matrix.json
c06_guard_replay_audit.json
controlled_semantic_replay_audit.json
known_bad_regression_report.json
```

## 현재 Stage 존재 여부

### 기본 production-style output

경로:

```text
output/test_census_v4_verified_full_tests
output/census_v4/2026-07-01
```

`census_stage_summary.json` 직접 확인 결과:

```text
stage_status_count = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

stage_decision_status_distribution:
  NO_CURRENT_CATALYST = 3306
  FINAL = 36
  PENDING_MATERIAL_GAPS = 30
  SOURCE_PENDING = 18
  RISK_REVIEW = 1

score_scope_distribution:
  EVENT_WEIGHTED_PARTIAL = 67
  NO_SCORE = 3324

verified_score_present_count = 0
full_e2r_verified_score_count = 0
full_thesis_stage_distribution = {"FULL_THESIS_NOT_RUN": 3391}
```

의미:

```text
Stage label은 전 종목에 있다.
하지만 그 label은 Census event board label이다.
FULL_E2R_100 점수 기반의 운영 Stage는 0개다.
```

쉬운 예:

```text
Stage0 3306개:
이번 일일 점검에서 현재 catalyst가 확인되지 않은 행이다.
"나쁜 종목"이라서 0점 Red라는 뜻이 아니다.

Stage1 54개:
공식 이벤트나 source pending이 있어서 watch 상태다.
정식 100점 thesis 점수가 아니다.

Stage2 30개:
material claim watch 또는 missing primitive가 있어 더 봐야 하는 상태다.
Green 후보를 Stage2로 확정했다는 뜻이 아니다.

3-Red 1개:
risk review 상태다.
단, 이것도 CENSUS_EVENT_BOARD scope이므로 full thesis 4C와 혼동하면 안 된다.
```

### 기본 production-style 예시 행

직접 집계한 예시:

```text
Stage1:
  000660 SK하이닉스
  scope = CENSUS_EVENT_BOARD
  status = FINAL
  score = daily event 4.0
  accepted_claim_count = 1
  signal = OFFICIAL_EVENT_WATCH

Stage2:
  001470 삼부토건
  scope = CENSUS_EVENT_BOARD
  status = PENDING_MATERIAL_GAPS
  score = daily event 4.4
  accepted_claim_count = 1
  signal = MATERIAL_CLAIM_WATCH

3-Red:
  030350 드래곤플라이
  scope = CENSUS_EVENT_BOARD
  status = RISK_REVIEW
  score = daily event 4.0
  accepted_claim_count = 1
  signal = RISK_REVIEW
```

이 예시는 중요하다.

```text
SK하이닉스가 기본 output에서 Stage1이라고 해서 C06/HBM thesis가 Stage1이라는 뜻이 아니다.
그 행은 일일 DART/공식 이벤트 상태판 행이다.
```

## controlled smoke output은 무엇인가

경로:

```text
output/test_census_v4_verified_full_tests_smoke
```

`census_stage_summary.json`:

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3389
  FULL_THESIS = 2

score_scope_distribution:
  EVENT_WEIGHTED_PARTIAL = 65
  FULL_E2R_100 = 2
  NO_SCORE = 3324

canonical_stage_distribution:
  0 = 3306
  1 = 52
  2 = 31
  3-Red = 1
  3-Yellow = 1

verified_score_present_count = 2
full_e2r_verified_score_count = 2
```

controlled smoke의 FULL_THESIS 2개:

```text
000660 SK하이닉스:
  stage_scope = FULL_THESIS
  canonical_stage = 3-Yellow
  full_e2r_verified_score = 88.0
  score_scale = FULL_E2R_100
  accepted_claim_count = 7
  stage_signal = FULL_THESIS_C06_HBM_STAGE

005930 삼성전자:
  stage_scope = FULL_THESIS
  canonical_stage = 2
  base_stage = Stage2-Watch
  full_e2r_verified_score = 72.0
  score_scale = FULL_E2R_100
  accepted_claim_count = 7
  stage_signal = FULL_THESIS_C06_HBM_STAGE
```

하지만 이 2개를 production pass로 읽으면 안 된다.

`full_thesis_production_audit.json`:

```text
production_pass_allowed = false
production_full_thesis_row_count = 0
controlled_smoke_full_thesis_row_count = 2
status = PENDING_FULL_THESIS_PRODUCTION
blockers = ["production_full_thesis_runner_not_implemented"]
```

쉬운 예:

```text
삼성전자 72점, 하이닉스 88점은 "배관이 점수를 합산할 수 있다"는 모의시험이다.
"실제 운영에서 원문을 다시 읽고 C06 claim을 뽑아 검증했다"는 뜻이 아니다.
```

## 가장 위험한 혼동: daily event score와 full thesis score

controlled smoke row에는 둘이 같이 보일 수 있다.

예:

```text
SK하이닉스 smoke row:
  daily_event_evidence_score = 4.0
  full_e2r_verified_score = 88.0
  score_scale = FULL_E2R_100

삼성전자 smoke row:
  daily_event_evidence_score = 4.0
  full_e2r_verified_score = 72.0
  score_scale = FULL_E2R_100
```

여기서 `daily_event_evidence_score=4.0`은 최근 공식 이벤트 상태판용 점수다.
`full_e2r_verified_score=72.0/88.0`은 controlled smoke의 C06 full thesis 모의 점수다.

따라서 다음 표현은 금지해야 한다.

```text
나쁜 표현:
삼성전자는 4점이다.
하이닉스는 기본 Census에서 Stage1이니 HBM thesis가 낮다.
controlled smoke 88점이 있으니 production full thesis가 완료됐다.
```

올바른 표현:

```text
기본 production-style:
삼성전자/하이닉스는 full thesis가 실행되지 않았고, daily event board 행만 있다.

controlled smoke:
삼성전자 72점 Stage2-Watch, 하이닉스 88점 3-Yellow 모의 row가 있다.
하지만 production runner가 아니고 semantic replay도 pending이다.
```

## Readiness와 Goal 상태

기본 production-style output의 `goal_completion_audit.json`:

```text
goal_completion_ready = false
blockers:
  brain_web_evidence_pass_false
  full_thesis_smoke_pending
  full_thesis_production_pass_false
  source_backed_replay_parity_all_archetypes_pending
  controlled_semantic_replay_pending
```

controlled smoke output의 `goal_completion_audit.json`:

```text
goal_completion_ready = false
blockers:
  brain_web_evidence_pass_false
  full_thesis_production_pass_false
  source_backed_replay_parity_all_archetypes_pending
  controlled_semantic_replay_pending
```

의미:

```text
controlled smoke에서는 full_thesis_smoke_pending만 빠진다.
하지만 production full thesis, Brain/Web evidence, all-archetype replay, controlled semantic replay는 여전히 막혀 있다.
```

`readiness_verdict.json` 공통 핵심:

```text
meaningful_operational_stage_pass = false
brain_web_evidence_pass = false
full_thesis_production_pass = false
all_archetype_replay_pass = false
controlled_semantic_replay_pass = false
```

## Brain/Web 상태

`brain_web_readiness_gate_audit.json`:

```text
brain_web_mode = disabled
verdict = NOT_REQUESTED
brain_web_evidence_pass_allowed = false
real_document_fetched_count = 0
llm_planner_call_count = 0
llm_claim_extractor_attempt_count = 0
source_task_execution_count = 0
web_search_call_count = 0
```

의미:

```text
이번 기본/canonical 산출물은 "Brain/Web이 실제로 원문을 찾아 읽었다"는 증거가 없다.
disabled 상태를 정직하게 disabled라고 적고 있는 것은 좋다.
하지만 이것은 운영 Brain/Web pass가 아니다.
```

쉬운 예:

```text
좋은 점:
"웹 조사 안 했는데 했다"고 거짓말하지 않는다.

아직 부족한 점:
실제 운영 목표는 selected candidate에 대해 official-first + bounded web/IR/report + LLM extraction이 돌아야 한다.
현재는 그 단계가 아직 아니다.
```

## All-archetype replay 상태

기본/canonical output의 `all_archetype_replay_matrix.json`:

```text
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 0
controlled_wiring_smoke_ready_count = 0
guard_replay_ready_count = 0
missing_required_archetype_count = 32
all_archetype_replay_pass = false
```

controlled smoke output:

```text
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 0
controlled_wiring_smoke_ready_count = 1
guard_replay_ready_count = 0
missing_required_archetype_count = 32
all_archetype_replay_pass = false
```

해석:

```text
C06은 controlled wiring smoke만 있다.
source-backed semantic replay ready가 아니다.
C08/C15/C17/C24/C28도 controlled semantic replay에서는 pending이다.
required 32개 아키타입의 source-backed positive+guard replay parity는 아직 없다.
```

## Controlled semantic replay 상태

`controlled_semantic_replay_audit.json`:

```text
controlled_semantic_replay_pass = false
case_count = 10
pass_count = 4
pending_count = 6
fail_count = 0
```

PASS:

```text
WRONG_SUBJECT_RISK_FIXTURE
OLD_RISK_RESOLVED_FIXTURE
PROVIDER_FAILURE_PENDING_FIXTURE
SEMANTIC_CONTRACT_GUARD_FIXTURE
```

PENDING:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

의미:

```text
월덱스 감사의견 오귀속, 과거 리스크 해소, provider failure, 비매출 계약 오인은 방어 테스트가 있다.
하지만 핵심 아키타입별 "positive 문서 + guard 문서" semantic replay는 아직 source-backed로 닫히지 않았다.
```

## C06 smoke overclaim 방지 상태

controlled smoke output의 `c06_guard_replay_audit.json`:

```text
positive_wiring_smoke_ready = true
positive_semantic_replay_ready = false
guard_cases_pass = true
guard_replay_pass = false
positive_guard_url_reuse_count = 3

blockers:
  c06_positive_semantic_replay_required_before_guard_pass
  controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted
  samsung_positive_smoke_reuses_c06_guard_urls
```

해석:

```text
C06 guard case 자체는 hard break false positive와 score leak 없이 통과했다.
하지만 삼성전자 positive smoke claim 일부가 C06 guard URL을 positive/current처럼 재사용했다.
따라서 C06을 source-backed semantic replay 완료로 세면 안 된다.
```

쉬운 예:

```text
같은 Reuters 지연 기사 하나를
"삼성전자 HBM positive evidence"와
"삼성전자 HBM qualification lag guard"로 동시에 쓰면 안 된다.

그 기사는 follow-up이 필요한 guard 문맥이지,
Green을 여는 positive claim이 아니다.
```

## Known-bad regression 상태

`known_bad_regression_report.json`:

```text
case_count = 11
모든 case status = PASS
```

확인된 주요 방어:

```text
wrong_subject_audit_opinion_not_target_risk = PASS
old_risk_resolved_not_current_hard_break = PASS
non_revenue_contract_not_contract_quality = PASS
source_proxy_score_guard = PASS
evidence_url_pending_score_guard = PASS
snippet_score_guard = PASS
provider_failure_final_score_guard = PASS
samsung_hynix_daily_event_not_full_thesis_or_4c = PASS
```

좋은 점:

```text
2020년 감사/회계 이슈처럼 오래됐고 해결된 risk를 현재 hard break로 쓰지 않는 방어가 생겼다.
월덱스 같은 타사 감사의견을 삼성전자 risk로 붙이는 종류의 오귀속 방어도 있다.
```

아직 부족한 점:

```text
known-bad 11개가 pass해도 아키타입별 positive thesis extraction이 완성됐다는 뜻은 아니다.
```

## 현재 무엇이 잘못되고 있나

문제를 한 문장으로 압축하면:

```text
가짜 완료 선언을 막는 방어막은 많이 생겼지만,
실제 운영 full thesis를 source-backed Brain/Web evidence로 채우는 실행 경로는 아직 닫히지 않았다.
```

더 구체적으로:

```text
1. 기본 output은 전 종목 상태판이지 운영 full thesis map이 아니다.
2. Stage label이 있으므로 "아무것도 없다"는 말도 틀렸지만, "운영 Stage가 완성됐다"도 틀렸다.
3. controlled smoke는 삼성/하이닉스 배관 검증일 뿐 production proof가 아니다.
4. Brain/Web mode가 disabled라서 LLM planner/extractor, web source task가 실제로 돌지 않았다.
5. all-archetype replay parity는 32개 required archetype 모두 pending이다.
6. C06 smoke는 positive semantic replay가 아니라 wiring smoke로만 세야 한다.
7. daily event score와 full thesis score가 같은 row에 같이 보일 수 있어 operator가 잘못 읽기 쉽다.
```

## 다음 패치 방향

### 1. Stage label 명칭을 더 공격적으로 분리

현재도 `stage_scope`, `score_scope`, `operator_stage_use`가 있지만 사람이 읽을 때 여전히 헷갈린다.

다음 패치에서 강화할 것:

```text
CENSUS_EVENT_BOARD row:
  operator_stage_use = NOT_FULL_THESIS_STAGE
  operator_score_use = NOT_FULL_E2R_SCORE
  canonical_stage_display 앞에 EVENT_BOARD_ prefix 유지
  full_thesis_not_run = true를 더 선명하게 노출

FULL_THESIS row:
  production_mode = CONTROLLED_SMOKE or PRODUCTION_LIVE
  controlled_smoke_allowed_for_completion = false
  source_backed_semantic_replay_status 필수
```

Acceptance:

```text
기본 output에서 FULL_THESIS_NOT_RUN row를 운영 full thesis로 읽을 수 있는 필드명/문구 0개.
controlled smoke row가 production pass로 count되는 경로 0개.
```

### 2. Brain/Web live path를 실제로 닫기

현재:

```text
brain_web_mode = disabled
llm_planner_call_count = 0
source_task_execution_count = 0
web_search_call_count = 0
```

목표:

```text
selected L3/L4 후보만 official-first SourceTask 생성
공식 소스로 해결 불가한 gap만 bounded web/IR/report fallback
LLM planner는 query/source intent 생성
LLM extractor는 contract-blind raw assertion 추출
코드는 anchor/date/entity/current/mapping 검증
accepted claim만 score contribution으로 연결
```

금지:

```text
전 종목 무제한 웹검색
snippet/headline 점수화
LLM이 stage/score 직접 출력
점수 gap을 보고 extractor가 답안 맞추기
```

### 3. Production full thesis runner 구현

현재:

```text
production_full_thesis_row_count = 0
blocker = production_full_thesis_runner_not_implemented
```

목표:

```text
controlled smoke와 별개로 production full thesis refresh task 생성
후보 선정 이유, source task, document, claim, primitive, contribution, StageCourt trace 연결
production row와 smoke row를 manifest에서 분리
```

Acceptance:

```text
full_thesis_production_audit.production_pass_allowed = true는
production_full_thesis_row_count > 0,
controlled_smoke_full_thesis_row_count와 별도,
Brain/Web 또는 official source trace가 claim-backed일 때만 가능.
```

### 4. All-archetype source-backed semantic replay 확대

현재:

```text
required 32개 중 source-backed semantic replay pass = 0
C06도 controlled wiring smoke only
```

목표:

```text
C06, C08, C15, C17, C24, C28 우선
각 아키타입에 positive case + guard case 최소 1개씩
source_proxy_only/evidence_url_pending row는 운영 fixture 정답 금지
직접 URL과 원문 anchor가 있는 case만 semantic replay로 승격
```

쉬운 예:

```text
C08:
제품 소개만 있는 문서 -> profile evidence, Green 불가
named customer/order 문서 -> customer/order primitive 가능
매출/마진 bridge 문서 -> Yellow/Green 쪽으로 이동 가능

C15:
원자재 가격 상승 기사 -> weather/trigger
회사 판가 전가와 realized margin 문서 -> score evidence
```

### 5. Score delta 감사 강화

앞으로 삼성전자 90점대에서 60점대로 흔들리는 일을 막으려면:

```text
모든 score delta > 0은 added/removed/superseded/contradicted claim delta로 설명
5점 이상 delta는 critical audit event
code/config/corpus/model hash가 다르면 NON_COMPARABLE 또는 EVIDENCE_UPDATE로 분류
```

Acceptance:

```text
점수 변화가 있는데 claim delta가 없으면 run failure.
같은 input replay 3회에서 score/stage 동일.
```

## 다음 에이전트가 공격해야 할 질문

아래 질문에 하나라도 답을 못 하면 "완료"가 아니다.

```text
1. 기본 output에서 FULL_THESIS row가 0개인데 왜 운영 Stage map이라고 부를 수 있는가?
2. Stage2 30개는 full thesis Stage2인가, event board watch인가?
3. 삼성전자/하이닉스 daily_event_evidence_score 4.0과 full_e2r_verified_score 72/88이 같은 화면에서 섞이지 않는가?
4. controlled smoke의 FTSMOKE claim은 contract-blind extractor가 원문에서 뽑은 것인가?
5. C06 삼성 positive smoke가 guard URL을 재사용하는데 왜 positive semantic replay로 세면 안 되는가?
6. brain_web_mode disabled인데 왜 LLM/웹 운영 준비라고 말할 수 있는가?
7. source_backed_ready_count가 0인데 왜 all-archetype replay parity라고 말할 수 있는가?
8. source_proxy_only/evidence_url_pending 연구자료가 score contribution으로 새지 않는가?
9. old resolved risk가 현재 4C/hard break로 들어가는 경로가 완전히 막혔는가?
10. production_full_thesis_runner_not_implemented blocker를 없애려면 어떤 source task trace가 필요한가?
```

## 재현 명령

핵심 JSON 교차검증:

```bash
python - <<'PY'
import json
from pathlib import Path

roots = [
    Path("output/test_census_v4_verified_full_tests"),
    Path("output/test_census_v4_verified_full_tests_smoke"),
    Path("output/census_v4/2026-07-01"),
]

for root in roots:
    print("\\n===", root, "===")
    summary = json.loads((root / "census_stage_summary.json").read_text())
    goal = json.loads((root / "goal_completion_audit.json").read_text())
    readiness = json.loads((root / "readiness_verdict.json").read_text())
    matrix = json.loads((root / "all_archetype_replay_matrix.json").read_text())
    semantic = json.loads((root / "controlled_semantic_replay_audit.json").read_text())
    prod = json.loads((root / "full_thesis_production_audit.json").read_text())
    brain = json.loads((root / "brain_web_readiness_gate_audit.json").read_text())

    print("stage_scope", summary.get("stage_scope_distribution"))
    print("canonical_stage", summary.get("canonical_stage_distribution"))
    print("score_scope", summary.get("score_scope_distribution"))
    print("full_e2r_verified_score_count", summary.get("full_e2r_verified_score_count"))
    print("goal_ready", goal.get("goal_completion_ready"))
    print("goal_blockers", goal.get("blockers"))
    print("readiness", {
        k: readiness.get(k)
        for k in [
            "meaningful_operational_stage_pass",
            "brain_web_evidence_pass",
            "full_thesis_smoke_pass",
            "full_thesis_production_pass",
            "all_archetype_replay_pass",
            "controlled_semantic_replay_pass",
        ]
    })
    print("matrix", {
        k: matrix.get(k)
        for k in [
            "source_backed_ready_count",
            "controlled_wiring_smoke_ready_count",
            "guard_replay_ready_count",
            "missing_required_archetype_count",
            "all_archetype_replay_pass",
        ]
    })
    print("semantic", {
        k: semantic.get(k)
        for k in ["case_count", "pass_count", "pending_count", "fail_count", "controlled_semantic_replay_pass"]
    })
    print("production", {
        k: prod.get(k)
        for k in ["production_pass_allowed", "production_full_thesis_row_count", "controlled_smoke_full_thesis_row_count", "blockers"]
    })
    print("brain", {
        k: brain.get(k)
        for k in ["brain_web_mode", "verdict", "llm_planner_call_count", "llm_claim_extractor_attempt_count", "source_task_execution_count", "web_search_call_count"]
    })
PY
```

## 최종 판정

현재 상태는 다음처럼 불러야 한다.

```text
정확한 명칭:
ANTI_FAKE_FULL_UNIVERSE_STATUS_BOARD with pending operational full thesis gates

부르면 안 되는 명칭:
READY_FOR_DAILY_TRIGGER_INTEGRATION
MEANINGFUL_OPERATIONAL_STAGE_PASS
FULL_LIVE_BRAIN_CENSUS
ALL_ARCHETYPE_REPLAY_PASS
PRODUCTION_FULL_THESIS_PASS
```

현재 잘된 부분:

```text
가짜 full thesis 완료 선언을 막는 audit이 생겼다.
daily event score와 full thesis score를 필드상 분리했다.
controlled smoke와 production full thesis를 분리했다.
C06 smoke overclaim을 source-backed replay로 세지 않게 막았다.
known-bad 11개 방어가 있다.
full repo unittest 4984개가 통과했다.
```

현재 안 된 부분:

```text
기본 production-style FULL_THESIS row = 0
Brain/Web/LLM 실행 = disabled
production full thesis runner = not implemented
source-backed all-archetype semantic replay = 0
controlled semantic replay = 4 PASS / 6 PENDING
C06 = wiring smoke only, semantic replay pending
```

다음 패치의 최우선 순위:

```text
1. Brain/Web live path를 selected candidate에 대해 실제로 실행한다.
2. production full thesis runner를 controlled smoke와 완전히 분리해서 구현한다.
3. C06/C08/C15/C17/C24/C28부터 source-backed positive+guard semantic replay를 만든다.
4. event board Stage가 운영 full thesis Stage로 오독되지 않게 UI/report/operator field를 더 강하게 분리한다.
5. 모든 score/stage 변화는 claim delta로 설명하게 한다.
```

