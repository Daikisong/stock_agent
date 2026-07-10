# E2R Reconstruction Phase 12 — Deterministic Score / Stage Integrity

## 판정

`DETERMINISTIC_SCORE_STAGE_INTEGRITY_PASS`

claim, 점수 기여분, score, canonical Stage, 상태, hard break, 누락 gap, StageCourt trace를 하나의 `AtomicStageDecision`으로 묶었다. 각 필드는 단순히 같이 저장되는 것이 아니라 같은 원천 claim과 config에서 다시 계산해도 일치해야 한다.

이번 검증은 deterministic fixture와 Phase 9 source-acquisition → claim-compiler 연결 경로를 사용했다. 실제 daily universe 실행 경로에 아직 연결한 것은 아니므로 `production_runtime_ready=false`다.

## 점수 세 종류

점수 이름은 다음 세 개만 허용한다.

| 점수 종류 | 의미 | 최종 Stage 확정 |
|---|---|---:|
| `EVENT_EVIDENCE_PARTIAL` | 한 이벤트가 제공한 일부 근거의 점수 | 불가 |
| `FULL_E2R_100` | material primitive와 current claim을 모두 검증한 100점 체계 | 가능 |
| `NO_SCORE` | source/provider/material 조건이 덜 채워진 상태 | 불가 |

쉬운 예를 들면 계약, FCF, revision, CAPA를 각각 25점으로 본다고 하자.

```text
네 항목 모두 current source-backed claim으로 확인
→ FULL_E2R_100 = 100점
→ Stage 3-Green

계약 품질 근거가 없음
→ 계산 중간값(raw reference)은 75점
→ 표시 점수는 NO_SCORE
→ Stage 0 / PENDING
```

두 번째 경우를 `75점 Stage 2`로 확정하면 “자료가 없어서 생긴 낮은 점수”와 “자료를 확인한 뒤 나온 낮은 점수”가 섞인다. 그래서 raw 75는 진단용으로만 남기고 최종 점수는 비워 둔다.

## Full score 계약

`FULL_E2R_100`이 되려면 다음 조건을 동시에 만족해야 한다.

- scope가 `FULL_THESIS`
- 모든 material primitive에 assessment와 점수 기여가 있음
- 기여 claim이 target-direct, current, OPEN, source-backed임
- claim-to-primitive mapping이 accepted 상태이고 mapping id가 보존됨
- contradiction이 해결됨
- `score_valid=true`, `score_finalization_allowed=true`
- StageCourt trace가 decision과 정확히 같음

점수 기여분은 `claim_id → mapping_id → primitive_id → component_key → points`의 계보를 가진다. 예를 들어 계약 claim 25점이 있다면 어느 문서 anchor에서 왔고 어떤 mapping으로 `contract_quality`에 연결됐는지 역추적할 수 있어야 한다.

## Stage와 trace의 동시 위조 방지

decision과 trace가 서로 같은지만 검사하면 둘을 같이 틀리게 바꿀 수 있다.

```text
실제 규칙 계산: 100점 → 3-Green
위조: decision.stage=2, trace.stage=2
```

두 값은 서로 같지만 규칙과는 다르다. Phase 12는 score rules, primitive assessments, threshold config, hard-break 상태에서 기대 Stage와 status를 다시 계산한다. 위 예는 `stage_score_trace_mismatch`로 잡힌다.

또한 다음 SHA-256 계보를 각각 재계산한다.

```text
claim state hash
→ config fingerprint
→ input fingerprint
→ score fingerprint
→ decision id / StageCourt trace id
```

한 claim의 본문 hash나 25점 규칙이 바뀌면 뒤쪽 fingerprint도 달라진다. decision과 trace만 손으로 맞춰도 원천 계보와 맞지 않으면 통과하지 못한다.

## Score delta 설명

점수가 바뀌려면 claim state 또는 scoring config가 바뀌어야 한다.

검증 fixture에서는 revision claim의 내용 버전과 evidence strength가 바뀌어 100점에서 95점이 됐다.

```text
claim_state_changed=true
contribution_changed=true
score_delta=-5
unexplained_score_delta=0
```

반대로 claim/config는 그대로인데 표시 점수만 100에서 99로 바꾸면 `ATOMIC_SCORE_DELTA_UNEXPLAINED`다. contribution 숫자만 손으로 바꾸는 것도 원천 claim/config 변경이 아니므로 설명으로 인정하지 않는다.

## Hard break 계약

hard break는 다음 조건을 모두 만족해야 한다.

- 대상 기업을 직접 가리킴 (`target_direct`)
- 현재 유효하고 아직 닫히지 않음 (`current OPEN`)
- source-backed임
- 논리를 훼손할 만큼 material함
- 아직 해결되지 않음 (`unresolved`)
- historical replay claim이 아님

예를 들어 2년 전 다른 회사의 계약 취소 뉴스는 위험해 보이더라도 현재 대상 기업의 hard break로 쓸 수 없다. 검증에서는 current direct 계약 취소 claim은 기존 thesis가 있을 때 `4C / RISK_REVIEW`가 됐고, wrong-subject claim은 거절됐다.

wrong subject, closed claim, source 미확인, non-material, historical replay, future-dated, resolved signal, support polarity의 8개 invalid probe를 각각 넣었고 모두 hard break에서 제외됐다. 반대로 조건을 모두 만족한 signal을 decision에서 몰래 빼는 경우도 audit가 탐지했다.

## 고정 검증 결과

| 항목 | 결과 |
|---|---:|
| full decision | 100점, `3-Green`, `FINAL` |
| event partial | 75점, `Stage 2`, finalization 불가 |
| material-gap decision | `NO_SCORE`, raw 75, `Stage 0 / PENDING` |
| claimless score | 0 |
| material gap full score | 0 |
| event score as full | 0 |
| stage/score/trace mismatch | 0 |
| pending final low score | 0 |
| invalid hard break | 0 |
| unexplained score delta | 0 |
| fingerprint mismatch concealed | 0 |

정상 3개 결정에 대한 audit hash는 `be5c0d66b45bee42d0e37285f5a96161672a4daf7c0e867c7d658090c3bf9dbe`다. 설명 가능한 -5점 delta hash는 `66cd8f060745f9c87089788f87657e545d23c8dcb384d9d1a3eb1f845c911803`이다.

## Phase 9 원천 연결

테스트는 임의의 점수 payload만 직접 넣지 않았다. Phase 9의 acquired document를 claim compiler에 넣고, 생성된 `ClaimLedgerEvent`를 atomic claim으로 변환했다.

```text
acquired document content_hash
→ ClaimLedgerEvent source anchor / mapping id
→ AtomicScoreClaim
→ AtomicScoreContribution
→ AtomicStageDecision
```

fixture claim은 `test_mode=true`일 때만 점수 재료가 된다. 같은 fixture를 production 경계로 변환하면 `score_eligible=false`다. 테스트 통과를 실제 운영 source라고 오인하지 않기 위한 장치다.

## 주요 파일

- `runtime/atomic_score_stage.py`: atomic score·Stage·trace 결정과 독립 audit
- `runtime/__init__.py`: Phase 12 public API
- `tests/test_atomic_score_stage_integrity.py`: score type, material gap, hard break, delta, fingerprint known-bad 검사
- `e2r_reconstruction_phase12_acceptance.json`: 고정 Phase 12 acceptance

## 검증 경계와 다음 단계

Phase 12는 원천 claim에서 점수와 Stage가 원자적으로 만들어지는 계약을 완성했다. 하지만 아직 전 종목 daily census가 이 객체를 실제로 사용한다는 뜻은 아니다. Phase 13에서 Universe → baseline → SourceTimeline → LastEffectiveThesis → DepthPolicy → selected deep → CensusStageStatus 흐름에 연결하고, 모든 종목에 LLM이나 일반 웹 검색을 돌리지 않는 bounded daily operation을 검증해야 한다.
