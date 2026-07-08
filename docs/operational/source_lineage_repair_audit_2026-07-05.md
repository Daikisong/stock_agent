# Source Lineage Repair Audit - 2026-07-05

이 문서는 source route 때문에 버려진 claim 후보를 전수 집계한다.

쉬운 예: 문장 자체는 `ARR 성장`처럼 맞게 뽑혔는데, URL이 검증된 증권사 원본 리포트로 인정되지 않아 점수 근거에서 탈락한 경우를 따로 모은다.

## Summary

- raw_assertion_rejection_count: `2692`
- lineage_rejection_count: `464`
- route_only_candidate_count: `37`
- current_code_verified_retry_candidate_count: `0`
- source_lineage_feedback_retry_execution_count: `0`
- reason_counts: `{"source_class_document_type_mismatch": 127, "source_lineage_unverified_original": 335, "source_provider_document_type_mismatch": 355, "source_task_provider_error_score_block": 2}`
- source_class_counts: `{"BrokerReportPublicPDF": 320, "CompanyGuide": 25, "CompanyNewsroom": 26, "IndustryMedia": 42, "TrustedNews": 49, "UNKNOWN": 2}`

## Archetypes

| archetype | lineage rejected | route-only candidates | current-code retry candidates | top domains |
|---|---:|---:|---:|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 34 | 15 | 0 | paxnet.co.kr:34 |
| C02_POWER_GRID_DATACENTER_CAPEX | 43 | 3 | 0 | genians.co.kr:10, snkpress.kr:15, thinkpool.com:18 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 11 | 0 | 0 | bnkfn.co.kr:43674:10, files-scs.pstatic.net:1 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 15 | 0 | 0 | rindir.co.kr:15 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 26 | 8 | 0 | paxnet.co.kr:17, topstarnews.net:9 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 34 | 7 | 0 | thinkpool.com:34 |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 10 | 0 | 0 | deepsearch.com:2, kr.tradingview.com:4, valueline.co.kr:4 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 2 | 0 | 0 | bujane.co.kr:2 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 14 | 0 | 0 | dart.fss.or.kr:4, zdnet.co.kr:10 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 17 | 0 | 0 | paxnet.co.kr:17 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 37 | 0 | 0 | ceomagazine.co.kr:15, iprovest.com:14, securities.miraeasset.com:8 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 28 | 0 | 0 | securities.miraeasset.com:28 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 18 | 0 | 0 | paxnet.co.kr:18 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 26 | 0 | 0 | home.imeritz.com:14, invest.kiwoom.com:12 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 16 | 0 | 0 | securities.miraeasset.com:16 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 42 | 0 | 0 | dart.fss.or.kr:4, paxnet.co.kr:22, securities.miraeasset.com:16 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 26 | 0 | 0 | securities.miraeasset.com:26 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 15 | 0 | 0 | securities.miraeasset.com:15 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 12 | 2 | 0 | shinyoung.com:12 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 16 | 2 | 0 | kind.krx.co.kr:16 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 11 | 0 | 0 | imgstock.naver.com:11 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 11 | 0 | 0 | imnews.imbc.com:11 |

## Safety

이 audit의 row는 점수 근거가 아니다. 새 runtime attempt에서 source anchor, direct target, current temporal, accepted primitive mapping을 다시 통과해야 한다.
