# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 117
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: STRATEGIC_RESOURCE_POLICY_OFFTAKE_PROCESSING_CASH_BRIDGE_HOLDOUT_V117_SMELTER_COPPER_GAS_ALUMINIUM_GOVERNANCE_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 036460/2024: reused_from_prior_local_C16_loop_116_exploration_policy_4B
    - 010130/2024: reused_from_prior_local_C16_C32_governance_contamination_row
    - 011790/2024: reused_from_prior_local_C16_C15_C17_battery_material_4B
    - 103140/2024: reused_from_prior_local_C16_C15_processing_4B
    - 025820/2024: reused_from_prior_local_C16_copper_label_hard_4C
    - 021050/2024: reused_from_prior_local_C16_copper_alloy_hard_4C
    - 004020/2024: reused_from_prior_local_C16_steel_supply_security_hard_4C
    - 006110/2024: reused_from_prior_local_C16_C15_foil_4B
    - 018470/2024: reused_from_prior_local_C16_C15_aluminium_hard_4C
    - 005490/2024: not_recomputed_this_turn_future_steel_material_resource_candidate
    - 003670/2024: not_recomputed_this_turn_future_battery_material_resource_candidate
    - 001120/2024: not_recomputed_this_turn_future_resource_trading_candidate
    - 014680/2024: not_recomputed_this_turn_future_specialty_policy_supply_candidate
    - 178920/2024: not_recomputed_this_turn_future_advanced_material_supply_candidate
    - 096770/2024: not_recomputed_this_turn_future_resource_energy_boundary
    - 010060/2024: not_recomputed_this_turn_C15_C17_polysilicon_boundary
    - 009830/2024: not_recomputed_this_turn_C15_C17_solar_policy_boundary
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - strategic_resource_policy_to_offtake_processing_cash_bridge_gate
  - smelter_governance_contamination_cap
  - copper_processing_false_positive_guard
  - exploration_policy_headline_no_cashflow_guard
  - aluminium_foil_high_MAE_local_4B_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` remains a Priority 0 archetype. The current no-repeat index marks C16 as under the 30-row minimum, and the v12 scheduler maps C15~C17 to `R4 / L4_MATERIALS_SPREAD_RESOURCE`.

This file continues the local C16 sequence after `R4/C16 loop 116`; selected loop is therefore `117`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct fresh C16 strategic-resource/policy-supply candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C16/C15/C32 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

```yaml
loop_117_note:
  independence_status: duplicate_holdout_only
  fresh_reprice_status: not_recomputed_this_execution
  reason: C16 remains under-covered, but this run reuses prior C16/C15/C32 boundary rows and must not create a new weight delta.
```


C16 should not reward a resource word or policy flare by itself.

C16 should reward strategic resource exposure only when the headline reaches a company-specific execution bridge:

```text
strategic resource / critical mineral / smelter / exploration / offtake / supply-security policy
→ reserve or recoverability confirmation
→ offtake / customer / processing allocation
→ refining / smelting / utilization / margin
→ cash conversion
→ price path validation
```

The recurring false positive is:

```text
resource policy headline
commodity label
critical mineral vocabulary
battery material event
governance/tender control premium
small copper/alloy theme
```

These may move price, but C16 only scores the part that reaches the operating or cash ledger. A mine without reserve economics is a rumor in the ground. A smelter without margin/offtake bridge is an address, not a cashflow. A copper theme without customer conversion is just a shiny label.

This holdout pass validates seven route types:

1. **Exploration / resource policy headline**
   - Large MFE can occur.
   - Without reserve, commerciality, recoverability, capex and cashflow bridge, it remains local 4B.

2. **Critical smelter with governance contamination**
   - Strategic resource company may be valid.
   - Tender/control-premium mechanics must cap C16 and reclassify to C32 if dominant.

3. **Smelter supply-tightness positive with contamination cap**
   - Stage2 can open if supply tightness and smelting margin bridge exist.
   - Governance window blocks clean Green learning.

4. **Battery/material event contamination**
   - High MFE can be real.
   - If dominant bridge is battery event rather than resource offtake, C16 contribution is capped.

5. **Dual-use copper processing bridge**
   - Processing plus defense/industrial demand can support C16, but high MAE requires local 4B.

6. **Copper/alloy label false positives**
   - Small-cap copper processing/alloy labels without strategic customer/offtake/cash bridge route to hard 4C or false-positive block.

7. **Aluminium foil / rolling commodity beta**
   - High-MFE foil rows stay 4B without customer/utilization/margin bridge; low-MFE rolling rows hard block.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 10
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C16 holdout validation
    - resource-policy-to-cash bridge gate
    - governance contamination reclassification
    - copper/alloy false-positive guard
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
  - R4/C16 loop 112
  - R4/C16 loop 113
  - R4/C16 loop 114
  - R4/C16 loop 115
  - R4/C16 loop 116
  - R4/C15 loops 105~108
  - R12/C32 governance/tender rows
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C16 strategic-resource/policy-supply candidate shards were not recomputed in this execution
  - exact duplicate C16 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"EXPLORATION_POLICY_HEADLINE_WITHOUT_CONFIRMED_RESERVE_CASHFLOW_LOCAL_4B","symbol":"036460","name":"한국가스공사","trigger_type":"Stage4B","entry_date":"2024-06-03","entry_price":38700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":66.67,"MAE_30D_pct":-3.49,"MFE_90D_pct":66.67,"MAE_90D_pct":-5.68,"MFE_180D_pct":66.67,"MAE_180D_pct":-23.51,"forward_high_30d":64500,"forward_low_30d":37350,"forward_high_90d":64500,"forward_low_90d":36500,"forward_high_180d":64500,"forward_low_180d":29600,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|036460|Stage4B|2024-06-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same KOGAS exploration-policy row from C16 loop 114","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"exploration_policy_local_4B","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|036460|Stage4B|2024-06-03","non_price_bridge":"East Sea oil/gas exploration policy headline without confirmed reserve, commerciality, recoverability, regulatory-return or company cashflow bridge","score_alignment":"local 4B; block Green until reserve/commerciality/cash bridge is confirmed"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"ZINC_TC_COLLAPSE_SUPPLY_TIGHTNESS_SMELTER_BRIDGE_WITH_GOVERNANCE_CONTAMINATION_CAP","symbol":"010130","name":"고려아연","trigger_type":"Stage4B","entry_date":"2024-04-09","entry_price":469000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.40,"MAE_30D_pct":-3.94,"MFE_90D_pct":16.42,"MAE_90D_pct":-3.94,"MFE_180D_pct":68.66,"MAE_180D_pct":-3.94,"forward_high_30d":499000,"forward_low_30d":450500,"forward_high_90d":546000,"forward_low_90d":450500,"forward_high_180d":791000,"forward_low_180d":450500,"corporate_action_window_status":"governance_tender_event_contamination_after_2024_09_13","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|010130|Stage4B|2024-04-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_with_contamination_cap","reuse_reason":"same Korea Zinc supply-tightness row from C16 loop 112","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"smelter_supply_positive_with_governance_cap","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|Stage4B|2024-04-09","non_price_bridge":"zinc TC collapse and strategic smelter supply-tightness bridge, but later governance/tender event contaminates 180D interpretation","score_alignment":"Stage2 can open; keep local 4B/cap and do not learn later governance-driven 180D MFE as C16 Green"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"CRITICAL_SMELTER_STRATEGIC_RESOURCE_WITH_GOVERNANCE_TENDER_CONTAMINATION_CAP","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Watch","entry_date":"2024-09-13","entry_price":666000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":131.68,"MAE_30D_pct":0.00,"MFE_90D_pct":131.68,"MAE_90D_pct":0.00,"MFE_180D_pct":131.68,"MAE_180D_pct":0.00,"forward_high_30d":1543000,"forward_low_30d":666000,"forward_high_90d":1543000,"forward_low_90d":666000,"forward_high_180d":1543000,"forward_low_180d":666000,"corporate_action_window_status":"governance_tender_mechanics_dominate","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|010130|Stage2-Watch|2024-09-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_reclassification_cap","reuse_reason":"same Korea Zinc governance-contamination row from C16 loop 114","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"governance_contamination_cap","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|Stage2-Watch|2024-09-13","non_price_bridge":"critical smelter/resource company, but selected move is dominated by tender/control-premium mechanics rather than offtake or smelting margin bridge","score_alignment":"cap C16 contribution; reclassify dominant bridge to C32 governance/tender mechanics"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"BATTERY_MATERIAL_EVENT_CONTAMINATION_NOT_RESOURCE_OFFTAKE_BRIDGE","symbol":"011790","name":"SKC","trigger_type":"Stage4B","entry_date":"2024-05-23","entry_price":117000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":70.94,"MAE_30D_pct":0.00,"MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"MFE_180D_pct":70.94,"MAE_180D_pct":-20.17,"forward_high_30d":200000,"forward_low_30d":117000,"forward_high_90d":200000,"forward_low_90d":107600,"forward_high_180d":200000,"forward_low_180d":93400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|011790|Stage4B|2024-05-23","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_event_contamination_4B","reuse_reason":"same SKC battery/material event contamination row from C16 loop 114","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"event_contamination_local_4B","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|011790|Stage4B|2024-05-23","non_price_bridge":"battery/material event-driven MFE rather than confirmed strategic resource offtake, reserve, or processing margin bridge","score_alignment":"local 4B; cap C16 contribution and require reclassification if battery/material event bridge dominates"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"DUAL_USE_COPPER_PROCESSING_OFFTAKE_MARGIN_REUSED_POSITIVE_CONTROL","symbol":"103140","name":"풍산","trigger_type":"Stage4B","entry_date":"2024-04-26","entry_price":62900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.44,"MAE_30D_pct":-10.17,"MFE_90D_pct":25.44,"MAE_90D_pct":-25.28,"MFE_180D_pct":25.44,"MAE_180D_pct":-26.63,"forward_high_30d":78900,"forward_low_30d":56500,"forward_high_90d":78900,"forward_low_90d":47000,"forward_high_180d":78900,"forward_low_180d":46150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|103140|Stage4B|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control_4B","reuse_reason":"same Poongsan positive control from C16 loops 113~114 and C15/C16 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"dual_use_processing_local_4B","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|103140|Stage4B|2024-04-26","non_price_bridge":"actual copper/non-ferrous processing plus defense dual-use supply relevance","score_alignment":"processing/offtake bridge can open Stage2, but high MAE requires local 4B and refreshed order/margin bridge"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_PROCESSING_LABEL_WITHOUT_OFFTAKE_OR_CASH_CONVERSION_BRIDGE","symbol":"025820","name":"이구산업","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":7880,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.85,"MAE_30D_pct":-33.88,"MFE_90D_pct":6.85,"MAE_90D_pct":-51.84,"MFE_180D_pct":6.85,"MAE_180D_pct":-55.01,"forward_high_30d":8420,"forward_low_30d":5210,"forward_high_90d":8420,"forward_low_90d":3795,"forward_high_180d":8420,"forward_low_180d":3545,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|025820|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Igu Industrial copper false-positive row from C16 loop 113","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"copper_label_hard_4C","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|025820|Stage4C|2024-05-20","non_price_bridge":"copper processing label without visible strategic offtake, customer allocation, processing-margin or cash conversion bridge","score_alignment":"hard 4C; low MFE and deep MAE reject Stage2 bonus"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"BRASS_COPPER_ALLOY_THEME_WITHOUT_STRATEGIC_CUSTOMER_BRIDGE","symbol":"021050","name":"서원","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":1916,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.65,"MAE_30D_pct":-28.18,"MFE_90D_pct":4.65,"MAE_90D_pct":-43.95,"MFE_180D_pct":4.65,"MAE_180D_pct":-48.17,"forward_high_30d":2005,"forward_low_30d":1377,"forward_high_90d":2005,"forward_low_90d":1074,"forward_high_180d":2005,"forward_low_180d":993,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|021050|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Seowon copper/alloy false-positive row from C16 loop 113","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"alloy_label_hard_4C","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|021050|Stage4C|2024-05-20","non_price_bridge":"brass/copper alloy vocabulary without strategic customer, offtake, processing-margin or cash bridge","score_alignment":"hard 4C; resource vocabulary failed"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"STEEL_SUPPLY_SECURITY_LABEL_WITHOUT_POLICY_OR_MARGIN_BRIDGE","symbol":"004020","name":"현대제철","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":32350,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.62,"MAE_30D_pct":-11.90,"MFE_90D_pct":0.62,"MAE_90D_pct":-24.73,"MFE_180D_pct":0.62,"MAE_180D_pct":-38.49,"forward_high_30d":32550,"forward_low_30d":28500,"forward_high_90d":32550,"forward_low_90d":24350,"forward_high_180d":32550,"forward_low_180d":19900,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|004020|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Hyundai Steel supply-security false-positive row from C16 loop 113","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"generic_steel_supply_label_hard_4C","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|004020|Stage4C|2024-05-20","non_price_bridge":"generic steel supply/security or value label without strategic policy, offtake, margin or cash bridge","score_alignment":"hard 4C; strategic-material vocabulary also fails without company-specific bridge"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"ALUMINIUM_BATTERY_FOIL_HIGH_MFE_HIGH_MAE_LOCAL_4B","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage4B","entry_date":"2024-05-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.34,"MAE_30D_pct":-7.28,"MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"MFE_180D_pct":28.34,"MAE_180D_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|006110|Stage4B|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_foil_4B","reuse_reason":"same Sam-A Aluminium resource-label high-MAE row from C16 loop 112 and C15 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"foil_high_MAE_local_4B","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006110|Stage4B|2024-05-20","non_price_bridge":"aluminium battery-foil material/resource label without refreshed customer order, utilization, ASP/margin or cash bridge","score_alignment":"local 4B only; block Green until order/utilization/margin bridge refresh"}
{"row_type":"trigger","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"ALUMINIUM_ROLLING_COMMODITY_BETA_LOW_MFE_HIGH_MAE_HARD_4C","symbol":"018470","name":"조일알미늄","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":2470,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.29,"MAE_30D_pct":-17.41,"MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"MFE_180D_pct":7.29,"MAE_180D_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C16|018470|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Choil Aluminium resource-label hard counterexample from C16 loop 112 and C15 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"aluminium_commodity_beta_hard_4C","novelty_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|018470|Stage4C|2024-05-20","non_price_bridge":"aluminium rolling commodity beta label without company-specific strategic offtake, volume, margin or FCF bridge","score_alignment":"hard 4C; low MFE and high MAE reject resource-policy bridge"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R4","selected_loop":117,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_NEW_RESOURCE_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["005490","003670","001120","009830","096770"],"candidate_names":["POSCO홀딩스","포스코퓨처엠","LX인터내셔널","한화솔루션","SK이노베이션"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C16 evidence; distinguish offtake/refining cash bridge from generic resource or battery event labels"}
```

---

## 6. Case analysis

### 6.1 KOGAS / 036460 — exploration policy local 4B

```yaml
entry_price: 38700
90D_MFE_MAE: +66.67 / -5.68
180D_MFE_MAE: +66.67 / -23.51
route: Stage4B
```

The price path shows how powerful a resource headline can be. But C16 should not learn it as Green because reserve, recoverability, regulated return and company cashflow bridge were not confirmed at trigger date.

### 6.2 Korea Zinc / 010130 — strategic smelter, but contribution cap

```yaml
2024-04-09:
  90D_MFE_MAE: +16.42 / -3.94
  180D_MFE_MAE: +68.66 / -3.94
  route: Stage4B with governance contamination cap

2024-09-13:
  90D_MFE_MAE: +131.68 / 0.00
  route: C16 cap / reclassify C32
```

The company is strategically important, but the later move is dominated by tender/control-premium mechanics. C16 should not steal C32’s cash-exit/tender bridge.

### 6.3 SKC / 011790 — battery/material event contamination

```yaml
entry_price: 117000
90D_MFE_MAE: +70.94 / -8.03
180D_MFE_MAE: +70.94 / -20.17
route: Stage4B / reclassification watch
```

This is a high-MFE event that still needs dominant-driver discipline. If the bridge is battery-material or customer event rather than resource offtake/processing cashflow, C16 contribution must be capped.

### 6.4 Poongsan / 103140 — processing/offtake positive but 4B watch

```yaml
entry_price: 62900
90D_MFE_MAE: +25.44 / -25.28
180D_MFE_MAE: +25.44 / -26.63
route: Stage4B
```

Poongsan keeps the guardrail honest: actual copper/non-ferrous processing plus dual-use supply relevance can support C16. High MAE still blocks clean Green.

### 6.5 Copper/alloy and steel label hard 4C rows

```yaml
hard_4C_rows:
  - 025820: copper processing label, no strategic offtake/cash bridge.
  - 021050: brass/copper alloy theme, no strategic customer bridge.
  - 004020: steel supply/security label, no margin/offtake bridge.
  - 018470: aluminium rolling beta, low MFE and deep MAE.
```

The resource word is not enough. C16 needs a cash bridge.

### 6.6 Aluminium foil 4B row

```yaml
entry_price: 75500
90D_MFE_MAE: +28.34 / -47.55
180D_MFE_MAE: +28.34 / -53.58
route: Stage4B
```

High MFE proves tradability, not durability. Without customer/order/utilization/margin refresh, the row stays in 4B.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 10
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 10
calibration_usable_trigger_count: 10
positive_case_count: 3
counterexample_count: 7
local_4B_watch_count: 5
hard_4C_count: 5
wrong_archetype_reclassification_count: 2
current_profile_error_count: 7
diversity_score_summary: "exploration policy, smelter supply/tender contamination, battery-material event contamination, dual-use copper processing, small-cap copper/alloy false positives, aluminium foil 4B and aluminium beta hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C16 lesson |
|---|---:|---:|---:|---|
| 036460 | exploration 4B | +66.67 / -5.68 | +66.67 / -23.51 | policy headline lacks reserve/cash bridge |
| 010130 | smelter supply cap | +16.42 / -3.94 | +68.66 / -3.94 | positive but governance contamination |
| 010130 | governance cap | +131.68 / 0.00 | +131.68 / 0.00 | tender mechanics belong to C32 |
| 011790 | event contamination 4B | +70.94 / -8.03 | +70.94 / -20.17 | battery event not resource offtake |
| 103140 | processing 4B | +25.44 / -25.28 | +25.44 / -26.63 | real bridge, high-MAE watch |
| 025820 | copper label 4C | +6.85 / -51.84 | +6.85 / -55.01 | no offtake/cash bridge |
| 021050 | alloy label 4C | +4.65 / -43.95 | +4.65 / -48.17 | no strategic customer bridge |
| 004020 | steel label 4C | +0.62 / -24.73 | +0.62 / -38.49 | generic supply label fails |
| 006110 | foil 4B | +28.34 / -47.55 | +28.34 / -53.58 | utilization/margin refresh needed |
| 018470 | aluminium beta 4C | +7.29 / -41.30 | +7.29 / -44.70 | commodity beta fails |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"036460","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":55,"stage_label_after":"Stage4B_local_watch","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","legal_or_contract_risk_score"],"component_delta_explanation":"Exploration headline created MFE, but reserve/commerciality/cash bridge was missing.","MFE_90D_pct":66.67,"MAE_90D_pct":-5.68,"score_return_alignment_label":"exploration_policy_local_4B","current_profile_verdict":"current_profile_too_generous_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"010130","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":63,"stage_label_after":"Stage4B_governance_contamination_cap","changed_components":["contract_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Supply-tightness bridge can open watch, but later governance/tender event contaminates full-window interpretation.","MFE_90D_pct":16.42,"MAE_90D_pct":-3.94,"score_return_alignment_label":"smelter_supply_positive_with_contamination_cap","current_profile_verdict":"requires_C32_contamination_cap"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"010130","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":1,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":46,"stage_label_after":"Reclassify_C32","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"The selected 2024-09-13 move is governance/tender mechanics, not C16 offtake or smelting margin.","MFE_90D_pct":131.68,"MAE_90D_pct":0.00,"score_return_alignment_label":"governance_tender_contamination_cap","current_profile_verdict":"requires_reclassification"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"011790","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":58,"stage_label_after":"Stage4B_event_contamination","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"High MFE was dominated by battery/material event mechanics rather than strategic resource offtake/cash bridge.","MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"score_return_alignment_label":"battery_material_event_contamination","current_profile_verdict":"cap_or_reclassify"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"103140","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":68,"stage_label_after":"Stage4B_processing_refresh","changed_components":["relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Real processing bridge exists, but high MAE requires order/margin/cash refresh before Actionable/Green.","MFE_90D_pct":25.44,"MAE_90D_pct":-25.28,"score_return_alignment_label":"processing_bridge_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"025820","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Copper processing label lacked strategic offtake/customer/cash bridge and suffered severe MAE.","MFE_90D_pct":6.85,"MAE_90D_pct":-51.84,"score_return_alignment_label":"copper_label_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"021050","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":56,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Brass/alloy theme had no strategic customer or offtake bridge.","MFE_90D_pct":4.65,"MAE_90D_pct":-43.95,"score_return_alignment_label":"alloy_label_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"004020","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Generic steel supply/security label did not convert into policy/offtake/margin bridge.","MFE_90D_pct":0.62,"MAE_90D_pct":-24.73,"score_return_alignment_label":"generic_steel_supply_label_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"006110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":71,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":56,"stage_label_after":"Stage4B_foil_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Foil/resource label had high MFE but margin/utilization bridge was unrefreshed and MAE severe.","MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"score_return_alignment_label":"foil_high_MAE_local_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"018470","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":41,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Aluminium rolling commodity beta lacked company-specific strategic offtake and price path rejected it.","MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"score_return_alignment_label":"aluminium_beta_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

---

## 9. Current calibrated profile stress test

The C16 strategic-resource-to-cash bridge gate held:

```text
exploration/resource policy headline
→ local 4B until reserve/commerciality/cash bridge

critical smelter supply tightness
→ Stage2 may open, but governance/tender contamination caps full-window learning

tender/control-premium mechanics
→ reclassify to C32

battery/material event-driven MFE
→ cap C16 and require dominant-driver reclassification

dual-use copper processing
→ local 4B if high MAE and margin/order refresh missing

small copper/alloy/steel labels
→ hard 4C without strategic customer/offtake/cash bridge

aluminium foil high-MFE high-MAE
→ local 4B, no Green

aluminium rolling low-MFE deep-MAE
→ hard 4C
```

### Rule candidate retained, not newly proposed

```text
C16_STRATEGIC_RESOURCE_POLICY_TO_OFFTAKE_PROCESSING_CASH_GATE_V117_HELD_OUT

if C16
and strategic_resource_policy_or_commodity_label == true
and reserve_offtake_processing_customer_margin_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C16
and exploration_policy_headline == true
and confirmed_reserve_commerciality_or_company_cashflow == false:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if C16
and governance_tender_control_premium_mechanics_dominate == true:
    cap_C16_contribution = true
    require_reclassification_to_C32 = true
```

```text
if C16
and resource_or_material_label == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -20
and refreshed_offtake_processing_margin_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C16
and commodity_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 10
    avg_MFE_90D_pct: 35.39
    avg_MAE_90D_pct: -25.16
    false_positive_risk: high_if_resource_labels_or_governance_contamination_are_left_actionable
    verdict: adequate_only_with_C16_resource_cash_bridge_and_reclassification_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for resource/commodity labels and vertical MFE
    eligible_trigger_count: 10
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L4 resource names require reserve/offtake/processing/margin/cash bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C16 requires strategic resource execution, not price flare
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: small-cap copper/alloy/commodity beta rows without strategic bridge route to hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | STRATEGIC_RESOURCE_POLICY_OFFTAKE_PROCESSING_CASH_BRIDGE_HOLDOUT_V117 | 3 | 7 | 5 | 5 | 0 | 10 | 10 | 0 | 7 | false | false | 18 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 10
calibration_usable_trigger_count: 10
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 10
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
reused_case_count: 10
reused_case_ids:
  - C16|036460|Stage4B|2024-06-03
  - C16|010130|Stage4B|2024-04-09
  - C16|010130|Stage2-Watch|2024-09-13
  - C16|011790|Stage4B|2024-05-23
  - C16|103140|Stage4B|2024-04-26
  - C16|025820|Stage4C|2024-05-20
  - C16|021050|Stage4C|2024-05-20
  - C16|004020|Stage4C|2024-05-20
  - C16|006110|Stage4B|2024-05-20
  - C16|018470|Stage4C|2024-05-20
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C16_resource_policy_to_offtake_processing_cash_gate
  - governance_contamination_reclassification_guard
residual_error_types_found:
  - exploration_policy_without_confirmed_cashflow
  - smelter_governance_tender_contamination
  - battery_material_event_wrong_bridge
  - copper_alloy_label_without_offtake
  - aluminium_commodity_beta_false_positive
new_axis_proposed: null
existing_axis_strengthened:
  - C16_STRATEGIC_RESOURCE_POLICY_TO_OFFTAKE_PROCESSING_CASH_GATE_V117_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C16 strategic-resource/policy-supply candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"117","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":0,"reused_case_count":10,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C16_resource_policy_to_offtake_processing_cash_gate","governance_contamination_reclassification_guard"],"residual_error_types_found":["exploration_policy_without_confirmed_cashflow","smelter_governance_tender_contamination","battery_material_event_wrong_bridge","copper_alloy_label_without_offtake","aluminium_commodity_beta_false_positive"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R4/C16 loop 117 as holdout validation only. Batch it with C16 loops 111~116, C15/C17 adjacent material rows, C32 governance-contamination rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C16 strategic-resource-policy-to-offtake-processing-cash bridge gate and governance/tender contamination reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should reprice POSCO홀딩스(005490), 포스코퓨처엠(003670), LX인터내셔널(001120), 한화솔루션(009830), SK이노베이션(096770) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R4
completed_loop: 117
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```
