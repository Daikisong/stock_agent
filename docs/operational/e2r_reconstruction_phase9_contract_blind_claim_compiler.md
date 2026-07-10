# E2R Reconstruction Phase 9 — Contract-Blind Claim Compiler

## 판정

`CONTRACT_BLIND_CLAIM_COMPILER_PASS`

Phase 8의 `AcquiredDocument`를 Evidence OS의 verified anchor, `RawAssertion`, `AdjudicatedClaim`, recipe mapping, score eligibility 후보, `QuestionSourceTask` satisfaction leaf로 연결했다. raw extractor는 target identity·`as_of_date`·source document와 검증 anchor context만 볼 수 있다.

이번 판정은 fixture LLM extractor/mapper로 계약을 검증한 결과다. 실제 LLM extractor와 recipe mapper의 production 완료를 증명하지 않았으므로 `production_runtime_ready=false`다. compiler는 점수나 Stage를 계산하지 않는다.

## raw extraction이 blind여야 하는 이유

나쁜 입력은 다음과 같다.

```text
primitive_gap = customer_preorder_or_allocation
desired_archetype = C06
current_score = 68
desired_stage = 3-Green
```

이 정보를 extractor가 보면 원문이 애매해도 원하는 답을 만들어낼 수 있다. 새 `BlindClaimExtractionInput`에는 다음만 있다.

- 대상 entity ID, 회사명, symbol, alias
- `as_of_date`
- source family, document type, URL, 공개·이용 가능일, content hash
- 원문
- recipe 이름을 제거한 verified anchor context

`primitive_id`, `recipe_id`, archetype, score, Stage, historical outcome은 provider payload에 없다. input과 response SHA-256을 남겨 같은 호출을 재현할 수 있다.

## anchor context

Phase 8에서 선택한 핵심 section 한 줄만 보면 subject나 날짜가 바로 앞 문장에 있을 수 있다.

```text
테스트기업은 2025-03-15 고객 배정 계약을 공개했다.
customer allocation and supply agreement terms were disclosed.
```

두 번째 줄만 anchor로 쓰고 “테스트기업의 계약”이라고 판단하면 subject를 추정한 셈이다. Phase 9 adapter는 선택 section 주변의 원문 문맥을 함께 hash한 anchor로 만든다. 같은 문맥을 가리키는 section이 여러 개면 context hash로 중복 제거해 LLM에 한 번만 보낸다.

raw assertion은 exact quote가 이 anchor에 실제로 존재해야 한다. subject entity 이름 또는 ticker도 quote에 있어야 하며 event/effective ISO date를 제안했다면 그 날짜 역시 quote로 확인한다.

문서당 raw assertion은 최대 20개로 제한한다. provider가 다른 입력의 hash를 반환하면 결과 전체를 거절하고, mapper가 candidate recipe 수보다 많은 mapping을 반환해도 provider 오류로 남긴다.

## canonical 순서

```text
Anchor
→ Entity / subject
→ Target directness
→ Temporal / effective period
→ Lifecycle
→ Contradiction / supersession
→ EvidenceRecipe / primitive mapping
→ Score eligibility
→ QuestionSourceTask satisfaction
```

mapping provider는 raw extraction과 entity/time 판정이 끝난 claim을 candidate recipe catalog와 비교한다. 원래 task ID나 primitive gap은 mapping input에도 주지 않는다. provider가 제안한 `recipe_id`, archetype, primitive, accepted predicate, required fields, polarity를 deterministic code가 검증한다. 유효한 mapping을 못 만들면 claim은 ledger에 남을 수 있지만 score eligible은 아니다.

쉬운 예: 계약 질문으로 가져온 문서에서 명확한 FCF claim만 발견되면 FCF recipe mapping은 ledger에 보존한다. 하지만 status는 `REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN`이고 원래 질문은 닫히지 않는다.

## claim acceptance와 task satisfaction 분리

| 상태 | 의미 | 원래 gap 닫힘 |
|---|---|---:|
| `DIRECT_TASK_SATISFIED` | 새 current claim이 정확한 task recipe를 충족 | 예 |
| `REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN` | 유효한 다른 claim을 찾음 | 아니요 |
| `BASELINE_CLAIM_REUSED` | 이미 source-backed current인 정확한 baseline claim 재사용 | 예 |
| `LIFECYCLE_REFRESH_ONLY` | 기존 claim의 상태만 갱신 | 아니요 |
| `COUNTER_CLAIM_FOUND` | 원래 질문의 반증 claim 발견 | 아니요 |
| `NO_RELEVANT_CLAIM` | 문서는 읽었지만 관련 accepted mapping 없음 | 아니요 |
| `WRONG_SUBJECT` | 다른 회사·고객·산업 claim뿐 | 아니요 |
| `STALE_ONLY` | old/expired/superseded/unknown claim뿐 | 아니요 |
| `PROVIDER_FAILED` | source/extractor/mapper provider 실패 | 아니요 |
| `SOURCE_EXHAUSTED` | bounded source route가 증거 없이 종료 | 아니요 |

counter claim과 direct support가 동시에 있으면 counter를 먼저 드러내 gap을 닫지 않는다. open contradiction 역시 score eligibility를 막는다. 알려진 baseline claim을 새 current claim이 supersede하는 관계는 mapping 전에 ledger에 기록한다. 존재하지 않는 claim ID를 supersede/contradict한다고 쓰면 거절한다.

## score eligibility guard

다음 조건을 모두 통과한 event만 `score_eligible=true`가 될 수 있다.

- source document ID, anchor ID, published/available date, subject와 target 존재
- exact quote와 anchor hash 검증
- subject가 entity registry와 quote에서 확인되고 target direct
- semantic status pass, temporal status current
- source proxy가 아님
- known lifecycle/contradiction 관계
- valid EvidenceRecipe와 accepted predicate mapping
- required predicate fields 완전, 허용 polarity, SUPPORT 또는 COUNTER direction
- LLM/fixture-LLM provider이며 parser/rule fallback이 아님

`score_eligible`은 deterministic scorer가 사용할 수 있는 claim 후보라는 뜻이지 compiler가 점수를 줬다는 뜻이 아니다. `production_score_eligible`은 production mode, real LLM extractor, real LLM mapper, provider error 없음까지 추가로 요구한다.

baseline reuse도 현재 task의 `as_of_date`로 published/available date를 다시 검사한다. 예를 들어 2025-04-01에 나온 claim은 2025-03-31 replay에서 baseline이라는 이유로 재사용할 수 없다.

## old risk와 wrong subject

예를 들어 2020년에 끝난 취소 위험을 2025년 현재 penalty로 쓰면 안 된다. old/expired/unknown risk claim은 ledger에는 남지만 score eligible이 아니며 task status는 `STALE_ONLY`다.

고객 CAPA 문장을 대상 회사 CAPA로 읽는 경우도 마찬가지다. subject entity와 relation을 먼저 판정하므로 wrong/indirect subject는 mapping이 제안돼도 점수로 갈 수 없다.

## legacy migration

기존 V4 bundle의 raw assertions, adjudicated claims, mappings는 side-by-side diagnostic leaf로 읽을 수 있다. 하지만 adapter 결과는 항상 `LEGACY_CLAIM_DIAGNOSTIC_ONLY`이며 canonical score credit과 task closure는 0이다.

기존 `LLMContractBlindRawAssertionExtractor`의 기본 provider가 rule fallback이면 새 production adapter가 이를 real LLM으로 가장하지 않는다. `LEGACY_RULE_FALLBACK`으로 표시해 provider pending으로 끝낸다. parser mention signal도 같은 방식으로 차단한다. deterministic primitive fallback은 만들지 않는다.

## 감사 결과

| 항목 | 결과 |
|---|---:|
| compilation result | 6 |
| raw assertion | 4 |
| adjudicated claim | 4 |
| claim ledger event | 4 |
| score-eligible event | 2 |
| direct original-gap closure | 1 |
| rerouted event | 1 |
| accepted claim missing provenance | 0 |
| source proxy current claim | 0 |
| wrong-subject score | 0 |
| old/unknown risk penalty | 0 |
| rerouted original-gap closure | 0 |
| rule fallback score | 0 |
| mappingless score | 0 |
| parser mention direct score | 0 |

고정 audit hash는 `dd1f97a90b17c6d35453063d63ecd0a16aa233de7706a9471a86df74f93f8c78`다.

## 검증 결과

- Phase 0~9 targeted chain: 173개 통과
- Phase 8~9 contract/acceptance: 47개 통과
- full suite: 5,478개 실행, 기존 기준선과 동일한 18개 실패
- Phase 9 신규 실패: 0개

18개는 Phase 0부터 기록한 mutable goal4 research-to-runtime operational snapshot 불일치다. 이를 통과로 숨기지 않으며 Phase 9 회귀로도 세지 않는다.

## 주요 파일

- `runtime/claim_compiler.py`: blind input, provider adapter, adjudication, recipe mapping, canonical claim ledger, audit
- `runtime/task_satisfaction.py`: 10개 satisfaction 상태와 original-gap closure
- `tests/test_contract_blind_claim_compiler.py`: provenance, reroute, baseline, lifecycle, contradiction, known-bad guard
- `e2r_reconstruction_phase9_acceptance.json`: phase-scoped 고정 판정

## 다음 경계

Phase 9는 “왜 task가 해결됐거나 실패했는지”를 정확한 leaf로 남긴다. Phase 10은 `NO_RELEVANT_CLAIM`, `WRONG_SUBJECT`, `STALE_ONLY`, reroute, mapping rejection, contradiction, provider/source failure를 서로 다른 next action으로 바꾸며 동일 query 재실행을 금지한다.
