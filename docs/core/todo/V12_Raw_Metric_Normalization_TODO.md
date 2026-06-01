# V12 Raw Metric Normalization TODO

작성일: 2026-06-01

이 문서는 향후 연구 row가 더 쌓인 뒤 C18/C19/C20, 특히 소비재/브랜드/유통/재고형 아키타입을 더 세밀하게 보정하기 위한 TODO다.

핵심은 다음이다.

- 현재 연구 row에는 MFE/MAE, entry price, peak/drawdown 같은 가격 결과 데이터가 많이 쌓이고 있다.
- 현재 연구 row에는 `margin_bridge_score`, `inventory_quality_score`, `sell_through_score` 같은 판단형 점수/프록시는 있다.
- 하지만 재고율, 매출성장률, OPM 변화, 매출채권 변화 같은 원자료 숫자 필드는 아직 표준 JSON field로 거의 누적되지 않았다.
- 따라서 "재고가 늘었다"를 무조건 나쁘게 보지 말고, 매출/마진/매출채권/셀스루와 같이 봐서 성장 재고와 채널스터핑을 분리해야 한다.

쉬운 예:

```text
케이스 A:
  inventory_yoy_pct = +10
  sales_yoy_pct = +40
  opm_change_pctp = +3
  receivables_yoy_pct = +5

해석:
  재고가 늘었지만 매출이 더 빠르게 늘고 OPM도 개선된다.
  성장 재고일 가능성이 있어 C19에서 기계적으로 감점하면 안 된다.
```

```text
케이스 B:
  inventory_yoy_pct = +45
  sales_yoy_pct = +5
  opm_change_pctp = -2
  receivables_yoy_pct = +30

해석:
  재고와 매출채권은 크게 늘었는데 매출은 둔화되고 OPM이 하락한다.
  채널스터핑, 할인판매, 마진 훼손 위험으로 보고 Green 차단 또는 4C 감시가 필요하다.
```

## 1. 현재 확인 상태

2026-06-01 기준으로 `docs/round/achieve_v12`와 `docs/round/achieve`의 JSON row를 점검했다.

| 항목 | 상태 |
|---|---:|
| 파싱 가능한 JSON row | 13,815 |
| `MFE_90D_pct` 보유 row | 8,944 |
| `MAE_90D_pct` 보유 row | 8,942 |
| `entry_price` 보유 row | 4,821 |
| `peak_date`/`peak_price` 보유 row | 4,816 |
| `current_profile_verdict` 보유 row | 6,557 |

가격 결과 데이터는 이미 충분히 많이 있다. 즉 "해당 Stage/score 이후 수익률과 낙폭이 어땠는지"는 보정 재료로 쓸 수 있다.

반면 원자료형 숫자 필드는 부족하다.

| 원자료 field | 현재 표준 row count |
|---|---:|
| `inventory_yoy_pct` | 0 |
| `inventory_days` | 0 |
| `receivables_yoy_pct` | 0 |
| `sales_yoy_pct` | 0 |
| `opm_expansion_pctp` | 0 |
| `gross_margin_yoy_pctp` | 0 |
| `sell_through_growth_pct` | 0 |
| `revenue_growth_pct` | 1 |

주의: 위 숫자는 "관련 개념이 문서에 전혀 없다"는 뜻이 아니다. `inventory_quality_score`, `inventory_turn_score`, `sell_through_score`, `margin_bridge_score` 같은 프록시 점수는 존재한다. 다만 나중에 임계값을 학습하기 좋은 원자료 field가 표준화되어 있지 않다는 뜻이다.

## 2. 앞으로 연구 row에 넣을 권장 field

소비재/브랜드/유통/재고형 연구 row에는 가능하면 아래 field를 같은 이름으로 넣는다.

| field | 의미 | 예시 |
|---|---|---:|
| `sales_yoy_pct` | 매출 YoY 성장률 | `40` |
| `revenue_yoy_pct` | 매출 YoY 성장률, 해외 자료에서 revenue 표현일 때 | `40` |
| `inventory_yoy_pct` | 재고 YoY 증가율 | `10` |
| `inventory_days` | 재고일수 | `75` |
| `inventory_days_change` | 재고일수 변화 | `-8` |
| `inventory_to_sales` | 재고/매출 비율 | `0.18` |
| `receivables_yoy_pct` | 매출채권 YoY 증가율 | `5` |
| `receivables_to_sales` | 매출채권/매출 비율 | `0.12` |
| `opm` | 영업이익률 | `14.5` |
| `opm_change_pctp` | OPM 변화폭, percentage point | `3` |
| `gross_margin` | 매출총이익률 | `42` |
| `gross_margin_yoy_pctp` | 매출총이익률 변화폭 | `2` |
| `sell_through_growth_pct` | 최종 판매 또는 sell-through 성장률 | `25` |
| `reorder_growth_pct` | 재주문 또는 repeat order 성장률 | `30` |
| `discount_rate_change_pctp` | 할인율 변화폭 | `-2` |

값이 없으면 억지로 만들지 않는다. 모르면 `null` 또는 field 생략이 낫다. 예를 들어 `as_of_date=2024-06-30`인데 2024-08-15에 나온 분기보고서 숫자를 넣으면 미래 데이터 누수다.

## 3. 적용 대상 아키타입

우선순위는 다음이다.

| 우선순위 | archetype | 이유 |
|---:|---|---|
| 1 | `C19_BRAND_RETAIL_INVENTORY_MARGIN` | 재고, 매출채권, 셀스루, 마진 훼손이 Stage 판단의 핵심 |
| 2 | `C18_CONSUMER_EXPORT_CHANNEL_REORDER` | 수출 채널과 재주문이 실수요인지 확인 필요 |
| 3 | `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` | 글로벌 유통 확장이 sell-through인지 shipment push인지 분리 필요 |
| 4 | `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` | 재고/매출채권/마진 악화가 4C thesis break로 이어지는지 검증 |

## 4. 나중에 구현할 scoring TODO

데이터가 더 쌓이면 아래 순서로 반영한다.

1. 연구 row parser가 위 raw field를 표준 key로 읽게 한다.
2. `FeatureEngineeringInput` 또는 parsed field에 raw metric을 전달한다.
3. C19용 `inventory_margin_quality_score`를 만든다.
4. C18/C20용 `sell_through_reorder_quality_score`를 만든다.
5. `receivables_inventory_spike`를 단순 bool에서 정도 기반 score로 확장한다.
6. C19 Green 조건에 `inventory_receivables_margin_quality` gate를 추가한다.
7. 반례 테스트를 추가한다.

테스트 예시는 다음이다.

```text
positive:
  inventory_yoy_pct +10
  sales_yoy_pct +40
  opm_change_pctp +3
  receivables_yoy_pct +5
  sell_through_growth_pct +25
  기대: C19에서 감점 없음 또는 visibility 보조점수

counterexample:
  inventory_yoy_pct +45
  sales_yoy_pct +5
  opm_change_pctp -2
  receivables_yoy_pct +30
  sell_through_growth_pct null
  기대: Green 차단, thesis break 또는 4C risk 상승
```

## 5. 운영 메모

가격 결과는 이미 많이 저장되고 있으므로, raw metric이 붙으면 미세조정은 가능하다.

현재 할 수 있는 보정:

- "재고/마진 리스크가 있었던 케이스가 대체로 실패했는지" 수준의 방향성 보정
- `inventory_quality_score`, `sell_through_score`, `margin_bridge_score` 같은 프록시 점수 기반 보정

추가 raw metric이 쌓이면 가능한 보정:

- 재고 +10%와 +45%를 다르게 처리
- 매출보다 재고가 빠르게 늘 때만 감점
- OPM 상승이 동반된 재고 증가는 성장 재고로 인정
- 매출채권 증가와 OPM 하락이 같이 나오면 채널스터핑/현금흐름 위험으로 가중
- C19 Stage 3-Green과 4C thesis break의 임계값을 데이터 기반으로 조정

이 TODO는 연구 row가 더 누적된 뒤 production scoring에 반영하기 위한 작업 대기열이다.
