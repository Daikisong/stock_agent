# Green Gate Deficit Autopsy

## 결론

삼전/하닉이 낮게 나온 이유는 HBM 신호 하나가 빠져서만이 아니다.

현재 replay는 Green 문턱을 통과하기 전에 다음 두 곳에서 거의 전역으로 막힌다.

1. `total_score`
2. `bottleneck_pricing`

수정 후 autopsy에는 각 gate의 `value / threshold / deficit`이 직접 찍힌다.

쉬운 예:

- 예전 출력: `failed_stage3_bottleneck`
- 새 출력: `bottleneck:11.05/14.25(-3.20)`

즉 "막혔다"가 아니라 "C06 weight 기준 14.25점 필요했는데 11.05점이라 3.20점 모자랐다"까지 볼 수 있다.

주의: 2026-06-19 후속 수정으로 autopsy는 raw component가 아니라 실제 `StageClassifier`와 같은 weighted component/threshold를 사용한다. raw component 기준 설명은 `weighted_gate_and_route_alignment_2026-06-19.md`가 최신 기준으로 보정한다.

## 구현 변경

변경 파일:

- `src/e2r/backtest/asof_stage_promotion_autopsy.py`
- `tests/test_asof_stage_promotion_autopsy.py`

추가한 autopsy 필드:

| field | 의미 |
| --- | --- |
| `stage3_total_deficit` | Green total 문턱 부족분 |
| `stage3_visibility_deficit` | Green visibility 문턱 부족분 |
| `stage3_bottleneck_deficit` | Green bottleneck 문턱 부족분 |
| `stage3_revision_deficit` | Green revision 문턱 부족분 |
| `stage3_contract_quality_deficit` | Green contract 문턱 부족분 |
| `structural_visibility_deficit` | 구조적 visibility 문턱 부족분 |
| `sector_visibility_deficit` | sector visibility 문턱 부족분 |
| `sector_bottleneck_deficit` | sector bottleneck 문턱 부족분 |
| `domain_specific_evidence_deficit` | 도메인 증거 문턱 부족분 |
| `stage3_yellow_total_deficit` | Yellow 총점 문턱 부족분 |
| `green_gate_deficit_summary` | 부족분을 큰 순서로 요약한 문자열 |

이 필드는 JSON과 `stage_gate_matrix.csv`에 같이 들어간다.

## 삼전/하닉은 어디서 깎였나

기준:

- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/2026-06-19_autopsy.json`
- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/stage_gate_matrix.csv`

| company | best row | stage | score | total deficit | visibility deficit | bottleneck deficit | yellow total deficit | 핵심 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| SK하이닉스 | 2024-05-01 | 3-Yellow | 76.7639 | 10.2361 | 0.0000 | 3.1978 | 0.0000 | visibility는 통과했지만 weighted bottleneck과 total이 모자람 |
| 삼성전자 | 2024-04-01 | Stage2 | 68.6752 | 18.3248 | 2.3037 | 3.5600 | 6.3248 | C10 route 기준 catch-up/volume 확증 부족으로 visibility, bottleneck, total이 같이 모자람 |

하닉의 autopsy summary:

```text
total:76.76/87.00(-10.24); bottleneck:11.05/14.25(-3.20)
```

삼성의 autopsy summary:

```text
total:68.68/87.00(-18.32); yellow_total:68.68/75.00(-6.32); bottleneck:6.94/10.50(-3.56); visibility:11.20/13.50(-2.30)
```

해석:

- 하닉은 `EPS/FCF`, `revision`, `domain evidence`, `visibility`가 이미 높다.
- 하지만 Green은 `bottleneck_pricing >= 15`도 요구한다.
- 현재 하닉은 `capa_constraint=0`, `contract_quality=0`, `backlog_rpo_visibility=15`라 고객 lock-in/CAPA 잠김/장기 물량 배정이 충분히 점수화되지 않는다.
- 삼성은 하닉보다 더 보수적으로 보는 것이 맞다. catch-up 사례라 Green이 아니라 Stage2/Yellow 후보 쪽이 자연스럽다.
- 문제는 삼성도 하닉도 "왜 낮은지"가 예전에는 뭉개졌고, 이제 gate deficit으로 숫자가 보인다는 점이다.

## 다른 아키타입도 같은가

섹터별 평균 deficit:

| sector_profile | n | total deficit | visibility deficit | bottleneck deficit | revision deficit | contract deficit | sector bottleneck deficit | domain evidence deficit | yellow total deficit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DEFENSE | 12 | 51.35 | 2.89 | 12.20 | 0.00 | 0.00 | 20.35 | 0.00 | 39.35 |
| GENERIC | 29 | 58.60 | 9.45 | 12.63 | 34.14 | 0.00 | 23.92 | 29.69 | 46.60 |
| K_BEAUTY_EXPORT | 11 | 36.91 | 3.34 | 5.64 | 0.00 | 0.00 | 0.00 | 0.00 | 24.91 |
| MEMORY_HBM | 20 | 12.10 | 0.30 | 4.18 | 0.00 | 0.00 | 0.00 | 0.00 | 1.12 |
| POWER_EQUIPMENT | 48 | 26.41 | 3.67 | 7.10 | 4.58 | 25.18 | 3.76 | 2.92 | 14.41 |

이 표가 말하는 것:

- MEMORY_HBM은 제일 가까운 축이다. 하닉이 Yellow까지 올라오는 이유다.
- POWER_EQUIPMENT는 revision/parser 오탐을 고친 뒤 점수는 올라갔지만, contract와 bottleneck deficit이 여전히 크다.
- DEFENSE는 계약/수주잔고는 있는데 납품, 마진, 실적 전환, ASP 같은 bottleneck 변환이 거의 안 된다.
- GENERIC은 도메인별 adapter가 없어서 revision/domain/sector bottleneck이 통째로 빠진다.
- K_BEAUTY는 구조적 visibility는 잡히지만 Green total과 bottleneck 문턱에는 못 간다.

쉬운 예:

- HBM: "HBM 물량이 잠겼다"를 CAPA/customer allocation/bottleneck으로 번역해야 한다.
- 전력기기: "변압기 리드타임과 수주잔고가 길다"를 납기/ASP/margin bridge로 번역해야 한다.
- 방산: "수주잔고가 크다"를 납품 스케줄, 수출 mix, OPM 전환으로 번역해야 한다.
- 바이오/플랫폼/보험: 아예 전용 adapter가 부족해서 GENERIC처럼 많이 떨어질 가능성이 크다.

## 대표 non-HBM 사례

| company | stage | score | total deficit | bottleneck deficit | 다른 큰 deficit | 해석 |
| --- | --- | ---: | ---: | ---: | --- | --- |
| HD현대일렉트릭 | Stage2 | 72.9633 | 14.0367 | 5.0950 | contract 3.5000 | revision은 100으로 회복됐지만 contract/bottleneck 부족 |
| 효성중공업 | Stage2 | 71.7472 | 15.2528 | 5.1907 | contract 45.0000 | 수주잔고는 잡히지만 contract_quality가 0이라 Green 차단 |
| 삼양식품 | Stage1 | 62.5526 | 24.4474 | 10.9190 | domain 21.0000, sector bottleneck 15.6000 | export/ASP는 잡히지만 K-food 도메인 adapter가 약함 |
| 한화에어로스페이스 | Stage1 | 35.6473 | 51.3527 | 12.2040 | sector bottleneck 20.3500, EPS/FCF 17.0000 | 수주잔고는 잡히지만 납품/마진/실적 전환이 약함 |

## 핵심 원인

현재 문제는 세 층이다.

1. Research label/scorecard는 누적되어 있다.
2. 일부 parser/field 변환은 들어와 있다.
3. 하지만 Green gate가 요구하는 runtime component로 변환되는 bridge가 부족하다.

특히 `bottleneck_pricing`은 거의 모든 섹터에서 병목이다.

쉬운 예:

- 연구자료: "수주잔고가 사상 최대, CAPA가 꽉 참, ASP 상승"
- 현재 runtime: `backlog_rpo_visibility`만 일부 반영, `capa_constraint`나 `contract_quality`는 0 또는 낮음
- 결과: 총점은 올라가도 `bottleneck_pricing >= 15` 문턱을 못 넘음

## 다음 구현 방향

HBM 전용 점수 보너스는 답이 아니다.

다음은 전역 구현 과제다.

1. `green_gate_deficit_summary`를 daily/benchmark report에도 노출한다.
2. `bottleneck_pricing` 입력별 loss report를 만든다.
   - `contract_quality`
   - `backlog_rpo_visibility`
   - `capa_constraint`
   - `asp_pricing_power`
   - `sector_bottleneck_score`

   진행: 병목 산식의 `selected_path`, `selected_raw`, `required_raw`, `raw_deficit`은 `bottleneck_formula_path_autopsy_2026-06-19.md`에 추가했다. 다음은 어떤 source-backed primitive가 0점이 됐는지 adapter에서 고치는 단계다.

3. 아키타입별 adapter를 만든다.
   - HBM: customer allocation, sold-out capacity, HBM ASP, yield/margin
   - Power: transformer lead time, backlog quality, capacity expansion, margin delivery
   - Defense: delivery schedule, export mix, backlog-to-revenue conversion
   - K-food/K-beauty: channel reorder, sell-through, ASP/mix, recurring export demand
   - Bio/insurance/platform: approval-to-revenue, CSM/K-ICS, ARR/RPO/retention 같은 전용 bridge
4. positive/guard fixture pair로 검증한다.
   - 하닉 positive를 통과시키면서 삼성 catch-up guard를 같이 Green으로 열면 안 된다.
   - 같은 방식으로 power/defense/consumer/bio/platform도 쌍으로 검증해야 한다.
