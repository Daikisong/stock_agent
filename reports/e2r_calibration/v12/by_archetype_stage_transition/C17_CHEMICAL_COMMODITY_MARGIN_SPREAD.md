# C17_CHEMICAL_COMMODITY_MARGIN_SPREAD Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `12`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C17_DAEHAN_006650_2024_03_06_ETHYLENE_POLYMER_SPREAD_BOUNCE_THEN_4C | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | 4c_too_late |
| C17_FOOSUNG_093370_2024_02_15_FLUOROCHEMICAL_SPREAD_FALSE_POSITIVE | 093370 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 9050.0 | None | None | 2.1 | None | stage2_captured_most_upside |
| C17_KUMHOPETRO_011780_2024_01_29_SYNTHETIC_RUBBER_SPREAD_RERATING | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 125400.0 | None | None | 33.17 | None | stage2_actionable_best_entry |
| C17_KUMHO_011780_2024_03_06_SYNTHETIC_RUBBER_SPREAD_RERATING_4B_BOUNDARY | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 144400.0 | None | None | 15.51 | None | stage2_actionable_best_entry |
| C17_LOTTECHEM_011170_2024_03_06_NAPHTHA_ETHYLENE_SPREAD_FALSE_RECOVERY_4C | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 122900.0 | None | None | 2.12 | None | stage2_captured_most_upside |
| C17_R4L93_004000_LOTTE_FINE_CHLORALKALI_DECAY | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_R4L93_014680_HANSOL_SPECIALTY_CHEM_SPREAD | 014680 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 169300.0 | None | None | 26.4 | None | stage2_actionable_best_entry |
| C17_R4L93_120110_KOLON_INDUSTRIES_MATERIALS_DECAY | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| C17_UNID_014830_2024_01_25_CAUSTIC_POTASH_SPREAD_RERATING | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 74900.0 | None | None | 58.48 | None | stage2_actionable_best_entry |
| R4L98_C17_AEKYUNGCHEM_2024_BATTERY_CHEMICAL_EVENT_CAP_4B | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | 16740.0 | None | None | 4b_good_peak_capture |
| R4L98_C17_KUMHOPETRO_2024_SYNTHETIC_RUBBER_SPREAD_MARGIN_BRIDGE_POSITIVE | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 112500.0 | None | None | 48.44 | None | stage2_actionable_best_entry |
| R4L98_C17_LOTTECHEM_2024_BASE_CHEMICAL_RECOVERY_FALSE_STAGE2 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 136900.0 | None | None | 2.85 | None | stage2_actionable_best_entry |
