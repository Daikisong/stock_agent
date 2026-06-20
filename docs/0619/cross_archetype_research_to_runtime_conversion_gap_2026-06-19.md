# Cross-Archetype Research to Runtime Conversion Gap - 2026-06-19

## 결론

삼전/하닉 문제는 HBM parser 하나만의 문제가 아니다.

현재 구조는 세 단계로 나뉜다.

1. 연구자료는 Green/반례를 많이 쌓았다.
2. 그 연구자료는 36개 canonical archetype의 7개 component weight로는 들어갔다.
3. 하지만 연구에서 나온 세부 score axis와 guardrail은 대부분 runtime parser/feature/gate field로 아직 연결되지 않았다.

쉬운 예:

- 연구자료: "하닉은 HBM sold-out capacity + Nvidia 고객 + revision visibility라 Green."
- 현재 runtime: "내가 아는 field는 `hbm_capacity_constraint`, `hbm_capacity_pre_sold`, `customer_preorder_or_allocation`, `opm_expansion_pctp`, `fcf_growth_pct`다."
- 변환 결과: 일부만 들어가서 `domain_specific_evidence_score=80`은 되지만 `contract_quality=0`, `capa_constraint=0`, `fcf_quality_score=0`이 남고 Green 총점까지 못 간다.

즉 문제는 "연구가 없었다"가 아니라 "연구축이 운영 점수 재료로 번역되지 않았다"다.

## 확인한 파일

이번 조사는 다음 현재 파일을 기준으로 했다.

| source | 용도 |
| --- | --- |
| `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` | 대표 trigger, Green/false/missed/late 분포 |
| `data/e2r/calibration/v12/v12_extracted_triggers_raw.jsonl` | stage별 evidence field |
| `data/e2r/calibration/v12/v12_raw_shadow_weight_rows.jsonl` | 연구가 제안한 shadow axis/guardrail |
| `configs/e2r_archetype_weight_profile_v2_2.json` | runtime archetype weight |
| `src/e2r/features.py` | runtime field -> score 변환 |
| `src/e2r/sector_profiles.py` | sector profile과 preferred field |
| `src/e2r/staging.py` | Green gate |

참고로 현재 `docs/round`는 `achieve` 아래에 완료 연구 md가 있고, `achieve`를 제외한 활성 `.md` 연구자료는 없다. 그래서 누적 상태 검증은 calibration JSONL을 authoritative source로 봤다.

## 큰 숫자

| 항목 | 값 | 의미 |
| --- | ---: | --- |
| representative trigger rows | 12,471 | 누적 대표 장부 규모 |
| runtime archetype weight profiles | 36 | C01-C32 + R13 guardrail scope까지 weight는 있음 |
| runtime sector profiles | 9 | feature/profile은 weight보다 훨씬 적음 |
| raw shadow weight rows | 3,741 | 연구가 제안한 추가 axis/guardrail |
| production changed shadow rows | 0 | shadow rows 자체는 운영 scoring 변경으로 표시되지 않음 |
| unique shadow axes | 2,248 | 연구 세부축/가드레일 이름 |
| exact runtime field matches | 4 | `capital_allocation`, `earnings_visibility`, `information_confidence`, `valuation_rerating`뿐 |

중요한 해석:

- 36개 아키타입별 weight는 runtime에 있다.
- 하지만 연구가 계속 만든 `margin_bridge_score`, `customer_quality_score`, `reserve_quality_score`, `policy_route_congruence_score`, `high_MAE_guardrail` 같은 세부축은 대부분 runtime field명이 아니다.
- 그래서 weight가 있어도 입력 field가 비면 점수는 안 오른다.

쉬운 예:

- C22 보험 weight는 `valuation`, `capital`, `visibility`를 크게 본다.
- 연구는 `CSM`, `K-ICS`, `reserve_quality`, `shareholder_return_quality`를 봤다.
- runtime이 그걸 field로 못 읽으면 그냥 generic `valuation_rerating`, `capital_allocation` 재료만 남는다.

## Green Gate가 요구하는 것

`src/e2r/staging.py`의 Green은 OR가 아니라 AND 조건이다.

| gate | 요구 |
| --- | --- |
| total | `stage3_green_total_min` 이상 |
| EPS/FCF | component threshold 이상 |
| visibility | component threshold 이상 |
| bottleneck | component threshold 이상 |
| mispricing | component threshold 이상 |
| valuation | component threshold 이상 |
| revision | `stage3_green_revision_min` 이상 |
| structural visibility | `stage3_green_structural_visibility_min` 이상 |
| contract-required archetype | `contract_quality >= 45` |
| one-off shortage | 70 미만 |
| red-team | LOW |

그래서 "전망이 미쳤다" 하나로는 Green이 안 된다.

쉬운 예:

- EPS/FCF가 20점 만점이어도 revision source가 비면 Green 실패다.
- HBM 수요가 강해도 capacity/customer/FCF bridge가 field로 안 들어오면 bottleneck/visibility가 부족하다.
- 정책 이벤트가 강해도 회사 매출/현금흐름으로 연결되는 bridge가 없으면 C31은 Green으로 못 간다.

## 하닉 C06에서 실제로 깎인 위치

하닉 2024-04-30 replay는 이미 별도 문서에 남겼고, 여기서는 전체 구조 안에서 다시 놓는다.

| component | raw | C06 weighted | Green effective threshold | 결과 |
| --- | ---: | ---: | ---: | --- |
| EPS/FCF | 20.0000 | 24.0000 | 20.4000 | 통과 |
| visibility | 15.1502 | 15.9077 | 15.7500 | 통과 |
| bottleneck | 11.6339 | 11.0522 | 14.2500 | 실패 |
| mispricing | 12.8520 | 12.8520 | 10.0000 | 통과 |
| valuation | 12.3390 | 9.8712 | 8.0000 | 통과 |
| total | 75.0761 raw | 76.7639 | 87.0000 | 실패 |

여기서 중요한 점:

- C06 weight는 하닉 점수를 깎지 않았다. 오히려 `75.0761 -> 76.7639`로 올렸다.
- Green 실패 원인은 total과 bottleneck이다.
- bottleneck을 망친 직접 이유는 연구 문장의 capacity/customer lock이 runtime field로 약하게 들어간 것이다.

하위 진단:

| diagnostic | 값 | 의미 |
| --- | ---: | --- |
| `revision_score` | 100.0 | revision 방향은 잡힘 |
| `domain_specific_evidence_score` | 80.0 | HBM 관련성은 잡힘 |
| `sector_bottleneck_score` | 46.0 | Green 병목으로는 약함 |
| `contract_quality` | 0.0 | 장기계약/취소불가/선수금 field 없음 |
| `backlog_rpo_visibility` | 15.0 | 물량 lock이 약하게만 반영 |
| `capa_constraint` | 0.0 | CAPA/packaging 병목 field로 안 들어감 |
| `fcf_quality_score` | 0.0 | FCF source 없음 |

정답 Green 날짜 replay도 같은 결론이다.

| date | runtime stage | score | failed gates |
| --- | --- | ---: | --- |
| 2024-04-25 | Stage3-Yellow | 76.0596 | `failed_stage3_total_score`, `failed_stage3_visibility`, `failed_stage3_bottleneck` |
| 2024-04-26 | Stage3-Yellow | 76.0596 | `failed_stage3_total_score`, `failed_stage3_visibility`, `failed_stage3_bottleneck` |

두 날짜 모두 research/web/official flow는 실행됐고, `revision_score=100`, `domain_specific_evidence_score=80`, `structural_visibility_quality=70.7335`였다. 그런데 `contract_quality=0`, `capa_constraint=0`, `fcf_quality_score=0`, `backlog_rpo_visibility=15`라서 Green까지 가지 못했다.

연구 장부상 C06 Green은 있었다.

| 항목 | 값 |
| --- | ---: |
| C06 rows | 229 |
| C06 trigger_type Stage3-Green | 9 |
| C06 strict weight-usable Green | 7 |
| C06 false positive | 66 |
| C06 missed structural | 11 |
| C06 too late | 36 |

따라서 "하닉은 Green으로 잡혔어야 한다"는 연구 장부 기준으로 맞다.  
다만 C06에는 false positive도 66개라 Green 기준을 무작정 낮추면 안 된다.

## 삼전은 하닉과 다른 문제

삼성 2024-04-30은 Green gate에서 낮게 평가된 것이 아니라 후보 승격 전 cheap scan에서 빠졌다.

| symbol | cheap total | next layer | financial score | reason |
| --- | ---: | --- | ---: | --- |
| SK하이닉스 | 34.75 | event_search | 95.0 | OP turnaround, OPM expansion, FCF turnaround |
| 삼성전자 | 6.25 | none | 0.0 | price near high only |

삼성 재무 실제값:

| period | OP | OPM | FCF |
| --- | ---: | ---: | ---: |
| 2023Q4 | 28,000 | 4.2 | 15,000 |
| 2024Q1 | 66,000 | 9.2 | 54,000 |

삼성은 OP가 크게 뛰었지만 이미 흑자였기 때문에 `FIN_OP_TURNAROUND`가 아니다. FCF도 이미 양수라 `FIN_FCF_TURNAROUND`가 아니다. OPM +5.0%p는 float 경계 문제로 빠질 수 있다.

즉:

- 하닉 문제: 후보는 들어왔고 Yellow까지 갔는데 Green 변환이 약함.
- 삼성 문제: 2024-04-30 기준 cheap scan 후보 승격부터 약함.

## 전체 아키타입 분포

아래 표는 representative trigger file의 현재 상태다. `Green`은 `trigger_type`에 Green이 있는 row 기준이고, `strict`는 `usable_for_weight_calibration=true`인 Green row다.

| archetype | rows | Green | strict Green | false | missed | late | source proxy | URL pending | runtime profile coverage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 288 | 9 | 6 | 63 | 21 | 36 | 68 | 79 | POWER_EQUIPMENT |
| C02_POWER_GRID_DATACENTER_CAPEX | 277 | 5 | 4 | 77 | 18 | 43 | 66 | 50 | POWER_EQUIPMENT |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 267 | 6 | 6 | 47 | 1 | 15 | 95 | 121 | DEFENSE |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 220 | 0 | 0 | 60 | 4 | 12 | 83 | 84 | GENERIC/partial |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 295 | 10 | 8 | 70 | 18 | 20 | 74 | 71 | GENERIC/partial |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | 9 | 7 | 66 | 11 | 36 | 63 | 78 | MEMORY_HBM if parsed |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 237 | 3 | 0 | 76 | 4 | 33 | 83 | 76 | MEMORY_HBM if parsed |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 247 | 10 | 3 | 56 | 8 | 37 | 47 | 118 | MEMORY_HBM/GENERIC |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 305 | 5 | 0 | 123 | 14 | 49 | 63 | 73 | MEMORY_HBM/GENERIC |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 366 | 4 | 4 | 115 | 15 | 61 | 63 | 69 | MEMORY_HBM/GENERIC |
| C11_BATTERY_ORDERBOOK_RERATING | 286 | 2 | 1 | 108 | 10 | 47 | 90 | 95 | BATTERY_OVERHEAT if parsed |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 262 | 0 | 0 | 101 | 3 | 26 | 86 | 81 | BATTERY_OVERHEAT if parsed |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 307 | 6 | 6 | 86 | 5 | 22 | 107 | 110 | BATTERY_OVERHEAT if parsed |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 264 | 1 | 1 | 72 | 8 | 46 | 71 | 76 | BATTERY_OVERHEAT if parsed |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 324 | 12 | 9 | 104 | 11 | 32 | 88 | 81 | GENERIC/partial |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 234 | 0 | 0 | 41 | 5 | 11 | 107 | 104 | GENERIC/partial |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 297 | 15 | 5 | 62 | 5 | 26 | 90 | 94 | GENERIC/partial |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 308 | 14 | 2 | 87 | 8 | 56 | 101 | 105 | K_FOOD/K_BEAUTY if parsed |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 223 | 5 | 1 | 56 | 5 | 29 | 92 | 99 | GENERIC/partial |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | 33 | 8 | 84 | 4 | 77 | 76 | 91 | K_FOOD/K_BEAUTY if parsed |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | 37 | 7 | 78 | 4 | 78 | 100 | 123 | no dedicated sector profile |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | 28 | 6 | 64 | 7 | 56 | 127 | 134 | no dedicated sector profile |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 30 | 16 | 73 | 11 | 62 | 74 | 87 | no dedicated sector profile |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 253 | 7 | 4 | 37 | 7 | 45 | 117 | 130 | no dedicated sector profile |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 259 | 12 | 4 | 83 | 11 | 31 | 91 | 94 | no dedicated sector profile |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 334 | 20 | 3 | 103 | 10 | 63 | 89 | 106 | AI_INFRA sometimes, otherwise generic |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 263 | 12 | 3 | 58 | 1 | 47 | 84 | 78 | no dedicated sector profile |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 285 | 14 | 4 | 90 | 11 | 49 | 105 | 84 | no dedicated sector profile |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 411 | 10 | 3 | 125 | 4 | 69 | 163 | 164 | no dedicated sector profile |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 377 | 3 | 0 | 99 | 15 | 56 | 149 | 156 | no dedicated sector profile |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 478 | 12 | 7 | 132 | 9 | 60 | 156 | 174 | no dedicated sector profile |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 378 | 2 | 1 | 122 | 8 | 64 | 116 | 114 | no dedicated sector profile |

해석:

- Green이 많은 아키타입은 C20, C21, C22, C23이다.
- 그런데 C21/C22/C23/C25/C28/C29/C30/C31/C32는 전용 sector profile이 없다.
- source proxy와 URL pending도 많다. 그래서 Green threshold를 낮추는 식의 단순 해결은 false positive를 같이 올린다.

## Green 연구는 무엇을 봤나

Green row의 evidence field는 대체로 다음을 반복한다.

| archetype group | Green evidence core | runtime conversion gap |
| --- | --- | --- |
| C01/C02/C03 infra/defense | order/backlog, delivery visibility, margin bridge, public disclosure | 일부 POWER/DEFENSE profile은 있으나 margin/FCF/delivery freshness guard가 부족 |
| C06 HBM | customer/order quality, capacity/volume route, durable customer confirmation, revision, financial visibility | capacity booked/sold-out이 `capa_constraint`, `backlog_rpo_visibility`, `contract_quality`로 약하게 변환 |
| C07/C08/C10 semi equipment | order/revenue conversion, customer quality, repeat demand, revision | 장비 order quality와 customer qualification이 generic HBM field로 압축 |
| C18/C20 consumer export | confirmed revision, financial visibility, margin bridge, repeat order, global channel | channel/reorder/sell-through가 있을 때만 profile이 먹고, 재고/채널 품질 guard는 약함 |
| C21 financial | ROE/PBR, capital return, credit/reserve quality, low red-team risk | 금융 전용 profile 없음. `roe`, `pbr` 일부만 valuation으로 들어감 |
| C22 insurance | reserve quality, rate cycle, CSM/K-ICS, capital return | 보험 전용 profile 없음. CSM/K-ICS/loss ratio field가 runtime 핵심에 없음 |
| C23/C24/C25 bio/medical | approval/trial event, commercialization bridge, royalty/reimbursement, partner quality | 바이오 전용 profile 없음. event headline과 revenue/royalty conversion 분리가 부족 |
| C26/C27/C28 platform/software | monetization, operating leverage, ARR/RPO/retention, contract retention | AI infra 일부만 있고 SaaS/security/content 전용 field 부족 |
| C29 mobility | volume/mix/margin/cash bridge, capital return | mobility 전용 profile 없음 |
| C30 construction/PF | PF repair, liquidity, balance-sheet cash bridge, margin/revision | 전용 profile 없음. credit/PF bridge가 shadow-only |
| C31 policy | direct policy-to-company cash route, subsidy capture, localization route | policy headline과 cashflow bridge 분리 부족 |
| C32 governance | minority cash path, tender cap, control premium, NAV/FCF/shareholder return | event premium cap/현금화 경로가 shadow-only |

## Shadow Axis가 운영 점수로 안 들어간 증거

`v12_raw_shadow_weight_rows.jsonl` 기준 상위 shadow axis:

| axis | count | runtime exact match |
| --- | ---: | --- |
| `stage2_required_bridge` | 207 | no |
| `local_4b_watch_guard` | 195 | no |
| `high_MAE_guardrail` | 131 | no |
| `full_4b_requires_non_price_evidence` | 14 | no |
| `hard_4c_thesis_break_routes_to_4c` | 10 | no |
| `cross_archetype_data_quality_repair_before_patch` | 8 | no |
| `share_count_drift_independent_weight_reduction` | 8 | no |
| `C29_volume_mix_margin_cash_bridge_required` | 8 | no |
| `C30_PF_liquidity_backlog_cash_bridge_required` | 6 | no |
| `C32_MINORITY_CASH_PATH_REQUIRED` | 6 | no |
| `C32_TENDER_PRICE_CAP_LOCAL_4B` | 6 | no |
| `cross_archetype_Green_requires_exact_non_price_bridge` | 6 | no |
| `C08_CUSTOMER_QUALIFICATION_REORDER_MARGIN_BRIDGE_REQUIRED` | 6 | no |

이 axis들은 이름 그대로 "운영에서 이런 bridge/guard가 필요하다"는 연구 결과다. 하지만 현재는 shadow-only라 실제 `StageClassifier`나 feature field로 직접 쓰이지 않는다.

쉬운 예:

- 연구: "C30은 PF repair cash bridge 없으면 Stage2/Green 막아야 한다."
- runtime: C30 전용 profile 없음. generic visibility/valuation으로 압축.
- 결과: 좋은 C30도 못 올리고, 나쁜 C30도 다른 evidence가 있으면 애매하게 올라올 수 있다.

## 왜 weight만으로는 부족한가

`configs/e2r_archetype_weight_profile_v2_2.json`에는 C06/C21/C22/C23/C28 같은 weight가 들어 있다.

예:

| archetype | EPS/FCF | visibility | bottleneck | valuation | capital | info | policy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| C06 HBM | 24 | 21 | 19 | 12 | 4 | 5 | HBM capacity/customer/revision |
| C21 financial | 15 | 20 | 5 | 25 | 15 | 5 | ROE/PBR/capital return |
| C22 insurance | 12 | 22 | 5 | 24 | 18 | 5 | reserve/rate/capital return |
| C23 bio approval | 12 | 24 | 5 | 10 | 7 | 30 | approval -> revenue/royalty conversion |
| C28 software/security | 20 | 24 | 8 | 14 | 8 | 10 | ARR/retention/margin leverage |

하지만 runtime feature는 결국 다음 7개 component로 점수를 만든다.

- `eps_fcf_explosion`
- `earnings_visibility`
- `bottleneck_pricing`
- `market_mispricing`
- `valuation_rerating`
- `capital_allocation`
- `information_confidence`

그리고 sector metrics는 9개 profile만 가진다.

- GENERIC
- POWER_EQUIPMENT
- DEFENSE
- K_FOOD_EXPORT
- K_BEAUTY_EXPORT
- MEMORY_HBM
- CYCLICAL_SHIPPING
- BATTERY_OVERHEAT
- AI_INFRA_PLATFORM

따라서 C21/C22/C23/C25/C28/C30/C31/C32 같은 Green-heavy 아키타입은 weight는 있어도 전문 field extractor/profile이 없어 generic으로 많이 압축된다.

## 현재 runtime field의 병목

`features.py`가 실제로 강하게 보는 field는 이런 류다.

| runtime score area | 주요 field |
| --- | --- |
| contract quality | `contract_duration_months`, `contract_amount_to_prior_sales`, `prepayment_exists`, `non_cancellable`, `multi_year_contract` |
| backlog/RPO | `order_backlog_to_sales`, `rpo_to_sales`, `record_backlog`, `customer_preorder_or_allocation`, `hbm_capacity_pre_sold` |
| CAPA | `capa_utilization_pct`, `lead_time_months`, `capacity_constraint`, `hbm_capacity_constraint`, `advanced_packaging_bottleneck` |
| pricing | `asp_yoy_pct`, `price_increase_pct`, `high_margin_mix_pct`, `pricing_power_mentioned` |
| revision | numeric `eps_revision_pct`, `op_revision_pct`, `fcf_revision_pct`, `target_price_revision_pct`, or `estimate_upgrade_mentioned` |
| actual conversion | `actual_op_yoy_pct`, `actual_eps_yoy_pct`, `actual_fcf_yoy_pct`, `opm_expansion_pctp`, `fcf_quality_score` |
| evidence confidence | independent consensus, independent consensus revision, date-verified reports/news/disclosure |

이 구조는 제조/수주형 winner에는 어느 정도 맞는다. 하지만 다음에는 부족하다.

- 금융/보험: ROE/PBR, CSM, K-ICS, reserve quality, shareholder return execution
- 바이오: approval quality, partner economics, royalty, reimbursement, trial site/data quality
- 플랫폼/소프트웨어: ARR, NRR, retention, backlog/RPO, seat expansion, cloud/security contract renewal
- 정책/지배구조: direct cash route, subsidy capture, minority shareholder cash path, tender cap
- 건설/PF: PF exposure repair, liquidity, refinancing, legal workout, balance-sheet cash bridge

## 전역 원인 지도

| layer | 지금 문제 | 삼전/하닉에서 보인 증상 | 다른 아키타입 증상 |
| --- | --- | --- | --- |
| candidate funnel | cheap scan이 적자전환/공시/가격 중심 | 삼성 OP 급증이 후보 승격에 약함 | 금융/보험/정책/바이오 event도 후보 전 단계에서 빠질 수 있음 |
| parser | 연구 문장을 normalized field로 못 바꿈 | HBM sold-out/capacity booked가 CAPA/contract/backlog로 약함 | CSM, ARR, royalty, sell-through, PF repair 등 누락 |
| feature compression | 전문축을 7개 component로 압축 | `domain_specific=80`인데 bottleneck final이 낮음 | C21/C22/C23/C28 등이 generic visibility/valuation으로 압축 |
| sector profile | 36 weights 대비 9 profiles | C06은 profile이 있지만 field conversion 약함 | 많은 Green-heavy archetype은 전용 profile 없음 |
| Green gate | AND gate | 하닉 total/bottleneck 실패 | 한 축만 비어도 Green 실패 |
| evidence family | 독립 source family 보수적 | report proxy는 많아도 consensus/news family 약함 | source proxy/url pending이 많아 Green confidence 약함 |
| shadow-only research | 연구축이 운영 field가 아님 | C06 capacity/customer bridge axis가 일부만 반영 | 3,741 shadow rows가 production 변경 아님 |

## 지금 고쳐야 할 방향

단순히 Green total 87을 낮추면 안 된다. false positive가 같이 올라온다.

해야 할 일은 변환부를 늘리는 것이다.

1. C06부터 replay fixture 고정
   - 하닉 positive: 2023-10-27, 2024-02-22, 2024-04-25/26
   - 삼성 false-positive/catch-up guard: 2024-03-20, 2024-05-24, 2024-08-07

2. 연구축 -> runtime field 사전 작성
   - `margin_bridge_score -> opm_expansion_pctp`, `actual_op_yoy_pct`, `actual_fcf_yoy_pct`, `fcf_quality_score`
   - `customer_quality_score -> named customer`, `customer_preorder_or_allocation`, `repeat_purchase`
   - `backlog_visibility_score -> order_backlog_to_sales`, `rpo_to_sales`, `delivery_schedule`
   - `contract_score -> duration`, `amount/sales`, `prepayment`, `non_cancellable`
   - `valuation_repricing_score -> target_multiple_delta`, `per_e`, `pbr_e`, `market_frame_shift`

3. Green-heavy archetype 전용 profile 추가
   - C21 금융
   - C22 보험
   - C23/C24/C25 바이오/의료
   - C27/C28 콘텐츠/보안/SaaS
   - C29 mobility
   - C30 PF/건설
   - C31 정책
   - C32 지배구조

4. shadow axis 승격 규칙 만들기
   - shadow-only row를 곧바로 production에 넣지 않는다.
   - strict usable positive와 counterexample이 같이 있는 axis만 fixture replay로 검증한다.
   - false positive guard와 positive recall을 동시에 통과한 것만 runtime field/gate로 승격한다.

5. score 설명을 개선
   - Green 실패 시 "total 부족"만 말하지 말고 어떤 연구축이 어떤 runtime field에서 0점이 됐는지 보여준다.
   - 예: `HBM capacity booked -> hbm_capacity_pre_sold missing -> capa_constraint 0 -> bottleneck fail`.

## 한 줄 진단

지금 시스템은 "아키타입별로 무엇을 더 중요하게 볼지"는 연구로 배웠다.  
하지만 "연구 문장을 어떤 source-backed runtime field로 번역할지"는 아직 충분히 배우지 못했다.

그래서 하닉처럼 연구 장부상 Green인 케이스도 runtime에서는 Yellow에 머물고, 삼성처럼 후보 단계에서 빠지는 케이스도 생긴다. 같은 구조가 금융, 보험, 바이오, 플랫폼, 정책, 지배구조 아키타입에도 남아 있다.
