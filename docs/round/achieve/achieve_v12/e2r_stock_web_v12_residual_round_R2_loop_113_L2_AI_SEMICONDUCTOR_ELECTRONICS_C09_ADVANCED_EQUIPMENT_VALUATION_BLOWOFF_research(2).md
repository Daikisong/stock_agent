# E2R Stock-Web V12 Residual Historical Calibration Research — R2 loop 113 — C09 Advanced Equipment Valuation Blowoff

## 0. Execution Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 113
selected_priority_bucket: Priority 0
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: C09_ADVANCED_METROLOGY_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_ORDER_MARGIN_REVISION_BRIDGE
deep_sub_archetype_id: C09_DEEP_HBM_OVERLAY_HPA_CMP_WAFER_INSPECTION_LOCAL_BLOWOFF_VS_VERIFIED_ORDER_MARGIN_BRIDGE
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
main_execution_prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
no_repeat_index_role: duplicate_avoidance_and_coverage_ledger_only
local_previous_output_avoided: e2r_stock_web_v12_residual_round_R1_loop_139_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
price_source: Songdaiki/stock-web
upstream_price_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: '2026-02-20'
```

This file is a standalone historical calibration research artifact. It is not a live scan, not a trade recommendation, not an automated order instruction, and not a production code patch. The purpose is to add non-duplicate C09 rows to the V12 calibration corpus and stress the current profile's C09 bridge/4B guardrails against realized 1D OHLC paths.

## 1. Selection Rationale

The No-Repeat ledger snapshot lists `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` as Priority 0 with 10 rows. `C02_POWER_GRID_DATACENTER_CAPEX` is also at 10 rows, but the immediately preceding local loop already generated a C02 artifact. To avoid same-canonical repetition in this session, this loop selects C09 and maps it to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`.

C09 is the semiconductor-equipment version of a mirage problem: the process technology can be genuinely scarce, but price often runs ahead of order, revenue, margin, or revision confirmation. This loop therefore mixes positive bridge cases with false-positive blowoff cases.

## 2. Coverage Gap Update

```yaml
pre_loop_index_rows_for_C09: 10
representative_rows_added_this_loop: 6
expected_post_loop_rows_for_C09: 16
remaining_to_30_row_floor: 14
remaining_to_50_row_preferred_depth: 34
new_independent_case_count: 6
reused_case_count: 0
new_symbol_count: 6
positive_case_count: 2
counterexample_count: 4
stage4b_case_count: 1
current_profile_error_count: 3
```

## 3. Price Source Validation

The loop uses `Songdaiki/stock-web` tradable OHLC shards only. All entries use `tradable_raw` close as entry price, forward windows are measured in trading rows, and each case has a full 180-trading-day forward path available before the manifest maximum date.

```yaml
price_manifest_url: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_usage: diagnostic_only_not_primary
manifest_max_date: '2026-02-20'
tradable_row_count: 14354401
symbol_count: 5414
corporate_action_windows_blocked: false
```

## 4. Case Summary Table

|case_id|symbol|name|label|trigger_type|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|DD_after_peak|residual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C09-L113-01|322310|오로스테크놀로지|counterexample|Stage3-Yellow|2024-05-17|29100|5.50|-25.60|5.50|-48.01|5.50|-54.71|-57.07|false_positive_or_too_early_without_verified_bridge|
|C09-L113-02|403870|HPSP|counterexample|Stage4B|2024-03-15|52200|5.94|-26.44|5.94|-39.37|5.94|-56.61|-59.04|guardrail_success_price_only_blowoff|
|C09-L113-03|348210|넥스틴|counterexample|Stage2-Actionable|2023-09-06|82500|4.12|-32.24|4.12|-35.52|4.12|-35.52|-38.07|false_positive_or_too_early_without_verified_bridge|
|C09-L113-04|281820|케이씨텍|positive|Stage2-Actionable|2024-05-27|37650|32.80|-3.05|56.71|-21.78|56.71|-33.20|-57.37|true_positive_bridge_pass|
|C09-L113-05|140860|파크시스템스|positive|Stage2-Actionable|2024-08-21|195800|2.91|-15.63|18.49|-15.63|27.68|-15.63|-27.48|true_positive_bridge_pass|
|C09-L113-06|240810|원익IPS|counterexample|Stage2-Actionable|2024-05-31|35400|13.84|-5.51|13.84|-21.89|13.84|-40.96|-48.14|false_positive_or_too_early_without_verified_bridge|


## 5. Case Notes

### C09-L113-01 — 오로스테크놀로지 / 322310 — HBM pad overlay headline without broad bridge

The 2024-05-16 Samsung HBM PAD overlay equipment supply is high-quality technology/customer evidence, but the realized path after the next tradable entry had only +5.50% 30/90/180D MFE and -54.71% 180D MAE. This is a textbook C09 false-positive risk: a real niche tool plus HBM vocabulary can look like Stage3-Yellow, but the calibration row says it should stay below positive rerating credit until the single-order evidence becomes backlog, repeat shipment, or margin/revision bridge.

### C09-L113-02 — HPSP / 403870 — HPHA monopoly narrative as local 4B watch

HPSP's HPHA/HPA technology evidence is real, and the company had strong scarcity language around high-pressure annealing and imec/JDP. The calibration problem is not technology validity; it is entry timing and valuation path. From 2024-03-15, the 180D window produced only +5.94% MFE versus -56.61% MAE. This should strengthen C09's local 4B valuation-blowoff watch rather than loosen Stage2/Stage3 scoring.

### C09-L113-03 — 넥스틴 / 348210 — China wafer inspection capex event too early

The Wuxi/China investment story extended addressable-market visibility, but the entry following the report had +4.12% 180D MFE and -35.52% 180D MAE. C09 should not translate a capacity/investment headline into Stage2-Actionable unless it sees a customer order, shipment, or explicit revenue/margin bridge.

### C09-L113-04 — 케이씨텍 / 281820 — CMP process-count bridge passes

This is the clean positive contrast. The evidence tied CMP process-count expansion and HBM stacking to equipment/slurry demand and also included Q1 revenue/profit context. The price path validated the bridge with +56.71% 180D MFE, although the -33.20% 180D MAE and -57.37% drawdown after peak warn that Green should still require revision durability and exit-risk discipline.

### C09-L113-05 — 파크시스템스 / 140860 — industrial AFM shipment bridge passes slowly

Park Systems is also positive, but not explosive at first. The 30D MFE was only +2.91%, while 180D MFE reached +27.68%. The case supports Stage2-Actionable, not immediate Stage3-Green, because the bridge is real but the path is delayed and still carries a -15.63% MAE.

### C09-L113-06 — 원익IPS / 240810 — upgrade with internal bridge conflict

Wonik IPS is the subtle counterexample. The report changed recommendation and raised target, but it simultaneously described the HBM cycle as insufficient for front-end capex, with limited new investment, NAND weakness, and customer-share issues. The realized path reached +13.84% MFE but ultimately carried -40.96% 180D MAE. C09 should penalize this internal bridge conflict instead of letting the upgrade headline override the guardrail.

## 6. Residual Pattern

C09 should reward semiconductor equipment only when the advanced-process story crosses a non-price bridge. The distinction is not “technology real or fake.” The distinction is whether the technology narrative has already become an order/revenue/margin/revision mechanism. Without that bridge, the archetype behaves like a shiny lens: it magnifies every HBM/advanced-node word and can burn the state machine if valuation has already heated up.

### Proposed residual rule candidate

```yaml
new_axis_proposed: C09_verified_order_margin_revision_bridge_required_before_yellow_or_green
rule_candidate:
  scope: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
  no_global_threshold_change: true
  stage2_actionable_requirement:
    require_any_of:
      - verified_customer_order_or_repeat_order
      - shipped_equipment_or_backlog_conversion
      - reported_revenue_profit_margin_bridge
      - explicit_estimate_revision_bridge
  cap_without_bridge:
    - Watch
    - Stage1.5
    - Stage4B-LocalWatch_if_price_extended
  stage3_green_guard:
    require_revision_visibility_and_no_price_only_blowoff
  full_4b_guard:
    require_non_price_thesis_break_evidence
```

## 7. Current Profile Stress Test

```yaml
current_profile_successes:
  - HPSP price-only/valuation blowoff can be correctly held as Stage4B-LocalWatch.
  - KC Tech and Park Systems pass Stage2 because evidence contains financial/shipment/process-demand bridge.
current_profile_residual_errors:
  - Oros can still be overpromoted if single-customer single-order HBM overlay is treated as enough for Stage3-Yellow.
  - Nextin can still be overpromoted if overseas capex/market-share expansion is treated as near-term order conversion.
  - Wonik IPS can still be overpromoted if report upgrade language overrides report-internal bridge conflict.
error_count: 3
```

## 8. Shadow Weight / Patch Candidate

No production profile change is made here. The following is a deferred calibration candidate only.

```csv
profile_scope,component,current_weight_proxy,candidate_delta,direction,reason
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,verified_order_backlog_or_shipment_bridge,22,4,increase,"positive cases needed order/shipment or financial bridge before Actionable/Yellow"
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,reported_revision_or_financial_bridge,20,3,increase,"Park/KC Tech positives passed because revenue/profit/revision visibility existed"
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,pure_technology_scarcity_headline,18,-3,decrease,"Oros/HPSP/Nextin show technology scarcity alone can coincide with poor 180D path"
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,valuation_blowoff_local_4b_guard,13,3,increase_guard,"HPSP and Oros needed cap/watch treatment after stretched price path"
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,internal_report_bridge_conflict_penalty,0,3,new_penalty,"Wonik report upgrade contained bridge-conflict evidence and should not override guardrails"
```

## 9. Machine-Readable JSONL Rows

```jsonl
{"all_windows_have_180_trading_days": true, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "loop_id": "R2_loop_113_C09", "manifest_max_date": "2026-02-20", "manifest_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "row_type": "price_source_validation", "source_name": "Songdaiki/stock-web", "symbol_count": 5414, "symbols_checked": ["140860", "240810", "281820", "322310", "348210", "403870"], "tradable_row_count": 14354401, "upstream_price_source": "FinanceData/marcap", "validation_result": "pass"}
{"MAE_180D_pct": -54.7079, "MAE_30D_pct": -25.6014, "MAE_90D_pct": -48.0069, "MFE_180D_pct": 5.4983, "MFE_30D_pct": 5.4983, "MFE_90D_pct": 5.4983, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-01", "current_error": "false_positive_if_technology_headline_promoted_to_stage3_without_revision_bridge", "direction": "counterexample", "drawdown_after_peak_pct": -57.0684, "entry_date": "2024-05-17", "entry_price": 29100.0, "evidence": "TheElec reported 2024-05-16 Samsung HBM PAD overlay equipment supply; Newspim/Kiwoom described packaging overlay/WaPIS expansion and 2025 sales target.", "fine": "HBM_PAD_OVERLAY_SINGLE_ORDER_PRICE_THEME_WITHOUT_MARGIN_BRIDGE", "forward_180D_trading_days_available": 180, "forward_30D_trading_days_available": 30, "forward_90D_trading_days_available": 90, "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "오로스테크놀로지", "peak_180D_date": "2024-05-17", "peak_180D_price": 30700.0, "peak_30D_date": "2024-05-17", "peak_30D_price": 30700.0, "peak_90D_date": "2024-05-17", "peak_90D_price": 30700.0, "peak_date": "2024-05-17", "peak_price": 30700.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested": "2024-05-17", "requested_entry_date": "2024-05-17", "row_type": "case", "source_ids": ["OROS_THEELEC_20240516", "OROS_NEWS_PIM_20240104"], "symbol": "322310", "thesis": "HBM pad overlay supply headline created C09 scarcity/advanced metrology excitement, but a single 4.8bn KRW order and customer-speed narrative did not yet prove broad backlog, revision, or margin bridge.", "trigger_type": "Stage3-Yellow"}
{"MAE_180D_pct": -56.6092, "MAE_30D_pct": -26.4368, "MAE_90D_pct": -39.3678, "MFE_180D_pct": 5.9387, "MFE_30D_pct": 5.9387, "MFE_90D_pct": 5.9387, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-02", "current_error": "guardrail_success_if_profile_keeps_as_local_4b_not_positive", "direction": "counterexample", "drawdown_after_peak_pct": -59.0416, "entry_date": "2024-03-15", "entry_price": 52200.0, "evidence": "HPSP official release described HPA/HPO R&D extension and imec JDP; MK noted market-cap around KRW 3.8tn and capacity expectation expansion narrative.", "fine": "HPA_HPHA_MONOPOLY_VALUATION_BLOWOFF_WITH_JDP_TECH_SCARCITY", "forward_180D_trading_days_available": 180, "forward_30D_trading_days_available": 30, "forward_90D_trading_days_available": 90, "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "HPSP", "peak_180D_date": "2024-03-28", "peak_180D_price": 55300.0, "peak_30D_date": "2024-03-28", "peak_30D_price": 55300.0, "peak_90D_date": "2024-03-28", "peak_90D_price": 55300.0, "peak_date": "2024-03-28", "peak_price": 55300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested": "2024-03-15", "requested_entry_date": "2024-03-15", "row_type": "case", "source_ids": ["HPSP_OFFICIAL_20240116", "HPSP_MK_20240201"], "symbol": "403870", "thesis": "World-first HPHA scarcity and imec/JDP narrative was real technology evidence, but by the selected entry the price/valuation path was already blowoff-like and needed local 4B watch rather than positive rerating credit.", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -35.5152, "MAE_30D_pct": -32.2424, "MAE_90D_pct": -35.5152, "MFE_180D_pct": 4.1212, "MFE_30D_pct": 4.1212, "MFE_90D_pct": 4.1212, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-03", "current_error": "stage2_too_early_if_capex_event_counted_as_order_bridge", "direction": "counterexample", "drawdown_after_peak_pct": -38.0675, "entry_date": "2023-09-06", "entry_price": 82500.0, "evidence": "DIGITIMES reported 2023-09-05 investment to produce wafer inspection tools in Wuxi and meet Chinese semiconductor demand.", "fine": "WAFER_INSPECTION_CHINA_CAPEX_EVENT_WITHOUT_NEAR_TERM_ORDER_CONVERSION", "forward_180D_trading_days_available": 180, "forward_30D_trading_days_available": 30, "forward_90D_trading_days_available": 90, "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "넥스틴", "peak_180D_date": "2023-09-08", "peak_180D_price": 85900.0, "peak_30D_date": "2023-09-08", "peak_30D_price": 85900.0, "peak_90D_date": "2023-09-08", "peak_90D_price": 85900.0, "peak_date": "2023-09-08", "peak_price": 85900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested": "2023-09-06", "requested_entry_date": "2023-09-06", "row_type": "case", "source_ids": ["NEXTIN_DIGITIMES_20230905"], "symbol": "348210", "thesis": "US$200m Wuxi/China investment event increased strategic addressable-market visibility, but it was capex/market-share narrative rather than confirmed shipment, customer order, or near-term earnings revision bridge.", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -33.2005, "MAE_30D_pct": -3.0544, "MAE_90D_pct": -21.7795, "MFE_180D_pct": 56.7065, "MFE_30D_pct": 32.8021, "MFE_90D_pct": 56.7065, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-04", "current_error": "no_error_positive_bridge_pass", "direction": "positive", "drawdown_after_peak_pct": -57.3729, "entry_date": "2024-05-27", "entry_price": 37650.0, "evidence": "Daum/Edaily report quoting DS described CMP count increase from process scaling/HBM stacking and Q1 revenue/profit beating consensus.", "fine": "CMP_PROCESS_COUNT_HBM_STACKING_DEMAND_WITH_REVENUE_PROFIT_BRIDGE", "forward_180D_trading_days_available": 180, "forward_30D_trading_days_available": 30, "forward_90D_trading_days_available": 90, "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "케이씨텍", "peak_180D_date": "2024-07-11", "peak_180D_price": 59000.0, "peak_30D_date": "2024-06-20", "peak_30D_price": 50000.0, "peak_90D_date": "2024-07-11", "peak_90D_price": 59000.0, "peak_date": "2024-07-11", "peak_price": 59000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested": "2024-05-27", "requested_entry_date": "2024-05-27", "row_type": "case", "source_ids": ["KCTECH_DAUM_EDAILY_20240524"], "symbol": "281820", "thesis": "CMP process-count expansion and HBM stacking were tied to actual equipment/slurry demand plus Q1 revenue/profit data, so the case passes the non-price bridge that C09 should require.", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -15.6282, "MAE_30D_pct": -15.6282, "MAE_90D_pct": -15.6282, "MFE_180D_pct": 27.6813, "MFE_30D_pct": 2.9111, "MFE_90D_pct": 18.4883, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-05", "current_error": "no_error_positive_bridge_pass_but_green_should_wait_for_revision_visibility", "direction": "positive", "drawdown_after_peak_pct": -27.48, "entry_date": "2024-08-21", "entry_price": 195800.0, "evidence": "Park Systems 2024-08-20 IR presentation reported Q2 revenue/profit growth and industrial product shipment ramp.", "fine": "INDUSTRIAL_AFM_SHIPMENT_Q2_REVENUE_PROFIT_BRIDGE", "forward_180D_trading_days_available": 180, "forward_30D_trading_days_available": 30, "forward_90D_trading_days_available": 90, "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "파크시스템스", "peak_180D_date": "2025-01-22", "peak_180D_price": 250000.0, "peak_30D_date": "2024-10-04", "peak_30D_price": 201500.0, "peak_90D_date": "2025-01-03", "peak_90D_price": 232000.0, "peak_date": "2025-01-22", "peak_price": 250000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested": "2024-08-21", "requested_entry_date": "2024-08-21", "row_type": "case", "source_ids": ["PARK_IR_20240820"], "symbol": "140860", "thesis": "AFM/metrology premium was backed by 2024 Q2 sales/profit acceleration and industrial-shipment mix, creating a slower but valid Stage2 bridge rather than pure valuation excitement.", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -40.9605, "MAE_30D_pct": -5.5085, "MAE_90D_pct": -21.8927, "MFE_180D_pct": 13.8418, "MFE_30D_pct": 13.8418, "MFE_90D_pct": 13.8418, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-06", "current_error": "false_positive_if_upgrade_overrides_internal_bridge_conflict", "direction": "counterexample", "drawdown_after_peak_pct": -48.139, "entry_date": "2024-05-31", "entry_price": 35400.0, "evidence": "Samsung Securities report changed to BUY but highlighted limited front-end investment, weak new capacity, HBM insufficiency, NAND weakness and customer share decline before later-cycle expectations.", "fine": "FRONT_END_EQUIPMENT_MEMORY_RECOVERY_EXPECTATION_WITH_INTERNAL_BRIDGE_CONFLICT", "forward_180D_trading_days_available": 180, "forward_30D_trading_days_available": 30, "forward_90D_trading_days_available": 90, "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "name": "원익IPS", "peak_180D_date": "2024-07-04", "peak_180D_price": 40300.0, "peak_30D_date": "2024-07-04", "peak_30D_price": 40300.0, "peak_90D_date": "2024-07-04", "peak_90D_price": 40300.0, "peak_date": "2024-07-04", "peak_price": 40300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested": "2024-05-31", "requested_entry_date": "2024-05-31", "row_type": "case", "source_ids": ["WONIK_SAMSUNG_20240530"], "symbol": "240810", "thesis": "The report upgrade captured possible direction change, but its own evidence showed front-end new investment was still limited, HBM contribution insufficient, NAND weak, and customer share declining; C09 should not give full positive credit until order/revision bridge appears.", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -54.7079, "MAE_30D_pct": -25.6014, "MAE_90D_pct": -48.0069, "MFE_180D_pct": 5.4983, "MFE_30D_pct": 5.4983, "MFE_90D_pct": 5.4983, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-01", "corporate_action_blocked_window": false, "corporate_action_candidate_count": 0, "current_profile_expected_stage": "Stage2-Actionable_OR_Stage3-Yellow_risk", "dedupe_for_aggregate": true, "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|322310|Stage3-Yellow|2024-05-17", "deep_sub_archetype_id": "C09_DEEP_HBM_OVERLAY_HPA_CMP_WAFER_INSPECTION_LOCAL_BLOWOFF_VS_VERIFIED_ORDER_MARGIN_BRIDGE", "direction_label": "counterexample", "drawdown_after_peak_pct": -57.0684, "entry_date": "2024-05-17", "entry_price": 29100.0, "evidence_family": "HBM_PAD_OVERLAY_SINGLE_ORDER_PRICE_THEME_WITHOUT_MARGIN_BRIDGE", "fine_archetype_id": "HBM_PAD_OVERLAY_SINGLE_ORDER_PRICE_THEME_WITHOUT_MARGIN_BRIDGE", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop_id": "R2_loop_113_C09", "name": "오로스테크놀로지", "peak_date": "2024-05-17", "peak_price": 30700.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "residual_error_type": "false_positive_or_too_early_without_verified_bridge", "row_type": "trigger", "same_archetype_new_symbol": true, "shadow_stage_after_candidate_rule": "Watch/Stage1.5_until_bridge", "source_ids": ["OROS_THEELEC_20240516", "OROS_NEWS_PIM_20240104"], "symbol": "322310", "thesis": "HBM pad overlay supply headline created C09 scarcity/advanced metrology excitement, but a single 4.8bn KRW order and customer-speed narrative did not yet prove broad backlog, revision, or margin bridge.", "trigger_date": "2024-05-17", "trigger_id": "TRG-C09-L113-01-322310-2024-05-17", "trigger_type": "Stage3-Yellow", "upstream_price_source": "FinanceData/marcap"}
{"MAE_180D_pct": -56.6092, "MAE_30D_pct": -26.4368, "MAE_90D_pct": -39.3678, "MFE_180D_pct": 5.9387, "MFE_30D_pct": 5.9387, "MFE_90D_pct": 5.9387, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-02", "corporate_action_blocked_window": false, "corporate_action_candidate_count": 2, "current_profile_expected_stage": "Stage4B-LocalWatch", "dedupe_for_aggregate": true, "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|403870|Stage4B|2024-03-15", "deep_sub_archetype_id": "C09_DEEP_HBM_OVERLAY_HPA_CMP_WAFER_INSPECTION_LOCAL_BLOWOFF_VS_VERIFIED_ORDER_MARGIN_BRIDGE", "direction_label": "counterexample", "drawdown_after_peak_pct": -59.0416, "entry_date": "2024-03-15", "entry_price": 52200.0, "evidence_family": "HPA_HPHA_MONOPOLY_VALUATION_BLOWOFF_WITH_JDP_TECH_SCARCITY", "fine_archetype_id": "HPA_HPHA_MONOPOLY_VALUATION_BLOWOFF_WITH_JDP_TECH_SCARCITY", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop_id": "R2_loop_113_C09", "name": "HPSP", "peak_date": "2024-03-28", "peak_price": 55300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "residual_error_type": "guardrail_success_price_only_blowoff", "row_type": "trigger", "same_archetype_new_symbol": true, "shadow_stage_after_candidate_rule": "Stage4B-LocalWatch", "source_ids": ["HPSP_OFFICIAL_20240116", "HPSP_MK_20240201"], "symbol": "403870", "thesis": "World-first HPHA scarcity and imec/JDP narrative was real technology evidence, but by the selected entry the price/valuation path was already blowoff-like and needed local 4B watch rather than positive rerating credit.", "trigger_date": "2024-03-15", "trigger_id": "TRG-C09-L113-02-403870-2024-03-15", "trigger_type": "Stage4B", "upstream_price_source": "FinanceData/marcap"}
{"MAE_180D_pct": -35.5152, "MAE_30D_pct": -32.2424, "MAE_90D_pct": -35.5152, "MFE_180D_pct": 4.1212, "MFE_30D_pct": 4.1212, "MFE_90D_pct": 4.1212, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-03", "corporate_action_blocked_window": false, "corporate_action_candidate_count": 2, "current_profile_expected_stage": "Stage2-Actionable_OR_Stage3-Yellow_risk", "dedupe_for_aggregate": true, "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|348210|Stage2-Actionable|2023-09-06", "deep_sub_archetype_id": "C09_DEEP_HBM_OVERLAY_HPA_CMP_WAFER_INSPECTION_LOCAL_BLOWOFF_VS_VERIFIED_ORDER_MARGIN_BRIDGE", "direction_label": "counterexample", "drawdown_after_peak_pct": -38.0675, "entry_date": "2023-09-06", "entry_price": 82500.0, "evidence_family": "WAFER_INSPECTION_CHINA_CAPEX_EVENT_WITHOUT_NEAR_TERM_ORDER_CONVERSION", "fine_archetype_id": "WAFER_INSPECTION_CHINA_CAPEX_EVENT_WITHOUT_NEAR_TERM_ORDER_CONVERSION", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop_id": "R2_loop_113_C09", "name": "넥스틴", "peak_date": "2023-09-08", "peak_price": 85900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "residual_error_type": "false_positive_or_too_early_without_verified_bridge", "row_type": "trigger", "same_archetype_new_symbol": true, "shadow_stage_after_candidate_rule": "Watch/Stage1.5_until_bridge", "source_ids": ["NEXTIN_DIGITIMES_20230905"], "symbol": "348210", "thesis": "US$200m Wuxi/China investment event increased strategic addressable-market visibility, but it was capex/market-share narrative rather than confirmed shipment, customer order, or near-term earnings revision bridge.", "trigger_date": "2023-09-06", "trigger_id": "TRG-C09-L113-03-348210-2023-09-06", "trigger_type": "Stage2-Actionable", "upstream_price_source": "FinanceData/marcap"}
{"MAE_180D_pct": -33.2005, "MAE_30D_pct": -3.0544, "MAE_90D_pct": -21.7795, "MFE_180D_pct": 56.7065, "MFE_30D_pct": 32.8021, "MFE_90D_pct": 56.7065, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-04", "corporate_action_blocked_window": false, "corporate_action_candidate_count": 0, "current_profile_expected_stage": "Stage2-Actionable", "dedupe_for_aggregate": true, "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|281820|Stage2-Actionable|2024-05-27", "deep_sub_archetype_id": "C09_DEEP_HBM_OVERLAY_HPA_CMP_WAFER_INSPECTION_LOCAL_BLOWOFF_VS_VERIFIED_ORDER_MARGIN_BRIDGE", "direction_label": "positive", "drawdown_after_peak_pct": -57.3729, "entry_date": "2024-05-27", "entry_price": 37650.0, "evidence_family": "CMP_PROCESS_COUNT_HBM_STACKING_DEMAND_WITH_REVENUE_PROFIT_BRIDGE", "fine_archetype_id": "CMP_PROCESS_COUNT_HBM_STACKING_DEMAND_WITH_REVENUE_PROFIT_BRIDGE", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop_id": "R2_loop_113_C09", "name": "케이씨텍", "peak_date": "2024-07-11", "peak_price": 59000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "residual_error_type": "true_positive_bridge_pass", "row_type": "trigger", "same_archetype_new_symbol": true, "shadow_stage_after_candidate_rule": "Stage2-Actionable", "source_ids": ["KCTECH_DAUM_EDAILY_20240524"], "symbol": "281820", "thesis": "CMP process-count expansion and HBM stacking were tied to actual equipment/slurry demand plus Q1 revenue/profit data, so the case passes the non-price bridge that C09 should require.", "trigger_date": "2024-05-27", "trigger_id": "TRG-C09-L113-04-281820-2024-05-27", "trigger_type": "Stage2-Actionable", "upstream_price_source": "FinanceData/marcap"}
{"MAE_180D_pct": -15.6282, "MAE_30D_pct": -15.6282, "MAE_90D_pct": -15.6282, "MFE_180D_pct": 27.6813, "MFE_30D_pct": 2.9111, "MFE_90D_pct": 18.4883, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-05", "corporate_action_blocked_window": false, "corporate_action_candidate_count": 0, "current_profile_expected_stage": "Stage2-Actionable", "dedupe_for_aggregate": true, "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|140860|Stage2-Actionable|2024-08-21", "deep_sub_archetype_id": "C09_DEEP_HBM_OVERLAY_HPA_CMP_WAFER_INSPECTION_LOCAL_BLOWOFF_VS_VERIFIED_ORDER_MARGIN_BRIDGE", "direction_label": "positive", "drawdown_after_peak_pct": -27.48, "entry_date": "2024-08-21", "entry_price": 195800.0, "evidence_family": "INDUSTRIAL_AFM_SHIPMENT_Q2_REVENUE_PROFIT_BRIDGE", "fine_archetype_id": "INDUSTRIAL_AFM_SHIPMENT_Q2_REVENUE_PROFIT_BRIDGE", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop_id": "R2_loop_113_C09", "name": "파크시스템스", "peak_date": "2025-01-22", "peak_price": 250000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "residual_error_type": "true_positive_bridge_pass", "row_type": "trigger", "same_archetype_new_symbol": true, "shadow_stage_after_candidate_rule": "Stage2-Actionable", "source_ids": ["PARK_IR_20240820"], "symbol": "140860", "thesis": "AFM/metrology premium was backed by 2024 Q2 sales/profit acceleration and industrial-shipment mix, creating a slower but valid Stage2 bridge rather than pure valuation excitement.", "trigger_date": "2024-08-21", "trigger_id": "TRG-C09-L113-05-140860-2024-08-21", "trigger_type": "Stage2-Actionable", "upstream_price_source": "FinanceData/marcap"}
{"MAE_180D_pct": -40.9605, "MAE_30D_pct": -5.5085, "MAE_90D_pct": -21.8927, "MFE_180D_pct": 13.8418, "MFE_30D_pct": 13.8418, "MFE_90D_pct": 13.8418, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-06", "corporate_action_blocked_window": false, "corporate_action_candidate_count": 0, "current_profile_expected_stage": "Stage2-Actionable_OR_Stage3-Yellow_risk", "dedupe_for_aggregate": true, "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|240810|Stage2-Actionable|2024-05-31", "deep_sub_archetype_id": "C09_DEEP_HBM_OVERLAY_HPA_CMP_WAFER_INSPECTION_LOCAL_BLOWOFF_VS_VERIFIED_ORDER_MARGIN_BRIDGE", "direction_label": "counterexample", "drawdown_after_peak_pct": -48.139, "entry_date": "2024-05-31", "entry_price": 35400.0, "evidence_family": "FRONT_END_EQUIPMENT_MEMORY_RECOVERY_EXPECTATION_WITH_INTERNAL_BRIDGE_CONFLICT", "fine_archetype_id": "FRONT_END_EQUIPMENT_MEMORY_RECOVERY_EXPECTATION_WITH_INTERNAL_BRIDGE_CONFLICT", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "loop_id": "R2_loop_113_C09", "name": "원익IPS", "peak_date": "2024-07-04", "peak_price": 40300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "residual_error_type": "false_positive_or_too_early_without_verified_bridge", "row_type": "trigger", "same_archetype_new_symbol": true, "shadow_stage_after_candidate_rule": "Watch/Stage1.5_until_bridge", "source_ids": ["WONIK_SAMSUNG_20240530"], "symbol": "240810", "thesis": "The report upgrade captured possible direction change, but its own evidence showed front-end new investment was still limited, HBM contribution insufficient, NAND weak, and customer share declining; C09 should not give full positive credit until order/revision bridge appears.", "trigger_date": "2024-05-31", "trigger_id": "TRG-C09-L113-06-240810-2024-05-31", "trigger_type": "Stage2-Actionable", "upstream_price_source": "FinanceData/marcap"}
{"canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-01", "component_scores_proxy": {"customer_concentration_risk": 58, "order_backlog_or_shipment_bridge": 52, "price_path_validation": 20, "red_team_penalty": 70, "revision_or_reported_financial_bridge": 25, "technology_scarcity": 72, "valuation_blowoff_risk": 65}, "current_profile_expected_stage": "Stage2-Actionable_OR_Stage3-Yellow_risk", "legacy_unpatched_score_proxy": 51.71, "loop_id": "R2_loop_113_C09", "row_type": "score_simulation", "shadow_stage_after_candidate_rule": "Watch/Stage1.5_until_bridge", "simulation_note": "Proxy simulation only; no production scoring change. Purpose is to stress C09 bridge/4B rules with realized OHLC path.", "symbol": "322310"}
{"canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-02", "component_scores_proxy": {"customer_concentration_risk": 35, "order_backlog_or_shipment_bridge": 35, "price_path_validation": 20, "red_team_penalty": 70, "revision_or_reported_financial_bridge": 25, "technology_scarcity": 72, "valuation_blowoff_risk": 65}, "current_profile_expected_stage": "Stage4B-LocalWatch", "legacy_unpatched_score_proxy": 46.0, "loop_id": "R2_loop_113_C09", "row_type": "score_simulation", "shadow_stage_after_candidate_rule": "Stage4B-LocalWatch", "simulation_note": "Proxy simulation only; no production scoring change. Purpose is to stress C09 bridge/4B rules with realized OHLC path.", "symbol": "403870"}
{"canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-03", "component_scores_proxy": {"customer_concentration_risk": 58, "order_backlog_or_shipment_bridge": 35, "price_path_validation": 20, "red_team_penalty": 70, "revision_or_reported_financial_bridge": 25, "technology_scarcity": 72, "valuation_blowoff_risk": 65}, "current_profile_expected_stage": "Stage2-Actionable_OR_Stage3-Yellow_risk", "legacy_unpatched_score_proxy": 49.29, "loop_id": "R2_loop_113_C09", "row_type": "score_simulation", "shadow_stage_after_candidate_rule": "Watch/Stage1.5_until_bridge", "simulation_note": "Proxy simulation only; no production scoring change. Purpose is to stress C09 bridge/4B rules with realized OHLC path.", "symbol": "348210"}
{"canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-04", "component_scores_proxy": {"customer_concentration_risk": 35, "order_backlog_or_shipment_bridge": 82, "price_path_validation": 75, "red_team_penalty": 30, "revision_or_reported_financial_bridge": 78, "technology_scarcity": 55, "valuation_blowoff_risk": 38}, "current_profile_expected_stage": "Stage2-Actionable", "legacy_unpatched_score_proxy": 56.14, "loop_id": "R2_loop_113_C09", "row_type": "score_simulation", "shadow_stage_after_candidate_rule": "Stage2-Actionable", "simulation_note": "Proxy simulation only; no production scoring change. Purpose is to stress C09 bridge/4B rules with realized OHLC path.", "symbol": "281820"}
{"canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-05", "component_scores_proxy": {"customer_concentration_risk": 35, "order_backlog_or_shipment_bridge": 82, "price_path_validation": 75, "red_team_penalty": 30, "revision_or_reported_financial_bridge": 78, "technology_scarcity": 72, "valuation_blowoff_risk": 38}, "current_profile_expected_stage": "Stage2-Actionable", "legacy_unpatched_score_proxy": 58.57, "loop_id": "R2_loop_113_C09", "row_type": "score_simulation", "shadow_stage_after_candidate_rule": "Stage2-Actionable", "simulation_note": "Proxy simulation only; no production scoring change. Purpose is to stress C09 bridge/4B rules with realized OHLC path.", "symbol": "140860"}
{"canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09-L113-06", "component_scores_proxy": {"customer_concentration_risk": 58, "order_backlog_or_shipment_bridge": 35, "price_path_validation": 20, "red_team_penalty": 70, "revision_or_reported_financial_bridge": 45, "technology_scarcity": 55, "valuation_blowoff_risk": 48}, "current_profile_expected_stage": "Stage2-Actionable_OR_Stage3-Yellow_risk", "legacy_unpatched_score_proxy": 47.29, "loop_id": "R2_loop_113_C09", "row_type": "score_simulation", "shadow_stage_after_candidate_rule": "Watch/Stage1.5_until_bridge", "simulation_note": "Proxy simulation only; no production scoring change. Purpose is to stress C09 bridge/4B rules with realized OHLC path.", "symbol": "240810"}
{"canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "canonical_archetype_rule_candidate": true, "counterexample_count": 4, "current_profile_error_count": 3, "do_not_propose_new_weight_delta": false, "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage2_required_bridge"], "existing_axis_weakened": null, "loop_contribution_label": "canonical_archetype_rule_candidate", "loop_id": "R2_loop_113_C09", "need_to_30_after_loop": 14, "need_to_50_after_loop": 34, "new_axis_proposed": "C09_verified_order_margin_revision_bridge_required_before_yellow_or_green", "new_independent_case_count": 6, "new_symbol_count": 6, "positive_case_count": 2, "post_loop_expected_rows": 16, "pre_loop_index_rows": 10, "representative_rows_added": 6, "reused_case_count": 0, "row_type": "residual_contribution", "sector_specific_rule_candidate": true, "selected_priority_bucket": "Priority 0", "stage4b_case_count": 1}
```

## 10. Source Map

- `MAIN_PROMPT` (execution_prompt): https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt —
- `NO_REPEAT_INDEX` (coverage_index): https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md —
- `STOCK_WEB_MANIFEST` (price_manifest): https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json —
- `OROS_THEELEC_20240516` (evidence): https://www.thelec.kr/news/articleView.html?idxno=27898 — 2024-05-16 HBM PAD overlay equipment supply to Samsung; 4.8bn KRW, HBM pad/bump alignment yield relevance.
- `OROS_NEWS_PIM_20240104` (evidence): https://www.newspim.com/news/view/20240104000140 — Kiwoom report summary: packaging overlay OL-900nw, WaPIS-30 orders, 2025 sales target after qualification.
- `HPSP_OFFICIAL_20240116` (evidence): https://thehpsp.com/ko/bbs/board.php?bo_table=notice&wr_id=25 — Official release on HPA/HPO R&D, imec JDP, HPHA technology.
- `HPSP_MK_20240201` (evidence): https://www.mk.co.kr/en/economy/10934475 — Market-cap/HPHA mass-production/capacity narrative.
- `NEXTIN_DIGITIMES_20230905` (evidence): https://www.digitimes.com/news/a20230905PD204/nextin-south-korea-semiconductor-equipment-inspection-tool-china.html — US$200m Wuxi wafer inspection tools investment.
- `KCTECH_DAUM_EDAILY_20240524` (evidence): https://v.daum.net/v/yWakH5VZkk?f=p — CMP process-count/HBM stacking demand and Q1 revenue/profit bridge.
- `PARK_IR_20240820` (evidence_pdf): https://file.alphasquare.co.kr/media/pdfs/company-ir/20240820%ED%8C%8C%ED%81%AC%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%8A%A4_%EA%B2%BD%EC%98%81_%ED%98%84%ED%99%A9_%EB%B0%8F_%EC%8B%A4%EC%A0%81_%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8.pdf — 2024 Q2 revenue/profit growth; industrial product shipment ramp.
- `WONIK_SAMSUNG_20240530` (evidence_pdf): https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024053008535715K_02_04.pdf&inlineYn=Y&saveKey=research.pdf — BUY upgrade but explicit bridge conflict: limited front-end capex, HBM insufficiency, weak NAND/customer share.
- `PROFILE_322310` (stock-web symbol profile): https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/322/322310.json — corporate_action_candidate_count=0; blocked_window=False
- `PROFILE_403870` (stock-web symbol profile): https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/403/403870.json — corporate_action_candidate_count=2; blocked_window=False
- `PROFILE_348210` (stock-web symbol profile): https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/348/348210.json — corporate_action_candidate_count=2; blocked_window=False
- `PROFILE_281820` (stock-web symbol profile): https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/281/281820.json — corporate_action_candidate_count=0; blocked_window=False
- `PROFILE_140860` (stock-web symbol profile): https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/140/140860.json — corporate_action_candidate_count=0; blocked_window=False
- `PROFILE_240810` (stock-web symbol profile): https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/240/240810.json — corporate_action_candidate_count=0; blocked_window=False

## 11. Deferred Coding Agent Handoff Prompt

```text
Read this Markdown artifact as a V12 historical calibration research input only.
Do not live-scan, do not recommend trades, do not connect brokerage APIs, and do not change production scoring directly.
Parse the JSONL rows under "Machine-Readable JSONL Rows".
Validate all trigger rows against Songdaiki/stock-web tradable_raw OHLC shards and symbol profiles.
Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
If rows pass validation, add them to the representative V12 calibration corpus.
Treat the C09 patch as a shadow candidate: require verified order/backlog/shipment/revenue/margin/revision bridge before Stage2-Actionable or Stage3-Yellow; otherwise cap at Watch/Stage1.5 or Stage4B-LocalWatch when price is extended.
Do not loosen Stage3-Green globally.
Do not convert this research artifact into a production profile patch without aggregate-level promotion rules passing.
```

## 12. Next Round State

```yaml
this_loop_contribution_label: canonical_archetype_rule_candidate
next_recommended_archetypes:
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
avoid_immediate_reuse:
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```
