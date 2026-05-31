# C05_EPC_MEGA_CONTRACT_MARGIN_GAP Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `19`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C05_006360_GS_EC_20230629_QUALITY_COST_4C_MARGIN_BREAK | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| C05_028050_SAMSUNG_EA_20230131_ORDER_BACKLOG_MARGIN_BRIDGE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 25850.0 | None | None | 46.2282 | None | stage2_actionable_best_entry |
| C05_047040_DAEWOO_EC_20230131_ORDER_HEADLINE_MARGIN_GAP | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 4785.0 | None | None | 3.4483 | None | stage2_captured_most_upside |
| R1L11_C05_DAEWOOENG_ORDERBOOK_MARGIN_GAP_20240131 | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 3935.0 | None | None | 12.07 | None | stage2_captured_most_upside |
| R1L11_C05_DLEC_VALUATION_CONTRACT_GAP_20240110 | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 40750.0 | None | None | 8.34 | None | stage2_actionable_best_entry |
| R1L11_C05_GSENG_QUALITY_4C_20230706 | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | 4c_too_late |
| R1L11_C05_HYUNDAIENG_OVERSEAS_EPC_20240125 | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 32050.0 | None | None | 12.32 | None | stage2_actionable_best_entry |
| R1L11_C05_SAMSUNGEA_MARGIN_BRIDGE_20240131 | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 22300.0 | None | None | 26.23 | None | stage2_actionable_best_entry |
| R1L15_C05_DAEWOO_20230703_BACKLOG_SURVIVOR | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 4165.0 | None | None | 15.01 | None | stage2_actionable_best_entry |
| R1L15_C05_DLENC_20240327_POLICY_BETA_MARGIN_CAP | 375500 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 36450.0 | None | None | 8.37 | None | stage2_actionable_best_entry |
| R1L15_C05_GS_20230706_REMEDIATION_COST_4C | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | 4c_too_late |
| R1L15_C05_HDC_20220112_SAFETY_TRUST_4C | 294870 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | 4c_too_late |
| R1L15_C05_HDEC_20230626_MEGA_ORDER_MARGIN_GAP | 000720 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 40800.0 | None | None | 8.82 | None | stage2_actionable_best_entry |
| R1L15_C05_SSGC_20240327_DIRECT_SUPPORT_CONTROL | 034300 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10630.0 | None | None | 75.45 | None | stage2_actionable_best_entry |
| `000720` | `000720` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 32050.0 | None | None | 12.32 | None | stage2_actionable_best_entry |
| `006360` | `006360` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | 4c_too_late |
| `028050` | `028050` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 22300.0 | None | None | 26.23 | None | stage2_actionable_best_entry |
| `047040` | `047040` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 3935.0 | None | None | 12.07 | None | stage2_captured_most_upside |
| `375500` | `375500` | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 40750.0 | None | None | 8.34 | None | stage2_actionable_best_entry |
