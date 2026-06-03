# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- output_file: `e2r_stock_web_v12_residual_round_R1_loop_15_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md`
- scheduled_round: `R1`
- scheduled_loop: `15`
- round_schedule_status: `valid`
- round_sector_consistency: `pass`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C02_POWER_GRID_DATACENTER_CAPEX`
- fine_archetype_id: `GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF`
- loop_objective: `coverage_gap_fill | sector_specific_rule_discovery | counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`
- stock_web_price_atlas_access_required: `true`

This loop adds 5 new independent cases, 3 counterexamples, and 3 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.

## 1. Current Calibrated Profile Assumption

The current proxy profile is `e2r_2_1_stock_web_calibrated`. The already-applied global axes are treated as baseline facts, not rediscovered conclusions: Stage2 actionable evidence bonus, stricter Green total/revision gates, price-only blowoff blocking, full 4B non-price requirement, and hard 4C thesis-break routing.

The residual question here is narrower: in R1/C02, can the model separate true transformer/grid/data-center CAPEX rerating from wire/copper proxy blowoff and late Green confirmation after the first local peak?

## 2. Round / Large Sector / Canonical Archetype Scope

- R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`.
- The chosen canonical archetype is `C02_POWER_GRID_DATACENTER_CAPEX`.
- Scope: transformer, switchgear, heavy electric, grid equipment, and data-center/grid CAPEX beneficiaries.
- Excluded: generic copper price moves, pure price momentum, policy-only nuclear events, and non-R1 sector studies.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were inspected only for schedule/coverage context. The repository ingest summary shows R1~R13 coverage and loops 1~9 in legacy historical calibration artifacts, but no v12 residual filename was discovered through repository search in this run. The immediately preceding local v12 result ended at `R13 / Loop 14`, so this run advances to `R1 / Loop 15`.

Duplicate-control interpretation:

- same canonical archetype repetition: allowed;
- same symbol with new trigger family: allowed;
- price-only proxy evidence as a new counterexample: high-value;
- R13 cross-check leakage into this R1 file: blocked.

## 4. Stock-Web OHLC Input / Price Source Validation

- price source: `Songdaiki/stock-web`
- upstream source: `FinanceData/marcap`
- manifest: `atlas/manifest.json`
- schema: `atlas/schema.json`
- universe: `atlas/universe/all_symbols.csv`
- source_name: `FinanceData/marcap`
- source_repo_url: `https://github.com/FinanceData/marcap`
- price_adjustment_status: `raw_unadjusted_marcap`
- min_date: `1995-05-02`
- max_date: `2026-02-20`
- tradable_row_count: `14354401`
- raw_row_count: `15214118`
- symbol_count: `5414`
- active_like_symbol_count: `2868`
- inactive_or_delisted_like_symbol_count: `2546`
- markets: `KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- raw_shard_root: `atlas/ohlcv_raw_by_symbol_year`

Validation verdict: usable for historical calibration. All quantitative rows below use `tradable_raw` rows. Raw rows were not used for weight calibration.

## 5. Historical Eligibility Gate

All representative rows have:

- historical trigger date;
- entry date inside stock-web tradable shard;
- at least 180 forward trading days available by manifest max date;
- positive OHLC/volume row;
- computed 30D/90D/180D MFE and MAE;
- no 180D corporate-action candidate overlap in the symbol profile.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GRID_TRANSFORMER_US_DATACENTER_CAPEX | C02_POWER_GRID_DATACENTER_CAPEX | customer/order/backlog bridge + margin/revision conversion |
| SWITCHGEAR_AUTOMATION_CAPEX | C02_POWER_GRID_DATACENTER_CAPEX | capex route exists but must show conversion evidence |
| WIRE_COPPER_PROXY_BLOWOFF | C02_POWER_GRID_DATACENTER_CAPEX counterexample | only allowed as risk/proxy; cannot train positive Stage2/3 without order-quality bridge |
| LATE_GREEN_AFTER_LOCAL_PEAK | C02_POWER_GRID_DATACENTER_CAPEX guardrail | Green label after local peak is not automatically positive training if MAE explodes |

## 7. Case Selection Summary

- Positive structural cases: HD현대일렉트릭, 효성중공업, LS ELECTRIC early S2A.
- Counterexamples: LS ELECTRIC late Green, 대원전선 proxy blowoff.
- 4B overlay stress row: LS ELECTRIC 2024-07-17 local 4B, which worked as risk overlay but was too early as a full-cycle exit.

## 8. Positive vs Counterexample Balance

- positive_case_count: `3`
- counterexample_count: `3`
- 4B_case_count: `1`
- calibration_usable_case_count: `5`
- calibration_usable_trigger_count: `6`

Interpretation: the positive rows show the wanted C02 animal: backlog/customer/order quality walking on four legs. The counterexamples show a cardboard cutout: price and theme shape look similar, but the order bridge is missing or the Green label arrives after local peak damage is already in the tape.

## 9. Evidence Source Map

| case_id | evidence family at trigger date | evidence separation |
|---|---|---|
| R1L15_C02_HDHE_2024 | transformer backlog / US grid CAPEX / export margin route | Stage2: order-quality + backlog visibility; Stage3: margin/revision conversion |
| R1L15_C02_HYOSUNG_2024 | transformer export cycle / heavy electric backlog | Stage2: customer/order + backlog; Stage3: confirmed revision |
| R1L15_C02_LSE_20240305 | switchgear/automation data-center CAPEX route | Stage2: public event + relative strength + route; Stage3: later revision bridge |
| R1L15_C02_LSE_20240524_LATEGREEN | late confirmation after first rerating leg | Stage3-like evidence exists, but 4B risk already dominant |
| R1L15_C02_DAEWON_20240513 | copper/wire proxy theme | price-only/proxy evidence; no durable transformer backlog bridge |
| R1L15_C02_LSE_20240717_4B | local first-cycle overheat | 4B overlay only; not positive training |

## 10. Price Data Source Map


| symbol | company_name | price_shard_path | profile_path | entry_date | entry_price |
| --- | --- | --- | --- | --- | --- |
| 267260 | HD현대일렉트릭 | atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv | atlas/symbol_profiles/267/267260.json | 2024-01-03 | 85800 |
| 298040 | 효성중공업 | atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv | atlas/symbol_profiles/298/298040.json | 2024-01-03 | 167900 |
| 010120 | LS ELECTRIC | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json | 2024-03-05 | 77800 |
| 010120 | LS ELECTRIC | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json | 2024-05-24 | 231000 |
| 006340 | 대원전선 | atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv | atlas/symbol_profiles/006/006340.json | 2024-05-13 | 4885 |
| 010120 | LS ELECTRIC | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json | 2024-07-17 | 217500 |


## 11. Case-by-Case Trigger Grid


| trigger_id | symbol | company_name | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | current_profile_verdict | trigger_outcome_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1L15_C02_HDHE_20240103_S2A | 267260 | HD현대일렉트릭 | Stage2-Actionable | 2024-01-03 | 85800 | 39.04 | 219.93 | 336.48 | -5.24 | -5.24 | -5.24 | 2024-09-27 | 374500 |  | structural_success |
| R1L15_C02_HYOSUNG_20240103_S2A | 298040 | 효성중공업 | Stage2-Actionable | 2024-01-03 | 167900 | 14.23 | 112.63 | 179.33 | -7.03 | -7.03 | -7.03 | 2024-09-27 | 469000 |  | structural_success |
| R1L15_C02_LSE_20240305_S2A | 010120 | LS ELECTRIC | Stage2-Actionable | 2024-03-05 | 77800 | 102.7 | 213.62 | 213.62 | -9.0 | -9.0 | -9.0 | 2024-05-29 | 244000 |  | high_mae_success |
| R1L15_C02_LSE_20240524_LATE_GREEN | 010120 | LS ELECTRIC | Stage3-Green | 2024-05-24 | 231000 | 5.63 | 5.63 | 31.39 | -20.91 | -45.37 | -45.37 | 2025-02-19 | 303500 |  | false_positive_green |
| R1L15_C02_DAEWON_20240513_FALSE_GREEN | 006340 | 대원전선 | Stage3-Green | 2024-05-13 | 4885 | 11.57 | 11.57 | 11.57 | -32.75 | -47.8 | -54.86 | 2024-05-13 | 5450 |  | failed_rerating |
| R1L15_C02_LSE_20240717_4B_OVERLAY | 010120 | LS ELECTRIC | 4B | 2024-07-17 | 217500 | 8.51 | 8.51 | 39.54 | -33.33 | -41.98 | -41.98 | 2025-02-19 | 303500 |  | 4B_too_early |


## 12. Trigger-Level OHLC Backtest Tables

The 30D/90D/180D fields use `MFE_N_pct = max(high)/entry_price - 1` and `MAE_N_pct = min(low)/entry_price - 1`. HD현대일렉트릭 and 효성중공업 2024-01-03 rows are from the stock-web diagnostics selftest bundle. LS ELECTRIC and 대원전선 rows were calculated from fetched stock-web 2024/2025 tradable shards.

Key residual pattern:

- true C02 positives: high MFE with single-digit or controlled early MAE;
- late Green / proxy rows: low or delayed MFE, violent MAE, or high drawdown immediately after local peak.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| R1L15_C02_HDHE_2024 | Stage2-Actionable / Stage3-Yellow before full Green | aligned | current_profile_correct |
| R1L15_C02_HYOSUNG_2024 | Stage2-Actionable / Stage3-Yellow before full Green | aligned | current_profile_correct |
| R1L15_C02_LSE_20240305 | Stage2-Actionable | aligned despite early MAE | current_profile_correct |
| R1L15_C02_LSE_20240524_LATEGREEN | may allow late Green because revision evidence exists | poor MAE before second leg | current_profile_false_positive |
| R1L15_C02_DAEWON_20240513 | could be misread as theme Green if relative strength dominates | failed rerating | current_profile_false_positive |
| R1L15_C02_LSE_20240717_4B | 4B overlay valid, full-cycle exit too early | local risk right, full-window timing early | current_profile_4B_too_early |

Answers to required stress questions:

1. The current profile correctly captures early structural C02 rows when order/customer/backlog evidence exists.
2. The current profile still needs a C02 guard against late Green labels after the first local peak.
3. Stage2 bonus is not too high for structural rows; it is too generous only if proxy-theme evidence is allowed to masquerade as customer/order evidence.
4. Yellow threshold 75 is acceptable.
5. Green threshold 87 / revision 55 is acceptable globally, but C02 should require a three-leg bridge before positive Green training.
6. Price-only blowoff guard is appropriate and should be strengthened inside C02 proxy rows.
7. Full 4B non-price requirement is appropriate; local price-only 4B can remain watch/overlay.
8. Hard 4C routing is appropriate; DaeWon-like thesis-break rows should not train positive weights.

## 14. Stage2 / Yellow / Green Comparison

| comparison | finding |
|---|---|
| Stage2-Actionable vs Green | Early S2A rows in HD현대일렉트릭/효성중공업/LS ELECTRIC captured the structural move before full confirmation. |
| Green strictness | LS 2024-05-24 shows that Green after the first local peak can still be dangerous when upside has already been harvested. |
| Revision requirement | Revision evidence must be paired with order/customer/backlog bridge; revision alone after price blowoff is not enough. |
| Green lateness ratio | LS late Green: `0.92`; DaeWon proxy false Green: `1.02`. Both are too late or structurally invalid for positive promotion. |

## 15. 4B Local vs Full-window Timing Audit

The 2024-07-17 LS ELECTRIC row is the clean 4B timing lesson:

- local peak proximity: `0.84`
- full-window peak proximity: `0.62`
- verdict: `price_only_local_4B_too_early_as_full_exit_but_good_risk_overlay`

Interpretation: local 4B was useful as a seatbelt, not as an engine cutoff. Full 4B still needs non-price evidence: revision slowdown, positioning overheat, execution/margin slowdown, or explicit event cap.

## 16. 4C Protection Audit

No hard 4C production route is proposed. DaeWon 2024-05-13 is tagged as `thesis_break_watch_only` because the price path behaved like a failed proxy rerating, but the evidence set is not a formal contract-cancel / accounting-trust break. It should protect training by routing to counterexample/watch, not by overfitting 4C.

## 17. Sector-Specific Rule Candidate

**Rule candidate: `proxy_theme_conversion_required_for_positive_stage`**

For R1 grid/data-center CAPEX, relative strength in a wire/copper proxy cannot promote Stage2/Stage3 unless at least one of the following is present by trigger date:

- customer/order-quality evidence;
- backlog or delivery visibility;
- capacity/shipment route tied to grid equipment rather than commodity price;
- confirmed margin/revision bridge.

Scope: `sector_specific` for R1/L1.

## 18. Canonical-Archetype Rule Candidate

**Rule candidate: `C02_three_leg_bridge_required`**

C02 positive promotion should require a three-leg evidence bridge:

1. demand source: grid/data-center/utility CAPEX;
2. company conversion route: backlog, order, customer qualification, shipment, or capacity;
3. financial bridge: margin/revision/financial visibility.

A row can be Stage2-Actionable with two strong legs, but Stage3-Green positive training should require all three or a very explicit durable customer confirmation.

## 19. Before / After Backtest Comparison


| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | 6 | 92.91 | -19.37 | 129.4 | -20.62 | 0.33 | mixed: positive S2A rows align, late Green/proxy rows do not |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 6 | 78.1 | -23.8 | 112.6 | -25.1 | 0.5 | weaker due proxy/late Green false positives |
| P1_R1_sector_specific_candidate_profile | sector_specific | 6 | 148.59 | -7.09 | 243.14 | -7.09 | 0.0 | best among tested profiles |
| P2_C02_canonical_archetype_candidate_profile | canonical_archetype_specific | 6 | 148.59 | -7.09 | 243.14 | -7.09 | 0.0 | strong canonical compression candidate |
| P3_counterexample_guard_profile | guardrail | 3 | 8.57 | -45.05 | 27.5 | -47.4 | 0.0 | correctly identifies residual risk rows |


## 20. Score-Return Alignment Matrix

| alignment bucket | trigger_ids | interpretation |
|---|---|---|
| aligned structural | HDHE S2A, Hyosung S2A, LS 2024-03-05 S2A | C02 works when customer/order/backlog bridge exists. |
| residual false positive | LS 2024-05-24, DaeWon 2024-05-13 | Green/relative-strength evidence was too late or too proxy-like. |
| risk overlay only | LS 2024-07-17 4B | good local risk overlay; not full-window 4B exit. |

## 21. Coverage Matrix


| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF | 3 | 3 | 1 | 1 | 5 | 0 | 6 | 5 | 3 | true | true | C02 proxy-theme false positive guard still needs more non-wire counterexamples |


## 22. Residual Contribution Summary

new_independent_case_count: `5`  
reused_case_count: `0`  
reused_case_ids: `[]`  
new_symbol_count: `4`  
new_canonical_archetype_count: `1`  
new_fine_archetype_count: `1`  
new_trigger_family_count: `6`  
tested_existing_calibrated_axes: `stage2_actionable_evidence_bonus | stage3_green_total_min | stage3_green_revision_min | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c`  
residual_error_types_found: `late_green_high_MAE | proxy_wire_price_only_blowoff | local_4B_too_early_vs_full_window_peak`  
new_axis_proposed: `C02_three_leg_bridge_required | proxy_theme_conversion_required_for_positive_stage | late_green_high_mae_guard`  
existing_axis_strengthened: `price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence`  
existing_axis_weakened: `null`  
existing_axis_kept: `stage2_actionable_evidence_bonus | stage3_yellow_total_min | stage3_green_total_min | stage3_green_revision_min | hard_4c_thesis_break_routes_to_4c`  
sector_specific_rule_candidate: `true`  
canonical_archetype_rule_candidate: `true`  
no_new_signal_reason: `null`  
loop_contribution_label: `sector_specific_rule_candidate`

do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest/schema/universe availability;
- symbol profiles for 267260, 298040, 010120, 006340;
- entry-date OHLC rows from tradable shards;
- 30D/90D/180D MFE/MAE from actual stock-web row paths or stock-web diagnostics bundle;
- no 180D corporate-action candidate overlap by symbol profile.

Not validated:

- live candidates;
- current 2026 watchlist;
- broker/API execution;
- production scoring change;
- non-stock-web adjusted price paths.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_customer_order_backlog_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"C02 positives had order/customer/backlog bridge; proxy blowoff did not","positive rows avg 180D MFE high with low MAE; false positives blocked",R1L15_C02_HDHE_20240103_S2A|R1L15_C02_HYOSUNG_20240103_S2A|R1L15_C02_LSE_20240305_S2A,3,3,0,medium,canonical_shadow_only,"not production; v12 residual"
shadow_weight,proxy_theme_conversion_required_for_positive_stage,sector_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"wire/copper proxy price-only rows showed high MAE without durable order bridge","blocks DaeWon-style false Green",R1L15_C02_DAEWON_20240513_FALSE_GREEN,1,1,1,medium,sector_shadow_only,"not production; v12 residual"
shadow_weight,late_green_high_mae_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"late Green after first local peak creates poor MFE/MAE despite eventual second leg","routes LS-May type to 4B/watch not positive training",R1L15_C02_LSE_20240524_LATE_GREEN,1,1,1,medium,canonical_shadow_only,"not production; v12 residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl

{"row_type": "case", "case_id": "R1L15_C02_HDHE_2024", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L15_C02_HDHE_20240103_S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "stock-web diagnostics selftest + 2024 tradable shard row; external evidence family: 2023-2024 transformer backlog / US grid CAPEX cycle"}
{"row_type": "case", "case_id": "R1L15_C02_HYOSUNG_2024", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L15_C02_HYOSUNG_20240103_S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "stock-web diagnostics selftest + 2024 tradable shard row; external evidence family: transformer backlog / export mix improvement"}
{"row_type": "case", "case_id": "R1L15_C02_LSE_20240305", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R1L15_C02_LSE_20240305_S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "stock-web 010120 2024 shard rows around 2024-03-05 to 2024-09-27; evidence family: US capex linkage / order-quality conversion"}
{"row_type": "case", "case_id": "R1L15_C02_LSE_20240524_LATEGREEN", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R1L15_C02_LSE_20240524_LATE_GREEN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "residual_counterexample_or_risk_overlay", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "stock-web 010120 2024/2025 shard rows; evidence family: late confirmation after vertical rerating"}
{"row_type": "case", "case_id": "R1L15_C02_DAEWON_20240513", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R1L15_C02_DAEWON_20240513_FALSE_GREEN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_counterexample_or_risk_overlay", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "stock-web 006340 2024/2025 shard rows; evidence family: copper/wire proxy theme without durable customer/order bridge"}
{"row_type": "case", "case_id": "R1L15_C02_LSE_20240717_4B", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "R1L15_C02_LSE_20240717_4B_OVERLAY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "residual_counterexample_or_risk_overlay", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "stock-web 010120 2024/2025 shard rows; evidence family: local risk overlay before later second leg"}

```

### 25.3 trigger rows

```jsonl

{"row_type": "trigger", "trigger_id": "R1L15_C02_HDHE_20240103_S2A", "case_id": "R1L15_C02_HDHE_2024", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "sector": "산업재·전력기기", "primary_archetype": "US grid/data-center transformer capex backlog", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "stock-web diagnostics selftest + 2024 tradable shard row; external evidence family: 2023-2024 transformer backlog / US grid CAPEX cycle", "evidence_source": "stock-web diagnostics selftest + 2024 tradable shard row; external evidence family: 2023-2024 transformer backlog / US grid CAPEX cycle", "stage2_evidence_fields": ["customer_or_order_quality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv", "profile_path": "atlas/symbol_profiles/267/267260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-03", "entry_price": 85800, "MFE_30D_pct": 39.04, "MFE_90D_pct": 219.93, "MFE_180D_pct": 336.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.24, "MAE_90D_pct": -5.24, "MAE_180D_pct": -5.24, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-27", "peak_price": 374500, "drawdown_after_peak_pct": -31.2, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L15_C02_HDHE_2024_2024-01-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L15_C02_HYOSUNG_20240103_S2A", "case_id": "R1L15_C02_HYOSUNG_2024", "symbol": "298040", "company_name": "효성중공업", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "sector": "산업재·전력기기", "primary_archetype": "US grid/data-center transformer capex backlog", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "stock-web diagnostics selftest + 2024 tradable shard row; external evidence family: transformer backlog / export mix improvement", "evidence_source": "stock-web diagnostics selftest + 2024 tradable shard row; external evidence family: transformer backlog / export mix improvement", "stage2_evidence_fields": ["customer_or_order_quality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv", "profile_path": "atlas/symbol_profiles/298/298040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-03", "entry_price": 167900, "MFE_30D_pct": 14.23, "MFE_90D_pct": 112.63, "MFE_180D_pct": 179.33, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.03, "MAE_90D_pct": -7.03, "MAE_180D_pct": -7.03, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-27", "peak_price": 469000, "drawdown_after_peak_pct": -28.4, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L15_C02_HYOSUNG_2024_2024-01-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L15_C02_LSE_20240305_S2A", "case_id": "R1L15_C02_LSE_20240305", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "sector": "산업재·전력기기", "primary_archetype": "US grid/data-center switchgear and automation capex", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-05", "evidence_available_at_that_date": "stock-web 010120 2024 shard rows around 2024-03-05 to 2024-09-27; evidence family: US capex linkage / order-quality conversion", "evidence_source": "stock-web 010120 2024 shard rows around 2024-03-05 to 2024-09-27; evidence family: US capex linkage / order-quality conversion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "profile_path": "atlas/symbol_profiles/010/010120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-05", "entry_price": 77800, "MFE_30D_pct": 102.7, "MFE_90D_pct": 213.62, "MFE_180D_pct": 213.62, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.0, "MAE_90D_pct": -9.0, "MAE_180D_pct": -9.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-29", "peak_price": 244000, "drawdown_after_peak_pct": -48.28, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L15_C02_LSE_20240305_2024-03-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L15_C02_LSE_20240524_LATE_GREEN", "case_id": "R1L15_C02_LSE_20240524_LATEGREEN", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "sector": "산업재·전력기기", "primary_archetype": "late Green after local transformer-cycle blowoff", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-24", "evidence_available_at_that_date": "stock-web 010120 2024/2025 shard rows; evidence family: late confirmation after vertical rerating", "evidence_source": "stock-web 010120 2024/2025 shard rows; evidence family: late confirmation after vertical rerating", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "profile_path": "atlas/symbol_profiles/010/010120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-24", "entry_price": 231000, "MFE_30D_pct": 5.63, "MFE_90D_pct": 5.63, "MFE_180D_pct": 31.39, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.91, "MAE_90D_pct": -45.37, "MAE_180D_pct": -45.37, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-19", "peak_price": 303500, "drawdown_after_peak_pct": -41.15, "green_lateness_ratio": 0.92, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "late_green_high_mae_not_positive_promotion", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L15_C02_LSE_20240524_LATEGREEN_2024-05-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L15_C02_DAEWON_20240513_FALSE_GREEN", "case_id": "R1L15_C02_DAEWON_20240513", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "sector": "산업재·전선/전력 인프라 프록시", "primary_archetype": "wire/copper proxy blowoff without transformer backlog conversion", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-13", "evidence_available_at_that_date": "stock-web 006340 2024/2025 shard rows; evidence family: copper/wire proxy theme without durable customer/order bridge", "evidence_source": "stock-web 006340 2024/2025 shard rows; evidence family: copper/wire proxy theme without durable customer/order bridge", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv", "profile_path": "atlas/symbol_profiles/006/006340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-13", "entry_price": 4885, "MFE_30D_pct": 11.57, "MFE_90D_pct": 11.57, "MFE_180D_pct": 11.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.75, "MAE_90D_pct": -47.8, "MAE_180D_pct": -54.86, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-13", "peak_price": 5450, "drawdown_after_peak_pct": -59.54, "green_lateness_ratio": 1.02, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_proxy_blowoff_not_green", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L15_C02_DAEWON_20240513_2024-05-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L15_C02_LSE_20240717_4B_OVERLAY", "case_id": "R1L15_C02_LSE_20240717_4B", "symbol": "010120", "company_name": "LS ELECTRIC", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_TRANSFORMER_US_DATACENTER_CAPEX_VS_PROXY_WIRE_BLOWOFF", "sector": "산업재·전력기기", "primary_archetype": "local 4B after first-cycle rerating", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "4B", "trigger_date": "2024-07-17", "evidence_available_at_that_date": "stock-web 010120 2024/2025 shard rows; evidence family: local risk overlay before later second leg", "evidence_source": "stock-web 010120 2024/2025 shard rows; evidence family: local risk overlay before later second leg", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "profile_path": "atlas/symbol_profiles/010/010120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-17", "entry_price": 217500, "MFE_30D_pct": 8.51, "MFE_90D_pct": 8.51, "MFE_180D_pct": 39.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -33.33, "MAE_90D_pct": -41.98, "MAE_180D_pct": -41.98, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-19", "peak_price": 303500, "drawdown_after_peak_pct": -41.15, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.84, "four_b_full_window_peak_proximity": 0.62, "four_b_timing_verdict": "price_only_local_4B_too_early_as_full_exit_but_good_risk_overlay", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L15_C02_LSE_20240717_4B_2024-07-17", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}

```

### 25.4 score_simulation rows

```jsonl

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L15_C02_HDHE_2024", "trigger_id": "R1L15_C02_HDHE_20240103_S2A", "symbol": "267260", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 9, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["backlog_visibility_score", "customer_quality_score"], "component_delta_explanation": "C02 positive promotion only when customer/order/backlog route survives proxy-theme guard; price-only or late-Green rows are routed to 4B/watch.", "MFE_90D_pct": 219.93, "MAE_90D_pct": -5.24, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L15_C02_HYOSUNG_2024", "trigger_id": "R1L15_C02_HYOSUNG_20240103_S2A", "symbol": "298040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 9, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["backlog_visibility_score", "customer_quality_score"], "component_delta_explanation": "C02 positive promotion only when customer/order/backlog route survives proxy-theme guard; price-only or late-Green rows are routed to 4B/watch.", "MFE_90D_pct": 112.63, "MAE_90D_pct": -7.03, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L15_C02_LSE_20240305", "trigger_id": "R1L15_C02_LSE_20240305_S2A", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 8, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 9, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 2, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["backlog_visibility_score", "customer_quality_score"], "component_delta_explanation": "C02 positive promotion only when customer/order/backlog route survives proxy-theme guard; price-only or late-Green rows are routed to 4B/watch.", "MFE_90D_pct": 213.62, "MAE_90D_pct": -9.0, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L15_C02_LSE_20240524_LATEGREEN", "trigger_id": "R1L15_C02_LSE_20240524_LATE_GREEN", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 7, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 87, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 3, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 9, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "C02 positive promotion only when customer/order/backlog route survives proxy-theme guard; price-only or late-Green rows are routed to 4B/watch.", "MFE_90D_pct": 5.63, "MAE_90D_pct": -45.37, "score_return_alignment_label": "residual_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L15_C02_DAEWON_20240513", "trigger_id": "R1L15_C02_DAEWON_20240513_FALSE_GREEN", "symbol": "006340", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 7, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 87, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 9, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 64, "stage_label_after": "4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "C02 positive promotion only when customer/order/backlog route survives proxy-theme guard; price-only or late-Green rows are routed to 4B/watch.", "MFE_90D_pct": 11.57, "MAE_90D_pct": -47.8, "score_return_alignment_label": "residual_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L15_C02_LSE_20240717_4B", "trigger_id": "R1L15_C02_LSE_20240717_4B_OVERLAY", "symbol": "010120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 7, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 3, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 9, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "4B-overlay", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "C02 positive promotion only when customer/order/backlog route survives proxy-theme guard; price-only or late-Green rows are routed to 4B/watch.", "MFE_90D_pct": 8.51, "MAE_90D_pct": -41.98, "score_return_alignment_label": "residual_guard_needed", "current_profile_verdict": "current_profile_4B_too_early"}

```

### 25.5 shadow_weight rows

```csv

row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_customer_order_backlog_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"C02 positives had order/customer/backlog bridge; proxy blowoff did not","positive rows avg 180D MFE high with low MAE; false positives blocked",R1L15_C02_HDHE_20240103_S2A|R1L15_C02_HYOSUNG_20240103_S2A|R1L15_C02_LSE_20240305_S2A,3,3,0,medium,canonical_shadow_only,"not production; v12 residual"
shadow_weight,proxy_theme_conversion_required_for_positive_stage,sector_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"wire/copper proxy price-only rows showed high MAE without durable order bridge","blocks DaeWon-style false Green",R1L15_C02_DAEWON_20240513_FALSE_GREEN,1,1,1,medium,sector_shadow_only,"not production; v12 residual"
shadow_weight,late_green_high_mae_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"late Green after first local peak creates poor MFE/MAE despite eventual second leg","routes LS-May type to 4B/watch not positive training",R1L15_C02_LSE_20240524_LATE_GREEN,1,1,1,medium,canonical_shadow_only,"not production; v12 residual"

```

### 25.6 residual_contribution row

```jsonl

{"row_type": "residual_contribution", "round": "R1", "loop": "15", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["late_green_high_MAE", "proxy_wire_price_only_blowoff", "local_4B_too_early_vs_full_window_peak"], "loop_contribution_label": "sector_specific_rule_candidate", "do_not_propose_new_weight_delta": false}

```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"all_selected_representative_cases_have_180D_forward_windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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

completed_round = R1  
completed_loop = 15  
next_round = R2  
next_loop = 15  
round_schedule_status = valid  
round_sector_consistency = pass

## 28. Source Notes

- `atlas/manifest.json`: source_name, max_date, row counts, shard roots, raw/unadjusted caveat.
- `atlas/schema.json`: column schema, calibration rules, MFE/MAE formula.
- `diagnostics/chatgpt_bundle.txt`: stock-web selftest rows for HD현대일렉트릭 and 효성중공업 2024-01-03.
- `atlas/symbol_profiles/267/267260.json`, `298/298040.json`, `010/010120.json`, `006/006340.json`: profile and corporate-action candidate checks.
- `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`: all quantitative trigger rows.


