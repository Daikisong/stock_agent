# C01_ORDER_BACKLOG_MARGIN_BRIDGE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `23`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 010620 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 80500.0 | None | None | 79.25 | None | stage2_actionable_best_entry |
| 097230 | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| 329180 | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 130000.0 | None | None | 185.77 | None | stage2_actionable_best_entry |
| C01_HDHE_20230413_GRID_ORDER_BACKLOG_MARGIN | 267260 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 45500.0 | None | None | 84.62 | None | stage2_actionable_best_entry |
| C01_LS_ELECTRIC_20240405_GRID_ORDER_MARGIN_BRIDGE | 010120 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 118600.0 | None | None | 131.45 | None | stage2_actionable_best_entry |
| C01_TAIHAN_20240513_CABLE_THEME_NO_MARGIN_BRIDGE | 001440 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 18110.0 | None | None | 15.68 | None | stage2_captured_most_upside |
| R1L14_C01_KSOE_PRICE_ONLY_4B_20230717 | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 128000.0 | None | None | no_valid_stage_transition |
| R1L14_C01_KSOE_STAGE2_20230104 | 009540 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 74400.0 | None | None | 74.73 | None | stage2_actionable_best_entry |
| R1L14_C01_MIPO_PRICE_ONLY_4B_20240731 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | 117500.0 | None | None | no_valid_stage_transition |
| R1L14_C01_MIPO_STAGE2_20240213 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 62700.0 | None | None | 95.85 | None | stage2_actionable_best_entry |
| R1L14_C01_SHI_STAGE2_20230131 | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 5790.0 | None | None | 63.56 | None | stage2_actionable_best_entry |
| R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 80500.0 | None | None | 79.25 | None | stage2_actionable_best_entry |
| R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 130000.0 | None | None | 185.77 | None | stage2_actionable_best_entry |
| R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN | 010140 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 7270.0 | None | None | 68.91 | None | stage2_actionable_best_entry |
| R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE | 100090 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 114300.0 | None | None | 94.66 | None | stage2_actionable_best_entry |
| R1L79-C01-077970-STX-ENGINE-ORDER-BACKLOG-DELIVERY-MARGIN | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11480.0 | None | None | 112.54 | None | stage2_actionable_best_entry |
| R1L79-C01-082740-HANWHA-ENGINE-SHIP-ENGINE-BACKLOG-MARGIN | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 8600.0 | None | None | 97.56 | None | stage2_actionable_best_entry |
| R1L79-C01-241560-DOOSAN-BOBCAT-CONSTRUCTION-EQUIPMENT-BACKLOG-FADE | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| R1L83-C01-077970-STX-ENGINE-MARINE-ENGINE-BACKLOG-MARGIN | 077970 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11480.0 | None | None | 112.54 | None | stage2_actionable_best_entry |
| R1L83-C01-082740-HANWHA-ENGINE-MARINE-ENGINE-BACKLOG-NAME-SHARECOUNT | 082740 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
| R1L83-C01-241560-DOOSAN-BOBCAT-EQUIPMENT-CYCLE-FADE | 241560 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | None | None | None | None | None | no_valid_stage_transition |
