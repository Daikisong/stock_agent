# C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `42`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 006800 | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| 016360 | 016360 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 37100.0 | None | None | 24.3929 | None | stage2_actionable_best_entry |
| 039490 | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 107300.0 | None | None | 36.25 | None | stage2_actionable_best_entry |
| 071050 | 071050 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 58700.0 | None | None | 32.3735 | None | stage2_actionable_best_entry |
| C21-R6L83-DGB-20240226 | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21-R6L83-IBK-20240226 | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 13400.0 | None | None | 19.48 | None | stage2_actionable_best_entry |
| C21-R6L83-JBFG-20240226 | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 13360.0 | None | None | 20.88 | None | stage2_actionable_best_entry |
| R6L71_C21_006800_POLICY_COUNTER | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 8660.0 | None | None | 5.77 | None | stage2_actionable_best_entry |
| R6L71_C21_138930_VALUEUP_POS | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 7720.0 | None | None | 33.94 | None | stage2_actionable_best_entry |
| R6L71_C21_139130_POLICY_COUNTER | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 9230.0 | None | None | 1.95 | None | stage2_actionable_best_entry |
| R6L71_C21_175330_VALUEUP_POS | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 13610.0 | None | None | 38.06 | None | stage2_actionable_best_entry |
| R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129 | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 7420.0 | None | None | 39.35 | None | stage2_actionable_best_entry |
| R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129 | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 8830.0 | None | None | 13.02 | None | stage2_actionable_best_entry |
| R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129 | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 12100.0 | None | None | 32.31 | None | stage2_actionable_best_entry |
| R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129 | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 11160.0 | None | None | 54.57 | None | stage2_actionable_best_entry |
| R6L71_C21_REGIONAL_BANK_BNK_20240126_STAGE2A | 138930 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 7220.0 | None | None | 43.21 | None | stage2_actionable_best_entry |
| R6L71_C21_REGIONAL_BANK_DGB_20240126_STAGE2A | 139130 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 8600.0 | None | None | 16.86 | None | stage2_actionable_best_entry |
| R6L71_C21_REGIONAL_BANK_JB_20240126_STAGE2A | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 10840.0 | None | None | 72.6 | None | stage2_actionable_best_entry |
| R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY | 006220 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 13230.0 | None | None | no_valid_stage_transition |
| R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 29100.0 | None | None | 7.22 | None | stage2_actionable_best_entry |
| R6L72_C21_KB_20240208_CAPITAL_RETURN_VALUEUP | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 67600.0 | None | None | 53.7 | None | stage2_actionable_best_entry |
| R6L72_C21_SHINHAN_20240208_CAPITAL_RETURN_VALUEUP | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 44150.0 | None | None | 46.32 | None | stage2_actionable_best_entry |
| R6L73_C21_003530_20240111_DIGITAL_CRYPTO_BROKERAGE_THEME_NO_ROE_BRIDGE | 003530 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 4400.0 | None | None | 21.14 | None | stage2_actionable_best_entry |
| R6L73_C21_005940_20240129_BROKERAGE_CAPITAL_RETURN_LOW_MAE_REPAIR | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 10430.0 | None | None | 38.06 | None | stage2_actionable_best_entry |
| R6L73_C21_006220_JEJUBANK_20230217 | 006220 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 20900.0 | None | 23750.0 | 33.25 | 41.0116 | stage2_actionable_best_entry |
| R6L73_C21_016360_20240129_BROKERAGE_ROE_CAPITAL_RETURN_BRIDGE | 016360 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 36950.0 | None | None | 32.34 | None | stage2_actionable_best_entry |
| R6L73_C21_105560_KB_20240208 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 67600.0 | None | None | 53.7 | None | stage2_actionable_best_entry |
| R6L73_C21_138040_MERITZ_20240208 | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 71800.0 | None | 99200.0 | 49.3 | 77.4068 | 4b_good_peak_capture |
| R6L73_C21_323410_KAKAOBANK_20240208 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 29100.0 | None | None | 7.22 | None | stage2_actionable_best_entry |
| R6L75_C21_001510_20240201_SMALL_SECURITIES_VALUEUP_THEME_NO_ROE_CAPITAL_RETURN_BRIDGE | 001510 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 647.0 | None | None | 3.4 | None | stage2_actionable_best_entry |
| R6L75_C21_016360_20240129_BROKERAGE_DIVIDEND_ROE_CAPITAL_RETURN_BRIDGE | 016360 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 36950.0 | None | None | 32.34 | None | stage2_actionable_best_entry |
| R6L75_C21_071050_20240129_FINANCIAL_HOLDCO_ROE_PBR_CAPITAL_RETURN_BRIDGE | 071050 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 58700.0 | None | None | 32.37 | None | stage2_actionable_best_entry |
| R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216 | 006220 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 10500.0 | None | 10500.0 | 165.24 | 0.0 | stage2_actionable_best_entry |
| R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 69800.0 | None | 69800.0 | 35.24 | 0.0 | 4b_good_peak_capture |
| R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208 | 105560 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 67600.0 | None | 67600.0 | 53.7 | 0.0 | 4b_good_peak_capture |
| R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426 | 138040 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 44450.0 | None | 44450.0 | 40.16 | 0.0 | 4b_good_peak_capture |
| R6L85-C21-01 | 016360 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 39300.0 | None | None | 24.43 | None | stage2_actionable_best_entry |
| R6L85-C21-02 | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 114500.0 | None | None | 27.86 | None | stage2_actionable_best_entry |
| R6L85-C21-03 | 030610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| R6L87-C21-01 | 071050 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 65900.0 | None | None | 17.91 | None | stage2_actionable_best_entry |
| R6L87-C21-02 | 029780 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 36200.0 | None | None | 25.83 | None | stage2_actionable_best_entry |
| R6L87-C21-03 | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
