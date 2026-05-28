# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only

scheduled_round = R1
scheduled_loop = 12
completed_round = R1
completed_loop = 12
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY
output_file = e2r_stock_web_v12_residual_round_R1_loop_12_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **4** new independent cases, **1** counterexamples, and **3** residual errors for `R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX`.

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

This MD does not re-prove the global Stage2 bonus or the price-only blocker. It tests a narrower C02 residual: **power-grid/datacenter CAPEX names often move before a clean formal revision threshold, but the same theme also produces price-only wire/low-quality rerating rows that must stay blocked.**

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R1
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
round_sector_consistency = pass
```

R1 is constrained to industrials / infrastructure / defense / grid. C02 was selected because previous R1 coverage is quantitatively large, but the remaining useful residual is not "Stage2 earlier" in general. The useful residual is whether C02 should support an **order-quality + margin-bridge Green bridge** while refusing price-only power/copper theme moves.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact review:

```text
reports/e2r_calibration/by_round/R1.md
reports/e2r_calibration/ingest_summary.md
data/e2r/calibration/md_registry.jsonl
```

Observed coverage from the allowed artifacts:

- R1 has `representative_triggers = 79` and `unique_cases = 32`.
- R1 trigger inventory is skewed toward `Stage2-Actionable = 32` and `Stage4B = 19`, while `Stage3-Yellow = 6` and `Stage3-Green = 11`.
- Global accepted axes already include Stage2 bonus, Yellow/Green thresholds, cross-evidence buffer, full 4B non-price requirement, and hard 4C routing.
- The ingest summary shows broad R1~R13 coverage through earlier loops, with rejected rows heavily concentrated in invalid/missing price-source fields in older material, not in stock-web-valid v12 rows.

Duplicate avoidance decision:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 4
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
manifest_max_date = 2026-02-20
```

The manifest reports `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `max_date = 2026-02-20`, and the committed calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. The schema maps tradable shard columns to `d,o,h,l,c,v,a,mc,s,m` and defines the calibration rules: tradable raw basis, positive OHLCV, entry row present, at least 180 forward tradable rows, computed MFE/MAE, and no 180D corporate-action contamination when blocking is enabled.

## 5. Historical Eligibility Gate

All representative trigger rows in this MD satisfy:

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
MFE_30D_90D_180D_computed = true
MAE_30D_90D_180D_computed = true
corporate_action_window_status = clean_180D_window
```

The 1Y/2Y fields are left null in machine-readable rows because this loop's quantitative proposal is explicitly based on 30D/90D/180D trigger-level calibration.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX

fine_archetype_id:
- GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY
- TRANSFORMER_EXPORT_BACKLOG_MARGIN_BRIDGE
- WIRE_COPPER_THEME_PRICE_ONLY_GUARD
```

Compression rule:

```text
if backlog_visibility + customer_quality + margin_bridge + capacity_route coexist:
    C02 can support earlier Green-bridge shadow promotion
else if only relative_strength + theme keyword exists:
    C02 stays Stage2-watch / price-only guard
```

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|current_profile_verdict|score_price_alignment|
|---|---|---|---|---|---|---|
|R1L12_C02_HDHE_267260_20240131|267260|HD현대일렉트릭|structural_success|positive|current_profile_too_late|large_structural_success_low_initial_MAE|
|R1L12_C02_LSE_010120_20240305|010120|LS ELECTRIC|structural_success|positive|current_profile_too_late|structural_success_with_high_post_peak_drawdown|
|R1L12_C02_HSHEAVY_298040_20240305|298040|효성중공업|high_mae_success|positive|current_profile_too_late|success_but_green_lateness_and_drawdown_risk|
|R1L12_C02_DAEWON_006340_20240405|006340|대원전선|price_moved_without_evidence|counterexample|current_profile_correct|price_only_counterexample_not_positive_promotion|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
calibration_usable_case_count = 4
new_independent_case_count = 4
```

The three positive rows test whether C02 structural winners were recognized too late by the current calibrated proxy. The counterexample row prevents the research from becoming a loose "all power/grid themes should be Green earlier" rule.

## 9. Evidence Source Map

|case_id|Stage2 evidence|Stage3 evidence|4B/4C evidence|Evidence caveat|
|---|---|---|---|---|
|R1L12_C02_HDHE_267260_20240131|disclosure/event, customer/order quality, backlog, export/grid route|margin bridge, financial visibility|valuation/positioning later|source label is historical; attach exact DART/news ID during batch ingestion|
|R1L12_C02_LSE_010120_20240305|relative strength, backlog, datacenter/grid route|financial visibility, repeat order/conversion|valuation/positioning later|source label is historical; attach exact DART/news ID during batch ingestion|
|R1L12_C02_HSHEAVY_298040_20240305|relative strength, backlog, transformer route|margin bridge emerging|valuation/positioning later|source label is historical; attach exact DART/news ID during batch ingestion|
|R1L12_C02_DAEWON_006340_20240405|relative strength only|none|price-only local peak, overhang risk|guardrail row; MFE is not evidence quality|

## 10. Price Data Source Map

|symbol|company|profile_path|price_shard_path|profile caveat|
|---|---|---|---|---|
|267260|HD현대일렉트릭|atlas/symbol_profiles/267/267260.json|atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv|corporate-action candidates exist but are pre-2020, outside test window|
|010120|LS ELECTRIC|atlas/symbol_profiles/010/010120.json|atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv|corporate-action candidates exist but are 2003 or earlier|
|298040|효성중공업|atlas/symbol_profiles/298/298040.json|atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv|corporate-action candidate count zero|
|006340|대원전선|atlas/symbol_profiles/006/006340.json|atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv|corporate-action candidates exist but are 2010 or earlier|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|trigger_outcome_label|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R1L12_C02_HDHE_STAGE2A_20240131|267260|HD현대일렉트릭|Stage2-Actionable|2024-01-30|2024-01-31|102700|205.74|-5.06|264.65|-5.06|2024-07-24|374500|current_profile_too_late|large_structural_success_low_initial_MAE|
|R1L12_C02_LSE_STAGE2A_20240305|010120|LS ELECTRIC|Stage2-Actionable|2024-03-05|2024-03-05|77800|213.62|-9.00|252.83|-9.00|2024-07-24|274500|current_profile_too_late|structural_success_with_high_post_peak_drawdown|
|R1L12_C02_HSHEAVY_STAGE2A_20240305|298040|효성중공업|Stage2-Actionable|2024-03-05|2024-03-05|230000|103.91|-3.70|103.91|-3.70|2024-05-28|469000|current_profile_too_late|success_but_green_lateness_and_drawdown_risk|
|R1L12_C02_DAEWON_PRICEONLY_20240405|006340|대원전선|Stage2|2024-04-05|2024-04-05|2095|160.14|-16.61|160.14|-16.61|2024-05-13|5450|current_profile_correct|price_only_counterexample_not_positive_promotion|
|R1L12_C02_LSE_STAGE4B_20240529|010120|LS ELECTRIC|Stage4B|2024-05-29|2024-05-29|231500|18.57|-45.49|18.57|-45.49|2024-07-24|274500|current_profile_4B_too_late|4B_overlay_success|
|R1L12_C02_DAEWON_STAGE4B_PRICEONLY_20240513|006340|대원전선|Stage4B|2024-05-13|2024-05-13|4885|11.57|-32.75|11.57|-32.75|2024-05-13|5450|current_profile_correct|price_only_counterexample|

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows only:

|symbol|entry_date|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
|267260|2024-01-31|102700|53.46|-5.06|205.74|-5.06|264.65|-5.06|2024-07-24|374500|-39.79|
|010120|2024-03-05|77800|107.07|-9.00|213.62|-9.00|252.83|-9.00|2024-07-24|274500|-54.02|
|298040|2024-03-05|230000|55.22|-3.70|103.91|-3.70|103.91|-3.70|2024-05-28|469000|-35.07|
|006340|2024-04-05|2095|160.14|-16.61|160.14|-16.61|160.14|-16.61|2024-05-13|5450|-39.72|

Aggregate:

```text
representative_trigger_count = 4
avg_MFE_90D_pct = 170.85
avg_MAE_90D_pct = -8.59
avg_MFE_180D_pct = 195.38
avg_MAE_180D_pct = -8.59
```

## 13. Current Calibrated Profile Stress Test

1. **HD현대일렉트릭**: current profile likely recognized Stage3 only after stronger revision/multiple-source confirmation. The price path says C02 order quality + margin bridge could have supported earlier Green-bridge. Verdict: `current_profile_too_late`.
2. **LS ELECTRIC**: current profile's Green threshold avoids false positives, but in this case it gives back a large part of upside before confirmation. Verdict: `current_profile_too_late`.
3. **효성중공업**: current profile likely waits for clearer revision; this is safer but late relative to MFE. Verdict: `current_profile_too_late`.
4. **대원전선**: current profile should block price-only promotion. The large MFE is not enough because no customer/order/margin bridge evidence exists. Verdict: `current_profile_correct`.

Existing axis status:

```text
stage2_actionable_evidence_bonus = existing_axis_kept
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_strengthened_conditionally_for_price_only_guard
stage3_green_revision_min = existing_axis_weakened_only_for_C02_order_quality_margin_bridge
stage3_cross_evidence_green_buffer = existing_axis_strengthened
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

```text
C02 residual:
- Stage2-Actionable works for early participation.
- Stage3-Yellow remains useful as the transition label.
- Stage3-Green is too late when customer/order quality + capacity route + margin bridge are already public before formal revision.
- Stage3-Green must remain blocked for price-only wire/theme rows.
```

Green lateness:

|symbol|Stage2 Actionable entry|Later Green proxy|peak|green_lateness_ratio|verdict|
|---|---:|---:|---:|---:|---|
|267260|102700|147000|374500|0.163|Green not very late if C02 bridge allowed|
|010120|77800|155000|274500|0.393|Green moderately late|
|298040|230000|370500|469000|0.588|Green late / most upside consumed|
|006340|2095|null|5450|null|no confirmed Stage3-Green trigger; price-only block|

## 15. 4B Local vs Full-window Timing Audit

|symbol|4B trigger|local proximity|full-window proximity|evidence type|verdict|
|---|---|---:|---:|---|---|
|267260|valuation/positioning watch around July 2024|0.86|0.86|valuation_blowoff, positioning_overheat|good full-window 4B if non-price evidence exists|
|010120|2024-05-29 local overheat|0.925|0.781|valuation_blowoff, positioning_overheat|local 4B also close to full-window peak|
|298040|2024-05-28 local/full peak|0.918|0.918|valuation_blowoff, positioning_overheat|good timing but needs non-price evidence|
|006340|2024-05-13 price-only peak|1.00|1.00|price_only, positioning_overheat|not full 4B unless non-price evidence appears|

The 4B audit supports the existing non-price requirement. It does not weaken it.

## 16. 4C Protection Audit

No hard 4C thesis-break row is promoted in this MD. The loop is a Green/4B guardrail study, not a cancellation or thesis-break study.

```text
four_c_protection_label:
- structural winners: thesis_break_watch_only
- price-only row: false_break
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R1 has multiple canonical archetypes; this evidence is specific to C02 power-grid/datacenter CAPEX, not all industrials.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX

rule_candidate:
    C02 can promote from Stage3-Yellow to shadow Green-bridge before formal revision if:
      1. customer_or_order_quality is supported,
      2. backlog_or_delivery_visibility is supported,
      3. margin_bridge or financial_visibility is supported,
      4. capacity_or_volume_route links to grid/datacenter/export demand,
      5. execution_risk_score is not elevated,
      6. relative_strength is not the only positive evidence.

guard:
    if evidence is only relative_strength + power/grid/copper theme,
    keep Stage2-watch and block Stage3-Green even if MFE is large.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current|4|170.85|-8.59|195.38|-8.59|0.25 if price-only Stage2 were promoted; 0.00 under current blocker|3|3|good blocker, too conservative for C02 structural winners|
|P0b e2r_2_0_baseline_reference|rollback_reference|4|170.85|-8.59|195.38|-8.59|0.25+|1|1|higher recall but unsafe on price-only wires/theme rows|
|P1 sector_specific_candidate_profile|sector_specific|4|170.85|-8.59|195.38|-8.59|0.00|2|2|acceptable but still leaves LS/효성 Green late|
|P2 canonical_archetype_candidate_profile|canonical_archetype_specific|4|170.85|-8.59|195.38|-8.59|0.00 under price-only blocker|0|1|best alignment in this loop|
|P3 counterexample_guard_profile|canonical_guard|4|170.85|-8.59|195.38|-8.59|0.00|1|1|safer than P0b; paired with P2 is preferred|

## 20. Score-Return Alignment Matrix

|case|P0 current|P2 C02 candidate|P3 guard|alignment|
|---|---|---|---|---|
|HD현대일렉트릭|too late|earlier Green-bridge|pass|P2 improves timing with low MAE|
|LS ELECTRIC|too late|earlier Green-bridge|pass|P2 improves timing but keeps 4B overlay|
|효성중공업|too late / high volatility|Yellow-to-Green bridge only after margin support|pass|P2 improves recall but does not over-size|
|대원전선|blocked|blocked|blocked|P3 keeps price-only theme out|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L1_INDUSTRIALS_INFRA_DEFENSE_GRID|C02_POWER_GRID_DATACENTER_CAPEX|GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY|3|1|2|0|4|0|6|4|3|False|True|C02 now has a price-only low-quality wire/theme counterexample; still needs C02 failed-backlog and explicit 4C cancellation cases.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3

tested_existing_calibrated_axes:
- stage3_green_revision_min
- stage3_cross_evidence_green_buffer
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- current_profile_too_late
- current_profile_4B_too_late
- price_only_counterexample

new_axis_proposed:
- C02_customer_quality_margin_bridge_green_bridge

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- stage3_cross_evidence_green_buffer

existing_axis_weakened:
- stage3_green_revision_min only within C02 if customer/order quality + margin bridge are already public

existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema basis
- symbol profile existence and corporate-action candidate review
- 2024 tradable shard entry rows
- 30D/90D/180D MFE/MAE using observed OHLC path
- C02 positive vs price-only counterexample balance
- current calibrated profile stress test
```

Not validated:

```text
- no stock_agent src/e2r code opened
- no production scoring patch
- no live candidate scan
- no current-stock recommendation
- no broker/API linkage
- exact official DART filing IDs are not attached in this research MD; later batch ingestion may attach them as source enrichment
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_customer_quality_margin_bridge_green_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Allow C02 Green bridge only when backlog/order quality + customer route + margin bridge coexist before formal revision confirmation","Recovered early structural positives while keeping price-only Daewon blocked",R1L12_C02_HDHE_STAGE2A_20240131|R1L12_C02_LSE_STAGE2A_20240305|R1L12_C02_HSHEAVY_STAGE2A_20240305|R1L12_C02_DAEWON_PRICEONLY_20240405,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C02_price_only_theme_blocker,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,1,1,0,"Keep existing price-only blocker; C02 wires/theme rows can have large MFE but should not promote without repeat order/customer quality","Blocks price-only counterexample from becoming false Green",R1L12_C02_DAEWON_PRICEONLY_20240405|R1L12_C02_DAEWON_STAGE4B_PRICEONLY_20240513,2,1,1,medium,axis_kept,"strengthens existing price-only blocker but no production change"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R1L12_C02_HDHE_267260_20240131","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R1L12_C02_HDHE_STAGE2A_20240131","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"large_structural_success_low_initial_MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"4Q23/2024 guidance season: transformer order backlog, export mix, margin bridge visibility and US/grid/datacenter capacity route were visible enough for Stage2-Actionable before formal Green confirmation."}
{"row_type":"case","case_id":"R1L12_C02_LSE_010120_20240305","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R1L12_C02_LSE_STAGE2A_20240305","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_with_high_post_peak_drawdown","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Power-grid/datacenter CAPEX rerating route became tradable with order/backlog and relative-strength confirmation; margin bridge was visible but later Green confirmation lagged a large part of the move."}
{"row_type":"case","case_id":"R1L12_C02_HSHEAVY_298040_20240305","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R1L12_C02_HSHEAVY_STAGE2A_20240305","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"success_but_green_lateness_and_drawdown_risk","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Transformer/power equipment rerating with order visibility and relative strength; the case tests whether C02 Green should wait for margin-bridge confirmation because the move included large local drawdowns."}
{"row_type":"case","case_id":"R1L12_C02_DAEWON_006340_20240405","symbol":"006340","company_name":"대원전선","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R1L12_C02_DAEWON_PRICEONLY_20240405","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_only_counterexample_not_positive_promotion","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Grid/copper/power-equipment theme move without clean customer-quality, repeat order, or margin bridge evidence. This is a guardrail row: strong MFE exists, but price-only rerating should not become Stage3 evidence."}
{"row_type":"trigger","trigger_id":"R1L12_C02_HDHE_STAGE2A_20240131","case_id":"R1L12_C02_HDHE_267260_20240131","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","sector":"산업재·수주·인프라·전력망","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-30","evidence_available_at_that_date":"4Q23/2024 guidance season: transformer order backlog, export mix, margin bridge visibility and US/grid/datacenter capacity route were visible enough for Stage2-Actionable before formal Green confirmation.","evidence_source":"historical public earnings/disclosure/news event label; stock-web OHLC rows validated by atlas shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-31","entry_price":102700,"MFE_30D_pct":53.46,"MFE_90D_pct":205.74,"MFE_180D_pct":264.65,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.06,"MAE_90D_pct":-5.06,"MAE_180D_pct":-5.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":374500,"drawdown_after_peak_pct":-39.79,"green_lateness_ratio":0.163,"four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"large_structural_success_low_initial_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate-action candidates are pre-2020, outside window","same_entry_group_id":"R1L12_C02_HDHE_267260_20240131__2024-01-31","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L12_C02_LSE_STAGE2A_20240305","case_id":"R1L12_C02_LSE_010120_20240305","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","sector":"산업재·수주·인프라·전력망","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-05","evidence_available_at_that_date":"Power-grid/datacenter CAPEX rerating route became tradable with order/backlog and relative-strength confirmation; margin bridge was visible but later Green confirmation lagged a large part of the move.","evidence_source":"historical public earnings/disclosure/news event label; stock-web OHLC rows validated by atlas shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-05","entry_price":77800,"MFE_30D_pct":107.07,"MFE_90D_pct":213.62,"MFE_180D_pct":252.83,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.0,"MAE_90D_pct":-9.0,"MAE_180D_pct":-9.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":274500,"drawdown_after_peak_pct":-54.02,"green_lateness_ratio":0.393,"four_b_local_peak_proximity":0.925,"four_b_full_window_peak_proximity":0.781,"four_b_timing_verdict":"good_full_window_4B_timing_when_valuation_and_positioning_overheat_exist","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_with_high_post_peak_drawdown","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate-action candidates are 2003 or earlier","same_entry_group_id":"R1L12_C02_LSE_010120_20240305__2024-03-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L12_C02_HSHEAVY_STAGE2A_20240305","case_id":"R1L12_C02_HSHEAVY_298040_20240305","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","sector":"산업재·수주·인프라·전력망","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-05","evidence_available_at_that_date":"Transformer/power equipment rerating with order visibility and relative strength; the case tests whether C02 Green should wait for margin-bridge confirmation because the move included large local drawdowns.","evidence_source":"historical public earnings/disclosure/news event label; stock-web OHLC rows validated by atlas shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-05","entry_price":230000,"MFE_30D_pct":55.22,"MFE_90D_pct":103.91,"MFE_180D_pct":103.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.7,"MAE_90D_pct":-3.7,"MAE_180D_pct":-3.7,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":469000,"drawdown_after_peak_pct":-35.07,"green_lateness_ratio":0.588,"four_b_local_peak_proximity":0.918,"four_b_full_window_peak_proximity":0.918,"four_b_timing_verdict":"good_local_4B_but_needs_non_price_overheat_for_full_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"success_but_green_lateness_and_drawdown_risk","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate-action candidate count is zero","same_entry_group_id":"R1L12_C02_HSHEAVY_298040_20240305__2024-03-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L12_C02_DAEWON_PRICEONLY_20240405","case_id":"R1L12_C02_DAEWON_006340_20240405","symbol":"006340","company_name":"대원전선","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","sector":"산업재·수주·인프라·전력망","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2","trigger_date":"2024-04-05","evidence_available_at_that_date":"Grid/copper/power-equipment theme move without clean customer-quality, repeat order, or margin bridge evidence. This is a guardrail row: strong MFE exists, but price-only rerating should not become Stage3 evidence.","evidence_source":"historical theme/price-row red-team label; stock-web OHLC rows validated by atlas shard","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-05","entry_price":2095,"MFE_30D_pct":160.14,"MFE_90D_pct":160.14,"MFE_180D_pct":160.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.61,"MAE_90D_pct":-16.61,"MAE_180D_pct":-16.61,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":5450,"drawdown_after_peak_pct":-39.72,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_if_no_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat","capital_raise_or_overhang"],"four_c_protection_label":"false_break","trigger_outcome_label":"price_only_counterexample_not_positive_promotion","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window under profile candidate rules; profile corporate-action candidates are 2010 or earlier","same_entry_group_id":"R1L12_C02_DAEWON_006340_20240405__2024-04-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L12_C02_LSE_STAGE4B_20240529","case_id":"R1L12_C02_LSE_010120_20240305","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","sector":"산업재·수주·인프라·전력망","primary_archetype":"power_grid_datacenter_capex","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-05-29","entry_date":"2024-05-29","entry_price":231500,"evidence_available_at_that_date":"Local/full-window overheat audit after sharp rerating; valuation/positioning evidence is required before treating this as full 4B.","evidence_source":"stock-web OHLC local/full peak audit plus historical valuation-positioning red-team label","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.4,"MFE_90D_pct":18.57,"MFE_180D_pct":18.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.48,"MAE_90D_pct":-45.49,"MAE_180D_pct":-45.49,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":274500,"drawdown_after_peak_pct":-54.02,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.925,"four_b_full_window_peak_proximity":0.781,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_evidence_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L12_C02_LSE_010120_20240305__20240529","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, separate 4B timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L12_C02_DAEWON_STAGE4B_PRICEONLY_20240513","case_id":"R1L12_C02_DAEWON_006340_20240405","symbol":"006340","company_name":"대원전선","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_US_DATACENTER_CAPEX_ORDER_VISIBILITY","sector":"산업재·수주·인프라·전력망","primary_archetype":"power_grid_datacenter_capex","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage4B","trigger_date":"2024-05-13","entry_date":"2024-05-13","entry_price":4885,"evidence_available_at_that_date":"Price-only local peak after theme acceleration; no repeat-order/customer-quality evidence, and share count/overhang risk weakens promotion quality.","evidence_source":"stock-web OHLC local/full peak audit plus historical price-only red-team label","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.57,"MFE_90D_pct":11.57,"MFE_180D_pct":11.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.75,"MAE_90D_pct":-32.75,"MAE_180D_pct":-32.75,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":5450,"drawdown_after_peak_pct":-39.72,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat","capital_raise_or_overhang"],"four_c_protection_label":"false_break","trigger_outcome_label":"price_only_counterexample","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L12_C02_DAEWON_006340_20240405__20240513","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, separate price-only 4B guard audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L12_C02_HDHE_267260_20240131","trigger_id":"R1L12_C02_HDHE_STAGE2A_20240131","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":7,"revision_score":5,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":5,"relative_strength_score":7,"customer_quality_score":9,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"capacity_or_shipment_score":2,"order_intake_quality_score":2},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","margin_bridge_score","capacity_or_shipment_score","order_intake_quality_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile rewards order/customer-quality + margin bridge; it penalizes price-only rerating and dilution/overhang without customer evidence.","MFE_90D_pct":205.74,"MAE_90D_pct":-5.06,"score_return_alignment_label":"large_structural_success_low_initial_MAE","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L12_C02_LSE_010120_20240305","trigger_id":"R1L12_C02_LSE_STAGE2A_20240305","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":76.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":7,"margin_bridge_score":7,"revision_score":4,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"capacity_or_shipment_score":2,"order_intake_quality_score":1},"weighted_score_after":87.5,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","margin_bridge_score","capacity_or_shipment_score","order_intake_quality_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile rewards order/customer-quality + margin bridge; it penalizes price-only rerating and dilution/overhang without customer evidence.","MFE_90D_pct":213.62,"MAE_90D_pct":-9.0,"score_return_alignment_label":"structural_success_with_high_post_peak_drawdown","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L12_C02_HSHEAVY_298040_20240305","trigger_id":"R1L12_C02_HSHEAVY_STAGE2A_20240305","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":3,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"capacity_or_shipment_score":2,"order_intake_quality_score":1},"weighted_score_after":84.0,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","capacity_or_shipment_score","order_intake_quality_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile rewards order/customer-quality + margin bridge; it penalizes price-only rerating and dilution/overhang without customer evidence.","MFE_90D_pct":103.91,"MAE_90D_pct":-3.7,"score_return_alignment_label":"success_but_green_lateness_and_drawdown_risk","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L12_C02_DAEWON_006340_20240405","trigger_id":"R1L12_C02_DAEWON_PRICEONLY_20240405","symbol":"006340","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":3,"accounting_trust_risk_score":1},"weighted_score_before":63.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":5,"accounting_trust_risk_score":1},"weighted_score_after":58.0,"stage_label_after":"Stage2-watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C02 shadow profile rewards order/customer-quality + margin bridge; it penalizes price-only rerating and dilution/overhang without customer evidence.","MFE_90D_pct":160.14,"MAE_90D_pct":-16.61,"score_return_alignment_label":"price_only_counterexample_not_positive_promotion","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R1","loop":"12","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","scheduled_round":"R1","scheduled_loop":"12","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":3,"counterexample_count":1,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_4B_too_late","price_only_counterexample"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"new symbols=4, new trigger families=3, positive=3, counterexample=1, current_profile_errors=3"}
```

CSV shadow rows are provided above in Section 24 and repeated here for parser compatibility:

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_customer_quality_margin_bridge_green_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"Allow C02 Green bridge only when backlog/order quality + customer route + margin bridge coexist before formal revision confirmation","Recovered early structural positives while keeping price-only Daewon blocked",R1L12_C02_HDHE_STAGE2A_20240131|R1L12_C02_LSE_STAGE2A_20240305|R1L12_C02_HSHEAVY_STAGE2A_20240305|R1L12_C02_DAEWON_PRICEONLY_20240405,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C02_price_only_theme_blocker,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,1,1,0,"Keep existing price-only blocker; C02 wires/theme rows can have large MFE but should not promote without repeat order/customer quality","Blocks price-only counterexample from becoming false Green",R1L12_C02_DAEWON_PRICEONLY_20240405|R1L12_C02_DAEWON_STAGE4B_PRICEONLY_20240513,2,1,1,medium,axis_kept,"strengthens existing price-only blocker but no production change"
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
completed_loop = 12
next_round = R2
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest confirms `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, and `max_date = 2026-02-20`.
- Stock-web schema confirms tradable columns and calibration basis.
- R1 allowed artifact confirms prior R1 coverage and accepted axes.
- Symbol profiles were checked for all four representative cases.
- This is historical calibration research only, not investment advice or live candidate discovery.

