# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R9
selected_loop: 108
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: HOLDOUT_VALIDATION_V108_VOLUME_MIX_MARGIN_GATE_VS_VALUEUP_PARTS_LOGISTICS_THEME_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 005850/2024: cache_miss_or_not_recomputed_this_turn
    - 064960/2024: cache_miss_or_not_recomputed_this_turn
    - 015750/2024: cache_miss_or_not_recomputed_this_turn
    - 161390/2024: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - volume_mix_margin_customer_order_gate
  - shareholder_return_valueup_reclassification_guard
  - supplier_logistics_local_4B_refresh_guard
  - generic_parts_hard_4C_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` remains Priority 0 in the no-repeat index. The v12 scheduler maps C29 to `R9 / L3_BATTERY_EV_GREEN_MOBILITY`.

This file continues the local C29 sequence after `R9/C29 loop 107`; selected loop is therefore `108`.

This is a **dedupe-aware holdout validation** MD. It does not claim fresh independent stock-web evidence because additional C29 candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C29 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C29 should not reward the word `mobility`. It should reward operating torque that reaches the income statement.

```text
vehicle volume
→ product mix / ASP
→ utilization / customer order / logistics load
→ margin / revision / cash
→ price path validation
```

The repeating false-positive family is:

```text
auto label
parts label
mobility theme
shareholder-return / Value-up label
one-month parts blowoff
```

These are nearby signals, but C29 only survives when operating leverage is visible. A Value-up announcement can be real, but if the bridge is capital return rather than volume/mix/margin, C29 must cap and reclassify. A parts rally can be real, but only if customer volume, utilization, A/S margin, or logistics load converts into cash.

This holdout pass validates seven route types:

1. **OEM volume/mix/margin positive-control**
   - Keep Stage2 when volume, mix, ASP, margin and cash bridge validate.

2. **OEM Value-up label cap**
   - Cap C29 if shareholder-return language is not tied to operating bridge.

3. **Core parts / A/S slow positive**
   - Stage2 can open, but Green requires stronger margin/revision refresh.

4. **Logistics volume/margin local 4B**
   - Real bridge, but margin/cash refresh is needed.

5. **Subsystem supplier local 4B**
   - Customer-volume and margin refresh required.

6. **Generic parts hard 4C**
   - Low MFE and high MAE without bridge should hard block.

7. **Auto-parts theme blowoff**
   - Local 4B at first, then block if no durable bridge appears.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 7
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C29 holdout validation
    - no new production scoring
    - no new weight delta from this file alone
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
  - R9/C29 loops 103~107
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional C29 candidate shards were not recomputed in this execution
  - exact duplicate C29 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R9","selected_loop":108,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_PRODUCT_MIX_MARGIN_OPERATING_LEVERAGE_POSITIVE_CONTROL","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":93000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C29 positive-control row from loops 103~107 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"OEM_mix_margin_positive_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","non_price_bridge":"OEM volume, product mix, ASP, margin and shareholder-return bridge","score_alignment":"keep Stage2; allow Yellow only while mix/margin bridge remains refreshed"}
{"row_type":"trigger","selected_round":"R9","selected_loop":108,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_SHAREHOLDER_RETURN_LABEL_WITHOUT_C29_OPERATING_BRIDGE_CAP","symbol":"005380","name":"현대차","trigger_type":"Stage2","entry_date":"2024-08-28","entry_price":259000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.09,"MAE_30D_pct":-14.48,"MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"MFE_180D_pct":3.09,"MAE_180D_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|005380|Stage2|2024-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_valueup_cap","reuse_reason":"same C29 Value-up label cap row from loops 104~107 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"OEM_valueup_label_cap","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2|2024-08-28","non_price_bridge":"shareholder-return intent existed, but C29 volume/mix/margin operating bridge did not validate","score_alignment":"cap C29 contribution; reclassify shareholder-return bridge to C21/C31 if confirmed"}
{"row_type":"trigger","selected_round":"R9","selected_loop":108,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CORE_PARTS_MODULE_AS_MARGIN_SLOW_POSITIVE_CONTROL","symbol":"012330","name":"현대모비스","trigger_type":"Stage2-Actionable","entry_date":"2024-10-16","entry_price":241500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.56,"MAE_30D_pct":-2.69,"MFE_90D_pct":11.18,"MAE_90D_pct":-2.69,"MFE_180D_pct":19.67,"MAE_180D_pct":-3.52,"forward_high_30d":267000,"forward_low_30d":235000,"forward_high_90d":268500,"forward_low_90d":235000,"forward_high_180d":289000,"forward_low_180d":233000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|012330|Stage2-Actionable|2024-10-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_slow_positive","reuse_reason":"same C29 module/A/S row from loops 104~107","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"parts_AS_slow_positive","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2-Actionable|2024-10-16","non_price_bridge":"module/core-parts/A/S profitability and future mobility parts bridge","score_alignment":"Stage2 can open, but Green requires stronger margin/revision refresh"}
{"row_type":"trigger","selected_round":"R9","selected_loop":108,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOGISTICS_VOLUME_MARGIN_CASH_BRIDGE_LOCAL_4B","symbol":"086280","name":"현대글로비스","trigger_type":"Stage4B","entry_date":"2024-10-16","entry_price":123900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.82,"MAE_30D_pct":-9.52,"MFE_90D_pct":21.87,"MAE_90D_pct":-9.93,"MFE_180D_pct":21.87,"MAE_180D_pct":-15.25,"forward_high_30d":127400,"forward_low_30d":112100,"forward_high_90d":151000,"forward_low_90d":111600,"forward_high_180d":151000,"forward_low_180d":105000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|086280|Stage4B|2024-10-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_logistics_4B","reuse_reason":"same C29 logistics local-4B row from loops 104~107","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"logistics_local_4B","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|086280|Stage4B|2024-10-16","non_price_bridge":"finished-vehicle logistics/PCC volume, shipping utilization and margin bridge","score_alignment":"local 4B until logistics margin/cash bridge refreshes"}
{"row_type":"trigger","selected_round":"R9","selected_loop":108,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_SUBSYSTEM_SUPPLIER_CUSTOMER_VOLUME_MARGIN_LOCAL_4B","symbol":"204320","name":"HL만도","trigger_type":"Stage4B","entry_date":"2024-04-29","entry_price":38350,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.38,"MAE_30D_pct":-5.48,"MFE_90D_pct":30.38,"MAE_90D_pct":-19.56,"MFE_180D_pct":30.38,"MAE_180D_pct":-19.56,"forward_high_30d":50000,"forward_low_30d":36250,"forward_high_90d":50000,"forward_low_90d":30850,"forward_high_180d":50000,"forward_low_180d":30850,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|204320|Stage4B|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_supplier_4B","reuse_reason":"same C29 subsystem supplier 4B row from loops 104~107 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"subsystem_supplier_local_4B","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage4B|2024-04-29","non_price_bridge":"ADAS/steering/brake subsystem supplier leverage, but customer-volume and margin refresh required","score_alignment":"local 4B until customer-volume, order and margin bridge refresh"}
{"row_type":"trigger","selected_round":"R9","selected_loop":108,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"GENERIC_PARTS_LABEL_LOW_MFE_HIGH_MAE_HARD_4C","symbol":"011210","name":"현대위아","trigger_type":"Stage4C","entry_date":"2024-09-13","entry_price":51600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.26,"MAE_30D_pct":-8.62,"MFE_90D_pct":4.26,"MAE_90D_pct":-28.20,"MFE_180D_pct":4.26,"MAE_180D_pct":-28.49,"forward_high_30d":53800,"forward_low_30d":47150,"forward_high_90d":53800,"forward_low_90d":37050,"forward_high_180d":53800,"forward_low_180d":36900,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|011210|Stage4C|2024-09-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C29 generic parts hard-block row from loops 104~107 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"generic_parts_hard_4C","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|011210|Stage4C|2024-09-13","non_price_bridge":"engine/module/machine-tool parts label without durable margin, customer-volume, revision or cash bridge","score_alignment":"hard 4C; label-only parts exposure fails"}
{"row_type":"trigger","selected_round":"R9","selected_loop":108,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_THEME_BLOWOFF_LOCAL_4B_THEN_BLOCK","symbol":"010690","name":"화신","trigger_type":"Stage4B","entry_date":"2024-06-12","entry_price":11690,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.93,"MAE_30D_pct":-4.53,"MFE_90D_pct":35.93,"MAE_90D_pct":-30.28,"MFE_180D_pct":35.93,"MAE_180D_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|010690|Stage4B|2024-06-12","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_theme_4B_to_4C","reuse_reason":"same C29 theme blowoff row from loops 103~107","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"theme_blowoff_local_4B_to_block","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|010690|Stage4B|2024-06-12","non_price_bridge":"auto-parts theme/volume label without durable customer-volume or margin bridge","score_alignment":"local 4B only; hard block if bridge does not refresh"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R9","selected_loop":108,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_NEW_SUPPLIER_TIRE_LOGISTICS_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["005850","064960","015750","161390"],"candidate_names":["에스엘","SNT모티브","성우하이텍","한국타이어앤테크놀로지"],"why_not_trigger_row_now":"uncached or not-recomputed stock-web symbol shards prevented fresh 30D/90D/180D MFE/MAE in this execution","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C29 evidence"}
```

---

## 6. Case analysis

### 6.1 Kia / 000270 — OEM bridge positive-control

Kia validates the C29 bridge: volume, mix, ASP, margin and cash conversion.

```yaml
entry_close: 93000
90D_MFE_MAE: +45.16 / -7.42
180D_MFE_MAE: +45.16 / -7.42
route: KeepStage2
```

### 6.2 Hyundai Motor / 005380 — Value-up cap

Shareholder-return can be real, but it is not C29 unless operating leverage is visible.

```yaml
entry_close: 259000
90D_MFE_MAE: +3.09 / -22.78
180D_MFE_MAE: +3.09 / -32.12
route: Stage2 / cap
```

### 6.3 Hyundai Mobis / 012330 — slow positive

Module/core-parts/A/S profitability is valid but slow. Green requires stronger revision/margin refresh.

```yaml
entry_close: 241500
90D_MFE_MAE: +11.18 / -2.69
180D_MFE_MAE: +19.67 / -3.52
route: Stage2-Actionable with refresh requirement
```

### 6.4 Hyundai Glovis / 086280 — logistics local 4B

The logistics/PCC volume bridge exists, but needs margin/cash refresh.

```yaml
entry_close: 123900
90D_MFE_MAE: +21.87 / -9.93
180D_MFE_MAE: +21.87 / -15.25
route: Stage4B
```

### 6.5 HL Mando / 204320 — supplier local 4B

Subsystem supplier bridge needs customer-volume and margin proof before Green.

```yaml
entry_close: 38350
90D_MFE_MAE: +30.38 / -19.56
180D_MFE_MAE: +30.38 / -19.56
route: Stage4B
```

### 6.6 Hyundai Wia / 011210 — generic parts hard 4C

Generic parts vocabulary without bridge failed.

```yaml
entry_close: 51600
90D_MFE_MAE: +4.26 / -28.20
180D_MFE_MAE: +4.26 / -28.49
route: Stage4C
```

### 6.7 Hwashin / 010690 — theme blowoff 4B to block

Theme MFE does not prove durable volume/margin bridge.

```yaml
entry_close: 11690
90D_MFE_MAE: +35.93 / -30.28
180D_MFE_MAE: +35.93 / -47.39
route: Stage4B -> block if no refresh
```

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 7
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 3
counterexample_count: 3
local_4B_watch_count: 3
hard_4C_count: 1
current_profile_error_count: 4
diversity_score_summary: "OEM positive, Value-up cap, parts/A/S slow positive, logistics 4B, supplier 4B, generic parts hard 4C, theme 4B-to-block covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C29 lesson |
|---|---:|---:|---:|---|
| 000270 | OEM positive | +45.16 / -7.42 | +45.16 / -7.42 | volume/mix/margin validates |
| 005380 | Value-up cap | +3.09 / -22.78 | +3.09 / -32.12 | shareholder-return not C29 bridge |
| 012330 | slow positive | +11.18 / -2.69 | +19.67 / -3.52 | parts/A/S bridge can survive |
| 086280 | logistics 4B | +21.87 / -9.93 | +21.87 / -15.25 | logistics bridge needs refresh |
| 204320 | supplier 4B | +30.38 / -19.56 | +30.38 / -19.56 | customer-volume refresh needed |
| 011210 | hard 4C | +4.26 / -28.20 | +4.26 / -28.49 | generic parts label fails |
| 010690 | 4B then block | +35.93 / -30.28 | +35.93 / -47.39 | theme MFE lacks durability |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":85,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":87,"stage_label_after":"Stage2-Actionable","changed_components":["revision_score"],"component_delta_explanation":"OEM volume/mix/margin bridge validated with controlled MAE.","MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"score_return_alignment_label":"OEM_margin_positive_control","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":47,"stage_label_after":"Stage2_cap_reclassify_if_capital_bridge","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Shareholder-return intent did not validate C29 operating leverage; cap and reclassify if capital-return bridge is confirmed elsewhere.","MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"score_return_alignment_label":"Valueup_label_without_C29_bridge","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"012330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":73,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":[],"component_delta_explanation":"Parts/A/S profitability bridge is valid but needs stronger revision and margin refresh before Green.","MFE_90D_pct":11.18,"MAE_90D_pct":-2.69,"score_return_alignment_label":"parts_AS_slow_positive","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"086280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":68,"stage_label_after":"Stage4B_logistics_refresh","changed_components":["relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Logistics/PCC bridge exists but margin/cash refresh remains required.","MFE_90D_pct":21.87,"MAE_90D_pct":-9.93,"score_return_alignment_label":"logistics_bridge_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":75,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":65,"stage_label_after":"Stage4B_supplier_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Subsystem bridge requires customer-volume, order and margin refresh before Actionable or Green.","MFE_90D_pct":30.38,"MAE_90D_pct":-19.56,"score_return_alignment_label":"supplier_bridge_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Generic parts label lacked durable margin, customer-volume, revision or cash bridge.","MFE_90D_pct":4.26,"MAE_90D_pct":-28.20,"score_return_alignment_label":"generic_parts_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"010690","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":71,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":55,"stage_label_after":"Stage4B_then_block_if_no_refresh","changed_components":["contract_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Auto-parts theme blowoff produced MFE, but durable customer-volume/margin bridge was not proven and 90D/180D MAE was severe.","MFE_90D_pct":35.93,"MAE_90D_pct":-30.28,"score_return_alignment_label":"theme_blowoff_local_4B_then_block","current_profile_verdict":"current_profile_too_generous_if_actionable"}
```

---

## 9. Current calibrated profile stress test

The C29 operating-bridge gate held again:

```text
OEM mix/margin bridge
→ keep Stage2

Value-up label without operating bridge
→ cap / reclassify

parts/A/S or logistics bridge
→ Stage2 or local 4B depending on path

generic parts label
→ hard 4C

theme blowoff
→ local 4B then block if no bridge refresh
```

### Rule candidate retained, not newly proposed

```text
C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V108_HELD_OUT

if C29
and auto_OEM_mobility_parts_or_valueup_label == true
and company_specific_volume_mix_margin_customer_order_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2
```

```text
if C29
and OEM_volume_mix_margin_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if C29
and logistics_or_parts_supplier_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -10:
    local_4B_watch = true
    block_stage3_green_until_customer_volume_margin_refresh = true
```

```text
if C29
and shareholder_return_or_valueup_label == true
and volume_mix_margin_bridge == false:
    cap_C29_contribution = true
    require_reclassification_to_C21_C31_if_financial_cash_bridge_exists = true
```

```text
if C29
and auto_parts_theme_label == true
and MFE_30D_pct >= +30
and MAE_90D_pct <= -25
and durable_customer_volume_margin_bridge == false:
    route = local_4B_then_block_if_no_refresh
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 7
    avg_MFE_90D_pct: 21.70
    avg_MAE_90D_pct: -17.27
    false_positive_risk: high_if_valueup_or_generic_parts_labels_are_left_actionable
    verdict: adequate_only_with_C29_operating_bridge_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for mobility/parts/value-up labels
    eligible_trigger_count: 7
    false_positive_rate: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L3 mobility names require volume/mix/customer-order/margin bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C29 requires operating leverage, not capital-return label
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: generic parts and theme blowoff rows without bridge route to 4C or 4B-then-block
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | V108_VOLUME_MIX_MARGIN_GATE | 3 | 3 | 3 | 1 | 0 | 7 | 7 | 0 | 4 | false | false | 27 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 7
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
reused_case_count: 7
reused_case_ids:
  - C29|000270|Stage2-Actionable|2024-01-25
  - C29|005380|Stage2|2024-08-28
  - C29|012330|Stage2-Actionable|2024-10-16
  - C29|086280|Stage4B|2024-10-16
  - C29|204320|Stage4B|2024-04-29
  - C29|011210|Stage4C|2024-09-13
  - C29|010690|Stage4B|2024-06-12
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C29_volume_mix_margin_customer_order_gate
residual_error_types_found:
  - valueup_without_operating_bridge
  - generic_parts_label_without_bridge
  - supplier_bridge_requires_refresh
  - theme_blowoff_without_durable_customer_volume
new_axis_proposed: null
existing_axis_strengthened:
  - C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V108_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after additional C29 candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"108","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":0,"reused_case_count":7,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C29_volume_mix_margin_customer_order_gate"],"residual_error_types_found":["valueup_without_operating_bridge","generic_parts_label_without_bridge","supplier_bridge_requires_refresh","theme_blowoff_without_durable_customer_volume"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R9/C29 loop 108 as holdout validation only. Batch it with C29 loops 100~107 and adjacent R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C29 volume/mix/margin/customer-order gate, but do not create a new weight delta from this loop because no new independent case was added. Future research should reprice 에스엘(005850), SNT모티브(064960), 성우하이텍(015750), 한국타이어앤테크놀로지(161390) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R9
completed_loop: 108
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
```
