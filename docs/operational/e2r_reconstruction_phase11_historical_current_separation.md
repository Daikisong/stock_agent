# E2R Reconstruction Phase 11 — Historical Replay / Current Operation Separation

## 판정

`HISTORICAL_CURRENT_MODE_SEPARATION_PASS`

Historical replay와 current operation을 서로 다른 run identity, output namespace, leaf schema로 분리했다. Historical leaf는 current watchlist에 들어갈 수 없고, current 입력에는 replay claim·expected label·future outcome이 들어갈 수 없다.

이번 historical 평가는 blind benchmark와 controlled snapshot을, current 평가는 bounded fixture를 사용했다. 실제 현재 KRX universe와 live provider를 실행한 결과가 아니므로 `production_runtime_ready=false`다.

## 왜 물리적으로 나누는가

과거 검증에는 정답이 필요하지만, 정답은 evaluator만 알아야 한다.

```text
planner가 보는 것
→ "고객이 다음 연도 HBM 물량을 예약했고 취소 조건이 명시됨"

evaluator만 보는 것
→ expected archetype=C06, expected primitive=customer allocation
```

두 정보를 같은 payload에 넣으면 모델이 연구하는 대신 답안지를 읽게 된다. 기존 `BR-C06-01` 같은 benchmark ID도 archetype 힌트이므로 planner request에서는 evidence/as-of hash인 `BLIND-...`로 바꿨다. planner input hash와 evaluator expected hash를 별도로 저장하고, 디스크에서도 `historical_replay_planner_inputs.jsonl`과 `historical_replay_evaluator_leaves.jsonl`을 나눈다.

Current operation은 반대다. 36개 archetype을 모두 채우는 것이 목적이 아니다.

```text
오늘 실제 trigger가 있는 후보: 5개
현재 근거로 추론된 archetype: 2개
나머지 34개 archetype row: 없어도 정상
```

예를 들어 오늘 임상 이벤트가 없으면 C24 row를 억지로 만들지 않는다. 과거 parity의 36/36 coverage와 현재 watchlist의 선택성은 서로 다른 성공 조건이다.

## Historical replay 계약

- 전체 canonical registry 36개에 archetype parity row가 있어야 함
- 모든 benchmark는 하나의 frozen `as_of_date`를 사용
- `NOT_ATTEMPTED`는 정확한 사유 없이는 허용하지 않음
- source는 URL-backed frozen replay이거나 exact blocker여야 함
- source proxy는 점수 0
- expected archetype/stage/outcome, MFE/MAE는 planner 입력에서 금지
- replay leaf는 `current_watchlist_eligible=false`

쉬운 예: `as_of_date=2023-07-27` replay라면 2023-07-28 공시는 retrieval·source·claim 판단에 들어갈 수 없다. 나중에 주가가 올랐다는 outcome도 evaluator에서 정확도 계산에만 쓰고 prompt에는 넣지 않는다.

## Historical 결과

| 항목 | 결과 |
|---|---:|
| registry coverage | 36/36, 100% |
| archetype parity rows | 36 |
| blind benchmark leaves | 61 |
| positive/guard/wrong-subject/old-risk/source-missing probes | 5/5 통과 |
| top-1 | 95% |
| top-3 | 100% |
| mapping precision | 100% |
| positive recall | 100% |
| guard accuracy | 100% |
| future leakage | 0 |
| source proxy score | 0 |
| current watchlist contamination | 0 |

Controlled URL-backed source가 있는 archetype은 1개다. 나머지 35개는 원문을 찾았다고 꾸미지 않고 `NO_URL_BACKED_FROZEN_SOURCE_FOR_ARCHETYPE` 같은 exact blocker로 남겼다. Goal의 “URL-backed replay or blocker”를 그대로 적용한 것이다.

Historical leaf hash는 `236ae82327e773a2062a18ab0a409a0dc2688a476818f60154d404ddc08b899d`다.

Request ID anonymization 뒤 전체 10,920-case corpus를 다시 compile했다. semantic node/edge는 25,532/44,221, top-3·recipe·positive/guard는 모두 100%, critical은 0이었다. Full-registry retrieval hash도 기존과 같은 `96d947b64fd66a708facc2cd69a484a8f02159d85f603dbfde688aabd784d3da`로 유지됐다.

## Current operation 계약

Current run은 다음 순서만 허용한다.

```text
full-universe baseline
→ current dated trigger
→ real trigger candidate
→ bounded selected deep
→ terminal outcome
```

Terminal outcome은 다음 다섯 가지다.

- `FULL_THESIS`
- `DISPROVED`
- `SOURCE_PENDING`
- `PROVIDER_PENDING`
- `BUDGET_PENDING`

선택된 deep candidate가 아무 결과 없이 사라질 수 없다. provider가 실패한 경우에도 낮은 점수를 확정하지 않고 `PROVIDER_PENDING`으로 끝낸다.

Trigger와 score evidence도 분리한다. 예를 들어 “주가 거래량 급증” 뉴스는 조사를 시작할 이유는 되지만, 그 자체로 계약 질이나 FCF 점수를 만들 수 없다. score claim은 current, OPEN, source-backed 조건을 만족해야 한다.

## Current fixture 결과

| 항목 | 결과 |
|---|---:|
| full-universe baseline | 6 |
| current trigger candidates | 5 |
| selected deep / budget | 5 / 5 |
| terminal outcomes | 각 종류 1개 |
| materialized current archetypes | 2 / registry 36 |
| forced archetype rows | 0 |
| archetype quota | 0 |
| replay input | 0 |
| trigger score evidence | 0 |

Current leaf hash는 `e6142d30f5360fb61b3fa519123e64539cd0cb4b0051ceac8c7ac4f80ed72fd1`다.

## Output root 분리

각 output root에는 `e2r_run_mode.json`이 먼저 생긴다.

```text
output/historical_replay/... → mode=HISTORICAL_REPLAY
output/current_operation/... → mode=CURRENT_OPERATION
```

Historical root에 current manifest를 쓰거나 반대로 쓰면 즉시 실패한다. 같은 폴더 이름만 다르게 보이는 수준이 아니라 marker와 반대 mode manifest를 검사한다.

독립 separation audit hash는 `702400d8e940a96ba194bb930fbb5409b11ad273693d1f584288c4d97cbc4836`이며 critical count는 0이다.

## 주요 파일

- `replay/historical_parity.py`: frozen benchmark leaf, registry parity row, threshold audit
- `runtime/current_operation.py`: current baseline, trigger, claim, bounded deep, terminal outcome
- `runtime/run_mode_separation.py`: mode marker, output-root ownership, cross-mode audit
- `tests/test_historical_current_mode_separation.py`: contamination·future·quota·output-root known-bad 검사
- `e2r_reconstruction_phase11_acceptance.json`: Phase 11 고정 acceptance

## 검증 경계

Phase 11은 historical/current 혼합을 막는 구조와 parity 기준을 완성했다. Current fixture의 `FULL_THESIS`는 score/stage 엔진 검증이 끝났다는 뜻이 아니다. Phase 12에서 accepted current claims, material gaps, contradiction resolution, StageCourt trace를 한 AtomicStageDecision으로 다시 검증한다.
