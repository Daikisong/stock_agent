# Evidence URL Pending Report

v12 잔차 장부입니다. 검증 통과 항목은 rolling calibration에 들어가고, 제약은 guardrail로 남깁니다.
source proxy 또는 evidence URL 한계는 positive patch를 막거나 scope 제한을 강화합니다.

- residual_rows: `27`

| trigger_id | symbol | archetype | verdict | source_proxy_only | evidence_url_pending |
|---|---|---|---|---|---|
| T_R9L10_000270_STAGE2 | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| T_R9L10_000270_4B | 000270 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| R6L41_C22_000810_T1_STAGE2A | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| R6L41_C22_000810_T2_GREEN_COMPARE | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | True | True |
| R6L41_C22_000810_T3_4B_LOCAL | 000810 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4B_too_early | True | True |
| TR_C16_UNION_S2_20230217 | 000910 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_false_positive | True | True |
| TR_C16_GEUMYANG_S2_20230221 | 001570 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late | True | True |
| T_R9L10_005380_STAGE2 | 005380 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_correct | False | True |
| TR_C16_POSCO_S2A_20230410 | 005490 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_correct | True | True |
| R6L41_C22_005830_T1_STAGE2A | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| R6L41_C22_005830_T2_GREEN_COMPARE | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_too_late | True | True |
| R6L41_C22_005830_T3_4B_FULL | 005830 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_correct | True | True |
| TRG_C05_006360_20230629_STAGE4C | 006360 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_4C_should_route_fast_when_quality_cost_break_confirms_margin_gap | True | True |
| R1L10_C02_010120_STAGE2A_2024_01_03 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
| R1L10_C02_010120_4B_WATCH_2024_04_12 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_correct | False | True |
| R4L10_C17_011170_T1 | 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_false_positive | False | True |
| R4L10_C17_011780_T1 | 011780 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| TR_C16_KDINV_S2_20221020 | 012320 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | current_profile_4B_too_late | True | True |
| TRG_C05_028050_20230131_STAGE2_ACTIONABLE | 028050 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_missed_structural_if_C05_has_no_runtime_weight | True | True |
| TRG_C05_047040_20230131_STAGE2_FALSE_POSITIVE | 047040 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | current_profile_false_positive_if_order_headline_scored_without_margin_bridge | True | True |
| R6L41_C22_088350_T1_STAGE2_POLICY_ONLY | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_false_positive | True | True |
| R6L41_C22_088350_T2_4C_WATCH | 088350 | C22_INSURANCE_RATE_CYCLE_RESERVE | current_profile_4C_too_late | True | True |
| T_R9L10_204320_STAGE2 | 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | current_profile_false_positive | False | True |
| R1L10_C02_267260_STAGE2A_2024_01_03 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
| R4L10_C17_298020_T4B | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| R4L10_C17_298020_T1 | 298020 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | current_profile_correct | False | True |
| R1L10_C02_298040_STAGE2A_2024_01_03 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | current_profile_too_late | False | True |
