# C14_EV_DEMAND_SLOWDOWN_4B_4C Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `21`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 095500 | 095500 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| 222080 | 222080 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 10820.0 | None | None | 39.65 | None | stage2_actionable_best_entry |
| 278280 | 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 74700.0 | None | None | no_valid_stage_transition |
| R3L72_C14_006400_20240131_4B_TOO_EARLY | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 372500.0 | None | None | no_valid_stage_transition |
| R3L72_C14_066970_20240430_4C_SUCCESS | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L72_C14_247540_20240430_4C_SUCCESS | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L72_C14_373220_20240430_4B_TOO_EARLY | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 389000.0 | None | None | no_valid_stage_transition |
| R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B | 006110 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 135600.0 | None | None | 17.18 | None | stage2_actionable_best_entry |
| R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B | 011790 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 103000.0 | None | None | 45.34 | None | stage2_actionable_best_entry |
| R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START | 095500 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 28600.0 | None | None | 7.17 | None | stage2_actionable_best_entry |
| R3L76_C14_LGES_20240425_CAPEX_SLOW_EV_FALSE_BREAK | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 372500.0 | None | None | 4b_too_early |
| R3L76_C14_LGES_20241028_CONSERVATIVE_2025_CAPEX_CUT | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 416500.0 | None | None | 4b_good_peak_capture |
| R3L76_C14_SDI_20240625_EUROPE_EV_SLOWDOWN_WARNING | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 368500.0 | None | None | 4b_good_peak_capture |
| R3L76_C14_SDI_20250305_DEMAND_SLUGGISH_UNTIL_2026 | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 213500.0 | None | None | no_valid_stage_transition |
| R3L85-C14-01 | 121600 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L85-C14-02 | 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L85-C14-03 | 020150 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 224000.0 | None | None | 209.82 | None | stage2_actionable_best_entry |
| R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK | 348370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 88200.0 | None | None | 347.28 | None | stage2_actionable_best_entry |
| R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
