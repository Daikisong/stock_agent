# C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `17`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 067310 | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 25500.0 | None | None | 35.29 | None | stage2_actionable_best_entry |
| 089030 | 089030 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 18200.0 | None | None | 289.01 | None | stage2_actionable_best_entry |
| 092870 | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 19150.0 | None | None | no_valid_stage_transition |
| R2L72_C08_058470 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 241500.0 | None | None | 27.95 | None | stage2_actionable_best_entry |
| R2L72_C08_058470 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 241500.0 | None | None | 27.95 | None | stage2_actionable_best_entry |
| R2L72_C08_095340 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 93700.0 | None | 99400.0 | 15.26 | 39.864 | stage2_actionable_best_entry |
| R2L72_C08_095340 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 93700.0 | None | 99400.0 | 15.26 | 39.864 | 4b_too_early |
| R2L72_C08_098120 | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 9440.0 | None | None | 17.9 | None | stage2_actionable_best_entry |
| R2L72_C08_098120 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 9440.0 | None | None | 17.9 | None | stage2_actionable_best_entry |
| R2L72_C08_131290 | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 57000.0 | None | 79000.0 | 54.0361 | 71.4272 | stage2_actionable_best_entry |
| R2L72_C08_131290 | None | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 57000.0 | None | 79000.0 | 54.0361 | 71.4272 | 4b_good_peak_capture |
| R2L74_C08_252990_20240123_CERAMIC_STF_PROBE_CARD_THEME_NO_DURABLE_BRIDGE | 252990 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 6860.0 | None | None | 28.86 | None | stage2_actionable_best_entry |
| R2L74_C08_424980_20240125_MEMS_PROBE_CARD_IPO_OPTIONALITY_NO_CUSTOMER_BRIDGE | 424980 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 16280.0 | None | None | 45.88 | None | stage2_actionable_best_entry |
| R2L74_C08_425420_20240208_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 35200.0 | None | None | 24.86 | None | stage2_actionable_best_entry |
| R2L85-C08-01 | 089030 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 18690.0 | None | None | 278.81 | None | stage2_actionable_best_entry |
| R2L85-C08-02 | 330860 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| R2L85-C08-03 | 252990 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
