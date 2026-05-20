# Round 259 R3 Loop 12 Battery / EV / Green Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_259.md
- round_id: round_187
- large_sector: BATTERY_EV_GREEN
- cases: 8
- success_candidate: 4
- failed_rerating: 3
- thesis_break_cases: 1
- hard_4c_case_count: 1
- 4C-watch or hard cases: 6
- Stage 3 dated cases: 0
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage2 | stage3 | 4B | 4C | round alignment | note |
|---|---|---|---|---|---|---|---|---|
| r3_loop12_samsung_sdi_starplus_share_sale_4c_watch | Samsung SDI | failed_rerating | 2025-04-09 |  | 2025-04-09 | 2026-02-10 | failed_rerating_4C_watch | 미국 현지화 CAPEX와 JV는 수요·희석·고객 이탈 리스크가 남으면 Green이 아니다. |
| r3_loop12_lges_contract_quality_ultium_utilization_break | LG Energy Solution | 4c_thesis_break |  |  |  | 2025-12-17 | thesis_break | 계약 취소와 공장 restart uncertainty가 겹친 이번 라운드의 확정 hard 4C다. |
| r3_loop12_skon_ford_jv_split_ess_pivot | SK On / SK Innovation | success_candidate | 2025-09-03 |  |  | 2025-12-11 | 4C_watch_plus_success_candidate | Ford JV split은 EV 논리 훼손이고, Flatiron ESS는 계약금액·가동률·마진·FCF 전 Stage 2다. |
| r3_loop12_battery_supply_chain_ford_demand_shock | POSCO Future M / SK IE Technology / EcoPro Materials / battery supply-chain basket | failed_rerating |  |  |  | 2025-12-16 | thesis_break_watch | 셀 업체보다 소재·분리막·전구체가 고객 EV 전략 변화에 더 민감하게 빠질 수 있다. |
| r3_loop12_sk_group14_silicon_anode_optional | SK / Group14 Technologies | success_candidate | 2025-08-20 |  |  |  | success_candidate | 투자와 소재 optionality는 Stage 2다. 고객 offtake·가동률·마진·SK 지분가치 전 Green이 아니다. |
| r3_loop12_hanwha_qcells_solar_uflpa_4c_watch | Hanwha Qcells / Hanwha Solutions exposure | success_candidate | 2024-08-08 |  |  | 2025-11-08 | success_candidate_plus_4C_watch | DOE loan과 현지화는 Stage 2다. component flow와 utilization이 막히면 4C-watch다. |
| r3_loop12_hyundai_hydrogen_fuelcell_capex | Hyundai Motor hydrogen fuel-cell plant | success_candidate | 2025-10-30 |  |  |  | success_candidate | 수소 fuel-cell CAPEX는 Stage 2다. offtake·가동률·수소경제성·마진·FCF 전 Green이 아니다. |
| r3_loop12_hyundai_lg_georgia_factory_visa_execution_watch | Hyundai-LG Georgia battery plant / HL-GA Battery | failed_rerating |  |  |  |  | thesis_break_watch | 공장과 자본만으로 부족하다. visa와 숙련 인력 execution이 막히면 startup이 지연된다. |

## Interpretation
- R3 Stage 3 is not `EV, ESS, hydrogen, solar, or localization is good`. It needs call-off, GWh, delivery, utilization, OPM, FCF, and cleared execution risks.
- LGES Ford/Freudenberg is the confirmed hard 4C in this round because expected revenue and utilization visibility broke.
- Samsung SDI, SK On/Ford, Qcells, and Hyundai-LG Georgia are 4C-watch cases, not forced hard 4C unless customer exit, license, restart, or revenue impairment is confirmed.
- SK/Group14 and Hyundai hydrogen are Stage 2 optionality cases. They need offtake, utilization, margin, and FCF before Green.
