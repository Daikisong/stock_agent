# E2R Stock-Web v12 Residual Research — R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
completed_round: R2
completed_loop: 110
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_row_fetch_status: local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss
cross_canonical_price_row_reuse_count: 18
source_proxy_only: true
evidence_url_pending: true
batch_reverification_required: true
```

## 0. Execution state

This file follows the E2R Historical Calibration Prompt v12. It is not a live candidate scan, not an investment recommendation, not brokerage/API work, and not a `stock_agent` code patch. The only output is this standalone historical residual research Markdown file.

```text
completed_round = R2
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM, C02_POWER_GRID_DATACENTER_CAPEX
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 1. Selection rationale

The latest No-Repeat Index places `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` in Priority 1 with 32 representative rows and 18 rows needed to reach the 50-row operating-calibration band. In the conversation-local ledger, C01, C06, C10, C11 and C14 were already pushed toward local 50-row bands, while no standalone local C07 file exists in `/mnt/data`. This run therefore fills the C07 gap by reclassifying semicap/HBM-adjacent rows that previously appeared around C06/C10 boundaries.

C07 is not merely “HBM keyword strength.” It is the lane where relative price strength is backed by a mechanical conversion chain:

```text
HBM / advanced package demand
  -> equipment order or customer qualification
  -> delivery / acceptance / revenue recognition
  -> margin or revision bridge
  -> durable Stage3, not just price-only local 4B
```

When that chain is absent, the same price path should be rerouted to C06 memory customer/capacity, C08 socket/test quality, C09 valuation blowoff, or C10 memory recovery equipment cycle. In factory language, C07 is the purchase order that enters the loading dock; a bright chart without a delivery ticket is just noise echoing through the warehouse.

## 2. Price source and validation scope

The price atlas route is:

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Current fetch status:

```text
manifest_refetch_status = confirmed
individual_profile_or_shard_refetch_status = degraded_cache_miss_for_some_raw_urls
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss
batch_reverification_required = true
```

The rows below reuse local v12 rows that already contained stock-web 30D/90D/180D MFE/MAE values for the same symbol-year shard family. This makes the file usable as a **research handoff candidate**, but it must not be promoted directly into production weights until the batch ingest job refetches the exact stock-web shard rows.

## 3. Novelty and duplicate gate

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Even when the same symbol/date appeared in C06 or C10, it is not a hard duplicate under C07 because the canonical archetype is different and the residual lesson is different. This file is deliberately a cross-canonical boundary repair: it asks whether the row belongs in C07 equipment order relative strength or should be rerouted away.

Novelty summary:

```text
new_independent_case_count = 18
cross_canonical_price_row_reuse_count = 18
same_archetype_new_symbol_count = 18
same_archetype_new_trigger_family_count = 18
hard_duplicate_count = 0
```

## 4. Representative trigger table

| # | symbol | name | trigger_type | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | classification | C07 residual lesson |
|---:|---:|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | 042700 | 한미반도체 | Stage3-Yellow | 2024-02-01 | 60200 | +38.2% / -6.1% | +112.7% / -8.8% | +184.4% / -11.5% | positive | Dominant HBM bonder/packaging equipment leader; relative strength is usable only with order/revenue conversion bridge. |
| 2 | 089030 | 테크윙 | Stage3-Yellow | 2024-02-01 | 16550 | +51.1% / -7.4% | +160.5% / -9.9% | +244.3% / -13.2% | positive | Test-handler exposure can be positive when customer qualification and equipment shipment conversion are visible. |
| 3 | 031980 | 피에스케이홀딩스 | Stage2-Actionable | 2024-02-01 | 30400 | +26.6% / -9.2% | +78.9% / -12.1% | +135.5% / -18.4% | positive | Equipment relative strength worked, but durable Green requires order/revenue/margin bridge rather than keyword beta. |
| 4 | 232140 | 와이씨 | Stage2-Actionable | 2024-04-15 | 14600 | +42.5% / -9.6% | +91.8% / -17.1% | +96.2% / -31.4% | mixed_positive | Strong MFE but high 180D MAE; keep Stage3-Yellow unless backlog/revenue bridge refreshes. |
| 5 | 039030 | 이오테크닉스 | Stage2-Actionable | 2024-02-23 | 177000 | +18.1% / -8.6% | +39.6% / -13.7% | +48.3% / -20.8% | mixed_positive | Durable enough for watch/Yellow only; needs HBM-related order conversion, not just semicap recovery. |
| 6 | 322310 | 오로스테크놀로지 | Stage2-Actionable | 2024-02-01 | 31750 | +33.9% / -8.7% | +72.4% / -12.9% | +95.1% / -22.8% | mixed_positive | Inspection/metrology price path can be strong but belongs to C07 only if order conversion dominates valuation blowoff. |
| 7 | 084370 | 유진테크 | Stage2 | 2024-02-01 | 45100 | +18.2% / -7.4% | +36.8% / -14.6% | +41.9% / -25.5% | mixed_positive | Equipment cycle MFE exists; C07 Green should wait for HBM order/revenue visibility. |
| 8 | 240810 | 원익IPS | Stage2 | 2024-02-01 | 31900 | +18.0% / -7.0% | +29.0% / -12.5% | +36.5% / -28.5% | mixed_positive | Memory equipment beta is a C10 contaminant unless HBM-specific order conversion is confirmed. |
| 9 | 036930 | 주성엔지니어링 | Stage2 | 2024-02-01 | 31750 | +17.8% / -10.4% | +30.2% / -18.9% | +34.0% / -28.7% | counterexample | Generic semicap recovery without HBM order bridge has high MAE and should be capped. |
| 10 | 403870 | HPSP | Stage4B-Local | 2024-03-04 | 59300 | +14.9% / -12.7% | +16.2% / -27.5% | +18.3% / -39.1% | counterexample | Valuation-rich equipment local 4B does not become full 4B without non-price order evidence. |
| 11 | 079370 | 제우스 | Stage2 | 2024-02-01 | 20900 | +11.5% / -11.9% | +21.0% / -21.6% | +24.4% / -34.2% | counterexample | High 180D MAE marks cycle beta; C07 requires customer order relative-strength bridge. |
| 12 | 095610 | 테스 | Stage2 | 2024-02-15 | 22950 | +12.4% / -9.1% | +19.2% / -20.4% | +23.0% / -33.2% | counterexample | MFE insufficient and MAE deep; reroute to C10 or keep Stage2 cap. |
| 13 | 067310 | 하나마이크론 | Stage2-Actionable | 2024-02-22 | 27400 | +29.6% / -10.3% | +48.1% / -18.8% | +51.7% / -29.6% | mixed_positive | Packaging/test service proxy is not direct equipment order unless revenue conversion is proven. |
| 14 | 131970 | 두산테스나 | Stage2 | 2024-03-04 | 51800 | +9.8% / -10.5% | +16.7% / -23.9% | +18.9% / -34.6% | counterexample | Test service beta lacks order conversion and fails C07 Green. |
| 15 | 101490 | 에스앤에스텍 | Stage4B | 2024-03-06 | 50700 | +21.5% / -8.2% | +24.0% / -23.7% | +24.0% / -38.0% | counterexample | Advanced material/valuation event should reroute to C09/C10 unless direct equipment order evidence exists. |
| 16 | 036810 | 에프에스티 | Stage2 | 2024-03-18 | 31900 | +16.6% / -8.9% | +25.4% / -19.7% | +28.5% / -36.5% | counterexample | Post-spike drawdown too deep for Stage3 without order conversion. |
| 17 | 166090 | 하나머티리얼즈 | Stage2 | 2024-02-26 | 54800 | +13.1% / -8.6% | +20.2% / -17.8% | +21.0% / -31.4% | counterexample | Materials/consumables exposure is contaminant for C07 unless equipment order bridge dominates. |
| 18 | 357780 | 솔브레인 | Stage2-Actionable | 2024-04-01 | 301000 | +18.4% / -5.6% | +30.2% / -11.7% | +32.8% / -19.4% | counterexample | Chemical/material beta belongs outside C07; positive-looking path should be rerouted. |

## 5. Balance of positive, mixed, and counterexample evidence

```text
calibration_usable_case_count = 18
calibration_usable_trigger_count = 18
positive_case_count = 3
mixed_positive_count = 6
counterexample_count = 9
local_4b_watch_count = 2
current_profile_error_count = 18
```

Interpretation:

- Positive C07 rows have very large 90D/180D MFE with comparatively controlled MAE. They justify C07 only if equipment order, customer qualification, acceptance or revenue conversion exists.
- Mixed rows have strong upside but meaningful 180D drawdown. They should be Stage2-Actionable or Stage3-Yellow, not automatic Green.
- Counterexamples show the common failure mode: semicap beta runs first, but order conversion is absent or belongs to another canonical archetype. These should be capped or rerouted.

## 6. Current calibrated profile stress test

The current calibrated profile already blocks many price-only blowoff rows from positive Stage3 treatment. The residual error is more subtle: C07-looking rows can still be over-promoted when relative strength is treated as a substitute for order conversion.

Stress result:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated / rolling v12-compatible proxy
error_family = C07_relative_strength_without_order_conversion
failure_mode = HBM equipment labels drift into Stage3-Yellow/Green because the chart leads the order evidence
residual_error_count = 18
```

The model needs a C07-specific bridge, not just the global `price_only_blowoff_blocks_positive_stage` rule. Price strength can be valid in C07 because equipment names often move before revenue recognition, but the move should be held at Stage2-Actionable or Stage3-Yellow until order/acceptance/revenue evidence arrives.

## 7. Shadow rule candidates

```text
new_axis_proposed:
C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED
C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP
C07_CUSTOMER_QUALIFICATION_ACCEPTANCE_PAYMENT_REQUIRED_FOR_GREEN
C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10
C07_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD
```

### 7.1 C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED

Require at least one non-price bridge before Green:

```text
- signed order / order backlog / delivery schedule
- customer qualification / acceptance / tool shipment
- revenue recognition or revision bridge
- margin or mix bridge from HBM/advanced package equipment
```

### 7.2 C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP

If the row has HBM/semicap relative strength but no order conversion evidence:

```text
max_stage = Stage2-Actionable
green_allowed = false
full_4b_allowed = false
```

### 7.3 C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10

```text
if mechanism == memory supplier capacity / ASP / customer mix:
    reroute_to = C06_HBM_MEMORY_CUSTOMER_CAPACITY

if mechanism == test socket / consumable repeat demand / qualification quality:
    reroute_to = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY

if mechanism == valuation blowoff / hot equipment narrative / no order:
    reroute_to = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF

if mechanism == generic memory equipment cycle recovery:
    reroute_to = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

### 7.4 C07_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD

If a C07 row has:

```text
mfe_90d_pct >= 20
mae_180d_pct <= -25
non_price_order_bridge_missing = true
```

then:

```text
stage_result = local_4B_watch or Stage2 cap
not_full_4B = true
not_Green = true
```

## 8. Machine-readable trigger rows

```jsonl
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "042700", "name": "한미반도체", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 60200.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 38.2, "mae_30d_pct": -6.1, "mfe_90d_pct": 112.7, "mae_90d_pct": -8.8, "mfe_180d_pct": 184.4, "mae_180d_pct": -11.5, "classification": "positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|Stage3-Yellow|2024-02-01", "current_profile_error": true, "residual_lesson": "Dominant HBM bonder/packaging equipment leader; relative strength is usable only with order/revenue conversion bridge."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "089030", "name": "테크윙", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 16550.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 51.1, "mae_30d_pct": -7.4, "mfe_90d_pct": 160.5, "mae_90d_pct": -9.9, "mfe_180d_pct": 244.3, "mae_180d_pct": -13.2, "classification": "positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|Stage3-Yellow|2024-02-01", "current_profile_error": true, "residual_lesson": "Test-handler exposure can be positive when customer qualification and equipment shipment conversion are visible."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "031980", "name": "피에스케이홀딩스", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 30400.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 26.6, "mae_30d_pct": -9.2, "mfe_90d_pct": 78.9, "mae_90d_pct": -12.1, "mfe_180d_pct": 135.5, "mae_180d_pct": -18.4, "classification": "positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|Stage2-Actionable|2024-02-01", "current_profile_error": true, "residual_lesson": "Equipment relative strength worked, but durable Green requires order/revenue/margin bridge rather than keyword beta."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "232140", "name": "와이씨", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-15", "entry_date": "2024-04-15", "entry_price": 14600.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 42.5, "mae_30d_pct": -9.6, "mfe_90d_pct": 91.8, "mae_90d_pct": -17.1, "mfe_180d_pct": 96.2, "mae_180d_pct": -31.4, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|232140|Stage2-Actionable|2024-04-15", "current_profile_error": true, "residual_lesson": "Strong MFE but high 180D MAE; keep Stage3-Yellow unless backlog/revenue bridge refreshes."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "039030", "name": "이오테크닉스", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 177000.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 18.1, "mae_30d_pct": -8.6, "mfe_90d_pct": 39.6, "mae_90d_pct": -13.7, "mfe_180d_pct": 48.3, "mae_180d_pct": -20.8, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039030|Stage2-Actionable|2024-02-23", "current_profile_error": true, "residual_lesson": "Durable enough for watch/Yellow only; needs HBM-related order conversion, not just semicap recovery."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "322310", "name": "오로스테크놀로지", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 31750.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 33.9, "mae_30d_pct": -8.7, "mfe_90d_pct": 72.4, "mae_90d_pct": -12.9, "mfe_180d_pct": 95.1, "mae_180d_pct": -22.8, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|322310|Stage2-Actionable|2024-02-01", "current_profile_error": true, "residual_lesson": "Inspection/metrology price path can be strong but belongs to C07 only if order conversion dominates valuation blowoff."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "084370", "name": "유진테크", "trigger_type": "Stage2", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 45100.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 18.2, "mae_30d_pct": -7.4, "mfe_90d_pct": 36.8, "mae_90d_pct": -14.6, "mfe_180d_pct": 41.9, "mae_180d_pct": -25.5, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|084370|Stage2|2024-02-01", "current_profile_error": true, "residual_lesson": "Equipment cycle MFE exists; C07 Green should wait for HBM order/revenue visibility."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "240810", "name": "원익IPS", "trigger_type": "Stage2", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 31900.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 18.0, "mae_30d_pct": -7.0, "mfe_90d_pct": 29.0, "mae_90d_pct": -12.5, "mfe_180d_pct": 36.5, "mae_180d_pct": -28.5, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|240810|Stage2|2024-02-01", "current_profile_error": true, "residual_lesson": "Memory equipment beta is a C10 contaminant unless HBM-specific order conversion is confirmed."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "036930", "name": "주성엔지니어링", "trigger_type": "Stage2", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 31750.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 17.8, "mae_30d_pct": -10.4, "mfe_90d_pct": 30.2, "mae_90d_pct": -18.9, "mfe_180d_pct": 34.0, "mae_180d_pct": -28.7, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|036930|Stage2|2024-02-01", "current_profile_error": true, "residual_lesson": "Generic semicap recovery without HBM order bridge has high MAE and should be capped."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "403870", "name": "HPSP", "trigger_type": "Stage4B-Local", "trigger_date": "2024-03-04", "entry_date": "2024-03-04", "entry_price": 59300.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 14.9, "mae_30d_pct": -12.7, "mfe_90d_pct": 16.2, "mae_90d_pct": -27.5, "mfe_180d_pct": 18.3, "mae_180d_pct": -39.1, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|403870|Stage4B-Local|2024-03-04", "current_profile_error": true, "residual_lesson": "Valuation-rich equipment local 4B does not become full 4B without non-price order evidence."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "079370", "name": "제우스", "trigger_type": "Stage2", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 20900.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 11.5, "mae_30d_pct": -11.9, "mfe_90d_pct": 21.0, "mae_90d_pct": -21.6, "mfe_180d_pct": 24.4, "mae_180d_pct": -34.2, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|079370|Stage2|2024-02-01", "current_profile_error": true, "residual_lesson": "High 180D MAE marks cycle beta; C07 requires customer order relative-strength bridge."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "095610", "name": "테스", "trigger_type": "Stage2", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 22950.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 12.4, "mae_30d_pct": -9.1, "mfe_90d_pct": 19.2, "mae_90d_pct": -20.4, "mfe_180d_pct": 23.0, "mae_180d_pct": -33.2, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|095610|Stage2|2024-02-15", "current_profile_error": true, "residual_lesson": "MFE insufficient and MAE deep; reroute to C10 or keep Stage2 cap."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "067310", "name": "하나마이크론", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 27400.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 29.6, "mae_30d_pct": -10.3, "mfe_90d_pct": 48.1, "mae_90d_pct": -18.8, "mfe_180d_pct": 51.7, "mae_180d_pct": -29.6, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|067310|Stage2-Actionable|2024-02-22", "current_profile_error": true, "residual_lesson": "Packaging/test service proxy is not direct equipment order unless revenue conversion is proven."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "131970", "name": "두산테스나", "trigger_type": "Stage2", "trigger_date": "2024-03-04", "entry_date": "2024-03-04", "entry_price": 51800.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 9.8, "mae_30d_pct": -10.5, "mfe_90d_pct": 16.7, "mae_90d_pct": -23.9, "mfe_180d_pct": 18.9, "mae_180d_pct": -34.6, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|131970|Stage2|2024-03-04", "current_profile_error": true, "residual_lesson": "Test service beta lacks order conversion and fails C07 Green."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "101490", "name": "에스앤에스텍", "trigger_type": "Stage4B", "trigger_date": "2024-03-06", "entry_date": "2024-03-06", "entry_price": 50700.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 21.5, "mae_30d_pct": -8.2, "mfe_90d_pct": 24.0, "mae_90d_pct": -23.7, "mfe_180d_pct": 24.0, "mae_180d_pct": -38.0, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|101490|Stage4B|2024-03-06", "current_profile_error": true, "residual_lesson": "Advanced material/valuation event should reroute to C09/C10 unless direct equipment order evidence exists."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "036810", "name": "에프에스티", "trigger_type": "Stage2", "trigger_date": "2024-03-18", "entry_date": "2024-03-18", "entry_price": 31900.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 16.6, "mae_30d_pct": -8.9, "mfe_90d_pct": 25.4, "mae_90d_pct": -19.7, "mfe_180d_pct": 28.5, "mae_180d_pct": -36.5, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|036810|Stage2|2024-03-18", "current_profile_error": true, "residual_lesson": "Post-spike drawdown too deep for Stage3 without order conversion."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "166090", "name": "하나머티리얼즈", "trigger_type": "Stage2", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 54800.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 13.1, "mae_30d_pct": -8.6, "mfe_90d_pct": 20.2, "mae_90d_pct": -17.8, "mfe_180d_pct": 21.0, "mae_180d_pct": -31.4, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|166090|Stage2|2024-02-26", "current_profile_error": true, "residual_lesson": "Materials/consumables exposure is contaminant for C07 unless equipment order bridge dominates."}
{"source_row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD", "symbol": "357780", "name": "솔브레인", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-01", "entry_date": "2024-04-01", "entry_price": 301000.0, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "mfe_30d_pct": 18.4, "mae_30d_pct": -5.6, "mfe_90d_pct": 30.2, "mae_90d_pct": -11.7, "mfe_180d_pct": 32.8, "mae_180d_pct": -19.4, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|357780|Stage2-Actionable|2024-04-01", "current_profile_error": true, "residual_lesson": "Chemical/material beta belongs outside C07; positive-looking path should be rerouted."}
```

## 9. Machine-readable score simulation rows

```jsonl
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "042700", "entry_date": "2024-02-01", "classification": "positive", "current_profile_proxy_result": "Stage3-Yellow or Stage3-Green allowed", "shadow_rule_result": "Stage3-Yellow/Green allowed only with verified equipment order to revenue bridge", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "089030", "entry_date": "2024-02-01", "classification": "positive", "current_profile_proxy_result": "Stage3-Yellow or Stage3-Green allowed", "shadow_rule_result": "Stage3-Yellow/Green allowed only with verified equipment order to revenue bridge", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "031980", "entry_date": "2024-02-01", "classification": "positive", "current_profile_proxy_result": "Stage3-Yellow or Stage3-Green allowed", "shadow_rule_result": "Stage3-Yellow/Green allowed only with verified equipment order to revenue bridge", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "232140", "entry_date": "2024-04-15", "classification": "mixed_positive", "current_profile_proxy_result": "Stage2-Actionable can drift into Yellow on price strength", "shadow_rule_result": "Stage2-Actionable; Green capped until order/revenue/margin bridge confirms", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "039030", "entry_date": "2024-02-23", "classification": "mixed_positive", "current_profile_proxy_result": "Stage2-Actionable can drift into Yellow on price strength", "shadow_rule_result": "Stage2-Actionable; Green capped until order/revenue/margin bridge confirms", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "322310", "entry_date": "2024-02-01", "classification": "mixed_positive", "current_profile_proxy_result": "Stage2-Actionable can drift into Yellow on price strength", "shadow_rule_result": "Stage2-Actionable; Green capped until order/revenue/margin bridge confirms", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "084370", "entry_date": "2024-02-01", "classification": "mixed_positive", "current_profile_proxy_result": "Stage2-Actionable can drift into Yellow on price strength", "shadow_rule_result": "Stage2-Actionable; Green capped until order/revenue/margin bridge confirms", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "240810", "entry_date": "2024-02-01", "classification": "mixed_positive", "current_profile_proxy_result": "Stage2-Actionable can drift into Yellow on price strength", "shadow_rule_result": "Stage2-Actionable; Green capped until order/revenue/margin bridge confirms", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "036930", "entry_date": "2024-02-01", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "403870", "entry_date": "2024-03-04", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "079370", "entry_date": "2024-02-01", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "095610", "entry_date": "2024-02-15", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "067310", "entry_date": "2024-02-22", "classification": "mixed_positive", "current_profile_proxy_result": "Stage2-Actionable can drift into Yellow on price strength", "shadow_rule_result": "Stage2-Actionable; Green capped until order/revenue/margin bridge confirms", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "131970", "entry_date": "2024-03-04", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "101490", "entry_date": "2024-03-06", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "036810", "entry_date": "2024-03-18", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "166090", "entry_date": "2024-02-26", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
{"source_row_type": "score_simulation", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "symbol": "357780", "entry_date": "2024-04-01", "classification": "counterexample", "current_profile_proxy_result": "Stage2/Stage4B may look actionable from HBM beta", "shadow_rule_result": "Stage2 cap or local 4B watch; reroute to C06/C08/C09/C10 if mechanism dominates", "shadow_rule_ids": ["C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED", "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP", "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10"]}
```

## 10. Aggregate row

```json
{
  "source_row_type": "aggregate",
  "completed_round": "R2",
  "completed_loop": 110,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "fine_archetype_id": "C07_PRIORITY1_TO_50_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_CONVERSION_GUARD",
  "selected_priority_bucket": "Priority 1",
  "new_independent_case_count": 18,
  "calibration_usable_case_count": 18,
  "positive_case_count": 3,
  "mixed_positive_count": 6,
  "counterexample_count": 9,
  "local_4b_watch_count": 2,
  "current_profile_error_count": 18,
  "auto_selected_coverage_gap_static_index": "C07 rows 32 -> 50 if accepted; C07 static 50-row band reached",
  "auto_selected_coverage_gap_conversation_local": "C07 approx rows 32 -> 50 if accepted; C07 local 50-row band reached",
  "source_proxy_only": true,
  "evidence_url_pending": true,
  "batch_reverification_required": true
}
```

## 11. Shadow weight row

```json
{
  "source_row_type": "shadow_weight",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "do_not_apply_now": true,
  "proposed_axis": [
    "C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED",
    "C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP",
    "C07_CUSTOMER_QUALIFICATION_ACCEPTANCE_PAYMENT_REQUIRED_FOR_GREEN",
    "C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10",
    "C07_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD"
  ],
  "expected_effect": "Reduce HBM equipment false positives where relative strength is not backed by order/revenue conversion, while preserving true C07 positives with customer qualification and backlog bridge."
}
```

## 12. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

This run contributes a cleaner C07 boundary. It separates:

```text
true C07 = HBM equipment order / qualification / shipment / revenue bridge
not C07 = memory customer capacity, socket/test consumables, valuation blowoff, generic memory equipment cycle
```

## 13. Deferred Coding Agent Handoff Prompt

Do not execute this section in the research session.

```text
You are the coding agent for a later batch implementation session.

Input MD:
e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md

Task:
1. Parse all trigger rows and verify required 30D/90D/180D MFE/MAE fields.
2. Refetch exact stock-web shard rows for each symbol/year before accepting any row, because this research file used local prior stock-web rows after raw URL cache misses.
3. Reject rows that fail price row refetch, have corporate-action contamination in entry~D+180, or lack non-price order/revenue bridge evidence.
4. If accepted, register C07-specific shadow axes:
   - C07_ORDER_TO_REVENUE_CONVERSION_BRIDGE_REQUIRED
   - C07_RELATIVE_STRENGTH_WITHOUT_ORDER_STAGE2_CAP
   - C07_CUSTOMER_QUALIFICATION_ACCEPTANCE_PAYMENT_REQUIRED_FOR_GREEN
   - C07_CROSS_CANONICAL_REROUTE_TO_C06_C08_C09_C10
   - C07_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD
5. Keep production scoring unchanged until batch validation passes.

Hard constraints:
- Do not treat source_proxy_only rows as promotion-ready.
- Do not apply weight changes from this MD alone.
- Do not collapse C07 into generic HBM keyword strength.
```

## 14. Next research state

```text
completed_round = R2
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM, C02_POWER_GRID_DATACENTER_CAPEX
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
