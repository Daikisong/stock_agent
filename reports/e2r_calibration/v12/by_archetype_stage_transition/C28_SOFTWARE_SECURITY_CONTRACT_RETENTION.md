# C28_SOFTWARE_SECURITY_CONTRACT_RETENTION Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `23`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 012510 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | no_valid_stage_transition |
| 030520 | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | no_valid_stage_transition |
| 053800 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | no_valid_stage_transition |
| 136540 | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | no_valid_stage_transition |
| 263860 | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | no_valid_stage_transition |
| C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | no_valid_stage_transition |
| C28_DOUZONE_2020_CLOUD_ERP_RETENTION | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 87900.0 | 126500.0 | None | 54.7214 | None | green_too_late |
| C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 11770.0 | 17490.0 | None | 49.8761 | None | green_too_late |
| C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 14700.0 | 22550.0 | None | 61.2248 | None | green_too_late |
| R13L39_C28_012510_DOZON_CLOUD_ERP_RETENTION | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 63900.0 | 90000.0 | None | 93.2732 | None | green_too_late |
| R13L39_C28_053800_AHNLAB_POLITICAL_SECURITY_ASSOCIATION | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 86500.0 | None | 145000.0 | 152.6017 | 44.318 | 4c_too_late |
| R13L39_C28_131370_RSUPPORT_REMOTE_WORK_DEMAND_SHOCK | 131370 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 3040.0 | None | 19950.0 | 677.9844 | 82.0447 | stage2_actionable_best_entry |
| R13L39_C28_263860_GENIANS_ZERO_TRUST_EDR | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 9700.0 | None | 16680.0 | 81.8636 | 87.9008 | stage2_actionable_best_entry |
| R13L54_C28_042510_RAON_IDENTITY_2022 | 042510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | 4c_too_late |
| R13L54_C28_067920_IGLOO_SECURITY_OPS_2021 | 067920 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 6040.0 | 7890.0 | None | 47.52 | None | green_too_late |
| R13L54_C28_184230_SGA_SOLUTIONS_2021 | 184230 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 1235.0 | None | 2065.0 | 83.0 | 80.9717 | stage2_actionable_best_entry |
| R13L54_C28_203650_DREAM_QUANTUM_2023 | 203650 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | 3790.0 | None | None | no_valid_stage_transition |
| R13L54_C28_356890_CYBERONE_MSS_2023 | 356890 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | 13130.0 | None | None | no_valid_stage_transition |
| R8L12_C28_012510_DUZON_CLOUD_2020 | 012510 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 88700.0 | None | None | 53.3117 | None | stage2_actionable_best_entry |
| R8L12_C28_030520_HANCOM_THEME_PREMIUM_2021 | 030520 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | no_valid_stage_transition |
| R8L12_C28_053800_AHNLAB_POLITICAL_EVENT_2022 | 053800 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | None | None | None | None | None | no_valid_stage_transition |
| R8L12_C28_136540_WINS_CONTRACT_RETENTION_NO_EXPLOSION_2020 | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 15650.0 | None | None | 17.6 | None | stage2_captured_most_upside |
| R8L12_C28_263860_GENIANS_EDR_2023 | 263860 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 9900.0 | None | None | 78.2144 | None | stage2_actionable_best_entry |
