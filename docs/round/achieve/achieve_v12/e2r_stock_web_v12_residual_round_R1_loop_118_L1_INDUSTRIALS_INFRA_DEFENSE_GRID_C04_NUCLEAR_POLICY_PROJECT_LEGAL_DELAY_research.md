# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 118
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: DUKOVANY_FINAL_CONTRACT_NO_BACKFILL_HOLDOUT_V118_PREFERRED_BIDDER_SUPPLIER_THEME_SERVICE_OM_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 034020/2024: cache_miss_observed_this_turn
    - 034020/2025: cache_miss_or_not_recomputed_this_turn
    - 052690/2024: cache_miss_observed_this_turn
    - 052690/2025: cache_miss_or_not_recomputed_this_turn
    - 051600/2024: cache_miss_observed_this_turn
    - 051600/2025: cache_miss_or_not_recomputed_this_turn
    - 457550/2025: cache_miss_or_not_recomputed_this_turn
    - 083650/2024: cache_miss_or_not_recomputed_this_turn
    - 105840/2024: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - final_contract_no_backfill_guard
  - preferred_bidder_vs_final_contract_temporal_split
  - supplier_theme_hard_4C_guard
  - service_OM_escape_hatch_check
  - cache_miss_todo_for_future_reprice
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` remains a Priority 0 archetype in the no-repeat index. It maps to `R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID` under the v12 scheduler.

This file continues the local C04 sequence after `R1/C04 loop 117`; selected loop is therefore `118`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct fresh 2024/2025 nuclear candidate shards cache-missed or were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C04 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C04 should not reward `nuclear policy headline` by itself.

It should reward the legal/project bridge:

```text
nuclear policy / preferred bidder / final contract / legal clearance
→ named order scope
→ contract economics
→ financing / margin / supplier allocation
→ revenue and cash collection
→ price path validation
```

The key temporal trap remains the Dukovany sequence:

```text
preferred bidder
≠ final contract
≠ accounting revenue bridge
```

The trigger-family distinction is mandatory:

```text
2024 preferred-bidder rows
→ evaluate with 2024 legal-delay risk and missing final-contract bridge

2025 final-contract rows
→ require separate 2025 trigger date and fresh stock-web MFE/MAE windows

later final-contract evidence
→ never backfill into 2024 preferred-bidder triggers
```

This holdout loop validates four routes:

1. **Preferred-bidder supply-chain spike**
   - Tradable MFE can exist.
   - Missing final contract and high MAE keep it local 4B / Watch.

2. **Direct engineering scope**
   - Direct exposure is better than supplier theme.
   - Still capped if legal clearance and final contract economics are absent at trigger date.

3. **Service / O&M escape hatch**
   - Recurring service and O&M visibility can survive better because the bridge is less dependent on one new-build contract signing.

4. **Small supplier theme spike**
   - Price-only supplier heat with severe MAE and no contract-scope bridge should hard block.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 4
  actual_trigger_rows: 4
  narrative_only_future_trigger_rows: 2
  source_archetypes:
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C04 holdout validation
    - final-contract no-backfill guard
    - legal-delay local 4B validation
    - supplier-theme hard 4C validation
    - O&M/service escape hatch validation
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
  - R1/C04 loop 114
  - R1/C04 loop 115
  - R1/C04 loops 110~117
  - R13 accounting-trust loops 11~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional 2024/2025 C04 candidate shards were not recomputed in this execution
  - exact duplicate C04 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R1","selected_loop":118,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"PREFERRED_BIDDER_SUPPLY_CHAIN_SPIKE_LEGAL_DELAY_LOCAL_4B","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage4B","entry_date":"2024-07-17","entry_price":21250,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.65,"MAE_30D_pct":-28.71,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"MFE_180D_pct":17.65,"MAE_180D_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C04|034020|Stage4B|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same C04 preferred-bidder row from loops 114~116 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"preferred_bidder_local_4B","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|034020|Stage4B|2024-07-17","non_price_bridge":"Czech preferred-bidder supply-chain exposure, but legal/final-contract/order-scope cash bridge incomplete in 2024 trigger window","score_alignment":"Stage2-Watch / local 4B; block Green until final contract, order scope, margin and cash bridge refresh"}
{"row_type":"trigger","selected_round":"R1","selected_loop":118,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"DIRECT_ENGINEERING_SCOPE_WITH_LEGAL_FINAL_CONTRACT_GAP_STAGE2_CAP","symbol":"052690","name":"한전기술","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_price":82000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.63,"MAE_30D_pct":-24.88,"MFE_90D_pct":19.63,"MAE_90D_pct":-24.88,"MFE_180D_pct":19.63,"MAE_180D_pct":-39.94,"forward_high_30d":98100,"forward_low_30d":61600,"forward_high_90d":98100,"forward_low_90d":61600,"forward_high_180d":98100,"forward_low_180d":49250,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C04|052690|Stage2-Watch|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","reuse_reason":"same C04 direct-scope legal-delay row from loops 114~116","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"direct_scope_stage2_cap","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|Stage2-Watch|2024-07-18","non_price_bridge":"direct nuclear engineering exposure, but preferred-bidder headline did not yet equal final contract cash bridge","score_alignment":"cap Stage2; high MAE blocks Green until legal clearance and final-contract economics are confirmed"}
{"row_type":"trigger","selected_round":"R1","selected_loop":118,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_SERVICE_OM_VISIBILITY_LOW_MAE_ESCAPE_HATCH","symbol":"051600","name":"한전KPS","trigger_type":"Stage2-Actionable","entry_date":"2024-09-12","entry_price":42150,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.47,"MAE_30D_pct":-4.39,"MFE_90D_pct":16.49,"MAE_90D_pct":-4.39,"MFE_180D_pct":16.49,"MAE_180D_pct":-9.85,"forward_high_30d":48250,"forward_low_30d":40300,"forward_high_90d":49100,"forward_low_90d":40300,"forward_high_180d":49100,"forward_low_180d":38000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C04|051600|Stage2-Actionable|2024-09-12","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_escape_hatch","reuse_reason":"same C04 service/O&M escape hatch row from loops 114~116","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"service_OM_escape_hatch","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|Stage2-Actionable|2024-09-12","non_price_bridge":"nuclear service/O&M visibility; less dependent on single preferred-bidder contract spike","score_alignment":"keep Stage2 with Green blocked until service/order economics refresh"}
{"row_type":"trigger","selected_round":"R1","selected_loop":118,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"SMALL_SUPPLIER_THEME_SPIKE_NO_CONTRACT_SCOPE_HARD_4C","symbol":"457550","name":"우진엔텍","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":31500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.06,"MAE_30D_pct":-50.83,"MFE_90D_pct":32.06,"MAE_90D_pct":-58.25,"MFE_180D_pct":32.06,"MAE_180D_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C04|457550|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C04 supplier spike hard-block row from loops 114~116 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"supplier_theme_hard_4C","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|457550|Stage4C|2024-07-18","non_price_bridge":"small supplier nuclear theme spike without listed-company final-contract, order scope or cash bridge","score_alignment":"hard 4C; do not learn price-only supplier spike as Green"}
```

---

## 5. Narrative-only future TODO rows

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R1","selected_loop":118,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"DUKOVANY_FINAL_CONTRACT_2025_SEPARATE_TRIGGER_REQUIRED","event_date":"2025-06-04","event_family":"final_contract_signed_after_court_clearance","symbols_to_reprice_later":["034020","052690","051600","457550"],"why_not_trigger_row_now":"2025 stock-web symbol shards were not recomputed in this execution; no 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"do not backfill 2025 final-contract evidence into 2024 preferred-bidder rows; compute separate stock-web windows from 2025-06-04 when shards are accessible"}
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R1","selected_loop":118,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"ADDITIONAL_NUCLEAR_SUPPLIER_SERVICE_REPRICE_TODO","candidate_symbols":["083650","105840"],"candidate_names":["비에이치아이","우진"],"candidate_trigger_family":["nuclear_supplier_scope","nuclear_instrumentation_service"],"why_not_trigger_row_now":"2024 stock-web symbol shards were not recomputed in this execution; no fresh MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting as new C04 evidence"}
```

---

## 6. Case analysis

### 6.1 Doosan Enerbility / 034020 — preferred bidder local 4B

The preferred-bidder event had project potential, but the accounting bridge was not final. High MAE confirms it should not be Green.

```yaml
entry_close: 21250
30D_MFE_MAE: +17.65 / -28.71
90D_MFE_MAE: +17.65 / -28.71
180D_MFE_MAE: +17.65 / -28.71
route: Stage2-Watch / local 4B
```

### 6.2 KEPCO Engineering / 052690 — direct scope cap

Direct engineering scope is meaningful, but final contract economics and legal clearance were missing at trigger date.

```yaml
entry_close: 82000
30D_MFE_MAE: +19.63 / -24.88
90D_MFE_MAE: +19.63 / -24.88
180D_MFE_MAE: +19.63 / -39.94
route: Stage2 cap
```

### 6.3 KEPCO KPS / 051600 — service/O&M escape hatch

Service/O&M visibility has lower drawdown because it is not fully dependent on a single preferred-bidder contract.

```yaml
entry_close: 42150
30D_MFE_MAE: +14.47 / -4.39
90D_MFE_MAE: +16.49 / -4.39
180D_MFE_MAE: +16.49 / -9.85
route: Stage2-Actionable with Green blocked
```

### 6.4 Woojin Entech / 457550 — supplier theme hard 4C

Supplier heat had a sharp MFE but no listed-company contract-scope bridge. Severe MAE confirms 4C.

```yaml
entry_close: 31500
30D_MFE_MAE: +32.06 / -50.83
90D_MFE_MAE: +32.06 / -58.25
180D_MFE_MAE: +32.06 / -58.25
route: Stage4C
```

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 4
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_trigger_count: 2
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
counterexample_count: 3
local_4B_watch_count: 2
hard_4C_count: 1
current_profile_error_count: 3
diversity_score_summary: "preferred-bidder 4B, direct-scope cap, service/O&M escape, supplier hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_future_trigger_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C04 lesson |
|---|---:|---:|---:|---|
| 034020 | preferred bidder local 4B | +17.65 / -28.71 | +17.65 / -28.71 | no final-contract backfill |
| 052690 | direct scope cap | +19.63 / -24.88 | +19.63 / -39.94 | engineering scope needs legal/cash bridge |
| 051600 | O&M escape hatch | +16.49 / -4.39 | +16.49 / -9.85 | service visibility survives better |
| 457550 | supplier hard 4C | +32.06 / -58.25 | +32.06 / -58.25 | supplier spike lacks contract economics |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"034020","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":4},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_after":64,"stage_label_after":"Stage4B_local_watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Preferred-bidder evidence opened watch but legal/final-contract bridge was incomplete and MAE was high.","MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"score_return_alignment_label":"preferred_bidder_local_4B_no_backfill","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"052690","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":69,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":61,"stage_label_after":"Stage2_Watch_Cap","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Direct engineering exposure still lacked final contract economics at entry date; drawdown validates cap.","MFE_90D_pct":19.63,"MAE_90D_pct":-24.88,"score_return_alignment_label":"direct_scope_cap_legal_gap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"051600","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":[],"component_delta_explanation":"Service/O&M visibility is less dependent on one project signing and had controlled MAE, but still requires order/revenue refresh before Green.","MFE_90D_pct":16.49,"MAE_90D_pct":-4.39,"score_return_alignment_label":"service_OM_escape_hatch","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"457550","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Supplier theme MFE did not represent contract-scope bridge; severe MAE confirms hard 4C.","MFE_90D_pct":32.06,"MAE_90D_pct":-58.25,"score_return_alignment_label":"supplier_theme_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

---

## 9. Current calibrated profile stress test

The C04 gate held again:

```text
preferred bidder / policy headline
→ Stage2-Watch or local 4B

direct engineering scope
→ not enough without legal/final-contract economics

service/O&M visibility
→ positive escape hatch with Green blocked

small supplier theme spike
→ hard 4C if no contract-scope bridge

later final contract
→ separate trigger, never backfill
```

### Rule candidate retained, not newly proposed

```text
C04_FINAL_CONTRACT_NO_BACKFILL_REQUIREMENT_V118_HELD_OUT

if C04
and preferred_bidder_or_policy_project_headline == true
and final_contract_legal_clearance_company_cash_bridge_at_trigger_date == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
    block_stage3_green = true
```

```text
if C04
and later_final_contract_signed == true
and later_contract_date > original_trigger_date:
    do_not_backfill_later_contract_to_original_trigger = true
    require_new_trigger_row_from_later_contract_date_with_stock_web_price_window = true
```

```text
if C04
and service_OM_visibility == true
and MFE_90D_pct >= +10
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_order_revenue_refresh = true
```

```text
if C04
and small_supplier_theme_spike == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -30
and listed_company_contract_scope == false:
    route = Stage4C
    do_not_learn_price_only_spike = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 4
    avg_MFE_90D_pct: 21.44
    avg_MAE_90D_pct: -29.18
    false_positive_risk: high_if_supplier_or_preferred_bidder_rows_are_left_actionable
    verdict: adequate_only_with_C04_no_backfill_guard
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for project/policy heat
    eligible_trigger_count: 4
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: nuclear project evidence requires legal/final-contract bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C04 final-contract/no-backfill rule needed
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: supplier-theme rows without contract-scope bridge route to hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | DUKOVANY_FINAL_CONTRACT_NO_BACKFILL_HOLDOUT_V118 | 1 | 3 | 2 | 1 | 0 | 4 | 4 | 0 | 3 | false | false | 24 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 4
narrative_only_future_trigger_count: 2
narrative_only_or_rejected_count: 2
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
reused_case_count: 4
reused_case_ids:
  - C04|034020|Stage4B|2024-07-17
  - C04|052690|Stage2-Watch|2024-07-18
  - C04|051600|Stage2-Actionable|2024-09-12
  - C04|457550|Stage4C|2024-07-18
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_trigger_count: 2
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - no_backfill_later_evidence
  - C04_final_contract_no_backfill_gate
residual_error_types_found:
  - preferred_bidder_without_final_contract
  - direct_scope_without_legal_cash_bridge
  - supplier_theme_price_only_spike
  - final_contract_backfill_risk
new_axis_proposed: null
existing_axis_strengthened:
  - C04_FINAL_CONTRACT_NO_BACKFILL_REQUIREMENT_V118_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after additional C04 candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_future_trigger_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"117","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","new_independent_case_count":0,"reused_case_count":4,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_trigger_count":2,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","no_backfill_later_evidence","C04_final_contract_no_backfill_gate"],"residual_error_types_found":["preferred_bidder_without_final_contract","direct_scope_without_legal_cash_bridge","supplier_theme_price_only_spike","final_contract_backfill_risk"],"loop_contribution_label":"duplicate_low_value_loop_with_future_trigger_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R1/C04 loop 117 as holdout validation only. Batch it with C04 loops 113~116 and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C04 final-contract no-backfill gate and supplier-theme hard 4C guard. When stock-web shards are accessible, compute separate 30D/90D/180D windows from the final-contract event date; do not backfill later final-contract evidence into 2024 preferred-bidder triggers. Also reprice additional C04 candidates such as 비에이치아이(083650) and 우진(105840) before counting them as new independent evidence.
```

---

## 15. Next research state

```yaml
completed_round: R1
completed_loop: 118
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```
