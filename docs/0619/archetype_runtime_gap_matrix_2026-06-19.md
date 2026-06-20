# Archetype Runtime Gap Matrix - 2026-06-19

## 목적

삼성전자/SK하이닉스 C06 문제를 전체 아키타입 문제와 분리해서 본다. 결론은 C06만의 문제가 아니다. V12 연구자료는 많은 아키타입에서 "현재 profile이 아직 너무 늦거나, 구조적 winner를 놓치거나, false positive를 만든다"고 기록한다.

쉬운 예:

- C06에서 `HBM sold-out capacity`가 운영 feature로 약하게 들어가는 문제가 있다.
- C01에서는 `수주잔고 -> 매출 -> 마진 -> FCF` bridge가 운영 feature로 약하게 들어갈 수 있다.
- C21에서는 `ROE/PBR + 실제 주주환원 실행`이 valuation label만으로 압축될 수 있다.

## 전체 집계

| scope | rows | positive | counter | profile errors | false positive | missed structural | too late | source proxy only | URL pending |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| global | 12,471 | 1,495 | 2,628 | 6,257 | 3,559 | 317 | 1,680 | 3,723 | 3,906 |
| L2 AI/Semi | 1,384 | 246 | 349 | 805 | 436 | 52 | 216 | 319 | 414 |
| C06 HBM | 229 | 32 | 56 | 150 | 66 | 11 | 36 | 63 | 78 |

해석:

- 연구자료가 누적되면서 C06 weight는 반영됐다.
- 그러나 aggregate는 "현재 운영 profile이 아직 틀리는 행이 많다"고 말한다.
- 특히 `source_proxy_only`와 `evidence_url_pending`이 많아서, 일부 연구축은 production score로 바로 승격되기 어렵다.

## 너무 늦는 아키타입

`current_profile_too_late_count` 상위권이다.

| archetype | rows | symbols | good/bad stage2 | errors | false positive | missed structural | too late | hit rate | bad-entry rate |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 1,023 | 430 | 210/234 | 610 | 336 | 18 | 184 | 0.5163 | 0.4187 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | 38 | 136/46 | 169 | 78 | 4 | 78 | 0.5546 | 0.0873 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | 50 | 122/43 | 192 | 84 | 4 | 77 | 0.7841 | 0.2557 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 411 | 59 | 125/87 | 208 | 125 | 4 | 69 | 0.5721 | 0.1703 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 378 | 67 | 108/67 | 215 | 122 | 8 | 64 | 0.6978 | 0.4011 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 334 | 37 | 98/71 | 176 | 103 | 10 | 63 | 0.5568 | 0.3027 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 38 | 78/45 | 147 | 73 | 11 | 62 | 0.5735 | 0.2353 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 366 | 102 | 125/103 | 243 | 115 | 15 | 61 | 0.6766 | 0.4255 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 478 | 180 | 110/105 | 223 | 132 | 9 | 60 | 0.5779 | 0.3443 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 308 | 58 | 98/56 | 167 | 87 | 8 | 56 | 0.5952 | 0.2679 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | 20 | 91/52 | 141 | 64 | 7 | 56 | 0.5422 | 0.1506 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 377 | 51 | 58/70 | 200 | 99 | 15 | 56 | 0.3654 | 0.1538 |

해석:

- "좋은 신호가 왔는데 운영 profile이 늦게 반응한다"는 문제가 C06만이 아니다.
- C20, C21, C23 같은 winner형 아키타입도 replay가 필요하다.

## 구조적 winner를 놓치는 아키타입

`current_profile_missed_structural_count` 상위권이다.

| archetype | rows | symbols | good/bad stage2 | errors | false positive | missed structural | too late | hit rate | bad-entry rate |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 288 | 89 | 115/43 | 134 | 63 | 21 | 36 | 0.6587 | 0.2814 |
| C02_POWER_GRID_DATACENTER_CAPEX | 277 | 44 | 116/45 | 151 | 77 | 18 | 43 | 0.8683 | 0.3174 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 295 | 88 | 63/56 | 126 | 70 | 18 | 20 | 0.4113 | 0.1631 |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 1,023 | 430 | 210/234 | 610 | 336 | 18 | 184 | 0.5163 | 0.4187 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 366 | 102 | 125/103 | 243 | 115 | 15 | 61 | 0.6766 | 0.4255 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 377 | 51 | 58/70 | 200 | 99 | 15 | 56 | 0.3654 | 0.1538 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 305 | 77 | 86/57 | 175 | 123 | 14 | 49 | 0.6933 | 0.4533 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 473 | 299 | 92/180 | 278 | 220 | 13 | 42 | 0.3833 | 0.5784 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | 58 | 82/42 | 150 | 66 | 11 | 36 | 0.6124 | 0.2868 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 324 | 96 | 80/69 | 157 | 104 | 11 | 32 | 0.5915 | 0.2317 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 38 | 78/45 | 147 | 73 | 11 | 62 | 0.5735 | 0.2353 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 259 | 52 | 90/62 | 131 | 83 | 11 | 31 | 0.6144 | 0.3922 |

해석:

- C06는 상위권이지만 1등은 아니다.
- C01/C02/C05는 계약/수주/마진/FCF bridge가 운영 feature로 빠질 위험이 크다.
- C09/C10은 HBM/장비 theme와 실제 order/revenue bridge를 구분하는 feature가 중요하다.

## false positive가 많은 아키타입

`current_profile_false_positive_count` 상위권이다.

| archetype | rows | symbols | good/bad stage2 | errors | false positive | missed structural | too late | hit rate | bad-entry rate |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 1,023 | 430 | 210/234 | 610 | 336 | 18 | 184 | 0.5163 | 0.4187 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 715 | 394 | 127/170 | 333 | 232 | 1 | 41 | 0.5065 | 0.5130 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 473 | 299 | 92/180 | 278 | 220 | 13 | 42 | 0.3833 | 0.5784 |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 619 | 326 | 129/73 | 278 | 153 | 9 | 19 | 0.6106 | 0.3894 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 478 | 180 | 110/105 | 223 | 132 | 9 | 60 | 0.5779 | 0.3443 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 411 | 59 | 125/87 | 208 | 125 | 4 | 69 | 0.5721 | 0.1703 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 305 | 77 | 86/57 | 175 | 123 | 14 | 49 | 0.6933 | 0.4533 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 378 | 67 | 108/67 | 215 | 122 | 8 | 64 | 0.6978 | 0.4011 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 366 | 102 | 125/103 | 243 | 115 | 15 | 61 | 0.6766 | 0.4255 |
| C11_BATTERY_ORDERBOOK_RERATING | 286 | 75 | 94/65 | 175 | 108 | 10 | 47 | 0.6471 | 0.3647 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 324 | 96 | 80/69 | 157 | 104 | 11 | 32 | 0.5915 | 0.2317 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 334 | 37 | 98/71 | 176 | 103 | 10 | 63 | 0.5568 | 0.3027 |

해석:

- Green recall만 올리면 false positive가 폭발할 수 있다.
- 그래서 패치 방향은 "Green 기준 완화"가 아니라 "연구축을 정확히 feature로 연결"이어야 한다.

## 다음 전면조사 우선순위

1. C06 historical replay
   - SK하이닉스 성공 행과 삼성전자 false-positive 행을 같은 runner로 재생한다.
2. C01/C02/C05 parser-feature bridge
   - 계약금액, 납기, 수주잔고, RPO, 마진, FCF 연결을 runtime score로 확인한다.
3. C09/C10 theme-to-order bridge
   - AI/HBM 단어와 실제 고객 order/revenue bridge를 분리한다.
4. C20/C21/C22 winner replay
   - 소비재/금융/보험 winner가 valuation label만으로 늦게 잡히는지 확인한다.
5. R13 guardrail replay
   - recall을 올리는 패치가 high-MAE false positive를 늘리지 않는지 확인한다.

투자 권고가 아니라 파이프라인 진단 기록이다.
