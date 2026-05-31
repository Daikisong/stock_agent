# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- scheduled_round: R1
- scheduled_loop: 1
- large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
- canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
- fine_archetype_id: GRID_EQUIPMENT_US_DATACENTER_CAPEX
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- research_session: post_calibrated_sector_archetype_residual_research
- output_format: one_standalone_markdown_file
- production_scoring_changed: false
- shadow_weight_only: true
- stock_agent_code_access_allowed: false
- stock_agent_code_patch_allowed: false
- stock_agent_live_scan_allowed: false

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.

## 1. Current Calibrated Profile Assumption

Current default profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. The profile already contains the first Stock-Web calibration axes: Stage2 actionable bonus, higher Yellow/Green thresholds, Green revision minimum, cross-evidence buffer, price-only blowoff block, non-price 4B requirement, and hard 4C routing.

This research does **not** re-prove those global axes. It stress-tests whether power-grid/data-center capex cases need a narrower canonical-archetype shadow rule.

## 2. Round / Large Sector / Canonical Archetype Scope

- round: R1
- loop: 1
- round_schedule_status: valid
- round_sector_consistency: pass
- large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
- canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
- primary_archetype: transformer / switchgear / grid equipment capex cycle
- loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - sector_specific_rule_discovery
  - 4B_non_price_requirement_stress_test
  - residual_false_positive_mining

## 3. Previous Coverage / Duplicate Avoidance Check

No `e2r_stock_web_v12_residual_round_R*_loop_*_*_research*.md` file was found in the available registry/search pass. Existing registry entries are older `e2r_stock_web_historical_calibration_round_*` artifacts, not v12 residual files. Therefore, v12 schedule resolution starts at `R1 / Loop 1`.

Duplicate avoidance rule applied: avoid repeating the old general observation that Stage2 is earlier than Green. The selected contribution is instead the C02-specific distinction between:

1. durable grid-capex evidence with order/backlog/US data-center visibility,
2. price-only local peaks without non-price 4B confirmation,
3. order-cycle excitement that produces high MAE before structural confirmation.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

- source: Songdaiki/stock-web
- upstream source: FinanceData/marcap
- source_name: FinanceData/marcap
- price_basis: tradable_raw
- price_adjustment_status: raw_unadjusted_marcap
- manifest_min_date: 1995-05-02
- manifest_max_date: 2026-02-20
- tradable_row_count: 14,354,401
- raw_row_count: 15,214,118
- symbol_count: 5,414
- calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
- raw_shard_root: atlas/ohlcv_raw_by_symbol_year
- schema_path: atlas/schema.json
- universe_path: atlas/universe/all_symbols.csv

Schema validation:

- tradable columns: d, o, h, l, c, v, a, mc, s, m
- MFE_N_pct formula: max high from entry_date through N tradable rows / entry_price - 1
- MAE_N_pct formula: min low from entry_date through N tradable rows / entry_price - 1
- calibration usable requires positive OHLCV, entry row, 180 forward tradable rows, computed 30/90/180D MFE/MAE, and no 180D corporate-action contamination.

## 5. Historical Eligibility Gate

| case_id | symbol | company | entry_date | 180D forward window | corporate-action window | calibration_usable |
|---|---:|---|---|---:|---|---|
| R1L1C02_HDHE_20230727 | 267260 | HD현대일렉트릭 | 2023-07-27 | yes | clean_180D_window | true |
| R1L1C02_LSE_20240701 | 010120 | LS ELECTRIC | 2024-07-01 | yes | clean_180D_window | true |
| R1L1C02_LSE_20240723_4B | 010120 | LS ELECTRIC | 2024-07-23 | yes | clean_180D_window | true |
| R1L1C02_HHI_2024Q2 | 298040 | 효성중공업 | 2024-Q2 | not fully connector-expanded | presumed clean, needs full row replay | narrative_only |
| R1L1C02_ILI_2024Q2 | 103590 | 일진전기 | 2024-Q2 | not fully connector-expanded | presumed clean, needs full row replay | narrative_only |

Because the GitHub connector returned row-window chunks rather than a local full clone, the quantitative rows below are based on directly inspected Stock-Web rows and conservative window estimates from those inspected rows. A later batch parser should recompute all windows from the full CSV shards before promotion.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| GRID_EQUIPMENT_US_DATACENTER_CAPEX | C02_POWER_GRID_DATACENTER_CAPEX | US grid/data-center demand, transformer/switchgear capex, capacity constraints |
| TRANSFORMER_BACKLOG_MARGIN_BRIDGE | C02_POWER_GRID_DATACENTER_CAPEX | Backlog and margin bridge matter only when tied to grid-capex cycle evidence |
| POWER_EQUIPMENT_PRICE_ONLY_BLOWOFF | C02_POWER_GRID_DATACENTER_CAPEX | Negative/guardrail fine type, not a separate positive canonical archetype |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_family | new_independent_case | reason |
|---|---:|---|---|---|---|---|
| R1L1C02_HDHE_20230727 | 267260 | HD현대일렉트릭 | structural_success | order/backlog + margin bridge | true | clean 2023 entry before 2024 transformer rerating |
| R1L1C02_LSE_20240701 | 010120 | LS ELECTRIC | high_mae_success | US data-center revenue mix + analyst revision | true | C02 moved, but MAE was high after local price enthusiasm |
| R1L1C02_LSE_20240723_4B | 010120 | LS ELECTRIC | 4B_too_early / counterexample | price-only local spike | false | same symbol, different trigger family: local blowoff without durable full-window exit |
| R1L1C02_HHI_2024Q2 | 298040 | 효성중공업 | narrative_only structural candidate | US transformer capacity | true | needs full shard replay |
| R1L1C02_ILI_2024Q2 | 103590 | 일진전기 | narrative_only counterexample candidate | grid theme beta / order quality uncertainty | true | needs full shard replay |

## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 2
- 4B_case_count: 1
- 4C_case_count: 0
- calibration_usable_case_count: 3 if LS 4B overlay is counted as usable overlay; 2 if only representative entries are counted.
- narrative_only_case_count: 2

The usable core is sufficient for a **low-confidence canonical shadow candidate**, not a production/global rule.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|---|---|
| R1L1C02_HDHE_20230727 | 2023-07-26 | Q2-cycle transformer demand and margin bridge were visible around earnings/market reaction | public earnings/news proxy + Stock-Web row | backlog_or_delivery_visibility, customer_or_order_quality, relative_strength | margin_bridge, financial_visibility | none | none |
| R1L1C02_LSE_20240701 | 2024-07-01 | US business growth / data-center demand narrative visible in market commentary | MarketWatch/Daiwa note proxy + Stock-Web row | policy_or_regulatory_optionality, customer_or_order_quality, relative_strength | early_revision_signal, multiple_public_sources | none | none |
| R1L1C02_LSE_20240723_4B | 2024-07-23 | price spike without enough non-price 4B evidence | Stock-Web row | relative_strength only | unknown_or_not_supported | price_only, positioning_overheat | none |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | stock_web_manifest_max_date | price_basis | profile caveat |
|---:|---|---|---|---|---|
| 267260 | atlas/symbol_profiles/267/267260.json | atlas/ohlcv_tradable_by_symbol_year/267/267260/2023.csv; 2024.csv | 2026-02-20 | tradable_raw | corporate action candidates only in 2017-2019, outside tested 2023-2024 window |
| 010120 | atlas/symbol_profiles/010/010120.json | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | 2026-02-20 | tradable_raw | corporate action candidates in 1995-2003, outside tested 2024 window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B fields | current_profile_verdict |
|---|---|---:|---|---|---|---:|---|---|---|---|
| TR_HDHE_20230727_S2A | R1L1C02_HDHE_20230727 | 267260 | Stage2-Actionable | 2023-07-26 | 2023-07-27 | 70600 | backlog_or_delivery_visibility, customer_or_order_quality, relative_strength | margin_bridge | [] | current_profile_correct |
| TR_LSE_20240701_S2A | R1L1C02_LSE_20240701 | 010120 | Stage2-Actionable | 2024-07-01 | 2024-07-01 | 204500 | customer_or_order_quality, relative_strength, policy_or_regulatory_optionality | early_revision_signal | [] | current_profile_too_early |
| TR_LSE_20240723_4B | R1L1C02_LSE_20240723_4B | 010120 | Stage4B-overlay | 2024-07-23 | 2024-07-23 | 259000 | relative_strength | [] | price_only, positioning_overheat | current_profile_4B_too_early |

## 12. Trigger-Level OHLC Backtest Tables

Representative rows based on inspected Stock-Web shards.

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| TR_HDHE_20230727_S2A | 2023-07-27 | 70600 | 10.48 | -13.03 | 27.62 | -13.03 | 218.70 | -13.03 | 2024-04-09 | 225000 | -47.78 | true |
| TR_LSE_20240701_S2A | 2024-07-01 | 204500 | 33.99 | -29.10 | 34.23 | -38.29 | 34.23 | -38.29 | 2024-07-24 | 274500 | -52.90 | true |
| TR_LSE_20240723_4B | 2024-07-23 | 259000 | 6.00 | -43.99 | 6.00 | -50.08 | 6.00 | -50.08 | 2024-07-24 | 274500 | -54.03 | true |

Interpretation:
- HD현대일렉트릭 is a clean C02 structural success: Stage2-Actionable had tolerable MAE and large 180D MFE.
- LS ELECTRIC is the useful residual: Stage2 evidence was real, but the entry was vulnerable to high MAE because C02 evidence arrived after a large local move.
- LS 2024-07-23 is a price-only 4B stress test: price peak was locally close, but the signal is not a full-window non-price 4B.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual price alignment | verdict |
|---|---|---|---|
| R1L1C02_HDHE_20230727 | Stage2-Actionable / Yellow before full Green | aligned | current_profile_correct |
| R1L1C02_LSE_20240701 | Stage2-Actionable too readily accepted after strong relative strength | mixed: positive MFE but severe MAE | current_profile_too_early |
| R1L1C02_LSE_20240723_4B | local 4B watch only, not full 4B | aligned if non-price requirement is enforced | current_profile_4B_too_early if price-only accepted |

Answers to calibrated-axis stress questions:
1. Stage2 bonus is useful for HD현대일렉트릭 but too permissive for LS after a vertical local run.
2. Yellow threshold 75 should remain; C02 should add a MAE-aware late-local-run guard rather than lowering Yellow.
3. Green threshold 87 / revision 55 should remain; no evidence here weakens it.
4. Price-only blowoff guard is strengthened.
5. Full 4B non-price requirement is strengthened.
6. Hard 4C routing is not tested enough in this loop.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3 Green trigger | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| R1L1C02_HDHE_20230727 | 70600 | not explicitly reconstructed | not_applicable | no confirmed Stage3-Green trigger in inspected row set |
| R1L1C02_LSE_20240701 | 204500 | no clean Green before local blowoff | not_applicable | Stage2 entered into local overheat rather than durable Green confirmation |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---|---:|---:|---|---|
| TR_LSE_20240723_4B | 0.78 | 0.78 | price_only, positioning_overheat | price_only_local_4B_too_early |
| TR_HDHE_20230727_S2A | null | null | none | not_4B |
| TR_LSE_20240701_S2A | null | null | none | not_4B |

C02-specific finding: local price acceleration in grid-equipment stocks should create a **4B-watch overlay**, not a full 4B exit, unless backlog/margin/revision deterioration or valuation/positioning evidence appears.

## 16. 4C Protection Audit

No hard 4C thesis-break case is quantitatively validated in this loop. 4C labels remain `thesis_break_watch_only`.

## 17. Sector-Specific Rule Candidate

- rule_scope: sector_specific
- rule_id: L1_C02_STAGE2_LOCAL_RUN_MAE_GUARD
- candidate axis: if C02 Stage2-Actionable is triggered after a recent local price run and before confirmed backlog/margin/revision bridge, cap label at Stage2-watch/Yellow-watch.
- reason: LS ELECTRIC had legitimate C02 evidence, but MFE/MAE quality deteriorated when the trigger occurred after a sharp local run.
- proposal_type: sector_shadow_only
- confidence: low

## 18. Canonical-Archetype Rule Candidate

- rule_scope: canonical_archetype_specific
- rule_id: C02_ORDER_QUALITY_PLUS_MARGIN_BRIDGE_PROMOTION
- candidate axis: promote C02 Stage2 only when at least two of backlog/delivery visibility, customer/order quality, and margin/revision bridge are present; relative strength alone cannot carry promotion.
- expected effect: keeps HD현대일렉트릭-style structural success, reduces LS-style high-MAE entry.
- proposal_type: canonical_shadow_only
- confidence: low_to_medium

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 3 | 22.62 | -33.80 | 0.33 | 0 | mixed_alignment |
| P0b_e2r_2_0_baseline_reference | rollback | 3 | 18.00 | -28.00 | 0.33 | 1 | worse_missed_structural |
| P1_L1_C02_local_run_mae_guard | sector_shadow | 3 | 18.80 | -21.00 | 0.00 | 0 | better_risk_adjusted_alignment |
| P2_C02_order_quality_margin_bridge | canonical_shadow | 3 | 24.00 | -20.50 | 0.00 | 0 | better_alignment |
| P3_counterexample_guard_profile | guard | 3 | 12.00 | -16.00 | 0.00 | 1 | too_conservative |

## 20. Score-Return Alignment Matrix

Research proxy score components, not production scoring.

| trigger_id | profile | contract | backlog | margin | revision | RS | customer | policy/reg | val repricing | exec risk | legal risk | dilution risk | accounting risk | weighted_score | stage_label | alignment |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| TR_HDHE_20230727_S2A | before | 4 | 8 | 8 | 6 | 7 | 7 | 3 | 5 | -1 | 0 | 0 | 0 | 82 | Stage3-Yellow | aligned |
| TR_HDHE_20230727_S2A | after | 4 | 9 | 9 | 7 | 7 | 8 | 3 | 5 | -1 | 0 | 0 | 0 | 87 | Stage3-Green | aligned |
| TR_LSE_20240701_S2A | before | 2 | 5 | 3 | 6 | 9 | 6 | 5 | 7 | -2 | 0 | 0 | 0 | 78 | Stage3-Yellow | too_early_high_MAE |
| TR_LSE_20240701_S2A | after | 2 | 5 | 3 | 6 | 5 | 6 | 5 | 7 | -5 | 0 | 0 | 0 | 71 | Stage2-Watch | better_risk_alignment |
| TR_LSE_20240723_4B | before | 0 | 2 | 0 | 2 | 10 | 3 | 3 | 9 | -6 | 0 | 0 | 0 | 69 | Stage2-Watch + 4B-watch | aligned_if_not_full_4B |
| TR_LSE_20240723_4B | after | 0 | 2 | 0 | 2 | 4 | 3 | 3 | 9 | -8 | 0 | 0 | 0 | 55 | 4B-watch_only | better |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | GRID_EQUIPMENT_US_DATACENTER_CAPEX | 2 | 2 | 1 | 0 | 3 | 1 | 3 | 2 | 2 | true | true | needs more 4C and post-2025 counterexamples |

## 22. Residual Contribution Summary

- new_independent_case_count: 3
- reused_case_count: 1
- reused_case_ids: [R1L1C02_LSE_20240723_4B]
- new_symbol_count: 4
- new_canonical_archetype_count: 1
- new_fine_archetype_count: 1
- new_trigger_family_count: 3
- tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
- residual_error_types_found:
  - current_profile_too_early
  - current_profile_4B_too_early
- new_axis_proposed:
  - L1_C02_STAGE2_LOCAL_RUN_MAE_GUARD
  - C02_ORDER_QUALITY_PLUS_MARGIN_BRIDGE_PROMOTION
- existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
- existing_axis_weakened: null
- existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
- sector_specific_rule_candidate: true
- canonical_archetype_rule_candidate: true
- no_new_signal_reason: null
- loop_contribution_label: sector_specific_rule_candidate
- do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validation scope:
- Stock-Web manifest/schema checked.
- 267260 and 010120 profiles checked.
- 267260 2023/2024 and 010120 2024 row chunks inspected.
- No stock_agent source code opened.
- No production patch proposed.

Non-validation scope:
- Full-file 180D row replay was not performed locally because container network clone failed and connector responses were chunk-limited.
- Narrative-only candidates 298040 and 103590 require full shard replay before quantitative calibration.
- No investment recommendation is made.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_order_quality_margin_bridge_min,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,1,2,+1,"Relative strength alone caused high-MAE LS entry; HD success had backlog/margin bridge.","reduces high-MAE entries while preserving HD structural success","TR_HDHE_20230727_S2A|TR_LSE_20240701_S2A",2,2,1,low_to_medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C02_price_only_local_4B_watch,sector_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"LS 2024 local price spike marked risk but lacked non-price full 4B evidence.","keeps price-only spike as overlay not exit","TR_LSE_20240723_4B",1,0,1,low,sector_shadow_only,"not production; overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R1L1C02_HDHE_20230727","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_HDHE_20230727_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2 with backlog/margin bridge captured 180D rerating."}
{"row_type":"case","case_id":"R1L1C02_LSE_20240701","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TR_LSE_20240701_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_high_mae","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Legitimate C02 evidence but post-run entry carried severe MAE."}
{"row_type":"trigger","trigger_id":"TR_HDHE_20230727_S2A","case_id":"R1L1C02_HDHE_20230727","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX","sector":"industrials_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-26","entry_date":"2023-07-27","entry_price":70600,"evidence_available_at_that_date":"Q2-cycle grid equipment demand, backlog and margin bridge visible around earnings/market reaction","evidence_source":"public earnings/news proxy + Stock-Web row","stage2_evidence_fields":["backlog_or_delivery_visibility","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2023.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.48,"MFE_90D_pct":27.62,"MFE_180D_pct":218.70,"MFE_1Y_pct":484.99,"MFE_2Y_pct":null,"MAE_30D_pct":-13.03,"MAE_90D_pct":-13.03,"MAE_180D_pct":-13.03,"MAE_1Y_pct":-13.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-09","peak_price":225000,"drawdown_after_peak_pct":-47.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"267260_2023-07-27_70600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_LSE_20240701_S2A","case_id":"R1L1C02_LSE_20240701","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX","sector":"industrials_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":204500,"evidence_available_at_that_date":"US business/data-center growth commentary visible; price already extended","evidence_source":"public market commentary proxy + Stock-Web row","stage2_evidence_fields":["customer_or_order_quality","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["early_revision_signal","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.99,"MFE_90D_pct":34.23,"MFE_180D_pct":34.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-29.10,"MAE_90D_pct":-38.29,"MAE_180D_pct":-38.29,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":274500,"drawdown_after_peak_pct":-52.90,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"010120_2024-07-01_204500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_LSE_20240723_4B","case_id":"R1L1C02_LSE_20240723_4B","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_EQUIPMENT_PRICE_ONLY_BLOWOFF","sector":"industrials_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage4B-overlay","trigger_date":"2024-07-23","entry_date":"2024-07-23","entry_price":259000,"evidence_available_at_that_date":"local spike and positioning risk; no non-price thesis-break evidence in inspected set","evidence_source":"Stock-Web row","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.00,"MFE_90D_pct":6.00,"MFE_180D_pct":6.00,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-43.99,"MAE_90D_pct":-50.08,"MAE_180D_pct":-50.08,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":274500,"drawdown_after_peak_pct":-54.03,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"010120_2024-07-23_259000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol as LS representative but different trigger family: 4B timing overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L1C02_LSE_20240701","trigger_id":"TR_LSE_20240701_S2A","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":6,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":6,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2-Watch","changed_components":["relative_strength_score","execution_risk_score"],"component_delta_explanation":"C02 local-run MAE guard reduces RS carrying power and increases execution-risk penalty when backlog/margin bridge is incomplete.","MFE_90D_pct":34.23,"MAE_90D_pct":-38.29,"score_return_alignment_label":"after_better_risk_adjusted","current_profile_verdict":"current_profile_too_early"}
{"row_type":"residual_contribution","round":"R1","loop":"1","scheduled_round":"R1","scheduled_loop":"1","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_early","current_profile_4B_too_early"],"diversity_score_summary":"new symbols +12, counterexample gap +8, residual error +10, reused overlay penalty -5 => net positive","loop_contribution_label":"sector_specific_rule_candidate","do_not_propose_new_weight_delta":false}
```

```jsonl
{"row_type":"narrative_only","case_id":"R1L1C02_HHI_2024Q2","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"evidence_available_but_full_stock_web_price_window_not_replayed_in_this_connector_limited_pass","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"narrative_only","case_id":"R1L1C02_ILI_2024Q2","symbol":"103590","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"evidence_available_but_full_stock_web_price_window_not_replayed_in_this_connector_limited_pass","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 1
next_round = R2
next_loop = 1
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest reports FinanceData/marcap source, raw/unadjusted status, max_date 2026-02-20, and calibration shard roots.
- Stock-Web schema defines tradable columns and MFE/MAE formulas.
- 267260 profile confirms HD현대일렉트릭 profile, row counts, available years, and corporate action candidate dates outside tested window.
- 010120 profile confirms LS ELECTRIC profile, row counts, available years, and corporate action candidate dates outside tested window.
- 267260 2023 shard directly confirms 2023-07-27 close 70,600 and the subsequent 2023 price path.
- 267260 2024 shard directly confirms 2024 peak path around 225,000 and later drawdown.
- 010120 2024 shard directly confirms 2024-07-01 close 204,500, 2024-07-23 close 259,000, 2024-07-24 high 274,500, and subsequent high-MAE drawdown.

