# Historical Green Simulation Bridge Gap - 2026-06-19

## 결론

예전 연구에는 Green/Green 후보가 실제로 많이 있다.

하지만 그 연구결과가 현재 runtime 점수표에 자동으로 더해지는 구조는 아니다. 현재 runtime은 과거 연구의 `score_simulation` 점수를 직접 읽지 않고, 매번 source-backed field를 다시 뽑아 7개 component로 계산한다.

그래서 문제가 생긴 위치는 세 군데다.

1. 과거 연구의 세부축 이름과 runtime field 이름이 다르다.
2. 아키타입별 weight는 반영됐지만, 세부축을 원천 증거 field로 번역하는 adapter가 부족하다.
3. 현재 benchmark replay는 parser audit 날짜 누수 오탐을 제거한 뒤에도 좋은 케이스가 `bottleneck`, `visibility`, `information_confidence`에서 막힌다.

쉬운 예:

- 과거 연구 답안: `orderbook_quality_score`, `capacity_conversion_score`, `customer_quality_score`를 올려 Green.
- 현재 채점표: `backlog_rpo_visibility`, `capa_constraint`, `contract_quality`만 본다.
- 중간 번역기가 없으면 답안에 "고객이 장기 좌석 예약"이라고 써 있어도 채점표의 "예약 확정" 칸은 빈칸으로 남는다.

## 1. 과거 연구 Green은 실제로 많다

대상:

- `docs/round/achieve/achieve_v12/**/*.md`
- JSON line 중 `row_type == "score_simulation"`

집계:

| 항목 | 수 |
| --- | ---: |
| 전체 `score_simulation` row | 9,052 |
| `stage_label_after`에 Green 포함 | 768 |
| 엄격한 `Stage3-Green` | 204 |
| Green 계열 중 `changed_components` 있음 | 668 |
| Green 계열 중 `changed_components` 없음 | 100 |

즉 "예전 연구에서 Green이 거의 없었다"가 아니다. Green 사례는 충분히 있었다.

문제는 그 Green이 현재 production 점수로 바로 변환되지 않는다는 점이다.

## 2. Green을 만든 아키타입은 HBM에만 있지 않다

Green 계열 `score_simulation` 상위 아키타입:

| archetype | Green 계열 row |
| --- | ---: |
| `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` | 54 |
| `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` | 48 |
| `C22_INSURANCE_RATE_CYCLE_RESERVE` | 45 |
| `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` | 42 |
| `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` | 40 |
| `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` | 33 |
| `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` | 29 |
| `C18_CONSUMER_EXPORT_CHANNEL_REORDER` | 29 |
| `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | 29 |
| `C02_POWER_GRID_DATACENTER_CAPEX` | 28 |
| `C11_BATTERY_ORDERBOOK_RERATING` | 24 |
| `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` | 20 |
| `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | 13 |

엄격한 `Stage3-Green`만 봐도 HBM 외 아키타입이 많다.

| archetype | strict `Stage3-Green` |
| --- | ---: |
| `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` | 27 |
| `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` | 25 |
| `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` | 20 |
| `C22_INSURANCE_RATE_CYCLE_RESERVE` | 18 |
| `C02_POWER_GRID_DATACENTER_CAPEX` | 14 |
| `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` | 13 |
| `C18_CONSUMER_EXPORT_CHANNEL_REORDER` | 9 |
| `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | 7 |
| `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | 4 |
| `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` | 3 |

따라서 삼전/하닉은 HBM 전용 보정 대상이 아니다.

삼전/하닉은 "과거 연구축이 현재 runtime 입력칸으로 안 넘어가는 문제"가 눈에 잘 보이는 대표 케이스다.

## 3. 과거 Green을 만든 component가 runtime field와 바로 맞지 않는다

Green 계열 row에서 자주 바뀐 `changed_components`:

| changed component | count | 현재 runtime 상태 |
| --- | ---: | --- |
| `execution_risk_score` | 383 | red-team 일부에만 흡수, 아키타입별 실행 리스크 bridge 부족 |
| `margin_bridge_score` | 317 | FCF/actual conversion 일부만 있음, 주문-to-margin bridge 부족 |
| `customer_quality_score` | 134 | HBM/defense 일부 키만 있음, named customer/retention/qualification bridge 부족 |
| `revision_score` | 130 | 있음. 다만 proxy/outlier quarantine으로 자주 약화 |
| `valuation_repricing_score` | 89 | 있음. 하지만 아키타입별 rerating frame은 약함 |
| `policy_or_regulatory_score` | 73 | 범용 policy-to-cashflow bridge 부족 |
| `backlog_visibility_score` | 65 | 일부 있음. orderbook quality/delivery/margin 연결 부족 |
| `relative_strength_score` | 60 | price stage는 있으나 Green 근거로 직접 쓰지 않음 |
| `legal_or_contract_risk_score` | 59 | 일부 guard만 있음 |
| `channel_reorder_score` | 45 | export/recurring 일부만 있음, sell-through/reorder bridge 부족 |
| `roe_pbr_capital_return_score` | 28 | valuation/capital 일부만 있음, 금융 전용 primitive 부족 |
| `commercialization_score` | 15 | 바이오/의료 approval-to-revenue bridge 부족 |
| `ifrs17_csm_quality_score` | 5 | 보험 전용 primitive 없음 |
| `kics_capital_buffer_score` | 5 | 보험 전용 primitive 없음 |
| `recurring_revenue_score` | 5 | SW ARR/RPO/retention primitive 부족 |

코드에서 현재 feature layer가 직접 읽는 parsed field key는 134개다.

하지만 위 Green 연구축 대부분은 exact runtime field로 존재하지 않는다. 이것은 단순 이름 차이만은 아니다. 의미 변환도 빠져 있다.

예:

- `customer_quality_score`는 C06 HBM에서는 `customer_preorder_or_allocation`일 수 있다.
- C08 test socket에서는 고객 qualification/repeat consumable일 수 있다.
- C28 SW/security에서는 retention, renewal, RPO일 수 있다.
- C21 금융에서는 신용비용과 자본환원 실행력일 수 있다.

같은 "고객 품질"이라도 아키타입마다 runtime field가 달라야 한다.

## 4. 현재 benchmark에서 좋은 케이스도 이렇게 낮다

`output/0619_asof_stage_promotion_benchmark_current_2023_2026/score_components_by_candidate.csv` 기준 best row:

| 후보 | best date | stage | score | sector | EPS | visibility | bottleneck | valuation | info | contract | backlog | capa | domain |
| --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SK하이닉스 | 2024-05-01 | 3-Yellow | 76.7639 | MEMORY_HBM | 20.0 | 15.1502 | 11.6339 | 12.3390 | 3.0 | 0.0 | 15.0 | 0.0 | 80.0 |
| 삼성전자 | 2024-04-01 | 2 | 68.6752 | MEMORY_HBM | 20.0 | 12.4403 | 9.9143 | 11.6985 | 3.0 | 0.0 | 0.0 | 0.0 | 60.0 |
| 효성중공업 | 2023-06-01 | 2 | 68.6325 | POWER_EQUIPMENT | 20.0 | 12.9531 | 10.3592 | 12.6517 | 3.0 | 0.0 | 70.0 | 23.0 | 36.0 |
| 일진전기 | 2023-12-01 | 2 | 68.5162 | POWER_EQUIPMENT | 20.0 | 15.9709 | 5.6740 | 10.6766 | 3.0 | 51.0 | 70.0 | 27.5 | 36.0 |
| HD현대일렉트릭 | 2023-08-01 | 2 | 66.3585 | POWER_EQUIPMENT | 20.0 | 14.5550 | 9.9811 | 8.0945 | 3.0 | 41.5 | 85.0 | 48.0 | 54.0 |
| 삼양식품 | 2024-06-01 | 1 | 57.0212 | GENERIC | 20.0 | 10.7931 | 4.0810 | 7.3823 | 3.0 | 35.0 | 0.0 | 0.0 | 14.0 |
| 산일전기 | 2025-03-01 | 1 | 51.1615 | POWER_EQUIPMENT | 18.0 | 6.1884 | 8.6640 | 9.5627 | 2.25 | 0.0 | 0.0 | 43.0 | 36.0 |
| 실리콘투 | 2024-06-01 | 1 | 50.0880 | K_BEAUTY_EXPORT | 9.0 | 11.6604 | 9.3589 | 8.7323 | 1.5 | 35.0 | 0.0 | 0.0 | 96.0 |
| 한화에어로스페이스 | 2024-08-01 | 1 | 29.4010 | DEFENSE | 0.0 | 10.6400 | 2.7960 | 6.8460 | 2.25 | 62.0 | 70.0 | 0.0 | 40.0 |

이 표가 말하는 것:

- 하닉은 EPS/visibility/valuation은 충분하지만 `capa=0`, `contract=0`, `backlog=15`라 bottleneck이 11.63에 멈춘다.
- 삼성은 하닉보다 backlog/domain이 약하므로 바로 Green으로 올리면 안 된다.
- 전력기기는 backlog가 들어와도 bottleneck이 낮다. 주문/리드타임/마진 전환을 bottleneck으로 더 잘 옮겨야 한다.
- 삼양식품은 EPS는 강하지만 sector가 `GENERIC`으로 잡혀 K-food/K-beauty export bridge가 약하다.
- 실리콘투는 domain 96인데 EPS/info/실적원천이 약해서 Stage 1이다. sell-through/reorder/financial actual 연결이 필요하다.
- 한화에어로는 contract/backlog가 있어도 EPS/FCF와 bottleneck이 거의 안 들어온다. defense delivery-to-revenue/margin bridge가 없다.

## 5. 섹터 평균도 같은 문제를 보인다

현재 benchmark 120 row 평균:

| sector | n | avg score | EPS | visibility | bottleneck | valuation | info | backlog | capa | domain |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MEMORY_HBM | 20 | 74.90 | 20.00 | 14.78 | 10.82 | 12.31 | 2.48 | 14.25 | 0.00 | 79.00 |
| POWER_EQUIPMENT | 48 | 58.36 | 17.88 | 11.38 | 8.05 | 9.43 | 2.70 | 51.56 | 32.43 | 37.12 |
| K_BEAUTY_EXPORT | 11 | 50.09 | 9.00 | 11.66 | 9.36 | 8.73 | 1.50 | 0.00 | 0.00 | 96.00 |
| DEFENSE | 12 | 29.40 | 0.00 | 10.64 | 2.80 | 6.85 | 2.25 | 70.00 | 0.00 | 40.00 |
| GENERIC | 29 | 26.30 | 7.59 | 5.06 | 2.37 | 3.08 | 1.89 | 0.00 | 0.00 | 5.31 |

공통 패턴:

- `bottleneck`이 모든 sector에서 Green 문턱 15보다 낮다.
- HBM은 거의 다 왔지만 CAPA/customer lock 변환이 빠졌다.
- POWER_EQUIPMENT는 backlog는 있는데 margin/leadtime/capacity lock이 bottleneck으로 덜 간다.
- DEFENSE는 backlog는 있는데 delivery-to-revenue/EPS/FCF 변환이 없다.
- K_BEAUTY_EXPORT는 domain은 높은데 financial actual과 정보 confidence가 약하다.
- GENERIC은 애초에 올바른 sector/archetype adapter로 못 들어간다.

## 6. 그러면 누적 연구가 잘못 반영된 건가

정확히 말하면 반만 반영됐다.

반영된 것:

- 아키타입별 7개 component weight는 runtime에 있다.
- `C06_HBM_MEMORY_CUSTOMER_CAPACITY`는 24/21/19/15/12/4/5 weight를 쓴다.
- `C21`, `C22`, `C23`, `C28` 같은 비-HBM weight도 있다.

덜 반영된 것:

- 과거 연구의 세부축을 source-backed runtime primitive로 바꾸는 adapter.
- score simulation의 `changed_components`를 현재 feature field로 연결하는 bridge.
- Green positive와 guard를 한 쌍으로 검증하는 fixture.
- field-level score loss report.

쉬운 예:

- 메뉴판에는 "보험은 CSM/K-ICS가 중요"라고 적혀 있다. 이것이 weight 반영이다.
- 그런데 주문 앱에는 아직 CSM/K-ICS 입력칸이 없다. 이것이 primitive/adapter 결손이다.
- 그래서 보험 Green 연구가 많아도 runtime은 그 점수를 제대로 못 만든다.

## 7. 다음 구현 요구사항

### A. ResearchAxisBridge 추가

과거 연구 component 이름을 바로 runtime 점수에 더하지 말고, source-backed primitive로 번역한다.

예:

| research axis | runtime primitive 후보 |
| --- | --- |
| `capacity_conversion_score` | `capacity_precommitted`, `capa_locked_years`, `capacity_utilization_pct`, `delivery_slot_locked` |
| `customer_quality_score` | `named_customer_confirmed`, `customer_preorder_or_allocation`, `retention_or_renewal`, `qualification_passed` |
| `margin_bridge_score` | `order_to_margin_visible`, `opm_expansion_pctp`, `fcf_quality_score`, `working_capital_clean` |
| `ifrs17_csm_quality_score` | `csm_growth_pct`, `kics_ratio`, `reserve_quality_score`, `shareholder_return_execution` |
| `commercialization_score` | `approval_granted`, `revenue_or_royalty_contract`, `partner_launch_confirmed` |
| `sell_through_score` | `sell_through_growth`, `repeat_order`, `channel_inventory_clean`, `receivables_clean` |
| `recurring_revenue_score` | `arr_growth`, `net_retention`, `rpo_growth`, `renewal_rate` |

### B. 아키타입별 adapter 필요

같은 `customer_quality_score`라도 C06, C08, C21, C28에서 의미가 다르다.

따라서 deterministic fallback query를 늘리는 방식이 아니라:

- LLM/parser가 source-backed evidence를 뽑고
- deterministic adapter가 canonical primitive로 정규화하고
- scorer가 primitive를 7개 component로 계산해야 한다.

### C. score loss report 강화

현재는 `failed_stage3_bottleneck`처럼 결과만 보인다.

필요한 설명은 이런 형태다.

```text
failed_stage3_bottleneck
- expected research axes: capacity_conversion_score, customer_quality_score
- observed runtime fields: capa_constraint=0, contract_quality=0, backlog_rpo_visibility=15
- missing primitive: capacity_precommitted, hbm_capacity_pre_sold, customer_allocation_source
```

이렇게 보여야 "왜 깎였는지"가 바로 보인다.

## 최종 판단

지금 낮은 점수는 HBM 전망을 낮게 본 결과가 아니다.

현재 시스템은 과거 연구에서 Green을 만든 축을 충분히 알고 있지만, 그 축이 runtime 입력 field로 안정적으로 변환되지 않는다. 그래서 삼전/하닉 테스트에서도 막히고, 비-HBM 아키타입에서도 같은 문제가 반복된다.

따라서 해결 방향은:

1. Green threshold를 낮추지 않는다.
2. HBM 전용 보정도 하지 않는다.
3. 과거 Green 연구축을 source-backed primitive로 번역하는 bridge를 만든다.
4. positive/guard fixture를 아키타입별로 같이 돌린다.
5. score explanation에 field-level 손실을 출력한다.
