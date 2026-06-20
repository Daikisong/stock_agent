# Current Benchmark Replay Green Gap Board - 2026-06-19

## 결론

현재 코드 기준으로 benchmark as-of replay를 다시 돌렸더니 `Stage3-Green`은 0개였다.

즉 SK하이닉스만 낮게 나오는 문제가 아니다. 알려진 구조적 winner들도 후보에는 들어오지만 대부분 Stage1/Stage2/Stage3-Yellow에서 멈춘다.

쉬운 예:

- 연구 장부: "HD현대일렉트릭은 변압기 수주잔고/마진/revision으로 Green 가능."
- runtime replay: "EPS는 좋다. 하지만 revision/contract/bottleneck/valuation gate가 부족해서 Stage2."

## 실행 명령

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --frequency monthly \
  --output-directory output/0619_asof_replay_benchmark_current_2023_2026 \
  --max-web-research-candidates-per-date 20 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10 \
  --no-theme-rebalance
```

```bash
PYTHONPATH=src python -m e2r.cli.analyze_asof_stage_promotion \
  --asof-output output/0619_asof_replay_benchmark_current_2023_2026/2023-01-01_to_2026-05-14 \
  --output-directory output/0619_asof_stage_promotion_benchmark_current_2023_2026 \
  --top-candidates 120 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10
```

## Replay Summary

| metric | value |
| --- | ---: |
| replay dates | 41 |
| universe rows scanned | 514 |
| layer1 candidates | 120 |
| web researched candidates | 120 |
| date verified documents | 860 |
| rejected future documents | 25 |
| discovered candidates | 120 |
| Stage 0 count | 7 |
| Stage 1 count | 67 |
| Stage 2 count | 34 |
| Stage3-Yellow count | 12 |
| Stage3-Green count | 0 |

이 결과는 "Green gate가 실제 운영 replay에서 거의 열리지 않는다"는 강한 신호다.

## Benchmark Best Rows

아래 표는 각 KR benchmark symbol의 최고 score row다. `expected_safe`는 benchmark label의 기대 안전 stage다.

| label | symbol | expected_safe | best date | runtime stage | score | sector | EPS | visibility | bottleneck | valuation | revision | structural visibility | missing families | failed gates |
| --- | --- | --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| HD현대일렉트릭 | 267260 | Green | 2023-08-01 | Stage2 | 72.9633 | POWER_EQUIPMENT | 20.0 | 16.1049 | 9.9050 | 10.0969 | 100.0 | 70.1030 | consensus, consensus_revision, news | total, bottleneck, contract |
| 효성중공업 | 298040 | Green | 2023-06-01 | Stage2 | 71.7472 | POWER_EQUIPMENT | 20.0 | 13.2566 | 9.8093 | 14.4893 | 100.0 | 48.6496 | consensus, consensus_revision, news | total, visibility, bottleneck, contract |
| 일진전기 | 103590 | Green | 2023-12-01 | Stage2 | 68.5162 | POWER_EQUIPMENT | 20.0 | 15.9709 | 5.6740 | 10.6766 | 100.0 | 68.8260 | consensus, consensus_revision, news | total, bottleneck, sector bottleneck |
| 산일전기 | 062040 | Yellow | 2025-03-01 | Stage1 | 51.1615 | POWER_EQUIPMENT | 18.0 | 6.1884 | 8.6640 | 9.5627 | 93.3333 | 24.6620 | financial_actual, consensus, consensus_revision, news | Stage2 total/info, Green total/visibility/bottleneck/valuation/contract |
| 삼양식품 | 003230 | Yellow | 2024-06-01 | Stage1 | 62.5526 | GENERIC | 20.0 | 12.0813 | 4.0810 | 8.7323 | 100.0 | 51.9810 | consensus, consensus_revision, news | Stage2 total, Green total/visibility/bottleneck/mispricing/valuation/domain |
| 한화에어로스페이스 | 012450 | Yellow | 2024-08-01 | Stage1 | 35.6473 | DEFENSE | 0.0 | 12.1119 | 2.7960 | 8.4460 | 83.3333 | 67.9472 | financial_actual, consensus, consensus_revision, news | Stage2 total/EPS/info, Green total/EPS/visibility/bottleneck/mispricing/valuation |
| 실리콘투 | 257720 | unknown | 2024-06-01 | Stage1 | 50.0880 | K_BEAUTY_EXPORT | 9.0 | 11.6604 | 9.3589 | 8.7323 | 100.0 | 74.7628 | financial_actual, disclosure, consensus, consensus_revision, news | Stage2 total/EPS/info, Green total/EPS/visibility/bottleneck/mispricing/valuation |
| 삼성전자 메모리 | 005930 | unknown | 2024-04-01 | Stage2 | 68.6752 | MEMORY_HBM | 20.0 | 12.4403 | 9.9143 | 11.6985 | 80.0 | 59.9121 | consensus, consensus_revision, news | total, visibility, bottleneck |
| SK하이닉스 메모리 | 000660 | unknown | 2024-05-01 | Stage3-Yellow | 76.7639 | MEMORY_HBM | 20.0 | 15.1502 | 11.6339 | 12.3390 | 100.0 | 71.3652 | consensus, consensus_revision, news | total, bottleneck |
| 에코프로비엠 | 247540 | Red | 2023-08-01 | Stage1 | 9.3080 | GENERIC | 0.0 | 0.0000 | 1.3200 | 0.4500 | 0.0 | 0.0000 | financial_actual, research_report, consensus, consensus_revision, news | many |
| 대한전선-like | 001440 | Red | 2026-02-01 | Stage1 | 0.0000 | POWER_EQUIPMENT | 0.0 | 0.0000 | 1.2000 | 0.4500 | 0.0 | 0.0000 | financial_actual, research_report, consensus, consensus_revision, news | many |

## Gate Failure Counts

전체 120개 candidate 기준:

| failed gate | count |
| --- | ---: |
| `failed_stage3_total_score` | 120 |
| `failed_stage3_bottleneck` | 120 |
| `failed_stage3_visibility` | 87 |
| `failed_stage3_valuation` | 67 |
| `failed_stage2_total_score` | 67 |
| `failed_stage2_information_confidence` | 63 |
| `failed_sector_bottleneck` | 56 |
| `failed_stage3_market_mispricing` | 56 |
| `failed_stage2_eps_fcf` | 45 |
| `failed_stage3_eps_fcf` | 45 |
| `failed_green_cross_evidence` | 40 |
| `failed_stage3_contract_quality` | 37 |
| `failed_domain_specific_evidence` | 33 |
| `failed_sector_visibility` | 33 |
| `failed_structural_visibility_quality` | 33 |
| `failed_stage3_revision` | 22 |

Structural benchmark best row만 보면:

| failed gate | count among 7 structural labels |
| --- | ---: |
| `failed_stage3_total_score` | 7 |
| `failed_stage3_bottleneck` | 7 |
| `failed_stage3_visibility` | 5 |
| `failed_stage2_total_score` | 4 |
| `failed_stage3_valuation` | 4 |
| `failed_sector_bottleneck` | 3 |
| `failed_stage2_information_confidence` | 3 |
| `failed_stage3_contract_quality` | 3 |
| `failed_stage3_market_mispricing` | 3 |
| `failed_stage2_eps_fcf` | 2 |
| `failed_stage3_eps_fcf` | 2 |

핵심은 Green 실패가 우연이 아니라 전역 패턴이라는 점이다. 후보 120개 모두 Green total과 Green bottleneck을 실패한다.

## 왜 Evidence가 있는데 Missing으로 보이나

benchmark recall 표에는 `consensus`, `consensus_revision`이 evidence로 보인다. 그런데 autopsy의 `missing_evidence_families`에는 `consensus`, `consensus_revision`, `news`가 자주 남는다.

이유는 runtime confidence 쪽에서 독립 consensus/revision과 report-derived proxy를 구분하기 때문이다.

쉬운 예:

- 리포트 안에 "컨센서스 상향" 문장이 있다.
- replay는 이걸 proxy consensus로 만들 수 있다.
- 하지만 Green family gate에서는 독립 consensus/revision으로 강하게 보지 않는다.
- 그래서 evidence 목록에는 consensus가 있는데 Green confidence 쪽에서는 missing으로 남을 수 있다.

이 보수성 자체는 필요하다. 문제는 proxy를 전부 버리는 것이 아니라, source-backed directional revision을 어떤 조건에서 어느 점수까지 인정할지 규칙이 부족하다는 것이다.

## 아키타입별 관찰

### C01/C02 Power Equipment

HD현대일렉트릭, 효성중공업, 일진전기는 모두 EPS/FCF가 20점이다. 그런데 Green은 실패한다.

주요 병목:

- contract/revision이 Green 기준에 부족
- `bottleneck_pricing`이 낮음
- 독립 consensus/revision/news family가 없음

쉬운 예:

- "수주잔고와 실적은 좋아"까지는 읽는다.
- "장기계약의 질, 납기/마진 bridge, 독립 추정치 상향"을 Green 확신으로 못 올린다.

### C06 HBM

SK하이닉스는 Stage3-Yellow까지는 간다. 하지만 Green은 total/bottleneck에서 막힌다.

주요 병목:

- `contract_quality=0`
- `capa_constraint=0`
- `fcf_quality_score=0`
- `backlog_rpo_visibility=15`

쉬운 예:

- "HBM이 좋다"는 80점으로 읽는다.
- "그 HBM 물량이 실제로 잠겼고, CAPA가 막혔고, 현금흐름으로 전환된다"는 점수로 못 바꾼다.

### C20/C18 Consumer Export

삼양식품과 실리콘투는 structural winner label인데 replay stage가 낮다.

주요 병목:

- 삼양식품은 `GENERIC`으로 들어가 K-food profile을 못 탄다.
- 실리콘투는 `K_BEAUTY_EXPORT`를 탔지만 EPS/FCF와 information confidence가 약하다.
- sell-through/reorder/channel margin bridge가 충분히 점수화되지 않는다.

쉬운 예:

- "해외에서 잘 팔린다"는 보인다.
- "반복 주문, 채널 sell-through, 마진 bridge, EPS revision"이 한 묶음으로 Green까지 못 올라간다.

### C03 Defense

한화에어로스페이스는 DEFENSE profile로 잡혔지만 Stage1이다.

주요 병목:

- financial_actual 없음
- EPS/FCF 0
- bottleneck 2.796
- revision 30

방산은 계약/수주잔고가 있어도 납품, 마진, 실적 전환 field가 없으면 Green은커녕 Stage2도 힘들다.

## 전역 진단

현재 replay는 후보 발굴 자체는 한다. 하지만 Green으로 승격하는 데 필요한 세부 bridge가 거의 항상 비어 있다.

| layer | 증상 | 의미 |
| --- | --- | --- |
| candidate funnel | structural winner들이 후보에는 대체로 등장 | 1차 발굴은 완전히 죽은 것은 아님 |
| score conversion | EPS/FCF는 자주 높지만 bottleneck/visibility가 낮음 | 연구 문장이 Green component로 충분히 변환 안 됨 |
| evidence family | consensus/revision/news missing 반복 | report proxy와 독립 source 구분 때문에 Green confidence 부족 |
| sector profile | 일부는 GENERIC으로 떨어짐 | 아키타입별 profile coverage 부족 |
| Green gate | 120개 모두 total/bottleneck 실패 | Green gate가 닫힌 상태에 가까움 |

## 다음 패치 우선순위

1. Green target fixture 세트를 먼저 고정한다.
   - C06 SK하이닉스 2024-04-25/26
   - C01/C02 HD현대일렉트릭/효성중공업/일진전기
   - C20 삼양식품
   - C03 한화에어로스페이스
   - C20/C25 실리콘투 또는 의료기기/수출형 winner

2. 각 fixture에서 research phrase -> runtime field 손실표를 만든다.
   - 예: "backlog + margin bridge"가 `bottleneck_pricing` 몇 점으로 들어갔는지
   - 예: "export reorder"가 `recurring_demand_visibility`와 `export_channel_visibility`에 들어갔는지

3. 독립 consensus가 없는 경우의 source-backed directional revision 인정 규칙을 만든다.
   - 무조건 Green으로 열면 안 된다.
   - date-verified report + numeric estimate table + target revision + financial actual이 같이 있을 때만 제한적으로 인정한다.

4. 아키타입 전용 profile을 늘린다.
   - C20 K-food/K-beauty classification 보강
   - C21/C22 금융/보험 profile
   - C23/C25 바이오/의료 상업화 profile
   - C28 software/security profile
   - C30/C31/C32 event/credit/governance profile

## 한 줄 진단

최신 benchmark replay는 "후보는 찾지만 Green은 거의 못 연다"는 상태다.  
이유는 Green threshold 숫자 하나가 아니라, 연구 Green의 핵심 bridge가 runtime field와 evidence family로 충분히 변환되지 않기 때문이다.
