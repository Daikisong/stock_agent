# C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `13`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R8L71_C26_035420_NAVER_LINE_REGULATORY_CAP | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| R8L71_C26_035720_KAKAO_LEGAL_TRUST_BREAK | 035720 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | None | None | None | None | 4c_too_late |
| R8L71_C26_042000_CAFE24_GOOGLE_YOUTUBE_SHOPPING | 042000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 22150.0 | None | None | 93.91 | None | stage2_actionable_best_entry |
| R8L71_C26_067160_SOOP_TWITCH_MIGRATION | 067160 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 76600.0 | None | None | 87.73 | None | stage2_actionable_best_entry |
| R8L73_C26_030000_20240129_AD_REVENUE_THEME_LOW_MFE_MARGIN_WEAK | 030000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 18710.0 | None | None | 3.37 | None | stage2_actionable_best_entry |
| R8L73_C26_214270_20240130_DIGITAL_AD_AI_THEME_BLOWOFF_NO_REVENUE_BRIDGE | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 3050.0 | None | None | 23.77 | None | stage2_actionable_best_entry |
| R8L73_C26_214320_20240129_GLOBAL_AD_AGENCY_MARGIN_LOW_BETA_BRIDGE | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 21500.0 | None | None | 6.05 | None | stage2_actionable_best_entry |
| R8L76_C26_042000_20240220_SOCIAL_COMMERCE_PLATFORM_GMV_TAKE_RATE_BRIDGE | 042000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 24500.0 | None | None | 75.31 | None | stage2_actionable_best_entry |
| R8L76_C26_214270_20240129_DIGITAL_AD_PLATFORM_THEME_NO_TAKE_RATE_MARGIN_BRIDGE | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 2730.0 | None | None | 38.28 | None | stage2_actionable_best_entry |
| R8L76_C26_237820_20240202_AI_AD_AGENCY_THEME_NO_RECURRING_REVENUE_BRIDGE | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 6820.0 | None | None | 56.3 | None | stage2_actionable_best_entry |
| R8L85-C26-01 | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 6250.0 | None | None | 70.56 | None | stage2_actionable_best_entry |
| R8L85-C26-02 | 216050 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| R8L85-C26-03 | 236810 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
