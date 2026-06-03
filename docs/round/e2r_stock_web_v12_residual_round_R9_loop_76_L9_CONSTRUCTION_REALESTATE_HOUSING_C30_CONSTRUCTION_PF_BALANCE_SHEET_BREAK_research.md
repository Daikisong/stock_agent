# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R9
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R10
computed_next_loop: 76
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_ORDER_ASSET_MARGIN_CASHFLOW_BALANCE_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r9_branch: L9_CONSTRUCTION_BRANCH_ALLOWED
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

R9 allows either the L3 mobility branch or the L9 construction/real-estate branch. The previous R9 loop used L3/C29 mobility, so this loop uses the allowed L9 branch. R10 loop 75 already used regional housing, building-materials and developer rebound; this file therefore shifts to formwork rental / regional policy construction / concrete-pile material false-starts.

| layer | id | definition |
|---|---|---|
| round | R9 | mobility or construction bridge round |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | construction, housing, real estate, PF, balance sheet, construction materials |
| canonical | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF, liquidity, balance sheet, order/cashflow repair |
| fine | C30_ORDER_ASSET_MARGIN_CASHFLOW_BALANCE_BRIDGE_GUARD | construction signal must become order, asset, margin, cashflow and balance evidence |
| deep | CONSTRUCTION_FORMWORK_RENTAL_ASSET_UTILIZATION_TO_MARGIN_CASHFLOW_AND_BALANCE_VALUE | formwork rental positive |
| deep | REGIONAL_CONSTRUCTION_POLICY_AND_INFRA_THEME_WITHOUT_ORDERBOOK_BALANCE_REPAIR_OR_CASHFLOW_CONVERSION | regional policy false positive |
| deep | CONCRETE_PILE_AND_CONSTRUCTION_MATERIAL_THEME_WITHOUT_HOUSING_ORDER_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION | concrete pile false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols remain `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run also avoids the recent C30 representatives `035890`, `007210`, `010780`, `003070`, `010960`, `002410`, `034300`, `013360`, `002780`, `012630`, `002460`, `001470`, `375500`, `021320`, `014790`, `013580`, `004960`, and `002990`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C30 | 018310 | new independent | not top-covered C30 symbol; formwork rental asset-utilization/margin/cashflow bridge |
| C30 | 025950 | new independent | not top-covered C30 symbol; regional construction/policy spike without orderbook/cashflow bridge |
| C30 | 228340 | new independent | not top-covered C30 symbol; concrete pile/material low-quality MFE without margin/cashflow bridge |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE/peak/drawdown computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
018310 has corporate-action candidates ending 2016-08-24, outside the selected 2024 representative window.
025950 has corporate-action candidates ending 2004-01-20, outside the selected 2024 representative window.
228340 has no corporate-action candidate dates.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| formwork_rental_margin_success_then_4B_interim_MAE_watch | 018310 | 삼목에스폼 | Stage2-Actionable | 2024-03-04 | 23700 | formwork rental asset-utilization/margin bridge worked, but interim high-MAE blocked Green |
| regional_construction_policy_spike_high_MAE_counterexample | 025950 | 동신건설 | Stage2-Actionable | 2024-03-14 | 26500 | regional construction policy spike lacked orderbook/cashflow bridge |
| concrete_pile_theme_low_MFE_high_MAE_counterexample | 228340 | 동양파일 | Stage2-Actionable | 2024-04-03 | 2400 | concrete-pile/material spike lacked volume/margin/cashflow bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 018310 | 삼목에스폼 | Stage2-Actionable | 2024-03-04 | 23700 | 16.03 | 16.03 | 22.15 | -15.4 | -25.02 | -28.02 | 2024-10-07 | 28950 | -12.61 |
| 025950 | 동신건설 | Stage2-Actionable | 2024-03-14 | 26500 | 20.19 | 20.19 | 20.19 | -29.85 | -29.85 | -33.85 | 2024-03-25 | 31850 | -44.96 |
| 228340 | 동양파일 | Stage2-Actionable | 2024-04-03 | 2400 | 12.71 | 12.71 | 12.71 | -10.0 | -11.88 | -20.83 | 2024-04-03 | 2705 | -29.76 |

## 9. Case-by-Case Notes

### 9.1 018310 / 삼목에스폼 — formwork rental asset-utilization bridge

The entry row is 2024-03-04 at 23,700. The path first reached 27,500, later fell hard, then recovered toward 28,950. This is a valid C30 positive only as guarded Yellow. The bridge is formwork rental asset utilization, construction-site order visibility, margin, cashflow and balance-value repair. However, the interim 17,060 low makes 4B/high-MAE watch mandatory and blocks Green.

### 9.2 025950 / 동신건설 — regional construction policy spike without cashflow bridge

The entry row is 2024-03-14 at 26,500. The local high reached 31,850, but the later low reached 17,530. This is the C30 false-positive shape: a regional construction or infrastructure policy spike can create MFE, but without orderbook, PF-risk containment, balance repair, margin and cashflow bridge, it should not become Stage3 evidence.

### 9.3 228340 / 동양파일 — concrete-pile material low-quality MFE

The entry row is 2024-04-03 at 2,400. The high was 2,705, while the later low reached 1,900. The MFE was shallow and local. Without housing-order pull-through, volume, utilization, price-cost margin and cashflow bridge, this row should remain Watch/4B/high-MAE.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C30 treats construction policy/material MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C30 needs order/asset/margin/cashflow/balance bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 025950 and 228340 local spikes. |
| Full 4B non-price requirement appropriate? | Yes. 018310 has better non-price bridge; 025950/228340 do not. |
| 4C timing issue? | High-MAE and interim-MAE watch are useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
018310:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after formwork rental / asset utilization / margin / cashflow bridge
  Stage3-Green = reject because interim high-MAE and construction-cycle risk remain active

025950:
  Stage2-Actionable = too generous if based only on regional construction or policy spike
  Stage3-Yellow = reject without orderbook, balance repair, margin and cashflow bridge
  Stage3-Green = reject despite MFE

228340:
  Stage2-Actionable = too generous if based only on concrete-pile/material spike
  Stage3-Yellow = reject without housing order, volume, utilization, margin and cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 018310 | 0.95 | 1.00 | formwork margin/cashflow bridge positive but interim-MAE and full-window 4B watch |
| 025950 | 1.00 | 1.00 | regional construction policy theme local 4B watch, not positive stage |
| 228340 | 1.00 | 1.00 | concrete-pile material theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c30_requires_order_asset_margin_cashflow_balance_bridge

rule:
  For C30 construction/PF rows, do not promote construction, regional construction,
  infrastructure policy, construction material, formwork, concrete-pile, developer,
  housing, or remodeling Stage2 signals into Stage3-Yellow/Green unless at least
  one non-price bridge is visible:
  orderbook/backlog, site-order visibility, asset utilization, balance repair,
  PF-risk containment, liquidity/refinancing, order-to-cashflow visibility,
  working-capital control, margin conversion, asset support, or credible
  capital-structure improvement.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 16.31 | -22.25 | 66.7% | too generous to construction policy/material MFE |
| P0b e2r_2_0_baseline_reference | 3 | 16.31 | -22.25 | 33.3% | safer but may miss 018310 |
| P1 sector_specific_candidate_profile | 3 | 16.31 | -22.25 | 66.7% | no broad L9 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 16.03 | -25.02 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 16.45 | -20.87 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 018310 | current_profile_correct_but_no_green | asset-utilization/margin/cashflow bridge aligned with MFE, but interim high-MAE blocks Green |
| 025950 | current_profile_false_positive | regional construction policy MFE lacked orderbook/cashflow bridge |
| 228340 | current_profile_false_positive | concrete-pile material MFE lacked volume/margin/cashflow bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_ORDER_ASSET_MARGIN_CASHFLOW_BALANCE_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R9/L9 C30 non-top-covered construction material/order residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- construction policy theme without order/cashflow bridge
- formwork rental margin winner needs interim-MAE watch
- concrete-pile low-quality MFE high-MAE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- R9 allowed L9 branch consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean windows outside listed corporate-action candidate dates
```

Not validated:

```text
- exact disclosure/report URLs
- exact orderbook/PF/cashflow announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_order_asset_margin_cashflow_balance_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction signal converts into orderbook/backlog, asset utilization, balance repair, PF-risk containment, liquidity/refinancing, order-to-cashflow, margin, working-capital or cashflow bridge","018310 survives only as guarded positive after formwork rental asset-utilization/margin/cashflow bridge; 025950 and 228340 are demoted because regional construction policy or concrete-pile/material MFE lacked orderbook, balance and cashflow bridge","TRG_R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE|TRG_R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE|TRG_R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R9 allowed L9 branch"
shadow_weight,c30_construction_policy_material_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Construction winners and policy/material theme false starts can peak before margin/cashflow durability is proven; local/full-window 4B and high-MAE watch should remain active","preserves 018310 guarded positive while preventing 025950/228340 construction-theme false positives","TRG_R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE|TRG_R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE|TRG_R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens delayed-MFE/interim-MAE and local/full-window 4B guard without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE","symbol":"018310","company_name":"삼목에스폼","round":"R9","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CONSTRUCTION_FORMWORK_RENTAL_ASSET_UTILIZATION_TO_MARGIN_CASHFLOW_AND_BALANCE_VALUE","case_type":"formwork_rental_margin_success_then_4B_interim_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_with_high_MAE_guard","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R9 allowed L9 branch. C30 construction/PF/balance-sheet rows require orderbook/backlog, asset utilization, balance repair, PF-risk containment, liquidity, order-to-cashflow, margin, working-capital or cashflow bridge; policy/material theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE","symbol":"025950","company_name":"동신건설","round":"R9","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_CONSTRUCTION_POLICY_THEME_WITHOUT_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_CONSTRUCTION_POLICY_AND_INFRA_THEME_WITHOUT_ORDERBOOK_BALANCE_REPAIR_OR_CASHFLOW_CONVERSION","case_type":"regional_construction_policy_spike_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R9 allowed L9 branch. C30 construction/PF/balance-sheet rows require orderbook/backlog, asset utilization, balance repair, PF-risk containment, liquidity, order-to-cashflow, margin, working-capital or cashflow bridge; policy/material theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE","symbol":"228340","company_name":"동양파일","round":"R9","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CONCRETE_PILE_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CONCRETE_PILE_AND_CONSTRUCTION_MATERIAL_THEME_WITHOUT_HOUSING_ORDER_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"concrete_pile_theme_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R9 allowed L9 branch. C30 construction/PF/balance-sheet rows require orderbook/backlog, asset utilization, balance repair, PF-risk containment, liquidity, order-to-cashflow, margin, working-capital or cashflow bridge; policy/material theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE","case_id":"R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE","symbol":"018310","company_name":"삼목에스폼","round":"R9","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CONSTRUCTION_FORMWORK_RENTAL_ASSET_UTILIZATION_TO_MARGIN_CASHFLOW_AND_BALANCE_VALUE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":23700,"evidence_available_at_that_date":"source_proxy_formwork_rental_asset_utilization_order_margin_cashflow_balance_value_bridge; evidence_url_pending","evidence_source":"source_proxy_formwork_rental_asset_utilization_order_margin_cashflow_balance_value_bridge; evidence_url_pending","bridge_summary":"formwork rental asset utilization and construction-site order visibility converted into margin/cashflow and balance-value bridge, but deep interim MAE and construction-cycle drawdown required 4B watch","stage2_evidence_fields":["formwork_rental_asset_utilization","construction_site_order_visibility","relative_strength","margin_cashflow_proxy"],"stage3_evidence_fields":["asset_utilization_to_margin_visibility","rental_cashflow_bridge","balance_value_repair_proxy"],"stage4b_evidence_fields":["delayed_MFE_watch","interim_high_MAE","construction_cycle_crowding"],"stage4c_evidence_fields":["interim_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018310/2024.csv","profile_path":"atlas/symbol_profiles/018/018310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.03,"MFE_90D_pct":16.03,"MFE_180D_pct":22.15,"MFE_1Y_pct":22.15,"MFE_2Y_pct":22.15,"MAE_30D_pct":-15.4,"MAE_90D_pct":-25.02,"MAE_180D_pct":-28.02,"MAE_1Y_pct":-28.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-07","peak_price":28950,"drawdown_after_peak_pct":-12.61,"green_lateness_ratio":"0.63","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"formwork_margin_cashflow_bridge_positive_but_interim_MAE_and_full_window_4B_watch","four_b_evidence_type":"non_price_order_margin_cashflow_balance_bridge","four_c_protection_label":"interim_high_MAE_watch","trigger_outcome_label":"formwork_rental_margin_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE","case_id":"R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE","symbol":"025950","company_name":"동신건설","round":"R9","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_CONSTRUCTION_POLICY_THEME_WITHOUT_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_CONSTRUCTION_POLICY_AND_INFRA_THEME_WITHOUT_ORDERBOOK_BALANCE_REPAIR_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":26500,"evidence_available_at_that_date":"source_proxy_regional_construction_policy_infra_theme_without_orderbook_balance_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_regional_construction_policy_infra_theme_without_orderbook_balance_cashflow_bridge; evidence_url_pending","bridge_summary":"regional construction/policy theme produced a local spike, but orderbook, PF-risk containment, balance repair, margin and cashflow bridge were absent; high MAE dominated the path","stage2_evidence_fields":["regional_construction_policy_theme","infra_event_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_policy_theme_peak","orderbook_bridge_absent","balance_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_orderbook_or_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025950/2024.csv","profile_path":"atlas/symbol_profiles/025/025950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.19,"MFE_90D_pct":20.19,"MFE_180D_pct":20.19,"MFE_1Y_pct":20.19,"MFE_2Y_pct":20.19,"MAE_30D_pct":-29.85,"MAE_90D_pct":-29.85,"MAE_180D_pct":-33.85,"MAE_1Y_pct":-33.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":31850,"drawdown_after_peak_pct":-44.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"regional_construction_policy_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"construction_policy_material_theme_without_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"regional_construction_policy_spike_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE","case_id":"R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE","symbol":"228340","company_name":"동양파일","round":"R9","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CONCRETE_PILE_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CONCRETE_PILE_AND_CONSTRUCTION_MATERIAL_THEME_WITHOUT_HOUSING_ORDER_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":2400,"evidence_available_at_that_date":"source_proxy_concrete_pile_construction_material_theme_without_housing_order_volume_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_concrete_pile_construction_material_theme_without_housing_order_volume_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"concrete pile / construction-material theme produced low-quality MFE, but housing order, volume, utilization, price-cost margin and cashflow bridge remained weak","stage2_evidence_fields":["concrete_pile_theme","construction_material_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_material_peak","housing_order_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_volume_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/228/228340/2024.csv","profile_path":"atlas/symbol_profiles/228/228340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.71,"MFE_90D_pct":12.71,"MFE_180D_pct":12.71,"MFE_1Y_pct":12.71,"MFE_2Y_pct":12.71,"MAE_30D_pct":-10.0,"MAE_90D_pct":-11.88,"MAE_180D_pct":-20.83,"MAE_1Y_pct":-20.83,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-03","peak_price":2705,"drawdown_after_peak_pct":-29.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"concrete_pile_material_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"construction_policy_material_theme_without_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"concrete_pile_theme_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE","trigger_id":"TRG_R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE","symbol":"018310","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":10,"asset_balance_score":12,"PF_risk_bridge_score":6,"liquidity_cashflow_score":11,"relative_strength_score":10,"risk_penalty":7},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":12,"asset_balance_score":15,"PF_risk_bridge_score":8,"liquidity_cashflow_score":14,"relative_strength_score":8,"risk_penalty":12},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_HighMAE","changed_components":["orderbook_score","asset_balance_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 row is promoted only because formwork rental/asset-utilization signal converts into margin, cashflow and balance-value bridge; interim high-MAE blocks Green.","MFE_90D_pct":16.03,"MAE_90D_pct":-25.02,"score_return_alignment_label":"score_return_aligned_with_high_MAE_guard","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE","trigger_id":"TRG_R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE","symbol":"025950","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":3,"asset_balance_score":2,"PF_risk_bridge_score":1,"liquidity_cashflow_score":0,"relative_strength_score":10,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":0,"asset_balance_score":0,"PF_risk_bridge_score":0,"liquidity_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["orderbook_score","asset_balance_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes construction policy/material theme rows when orderbook, balance repair, margin, working-capital and cashflow bridge are absent.","MFE_90D_pct":20.19,"MAE_90D_pct":-29.85,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE","trigger_id":"TRG_R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE","symbol":"228340","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":3,"asset_balance_score":2,"PF_risk_bridge_score":1,"liquidity_cashflow_score":0,"relative_strength_score":10,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":0,"asset_balance_score":0,"PF_risk_bridge_score":0,"liquidity_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["orderbook_score","asset_balance_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes construction policy/material theme rows when orderbook, balance repair, margin, working-capital and cashflow bridge are absent.","MFE_90D_pct":12.71,"MAE_90D_pct":-11.88,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_order_asset_margin_cashflow_balance_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction signal converts into orderbook/backlog, asset utilization, balance repair, PF-risk containment, liquidity/refinancing, order-to-cashflow, margin, working-capital or cashflow bridge","018310 survives only as guarded positive after formwork rental asset-utilization/margin/cashflow bridge; 025950 and 228340 are demoted because regional construction policy or concrete-pile/material MFE lacked orderbook, balance and cashflow bridge","TRG_R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE|TRG_R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE|TRG_R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R9 allowed L9 branch"
shadow_weight,c30_construction_policy_material_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Construction winners and policy/material theme false starts can peak before margin/cashflow durability is proven; local/full-window 4B and high-MAE watch should remain active","preserves 018310 guarded positive while preventing 025950/228340 construction-theme false positives","TRG_R9L76_C30_018310_20240304_FORMWORK_RENTAL_ORDER_MARGIN_CASHFLOW_BRIDGE|TRG_R9L76_C30_025950_20240314_REGIONAL_CONSTRUCTION_POLICY_THEME_NO_CASHFLOW_BRIDGE|TRG_R9L76_C30_228340_20240403_CONCRETE_PILE_THEME_LOW_MFE_NO_MARGIN_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens delayed-MFE/interim-MAE and local/full-window 4B guard without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"76","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["construction_policy_theme_without_order_cashflow_bridge","formwork_rental_margin_winner_needs_interim_MAE_watch","concrete_pile_low_quality_MFE_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R9-specific handling

- R9 may use `L3_BATTERY_EV_GREEN_MOBILITY` or `L9_CONSTRUCTION_REALESTATE_HOUSING`.
- This MD uses the allowed L9 construction branch.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- Positive score promotion requires non-price evidence and clean MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/construction-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R9 allowed L9 branch and large_sector_id.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C30 construction/PF rows cannot promote without orderbook/backlog, site-order visibility, asset utilization, balance repair, PF-risk containment, liquidity/refinancing, order-to-cashflow visibility, working-capital control, margin conversion, asset support, or capital-structure improvement.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R9
completed_loop = 76
next_round = R10
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/018/018310.json
atlas/symbol_profiles/025/025950.json
atlas/symbol_profiles/228/228340.json
atlas/ohlcv_tradable_by_symbol_year/018/018310/2024.csv
atlas/ohlcv_tradable_by_symbol_year/025/025950/2024.csv
atlas/ohlcv_tradable_by_symbol_year/228/228340/2024.csv
```

This loop continues loop 76 with R9 and adds 3 new independent C30 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R9/L9.
