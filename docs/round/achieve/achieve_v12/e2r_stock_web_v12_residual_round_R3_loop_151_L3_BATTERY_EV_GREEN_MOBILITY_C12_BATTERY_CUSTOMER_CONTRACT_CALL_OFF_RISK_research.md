# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
filename = e2r_stock_web_v12_residual_round_R3_loop_151_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round = R3
selected_loop = 151
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = mixed_c12_customer_contract_calloff_revenue_timing_leaf_set
loop_objective = priority1_to_50_fill|counterexample_mining|customer_calloff_risk_gate|4B_exit_after_contract_rerating|canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 7 new independent C12 cases, 4 positives, 3 counterexamples, and 5 residual errors for `L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`. The global axes are treated as active: Stage2 actionable evidence bonus, Yellow/Green strictness, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing. This MD does not patch production scoring; it proposes a C12-specific shadow gate.

## 2. Round / Large Sector / Canonical Archetype Scope

C12 belongs to R3/L3. The selected scope is battery customer contract call-off risk: the difference between a real customer contract that converts into revenue/margin and a customer-exposed story that fails because call-off, production cuts, pilot timing, or demand slowdown are not resolved.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index lists C12 as Priority 1 with 32 representative rows and need-to-50 = 18. This session cleared the visible Priority 0 clusters through loop 150, so this run moves into the lowest Priority 1 bucket. The session has not produced a C12-specific loop yet. The selected symbols avoid the prior C11/C14 clusters used in loops 127, 131, 136, 141, 144, 148, and 149 where possible.

```text
hard_duplicate_check = pass
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = none
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

- primary_price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- stock_web_manifest_max_date: `2026-02-20`
- entry_price basis: entry date close (`c` column), per v12 prompt.

## 5. Historical Eligibility Gate

All trigger rows below have entry date in tradable shard, high/low/close/volume present, forward 180 trading rows available by stock-web max date, and no corporate-action candidate inside entry~D+180. Profiles with old corporate-action candidates were retained only where the candidate dates did not overlap the entry-to-D180 window.

## 6. Canonical Archetype Compression Map

```text
BATTERY_CAN_CUSTOMER_CONCENTRATION_RESET_REACCELERATION -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
CYLINDRICAL_BATTERY_NICKEL_PLATE_CAPA_FORECAST_WITH_CUSTOMER_CALLOFF_RISK -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
CYLINDRICAL_4680_CAN_CUSTOMER_SUPPLY_AND_RAMP_TIMING -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
EV_THERMAL_MATERIAL_CUSTOMER_PRODUCTION_CUT_CALLOFF_RISK -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
COMMERCIAL_VEHICLE_BATTERY_PARTS_NAMED_CUSTOMER_LONG_CONTRACT -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
BATTERY_CAN_CAP_ASSY_PILOT_TO_MASS_PRODUCTION_CUSTOMER_TIMING_RISK -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
SILICON_ANODE_MODEL_EXPANSION_CUSTOMER_QUALIFICATION_AND_EXIT_RISK -> C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

## 7. Case Selection Summary

| case | symbol | trigger | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 상신이디피 | 091580 | Stage2-Actionable | 2024-12-05 | 7140 | 17.23 | -8.82 | 38.66 | -8.82 | 58.26 | -8.82 | current_profile_too_late |
| TCC스틸 | 002710 | Stage2 | 2024-03-12 | 67000 | 2.09 | -24.93 | 2.09 | -42.54 | 2.09 | -59.7 | current_profile_false_positive |
| 동원시스템즈 | 014820 | Stage2-Actionable | 2024-04-01 | 42600 | 7.75 | -12.91 | 22.07 | -13.03 | 27.23 | -13.03 | current_profile_correct_with_4B_exit_watch |
| 나노팀 | 417010 | Stage2 | 2024-06-11 | 14150 | 16.61 | -22.83 | 16.61 | -45.87 | 16.61 | -56.82 | current_profile_false_positive |
| 삼기이브이 | 419050 | Stage2-Actionable | 2024-12-05 | 1850 | 17.03 | -16.22 | 17.03 | -20.7 | 41.35 | -20.7 | current_profile_4B_too_late_or_staged_entry_needed |
| 에스피시스템스 | 317830 | Stage2 | 2023-04-12 | 16500 | 16.97 | -25.45 | 16.97 | -27.7 | 18.97 | -49.33 | current_profile_false_positive |
| 대주전자재료 | 078600 | Stage2-Actionable | 2024-05-14 | 100800 | 62.1 | -6.45 | 62.1 | -11.31 | 62.1 | -29.56 | current_profile_4B_too_late |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 4
counterexample_count = 3
4B_watch_or_overlay_count = 5
4C_or_thesis_break_watch_count = 3
current_profile_error_count = 5
```

The clean positives are 상신이디피 reset-after-inventory pressure, 동원시스템즈 4680 can supply/ramp, 삼기이브이 named LGES long contract, and 대주전자재료 silicon-anode model expansion. The failures are TCC스틸 forecast-only cylindrical demand, 나노팀 customer production cut, and 에스피시스템스 pilot-to-mass-production timing. 대주전자재료 and 삼기이브이 are positive but still need 4B/staged-entry protection because early peak or 90D drawdown risk is visible.

## 9. Evidence Source Map

- 상신이디피 2024-12-05: https://w4.kirs.or.kr/download/research/241205_IT%EB%B6%80%ED%92%88_%EC%83%81%EC%8B%A0%EC%9D%B4%EB%94%94%ED%94%BC%28091580%29_%EC%95%88%EC%A0%84%ED%95%9C%20%EC%9D%B4%EC%B0%A8%EC%A0%84%EC%A7%80%EB%A5%BC%20%EC%9C%84%ED%95%9C%20CAN%20%EC%A0%9C%EC%A1%B0%20%ED%9A%8C%EC%82%AC_%ED%95%9C%EA%B5%AD%EA%B8%B0%EC%88%A0%EC%8B%A0%EC%9A%A9%ED%8F%89%EA%B0%80%28%EC%A3%BC%29.pdf — 2024-12-05 KIRS/Korea Ratings report describes Sangsinedp as CAN manufacturer for safe secondary batteries; customer and product-cycle risk is visible but entry after reset had strong path.
- TCC스틸 2024-03-12: https://www.newspim.com/news/view/20240312000188 — 2024-03-12 report emphasized nickel-plated steel capacity and LGES/Samsung SDI final demand, but the trigger lacked near-term customer call-off/revenue confirmation.
- 동원시스템즈 2024-04-01: https://www.etnews.com/20240401000257 — 2024-04-01 interview stated 4680 cylindrical battery can supply and Q3 production plan, with customer-location-driven overseas line consideration.
- 나노팀 2024-06-11: https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024053116341272K_02_07.pdf&inlineYn=Y&saveKey=research.pdf — 2024-06-11 Samsung Securities note explicitly flagged 2024 slowdown from Hyundai Motor Group EV production cuts despite new thermal-runaway pad potential from 2025.
- 삼기이브이 2024-12-05: https://marketin.edaily.co.kr/News/ReadE?newsId=02492806639115568 — 2024-12-05 report stated LG Energy Solution commercial-vehicle battery parts contract, term 2026-11 through 2032-12.
- 에스피시스템스 2023-04-12: https://ssl.pstatic.net/imgstock/upload/research/company/1681254617926.pdf — 2023-04-12 report described battery Can/Cap Assy pilot and 2024 mass-production plan, but also depended on customer product mass-production timing.
- 대주전자재료 2024-05-14: https://ssl.pstatic.net/imgstock/upload/research/company/1715643143026.pdf — 2024-05-14 report tied silicon-anode sales to Porsche Taycan facelift shipments and additional vehicle-model expansion, but 180D drawdown after early peak required exit guard.

## 10. Price Data Source Map

- 091580 상신이디피: `atlas/ohlcv_tradable_by_symbol_year/091/091580/2024.csv` / `atlas/ohlcv_tradable_by_symbol_year/091/091580/2025.csv` / `atlas/symbol_profiles/091/091580.json` / entry `2024-12-05` close `7140`
- 002710 TCC스틸: `atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv` / `atlas/ohlcv_tradable_by_symbol_year/002/002710/2025.csv` / `atlas/symbol_profiles/002/002710.json` / entry `2024-03-12` close `67000`
- 014820 동원시스템즈: `atlas/ohlcv_tradable_by_symbol_year/014/014820/2024.csv` / `atlas/ohlcv_tradable_by_symbol_year/014/014820/2025.csv` / `atlas/symbol_profiles/014/014820.json` / entry `2024-04-01` close `42600`
- 417010 나노팀: `atlas/ohlcv_tradable_by_symbol_year/417/417010/2024.csv` / `atlas/ohlcv_tradable_by_symbol_year/417/417010/2025.csv` / `atlas/symbol_profiles/417/417010.json` / entry `2024-06-11` close `14150`
- 419050 삼기이브이: `atlas/ohlcv_tradable_by_symbol_year/419/419050/2024.csv` / `atlas/ohlcv_tradable_by_symbol_year/419/419050/2025.csv` / `atlas/symbol_profiles/419/419050.json` / entry `2024-12-05` close `1850`
- 317830 에스피시스템스: `atlas/ohlcv_tradable_by_symbol_year/317/317830/2023.csv` / `atlas/ohlcv_tradable_by_symbol_year/317/317830/2024.csv` / `atlas/symbol_profiles/317/317830.json` / entry `2023-04-12` close `16500`
- 078600 대주전자재료: `atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv` / `atlas/ohlcv_tradable_by_symbol_year/078/078600/2025.csv` / `atlas/symbol_profiles/078/078600.json` / entry `2024-05-14` close `100800`

## 11. Case-by-Case Trigger Grid

### C12L151_091580_20241205_SANGSIN_CAN_RESET_REACCELERATION
The report-stage trigger came after a visible reset in the stock and in the battery-parts cycle. The path is clean: MFE_90D 38.66%, MFE_180D 58.26%, and MAE_180D only -8.82%. C12 should allow Stage2-Actionable after inventory/call-off pressure has already reset and the customer/product bridge is still intact.

### C12L151_002710_20240312_TCC_NICKEL_PLATE_4680_FORECAST
The story had a clear final-customer chain, but it was still forecast-heavy. Entry MFE was only 2.09% while MAE_180D reached -59.70%. For C12, final-demand vocabulary and capacity expansion are not enough without near-term call-off and shipment timing.

### C12L151_014820_20240401_DONGWON_4680_CAN_SUPPLY
The 4680 battery can narrative had a hard product/ramp bridge. MFE_90D 22.07% and MFE_180D 27.23% with controlled MAE_180D -13.03% support Stage2-Actionable. Still, the later drawdown after peak shows why C12 should keep a local 4B exit watch.

### C12L151_417010_20240611_NANOTIM_HYUNDAI_PRODUCTION_CUT
The source explicitly framed 2024 slowdown from Hyundai Motor Group EV production cuts. The product optionality was real, but current call-off risk dominated: MAE_90D -45.87%, MAE_180D -56.82%. This is a clean C12 false positive guard case.

### C12L151_419050_20241205_SAMKEE_LGES_COMMERCIAL_VEHICLE_PARTS
The named LGES contract and long-dated supply term justify Stage2-Actionable, but the trigger still had entry stress: MAE_90D -20.70% before 180D MFE reached 41.35%. C12 should score this as staged-entry positive rather than immediate Green.

### C12L151_317830_20230412_SPSYSTEMS_CAN_CAP_PILOT_TIMING
Pilot and quasi-mass-production language did not convert on the expected schedule. MFE_180D stayed below 19% while MAE_180D reached -49.33%. C12 should downgrade pilot-stage Can/Cap Assy claims until customer product timing is confirmed.

### C12L151_078600_20240514_DAEJOO_SILICON_ANODE_MODEL_EXPANSION
Silicon-anode model expansion worked very quickly: MFE_30D/90D/180D all reached 62.10%. But the same 180D window shows MAE -29.56% and drawdown_after_peak -56.55%. C12 positives with model-launch concentration need a fast 4B exit overlay after early MFE.

## 12. Trigger-Level OHLC Backtest Tables

| case | symbol | trigger | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 상신이디피 | 091580 | Stage2-Actionable | 2024-12-05 | 7140 | 17.23 | -8.82 | 38.66 | -8.82 | 58.26 | -8.82 | current_profile_too_late |
| TCC스틸 | 002710 | Stage2 | 2024-03-12 | 67000 | 2.09 | -24.93 | 2.09 | -42.54 | 2.09 | -59.7 | current_profile_false_positive |
| 동원시스템즈 | 014820 | Stage2-Actionable | 2024-04-01 | 42600 | 7.75 | -12.91 | 22.07 | -13.03 | 27.23 | -13.03 | current_profile_correct_with_4B_exit_watch |
| 나노팀 | 417010 | Stage2 | 2024-06-11 | 14150 | 16.61 | -22.83 | 16.61 | -45.87 | 16.61 | -56.82 | current_profile_false_positive |
| 삼기이브이 | 419050 | Stage2-Actionable | 2024-12-05 | 1850 | 17.03 | -16.22 | 17.03 | -20.7 | 41.35 | -20.7 | current_profile_4B_too_late_or_staged_entry_needed |
| 에스피시스템스 | 317830 | Stage2 | 2023-04-12 | 16500 | 16.97 | -25.45 | 16.97 | -27.7 | 18.97 | -49.33 | current_profile_false_positive |
| 대주전자재료 | 078600 | Stage2-Actionable | 2024-05-14 | 100800 | 62.1 | -6.45 | 62.1 | -11.31 | 62.1 | -29.56 | current_profile_4B_too_late |


MFE/MAE formula used: max high / min low from entry date through N trading rows vs entry close. N = 30/90/180 trading days.

## 13. Current Calibrated Profile Stress Test

- `current_profile_too_late`: 상신이디피 reset-after-pressure path.
- `current_profile_correct_with_4B_exit_watch`: 동원시스템즈.
- `current_profile_4B_too_late_or_staged_entry_needed`: 삼기이브이.
- `current_profile_4B_too_late`: 대주전자재료.
- `current_profile_false_positive`: TCC스틸, 나노팀, 에스피시스템스.

The residual error is not that C12 lacks positive cases. The error is that customer contracts and customer exposure are two different objects. A named customer contract with revenue timing can be actionable; a single-customer dependence, pilot-stage program, or demand forecast without confirmed call-off can be a drawdown trap.

## 14. Stage2 / Yellow / Green Comparison

No clean Stage3-Green trigger is emitted here. Green would require repeated revenue conversion, margin/revision confirmation, and call-off visibility. C12 can produce good Stage2-Actionable entries, but Green without call-off confirmation would have been false precision in TCC스틸, 나노팀, and 에스피시스템스.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

C12 needs local 4B rather than blanket bearish reversal. 대주전자재료 had +62.10% MFE before a -56.55% drawdown after peak. 삼기이브이 had a valid long-contract bridge but required staged entry after an early -20.70% MAE. 동원시스템즈 was cleaner, yet still gave a -26.94% drawdown after its D180 peak. The rule should not turn all C12 positives into 4C; it should watch for post-contract rerating exhaustion.

## 16. 4C Protection Audit

Hard 4C should fire only when call-off/demand evidence breaks the thesis: customer production cuts, pilot-to-mass-production delay, or forecast-only demand with no shipment bridge. 나노팀 and 에스피시스템스 are 4C-watch cases. TCC스틸 is more of a local 4B/false-positive block because the long-term demand thesis may remain but the entry trigger lacked near-term call-off evidence.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L3_CUSTOMER_CONTRACT_CALLOFF_AND_REVENUE_TIMING_GATE_V1
```

For L3 battery customer-exposed names, require at least one hard commercial bridge and one conversion bridge before Stage2-Actionable. Hard commercial bridge: named customer, signed supply term, call-off, customer capacity ramp, or model program. Conversion bridge: shipment timing, revenue recognition, margin/revision, inventory reset, or proven production run-rate.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C12_CUSTOMER_CONTRACT_CALLOFF_VISIBILITY_GATE_V1
```

C12 should distinguish four leaves:

1. named customer contract + revenue/call-off timing = actionable;
2. named customer exposure + inventory reset already priced = staged actionable;
3. single-customer concentration + customer production cut = false positive / 4C-watch;
4. pilot/forecast/capacity vocabulary without customer call-off = watch or reject.

## 19. Before / After Backtest Comparison

| profile_id | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 7 | 25.08 | -24.28 | 32.37 | -33.99 | 0.43 | too permissive for forecast/pilot/customer-cut rows |
| P1 sector_specific_candidate_profile | 5 | 31.42 | -14.82 | 42.24 | -20.43 | 0.20 | keeps signed or reset positives; downgrades production-cut/pilot failures |
| P2 canonical_archetype_candidate_profile | 4 | 34.97 | -13.46 | 47.23 | -18.03 | 0.00 | best precision; accepts named/confirmed contract positives only |
| P3 counterexample_guard_profile | 3 | 11.89 | -38.7 | 12.56 | -55.28 | n/a | isolates customer-cut, forecast-only, and pilot-stage failures |

## 20. Score-Return Alignment Matrix

The positive bucket has average MFE_90D 34.97% and average MAE_90D -13.46%. The counterexample bucket has average MFE_90D 11.89% and average MAE_90D -38.7%. The gap is explained by call-off visibility and conversion timing rather than by the mere presence of a large battery customer.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | mixed_c12_customer_contract_calloff_revenue_timing_leaf_set | 4 | 3 | 5 | 3 | 7 | 0 | 7 | 7 | 5 | L3_CUSTOMER_CONTRACT_CALLOFF_AND_REVENUE_TIMING_GATE_V1 | C12_CUSTOMER_CONTRACT_CALLOFF_VISIBILITY_GATE_V1 | index baseline 32 -> 39; need 11 more to 50 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: customer_contract_without_calloff_visibility_false_positive|pilot_to_mass_production_timing_false_positive|customer_production_cut_high_mae|named_contract_positive_needs_4b_exit_guard
new_axis_proposed: c12_customer_contract_calloff_visibility_gate_v1
existing_axis_strengthened: full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage|hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus
sector_specific_rule_candidate: L3_CUSTOMER_CONTRACT_CALLOFF_AND_REVENUE_TIMING_GATE_V1
canonical_archetype_rule_candidate: C12_CUSTOMER_CONTRACT_CALLOFF_VISIBILITY_GATE_V1
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical C12 trigger-level calibration using stock-web 1D OHLCV only. Non-validation scope: live recommendation, forward watchlist, production scoring patch, brokerage/API action, or current market opinion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_customer_contract_calloff_visibility_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,Require named customer contract plus call-off/revenue timing or proven demand reset before Stage2-Actionable; downgrade production-cut/pilot/forecast-only exposure,positive avg MFE90 34.97 vs counterexample avg MFE90 11.89; counterexample avg MAE90 -38.7,TRIG_R3_L151_C12_01_091580_20241205|TRIG_R3_L151_C12_02_002710_20240312|TRIG_R3_L151_C12_03_014820_20240401|TRIG_R3_L151_C12_04_417010_20240611|TRIG_R3_L151_C12_05_419050_20241205|TRIG_R3_L151_C12_06_317830_20230412|TRIG_R3_L151_C12_07_078600_20240514,7,7,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c12_contract_rerating_4b_exit_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,Add local 4B/exit watch when early MFE appears but drawdown_after_peak_180D exceeds 25% or MAE90 <= -20%,captures Daejoo Samkee Dongwon and separates valid positive from durable Green,TRIG_R3_L151_C12_03_014820_20240401|TRIG_R3_L151_C12_05_419050_20241205|TRIG_R3_L151_C12_07_078600_20240514,7,7,3,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C12L151_091580_20241205_SANGSIN_CAN_RESET_REACCELERATION", "symbol": "091580", "company_name": "상신이디피", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONCENTRATION_RESET_REACCELERATION", "case_type": "reset_success", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R3_L151_C12_01_091580_20241205", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_after_reset", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "2024-12-05 KIRS/Korea Ratings report describes Sangsinedp as CAN manufacturer for safe secondary batteries; customer and product-cycle risk is visible but entry after reset had strong path."}
{"row_type": "case", "case_id": "C12L151_002710_20240312_TCC_NICKEL_PLATE_4680_FORECAST", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CYLINDRICAL_BATTERY_NICKEL_PLATE_CAPA_FORECAST_WITH_CUSTOMER_CALLOFF_RISK", "case_type": "forecast_failure", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R3_L151_C12_02_002710_20240312", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_high_mae", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2024-03-12 report emphasized nickel-plated steel capacity and LGES/Samsung SDI final demand, but the trigger lacked near-term customer call-off/revenue confirmation."}
{"row_type": "case", "case_id": "C12L151_014820_20240401_DONGWON_4680_CAN_SUPPLY", "symbol": "014820", "company_name": "동원시스템즈", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CYLINDRICAL_4680_CAN_CUSTOMER_SUPPLY_AND_RAMP_TIMING", "case_type": "commercial_bridge_success", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R3_L151_C12_03_014820_20240401", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_but_exit_guard_needed", "current_profile_verdict": "current_profile_correct_with_4B_exit_watch", "price_source": "Songdaiki/stock-web", "notes": "2024-04-01 interview stated 4680 cylindrical battery can supply and Q3 production plan, with customer-location-driven overseas line consideration."}
{"row_type": "case", "case_id": "C12L151_417010_20240611_NANOTIM_HYUNDAI_PRODUCTION_CUT", "symbol": "417010", "company_name": "나노팀", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "EV_THERMAL_MATERIAL_CUSTOMER_PRODUCTION_CUT_CALLOFF_RISK", "case_type": "customer_production_cut_failure", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R3_L151_C12_04_417010_20240611", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_high_mae", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2024-06-11 Samsung Securities note explicitly flagged 2024 slowdown from Hyundai Motor Group EV production cuts despite new thermal-runaway pad potential from 2025."}
{"row_type": "case", "case_id": "C12L151_419050_20241205_SAMKEE_LGES_COMMERCIAL_VEHICLE_PARTS", "symbol": "419050", "company_name": "삼기이브이", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COMMERCIAL_VEHICLE_BATTERY_PARTS_NAMED_CUSTOMER_LONG_CONTRACT", "case_type": "signed_customer_contract_success_with_mae", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R3_L151_C12_05_419050_20241205", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_but_high_mae_guard_needed", "current_profile_verdict": "current_profile_4B_too_late_or_staged_entry_needed", "price_source": "Songdaiki/stock-web", "notes": "2024-12-05 report stated LG Energy Solution commercial-vehicle battery parts contract, term 2026-11 through 2032-12."}
{"row_type": "case", "case_id": "C12L151_317830_20230412_SPSYSTEMS_CAN_CAP_PILOT_TIMING", "symbol": "317830", "company_name": "에스피시스템스", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CAP_ASSY_PILOT_TO_MASS_PRODUCTION_CUSTOMER_TIMING_RISK", "case_type": "pilot_to_mass_production_failure", "positive_or_counterexample": "counterexample", "best_trigger": "TRIG_R3_L151_C12_06_317830_20230412", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_high_mae", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2023-04-12 report described battery Can/Cap Assy pilot and 2024 mass-production plan, but also depended on customer product mass-production timing."}
{"row_type": "case", "case_id": "C12L151_078600_20240514_DAEJOO_SILICON_ANODE_MODEL_EXPANSION", "symbol": "078600", "company_name": "대주전자재료", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SILICON_ANODE_MODEL_EXPANSION_CUSTOMER_QUALIFICATION_AND_EXIT_RISK", "case_type": "model_expansion_success_with_exit_risk", "positive_or_counterexample": "positive", "best_trigger": "TRIG_R3_L151_C12_07_078600_20240514", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_but_4b_exit_needed", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "2024-05-14 report tied silicon-anode sales to Porsche Taycan facelift shipments and additional vehicle-model expansion, but 180D drawdown after early peak required exit guard."}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L151_C12_01_091580_20241205", "case_id": "C12L151_091580_20241205_SANGSIN_CAN_RESET_REACCELERATION", "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|091580|Stage2-Actionable|2024-12-05", "symbol": "091580", "company_name": "상신이디피", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONCENTRATION_RESET_REACCELERATION", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-12-05", "entry_date": "2024-12-05", "entry_price": 7140, "MFE_30D_pct": 17.23, "MAE_30D_pct": -8.82, "MFE_90D_pct": 38.66, "MAE_90D_pct": -8.82, "MFE_180D_pct": 58.26, "MAE_180D_pct": -8.82, "drawdown_after_peak_180D_pct": -16.11, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "profile_path": "atlas/symbol_profiles/091/091580.json", "corporate_action_status": "no_overlap_in_entry_to_D180; profile candidates 2007-06-11,2010-01-26,2011-05-11", "source_url": "https://w4.kirs.or.kr/download/research/241205_IT%EB%B6%80%ED%92%88_%EC%83%81%EC%8B%A0%EC%9D%B4%EB%94%94%ED%94%BC%28091580%29_%EC%95%88%EC%A0%84%ED%95%9C%20%EC%9D%B4%EC%B0%A8%EC%A0%84%EC%A7%80%EB%A5%BC%20%EC%9C%84%ED%95%9C%20CAN%20%EC%A0%9C%EC%A1%B0%20%ED%9A%8C%EC%82%AC_%ED%95%9C%EA%B5%AD%EA%B8%B0%EC%88%A0%EC%8B%A0%EC%9A%A9%ED%8F%89%EA%B0%80%28%EC%A3%BC%29.pdf", "positive_or_counterexample": "positive", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_too_late"}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L151_C12_02_002710_20240312", "case_id": "C12L151_002710_20240312_TCC_NICKEL_PLATE_4680_FORECAST", "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|002710|Stage2|2024-03-12", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CYLINDRICAL_BATTERY_NICKEL_PLATE_CAPA_FORECAST_WITH_CUSTOMER_CALLOFF_RISK", "trigger_type": "Stage2", "trigger_date": "2024-03-12", "entry_date": "2024-03-12", "entry_price": 67000, "MFE_30D_pct": 2.09, "MAE_30D_pct": -24.93, "MFE_90D_pct": 2.09, "MAE_90D_pct": -42.54, "MFE_180D_pct": 2.09, "MAE_180D_pct": -59.7, "drawdown_after_peak_180D_pct": -60.53, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "profile_path": "atlas/symbol_profiles/002/002710.json", "corporate_action_status": "no_overlap_in_entry_to_D180; profile candidate 2009-05-08 only", "source_url": "https://www.newspim.com/news/view/20240312000188", "positive_or_counterexample": "counterexample", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L151_C12_03_014820_20240401", "case_id": "C12L151_014820_20240401_DONGWON_4680_CAN_SUPPLY", "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|014820|Stage2-Actionable|2024-04-01", "symbol": "014820", "company_name": "동원시스템즈", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CYLINDRICAL_4680_CAN_CUSTOMER_SUPPLY_AND_RAMP_TIMING", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "entry_date": "2024-04-01", "entry_price": 42600, "MFE_30D_pct": 7.75, "MAE_30D_pct": -12.91, "MFE_90D_pct": 22.07, "MAE_90D_pct": -13.03, "MFE_180D_pct": 27.23, "MAE_180D_pct": -13.03, "drawdown_after_peak_180D_pct": -26.94, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "profile_path": "atlas/symbol_profiles/014/014820.json", "corporate_action_status": "no_overlap_in_entry_to_D180; profile candidates all before 2014", "source_url": "https://www.etnews.com/20240401000257", "positive_or_counterexample": "positive", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_correct_with_4B_exit_watch"}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L151_C12_04_417010_20240611", "case_id": "C12L151_417010_20240611_NANOTIM_HYUNDAI_PRODUCTION_CUT", "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|417010|Stage2|2024-06-11", "symbol": "417010", "company_name": "나노팀", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "EV_THERMAL_MATERIAL_CUSTOMER_PRODUCTION_CUT_CALLOFF_RISK", "trigger_type": "Stage2", "trigger_date": "2024-06-11", "entry_date": "2024-06-11", "entry_price": 14150, "MFE_30D_pct": 16.61, "MAE_30D_pct": -22.83, "MFE_90D_pct": 16.61, "MAE_90D_pct": -45.87, "MFE_180D_pct": 16.61, "MAE_180D_pct": -56.82, "drawdown_after_peak_180D_pct": -62.97, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "profile_path": "atlas/symbol_profiles/417/417010.json", "corporate_action_status": "no corporate_action_candidate_dates in profile", "source_url": "https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024053116341272K_02_07.pdf&inlineYn=Y&saveKey=research.pdf", "positive_or_counterexample": "counterexample", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L151_C12_05_419050_20241205", "case_id": "C12L151_419050_20241205_SAMKEE_LGES_COMMERCIAL_VEHICLE_PARTS", "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|419050|Stage2-Actionable|2024-12-05", "symbol": "419050", "company_name": "삼기이브이", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COMMERCIAL_VEHICLE_BATTERY_PARTS_NAMED_CUSTOMER_LONG_CONTRACT", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-12-05", "entry_date": "2024-12-05", "entry_price": 1850, "MFE_30D_pct": 17.03, "MAE_30D_pct": -16.22, "MFE_90D_pct": 17.03, "MAE_90D_pct": -20.7, "MFE_180D_pct": 41.35, "MAE_180D_pct": -20.7, "drawdown_after_peak_180D_pct": -20.27, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "profile_path": "atlas/symbol_profiles/419/419050.json", "corporate_action_status": "no_overlap_in_entry_to_D180; profile candidates 2023-08-31 and 2023-09-22 only", "source_url": "https://marketin.edaily.co.kr/News/ReadE?newsId=02492806639115568", "positive_or_counterexample": "positive", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_4B_too_late_or_staged_entry_needed"}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L151_C12_06_317830_20230412", "case_id": "C12L151_317830_20230412_SPSYSTEMS_CAN_CAP_PILOT_TIMING", "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|317830|Stage2|2023-04-12", "symbol": "317830", "company_name": "에스피시스템스", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CAP_ASSY_PILOT_TO_MASS_PRODUCTION_CUSTOMER_TIMING_RISK", "trigger_type": "Stage2", "trigger_date": "2023-04-12", "entry_date": "2023-04-12", "entry_price": 16500, "MFE_30D_pct": 16.97, "MAE_30D_pct": -25.45, "MFE_90D_pct": 16.97, "MAE_90D_pct": -27.7, "MFE_180D_pct": 18.97, "MAE_180D_pct": -49.33, "drawdown_after_peak_180D_pct": -57.41, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "profile_path": "atlas/symbol_profiles/317/317830.json", "corporate_action_status": "no corporate_action_candidate_dates in profile", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1681254617926.pdf", "positive_or_counterexample": "counterexample", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "trigger", "trigger_id": "TRIG_R3_L151_C12_07_078600_20240514", "case_id": "C12L151_078600_20240514_DAEJOO_SILICON_ANODE_MODEL_EXPANSION", "same_entry_group_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|078600|Stage2-Actionable|2024-05-14", "symbol": "078600", "company_name": "대주전자재료", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SILICON_ANODE_MODEL_EXPANSION_CUSTOMER_QUALIFICATION_AND_EXIT_RISK", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-14", "entry_date": "2024-05-14", "entry_price": 100800, "MFE_30D_pct": 62.1, "MAE_30D_pct": -6.45, "MFE_90D_pct": 62.1, "MAE_90D_pct": -11.31, "MFE_180D_pct": 62.1, "MAE_180D_pct": -29.56, "drawdown_after_peak_180D_pct": -56.55, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "profile_path": "atlas/symbol_profiles/078/078600.json", "corporate_action_status": "no corporate_action_candidate_dates in profile", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1715643143026.pdf", "positive_or_counterexample": "positive", "calibration_usable": true, "representative_for_aggregate": true, "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C12L151_091580_20241205_SANGSIN_CAN_RESET_REACCELERATION", "trigger_id": "TRIG_R3_L151_C12_01_091580_20241205", "symbol": "091580", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 75, "customer_quality_score": 70, "calloff_risk_score": 30, "revenue_timing_score": 65, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 55, "execution_risk_score": 35, "valuation_repricing_score": 50, "accounting_trust_risk_score": 10}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 80, "customer_quality_score": 75, "calloff_risk_score": 25, "revenue_timing_score": 70, "margin_bridge_score": 58, "revision_score": 48, "relative_strength_score": 55, "execution_risk_score": 35, "valuation_repricing_score": 45, "accounting_trust_risk_score": 10}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "calloff_risk_score", "revenue_timing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C12 gate rewards named customer contracts with call-off visibility and revenue/margin timing; it downgrades single-customer exposure, forecast-only 46xx/EV demand, pilot-stage production, or customer production cuts.", "MFE_90D_pct": 38.66, "MAE_90D_pct": -8.82, "score_return_alignment_label": "aligned_after_reset", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C12L151_002710_20240312_TCC_NICKEL_PLATE_4680_FORECAST", "trigger_id": "TRIG_R3_L151_C12_02_002710_20240312", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 55, "customer_quality_score": 45, "calloff_risk_score": 78, "revenue_timing_score": 30, "margin_bridge_score": 20, "revision_score": 15, "relative_strength_score": 55, "execution_risk_score": 70, "valuation_repricing_score": 50, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 45, "customer_quality_score": 35, "calloff_risk_score": 88, "revenue_timing_score": 18, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 55, "execution_risk_score": 82, "valuation_repricing_score": 45, "accounting_trust_risk_score": 10}, "weighted_score_after": 48, "stage_label_after": "Rejected", "changed_components": ["customer_quality_score", "calloff_risk_score", "revenue_timing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C12 gate rewards named customer contracts with call-off visibility and revenue/margin timing; it downgrades single-customer exposure, forecast-only 46xx/EV demand, pilot-stage production, or customer production cuts.", "MFE_90D_pct": 2.09, "MAE_90D_pct": -42.54, "score_return_alignment_label": "misaligned_high_mae", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C12L151_014820_20240401_DONGWON_4680_CAN_SUPPLY", "trigger_id": "TRIG_R3_L151_C12_03_014820_20240401", "symbol": "014820", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 75, "customer_quality_score": 70, "calloff_risk_score": 30, "revenue_timing_score": 65, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 55, "execution_risk_score": 35, "valuation_repricing_score": 50, "accounting_trust_risk_score": 10}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 80, "customer_quality_score": 75, "calloff_risk_score": 25, "revenue_timing_score": 70, "margin_bridge_score": 58, "revision_score": 48, "relative_strength_score": 55, "execution_risk_score": 35, "valuation_repricing_score": 45, "accounting_trust_risk_score": 10}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "calloff_risk_score", "revenue_timing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C12 gate rewards named customer contracts with call-off visibility and revenue/margin timing; it downgrades single-customer exposure, forecast-only 46xx/EV demand, pilot-stage production, or customer production cuts.", "MFE_90D_pct": 22.07, "MAE_90D_pct": -13.03, "score_return_alignment_label": "aligned_but_exit_guard_needed", "current_profile_verdict": "current_profile_correct_with_4B_exit_watch"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C12L151_417010_20240611_NANOTIM_HYUNDAI_PRODUCTION_CUT", "trigger_id": "TRIG_R3_L151_C12_04_417010_20240611", "symbol": "417010", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 55, "customer_quality_score": 45, "calloff_risk_score": 78, "revenue_timing_score": 30, "margin_bridge_score": 20, "revision_score": 15, "relative_strength_score": 55, "execution_risk_score": 70, "valuation_repricing_score": 50, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 45, "customer_quality_score": 35, "calloff_risk_score": 88, "revenue_timing_score": 18, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 55, "execution_risk_score": 82, "valuation_repricing_score": 45, "accounting_trust_risk_score": 10}, "weighted_score_after": 48, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "calloff_risk_score", "revenue_timing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C12 gate rewards named customer contracts with call-off visibility and revenue/margin timing; it downgrades single-customer exposure, forecast-only 46xx/EV demand, pilot-stage production, or customer production cuts.", "MFE_90D_pct": 16.61, "MAE_90D_pct": -45.87, "score_return_alignment_label": "misaligned_high_mae", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C12L151_419050_20241205_SAMKEE_LGES_COMMERCIAL_VEHICLE_PARTS", "trigger_id": "TRIG_R3_L151_C12_05_419050_20241205", "symbol": "419050", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 75, "customer_quality_score": 70, "calloff_risk_score": 30, "revenue_timing_score": 65, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 55, "execution_risk_score": 35, "valuation_repricing_score": 50, "accounting_trust_risk_score": 10}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 80, "customer_quality_score": 75, "calloff_risk_score": 25, "revenue_timing_score": 70, "margin_bridge_score": 58, "revision_score": 48, "relative_strength_score": 55, "execution_risk_score": 35, "valuation_repricing_score": 45, "accounting_trust_risk_score": 10}, "weighted_score_after": 77, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "calloff_risk_score", "revenue_timing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C12 gate rewards named customer contracts with call-off visibility and revenue/margin timing; it downgrades single-customer exposure, forecast-only 46xx/EV demand, pilot-stage production, or customer production cuts.", "MFE_90D_pct": 17.03, "MAE_90D_pct": -20.7, "score_return_alignment_label": "aligned_but_high_mae_guard_needed", "current_profile_verdict": "current_profile_4B_too_late_or_staged_entry_needed"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C12L151_317830_20230412_SPSYSTEMS_CAN_CAP_PILOT_TIMING", "trigger_id": "TRIG_R3_L151_C12_06_317830_20230412", "symbol": "317830", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 55, "customer_quality_score": 45, "calloff_risk_score": 78, "revenue_timing_score": 30, "margin_bridge_score": 20, "revision_score": 15, "relative_strength_score": 55, "execution_risk_score": 70, "valuation_repricing_score": 50, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 45, "customer_quality_score": 35, "calloff_risk_score": 88, "revenue_timing_score": 18, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 55, "execution_risk_score": 82, "valuation_repricing_score": 45, "accounting_trust_risk_score": 10}, "weighted_score_after": 48, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "calloff_risk_score", "revenue_timing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C12 gate rewards named customer contracts with call-off visibility and revenue/margin timing; it downgrades single-customer exposure, forecast-only 46xx/EV demand, pilot-stage production, or customer production cuts.", "MFE_90D_pct": 16.97, "MAE_90D_pct": -27.7, "score_return_alignment_label": "misaligned_high_mae", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C12L151_078600_20240514_DAEJOO_SILICON_ANODE_MODEL_EXPANSION", "trigger_id": "TRIG_R3_L151_C12_07_078600_20240514", "symbol": "078600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 75, "customer_quality_score": 70, "calloff_risk_score": 30, "revenue_timing_score": 65, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 55, "execution_risk_score": 35, "valuation_repricing_score": 50, "accounting_trust_risk_score": 10}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 80, "customer_quality_score": 75, "calloff_risk_score": 25, "revenue_timing_score": 70, "margin_bridge_score": 58, "revision_score": 48, "relative_strength_score": 55, "execution_risk_score": 35, "valuation_repricing_score": 45, "accounting_trust_risk_score": 10}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "calloff_risk_score", "revenue_timing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C12 gate rewards named customer contracts with call-off visibility and revenue/margin timing; it downgrades single-customer exposure, forecast-only 46xx/EV demand, pilot-stage production, or customer production cuts.", "MFE_90D_pct": 62.1, "MAE_90D_pct": -11.31, "score_return_alignment_label": "aligned_but_4b_exit_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "aggregate", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "mixed_c12_customer_contract_calloff_revenue_timing_leaf_set", "new_independent_case_count": 7, "reused_case_count": 0, "positive_case_count": 4, "counterexample_count": 3, "calibration_usable_trigger_count": 7, "representative_trigger_count": 7, "avg_positive_MFE90": 34.97, "avg_positive_MAE90": -13.46, "avg_counterexample_MFE90": 11.89, "avg_counterexample_MAE90": -38.7, "current_profile_error_count": 5}
{"row_type": "shadow_weight", "axis": "c12_customer_contract_calloff_visibility_gate", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Require named customer contract plus call-off/revenue timing or proven demand offset before Stage2-Actionable; downgrade customer production cuts, pilot-stage claims, forecast-only 46xx demand, or single-customer concentration without conversion bridge.", "backtest_effect": "positive avg MFE90 34.97 vs counterexample avg MFE90 11.89; counterexample avg MAE90 -38.7", "trigger_ids": "TRIG_R3_L151_C12_01_091580_20241205|TRIG_R3_L151_C12_02_002710_20240312|TRIG_R3_L151_C12_03_014820_20240401|TRIG_R3_L151_C12_04_417010_20240611|TRIG_R3_L151_C12_05_419050_20241205|TRIG_R3_L151_C12_06_317830_20230412|TRIG_R3_L151_C12_07_078600_20240514", "calibration_usable_count": 7, "new_independent_case_count": 7, "counterexample_count": 3, "confidence": "medium", "proposal_type": "canonical_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "residual_contribution", "round": "R3", "loop": "151", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "new_independent_case_count": 7, "reused_case_count": 0, "new_symbol_count": 7, "new_trigger_family_count": 7, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["customer_contract_without_calloff_visibility_false_positive", "pilot_to_mass_production_timing_false_positive", "customer_production_cut_high_mae", "named_contract_positive_needs_4b_exit_guard"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

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

```text
completed_round = R3
completed_loop = 151
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- All price rows were computed from stock-web local downloaded shards listed in section 10 using entry-date close.
