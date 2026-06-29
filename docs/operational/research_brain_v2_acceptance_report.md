# Research Brain v2 Acceptance Report

## 1. Commit

- report_base_commit_sha: bc8e5cd6ee1d4ebece515df43870514c9536bd1e
- final_commit_sha: see `git rev-parse HEAD` after the report commit is checked out
- commit_message: Research Brain v2 운영 라우터와 상태판 구현
- push_status: completed by final git push
- working_tree_status: clean after final push verification

## 2. Tests

- command: `PYTHONPATH=src python -m unittest discover -s tests -v`
- passed: 4573
- failed: 0
- skipped: 0

## 3. Evidence OS regression

- READY 유지 여부: True
- orphan_score_count: 0
- legacy direct path count: 0
- source_proxy_to_score count: 0
- research_brain_direct_score_stage_key_count: 0
- future leakage in extraction prompt count: 0

## 4. Archetype router

- top1 accuracy: 1.0
- top3 accuracy: 1.0
- C06/C08/C15/C17/C24/C28 mandatory replay result: True
- mandatory_six_results: `{"C06_HBM_MEMORY_CUSTOMER_CAPACITY": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "C15_MATERIAL_SPREAD_SUPERCYCLE": "C15_MATERIAL_SPREAD_SUPERCYCLE", "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "C24_BIO_TRIAL_DATA_EVENT_RISK": "C24_BIO_TRIAL_DATA_EVENT_RISK", "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"}`
- R13 overroute count: 0

## 5. Memory cards

- C01-C36 card count: 36
- source quality breakdown: `{"ontology_only_count": 172166, "price_path_only_count": 361665, "production_fixture_count": 28021, "source_proxy_count": 860101, "url_backed_count": 233705}`
- source gap count: 67

## 6. Source quality

- A2/A1/A0/B/C/D/E counts: `{"A0_URL_STRING_ONLY": 0, "A1_URL_BACKED_ANCHOR_PENDING": 202347, "A2_EVIDENCE_OS_REPLAY_VERIFIED": 200, "B_URL_REPAIR_NEEDED": 31158, "C_SOURCE_PROXY_ONTOLOGY_ONLY": 860101, "D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK": 361665, "E_INVALID_OR_DUPLICATE": 100483}`
- A2 replay sample pass count: 200
- repair queue count: 233505

## 7. Candidate discovery

- candidate_event_count: 60
- sector coverage: `{"L2_AI_SEMICONDUCTOR_ELECTRONICS": 59, "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL": 1}`
- sector gap count: 9
- event type breakdown: `{"capital_return": 1, "price_relative_strength": 46, "supply_contract": 13}`
- targeted_smoke_only: False

## 8. Source task execution

- planned/executed/fetched/parsed/accepted counts: 180 / 180 / 99 / 99 / 99
- provider failures: 0
- budget exhausted material gaps: 0
- general search ratio: 0.0

## 9. Daily watchlist

- Green count: 0
- Yellow-Pending count: 0
- Stage2-Actionable count: 0
- Stage2-Watch count: 33
- 4B-watch count: 0
- Reject/Red count: 0
- Provider pending count: 27

## 10. Production verdict

- verdict: READY_FOR_SHADOW_DAILY_RUN
- blockers: []
- exact next step: run five frozen daily shadow runs with real planner provider before PRODUCTION_READY

쉬운 예: C06 HBM 이벤트에 `false positive` 우려가 붙어도 primary는 C06이어야 한다. R13은 검사관처럼 옆에 붙는 overlay이지, HBM 사건 자체의 primary archetype이 아니다.
