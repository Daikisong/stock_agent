# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R11
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R12
computed_next_loop: 73
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: C03_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r11_branch: L1_defense_linked_allowed
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

R11 allows the L10 policy/event branch or an L1 defense-linked branch. This run uses the defense-linked branch because R11 loop 72 already covered C32 governance/control premium. The selected C03 residual avoids the top-covered defense cluster and focuses on aerospace/guided-weapon export backlog.

| layer | id | definition |
|---|---|---|
| round | R11 | policy/event cross round with L1 defense-linked allowance |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | industrials, defense, export backlog, infra/grid |
| canonical | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | defense export framework, backlog, delivery, margin bridge |
| fine | C03_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_GUARD | defense theme must convert into export/backlog/delivery/margin bridge |
| deep | MIDDLE_EAST_GUIDED_WEAPON_EXPORT_BACKLOG_TO_REVENUE_AND_MARGIN | guided-weapon export backlog positive |
| deep | AIRCRAFT_EXPORT_BACKLOG_DELIVERY_TO_MARGIN_AND_PLATFORM_OPTIONALITY | aircraft export/delivery delayed positive |
| deep | SPACE_DEFENSE_AEROSTRUCTURE_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CONVERSION | aerospace subcontractor false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C03 top-covered symbols are `064350`, `272210`, `UNKNOWN_SYMBOL`, `012450`, `010820`, and `003570`. This run avoids that cluster and also avoids using R1 C01/C05 infrastructure names.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C03 | 079550 | new independent | not top-covered C03 symbol; guided-weapon export/backlog/margin bridge |
| C03 | 047810 | new independent | not top-covered C03 symbol; aerospace defense export/delivery bridge |
| C03 | 274090 | new independent | not top-covered C03 symbol; aerospace subcontractor theme false start |

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
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
079550 has no corporate-action candidate dates.
047810 has no corporate-action candidate dates.
274090 has a 2021-03-25 corporate-action candidate date, outside the selected 2024 representative window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 079550 | LIG넥스원 | Stage2-Actionable | 2024-02-14 | 127000 | export framework/backlog/margin bridge worked |
| structural_success_delayed_then_4B_watch | 047810 | 한국항공우주 | Stage2-Actionable | 2024-07-26 | 51100 | aerospace export/delivery bridge worked later |
| failed_rerating_low_MFE_high_MAE | 274090 | 켄코아에어로스페이스 | Stage2-Actionable | 2024-01-18 | 14840 | aerospace/space defense theme lacked customer backlog and margin bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 1
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 079550 | LIG넥스원 | Stage2-Actionable | 2024-02-14 | 127000 | 50.63 | 74.41 | 108.66 | -0.94 | -0.94 | -0.94 | 2024-10-22 | 265000 | -11.32 |
| 047810 | 한국항공우주 | Stage2-Actionable | 2024-07-26 | 51100 | 15.85 | 38.16 | 91.78 | -6.07 | -6.07 | -6.07 | 2025-03-18 | 98000 | -27.96 |
| 274090 | 켄코아에어로스페이스 | Stage2-Actionable | 2024-01-18 | 14840 | 7.14 | 7.14 | 7.14 | -25.4 | -28.23 | -34.91 | 2024-01-18 | 15900 | -39.25 |

## 9. Case-by-Case Notes

### 9.1 079550 / LIG넥스원 — guided-weapon export backlog bridge

The entry row is 2024-02-14 at 127,000. The 30D path reaches 191,300, the 90D path reaches 221,500, and the wider path reaches 265,000. This is a valid C03 positive because price strength was supported by the defense-export stack: customer quality, export framework, backlog-to-revenue route, and margin visibility.

### 9.2 047810 / 한국항공우주 — aerospace export/delivery bridge

The entry row is 2024-07-26 at 51,100. The first 30D path reaches 59,200, but the larger move comes later as delivery/platform optionality and defense export evidence compound. This is a delayed C03 success. The correct label is Yellow plus 4B watch, because the engine starts slowly and then accelerates.

### 9.3 274090 / 켄코아에어로스페이스 — aerospace subcontractor theme false start

The entry row is 2024-01-18 at 14,840. The path reaches only 15,900, then falls to 9,660. This is the C03 trap: aerospace, space, and defense optionality can sound like export backlog, but without repeat customer orders, delivery visibility, margin conversion, or cashflow, the theme is just a runway without an aircraft.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C03 treats aerospace/defense theme price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C03 needs export/backlog/delivery/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 274090 and delayed 4B winners. |
| Full 4B non-price requirement appropriate? | Yes. 079550/047810 have non-price bridge evidence; 274090 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
079550:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after export framework / backlog / margin bridge
  Stage3-Green = wait for delivery durability and post-MFE 4B review

047810:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after aircraft delivery / export platform bridge
  Stage3-Green = reject unless delayed MFE and execution risk are cleared

274090:
  Stage2-Actionable = too generous if based only on aerospace/space/defense theme
  Stage3-Yellow = reject without customer backlog, delivery, margin, or repeat-order bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 079550 | 0.94 | 1.00 | good full-window 4B watch after export backlog/margin bridge |
| 047810 | 0.72 | 1.00 | delayed full-window 4B watch after delivery/margin bridge |
| 274090 | 1.00 | 1.00 | aerospace theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c03_requires_export_framework_backlog_delivery_margin_bridge

rule:
  For C03 defense/export rows, do not promote defense, aerospace, space,
  weapon-system, or geopolitical-demand Stage2 signals into Stage3-Yellow/Green unless at least
  one non-price bridge is visible:
  export framework, customer country quality, contract/backlog confirmation,
  delivery schedule, backlog-to-revenue conversion, margin bridge, follow-on order,
  platform expansion, or FCF/cash conversion.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 39.9 | -11.75 | 33.3% | useful but can over-credit aerospace theme |
| P0b e2r_2_0_baseline_reference | 3 | 39.9 | -11.75 | 0% | safer but may miss 079550/047810 |
| P1 sector_specific_candidate_profile | 3 | 39.9 | -11.75 | 33.3% | no broad L1 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 56.28 | -3.5 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 7.14 | -28.23 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 079550 | current_profile_correct | guided-weapon export/backlog bridge aligned with strong MFE |
| 047810 | current_profile_partially_correct | aerospace delivery bridge worked later, requiring delayed 4B watch |
| 274090 | current_profile_false_positive | aerospace/space theme produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | C03_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_GUARD | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 1 | false | true | R11 defense-linked C03 non-top-covered aerospace/guided-weapon residual reduced |

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
- aerospace defense theme without backlog/margin bridge
- defense export winner needs 4B watch
- delayed MFE after delivery/margin bridge
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
- R11 defense-linked branch consistency
- large_sector/canonical consistency under allowed R11 branch
- duplicate avoidance at symbol level
- representative rows use clean forward windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c03_requires_export_framework_backlog_delivery_margin_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"R11 defense-linked branch: C03 defense/export rows should not promote toward Stage3-Yellow/Green unless defense or aerospace signal converts into export framework, customer quality, backlog-to-revenue, delivery, margin, follow-on order, or FCF bridge","079550 and 047810 survive after export/backlog/delivery bridge; 274090 fails when aerospace/space/defense theme lacks customer backlog and margin bridge","TRG_R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE|TRG_R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE|TRG_R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c03_defense_export_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,1,1,0,"Defense export winners and aerospace-theme false starts can peak before delivery and margin durability is confirmed; local/full-window 4B and high-MAE watch must remain active","preserves 079550/047810 positives while preventing 274090 aerospace-theme false positive","TRG_R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE|TRG_R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE|TRG_R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","symbol":"079550","company_name":"LIG넥스원","round":"R11","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_GUIDED_WEAPON_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE","deep_sub_archetype_id":"MIDDLE_EAST_GUIDED_WEAPON_EXPORT_BACKLOG_TO_REVENUE_AND_MARGIN","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"R11 defense-linked branch: C03 defense/export rows require export framework, customer quality, backlog-to-revenue, delivery, margin, or follow-on order bridge; defense/aerospace theme alone is insufficient."}
{"row_type":"case","case_id":"R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE","symbol":"047810","company_name":"한국항공우주","round":"R11","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AEROSPACE_DEFENSE_EXPORT_DELIVERY_MARGIN_BRIDGE","deep_sub_archetype_id":"AIRCRAFT_EXPORT_BACKLOG_DELIVERY_TO_MARGIN_AND_PLATFORM_OPTIONALITY","case_type":"structural_success_delayed_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_late","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"R11 defense-linked branch: C03 defense/export rows require export framework, customer quality, backlog-to-revenue, delivery, margin, or follow-on order bridge; defense/aerospace theme alone is insufficient."}
{"row_type":"case","case_id":"R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE","symbol":"274090","company_name":"켄코아에어로스페이스","round":"R11","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AEROSPACE_SUBCONTRACT_THEME_WITHOUT_CUSTOMER_BACKLOG_MARGIN_BRIDGE","deep_sub_archetype_id":"SPACE_DEFENSE_AEROSTRUCTURE_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CONVERSION","case_type":"failed_rerating_low_MFE_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R11 defense-linked branch: C03 defense/export rows require export framework, customer quality, backlog-to-revenue, delivery, margin, or follow-on order bridge; defense/aerospace theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","case_id":"R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","symbol":"079550","company_name":"LIG넥스원","round":"R11","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_GUIDED_WEAPON_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE","deep_sub_archetype_id":"MIDDLE_EAST_GUIDED_WEAPON_EXPORT_BACKLOG_TO_REVENUE_AND_MARGIN","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":127000,"evidence_available_at_that_date":"source_proxy_guided_weapon_export_framework_backlog_revenue_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_guided_weapon_export_framework_backlog_revenue_margin_bridge; evidence_url_pending","bridge_summary":"guided-weapon export framework and backlog translated into revenue, margin, and customer-quality visibility rather than defense headline alone","stage2_evidence_fields":["defense_export_framework","guided_weapon_backlog","customer_country_quality","relative_strength"],"stage3_evidence_fields":["backlog_to_revenue_visibility","margin_bridge","repeat_export_or_follow_on_optionality"],"stage4b_evidence_fields":["post_MFE_peak_watch","defense_export_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","profile_path":"atlas/symbol_profiles/079/079550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":50.63,"MFE_90D_pct":74.41,"MFE_180D_pct":108.66,"MFE_1Y_pct":108.66,"MFE_2Y_pct":108.66,"MAE_30D_pct":-0.94,"MAE_90D_pct":-0.94,"MAE_180D_pct":-0.94,"MAE_1Y_pct":-0.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-22","peak_price":265000,"drawdown_after_peak_pct":-11.32,"green_lateness_ratio":"0.36","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_export_backlog_margin_bridge","four_b_evidence_type":"non_price_export_backlog_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE","case_id":"R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE","symbol":"047810","company_name":"한국항공우주","round":"R11","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AEROSPACE_DEFENSE_EXPORT_DELIVERY_MARGIN_BRIDGE","deep_sub_archetype_id":"AIRCRAFT_EXPORT_BACKLOG_DELIVERY_TO_MARGIN_AND_PLATFORM_OPTIONALITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":51100,"evidence_available_at_that_date":"source_proxy_aerospace_defense_aircraft_export_delivery_margin_platform_bridge; evidence_url_pending","evidence_source":"source_proxy_aerospace_defense_aircraft_export_delivery_margin_platform_bridge; evidence_url_pending","bridge_summary":"aircraft/export backlog and delivery/platform optionality eventually converted into strong MFE, but the route required delivery and margin bridge confirmation","stage2_evidence_fields":["aerospace_defense_export_backlog","aircraft_delivery_visibility","platform_optional_route","relative_strength"],"stage3_evidence_fields":["delivery_to_revenue_visibility","margin_bridge","export_platform_follow_on_optional"],"stage4b_evidence_fields":["delayed_MFE_peak_watch","aerospace_defense_rerating_crowding"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv|atlas/ohlcv_tradable_by_symbol_year/047/047810/2025.csv","profile_path":"atlas/symbol_profiles/047/047810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.85,"MFE_90D_pct":38.16,"MFE_180D_pct":91.78,"MFE_1Y_pct":91.78,"MFE_2Y_pct":91.78,"MAE_30D_pct":-6.07,"MAE_90D_pct":-6.07,"MAE_180D_pct":-6.07,"MAE_1Y_pct":-6.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-18","peak_price":98000,"drawdown_after_peak_pct":-27.96,"green_lateness_ratio":"0.58","four_b_local_peak_proximity":0.72,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"delayed_full_window_4B_watch_after_delivery_margin_bridge","four_b_evidence_type":"non_price_export_backlog_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_delayed_then_4B_watch","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE","case_id":"R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE","symbol":"274090","company_name":"켄코아에어로스페이스","round":"R11","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_AEROSPACE_SUBCONTRACT_THEME_WITHOUT_CUSTOMER_BACKLOG_MARGIN_BRIDGE","deep_sub_archetype_id":"SPACE_DEFENSE_AEROSTRUCTURE_OPTIONALITY_WITHOUT_REPEAT_ORDER_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":14840,"evidence_available_at_that_date":"source_proxy_aerospace_subcontract_space_defense_theme_without_customer_backlog_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_aerospace_subcontract_space_defense_theme_without_customer_backlog_margin_bridge; evidence_url_pending","bridge_summary":"aerospace/space/defense subcontractor theme lacked repeat customer order, backlog conversion, margin, and cashflow bridge; upside stayed shallow while MAE expanded","stage2_evidence_fields":["aerospace_defense_theme","space_optional_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","customer_backlog_bridge_absent","margin_conversion_absent"],"stage4c_evidence_fields":["high_MAE_without_backlog_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/274/274090/2024.csv","profile_path":"atlas/symbol_profiles/274/274090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.14,"MFE_90D_pct":7.14,"MFE_180D_pct":7.14,"MFE_1Y_pct":7.14,"MFE_2Y_pct":7.14,"MAE_30D_pct":-25.4,"MAE_90D_pct":-28.23,"MAE_180D_pct":-34.91,"MAE_1Y_pct":-34.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-18","peak_price":15900,"drawdown_after_peak_pct":-39.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"aerospace_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"aerospace_defense_theme_without_backlog_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","trigger_id":"TRG_R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","symbol":"079550","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"export_framework_score":12,"customer_backlog_score":13,"delivery_revenue_score":11,"margin_bridge_score":10,"relative_strength_score":10,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_framework_score":15,"customer_backlog_score":16,"delivery_revenue_score":14,"margin_bridge_score":13,"relative_strength_score":8,"risk_penalty":5},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["export_framework_score","customer_backlog_score","delivery_revenue_score","margin_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C03 row is promoted only because defense export framework converts into backlog-to-revenue, delivery and margin bridge.","MFE_90D_pct":74.41,"MAE_90D_pct":-0.94,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE","trigger_id":"TRG_R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE","symbol":"047810","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"export_framework_score":10,"customer_backlog_score":11,"delivery_revenue_score":9,"margin_bridge_score":8,"relative_strength_score":10,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_framework_score":13,"customer_backlog_score":14,"delivery_revenue_score":12,"margin_bridge_score":10,"relative_strength_score":7,"risk_penalty":8},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["export_framework_score","customer_backlog_score","delivery_revenue_score","margin_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C03 aerospace defense bridge works, but delayed peak and execution risk prevent Green loosening.","MFE_90D_pct":38.16,"MAE_90D_pct":-6.07,"score_return_alignment_label":"score_return_aligned_late","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE","trigger_id":"TRG_R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE","symbol":"274090","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"export_framework_score":5,"customer_backlog_score":1,"delivery_revenue_score":1,"margin_bridge_score":0,"relative_strength_score":10,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"export_framework_score":2,"customer_backlog_score":0,"delivery_revenue_score":0,"margin_bridge_score":0,"relative_strength_score":4,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["export_framework_score","customer_backlog_score","delivery_revenue_score","margin_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C03 guard demotes aerospace/defense theme rows when export/backlog/customer, delivery, revenue, margin or FCF bridge is absent.","MFE_90D_pct":7.14,"MAE_90D_pct":-28.23,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c03_requires_export_framework_backlog_delivery_margin_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,0,1,+1,"R11 defense-linked branch: C03 defense/export rows should not promote toward Stage3-Yellow/Green unless defense or aerospace signal converts into export framework, customer quality, backlog-to-revenue, delivery, margin, follow-on order, or FCF bridge","079550 and 047810 survive after export/backlog/delivery bridge; 274090 fails when aerospace/space/defense theme lacks customer backlog and margin bridge","TRG_R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE|TRG_R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE|TRG_R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c03_defense_export_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,1,1,0,"Defense export winners and aerospace-theme false starts can peak before delivery and margin durability is confirmed; local/full-window 4B and high-MAE watch must remain active","preserves 079550/047810 positives while preventing 274090 aerospace-theme false positive","TRG_R11L73_C03_079550_20240214_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE|TRG_R11L73_C03_047810_20240726_AEROSPACE_DEFENSE_EXPORT_DELIVERY_BRIDGE|TRG_R11L73_C03_274090_20240118_AEROSPACE_SUBCONTRACT_THEME_NO_BACKLOG_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["aerospace_defense_theme_without_backlog_margin_bridge","defense_export_winner_needs_4B_watch","delayed_MFE_after_delivery_margin_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R11-specific handling

- R11 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or a defense-linked `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` branch.
- This MD uses the allowed L1 defense-linked branch.
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
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/defense-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R11 allowed branch and large_sector_id.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C03 defense/export rows cannot promote without export framework, customer quality, backlog-to-revenue, delivery schedule, margin, follow-on order, or FCF bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R11
completed_loop = 73
next_round = R12
next_loop = 73
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
atlas/symbol_profiles/047/047810.json
atlas/symbol_profiles/274/274090.json
atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv
atlas/ohlcv_tradable_by_symbol_year/047/047810/2025.csv
atlas/ohlcv_tradable_by_symbol_year/274/274090/2024.csv
```

This loop continues loop 73 with R11 and adds 3 new independent C03 representative cases, 2 positives, 1 counterexample, and 1 residual error for R11/L1/C03.
