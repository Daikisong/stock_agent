# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_137_L1_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round: R1
selected_loop: 137
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_DATACENTER_CAPEX_BACKLOG_ASP_MARGIN_RERATING_4B_WATCH
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

This is the corrected valid run after a duplicate C23 loop136 materialization path was discarded. C23 reached the 30-row stability threshold at loop136, so this run moves to the next thin Priority 0 archetype: C02.

This loop adds 4 new independent C02 rows and moves C02 from static 24 rows to projected 28 rows. It still needs 2 rows to reach the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C02:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R1 -> L1_INFRA_DEFENSE_GRID
C02 -> C02_POWER_GRID_DATACENTER_CAPEX
```

C02 is the power-grid / datacenter CAPEX archetype. Backlog is the spine, ASP and margin are the muscle, and FCF is the pulse. A pure price sprint without those body parts is only 4B heat, not Green evidence.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C02 static rows | 24 |
| C02 need to 30 | 6 |
| C02 need to 50 | 26 |
| C02 investigation point | 전력기기/데이터센터 CAPEX, backlog, CAPA lock, ASP |
| local previous C02 rows in this session | 0 |
| this loop projected rows | 28 |

Selected C02 symbols:

| symbol | company | status |
|---|---|---|
| 267260 | HD현대일렉트릭 | new local C02 direct transformer/datacenter positive |
| 298040 | 효성중공업 | new local C02 clean direct grid-backlog positive |
| 010120 | LS ELECTRIC | new local C02 extreme 4B timing row |
| 000500 | 가온전선 | new local C02 wire/cable price-blowoff counterexample |

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
| 267260 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 298040 / 2024-03-06 | true | true | clean_180D_window | true, weight 1.00 |
| 010120 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 000500 / 2024-03-06 | true | true | main_4B_window_clean_but_late_2024_corporate_action_candidate | true, weight 0.75 |

Corporate-action notes:

- HD현대일렉트릭 has old corporate-action candidates before the selected 2024 window.
- 효성중공업 has zero corporate-action candidates.
- LS ELECTRIC has old corporate-action candidates before the selected 2024 window.
- 가온전선 has a late-2024 corporate-action/share-count drift watch, so it is retained as reduced-weight guardrail evidence.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| TRANSFORMER_DATACENTER_CAPEX_BACKLOG_ASP_MARGIN_RERATING_4B_WATCH | C02 | direct transformer/datacenter backlog can support Stage2A, but Green needs margin/revision/FCF conversion |
| POWER_EQUIPMENT_US_GRID_BACKLOG_MARGIN_RERATING_4B_WATCH | C02 | US grid equipment backlog can work, but still needs 4B peak audit |
| DATACENTER_GRID_CAPEX_RELATIVE_STRENGTH_EXTREME_4B_WITH_DELAYED_AUDIT | C02 | extreme relative strength is tradable but price-only blowoff blocks Green |
| WIRE_CABLE_CAPEX_BETA_PRICE_BLOWOFF_WITHOUT_DIRECT_BACKLOG_MARGIN_BRIDGE | C02 | wire/cable theme beta needs direct backlog/ASP/margin bridge before Yellow/Green |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C02_HDHE_267260_2024_03_06_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_RERATING_4B | 267260 | HD현대일렉트릭 | 4B_overlay_success | positive | 204.04% 180D MFE with limited entry MAE |
| C02_HYOSUNGHEAVY_298040_2024_03_06_POWER_EQUIPMENT_US_GRID_BACKLOG_RERATING_4B | 298040 | 효성중공업 | 4B_overlay_success | positive | 123.28% 180D MFE with clean profile |
| C02_LSELECTRIC_010120_2024_03_06_DATACENTER_GRID_CAPEX_EXTREME_4B_BLOWOFF | 010120 | LS ELECTRIC | extreme_4B_overlay_success | positive_boundary | 208.47% MFE but later -48.28% post-peak drawdown |
| C02_GAONCABLE_000500_2024_03_06_WIRE_CABLE_CAPEX_BETA_BLOWOFF_COUNTEREXAMPLE | 000500 | 가온전선 | price_blowoff_counterexample | counterexample | huge price MFE but bridge absent and -61.61% post-peak drawdown |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| positive_boundary_case_count | 1 |
| counterexample_count | 1 |
| 4B_case_count | 4 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 3 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 267260 | source_proxy_only | transformer backlog / datacenter CAPEX / export ASP-margin route | required before promotion |
| 298040 | source_proxy_only | US grid backlog / power-equipment margin route | required before promotion |
| 010120 | source_proxy_only | datacenter/smart-grid CAPEX and relative strength, but extreme 4B audit needed | required before promotion |
| 000500 | source_proxy_only | wire/cable CAPEX beta but direct backlog/ASP/margin bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 267260 | atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv | atlas/symbol_profiles/267/267260.json |
| 298040 | atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv | atlas/symbol_profiles/298/298040.json |
| 010120 | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json |
| 000500 | atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv | atlas/symbol_profiles/000/000500.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HDHE_267260_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_CAPEX_BACKLOG | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 136000 | transformer/datacenter backlog CAPEX route |
| HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_US_GRID_BACKLOG_CAPEX | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 232000 | US grid / power-equipment backlog CAPEX |
| LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_DATACENTER_CAPEX_4B | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 79100 | datacenter grid CAPEX extreme 4B |
| GAONCABLE_000500_2024_03_06_STAGE2_FALSE_POSITIVE_WIRE_CABLE_CAPEX_BETA | Stage2 | 2024-03-06 | 2024-03-06 | 27150 | wire/cable CAPEX beta without direct bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 267260 | 2024-03-06 | 136000 | 95.22 | -7.65 | 166.91 | -7.65 | 204.04 | -7.65 | 2024-11-12 | 413500 | -19.23 |
| 298040 | 2024-03-06 | 232000 | 53.88 | -4.53 | 102.16 | -4.53 | 123.28 | -4.53 | 2024-11-12 | 518000 | -25.87 |
| 010120 | 2024-03-06 | 79100 | 103.67 | -3.41 | 208.47 | -3.41 | 208.47 | -3.41 | 2024-05-29 | 244000 | -48.28 |
| 000500 | 2024-03-06 | 27150 | 77.35 | -4.42 | 174.40 | -4.42 | 174.40 | -4.42 | 2024-05-13 | 74500 | -61.61 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 267260 | Stage2A/Yellow-risk if CAPEX backlog is over-credited | huge MFE, but Green needs conversion evidence | current_profile_4B_too_late |
| 298040 | Stage2A direct grid backlog | huge MFE and clean row; 4B peak audit still needed | current_profile_4B_too_late |
| 010120 | Stage2A but extreme relative-strength blowoff | huge MFE then deep post-peak drawdown | current_profile_4B_too_late_after_extreme_price_blowoff |
| 000500 | Stage2 theme beta risk | price-only blowoff without direct bridge | current_profile_false_positive_if_wire_beta_promoted_to_Green |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C02 interpretation:

- Stage2A works when backlog, CAPA lock, datacenter/grid CAPEX, ASP/margin and revision routes are visible.
- Yellow/Green require non-price backlog-to-margin conversion and FCF evidence.
- Extreme price-only relative strength and wire/cable theme beta must remain 4B or Stage2-watch unless direct backlog/margin bridge is visible.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 267260 | 0.33 | 1.00 | transformer backlog / CAPEX rerating | full-window C02 4B audit required |
| 298040 | 0.45 | 1.00 | power-equipment backlog rerating | full-window C02 4B audit required |
| 010120 | 0.32 | 1.00 | extreme relative-strength blowoff | delayed 4B/4C peak audit required |
| 000500 | 0.36 | 1.00 | wire/cable price blowoff | price-only Green block |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 267260 | thesis_break_watch_only | not hard 4C, but price peak cannot be Green without conversion |
| 298040 | thesis_break_watch_only | clean Stage2A, but Green needs realized bridge |
| 010120 | delayed_4c_watch_after_peak | extreme price rally needs delayed audit |
| 000500 | price_only_green_block | theme beta blocks Yellow/Green without direct backlog/ASP/margin bridge |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L1_INFRA_DEFENSE_GRID
confidence = medium
```

Candidate:

> In L1 grid/infrastructure names, power-grid/datacenter CAPEX should promote Stage2A only when backlog, CAPA lock, ASP/margin bridge, revision or FCF conversion is visible. Wire/cable theme beta or price-only relative strength should stay as 4B/watch and should not become Yellow/Green without direct backlog/margin proof.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C02_POWER_GRID_DATACENTER_CAPEX
confidence = medium
```

Candidate C02 rule:

```text
C02_grid_capex_backlog_margin_bridge_required =
  power_grid_or_datacenter_capex_route
  AND (backlog_visibility OR CAPA_lock OR ASP_bridge OR margin_bridge OR confirmed_revision OR fcf_conversion)

if direct_power_equipment and backlog_margin_bridge_visible:
    allow_stage2_actionable = true
    require_4B_peak_audit_if_MFE_90D > 80

if wire_cable_theme_beta and direct_backlog_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if price_only_relative_strength and MFE_90D > 100:
    add C02_price_blowoff_4B_audit = true

if late_share_count_or_corporate_action_drift:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / blowoff | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 4 | 162.98 | -5.0 | 177.55 | -5.0 | 1 | strong C02 but Green bridge too loose |
| P0b calibrated rollback | rollback | 4 | 162.98 | -5.0 | 177.55 | -5.0 | 1 | over-credits price-only grid beta |
| P1 sector_specific_candidate_profile | L1 | 3 Stage2A + 1 guard | 159.18 | -5.2 | 178.6 | -5.2 | 0 | better with backlog/margin bridge |
| P2 canonical_archetype_candidate_profile | C02 | 3 Stage2A + 1 guard | 159.18 | -5.2 | 178.6 | -5.2 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C02 guard | 3 Stage2A + 1 guard | 159.18 | -5.2 | 178.6 | -5.2 | 0 | adds wire/cable blowoff guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 267260 | Stage2A aligned; 4B peak audit needed | current_profile_4B_too_late |
| 298040 | Stage2A aligned; 4B audit needed | current_profile_4B_too_late |
| 010120 | Stage2A aligned but extreme price-only blowoff needs delayed audit | current_profile_4B_too_late_after_extreme_price_blowoff |
| 000500 | Stage2 theme beta should not become Yellow/Green without bridge | current_profile_false_positive_if_wire_beta_promoted_to_Green |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | positive boundary | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | mixed C02 fine ids | 2 | 1 | 1 | 4 | 1 | 4 | 0 | 4 | 4 | 4 | true | true | static 24 -> projected 28; still need 2 to reach 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive_if_price_blowoff_promoted_to_Green
new_axis_proposed: C02_grid_capex_backlog_margin_bridge_required|C02_price_blowoff_4B_audit|C02_wire_cable_theme_beta_green_block|late_share_count_or_corporate_action_weight_reduction
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
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
- Uses C02 Priority 0 coverage gap.
- Uses new local C02 symbols.
- Keeps 000500 with reduced independent weight because late-2024 corporate-action/share-count drift is visible.
- Treats 000500 as price-blowoff counterexample, not Green promotion.
- Discards the accidental duplicate C23 loop136 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated C23 loop136 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_grid_capex_backlog_margin_bridge_required,canonical_archetype_specific,L1_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"267260/298040/010120 show direct C02 routes can work when backlog/CAPEX/margin path is visible while 000500 needs a bridge guard","preserves direct Stage2A rows and blocks wire/cable beta from Green","HDHE_267260_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_CAPEX_BACKLOG|HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_US_GRID_BACKLOG_CAPEX|LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_DATACENTER_CAPEX_4B|GAONCABLE_000500_2024_03_06_STAGE2_FALSE_POSITIVE_WIRE_CABLE_CAPEX_BETA",4,4,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C02_price_blowoff_4B_audit,canonical_archetype_specific,L1_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"010120/000500 had extreme MFE followed by large post-peak drawdown, so price-only C02 blowoffs need audit","prevents price-only peaks from becoming Green without backlog/margin/FCF confirmation","LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_DATACENTER_CAPEX_4B|GAONCABLE_000500_2024_03_06_STAGE2_FALSE_POSITIVE_WIRE_CABLE_CAPEX_BETA",2,2,1,medium,canonical_shadow_only,"4B overlay/risk calibration"
shadow_weight,C02_wire_cable_theme_beta_green_block,canonical_archetype_specific,L1_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"000500 shows wire/cable CAPEX beta can price-rerate without direct backlog, ASP/margin and FCF bridge","caps wire/cable theme beta at Stage1/Stage2-watch unless direct bridge exists","GAONCABLE_000500_2024_03_06_STAGE2_FALSE_POSITIVE_WIRE_CABLE_CAPEX_BETA",1,1,1,medium,canonical_shadow_only,"counterexample guardrail"
shadow_weight,late_share_count_or_corporate_action_weight_reduction,archetype_specific_quality_flag,L1_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"000500 has late-2024 corporate-action/share-count drift after the main 4B window","keeps row usable but lowers independent evidence weight","GAONCABLE_000500_2024_03_06_STAGE2_FALSE_POSITIVE_WIRE_CABLE_CAPEX_BETA",1,1,1,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C02_HDHE_267260_2024_03_06_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_RERATING_4B","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_CAPEX_BACKLOG_ASP_MARGIN_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HDHE_267260_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_CAPEX_BACKLOG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; selected forward window is clean","independent_evidence_weight":0.95,"score_price_alignment":"transformer/datacenter grid CAPEX and backlog rerating captured very large MFE with limited entry MAE, but full-window peak watch still requires C02 4B audit before Green promotion","current_profile_verdict":"current_profile_4B_too_late_if_CAPEX_backlog_overpromoted_to_Green","price_source":"Songdaiki/stock-web","notes":"new local C02 symbol; transformer/datacenter CAPEX anchor positive"}
{"row_type":"case","case_id":"C02_HYOSUNGHEAVY_298040_2024_03_06_POWER_EQUIPMENT_US_GRID_BACKLOG_RERATING_4B","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_EQUIPMENT_US_GRID_BACKLOG_MARGIN_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_US_GRID_BACKLOG_CAPEX","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"power-equipment/grid backlog route captured over 100% MFE and low entry MAE, validating Stage2A but not price-only Green","current_profile_verdict":"current_profile_4B_too_late_if_grid_backlog_rerating_not_peak_audited","price_source":"Songdaiki/stock-web","notes":"clean profile with zero corporate-action candidates; C02 direct positive"}
{"row_type":"case","case_id":"C02_LSELECTRIC_010120_2024_03_06_DATACENTER_GRID_CAPEX_EXTREME_4B_BLOWOFF","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DATACENTER_GRID_CAPEX_RELATIVE_STRENGTH_EXTREME_4B_WITH_DELAYED_AUDIT","case_type":"extreme_4B_overlay_success","positive_or_counterexample":"positive_boundary","best_trigger":"LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_DATACENTER_CAPEX_4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window; selected window is clean","independent_evidence_weight":0.95,"score_price_alignment":"datacenter/grid CAPEX rerating produced extreme MFE, but peak-to-drawdown shows price-only 4B cannot become Green without backlog/margin/revision proof","current_profile_verdict":"current_profile_4B_too_late_after_extreme_price_blowoff","price_source":"Songdaiki/stock-web","notes":"new local C02 symbol; extreme 4B timing row"}
{"row_type":"case","case_id":"C02_GAONCABLE_000500_2024_03_06_WIRE_CABLE_CAPEX_BETA_BLOWOFF_COUNTEREXAMPLE","symbol":"000500","company_name":"가온전선","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"WIRE_CABLE_CAPEX_BETA_PRICE_BLOWOFF_WITHOUT_DIRECT_BACKLOG_MARGIN_BRIDGE","case_type":"price_blowoff_counterexample","positive_or_counterexample":"counterexample","best_trigger":"GAONCABLE_000500_2024_03_06_STAGE2_FALSE_POSITIVE_WIRE_CABLE_CAPEX_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"2024-11-11 corporate-action/share-count drift occurs after main 4B window; retained as reduced-weight guardrail","independent_evidence_weight":0.75,"score_price_alignment":"wire/cable CAPEX beta produced large price MFE but later deep drawdown and share-count drift; it is a price-only blowoff counterexample to Green promotion without direct backlog/ASP/margin bridge","current_profile_verdict":"current_profile_false_positive_if_wire_beta_promoted_to_Green","price_source":"Songdaiki/stock-web","notes":"new local C02 symbol; reduced weight due to late-2024 corporate-action/share-count drift"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HDHE_267260_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_CAPEX_BACKLOG","case_id":"C02_HDHE_267260_2024_03_06_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_RERATING_4B","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_CAPEX_BACKLOG_ASP_MARGIN_RERATING_4B_WATCH","sector":"infra / defense / grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":136000.0,"evidence_available_at_that_date":"source_proxy_only: transformer backlog, datacenter/grid CAPEX demand, export ASP/margin route and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["transformer_backlog","datacenter_grid_capex","export_asp_margin_route","relative_strength"],"stage3_evidence_fields":["backlog_visibility_partial","margin_bridge_partial","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["capex_backlog_rerating","valuation_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":95.22,"MFE_90D_pct":166.91,"MFE_180D_pct":204.04,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.65,"MAE_90D_pct":-7.65,"MAE_180D_pct":-7.65,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":413500.0,"drawdown_after_peak_pct":-19.23,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.33,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"C02 CAPEX/backlog rerating worked, but full Green needs realized backlog, margin, revision and FCF conversion","four_b_evidence_type":["backlog_rerating","datacenter_grid_capex"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late_if_CAPEX_backlog_overpromoted_to_Green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C02_267260_2024_03_06_136000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_US_GRID_BACKLOG_CAPEX","case_id":"C02_HYOSUNGHEAVY_298040_2024_03_06_POWER_EQUIPMENT_US_GRID_BACKLOG_RERATING_4B","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_EQUIPMENT_US_GRID_BACKLOG_MARGIN_RERATING_4B_WATCH","sector":"infra / defense / grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":232000.0,"evidence_available_at_that_date":"source_proxy_only: power equipment / US grid backlog, datacenter grid capex, transformer margin route and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["power_equipment_backlog","US_grid_capex","transformer_margin_route","relative_strength"],"stage3_evidence_fields":["backlog_visibility_partial","margin_bridge_partial","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["grid_backlog_rerating","valuation_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.88,"MFE_90D_pct":102.16,"MFE_180D_pct":123.28,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.53,"MAE_90D_pct":-4.53,"MAE_180D_pct":-4.53,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":518000.0,"drawdown_after_peak_pct":-25.87,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.45,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"grid backlog rerating worked as Stage2A but requires C02 4B peak audit before Green","four_b_evidence_type":["grid_backlog_rerating","US_transformer_capex"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late_if_grid_backlog_rerating_not_peak_audited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_298040_2024_03_06_232000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_DATACENTER_CAPEX_4B","case_id":"C02_LSELECTRIC_010120_2024_03_06_DATACENTER_GRID_CAPEX_EXTREME_4B_BLOWOFF","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DATACENTER_GRID_CAPEX_RELATIVE_STRENGTH_EXTREME_4B_WITH_DELAYED_AUDIT","sector":"infra / defense / grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":79100.0,"evidence_available_at_that_date":"source_proxy_only: datacenter power equipment, smart grid/capex route, relative strength and backlog/ASP narrative visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["datacenter_power_equipment","smart_grid_capex","relative_strength","backlog_ASP_narrative"],"stage3_evidence_fields":["backlog_visibility_partial","margin_bridge_partial","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["extreme_relative_strength","valuation_peak_watch","price_blowoff"],"stage4c_evidence_fields":["delayed_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":103.67,"MFE_90D_pct":208.47,"MFE_180D_pct":208.47,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-3.41,"MAE_90D_pct":-3.41,"MAE_180D_pct":-3.41,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":244000.0,"drawdown_after_peak_pct":-48.28,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.32,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"extreme grid/datacenter rerating worked, but price-only blowoff and later drawdown require delayed 4B audit","four_b_evidence_type":["extreme_relative_strength","capex_theme_blowoff"],"four_c_protection_label":"delayed_4c_watch_after_peak","trigger_outcome_label":"positive_extreme_mfe_then_peak_drawdown","current_profile_verdict":"current_profile_4B_too_late_after_extreme_price_blowoff","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C02_010120_2024_03_06_79100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"GAONCABLE_000500_2024_03_06_STAGE2_FALSE_POSITIVE_WIRE_CABLE_CAPEX_BETA","case_id":"C02_GAONCABLE_000500_2024_03_06_WIRE_CABLE_CAPEX_BETA_BLOWOFF_COUNTEREXAMPLE","symbol":"000500","company_name":"가온전선","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"WIRE_CABLE_CAPEX_BETA_PRICE_BLOWOFF_WITHOUT_DIRECT_BACKLOG_MARGIN_BRIDGE","sector":"infra / defense / grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":27150.0,"evidence_available_at_that_date":"source_proxy_only: wire/cable CAPEX beta and grid theme relative strength visible, but direct long-cycle backlog, ASP/margin and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["wire_cable_capex_beta","grid_theme_beta","relative_strength_event"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_blowoff","bridge_absent","late_share_count_drift_watch"],"stage4c_evidence_fields":["backlog_bridge_absent","margin_bridge_absent","fcf_bridge_absent","late_share_count_drift_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv","profile_path":"atlas/symbol_profiles/000/000500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":77.35,"MFE_90D_pct":174.4,"MFE_180D_pct":174.4,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.42,"MAE_90D_pct":-4.42,"MAE_180D_pct":-4.42,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":74500.0,"drawdown_after_peak_pct":-61.61,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.36,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"wire/cable beta had price MFE but should not become C02 Green without direct backlog, ASP/margin and FCF bridge","four_b_evidence_type":["price_blowoff","theme_beta"],"four_c_protection_label":"price_only_green_block","trigger_outcome_label":"counterexample_price_blowoff_without_direct_bridge","current_profile_verdict":"current_profile_false_positive_if_wire_beta_promoted_to_Green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["late_2024_corporate_action_share_count_drift_reduced_weight"],"corporate_action_window_status":"main_4B_window_clean_but_late_2024_corporate_action_candidate","same_entry_group_id":"C02_000500_2024_03_06_27150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"late-2024 corporate-action/share-count drift watch","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C02_HDHE_267260_2024_03_06_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_RERATING_4B","trigger_id":"HDHE_267260_2024_03_06_STAGE2A_TRANSFORMER_DATACENTER_CAPEX_BACKLOG","symbol":"267260","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable / Yellow-risk / 4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":75,"stage_label_after":"Stage2A with mandatory C02 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Backlog/CAPEX route worked, but Green needs realized backlog, margin, revision and FCF conversion.","MFE_90D_pct":166.91,"MAE_90D_pct":-7.65,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late_if_CAPEX_backlog_overpromoted_to_Green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C02_HYOSUNGHEAVY_298040_2024_03_06_POWER_EQUIPMENT_US_GRID_BACKLOG_RERATING_4B","trigger_id":"HYOSUNGHEAVY_298040_2024_03_06_STAGE2A_US_GRID_BACKLOG_CAPEX","symbol":"298040","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2A with C02 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Power-equipment backlog route worked, but full Green needs conversion evidence.","MFE_90D_pct":102.16,"MAE_90D_pct":-4.53,"score_return_alignment_label":"positive_high_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late_if_grid_backlog_rerating_not_peak_audited"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C02_LSELECTRIC_010120_2024_03_06_DATACENTER_GRID_CAPEX_EXTREME_4B_BLOWOFF","trigger_id":"LSELECTRIC_010120_2024_03_06_STAGE2A_GRID_DATACENTER_CAPEX_4B","symbol":"010120","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2A / extreme 4B blowoff risk","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-watch with extreme 4B audit","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Extreme price rerating was real, but post-peak drawdown proves price-only blowoff must not become Green.","MFE_90D_pct":208.47,"MAE_90D_pct":-3.41,"score_return_alignment_label":"extreme_4b_blowoff_guard_needed","current_profile_verdict":"current_profile_4B_too_late_after_extreme_price_blowoff"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C02_GAONCABLE_000500_2024_03_06_WIRE_CABLE_CAPEX_BETA_BLOWOFF_COUNTEREXAMPLE","trigger_id":"GAONCABLE_000500_2024_03_06_STAGE2_FALSE_POSITIVE_WIRE_CABLE_CAPEX_BETA","symbol":"000500","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":9,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive / price blowoff risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":3,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage1/4B blowoff guard, not C02 Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Wire/cable theme beta had price MFE but lacked direct backlog/ASP/margin/FCF bridge.","MFE_90D_pct":174.4,"MAE_90D_pct":-4.42,"score_return_alignment_label":"price_blowoff_counterexample","current_profile_verdict":"current_profile_false_positive_if_wire_beta_promoted_to_Green"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"137","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive_if_price_blowoff_promoted_to_Green"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R1
completed_loop = 137
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

If this loop is accepted, C02 moves to projected 28 rows and still needs 2 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C02 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/267/267260.json
  - atlas/symbol_profiles/298/298040.json
  - atlas/symbol_profiles/010/010120.json
  - atlas/symbol_profiles/000/000500.json
- Rejected duplicate materialization path:
  - e2r_stock_web_v12_residual_round_R7_loop_136_L7_BIO_HEALTHCARE_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
