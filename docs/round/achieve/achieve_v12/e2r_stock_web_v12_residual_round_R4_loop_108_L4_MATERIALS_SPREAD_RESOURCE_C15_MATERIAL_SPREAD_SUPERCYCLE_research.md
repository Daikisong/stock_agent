# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 108
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: MATERIAL_LABEL_TO_ASP_MARGIN_FCF_HOLDOUT_V108_FOIL_COPPER_ALUMINIUM_CHEMICAL_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 010130/2024: cache_miss_observed
    - 005490/2024: cache_miss_observed
    - 003670/2024: cache_miss_observed
    - additional_C15_candidate_shards: not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - material_label_to_ASP_margin_FCF_bridge_gate
  - high_MFE_high_MAE_4B_vs_hard_4C_split
  - chemical_spread_repair_absent_guard
  - wrong_archetype_reclassification_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C15_MATERIAL_SPREAD_SUPERCYCLE` remains a Priority 0 archetype in the current no-repeat index. The v12 scheduler maps C15~C17 to `R4 / L4_MATERIALS_SPREAD_RESOURCE`.

This file continues the local C15 sequence after `R4/C15 loop 107`; selected loop is therefore `108`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because additional material candidate shards returned cache miss or were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C15/C16/C17 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C15 should not reward the word `material`.

C15 should reward company-level spread conversion:

```text
metal / chemical / battery foil / silicone / copper / aluminium label
→ ASP
→ volume / utilization
→ inventory gain or loss
→ margin / FCF / revision
→ price path validation
```

A commodity price can shout. C15 only listens when the shout reaches the income statement.

The current holdout rule remains:

```text
company-specific material margin bridge
→ keep Stage2

material label + high MFE + severe MAE
→ local 4B until utilization / margin refresh

commodity beta + low MFE + deep MAE
→ hard 4C

chemical label without spread repair
→ hard 4C

real processing / dual-use material bridge + high MAE
→ local 4B until order / margin / cash refresh
```

This loop validates five route types:

1. **Company-specific material margin positive-control**
   - Keep Stage2 when margin/FCF bridge validates and MAE is controlled.

2. **Battery-foil / aluminium high-MFE high-MAE route**
   - Early MFE can be tradable.
   - Severe 90D/180D MAE means local 4B only until utilization/order/margin refresh.

3. **Aluminium rolling commodity beta false positive**
   - Low MFE and deep MAE with no company margin bridge should hard block.

4. **Petrochemical / PP label hard counterexample**
   - Chemical vocabulary without product-spread repair, balance-sheet relief or FCF should hard block.

5. **Dual-use copper / processing bridge**
   - Real processing bridge can open Stage2, but high MAE requires local 4B until order/margin/cash refresh.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 5
  actual_trigger_rows: 5
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
    - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C15 holdout validation
    - material-label false-positive guard
    - high-MFE/high-MAE local 4B split
    - company-specific margin bridge positive-control
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R4/C15 loop 104
  - R4/C15 loop 105
  - R4/C15 loop 106
  - R4/C15 loop 107
  - R4/C16 loops 112~114
  - R4/C17 loops 136~138
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional material candidate shards returned cache miss or were not recomputed in this execution
  - exact duplicate C15 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R4","selected_loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COMPANY_SPECIFIC_SILICONE_PAINT_MATERIAL_MARGIN_POSITIVE_CONTROL","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_price":244000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.62,"MAE_30D_pct":-2.46,"MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"MFE_180D_pct":41.39,"MAE_180D_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C15|002380|Stage2-Actionable|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C15 material margin positive-control row from loops 104~107 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"material_margin_positive_control","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|002380|Stage2-Actionable|2024-01-30","non_price_bridge":"company-specific materials/silicone/paint margin recovery bridge rather than generic commodity beta","score_alignment":"keep Stage2; allow Yellow path only while margin/revision/FCF bridge remains refreshed"}
{"row_type":"trigger","selected_round":"R4","selected_loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINIUM_BATTERY_FOIL_HIGH_MFE_HIGH_MAE_LOCAL_4B","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage4B","entry_date":"2024-05-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.34,"MAE_30D_pct":-7.28,"MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"MFE_180D_pct":28.34,"MAE_180D_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C15|006110|Stage4B|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same C15 aluminium foil high-MAE row from loops 105~107 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"high_MFE_high_MAE_local_4B","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|006110|Stage4B|2024-05-20","non_price_bridge":"aluminium battery-foil material label without refreshed customer order, utilization, ASP/margin or cash bridge","score_alignment":"local 4B only; block Green until order/utilization/margin bridge refresh"}
{"row_type":"trigger","selected_round":"R4","selected_loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINIUM_ROLLING_COMMODITY_BETA_LOW_MFE_HIGH_MAE_HARD_4C","symbol":"018470","name":"조일알미늄","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":2470,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.29,"MAE_30D_pct":-17.41,"MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"MFE_180D_pct":7.29,"MAE_180D_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C15|018470|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C15 aluminium rolling hard counterexample row from loops 105~107 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"hard_counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|018470|Stage4C|2024-05-20","non_price_bridge":"aluminium rolling commodity beta label without company-specific ASP, volume, margin or FCF bridge","score_alignment":"hard 4C; low MFE and high MAE reject C15 material-spread bridge"}
{"row_type":"trigger","selected_round":"R4","selected_loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"PETROCHEM_PP_MATERIAL_LABEL_MARGIN_BALANCE_SHEET_DECAY_HARD_4C","symbol":"298000","name":"효성화학","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":71000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.41,"MAE_30D_pct":-16.20,"MFE_90D_pct":9.01,"MAE_90D_pct":-22.39,"MFE_180D_pct":9.01,"MAE_180D_pct":-60.35,"forward_high_30d":72000,"forward_low_30d":59500,"forward_high_90d":77400,"forward_low_90d":55100,"forward_high_180d":77400,"forward_low_180d":28150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C15|298000|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C15 petrochemical hard counterexample row from loops 105~107","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"hard_counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|298000|Stage4C|2024-05-20","non_price_bridge":"petrochemical/PP material label without visible product-spread, margin repair, FCF or balance-sheet bridge","score_alignment":"hard 4C; severe 180D MAE shows material label failed"}
{"row_type":"trigger","selected_round":"R4","selected_loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"DUAL_USE_COPPER_PROCESSING_BRIDGE_HIGH_MAE_LOCAL_4B","symbol":"103140","name":"풍산","trigger_type":"Stage4B","entry_date":"2024-04-26","entry_price":62900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.44,"MAE_30D_pct":-10.17,"MFE_90D_pct":25.44,"MAE_90D_pct":-25.28,"MFE_180D_pct":25.44,"MAE_180D_pct":-26.63,"forward_high_30d":78900,"forward_low_30d":56500,"forward_high_90d":78900,"forward_low_90d":47000,"forward_high_180d":78900,"forward_low_180d":46150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C15|103140|Stage4B|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same C15/C16 dual-use processing row from loops 105~107 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|103140|Stage4B|2024-04-26","non_price_bridge":"actual copper/non-ferrous processing plus defense dual-use material demand; high MAE requires order/margin refresh","score_alignment":"Stage2 may open; local 4B until processing margin, order and cash bridge refresh"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R4","selected_loop":108,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_NEW_MATERIALS_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["010130","005490","003670"],"candidate_names":["고려아연","POSCO홀딩스","포스코퓨처엠"],"why_not_trigger_row_now":"uncached 2024 stock-web symbol shards returned cache miss or were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C15 evidence"}
```

---

## 6. Case analysis

### 6.1 KCC / 002380 — margin bridge positive control

KCC is still the clean C15 control because material margin became company economics.

```yaml
entry_close: 244000
90D_MFE_MAE: +20.49 / -7.79
180D_MFE_MAE: +41.39 / -7.79
route: KeepStage2
```

### 6.2 Sam-A Aluminium / 006110 — foil 4B

Foil label had strong MFE but severe later MAE. It stays 4B only while utilization and margin bridge are checked.

```yaml
entry_close: 75500
90D_MFE_MAE: +28.34 / -47.55
180D_MFE_MAE: +28.34 / -53.58
route: Local4B
```

### 6.3 Choil Aluminium / 018470 — commodity beta hard 4C

Commodity beta did not become company spread.

```yaml
entry_close: 2470
90D_MFE_MAE: +7.29 / -41.30
180D_MFE_MAE: +7.29 / -44.70
route: Stage4C
```

### 6.4 Hyosung Chemical / 298000 — chemical label hard 4C

The PP/petrochemical label failed to become product-spread repair or balance-sheet relief.

```yaml
entry_close: 71000
90D_MFE_MAE: +9.01 / -22.39
180D_MFE_MAE: +9.01 / -60.35
route: Stage4C
```

### 6.5 Poongsan / 103140 — processing bridge 4B

The copper/processing bridge is real enough to avoid hard block, but high MAE requires margin and order refresh.

```yaml
entry_close: 62900
90D_MFE_MAE: +25.44 / -25.28
180D_MFE_MAE: +25.44 / -26.63
route: Local4B
```

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 5
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_count: 3
local_4B_watch_count: 2
hard_4C_count: 2
current_profile_error_count: 4
diversity_score_summary: "positive-control, foil 4B, aluminium hard 4C, chemical hard 4C, dual-use processing 4B covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C15 lesson |
|---|---:|---:|---:|---|
| 002380 | margin positive | +20.49 / -7.79 | +41.39 / -7.79 | margin bridge validates |
| 006110 | foil local 4B | +28.34 / -47.55 | +28.34 / -53.58 | utilization/margin refresh needed |
| 018470 | aluminium hard 4C | +7.29 / -41.30 | +7.29 / -44.70 | commodity beta fails |
| 298000 | chemical hard 4C | +9.01 / -22.39 | +9.01 / -60.35 | spread repair absent |
| 103140 | processing local 4B | +25.44 / -25.28 | +25.44 / -26.63 | real bridge, refresh required |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"002380","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Company-specific material margin bridge validated; controlled MAE supports Stage2 hold.","MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"score_return_alignment_label":"material_margin_positive_control","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"006110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":71,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":56,"stage_label_after":"Stage4B_local_watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Foil label had high MFE but margin/utilization bridge was unrefreshed and MAE severe; local 4B only.","MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"score_return_alignment_label":"foil_high_MAE_local_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"018470","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":41,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Aluminium commodity beta lacked company spread bridge and price path rejected the label.","MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"score_return_alignment_label":"commodity_beta_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"298000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","dilution_cb_risk_score"],"component_delta_explanation":"Petrochemical label did not become spread repair or FCF; severe 180D drawdown confirms hard 4C.","MFE_90D_pct":9.01,"MAE_90D_pct":-22.39,"score_return_alignment_label":"chemical_margin_decay_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"103140","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":68,"stage_label_after":"Stage4B_local_watch","changed_components":["relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Real processing bridge exists, but high MAE requires order/margin/cash refresh before Actionable.","MFE_90D_pct":25.44,"MAE_90D_pct":-25.28,"score_return_alignment_label":"processing_bridge_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
```

---

## 9. Current calibrated profile stress test

The C15 material-to-cash bridge gate held again:

```text
company-specific material margin bridge
→ keep Stage2

material label with high MFE but severe MAE
→ local 4B until refresh

commodity beta with low MFE / deep MAE
→ hard 4C

chemical label without spread repair
→ hard 4C

processing bridge with high MAE
→ local 4B
```

### Rule candidate retained, not newly proposed

```text
C15_MATERIAL_LABEL_TO_ASP_MARGIN_FCF_BRIDGE_REQUIREMENT_V108_HELD_OUT

if C15
and material_metal_chemical_or_battery_foil_label == true
and company_specific_ASP_volume_utilization_margin_or_FCF_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C15
and company_specific_material_margin_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if C15
and material_label == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -25
and refreshed_margin_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C15
and material_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C15
and dominant_driver_belongs_to_C16_C17_battery_policy_or_governance_axis == true:
    cap_C15_contribution = true
    require_reclassification = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 5
    avg_MFE_90D_pct: 18.11
    avg_MAE_90D_pct: -28.86
    false_positive_risk: high_if_material_label_rows_are_left_actionable
    verdict: adequate_only_with_C15_bridge_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for material/commodity heat
    eligible_trigger_count: 5
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L4 material names require ASP/margin/FCF conversion
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C15 requires company spread bridge rather than commodity label
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: commodity beta / chemical decay rows route to hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | MATERIAL_LABEL_TO_ASP_MARGIN_FCF_HOLDOUT_V108 | 2 | 3 | 2 | 2 | 0 | 5 | 5 | 0 | 4 | false | false | 24 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 5
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 5
reused_case_ids:
  - C15|002380|Stage2-Actionable|2024-01-30
  - C15|006110|Stage4B|2024-05-20
  - C15|018470|Stage4C|2024-05-20
  - C15|298000|Stage4C|2024-05-20
  - C15|103140|Stage4B|2024-04-26
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - material_label_to_margin_cash_bridge
residual_error_types_found:
  - material_label_without_company_margin_bridge
  - high_MFE_high_MAE_battery_foil_4B
  - aluminium_commodity_beta_false_positive
  - petrochemical_spread_repair_absent
new_axis_proposed: null
existing_axis_strengthened:
  - C15_MATERIAL_LABEL_TO_ASP_MARGIN_FCF_BRIDGE_REQUIREMENT_V108_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after additional material candidate shards returned cache miss or were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"108","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":0,"reused_case_count":5,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","material_label_to_margin_cash_bridge"],"residual_error_types_found":["material_label_without_company_margin_bridge","high_MFE_high_MAE_battery_foil_4B","aluminium_commodity_beta_false_positive","petrochemical_spread_repair_absent"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R4/C15 loop 108 as holdout validation only. Batch it with C15 loops 101~107, C16/C17 adjacent material rows, and R13 high-MAE/accounting-trust/Stage2 false-positive/4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C15 material-label-to-ASP-margin-FCF gate, but do not create a new weight delta from this loop because no new independent case was added. Future research should reprice 고려아연(010130), POSCO홀딩스(005490), 포스코퓨처엠(003670) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R4
completed_loop: 108
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```
