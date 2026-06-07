# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round: R1
selected_loop: 90
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_DATACENTER_EXPORT_BACKLOG_CAPA_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent C02 rows and, after the locally generated loop 81, moves C02 from projected 27 rows to projected 30 rows.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C02:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R1 -> L1_INDUSTRIALS_INFRA_DEFENSE_GRID
C02 -> C02_POWER_GRID_DATACENTER_CAPEX
```

C02 is the grid / transformer / cable / data-center power bottleneck archetype. The real bridge is:

```text
power-demand narrative -> backlog/CAPA slot -> ASP or margin bridge -> EPS/FCF conversion
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C02 rows | 24 |
| static C02 symbols | 13 |
| static C02 good/bad Stage2 | 8 / 3 |
| static C02 4B/4C | 3 / 1 |
| static C02 URL pending/proxy | 21 / 18 |
| top covered symbols | 199820, 103590, 267260, 298040, 010120, 237750 |
| local C02 loop 81 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid both the static top-covered C02 list and the local loop 81 C02 symbols `006260`, `017510`, and `189860`.

| symbol | company | status |
|---|---|---|
| 033100 | 제룡전기 | new C02 symbol versus static top-covered and local C02 loop |
| 006340 | 대원전선 | new C02 symbol versus static top-covered and local C02 loop |
| 017040 | 광명전기 | new C02 symbol versus static top-covered and local C02 loop |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated loop memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 033100 / 2024-03-06 | true | true | clean_180D_window | true |
| 006340 / 2024-04-05 | true | true | clean_180D_window | true |
| 017040 / 2024-05-07 | true | true | clean_180D_window | true |

Corporate-action notes:

- 제룡전기 has corporate-action candidates only through 2014.
- 대원전선 has corporate-action candidates only through 2010.
- 광명전기 has corporate-action candidates only through 2001.
- 001440 and 000500 were considered but rejected because their profiles contain 2024 corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| TRANSFORMER_DATACENTER_EXPORT_BACKLOG_CAPA_4B_WATCH | C02 | transformer export/datacenter power bottleneck; CAPA and ASP bridge needed before Green |
| GRID_CABLE_SMALLCAP_ORDER_BETA_4B_HIGH_MAE | C02 | small-cap cable beta can work but has high 4B and execution-risk load |
| SWITCHGEAR_GRID_EVENT_PREMIUM_BACKLOG_BRIDGE_ABSENT | C02 | switchgear/event premium without backlog/CAPA bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C02_JERYONG_033100_2024_03_06_TRANSFORMER_DATACENTER_EXPORT_RERATING | 033100 | 제룡전기 | 4B_overlay_success | positive | transformer/export/datacenter route produced extreme MFE and later deep peak drawdown |
| C02_DAEWONCABLE_006340_2024_04_05_GRID_CABLE_SMALLCAP_BETA_4B | 006340 | 대원전선 | high_mfe_high_mae_success | positive | cable small-cap beta produced huge MFE but demanded 4B audit |
| C02_KWANGMYUNG_017040_2024_05_07_SWITCHGEAR_EVENT_PREMIUM_FALSE_POSITIVE | 017040 | 광명전기 | failed_rerating | counterexample | late event premium had only 4% MFE and deep MAE without backlog/CAPA bridge |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 033100 | source_proxy_only | transformer/export/datacenter route; CAPA/ASP bridge partial | required before promotion |
| 006340 | source_proxy_only | cable/grid small-cap beta; order bridge partial | required before promotion |
| 017040 | source_proxy_only | switchgear event premium but backlog/CAPA bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 033100 | atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv | atlas/symbol_profiles/033/033100.json |
| 006340 | atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv | atlas/symbol_profiles/006/006340.json |
| 017040 | atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv | atlas/symbol_profiles/017/017040.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| JERYONG_033100_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_EXPORT | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 30700 | transformer/export/datacenter power bottleneck |
| DAEWONCABLE_006340_2024_04_05_STAGE2A_GRID_CABLE_SMALLCAP_BETA | Stage2-Actionable | 2024-04-05 | 2024-04-05 | 2095 | grid cable small-cap beta |
| KWANGMYUNG_017040_2024_05_07_STAGE2_FALSE_POSITIVE_SWITCHGEAR_EVENT_PREMIUM | Stage2 | 2024-05-07 | 2024-05-07 | 3185 | late switchgear event premium without backlog/CAPA bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 033100 | 2024-03-06 | 30700 | 84.04 | -11.07 | 228.01 | -11.07 | 228.01 | -11.07 | 2024-07-11 | 100700 | -63.70 |
| 006340 | 2024-04-05 | 2095 | 160.14 | -16.61 | 160.14 | -16.61 | 160.14 | -16.61 | 2024-05-13 | 5450 | -51.56 |
| 017040 | 2024-05-07 | 3185 | 4.24 | -30.93 | 4.24 | -51.33 | 4.24 | -55.01 | 2024-05-08 | 3320 | -56.84 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 033100 | Stage2A/Yellow possible; 4B after extreme rerating | extreme MFE, later deep peak drawdown | current_profile_4B_too_late |
| 006340 | Stage2A possible; high small-cap 4B risk | huge MFE, high MAE and drawdown | current_profile_4B_too_late |
| 017040 | Stage2 risk if event premium is over-credited | low MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C02 interpretation:

- Stage2A can work when transformer/cable demand is tied to export backlog, datacenter power bottleneck, CAPA slot, or ASP evidence.
- Yellow/Green require backlog conversion, CAPA visibility, ASP/margin bridge, revision, and FCF.
- Late switchgear or grid event premium without bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 033100 | 1.00 | 1.00 | valuation / positioning | extreme MFE requires 4B audit |
| 006340 | 1.00 | 1.00 | small-cap price extension | 4B audit required before Yellow/Green |
| 017040 | 1.00 | 1.00 | event premium / price-only | not Stage3 without backlog/CAPA bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 033100 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 006340 | thesis_break_watch_only | not hard 4C, but high-MAE small-cap 4B cap needed |
| 017040 | hard_4c_late | bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
confidence = medium
```

Candidate:

> In L1 grid/datacenter capex names, transformer and cable demand can support Stage2A when backlog, export, CAPA slot, or ASP evidence exists. But small-cap grid beta and event premium require a stricter bridge gate: no backlog/CAPA/ASP/FCF bridge, no Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C02_POWER_GRID_DATACENTER_CAPEX
confidence = medium
```

Candidate C02 rule:

```text
C02_grid_capex_bridge_required =
  grid_or_datacenter_power_demand
  AND (backlog_conversion OR export_order_bridge OR capa_slot_lock OR asp_bridge OR margin_bridge OR fcf_conversion)

if late_switchgear_or_grid_event_premium and bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 80 and drawdown_after_peak < -40:
    add C02_peak_proximity_4B_audit = true

if MFE_90D < 10 and MAE_90D < -30:
    classify_as C02_event_premium_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 130.8 | -26.34 | 130.8 | -27.56 | 1 | useful but event-premium bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 130.8 | -26.34 | 130.8 | -27.56 | 1 | over-credits grid small-cap beta |
| P1 sector_specific_candidate_profile | L1 | 2 promoted + 1 guard | 194.07 | -13.84 | 194.07 | -13.84 | 0 | better after backlog/CAPA bridge gate |
| P2 canonical_archetype_candidate_profile | C02 | 2 promoted + 1 guard | 194.07 | -13.84 | 194.07 | -13.84 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C02 guard | 2 promoted + 1 guard | 194.07 | -13.84 | 194.07 | -13.84 | 0 | adds event-premium false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 033100 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 006340 | Stage2A aligned but high-MAE; 4B audit late | current_profile_4B_too_late |
| 017040 | Stage2 false positive if event premium not gated | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | mixed C02 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 24 -> local projected 27 -> projected 30; reaches minimum stability threshold |

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
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C02_grid_capex_bridge_required|C02_peak_proximity_4B_audit|C02_event_premium_false_positive_guardrail
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
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
- Uses C02 Priority 0 coverage gap.
- Avoids static C02 top-covered symbols and local loop 81 C02 symbols.
- Rejects 001440 and 000500 due to 2024 corporate-action candidates.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_grid_capex_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"017040 shows switchgear/grid event premium can fail without backlog/CAPA/ASP bridge while 033100/006340 work only as Stage2A with 4B audit","blocks 017040 false positive while preserving 033100/006340 Stage2A","JERYONG_033100_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_EXPORT|DAEWONCABLE_006340_2024_04_05_STAGE2A_GRID_CABLE_SMALLCAP_BETA|KWANGMYUNG_017040_2024_05_07_STAGE2_FALSE_POSITIVE_SWITCHGEAR_EVENT_PREMIUM",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C02_peak_proximity_4B_audit,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"033100/006340 extreme MFE grid capex reratings still needed 4B audit after valuation extension","adds 4B audit after large C02 MFE without converting price-only peaks into Green","JERYONG_033100_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_EXPORT|DAEWONCABLE_006340_2024_04_05_STAGE2A_GRID_CABLE_SMALLCAP_BETA",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C02_event_premium_false_positive_guardrail,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"017040 had low MFE and high MAE after switchgear event premium","requires backlog/CAPA/ASP/FCF bridge before Stage2/Yellow promotion","KWANGMYUNG_017040_2024_05_07_STAGE2_FALSE_POSITIVE_SWITCHGEAR_EVENT_PREMIUM",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C02_JERYONG_033100_2024_03_06_TRANSFORMER_DATACENTER_EXPORT_RERATING","symbol":"033100","company_name":"제룡전기","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_EXPORT_BACKLOG_CAPA_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"JERYONG_033100_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_EXPORT","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"transformer/datacenter/export power-equipment route captured extreme MFE, but later peak-to-drawdown requires C02 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C02 symbol versus top-covered C02 list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C02_DAEWONCABLE_006340_2024_04_05_GRID_CABLE_SMALLCAP_BETA_4B","symbol":"006340","company_name":"대원전선","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_CABLE_SMALLCAP_ORDER_BETA_4B_HIGH_MAE","case_type":"high_mfe_high_mae_success","positive_or_counterexample":"positive","best_trigger":"DAEWONCABLE_006340_2024_04_05_STAGE2A_GRID_CABLE_SMALLCAP_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"grid cable/small-cap beta produced extreme MFE, but same-day MAE and later drawdown require order/CAPA bridge before Yellow/Green","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C02 symbol; clean 2024 corporate-action window"}
{"row_type":"case","case_id":"C02_KWANGMYUNG_017040_2024_05_07_SWITCHGEAR_EVENT_PREMIUM_FALSE_POSITIVE","symbol":"017040","company_name":"광명전기","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_GRID_EVENT_PREMIUM_BACKLOG_BRIDGE_ABSENT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"KWANGMYUNG_017040_2024_05_07_STAGE2_FALSE_POSITIVE_SWITCHGEAR_EVENT_PREMIUM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late switchgear/grid event premium had only 4% MFE before -50%+ MAE because backlog/CAPA/ASP bridge was absent","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C02 symbol; counterexample for theme/event premium without conversion bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"JERYONG_033100_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_EXPORT","case_id":"C02_JERYONG_033100_2024_03_06_TRANSFORMER_DATACENTER_EXPORT_RERATING","symbol":"033100","company_name":"제룡전기","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_EXPORT_BACKLOG_CAPA_4B_WATCH","sector":"industrials / grid / datacenter power capex","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":30700.0,"evidence_available_at_that_date":"source_proxy_only: transformer/export backlog route, datacenter power-equipment bottleneck, relative strength, and CAPA-slot narrative visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["transformer_export_route","datacenter_power_capex_route","backlog_visibility_route","relative_strength"],"stage3_evidence_fields":["capa_slot_bridge_partial","asp_margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv","profile_path":"atlas/symbol_profiles/033/033100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":84.04,"MFE_90D_pct":228.01,"MFE_180D_pct":228.01,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.07,"MAE_90D_pct":-11.07,"MAE_180D_pct":-11.07,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":100700.0,"drawdown_after_peak_pct":-63.7,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"excellent_stage2a_but_extreme_peak_requires_C02_4B_audit","four_b_evidence_type":["valuation_rerating","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_033100_2024_03_06_30700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DAEWONCABLE_006340_2024_04_05_STAGE2A_GRID_CABLE_SMALLCAP_BETA","case_id":"C02_DAEWONCABLE_006340_2024_04_05_GRID_CABLE_SMALLCAP_BETA_4B","symbol":"006340","company_name":"대원전선","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_CABLE_SMALLCAP_ORDER_BETA_4B_HIGH_MAE","sector":"industrials / grid / datacenter power capex","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-05","entry_date":"2024-04-05","entry_price":2095.0,"evidence_available_at_that_date":"source_proxy_only: cable/grid small-cap beta, power-grid capex sympathy, and relative strength visible; backlog/CAPA conversion not fully verified","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["grid_cable_route","smallcap_power_capex_beta","relative_strength"],"stage3_evidence_fields":["order_bridge_partial","capa_lock_pending","margin_bridge_pending"],"stage4b_evidence_fields":["price_extension","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":160.14,"MFE_90D_pct":160.14,"MFE_180D_pct":160.14,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-16.61,"MAE_90D_pct":-16.61,"MAE_180D_pct":-16.61,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":5450.0,"drawdown_after_peak_pct":-51.56,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_grid_cable_beta_worked_but_requires_4B_audit_and_bridge_check","four_b_evidence_type":["price_extension","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_high_mae_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_006340_2024_04_05_2095","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KWANGMYUNG_017040_2024_05_07_STAGE2_FALSE_POSITIVE_SWITCHGEAR_EVENT_PREMIUM","case_id":"C02_KWANGMYUNG_017040_2024_05_07_SWITCHGEAR_EVENT_PREMIUM_FALSE_POSITIVE","symbol":"017040","company_name":"광명전기","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_GRID_EVENT_PREMIUM_BACKLOG_BRIDGE_ABSENT","sector":"industrials / grid / datacenter power capex","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-05-07","entry_date":"2024-05-07","entry_price":3185.0,"evidence_available_at_that_date":"source_proxy_only: switchgear/grid event premium and late small-cap relative strength visible, but backlog, CAPA, ASP and FCF bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["switchgear_event_premium","late_relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","price_only_peak","backlog_bridge_absent"],"stage4c_evidence_fields":["capa_lock_absent","asp_bridge_absent","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv","profile_path":"atlas/symbol_profiles/017/017040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.24,"MFE_90D_pct":4.24,"MFE_180D_pct":4.24,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-30.93,"MAE_90D_pct":-51.33,"MAE_180D_pct":-55.01,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-08","peak_price":3320.0,"drawdown_after_peak_pct":-56.84,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_switchgear_event_premium_not_stage3_without_backlog_capa_bridge","four_b_evidence_type":["price_only","event_premium"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_017040_2024_05_07_3185","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_JERYONG_033100_2024_03_06_TRANSFORMER_DATACENTER_EXPORT_RERATING","trigger_id":"JERYONG_033100_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_EXPORT","symbol":"033100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable with mandatory C02 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Extreme transformer/datacenter rerating worked, but Green should wait for CAPA/ASP/FCF bridge and peak-proximity audit.","MFE_90D_pct":228.01,"MAE_90D_pct":-11.07,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_DAEWONCABLE_006340_2024_04_05_GRID_CABLE_SMALLCAP_BETA_4B","trigger_id":"DAEWONCABLE_006340_2024_04_05_STAGE2A_GRID_CABLE_SMALLCAP_BETA","symbol":"006340","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-watch / 4B audit, not Yellow","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Small-cap cable beta can work violently, but high MAE means order/CAPA proof must gate Stage3.","MFE_90D_pct":160.14,"MAE_90D_pct":-16.61,"score_return_alignment_label":"positive_but_high_mae_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_KWANGMYUNG_017040_2024_05_07_SWITCHGEAR_EVENT_PREMIUM_FALSE_POSITIVE","trigger_id":"KWANGMYUNG_017040_2024_05_07_STAGE2_FALSE_POSITIVE_SWITCHGEAR_EVENT_PREMIUM","symbol":"017040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":7,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Late switchgear event premium without backlog/CAPA/ASP bridge produced low MFE and high MAE.","MFE_90D_pct":4.24,"MAE_90D_pct":-51.33,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R1
completed_loop = 90
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C11_BATTERY_ORDERBOOK_RERATING, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

If this loop is accepted together with local loop 81, C02 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C02 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/033/033100.json
  - atlas/symbol_profiles/006/006340.json
  - atlas/symbol_profiles/017/017040.json
- Rejected due to corporate-action candidates:
  - atlas/symbol_profiles/001/001440.json
  - atlas/symbol_profiles/000/000500.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
