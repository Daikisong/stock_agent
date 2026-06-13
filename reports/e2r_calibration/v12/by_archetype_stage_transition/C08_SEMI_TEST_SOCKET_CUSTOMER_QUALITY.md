# C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `28`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 080580 | 080580 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| 098120 | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| 131290 | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 46450.0 | None | None | no_valid_stage_transition |
| 252990 | 252990 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 6970.0 | None | None | no_valid_stage_transition |
| 253590 | 253590 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| 425420 | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 37100.0 | None | None | no_valid_stage_transition |
| C08-L158-001 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 235500.0 | None | None | 31.21 | None | stage2_actionable_best_entry |
| C08-L158-002 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 255500.0 | None | None | no_valid_stage_transition |
| C08-L158-003 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 268000.0 | None | None | no_valid_stage_transition |
| C08-L158-004 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 73200.0 | None | None | 47.54 | None | stage2_actionable_best_entry |
| C08-L158-005 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 98000.0 | None | None | 4b_good_peak_capture |
| C08-L158-006 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| C08-L184-CASE01-425420-TFE | 425420 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 16230.0 | None | None | 186.51 | None | stage2_actionable_best_entry |
| C08-L184-CASE02-405100-QRT | 405100 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 16130.0 | None | None | 169.68 | None | stage2_actionable_best_entry |
| C08-L184-CASE03-405100-QRT | 405100 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 21450.0 | None | None | 14.69 | None | stage2_captured_most_upside |
| C08-L184-CASE04-252990-SAM_CANDS | 252990 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 6800.0 | None | None | 7.94 | None | stage2_captured_most_upside |
| C08-L184-CASE05-098120-MICRO_CONTACT_SOLUTION | 098120 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| C08-L184-CASE06-330860-NEPES_ARK | 330860 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | None | None | None | no_valid_stage_transition |
| C08-L184-CASE07-131970-DOOSAN_TESNA | 131970 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 22500.0 | None | None | 223.56 | None | stage2_actionable_best_entry |
| C08-L184-CASE08-131290-TSE | 131290 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 51400.0 | None | None | 70.82 | None | stage2_captured_most_upside |
| C08_R2L111_033640_NEPES_2_5D_PACKAGING_ROADMAP_WITHOUT_CUSTOMER_REVENUE_20240520 | 033640 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 17870.0 | None | None | 4b_good_peak_capture |
| C08_R2L111_053610_PROTEC_SAMSUNG_HBM_SORTER_SMALL_SCALE_ORDER_CAP_20240925 | 053610 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 29900.0 | None | None | 4b_good_peak_capture |
| C08_R2L111_058470_LEENO_HBM_TEST_SOCKET_RND_TO_MASS_PRODUCTION_OPTIONALITY_20240124 | 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 225000.0 | None | None | 37.33 | None | stage2_actionable_best_entry |
| C08_R2L111_067310_HANAMICRON_BACKEND_PACKAGING_TEST_CUSTOMER_PROXY_20231023 | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 28050.0 | None | None | 22.99 | None | stage2_actionable_best_entry |
| C08_R2L111_095340_ISC_HBM_TEST_SOCKET_DEVELOPMENT_EXPECTED_RAMP_HIGH_MAE_20241223 | 095340 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 72000.0 | None | None | 4b_good_peak_capture |
| C08_R2L111_131970_DOOSANTESNA_GENERAL_OSAT_STRATEGY_NO_TEST_CUSTOMER_REORDER_20240713 | 131970 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 41900.0 | None | None | 4b_good_peak_capture |
| C08_R2L111_219130_TIGERELEC_PROBE_CARD_PCB_QUALIFICATION_FAST_MFE_HIGH_MAE_20240124 | 219130 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 25000.0 | None | None | 81.2 | None | stage2_actionable_best_entry |
| C08_R2L111_420770_GIGAVIS_FCBGA_FINAL_TEST_OPTIONALITY_NOT_ORDER_20240807 | 420770 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | None | None | 36850.0 | None | None | 4b_good_peak_capture |
