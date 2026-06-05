# C15_MATERIAL_SPREAD_SUPERCYCLE Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `30`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 004020 | 004020 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| 006260 | 006260 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| 010060 | 010060 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L83_001780_ALUKO_PRICE_SPIKE_ROUNDTRIP | 001780 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L83_006110_SAMA_ALUMINUM_FOIL_HIGH_MAE | 006110 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L83_103140_POONGSAN_COPPER_DEFENSE_POSITIVE_CONTROL | 103140 | C15_MATERIAL_SPREAD_SUPERCYCLE | 42200.0 | None | None | 86.97 | None | stage2_actionable_best_entry |
| C15_R4L88_004430_SONGWON_SPECIALTY_CHEM_SPREAD | 004430 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L88_006110_SAMA_ALUMINUM_REBOUND_NO_DEMAND_MARGIN | 006110 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L88_024840_KBI_COPPER_METAL_SUPERCYCLE | 024840 | C15_MATERIAL_SPREAD_SUPERCYCLE | 1641.0 | None | None | 189.15 | None | stage2_actionable_best_entry |
| C15_R4L91_005810_POONGSAN_HOLDINGS_COPPER_HOLDCO | 005810 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L91_006340_DAEWON_COPPER_WIRE_SPREAD | 006340 | C15_MATERIAL_SPREAD_SUPERCYCLE | 1358.0 | None | None | 301.33 | None | stage2_actionable_best_entry |
| C15_R4L91_008350_NAMSUN_ALUMINUM_THEME | 008350 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L92_001430_2024_02_23 | 001430 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L92_004020_2024_02_07 | 004020 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L92_306200_2024_01_24 | 306200 | C15_MATERIAL_SPREAD_SUPERCYCLE | 121800.0 | None | None | 18.1 | None | stage2_captured_most_upside |
| C15_R4L95_001430_2024_02_01 | 001430 | C15_MATERIAL_SPREAD_SUPERCYCLE | 22900.0 | None | None | 19.4 | None | stage2_captured_most_upside |
| C15_R4L95_002240_2024_02_20 | 002240 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L95_005010_2024_02_01 | 005010 | C15_MATERIAL_SPREAD_SUPERCYCLE | 5340.0 | None | None | 15.5 | None | stage2_captured_most_upside |
| C15_R4L98_008260_2024_02_01 | 008260 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | None | None | None | no_valid_stage_transition |
| C15_R4L98_084010_2024_02_01 | 084010 | C15_MATERIAL_SPREAD_SUPERCYCLE | 13480.0 | None | None | 5.7 | None | stage2_captured_most_upside |
| C15_R4L98_104700_2024_02_01 | 104700 | C15_MATERIAL_SPREAD_SUPERCYCLE | 6970.0 | None | None | 81.9 | None | stage2_captured_most_upside |
| R4L90_C15_CHOILALUMINUM_2024_ALUMINUM_THEME_FALSE_STAGE2 | 018470 | C15_MATERIAL_SPREAD_SUPERCYCLE | 2510.0 | None | None | 9.96 | None | stage2_actionable_best_entry |
| R4L90_C15_KBIMETAL_2024_COPPER_SPREAD_MARGIN_BRIDGE_POSITIVE | 024840 | C15_MATERIAL_SPREAD_SUPERCYCLE | 1535.0 | None | None | 209.12 | None | stage2_actionable_best_entry |
| R4L90_C15_SAMAALUMINUM_2024_ALUMINUM_FOIL_EVENT_CAP_4B | 006110 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | 96300.0 | None | None | 4b_good_peak_capture |
| R4L93_C15_HEUNGGOO_2024_OIL_RESOURCE_SPREAD_EVENT_CAP_4B | 024060 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | 19240.0 | None | None | 4b_good_peak_capture |
| R4L93_C15_KGSTEEL_2024_STEEL_COIL_SPREAD_FALSE_STAGE2 | 016380 | C15_MATERIAL_SPREAD_SUPERCYCLE | 7970.0 | None | None | 1.51 | None | stage2_actionable_best_entry |
| R4L93_C15_SEAHSTEELHOLDINGS_2024_STEEL_PIPE_EXPORT_SPREAD_MARGIN_POSITIVE | 003030 | C15_MATERIAL_SPREAD_SUPERCYCLE | 197600.0 | None | None | 21.71 | None | stage2_actionable_best_entry |
| R4L96_C15_HWANGGEUMST_2024_STAINLESS_NICKEL_SPREAD_FALSE_STAGE2 | 032560 | C15_MATERIAL_SPREAD_SUPERCYCLE | 7330.0 | None | None | 2.32 | None | stage2_actionable_best_entry |
| R4L96_C15_NAMSEONALUMINUM_2024_ALUMINUM_POLICY_SPREAD_EVENT_CAP_4B | 008350 | C15_MATERIAL_SPREAD_SUPERCYCLE | None | None | 2515.0 | None | None | 4b_good_peak_capture |
| R4L96_C15_POSCOSTEELION_2024_COATED_STEEL_SPREAD_MARGIN_POSITIVE | 058430 | C15_MATERIAL_SPREAD_SUPERCYCLE | 47350.0 | None | None | 12.57 | None | stage2_actionable_best_entry |
