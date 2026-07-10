# E2R Reconstruction Phase 15 — Unified Known-Bad Suite

## 결론

상태는 `UNIFIED_KNOWN_BAD_SUITE_PASS`다.

- goal.md의 known-bad 요구사항: 25개
- 실제 프로브: 26개
- 탐지 성공: 26/26
- 미탐지: 0개
- 실행한 고유 detector unittest: 27개
- 독립 무결성 감사 항목: 21개
- critical count: 0
- run id: `KNOWNBAD-961df87966919c2418a69af5`
- leaf hash: `5b8dcb9699e7678051d60d160b67a05a4c3e6add75b67ee806b8737d7118fc55`
- `test-only=true`
- `production_runtime_ready=false`

이 통과는 “Phase 2~13에서 만든 방어 규칙들을 하나의 시험에서 다시 실행했더니 모두 작동했다”는 뜻이다. 실제 daily provider와 실제 시장 데이터에 고의 장애를 주었다는 뜻은 아니다.

쉬운 예: 소방 훈련에서 비상벨, 방화문, 대피 경로를 모두 시험해 통과한 상태다. 실제 화재가 한 번도 없었다는 뜻도 아니고, 모든 건물이 운영 승인을 받았다는 뜻도 아니다.

## 왜 이름만 모은 목록이 아닌가

각 observation은 다음 네 가지를 가진다.

1. 고정된 `probe_id`
2. 그 실패를 실제로 검사하는 `detector_ids`
3. 이번 실행에서 detector가 성공했다는 `signal_ids`
4. 어떤 잘못된 변이를 막는지 설명하는 `mutation_description`

suite는 detector 이름이 파일에 존재하는 것만으로 통과시키지 않는다. 같은 Python 프로세스 안에서 27개의 unittest를 다시 실행하고, 성공 신호가 생긴 probe만 `detected=true`로 만든다. detector 하나라도 실패하거나 로드되지 않으면 suite 결과 자체를 만들 수 없다.

쉬운 예: “문 잠금 테스트가 있다”는 체크박스만 보는 것이 아니다. 실제로 문을 당겨 보고 잠겨 있다는 결과를 받은 뒤에만 통과로 기록한다.

## 25개 요구사항을 26개 프로브로 검사한 이유

goal.md의 `C05 context copy`는 두 경계로 분리했다.

- `C05_CONTEXT_COPY_CORPUS`: 과거 자료의 `source_primary`, 예상 archetype, 미래 성과 같은 정답표가 blind planner 입력으로 복사되는지 본다.
- `C05_CONTEXT_COPY_CURRENT`: 그 편향 때문에 현재의 서로 다른 후보가 모두 C05로 몰리는지 본다.

두 번째 경계에는 모든 planner 결과를 C05로 만든 직접 변이 fixture를 넣었다. 결과가 `c05_top1_share=1.0`이 되면 bias audit가 `PLANNER_ARCHETYPE_ROUTING_BIAS_NOT_READY`로 차단하는 것을 확인했다.

쉬운 예: 시험지 뒷면에 정답을 인쇄하는 문제와, 그 정답 때문에 학생 전원이 똑같은 오답을 쓰는 문제는 연결되어 있지만 확인 지점은 다르다. 둘을 각각 검사해야 원인과 결과를 모두 잡을 수 있다.

## 전체 probe 표

| # | Probe | 분류 | 원래 방어 Phase | 탐지하는 잘못 |
|---:|---|---|---:|---|
| 1 | `FILE_LEVEL_CASE_COLLAPSE` | CORPUS | 2 | 한 파일의 여러 의미 사건을 한 case로 합침 |
| 2 | `FIRST_SYMBOL_EXTRACTION` | CORPUS | 2 | 모든 row에 파일의 첫 symbol을 복사함 |
| 3 | `COMPANY_DATE_LOSS` | CORPUS | 2 | 존재하던 회사명 또는 서로 다른 trigger date를 잃음 |
| 4 | `ONE_URL_WHOLE_FILE_A2` | SOURCE | 3 | 좋은 URL 하나로 같은 파일의 모든 case를 A2 처리함 |
| 5 | `HANDOFF_PROMPT_AS_CASE` | CORPUS | 2 | coding handoff prompt를 연구 case로 읽음 |
| 6 | `SOURCE_PROXY_PROMOTED` | SOURCE | 9 | source proxy 또는 parser signal에 score credit을 줌 |
| 7 | `C05_CONTEXT_COPY_CORPUS` | PLANNER | 5 | 과거 정답 archetype/source context를 blind 입력에 복사함 |
| 8 | `C05_CONTEXT_COPY_CURRENT` | PLANNER | 5 | 현재 후보를 근거 없이 C05로 몰아줌 |
| 9 | `PRODUCT_PROFILE_AS_ORDER` | SEMANTIC | 9 | 제품 소개나 파트너십을 고객 주문으로 읽음 |
| 10 | `HBM_KEYWORD_POSITIVE` | SEMANTIC | 9 | HBM 단어 또는 mix 언급만으로 allocation을 확정함 |
| 11 | `SECURITY_KEYWORD_ARR` | SEMANTIC | 6 | security 단어만으로 ARR/retention을 확정함 |
| 12 | `COMMODITY_HEADLINE_MARGIN` | SEMANTIC | 6 | 원자재 가격 headline만으로 대상 회사 margin을 확정함 |
| 13 | `SNIPPET_SCORE` | SOURCE | 7 | 원문 fetch가 없는 검색 snippet에 점수를 줌 |
| 14 | `WRONG_SUBJECT` | CLAIM | 9 | 다른 회사의 사실로 대상 회사 gap을 닫음 |
| 15 | `CUSTOMER_CAPA_AS_TARGET_CAPA` | CLAIM | 9 | 고객의 CAPA 증설을 대상 회사의 CAPA로 바꿈 |
| 16 | `INDUSTRY_DEMAND_AS_ISSUER_ORDER` | CLAIM | 9 | 산업 수요를 발행사의 실제 주문으로 바꿈 |
| 17 | `FINANCIAL_CONTRACT_AS_COMMERCIAL` | CLAIM | 9 | 자사주 신탁·담보 계약을 매출 계약으로 바꿈 |
| 18 | `STALE_RISK_PENALTY` | CLAIM | 9 | 유효기간이 끝난 악재를 현재 감점에 사용함 |
| 19 | `REROUTED_GAP_CLOSURE` | CLAIM | 10 | 다른 recipe로 reroute된 claim이 원래 gap도 닫았다고 기록함 |
| 20 | `PROVIDER_FAILURE_RED` | SCORE_STAGE | 13 | provider failure를 Red 또는 논리 훼손으로 확정함 |
| 21 | `REPLAY_AS_REAL_FETCH` | SOURCE | 7 | snapshot/report replay를 live fetch로 계산함 |
| 22 | `EVENT_SCORE_FULL_SCORE` | SCORE_STAGE | 12 | event partial score를 full E2R score로 확정함 |
| 23 | `STAGE_TRACE_MISMATCH` | SCORE_STAGE | 12 | score와 맞지 않는 Stage/trace 위조를 허용함 |
| 24 | `HISTORICAL_OUTCOME_LEAKAGE` | MODE | 11 | 미래 가격·예상 Stage가 과거 planner 입력에 들어감 |
| 25 | `HISTORICAL_REPLAY_CURRENT_WATCHLIST` | MODE | 11 | historical replay claim이 current watchlist를 오염시킴 |
| 26 | `FORCED_CURRENT_ARCHETYPE_MATERIALIZATION` | CURRENT | 11 | 실제 trigger 없이 current archetype quota를 강제함 |

## 중요한 쉬운 예

### 고객의 CAPA와 대상 회사의 CAPA

엔비디아가 데이터센터 CAPA를 늘린다는 문장이 있다고 하자. 이것은 SK하이닉스 자체 생산 CAPA가 늘었다는 증거가 아니다. 관계가 `CUSTOMER`이면 claim은 보존할 수 있지만 `issuer capacity` primitive에는 연결하지 않는다.

### 오래된 악재

`as_of_date=2026-06-30`인데 2020년에만 유효했던 부정 사건이 있다면 현재 risk penalty로 쓰지 않는다. 기록은 `EXPIRED` 또는 `STALE_ONLY`로 남지만 현재 gap을 닫거나 점수를 깎지 않는다.

### provider failure

OpenDART가 잠시 응답하지 않았다고 회사 논리가 나빠진 것은 아니다. 따라서 결과는 `PENDING_PROVIDER`여야 하고 `Red`나 `Reject`가 되면 안 된다. 택배 조회 서버가 멈췄다고 택배 물건이 파손됐다고 결론 내릴 수 없는 것과 같다.

### rerouted claim

C06의 고객 allocation을 찾다가 C15의 원자재 spread에 유용한 문서를 찾을 수 있다. 그 claim은 C15에 보존할 수 있지만 C06의 원래 질문은 여전히 open이다. “유용한 답을 하나 찾음”과 “원래 질문에 답함”을 분리한다.

### event score와 full score

계약 공시 한 건으로 75점 상당 event evidence를 계산할 수 있어도, FCF나 revision처럼 full thesis에 필요한 material primitive가 비어 있으면 `EVENT_EVIDENCE_PARTIAL`이다. 이를 `FULL_E2R_100`으로 바꾸지 않는다.

## 독립 무결성 감사

`audit_known_bad_suite()`는 observation leaf에서 다음 값을 다시 계산한다.

- required/observed/detected probe 수
- 중복·누락·예상 밖 probe
- detector lineage와 detection signal 존재 여부
- category별 probe 수
- 고유 detector 수
- fixture-only 경계
- leaf hash와 run id
- manifest count/hash/category 일치 여부
- `production_runtime_ready` 과장 여부

테스트는 정상 결과만 보는 데서 끝나지 않았다. 다음 변이를 별도로 넣어 감사기가 실패시키는 것도 확인했다.

- required probe 한 개 삭제
- 같은 probe 중복 삽입
- `detected=false`로 변경
- mutation 설명을 바꿔 leaf hash 훼손
- 오래된 run id/manifest hash 유지
- `production_runtime_ready=true`로 과장

이 변이들은 모두 `UNIFIED_KNOWN_BAD_SUITE_FAIL`로 탐지된다.

## 산출물과 코드 위치

- runtime 모델·compiler·audit: `src/e2r/research_brain/runtime/known_bad_suite.py`
- test-only detector registry: `tests/known_bad_suite_fixture.py`
- suite contract test: `tests/test_unified_known_bad_suite.py`
- Phase acceptance test: `tests/test_e2r_reconstruction_phase15_acceptance.py`
- frozen acceptance: `e2r_reconstruction_phase15_acceptance.json`

## 검증 명령

```bash
PYTHONPATH=src:tests python -m unittest \
  tests.test_unified_known_bad_suite \
  tests.test_e2r_reconstruction_phase15_acceptance -v
```

Phase 15 자체는 12개 contract/acceptance test로 검증한다. detector registry 내부에서는 27개 기존·직접 변이 unittest를 같은 실행 안에서 추가로 다시 수행한다.

전체 검증 결과는 다음과 같다.

- Phase 0~15 targeted chain: 264개 통과
- full suite: 5,569개 실행
- full suite 실패: 18개
- Phase 0 기준선의 알려진 실패: 같은 18개
- Phase 15 신규 실패: 0개

18개는 mutable goal4 research-to-runtime operational snapshot과 과거 기대값의 불일치 cluster다. 이를 전체 통과라고 숨기지는 않지만 Phase 15 known-bad suite가 만든 새 회귀로도 세지 않는다.

## 한계와 Phase 16 인계

이번 결과는 deterministic fixture와 regression detector 기반의 test-only acceptance다. 실제 production provider를 고의로 중단하거나 실제 daily watchlist에 오염 데이터를 주입한 결과는 아니므로 `production_runtime_ready=false`를 유지한다.

Phase 16에서는 goal.md에 적힌 공식 full test, compile, historical replay, current operation, Census 명령을 실제 CLI 경로로 실행한다. 각 실행이 commit/config/corpus/memory/recipe/prompt/source hash와 dirty status를 남기는지도 감사해야 한다.
