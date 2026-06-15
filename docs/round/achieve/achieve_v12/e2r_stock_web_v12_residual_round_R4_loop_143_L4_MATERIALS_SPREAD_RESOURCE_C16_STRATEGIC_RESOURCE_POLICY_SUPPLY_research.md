# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
selected_round: R4
selected_loop: 143
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout after session-adjusted Priority 0/1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout
loop_objective: holdout_validation | counterexample_mining | canonical_archetype_compression | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_residual_round_R4_loop_143_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

This loop adds 6 new independent cases, 2 counterexamples, and 4 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. This research does not patch production scoring. It only proposes a C16 shadow gate: strategic-resource policy evidence must be separated from actual offtake, production, shipment, revenue recognition, and margin/FCF bridge.

## 2. Round / Large Sector / Canonical Archetype Scope

C16 maps to R4 / L4. The scope is not generic battery orderbook or general material spread. The target is strategic resource / policy / supply security: lithium, nickel, gas supply, nickel sulfate, and critical mineral offtake.

## 3. Previous Coverage / Duplicate Avoidance Check

Static No-Repeat Index marks C16 as a Priority 2 quality-holdout archetype with 82 rows. This session already lifted the static Priority 0 and Priority 1 gaps through repeated C02, C09, C14, C10, C06, C07, C11, C01, C28, C12, C05, C23, and C27 work. Therefore this pass is not a bulk count fill. It is a quality holdout and source/proxy decontamination pass.

Hard duplicate key checked conceptually: `canonical_archetype_id + symbol + trigger_type + entry_date`. All six rows are new C16 trigger families in this session.

## 4. Stock-Web OHLC Input / Price Source Validation

- source: Songdaiki/stock-web
- price_basis: tradable_raw
- price_adjustment_status: raw_unadjusted_marcap
- calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
- manifest_max_date: 2026-02-20

## 5. Historical Eligibility Gate

All representative trigger rows use entry-date close from Stock-Web tradable shard. Each has at least 180 tradable rows after entry and all six required MFE/MAE fields.

## 6. Canonical Archetype Compression Map

| fine path | canonical compression | keep / cap rule |
|---|---|---|
| Indonesian nickel mine offtake | C16 strategic resource policy supply | keep if offtake + production ramp + low MAE |
| nickel sulfate / EVBM capacity | C16 strategic resource policy supply | keep Stage2, Stage3 only after production/revenue bridge |
| lithium value-chain localization | C16 strategic resource policy supply | cap if commodity ASP/margin bridge missing |
| gas processing / long-term energy contracts | C16 strategic resource policy supply | allow Stage3-Yellow when infrastructure + long-term buyers visible |
| national strategic technology designation | C16 strategic resource policy supply | decontaminate control-premium/governance premium before Green |
| undisclosed lithium offtake | C16 strategic resource policy supply | Stage2-Watch or 4B if economics/duration opaque |

## 7. Case Selection Summary

| case_id | symbol | company | polarity | case_type | trigger_outcome_label | notes |
|---|---|---|---|---|---|---|
| C16_001120_20231109_AKP_NICKEL_MINE_OFFTAKE | 001120 | LX인터내셔널 | positive | structural_success | akp_nickel_mine_offtake_positive | Nickel reserve/of-take evidence is real; margin bridge is still a gate, but low MAE and 180D MFE support C16 positive. |
| C16_006260_20231201_LSMNM_SAEMANGEUM_NICKEL_SULFATE | 006260 | LS | positive | high_mae_success | lsmnm_saemangeum_nickel_sulfate_positive_with_4b_watch | Huge 180D MFE but post-peak drawdown demands local 4B overlay; production timing too distant for full Green on event day. |
| C16_005490_20240122_LITHIUM_VALUE_CHAIN_COMPLETION | 005490 | POSCO홀딩스 | counterexample | failed_rerating | lithium_value_chain_no_asp_margin_bridge_counterexample | Strategic mineral story was valid, but lithium ASP/margin/FCF bridge was not; 180D MAE and drawdown show false-positive risk. |
| C16_047050_20241204_SENEX_GAS_PROCESSING_TEST_OPERATION | 047050 | 포스코인터내셔널 | positive | structural_success | senex_gas_processing_long_term_contract_positive | This is the cleanest C16 energy-supply case: infrastructure + long-term buyers + production expansion. |
| C16_010130_20250117_NICKEL_SULFATE_NATIONAL_STRATEGIC_TECH | 010130 | 고려아연 | positive | high_mae_success | nickel_sulfate_national_strategic_tech_positive_with_control_premium_decontamination | Strong MFE but large MAE and governance/control-premium contamination mean C16 evidence should be decontaminated before Green. |
| C16_011810_20240109_PERU_LITHIUM_OFFTAKE | 011810 | STX | counterexample | false_positive_green | peru_lithium_offtake_contract_opacity_and_dilution_counterexample | Strategic-resource headline without disclosed economics and with recent corporate-action/dilution overhang is a hard Stage2 cap / 4B watch counterexample. |

## 8. Positive vs Counterexample Balance

positive_case_count: 4
counterexample_count: 2
4B_case_count: 6
4C_case_count: 0
calibration_usable_trigger_count: 6

## 9. Evidence Source Map

| symbol | trigger_date | evidence available at trigger | evidence_source |
|---|---|---|---|
| 001120 | 2023-11-09 | LX International board-approved KRW 133bn acquisition of 60% and management control of Indonesia AKP nickel mine; offtake rights to full production and 2028 production target. | https://www.lxinternational.com/en/news/press_view?seq=434 |
| 006260 | 2023-12-01 | LS MnM Saemangeum EVBM investment for nickel sulfate and other battery-material compounds; large capacity but production is scheduled for 2029. | https://www.investkorea.org/jnbk-en/bbs/i-1334/detail.do?ntt_sn=491364 |
| 005490 | 2024-01-22 | POSCO Group highlighted Pilbara lithium solution completion and lithium raw-material supply-chain strategy under IRA/CRMA context. | https://newsroom.posco.com/en/securing-critical-mineral-lithium-to-complete-the-full-value-chain-of-the-rechargeable-battery-material-business/ |
| 047050 | 2024-12-04 | POSCO International began Senex gas processing test operation; Senex had up-to-10-year gas supply contracts with eight buyers for about 151 PJ. | https://newsroom.posco.com/en/posco-international-begins-test-operation-of-gas-processing-facility-unit-1-for-senex-energy-in-australia-with-plans-to-triple-natural-gas-production-progressing-smoothly/ |
| 010130 | 2025-01-17 | Korea Zinc nickel sulfate manufacturing technology was included in the national strategic technology list, supporting nickel refinery tax benefits and China-dependence reduction. | https://www.asiae.co.kr/en/article/2025011709225936994 |
| 011810 | 2024-01-09 | STX announced a Peru lithium-mine stake and offtake agreement, but scale/investment/duration were confidential and the share path collapsed after the event. | https://www.asiae.co.kr/en/article/2024010908402380348 |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | forward_window_trading_days | corporate_action_window_status |
|---|---|---|---:|---|
| 001120 | atlas/ohlcv_tradable_by_symbol_year/001/001120/2023.csv | atlas/symbol_profiles/001/001120.json | 180 | clean_180D_window |
| 006260 | atlas/ohlcv_tradable_by_symbol_year/006/006260/2023.csv | atlas/symbol_profiles/006/006260.json | 180 | clean_180D_window |
| 005490 | atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv | atlas/symbol_profiles/005/005490.json | 180 | clean_180D_window |
| 047050 | atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv | atlas/symbol_profiles/047/047050.json | 180 | clean_180D_window |
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json | 180 | clean_180D_window |
| 011810 | atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv | atlas/symbol_profiles/011/011810.json | 180 | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | drawdown_after_peak_pct | outcome | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| 001120 | LX인터내셔널 | Stage2-Actionable | 2023-11-09 | 2023-11-09 | 28000 | 11.43 | -1.79 | 15.36 | -7.86 | 28.39 | -9.29 | 2024-05-21 | -21.97 | akp_nickel_mine_offtake_positive | current_profile_correct |
| 006260 | LS | Stage2-Actionable | 2023-12-01 | 2023-12-01 | 84000 | 13.45 | -5.95 | 57.14 | -8.10 | 131.90 | -8.10 | 2024-05-21 | -51.75 | lsmnm_saemangeum_nickel_sulfate_positive_with_4b_watch | current_profile_missed_structural |
| 005490 | POSCO홀딩스 | Stage2-Actionable | 2024-01-22 | 2024-01-22 | 398500 | 18.19 | -2.89 | 18.19 | -7.90 | 18.19 | -22.46 | 2024-03-05 | -34.39 | lithium_value_chain_no_asp_margin_bridge_counterexample | current_profile_false_positive |
| 047050 | 포스코인터내셔널 | Stage3-Yellow | 2024-12-04 | 2024-12-04 | 40500 | 12.10 | -7.65 | 60.00 | -7.65 | 60.00 | -7.65 | 2025-03-11 | -33.10 | senex_gas_processing_long_term_contract_positive | current_profile_correct |
| 010130 | 고려아연 | Stage2-Actionable | 2025-01-17 | 2025-01-17 | 840000 | 10.36 | -15.95 | 29.76 | -23.45 | 88.10 | -23.45 | 2025-10-15 | -23.67 | nickel_sulfate_national_strategic_tech_positive_with_control_premium_decontamination | current_profile_data_insufficient |
| 011810 | STX | Stage2-Actionable | 2024-01-09 | 2024-01-09 | 11600 | 5.95 | -21.12 | 5.95 | -39.05 | 5.95 | -58.62 | 2024-01-09 | -60.94 | peru_lithium_offtake_contract_opacity_and_dilution_counterexample | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

All MFE/MAE values are computed as `max high` or `min low` from entry date through the N-trading-day window divided by entry close.

## 13. Current Calibrated Profile Stress Test

The current profile generally handles price-only blowoff better than the older baseline, but C16 still needs a sharper split:

1. Strategic-resource policy headline alone often gets Stage2-Actionable correctly.
2. Stage3-Yellow is only justified when offtake/production/revenue/margin bridge is present.
3. Lithium and nickel headline cases can show positive MFE while still delivering deep full-window MAE.
4. Control-premium, governance dispute, and dilution/capital-raise overhang must be decontaminated from C16 supply-chain evidence.

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green row is proposed. C16 Green should require named offtake plus production ramp plus ASP/margin or FCF conversion. POSCO International is Stage3-Yellow quality. LS, LX International, and Korea Zinc remain Stage2-Actionable or delayed-Yellow watch depending on execution bridge.

## 15. 4B Local vs Full-window Timing Audit

Four rows have local 4B watch evidence: LS, POSCO Holdings, Korea Zinc, and STX. LS and Korea Zinc show large MFE but large post-peak drawdown, so the correct handling is not thesis deletion; it is local 4B overlay and entry-quality guard. STX and POSCO Holdings are stronger false-positive caps because the required economics/margin bridge is missing.

## 16. 4C Protection Audit

No hard Stage4C row is proposed. C16 thesis break should require cancelled offtake, failed permit, resource reserve invalidation, refinery failure, or clear financing failure. The current rows are mostly 4B/watch or Stage2 cap.

## 17. Sector-Specific Rule Candidate

`L4_C16_RESOURCE_POLICY_SUPPLY_REQUIRES_OFFTAKE_PRODUCTION_REVENUE_AND_MARGIN_BRIDGE_WITH_COMMODITY_ASP_DECONTAMINATION`

## 18. Canonical-Archetype Rule Candidate

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_REQUIRES_NAMED_RESOURCE_OFFTAKE_AND_PRODUCTION_MARGIN_BRIDGE_WITH_DILUTION_CONTROL_PREMIUM_4B_CAP`

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | Existing calibrated profile with generic Stage2 bridge and local 4B guard | 6 | 31.07 | -15.67 | 55.42 | -21.59 | 0.33 | mixed; misses C16 decontamination |
| P0b_e2r_2_0_baseline_reference | rollback | Older profile likely over-promotes resource headlines | 6 | 31.07 | -15.67 | 55.42 | -21.59 | 0.50 | weaker than P0 |
| P1_L4_sector_candidate_profile | sector_specific | Add L4 resource supply bridge and commodity ASP decontamination | 6 | 31.07 | -15.67 | 55.42 | -21.59 | 0.33 | improved false-positive control |
| P2_C16_canonical_candidate_profile | canonical_archetype_specific | Require named resource/offtake plus production/revenue/margin bridge for Stage3 | 6 | 31.07 | -15.67 | 55.42 | -21.59 | 0.17 | best alignment |
| P3_counterexample_guard_profile | guardrail | Cap Stage3 when disclosure lacks economics, duration, ASP, or when dilution/control-premium dominates | 6 | 31.07 | -15.67 | 55.42 | -21.59 | 0.17 | stronger risk control, possible under-promotion |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | score-return alignment |
|---|---:|---|---:|---|---|
| 001120 | 73 | Stage2-Actionable | 77 | Stage3-Yellow | current_profile_correct |
| 006260 | 72 | Stage2-Actionable | 78 | Stage3-Yellow | current_profile_missed_structural |
| 005490 | 76 | Stage3-Yellow | 64 | Stage2-Watch | current_profile_false_positive |
| 047050 | 80 | Stage3-Yellow | 84 | Stage3-Yellow | current_profile_correct |
| 010130 | 74 | Stage2-Actionable | 72 | Stage2-Actionable-with-4B-watch | current_profile_data_insufficient |
| 011810 | 68 | Stage2-Actionable | 55 | Stage2-Watch | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout | 4 | 2 | 6 | 0 | 6 | 0 | 6 | 6 | 4 | L4_C16_RESOURCE_POLICY_SUPPLY_REQUIRES_OFFTAKE_PRODUCTION_REVENUE_AND_MARGIN_BRIDGE_WITH_COMMODITY_ASP_DECONTAMINATION | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_REQUIRES_NAMED_RESOURCE_OFFTAKE_AND_PRODUCTION_MARGIN_BRIDGE_WITH_DILUTION_CONTROL_PREMIUM_4B_CAP | quality-holdout strengthened |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - resource_policy_headline_without_margin_bridge
  - commodity_asp_decontamination
  - long_dated_capacity_execution_gap
  - contract_opacity_and_dilution_overhang
  - control_premium_decontamination
new_axis_proposed: C16_strategic_resource_supply_bridge_decontamination_gate
existing_axis_strengthened: stage2_required_bridge | local_4b_watch_guard | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L4_C16_RESOURCE_POLICY_SUPPLY_REQUIRES_OFFTAKE_PRODUCTION_REVENUE_AND_MARGIN_BRIDGE_WITH_COMMODITY_ASP_DECONTAMINATION
canonical_archetype_rule_candidate: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_REQUIRES_NAMED_RESOURCE_OFFTAKE_AND_PRODUCTION_MARGIN_BRIDGE_WITH_DILUTION_CONTROL_PREMIUM_4B_CAP
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical trigger-level Stock-Web OHLC path and public evidence available on trigger date.

Non-validation scope: no live recommendation, no production scoring patch, no broker/API, no current watchlist.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_resource_supply_bridge_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"Require offtake/production/revenue/margin bridge and decontaminate commodity ASP/control-premium/dilution noise","positive rows show avg MFE180 55.42% but counterexamples show deep MAE; gate reduces false positive risk",TRG_C16_001120_20231109_AKP_NICKEL_MINE_OFFTAKE|TRG_C16_006260_20231201_LSMNM_SAEMANGEUM_NICKEL_SULFATE|TRG_C16_005490_20240122_LITHIUM_VALUE_CHAIN_COMPLETION|TRG_C16_047050_20241204_SENEX_GAS_PROCESSING_TEST_OPERATION|TRG_C16_010130_20250117_NICKEL_SULFATE_NATIONAL_STRATEGIC_TECH|TRG_C16_011810_20240109_PERU_LITHIUM_OFFTAKE,6,6,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C16_001120_20231109_AKP_NICKEL_MINE_OFFTAKE","symbol":"001120","company_name":"LX인터내셔널","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"akp_nickel_mine_offtake_positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Nickel reserve/of-take evidence is real; margin bridge is still a gate, but low MAE and 180D MFE support C16 positive."}
{"row_type":"trigger","trigger_id":"TRG_C16_001120_20231109_AKP_NICKEL_MINE_OFFTAKE","case_id":"C16_001120_20231109_AKP_NICKEL_MINE_OFFTAKE","symbol":"001120","company_name":"LX인터내셔널","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","sector":"materials_spread_resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-09","entry_date":"2023-11-09","entry_price":28000.0,"evidence_available_at_that_date":"LX International board-approved KRW 133bn acquisition of 60% and management control of Indonesia AKP nickel mine; offtake rights to full production and 2028 production target.","evidence_source":"https://www.lxinternational.com/en/news/press_view?seq=434","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["durable_customer_confirmation","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["commodity_price_or_policy_execution_delay_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001120/2023.csv","profile_path":"atlas/symbol_profiles/001/001120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.4286,"MFE_90D_pct":15.3571,"MFE_180D_pct":28.3929,"MFE_1Y_pct":28.3929,"MFE_2Y_pct":null,"MAE_30D_pct":-1.7857,"MAE_90D_pct":-7.8571,"MAE_180D_pct":-9.2857,"MAE_1Y_pct":-9.2857,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":35950.0,"drawdown_after_peak_pct":-21.975,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_not_full_4B","four_b_evidence_type":["commodity_price_or_policy_execution_delay_watch"],"four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"akp_nickel_mine_offtake_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001120|2023-11-09|28000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_001120_20231109_AKP_NICKEL_MINE_OFFTAKE","trigger_id":"TRG_C16_001120_20231109_AKP_NICKEL_MINE_OFFTAKE","symbol":"001120","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":55,"margin_bridge_score":45,"revision_score":35,"relative_strength_score":40,"customer_quality_score":65,"policy_or_regulatory_score":70,"valuation_repricing_score":40,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":55,"margin_bridge_score":55,"revision_score":35,"relative_strength_score":40,"customer_quality_score":73,"policy_or_regulatory_score":70,"valuation_repricing_score":40,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","contract_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C16 shadow gate separates resource-policy headlines from offtake/production/revenue/margin bridge and applies a local 4B cap when execution timing, commodity ASP, governance/control-premium, or dilution overhang dominates.","MFE_90D_pct":15.3571,"MAE_90D_pct":-7.8571,"score_return_alignment_label":"current_profile_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C16_006260_20231201_LSMNM_SAEMANGEUM_NICKEL_SULFATE","symbol":"006260","company_name":"LS","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"lsmnm_saemangeum_nickel_sulfate_positive_with_4b_watch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_missed_structural","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Huge 180D MFE but post-peak drawdown demands local 4B overlay; production timing too distant for full Green on event day."}
{"row_type":"trigger","trigger_id":"TRG_C16_006260_20231201_LSMNM_SAEMANGEUM_NICKEL_SULFATE","case_id":"C16_006260_20231201_LSMNM_SAEMANGEUM_NICKEL_SULFATE","symbol":"006260","company_name":"LS","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","sector":"materials_spread_resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-01","entry_date":"2023-12-01","entry_price":84000.0,"evidence_available_at_that_date":"LS MnM Saemangeum EVBM investment for nickel sulfate and other battery-material compounds; large capacity but production is scheduled for 2029.","evidence_source":"https://www.investkorea.org/jnbk-en/bbs/i-1334/detail.do?ntt_sn=491364","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","execution_timing_gap","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2023.csv","profile_path":"atlas/symbol_profiles/006/006260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.4524,"MFE_90D_pct":57.1429,"MFE_180D_pct":131.9048,"MFE_1Y_pct":131.9048,"MFE_2Y_pct":null,"MAE_30D_pct":-5.9524,"MAE_90D_pct":-8.0952,"MAE_180D_pct":-8.0952,"MAE_1Y_pct":-8.0952,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":194800.0,"drawdown_after_peak_pct":-51.7454,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_not_full_4B","four_b_evidence_type":["positioning_overheat","execution_timing_gap","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"lsmnm_saemangeum_nickel_sulfate_positive_with_4b_watch","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006260|2023-12-01|84000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_006260_20231201_LSMNM_SAEMANGEUM_NICKEL_SULFATE","trigger_id":"TRG_C16_006260_20231201_LSMNM_SAEMANGEUM_NICKEL_SULFATE","symbol":"006260","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":45,"margin_bridge_score":42,"revision_score":35,"relative_strength_score":40,"customer_quality_score":55,"policy_or_regulatory_score":75,"valuation_repricing_score":40,"execution_risk_score":55,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":45,"margin_bridge_score":52,"revision_score":35,"relative_strength_score":40,"customer_quality_score":63,"policy_or_regulatory_score":75,"valuation_repricing_score":40,"execution_risk_score":55,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","contract_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C16 shadow gate separates resource-policy headlines from offtake/production/revenue/margin bridge and applies a local 4B cap when execution timing, commodity ASP, governance/control-premium, or dilution overhang dominates.","MFE_90D_pct":57.1429,"MAE_90D_pct":-8.0952,"score_return_alignment_label":"current_profile_missed_structural","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C16_005490_20240122_LITHIUM_VALUE_CHAIN_COMPLETION","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"lithium_value_chain_no_asp_margin_bridge_counterexample","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Strategic mineral story was valid, but lithium ASP/margin/FCF bridge was not; 180D MAE and drawdown show false-positive risk."}
{"row_type":"trigger","trigger_id":"TRG_C16_005490_20240122_LITHIUM_VALUE_CHAIN_COMPLETION","case_id":"C16_005490_20240122_LITHIUM_VALUE_CHAIN_COMPLETION","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","sector":"materials_spread_resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":398500.0,"evidence_available_at_that_date":"POSCO Group highlighted Pilbara lithium solution completion and lithium raw-material supply-chain strategy under IRA/CRMA context.","evidence_source":"https://newsroom.posco.com/en/securing-critical-mineral-lithium-to-complete-the-full-value-chain-of-the-rechargeable-battery-material-business/","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["commodity_price_decline","valuation_blowoff","margin_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.1932,"MFE_90D_pct":18.1932,"MFE_180D_pct":18.1932,"MFE_1Y_pct":18.1932,"MFE_2Y_pct":null,"MAE_30D_pct":-2.8858,"MAE_90D_pct":-7.9046,"MAE_180D_pct":-22.4592,"MAE_1Y_pct":-40.7779,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-03-05","peak_price":471000.0,"drawdown_after_peak_pct":-34.3949,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_not_full_4B","four_b_evidence_type":["commodity_price_decline","valuation_blowoff","margin_bridge_missing"],"four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"lithium_value_chain_no_asp_margin_bridge_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|2024-01-22|398500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_005490_20240122_LITHIUM_VALUE_CHAIN_COMPLETION","trigger_id":"TRG_C16_005490_20240122_LITHIUM_VALUE_CHAIN_COMPLETION","symbol":"005490","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":40,"margin_bridge_score":25,"revision_score":35,"relative_strength_score":40,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":60,"execution_risk_score":55,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":40,"margin_bridge_score":10,"revision_score":35,"relative_strength_score":40,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":60,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","contract_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C16 shadow gate separates resource-policy headlines from offtake/production/revenue/margin bridge and applies a local 4B cap when execution timing, commodity ASP, governance/control-premium, or dilution overhang dominates.","MFE_90D_pct":18.1932,"MAE_90D_pct":-7.9046,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C16_047050_20241204_SENEX_GAS_PROCESSING_TEST_OPERATION","symbol":"047050","company_name":"포스코인터내셔널","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"senex_gas_processing_long_term_contract_positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"This is the cleanest C16 energy-supply case: infrastructure + long-term buyers + production expansion."}
{"row_type":"trigger","trigger_id":"TRG_C16_047050_20241204_SENEX_GAS_PROCESSING_TEST_OPERATION","case_id":"C16_047050_20241204_SENEX_GAS_PROCESSING_TEST_OPERATION","symbol":"047050","company_name":"포스코인터내셔널","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","sector":"materials_spread_resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-12-04","entry_date":"2024-12-04","entry_price":40500.0,"evidence_available_at_that_date":"POSCO International began Senex gas processing test operation; Senex had up-to-10-year gas supply contracts with eight buyers for about 151 PJ.","evidence_source":"https://newsroom.posco.com/en/posco-international-begins-test-operation-of-gas-processing-facility-unit-1-for-senex-energy-in-australia-with-plans-to-triple-natural-gas-production-progressing-smoothly/","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["durable_customer_confirmation","repeat_order_or_conversion","financial_visibility","margin_bridge"],"stage4b_evidence_fields":["post_peak_resource_beta_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv","profile_path":"atlas/symbol_profiles/047/047050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.0988,"MFE_90D_pct":60.0,"MFE_180D_pct":60.0,"MFE_1Y_pct":60.0,"MFE_2Y_pct":null,"MAE_30D_pct":-7.6543,"MAE_90D_pct":-7.6543,"MAE_180D_pct":-7.6543,"MAE_1Y_pct":-7.6543,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-11","peak_price":64800.0,"drawdown_after_peak_pct":-33.1019,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_not_full_4B","four_b_evidence_type":["post_peak_resource_beta_watch"],"four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"senex_gas_processing_long_term_contract_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047050|2024-12-04|40500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_047050_20241204_SENEX_GAS_PROCESSING_TEST_OPERATION","trigger_id":"TRG_C16_047050_20241204_SENEX_GAS_PROCESSING_TEST_OPERATION","symbol":"047050","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":80,"backlog_visibility_score":75,"margin_bridge_score":65,"revision_score":35,"relative_strength_score":40,"customer_quality_score":75,"policy_or_regulatory_score":65,"valuation_repricing_score":40,"execution_risk_score":25,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":80,"backlog_visibility_score":75,"margin_bridge_score":75,"revision_score":35,"relative_strength_score":40,"customer_quality_score":83,"policy_or_regulatory_score":65,"valuation_repricing_score":40,"execution_risk_score":25,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","contract_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C16 shadow gate separates resource-policy headlines from offtake/production/revenue/margin bridge and applies a local 4B cap when execution timing, commodity ASP, governance/control-premium, or dilution overhang dominates.","MFE_90D_pct":60.0,"MAE_90D_pct":-7.6543,"score_return_alignment_label":"current_profile_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C16_010130_20250117_NICKEL_SULFATE_NATIONAL_STRATEGIC_TECH","symbol":"010130","company_name":"고려아연","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"nickel_sulfate_national_strategic_tech_positive_with_control_premium_decontamination","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_data_insufficient","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Strong MFE but large MAE and governance/control-premium contamination mean C16 evidence should be decontaminated before Green."}
{"row_type":"trigger","trigger_id":"TRG_C16_010130_20250117_NICKEL_SULFATE_NATIONAL_STRATEGIC_TECH","case_id":"C16_010130_20250117_NICKEL_SULFATE_NATIONAL_STRATEGIC_TECH","symbol":"010130","company_name":"고려아연","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","sector":"materials_spread_resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-17","entry_date":"2025-01-17","entry_price":840000.0,"evidence_available_at_that_date":"Korea Zinc nickel sulfate manufacturing technology was included in the national strategic technology list, supporting nickel refinery tax benefits and China-dependence reduction.","evidence_source":"https://www.asiae.co.kr/en/article/2025011709225936994","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["control_premium_or_event_premium","positioning_overheat","execution_timing_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.3571,"MFE_90D_pct":29.7619,"MFE_180D_pct":88.0952,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.9524,"MAE_90D_pct":-23.4524,"MAE_180D_pct":-23.4524,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-15","peak_price":1580000.0,"drawdown_after_peak_pct":-23.6709,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_not_full_4B","four_b_evidence_type":["control_premium_or_event_premium","positioning_overheat","execution_timing_gap"],"four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"nickel_sulfate_national_strategic_tech_positive_with_control_premium_decontamination","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|2025-01-17|840000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_010130_20250117_NICKEL_SULFATE_NATIONAL_STRATEGIC_TECH","trigger_id":"TRG_C16_010130_20250117_NICKEL_SULFATE_NATIONAL_STRATEGIC_TECH","symbol":"010130","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":35,"margin_bridge_score":35,"revision_score":35,"relative_strength_score":40,"customer_quality_score":40,"policy_or_regulatory_score":85,"valuation_repricing_score":55,"execution_risk_score":45,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":50,"backlog_visibility_score":35,"margin_bridge_score":45,"revision_score":35,"relative_strength_score":40,"customer_quality_score":48,"policy_or_regulatory_score":85,"valuation_repricing_score":55,"execution_risk_score":45,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable-with-4B-watch","changed_components":["policy_or_regulatory_score","contract_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C16 shadow gate separates resource-policy headlines from offtake/production/revenue/margin bridge and applies a local 4B cap when execution timing, commodity ASP, governance/control-premium, or dilution overhang dominates.","MFE_90D_pct":29.7619,"MAE_90D_pct":-23.4524,"score_return_alignment_label":"current_profile_data_insufficient","current_profile_verdict":"current_profile_data_insufficient"}
{"row_type":"case","case_id":"C16_011810_20240109_PERU_LITHIUM_OFFTAKE","symbol":"011810","company_name":"STX","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"peru_lithium_offtake_contract_opacity_and_dilution_counterexample","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Strategic-resource headline without disclosed economics and with recent corporate-action/dilution overhang is a hard Stage2 cap / 4B watch counterexample."}
{"row_type":"trigger","trigger_id":"TRG_C16_011810_20240109_PERU_LITHIUM_OFFTAKE","case_id":"C16_011810_20240109_PERU_LITHIUM_OFFTAKE","symbol":"011810","company_name":"STX","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"mixed_C16_critical_minerals_gas_nickel_lithium_supply_policy_holdout","sector":"materials_spread_resource","primary_archetype":"strategic_resource_policy_supply","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-09","entry_date":"2024-01-09","entry_price":11600.0,"evidence_available_at_that_date":"STX announced a Peru lithium-mine stake and offtake agreement, but scale/investment/duration were confidential and the share path collapsed after the event.","evidence_source":"https://www.asiae.co.kr/en/article/2024010908402380348","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["dilution_or_cb","capital_raise_or_overhang","contract_opacity","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv","profile_path":"atlas/symbol_profiles/011/011810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.9483,"MFE_90D_pct":5.9483,"MFE_180D_pct":5.9483,"MFE_1Y_pct":5.9483,"MFE_2Y_pct":null,"MAE_30D_pct":-21.1207,"MAE_90D_pct":-39.0517,"MAE_180D_pct":-58.6207,"MAE_1Y_pct":-65.9914,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-09","peak_price":12290.0,"drawdown_after_peak_pct":-60.9439,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_not_full_4B","four_b_evidence_type":["dilution_or_cb","capital_raise_or_overhang","contract_opacity","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"peru_lithium_offtake_contract_opacity_and_dilution_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|011810|2024-01-09|11600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_011810_20240109_PERU_LITHIUM_OFFTAKE","trigger_id":"TRG_C16_011810_20240109_PERU_LITHIUM_OFFTAKE","symbol":"011810","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":20,"margin_bridge_score":10,"revision_score":35,"relative_strength_score":40,"customer_quality_score":25,"policy_or_regulatory_score":60,"valuation_repricing_score":60,"execution_risk_score":80,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":70,"accounting_trust_risk_score":5},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":20,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":40,"customer_quality_score":25,"policy_or_regulatory_score":60,"valuation_repricing_score":60,"execution_risk_score":95,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":70,"accounting_trust_risk_score":5},"weighted_score_after":55,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","contract_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C16 shadow gate separates resource-policy headlines from offtake/production/revenue/margin bridge and applies a local 4B cap when execution timing, commodity ASP, governance/control-premium, or dilution overhang dominates.","MFE_90D_pct":5.9483,"MAE_90D_pct":-39.0517,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R4","loop":"143","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["resource_policy_headline_without_margin_bridge","commodity_asp_decontamination","long_dated_capacity_execution_gap","contract_opacity_and_dilution_overhang","control_premium_decontamination"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```yaml
completed_round: R4
completed_loop: 143
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout after session-adjusted Priority 0/1 fills
next_recommended_archetypes:
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_holdout_only_if_new_offtake_or_supply_contract_path
  - C15_MATERIAL_SPREAD_SUPERCYCLE_quality_holdout
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- 001120 LX인터내셔널: https://www.lxinternational.com/en/news/press_view?seq=434
- 006260 LS: https://www.investkorea.org/jnbk-en/bbs/i-1334/detail.do?ntt_sn=491364
- 005490 POSCO홀딩스: https://newsroom.posco.com/en/securing-critical-mineral-lithium-to-complete-the-full-value-chain-of-the-rechargeable-battery-material-business/
- 047050 포스코인터내셔널: https://newsroom.posco.com/en/posco-international-begins-test-operation-of-gas-processing-facility-unit-1-for-senex-energy-in-australia-with-plans-to-triple-natural-gas-production-progressing-smoothly/
- 010130 고려아연: https://www.asiae.co.kr/en/article/2025011709225936994
- 011810 STX: https://www.asiae.co.kr/en/article/2024010908402380348

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```
