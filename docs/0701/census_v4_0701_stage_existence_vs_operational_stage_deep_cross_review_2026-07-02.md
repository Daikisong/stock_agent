# Census v4 Stage 존재 여부와 운영 Stage 진실 교차검증

작성일: 2026-07-02  
기준 output: `output/census_v4/2026-07-01`  
질문: "뭔가 잘못되고 있는 거 맞지? stage가 있는 애들이 있긴 해?"

> 최신 수치 주의: 이 문서는 C15 패치 직후 스냅샷이다. C24 source-backed replay 이후 최신값은 `census_v4_0701_stage_existence_c24_patch_cross_review_packet_2026-07-02.md`와 `README.md`를 기준으로 한다. 최신 replay matrix는 `source_backed_ready_count=5`, `guard_replay_ready_count=5`, `missing_required_archetype_count=27`, controlled semantic replay는 `9/10 pass`다. Stage truth 자체는 변하지 않았다. 운영 `FULL_THESIS` row는 여전히 0개다.

## 최종 답

```text
Stage label이 있는 row는 있다.
하지만 운영용 FULL_THESIS Stage row는 아직 0개다.
```

현재 output의 Stage는 전부 `CENSUS_EVENT_BOARD` 범위다. 즉 "이번 전체 universe 점검에서 현재 공시/이벤트/claim이 있었는지 표시한 상태판"이다. 이것을 "E2R 전체 thesis를 끝까지 조사해서 100점 만점으로 산출한 운영 Stage"로 읽으면 안 된다.

쉬운 예:

```text
하이닉스 Stage1:
  공식 DART 이벤트 1개가 있어서 watch row로 올라온 상태다.
  HBM C06 전체 논리로 Stage1이라고 확정한 것이 아니다.

삼성전자 Stage1:
  공식 DART 이벤트 1개가 있어서 event-board 점수 4.0이 찍힌 상태다.
  삼성전자 HBM thesis 전체를 검증한 운영 점수/Stage가 아니다.

Stage0 3306개:
  "이번 census에서 현재 catalyst가 안 보임"이라는 뜻이다.
  "E2R 점수 0점인 나쁜 종목"이라는 뜻이 아니다.
```

따라서 현재 상태는 다음처럼 판단해야 한다.

```text
Anti-fake full universe status board:
  통과

Meaningful operational full-thesis stage:
  미통과

Full E2R 100점 verified score:
  0개
```

## 증거 요약

`census_stage_summary.json` 기준:

```text
stage_status_count = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391
  FULL_THESIS = 0

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

full_thesis_stage_distribution:
  FULL_THESIS_NOT_RUN = 3391

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use_distribution:
  NOT_FULL_E2R_SCORE = 3391

verified_score_present_count = 0
full_e2r_verified_score_count = 0
event_evidence_score_count = 67
```

핵심은 숫자가 2개로 갈린다는 점이다.

```text
Stage row가 있느냐?
  있다. 3391개다.

운영 Stage가 있느냐?
  없다. FULL_THESIS row는 0개다.
```

## Stage row의 실제 의미

현재 Stage row는 세 층으로 나누어야 한다.

### 1. CensusAssessmentEvent 상태판

```text
rows = 3306
canonical_stage = 0
score_scope = NO_SCORE
candidate_event_scope = ASSESSMENT_ONLY
stage_decision_status = NO_CURRENT_CATALYST
```

뜻:

```text
전체 universe 점검 대상으로 올라왔지만 현재 candidate event는 발견되지 않았다.
```

금지 해석:

```text
나쁜 종목이라서 E2R 0점이다.
FULL_THESIS에서 탈락했다.
```

### 2. Event-board watch Stage

```text
Stage1 = 54
Stage2-Watch = 30
3-Red = 1
```

뜻:

```text
공식 이벤트나 단일 material claim이 있어 상태판에 watch/risk 표시가 붙었다.
```

금지 해석:

```text
전체 아키타입 thesis를 검증해서 Stage1/Stage2/Red가 확정됐다.
```

### 3. Full-thesis 운영 Stage

```text
현재 row = 0
```

필요 조건:

```text
FULL_THESIS stage_scope
FULL_E2R_100 score_scope
full_e2r_verified_score 존재
source-backed claim -> primitive -> score contribution -> StageCourt 경로
material source gap이 있으면 pending 처리
```

현재는 이 단계가 실행되지 않았다.

## 대표 종목 확인

### 삼성전자

`census_stage_status.jsonl`의 삼성전자 row:

```text
symbol = 005930
company_name = 삼성전자
canonical_stage = 1
base_stage = Stage1
stage_scope = CENSUS_EVENT_BOARD
score_scope = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
full_e2r_verified_score = null
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
full_thesis_missing_primitives = ["full_thesis_refresh_task_not_run"]
accepted_claim_count = 1
candidate_event_count = 4
stage_decision_status = FINAL
stage_signal = OFFICIAL_EVENT_WATCH
```

해석:

```text
삼성전자 row에는 Stage1 label이 있다.
하지만 이것은 DART 이벤트 기반 event-board Stage1이다.
삼성전자 HBM/C06 전체 운영 Stage는 아직 계산되지 않았다.
```

이 row를 "삼성전자가 운영상 Stage1이다"라고 말하면 틀린 설명이다.

### SK하이닉스

`census_stage_status.jsonl`의 SK하이닉스 row:

```text
symbol = 000660
company_name = SK하이닉스
canonical_stage = 1
base_stage = Stage1
stage_scope = CENSUS_EVENT_BOARD
score_scope = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
full_e2r_verified_score = null
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
full_thesis_missing_primitives = ["full_thesis_refresh_task_not_run"]
accepted_claim_count = 1
candidate_event_count = 8
stage_decision_status = FINAL
stage_signal = OFFICIAL_EVENT_WATCH
```

해석:

```text
하이닉스도 Stage1 label은 있다.
하지만 HBM 고객 배정, qualification, capacity allocation, revenue mix, cash/revision conversion을 전부 엮은 FULL_THESIS 평가는 아니다.
```

쉬운 예:

```text
현재 row:
  "하이닉스 관련 공식 이벤트가 있다."

아직 없는 row:
  "하이닉스 HBM thesis가 C06 Evidence Contract를 만족해 어느 Stage인지 확정했다."
```

### Stage2-Watch sample

예시:

```text
삼부토건
canonical_stage = 2
base_stage = Stage2-Watch
stage_scope = CENSUS_EVENT_BOARD
score_scope = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.4
full_e2r_verified_score = null
stage_decision_status = PENDING_MATERIAL_GAPS
operator_stage_use = NOT_FULL_THESIS_STAGE
```

해석:

```text
공식 material claim 때문에 event-board에서 Stage2-Watch가 붙었다.
하지만 repeat evidence family, cash/revision conversion, multi-source confirmation이 없어서 full thesis Stage가 아니다.
```

### 3-Red sample

예시:

```text
드래곤플라이
canonical_stage = 3-Red
base_stage = Red
stage_scope = CENSUS_EVENT_BOARD
score_scope = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
full_e2r_verified_score = null
stage_decision_status = RISK_REVIEW
operator_stage_use = NOT_FULL_THESIS_STAGE
```

해석:

```text
위험 검토가 필요한 event-board row다.
운영 thesis의 3-Red/4B/4C 전이와 섞으면 안 된다.
```

## 교차검증 결과

### A. Stage summary와 stage status가 일치한다

`census_stage_summary.json`:

```text
stage_scope_distribution = {"CENSUS_EVENT_BOARD": 3391}
verified_score_present_count = 0
```

`census_stage_status.jsonl` 직접 집계:

```text
stage_scope = CENSUS_EVENT_BOARD 3391
full_e2r_verified_score non-null = 0
event_evidence_score non-null = 67
accepted_claim_count > 0 rows = 67
```

판정:

```text
report와 leaf artifact가 같은 말을 한다.
FULL_THESIS row가 숨겨져 있는 상태가 아니다.
```

### B. Atomic decisions도 event-board 범위다

`atomic_stage_decisions.jsonl`:

```text
rows = 92
stage_scope = CENSUS_EVENT_BOARD 92
score_scope = EVENT_WEIGHTED_PARTIAL 85
score_scope = NO_SCORE 7
canonical_stage:
  1 = 54
  2 = 37
  3-Red = 1
```

주의:

```text
atomic decision이 있다는 것은 "그 event row는 trace가 있다"는 뜻이다.
FULL_THESIS decision이 있다는 뜻이 아니다.
```

### C. Score contribution은 claim-backed이지만 full score가 아니다

`score_contributions.jsonl`:

```text
rows = 92
nonzero rows = 92
support_claim_ids present = 92
```

좋은 점:

```text
claim 없는 score contribution은 현재 확인되지 않았다.
```

한계:

```text
component_key는 event/official disclosure 수준이다.
FULL_E2R_100 점수표 전체를 채운 것이 아니다.
```

즉 "근거 있는 작은 event 점수"는 있지만 "운영 full thesis 점수"는 없다.

### D. Brain/Web/LLM은 이번 canonical run에서 꺼져 있다

`brain_web_readiness_gate_audit.json`:

```text
brain_web_mode = disabled
verdict = NOT_REQUESTED
llm_claim_extractor_attempt_count = 0
llm_planner_call_count = 0
web_search_call_count = 0
web_fetched_document_count = 0
web_or_llm_accepted_claim_count = 0
brain_web_evidence_pass_allowed = false
```

해석:

```text
이번 run은 Brain/Web 운영 증거 run이 아니다.
그래도 "Brain/Web을 돌렸다"고 과장하지는 않고 있다.
```

이것은 좋은 방어다. 하지만 목표 완료에는 부족하다.

### E. Full thesis smoke는 task만 만들고 실행하지 않았다

`samsung_hynix_full_thesis_smoke_audit.json`:

```text
verdict = PENDING_FULL_THESIS_REFRESH
score_allowed_before_execution = false
smoke_task_count = 14
required_symbols = ["005930", "000660"]
required_full_thesis_primitives:
  named_customer_or_customer_quality
  qualification_status
  capacity_allocation_or_pre_sold
  hbm_shipment_or_revenue_mix
  cash_or_revision_conversion
  repeat_evidence_family
  source_quorum
```

`full_thesis_smoke_tasks.jsonl`:

```text
rows = 14
task_status = PLANNING_REQUIRED 14
accepted_claim_ids = []
score_allowed_before_execution = false
```

해석:

```text
삼성전자/하이닉스 FULL_THESIS에 필요한 source task 목록은 있다.
하지만 실행과 accepted claim은 없다.
따라서 점수/Stage를 내면 안 된다.
```

이 방어는 맞다. 다만 아직 운영 pipeline이 완성된 것은 아니다.

### F. All-archetype replay는 3/32만 source-backed ready다

`all_archetype_replay_matrix.json`:

```text
required_archetype_count = 32
source_backed_ready_count = 3
guard_replay_ready_count = 3
missing_required_archetype_count = 29
all_archetype_replay_pass = false

READY:
  C06_HBM_MEMORY_CUSTOMER_CAPACITY
  C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
  C15_MATERIAL_SPREAD_SUPERCYCLE
```

해석:

```text
현재 C06/C08/C15는 source-backed replay가 닫혔다.
하지만 전 아키타입 운영 parity는 아직 멀었다.
```

### G. Controlled semantic replay도 7/10이다

`controlled_semantic_replay_audit.json`:

```text
case_count = 10
pass_count = 7
pending_count = 3
fail_count = 0
controlled_semantic_replay_pass = false

pending:
  C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
  C24_CLINICAL_BINARY_EVENT_GUARD
  C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

해석:

```text
known-bad와 C06/C08/C15 guard 일부는 통과했다.
하지만 C17/C24/C28 핵심 guard가 아직 닫히지 않았다.
```

## 그러면 "잘못되고 있는가?"

둘로 나눠서 봐야 한다.

### 시스템이 현재 상태를 숨기고 있지는 않다

좋은 점:

```text
FULL_THESIS_NOT_RUN = 3391
NOT_FULL_THESIS_STAGE = 3391
NOT_FULL_E2R_SCORE = 3391
brain_web_mode = disabled
web_fetched_document_count = 0
llm_planner_call_count = 0
score_allowed_before_execution = false
goal_completion_ready = false
```

이 말은 현재 output이 적어도 "안 한 것을 했다고 주장"하지는 않는다는 뜻이다.

### 하지만 사람이 Stage label만 보면 오해하기 쉽다

위험한 점:

```text
canonical_stage_distribution에 0/1/2/3-Red가 찍혀 있다.
삼성전자와 하이닉스도 Stage1처럼 보인다.
삼부토건 같은 종목은 Stage2-Watch처럼 보인다.
```

이 row들을 운영 Stage로 말하면 바로 문제가 된다.

쉬운 예:

```text
잘못된 설명:
  "하이닉스는 현재 Stage1입니다."

정확한 설명:
  "하이닉스는 Census event-board에서는 Stage1 watch row가 있습니다.
   하지만 full-thesis 운영 Stage는 아직 산출되지 않았습니다."
```

따라서 현재 가장 큰 문제는 계산 자체보다 **출력 의미가 너무 헷갈리는 것**이다.

## 다음 패치 방향

### 1. 운영 표시에 event-board Stage를 못 쓰게 막기

Operator-facing 출력에서는 다음 조건을 강제해야 한다.

```text
if stage_scope != FULL_THESIS:
  display_stage = "STATUS_BOARD_ONLY"
  operator_stage = null
  operator_stage_use = NOT_FULL_THESIS_STAGE
```

예:

```text
삼성전자:
  event_board_stage = Stage1
  operational_stage = null
  operational_status = FULL_THESIS_NOT_RUN
```

이렇게 보여야 사용자가 "삼성전자 Stage1이래"라고 오해하지 않는다.

### 2. `canonical_stage` 이름을 full-thesis와 event-board에서 분리

현재 `canonical_stage`는 Stage enum 값을 담고 있다. 하지만 scope가 `CENSUS_EVENT_BOARD`일 때도 `canonical_stage=1`이므로 매우 헷갈린다.

권장 출력:

```text
event_board_canonical_stage
full_thesis_canonical_stage
operator_canonical_stage
```

또는 최소한 report에는 다음을 크게 출력해야 한다.

```text
WARNING:
  canonical_stage in this file is scoped by stage_scope.
  CENSUS_EVENT_BOARD canonical_stage is not FULL_THESIS stage.
```

### 3. FULL_THESIS runner를 실제 source-backed로 실행하기 전까지 Stage 산출 금지

삼성전자/하이닉스 smoke는 현재 task만 만들었다. 다음 단계는 task 실행이다.

필수:

```text
bounded SourceTask 실행
official-first
LLM query generation allowed
accepted source-backed claims 생성
primitive states 생성
ScoreContribution 생성
StageCourt 실행
score_allowed_before_execution=false 유지
```

금지:

```text
task만 만든 뒤 Stage 산출
snippet-only score
source_proxy_only 연구자료 score 반영
unbounded general web fetch
```

### 4. C17/C24/C28 controlled semantic replay부터 닫기

현재 pending guard:

```text
C17:
  raw spread headline만으로 realized margin/FCF bridge를 열면 안 됨

C24:
  임상 binary headline만으로 endpoint/effect-size/regulatory/runway bridge를 열면 안 됨

C28:
  software/security 키워드만으로 ARR/RPO/renewal/retention bridge를 열면 안 됨
```

이 세 개가 닫히지 않으면 Brain/Web을 붙였을 때 다시 이상한 점수가 튈 위험이 크다.

### 5. 전 아키타입 source-backed replay matrix 확장

현재:

```text
source_backed_ready_count = 3 / 32
missing_required_archetype_count = 29
```

목표:

```text
32 / 32 source-backed positive + guard replay ready
source_proxy_only production contribution = 0
score contribution without accepted support claim = 0
```

## 다음 에이전트 공격 체크리스트

다음 에이전트가 완료 주장을 검증할 때 아래를 먼저 확인하면 된다.

```text
1. `census_stage_summary.json`에서 FULL_THESIS row가 0보다 큰가?
2. `FULL_E2R_100` score_scope row가 0보다 큰가?
3. `verified_score_present_count`가 0보다 큰가?
4. operator-facing report가 CENSUS_EVENT_BOARD Stage를 운영 Stage로 표시하지 않는가?
5. 삼성전자/하이닉스 full thesis smoke task가 실제 실행되었는가?
6. 그 실행에서 accepted_claim_ids가 생겼는가?
7. 그 accepted claim이 C06 required primitives에 매핑되었는가?
8. score contribution이 FULL_E2R_100 또는 명확한 full-thesis score로 생성되었는가?
9. material source gap이 있으면 낮은 Stage 확정이 아니라 pending으로 남는가?
10. Brain/Web/LLM call count가 0인데 Brain/Web pass를 주장하지 않는가?
11. source-backed replay ready가 C06/C08/C15만이 아니라 전 required archetype으로 확장되었는가?
12. C17/C24/C28 guard pending이 사라졌는가?
13. event-board Stage2-Watch row를 운영 Stage2로 홍보하지 않는가?
14. 3-Red event-board risk row를 4B/4C thesis transition으로 오해하지 않는가?
15. Stage0을 E2R 0점/탈락으로 해석하지 않는가?
```

## 재현 명령

아래 명령으로 이 문서의 핵심 숫자를 재검증했다.

```bash
python - <<'PY'
import json
from pathlib import Path
from collections import Counter
root=Path('output/census_v4/2026-07-01')

def rows(name):
    p=root/name
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]

stage=rows('census_stage_status.jsonl')
atomic=rows('atomic_stage_decisions.jsonl')
score=rows('score_contributions.jsonl')

for key in [
    'stage_scope',
    'canonical_stage',
    'base_stage',
    'score_scope',
    'operator_stage_use',
    'operator_score_use',
    'full_thesis_stage',
    'stage_decision_status',
    'stage_signal',
    'candidate_event_scope',
]:
    print(key, Counter(r.get(key) for r in stage))

print('stage rows', len(stage))
print('full_e2r_verified_score nonnull', sum(r.get('full_e2r_verified_score') is not None for r in stage))
print('event_evidence_score nonnull', sum(r.get('event_evidence_score') is not None for r in stage))
print('accepted_claim_count > 0 rows', sum((r.get('accepted_claim_count') or 0)>0 for r in stage))
print('atomic rows', len(atomic))
print('score contribution rows', len(score))
print('score contribution rows with support_claim_ids', sum(bool(r.get('support_claim_ids')) for r in score))
PY
```

## 현재 판정 문장

최신 상태를 한 문장으로 쓰면 다음이 맞다.

```text
현재 Census v4는 전 universe 상태판을 fake 없이 만들고, 일부 event-board Stage와 claim-backed partial event score를 생성하지만, 아직 FULL_THESIS 운영 Stage와 FULL_E2R_100 verified score는 하나도 생성하지 못했다.
```

이 문장이 바뀌려면 최소한 다음 숫자가 바뀌어야 한다.

```text
FULL_THESIS row > 0
FULL_E2R_100 row > 0
verified_score_present_count > 0
Brain/Web 또는 official source task가 실제 accepted full-thesis claim으로 연결
```
