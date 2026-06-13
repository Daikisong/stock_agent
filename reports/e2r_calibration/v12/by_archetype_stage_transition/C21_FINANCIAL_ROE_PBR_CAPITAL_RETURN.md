# C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `25`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 024110 | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| 039490 | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 129500.0 | None | None | 13.0502 | None | stage2_actionable_best_entry |
| 071050 | 071050 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| 138040 | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | 83400.0 | None | None | None | green_good_but_late |
| 138930 | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 9440.0 | None | None | 30.2966 | None | stage2_actionable_best_entry |
| 175330 | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | 15030.0 | None | None | None | green_good_but_late |
| C21_169_039490_20240528_VALUEUP_PLAN_ROE15_PBR1_RETURN30 | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_169_039490_20241030_Q3_BEAT_BROKERAGE_DRAG | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_169_039490_20250205_FY2024_PROFIT_SURGE_BUT_Q4_MISS | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 117000.0 | None | None | 175.64 | None | stage2_actionable_best_entry |
| C21_169_086790_20240429_EXPECTED_CET1_SHAREHOLDER_RETURN_WATCH | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_169_086790_20241029_Q3_VALUEUP_150BN_BUYBACK_TARGET_50 | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 65000.0 | None | None | 49.38 | None | stage2_actionable_best_entry |
| C21_169_086790_20250204_RECORD_PROFIT_400BN_BUYBACK | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 61500.0 | None | None | 57.89 | None | stage2_actionable_best_entry |
| C21_169_138040_20240208_ONE_MERITZ_BUYBACK_RETIREMENT_POLICY | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 71800.0 | None | None | 49.3 | None | stage2_actionable_best_entry |
| C21_169_138040_20240705_RETURN50_POLICY_CONTINUATION | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 83400.0 | None | None | 52.76 | None | stage2_actionable_best_entry |
| C21_169_138040_20241121_ACTIVE_BUYBACK_CANCELLATION_EPS_ACC | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 103800.0 | None | None | 22.74 | None | stage2_actionable_best_entry |
| C21_L190_001_JBFG_2Q24_BUYBACK_CANCEL_EXECUTION | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 13430.0 | None | None | 52.64 | None | stage2_actionable_best_entry |
| C21_L190_002_JBFG_VALUEUP_DISCLOSURE_CONFIRMED_RETURN | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 15030.0 | None | None | 48.37 | None | stage2_actionable_best_entry |
| C21_L190_003_BNK_Q3_VALUEUP_RETURN_BRIDGE | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 9440.0 | None | None | 70.02 | None | stage2_actionable_best_entry |
| C21_L190_004_BNK_FY24_STAGED_RETURN_HIGH_MAE | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_L190_005_DGB_EXEC_BUYBACK_LOW_PBR_BUT_CAPITAL_NEED | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_L190_006_DGB_2Q24_RETURN_NOT_FEASIBLE_UNTIL_2027 | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_L190_007_IBK_DIVIDEND_PAYOUT_STATE_BANK_LOW_ALPHA | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_L190_008_KIH_FY24_EARNINGS_DIVIDEND_REPRICING | 071050 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_L190_009_SAMSUNG_SECURITIES_Q1_EARNINGS_BROKERAGE_ROE | 016360 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 38800.0 | None | None | 30.67 | None | stage2_actionable_best_entry |
| C21_L190_010_KAKAOBANK_RECORD_PROFIT_NO_RETURN_BRIDGE | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
