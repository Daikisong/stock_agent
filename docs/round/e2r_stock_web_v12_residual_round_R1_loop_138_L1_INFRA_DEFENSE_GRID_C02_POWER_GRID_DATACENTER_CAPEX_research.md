# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_138_L1_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selected_round: R1
selected_loop: 138
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: WIRE_TRANSFORMER_GRID_CAPEX_BACKLOG_ASP_MARGIN_RERATING_4B_WATCH
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

This is the corrected valid run after an accidental duplicate loop137 materialization path was discarded. Loop137 already used `267260`, `298040`, `010120`, and `000500`; this loop uses new C02 symbol/trigger/date combinations only.

This loop adds 3 new independent C02 rows and moves C02 from static 24 rows to local projected 28 after loop137, then to projected 31 after this loop. The 30-row minimum stability threshold is reached.

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

C02 is the power-grid / datacenter CAPEX archetype. Direct transformer backlog is a load-bearing girder. Cable/theme beta after a capital event is scaffolding: useful for a temporary climb, but not a permanent floor unless backlog, ASP, margin, revision and FCF lock in.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C02 static rows | 24 |
| C02 need to 30 | 6 |
| local C02 loop137 projected rows | 28 |
| this loop projected rows | 31 |

Rejected local duplicate set:

```text
267260, 298040, 010120, 000500
```

Selected C02 symbols:

| symbol | company | status |
|---|---|---|
| 103590 | 일진전기 | new local C02 grid/wire/transformer positive |
| 033100 | 제룡전기 | new local C02 distribution-transformer extreme 4B positive |
| 001440 | 대한전선 | new local C02 cable-theme blowoff Green-block counterexample |

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
| 103590 / 2024-03-06 | true | true | entry_after_2024_02_13_corporate_action_candidate_clean_forward_window | true, weight 0.90 |
| 033100 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 001440 / 2024-04-04 | true | true | entry_after_2024_04_02_corporate_action_candidate | true, weight 0.85 |

Corporate-action notes:

- 일진전기 has a 2024-02-13 corporate-action candidate before the selected 2024-03-06 entry, so the row is usable but reduced weight.
- 제룡전기 has old corporate-action candidates before the selected 2024 window.
- 대한전선 has a 2024-04-02 corporate-action candidate, so entry is deliberately moved to 2024-04-04 and the row is reduced weight.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| WIRE_TRANSFORMER_GRID_CAPEX_BACKLOG_ASP_MARGIN_RERATING_4B_WATCH | C02 | grid/wire/transformer CAPEX can support Stage2A, but Green needs conversion evidence |
| DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG_EXTREME_4B_WITH_MARGIN_BRIDGE_WATCH | C02 | transformer export backlog can produce extreme 4B but requires delayed peak audit |
| CABLE_CAPEX_THEME_BLOWOFF_AFTER_CAPITAL_EVENT_WITHOUT_DIRECT_MARGIN_FCF_BRIDGE | C02 | cable CAPEX beta after capital event should not become Green without direct backlog/margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C02_ILJIN_103590_2024_03_06_WIRE_TRANSFORMER_GRID_CAPEX_BACKLOG_RERATING_4B | 103590 | 일진전기 | 4B_overlay_success | positive | 133.95% 90D MFE with direct grid/backlog route |
| C02_JERYONG_033100_2024_03_06_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG_EXTREME_4B | 033100 | 제룡전기 | extreme_4B_overlay_success | positive | 228.01% 90D MFE but 61.07% post-peak drawdown |
| C02_DAEHANCABLE_001440_2024_04_04_CABLE_CAPEX_RERATING_AFTER_CAPITAL_EVENT_GREEN_BLOCK | 001440 | 대한전선 | price_blowoff_counterexample | counterexample | 83.45% MFE but capital-event/cable-beta bridge insufficient for Green |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 3 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 3 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 103590 | source_proxy_only | grid/wire/transformer backlog and export ASP/margin route | required before promotion |
| 033100 | source_proxy_only | distribution-transformer export backlog and margin route | required before promotion |
| 001440 | source_proxy_only | cable CAPEX theme after capital event, but direct backlog/margin bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 103590 | atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv | atlas/symbol_profiles/103/103590.json |
| 033100 | atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv | atlas/symbol_profiles/033/033100.json |
| 001440 | atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv | atlas/symbol_profiles/001/001440.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| ILJIN_103590_2024_03_06_STAGE2A_GRID_BACKLOG_CAPEX | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 12930 | grid/wire/transformer backlog CAPEX route |
| JERYONG_033100_2024_03_06_STAGE2A_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 30700 | distribution transformer export backlog |
| DAEHANCABLE_001440_2024_04_04_STAGE2_FALSE_POSITIVE_CABLE_CAPEX_GREEN_BLOCK | Stage2 | 2024-04-04 | 2024-04-04 | 11420 | cable CAPEX beta after capital event |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 103590 | 2024-03-06 | 12930 | 89.48 | -7.11 | 133.95 | -7.11 | 133.95 | -7.11 | 2024-05-29 | 30250 | -45.12 |
| 033100 | 2024-03-06 | 30700 | 84.04 | -11.07 | 228.01 | -11.07 | 228.01 | -11.07 | 2024-07-11 | 100700 | -61.07 |
| 001440 | 2024-04-04 | 11420 | 83.45 | -5.17 | 83.45 | -5.17 | 83.45 | -12.43 | 2024-05-21 | 20950 | -52.27 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 103590 | Stage2A possible; 4B after grid/backlog rerating | high MFE but peak drawdown | current_profile_4B_too_late |
| 033100 | Stage2A possible; extreme transformer rerating | huge MFE then severe peak drawdown | current_profile_4B_too_late_after_extreme_transformer_blowoff |
| 001440 | Stage2 risk if cable CAPEX beta is over-credited | price MFE but Green bridge absent | current_profile_false_positive_if_cable_capex_beta_promoted_to_Green |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C02 interpretation:

- Stage2A works when grid CAPEX is connected to transformer backlog, export ASP/margin, revision and FCF.
- Extreme transformer rerating is useful, but still a 4B audit unless conversion evidence is visible.
- Cable CAPEX beta after a capital event must be capped below Yellow/Green without direct backlog/margin bridge.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 103590 | 0.43 | 1.00 | grid/wire/transformer backlog rerating | full-window 4B audit required |
| 033100 | 0.30 | 1.00 | distribution-transformer export backlog | delayed 4B/4C audit required |
| 001440 | 0.55 | 1.00 | cable CAPEX price blowoff after capital event | price-only Green block |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 103590 | thesis_break_watch_only | not hard 4C, but Green needs realized conversion |
| 033100 | delayed_4c_watch_after_peak | extreme peak drawdown requires delayed audit |
| 001440 | price_only_green_block | cable theme beta blocks Yellow/Green without direct bridge |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L1_INFRA_DEFENSE_GRID
confidence = medium
```

Candidate:

> In L1 grid/infrastructure names, direct transformer/grid CAPEX names can enter Stage2A when backlog, CAPA/ASP, margin and revision routes are visible. But cable CAPEX theme beta, especially after a capital event, should remain Stage1/Stage2-watch unless direct backlog/margin/FCF bridge is confirmed.

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

if direct_transformer_or_power_equipment and backlog_margin_bridge_visible:
    allow_stage2_actionable = true
    require_4B_peak_audit_if_MFE_90D > 80

if cable_capex_theme_beta and capital_event_quality_watch:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if price_only_relative_strength and MFE_90D > 80:
    add C02_price_blowoff_4B_audit = true

if recent_or_pre_entry_corporate_action_quality_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / blowoff | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 148.47 | -7.78 | 148.47 | -10.2 | 1 | strong C02 but bridge/quality rule needed |
| P0b calibrated rollback | rollback | 3 | 148.47 | -7.78 | 148.47 | -10.2 | 1 | over-credits cable CAPEX beta |
| P1 sector_specific_candidate_profile | L1 | 2 Stage2A + 1 guard | 180.98 | -9.09 | 180.98 | -9.09 | 0 | better with direct backlog/margin bridge |
| P2 canonical_archetype_candidate_profile | C02 | 2 Stage2A + 1 guard | 180.98 | -9.09 | 180.98 | -9.09 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C02 guard | 2 Stage2A + 1 guard | 180.98 | -9.09 | 180.98 | -9.09 | 0 | adds cable/capital-event blowoff guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 103590 | Stage2A aligned; 4B/capital-quality audit needed | current_profile_4B_too_late |
| 033100 | Stage2A aligned; extreme 4B audit needed | current_profile_4B_too_late_after_extreme_transformer_blowoff |
| 001440 | Stage2 theme beta should not become Yellow/Green without bridge | current_profile_false_positive_if_cable_capex_beta_promoted_to_Green |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | mixed C02 fine ids | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 24 -> local 28 -> projected 31; reaches minimum stability threshold |

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
  - current_profile_false_positive_if_price_blowoff_promoted_to_Green
new_axis_proposed: C02_grid_capex_backlog_margin_bridge_required|C02_price_blowoff_4B_audit|C02_cable_capex_theme_beta_green_block|capital_event_quality_weight_reduction
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
- Avoids loop137 C02 symbols.
- Moves C02 to projected 31 rows, crossing the 30-row stability threshold.
- Keeps 001440 with reduced independent weight because the selected trigger follows a recent 2024-04-02 corporate-action candidate.
- Treats 001440 as cable CAPEX blowoff/Green-block evidence, not Green promotion.
- Discards the accidental duplicate loop137 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated C02 loop137 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_grid_capex_backlog_margin_bridge_required,canonical_archetype_specific,L1_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"103590/033100 show direct grid/transformer routes can work while 001440 needs a cable-theme guard","preserves direct Stage2A rows and blocks cable theme beta from Green","ILJIN_103590_2024_03_06_STAGE2A_GRID_BACKLOG_CAPEX|JERYONG_033100_2024_03_06_STAGE2A_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG|DAEHANCABLE_001440_2024_04_04_STAGE2_FALSE_POSITIVE_CABLE_CAPEX_GREEN_BLOCK",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C02_price_blowoff_4B_audit,canonical_archetype_specific,L1_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"103590/033100/001440 all had large MFE and later drawdown, so price-only peaks need audit","prevents C02 price-only peaks from becoming Green without backlog/margin/FCF confirmation","ILJIN_103590_2024_03_06_STAGE2A_GRID_BACKLOG_CAPEX|JERYONG_033100_2024_03_06_STAGE2A_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG|DAEHANCABLE_001440_2024_04_04_STAGE2_FALSE_POSITIVE_CABLE_CAPEX_GREEN_BLOCK",3,3,1,medium,canonical_shadow_only,"4B overlay/risk calibration"
shadow_weight,C02_cable_capex_theme_beta_green_block,canonical_archetype_specific,L1_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"001440 shows cable CAPEX theme beta after capital event can price-rerate without direct backlog, ASP/margin and FCF bridge","caps cable CAPEX beta at Stage1/Stage2-watch unless direct bridge exists","DAEHANCABLE_001440_2024_04_04_STAGE2_FALSE_POSITIVE_CABLE_CAPEX_GREEN_BLOCK",1,1,1,medium,canonical_shadow_only,"counterexample guardrail"
shadow_weight,capital_event_quality_weight_reduction,archetype_specific_quality_flag,L1_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"103590 and 001440 have near-entry corporate-action/capital-quality caveats","keeps rows usable but lowers independent evidence weight","ILJIN_103590_2024_03_06_STAGE2A_GRID_BACKLOG_CAPEX|DAEHANCABLE_001440_2024_04_04_STAGE2_FALSE_POSITIVE_CABLE_CAPEX_GREEN_BLOCK",2,2,1,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C02_ILJIN_103590_2024_03_06_WIRE_TRANSFORMER_GRID_CAPEX_BACKLOG_RERATING_4B","symbol":"103590","company_name":"일진전기","round":"R1","loop":"138","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"WIRE_TRANSFORMER_GRID_CAPEX_BACKLOG_ASP_MARGIN_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"ILJIN_103590_2024_03_06_STAGE2A_GRID_BACKLOG_CAPEX","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"corporate-action candidate on 2024-02-13 before selected entry; selected 2024-03-06 forward window treated as usable with reduced weight","independent_evidence_weight":0.9,"score_price_alignment":"wire/transformer grid CAPEX and backlog route captured 133.95% 90D MFE, but peak-to-trough drawdown required C02 4B audit before Green","current_profile_verdict":"current_profile_4B_too_late_if_grid_backlog_overpromoted_to_Green","price_source":"Songdaiki/stock-web","notes":"new local C02 symbol; direct grid CAPEX/backlog positive with pre-entry corporate-action caveat"}
{"row_type":"case","case_id":"C02_JERYONG_033100_2024_03_06_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG_EXTREME_4B","symbol":"033100","company_name":"제룡전기","round":"R1","loop":"138","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG_EXTREME_4B_WITH_MARGIN_BRIDGE_WATCH","case_type":"extreme_4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"JERYONG_033100_2024_03_06_STAGE2A_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only before selected 2024 window","independent_evidence_weight":0.95,"score_price_alignment":"distribution-transformer/export backlog rerating captured 228.01% 90D MFE, but later 61% peak drawdown required 4B peak audit rather than price-only Green","current_profile_verdict":"current_profile_4B_too_late_after_extreme_transformer_blowoff","price_source":"Songdaiki/stock-web","notes":"new local C02 symbol; KOSDAQ transformer extreme 4B row"}
{"row_type":"case","case_id":"C02_DAEHANCABLE_001440_2024_04_04_CABLE_CAPEX_RERATING_AFTER_CAPITAL_EVENT_GREEN_BLOCK","symbol":"001440","company_name":"대한전선","round":"R1","loop":"138","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"CABLE_CAPEX_THEME_BLOWOFF_AFTER_CAPITAL_EVENT_WITHOUT_DIRECT_MARGIN_FCF_BRIDGE","case_type":"price_blowoff_counterexample","positive_or_counterexample":"counterexample","best_trigger":"DAEHANCABLE_001440_2024_04_04_STAGE2_FALSE_POSITIVE_CABLE_CAPEX_GREEN_BLOCK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"2024-04-02 corporate-action candidate avoided by selecting 2024-04-04 entry; old corporate-action history remains a quality caveat","independent_evidence_weight":0.85,"score_price_alignment":"cable CAPEX theme after capital event produced 83.45% MFE but later fell below entry; this is a price/blowoff and bridge-quality counterexample to C02 Green promotion","current_profile_verdict":"current_profile_false_positive_if_cable_capex_beta_promoted_to_Green","price_source":"Songdaiki/stock-web","notes":"entry moved to 2024-04-04 after 2024-04-02 corporate-action candidate; reduced-weight Green-block counterexample"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"ILJIN_103590_2024_03_06_STAGE2A_GRID_BACKLOG_CAPEX","case_id":"C02_ILJIN_103590_2024_03_06_WIRE_TRANSFORMER_GRID_CAPEX_BACKLOG_RERATING_4B","symbol":"103590","company_name":"일진전기","round":"R1","loop":"138","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"WIRE_TRANSFORMER_GRID_CAPEX_BACKLOG_ASP_MARGIN_RERATING_4B_WATCH","sector":"infra / defense / grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":12930.0,"evidence_available_at_that_date":"source_proxy_only: transformer/wire backlog, grid CAPEX demand, export ASP/margin route and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["grid_capex","transformer_wire_backlog","export_ASP_margin_route","relative_strength"],"stage3_evidence_fields":["backlog_visibility_partial","margin_bridge_partial","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["grid_capex_rerating","valuation_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv","profile_path":"atlas/symbol_profiles/103/103590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":89.48,"MFE_90D_pct":133.95,"MFE_180D_pct":133.95,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.11,"MAE_90D_pct":-7.11,"MAE_180D_pct":-7.11,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":30250.0,"drawdown_after_peak_pct":-45.12,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.43,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"grid/wire/transformer backlog rerating worked as Stage2A, but 45% peak drawdown means Green requires non-price conversion proof","four_b_evidence_type":["grid_capex_rerating","backlog_rerating"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch_reduced_weight","current_profile_verdict":"current_profile_4B_too_late_if_grid_backlog_overpromoted_to_Green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["pre_entry_2024_02_13_corporate_action_candidate_reduced_weight"],"corporate_action_window_status":"entry_after_corporate_action_candidate_clean_forward_window","same_entry_group_id":"C02_103590_2024_03_06_12930","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"2024-02-13 corporate-action candidate before selected entry","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"JERYONG_033100_2024_03_06_STAGE2A_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG","case_id":"C02_JERYONG_033100_2024_03_06_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG_EXTREME_4B","symbol":"033100","company_name":"제룡전기","round":"R1","loop":"138","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG_EXTREME_4B_WITH_MARGIN_BRIDGE_WATCH","sector":"infra / defense / grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":30700.0,"evidence_available_at_that_date":"source_proxy_only: distribution transformer export backlog, grid CAPEX, margin route and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["distribution_transformer_export_backlog","grid_capex","margin_bridge_route","relative_strength"],"stage3_evidence_fields":["backlog_visibility_partial","margin_bridge_partial","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["extreme_transformer_rerating","valuation_peak_watch"],"stage4c_evidence_fields":["delayed_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv","profile_path":"atlas/symbol_profiles/033/033100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":84.04,"MFE_90D_pct":228.01,"MFE_180D_pct":228.01,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.07,"MAE_90D_pct":-11.07,"MAE_180D_pct":-11.07,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":100700.0,"drawdown_after_peak_pct":-61.07,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.3,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"extreme distribution-transformer rerating worked, but 61% peak drawdown forces delayed 4B/4C audit","four_b_evidence_type":["extreme_transformer_rerating","export_backlog_rerating"],"four_c_protection_label":"delayed_4c_watch_after_peak","trigger_outcome_label":"positive_extreme_mfe_then_peak_drawdown","current_profile_verdict":"current_profile_4B_too_late_after_extreme_transformer_blowoff","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C02_033100_2024_03_06_30700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DAEHANCABLE_001440_2024_04_04_STAGE2_FALSE_POSITIVE_CABLE_CAPEX_GREEN_BLOCK","case_id":"C02_DAEHANCABLE_001440_2024_04_04_CABLE_CAPEX_RERATING_AFTER_CAPITAL_EVENT_GREEN_BLOCK","symbol":"001440","company_name":"대한전선","round":"R1","loop":"138","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"CABLE_CAPEX_THEME_BLOWOFF_AFTER_CAPITAL_EVENT_WITHOUT_DIRECT_MARGIN_FCF_BRIDGE","sector":"infra / defense / grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":11420.0,"evidence_available_at_that_date":"source_proxy_only: cable CAPEX/grid theme rebound after capital event visible, but direct backlog, ASP/margin, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cable_capex_theme_beta","grid_theme_rebound","relative_strength_event"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_blowoff","capital_event_quality_watch","bridge_absent"],"stage4c_evidence_fields":["direct_backlog_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv","profile_path":"atlas/symbol_profiles/001/001440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":83.45,"MFE_90D_pct":83.45,"MFE_180D_pct":83.45,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.17,"MAE_90D_pct":-5.17,"MAE_180D_pct":-12.43,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":20950.0,"drawdown_after_peak_pct":-52.27,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.55,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cable CAPEX theme after capital event was tradable as 4B but must not become Green without direct backlog/margin/FCF bridge","four_b_evidence_type":["price_blowoff","capital_event_quality_watch"],"four_c_protection_label":"price_only_green_block","trigger_outcome_label":"counterexample_price_blowoff_without_direct_bridge","current_profile_verdict":"current_profile_false_positive_if_cable_capex_beta_promoted_to_Green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["post_2024_04_02_corporate_action_entry_reduced_weight"],"corporate_action_window_status":"entry_after_2024_04_02_corporate_action_candidate","same_entry_group_id":"C02_001440_2024_04_04_11420","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"entry selected after 2024-04-02 corporate-action candidate","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C02_ILJIN_103590_2024_03_06_WIRE_TRANSFORMER_GRID_CAPEX_BACKLOG_RERATING_4B","trigger_id":"ILJIN_103590_2024_03_06_STAGE2A_GRID_BACKLOG_CAPEX","symbol":"103590","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2A with C02 4B/capital-quality audit","changed_components":["valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Grid/wire/transformer route worked, but Green needs backlog-to-margin conversion and clean capital-quality audit.","MFE_90D_pct":133.95,"MAE_90D_pct":-7.11,"score_return_alignment_label":"positive_high_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late_if_grid_backlog_overpromoted_to_Green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C02_JERYONG_033100_2024_03_06_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG_EXTREME_4B","trigger_id":"JERYONG_033100_2024_03_06_STAGE2A_DISTRIBUTION_TRANSFORMER_EXPORT_BACKLOG","symbol":"033100","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":10,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage2A / extreme transformer 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage2-watch with extreme C02 4B audit","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Extreme transformer rerating was real, but 61% peak drawdown proves price-only peak cannot become Green.","MFE_90D_pct":228.01,"MAE_90D_pct":-11.07,"score_return_alignment_label":"extreme_4b_blowoff_guard_needed","current_profile_verdict":"current_profile_4B_too_late_after_extreme_transformer_blowoff"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C02_DAEHANCABLE_001440_2024_04_04_CABLE_CAPEX_RERATING_AFTER_CAPITAL_EVENT_GREEN_BLOCK","trigger_id":"DAEHANCABLE_001440_2024_04_04_STAGE2_FALSE_POSITIVE_CABLE_CAPEX_GREEN_BLOCK","symbol":"001440","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":3,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 false-positive / cable CAPEX blowoff risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":4,"accounting_trust_risk_score":0},"weighted_score_after":42,"stage_label_after":"Stage1/4B blowoff guard, not C02 Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Cable theme after capital event lacked direct backlog/ASP/margin/FCF bridge.","MFE_90D_pct":83.45,"MAE_90D_pct":-5.17,"score_return_alignment_label":"price_blowoff_counterexample","current_profile_verdict":"current_profile_false_positive_if_cable_capex_beta_promoted_to_Green"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"138","large_sector_id":"L1_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive_if_price_blowoff_promoted_to_Green"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 138
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C02_POWER_GRID_DATACENTER_CAPEX_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted together with local C02 loop137, C02 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C02 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/103/103590.json
  - atlas/symbol_profiles/033/033100.json
  - atlas/symbol_profiles/001/001440.json
- Rejected local duplicate C02 symbols:
  - 267260, 298040, 010120, 000500
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R1_loop_137_L1_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
