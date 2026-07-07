# Source Lineage Repair Audit - 2026-07-05

이 문서는 source route 때문에 버려진 claim 후보를 전수 집계한다.

쉬운 예: 문장 자체는 `ARR 성장`처럼 맞게 뽑혔는데, URL이 검증된 증권사 원본 리포트로 인정되지 않아 점수 근거에서 탈락한 경우를 따로 모은다.

## Summary

- raw_assertion_rejection_count: `2502`
- lineage_rejection_count: `524`
- route_only_candidate_count: `29`
- current_code_verified_retry_candidate_count: `50`
- source_lineage_feedback_retry_execution_count: `0`
- reason_counts: `{"source_class_document_type_mismatch": 135, "source_lineage_unverified_original": 413, "source_provider_document_type_mismatch": 417, "source_task_provider_error_score_block": 32}`
- source_class_counts: `{"BrokerReportPublicPDF": 395, "CompanyGuide": 31, "CompanyNewsroom": 49, "TrustedNews": 49}`

## Archetypes

| archetype | lineage rejected | route-only candidates | current-code retry candidates | top domains |
|---|---:|---:|---:|---|
| C02_POWER_GRID_DATACENTER_CAPEX | 8 | 0 | 0 | genians.co.kr:8 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 36 | 0 | 0 | paxnet.co.kr:8, redhorseblog.co.kr:13, rindir.co.kr:15 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 5 | 1 | 0 | dart.fss.or.kr:5 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 23 | 1 | 14 | dart.fss.or.kr:5, eugenefn.com:14, valueline.co.kr:4 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 55 | 16 | 0 | dart.fss.or.kr:2, imgstock.naver.com:9, invest.kiwoom.com:15, paxnet.co.kr:29 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 5 | 0 | 0 | dart.fss.or.kr:4, deepsearch.com:1 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 25 | 0 | 0 | dart.fss.or.kr:4, thinkpool.com:21 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 4 | 0 | 0 | dart.fss.or.kr:4 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 39 | 0 | 0 | securities.miraeasset.com:39 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 32 | 0 | 0 | dart.fss.or.kr:3, paxnet.co.kr:29 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 14 | 0 | 0 | imgstock.naver.com:6, paxnet.co.kr:8 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 8 | 0 | 0 | file.myasset.com:8 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 24 | 0 | 0 | home.imeritz.com:19, medicaltimes.com:5 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 1 | 1 | 0 | file.myasset.com:1 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 23 | 0 | 10 | securities.miraeasset.com:23 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 77 | 0 | 0 | imgstock.naver.com:40, money2.daishin.com:11, securities.miraeasset.com:24, statista.com:2 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 22 | 0 | 0 | securities.miraeasset.com:22 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 26 | 4 | 26 | bbn.kiwoom.com:12, securities.miraeasset.com:14 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 61 | 6 | 0 | emoderntimes.com:22, equity.co.kr:19, securities.miraeasset.com:20 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 16 | 0 | 0 | imgstock.naver.com:16 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 16 | 0 | 0 | businesspost.co.kr:16 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 4 | 0 | 0 | dart.fss.or.kr:4 |

## Safety

이 audit의 row는 점수 근거가 아니다. 새 runtime attempt에서 source anchor, direct target, current temporal, accepted primitive mapping을 다시 통과해야 한다.
