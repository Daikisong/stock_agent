# V12 Score Normalization Trend

작성일: 2026-06-01

이 문서는 지금까지 점수 체계가 어떻게 바뀌었고, 현재 v12 연구결과가 아키타입별 점수비중에 어떻게 적용되는지 보기 위한 운영 문서다.

핵심은 다음이다.

- 기본 7개 컴포넌트는 점수 언어로 유지한다.
- 실제 런타임 점수비중은 `canonical_archetype_id`별로 달라진다.
- large sector weight는 참고/검증용으로 남아 있지만, runtime scoring은 canonical archetype 직접 매칭만 쓴다.
- 모르면 기본형으로 계산하지 않는다. agent/feature layer가 검색, 리포트, 공시, 뉴스, 파싱 필드로 L/C를 먼저 판별하고 그 아키타입 점수로 진행한다.
- Stage 3-Green 전역 기준은 완화하지 않았다.

## 1. 프로파일 추이

| 단계 | profile | 주요 변화 | Stage 3-Green total | revision | 의미 |
|---|---|---|---:|---:|---|
| 기준선 | `e2r_2_0_baseline` | 공통 7개 컴포넌트 점수표 | 85 | 50 | 모든 업종을 같은 100점표로 본 초기 기준 |
| 1차 보정 | `e2r_2_1_stock_web_calibrated` | price-only guard, 4B/4C guard, Green 기준 강화 | 87 | 55 | 가격만 오른 케이스와 one-off를 더 조심 |
| 현재 | `e2r_2_2_rolling_calibrated` | v12 rolling, 아키타입별 weight, agent classifier | 87 | 55 | C/R 아키타입별로 실제 점수비중이 달라짐 |

쉬운 예:

```text
예전:
  보험, 바이오, 전력기기, 화장품을 모두 EPS 20 + 가시성 20 + 병목 20 ...로 계산

현재:
  전력기기 C02는 backlog/가시성/병목을 더 본다.
  보험 C22는 병목보다 valuation/자본환원을 더 본다.
  바이오 임상 C24는 EPS보다 정보신뢰/이벤트 리스크를 훨씬 더 본다.
```

## 2. 기본표 대비 큰 방향

기본표는 비교 기준이다.

| 컴포넌트 | 기본 max |
|---|---:|
| EPS/FCF | 20 |
| 실적가시성 | 20 |
| 병목/가격 | 20 |
| 미스프라이싱 | 15 |
| 밸류에이션 | 15 |
| 자본정책 | 5 |
| 정보신뢰 | 5 |

현재 가장 크게 바뀐 축은 다음이다.

| 방향 | 아키타입 예 | 해석 |
|---|---|---|
| 정보신뢰 대폭 상향 | C24, R13, C14, C30, C31 | 이벤트/임상/정책/4B/4C는 “좋은 이야기”보다 검증 신뢰가 우선 |
| 병목/가격 대폭 하향 | C21, C22, C23, C24, C32 | 금융/보험/바이오/거버넌스는 물리적 병목 점수로 보면 왜곡됨 |
| 자본정책 상향 | C21, C22, C32, R13 accounting | ROE/PBR, 배당/자사주, 지배구조, 회계신뢰가 핵심인 영역 |
| EPS/FCF 상향 | C06, C07, C08, C10, C18, C20 | HBM/반도체/소비재 유통은 EPS revision과 이익 전환이 중요 |
| Green 제한 강화 | C04, C05, C11~C17, C23~C24, C30~C31, R13 | Stage 2는 가능하지만 Green은 추가 증거가 필요 |

## 3. 현재 아키타입별 점수표

표 순서는 `EPS/Vis/Bot/Mis/Val/Cap/Info`다.

- `EPS`: EPS/FCF
- `Vis`: 실적가시성
- `Bot`: 병목/가격
- `Mis`: 미스프라이싱
- `Val`: 밸류에이션
- `Cap`: 자본정책
- `Info`: 정보신뢰

`delta`는 기본표 `20/20/20/15/15/5/5` 대비 증감이다.

| archetype | posture | weights EPS/Vis/Bot/Mis/Val/Cap/Info | delta vs base | 핵심 변화 |
|---|---|---:|---:|---|
| `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | Green 가능 | 20/25/18/12/12/8/5 | 0/+5/-2/-3/-3/+3/0 | 상향: Vis, Cap; 하향: Bot, Mis, Val |
| `C02_POWER_GRID_DATACENTER_CAPEX` | Green 가능 | 21/24/20/13/12/5/5 | +1/+4/0/-2/-3/0/0 | 상향: EPS, Vis; 하향: Mis, Val |
| `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` | Green 가능 | 20/24/17/14/14/6/5 | 0/+4/-3/-1/-1/+1/0 | 상향: Vis, Cap; 하향: Bot, Mis, Val |
| `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` | Watch -> Green 조건부 | 15/22/10/15/18/10/10 | -5/+2/-10/0/+3/+5/+5 | 상향: Vis, Val, Cap, Info; 하향: EPS, Bot |
| `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` | Watch -> Green 조건부 | 18/22/10/12/10/8/20 | -2/+2/-10/-3/-5/+3/+15 | 상향: Vis, Cap, Info; 하향: EPS, Bot, Mis, Val |
| `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | Green 가능 | 24/21/19/15/12/4/5 | +4/+1/-1/0/-3/-1/0 | 상향: EPS, Vis; 하향: Bot, Val, Cap |
| `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` | Green 가능 | 22/22/19/14/12/6/5 | +2/+2/-1/-1/-3/+1/0 | 상향: EPS, Vis, Cap; 하향: Bot, Mis, Val |
| `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY` | Green 가능 | 22/21/16/14/12/6/9 | +2/+1/-4/-1/-3/+1/+4 | 상향: EPS, Vis, Cap, Info; 하향: Bot, Mis, Val |
| `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` | Watch -> Green 조건부 | 22/20/18/13/11/6/10 | +2/0/-2/-2/-4/+1/+5 | 상향: EPS, Cap, Info; 하향: Bot, Mis, Val |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | Watch -> Green 조건부 | 22/18/14/12/10/5/19 | +2/-2/-6/-3/-5/0/+14 | 상향: EPS, Info; 하향: Vis, Bot, Mis, Val |
| `C11_BATTERY_ORDERBOOK_RERATING` | Watch -> Green 조건부 | 20/20/15/12/10/8/15 | 0/0/-5/-3/-5/+3/+10 | 상향: Cap, Info; 하향: Bot, Mis, Val |
| `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` | Watch -> Green 조건부 | 20/18/14/10/10/8/20 | 0/-2/-6/-5/-5/+3/+15 | 상향: Cap, Info; 하향: Vis, Bot, Mis, Val |
| `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | Watch -> Green 조건부 | 20/18/14/12/10/10/16 | 0/-2/-6/-3/-5/+5/+11 | 상향: Cap, Info; 하향: Vis, Bot, Mis, Val |
| `C14_EV_DEMAND_SLOWDOWN_4B_4C` | Red/Watch gate | 15/12/10/8/8/7/40 | -5/-8/-10/-7/-7/+2/+35 | 상향: Cap, Info; 하향: EPS, Vis, Bot, Mis, Val |
| `C15_MATERIAL_SPREAD_SUPERCYCLE` | Watch -> Green 조건부 | 20/12/20/10/10/8/20 | 0/-8/0/-5/-5/+3/+15 | 상향: Cap, Info; 하향: Vis, Mis, Val |
| `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` | Watch -> Green 조건부 | 18/18/18/12/12/7/15 | -2/-2/-2/-3/-3/+2/+10 | 상향: Cap, Info; 하향: EPS, Vis, Bot, Mis, Val |
| `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` | Red/Watch gate | 20/12/18/10/10/5/25 | 0/-8/-2/-5/-5/0/+20 | 상향: Info; 하향: Vis, Bot, Mis, Val |
| `C18_CONSUMER_EXPORT_CHANNEL_REORDER` | Green 가능 | 22/23/12/16/13/4/10 | +2/+3/-8/+1/-2/-1/+5 | 상향: EPS, Vis, Mis, Info; 하향: Bot, Val, Cap |
| `C19_BRAND_RETAIL_INVENTORY_MARGIN` | Watch -> Green 조건부 | 18/18/8/15/14/7/20 | -2/-2/-12/0/-1/+2/+15 | 상향: Cap, Info; 하향: EPS, Vis, Bot, Val |
| `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` | Green 가능 | 22/23/12/16/13/4/10 | +2/+3/-8/+1/-2/-1/+5 | 상향: EPS, Vis, Mis, Info; 하향: Bot, Val, Cap |
| `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` | Green 가능 | 15/20/5/15/25/15/5 | -5/0/-15/0/+10/+10/0 | 상향: Val, Cap; 하향: EPS, Bot |
| `C22_INSURANCE_RATE_CYCLE_RESERVE` | Green 가능 | 12/22/5/14/24/18/5 | -8/+2/-15/-1/+9/+13/0 | 상향: Vis, Val, Cap; 하향: EPS, Bot, Mis |
| `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` | Watch -> Green 조건부 | 12/24/5/12/10/7/30 | -8/+4/-15/-3/-5/+2/+25 | 상향: Vis, Cap, Info; 하향: EPS, Bot, Mis, Val |
| `C24_BIO_TRIAL_DATA_EVENT_RISK` | Red/Watch gate | 5/15/5/10/5/5/55 | -15/-5/-15/-5/-10/0/+50 | 상향: Info; 하향: EPS, Vis, Bot, Mis, Val |
| `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` | Green 가능 | 20/22/13/14/12/9/10 | 0/+2/-7/-1/-3/+4/+5 | 상향: Vis, Cap, Info; 하향: Bot, Mis, Val |
| `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` | Green 가능 | 20/22/8/16/14/10/10 | 0/+2/-12/+1/-1/+5/+5 | 상향: Vis, Mis, Cap, Info; 하향: Bot, Val |
| `C27_CONTENT_IP_GLOBAL_MONETIZATION` | Watch -> Green 조건부 | 20/18/8/14/12/8/20 | 0/-2/-12/-1/-3/+3/+15 | 상향: Cap, Info; 하향: Vis, Bot, Mis, Val |
| `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` | Green 가능 | 20/24/8/16/14/8/10 | 0/+4/-12/+1/-1/+3/+5 | 상향: Vis, Mis, Cap, Info; 하향: Bot, Val |
| `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` | Watch -> Green 조건부 | 20/18/10/15/17/15/5 | 0/-2/-10/0/+2/+10/0 | 상향: Val, Cap; 하향: Vis, Bot |
| `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` | Red/Watch gate | 18/12/8/12/10/10/30 | -2/-8/-12/-3/-5/+5/+25 | 상향: Cap, Info; 하향: EPS, Vis, Bot, Mis, Val |
| `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` | Red/Watch gate | 12/15/8/15/15/10/25 | -8/-5/-12/0/0/+5/+20 | 상향: Cap, Info; 하향: EPS, Vis, Bot |
| `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` | Green 가능 | 12/18/5/20/25/15/5 | -8/-2/-15/+5/+10/+10/0 | 상향: Mis, Val, Cap; 하향: EPS, Vis, Bot |
| `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` | Red/Watch gate | 8/12/8/10/8/4/50 | -12/-8/-12/-5/-7/-1/+45 | 상향: Info; 하향: EPS, Vis, Bot, Mis, Val, Cap |
| `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` | Red/Watch gate | 8/12/5/10/8/20/37 | -12/-8/-15/-5/-7/+15/+32 | 상향: Cap, Info; 하향: EPS, Vis, Bot, Mis, Val |
| `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` | Red/Watch gate | 10/14/8/12/10/6/40 | -10/-6/-12/-3/-5/+1/+35 | 상향: Cap, Info; 하향: EPS, Vis, Bot, Mis, Val |
| `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` | Red/Watch gate | 10/14/8/12/10/6/40 | -10/-6/-12/-3/-5/+1/+35 | 상향: Cap, Info; 하향: EPS, Vis, Bot, Mis, Val |

## 4. 잘 적용되고 있는지 확인한 포인트

| 확인 항목 | 상태 |
|---|---|
| active profile | `e2r_2_2_rolling_calibrated` |
| runtime weight profile | `e2r_2_2_archetype_weight_runtime` |
| canonical archetype weights | 36개 |
| large sector weights | 10개, runtime fallback 용도 아님 |
| agent classifier | `FeatureEngineeringInput` -> `classify_v12_archetype` -> `ScoringPayload` |
| unknown/mismatch 처리 | 정상 agent 경로에서는 재분류 후 scoring, 직접 scorer 우회 호출은 strict error |
| 검증 | `PYTHONPATH=src python -m unittest discover -s tests -v` -> 3575 tests OK |

적용 예시는 다음과 같다.

```text
C02_POWER_GRID_DATACENTER_CAPEX:
  기본 20/20/20/15/15/5/5
  현재 21/24/20/13/12/5/5

해석:
  전력망/데이터센터 CAPEX는 EPS와 visibility를 더 보고,
  단순 valuation rerating은 덜 본다.
```

```text
C22_INSURANCE_RATE_CYCLE_RESERVE:
  기본 20/20/20/15/15/5/5
  현재 12/22/5/14/24/18/5

해석:
  보험은 공장 병목이 아니라 rate cycle, reserve, PBR/ROE, 자본환원이 핵심이다.
```

```text
C24_BIO_TRIAL_DATA_EVENT_RISK:
  기본 20/20/20/15/15/5/5
  현재 5/15/5/10/5/5/55

해석:
  임상 이벤트는 EPS를 크게 주면 안 된다.
  데이터 신뢰, 규제/임상 리스크, 이벤트 검증이 대부분을 차지한다.
```

## 5. 운영상 해석

현재 적용은 의도한 방향이다.

- R1~R13이 모두 같은 기본형으로 계산되는 상태가 아니다.
- 기본형은 비교 기준이고, 실제 scoring은 C/R archetype weight를 사용한다.
- 소비재, 보험, 바이오, 정책, 4B/4C red-team처럼 성격이 다른 영역은 확실히 다른 점수표로 분리됐다.
- 다만 다음 연구결과를 더 넣으면 support가 부족한 아키타입은 계속 세밀하게 보정해야 한다.

다음 라운드에서 추가로 보면 좋은 것은 다음이다.

1. C04/C05처럼 Watch -> Green 조건부인 산업재 이벤트의 Green 전환 조건
2. C18/C19/C20 소비재 안에서 reorder, inventory, global distribution 분리 정확도
3. C23/C24 바이오에서 approval과 trial event가 섞이지 않는지
4. C31 정책 이벤트가 실제 cashflow 전환 없이 Green으로 올라가지 않는지
5. R13 red-team scope가 score를 막는 역할을 제대로 하는지
