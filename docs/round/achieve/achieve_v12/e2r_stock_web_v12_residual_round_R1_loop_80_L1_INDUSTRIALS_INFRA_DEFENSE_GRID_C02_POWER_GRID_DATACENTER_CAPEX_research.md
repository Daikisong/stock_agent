# E2R Stock-Web v12 Residual Research — R1 Loop 80 / L1 / C02

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 80,
  "computed_next_round": "R2",
  "computed_next_loop": 80,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "power_grid_datacenter_capex_guardrail",
    "power_cable_transformer_backlog_margin_bridge_vs_switchgear_theme_beta",
    "post_corporate_action_validation_queue_creation",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R13 / loop 79.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 80
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
computed_next_round = R2
computed_next_loop = 80
```

R1 was routed to C02 because loop 79 R1 used C01 and loop 79 R11 used C03.  
This file tests power cable / switchgear / grid-datacenter capex bridge rows.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Previous C02 loop material used names such as HD Hyundai Electric, LS ELECTRIC, Hyosung Heavy Industries, Jeil Electric, Daewon Cable, Iljin Electric, Gaon Cable, JeRyong Electric and Gwangmyeong Electric in older loops.  
This run focuses on three different or differently framed rows:

```text
001440 / 대한전선 / post-CA power-cable grid capex bridge
199820 / 제일일렉트릭 / post-CA switchgear theme fade
189860 / 서전기전 / switchgear/grid theme backlog gap
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
001440 and 199820 require post-corporate-action validation before runtime promotion.
```

## Research thesis

C02 is not “전력망 테마가 올랐다.”

The mechanism must pass through:

```text
grid / datacenter / utility capex
→ named customer or export order
→ order backlog
→ delivery schedule and revenue recognition
→ pricing / margin bridge
→ durable rerating
```

전력망 capex는 송전탑 그림이 아니다.  
C02가 보려는 것은 그 철탑 뒤에 실제 발주, 납기, 매출 인식, 마진 전류가 흐르는지다.

---

## Case 1 — Post-CA positive: 001440 / 대한전선

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
source_repair_required = true
```

The source-repair task is power cable grid/datacenter capex order backlog, export/customer quality, delivery schedule and margin bridge evidence.

```text
evidence_family = POWER_CABLE_GRID_DATACENTER_CAPEX_BACKLOG_EXPORT_ORDER_DELIVERY_MARGIN_BRIDGE_POST_CA
case_role = positive_post_CA_with_later_4b_watch
trigger_date = 2024-04-02
entry_date = 2024-04-03
entry_price = 10,830
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv`:

```text
2024-04-02,10620,11230,10410,10830
2024-04-03,10830,10910,10140,10720
2024-04-05,12630,13820,12010,12790
2024-05-13,15000,18900,14640,18110
2024-05-21,19890,20950,19020,19300
2024-08-05,12630,12870,11170,11580
2024-09-09,10370,10880,10270,10770
```

### Backtest

```text
MFE_30D  = +37.77%
MAE_30D  = -6.37%
MFE_90D  = +93.44%
MAE_90D  = -6.37%
MFE_180D = +93.44%
MAE_180D = -6.37%
peak_180 = 20,950 on 2024-05-21
trough_180 = 10,140 on 2024-04-03
peak_to_later_drawdown = -50.98%
```

### Interpretation

This is a C02 power-cable positive, but only after post-CA validation.  
The MFE was very large, but the later drawdown says backlog/delivery/margin bridge must refresh.

Correct treatment:

```text
verified cable order / export / delivery / margin bridge → Stage2 possible
post-CA validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Post-CA counterexample / local 4B: 199820 / 제일일렉트릭

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
source_repair_required = true
```

This row tests post-CA switchgear/circuit-breaker datacenter theme beta without enough order and margin bridge.

```text
evidence_family = SWITCHGEAR_CIRCUIT_BREAKER_DATACENTER_THEME_WITH_WEAK_POST_CA_ORDER_MARGIN_BRIDGE
case_role = counterexample_post_CA_switchgear_theme_local4b
trigger_date = 2024-06-11
entry_date = 2024-06-12
entry_price = 10,630
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/199/199820/2024.csv`:

```text
2024-06-11,11500,11630,10530,10530
2024-06-12,10630,10810,10110,10250
2024-06-28,9400,10840,9350,10050
2024-08-05,6710,6960,5700,6010
2024-09-11,8350,9330,7780,8700
2024-09-27,10820,11000,9670,9700
2024-10-25,8910,9500,8810,8810
```

### Backtest

```text
MFE_30D  = +3.48%
MAE_30D  = -22.86%
MFE_90D  = +3.48%
MAE_90D  = -46.38%
MFE_180D = +3.48%
MAE_180D = -46.38%
peak_180 = 11,000 on 2024-09-27
trough_180 = 5,700 on 2024-08-05
peak_to_later_drawdown = -47.09%
```

### Interpretation

This is a C02 post-CA false-positive boundary.  
The post-CA path did not validate durable order-backlog rerating.

Correct treatment:

```text
switchgear / datacenter theme beta
→ no verified post-CA order / delivery / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 189860 / 서전기전

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests switchgear/grid/nuclear/datacenter theme beta without enough named customer, backlog, delivery and margin bridge.

```text
evidence_family = SWITCHGEAR_GRID_NUCLEAR_DATACENTER_THEME_WITH_WEAK_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE
case_role = counterexample_switchgear_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,235
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv`:

```text
2024-02-01,4235,4245,4160,4235
2024-02-22,4265,4385,4220,4350
2024-03-07,4100,4135,3825,3925
2024-04-12,4295,4995,4295,4490
2024-07-24,6080,6210,5850,5960
2024-08-05,5350,5350,4510,4805
2024-10-11,4110,4145,4005,4080
```

### Backtest

```text
MFE_30D  = +3.54%
MAE_30D  = -9.68%
MFE_90D  = +17.95%
MAE_90D  = -9.68%
MFE_180D = +46.64%
MAE_180D = -9.68%
peak_180 = 6,210 on 2024-07-24
trough_180 = 3,825 on 2024-03-07
peak_to_later_drawdown = -35.51%
```

### Interpretation

This is a C02 theme-fade boundary.  
The MFE was tradable, but durable C02 requires order, delivery and margin proof.

Correct treatment:

```text
switchgear/grid theme beta
→ no verified named customer / backlog / delivery / margin bridge
→ local 4B-watch rather than durable Green
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
post_corporate_action_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C02_grid_capex_theme_weight = true
do_not_treat_all_power_grid_MFE_as_Green = true
do_not_ingest_post_CA_grid_rows_without_validation = true
do_not_convert_grid_theme_drawdown_to_hard_4C_without_non_price_order_delivery_margin_or_financing_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE
```

This fine archetype covers:

```text
1. post-CA cable/grid capex backlog bridge → Stage2 possible after source repair and CA validation
2. post-CA switchgear/circuit-breaker theme without bridge → false Stage2 / local 4B
3. switchgear/grid theme without order/delivery bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L80-C02-001440-DAEHAN-CABLE-POST-CA-GRID-CAPEX-BACKLOG", "symbol": "001440", "company_name": "대한전선", "round": "R1", "loop": "80", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-PostCAPowerCableGridCapexBacklogMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should allow power-cable positives when grid/datacenter capex maps to cable order backlog, export/customer quality, delivery schedule, revenue recognition and margin bridge. Daehan Cable produced a very large post-CA MFE, but runtime promotion requires post-CA continuity and source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy grid/datacenter capex, order backlog, customer quality, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L80-C02-199820-CHEIL-ELECTRIC-POST-CA-SWITCHGEAR-FADE", "symbol": "199820", "company_name": "제일일렉트릭", "round": "R1", "loop": "80", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / PostCASwitchgearDatacenterThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should not treat post-CA switchgear/datacenter theme beta as durable Stage2 unless order backlog, customer quality, delivery schedule, revenue recognition and margin bridge survive the corporate-action reset. Cheil Electric's post-CA path had small MFE and high MAE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy grid/datacenter capex, order backlog, customer quality, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L80-C02-189860-SEOJEON-ELECTRIC-SWITCHGEAR-THEME-BACKLOG-GAP", "symbol": "189860", "company_name": "서전기전", "round": "R1", "loop": "80", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SwitchgearGridThemeBacklogGap", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should not treat switchgear/grid/nuclear theme beta as durable Stage2 unless named customer, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Seojeon Electric produced tradable MFE, then a post-peak drawdown, making it local 4B-watch rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy grid/datacenter capex, order backlog, customer quality, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L80-C02-001440-DAEHAN-CABLE-POST-CA-GRID-CAPEX-BACKLOG", "case_id": "R1L80-C02-001440-DAEHAN-CABLE-POST-CA-GRID-CAPEX-BACKLOG", "symbol": "001440", "company_name": "대한전선", "round": "R1", "loop": "80", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-Actionable-PostCAPowerCableGridCapexBacklogMarginBridgeWithLifecycle4B", "trigger_date": "2024-04-02", "entry_date": "2024-04-03", "entry_price": 10830.0, "evidence_available_at_that_date": "POWER_CABLE_GRID_DATACENTER_CAPEX_BACKLOG_EXPORT_ORDER_DELIVERY_MARGIN_BRIDGE_POST_CA", "evidence_source": "source_proxy_manual_verification_required:DAEHAN_CABLE_2024_POWER_CABLE_GRID_DATACENTER_CAPEX_ORDER_BACKLOG_EXPORT_DELIVERY_MARGIN_BRIDGE_POST_CA", "stage2_evidence_fields": ["grid_datacenter_capex_candidate", "order_backlog_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_export_order_candidate"], "stage4b_evidence_fields": ["grid_or_switchgear_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv", "profile_path": "atlas/symbol_profiles/001/001440.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 37.77, "MFE_90D_pct": 93.44, "MFE_180D_pct": 93.44, "MAE_30D_pct": -6.37, "MAE_90D_pct": -6.37, "MAE_180D_pct": -6.37, "peak_date": "2024-05-21", "peak_price": 20950.0, "drawdown_after_peak_pct": -50.98, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_peak_if_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_post_CA_with_later_4b_watch", "current_profile_verdict": "C02 should allow power-cable positives when grid/datacenter capex maps to cable order backlog, export/customer quality, delivery schedule, revenue recognition and margin bridge. Daehan Cable produced a very large post-CA MFE, but runtime promotion requires post-CA continuity and source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C02_GRID_CAPEX_001440_2024-04-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L80-C02-199820-CHEIL-ELECTRIC-POST-CA-SWITCHGEAR-FADE", "case_id": "R1L80-C02-199820-CHEIL-ELECTRIC-POST-CA-SWITCHGEAR-FADE", "symbol": "199820", "company_name": "제일일렉트릭", "round": "R1", "loop": "80", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-FalsePositive / PostCASwitchgearDatacenterThemeFade", "trigger_date": "2024-06-11", "entry_date": "2024-06-12", "entry_price": 10630.0, "evidence_available_at_that_date": "SWITCHGEAR_CIRCUIT_BREAKER_DATACENTER_THEME_WITH_WEAK_POST_CA_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CHEIL_ELECTRIC_2024_SWITCHGEAR_CIRCUIT_BREAKER_DATACENTER_ORDER_MARGIN_BRIDGE_POST_CA", "stage2_evidence_fields": ["grid_datacenter_capex_candidate", "order_backlog_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_export_order_candidate"], "stage4b_evidence_fields": ["grid_or_switchgear_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/199/199820/2024.csv", "profile_path": "atlas/symbol_profiles/199/199820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.48, "MFE_90D_pct": 3.48, "MFE_180D_pct": 3.48, "MAE_30D_pct": -22.86, "MAE_90D_pct": -46.38, "MAE_180D_pct": -46.38, "peak_date": "2024-09-27", "peak_price": 11000.0, "drawdown_after_peak_pct": -47.09, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_peak_if_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_post_CA_switchgear_theme_local4b", "current_profile_verdict": "C02 should not treat post-CA switchgear/datacenter theme beta as durable Stage2 unless order backlog, customer quality, delivery schedule, revenue recognition and margin bridge survive the corporate-action reset. Cheil Electric's post-CA path had small MFE and high MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C02_GRID_CAPEX_199820_2024-06-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L80-C02-189860-SEOJEON-ELECTRIC-SWITCHGEAR-THEME-BACKLOG-GAP", "case_id": "R1L80-C02-189860-SEOJEON-ELECTRIC-SWITCHGEAR-THEME-BACKLOG-GAP", "symbol": "189860", "company_name": "서전기전", "round": "R1", "loop": "80", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-FalsePositive / SwitchgearGridThemeBacklogGap", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4235.0, "evidence_available_at_that_date": "SWITCHGEAR_GRID_NUCLEAR_DATACENTER_THEME_WITH_WEAK_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SEOJEON_ELECTRIC_2024_SWITCHGEAR_GRID_NUCLEAR_DATACENTER_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["grid_datacenter_capex_candidate", "order_backlog_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_export_order_candidate"], "stage4b_evidence_fields": ["grid_or_switchgear_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv", "profile_path": "atlas/symbol_profiles/189/189860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.54, "MFE_90D_pct": 17.95, "MFE_180D_pct": 46.64, "MAE_30D_pct": -9.68, "MAE_90D_pct": -9.68, "MAE_180D_pct": -9.68, "peak_date": "2024-07-24", "peak_price": 6210.0, "drawdown_after_peak_pct": -35.51, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_peak_if_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_switchgear_theme_local4b", "current_profile_verdict": "C02 should not treat switchgear/grid/nuclear theme beta as durable Stage2 unless named customer, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Seojeon Electric produced tradable MFE, then a post-peak drawdown, making it local 4B-watch rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C02_GRID_CAPEX_189860_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L80-C02-001440-DAEHAN-CABLE-POST-CA-GRID-CAPEX-BACKLOG", "trigger_id": "TRG_R1L80-C02-001440-DAEHAN-CABLE-POST-CA-GRID-CAPEX-BACKLOG", "symbol": "001440", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_score": 15, "order_backlog_score": 14, "customer_quality_score": 13, "delivery_revenue_score": 14, "margin_bridge_score": 14, "relative_strength_score": 14, "execution_risk_score": 9, "post_CA_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"grid_capex_score": 17, "order_backlog_score": 16, "customer_quality_score": 15, "delivery_revenue_score": 16, "margin_bridge_score": 16, "relative_strength_score": 13, "execution_risk_score": 10, "post_CA_validation_risk": 12, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["grid_capex_score", "order_backlog_score", "customer_quality_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified grid/datacenter capex, order backlog, customer/export quality, delivery/revenue and margin bridge; cap switchgear/theme beta when evidence fails to refresh or CA continuity is unvalidated.", "MFE_90D_pct": 93.44, "MAE_90D_pct": -6.37, "score_return_alignment_label": "power_cable_grid_capex_positive_with_lifecycle_4b", "current_profile_verdict": "C02 should allow power-cable positives when grid/datacenter capex maps to cable order backlog, export/customer quality, delivery schedule, revenue recognition and margin bridge. Daehan Cable produced a very large post-CA MFE, but runtime promotion requires post-CA continuity and source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L80-C02-199820-CHEIL-ELECTRIC-POST-CA-SWITCHGEAR-FADE", "trigger_id": "TRG_R1L80-C02-199820-CHEIL-ELECTRIC-POST-CA-SWITCHGEAR-FADE", "symbol": "199820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_score": 5, "order_backlog_score": 3, "customer_quality_score": 3, "delivery_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 22, "post_CA_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_before": 45, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"grid_capex_score": 3, "order_backlog_score": 1, "customer_quality_score": 1, "delivery_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "post_CA_validation_risk": 12, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["grid_capex_score", "order_backlog_score", "customer_quality_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified grid/datacenter capex, order backlog, customer/export quality, delivery/revenue and margin bridge; cap switchgear/theme beta when evidence fails to refresh or CA continuity is unvalidated.", "MFE_90D_pct": 3.48, "MAE_90D_pct": -46.38, "score_return_alignment_label": "false_positive_switchgear_grid_theme_bridge_gap", "current_profile_verdict": "C02 should not treat post-CA switchgear/datacenter theme beta as durable Stage2 unless order backlog, customer quality, delivery schedule, revenue recognition and margin bridge survive the corporate-action reset. Cheil Electric's post-CA path had small MFE and high MAE."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L80-C02-189860-SEOJEON-ELECTRIC-SWITCHGEAR-THEME-BACKLOG-GAP", "trigger_id": "TRG_R1L80-C02-189860-SEOJEON-ELECTRIC-SWITCHGEAR-THEME-BACKLOG-GAP", "symbol": "189860", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_score": 5, "order_backlog_score": 3, "customer_quality_score": 3, "delivery_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 22, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 45, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"grid_capex_score": 3, "order_backlog_score": 1, "customer_quality_score": 1, "delivery_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["grid_capex_score", "order_backlog_score", "customer_quality_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified grid/datacenter capex, order backlog, customer/export quality, delivery/revenue and margin bridge; cap switchgear/theme beta when evidence fails to refresh or CA continuity is unvalidated.", "MFE_90D_pct": 17.95, "MAE_90D_pct": -9.68, "score_return_alignment_label": "false_positive_switchgear_grid_theme_bridge_gap", "current_profile_verdict": "C02 should not treat switchgear/grid/nuclear theme beta as durable Stage2 unless named customer, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Seojeon Electric produced tradable MFE, then a post-peak drawdown, making it local 4B-watch rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 80, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_POST_CA_GRID_CAPEX_BRIDGE_VS_SWITCHGEAR_POST_CA_AND_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "post_corporate_action_validation_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C02 grid/cable/switchgear symbols outside loop-78/79 C02 names, +3 post-CA cable/post-CA switchgear/theme-fade trigger families, +1 power-cable post-CA positive, +2 switchgear/grid theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_post_CA_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 80, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "axis": "power_cable_post_CA_grid_capex_bridge_vs_switchgear_post_CA_and_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C02 should split verified power-cable/grid capex order-backlog margin rerating from switchgear/electrical theme beta and unvalidated post-CA paths. Stage2 requires grid/datacenter capex, named customer/export order, backlog, delivery schedule, revenue recognition and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Post-CA rows require continuity validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["001440", "199820", "189860"], "post_corporate_action_validation_required": ["001440", "199820"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 80, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "post_corporate_action_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C02 needs grid/datacenter capex, order backlog, customer/export quality, delivery and margin proof. Daehan Cable shows a post-CA power-cable MFE candidate after source repair; Cheil Electric and Seojeon Electric show switchgear/grid theme beta fading into local 4B when order, delivery and margin bridge are absent or CA continuity is unvalidated."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
001440:
  name = 대한전선
  corporate_action_candidate_dates = 2002-04-22, 2003-10-13, 2010-05-03, 2010-10-18, 2012-11-08, 2012-12-21, 2014-01-10, 2015-12-08, 2022-03-30, 2023-05-16, 2024-04-02
  selected entry starts 2024-04-03 after the 2024-04-02 candidate
  contamination = false after post-CA entry, but coding-agent validation required

199820:
  name = 제일일렉트릭 from 2024-05-08, 제일전기공업 before that
  corporate_action_candidate_dates = 2024-05-21, 2024-06-11
  selected entry starts 2024-06-12 after the 2024-06-11 candidate
  contamination = false after post-CA entry, but coding-agent validation required

189860:
  name = 서전기전
  corporate_action_candidate_dates = 2018-11-16
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C02 rows are source_proxy_only / evidence_url_pending.
001440 and 199820 also require post-corporate-action validation before runtime promotion.
This MD is useful for stock-web path calibration and C02 rule-shape discovery,
but coding-agent promotion requires non-proxy grid/datacenter capex, order backlog, customer quality, delivery schedule, revenue recognition and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C02 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 001440/199820 need post-CA validation.

Candidate axis:
power_cable_post_CA_grid_capex_bridge_vs_switchgear_post_CA_and_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 001440, 199820 and 189860.
4. Validate 001440 post-CA continuity after 2024-04-02.
5. Validate 199820 post-CA continuity after 2024-05-21 and 2024-06-11.
6. Keep generic C02 grid/datacenter capex weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - grid/datacenter capex is explicit,
   - named customer/export order or backlog is visible,
   - delivery schedule and revenue recognition are visible,
   - pricing or margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
8. Consider local 4B-watch when:
   - the trigger is grid/switchgear theme beta only,
   - order/delivery/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, delivery delay, customer loss, financing or margin break.
10. Emit before/after diagnostics and reject if verified cable/grid capex positives or post-CA rows are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 80
next_round = R2
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

