# C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `26`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C29_L179_001_HANKOOK_Q1_2024_LATE_HEADLINE_HIGH_MAE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_L179_002_HANKOOK_FY2024_RESET_POSITIVE | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 37750.0 | None | None | 28.48 | None | stage2_actionable_best_entry |
| C29_L179_003_KUMHO_Q1_2024_LATE_BLOWOFF | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_L179_004_KUMHO_Q3_2024_MIX_REORDER_RESET_POSITIVE | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 4425.0 | None | None | 21.81 | None | stage2_actionable_best_entry |
| C29_L179_005_NEXEN_FY2023_TURNAROUND_EARLY_POSITIVE | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 8000.0 | None | None | 20.88 | None | stage2_actionable_best_entry |
| C29_L179_006_NEXEN_2H24_CZECH_RAMP_LATE_HIGH_MAE | 002350 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_L179_007_HANON_FY2024_EV_SLOWDOWN_STRUCTURE_COST_4C | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_L179_008_HYUNDAI_WIA_Q1_2025_FALSE_4C_POSITIVE | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_L179_009_HYUNDAI_GLOVIS_Q1_2025_PCTC_RECORD_POSITIVE | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9_L100_000270_20240125_oem_record_sales_margin | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 93000.0 | None | None | 45.2 | None | stage2_actionable_best_entry |
| C29_R9_L100_005380_20240125_oem_volume_mix_margin | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 188700.0 | None | None | 58.7 | None | stage2_actionable_best_entry |
| C29_R9_L100_018880_20250214_supplier_margin_break_4c | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | 4c_too_late |
| C29_R9_L100_118990_20250514_ivi_growth_high_mae | 118990 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 9320.0 | None | None | 24.1 | None | stage2_actionable_best_entry |
| C29_R9_L100_204320_20240205_parts_revenue_margin_recovery | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 36850.0 | None | None | 35.7 | None | stage2_actionable_best_entry |
| C29_R9_L101_005850_20240517_lighting_supplier_led_mix_margin_bridge | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9_L101_010690_20240516_ev_battery_case_order_revenue_timing_high_mae | 010690 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 10490.0 | None | None | no_valid_stage_transition |
| C29_R9_L101_011210_20240129_auto_parts_scale_with_weak_durability | 011210 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 58000.0 | None | None | no_valid_stage_transition |
| C29_R9_L101_012330_20240129_oem_core_parts_mix_margin_bridge | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 202500.0 | None | None | 33.3333 | None | stage2_actionable_best_entry |
| C29_R9_L101_064960_20250318_hev_eop_xev_parts_revenue_recovery | 064960 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 25550.0 | None | None | 59.6869 | None | stage2_actionable_best_entry |
| C29_R9_L101_073240_20240206_tire_turnaround_margin_recovery | 073240 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 6140.0 | None | None | 36.1564 | None | stage2_actionable_best_entry |
| C29_R9_L101_161390_20240205_tire_premium_mix_operating_leverage | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 50000.0 | None | None | 26.6 | None | stage2_actionable_best_entry |
| C29_R9_L123_CASE_001B_000270_KIA_LOCAL_4B_OVERLAY | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | 132300.0 | None | None | no_valid_stage_transition |
| C29_R9_L123_CASE_001_000270_KIA_2023_ANNUAL_OPM_CAPITAL_RETURN | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | None | None | None | None | None | no_valid_stage_transition |
| C29_R9_L123_CASE_002_012330_MOBIS_2024_MARGIN_RECOVERY | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 263500.0 | None | None | 24.1 | None | stage2_actionable_best_entry |
| C29_R9_L123_CASE_003_204320_HL_MANDO_Q2_MISS | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 39850.0 | None | None | 17.94 | None | stage2_actionable_best_entry |
| C29_R9_L123_CASE_004_005380_HYUNDAI_Q2_RECORD_ALREADY_PRICED | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 243500.0 | None | None | 9.65 | None | stage2_actionable_best_entry |
