# C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `3`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R8L99_C26_CAFE24_2024_COMMERCE_PLATFORM_GMV_AD_TAKE_RATE_OPERATING_LEVERAGE_POSITIVE | 042000 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 19390.0 | None | None | 121.51 | None | stage2_actionable_best_entry |
| R8L99_C26_NAVER_2024_SEARCH_PORTAL_AD_RECOVERY_FALSE_STAGE2 | 035420 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 231000.0 | None | None | 1.95 | None | stage2_actionable_best_entry |
| R8L99_C26_PLAYD_2024_DIGITAL_ADTECH_EVENT_CAP_4B | 237820 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | None | None | 8900.0 | None | None | 4b_good_peak_capture |
