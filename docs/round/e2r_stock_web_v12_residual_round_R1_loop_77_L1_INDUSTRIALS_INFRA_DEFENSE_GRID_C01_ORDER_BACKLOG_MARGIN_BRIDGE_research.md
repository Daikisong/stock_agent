# E2R Stock-Web v12 Residual Research — R1 Loop 77 / L1 / C01

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 77,
  "computed_next_round": "R2",
  "computed_next_loop": 77,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "shipbuilding_orderbook_margin_guardrail",
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

Previous completed state in this interactive run: R13 / loop 76.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 77
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
computed_next_round = R2
computed_next_loop = 77
```

R1 was routed to C01 because loop 76 used C02 and recent visible R1 coverage already shows C03/C04.  
This file tests shipbuilding/offshore orderbook and margin bridge behavior rather than power-grid capex, defense export or nuclear policy.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Visible No-Repeat R1 concentration:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

C01 is not present in the visible coverage slice, so this run uses new symbols and new trigger families:

```text
010140 / 삼성중공업 / shipbuilding LNG-offshore orderbook margin bridge
329180 / HD현대중공업 / large shipbuilding naval-LNG orderbook margin bridge
100090 / SK오션플랜트 / offshore plant project-backlog beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C01 is not “산업재 주가가 올랐다.”

The mechanism must pass through:

```text
order / backlog / project award
→ customer quality and delivery slot
→ ASP, product mix or utilization
→ margin conversion
→ durable rerating
```

수주잔고는 창고에 쌓인 종이가 아니다.  
좋은 C01은 그 종이가 선표, 납기, 단가, 마진으로 변할 때 살아난다.

---

## Case 1 — Positive with lifecycle 4B: 010140 / 삼성중공업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is LNG/offshore shipbuilding orderbook, customer quality, delivery schedule, ASP/product mix and margin bridge evidence.

```text
evidence_family = SHIPBUILDING_LNG_OFFSHORE_ORDERBOOK_MIX_PRICING_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,270
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv`:

```text
2024-02-01,7270,7310,7100,7140
2024-03-15,9200,9390,8810,8850
2024-05-13,9980,10300,9940,10170
2024-07-26,11190,12280,11100,11870
2024-10-31,9600,9680,9420,9590
```

### Backtest

```text
MFE_30D  = +29.16%
MAE_30D  = -2.34%
MFE_90D  = +41.68%
MAE_90D  = -2.34%
MFE_180D = +68.91%
MAE_180D = -2.34%
peak_180 = 12,280 on 2024-07-26
trough_180 = 7,100 on 2024-02-01
peak_to_later_drawdown = -23.29%
```

### Interpretation

This is a C01 positive-shaped path.  
The entry-basis MAE was controlled and the MFE expanded over months.

Correct treatment:

```text
verified backlog / delivery slot / ASP / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Positive with lifecycle 4B: 329180 / HD현대중공업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is naval/LNG orderbook, customer quality, delivery slot, ASP and margin bridge evidence.

```text
evidence_family = LARGE_SHIPBUILDING_NAVAL_LNG_ORDERBOOK_PRICING_DELIVERY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 114,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv`:

```text
2024-02-01,114300,114400,111200,112800
2024-03-20,122800,127800,122800,125800
2024-06-28,156600,158500,154000,155700
2024-08-09,221000,222500,208000,212000
2024-09-09,170600,177900,169900,177900
```

### Backtest

```text
MFE_30D  = +11.81%
MAE_30D  = -5.60%
MFE_90D  = +38.67%
MAE_90D  = -5.60%
MFE_180D = +94.66%
MAE_180D = -5.60%
peak_180 = 222,500 on 2024-08-09
trough_180 = 107,900 on 2024-02-14
peak_to_later_drawdown = -23.64%
```

### Interpretation

This is the cleaner large-cap C01 orderbook winner.  
It should not be overblocked if backlog, customer and margin evidence is repaired.

Correct treatment:

```text
Stage2 possible after source repair
lifecycle local 4B if orderbook/margin bridge fades
```

---

## Case 3 — Counterexample / local 4B: 100090 / SK오션플랜트

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests offshore-wind / offshore-plant project backlog beta without enough project award, utilization and margin bridge.

```text
evidence_family = OFFSHORE_WIND_PLANT_ORDERBOOK_THEME_WITH_WEAK_PROJECT_MARGIN_BRIDGE
case_role = counterexample_offshore_orderbook_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 15,570
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv`:

```text
2024-02-01,15570,15570,14980,15340
2024-02-16,16050,16390,15890,16170
2024-02-27,13100,13190,12820,12860
2024-08-05,12350,12400,10300,10880
2024-10-25,12870,13070,12450,12470
```

### Backtest

```text
MFE_30D  = +5.27%
MAE_30D  = -17.66%
MFE_90D  = +5.27%
MAE_90D  = -20.10%
MFE_180D = +5.27%
MAE_180D = -33.85%
peak_180 = 16,390 on 2024-02-16
trough_180 = 10,300 on 2024-08-05
peak_to_later_drawdown = -37.16%
```

### Interpretation

This is the C01 false-positive boundary.  
The first bounce did not become a durable orderbook rerating.

Correct treatment:

```text
offshore/project backlog beta
→ no project award / utilization / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C01_industrial_orderbook_weight = true
do_not_treat_all_shipbuilding_or_offshore_MFE_as_Green = true
do_not_convert_orderbook_drawdown_to_hard_4C_without_non_price_order_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE
```

This fine archetype covers:

```text
1. LNG/offshore shipbuilding backlog and ASP/margin bridge → Stage2 possible after source repair
2. large shipbuilding naval/LNG delivery-slot and margin bridge → Stage2 possible
3. offshore plant / offshore wind project beta without utilization/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN", "symbol": "010140", "company_name": "삼성중공업", "round": "R1", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-ShipbuildingOrderbookMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should allow shipbuilding orderbook Stage2 when backlog, LNG/offshore mix, pricing discipline, delivery schedule and margin bridge are visible. Samsung Heavy produced a large MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if backlog/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy project/order backlog, customer quality, delivery schedule, ASP/mix, utilization and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN", "symbol": "329180", "company_name": "HD현대중공업", "round": "R1", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-LargeShipbuildingOrderbookMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should preserve large shipbuilding orderbook winners when customer quality, delivery slots, naval/LNG mix, ASP and margin bridge are visible. HD Hyundai Heavy produced high MFE with controlled MAE; later drawdown should be lifecycle-managed, not treated as a hard 4C without order/margin break.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy project/order backlog, customer quality, delivery schedule, ASP/mix, utilization and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE", "symbol": "100090", "company_name": "SK오션플랜트", "round": "R1", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / OffshorePlantOrderbookBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should not treat offshore plant / orderbook beta as durable Stage2 unless project award, backlog conversion, delivery schedule, utilization and margin bridge are visible. SK Oceanplant had only small MFE and then a large MAE drawdown, making it local 4B-watch rather than a backlog Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy project/order backlog, customer quality, delivery schedule, ASP/mix, utilization and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN", "case_id": "R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN", "symbol": "010140", "company_name": "삼성중공업", "round": "R1", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|shipbuilding_orderbook_margin_guardrail", "trigger_type": "Stage2-Actionable-ShipbuildingOrderbookMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7270.0, "evidence_available_at_that_date": "SHIPBUILDING_LNG_OFFSHORE_ORDERBOOK_MIX_PRICING_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SAMSUNG_HEAVY_2024_SHIPBUILDING_LNG_OFFSHORE_ORDERBOOK_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_or_project_award_candidate", "customer_quality_or_delivery_slot_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "ASP_mix_utilization_bridge_candidate"], "stage4b_evidence_fields": ["backlog_or_project_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv", "profile_path": "atlas/symbol_profiles/010/010140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.16, "MFE_90D_pct": 41.68, "MFE_180D_pct": 68.91, "MAE_30D_pct": -2.34, "MAE_90D_pct": -2.34, "MAE_180D_pct": -2.34, "peak_date": "2024-07-26", "peak_price": 12280.0, "drawdown_after_peak_pct": -23.29, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_orderbook_peak_if_delivery_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_project_delay_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C01 should allow shipbuilding orderbook Stage2 when backlog, LNG/offshore mix, pricing discipline, delivery schedule and margin bridge are visible. Samsung Heavy produced a large MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if backlog/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C01_ORDERBOOK_010140_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN", "case_id": "R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN", "symbol": "329180", "company_name": "HD현대중공업", "round": "R1", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|shipbuilding_orderbook_margin_guardrail", "trigger_type": "Stage2-Actionable-LargeShipbuildingOrderbookMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 114300.0, "evidence_available_at_that_date": "LARGE_SHIPBUILDING_NAVAL_LNG_ORDERBOOK_PRICING_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HD_HYUNDAI_HEAVY_2024_SHIPBUILDING_NAVAL_LNG_ORDERBOOK_ASP_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_or_project_award_candidate", "customer_quality_or_delivery_slot_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "ASP_mix_utilization_bridge_candidate"], "stage4b_evidence_fields": ["backlog_or_project_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv", "profile_path": "atlas/symbol_profiles/329/329180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.81, "MFE_90D_pct": 38.67, "MFE_180D_pct": 94.66, "MAE_30D_pct": -5.6, "MAE_90D_pct": -5.6, "MAE_180D_pct": -5.6, "peak_date": "2024-08-09", "peak_price": 222500.0, "drawdown_after_peak_pct": -23.64, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_orderbook_peak_if_delivery_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_project_delay_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C01 should preserve large shipbuilding orderbook winners when customer quality, delivery slots, naval/LNG mix, ASP and margin bridge are visible. HD Hyundai Heavy produced high MFE with controlled MAE; later drawdown should be lifecycle-managed, not treated as a hard 4C without order/margin break.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C01_ORDERBOOK_329180_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE", "case_id": "R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE", "symbol": "100090", "company_name": "SK오션플랜트", "round": "R1", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|shipbuilding_orderbook_margin_guardrail", "trigger_type": "Stage2-FalsePositive / OffshorePlantOrderbookBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 15570.0, "evidence_available_at_that_date": "OFFSHORE_WIND_PLANT_ORDERBOOK_THEME_WITH_WEAK_PROJECT_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SK_OCEANPLANT_2024_OFFSHORE_WIND_PLANT_PROJECT_BACKLOG_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_or_project_award_candidate", "customer_quality_or_delivery_slot_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "ASP_mix_utilization_bridge_candidate"], "stage4b_evidence_fields": ["backlog_or_project_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv", "profile_path": "atlas/symbol_profiles/100/100090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.27, "MFE_90D_pct": 5.27, "MFE_180D_pct": 5.27, "MAE_30D_pct": -17.66, "MAE_90D_pct": -20.1, "MAE_180D_pct": -33.85, "peak_date": "2024-02-16", "peak_price": 16390.0, "drawdown_after_peak_pct": -37.16, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_orderbook_peak_if_delivery_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_project_delay_margin_or_financing_break", "trigger_outcome_label": "counterexample_offshore_orderbook_beta_local4b", "current_profile_verdict": "C01 should not treat offshore plant / orderbook beta as durable Stage2 unless project award, backlog conversion, delivery schedule, utilization and margin bridge are visible. SK Oceanplant had only small MFE and then a large MAE drawdown, making it local 4B-watch rather than a backlog Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C01_ORDERBOOK_100090_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN", "trigger_id": "TRG_R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN", "symbol": "010140", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 14, "customer_quality_score": 13, "delivery_slot_score": 13, "ASP_mix_score": 12, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"order_backlog_score": 16, "customer_quality_score": 15, "delivery_slot_score": 15, "ASP_mix_score": 14, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "customer_quality_score", "delivery_slot_score", "ASP_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified project/order backlog, customer quality, delivery slot, ASP/mix and margin bridge; cap offshore/orderbook beta when project/margin evidence fails to refresh.", "MFE_90D_pct": 41.68, "MAE_90D_pct": -2.34, "score_return_alignment_label": "orderbook_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C01 should allow shipbuilding orderbook Stage2 when backlog, LNG/offshore mix, pricing discipline, delivery schedule and margin bridge are visible. Samsung Heavy produced a large MFE with controlled entry-basis MAE, but post-peak drawdown requires lifecycle local 4B if backlog/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN", "trigger_id": "TRG_R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN", "symbol": "329180", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 14, "customer_quality_score": 13, "delivery_slot_score": 13, "ASP_mix_score": 12, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"order_backlog_score": 16, "customer_quality_score": 15, "delivery_slot_score": 15, "ASP_mix_score": 14, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "customer_quality_score", "delivery_slot_score", "ASP_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified project/order backlog, customer quality, delivery slot, ASP/mix and margin bridge; cap offshore/orderbook beta when project/margin evidence fails to refresh.", "MFE_90D_pct": 38.67, "MAE_90D_pct": -5.6, "score_return_alignment_label": "orderbook_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C01 should preserve large shipbuilding orderbook winners when customer quality, delivery slots, naval/LNG mix, ASP and margin bridge are visible. HD Hyundai Heavy produced high MFE with controlled MAE; later drawdown should be lifecycle-managed, not treated as a hard 4C without order/margin break."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE", "trigger_id": "TRG_R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE", "symbol": "100090", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 5, "customer_quality_score": 4, "delivery_slot_score": 3, "ASP_mix_score": 3, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 49, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"order_backlog_score": 3, "customer_quality_score": 2, "delivery_slot_score": 2, "ASP_mix_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 36, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["order_backlog_score", "customer_quality_score", "delivery_slot_score", "ASP_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified project/order backlog, customer quality, delivery slot, ASP/mix and margin bridge; cap offshore/orderbook beta when project/margin evidence fails to refresh.", "MFE_90D_pct": 5.27, "MAE_90D_pct": -20.1, "score_return_alignment_label": "false_positive_offshore_orderbook_bridge_gap", "current_profile_verdict": "C01 should not treat offshore plant / orderbook beta as durable Stage2 unless project award, backlog conversion, delivery schedule, utilization and margin bridge are visible. SK Oceanplant had only small MFE and then a large MAE drawdown, making it local 4B-watch rather than a backlog Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 77, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C01 industrial/shipbuilding orderbook symbols outside visible C03/C04 R1 coverage, +3 shipbuilding/offshore trigger families, +2 orderbook-margin positives, +1 offshore plant project-beta local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 77, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "axis": "shipbuilding_offshore_orderbook_mix_margin_bridge_vs_offshore_theme_backlog_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C01 should split verified shipbuilding/offshore orderbook margin bridges from project/backlog beta. Stage2 requires project/order backlog, customer quality, delivery slot, ASP or product mix and margin conversion. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["010140", "329180", "100090"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 77, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C01 needs backlog and margin proof. Samsung Heavy and HD Hyundai Heavy show shipbuilding orderbook/mix-margin positives after source repair; SK Oceanplant shows offshore project/backlog beta fading into local 4B when project award, utilization and margin bridge are absent."}
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
010140:
  corporate_action_candidate_dates = 1998-11-05, 1999-01-22, 1999-07-21, 2016-11-28, 2018-05-04, 2021-11-19
  selected window = 2024-02-01~D+180
  contamination = false

329180:
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

100090:
  corporate_action_candidate_dates = 2012-03-26, 2012-04-24, 2018-08-08, 2022-09-16
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C01 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C01 rule-shape discovery,
but coding-agent promotion requires non-proxy project/order backlog, customer quality, delivery schedule, ASP/mix, utilization and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C01 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
shipbuilding_offshore_orderbook_mix_margin_bridge_vs_offshore_theme_backlog_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 010140, 329180 and 100090.
4. Keep generic C01 order-backlog weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - project/order backlog is explicit,
   - customer quality and delivery slot are visible,
   - ASP, product mix, utilization or margin bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is orderbook/project/offshore beta only,
   - project award or margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, project delay, customer loss, capacity underutilization, financing or margin break.
8. Emit before/after diagnostics and reject if verified shipbuilding backlog/margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 77
next_round = R2
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

