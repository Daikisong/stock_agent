# Archetype Runtime Profile Coverage - 2026-06-19

## 결론

현재 runtime은 36개 canonical archetype weight를 갖고 있지만, feature engineering의 sector profile은 9개뿐이다.

따라서 연구 장부가 배운 Green 논리가 모든 아키타입에 똑같이 런타임 점수로 번역되지 않는다.

쉬운 예:

- C21 금융 연구: `ROE/PBR + 자본환원 실행`이 Green 핵심.
- 현재 runtime: 금융 전용 profile이 없어서 `est_pbr`, `roe`, `capital_allocation` 일부로 압축.
- 결과: 연구 논리는 맞아도 Green component가 충분히 안 찰 수 있다.

## Runtime SectorProfile

`src/e2r/sector_profiles.py` 기준 현재 profile:

| profile | 성격 |
| --- | --- |
| `POWER_EQUIPMENT` | 전력기기 backlog/lead-time/capacity |
| `DEFENSE` | 방산 정부고객/수출/납품 |
| `K_FOOD_EXPORT` | K-food export/channel/repeat demand |
| `K_BEAUTY_EXPORT` | K-beauty export/channel/platform |
| `MEMORY_HBM` | HBM demand/price/customer/capacity |
| `CYCLICAL_SHIPPING` | shipping/freight |
| `BATTERY_OVERHEAT` | battery overheat/guard 성격 |
| `AI_INFRA_PLATFORM` | AI infra/cloud/RPO |
| `GENERIC` | 나머지 일반 경로 |

## Archetype Coverage Table

| archetype | runtime coverage | rows | Green/usable | good/bad Stage2 | false/missed/late | 핵심 runtime gap |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | partial | 288 | 9/6 | 115/43 | 63/21/36 | industrial generic/backlog fields exist; no C01 margin bridge profile |
| C02_POWER_GRID_DATACENTER_CAPEX | dedicated | 277 | 5/4 | 116/45 | 77/18/43 | POWER_EQUIPMENT profile covers backlog/leadtime/capacity |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | dedicated | 267 | 6/6 | 110/30 | 47/1/15 | DEFENSE profile covers government/export/delivery |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | partial | 220 | 0/0 | 52/33 | 60/4/12 | policy/project/legal delay mostly generic/guard |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | partial | 295 | 10/8 | 63/56 | 70/18/20 | contract fields exist; no EPC margin/cost-overrun profile |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | dedicated-but-thin | 229 | 9/7 | 82/42 | 66/11/36 | MEMORY_HBM exists; capacity/customer/margin conversion too thin |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | partial | 237 | 2/0 | 89/44 | 76/4/33 | HBM/equipment shares MEMORY_HBM/generic; no equipment order profile |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | partial | 247 | 10/3 | 88/40 | 56/8/37 | customer quality not dedicated |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | partial | 305 | 3/0 | 86/57 | 123/14/49 | valuation/overheat guard exists; no advanced equipment profile |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | partial | 366 | 4/4 | 125/103 | 115/15/61 | memory cycle partly HBM/generic; no recovery cycle profile |
| C11_BATTERY_ORDERBOOK_RERATING | partial | 286 | 2/1 | 94/65 | 108/10/47 | contract/order fields exist; battery profile is mostly overheat guard |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | partial | 262 | 0/0 | 62/63 | 101/3/26 | contract fields exist; call-off risk not first-class |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | partial | 307 | 6/6 | 63/77 | 86/5/22 | policy/utilization/AMPC not first-class |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | guard | 264 | 1/1 | 16/19 | 72/8/46 | BATTERY_OVERHEAT/guard direction, not Green unlock |
| C15_MATERIAL_SPREAD_SUPERCYCLE | generic | 324 | 12/9 | 80/69 | 104/11/32 | no materials spread profile |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | generic | 234 | 0/0 | 55/50 | 41/5/11 | no resource/policy supply profile |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | generic | 297 | 15/5 | 92/51 | 62/5/26 | no chemical spread profile |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | dedicated-ish | 308 | 14/2 | 98/56 | 87/8/56 | K_FOOD/K_BEAUTY export fields cover some channel/repeat demand |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | partial | 223 | 5/1 | 46/47 | 56/5/29 | brand/channel fields exist; inventory/sell-through weak |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | dedicated-ish | 358 | 33/8 | 122/43 | 84/4/77 | K_FOOD/K_BEAUTY export fields cover distribution/repeat/margin |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | generic | 413 | 37/7 | 136/46 | 78/4/78 | no finance profile; ROE/PBR/capital return thin |
| C22_INSURANCE_RATE_CYCLE_RESERVE | generic | 327 | 28/6 | 91/52 | 64/7/56 | no insurance profile; reserve/K-ICS/rate cycle missing |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | generic | 269 | 30/16 | 78/45 | 73/11/62 | no bio commercialization profile |
| C24_BIO_TRIAL_DATA_EVENT_RISK | guard/generic | 253 | 7/4 | 78/32 | 37/7/45 | trial event risk mostly guard/generic |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | generic | 259 | 12/4 | 90/62 | 83/11/31 | no reimbursement/export conversion profile |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | partial | 334 | 19/3 | 98/71 | 103/10/63 | AI_INFRA_PLATFORM exists but not ad/ARPU specific |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | generic | 263 | 12/3 | 70/56 | 58/1/47 | no content/IP monetization profile |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | partial | 285 | 14/4 | 75/55 | 90/11/49 | some contract/RPO fields; no SaaS/security retention profile |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | generic | 411 | 10/3 | 125/87 | 125/4/69 | no mobility/leisure profile |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | guard/generic | 377 | 3/0 | 58/70 | 99/15/56 | PF/legal balance sheet mainly guard/generic |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | guard/generic | 478 | 12/7 | 110/105 | 132/9/60 | policy headline guard; company cash bridge missing |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | guard/generic | 378 | 1/1 | 108/67 | 122/8/64 | governance/tender premium not structural profile |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | guard | 473 | 5/5 | 92/180 | 220/13/42 | red-team guardrail scope |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | guard | 1023 | 32/16 | 210/234 | 336/18/184 | red-team guardrail scope |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | guard | 619 | 8/8 | 129/73 | 153/9/19 | red-team guardrail scope |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | guard | 715 | 5/4 | 127/170 | 232/1/41 | red-team guardrail scope |

## 가장 큰 구조 문제

### 1. Weight는 넓고 feature profile은 좁다

아키타입별 weight는 36개다. 하지만 sector profile은 9개뿐이다.

그래서 C21/C22/C23/C25/C28처럼 Green 연구가 많은 아키타입도 runtime에서는 generic feature로 눌린다.

### 2. Green 사례가 많은 곳일수록 전용 field가 더 필요하다

특히 다음은 우선순위가 높다.

| archetype | Green/usable | 필요한 runtime field |
| --- | ---: | --- |
| C21 금융 | 37/7 | `roe`, `pbr`, capital return execution, buyback/cancellation, dividend visibility |
| C22 보험 | 28/6 | CSM, K-ICS, reserve quality, loss ratio, shareholder return |
| C23 바이오 | 30/16 | approval to revenue, royalty route, partner commercialization |
| C25 의료기기 | 12/4 | reimbursement listing, hospital adoption, billing volume, export reorder |
| C28 SW/security | 14/4 | ARR, retention, NRR, contract renewal, margin leverage |

### 3. Guard archetype는 Green unlock보다 false-positive 방어가 먼저다

R13/C30/C31/C32는 Green을 여는 축보다 잘 막는 축이 중요하다.

예:

- 정책 headline만으로 Green
- PF/legal risk를 무시한 Stage2
- price-only blowoff를 structural Green으로 착각
- governance premium을 반복 cashflow로 착각

이런 반례가 많기 때문에 Green threshold를 단순히 낮추면 안 된다.

## 다음 구현 우선순위

1. C06 HBM parser/feature conversion
   - 하닉 같은 명확한 winner를 놓친 핵심 증상이다.
   - 삼성 2024 catch-up false positive와 같이 검증해야 한다.

2. Common margin/revision/customer/backlog mapping
   - `margin_bridge_score`, `customer_quality_score`, `contract_score`, `backlog_visibility_score`가 여러 아키타입에 공통이다.

3. C21/C22/C23/C25/C28 전용 field 설계
   - Green 사례는 많은데 runtime profile이 generic이다.

4. R13/C30/C31 guard replay
   - Green recall을 올릴 때 false positive가 같이 올라오는지 반드시 확인한다.

## 검증 메모

이 문서의 row/Green/Stage2/error counts는 다음 파일에서 재계산했다.

- `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl`
- `configs/e2r_archetype_weight_profile_v2_2.json`

이번 문서는 분석/문서화이며 runtime code는 수정하지 않았다.
