# Component Formula Loss Trace - 2026-06-19

## 목적

삼전/하닉을 HBM에 과적합하기 위한 예시로 쓰지 않는다.

이 문서는 삼전/하닉을 대표 케이스로 삼아, 연구자료에 있는 신호가 runtime 점수 입력칸으로 얼마나 들어왔는지 추적한다. 같은 방식으로 다른 아키타입에서도 `연구축 -> runtime primitive -> component score -> stage gate` 변환 손실을 찾아야 한다.

주의:

- 이 문서는 병목 내부 formula와 raw 20점 component를 추적하는 문서다.
- 2026-06-19 후속 수정 이후 실제 Green gate deficit은 `archetype_component_*` weighted 기준으로 계산한다.
- 최신 weighted gate 설명은 `weighted_gate_and_route_alignment_2026-06-19.md`를 기준으로 본다.

쉬운 예:

- 연구자료에는 "고객이 생산능력을 미리 잡아갔다"는 내용이 있다.
- 그런데 runtime 입력값 `capa_constraint`가 0이면, 시험 답안지는 맞게 썼는데 채점표의 "CAPA 잠김" 칸은 빈칸으로 남은 것이다.
- 하닉은 이 문제가 가장 잘 보이는 예시이고, 삼성은 catch-up guard로 같이 봐야 하는 예시다.

## Green Gate와 관련 공식

Stage 3-Green 주요 문턱:

| 항목 | Green 문턱 |
| --- | ---: |
| total score | 87 |
| EPS/revision component | 17 |
| earnings visibility | 15 |
| bottleneck/pricing | 15 |
| mispricing | 10 |
| valuation | 10 |
| medium revision | 55 |
| structural visibility | 45 |

현재 component 공식에서 중요한 부분:

| component | 핵심 입력 |
| --- | --- |
| earnings visibility | `visibility_raw / 100 * 20 - one_off_shortage_risk / 100 * 3` |
| sector visibility raw | `structural_visibility_quality * 0.55 + medium_term_revision_visibility * 0.20 + fcf_quality * 0.15 + backlog_rpo_visibility * 0.10` |
| industrial visibility raw | `contract_quality * 0.35 + backlog_rpo_visibility * 0.45 + fcf_quality * 0.20` |
| bottleneck/pricing | `bottleneck_raw / 100 * 20 - one_off_shortage_risk / 100 * 4` |
| sector bottleneck raw | `sector_bottleneck_score * 0.60 + asp_pricing_power * 0.25 + structural_shortage * 0.15` |
| industrial bottleneck raw | `capa_constraint * 0.35 + asp_pricing_power * 0.35 + structural_shortage * 0.30` |

실제 전환 bridge가 있으면 `actual_conversion`, `structural_visibility_quality`, `fcf_quality`, `backlog_rpo_visibility`도 일부 섞인다. 하지만 그 bridge 역시 source-backed field가 채워져야 작동한다.

## SK Hynix 000660 손실 추적

### 2024-04-01

| 항목 | 값 |
| --- | ---: |
| stage | 3-Yellow |
| total score | 76.0596 |
| total Green 부족분 | 10.9404 |
| visibility 부족분 | 0.2943 |
| bottleneck 부족분 | 3.6040 |
| EPS 부족분 | 0 |
| mispricing/valuation/revision/structural 부족분 | 0 |

주요 입력값:

| field | 값 | 해석 |
| --- | ---: | --- |
| `contract_quality` | 0.0 | 장기계약/고객잠김 증거가 계약 field로 못 들어옴 |
| `backlog_rpo_visibility` | 15.0 | 일부 allocation/preorder만 반영 |
| `capa_constraint` | 0.0 | CAPA 잠김/생산능력 제약이 핵심인데 0점 |
| `asp_pricing_power` | 20.0 | 가격 신호는 일부 반영 |
| `structural_shortage` | 68.4 | 구조적 shortage는 반영 |
| `sector_bottleneck_score` | 51.115 | sector bottleneck은 중간 수준 |
| `domain score` | 80.0 | HBM 도메인 신호는 강함 |

formula 관점:

| 계산값 | 값 |
| --- | ---: |
| industrial bottleneck raw | 27.5200 |
| sector bottleneck raw | 45.9290 |
| actual-conversion bridge bottleneck raw | 56.9800 |
| visibility raw | 73.5285 |
| inferred actual_conversion | 75.9590 |
| inferred fcf_quality | 87.5005 |

해석:

- EPS, valuation, revision이 낮아서 탈락한 것이 아니다.
- 거의 Green 근처까지 왔지만 `bottleneck/pricing`이 15점 문턱에서 3.604점 부족했다.
- 핵심 원인은 `capa_constraint=0`, `contract_quality=0`, `backlog_rpo_visibility=15`다.
- 즉 연구에서 보이는 "HBM CAPA 잠김, 고객 allocation, 장기 visibility"가 runtime primitive로 충분히 번역되지 않았다.

### 2024-05-01 이후 2025-03까지 반복

| 항목 | 값 |
| --- | ---: |
| stage | 3-Yellow |
| total score | 76.7639 |
| total Green 부족분 | 10.2361 |
| visibility 부족분 | 0 |
| raw bottleneck 부족분 | 3.3661 |
| weighted bottleneck 부족분 | 3.1978 |
| EPS 부족분 | 0 |
| mispricing/valuation/revision/structural 부족분 | 0 |

주요 입력값:

| field | 값 |
| --- | ---: |
| `contract_quality` | 0.0 |
| `backlog_rpo_visibility` | 15.0 |
| `capa_constraint` | 0.0 |
| `asp_pricing_power` | 20.0 |
| `structural_shortage` | 68.4 |
| `sector_bottleneck_score` | 51.604 |
| `domain score` | 80.0 |

formula 관점:

| 계산값 | 값 |
| --- | ---: |
| industrial bottleneck raw | 27.5200 |
| sector bottleneck raw | 46.2224 |
| actual-conversion bridge bottleneck raw | 58.1695 |
| visibility raw | 75.7510 |
| inferred actual_conversion | 80.0324 |
| inferred fcf_quality | 100.0009 |

해석:

- visibility는 15점 문턱을 통과한다.
- 그래도 bottleneck이 raw 기준 3.3661점, C06 weighted gate 기준 3.1978점 부족해서 Green이 막힌다.
- 이건 HBM 점수를 억지로 올릴 문제가 아니라, `capacity lock`과 `customer lock`을 모든 아키타입에서 primitive로 받을 수 있게 만드는 문제다.

쉬운 예:

- 하닉은 수학 문제 대부분을 맞혔는데, 채점표의 "생산능력 선점 증거" 칸이 빈칸이라 가산점을 못 받은 상태다.
- 정답은 "하닉이면 Green"이 아니라 "CAPA/고객잠김 증거가 source-backed로 있으면 해당 field가 채워지게 한다"다.

## Samsung 005930 손실 추적

### 2024-04-01

| 항목 | 값 |
| --- | ---: |
| stage | 2 |
| total score | 68.6752 |
| total Green 부족분 | 18.3248 |
| raw visibility 부족분 | 2.5597 |
| weighted visibility 부족분 | 2.3037 |
| raw bottleneck 부족분 | 5.0857 |
| weighted bottleneck 부족분 | 3.5600 |
| EPS 부족분 | 0 |
| mispricing/valuation/revision/structural 부족분 | 0 |

주요 입력값:

| field | 값 | 해석 |
| --- | ---: | --- |
| `contract_quality` | 0.0 | 장기계약/고객잠김이 계약 field로 안 들어옴 |
| `backlog_rpo_visibility` | 0.0 | 하닉보다 visibility 증거가 더 약하게 들어옴 |
| `capa_constraint` | 0.0 | CAPA 제약 field 미반영 |
| `asp_pricing_power` | 20.0 | 가격 신호 일부 반영 |
| `structural_shortage` | 66.6 | 구조적 shortage는 일부 반영 |
| `sector_bottleneck_score` | 40.55 | 하닉보다 낮음 |
| `domain score` | 60.0 | 하닉 80보다 낮음 |

formula 관점:

| 계산값 | 값 |
| --- | ---: |
| industrial bottleneck raw | 26.9800 |
| sector bottleneck raw | 39.3200 |
| actual-conversion bridge bottleneck raw | 49.5715 |
| visibility raw | 62.2015 |
| inferred actual_conversion | 62.9160 |
| inferred fcf_quality | 74.9990 |

해석:

- 삼성도 EPS만 보면 문제가 없어 보일 수 있다.
- 하지만 Green까지는 total 18.3248점, C10 weighted bottleneck 3.5600점, weighted visibility 2.3037점이 부족하다.
- 하닉보다 `backlog_rpo_visibility`, `domain score`, `sector_bottleneck_score`, `actual_conversion`이 모두 낮게 들어온다.
- 따라서 삼성은 "하닉과 같이 무조건 Green"이 아니라, catch-up 후보와 false-positive guard를 동시에 검증하는 케이스가 맞다.

쉬운 예:

- 하닉은 답안지에 "고객이 좌석을 미리 예약했다"는 근거가 있는데 채점표가 못 읽은 상황에 가깝다.
- 삼성은 같은 행사장에 들어오고 있지만, 그 좌석 예약 증거가 하닉만큼 강하게 찍히지 않은 상태다.
- 그래서 둘을 같이 Green으로 올리는 패치가 아니라, 하닉 positive와 삼성 guard가 동시에 깨지지 않는 bridge가 필요하다.

## 전체 Benchmark Deficit

운영 benchmark 120개 row 기준으로 모든 row가 total과 bottleneck 문턱에서 실패했다.

| 항목 | 평균 부족분 | 중앙값 부족분 | 실패 row | 최대 부족분 |
| --- | ---: | ---: | ---: | ---: |
| total | 37.28 | 29.98 | 120 | 87.00 |
| EPS | 5.55 | 0.00 | 45 | 17.00 |
| visibility | 4.73 | 3.34 | 98 | 15.00 |
| bottleneck | raw 8.33 / weighted 6.21 | raw 6.34 | 120 | raw 13.80 |
| mispricing | 2.56 | 0.07 | 67 | 9.40 |
| valuation | 2.64 | 1.27 | 78 | 9.55 |
| revision | 17.17 | 0.00 | 56 | 55.00 |
| structural visibility | 10.31 | 0.00 | 44 | 45.00 |

섹터별 평균 부족분:

| sector | n | total | EPS | visibility | bottleneck | mispricing | valuation | revision | structural visibility |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| POWER_EQUIPMENT | 48 | 28.64 | 1.42 | 3.84 | 6.95 | 1.23 | 1.33 | 16.04 | 8.89 |
| GENERIC | 29 | 60.70 | 10.55 | 9.94 | 12.63 | 6.88 | 6.92 | 34.14 | 27.93 |
| MEMORY_HBM | 20 | 12.10 | 0.00 | 0.30 | 4.18 | 0.00 | 0.00 | 0.00 | 0.00 |
| DEFENSE | 12 | 57.60 | 17.00 | 4.36 | 12.20 | 3.98 | 3.15 | 25.00 | 0.00 |
| K_BEAUTY_EXPORT | 11 | 36.91 | 8.00 | 3.34 | 5.64 | 0.07 | 1.27 | 0.00 | 0.00 |

가장 Green에 가까운 row:

| 후보 | 기간 | total score | total 부족분 | visibility 부족분 | bottleneck 부족분 | `capa_constraint` | `backlog_rpo_visibility` | domain |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SK Hynix | 2024-05~2025-03 | 76.7639 | 10.2361 | 0.0000 | raw 3.3661 / weighted 3.1978 | 0.0 | 15.0 | 80.0 |
| SK Hynix | 2024-04 | 76.0596 | 10.9404 | 0.2943 | 3.6040 | 0.0 | 15.0 | 80.0 |
| SK Hynix | 2025-04 이후 | 약 72.70 | 14.30 | 0.00 | 5.41 | 0.0 | 15.0 | 80.0 |

bottleneck이 가장 가까운 row:

| 후보 | bottleneck score | bottleneck 부족분 | `capa_constraint` | `asp_pricing_power` | `structural_shortage` | `sector_bottleneck_score` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SK Hynix 2024-05~2025-03 | raw 11.6339 / weighted 11.0522 | raw 3.3661 / weighted 3.1978 | 0.0 | 20.0 | 68.4 | 51.604 |
| SK Hynix 2024-04 | 11.3960 | 3.6040 | 0.0 | 20.0 | 68.4 | 51.115 |
| Power equipment 상위권 | 약 10.36 | 약 4.64 | 23.0 | 20.0 | 77.3 | 37.775 |

## 전체 아키타입으로 일반화

이 결과가 말하는 것은 HBM 과적합이 아니다.

| 범주 | 관찰 | 필요한 해결 |
| --- | --- | --- |
| MEMORY_HBM | total은 Green 근처지만 bottleneck/CAPA field가 비어 막힘 | capacity lock, allocation, customer prepayment, advanced packaging constraint를 source-backed primitive로 변환 |
| POWER_EQUIPMENT | backlog/CAPA 신호 일부가 있어도 bottleneck/visibility와 revision이 부족 | backlog-to-margin, grid lead time, transformer slot lock 같은 bridge 보강 |
| GENERIC | 거의 모든 component가 부족 | generic fallback에 빠지는 아키타입을 sector/archetype profile로 승격 |
| DEFENSE | EPS/revision/bottleneck이 크게 부족 | 수주잔고, book-to-bill, 예산/정책 visibility, margin bridge primitive 필요 |
| K_BEAUTY_EXPORT | visibility/bottleneck과 EPS가 부족 | sell-through, channel inventory, export mix, repeat order bridge 필요 |

쉬운 예:

- 하닉은 "CAPA 잠김 칸" 하나가 비어서 Green이 막힌 대표 케이스다.
- GENERIC은 시험지가 아예 다른 과목 양식으로 채점되는 케이스다.
- DEFENSE는 수주잔고와 정책 예산이 답안에 있어도 EPS/revision 채점칸으로 못 옮겨지는 케이스다.

## 결론

1. 하닉이 낮은 이유는 EPS/valuation/revision이 아니라 `capa_constraint=0`, `contract_quality=0`, 낮은 `backlog_rpo_visibility` 때문에 bottleneck component가 문턱을 못 넘기기 때문이다.
2. 삼성은 하닉보다 domain, backlog, actual conversion이 낮게 들어와서 catch-up guard로 봐야 한다. 삼성까지 자동 Green으로 올리는 패치는 위험하다.
3. benchmark 120개 row 전체가 bottleneck 문턱에서 실패한다. 이는 HBM 한 섹터 문제가 아니라 component 변환 공통 문제다.
4. 다음 구현은 threshold 완화가 아니라 source-backed evidence bridge, archetype adapter, score loss report여야 한다.

완료 기준은 단순하다.

- 하닉 positive는 Green 또는 Green-candidate로 올라와야 한다.
- 삼성 guard는 증거가 부족하면 같이 Green으로 뚫리면 안 된다.
- 비-HBM positive/guard fixture도 같은 원칙으로 통과해야 한다.
- 설명에는 "왜 몇 점 깎였는지"가 field 단위로 보여야 한다.
