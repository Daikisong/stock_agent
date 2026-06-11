# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_81_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round: R1
selected_loop: 81
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: GRID_CABLE_DATACENTER_CAPEX_BACKLOG_CAPA_4B_WATCH
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

This loop adds 3 independent cases, 2 C02 grid/datacenter-capex success paths, and 1 late-beta counterexample for R1/L1/C02.

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

C02 is the power-grid / data-center electricity bottleneck route. The central bridge is not “the stock moved with grid theme,” but:

```text
grid/datacenter capex -> backlog/CAPA slot -> ASP or margin bridge -> EPS/FCF conversion
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C02 current rows | 24 |
| C02 current symbols | 13 |
| C02 good/bad Stage2 | 8 / 3 |
| C02 4B/4C | 3 / 1 |
| C02 URL pending/proxy | 21 / 18 |
| top covered symbols | 199820, 103590, 267260, 298040, 010120, 237750 |

Selected symbols avoid the C02 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 006260 | LS | new C02 symbol versus top-covered C02 list |
| 017510 | 세명전기 | new C02 symbol versus top-covered C02 list |
| 189860 | 서전기전 | new C02 symbol versus top-covered C02 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 006260 / 2024-03-14 | true | true | clean_180D_window | true |
| 017510 / 2024-04-05 | true | true | clean_180D_window | true |
| 189860 / 2024-07-09 | true | true | clean_180D_window | true |

Corporate-action notes:

- LS has corporate-action candidates only in 1996 and 1999; selected 2024 window is clean.
- 세명전기 has corporate-action candidates only before 2000; selected 2024 window is clean.
- 서전기전 has a corporate-action candidate in 2018 only; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GRID_CABLE_DATACENTER_CAPEX_BACKLOG_CAPA_4B_WATCH | C02 | cable/grid route connected to datacenter capex and power bottleneck |
| GRID_COMPONENT_SMALLCAP_ORDER_BETA_4B_WATCH | C02 | grid component beta can work but needs order/CAPA bridge before Yellow/Green |
| SWITCHGEAR_SMALLCAP_LATE_BETA_BACKLOG_BRIDGE_ABSENT | C02 | late switchgear beta without backlog/CAPA/ASP bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C02_LS_006260_2024_03_14_GRID_CABLE_DATACENTER_CAPEX_RERATING | 006260 | LS | 4B_overlay_success | positive | grid cable/datacenter capex route produced >90% MFE, then 4B drawdown |
| C02_SEMYUNG_017510_2024_04_05_GRID_COMPONENT_ORDER_BETA_4B | 017510 | 세명전기 | high_mfe_success | positive | small-cap grid component route produced >160% MFE but high MAE/drawdown |
| C02_SEOJUN_189860_2024_07_09_SWITCHGEAR_LATE_BETA_FALSE_POSITIVE | 189860 | 서전기전 | failed_rerating | counterexample | late switchgear beta lacked backlog/CAPA bridge and produced poor MFE/MAE |

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

Minimum conditions pass:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 006260 | source_proxy_only | grid cable / datacenter capex / backlog route; CAPA/ASP bridge partial | required before promotion |
| 017510 | source_proxy_only | grid component / transmission equipment route; order bridge partial | required before promotion |
| 189860 | source_proxy_only | late switchgear beta without backlog/CAPA/ASP bridge | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 006260 | atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv | atlas/symbol_profiles/006/006260.json |
| 017510 | atlas/ohlcv_tradable_by_symbol_year/017/017510/2024.csv | atlas/symbol_profiles/017/017510.json |
| 189860 | atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv | atlas/symbol_profiles/189/189860.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| LS_006260_2024_03_14_STAGE2A_GRID_CABLE_DATACENTER_CAPEX | Stage2-Actionable | 2024-03-14 | 2024-03-14 | 101300 | grid cable/datacenter capex route |
| SEMYUNG_017510_2024_04_05_STAGE2A_GRID_COMPONENT_ORDER_BETA | Stage2-Actionable | 2024-04-05 | 2024-04-05 | 3710 | small-cap grid component/order beta |
| SEOJUN_189860_2024_07_09_STAGE2_FALSE_POSITIVE_SWITCHGEAR_LATE_BETA | Stage2 | 2024-07-09 | 2024-07-09 | 7130 | late switchgear beta without backlog/CAPA bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 006260 | 2024-03-14 | 101300 | 34.85 | -1.38 | 92.30 | -1.38 | 92.30 | -7.90 | 2024-05-21 | 194800 | -52.10 |
| 017510 | 2024-04-05 | 3710 | 107.55 | -19.81 | 169.54 | -19.81 | 169.54 | -19.81 | 2024-07-10 | 10000 | -59.35 |
| 189860 | 2024-07-09 | 7130 | 15.99 | -32.33 | 15.99 | -43.83 | 15.99 | -43.83 | 2024-07-18 | 8270 | -51.57 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 006260 | Stage2A/Yellow possible; 4B after rerating | high MFE then >50% post-peak drawdown | current_profile_4B_too_late |
| 017510 | Stage2A possible; small-cap beta can overshoot | extreme MFE but high MAE and >59% drawdown | current_profile_4B_too_late |
| 189860 | Stage2 risk if late switchgear beta is over-credited | low MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C02 interpretation:

- Stage2A can work when grid/datacenter capex is tied to backlog, cable/equipment demand, or capacity slot lock.
- Yellow/Green require backlog conversion, CAPA visibility, ASP/margin bridge, and FCF.
- Late small-cap grid/switchgear beta without bridge should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 006260 | 1.00 | 1.00 | valuation / positioning | good 4B audit after grid cable rerating |
| 017510 | 1.00 | 1.00 | price extension / positioning | extreme MFE requires 4B audit before Yellow/Green |
| 189860 | 1.00 | 1.00 | price-only late beta | late beta was not Stage3 and not full positive C02 |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 006260 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 017510 | thesis_break_watch_only | not hard 4C, but small-cap 4B cap needed |
| 189860 | hard_4c_late | missing backlog/CAPA/ASP bridge should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
confidence = low_to_medium
```

Candidate:

> In L1 grid/datacenter capex names, Stage2A can be supported by grid cable, transformer, switchgear, or data-center power demand evidence. However, Stage3-Yellow/Green should require backlog conversion, CAPA slot lock, ASP/margin bridge, or FCF conversion. Late small-cap grid beta without that bridge should be capped at Stage1/Stage2-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C02_POWER_GRID_DATACENTER_CAPEX
confidence = low_to_medium
```

Candidate C02 rule:

```text
C02_grid_capex_bridge_required =
  grid_or_datacenter_power_demand
  AND (backlog_conversion OR capa_slot_lock OR asp_bridge OR margin_bridge OR fcf_conversion)

if late_switchgear_or_grid_beta and bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 80 and drawdown_after_peak < -40:
    add C02_peak_proximity_4B_audit = true

if MFE_90D < 20 and MAE_90D < -30:
    classify_as C02_late_beta_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 92.61 | -21.67 | 92.61 | -23.85 | 1 | useful but C02 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 92.61 | -21.67 | 92.61 | -23.85 | 1 | over-credits late grid beta |
| P1 sector_specific_candidate_profile | L1 | 2 promoted + 1 guard | 130.92 | -10.59 | 130.92 | -13.86 | 0 | better after backlog/CAPA bridge gate |
| P2 canonical_archetype_candidate_profile | C02 | 2 promoted + 1 guard | 130.92 | -10.59 | 130.92 | -13.86 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C02 guard | 2 promoted + 1 guard | 130.92 | -10.59 | 130.92 | -13.86 | 0 | adds late-beta false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 006260 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 017510 | Stage2A aligned but high-MAE; 4B audit late | current_profile_4B_too_late |
| 189860 | Stage2 false positive if bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | mixed C02 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | 24 -> projected 27 rows; still need 3 to reach 30 |

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
new_axis_proposed: C02_grid_capex_bridge_required|C02_peak_proximity_4B_audit|C02_late_beta_false_positive_guardrail
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
- Uses three symbols not in the C02 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_grid_capex_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"189860 shows late switchgear/grid beta can fail without backlog/CAPA/ASP bridge","blocks 189860 false positive while preserving 006260/017510 Stage2A","LS_006260_2024_03_14_STAGE2A_GRID_CABLE_DATACENTER_CAPEX|SEMYUNG_017510_2024_04_05_STAGE2A_GRID_COMPONENT_ORDER_BETA|SEOJUN_189860_2024_07_09_STAGE2_FALSE_POSITIVE_SWITCHGEAR_LATE_BETA",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C02_peak_proximity_4B_audit,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"006260/017510 high-MFE grid capex reratings still needed 4B audit after valuation extension","adds 4B audit after large C02 MFE without converting price-only peaks into full 4B","LS_006260_2024_03_14_STAGE2A_GRID_CABLE_DATACENTER_CAPEX|SEMYUNG_017510_2024_04_05_STAGE2A_GRID_COMPONENT_ORDER_BETA",2,2,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C02_late_beta_false_positive_guardrail,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"189860 had low MFE and high MAE after late switchgear beta","requires backlog/CAPA/ASP bridge before Stage2/Yellow promotion","SEOJUN_189860_2024_07_09_STAGE2_FALSE_POSITIVE_SWITCHGEAR_LATE_BETA",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C02_LS_006260_2024_03_14_GRID_CABLE_DATACENTER_CAPEX_RERATING","symbol":"006260","company_name":"LS","round":"R1","loop":"81","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_CABLE_DATACENTER_CAPEX_BACKLOG_CAPA_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"LS_006260_2024_03_14_STAGE2A_GRID_CABLE_DATACENTER_CAPEX","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"grid/cable/datacenter capex route captured >90% MFE, but later peak-to-drawdown requires 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C02 symbol versus top-covered C02 list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C02_SEMYUNG_017510_2024_04_05_GRID_COMPONENT_ORDER_BETA_4B","symbol":"017510","company_name":"세명전기","round":"R1","loop":"81","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_COMPONENT_SMALLCAP_ORDER_BETA_4B_WATCH","case_type":"high_mfe_success","positive_or_counterexample":"positive","best_trigger":"SEMYUNG_017510_2024_04_05_STAGE2A_GRID_COMPONENT_ORDER_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"grid component beta produced >160% MFE, but high same-day MAE and later drawdown demand stronger order/CAPA bridge","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C02 symbol; useful high-MFE/4B timing case"}
{"row_type":"case","case_id":"C02_SEOJUN_189860_2024_07_09_SWITCHGEAR_LATE_BETA_FALSE_POSITIVE","symbol":"189860","company_name":"서전기전","round":"R1","loop":"81","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_SMALLCAP_LATE_BETA_BACKLOG_BRIDGE_ABSENT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"SEOJUN_189860_2024_07_09_STAGE2_FALSE_POSITIVE_SWITCHGEAR_LATE_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late switchgear/grid beta gave only mid-teens MFE before -40%+ MAE because backlog/CAPA/ASP bridge was absent","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C02 symbol; counterexample for late small-cap grid beta without backlog/CAPA lock"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"LS_006260_2024_03_14_STAGE2A_GRID_CABLE_DATACENTER_CAPEX","case_id":"C02_LS_006260_2024_03_14_GRID_CABLE_DATACENTER_CAPEX_RERATING","symbol":"006260","company_name":"LS","round":"R1","loop":"81","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_CABLE_DATACENTER_CAPEX_BACKLOG_CAPA_4B_WATCH","sector":"industrials / grid / datacenter power capex","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":101300.0,"evidence_available_at_that_date":"source_proxy_only: grid cable / data-center power capex / power equipment backlog route visible; confirmed CAPA/ASP/FCF bridge partial; URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["grid_cable_route","datacenter_power_capex_route","backlog_visibility_route","relative_strength"],"stage3_evidence_fields":["capa_lock_partial","asp_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","profile_path":"atlas/symbol_profiles/006/006260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.85,"MFE_90D_pct":92.3,"MFE_180D_pct":92.3,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-1.38,"MAE_90D_pct":-1.38,"MAE_180D_pct":-7.9,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":194800.0,"drawdown_after_peak_pct":-52.1,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_grid_cable_datacenter_capex_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_006260_2024_03_14_101300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SEMYUNG_017510_2024_04_05_STAGE2A_GRID_COMPONENT_ORDER_BETA","case_id":"C02_SEMYUNG_017510_2024_04_05_GRID_COMPONENT_ORDER_BETA_4B","symbol":"017510","company_name":"세명전기","round":"R1","loop":"81","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_COMPONENT_SMALLCAP_ORDER_BETA_4B_WATCH","sector":"industrials / grid / datacenter power capex","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-05","entry_date":"2024-04-05","entry_price":3710.0,"evidence_available_at_that_date":"source_proxy_only: grid component / transmission equipment small-cap beta and power capex theme visible; backlog/CAPA bridge not yet fully verified","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["grid_component_route","transmission_equipment_beta","relative_strength"],"stage3_evidence_fields":["order_bridge_partial","capa_lock_pending","margin_bridge_pending"],"stage4b_evidence_fields":["price_extension","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017510/2024.csv","profile_path":"atlas/symbol_profiles/017/017510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":107.55,"MFE_90D_pct":169.54,"MFE_180D_pct":169.54,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-19.81,"MAE_90D_pct":-19.81,"MAE_180D_pct":-19.81,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-10","peak_price":10000.0,"drawdown_after_peak_pct":-59.35,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"extreme_smallcap_grid_beta_requires_peak_proximity_4B_audit","four_b_evidence_type":["price_extension","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_high_mae_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_017510_2024_04_05_3710","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SEOJUN_189860_2024_07_09_STAGE2_FALSE_POSITIVE_SWITCHGEAR_LATE_BETA","case_id":"C02_SEOJUN_189860_2024_07_09_SWITCHGEAR_LATE_BETA_FALSE_POSITIVE","symbol":"189860","company_name":"서전기전","round":"R1","loop":"81","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_SMALLCAP_LATE_BETA_BACKLOG_BRIDGE_ABSENT","sector":"industrials / grid / datacenter power capex","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-07-09","entry_date":"2024-07-09","entry_price":7130.0,"evidence_available_at_that_date":"source_proxy_only: switchgear/grid late beta and power capex sympathy visible, but backlog/CAPA lock/ASP bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["switchgear_theme_beta","late_relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_late_peak","backlog_bridge_absent"],"stage4c_evidence_fields":["capa_lock_absent","asp_bridge_absent","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv","profile_path":"atlas/symbol_profiles/189/189860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.99,"MFE_90D_pct":15.99,"MFE_180D_pct":15.99,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-32.33,"MAE_90D_pct":-43.83,"MAE_180D_pct":-43.83,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":8270.0,"drawdown_after_peak_pct":-51.57,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_smallcap_switchgear_beta_not_stage3_without_backlog_capa_bridge","four_b_evidence_type":["price_only","late_beta"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_189860_2024_07_09_7130","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_LS_006260_2024_03_14_GRID_CABLE_DATACENTER_CAPEX_RERATING","trigger_id":"LS_006260_2024_03_14_STAGE2A_GRID_CABLE_DATACENTER_CAPEX","symbol":"006260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with mandatory C02 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Grid cable/data-center capex route worked, but valuation extension after >90% MFE requires 4B audit unless CAPA/ASP/FCF bridge is verified.","MFE_90D_pct":92.3,"MAE_90D_pct":-1.38,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_SEMYUNG_017510_2024_04_05_GRID_COMPONENT_ORDER_BETA_4B","trigger_id":"SEMYUNG_017510_2024_04_05_STAGE2A_GRID_COMPONENT_ORDER_BETA","symbol":"017510","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":10,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-watch / 4B audit, not Yellow","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Small-cap grid component beta can produce huge MFE, but high same-day MAE and drawdown require order/CAPA bridge before Yellow/Green.","MFE_90D_pct":169.54,"MAE_90D_pct":-19.81,"score_return_alignment_label":"positive_but_high_mae_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_SEOJUN_189860_2024_07_09_SWITCHGEAR_LATE_BETA_FALSE_POSITIVE","trigger_id":"SEOJUN_189860_2024_07_09_STAGE2_FALSE_POSITIVE_SWITCHGEAR_LATE_BETA","symbol":"189860","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":7,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Late switchgear small-cap beta without backlog/CAPA/ASP bridge had poor MFE/MAE alignment and should not receive C02 Stage2 credit.","MFE_90D_pct":15.99,"MAE_90D_pct":-43.83,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"81","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 81
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

If this loop is accepted, C02 moves from 24 to a projected 27 rows. It remains below 30-row minimum stability, so a later run can still add 3 more C02 rows, but the next run should re-read the latest No-Repeat Index before selecting another C02 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/017/017510/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/006/006260.json
  - atlas/symbol_profiles/017/017510.json
  - atlas/symbol_profiles/189/189860.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
