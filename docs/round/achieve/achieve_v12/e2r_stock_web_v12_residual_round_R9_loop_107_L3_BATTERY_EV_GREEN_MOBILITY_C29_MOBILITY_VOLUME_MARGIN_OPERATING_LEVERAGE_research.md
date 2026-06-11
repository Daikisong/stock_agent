# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R9
selected_loop: 107
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: HOLDOUT_VALIDATION_V107_VOLUME_MIX_MARGIN_GATE_VS_VALUEUP_PARTS_LOGISTICS_THEME_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - additional_C29_candidate_shards: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - volume_mix_margin_customer_order_gate
  - shareholder_return_valueup_reclassification_guard
  - supplier_logistics_local_4B_refresh_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` remains Priority 0 in the no-repeat index. The v12 scheduler maps C29 to `R9 / L3_BATTERY_EV_GREEN_MOBILITY`.

This file continues the local C29 sequence after `R9/C29 loop 106`; selected loop is therefore `107`.

This is a **dedupe-aware holdout validation** MD. It does not claim fresh independent stock-web evidence because additional C29 candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C29 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C29 should reward drivetrain torque reaching the wheels, not the word `mobility`.

```text
vehicle volume
→ product mix / ASP
→ utilization / customer order / logistics load
→ margin / revision / cash
→ price path validation
```

The recurring false-positive bucket is:

```text
auto label
parts label
mobility theme
shareholder-return / Value-up label
short theme blowoff
```

Those signals can be adjacent, but C29 needs a company-specific operating bridge. A Value-up announcement can be real, but if the bridge is payout/capital rather than volume/mix/margin, C29 must cap and reclassify. A parts rally can be real, but only if customer volume, utilization, A/S margin, or logistics load converts into cash.

This holdout pass validates seven route types:

1. **OEM volume/mix/margin positive-control**
   - Keep Stage2 when volume, mix, ASP, margin and cash bridge validate.

2. **OEM Value-up label cap**
   - Cap C29 if shareholder-return language is not tied to operating bridge.

3. **Core parts / A/S slow positive**
   - Stage2 can open, but Green requires stronger margin/revision refresh.

4. **Logistics volume/margin local 4B**
   - Real bridge, but refresh is needed.

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
  - R9/C29 loops 103~106
  - R13 accounting-trust loops 12~13
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
{"row_type":"trigger","selected_round":"R9","selected_loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_PRODUCT_MIX_MARGIN_OPERATING_LEVERAGE_POSITIVE_CONTROL","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":93000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same C29 positive-control row from loops 103~106 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"OEM_mix_margin_positive_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","non_price_bridge":"OEM volume, product mix, ASP, margin and shareholder-return bridge","score_alignment":"keep Stage2; allow Yellow only while mix/margin bridge remains refreshed"}
{"row_type":"trigger","selected_round":"R9","selected_loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_SHAREHOLDER_RETURN_LABEL_WITHOUT_C29_OPERATING_BRIDGE_CAP","symbol":"005380","name":"현대차","trigger_type":"Stage2","entry_date":"2024-08-28","entry_price":259000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.09,"MAE_30D_pct":-14.48,"MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"MFE_180D_pct":3.09,"MAE_180D_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|005380|Stage2|2024-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_valueup_cap","reuse_reason":"same C29 Value-up label cap row from loops 104~106 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"OEM_valueup_label_cap","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2|2024-08-28","non_price_bridge":"shareholder-return intent existed, but C29 volume/mix/margin operating bridge did not validate","score_alignment":"cap C29 contribution; reclassify shareholder-return bridge to C21/C31 if confirmed"}
{"row_type":"trigger","selected_round":"R9","selected_loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CORE_PARTS_MODULE_AS_MARGIN_SLOW_POSITIVE_CONTROL","symbol":"012330","name":"현대모비스","trigger_type":"Stage2-Actionable","entry_date":"2024-10-16","entry_price":241500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":10.56,"MAE_30D_pct":-2.69,"MFE_90D_pct":11.18,"MAE_90D_pct":-2.69,"MFE_180D_pct":19.67,"MAE_180D_pct":-3.52,"forward_high_30d":267000,"forward_low_30d":235000,"forward_high_90d":268500,"forward_low_90d":235000,"forward_high_180d":289000,"forward_low_180d":233000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|012330|Stage2-Actionable|2024-10-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_slow_positive","reuse_reason":"same C29 module/A/S row from loops 104~106","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"parts_AS_slow_positive","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2-Actionable|2024-10-16","non_price_bridge":"module/core-parts/A/S profitability and future mobility parts bridge","score_alignment":"Stage2 can open, but Green requires stronger margin/revision refresh"}
{"row_type":"trigger","selected_round":"R9","selected_loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOGISTICS_VOLUME_MARGIN_CASH_BRIDGE_LOCAL_4B","symbol":"086280","name":"현대글로비스","trigger_type":"Stage4B","entry_date":"2024-10-16","entry_price":123900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.82,"MAE_30D_pct":-9.52,"MFE_90D_pct":21.87,"MAE_90D_pct":-9.93,"MFE_180D_pct":21.87,"MAE_180D_pct":-15.25,"forward_high_30d":127400,"forward_low_30d":112100,"forward_high_90d":151000,"forward_low_90d":111600,"forward_high_180d":151000,"forward_low_180d":105000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|086280|Stage4B|2024-10-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_logistics_4B","reuse_reason":"same C29 logistics local-4B row from loops 104~106","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"logistics_local_4B","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|086280|Stage4B|2024-10-16","non_price_bridge":"finished-vehicle logistics/PCC volume, shipping utilization and margin bridge","score_alignment":"local 4B until logistics margin/cash bridge refreshes"}
{"row_type":"trigger","selected_round":"R9","selected_loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_SUBSYSTEM_SUPPLIER_CUSTOMER_VOLUME_MARGIN_LOCAL_4B","symbol":"204320","name":"HL만도","trigger_type":"Stage4B","entry_date":"2024-04-29","entry_price":38350,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":30.38,"MAE_30D_pct":-5.48,"MFE_90D_pct":30.38,"MAE_90D_pct":-19.56,"MFE_180D_pct":30.38,"MAE_180D_pct":-19.56,"forward_high_30d":50000,"forward_low_30d":36250,"forward_high_90d":50000,"forward_low_90d":30850,"forward_high_180d":50000,"forward_low_180d":30850,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|204320|Stage4B|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_supplier_4B","reuse_reason":"same C29 subsystem supplier 4B row from loops 104~106 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"subsystem_supplier_local_4B","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage4B|2024-04-29","non_price_bridge":"ADAS/steering/brake subsystem supplier leverage, but customer-volume and margin refresh required","score_alignment":"local 4B until customer-volume, order and margin bridge refresh"}
{"row_type":"trigger","selected_round":"R9","selected_loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"GENERIC_PARTS_LABEL_LOW_MFE_HIGH_MAE_HARD_4C","symbol":"011210","name":"현대위아","trigger_type":"Stage4C","entry_date":"2024-09-13","entry_price":51600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.26,"MAE_30D_pct":-8.62,"MFE_90D_pct":4.26,"MAE_90D_pct":-28.20,"MFE_180D_pct":4.26,"MAE_180D_pct":-28.49,"forward_high_30d":53800,"forward_low_30d":47150,"forward_high_90d":53800,"forward_low_90d":37050,"forward_high_180d":53800,"forward_low_180d":36900,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|011210|Stage4C|2024-09-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same C29 generic parts hard-block row from loops 104~106 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"generic_parts_hard_4C","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|011210|Stage4C|2024-09-13","non_price_bridge":"engine/module/machine-tool parts label without durable margin, customer-volume, revision or cash bridge","score_alignment":"hard 4C; label-only parts exposure fails"}
{"row_type":"trigger","selected_round":"R9","selected_loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_THEME_BLOWOFF_LOCAL_4B_THEN_BLOCK","symbol":"010690","name":"화신","trigger_type":"Stage4B","entry_date":"2024-06-12","entry_price":11690,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":35.93,"MAE_30D_pct":-4.53,"MFE_90D_pct":35.93,"MAE_90D_pct":-30.28,"MFE_180D_pct":35.93,"MAE_180D_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C29|010690|Stage4B|2024-06-12","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_theme_4B_to_4C","reuse_reason":"same C29 theme blowoff row from loops 103~106","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"theme_blowoff_local_4B_to_block","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|010690|Stage4B|2024-06-12","non_price_bridge":"auto-parts theme/volume label without durable customer-volume or margin bridge","score_alignment":"local 4B only; hard block if bridge does not refresh"}
```

---

## 5. Case analysis

### 5.1 Kia / 000270 — OEM positive-control

Kia validates the C29 bridge: volume, mix, ASP, margin and cash conversion are the core.

```yaml
entry_close: 93000
90D_MFE_MAE: +45.16 / -7.42
180D_MFE_MAE: +45.16 / -7.42
route: KeepStage2
```

### 5.2 Hyundai Motor / 005380 — Value-up cap

Shareholder-return intent may be meaningful, but it is not C29 unless operating bridge is visible.

```yaml
entry_close: 259000
90D_MFE_MAE: +3.09 / -22.78
180D_MFE_MAE: +3.09 / -32.12
route: Stage2 / cap
```

### 5.3 Hyundai Mobis / 012330 — slow positive

Module/core-parts/A/S profitability is a valid but slower bridge.

```yaml
entry_close: 241500
90D_MFE_MAE: +11.18 / -2.69
180D_MFE_MAE: +19.67 / -3.52
route: Stage2-Actionable with refresh requirement
```

### 5.4 Hyundai Glovis / 086280 — logistics local 4B

Logistics bridge exists, but needs margin/cash refresh.

```yaml
entry_close: 123900
90D_MFE_MAE: +21.87 / -9.93
180D_MFE_MAE: +21.87 / -15.25
route: Stage4B
```

### 5.5 HL Mando / 204320 — supplier local 4B

Subsystem bridge needs customer-volume and margin proof before Green.

```yaml
entry_close: 38350
90D_MFE_MAE: +30.38 / -19.56
180D_MFE_MAE: +30.38 / -19.56
route: Stage4B
```

### 5.6 Hyundai Wia / 011210 — generic parts hard 4C

Generic parts vocabulary without bridge failed.

```yaml
entry_close: 51600
90D_MFE_MAE: +4.26 / -28.20
180D_MFE_MAE: +4.26 / -28.49
route: Stage4C
```

### 5.7 Hwashin / 010690 — theme blowoff 4B to block

Theme MFE does not prove durable volume/margin bridge.

```yaml
entry_close: 11690
90D_MFE_MAE: +35.93 / -30.28
180D_MFE_MAE: +35.93 / -47.39
route: Stage4B -> block if no refresh
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
hard_4C_count: 1
current_profile_error_count: 4
diversity_score_summary: "OEM positive, Value-up cap, parts/A/S slow positive, logistics 4B, supplier 4B, generic parts hard 4C, theme 4B-to-block covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
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

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"000270","raw_volume_mix_margin_bridge":5,"raw_customer_order_bridge":4,"raw_cash_revision_bridge":4,"raw_price_validation":5,"raw_label_only_risk":0,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OEMMarginBridge"}
{"row_type":"score_simulation","symbol":"005380","raw_volume_mix_margin_bridge":1,"raw_customer_order_bridge":1,"raw_cash_revision_bridge":1,"raw_price_validation":0,"raw_label_only_risk":4,"raw_wrong_archetype_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_ValueupLabel"}
{"row_type":"score_simulation","symbol":"012330","raw_volume_mix_margin_bridge":3,"raw_customer_order_bridge":3,"raw_cash_revision_bridge":2,"raw_price_validation":2,"raw_label_only_risk":1,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Watch_SlowPartsBridge"}
{"row_type":"score_simulation","symbol":"086280","raw_volume_mix_margin_bridge":3,"raw_customer_order_bridge":3,"raw_cash_revision_bridge":2,"raw_price_validation":3,"raw_label_only_risk":1,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_LogisticsRefresh"}
{"row_type":"score_simulation","symbol":"204320","raw_volume_mix_margin_bridge":3,"raw_customer_order_bridge":2,"raw_cash_revision_bridge":2,"raw_price_validation":3,"raw_label_only_risk":1,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_SupplierRefresh"}
{"row_type":"score_simulation","symbol":"011210","raw_volume_mix_margin_bridge":0,"raw_customer_order_bridge":0,"raw_cash_revision_bridge":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_wrong_archetype_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_GenericParts"}
{"row_type":"score_simulation","symbol":"010690","raw_volume_mix_margin_bridge":1,"raw_customer_order_bridge":1,"raw_cash_revision_bridge":0,"raw_price_validation":2,"raw_label_only_risk":4,"raw_wrong_archetype_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenBlock"}
```

---

## 8. Current calibrated profile stress test

The C29 gate held in this holdout pass:

```text
OEM mix/margin bridge -> keep Stage2
Value-up label without operating bridge -> cap
parts/A/S or logistics bridge -> Stage2 or local 4B depending on path
generic parts label -> hard 4C
theme blowoff -> local 4B then block if no bridge refresh
```

### Rule candidate retained, not newly proposed

```text
C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V107_HELD_OUT

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

## 9. Batch Ingest Self-Audit

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

## 10. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
new_axis_proposed: null
existing_axis_strengthened:
  - C29_VOLUME_MIX_MARGIN_CUSTOMER_ORDER_REQUIREMENT_V107_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the C29 volume/mix/margin/customer-order gate across OEM, Value-up cap, parts, logistics, supplier 4B, generic parts hard 4C and theme blowoff rows."
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R9/C29 loop 107 as holdout validation only. Batch it with C29 loops 100~106 and adjacent R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C29 volume/mix/margin/customer-order gate, but do not create a new weight delta from this loop because no new independent case was added.
```

---

## 12. Next research state

```yaml
completed_round: R9
completed_loop: 107
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
