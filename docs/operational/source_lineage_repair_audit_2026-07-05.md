# Source Lineage Repair Audit - 2026-07-05

이 문서는 source route 때문에 버려진 claim 후보를 전수 집계한다.

쉬운 예: 문장 자체는 `ARR 성장`처럼 맞게 뽑혔는데, URL이 검증된 증권사 원본 리포트로 인정되지 않아 점수 근거에서 탈락한 경우를 따로 모은다.

## Summary

- raw_assertion_rejection_count: `2529`
- lineage_rejection_count: `657`
- route_only_candidate_count: `27`
- current_code_verified_retry_candidate_count: `0`
- source_lineage_feedback_retry_execution_count: `0`
- reason_counts: `{"source_class_document_type_mismatch": 238, "source_lineage_unverified_original": 450, "source_provider_document_type_mismatch": 461, "source_task_provider_error_score_block": 50}`
- source_class_counts: `{"BrokerReportPublicPDF": 421, "CompanyGuide": 72, "CompanyNewsroom": 60, "IndustryMedia": 46, "TrustedNews": 48, "UNKNOWN": 10}`

## Archetypes

| archetype | lineage rejected | route-only candidates | current-code retry candidates | top domains |
|---|---:|---:|---:|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 3 | 2 | 0 | dart.fss.or.kr:3 |
| C02_POWER_GRID_DATACENTER_CAPEX | 52 | 0 | 0 | dart.fss.or.kr:3, genians.co.kr:12, newspim.com:5, paxnet.co.kr:20 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 13 | 0 | 0 | redhorseblog.co.kr:13 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 13 | 2 | 0 | contents.premium.naver.com:2, dart.fss.or.kr:5, investpension.miraeasset.com:6 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 19 | 0 | 0 | imgstock.naver.com:19 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 28 | 7 | 0 | paxnet.co.kr:19, topstarnews.net:9 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 35 | 9 | 0 | dart.fss.or.kr:4, paxnet.co.kr:14, thinkpool.com:17 |
| C11_BATTERY_ORDERBOOK_RERATING | 18 | 0 | 0 | hankyung.com:18 |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 17 | 0 | 0 | comp.wisereport.co.kr:17 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 39 | 7 | 0 | contents.premium.naver.com:10, dart.fss.or.kr:4, namu.wiki:25 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 51 | 0 | 0 | dart.fss.or.kr:4, paxnet.co.kr:47 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 4 | 0 | 0 | dart.fss.or.kr:4 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 49 | 0 | 0 | securities.miraeasset.com:49 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 18 | 0 | 0 | dart.fss.or.kr:3, paxnet.co.kr:15 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 8 | 0 | 0 | apnews.kr:8 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 7 | 0 | 0 | fetv.co.kr:7 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 53 | 0 | 0 | home.imeritz.com:53 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 1 | 0 | 0 | imgstock.naver.com:1 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 44 | 0 | 0 | dart.fss.or.kr:4, imgstock.naver.com:18, paxnet.co.kr:22 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 84 | 0 | 0 | dart.fss.or.kr:3, money2.daishin.com:11, securities.miraeasset.com:70 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 40 | 0 | 0 | deadline.com:13, newsroom.cj.net:6, securities.miraeasset.com:21 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 25 | 0 | 0 | shinyoung.com:25 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 14 | 0 | 0 | dart.fss.or.kr:14 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 20 | 0 | 0 | businesspost.co.kr:20 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 2 | 0 | 0 | dart.fss.or.kr:2 |

## Safety

이 audit의 row는 점수 근거가 아니다. 새 runtime attempt에서 source anchor, direct target, current temporal, accepted primitive mapping을 다시 통과해야 한다.
