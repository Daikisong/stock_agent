# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_vs_full_4B_timing_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
```

This loop starts loop 91 after the completed R13 loop 90 cross-archetype review. It fills C02 with a transformer/data-center CAPEX positive case and two timing/bridge-quality guardrails.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 91
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 91
```

R1 permits L1 industrials / infrastructure / defense / grid research. Previous R1 loop 90 used C04 nuclear, and R11 loop 90 used C05 EPC; this loop returns to C02 but avoids the top repeated C02 symbols.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C02_POWER_GRID_DATACENTER_CAPEX = 22 rows / 12 symbols / good-bad Stage2 11-4 / 4B-4C 2-0
top covered symbols include 000500(3), 006340(3), 033100(3), 001440(2), 017040(2), 189860(2)
previous R1 loop-89 C02 symbols avoided: 103590, 199820, 060370
previous R1 loop-90 C04 symbols avoided: 130660, 105840, 094820
previous R11 loop-90 C05 symbols avoided: 047040, 028050, 052690
```

Selected rows avoid hard duplicates and top repeated C02 symbols:

```text
298040 / Stage2-Actionable / 2024-02-20
119850 / Stage2-Actionable / 2024-05-16
010120 / Stage4B / 2024-07-24
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 298040 | atlas/symbol_profiles/298/298040.json | no corporate-action candidate |
| 119850 | atlas/symbol_profiles/119/119850.json | selected 2024/2025 window clean after old 2013/2014/2017 CA candidates |
| 010120 | atlas/symbol_profiles/010/010120.json | selected 2024/2025 window clean after old 1995/1999/2003 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L91_C02_HYOSUNGHEAVY_2024_TRANSFORMER_DATACENTER_CAPEX_POSITIVE | 298040 | 2024-02-20 | yes | 180 | yes | yes | true |
| R1L91_C02_GNCENERGY_2024_BACKUP_POWER_THEME_HIGH_MAE_FALSE_STAGE2 | 119850 | 2024-05-16 | yes | 180 | yes | yes | true |
| R1L91_C02_LSELECTRIC_2024_SWITCHGEAR_CAPEX_LOCAL_4B_TOO_EARLY | 010120 | 2024-07-24 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C02_POWER_GRID_DATACENTER_CAPEX | TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE | Positive Stage2 requires backlog, capacity, customer quality, delivery, margin, or revision bridge. |
| C02_POWER_GRID_DATACENTER_CAPEX | BACKUP_POWER_THEME_HIGH_MAE_FALSE_STAGE2 | Backup-power/data-center label without order/margin bridge can create high-MAE timing traps. |
| C02_POWER_GRID_DATACENTER_CAPEX | SWITCHGEAR_LOCAL_4B_TOO_EARLY | Local 4B after spike can be too early if full-window order/revision bridge later survives. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L91_C02_HYOSUNGHEAVY_2024_TRANSFORMER_DATACENTER_CAPEX_POSITIVE | 298040 | 효성중공업 | positive | Transformer/data-center grid CAPEX bridge produced very high MFE with shallow MAE. |
| R1L91_C02_GNCENERGY_2024_BACKUP_POWER_THEME_HIGH_MAE_FALSE_STAGE2 | 119850 | 지엔씨에너지 | counterexample | Backup-power theme had high MAE and needs bridge-quality filter. |
| R1L91_C02_LSELECTRIC_2024_SWITCHGEAR_CAPEX_LOCAL_4B_TOO_EARLY | 010120 | LS ELECTRIC | counterexample / 4B timing | Severe local drawdown looked like 4B, but full-window later made a new high. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Hyosung Heavy transformer/CAPEX bridge | historical public/report proxy | true | true | shadow-only positive |
| GNC Energy backup-power high-MAE row | historical public/news proxy | true | true | false-Stage2 / timing guardrail |
| LS ELECTRIC local-4B timing row | historical public/news proxy | true | true | 4B local-vs-full counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 298040 | atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv | atlas/symbol_profiles/298/298040.json |
| 119850 | atlas/ohlcv_tradable_by_symbol_year/119/119850/2024.csv; 2025.csv | atlas/symbol_profiles/119/119850.json |
| 010120 | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; 2025.csv | atlas/symbol_profiles/010/010120.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L91_C02_HYOSUNGHEAVY_2024_STAGE2_ACTIONABLE_TRANSFORMER_DATACENTER_CAPEX | 298040 | Stage2-Actionable | 2024-02-20 | 186100 | positive | transformer/data-center CAPEX bridge worked |
| R1L91_C02_GNCENERGY_2024_STAGE2_FALSE_POSITIVE_BACKUP_POWER_THEME | 119850 | Stage2-Actionable | 2024-05-16 | 9950 | counterexample | backup-power theme high-MAE timing trap |
| R1L91_C02_LSELECTRIC_2024_STAGE4B_LOCAL_SWITCHGEAR_CAPEX_CAP | 010120 | Stage4B | 2024-07-24 | 260000 | 4B timing counterexample | local 4B too early; full-window later recovered |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L91_C02_HYOSUNGHEAVY_2024_STAGE2_ACTIONABLE_TRANSFORMER_DATACENTER_CAPEX | 186100 | 56.37 | -3.39 | 151.99 | -3.39 | 178.34 | -3.39 | 2024-11-12 | 518000 | -29.34 |
| R1L91_C02_GNCENERGY_2024_STAGE2_FALSE_POSITIVE_BACKUP_POWER_THEME | 9950 | 14.97 | -28.04 | 14.97 | -38.89 | 88.64 | -38.89 | 2025-02-19 | 18770 | -26.16 |
| R1L91_C02_LSELECTRIC_2024_STAGE4B_LOCAL_SWITCHGEAR_CAPEX_CAP | 260000 | 5.58 | -44.23 | 5.58 | -51.46 | 16.73 | -51.46 | 2025-02-19 | 303500 | -51.63 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C02 Stage2 needs order/backlog/capacity/margin/revision bridge |
| local_4b_watch_guard | refine: local 4B must be split from full-window 4B when order/revision bridge continues |
| high_MAE_guardrail | strengthen: high MAE triggers bridge recheck, not automatic 4C |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is grid-CAPEX bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 298040 | good_stage2 | Backlog/capacity/margin bridge produced high MFE with shallow MAE. |
| 119850 | bad_stage2 / timing trap | Theme entry had high MAE and required order/margin bridge verification. |
| 010120 | local_4B_timing_counterexample | Local drawdown was severe, but full-window later made a higher peak. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 119850 backup-power theme | 0.61 | 0.61 | high-MAE timing trap; not clean positive Stage2 without bridge |
| 010120 switchgear CAPEX | 0.95 | 0.86 | local 4B too early because full-window order/revision bridge later recovered |
| 298040 transformer CAPEX | n/a | n/a | positive Stage2, but later transformer valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 119850 / 010120
```

No hard 4C candidate is proposed. R1 loop 91 is about Stage2 bridge quality and local-vs-full 4B timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 power grid / data-center CAPEX cases, Stage2 requires verified order/backlog, capacity, customer quality, delivery schedule, gross-margin recovery, or revision bridge. Grid, data-center, switchgear, transformer, or backup-power label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
rule = C02 should split real transformer/grid CAPEX positives from backup-power theme timing traps and local-4B-too-early rows. 4B rows are overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 57.51 | -31.25 | 0.67 | mixed; C02 bridge/timing split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 57.51 | -31.25 | 0.67 | weaker bridge/local-4B handling |
| P1 sector_specific_candidate_profile | L1 grid CAPEX bridge required | 2 | 83.48 | -21.14 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C02 bridge vs timing split | 2 | 83.48 | -21.14 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing grid themes as positive | 1 | 151.99 | -3.39 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 298040 transformer CAPEX bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 151.99 | -3.39 | transformer_datacenter_CAPEX_bridge_positive |
| 119850 backup-power theme | 66 | Stage2-Actionable | 53 | Stage1/Watch | 14.97 | -38.89 | backup_power_theme_high_MAE_false_stage2 |
| 010120 local switchgear 4B | 70 | Stage3-Yellow-like | 56 | Stage4B-local-watch/full-window-recheck | 5.58 | -51.46 | local_4B_too_early_full_window_recovery |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C02 transformer/data-center CAPEX positive, backup-power theme high-MAE false Stage2, and switchgear local-4B-too-early timing split using non-top-covered symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: transformer_datacenter_CAPEX_bridge_positive, backup_power_theme_high_MAE_false_stage2, local_4B_too_early_full_window_recovery
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C02 power grid/data-center CAPEX bridge vs theme/timing split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,C02_requires_order_backlog_capacity_margin_revision_bridge,0,"C02 Stage2 should require order/backlog, capacity, customer quality, delivery, margin, or revision bridge, not grid/data-center/backup-power label alone","Hyosung Heavy positive worked; GNC Energy local theme row showed high MAE without bridge","R1L91_C02_HYOSUNGHEAVY_2024_STAGE2_ACTIONABLE_TRANSFORMER_DATACENTER_CAPEX|R1L91_C02_GNCENERGY_2024_STAGE2_FALSE_POSITIVE_BACKUP_POWER_THEME",2,2,1,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,split_local_4B_from_full_window_4B_when_order_revision_bridge_continues,0,"Power equipment leaders can suffer severe local drawdown yet later make new highs if order/revision bridge continues; local 4B cannot be treated as full thesis cap without non-price deterioration","LS ELECTRIC local 4B had MAE90=-51.46 but later full-window peak exceeded local spike","R1L91_C02_LSELECTRIC_2024_STAGE4B_LOCAL_SWITCHGEAR_CAPEX_CAP",1,1,1,medium,guardrail_shadow_only,"4B timing overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,high_MAE_requires_bridge_recheck_not_automatic_4C,0,"High MAE in C02 after theme spikes should trigger bridge recheck; it is not automatically 4C if full-window order/revision evidence later survives","GNC Energy and LS ELECTRIC both had high local MAE but different full-window outcomes","R1L91_C02_GNCENERGY_2024_STAGE2_FALSE_POSITIVE_BACKUP_POWER_THEME|R1L91_C02_LSELECTRIC_2024_STAGE4B_LOCAL_SWITCHGEAR_CAPEX_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L91_C02_HYOSUNGHEAVY_2024_TRANSFORMER_DATACENTER_CAPEX_POSITIVE", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L91_C02_HYOSUNGHEAVY_2024_STAGE2_ACTIONABLE_TRANSFORMER_DATACENTER_CAPEX", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Transformer / data-center grid CAPEX order and margin bridge produced very high 90D/180D MFE with shallow early MAE; C02 works when backlog, capacity, customer quality, and margin/revision bridge are visible.", "current_profile_verdict": "current_profile_kept_but_C02_positive_requires_order_backlog_capacity_margin_bridge_not_grid_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L91_C02_GNCENERGY_2024_BACKUP_POWER_THEME_HIGH_MAE_FALSE_STAGE2", "symbol": "119850", "company_name": "지엔씨에너지", "round": "R1", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING", "case_type": "failed_rerating_high_mae_timing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L91_C02_GNCENERGY_2024_STAGE2_FALSE_POSITIVE_BACKUP_POWER_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.75, "score_price_alignment": "Data-center backup-power / genset theme showed high local MFE but also deep MAE and later re-acceleration; C02 should not score this as clean Stage2 unless generator order, margin, delivery, and recurring service bridge are verified.", "current_profile_verdict": "current_profile_false_positive_if_backup_power_theme_counts_without_order_margin_delivery_bridge", "price_source": "Songdaiki/stock-web", "notes": "Modern window clean after old 2013/2014/2017 CA candidates. Reduced weight because full-window later recovery makes it a timing/bridge-quality counterexample rather than a pure failure."}
{"row_type": "case", "case_id": "R1L91_C02_LSELECTRIC_2024_SWITCHGEAR_CAPEX_LOCAL_4B_TOO_EARLY", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING", "case_type": "local_4b_timing_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L91_C02_LSELECTRIC_2024_STAGE4B_LOCAL_SWITCHGEAR_CAPEX_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.75, "score_price_alignment": "Switchgear / grid CAPEX premium had a severe local drawdown after the July spike, but the full 180D window later made a new high. This is a local-4B timing counterexample: price-only local cap must not override still-expanding non-price order/revision evidence.", "current_profile_verdict": "current_profile_local_4B_too_early_if_full_window_order_revision_bridge_continues", "price_source": "Songdaiki/stock-web", "notes": "Old CA candidates are before 2004; selected 2024/2025 window clean. Reduced weight because it tests local-vs-full 4B timing rather than pure negative outcome."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L91_C02_HYOSUNGHEAVY_2024_STAGE2_ACTIONABLE_TRANSFORMER_DATACENTER_CAPEX", "case_id": "R1L91_C02_HYOSUNGHEAVY_2024_TRANSFORMER_DATACENTER_CAPEX_POSITIVE", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING", "sector": "transformer_datacenter_grid_CAPEX", "primary_archetype": "transformer_backlog_capacity_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_vs_full_4B_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-20", "entry_price": 186100.0, "evidence_available_at_that_date": "transformer/grid data-center CAPEX, order backlog, capacity, export/customer quality, and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["transformer_order_backlog_proxy", "datacenter_grid_CAPEX_proxy", "capacity_expansion_visibility", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "very_high_MFE90", "very_high_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["valuation_watch_after_transformer_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv", "profile_path": "atlas/symbol_profiles/298/298040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 56.37, "MFE_90D_pct": 151.99, "MFE_180D_pct": 178.34, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.39, "MAE_90D_pct": -3.39, "MAE_180D_pct": -3.39, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-12", "peak_price": 518000.0, "drawdown_after_peak_pct": -29.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_transformer_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "grid_CAPEX_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_transformer_datacenter_CAPEX_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L91_C02_298040_2024-02-20_186100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L91_C02_GNCENERGY_2024_STAGE2_FALSE_POSITIVE_BACKUP_POWER_THEME", "case_id": "R1L91_C02_GNCENERGY_2024_BACKUP_POWER_THEME_HIGH_MAE_FALSE_STAGE2", "symbol": "119850", "company_name": "지엔씨에너지", "round": "R1", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING", "sector": "datacenter_backup_power_genset", "primary_archetype": "backup_power_theme_without_order_margin_delivery_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_vs_full_4B_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 9950.0, "evidence_available_at_that_date": "data-center backup power / generator-set theme and emergency power demand proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["backup_power_theme", "datacenter_power_demand_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["high_MAE30", "high_MAE90", "order_margin_delivery_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/119/119850/2024.csv|atlas/ohlcv_tradable_by_symbol_year/119/119850/2025.csv", "profile_path": "atlas/symbol_profiles/119/119850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.97, "MFE_90D_pct": 14.97, "MFE_180D_pct": 88.64, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.04, "MAE_90D_pct": -38.89, "MAE_180D_pct": -38.89, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-19", "peak_price": 18770.0, "drawdown_after_peak_pct": -26.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.61, "four_b_full_window_peak_proximity": 0.61, "four_b_timing_verdict": "local_theme_entry_had_high_MAE_but_full_window_later_recovery_requires_bridge_confirmation", "four_b_evidence_type": ["theme_premium", "positioning_overheat", "order_margin_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_backup_power_theme_high_MAE_timing_counterexample", "current_profile_verdict": "current_profile_false_positive_if_backup_power_theme_counts_without_order_margin_delivery_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R1L91_C02_119850_2024-05-16_9950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L91_C02_LSELECTRIC_2024_STAGE4B_LOCAL_SWITCHGEAR_CAPEX_CAP", "case_id": "R1L91_C02_LSELECTRIC_2024_SWITCHGEAR_CAPEX_LOCAL_4B_TOO_EARLY", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING", "sector": "switchgear_grid_CAPEX_order_revision", "primary_archetype": "local_4B_too_early_when_order_revision_bridge_continues", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_vs_full_4B_timing_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-07-24", "entry_date": "2024-07-24", "entry_price": 260000.0, "evidence_available_at_that_date": "switchgear/grid CAPEX premium after July spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["switchgear_grid_CAPEX_theme", "relative_strength_spike", "order_revision_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["local_event_premium_cap", "severe_local_MAE", "full_window_later_high"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv", "profile_path": "atlas/symbol_profiles/010/010120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.58, "MFE_90D_pct": 5.58, "MFE_180D_pct": 16.73, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -44.23, "MAE_90D_pct": -51.46, "MAE_180D_pct": -51.46, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-19", "peak_price": 303500.0, "drawdown_after_peak_pct": -51.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "local_4B_timing_too_early_full_window_order_revision_bridge_later_made_new_high", "four_b_evidence_type": ["local_event_premium", "positioning_overheat", "full_window_bridge_continued"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "local_4B_too_early_switchgear_CAPEX_full_window_recovery", "current_profile_verdict": "current_profile_local_4B_too_early_if_full_window_order_revision_bridge_continues", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R1L91_C02_010120_2024-07-24_260000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_timing_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L91_C02_HYOSUNGHEAVY_2024_TRANSFORMER_DATACENTER_CAPEX_POSITIVE", "trigger_id": "R1L91_C02_HYOSUNGHEAVY_2024_STAGE2_ACTIONABLE_TRANSFORMER_DATACENTER_CAPEX", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 30, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 55, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "transformer_datacenter_CAPEX_bridge_positive", "MFE_90D_pct": 151.99, "MAE_90D_pct": -3.39, "score_return_alignment_label": "transformer_datacenter_CAPEX_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L91_C02_GNCENERGY_2024_BACKUP_POWER_THEME_HIGH_MAE_FALSE_STAGE2", "trigger_id": "R1L91_C02_GNCENERGY_2024_STAGE2_FALSE_POSITIVE_BACKUP_POWER_THEME", "symbol": "119850", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 30, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 20, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "backup_power_theme_high_MAE_false_stage2", "MFE_90D_pct": 14.97, "MAE_90D_pct": -38.89, "score_return_alignment_label": "backup_power_theme_high_MAE_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_backup_power_theme_counts_without_order_margin_delivery_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L91_C02_LSELECTRIC_2024_SWITCHGEAR_CAPEX_LOCAL_4B_TOO_EARLY", "trigger_id": "R1L91_C02_LSELECTRIC_2024_STAGE4B_LOCAL_SWITCHGEAR_CAPEX_CAP", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 30, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 20, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage4B-local-watch/full-window-recheck", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "local_4B_too_early_full_window_recovery", "MFE_90D_pct": 5.58, "MAE_90D_pct": -51.46, "score_return_alignment_label": "local_4B_too_early_full_window_recovery", "current_profile_verdict": "current_profile_local_4B_too_early_if_full_window_order_revision_bridge_continues"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "91", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_BACKUP_POWER_AND_SWITCHGEAR_THEME_TIMING", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["transformer_datacenter_CAPEX_bridge_positive", "backup_power_theme_high_MAE_false_stage2", "local_4B_too_early_full_window_recovery"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- 4B timing rows must split local proximity from full-window proximity.
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
completed_loop = 91
next_round = R2
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
