# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R9
selected_loop: 105
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: HOLDOUT_VALIDATION_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_GATE_VS_VALUEUP_AND_PARTS_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - 064960: cache_miss
    - 005850: cache_miss
    - 015750: cache_miss
    - 161390: cache_miss
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This file is a C29 holdout / consolidation pass, not a new production-scoring patch. The latest index still puts `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` in Priority 0, and v12 maps C29 to `R9 / L3_BATTERY_EV_GREEN_MOBILITY`. Direct uncached symbol shards for additional candidates returned cache miss during this turn, so this MD does **not** pretend to add fresh stock-web rows. It consolidates current-session C29 rows already computed from `Songdaiki/stock-web` tradable OHLC and marks the loop as low new-weight evidence.

---

## 1. Research thesis

C29 should not reward mobility vocabulary by itself.

```text
auto / OEM / mobility / parts / logistics / Value-up label
→ must become volume, product mix, ASP, utilization, customer order, A/S margin, logistics margin, revision or cash
→ then price path decides Stage2, local 4B, or hard 4C
```

The holdout question is narrower than discovery:

```text
Does the existing C29 gate consistently separate:
1. OEM mix/margin positives,
2. supplier/logistics local 4B rows,
3. generic parts or Value-up label false positives?
```

The answer in this pass is yes, but because most rows are reused from the prior C29 loop, this file should be treated as **holdout validation / rule consolidation**, not new weight evidence.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 5
  actual_cases: 7
  source_archetypes:
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
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

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R9/C29 loop 103
  - R9/C29 loop 104
  - R13 accounting-trust loop 12
  - R13 Stage2 false-positive loop 10
  - R13 high-MAE loop 8
  - R13 4B/4C loop 103
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - uncached additional symbol shards returned cache miss in this turn
  - exact duplicate C29 keys should be deduped during batch ingest
  - this file is rule-consolidation evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R9","selected_loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_PRODUCT_MIX_MARGIN_OPERATING_LEVERAGE_POSITIVE_CONTROL","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":93000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C29 positive-control row from loop 104; used for holdout validation","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"reused_positive_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","non_price_bridge":"OEM volume, product mix, ASP, margin and shareholder-return bridge","score_alignment":"keep Stage2; allow Yellow only while mix/margin bridge remains refreshed"}
{"row_type":"trigger","selected_round":"R9","selected_loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_LABEL_WITHOUT_OPERATING_BRIDGE_CAP","symbol":"005380","name":"현대차","trigger_type":"Stage2","entry_date":"2024-08-28","entry_price":259000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.09,"MAE_30D_pct":-14.48,"MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"MFE_180D_pct":3.09,"MAE_180D_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|005380|Stage2|2024-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","reuse_reason":"same C29 boundary row from loop 104; used to validate value-up label cap","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"stage2_cap_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2|2024-08-28","non_price_bridge":"shareholder-return intent existed, but C29 volume/mix/margin operating bridge did not validate","score_alignment":"cap C29 contribution; reclassify shareholder-return bridge to C21/C31 if confirmed"}
{"row_type":"trigger","selected_round":"R9","selected_loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CORE_PARTS_MODULE_AS_MARGIN_BRIDGE_POSITIVE_CONTROL","symbol":"012330","name":"현대모비스","trigger_type":"Stage2-Actionable","entry_date":"2024-10-16","entry_price":241500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":10.56,"MAE_30D_pct":-2.69,"MFE_90D_pct":11.18,"MAE_90D_pct":-2.69,"MFE_180D_pct":19.67,"MAE_180D_pct":-3.52,"forward_high_30d":267000,"forward_low_30d":235000,"forward_high_90d":268500,"forward_low_90d":235000,"forward_high_180d":289000,"forward_low_180d":233000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|012330|Stage2-Actionable|2024-10-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_slow_positive","reuse_reason":"same C29 module/A/S bridge row from loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"reused_positive_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2-Actionable|2024-10-16","non_price_bridge":"module/core-parts/A/S profitability and future mobility parts bridge","score_alignment":"Stage2 can open, but Green requires stronger margin/revision refresh"}
{"row_type":"trigger","selected_round":"R9","selected_loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOGISTICS_VOLUME_MARGIN_BRIDGE_LOCAL_4B","symbol":"086280","name":"현대글로비스","trigger_type":"Stage4B","entry_date":"2024-10-16","entry_price":123900,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.82,"MAE_30D_pct":-9.52,"MFE_90D_pct":21.87,"MAE_90D_pct":-9.93,"MFE_180D_pct":21.87,"MAE_180D_pct":-15.25,"forward_high_30d":127400,"forward_low_30d":112100,"forward_high_90d":151000,"forward_low_90d":111600,"forward_high_180d":151000,"forward_low_180d":105000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|086280|Stage4B|2024-10-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same logistics 4B bridge row from loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"reused_local_4B","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|086280|Stage4B|2024-10-16","non_price_bridge":"finished-vehicle logistics/PCC volume, shipping utilization and margin bridge","score_alignment":"local 4B until logistics margin/cash bridge refreshes"}
{"row_type":"trigger","selected_round":"R9","selected_loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_SUBSYSTEM_SUPPLIER_MARGIN_REFRESH_LOCAL_4B","symbol":"204320","name":"HL만도","trigger_type":"Stage4B","entry_date":"2024-04-29","entry_price":38350,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":30.38,"MAE_30D_pct":-5.48,"MFE_90D_pct":30.38,"MAE_90D_pct":-19.56,"MFE_180D_pct":30.38,"MAE_180D_pct":-19.56,"forward_high_30d":50000,"forward_low_30d":36250,"forward_high_90d":50000,"forward_low_90d":30850,"forward_high_180d":50000,"forward_low_180d":30850,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|204320|Stage4B|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same subsystem supplier 4B row from loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"reused_local_4B","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage4B|2024-04-29","non_price_bridge":"ADAS/steering/brake subsystem supplier leverage, but customer-volume and margin refresh required","score_alignment":"local 4B until customer-volume, order and margin bridge refresh"}
{"row_type":"trigger","selected_round":"R9","selected_loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"GENERIC_PARTS_LABEL_LOW_MFE_HIGH_MAE_HARD_4C","symbol":"011210","name":"현대위아","trigger_type":"Stage4C","entry_date":"2024-09-13","entry_price":51600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.26,"MAE_30D_pct":-8.62,"MFE_90D_pct":4.26,"MAE_90D_pct":-28.20,"MFE_180D_pct":4.26,"MAE_180D_pct":-28.49,"forward_high_30d":53800,"forward_low_30d":47150,"forward_high_90d":53800,"forward_low_90d":37050,"forward_high_180d":53800,"forward_low_180d":36900,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|011210|Stage4C|2024-09-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same generic parts hard-block row from loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"reused_hard_4C","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|011210|Stage4C|2024-09-13","non_price_bridge":"engine/module/machine-tool parts label without durable margin, customer-volume, revision or cash bridge","score_alignment":"hard 4C; label-only parts exposure fails"}
{"row_type":"trigger","selected_round":"R9","selected_loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_THEME_BLOWOFF_LOCAL_4B_THEN_BLOCK","symbol":"010690","name":"화신","trigger_type":"Stage4B","entry_date":"2024-06-12","entry_price":11690,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":35.93,"MAE_30D_pct":-4.53,"MFE_90D_pct":35.93,"MAE_90D_pct":-30.28,"MFE_180D_pct":35.93,"MAE_180D_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|010690|Stage4B|2024-06-12","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_4B_to_4C","reuse_reason":"same theme blowoff row from loop 104","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"reused_local_4B_to_block","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|010690|Stage4B|2024-06-12","non_price_bridge":"auto-parts theme/volume label without durable customer-volume or margin bridge","score_alignment":"local 4B only; hard block if bridge does not refresh"}
```

---

## 5. Case analysis

### 5.1 Kia / 000270 — holdout positive control

Kia remains the clean C29 positive control.

```yaml
entry_close: 93000
90D_MFE_MAE: +45.16 / -7.42
180D_MFE_MAE: +45.16 / -7.42
route: KeepStage2
```

The model should preserve this because volume, mix, ASP and margin bridge are visible.

### 5.2 Hyundai Motor / 005380 — Value-up label cap

This is the boundary control. Shareholder-return intent is not enough for C29 if volume/mix/margin fails.

```yaml
entry_close: 259000
90D_MFE_MAE: +3.09 / -22.78
180D_MFE_MAE: +3.09 / -32.12
route: Stage2Cap
```

### 5.3 Hyundai Mobis / 012330 — slow positive bridge

Mobis validates a slower supplier/A/S bridge.

```yaml
entry_close: 241500
90D_MFE_MAE: +11.18 / -2.69
180D_MFE_MAE: +19.67 / -3.52
route: Stage2-Watch / slow positive
```

### 5.4 Hyundai Glovis / 086280 — logistics local 4B

Glovis has a real logistics bridge, but it remains local 4B until margin/cash refresh.

```yaml
entry_close: 123900
90D_MFE_MAE: +21.87 / -9.93
180D_MFE_MAE: +21.87 / -15.25
route: Local4B
```

### 5.5 HL Mando / 204320 — subsystem local 4B

A subsystem supplier bridge is not enough for Green without customer-volume and margin refresh.

```yaml
entry_close: 38350
90D_MFE_MAE: +30.38 / -19.56
180D_MFE_MAE: +30.38 / -19.56
route: Local4B
```

### 5.6 Hyundai Wia / 011210 — generic parts hard 4C

Generic parts vocabulary failed.

```yaml
entry_close: 51600
90D_MFE_MAE: +4.26 / -28.20
180D_MFE_MAE: +4.26 / -28.49
route: Stage4C
```

### 5.7 Hwashin / 010690 — 4B then block

Hwashin proves that early theme MFE cannot become Green without bridge refresh.

```yaml
entry_close: 11690
90D_MFE_MAE: +35.93 / -30.28
180D_MFE_MAE: +35.93 / -47.39
route: Local4B -> block if no refresh
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 7
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 3
counterexample_count: 3
local_4B_watch_count: 3
current_profile_error_count: 4
diversity_score_summary: "positive/control/cap/4B/4C covered, but all rows are reused holdout controls"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | holdout lesson |
|---|---:|---:|---:|---|
| 000270 | positive control | +45.16 / -7.42 | +45.16 / -7.42 | OEM mix/margin works |
| 005380 | cap control | +3.09 / -22.78 | +3.09 / -32.12 | Value-up label lacks C29 bridge |
| 012330 | slow positive | +11.18 / -2.69 | +19.67 / -3.52 | parts/A/S bridge is valid but slower |
| 086280 | local 4B | +21.87 / -9.93 | +21.87 / -15.25 | logistics bridge needs refresh |
| 204320 | local 4B | +30.38 / -19.56 | +30.38 / -19.56 | subsystem bridge needs customer-volume refresh |
| 011210 | hard 4C | +4.26 / -28.20 | +4.26 / -28.49 | generic parts label fails |
| 010690 | 4B -> block | +35.93 / -30.28 | +35.93 / -47.39 | theme MFE lacks durability |

---

## 7. Current calibrated profile stress test

The rule held up in holdout form:

```text
OEM mix/margin bridge -> keep Stage2
logistics / supplier bridge with drawdown -> local 4B
Value-up label without C29 operating bridge -> cap
generic parts label -> hard 4C
theme blowoff -> local 4B then block without refresh
```

### Rule candidate retained, not newly proposed

```text
C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V104_HELD_OUT

if C29
and auto_OEM_mobility_parts_or_valueup_label == true
and company_specific_volume_mix_margin_customer_order_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
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
and auto_parts_theme_label == true
and MFE_30D_pct >= +30
and MAE_90D_pct <= -25
and durable_customer_volume_margin_bridge == false:
    route = local_4B_then_block_if_no_refresh
```

---

## 8. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 7
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
new_axis_proposed: null
existing_axis_strengthened:
  - C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V104_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases, 3 counterexamples, and 4 residual-error holdout controls for R9/L3/C29."
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R9/C29 loop 105 as holdout validation only. Batch it with C29 loops 100~104 and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C29 volume/mix/margin/customer-order gate, but do not create a new weight delta from this loop because uncached additional symbol shards returned cache miss and no new independent case was added.
```

---

## 11. Next research state

```yaml
completed_round: R9
completed_loop: 105
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
