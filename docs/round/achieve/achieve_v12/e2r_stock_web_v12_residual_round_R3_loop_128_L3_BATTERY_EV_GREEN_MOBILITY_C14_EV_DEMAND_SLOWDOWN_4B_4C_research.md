# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_128_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round: R3
selected_loop: 128
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C_WITH_4B_BOUNCE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_4C_timing_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This is the corrected valid run after a duplicate C10 loop127 materialization path was discarded. C10 reached the local 30-row stability threshold at loop127, so this loop moves to the next Priority 0 gap: C14.

This loop adds 3 new independent C14 rows and moves C14 from static 21 rows to projected 24 rows. It still needs 6 rows to reach the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C14:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C14 -> C14_EV_DEMAND_SLOWDOWN_4B_4C
```

C14 is the EV demand slowdown / 4B / 4C archetype. The calibration point is not “EV is weak” in the abstract. It is whether utilization, customer call-off, ASP/mix pressure, inventory, and FCF deterioration are strong enough to override a temporary 4B rebound.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C14 static rows | 21 |
| C14 need to 30 | 9 |
| C14 need to 50 | 29 |
| C14 investigation point | EV 수요 둔화, utilization, call-off, hard 4C 확인 |
| local previous C14 rows in this session | 0 |
| this loop projected rows | 24 |

Selected symbols avoid local C06/C07/C08/C09/C10 completed-threshold loops. C10 duplicate materialization was rejected before this C14 artifact.

| symbol | company | status |
|---|---|---|
| 247540 | 에코프로비엠 | new local C14 hard 4C protection |
| 066970 | 엘앤에프 | new local C14 hard 4C protection after 4B bounce |
| 373220 | LG에너지솔루션 | new local C14 overblock counterexample |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 247540 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, reduced weight 0.95 |
| 066970 / 2024-03-06 | true | true | clean_180D_window_after_market_transfer | true, reduced weight 0.95 |
| 373220 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 에코프로비엠 has old corporate-action candidates in 2022 only; selected 2024 window is clean.
- 엘앤에프 has old corporate-action candidates before 2024 and a market transfer completed before selected entry; selected forward window is usable.
- LG에너지솔루션 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C_WITH_4B_BOUNCE | C14 | cathode 4B bounce should be capped when utilization/ASP/call-off pressure persists |
| EV_CATHODE_CUSTOMER_CALL_OFF_DEMAND_SLOWDOWN_HARD_4C | C14 | customer call-off and ASP pressure are hard 4C when bridge is absent |
| EV_CELL_UTILIZATION_SLOWDOWN_OVERBLOCK_WITH_CUSTOMER_SCALE_BUFFER | C14 | blanket EV slowdown 4C can over-block cell leaders with scale/customer/policy buffer |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C14_ECOPROBM_247540_2024_03_06_EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C | 247540 | 에코프로비엠 | hard_4c_protection_success | positive_protection | 18.84% bounce followed by -51.74% 180D MAE |
| C14_LNF_066970_2024_03_06_EV_CATHODE_CUSTOMER_CALL_OFF_HARD_4C | 066970 | 엘앤에프 | hard_4c_protection_success | positive_protection | 27.08% bounce followed by -47.06% 180D MAE |
| C14_LGES_373220_2024_03_06_CELL_UTILIZATION_SLOWDOWN_OVERBLOCK_COUNTEREXAMPLE | 373220 | LG에너지솔루션 | overblock_counterexample | counterexample | blanket hard 4C would have over-blocked a cell-scale buffer case |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_protection_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| overblock_counterexample_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 247540 | source_proxy_only | cathode demand slowdown / utilization / ASP / call-off risk | required before promotion |
| 066970 | source_proxy_only | customer call-off / cathode ASP pressure / inventory overhang | required before promotion |
| 373220 | source_proxy_only | cell-scale/customer/policy buffer versus blanket slowdown | required; useful as overblock counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | atlas/symbol_profiles/247/247540.json |
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | atlas/symbol_profiles/066/066970.json |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| ECOPROBM_247540_2024_03_06_STAGE4C_EV_CATHODE_DEMAND_SLOWDOWN | Stage4C | 2024-03-06 | 2024-03-06 | 249500 | cathode demand slowdown / utilization pressure |
| LNF_066970_2024_03_06_STAGE4C_EV_CATHODE_CALL_OFF_RISK | Stage4C | 2024-03-06 | 2024-03-06 | 156600 | cathode customer call-off / ASP pressure |
| LGES_373220_2024_03_06_STAGE2_OVERBLOCK_COUNTEREXAMPLE_CELL_SCALE_BUFFER | Stage2 | 2024-03-06 | 2024-03-06 | 387000 | cell-scale buffer against blanket hard 4C |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 247540 | 2024-03-06 | 249500 | 18.84 | -13.83 | 18.84 | -29.78 | 18.84 | -51.74 | 2024-03-25 | 296500 | -59.39 |
| 066970 | 2024-03-06 | 156600 | 27.08 | -10.22 | 27.08 | -14.37 | 27.08 | -47.06 | 2024-03-25 | 199000 | -58.34 |
| 373220 | 2024-03-06 | 387000 | 9.04 | -7.49 | 9.04 | -16.67 | 14.73 | -16.67 | 2024-10-08 | 444000 | -16.44 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 247540 | Stage2 bounce risk if cathode recovery beta is over-credited | hard 4C protection worked | current_profile_4C_too_late |
| 066970 | Stage2 bounce risk if market-transfer/liquidity rebound is over-credited | hard 4C protection worked after bounce | current_profile_4C_too_late_after_stage2_bounce |
| 373220 | hard 4C risk if all EV slowdown is treated equally | overblock counterexample | current_profile_overblocks_if_all_EV_slowdown_equal |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C14 interpretation:

- A cathode rebound after bad news can be only a 4B bounce.
- Hard 4C needs utilization, call-off, ASP/mix, inventory and FCF pressure.
- A blanket EV slowdown rule over-blocks when customer scale, policy buffer, and large-contract optionality are visible.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 247540 | 0.84 | 1.00 | cathode rebound / demand slowdown | 4B bounce should not override hard 4C |
| 066970 | 0.79 | 1.00 | liquidity rebound / call-off risk | 4B bounce should be capped by hard 4C |
| 373220 | 0.87 | 1.00 | cell-scale buffer / policy buffer | not hard 4C without bridge failure |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 247540 | hard_4c_success | utilization/ASP/call-off pressure protected against later drawdown |
| 066970 | hard_4c_success_after_bounce | call-off/ASP pressure protected after a temporary rally |
| 373220 | overblock_counterexample | blanket hard 4C would have over-penalized cell-scale buffer |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, EV demand slowdown should trigger hard 4C only when utilization, call-off, ASP/mix, inventory, margin, revision or FCF deterioration is visible. A temporary rebound is only 4B unless non-price customer/scale evidence turns it into Stage2A. Cell leaders with customer-scale and policy buffer need an overblock exception.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C14_EV_DEMAND_SLOWDOWN_4B_4C
confidence = medium
```

Candidate C14 rule:

```text
C14_ev_demand_slowdown_hard_4c =
  ev_demand_slowdown
  AND (utilization_pressure OR customer_call_off OR asp_mix_pressure OR inventory_overhang OR margin_revision_down OR fcf_deterioration)

if 4b_bounce_after_bad_news and C14_ev_demand_slowdown_hard_4c:
    cap_stage = Stage4C
    do_not_allow_Stage3_Yellow_or_Green = true

if cell_scale_customer_buffer and policy_or_ampc_buffer and MAE_180D > -25:
    classify_as C14_overblock_counterexample
    cap_stage = Stage2-watch_not_4C

if MFE_90D > 15 and MAE_180D < -40 and hard_4c_evidence:
    strengthen C14_4B_to_4C_timing_guard
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / overblock | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 18.32 | -20.27 | 20.22 | -38.49 | 1 overblock | useful but timing/exception rule needed |
| P0b calibrated rollback | rollback | 3 | 18.32 | -20.27 | 20.22 | -38.49 | 1 overblock | over-credits 4B bounce or overblocks broad EV weakness |
| P1 sector_specific_candidate_profile | L3 | 2 hard 4C + 1 overblock exception | 22.96 | -22.07 | 22.96 | -49.4 | 0 | better with 4B-to-4C timing and exception |
| P2 canonical_archetype_candidate_profile | C14 | 2 hard 4C + 1 overblock exception | 22.96 | -22.07 | 22.96 | -49.4 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C14 guard | 2 hard 4C + 1 overblock exception | 22.96 | -22.07 | 22.96 | -49.4 | 0 | adds blanket-4C overblock guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 247540 | hard 4C aligned; 4B bounce was trap-like | current_profile_4C_too_late |
| 066970 | hard 4C aligned after Stage2 bounce | current_profile_4C_too_late_after_stage2_bounce |
| 373220 | hard 4C overblock if applied too broadly | current_profile_overblocks_if_all_EV_slowdown_equal |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive protection | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed C14 fine ids | 2 | 1 | 2 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> projected 24; still need 6 to reach 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4C_too_late
  - current_profile_overblocks_if_all_EV_slowdown_equal
new_axis_proposed: C14_ev_demand_slowdown_hard_4c|C14_4B_to_4C_timing_guard|C14_cell_scale_policy_buffer_overblock_exception
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses C14 Priority 0 coverage gap.
- Avoids local C10 loop127 repetition after C10 threshold completion.
- Keeps 247540/066970/373220 as first local C14 row set.
- Treats 373220 as overblock counterexample rather than a hard 4C failure.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated loop127 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_ev_demand_slowdown_hard_4c,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"247540/066970 show cathode 4B rebounds can fail when utilization/call-off/ASP pressure persists","caps Stage2/Yellow after 4B bounce and preserves hard 4C protection","ECOPROBM_247540_2024_03_06_STAGE4C_EV_CATHODE_DEMAND_SLOWDOWN|LNF_066970_2024_03_06_STAGE4C_EV_CATHODE_CALL_OFF_RISK",2,2,0,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C14_4B_to_4C_timing_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"247540/066970 had tradable MFE before major 180D MAE, so 4B bounce needs demand-slowdown timing cap","prevents 4B rebounds from becoming Green without customer/margin/FCF recovery","ECOPROBM_247540_2024_03_06_STAGE4C_EV_CATHODE_DEMAND_SLOWDOWN|LNF_066970_2024_03_06_STAGE4C_EV_CATHODE_CALL_OFF_RISK",2,2,0,medium,canonical_shadow_only,"4B/4C timing calibration only"
shadow_weight,C14_cell_scale_policy_buffer_overblock_exception,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"373220 shows blanket EV slowdown hard 4C can overblock cell-scale/policy-buffer cases","keeps 373220 as Stage2-watch rather than hard 4C","LGES_373220_2024_03_06_STAGE2_OVERBLOCK_COUNTEREXAMPLE_CELL_SCALE_BUFFER",1,1,1,medium,canonical_shadow_only,"overblock guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C14_ECOPROBM_247540_2024_03_06_EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"128","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C_WITH_4B_BOUNCE","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"ECOPROBM_247540_2024_03_06_STAGE4C_EV_CATHODE_DEMAND_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates in 2022 only; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"cathode demand-slowdown guard allowed only a 18.84% bounce before a -51.74% 180D MAE, so hard 4C protection was directionally correct","current_profile_verdict":"current_profile_4C_too_late_if_recovery_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; EV cathode utilization/ASP/call-off risk with early 4B bounce"}
{"row_type":"case","case_id":"C14_LNF_066970_2024_03_06_EV_CATHODE_CUSTOMER_CALL_OFF_HARD_4C","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"128","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CATHODE_CUSTOMER_CALL_OFF_DEMAND_SLOWDOWN_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"LNF_066970_2024_03_06_STAGE4C_EV_CATHODE_CALL_OFF_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected 2024 window; KOSPI transfer already complete before selected entry","independent_evidence_weight":0.95,"score_price_alignment":"cathode/customer call-off risk produced a 27.08% bounce but later -47.06% 180D MAE; 4B bounce had to be capped by demand-slowdown 4C","current_profile_verdict":"current_profile_4C_too_late_after_stage2_bounce","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; selected after market transfer to avoid pre-transfer boundary"}
{"row_type":"case","case_id":"C14_LGES_373220_2024_03_06_CELL_UTILIZATION_SLOWDOWN_OVERBLOCK_COUNTEREXAMPLE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"128","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CELL_UTILIZATION_SLOWDOWN_OVERBLOCK_WITH_CUSTOMER_SCALE_BUFFER","case_type":"overblock_counterexample","positive_or_counterexample":"counterexample","best_trigger":"LGES_373220_2024_03_06_STAGE2_OVERBLOCK_COUNTEREXAMPLE_CELL_SCALE_BUFFER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"cell leader had only -16.67% 180D MAE and later +14.73% MFE, so a blanket EV slowdown 4C would over-block without customer/scale buffer logic","current_profile_verdict":"current_profile_overblocks_if_all_EV_slowdown_equal","price_source":"Songdaiki/stock-web","notes":"new local C14 symbol; clean profile with zero corporate-action candidates"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"ECOPROBM_247540_2024_03_06_STAGE4C_EV_CATHODE_DEMAND_SLOWDOWN","case_id":"C14_ECOPROBM_247540_2024_03_06_EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"128","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C_WITH_4B_BOUNCE","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":249500.0,"evidence_available_at_that_date":"source_proxy_only: EV cathode demand slowdown, utilization pressure, ASP/mix pressure and call-off risk visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cathode_recovery_beta","short_squeeze_bounce","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["4b_bounce_after_bad_news","valuation_peak_watch"],"stage4c_evidence_fields":["ev_demand_slowdown","utilization_pressure","asp_pressure","call_off_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.84,"MFE_90D_pct":18.84,"MFE_180D_pct":18.84,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-13.83,"MAE_90D_pct":-29.78,"MAE_180D_pct":-51.74,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":296500.0,"drawdown_after_peak_pct":-59.39,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"4B bounce existed but should not override C14 demand-slowdown hard 4C","four_b_evidence_type":["short_squeeze_bounce","valuation_peak_watch"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protection_high_mae_after_bounce","current_profile_verdict":"current_profile_4C_too_late_if_recovery_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C14_247540_2024_03_06_249500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LNF_066970_2024_03_06_STAGE4C_EV_CATHODE_CALL_OFF_RISK","case_id":"C14_LNF_066970_2024_03_06_EV_CATHODE_CUSTOMER_CALL_OFF_HARD_4C","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"128","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CATHODE_CUSTOMER_CALL_OFF_DEMAND_SLOWDOWN_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":156600.0,"evidence_available_at_that_date":"source_proxy_only: cathode customer call-off risk, demand slowdown, ASP pressure and inventory/utilization stress visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cathode_recovery_beta","market_transfer_liquidity","relative_strength_bounce"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["4b_bounce_after_stage2","valuation_peak_watch"],"stage4c_evidence_fields":["customer_call_off_risk","demand_slowdown","asp_pressure","inventory_overhang"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.08,"MFE_90D_pct":27.08,"MFE_180D_pct":27.08,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.22,"MAE_90D_pct":-14.37,"MAE_180D_pct":-47.06,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000.0,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"4B rebound was real but C14 call-off/ASP pressure should have capped Stage2/Yellow promotion","four_b_evidence_type":["liquidity_bounce","valuation_peak_watch"],"four_c_protection_label":"hard_4c_success_after_bounce","trigger_outcome_label":"positive_protection_high_mae_after_stage2_bounce","current_profile_verdict":"current_profile_4C_too_late_after_stage2_bounce","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_after_market_transfer","same_entry_group_id":"C14_066970_2024_03_06_156600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window; market transfer completed before entry","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LGES_373220_2024_03_06_STAGE2_OVERBLOCK_COUNTEREXAMPLE_CELL_SCALE_BUFFER","case_id":"C14_LGES_373220_2024_03_06_CELL_UTILIZATION_SLOWDOWN_OVERBLOCK_COUNTEREXAMPLE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"128","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_CELL_UTILIZATION_SLOWDOWN_OVERBLOCK_WITH_CUSTOMER_SCALE_BUFFER","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":387000.0,"evidence_available_at_that_date":"source_proxy_only: EV cell demand slowdown/utilization pressure visible, but customer scale, AMPC/policy buffer and large-contract optionality partly offset a blanket hard 4C; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cell_scale_buffer","customer_diversification","policy_or_ampc_buffer","relative_strength_partial"],"stage3_evidence_fields":["customer_scale_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["broad_ev_slowdown_peak_watch"],"stage4c_evidence_fields":["utilization_pressure_watch","demand_slowdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.04,"MFE_90D_pct":9.04,"MFE_180D_pct":14.73,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.49,"MAE_90D_pct":-16.67,"MAE_180D_pct":-16.67,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000.0,"drawdown_after_peak_pct":-16.44,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"blanket EV slowdown 4C would overblock cell-scale buffer case; needs customer/scale exception","four_b_evidence_type":["customer_scale_buffer","policy_buffer"],"four_c_protection_label":"overblock_counterexample","trigger_outcome_label":"counterexample_overbroad_4c","current_profile_verdict":"current_profile_overblocks_if_all_EV_slowdown_equal","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_373220_2024_03_06_387000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_ECOPROBM_247540_2024_03_06_EV_CATHODE_UTILIZATION_DEMAND_SLOWDOWN_HARD_4C","trigger_id":"ECOPROBM_247540_2024_03_06_STAGE4C_EV_CATHODE_DEMAND_SLOWDOWN","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 bounce risk / late 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":43,"stage_label_after":"Stage4C hard demand-slowdown protection","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Cathode demand slowdown and utilization/ASP pressure should dominate a temporary 4B bounce.","MFE_90D_pct":18.84,"MAE_90D_pct":-29.78,"score_return_alignment_label":"hard_4c_protection_success","current_profile_verdict":"current_profile_4C_too_late_if_recovery_beta_overcredited"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_LNF_066970_2024_03_06_EV_CATHODE_CUSTOMER_CALL_OFF_HARD_4C","trigger_id":"LNF_066970_2024_03_06_STAGE4C_EV_CATHODE_CALL_OFF_RISK","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 bounce risk / late 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":43,"stage_label_after":"Stage4C hard call-off/ASP protection","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Customer call-off/ASP pressure should cap the Stage2 bounce and prevent Yellow/Green promotion.","MFE_90D_pct":27.08,"MAE_90D_pct":-14.37,"score_return_alignment_label":"hard_4c_protection_success_after_bounce","current_profile_verdict":"current_profile_4C_too_late_after_stage2_bounce"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C14_LGES_373220_2024_03_06_CELL_UTILIZATION_SLOWDOWN_OVERBLOCK_COUNTEREXAMPLE","trigger_id":"LGES_373220_2024_03_06_STAGE2_OVERBLOCK_COUNTEREXAMPLE_CELL_SCALE_BUFFER","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-watch / not hard 4C","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-watch with C14 overblock exception","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Cell-scale/customer buffer prevents blanket EV slowdown hard 4C; still no Green without margin/FCF confirmation.","MFE_90D_pct":9.04,"MAE_90D_pct":-16.67,"score_return_alignment_label":"overblock_counterexample","current_profile_verdict":"current_profile_overblocks_if_all_EV_slowdown_equal"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"128","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_overblocks_if_all_EV_slowdown_equal"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_2 rolling calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 128
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

If this loop is accepted, C14 moves to projected 24 rows and still needs 6 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C14 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/247/247540.json
  - atlas/symbol_profiles/066/066970.json
  - atlas/symbol_profiles/373/373220.json
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R2_loop_127_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
