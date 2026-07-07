# Goal4 C24 Replay Symbol Handoff Patch - 2026-07-08

## 목적

이번 패치는 `C24_BIO_TRIAL_DATA_EVENT_RISK`의 URL-backed replay 의무가 다음 runtime 실행 계획으로 제대로 이어지도록 만든다.

Goal4 기준에서 중요한 사슬은 다음이다.

```text
연구자료
→ replay/source-backed 기억
→ 다음 runtime source task
→ 현재 원문 재검증
→ accepted claim
→ score contribution
→ full thesis row
```

이번에 확인된 문제는 이 사슬의 두 번째와 세 번째 사이에서 생겼다.

쉬운 예:

```text
예전 진료 기록에 재검사해야 할 환자 A, B가 적혀 있음
→ 그런데 다음 예약표에는 전혀 다른 환자 C가 올라감
→ A, B의 재검사 의무가 사라진 것처럼 보임
```

E2R로 바꾸면 다음과 같다.

```text
C24 replay matrix에는 source-backed symbol 009420, 215600이 있음
→ 그런데 next attempt planner는 source_proxy_only 연구 후보 000100 쪽으로 target을 잡음
→ C24 URL-backed replay obligation이 실제 다음 source task로 이어지지 않음
```

## 기존 상태

`docs/operational/all_archetype_runtime_parity_matrix.json` 기준 C24는 다음 상태였다.

```text
runtime_status: PLANNING_ONLY
primary_blocker_class: SOURCE_TASK_NOT_CREATED
url_backed_replay_obligation_status: REPLAY_ACCEPTED_CLAIM_ONLY_NOT_PRODUCTION_EXECUTED
url_backed_case_count: 60
replay_accepted_claim_count: 5
runtime_source_task_count: 0
runtime_source_task_executed_count: 0
```

해석:

```text
C24에는 URL-backed 연구자료와 replay accepted claim이 있다.
하지만 production source task가 아직 0개라서 점수/Stage 증거로 쓸 수 없다.
```

중요한 점:

```text
replay accepted claim이 있다
!= 오늘 production에서 현재 원문 검증이 끝났다
```

따라서 이 상태는 pass가 아니라 hard failure로 남아야 한다.

## 새로 연결한 경로

이번 패치는 다음 필드를 runtime parity/status matrix에서 next attempt planner까지 전달한다.

```text
source_backed_replay_symbols
source_backed_replay_candidate_ids
url_backed_replay_obligation_status
url_backed_replay_obligation_unmet
```

C24의 현재 전달값:

```json
{
  "source_backed_replay_symbols": ["009420", "215600"],
  "source_backed_replay_candidate_ids": [
    "RPLAY-db4d394cff34a673dc59",
    "RPLAY-df585429523a163e5ba6",
    "RPLAY-e8c3226596e8da7f3db8"
  ],
  "url_backed_replay_obligation_status": "REPLAY_ACCEPTED_CLAIM_ONLY_NOT_PRODUCTION_EXECUTED",
  "url_backed_replay_obligation_unmet": true
}
```

이제 next attempt planner는 C24를 다음처럼 잡는다.

```text
target_symbol_mode: SYMBOL_SPECIFIC
target_symbols: 009420, 215600
target_materialization_candidates: []
target_symbol_source_backed_replay_support_count: 2
```

즉 `000100` 같은 source_proxy_only 후보를 target으로 쓰지 않고, replay matrix에서 source-backed로 확인된 symbol을 다음 runtime source task의 target으로 넘긴다.

## 점수 증거로 쓰지 않는 안전장치

이번 패치는 replay 자료를 바로 점수에 넣지 않는다.

각 replay support에는 다음 플래그가 붙는다.

```text
score_evidence_allowed_from_replay: false
target_materialization_source: CENSUS_V4_ALL_ARCHETYPE_REPLAY_MATRIX
target_materialization_status: SOURCE_BACKED_REPLAY_SYMBOL_RECHECK_REQUIRED
```

쉬운 예:

```text
예전 검사 기록은 오늘 검사를 받을 사람을 고르는 데만 사용한다.
예전 검사 기록 자체로 오늘 진단서를 발급하지 않는다.
```

E2R 운영 의미:

```text
009420, 215600은 C24 runtime source task의 target 후보가 된다.
하지만 점수/Stage는 새 source task가 현재 원문을 fetch하고 accepted Evidence OS claim을 만든 뒤에만 가능하다.
```

## task 수 변화

패치 전에는 next attempt가 총 108개 source task였다.

패치 후:

```json
{
  "source_task_count": 111,
  "seed_event_count": 111,
  "target_symbol_mode_counts": {
    "ARCHETYPE_LEVEL_DISCOVERY": 3,
    "SYMBOL_SPECIFIC": 33
  },
  "source_backed_replay_symbol_target_archetype_count": 1,
  "source_backed_replay_symbol_target_task_count": 6,
  "url_backed_replay_obligation_unmet_task_count": 6,
  "target_materialization_required_task_count": 9
}
```

왜 111개인가:

```text
C24 replay target symbol 2개
× C24 required primitive gap 3개
= 6개 source task

기존 source_proxy 후보 000100 기반 task 3개는 빠짐
따라서 108 - 3 + 6 = 111
```

C24의 6개 task는 다음 조합이다.

```text
009420 × approval_not_confirmed
009420 × binary_event_unresolved
009420 × trial_quality_visible
215600 × approval_not_confirmed
215600 × binary_event_unresolved
215600 × trial_quality_visible
```

## 코드 변경 요약

대상 파일:

```text
src/e2r/census/research_to_runtime_parity.py
src/e2r/census/all_archetype_runtime_status_matrix.py
src/e2r/census/all_archetype_next_attempt_planner.py
```

변경 내용:

```text
1. replay matrix의 source_backed_replay_symbols를 parity/status row로 전달
2. url_backed_replay_obligation_unmet=true인데 일반 symbol이 없으면 replay symbol을 target_symbols로 사용
3. replay support를 planner input으로만 기록
4. replay support task query intent에 "현재 직접 원문 재검증 필요"를 명시
5. summary에 replay-symbol target task count를 추가
```

## 테스트로 고정한 조건

추가/수정된 테스트는 다음을 고정한다.

```text
C24 source_backed_replay_symbols == ["009420", "215600"]
C24 target_symbol_mode == SYMBOL_SPECIFIC
C24 target_symbols == ["009420", "215600"]
C24 target_materialization_candidates == []
C24 target_symbol_source_backed_replay_support_count == 2
모든 replay support는 score_evidence_allowed_from_replay == false
replay source task는 6개
replay source task는 target_symbol_research_memory_support를 쓰지 않음
source_task_count == seed_event_count == 111
```

## 아직 완료가 아닌 이유

이 패치는 C24를 "점수 확정"으로 만든 것이 아니다.

현재 상태:

```text
C24 URL-backed replay obligation이 다음 runtime source task로 연결됨
```

아직 필요한 다음 단계:

```text
1. 111개 seed/source task를 실제 bounded runtime으로 실행
2. C24 009420/215600에 대해 현재 직접 원문을 fetch
3. approval/trial/binary event primitive별 accepted claim 생성
4. accepted claim이 score contribution으로 연결되는지 확인
5. full thesis row가 의미 있게 닫히는지 확인
```

따라서 Goal4 최종 상태는 여전히 다음이다.

```text
goal4_hard_failures_clear: false
runtime_parity_not_proven_count: 36
```

하지만 이번 패치로 최소한 다음 문제는 막았다.

```text
URL-backed replay 의무가 있는데도 다음 실행 target이 source_proxy_only 후보로 새는 문제
```

## 최종 해석

이번 패치는 C24를 Green이나 pass로 만드는 패치가 아니다.

정확한 의미는 다음이다.

```text
과거 source-backed replay가 있던 symbol을
다음 production runtime의 재검증 source task로 넘기되,
그 replay 기억 자체는 점수 증거로 쓰지 못하게 막은 패치
```

이게 Goal4 방향과 맞는 이유:

```text
연구자료는 운영 점수의 답안지가 아니라
운영 파이프라인이 다시 검증해야 할 source route와 target 후보를 제공한다.
```
