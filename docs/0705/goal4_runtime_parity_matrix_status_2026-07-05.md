# Goal4 Runtime Parity Matrix Status - 2026-07-05

## 결론

이번 패치는 goal4를 완료시킨 것이 아니라, **전 아키타입 runtime 상태판을 더 정확하게 만든 작업**이다.

쉬운 예로, 예전 표는 "환자 36명이 접수됐는지" 중심이었다. 새 표는 환자마다:

- 연구자료가 얼마나 있는지
- URL-backed 판례가 있는지
- source task가 실제로 실행됐는지
- accepted claim이 생겼는지
- full thesis row까지 닫혔는지
- 막힌 이유가 무엇인지

를 한 줄로 붙인다.

추가 패치로 source task 실행 로그의 실패 축도 붙였다. 이제 `accepted claim 0`에서 멈추지 않고, 다음처럼 왜 실패했는지까지 볼 수 있다.

```text
NO_ACCEPTED_CLAIM
NO_SCORE_ELIGIBLE_REAL_CLAIM
PRIMITIVE_GAP_UNSATISFIED
PRIMITIVE_MAPPING_REJECTED
PROVIDER_ERROR_RECORDED
```

## 새 산출물

- `docs/operational/all_archetype_runtime_parity_matrix.json`
- `docs/operational/all_archetype_runtime_parity_summary.md`
- 기존 `docs/operational/all_archetype_runtime_status_matrix*.json`에도 같은 goal4 감사 필드를 포함한다.

## 현재 전 아키타입 상태

`all_archetype_runtime_parity_matrix.json` 기준:

- registered contract: `36`
- C01~C32: `32`
- R13 cross-archetype: `4`
- memory card ready: `36`
- source route ready: `36`
- meaningful_runtime_parity_ready: `false`

runtime status 분포:

```text
SCORE_PATH_CLOSED_WITH_THESIS_GAPS: 4
SOURCE_REPAIR_REQUIRED: 28
TARGET_MATERIALIZATION_REQUIRED: 3
PLANNING_ONLY: 1
```

primary blocker 분포:

```text
ACCEPTED_CLAIM_NOT_CREATED: 27
REQUIRED_POSITIVE_MISSING: 5
CANDIDATE_SELECTOR_DID_NOT_ATTEMPT: 3
SOURCE_TASK_NOT_CREATED: 1
```

## 중요한 해석

`SCORE_PATH_CLOSED_WITH_THESIS_GAPS`는 "좋은 full thesis 통과"가 아니다.

쉬운 예:

```text
시험 답안지는 채점됐지만
필수 서술형 문제가 비어 있는 상태
```

현재 해당 상태인 대표 행:

- C01: accepted claim과 full row는 있으나 required-positive/Green gap 남음
- C03: accepted claim과 full row는 있으나 required-positive/Green gap 남음
- C05: accepted claim과 full row는 있으나 required-positive/Green gap 남음
- C06: accepted claim과 full row는 있으나 required-positive/Green gap 남음

따라서 C06도 "운영 full thesis가 의미 있게 Green/Yellow를 낸 상태"가 아니라, **점수 경로가 닫혔지만 필수 증거가 부족한 상태**다.

## 주요 canary 상태

```text
C05: SCORE_PATH_CLOSED_WITH_THESIS_GAPS / REQUIRED_POSITIVE_MISSING
C06: SCORE_PATH_CLOSED_WITH_THESIS_GAPS / REQUIRED_POSITIVE_MISSING
C08: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
C15: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
C17: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
C24: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
C28: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
```

예를 들어 C08은 연구 case `300`, URL-backed case `61`, source task `28`까지 있다. 그런데 accepted claim은 `0`이다. 즉 연구자료가 부족한 문제가 아니라, **운영 source task가 현재 원문에서 score-eligible accepted claim을 만들지 못한 문제**다.

source task execution log 기준 C08의 실제 실패 축:

```text
execution_log_count: 14
NO_ACCEPTED_CLAIM: 14
NO_SCORE_ELIGIBLE_REAL_CLAIM: 11
PRIMITIVE_GAP_UNSATISFIED: 11
PRIMITIVE_MAPPING_REJECTED: 7
MAPPING_NOT_ACCEPTED: 7
PROVIDER_ERROR_RECORDED: 5
```

C24/C28도 같은 패턴이다.

```text
C24:
  execution_log_count: 21
  NO_ACCEPTED_CLAIM: 21
  NO_SCORE_ELIGIBLE_REAL_CLAIM: 15
  PRIMITIVE_GAP_UNSATISFIED: 15
  PROVIDER_ERROR_RECORDED: 9

C28:
  execution_log_count: 21
  NO_ACCEPTED_CLAIM: 21
  NO_SCORE_ELIGIBLE_REAL_CLAIM: 15
  PRIMITIVE_GAP_UNSATISFIED: 15
  PROVIDER_ERROR_RECORDED: 9
```

쉬운 예:

```text
source task 실행
→ 병원 검사는 예약하고 일부 검체도 채취함
→ 하지만 검사 결과지가 해당 질병 항목에 맞지 않음
→ accepted claim 0
```

따라서 다음 작업은 "source task를 더 많이 실행"이 아니라, `no_score_eligible_real_claim`과 `primitive_mapping_rejected`가 왜 생기는지 원문/primitive/source-class 단위로 좁히는 것이다.

## 자기참조 버그 수정

새로 만든 parity matrix/summary가 연구 reverse scanner에 다시 흡수되는 문제가 발견됐다.

잘못된 흐름:

```text
all_archetype_runtime_parity_matrix.json 생성
→ docs/operational/*.json scanner가 이를 연구자료로 읽음
→ research_reverse_case_inventory record_count가 11425에서 11466으로 부풀어 오름
```

패치:

```text
GENERATED_GOAL4_PREFIXES에 all_archetype_runtime_parity_ 추가
```

검증:

```text
research_case_count: 11425
documented_corpus_size: 2659
parity matrix가 research inventory source_file로 재흡수되지 않음
```

## 남은 실제 Goal4 blocker

아직 goal4 complete가 아닌 이유:

1. C08/C15/C17/C24/C28 등 대부분 아키타입은 source task는 실행됐지만 accepted claim이 0이다.
2. C01/C03/C05/C06/C31은 accepted claim이 있거나 score path가 일부 닫혔지만 required-positive primitive가 남아 있다.
3. R13 일부는 실제 target symbol materialization 전 단계에 머물러 있다.
4. full thesis row가 있는 4개도 Green/required-positive gap rate가 `1.0`이다.

## 테스트

통과:

```bash
PYTHONPATH=src python -m unittest tests.test_research_reverse_case_extractor tests.test_all_archetype_runtime_status_matrix tests.test_all_archetype_runtime_parity_matrix tests.test_research_to_runtime_parity_goal4 -v
```

이후 전체 테스트도 통과했다.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

전체 결과:

```text
Ran 5256 tests in 427.232s
OK
```

## 다음 작업 방향

다음 패치는 "source task 실패 축"에서 한 단계 더 들어가 **rejected claim / not eligible reason / primitive gap별 원문 사례를 붙이는 것**이어야 한다.

우선순위:

1. `PRIMITIVE_MAPPING_REJECTED` 행에서 어떤 rejected claim이 어떤 primitive에 실패했는지 sample을 붙인다.
2. `PROVIDER_ERROR_RECORDED` 행에서 source family별로 external blocker인지, route 설계 문제인지 분리한다.
3. C08/C15/C17/C24/C28 canary부터 accepted claim 1개 이상을 만들 수 있는 운영 source route를 닫는다.
4. 그 다음 required-positive gap이 남은 C01/C03/C05/C06/C31의 missing primitive별 follow-up task를 actual source/claim으로 연결한다.

한 줄로 말하면:

> 지금은 전 아키타입에 "어느 단계와 어떤 실패 축에서 막혔는지"가 붙었다. 다음은 실패 축별 rejected claim 원문을 붙이고, canary부터 accepted claim을 실제로 만들어야 한다.
