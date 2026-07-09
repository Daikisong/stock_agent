# Source Lineage Repair Audit - 2026-07-05

이 문서는 source route 때문에 버려진 claim 후보를 전수 집계한다.

쉬운 예: 문장 자체는 `ARR 성장`처럼 맞게 뽑혔는데, URL이 검증된 증권사 원본 리포트로 인정되지 않아 점수 근거에서 탈락한 경우를 따로 모은다.

## Summary

- raw_assertion_rejection_count: `2716`
- lineage_rejection_count: `695`
- route_only_candidate_count: `31`
- current_code_verified_retry_candidate_count: `0`
- source_lineage_feedback_retry_execution_count: `0`
- reason_counts: `{"source_class_document_type_mismatch": 203, "source_lineage_unverified_original": 588, "source_provider_document_type_mismatch": 558, "source_task_provider_error_score_block": 18}`
- source_class_counts: `{"BrokerReportPublicPDF": 472, "CompanyGuide": 29, "CompanyNewsroom": 85, "IndustryMedia": 19, "TrustedNews": 90}`

## Archetypes

| archetype | lineage rejected | route-only candidates | current-code retry candidates | top domains |
|---|---:|---:|---:|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 3 | 2 | 0 | dart.fss.or.kr:3 |
| C02_POWER_GRID_DATACENTER_CAPEX | 77 | 0 | 0 | genians.co.kr:22, oksiri.com:19, paxnet.co.kr:18, snkpress.kr:18 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 36 | 0 | 0 | imgstock.naver.com:36 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 13 | 0 | 0 | comp.wisereport.co.kr:13 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 22 | 1 | 0 | s-journal.co.kr:22 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 60 | 19 | 0 | contents.premium.naver.com:7, edaily.co.kr:19, imgstock.naver.com:13, paxnet.co.kr:21 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 3 | 0 | 0 | dart.fss.or.kr:3 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 15 | 6 | 0 | dart.fss.or.kr:2, paxnet.co.kr:13 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 27 | 0 | 0 | hohostock.co.kr:27 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 16 | 0 | 0 | securities.miraeasset.com:16 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 28 | 0 | 0 | biztribune.co.kr:13, securities.miraeasset.com:15 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 22 | 0 | 0 | securities.miraeasset.com:22 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 16 | 0 | 0 | dart.fss.or.kr:3, paxnet.co.kr:13 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 15 | 0 | 0 | securities.miraeasset.com:15 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 28 | 0 | 0 | securities.miraeasset.com:28 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 35 | 0 | 0 | paxnet.co.kr:18, snumidas.com:17 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 109 | 0 | 0 | buffettlab.co.kr:14, securities.miraeasset.com:95 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 45 | 0 | 0 | securities.miraeasset.com:45 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 42 | 1 | 0 | imgstock.naver.com:29, shinyoung.com:13 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 38 | 1 | 0 | imgstock.naver.com:11, money2.daishin.com:19, sktelecom.com:8 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 21 | 0 | 0 | hanmiglobal.com:9, thinkpool.com:12 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 22 | 1 | 0 | dart.fss.or.kr:4, file.truefriend.com:18 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 2 | 0 | 0 | dart.fss.or.kr:2 |

## Safety

이 audit의 row는 점수 근거가 아니다. 새 runtime attempt에서 source anchor, direct target, current temporal, accepted primitive mapping을 다시 통과해야 한다.
