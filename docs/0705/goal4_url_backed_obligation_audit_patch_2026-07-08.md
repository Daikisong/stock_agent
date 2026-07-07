# Goal4 URL-Backed Obligation Audit Patch - 2026-07-08

## 목적

`goal4.md`는 단순히 "36개 아키타입 row가 있다"가 아니라, 각 아키타입마다 다음 사슬을 증명하라고 요구한다.

```text
연구자료
→ runtime memory card
→ source route
→ source execution
→ accepted claim
→ score contribution
→ full thesis row
```

이번 패치는 이 사슬 중 특히 놓치기 쉬운 부분을 더 세게 드러내기 위한 감사 패치다.

쉬운 예:

```text
과거 진료기록(URL-backed 연구자료)이 있음
→ 이번 production에서 실제 검사를 다시 안 함
→ "자료가 있다"로 pass하면 안 됨
→ "재검사 미실행" 경고등이 켜져야 함
```

## 기존 약점

기존 `all_archetype_runtime_parity_matrix.json`은 36개 row를 만들고, runtime status도 나눴다.

하지만 다음 질문에 대한 상위 summary가 약했다.

```text
1. URL-backed 연구자료가 있는데 production source execution까지 못 간 아키타입이 있는가?
2. source_proxy_only 연구자료가 점수로 새는가?
3. runtime attempt가 없는데 이유도 없는 row가 있는가?
4. C05 하나만 의미 있는 pass처럼 보이는 상태를 하드 실패로 잡는가?
```

이 질문들이 row 안에 간접적으로 보이더라도, Goal4 감사에서는 상위 hard-failure count로 고정해야 한다.

## 패치 내용

대상 파일:

```text
src/e2r/census/all_archetype_runtime_status_matrix.py
tests/test_all_archetype_runtime_status_matrix.py
tests/test_all_archetype_runtime_parity_matrix.py
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.md
docs/operational/all_archetype_runtime_status_matrix.json
docs/operational/all_archetype_runtime_parity_matrix.json
docs/operational/all_archetype_runtime_parity_summary.md
```

새 row 필드:

```text
url_backed_replay_obligation_status
url_backed_replay_obligation_unmet
source_proxy_to_score_count
```

새 matrix summary 필드:

```text
url_backed_replay_obligation_status_counts
url_backed_case_exists_without_runtime_execution_count
url_backed_case_exists_without_runtime_execution_archetype_ids
source_proxy_to_score_count
source_proxy_to_score_archetype_ids
not_attempted_without_reason_count
not_attempted_without_reason_archetype_ids
c05_only_meaningful_runtime_parity_hard_fail
goal4_hard_failure_counts
goal4_hard_failures_clear
```

## URL-backed obligation 상태 정의

```text
NO_URL_BACKED_RESEARCH_CASES
```

연구 inventory에 URL-backed 사례가 없다. 이 상태 자체는 runtime replay 실패가 아니라 연구자료 부족 상태다.

```text
PRODUCTION_FULL_THESIS_ATTEMPTED
```

URL-backed 연구 기억이 production full thesis row까지 이어졌다. 단, required-positive/Green gap이 남아 있으면 여전히 meaningful pass는 아니다.

쉬운 예:

```text
C06 삼성전자 row가 생김
→ full thesis row 있음
→ 하지만 Green/required-positive gap 있음
→ "시도는 됐지만 완성은 아님"
```

```text
PRODUCTION_SOURCE_EXECUTED_NOT_FULL_THESIS_CLOSED
```

URL-backed 연구 기억이 source task 실행까지는 갔지만 full thesis row까지 닫히지 않았다.

쉬운 예:

```text
검사는 했음
→ 검사 결과가 점수 칸에 못 들어감
→ claim/primitive/score 연결 수리가 필요
```

```text
REPLAY_ACCEPTED_CLAIM_ONLY_NOT_PRODUCTION_EXECUTED
```

과거 replay accepted claim은 있지만 production source task 실행이 없다. 이 상태는 Goal4 hard failure로 잡힌다.

쉬운 예:

```text
예전 검사 결과지는 있음
→ 오늘 운영 검사는 안 함
→ 오늘 점수 확정 증거로 쓰면 안 됨
```

```text
URL_BACKED_CASE_EXISTS_BUT_PLANNER_ONLY
```

URL-backed 연구자료가 있는데 planner 가설까지만 있고 source execution이 없다.

```text
URL_BACKED_CASE_EXISTS_NOT_RUNTIME_ATTEMPTED
```

URL-backed 연구자료가 있는데 planner/source/full-thesis 어느 단계도 없다.

## 현재 재생성 결과

`docs/operational/all_archetype_runtime_parity_matrix.json` 기준:

```json
{
  "goal4_hard_failures_clear": false,
  "goal4_hard_failure_counts": {
    "c05_only_meaningful_runtime_parity_count": 0,
    "duplicate_parity_source_row_count": 0,
    "extra_parity_source_row_count": 0,
    "missing_parity_source_row_count": 0,
    "not_attempted_without_reason_count": 0,
    "runtime_parity_not_proven_count": 36,
    "source_proxy_to_score_count": 0,
    "url_backed_case_exists_without_runtime_execution_count": 1
  }
}
```

중요한 해석:

```text
source_proxy_to_score_count = 0
```

source_proxy_only 연구자료가 production score로 새는 증거는 없다.

```text
not_attempted_without_reason_count = 0
```

시도하지 않은 상태가 있더라도 이유 없이 비어 있는 row는 없다.

```text
url_backed_case_exists_without_runtime_execution_count = 1
```

URL-backed 연구자료가 있는데 production source execution이 없는 hard failure가 1개 있다.

대상:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK
```

C24 상세:

```text
research cases: 276
URL-backed cases: 60
replay accepted claims: 5
production source execution: 0
runtime status: PLANNING_ONLY
primary blocker: SOURCE_TASK_NOT_CREATED
URL obligation: REPLAY_ACCEPTED_CLAIM_ONLY_NOT_PRODUCTION_EXECUTED
```

쉽게 말하면:

```text
C24는 과거 연구자료와 replay claim이 있다.
하지만 이번 production runtime에서는 실제 source task 실행이 0이다.
그러므로 "연구자료가 있으니 pass"가 아니라 "운영 재검사 미실행"으로 막아야 한다.
```

## 전체 분포

```json
{
  "NO_URL_BACKED_RESEARCH_CASES": 3,
  "PRODUCTION_FULL_THESIS_ATTEMPTED": 6,
  "PRODUCTION_SOURCE_EXECUTED_NOT_FULL_THESIS_CLOSED": 26,
  "REPLAY_ACCEPTED_CLAIM_ONLY_NOT_PRODUCTION_EXECUTED": 1
}
```

해석:

```text
6개는 full thesis row까지 시도됨
26개는 source execution까지는 갔지만 full thesis가 안 닫힘
1개는 replay claim은 있지만 production source execution이 없음
3개는 URL-backed 연구자료가 없는 R13 계열
```

따라서 현재 상태는 `meaningful_runtime_parity_ready=false`가 맞다.

## 왜 이게 중요한가

이전에는 C24 같은 row가 `PLANNING_ONLY`로만 보였다.

그 표현도 틀리진 않지만, Goal4 관점에서는 더 강하게 말해야 한다.

```text
단순 planner-only
```

보다

```text
URL-backed 연구자료와 replay claim은 있는데 production source execution이 없음
```

이 훨씬 중요한 실패다.

이제 reviewer가 다음 질문을 바로 할 수 있다.

```text
C24는 왜 source task가 0인가?
replay accepted claim 5개는 어떤 source route로 production task가 되어야 하는가?
bio trial endpoint / safety / regulatory primitive 중 어떤 것이 materialize되지 않았는가?
```

## 현재 Goal4 완료 여부

완료 아님.

```text
runtime_parity_not_proven_count = 36
meaningful_runtime_parity_ready = false
goal4_hard_failures_clear = false
```

특히 full thesis row가 있는 6개도 required-positive/Green gap이 남아 있다.

쉬운 예:

```text
답안지를 제출한 학생 6명은 있음
하지만 필수 문제와 Green 승급 문제를 비워 둠
나머지 30명은 답안지가 없거나 채점표까지 못 감
그래서 반 전체 합격은 아님
```

## 검증

관련 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_all_archetype_runtime_status_matrix tests.test_all_archetype_runtime_parity_matrix -v
```

결과:

```text
Ran 12 tests
OK
```

## 다음 작업

가장 직접적인 다음 수리 대상은 C24다.

```text
C24 replay accepted claim 5개
→ bounded official-first source task로 변환
→ production source execution 생성
→ accepted claim이 endpoint/safety/regulatory/funding primitive로 닫히는지 확인
```

동시에 나머지 26개 `PRODUCTION_SOURCE_EXECUTED_NOT_FULL_THESIS_CLOSED` 아키타입은 source task 실행은 있으므로, accepted claim 생성 실패 원인을 primitive family mismatch, generic disclosure, temporal not current, mapping rejected로 나눠 수리해야 한다.

이 패치는 점수나 stage를 올리는 패치가 아니다. Goal4가 요구한 대로 "어디까지 실제 운영 경로가 닫혔고 어디서 막혔는지"를 더 거짓말 못 하게 만든 감사 패치다.
