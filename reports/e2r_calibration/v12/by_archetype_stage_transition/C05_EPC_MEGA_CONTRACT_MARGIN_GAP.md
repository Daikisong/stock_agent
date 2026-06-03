# C05_EPC_MEGA_CONTRACT_MARGIN_GAP Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `10`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| R1L72_C05_023960_20230421_EPC_CONTRACT_PRICE_SPIKE_MARGIN_WEAK | 023960 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 2695.0 | None | None | 43.23 | None | stage2_actionable_best_entry |
| R1L72_C05_083650_20230331_POWER_PLANT_BOILER_ORDER_BRIDGE_4B | 083650 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 7720.0 | None | None | 51.17 | None | stage2_actionable_best_entry |
| R1L72_C05_100840_20230421_PLANT_EQUIPMENT_ORDER_MARGIN_CONVERSION | 100840 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 21800.0 | None | None | 50.0 | None | stage2_actionable_best_entry |
| R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE | 011560 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 8560.0 | None | None | 74.53 | None | stage2_actionable_best_entry |
| R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY | 053690 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 16700.0 | None | None | 15.45 | None | stage2_actionable_best_entry |
| R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START | 097230 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 3540.0 | None | None | 6.64 | None | stage2_actionable_best_entry |
| R1L84-C05-01 | 053690 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 16690.0 | None | None | 16.84 | None | stage2_actionable_best_entry |
| R1L84-C05-02 | 054930 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| R1L84-C05-03 | 002150 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
| R1L84-C05-04 | 023350 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | None | None | None | None | None | no_valid_stage_transition |
