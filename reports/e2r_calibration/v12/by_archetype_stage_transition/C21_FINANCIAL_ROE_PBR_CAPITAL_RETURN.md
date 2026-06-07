# C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `6`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R6L100_C21_IBK_2024_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 12100.0 | None | None | 32.31 | None | stage2_actionable_best_entry |
| R6L100_C21_KAKAOBANK_2024_DIGITAL_BANK_ROE_PBR_FALSE_STAGE2 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 31450.0 | None | None | 0.16 | None | stage2_actionable_best_entry |
| R6L100_C21_KYOBOSECU_2024_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP_4B | 030610 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 5640.0 | None | None | 4b_good_peak_capture |
| R6L98_C21_HANAFIN_2024_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE | 086790 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 54300.0 | None | None | 27.62 | None | stage2_actionable_best_entry |
| R6L98_C21_HANWHAINVEST_2024_BROKERAGE_DIGITAL_ASSET_EVENT_CAP_4B | 003530 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | None | None | 4780.0 | None | None | 4b_good_peak_capture |
| R6L98_C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_STAGE2 | 323410 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 28400.0 | None | None | 9.86 | None | stage2_actionable_best_entry |
