# Bottleneck Formula Path Autopsy - 2026-06-19

## 결론

이 문서는 HBM에 과적합하기 위한 문서가 아니다.

삼성전자와 SK하이닉스는 대표 증상이다. 같은 방식으로 전력기기, 방산, K-뷰티, generic fallback에서도 `연구자료 -> runtime primitive -> bottleneck component -> Green gate` 변환 손실이 발생하는지 보는 기준으로 쓴다.

쉬운 예:

- 나쁜 해결: "하닉이 낮으니 HBM이면 병목 점수를 올린다."
- 맞는 해결: "CAPA 잠김, 고객 allocation, 수주잔고, 납기, 수출 mix 같은 증거가 source-backed field로 들어왔는지 확인한다."
- 더 맞는 해결: "하닉 positive는 올라오되, 삼성 catch-up guard와 다른 섹터 guard가 같이 뚫리지 않는지 fixture 쌍으로 검증한다."

## 병목 점수 구조

Green의 병목 문턱은 `bottleneck_pricing >= 15`다.

현재 병목 component는 raw 100점 값을 20점 component로 바꾼다.

```text
bottleneck_pricing = selected_bottleneck_raw / 100 * 20 - one_off_shortage_penalty
```

현재 benchmark 주요 row는 `one_off_shortage_penalty=0`이므로 Green 병목 15점을 받으려면 `selected_bottleneck_raw >= 75`가 필요하다.

쉬운 예:

- 병목 raw가 75면 `75 / 100 * 20 = 15`라 Green 병목 문턱 통과다.
- 병목 raw가 58이면 `58 / 100 * 20 = 11.6`이라 3.4점 부족하다.

선택 후보 산식은 세 개다.

| path | 산식 | 의미 |
| --- | --- | --- |
| `industrial` | `capa_constraint * 0.35 + asp_pricing_power * 0.35 + structural_shortage * 0.30` | CAPA/가격/쇼티지 산업 병목 |
| `sector` | `sector_bottleneck_score * 0.60 + asp_pricing_power * 0.25 + structural_shortage * 0.15` | 섹터 병목 profile 중심 |
| `actual_conversion_bridge` | `actual_profit_conversion * 0.25 + sector_bottleneck * 0.35 + structural_shortage * 0.25 + asp * 0.15` | 실적 전환이 확인된 병목 bridge |

runtime은 이 중 가장 높은 raw를 고른다.

## 대표 사례

기준 파일:

- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/stage_gate_matrix.csv`
- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/score_components_by_candidate.csv`

| company | date | sector | canonical archetype | stage | selected path | selected raw | Green 필요 raw | raw 부족 | raw bottleneck | weighted bottleneck | weighted 문턱 | weighted 부족 | total 부족 |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SK하이닉스 | 2024-05-01 | MEMORY_HBM | C06 | 3-Yellow | `actual_conversion_bridge` | 58.1697 | 75.0000 | 16.8303 | 11.6339 | 11.0522 | 14.2500 | 3.1978 | 10.2361 |
| 삼성전자 | 2024-04-01 | MEMORY_HBM | C10 | 2 | `actual_conversion_bridge` | 49.5717 | 75.0000 | 25.4283 | 9.9143 | 6.9400 | 10.5000 | 3.5600 | 18.3248 |
| HD현대일렉트릭 | 2024-05-01 | POWER_EQUIPMENT | C02 | 2 | `industrial` | 49.5250 | 75.0000 | 25.4750 | 9.9050 | 9.9050 | 15.0000 | 5.0950 | 14.0367 |
| 효성중공업 | 2023-06-01 | POWER_EQUIPMENT | C02 | 2 | `actual_conversion_bridge` | 49.0463 | 75.0000 | 25.9537 | 9.8093 | 9.8093 | 15.0000 | 5.1907 | 15.2528 |

주의:

- `selected raw`는 병목 내부 산식의 0~100 raw다.
- `raw bottleneck`은 canonical 20점 component다.
- `weighted bottleneck`은 아키타입 weight 적용 후 실제 Green gate에서 비교하는 값이다.

## SK하이닉스 계산

2024-05-01 SK하이닉스는 EPS, revision, visibility 쪽이 크게 막힌 것이 아니다. 병목 raw가 75까지 올라가지 못한 것이 직접 원인이다.

입력:

| field | 값 |
| --- | ---: |
| `capa_constraint` | 0.0000 |
| `asp_pricing_power` | 20.0000 |
| `structural_shortage` | 68.4000 |
| `sector_bottleneck_score` | 51.6040 |
| `actual_profit_conversion_score` | 80.0333 |
| `backlog_rpo_visibility` | 15.0000 |
| `contract_quality` | 0.0000 |
| `domain_specific_evidence_score` | 80.0000 |

선택된 bridge 계산:

```text
80.0333 * 0.25
+ 51.6040 * 0.35
+ 68.4000 * 0.25
+ 20.0000 * 0.15
= 58.1697
```

해석:

- `actual_profit_conversion_score=80.0333`이라 실적 전환은 꽤 잡혔다.
- `domain_specific_evidence_score=80`이라 HBM 도메인 신호도 잡혔다.
- 하지만 `capa_constraint=0`, `contract_quality=0`, `backlog_rpo_visibility=15`라 "생산능력/고객 물량이 잠겼다"는 핵심 증거가 Green 병목 raw 75까지 밀어 올리지 못한다.

쉬운 예:

- 하닉은 답안에 "HBM 좌석이 대부분 예약됐다"는 내용이 있는데, 채점표의 `capa_constraint` 칸은 0점인 상태다.
- 정답은 "하닉이면 보너스"가 아니라 "좌석 예약 증거가 있으면 어떤 아키타입이든 해당 칸에 점수가 들어가게 한다"다.

## 삼성전자 계산

삼성전자 2024-04-01도 같은 HBM sector에 있지만 하닉보다 낮게 들어온다.

입력:

| field | 값 |
| --- | ---: |
| `capa_constraint` | 0.0000 |
| `asp_pricing_power` | 20.0000 |
| `structural_shortage` | 66.6000 |
| `sector_bottleneck_score` | 40.5500 |
| `actual_profit_conversion_score` | 62.9167 |
| `backlog_rpo_visibility` | 0.0000 |
| `contract_quality` | 0.0000 |
| `domain_specific_evidence_score` | 60.0000 |

선택된 bridge raw는 49.5717이고, Green 필요 raw 75까지 25.4283 부족하다.

해석:

- 하닉보다 `actual_profit_conversion`, `sector_bottleneck`, `domain`, `backlog`가 모두 낮다.
- 따라서 삼성은 catch-up guard로 보는 것이 맞다.
- 하닉 positive를 고치면서 삼성까지 자동 Green으로 열리면 과적합 또는 false positive다.

쉬운 예:

- 하닉은 예약표가 어느 정도 보이는 케이스다.
- 삼성은 행사장에 들어오고 있지만 예약표가 하닉만큼 강하게 찍히지 않은 케이스다.
- 둘 다 같은 HBM이라는 이유만으로 같은 점수를 주면 안 된다.

## 전체 섹터 경로 분포

120개 benchmark row 기준 병목 selected path:

| sector | n | selected path 분포 |
| --- | ---: | --- |
| DEFENSE | 12 | `sector`: 12 |
| GENERIC | 29 | `sector`: 29 |
| K_BEAUTY_EXPORT | 11 | `sector`: 11 |
| MEMORY_HBM | 20 | `actual_conversion_bridge`: 20 |
| POWER_EQUIPMENT | 48 | `actual_conversion_bridge`: 11, `industrial`: 26, `sector`: 11 |

섹터별 평균:

| sector | selected raw | raw 부족 | component 점수 | bottleneck 부족 | total 부족 | visibility 부족 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| DEFENSE | 13.98 | 61.02 | 2.80 | 12.20 | 51.35 | 2.89 |
| GENERIC | 11.84 | 63.16 | 2.37 | 12.63 | 58.60 | 9.45 |
| K_BEAUTY_EXPORT | 46.79 | 28.21 | 9.36 | 5.64 | 36.91 | 3.34 |
| MEMORY_HBM | 54.10 | 20.90 | 10.82 | 4.18 | 12.10 | 0.30 |
| POWER_EQUIPMENT | 39.52 | 35.48 | 7.90 | 7.10 | 26.41 | 3.67 |

이 표가 중요한 이유:

- HBM은 Green에 가장 가까운 sector지만 병목 raw가 75까지 못 간다.
- 전력기기는 path가 섞인다. 어떤 row는 `industrial`, 어떤 row는 `actual_conversion_bridge`, 어떤 row는 `sector`가 선택된다. 즉 전력기기는 HBM 보너스로 풀 수 없다.
- 방산과 generic은 `sector` path만 선택되고 raw가 매우 낮다. 전용 adapter/primitive가 부족하다는 신호다.
- K-뷰티는 sector raw는 중간까지 오지만 Green total과 병목에는 아직 부족하다.

## 필요한 수정 방향

이번 autopsy가 요구하는 수정은 threshold 완화가 아니다.

필요한 것은 다음이다.

1. source-backed evidence bridge
   - 연구자료의 문장을 runtime primitive로 옮긴다.
   - 예: "고객 allocation", "sold-out capacity", "lead time", "수주잔고 질", "수출 mix", "CSM", "ARR/RPO" 등.

2. archetype adapter
   - 36개 아키타입을 9개 sector profile만으로 압축하지 않는다.
   - 예: HBM의 capacity lock, 전력기기의 transformer lead time, 방산의 delivery schedule, 보험의 CSM/K-ICS는 서로 다른 primitive가 필요하다.

3. positive/guard fixture pair
   - 하닉 positive는 올라와야 한다.
   - 삼성 catch-up guard는 증거가 부족하면 같이 Green으로 뚫리면 안 된다.
   - 비-HBM도 같은 방식으로 positive/guard pair가 필요하다.

4. score loss report
   - `failed_stage3_bottleneck`만 보여주지 않는다.
   - `selected_path`, `selected_raw`, `required_raw`, `raw_deficit`, 그리고 어떤 primitive가 0점인지 같이 보여준다.

## 완료 기준

완료는 하닉 하나가 Green이 되는 것이 아니다.

다음이 동시에 맞아야 한다.

- 하닉 같은 historical positive가 Green 또는 Green-candidate로 올라온다.
- 삼성 같은 catch-up guard가 근거 부족 상태에서 같이 Green으로 열리지 않는다.
- 전력기기, 방산, 소비재, 바이오, 보험, 플랫폼도 각자 positive/guard fixture를 통과한다.
- 설명에 "무슨 field가 몇 점이라 몇 점 부족했는지"가 표시된다.
