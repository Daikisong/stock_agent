# C01_ORDER_BACKLOG_MARGIN_BRIDGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `23`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 010140 | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 9690.0 | None | None | 26.83 | None | stage2_actionable_best_entry |
| 017960 | 017960 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11350.0 | None | None | 18.94 | None | stage2_actionable_best_entry |
| 042660 | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 23050.0 | None | None | 251.4085 | None | stage2_actionable_best_entry |
| 071970 | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 17730.0 | None | None | 54.26 | None | stage2_actionable_best_entry |
| 077970 | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 12900.0 | None | None | 89.15 | None | stage2_actionable_best_entry |
| 082740 | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 9670.0 | None | None | 77.46 | None | stage2_actionable_best_entry |
| 097230 | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| 100090 | 100090 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| 329180 | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 110400.0 | None | None | 178.5266 | None | stage2_actionable_best_entry |
| R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 24150.0 | None | None | 69.98 | None | stage2_actionable_best_entry |
| R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 13990.0 | None | None | 77.63 | None | stage2_actionable_best_entry |
| R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE | 100090 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 22900.0 | None | None | 2.62 | None | stage2_actionable_best_entry |
| R1L75_C01_009540_20240222_PARENT_BACKLOG_MARGIN_BRIDGE | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 116800.0 | None | None | 82.36 | None | stage2_actionable_best_entry |
| R1L75_C01_010140_20230131_ORDERBOOK_RECOVERY_HIGH_MAE | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 5790.0 | None | None | 68.74 | None | stage2_actionable_best_entry |
| R1L75_C01_010620_20240102_ORDERBOOK_BETA_BEFORE_MARGIN_TROUGH | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 85400.0 | None | None | 43.79 | None | stage2_actionable_best_entry |
| R1L75_C01_042660_20240322_HANWHAOCEAN_LOCAL_PEAK_4B_OVERLAY | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 30700.0 | None | None | no_valid_stage_transition |
| R1L75_C01_329180_20240222_YARD_BACKLOG_OPERATING_LEVERAGE | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 110800.0 | None | None | 120.67 | None | stage2_actionable_best_entry |
| R1L76_C01_042660_20240314_SHIPBUILDING_BACKLOG_TURNAROUND_MARGIN_BRIDGE | 042660 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 27000.0 | None | None | 30.74 | None | stage2_actionable_best_entry |
| R1L76_C01_071970_20240314_ENGINE_BACKLOG_MARGIN_REPRICING_BRIDGE | 071970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 10680.0 | None | None | 132.68 | None | stage2_actionable_best_entry |
| R1L76_C01_241560_20240201_COMPACT_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 49300.0 | None | None | 20.69 | None | stage2_actionable_best_entry |
| R1L85-C01-01 | 014620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11540.0 | None | None | 181.63 | None | stage2_actionable_best_entry |
| R1L85-C01-02 | 023160 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 13410.0 | None | None | 33.63 | None | stage2_actionable_best_entry |
| R1L85-C01-03 | 100090 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
