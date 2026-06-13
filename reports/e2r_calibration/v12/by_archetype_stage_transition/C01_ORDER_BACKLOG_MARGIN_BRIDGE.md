# C01_ORDER_BACKLOG_MARGIN_BRIDGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `43`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 009540 | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 123700.0 | None | None | 4.28 | None | stage2_actionable_best_entry |
| 010140 | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| 017960 | 017960 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 10840.0 | None | None | 23.15 | None | stage2_actionable_best_entry |
| 033500 | 033500 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| 042660 | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| 077970 | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| 097230 | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 3510.0 | None | None | 182.05 | None | stage2_actionable_best_entry |
| C01-132-01 | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 6500.0 | None | None | 45.69 | None | stage2_actionable_best_entry |
| C01-132-02 | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 121500.0 | None | None | no_valid_stage_transition |
| C01-132-03 | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 177500.0 | None | None | 128.73 | None | stage2_actionable_best_entry |
| C01-132-04 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 102600.0 | None | None | 40.64 | None | stage2_actionable_best_entry |
| C01-132-05 | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01-132-06 | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 30950.0 | None | None | no_valid_stage_transition |
| C01-L207-01 | 033500 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 13230.0 | None | None | 69.69 | None | stage2_actionable_best_entry |
| C01-L207-02 | 033500 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01-L207-03 | 075580 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 6850.0 | None | None | 59.42 | None | stage2_actionable_best_entry |
| C01-L207-04 | 075580 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01-L207-05 | 014940 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 5260.0 | None | None | 146.96 | None | stage2_actionable_best_entry |
| C01-L207-06 | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 7190.0 | None | None | 377.75 | None | stage2_actionable_best_entry |
| C01-L207-07 | 443060 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 163900.0 | None | None | 4b_too_early |
| C01-L207-08 | 443060 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 165000.0 | None | None | 55.76 | None | stage2_actionable_best_entry |
| C01-L207-09 | 073010 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 4035.0 | None | None | 40.02 | None | stage2_captured_most_upside |
| C01-L207-10 | 108380 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 16490.0 | None | None | 26.74 | None | stage2_captured_most_upside |
| C01_013030_2024-05-24_instrumentation_fitting_valve_quality_but_low_alpha_path | 013030 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 28500.0 | None | None | 13.8596 | None | stage2_actionable_best_entry |
| C01_014620_2024-08-14_new_orders_shipbuilding_lng_mix_margin_reacceleration | 014620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_023160_2024-09-23_welded_fitting_h2_order_recovery_lng_offshore_mix | 023160 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_073010_2024-04-25_marine_engine_parts_backlog_capacity_expansion | 073010 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_086670_2024-05-30_industrial_fitting_valve_multicycle_exposure_high_mae_false_stage2 | 086670 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 12700.0 | None | None | 11.2598 | None | stage2_actionable_best_entry |
| C01_103230_2024-12-20_ship_engine_parts_delivery_from_accumulated_backlog | 103230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L115_010620_20250117_mipo_profit_swing_order_target | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L115_071970_20240731_hd_marine_engine_launch_stage_timing | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 23050.0 | None | None | 67.68 | None | stage2_actionable_best_entry |
| C01_R1L115_075580_20240402_sejin_tank_deckhouse_customer_backlog | 075580 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 6850.0 | None | None | 59.42 | None | stage2_actionable_best_entry |
| C01_R1L115_082740_20240821_hanwha_engine_backlog_revenue_recognition | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| C01_R1L115_100090_20240822_sk_oceanplant_backlog_revenue_delay | 100090 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 14270.0 | None | None | no_valid_stage_transition |
| C01_R1L115_329180_20250217_hhi_commercial_ship_engine_margin | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| c01_loop142_013030_06 | 013030 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 28500.0 | None | None | 13.86 | None | stage2_actionable_best_entry |
| c01_loop142_014620_05 | 014620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11570.0 | None | None | 180.9 | None | stage2_captured_most_upside |
| c01_loop142_017960_01 | 017960 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 10340.0 | None | None | 29.11 | None | stage2_actionable_best_entry |
| c01_loop142_023160_04 | 023160 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 13370.0 | None | None | 101.94 | None | stage2_captured_most_upside |
| c01_loop142_042670_07 | 042670 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| c01_loop142_071970_03 | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 15880.0 | None | None | 94.9 | None | stage2_actionable_best_entry |
| c01_loop142_082740_02 | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 10130.0 | None | None | 81.05 | None | stage2_actionable_best_entry |
| c01_loop142_241560_08 | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 52000.0 | None | None | 4b_good_peak_capture |
