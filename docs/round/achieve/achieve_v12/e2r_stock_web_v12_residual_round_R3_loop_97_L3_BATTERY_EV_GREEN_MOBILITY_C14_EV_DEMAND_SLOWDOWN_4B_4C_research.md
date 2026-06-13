# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
selected_round: R3
selected_loop: 97
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows; static C14 rows=11, need_to_30=19
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass
loop_objective: coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_filename: e2r_stock_web_v12_residual_round_R3_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_code_patch_included: false
production_scoring_patch_applied: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent C14 cases, 3 counterexamples, and 3 residual errors for R3/L3/C14.

## 1. Current Calibrated Profile Assumption

Current profile proxy: `e2r_2_1_stock_web_calibrated_proxy`.
Already-applied global axes are treated as baseline guardrails, not re-proposed globally: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`.

The residual question in this loop is narrower: within C14, when EV-demand slowdown evidence appears, should the model route immediately to hard 4C, keep only Stage4B watch, or allow Stage2-Actionable because profitability/portfolio optionality still exists?

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R3`
- large_sector_id: `L3_BATTERY_EV_GREEN_MOBILITY`
- canonical_archetype_id: `C14_EV_DEMAND_SLOWDOWN_4B_4C`
- fine_archetype_id: `mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass`
- scope consistency: `pass`

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index static Priority 0 lists C14 with 11 representative rows and need-to-30 of 19. In this conversation, C14 loop95 and loop96 already used `361610`, `006400`, `003670`, `247540`, `373220`, `093370`, `278280`, `348370`, `121600`, `336370`. This loop avoids those C14 symbols and uses five new C14 symbol/family combinations: `066970`, `393890`, `011790`, `020150`, `005070`.

Hard duplicate key avoided:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest basis:

```yaml
source_name: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
```

The schema rule used here is:

```text
MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative trigger rows in this MD satisfy:

- trigger_date is historical.
- entry_date exists in Stock-Web tradable shard.
- entry_price is the `c` column on entry_date.
- at least 180 forward tradable rows are available.
- 30D/90D/180D MFE and MAE are all computed.
- 180D corporate-action window is clean.
- no trigger row uses compact MFE/MAE aliases only.

## 6. Canonical Archetype Compression Map

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C
  -> customer_inventory_or_order_cut_break
  -> utilization_or_operating_loss_break
  -> material_price_lag_rebound_then_high_MAE
  -> parent_company_portfolio_optionality_false_hard_4C
  -> profitability_defense_without_demand_recovery_false_positive
```

Compression rule candidate:

```text
C14_CUSTOMER_INVENTORY_UTILIZATION_OR_ORDER_CUT_4C_GATE_WITH_OPTIONALITY_4B_BUFFER
```

## 7. Case Selection Summary

| symbol | company | role | evidence summary | price path interpretation |
|---:|---|---|---|---|
| 066970 | 엘앤에프 | material-price-lag 4B watch counterexample | 2023 annual operating loss and lithium-price inventory valuation loss disclosed; company also said EV-demand slowdown caused schedule changes, but order direction and volume/pricing discussions remained ongoing. | A hard 4C on the headline would have missed the 90D rebound, but leaving it as clean Stage2/3 would ignore the later -43% 180D MAE. |
| 393890 | 더블유씨피 | hard 4C protection success | 3Q24 operating loss; EV chasm, European inventory depletion, weak US OEM sales, lower utilization, and flexible new-line timing disclosed. | Confirmed utilization and customer-demand weakness protected the model from a false Stage2 recovery. |
| 011790 | SKC | false hard-4C / non-battery optionality counterexample | SK Nexilis delayed copper-foil plant completion due to slow European demand recovery; 2Q copper-foil loss and delayed turnaround were disclosed, while SKC still had portfolio optionality outside EV copper foil. | EV copper-foil evidence was negative, but a parent-company hard 4C would have missed the +59% 180D MFE driven by non-EV optionality. |
| 020150 | 롯데에너지머티리얼즈 | hard 4C protection success | 3Q24 operating loss; EV-market slowdown, customer inventory adjustment, lower Iksan/Malaysia utilization, inventory valuation loss, and limited 4Q recovery were disclosed. | The 180D path had almost no upside and a -46.8% MAE, confirming the hard 4C/customer-inventory gate. |
| 005070 | 코스모신소재 | profitable-but-high-MAE false positive | Company remained profitable despite the EV chasm and reported 2Q24 revenue and operating-profit growth, but the evidence was profitability defense rather than confirmed demand recovery. | Profitability defense alone would have looked Stage2-friendly, but the 90D/180D MAE required a C14-specific high-MAE guard. |


## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 2
counterexample_count: 3
4B_case_count: 3
4C_case_count: 2
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
current_profile_error_count: 3
```

Positive protection cases are WCP and Lotte Energy Materials, where confirmed demand/utilization/customer-inventory damage made hard 4C protection useful. Counterexamples are L&F, SKC, and Cosmo Advanced Materials, where a simple EV-slowdown headline could either over-route to hard 4C or under-route into false Stage2.

## 9. Evidence Source Map

| symbol | company | trigger_date | evidence_source | source note |
|---:|---|---:|---|---|
| 066970 | 엘앤에프 | 2024-02-01 | https://www.asiae.co.kr/en/article/2024020116473792269 | 2023 annual operating loss and lithium-price inventory valuation loss disclosed; company also said EV-demand slowdown caused schedule changes, but order direction and volume/pricing discussions remained ongoing. |
| 393890 | 더블유씨피 | 2024-11-14 | https://zdnet.co.kr/view/?no=20241114180902 | 3Q24 operating loss; EV chasm, European inventory depletion, weak US OEM sales, lower utilization, and flexible new-line timing disclosed. |
| 011790 | SKC | 2024-08-07 | https://www.koreatimes.co.kr/business/companies/20240807/sk-nexilis-lotte-energy-materials-delay-construction-of-european-copper-foil-plants-amid-ev-glut | SK Nexilis delayed copper-foil plant completion due to slow European demand recovery; 2Q copper-foil loss and delayed turnaround were disclosed, while SKC still had portfolio optionality outside EV copper foil. |
| 020150 | 롯데에너지머티리얼즈 | 2024-11-01 | https://lotteenergymaterials.com/pr/promotion_detail.do?seq=97 | 3Q24 operating loss; EV-market slowdown, customer inventory adjustment, lower Iksan/Malaysia utilization, inventory valuation loss, and limited 4Q recovery were disclosed. |
| 005070 | 코스모신소재 | 2024-07-24 | https://v.daum.net/v/20240724113600250 | Company remained profitable despite the EV chasm and reported 2Q24 revenue and operating-profit growth, but the evidence was profitability defense rather than confirmed demand recovery. |


## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | corporate_action_window_status |
|---:|---|---|---|
| 066970 | atlas/symbol_profiles/066/066970.json | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv|atlas/ohlcv_tradable_by_symbol_year/066/066970/2025.csv | clean_180D_window; profile has 2016-02-19 and 2021-08-11 candidates only |
| 393890 | atlas/symbol_profiles/393/393890.json | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv|atlas/ohlcv_tradable_by_symbol_year/393/393890/2025.csv | clean_180D_window; profile has no corporate_action_candidate_dates |
| 011790 | atlas/symbol_profiles/011/011790.json | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv|atlas/ohlcv_tradable_by_symbol_year/011/011790/2025.csv | clean_180D_window; profile has 1998-01-03 and 2001-12-21 candidates only |
| 020150 | atlas/symbol_profiles/020/020150.json | atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv|atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv | clean_180D_window; profile has no corporate_action_candidate_dates |
| 005070 | atlas/symbol_profiles/005/005070.json | atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005070/2025.csv | clean_180D_window; profile latest corporate-action candidate is 2019-11-13 |


## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C14_R3_L97_066970_20240202_LNF_MATERIAL_PRICE_LAG_HIGH_MAE | 066970 | Stage4B | 2024-02-01 | 2024-02-02 | 145600 | 24.66 | -9.27 | 36.68 | -9.27 | 36.68 | -43.06 | 2024-03-25 | 199000 | -58.34 | current_profile_4B_too_late |
| C14_R3_L97_393890_20241115_WCP_SEPARATOR_CHASM_4C | 393890 | Stage4C | 2024-11-14 | 2024-11-15 | 12500 | 7.92 | -13.28 | 7.92 | -41.28 | 7.92 | -46.0 | 2024-11-26 | 13490 | -49.96 | current_profile_correct |
| C14_R3_L97_011790_20240808_SKC_COPPERFOIL_DELAY_OPTIONALITY_REBOUND | 011790 | Stage4B | 2024-08-07 | 2024-08-08 | 113700 | 17.15 | -8.27 | 50.75 | -20.58 | 59.19 | -24.19 | 2025-01-20 | 181000 | -52.38 | current_profile_missed_structural |
| C14_R3_L97_020150_20241104_LOTTE_EM_COPPERFOIL_INVENTORY_UTILIZATION_4C | 020150 | Stage4C | 2024-11-01 | 2024-11-04 | 36550 | 1.09 | -42.82 | 1.09 | -44.6 | 1.09 | -46.76 | 2024-11-04 | 36950 | -47.33 | current_profile_correct |
| C14_R3_L97_005070_20240725_COSMO_PROFITABLE_CHASM_HIGH_MAE | 005070 | Stage2-Actionable | 2024-07-24 | 2024-07-25 | 130800 | 5.66 | -23.47 | 5.66 | -57.65 | 5.66 | -75.04 | 2024-07-26 | 138200 | -76.37 | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

Same as Section 11. Each representative trigger row is duplicated in JSONL under Section 25 with canonical keys `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`.

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely action | actual path | verdict | implication |
|---:|---|---|---|---|
| 066970 | Stage2-Actionable or weak 4B because no confirmed customer cancellation | +36.68% 90D MFE but -43.06% 180D MAE | current_profile_4B_too_late | Material-price lag can rebound, but needs earlier local 4B watch. |
| 393890 | hard 4C because customer inventory, utilization, and operating loss were all visible | +7.92% 180D MFE / -46.00% MAE | current_profile_correct | Confirmed separator demand break should block positive Stage2. |
| 011790 | possible hard 4C if EV copper-foil evidence is naively applied to parent company | +59.19% 180D MFE | current_profile_missed_structural | Parent-company optionality needs 4B watch, not automatic hard 4C. |
| 020150 | hard 4C because customer inventory, utilization, and operating loss were confirmed | +1.09% 180D MFE / -46.76% MAE | current_profile_correct | Copper-foil customer inventory/utilization break is a clean protection row. |
| 005070 | Stage2-Actionable because profitability persisted despite chasm | +5.66% 180D MFE / -75.04% MAE | current_profile_false_positive | Profitability defense is not enough without demand-recovery bridge. |

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green row is emitted. The study is about C14 down-route protection and Stage2 false-positive prevention. `green_lateness_ratio = not_applicable:no_confirmed_Stage3_Green_trigger` for all representative rows.

Stage2 should remain possible only when EV slowdown evidence is counterbalanced by confirmed demand recovery, named customer conversion, or non-EV portfolio optionality. Yellow/Green remain blocked when demand recovery is only hoped for, or when margin/utilization bridge is negative.

## 15. 4B Local vs Full-window Timing Audit

C14 needs a split between hard 4C and local 4B watch:

- L&F: hard 4C would have been too blunt because 90D MFE was +36.68%; but the later drawdown of -58.34% after peak shows local 4B watch was needed.
- SKC: parent-company optionality makes hard 4C too blunt; however, post-peak drawdown of -52.38% still argues for full-window risk overlay.
- Cosmo: profitability headline without demand bridge generated only +5.66% MFE and severe -75.04% MAE, so Stage2/Yellow should be blocked or capped by 4B watch.

## 16. 4C Protection Audit

Hard 4C succeeds when the evidence contains at least two of:

```text
customer inventory adjustment
utilization decline
operating loss directly linked to EV demand slowdown
order cut / flexible line timing / capex delay
```

WCP and Lotte Energy Materials meet this gate and show low upside with severe drawdown. SKC and L&F do not meet the same hard 4C threshold at parent-company or material-price-lag level; they require Stage4B watch instead.

## 17. Sector-Specific Rule Candidate

```text
L3_C14_EV_SLOWDOWN_UTILIZATION_CUSTOMER_INVENTORY_GATE
```

Sector rule: In L3 battery/EV materials, EV slowdown headlines should not automatically become hard 4C. Hard 4C requires a confirmed utilization/customer-inventory/order-cut/operating-loss break. If evidence is only material-price lag, profitability defense, or parent-company portfolio mix, route to Stage4B watch until demand-recovery or thesis-break proof arrives.

## 18. Canonical-Archetype Rule Candidate

```text
C14_CUSTOMER_INVENTORY_UTILIZATION_OR_ORDER_CUT_4C_GATE_WITH_OPTIONALITY_4B_BUFFER
```

C14-specific gate:

1. Confirmed customer inventory or utilization break -> Stage4C if 90D/180D MFE is low and MAE is severe.
2. Material-price lag with continuing customer discussion -> Stage4B watch, not hard 4C.
3. Parent-company optionality outside EV material exposure -> Stage4B watch, not automatic hard 4C.
4. Profitability defense without demand-recovery bridge -> cap at Stage2 watch; do not promote Yellow/Green.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | Global calibrated guardrails applied without C14 material-lag/portfolio split | 5 | 20.42 | -34.68 | 22.11 | -47.01 | 0.60 | 1 | partially aligned but still confuses temporary price-lag rebound and parent-company optionality |
| P0b e2r_2_0_baseline_reference | rollback | Earlier profile over-promotes any battery-linked rebound and under-detects hard 4C | 5 | 20.42 | -34.68 | 22.11 | -47.01 | 0.80 | 0 | weak: high-MAE false positives remain |
| P1 sector_specific_candidate_profile | L3 sector | Add utilization/customer-inventory/order-cut gate across EV materials | 5 | 13.49 | -21.27 | 15.79 | -28.80 | 0.40 | 1 | better downside filtering, but still too broad for portfolio optionality |
| P2 canonical_archetype_candidate_profile | C14 | Hard 4C only when customer inventory, utilization, order cut, or operating-loss break is confirmed; otherwise Stage4B watch | 5 | 13.49 | -21.27 | 15.79 | -28.80 | 0.20 | 0 | best alignment for this loop |
| P3 counterexample_guard_profile | C14 guardrail | Profitability defense or parent optionality cannot override high-MAE C14 watch unless demand recovery bridge exists | 5 | 13.49 | -21.27 | 15.79 | -28.80 | 0.20 | 0 | strongest false-positive control |


## 20. Score-Return Alignment Matrix

| symbol | before score/stage | after score/stage | alignment note |
|---:|---|---|---|
| 066970 | 63 / Stage2-Actionable | 57 / Stage4B-watch | inventory_loss_and_ev_slowdown_not_hard_4c_but_requires_local_4b_watch |
| 393890 | 51 / Stage4C | 47 / Stage4C | separator_customer_inventory_and_utilization_break_hard_4c_success |
| 011790 | 55 / Stage4C | 60 / Stage4B-watch | copper_foil_slowdown_is_4b_watch_not_automatic_parent_company_hard_4c |
| 020150 | 49 / Stage4C | 46 / Stage4C | copperfoil_customer_inventory_utilization_break_hard_4c_success |
| 005070 | 66 / Stage2-Actionable | 55 / Stage4B-watch | profitability_defense_does_not_override_ev_demand_slowdown_high_mae_guardrail |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass | 2 | 3 | 3 | 2 | 5 | 0 | 5 | 5 | 3 | L3_C14_EV_SLOWDOWN_UTILIZATION_CUSTOMER_INVENTORY_GATE | C14_CUSTOMER_INVENTORY_UTILIZATION_OR_ORDER_CUT_4C_GATE_WITH_OPTIONALITY_4B_BUFFER | No-Repeat static C14 11→16; current-session adjusted C14 loop95/96/97 = 11→26 |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - hard_4c_overroute_risk_when_parent_has_non_ev_optionality
  - stage2_false_positive_when_profitability_defense_lacks_demand_recovery
  - 4b_too_late_after_material_price_lag_rebound
new_axis_proposed: C14_CUSTOMER_INVENTORY_UTILIZATION_OR_ORDER_CUT_4C_GATE_WITH_OPTIONALITY_4B_BUFFER
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L3_C14_EV_SLOWDOWN_UTILIZATION_CUSTOMER_INVENTORY_GATE
canonical_archetype_rule_candidate: C14_CUSTOMER_INVENTORY_UTILIZATION_OR_ORDER_CUT_4C_GATE_WITH_OPTIONALITY_4B_BUFFER
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical trigger-level backtest using Stock-Web tradable 1D OHLCV.
- C14 evidence timing, price path, and down-route gate.
- New symbols and trigger families within C14.

Non-validation scope:

- No live candidate discovery.
- No current stock recommendation.
- No production code or scoring patch.
- No new price route discovery.
- No brokerage/API/trading action.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_customer_inventory_utilization_or_order_cut_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"hard 4C only when utilization/customer inventory/order cut/operating-loss break is confirmed","WCP and Lotte hard-4C rows had low upside and severe MAE; L&F/SKC show why hard 4C should not be automatic","T_C14_R3_L97_393890_STAGE4C_20241114|T_C14_R3_L97_020150_STAGE4C_20241101|T_C14_R3_L97_066970_STAGE4B_20240201|T_C14_R3_L97_011790_STAGE4B_20240807",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C14_profitability_defense_high_mae_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"profitability defense alone does not prove demand recovery","Cosmo remained profitable but suffered -57.65% 90D and -75.04% 180D MAE","T_C14_R3_L97_005070_STAGE2_20240724",5,5,3,medium,guardrail_shadow_only,"not production; needs batch validation"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C14_R3_L97_066970_20240202_LNF_MATERIAL_PRICE_LAG_HIGH_MAE","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"inventory_loss_and_ev_slowdown_not_hard_4c_but_requires_local_4b_watch","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"A hard 4C on the headline would have missed the 90D rebound, but leaving it as clean Stage2/3 would ignore the later -43% 180D MAE."}
{"row_type":"trigger","trigger_id":"T_C14_R3_L97_066970_STAGE4B_20240201","case_id":"C14_R3_L97_066970_20240202_LNF_MATERIAL_PRICE_LAG_HIGH_MAE","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","sector":"battery_ev_materials","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-02-01","evidence_available_at_that_date":"2023 annual operating loss and lithium-price inventory valuation loss disclosed; company also said EV-demand slowdown caused schedule changes, but order direction and volume/pricing discussions remained ongoing.","evidence_source":"https://www.asiae.co.kr/en/article/2024020116473792269","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["not_supported: margin bridge not confirmed","not_supported: durable customer confirmation not enough for hard recovery"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","explicit_event_cap","price_only_local_peak","revision_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only","not_supported: no confirmed customer cancellation at trigger date"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv|atlas/ohlcv_tradable_by_symbol_year/066/066970/2025.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":145600,"MFE_30D_pct":24.66,"MFE_90D_pct":36.68,"MFE_180D_pct":36.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.27,"MAE_90D_pct":-9.27,"MAE_180D_pct":-43.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only_or_hard_4c_single_trigger_entry","four_b_evidence_type":"margin_or_backlog_slowdown|explicit_event_cap|price_only_local_peak|revision_slowdown","four_c_protection_label":"thesis_break_watch_only_or_false_break","trigger_outcome_label":"inventory_loss_and_ev_slowdown_not_hard_4c_but_requires_local_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_R3_L97_066970_20240202_LNF_MATERIAL_PRICE_LAG_HIGH_MAE|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L97_066970_20240202_LNF_MATERIAL_PRICE_LAG_HIGH_MAE","trigger_id":"T_C14_R3_L97_066970_STAGE4B_20240201","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":35,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":75,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":35,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":85,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":57,"stage_label_after":"Stage4B-watch","changed_components":["utilization_score","margin_bridge_score","execution_risk_score","customer_inventory_or_order_cut_gate"],"component_delta_explanation":"C14-specific shadow pass separates temporary material-price lag / portfolio optionality from confirmed utilization, customer inventory, or order-cut break. Scores are research proxies only, not production scoring.","MFE_90D_pct":36.68,"MAE_90D_pct":-9.27,"score_return_alignment_label":"inventory_loss_and_ev_slowdown_not_hard_4c_but_requires_local_4b_watch","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C14_R3_L97_393890_20241115_WCP_SEPARATOR_CHASM_4C","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"separator_customer_inventory_and_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Confirmed utilization and customer-demand weakness protected the model from a false Stage2 recovery."}
{"row_type":"trigger","trigger_id":"T_C14_R3_L97_393890_STAGE4C_20241114","case_id":"C14_R3_L97_393890_20241115_WCP_SEPARATOR_CHASM_4C","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","sector":"battery_ev_materials","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-11-14","evidence_available_at_that_date":"3Q24 operating loss; EV chasm, European inventory depletion, weak US OEM sales, lower utilization, and flexible new-line timing disclosed.","evidence_source":"https://zdnet.co.kr/view/?no=20241114180902","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["not_supported: margin bridge broken","not_supported: repeat conversion not visible"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay","revision_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv|atlas/ohlcv_tradable_by_symbol_year/393/393890/2025.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-15","entry_price":12500,"MFE_30D_pct":7.92,"MFE_90D_pct":7.92,"MFE_180D_pct":7.92,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.28,"MAE_90D_pct":-41.28,"MAE_180D_pct":-46.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-26","peak_price":13490,"drawdown_after_peak_pct":-49.96,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only_or_hard_4c_single_trigger_entry","four_b_evidence_type":"margin_or_backlog_slowdown|contract_delay|revision_slowdown","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"separator_customer_inventory_and_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_R3_L97_393890_20241115_WCP_SEPARATOR_CHASM_4C|2024-11-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L97_393890_20241115_WCP_SEPARATOR_CHASM_4C","trigger_id":"T_C14_R3_L97_393890_STAGE4C_20241114","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":10,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":90,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":51,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":10,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":47,"stage_label_after":"Stage4C","changed_components":["utilization_score","margin_bridge_score","execution_risk_score","customer_inventory_or_order_cut_gate"],"component_delta_explanation":"C14-specific shadow pass separates temporary material-price lag / portfolio optionality from confirmed utilization, customer inventory, or order-cut break. Scores are research proxies only, not production scoring.","MFE_90D_pct":7.92,"MAE_90D_pct":-41.28,"score_return_alignment_label":"separator_customer_inventory_and_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C14_R3_L97_011790_20240808_SKC_COPPERFOIL_DELAY_OPTIONALITY_REBOUND","symbol":"011790","company_name":"SKC","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","case_type":"missed_structural","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"copper_foil_slowdown_is_4b_watch_not_automatic_parent_company_hard_4c","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"EV copper-foil evidence was negative, but a parent-company hard 4C would have missed the +59% 180D MFE driven by non-EV optionality."}
{"row_type":"trigger","trigger_id":"T_C14_R3_L97_011790_STAGE4B_20240807","case_id":"C14_R3_L97_011790_20240808_SKC_COPPERFOIL_DELAY_OPTIONALITY_REBOUND","symbol":"011790","company_name":"SKC","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","sector":"battery_ev_materials","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-08-07","evidence_available_at_that_date":"SK Nexilis delayed copper-foil plant completion due to slow European demand recovery; 2Q copper-foil loss and delayed turnaround were disclosed, while SKC still had portfolio optionality outside EV copper foil.","evidence_source":"https://www.koreatimes.co.kr/business/companies/20240807/sk-nexilis-lotte-energy-materials-delay-construction-of-european-copper-foil-plants-amid-ev-glut","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["not_supported: battery-material margin bridge broken","not_supported: copper-foil conversion delayed"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay","explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch_only","not_supported: portfolio-level thesis not fully broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv|atlas/ohlcv_tradable_by_symbol_year/011/011790/2025.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-08","entry_price":113700,"MFE_30D_pct":17.15,"MFE_90D_pct":50.75,"MFE_180D_pct":59.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.27,"MAE_90D_pct":-20.58,"MAE_180D_pct":-24.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-20","peak_price":181000,"drawdown_after_peak_pct":-52.38,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only_or_hard_4c_single_trigger_entry","four_b_evidence_type":"margin_or_backlog_slowdown|contract_delay|explicit_event_cap|positioning_overheat","four_c_protection_label":"thesis_break_watch_only_or_false_break","trigger_outcome_label":"copper_foil_slowdown_is_4b_watch_not_automatic_parent_company_hard_4c","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_R3_L97_011790_20240808_SKC_COPPERFOIL_DELAY_OPTIONALITY_REBOUND|2024-08-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L97_011790_20240808_SKC_COPPERFOIL_DELAY_OPTIONALITY_REBOUND","trigger_id":"T_C14_R3_L97_011790_STAGE4B_20240807","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":80,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":55,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":55,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage4B-watch","changed_components":["utilization_score","margin_bridge_score","execution_risk_score","customer_inventory_or_order_cut_gate"],"component_delta_explanation":"C14-specific shadow pass separates temporary material-price lag / portfolio optionality from confirmed utilization, customer inventory, or order-cut break. Scores are research proxies only, not production scoring.","MFE_90D_pct":50.75,"MAE_90D_pct":-20.58,"score_return_alignment_label":"copper_foil_slowdown_is_4b_watch_not_automatic_parent_company_hard_4c","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C14_R3_L97_020150_20241104_LOTTE_EM_COPPERFOIL_INVENTORY_UTILIZATION_4C","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"copperfoil_customer_inventory_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"The 180D path had almost no upside and a -46.8% MAE, confirming the hard 4C/customer-inventory gate."}
{"row_type":"trigger","trigger_id":"T_C14_R3_L97_020150_STAGE4C_20241101","case_id":"C14_R3_L97_020150_20241104_LOTTE_EM_COPPERFOIL_INVENTORY_UTILIZATION_4C","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","sector":"battery_ev_materials","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-11-01","evidence_available_at_that_date":"3Q24 operating loss; EV-market slowdown, customer inventory adjustment, lower Iksan/Malaysia utilization, inventory valuation loss, and limited 4Q recovery were disclosed.","evidence_source":"https://lotteenergymaterials.com/pr/promotion_detail.do?seq=97","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["not_supported: margin bridge broken","not_supported: utilization visible but negative"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","revision_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv|atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv","profile_path":"atlas/symbol_profiles/020/020150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-04","entry_price":36550,"MFE_30D_pct":1.09,"MFE_90D_pct":1.09,"MFE_180D_pct":1.09,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-42.82,"MAE_90D_pct":-44.6,"MAE_180D_pct":-46.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-04","peak_price":36950,"drawdown_after_peak_pct":-47.33,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only_or_hard_4c_single_trigger_entry","four_b_evidence_type":"margin_or_backlog_slowdown|revision_slowdown|explicit_event_cap","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"copperfoil_customer_inventory_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_R3_L97_020150_20241104_LOTTE_EM_COPPERFOIL_INVENTORY_UTILIZATION_4C|2024-11-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L97_020150_20241104_LOTTE_EM_COPPERFOIL_INVENTORY_UTILIZATION_4C","trigger_id":"T_C14_R3_L97_020150_STAGE4C_20241101","symbol":"020150","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":5,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":49,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":5,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":98,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage4C","changed_components":["utilization_score","margin_bridge_score","execution_risk_score","customer_inventory_or_order_cut_gate"],"component_delta_explanation":"C14-specific shadow pass separates temporary material-price lag / portfolio optionality from confirmed utilization, customer inventory, or order-cut break. Scores are research proxies only, not production scoring.","MFE_90D_pct":1.09,"MAE_90D_pct":-44.6,"score_return_alignment_label":"copperfoil_customer_inventory_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C14_R3_L97_005070_20240725_COSMO_PROFITABLE_CHASM_HIGH_MAE","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"profitability_defense_does_not_override_ev_demand_slowdown_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Profitability defense alone would have looked Stage2-friendly, but the 90D/180D MAE required a C14-specific high-MAE guard."}
{"row_type":"trigger","trigger_id":"T_C14_R3_L97_005070_STAGE2_20240724","case_id":"C14_R3_L97_005070_20240725_COSMO_PROFITABLE_CHASM_HIGH_MAE","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_ev_demand_slowdown_materials_copperfoil_separator_third_pass","sector":"battery_ev_materials","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-24","evidence_available_at_that_date":"Company remained profitable despite the EV chasm and reported 2Q24 revenue and operating-profit growth, but the evidence was profitability defense rather than confirmed demand recovery.","evidence_source":"https://v.daum.net/v/20240724113600250","stage2_evidence_fields":["public_event_or_disclosure","margin_bridge","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility_partial","not_supported: durable EV customer demand recovery not confirmed"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak","revision_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005070/2025.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-25","entry_price":130800,"MFE_30D_pct":5.66,"MFE_90D_pct":5.66,"MFE_180D_pct":5.66,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.47,"MAE_90D_pct":-57.65,"MAE_180D_pct":-75.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-26","peak_price":138200,"drawdown_after_peak_pct":-76.37,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only_or_hard_4c_single_trigger_entry","four_b_evidence_type":"valuation_blowoff|positioning_overheat|price_only_local_peak|revision_slowdown","four_c_protection_label":"thesis_break_watch_only_or_false_break","trigger_outcome_label":"profitability_defense_does_not_override_ev_demand_slowdown_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_R3_L97_005070_20240725_COSMO_PROFITABLE_CHASM_HIGH_MAE|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3_L97_005070_20240725_COSMO_PROFITABLE_CHASM_HIGH_MAE","trigger_id":"T_C14_R3_L97_005070_STAGE2_20240724","symbol":"005070","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":45,"revision_score":35,"relative_strength_score":25,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":30,"revision_score":20,"relative_strength_score":25,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":75,"execution_risk_score":85,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage4B-watch","changed_components":["utilization_score","margin_bridge_score","execution_risk_score","customer_inventory_or_order_cut_gate"],"component_delta_explanation":"C14-specific shadow pass separates temporary material-price lag / portfolio optionality from confirmed utilization, customer inventory, or order-cut break. Scores are research proxies only, not production scoring.","MFE_90D_pct":5.66,"MAE_90D_pct":-57.65,"score_return_alignment_label":"profitability_defense_does_not_override_ev_demand_slowdown_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"97","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["hard_4c_overroute_risk_when_parent_has_non_ev_optionality","stage2_false_positive_when_profitability_defense_lacks_demand_recovery","4b_too_late_after_material_price_lag_rebound"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
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
completed_loop = 97
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows; static C14 rows=11, need_to_30=19
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C14_EV_DEMAND_SLOWDOWN_4B_4C_followup_if_still_below_30 | C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Evidence sources are listed per case in Section 9 and in JSONL `evidence_source` fields.
