# C17_CHEMICAL_COMMODITY_MARGIN_SPREAD Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `19`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| CASE_R4L72_C17_006650_DAEHAN_4B_OVERLAY | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | 393500.0 | None | None | no_valid_stage_transition |
| CASE_R4L72_C17_006650_DAEHAN_REOPENING_SPREAD_BLOWOFF_FALSE_PROMOTION | 006650 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| CASE_R4L72_C17_010060_OCI_POLYSILICON_SPREAD_STRUCTURAL | 010060 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 114000.0 | None | None | 48.25 | None | stage2_actionable_best_entry |
| CASE_R4L72_C17_011170_LOTTECHEM_REOPENING_SPREAD_BETA_FALSE_STAGE3 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| CASE_R4L72_C17_011780_KUMHO_4B_POST_PEAK_OVERLAY | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | 281000.0 | None | None | no_valid_stage_transition |
| CASE_R4L72_C17_011780_KUMHO_NB_LATEX_STRUCTURAL_MARGIN_BRIDGE | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 94200.0 | None | None | 216.88 | None | stage2_actionable_best_entry |
| CASE_R4L76_C17_001390_KG_CHEM_FERTILIZER_THEME_FALSE_PROMOTION | 001390 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| CASE_R4L76_C17_004000_LOTTE_FINE_ECH_CAUSTIC_MARGIN_BRIDGE | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 72500.0 | None | 98500.0 | 40.0059 | 89.642 | 4b_good_peak_capture |
| CASE_R4L76_C17_298020_HYOSUNG_TNC_SPANDEX_MARGIN_BRIDGE | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 155500.0 | None | 881000.0 | 519.3062 | 89.8429 | 4b_good_peak_capture |
| CASE_R4L76_C17_298050_HS_ADV_MATERIALS_TIRECORD_HIGH_MAE | 298050 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 614000.0 | None | None | 42.83 | None | stage2_actionable_best_entry |
| R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE | 004000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 73300.0 | None | None | 38.47 | None | stage2_actionable_best_entry |
| R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 67900.0 | None | None | 40.94 | None | stage2_actionable_best_entry |
| R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE | 161000 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 26650.0 | None | None | 4.32 | None | stage2_actionable_best_entry |
| R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE | 002380 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 233500.0 | None | None | 47.75 | None | stage2_actionable_best_entry |
| R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE | 009830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 35000.0 | None | None | 2.43 | None | stage2_actionable_best_entry |
| R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE | 014680 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 210500.0 | None | None | 1.66 | None | stage2_actionable_best_entry |
| R4L85-C17-01 | 014680 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R4L85-C17-02 | 005950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
| R4L85-C17-03 | 069260 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | None | None | None | None | None | no_valid_stage_transition |
