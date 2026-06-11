# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round: R3
selected_loop: 96
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: ELECTROLYTE_EV_DEMAND_ASP_UTILIZATION_HARD_4C
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_4C_protection_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent C14 rows and moves C14 from static 21 rows to local projected 24 after loop79, 27 after loop95, and 30 after this loop. The minimum 30-row stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

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

C14 is the battery/EV demand slowdown protection archetype. The calibration hinge is whether the slowdown is company-specific: utilization break, customer pull-through failure, ASP pressure, margin break, or inventory/capacity imbalance. Broad sector fear alone is not enough for hard 4C.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C14 rows | 21 |
| static C14 symbols | 17 |
| static C14 good/bad Stage2 | 3 / 3 |
| static C14 4B/4C | 5 / 7 |
| static C14 URL pending/proxy | 21 / 15 |
| static top covered symbols | 336370, 222080, 361610, 011790, 014820, 025900 |
| local C14 loop79 projected rows | 24 |
| local C14 loop95 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid the static C14 top-covered list and local C14 loop79/95 symbols `247540`, `006400`, `373220`, `051910`, `005070`, and `137400`.

| symbol | company | status |
|---|---|---|
| 278280 | 천보 | new C14 symbol; used previously only under C12 |
| 393890 | 더블유씨피 | new C14 symbol; used previously only under C12/C13 |
| 020150 | 롯데에너지머티리얼즈 | new C14 symbol; used as C14 false-hard-4C counterexample |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C14 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 278280 / 2024-02-21 | true | true | clean_180D_window | true |
| 393890 / 2024-02-21 | true | true | clean_180D_window | true |
| 020150 / 2024-02-21 | true | true | clean_180D_window | true |

Corporate-action notes:

- 천보 has zero corporate-action candidates.
- 더블유씨피 has zero corporate-action candidates.
- 롯데에너지머티리얼즈 has zero corporate-action candidates.
- SK이노베이션(096770) and 에코프로(086520) were considered but rejected because their 2024 corporate-action candidates made the candidate window less clean for this loop.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| ELECTROLYTE_EV_DEMAND_ASP_UTILIZATION_HARD_4C | C14 | electrolyte demand/ASP/utilization break routes to hard 4C |
| SEPARATOR_EV_DEMAND_UTILIZATION_MARGIN_HARD_4C | C14 | separator utilization and margin break routes to hard 4C |
| COPPER_FOIL_BROAD_EV_SLOWDOWN_FALSE_4C_ORDERBOOK_OFFSET | C14 | broad EV fear alone is false hard-4C when company orderbook offset works |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C14_CHUNBO_278280_2024_02_21_ELECTROLYTE_EV_DEMAND_HARD_4C | 278280 | 천보 | hard_4c_protection_success | positive | low MFE and severe MAE validated electrolyte demand/ASP protection |
| C14_WCP_393890_2024_02_21_SEPARATOR_EV_DEMAND_UTILIZATION_HARD_4C | 393890 | 더블유씨피 | hard_4c_protection_success | positive | separator relief failed without utilization/margin recovery |
| C14_LOTTEEM_020150_2024_02_21_FALSE_4C_COPPER_FOIL_ORDERBOOK_OFFSET | 020150 | 롯데에너지머티리얼즈 | failed_hard_4c_overblock | counterexample | broad EV fear would have blocked a 56% MFE orderbook-offset path |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 3 |
| 4C_case_count | 3 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| cross_canonical_symbol_reuse_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 278280 | source_proxy_only | electrolyte demand slowdown / ASP / utilization risk | required before promotion |
| 393890 | source_proxy_only | separator demand slowdown / utilization / margin risk | required before promotion |
| 020150 | source_proxy_only | broad EV fear only, with copper-foil orderbook offset | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 278280 | atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv | atlas/symbol_profiles/278/278280.json |
| 393890 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json |
| 020150 | atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv | atlas/symbol_profiles/020/020150.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_EV_DEMAND | 4C-Protective | 2024-02-21 | 2024-02-21 | 95600 | electrolyte EV demand/ASP/utilization break |
| WCP_393890_2024_02_21_4C_SEPARATOR_EV_DEMAND | 4C-Protective | 2024-02-21 | 2024-02-21 | 45750 | separator EV demand/utilization/margin break |
| LOTTEEM_020150_2024_02_21_FALSE_4C_BROAD_EV_SLOWDOWN | 4C-FalsePositive | 2024-02-21 | 2024-02-21 | 37800 | broad EV fear with copper-foil orderbook offset |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 278280 | 2024-02-21 | 95600 | 4.39 | -14.64 | 4.39 | -39.12 | 4.39 | -62.87 | 2024-02-21 | 99800 | -64.43 |
| 393890 | 2024-02-21 | 45750 | 8.00 | -19.34 | 8.20 | -35.96 | 8.20 | -61.29 | 2024-03-07 | 49500 | -64.22 |
| 020150 | 2024-02-21 | 37800 | 38.62 | -7.94 | 56.61 | -7.94 | 56.61 | -7.94 | 2024-06-18 | 59200 | -27.45 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 278280 | Stage2/4B-watch risk if demand break underweighted | low MFE, severe MAE | current_profile_4C_too_late |
| 393890 | Stage2/4B-watch risk if separator relief over-credited | low MFE, severe MAE | current_profile_4C_too_late |
| 020150 | hard 4C risk if broad EV fear overgeneralized | high MFE, controlled MAE | current_profile_overprotective_4C |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C14 interpretation:

- Hard 4C should fire when company-specific demand/utilization/ASP/margin break is visible.
- Hard 4C should not fire from broad EV sector fear alone if orderbook, copper-foil route, or company-specific bridge offsets the risk.
- 4B audit still applies after the successful offset rally.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 278280 | 1.00 | 1.00 | valuation overhang / weak follow-through | local peak aligned; hard 4C needed |
| 393890 | 1.00 | 1.00 | utilization bridge pending | local relief peak aligned; hard 4C needed |
| 020150 | 0.64 | 1.00 | orderbook offset / company bridge present | broad slowdown fear alone was false hard 4C |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 278280 | hard_4c_success | electrolyte demand/ASP/utilization risk protected against deep MAE |
| 393890 | hard_4c_success | separator utilization/margin risk protected against deep MAE |
| 020150 | false_4c_overblock | broad EV fear alone would have blocked a 56% MFE copper-foil route |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery/EV names, C14 hard 4C requires company-specific demand break: utilization delay, customer pull-through failure, ASP pressure, margin bridge failure, or inventory/capacity imbalance. Broad EV slowdown fear alone should cap optimism but should not hard-block names with working orderbook/CAPA/copper-foil bridge.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C14_EV_DEMAND_SLOWDOWN_4B_4C
confidence = medium
```

Candidate C14 rule:

```text
C14_company_specific_demand_break_required =
  ev_demand_slowdown
  AND (utilization_break OR customer_call_off OR asp_pressure OR margin_bridge_failure OR volume_conversion_failure OR inventory_capacity_imbalance)

if broad_ev_slowdown_fear and company_specific_break_absent and orderbook_or_copperfoil_bridge_present:
    cap_stage = Stage2-watch
    do_not_route_hard_4C = true

if MFE_90D < 10 and MAE_180D < -40:
    classify_as C14_protective_4C_success

if MFE_90D > 35 and broad_ev_slowdown_fear_only:
    classify_as C14_false_4C_overblock_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false 4C | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 23.07 | -27.67 | 23.07 | -44.03 | 1 | C14 needs company-specific demand-break split |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 23.07 | -27.67 | 23.07 | -44.03 | 1 | over-credits relief rallies and broad fear |
| P1 sector_specific_candidate_profile | L3 | 2 protective + 1 false-4C guard | 6.29 | -37.54 | 6.29 | -62.08 | 0 | better after company-specific demand gate |
| P2 canonical_archetype_candidate_profile | C14 | 2 protective + 1 false-4C guard | 6.29 | -37.54 | 6.29 | -62.08 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C14 guard | 2 protective + 1 false-4C guard | 6.29 | -37.54 | 6.29 | -62.08 | 0 | avoids broad-fear hard 4C |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 278280 | protective 4C aligned; Stage2 would be false positive | current_profile_4C_too_late |
| 393890 | protective 4C aligned; separator relief-rally Stage2 would fail | current_profile_4C_too_late |
| 020150 | hard 4C overblocked orderbook/copper-foil offset path | current_profile_overprotective_4C |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed C14 fine ids | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 24 -> local 27 -> projected 30; reaches minimum stability threshold |

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage2_actionable_evidence_bonus
residual_error_types_found:
  - current_profile_4C_too_late
  - current_profile_overprotective_4C
new_axis_proposed: C14_company_specific_demand_break_required|C14_false_4c_overblock_guard|C14_protective_4c_low_mfe_high_mae
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
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
- Uses clean 180D windows.
- Uses C14 Priority 0 coverage gap.
- Avoids static C14 top-covered symbols and local C14 loop79/95 symbols.
- Rejects 096770 and 086520 due to 2024 corporate-action contamination risk.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_company_specific_demand_break_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"278280/393890 show hard 4C works when company-level demand/utilization/margin break is visible, while 020150 shows broad fear alone over-blocks","preserves protective 4C but avoids false hard-4C for orderbook-offset names","CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_EV_DEMAND|WCP_393890_2024_02_21_4C_SEPARATOR_EV_DEMAND|LOTTEEM_020150_2024_02_21_FALSE_4C_BROAD_EV_SLOWDOWN",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C14_false_4c_overblock_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"020150 rallied 56% despite broad EV slowdown fear because copper-foil orderbook/relief route worked","prevents broad EV slowdown from automatic hard 4C","LOTTEEM_020150_2024_02_21_FALSE_4C_BROAD_EV_SLOWDOWN",1,1,1,medium,canonical_shadow_only,"false-4C guardrail"
shadow_weight,C14_protective_4c_low_mfe_high_mae,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"278280/393890 had low MFE and deep MAE after EV demand/utilization break","routes company-specific demand break to hard 4C before Stage2 promotion","CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_EV_DEMAND|WCP_393890_2024_02_21_4C_SEPARATOR_EV_DEMAND",2,2,0,medium,canonical_shadow_only,"4C/protection calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C14_CHUNBO_278280_2024_02_21_ELECTROLYTE_EV_DEMAND_HARD_4C","symbol":"278280","company_name":"천보","round":"R3","loop":"96","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"ELECTROLYTE_EV_DEMAND_ASP_UTILIZATION_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_EV_DEMAND","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol was used in C12 loop84, but this row tests C14 EV-demand/utilization hard-4C rather than customer call-off canonical","independent_evidence_weight":0.85,"score_price_alignment":"electrolyte EV-demand/ASP/utilization risk produced only 4% MFE and severe 90D/180D MAE, validating C14 hard-4C routing","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"new C14 symbol versus static top-covered list and local C14 loops; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C14_WCP_393890_2024_02_21_SEPARATOR_EV_DEMAND_UTILIZATION_HARD_4C","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"96","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_EV_DEMAND_UTILIZATION_MARGIN_HARD_4C","case_type":"hard_4c_protection_success","positive_or_counterexample":"positive","best_trigger":"WCP_393890_2024_02_21_4C_SEPARATOR_EV_DEMAND","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol was used in C12 loop84, but this row tests C14 EV-demand/utilization hard-4C rather than customer call-off canonical","independent_evidence_weight":0.85,"score_price_alignment":"separator EV-demand/utilization risk produced single-digit MFE before severe 180D MAE, validating C14 protective routing","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"new C14 symbol versus static top-covered list and local C14 loops; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C14_LOTTEEM_020150_2024_02_21_FALSE_4C_COPPER_FOIL_ORDERBOOK_OFFSET","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"96","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPER_FOIL_BROAD_EV_SLOWDOWN_FALSE_4C_ORDERBOOK_OFFSET","case_type":"failed_hard_4c_overblock","positive_or_counterexample":"counterexample","best_trigger":"LOTTEEM_020150_2024_02_21_FALSE_4C_BROAD_EV_SLOWDOWN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"020150 is a static C11 top symbol, but it has not been used in local C14 loops; this row tests C14 false-hard-4C split","independent_evidence_weight":0.9,"score_price_alignment":"broad EV slowdown fear alone would have over-blocked a copper-foil orderbook/relief route that later produced 56% MFE with controlled MAE","current_profile_verdict":"current_profile_overprotective_4C","price_source":"Songdaiki/stock-web","notes":"new C14 symbol; clean 2024 corporate-action profile"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_EV_DEMAND","case_id":"C14_CHUNBO_278280_2024_02_21_ELECTROLYTE_EV_DEMAND_HARD_4C","symbol":"278280","company_name":"천보","round":"R3","loop":"96","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"ELECTROLYTE_EV_DEMAND_ASP_UTILIZATION_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":95600.0,"evidence_available_at_that_date":"source_proxy_only: electrolyte EV demand slowdown, ASP pressure, utilization/margin risk, and weak customer pull-through visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["electrolyte_relief_rally","battery_material_route"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","valuation_overhang","peak_proximity"],"stage4c_evidence_fields":["ev_demand_slowdown","asp_pressure","utilization_risk","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.39,"MFE_90D_pct":4.39,"MFE_180D_pct":4.39,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-14.64,"MAE_90D_pct":-39.12,"MAE_180D_pct":-62.87,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":99800.0,"drawdown_after_peak_pct":-64.43,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_relief_peak_aligned_but_hard_4C_required_for_electrolyte_demand_and_margin_break","four_b_evidence_type":["weak_follow_through","valuation_overhang"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_low_mfe_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_278280_2024_02_21_95600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol was used in C12 loop84, but canonical/evidence family differs","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"WCP_393890_2024_02_21_4C_SEPARATOR_EV_DEMAND","case_id":"C14_WCP_393890_2024_02_21_SEPARATOR_EV_DEMAND_UTILIZATION_HARD_4C","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"96","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_EV_DEMAND_UTILIZATION_MARGIN_HARD_4C","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-Protective","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750.0,"evidence_available_at_that_date":"source_proxy_only: separator EV demand slowdown, utilization risk, margin bridge absence, and customer volume pressure visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["separator_relief_rally","battery_material_route"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","utilization_bridge_pending"],"stage4c_evidence_fields":["ev_demand_slowdown","utilization_risk","margin_bridge_absent","customer_volume_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.0,"MFE_90D_pct":8.2,"MFE_180D_pct":8.2,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-19.34,"MAE_90D_pct":-35.96,"MAE_180D_pct":-61.29,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":49500.0,"drawdown_after_peak_pct":-64.22,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"separator_relief_peak_failed_without_ev_demand_and_utilization_resolution","four_b_evidence_type":["weak_follow_through","utilization_bridge_pending"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"positive_protective_4c_low_mfe_high_mae","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_393890_2024_02_21_45750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol was used in C12 loop84, but canonical/evidence family differs","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LOTTEEM_020150_2024_02_21_FALSE_4C_BROAD_EV_SLOWDOWN","case_id":"C14_LOTTEEM_020150_2024_02_21_FALSE_4C_COPPER_FOIL_ORDERBOOK_OFFSET","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"96","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPER_FOIL_BROAD_EV_SLOWDOWN_FALSE_4C_ORDERBOOK_OFFSET","sector":"battery / EV / green mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_stress_test|canonical_archetype_compression","trigger_type":"4C-FalsePositive","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":37800.0,"evidence_available_at_that_date":"source_proxy_only: broad EV slowdown fear existed, but copper-foil orderbook/relief and customer route offset hard-4C; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["copper_foil_orderbook_route","customer_relief_route","relative_strength_after_entry"],"stage3_evidence_fields":["orderbook_conversion_partial","margin_bridge_pending"],"stage4b_evidence_fields":["valuation_rerating","peak_proximity_after_rerating"],"stage4c_evidence_fields":["broad_ev_slowdown_fear_only","company_specific_demand_break_not_confirmed"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","profile_path":"atlas/symbol_profiles/020/020150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.62,"MFE_90D_pct":56.61,"MFE_180D_pct":56.61,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.94,"MAE_90D_pct":-7.94,"MAE_180D_pct":-7.94,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":59200.0,"drawdown_after_peak_pct":-27.45,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.64,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"broad_sector_slowdown_fear_was_not_sufficient_for_C14_hard_4C_when_copper_foil_orderbook_offset_worked","four_b_evidence_type":["orderbook_offset","company_specific_bridge_present"],"four_c_protection_label":"false_4c_overblock","trigger_outcome_label":"counterexample_false_4c_high_mfe_orderbook_offset","current_profile_verdict":"current_profile_overprotective_4C","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_020150_2024_02_21_37800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_CHUNBO_278280_2024_02_21_ELECTROLYTE_EV_DEMAND_HARD_4C","trigger_id":"CHUNBO_278280_2024_02_21_4C_ELECTROLYTE_EV_DEMAND","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive / 4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"4C-Protective, not Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Electrolyte EV demand and ASP/utilization break should route to C14 protective 4C.","MFE_90D_pct":4.39,"MAE_90D_pct":-39.12,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_WCP_393890_2024_02_21_SEPARATOR_EV_DEMAND_UTILIZATION_HARD_4C","trigger_id":"WCP_393890_2024_02_21_4C_SEPARATOR_EV_DEMAND","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive / separator relief risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44,"stage_label_after":"4C-Protective, not Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Separator EV demand/utilization break should hard-cap Stage2 optimism.","MFE_90D_pct":8.2,"MAE_90D_pct":-35.96,"score_return_alignment_label":"protective_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_LOTTEEM_020150_2024_02_21_FALSE_4C_COPPER_FOIL_ORDERBOOK_OFFSET","trigger_id":"LOTTEEM_020150_2024_02_21_FALSE_4C_BROAD_EV_SLOWDOWN","symbol":"020150","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable with broad C14 fear","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable / not hard 4C; 4B audit after rerating","changed_components":[],"component_delta_explanation":"Broad EV slowdown fear alone should not hard-block when copper-foil orderbook/relief route offsets the sector risk.","MFE_90D_pct":56.61,"MAE_90D_pct":-7.94,"score_return_alignment_label":"false_4c_overblock_guard_needed","current_profile_verdict":"current_profile_overprotective_4C"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"96","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","stage2_actionable_evidence_bonus"],"residual_error_types_found":["current_profile_4C_too_late","current_profile_overprotective_4C"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

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
completed_loop = 96
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

If this loop is accepted together with local loop79 and loop95, C14 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C14 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/278/278280.json
  - atlas/symbol_profiles/393/393890.json
  - atlas/symbol_profiles/020/020150.json
- Rejected due to 2024 corporate-action contamination risk:
  - atlas/symbol_profiles/096/096770.json
  - atlas/symbol_profiles/086/086520.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
