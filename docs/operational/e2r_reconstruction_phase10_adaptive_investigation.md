# E2R Reconstruction Phase 10 — Adaptive Investigation Controller

## 판정

`ADAPTIVE_EVIDENCE_CLOSURE_PASS`

Phase 9의 acquisition·claim·task satisfaction leaf를 실패 이유로 정규화하고, LLM이 새 literal query와 source/document/target/time 제약을 제안하는 bounded runtime controller를 만들었다. material gap이 남아 있는 모든 action/pending 결과는 `score_valid=false`이고 score finalization도 허용하지 않는다.

이번 검증은 fixture LLM investigation provider를 사용했다. 새 query를 실제 live provider로 실행해 claim closure까지 완료한 것이 아니므로 `production_runtime_ready=false`다.

## 왜 같은 retry로는 안 되는가

다음 두 실패는 행동이 달라야 한다.

- 문서 없음: 다른 official/source route와 document type을 찾아야 함
- wrong subject: query의 대상 회사와 directness constraint를 강화해야 함

둘 다 단순히 같은 query를 한 번 더 실행하면 실패 원인이 그대로 남는다. 새 controller는 실패 reason 없이 retry action을 만들 수 없고, 이전 query와 정규화 결과가 같으면 거절한다.

## 실패 taxonomy

| 실패 | 다음 action이 반드시 바꾸는 축 | 쉬운 예 |
|---|---|---|
| `NO_DOCUMENT_FOUND` | QUERY, SOURCE, DOCUMENT | DART 결과가 없으면 다른 official route와 문서 종류를 LLM이 제안 |
| `WRONG_SUBJECT` | QUERY, TARGET, DOCUMENT | 고객 CAPA가 아니라 대상 회사 CAPA가 명시된 문서 요구 |
| `STALE_ONLY` | QUERY, TIME, DOCUMENT | 2020년 risk가 아니라 기준일 현재 lifecycle 문서 요구 |
| `GENERIC_CONTEXT_ONLY` | QUERY, DOCUMENT, TARGET | 산업 설명이 아닌 target-direct claim section 요구 |
| `REROUTED_PRIMITIVE` | QUERY, SOURCE, DOCUMENT | FCF claim은 보존하고 계약 질문은 다른 source로 계속 조사 |
| `MAPPING_REJECTED` | QUERY, DOCUMENT | accepted predicate의 빠진 value/unit/time field가 있는 문서 요구 |
| `CONTRADICTION_OPEN` | QUERY, SOURCE, TARGET | 상반된 claim을 resolve할 최신 target-direct official source 요구 |
| `PROVIDER_FAILED` | QUERY, SOURCE | 실패한 provider와 다른 bounded provider 경로 요구 |
| `SOURCE_EXHAUSTED` | QUERY, SOURCE, DOCUMENT | 이미 소진한 source/document 조합을 반복하지 않음 |

이 표는 query 문구를 코드에 하드코딩한 것이 아니다. deterministic code는 어떤 제약 축이 바뀌어야 하는지만 검사한다. 실제 query, 선호·제외 source, 문서 종류·section, target constraint는 LLM 출력이다.

## LLM query validation

새 query는 다음을 통과해야 한다.

- 대상 회사명·symbol·ID·alias 중 하나 포함
- 명시적인 reporting year 포함
- `as_of_date` 이후 date/year/quarter 없음
- `latest`, `오늘`, `최신` 같은 상대시점 없음
- original/rejected/previous-round query와 중복 없음
- primitive/archetype/score/Stage/outcome 내부 라벨 복사 없음
- 남은 `max_queries` 이내

동일 query가 나오면 코드가 다른 문구를 대신 만들지 않는다. rejected query와 validator error를 다음 LLM attempt에 돌려주며 최대 3회만 시도한다. `SOURCE` 변경이 필요한 실패에서는 실제 실패 source를 제외하고 그 밖의 source를 선호해야 하며, 한 source를 prefer/exclude에 동시에 넣을 수 없다. document time constraint도 미래 날짜와 상대시점을 쓸 수 없고, `STALE_ONLY`는 명시적인 reporting period를 요구한다. 세 번 모두 실패하면 `INVESTIGATION_VALIDATION_RETRY_EXHAUSTED` pending이다.

## rerouted feedback

`REROUTED_PRIMITIVE`는 발견한 claim을 폐기하지 않는다. 다음 leaf를 LLM에 돌려준다.

- original recipe/primitive
- accepted rerouted claim ID
- 실제 mapped recipe/primitive
- 같은 결과만 낸 source family
- original gap은 여전히 열려 있다는 safe instruction

새 action은 같은 source를 exclude해야 한다. 예를 들어 계약 질문에서 FCF claim만 찾았다면 FCF claim은 ledger에 남지만, 다음 action은 다른 source/document에서 계약 취소 조건을 찾는다.

## pending과 round limit

다음은 낮은 점수 확정이 아니라 pending이다.

- provider 없음 또는 오류
- fixture provider를 test mode 밖에서 사용
- query validation 3회 실패
- SourceTask query/candidate/fetch budget 소진
- `round_limit` 도달
- LLM이 실행 가능한 새 query를 안전하게 만들 수 없어 명시적으로 abstain

rollback이 필요하면 `round_limit=1`로 adaptive loop를 안전하게 한 번으로 제한할 수 있다. 어느 경우에도 unresolved material gap은 score finalization으로 넘어가지 않는다. Phase 10의 `RESOLVED`도 “조사 gap이 닫힘”만 뜻하며 score를 직접 만들거나 유효화할 수 없다.

누적 사용량은 직전 acquisition 사용량보다 작게 신고할 수 없다. round·failure·action의 task/round/reason leaf identity도 서로 같아야 한다. 또한 provider 예외와 abstain 응답 모두 prompt/response hash를 가진 provider trace를 남긴다. 실제 운영 provider는 기존 `.env` 로딩과 Codex structured transport를 재사용하는 canonical builder로 연결된다.

## runtime investigation과 systemic code repair 분리

runtime investigation은 한 task의 source/query를 바꾸는 일이다. coding-agent systemic repair는 서로 다른 두 개 이상의 task에서 같은 failure signature가 반복될 때만 cluster 후보가 된다.

```text
한 종목 provider timeout
→ runtime pending/action

여러 종목에서 같은 connector identity mismatch 반복
→ SystemicFailureCluster
→ commit + changed files + verification tests를 가진 CodeRepairHistoryEntry
```

runtime round에는 `coding_agent_repair=false`, `runtime_self_repair_label_allowed=false`가 강제된다. 단순 `until_pass` rerun을 self-repair라고 부를 수 없다. production code-repair history는 실제 git commit SHA와 changed files, verification tests가 없으면 생성할 수 없다.

Phase 10 acceptance의 systemic cluster 1개와 code history 1개는 schema 검증용 test fixture다. 실제 production code repair 실적이나 production readiness로 세지 않는다.

## 감사 결과

### Adaptive runtime

| 항목 | 결과 |
|---|---:|
| failure/result | 10 |
| planned action | 9 |
| resolved/no-retry | 1 |
| rerouted feedback action | 1 |
| failure reason 없는 retry | 0 |
| 동일 query retry | 0 |
| failure-specific constraint 누락 | 0 |
| action trace 누락 | 0 |
| unresolved material score valid | 0 |
| runtime retry self-repair 오표기 | 0 |

고정 adaptive audit hash는 `53f997ca1e88e4836e612683854ece9b9c14386b7495c8fce48e22033850fd5a`다.

### Systemic separation

| 항목 | 결과 |
|---|---:|
| systemic fixture cluster | 1 |
| fixture code repair history | 1 |
| single-task cluster | 0 |
| runtime retry code-repair 오표기 | 0 |
| history leaf 누락 | 0 |

고정 systemic audit hash는 `3588710cea478e0eebfa43548b60528e57fb252eeb25050441e096ab5e6bf03d`다.

## 검증 결과

- Phase 0~10 targeted chain: 190개 통과
- Phase 8~10 contract/acceptance: 64개 통과
- full suite: 5,495개 실행, 기존 기준선과 동일한 18개 실패
- Phase 10 신규 실패: 0개

18개는 Phase 0부터 기록한 mutable goal4 research-to-runtime operational snapshot 불일치다. 이를 통과로 숨기지 않으며 Phase 10 회귀로도 세지 않는다.

## 주요 파일

- `runtime/adaptive_investigation_controller.py`: failure normalization, LLM action schema, query validator, round/pending controller, audit
- `runtime/systemic_failure_cluster.py`: multi-task cluster, code repair history, runtime/systemic separation audit
- `tests/test_adaptive_investigation_controller.py`: 9개 failure transition, duplicate/budget/round/provider pending, systemic ledger
- `e2r_reconstruction_phase10_acceptance.json`: phase-scoped 고정 판정

## 다음 경계

Phase 10은 한 task 안에서 evidence closure를 어떻게 계속할지 완성했다. Phase 11은 historical replay와 current operation을 별도 run schema·output root·CLI로 분리해 replay claim이나 전 아키타입 quota가 현재 watchlist로 섞이지 않게 한다.
