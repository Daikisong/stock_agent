# C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `48`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 086790 | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 54600.0 | None | None | 26.92 | None | stage2_actionable_best_entry |
| 316140 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| 323410 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L85_086790_HANA_BANK_ROE_PBR_CAPITAL_RETURN | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 46400.0 | None | None | 49.14 | None | stage2_actionable_best_entry |
| C21_R6L85_323410_KAKAOBANK_DIGITAL_BETA_NO_CAPITAL_RETURN | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L85_377300_KAKAOPAY_FINTECH_BETA_NO_ROE_BRIDGE | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L87_006800_MIRAE_BROKERAGE_ROE_CAPITAL_RETURN | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 7140.0 | None | None | 30.25 | None | stage2_actionable_best_entry |
| C21_R6L87_039490_KIWOOM_LATE_VALUEUP_EXTENSION | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L87_316140_WOORI_LATE_BANK_VALUEUP_EXTENSION | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L89_001200_EUGENE_BROKERAGE_PRICE_ONLY_BLOWOFF | 001200 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L89_001510_SK_SMALL_BROKERAGE_REBOUND | 001510 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L89_024110_IBK_BANK_VALUEUP_CAPITAL_RETURN | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 11870.0 | None | None | 34.88 | None | stage2_actionable_best_entry |
| C21_R6L90_005940_2024_02_28 | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 11550.0 | None | None | 24.7 | None | stage2_captured_most_upside |
| C21_R6L90_006800_2024_02_28 | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L90_039490_2024_02_28 | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 124900.0 | None | None | 17.2 | None | stage2_captured_most_upside |
| C21_R6L91_001290_SANGSANGIN_TURNAROUND_BROKERAGE | 001290 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L91_005940_NH_BROKERAGE_CAPITAL_RETURN | 005940 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 10430.0 | None | None | 39.31 | None | stage2_actionable_best_entry |
| C21_R6L91_030610_KYOBO_SMALL_BROKERAGE_VALUEUP | 030610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L92_029780_2024_02_26 | 029780 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 36200.0 | None | None | 27.1 | None | stage2_captured_most_upside |
| C21_R6L92_030610_2024_02_26 | 030610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 5220.0 | None | None | 12.5 | None | stage2_captured_most_upside |
| C21_R6L92_175330_2024_02_26 | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 13360.0 | None | None | 40.0 | None | stage2_captured_most_upside |
| C21_R6L94_001510_2024_02_01 | 001510 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L94_055550_2024_02_01 | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 42500.0 | None | None | 52.0 | None | stage2_captured_most_upside |
| C21_R6L94_316140_2024_02_01 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 14410.0 | None | None | 18.7 | None | stage2_captured_most_upside |
| C21_R6L95_001450_2024_02_01 | 001450 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 35450.0 | None | None | 3.8 | None | stage2_captured_most_upside |
| C21_R6L95_016610_2024_02_01 | 016610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 4210.0 | None | None | 49.2 | None | stage2_captured_most_upside |
| C21_R6L95_085620_2024_02_05 | 085620 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| C21_R6L97_055550_2024_02_01 | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 42500.0 | None | None | 52.0 | None | stage2_captured_most_upside |
| C21_R6L97_086790_2024_02_01 | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 52000.0 | None | None | 33.3 | None | stage2_captured_most_upside |
| C21_R6L97_377300_2024_02_15 | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| R6L83_C21_006800_MIRAE_BROKERAGE_BETA_NO_ROE_BRIDGE | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| R6L83_C21_039490_KIWOOM_LATE_RETAIL_BROKERAGE_PRICE_SPIKE | 039490 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | None | None | None | no_valid_stage_transition |
| R6L83_C21_055550_SHINHAN_VALUEUP_CAPITAL_RETURN_BRIDGE | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 45300.0 | None | None | 32.23 | None | stage2_actionable_best_entry |
| R6L88_C21_HANAFG_2024_BANK_VALUEUP_CAPITAL_RETURN_POSITIVE | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 42800.0 | None | None | 61.92 | None | stage2_actionable_best_entry |
| R6L88_C21_HANWHAINV_2024_DIGITAL_BROKERAGE_THEME_CAP_4B | 003530 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 4780.0 | None | None | 4b_good_peak_capture |
| R6L88_C21_IBK_2024_POLICY_BANK_VALUEUP_EVENT_CAP_4B | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 15700.0 | None | None | 4b_good_peak_capture |
| R6L90_C21_HANYANGSEC_2024_BROKERAGE_CONTROL_PREMIUM_EVENT_CAP_4B | 001750 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 16160.0 | None | None | 4b_good_peak_capture |
| R6L90_C21_SKSEC_2024_SMALL_BROKERAGE_VALUEUP_FALSE_STAGE2 | 001510 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 647.0 | None | None | 3.4 | None | stage2_actionable_best_entry |
| R6L90_C21_WOORI_2024_BANK_VALUEUP_ROE_CAPITAL_RETURN_POSITIVE | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 13000.0 | None | None | 30.46 | None | stage2_actionable_best_entry |
| R6L92_C21_DBSEC_2024_BROKERAGE_CAPITAL_RETURN_EVENT_CAP_4B | 016610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 4650.0 | None | None | 4b_good_peak_capture |
| R6L92_C21_JBFG_2024_REGIONAL_BANK_ROE_CAPITAL_RETURN_POSITIVE | 175330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 10770.0 | None | None | 59.8 | None | stage2_actionable_best_entry |
| R6L92_C21_YUANTA_2024_BROKERAGE_VALUEUP_FALSE_STAGE2 | 003470 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 2880.0 | None | None | 0.35 | None | stage2_actionable_best_entry |
| R6L94_C21_MIRAESEC_2024_BROKERAGE_PBR_VALUEUP_FALSE_STAGE2 | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 8950.0 | None | None | 2.79 | None | stage2_actionable_best_entry |
| R6L94_C21_SHINHAN_2024_BANK_VALUEUP_CAPITAL_RETURN_ROE_PBR_POSITIVE | 055550 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 40050.0 | None | None | 35.58 | None | stage2_actionable_best_entry |
| R6L94_C21_WOORITECHINVEST_2024_DIGITAL_ASSET_FINANCIAL_EVENT_CAP_4B | 041190 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 11210.0 | None | None | 4b_good_peak_capture |
| R6L96_C21_KAKAOPAY_2024_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP_4B | 377300 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 58000.0 | None | None | 4b_good_peak_capture |
| R6L96_C21_PUREUNSB_2024_SAVINGS_BANK_RATE_VALUEUP_FALSE_STAGE2 | 007330 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 9970.0 | None | None | 5.32 | None | stage2_actionable_best_entry |
| R6L96_C21_SAMSUNGCARD_2024_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_POSITIVE | 029780 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 34900.0 | None | None | 24.07 | None | stage2_actionable_best_entry |
