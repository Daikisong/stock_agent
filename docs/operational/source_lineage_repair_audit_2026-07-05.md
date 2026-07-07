# Source Lineage Repair Audit - 2026-07-05

이 문서는 source route 때문에 버려진 claim 후보를 전수 집계한다.

쉬운 예: 문장 자체는 `ARR 성장`처럼 맞게 뽑혔는데, URL이 검증된 증권사 원본 리포트로 인정되지 않아 점수 근거에서 탈락한 경우를 따로 모은다.

## Summary

- raw_assertion_rejection_count: `2478`
- lineage_rejection_count: `664`
- route_only_candidate_count: `10`
- current_code_verified_retry_candidate_count: `0`
- source_lineage_feedback_retry_execution_count: `0`
- reason_counts: `{"source_class_document_type_mismatch": 194, "source_lineage_unverified_original": 485, "source_provider_document_type_mismatch": 531, "source_task_provider_error_score_block": 61}`
- source_class_counts: `{"BrokerReportPublicPDF": 482, "CompanyGuide": 70, "CompanyNewsroom": 29, "IndustryMedia": 20, "KIND": 14, "TrustedNews": 49}`

## Archetypes

| archetype | lineage rejected | route-only candidates | current-code retry candidates | top domains |
|---|---:|---:|---:|---|
| C02_POWER_GRID_DATACENTER_CAPEX | 33 | 1 | 0 | genians.co.kr:13, snkpress.kr:20 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 28 | 0 | 0 | securities.miraeasset.com:13, snumidas.com:15 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 29 | 0 | 0 | redhorseblog.co.kr:13, rindir.co.kr:16 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 17 | 0 | 0 | contents.premium.naver.com:3, securities.miraeasset.com:14 |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 3 | 0 | 0 | dart.fss.or.kr:3 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 5 | 0 | 0 | dart.fss.or.kr:5 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 27 | 5 | 0 | dart.fss.or.kr:3, paxnet.co.kr:24 |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 40 | 0 | 0 | money2.daishin.com:40 |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 17 | 0 | 0 | deepsearch.com:1, paxnet.co.kr:16 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 29 | 0 | 0 | hohostock.co.kr:29 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 20 | 0 | 0 | stockhandbook.blog:20 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 19 | 4 | 0 | bnkfn.co.kr:11, securities.miraeasset.com:8 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 34 | 0 | 0 | dart.fss.or.kr:4, securities.miraeasset.com:7, stock.pstatic.net:23 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 45 | 0 | 0 | securities.miraeasset.com:45 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 19 | 0 | 0 | imgstock.naver.com:14, securities.miraeasset.com:5 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 56 | 0 | 0 | alphabiz.co.kr:15, home.imeritz.com:22, mt.co.kr:14, news1.kr:5 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 9 | 0 | 0 | imgstock.naver.com:9 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 103 | 0 | 0 | dart.fss.or.kr:3, money2.daishin.com:10, paxnet.co.kr:10, securities.miraeasset.com:77 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 25 | 0 | 0 | cjnews.cj.net:10, securities.miraeasset.com:15 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 14 | 0 | 0 | shinyoung.com:14 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 9 | 0 | 0 | securities.miraeasset.com:9 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 30 | 0 | 0 | imgstock.naver.com:16, stock.pstatic.net:14 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 18 | 0 | 0 | money2.daishin.com:18 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 22 | 0 | 0 | jusikai.com:10, paxnet.co.kr:12 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 13 | 0 | 0 | dart.fss.or.kr:2, imgstock.naver.com:11 |

## Safety

이 audit의 row는 점수 근거가 아니다. 새 runtime attempt에서 source anchor, direct target, current temporal, accepted primitive mapping을 다시 통과해야 한다.
