---
fixture_id: e2r_phase2_mandatory_golden
expected_case_count: 6
---

# Phase 2 mandatory golden research

The machine-readable rows below are the source of truth. This narrative URL
must not be attached to every case: https://example.invalid/file-wide-only

```jsonl
{"row_type":"case","case_id":"GOLDEN_C06_HBM","symbol":"000660","company_name":"SK하이닉스","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","classification":"positive","case_role":"structural_success","trigger_date":"2024-04-24","evidence_url":"https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/","evidence_summary":"HBM 수요와 실적 가시성을 연결한 당시 공개 보도","declared_source_quality":"URL_PRESENT_UNVERIFIED"}
{"row_type":"trigger","case_id":"GOLDEN_C06_HBM","trigger_id":"GOLDEN_C06_T01_FULL","symbol":"000660","company_name":"SK하이닉스","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","trigger_type":"capacity_visibility","trigger_date":"2024-04-24","entry_date":"2024-04-24","evidence_family":"capacity_and_customer"}
{"row_type":"case","case_id":"GOLDEN_C08_SOCKET","symbol":"058470","company_name":"리노공업","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","classification":"positive","case_role":"customer_quality","trigger_date":"2024-02-01","evidence_url":"https://www.leeno.com/","evidence_summary":"회사 공식 사이트에 제품·고객 품질 관련 자료가 존재하는지 검증할 URL","declared_source_quality":"URL_PRESENT_UNVERIFIED"}
{"row_type":"trigger","case_id":"GOLDEN_C08_SOCKET","trigger_id":"GOLDEN_C08_T01_FULL","symbol":"058470","company_name":"리노공업","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","trigger_type":"customer_quality","trigger_date":"2024-02-01","entry_date":"2024-02-01","evidence_family":"customer_quality"}
{"row_type":"case","case_id":"GOLDEN_C15_SPREAD","symbol":"010950","company_name":"S-Oil","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","classification":"positive","case_role":"spread_cycle","trigger_date":"2022-04-27","evidence_url":"https://www.s-oil.com/en/relation/ir/FinancialHighlight.aspx","evidence_summary":"정제마진과 실적 연결을 검증할 회사 공식 IR URL","declared_source_quality":"URL_PRESENT_UNVERIFIED"}
{"row_type":"trigger","case_id":"GOLDEN_C15_SPREAD","trigger_id":"GOLDEN_C15_T01_FULL","symbol":"010950","company_name":"S-Oil","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","trigger_type":"spread_margin_bridge","trigger_date":"2022-04-27","entry_date":"2022-04-27","evidence_family":"spread_and_margin"}
{"row_type":"case","case_id":"GOLDEN_C17_PROXY","symbol":"004000","company_name":"롯데정밀화학","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","classification":"positive","case_role":"source_repair","trigger_date":"2021-09-01","source_proxy_only":true,"evidence_summary":"과거 연구 요약만 있고 case-level 원문 URL은 아직 없음"}
{"row_type":"trigger","case_id":"GOLDEN_C17_PROXY","trigger_id":"GOLDEN_C17_T01_FULL","symbol":"004000","company_name":"롯데정밀화학","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","trigger_type":"spread_margin_bridge","trigger_date":"2021-09-01","entry_date":"2021-09-01"}
{"row_type":"case","case_id":"GOLDEN_C24_PROXY","symbol":"068270","company_name":"셀트리온","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","classification":"counterexample","case_role":"event_risk_guard","trigger_date":"2023-05-01","source_proxy_only":true,"evidence_summary":"임상 이벤트 결과의 case-level 원문 확인이 필요함"}
{"row_type":"trigger","case_id":"GOLDEN_C24_PROXY","trigger_id":"GOLDEN_C24_T01_FULL","symbol":"068270","company_name":"셀트리온","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","trigger_type":"trial_event_risk","trigger_date":"2023-05-01","entry_date":"2023-05-01"}
{"row_type":"case","case_id":"GOLDEN_C28_PROXY","symbol":"053800","company_name":"안랩","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","classification":"guard","case_role":"retention_guard","trigger_date":"2022-03-21","source_proxy_only":true,"evidence_summary":"계약 유지율 원문이 없어 source repair가 필요함"}
{"row_type":"trigger","case_id":"GOLDEN_C28_PROXY","trigger_id":"GOLDEN_C28_T01_FULL","symbol":"053800","company_name":"안랩","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","trigger_type":"contract_retention","trigger_date":"2022-03-21","entry_date":"2022-03-21"}
```

## Deferred Coding Agent Handoff Prompt

The following is an instruction example, not historical evidence.

```jsonl
{"row_type":"case","case_id":"MUST_NOT_BE_PARSED","symbol":"999999","company_name":"가짜회사","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","trigger_date":"2099-01-01"}
```
