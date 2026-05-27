# C14_EV_DEMAND_SLOWDOWN_4B_4C Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `19`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C14_ECOPROBM_20240725_HARD4C | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_LNF_20240725_HARD4C | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_POSCOFM_20231025_BROAD_OEM_COUNTEREX | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_POSCOFM_20240725_HARD4C | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R13L10C14_ECOPROBM_247540_20240726 | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R13L10C14_LGES_373220_20240725 | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R13L10C14_POSCOFUTUREM_003670_20240726 | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023 | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 560000.0 | None | None | 4b_good_peak_capture |
| R13L55_C14_066970_LNF_BLOWOFF_2023 | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 263000.0 | None | None | 4b_good_peak_capture |
| R13L55_C14_247540_ECOPROBM_BLOWOFF_2023 | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 455000.0 | None | None | 4b_good_peak_capture |
| R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023 | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L68_C14_006400_20240731_EU_DEMAND_GUIDANCE_TOO_EARLY_4C | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L68_C14_066970_20241220_REPEATED_MARGIN_HARD4C | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L68_C14_247540_20241106_CATHODE_POLICY_DEMAND_HARD4C | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L68_C14_373220_20241115_CELL_DEMAND_HARD4C_COUNTEREXAMPLE | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L71_C14_006400_20240625_SDI_EUROPE_EXPOSURE_4C | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L71_C14_066970_20240125_LF_LITHIUM_PRICE_ONLY_COUNTEREXAMPLE | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L71_C14_247540_20241028_ECOPROBM_CATHODE_READTHROUGH | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| R3L71_C14_373220_20241028_LGES_CAPEX_CUT_4C | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
