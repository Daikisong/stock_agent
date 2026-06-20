# Weighted Gate and Route Alignment - 2026-06-19

## 결론

누적 연구에서 만든 아키타입별 weight는 runtime에 적용되고 있었다.

하지만 autopsy 설명이 실제 `StageClassifier`와 완전히 같은 자를 쓰지 않는 문제가 있었다.

수정 전:

- `StageClassifier`: 아키타입 weight가 적용된 component와 weight 비례 문턱을 비교
- `stage_gate_diagnostics`: raw component와 고정 문턱을 비교

수정 후:

- diagnostic도 weighted component와 weighted threshold를 쓴다.
- score/stage 판정 자체는 바뀌지 않았다.
- 바뀐 것은 "어디서 몇 점 부족한지" 설명의 정확도다.

쉬운 예:

- 하닉 C06의 bottleneck weight는 19점이다.
- raw bottleneck은 `11.6339 / 20`이다.
- 실제 gate 비교는 `11.0522 / 14.2500`이다.
- 예전 설명의 `11.63 / 15`는 방향은 맞지만 실제 채점표 숫자는 아니었다.

## 수정한 코드

변경 파일:

- `src/e2r/stage_gate_diagnostics.py`
- `src/e2r/backtest/asof_stage_promotion_autopsy.py`
- `tests/test_stage_gate_diagnostics.py`
- `tests/test_asof_stage_promotion_autopsy.py`

추가 출력:

- `large_sector_id`
- `canonical_archetype_id`
- `archetype_weight_*`
- `archetype_component_*`
- `archetype_weighted_total_before_calibration`

이제 `score_components_by_candidate.csv`와 `stage_gate_matrix.csv`에서 raw component와 weighted component를 같이 볼 수 있다.

## 삼전/하닉 정정 숫자

기준:

- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/stage_gate_matrix.csv`
- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/score_components_by_candidate.csv`

| company | date | sector | canonical archetype | raw bottleneck | weighted bottleneck | weighted threshold | weighted deficit | total deficit |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| SK하이닉스 | 2024-05-01 | MEMORY_HBM | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 11.6339 | 11.0522 | 14.2500 | 3.1978 | 10.2361 |
| 삼성전자 | 2024-04-01 | MEMORY_HBM | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 9.9143 | 6.9400 | 10.5000 | 3.5600 | 18.3248 |

하닉 해석:

- C06 weight는 제대로 적용됐다.
- 그래도 `capa_constraint=0`, `contract_quality=0`, `backlog_rpo_visibility=15`라 병목 raw가 58.1697에 머문다.
- Green 병목을 통과하려면 raw 75가 필요하다.
- 따라서 문제는 weight 적용 실패가 아니라 source-backed primitive 변환 부족이다.

삼성 해석:

- 삼성은 MEMORY_HBM sector지만 canonical archetype은 C10으로 잡혔다.
- 이유는 고객/CAPA lock 증거가 약하고 memory recovery/price-cycle 문맥이 강하기 때문이다.
- 만약 C06 weight로 강제해도 total은 약 70.4869로 Green은 아니다.
- 따라서 삼성은 "같은 HBM이니 같이 Green"이 아니라 catch-up guard로 두는 것이 맞다.

쉬운 예:

- 하닉은 "고객이 좌석을 예약했다"는 증거가 일부 있는데 채점표의 CAPA 잠김 칸이 비어 있다.
- 삼성은 행사장에는 들어왔지만 좌석 예약 증거가 더 약해서 C10 recovery/cycle 쪽으로 분류됐다.
- 둘을 같은 C06으로 강제하면 guard가 약해진다.

## 전체 benchmark 영향

120개 row 기준 pass/fail 변화:

| component | weighted deficit - raw deficit 평균 | pass/fail 변화 |
| --- | ---: | ---: |
| EPS/FCF | -0.8050 | 0 |
| visibility | -0.0151 | 0 |
| bottleneck | -2.1129 | 0 |
| mispricing | -0.2394 | 0 |
| valuation | -0.4420 | 0 |

즉 stage 결과가 바뀐 것은 아니다. 하지만 deficit 설명은 더 정확해졌다.

섹터별 bottleneck deficit:

| sector | n | raw deficit avg | weighted deficit avg | 차이 |
| --- | ---: | ---: | ---: | ---: |
| DEFENSE | 12 | 12.20 | 10.37 | -1.83 |
| GENERIC | 29 | 12.63 | 5.88 | -6.75 |
| K_BEAUTY_EXPORT | 11 | 5.64 | 3.38 | -2.26 |
| MEMORY_HBM | 20 | 4.18 | 3.91 | -0.27 |
| POWER_EQUIPMENT | 48 | 7.10 | 6.98 | -0.12 |

GENERIC은 bottleneck weight가 낮은 아키타입이 많아서 raw deficit 설명이 특히 과장됐다. 하지만 total 87과 핵심 primitive 부족 문제는 그대로 남는다.

## 추가로 고친 diagnostic 불일치

`StageClassifier`는 price-only blowoff가 크면 Stage2도 막는다. diagnostic의 Stage2 gate 집계에는 이 실패가 빠져 있었다.

또 `StageClassifier`는 POWER/DEFENSE 같은 profile에서 contract quality를 Green 조건으로 본다. diagnostic의 `stage3_green_gate_passed` 집계에는 contract 실패가 빠져 있었다.

수정 후:

- price-only blowoff는 Stage2 diagnostic도 막는다.
- contract quality 실패는 Stage3-Green diagnostic도 막는다.

## 지금까지 답

"누적 연구가 반영되지 않은 것 아니냐"에 대한 답:

- 아키타입별 weight는 반영됐다.
- C06 하닉은 실제로 C06 weight로 계산됐다.
- 하지만 weight는 빈 field를 채워주지 못한다.
- 연구축을 runtime primitive로 번역하는 bridge가 약해서 Green까지 못 간다.

쉬운 예:

- 연구 장부가 "금융은 자본환원을 크게 봐라"라고 배웠다.
- runtime weight도 금융의 capital weight를 키웠다.
- 그런데 parser/feature가 buyback, cancellation, dividend visibility를 `capital_allocation` 원점수로 못 옮기면 큰 weight는 0점에 곱해질 뿐이다.

## 다음 구현 기준

1. route audit
   - 하닉 C06 positive와 삼성 C10/C06 guard가 의도대로 나뉘는지 fixture로 고정한다.

2. weighted loss report
   - 모든 autopsy는 raw component, weighted component, weighted threshold를 같이 보여줘야 한다.

3. primitive bridge
   - HBM: capacity/customer allocation/pre-sold/packaging bottleneck
   - 금융/보험: buyback/cancellation/dividend, CSM, K-ICS, reserve quality
   - 바이오/의료: approval-to-revenue, royalty, reimbursement
   - SW/security: ARR/RPO, retention, NRR, renewal, margin leverage

완료는 아니다. 이번 작업은 "설명 계기판"을 실제 채점 로직에 맞춘 단계다.

