# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R11
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R12
computed_next_loop: 76
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: C03_EXPORT_FRAMEWORK_SIGNED_ORDER_BACKLOG_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r11_branch: L1_policy_defense_linkage_branch
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

R11 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or a policy/defense-linked `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` branch. The previous R11 loop used L1/C04 nuclear-policy. This run stays in the allowed L1 branch but rotates to C03 defense export framework/backlog, avoiding the top-covered defense exporters and using a fresh guided-weapon / tactical-communication / RF-component split.

| layer | id | definition |
|---|---|---|
| round | R11 | policy/event or policy-linked infra/defense cross round |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | industrials, infra, defense, grid, policy-linked backlog |
| canonical | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | defense export framework, signed order, backlog and margin bridge |
| fine | C03_EXPORT_FRAMEWORK_SIGNED_ORDER_BACKLOG_MARGIN_BRIDGE_GUARD | defense signal must become export/order/backlog/margin evidence |
| deep | GUIDED_WEAPON_EXPORT_FRAMEWORK_ORDERBOOK_TO_BACKLOG_MARGIN_AND_REVENUE_VISIBILITY | guided weapon positive |
| deep | TACTICAL_COMMUNICATION_AND_UAV_COMPONENT_THEME_WITHOUT_EXPORT_CONTRACT_BACKLOG_MARGIN_CASHFLOW_CONVERSION | tactical communication false positive |
| deep | RF_DEFENSE_COMPONENT_AND_MISSILE_ELECTRONICS_THEME_WITHOUT_EXPORT_FRAMEWORK_BACKLOG_MARGIN_CASHFLOW_CONVERSION | RF component false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C03 top-covered symbols are `064350`, `272210`, `UNKNOWN_SYMBOL`, `012450`, `010820`, and `003570`. This run avoids that cluster and also avoids the previous R11/C04 nuclear representatives `083650`, `042370`, and `011700`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C03 | 079550 | new independent | not top-covered C03 symbol; guided-weapon export framework and backlog bridge |
| C03 | 005870 | new independent | not top-covered C03 symbol; tactical-communication/UAV component theme without durable export-order bridge |
| C03 | 095270 | new independent | not top-covered C03 symbol; RF defense component local spike without export/backlog bridge |

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
079550 has no corporate-action candidate dates.
005870 has corporate-action candidates ending 2007-05-09, outside the selected 2024 representative window.
095270 has a 2020-10-15 corporate-action candidate, outside the selected 2024/2025 representative window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| guided_weapon_export_backlog_success_then_4B_watch | 079550 | LIG넥스원 | Stage2-Actionable | 2024-02-14 | 127000 | export framework/backlog/margin bridge worked, but full-window 4B guard required |
| tactical_communication_theme_MFE_then_high_MAE_counterexample | 005870 | 휴니드 | Stage2-Actionable | 2024-01-17 | 8200 | tactical-communication/UAV theme MFE lacked durable export-order bridge |
| RF_defense_component_spike_then_severe_high_MAE_counterexample | 095270 | 웨이브일렉트로 | Stage2-Actionable | 2024-07-15 | 7320 | RF defense component spike lacked export framework/backlog bridge |

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
| 079550 | LIG넥스원 | Stage2-Actionable | 2024-02-14 | 127000 | 50.63 | 72.83 | 96.06 | -9.13 | -9.13 | -9.13 | 2024-07-17 | 249000 | -32.25 |
| 005870 | 휴니드 | Stage2-Actionable | 2024-01-17 | 8200 | 8.54 | 8.54 | 36.1 | -23.17 | -24.39 | -25.85 | 2024-08-06 | 11160 | -38.89 |
| 095270 | 웨이브일렉트로 | Stage2-Actionable | 2024-07-15 | 7320 | 6.69 | 6.69 | 6.69 | -31.42 | -40.3 | -50.07 | 2024-07-16 | 7810 | -53.2 |

## 9. Case-by-Case Notes

### 9.1 079550 / LIG넥스원 — guided weapon export framework bridge

The entry row is 2024-02-14 at 127,000. The 30D path reached 191,300, the 90D path reached 219,500, and the wider window reached 249,000. This is a valid C03 positive because the source bridge is not just defense theme beta. It requires export framework, orderbook, backlog-to-revenue and margin visibility. The post-peak defense crowding and execution-timing risk keep full-window 4B active and block Green.

### 9.2 005870 / 휴니드 — tactical communication theme without durable export bridge

The entry row is 2024-01-17 at 8,200. MFE existed, later reaching 11,160, but the path also fell to 6,080 before the later spike and then drew down after the peak. This is useful as a counterexample because price MFE alone can tempt Stage3. Without signed export contract, repeat order, backlog-to-revenue, margin and cashflow bridge, it should remain Watch/4B/high-MAE.

### 9.3 095270 / 웨이브일렉트로 — RF component spike without backlog bridge

The entry row is 2024-07-15 at 7,320. The local high reached 7,810, but the wider low fell to 3,655. This is the clean 4B/4C guard case: RF defense component and missile-electronics optionality created a short local spike, but without export framework, signed backlog, customer order, margin or cashflow bridge, it should not receive positive Stage3 credit.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C03 treats defense-component MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C03 needs export framework/order/backlog/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 005870/095270 theme spikes. |
| Full 4B non-price requirement appropriate? | Yes. 079550 has a bridge; 005870/095270 do not. |
| 4C timing issue? | High-MAE and severe-MAE watch are useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
079550:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after export framework / orderbook / backlog-to-revenue / margin bridge
  Stage3-Green = reject unless post-peak defense crowding and delivery execution risk clear

005870:
  Stage2-Actionable = acceptable only as tactical-communication/UAV component watch
  Stage3-Yellow = reject without signed export order, repeat order, backlog and margin bridge
  Stage3-Green = reject despite MFE

095270:
  Stage2-Actionable = too generous if based only on RF defense component spike
  Stage3-Yellow = reject without export framework, customer order, margin and cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 079550 | 0.77 | 1.00 | guided-weapon export/backlog bridge positive but full-window 4B/drawdown watch |
| 005870 | 0.80 | 1.00 | tactical-communication MFE but no durable order bridge; keep 4B/high-MAE watch |
| 095270 | 1.00 | 1.00 | RF defense component local spike, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c03_requires_export_framework_signed_order_backlog_margin_bridge

rule:
  For C03 defense export framework rows, do not promote defense,
  guided weapon, tactical communication, UAV component, RF component,
  missile electronics, radar, ship combat system, or defense-policy Stage2
  signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  export framework, signed order, orderbook/backlog, backlog-to-revenue conversion,
  delivery schedule quality, execution-margin proof, customer acceptance,
  FCF/cash conversion, or earnings revision tied to defense backlog economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 29.35 | -24.61 | 66.7% | too generous to defense-component/theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 29.35 | -24.61 | 33.3% | safer but may miss 079550 |
| P1 sector_specific_candidate_profile | 3 | 29.35 | -24.61 | 66.7% | no broad L1 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 72.83 | -9.13 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 7.62 | -32.34 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 079550 | current_profile_correct_but_no_green | export/backlog/margin bridge aligned with MFE, but 4B drawdown watch remains |
| 005870 | current_profile_false_positive_if_green | defense communication MFE lacked durable export-order/backlog bridge |
| 095270 | current_profile_false_positive | RF component spike produced severe high MAE without export/backlog bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03_EXPORT_FRAMEWORK_SIGNED_ORDER_BACKLOG_MARGIN_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R11 allowed L1/C03 non-top-covered defense residual reduced |

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
- defense component theme without export/backlog bridge
- guided weapon export winner needs 4B watch
- RF component spike severe high-MAE
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
- R11 allowed L1 policy-defense branch consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean windows outside listed corporate-action candidate dates
```

Not validated:

```text
- exact disclosure/report URLs
- exact export framework / signed order announcement URLs
- production scoring behavior
- live candidate status
- C32 governance branch, intentionally skipped because top-covered concentration and prior R11/C32 history were higher than this L1/C03 residual branch
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c03_requires_export_framework_signed_order_backlog_margin_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"C03 defense export rows should not promote toward Stage3-Yellow/Green unless defense signal converts into export framework, signed order, orderbook/backlog, backlog-to-revenue, execution margin, delivery schedule, FCF or cashflow bridge","079550 survives as guarded positive after guided-weapon export/backlog bridge; 005870 and 095270 are demoted because tactical-communication/RF component theme MFE lacked durable export order, backlog and margin bridge","TRG_R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE|TRG_R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE|TRG_R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R11 allowed L1 policy-defense branch"
shadow_weight,c03_defense_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,1,1,0,"Defense export winners and component-theme false starts can peak before export/backlog durability is proven; local/full-window 4B and high-MAE watch should remain active","preserves 079550 guarded positive while preventing 005870/095270 defense-component theme false positives","TRG_R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE|TRG_R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE|TRG_R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","symbol":"079550","company_name":"LIG넥스원","round":"R11","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","deep_sub_archetype_id":"GUIDED_WEAPON_EXPORT_FRAMEWORK_ORDERBOOK_TO_BACKLOG_MARGIN_AND_REVENUE_VISIBILITY","case_type":"guided_weapon_export_backlog_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R11 uses allowed L1 policy-defense linkage branch. C03 defense export rows require export framework, signed order, orderbook/backlog, backlog-to-revenue, execution margin, delivery schedule, or cashflow bridge; defense-component theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE","symbol":"005870","company_name":"휴니드","round":"R11","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_TACTICAL_COMMUNICATION_THEME_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"TACTICAL_COMMUNICATION_AND_UAV_COMPONENT_THEME_WITHOUT_EXPORT_CONTRACT_BACKLOG_MARGIN_CASHFLOW_CONVERSION","case_type":"tactical_communication_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R11 uses allowed L1 policy-defense linkage branch. C03 defense export rows require export framework, signed order, orderbook/backlog, backlog-to-revenue, execution margin, delivery schedule, or cashflow bridge; defense-component theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE","symbol":"095270","company_name":"웨이브일렉트로","round":"R11","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_RF_DEFENSE_COMPONENT_SPIKE_WITHOUT_EXPORT_BACKLOG_BRIDGE","deep_sub_archetype_id":"RF_DEFENSE_COMPONENT_AND_MISSILE_ELECTRONICS_THEME_WITHOUT_EXPORT_FRAMEWORK_BACKLOG_MARGIN_CASHFLOW_CONVERSION","case_type":"RF_defense_component_spike_then_severe_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R11 uses allowed L1 policy-defense linkage branch. C03 defense export rows require export framework, signed order, orderbook/backlog, backlog-to-revenue, execution margin, delivery schedule, or cashflow bridge; defense-component theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","case_id":"R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","symbol":"079550","company_name":"LIG넥스원","round":"R11","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","deep_sub_archetype_id":"GUIDED_WEAPON_EXPORT_FRAMEWORK_ORDERBOOK_TO_BACKLOG_MARGIN_AND_REVENUE_VISIBILITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":127000,"evidence_available_at_that_date":"source_proxy_guided_weapon_export_framework_orderbook_backlog_margin_revenue_visibility_bridge; evidence_url_pending","evidence_source":"source_proxy_guided_weapon_export_framework_orderbook_backlog_margin_revenue_visibility_bridge; evidence_url_pending","bridge_summary":"guided-weapon export framework and defense orderbook converted into backlog-to-revenue, margin and earnings-visibility bridge, but post-peak defense crowding and execution timing required 4B watch","stage2_evidence_fields":["guided_weapon_export_framework","defense_orderbook_proxy","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["export_framework_to_backlog_visibility","backlog_to_revenue_bridge","margin_earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","defense_export_crowding","order_execution_timing_risk"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","profile_path":"atlas/symbol_profiles/079/079550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":50.63,"MFE_90D_pct":72.83,"MFE_180D_pct":96.06,"MFE_1Y_pct":96.06,"MFE_2Y_pct":96.06,"MAE_30D_pct":-9.13,"MAE_90D_pct":-9.13,"MAE_180D_pct":-9.13,"MAE_1Y_pct":-9.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":249000,"drawdown_after_peak_pct":-32.25,"green_lateness_ratio":"0.44","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"guided_weapon_export_backlog_bridge_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_export_framework_backlog_margin_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"guided_weapon_export_backlog_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE","case_id":"R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE","symbol":"005870","company_name":"휴니드","round":"R11","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_TACTICAL_COMMUNICATION_THEME_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"TACTICAL_COMMUNICATION_AND_UAV_COMPONENT_THEME_WITHOUT_EXPORT_CONTRACT_BACKLOG_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-17","entry_date":"2024-01-17","entry_price":8200,"evidence_available_at_that_date":"source_proxy_tactical_communication_UAV_component_defense_theme_without_export_contract_backlog_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_tactical_communication_UAV_component_defense_theme_without_export_contract_backlog_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"tactical communication/UAV component defense theme created MFE, but export contract, repeat order, backlog-to-revenue, margin and cashflow bridge were not durable enough","stage2_evidence_fields":["tactical_communication_theme","UAV_component_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_theme_peak","export_contract_bridge_absent","backlog_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_export_order_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005870/2024.csv","profile_path":"atlas/symbol_profiles/005/005870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.54,"MFE_90D_pct":8.54,"MFE_180D_pct":36.1,"MFE_1Y_pct":36.1,"MFE_2Y_pct":36.1,"MAE_30D_pct":-23.17,"MAE_90D_pct":-24.39,"MAE_180D_pct":-25.85,"MAE_1Y_pct":-25.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-06","peak_price":11160,"drawdown_after_peak_pct":-38.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.8,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"tactical_communication_MFE_but_no_durable_order_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"defense_component_theme_without_export_backlog_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"tactical_communication_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE","case_id":"R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE","symbol":"095270","company_name":"웨이브일렉트로","round":"R11","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_RF_DEFENSE_COMPONENT_SPIKE_WITHOUT_EXPORT_BACKLOG_BRIDGE","deep_sub_archetype_id":"RF_DEFENSE_COMPONENT_AND_MISSILE_ELECTRONICS_THEME_WITHOUT_EXPORT_FRAMEWORK_BACKLOG_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-15","entry_date":"2024-07-15","entry_price":7320,"evidence_available_at_that_date":"source_proxy_RF_defense_component_missile_electronics_theme_without_export_framework_backlog_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_RF_defense_component_missile_electronics_theme_without_export_framework_backlog_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"RF defense component and missile-electronics theme produced only a short local spike; export framework, signed backlog, customer order, margin and cashflow bridge were absent","stage2_evidence_fields":["RF_defense_component_theme","missile_electronics_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_spike_peak","export_framework_bridge_absent","backlog_cashflow_bridge_absent"],"stage4c_evidence_fields":["severe_high_MAE_without_export_backlog_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095270/2024.csv|atlas/ohlcv_tradable_by_symbol_year/095/095270/2025.csv","profile_path":"atlas/symbol_profiles/095/095270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.69,"MFE_90D_pct":6.69,"MFE_180D_pct":6.69,"MFE_1Y_pct":6.69,"MFE_2Y_pct":6.69,"MAE_30D_pct":-31.42,"MAE_90D_pct":-40.3,"MAE_180D_pct":-50.07,"MAE_1Y_pct":-50.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":7810,"drawdown_after_peak_pct":-53.2,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"RF_defense_component_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"defense_component_theme_without_export_backlog_bridge","four_c_protection_label":"severe_high_MAE_watch","trigger_outcome_label":"RF_defense_component_spike_then_severe_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","trigger_id":"TRG_R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","symbol":"079550","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"export_framework_score":12,"signed_order_score":12,"backlog_revenue_score":12,"margin_cashflow_score":10,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_framework_score":15,"signed_order_score":15,"backlog_revenue_score":15,"margin_cashflow_score":13,"relative_strength_score":8,"theme_risk_penalty":9},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["export_framework_score","signed_order_score","backlog_revenue_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C03 row is promoted only because defense export framework converts into backlog-to-revenue and margin bridge; post-peak export/crowding 4B blocks Green.","MFE_90D_pct":72.83,"MAE_90D_pct":-9.13,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE","trigger_id":"TRG_R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE","symbol":"005870","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"export_framework_score":5,"signed_order_score":1,"backlog_revenue_score":1,"margin_cashflow_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_framework_score":1,"signed_order_score":0,"backlog_revenue_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["export_framework_score","signed_order_score","backlog_revenue_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C03 guard demotes defense component/theme rows when export framework, signed order, backlog, margin and cashflow bridge are absent.","MFE_90D_pct":8.54,"MAE_90D_pct":-24.39,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE","trigger_id":"TRG_R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE","symbol":"095270","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"export_framework_score":5,"signed_order_score":1,"backlog_revenue_score":1,"margin_cashflow_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_framework_score":1,"signed_order_score":0,"backlog_revenue_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["export_framework_score","signed_order_score","backlog_revenue_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C03 guard demotes defense component/theme rows when export framework, signed order, backlog, margin and cashflow bridge are absent.","MFE_90D_pct":6.69,"MAE_90D_pct":-40.3,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c03_requires_export_framework_signed_order_backlog_margin_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"C03 defense export rows should not promote toward Stage3-Yellow/Green unless defense signal converts into export framework, signed order, orderbook/backlog, backlog-to-revenue, execution margin, delivery schedule, FCF or cashflow bridge","079550 survives as guarded positive after guided-weapon export/backlog bridge; 005870 and 095270 are demoted because tactical-communication/RF component theme MFE lacked durable export order, backlog and margin bridge","TRG_R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE|TRG_R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE|TRG_R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R11 allowed L1 policy-defense branch"
shadow_weight,c03_defense_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,1,1,0,"Defense export winners and component-theme false starts can peak before export/backlog durability is proven; local/full-window 4B and high-MAE watch should remain active","preserves 079550 guarded positive while preventing 005870/095270 defense-component theme false positives","TRG_R11L76_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE|TRG_R11L76_C03_005870_20240117_TACTICAL_COMMUNICATION_THEME_NO_DURABLE_ORDER_BRIDGE|TRG_R11L76_C03_095270_20240715_RF_DEFENSE_COMPONENT_SPIKE_NO_EXPORT_BACKLOG_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"76","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["defense_component_theme_without_export_backlog_bridge","guided_weapon_export_winner_needs_4B_watch","RF_component_spike_severe_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R11-specific handling

- R11 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or an L1 policy/defense-linked branch.
- This MD uses the allowed `L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` branch.
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
- price-only/defense-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R11 allowed L1 branch.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C03 defense export rows cannot promote without export framework, signed order, orderbook/backlog, backlog-to-revenue conversion, delivery schedule quality, execution-margin proof, customer acceptance, FCF/cash conversion, or earnings revision tied to defense backlog economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R11
completed_loop = 76
next_round = R12
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
atlas/symbol_profiles/079/079550.json
atlas/symbol_profiles/005/005870.json
atlas/symbol_profiles/095/095270.json
atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
atlas/ohlcv_tradable_by_symbol_year/005/005870/2024.csv
atlas/ohlcv_tradable_by_symbol_year/095/095270/2024.csv
atlas/ohlcv_tradable_by_symbol_year/095/095270/2025.csv
```

This loop continues loop 76 with R11 and adds 3 new independent C03 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R11/L1.
