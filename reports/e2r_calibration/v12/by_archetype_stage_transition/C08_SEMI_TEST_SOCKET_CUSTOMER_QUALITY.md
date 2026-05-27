# C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `6`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R2L11_C08_058470_LINO_20240308 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 215500.0 | 274500.0 | None | 43.39 | None | green_too_late |
| R2L11_C08_058470_LINO_20240308 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 215500.0 | 274500.0 | None | 43.39 | None | green_too_late |
| R2L11_C08_095340_ISC_20240308 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| R2L11_C08_095340_ISC_20240308 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| R2L11_C08_131290_TSE_20240424 | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 64200.0 | None | None | 36.7611 | None | stage2_actionable_best_entry |
| R2L11_C08_131290_TSE_20240424 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 64200.0 | None | None | 36.7611 | None | stage2_actionable_best_entry |
