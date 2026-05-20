# Round 272 R3 Loop 13 Battery EV Green Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_272.md
- round_id: round_200
- large_sector: BATTERY_EV_GREEN
- cases: 8
- success_candidate: 3
- event_premium: 1
- failed_rerating: 2
- hard_4c_reference: 2
- hard_4c_case_count: 2
- Stage 3 dated cases: 0
- 4B-watch cases: 6
- 4C-watch/hard cases: 4
- price_moved_without_evidence: 2
- evidence_good_but_price_failed: 3
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r3_loop13_lnf_tesla_4680_contract_collapse | L&F | hard_4C_contract_collapse | 2023-02-01 |  |  | 2025-12-29 | thesis_break | Tesla 이름과 계약금액만으로 Green을 주면 안 된다. 실제 call-off가 실패하면 계약은 hard 4C가 된다. |
| r3_loop13_lges_tesla_lfp_ess_stage2 | LG Energy Solution | success_candidate_stage2_not_green | 2025-07-30 |  |  |  | success_candidate | 좋은 Stage 2 계약이지만 GWh, 납품, 가동률, 마진, 보조금 제외 OP 전에는 Green이 아니다. |
| r3_loop13_lges_ira_subsidy_op_quality_gate | LG Energy Solution | evidence_good_but_quality_gate_failed | 2025-07-25 |  |  | 2025-07-25 | evidence_good_but_price_failed | 겉보기 OP보다 보조금 제외 OP를 봐야 한다. 예: 492B OP 중 ex-IRA OP가 1.4B면 Green 품질이 아니다. |
| r3_loop13_lgchem_lges_stake_sale_capital_recycling | LG Chem | success_candidate_capital_recycling_watch | 2025-10-01 |  |  |  | success_candidate_capital_recycling_watch | 지분매각은 Green이 아니라 자본재활용 Stage 2다. ROIC와 부채감축, 주주환원, 소재마진이 확인되어야 한다. |
| r3_loop13_samsung_sdi_tesla_ess_unconfirmed_report | Samsung SDI | event_premium_unconfirmed_report | 2025-11-03 |  | 2025-11-03 |  | event_premium | 회사가 '결정된 것 없다'고 한 보도는 signed contract가 아니다. Green 대신 event premium으로 둔다. |
| r3_loop13_ecopro_materials_precursor_demand_break | EcoPro Materials | failed_rerating_precursor_demand_break | 2023-11-01 |  | 2023-11-01 | 2024-06-14 | failed_rerating | IPO와 수직계열화 story는 고객주문, 가동률, 마진, FCF를 대신하지 못한다. |
| r3_loop13_aricell_sconnect_battery_safety_hard_reference | Aricell / S-Connect | hard_4C_safety_reference |  |  |  | 2024-06-24 | thesis_break | 배터리 업종에서 안전·품질 사고는 매출 성장보다 먼저 보는 hard gate다. |
| r3_loop13_feoc_graphite_policy_relief | Korea FEOC / graphite supply-chain policy relief basket | success_candidate_policy_relief | 2024-05-08 |  |  |  | success_candidate_policy_relief | FEOC/graphite 정책은 섹터 relief다. 실제 탈중국 공급계약, 고객 인증, 마진 전에는 회사 Green이 아니다. |

## Interpretation
- R3 Stage 3 is not the word Tesla, ESS, LFP, IRA, graphite, policy, or battery material.
- L&F/Tesla is hard 4C because the contract value collapsed from $2.9B to $7,386.
- LGES/Tesla LFP ESS is Stage 2, not Green, until GWh, shipment, utilization, margin, ex-subsidy OP and FCF confirm.
- LGES Q2 shows headline OP can fail quality gates when ex-IRA OP is nearly absent.
- Samsung SDI/Tesla ESS is event premium while company confirmation is missing.
- Aricell/S-Connect is a battery safety hard reference: safety/quality can override growth narratives.
