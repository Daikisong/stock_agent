# stock-web v12 residual research — R5 loop 109 — C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
live_candidate_mode = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection

```text
selected_round = R5
selected_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_ECOMMERCE_GLOBAL_DISTRIBUTION_ODM_MARGIN_BRIDGE_VS_BRAND_CHANNEL_EXPANSION_HIGH_MAE_FADE
```

C20 is a Priority 1 residual bucket. The no-repeat index records 33 rows and 17 rows needed to reach the 50-row practical calibration target. This run avoids the prior C20 case set using Silicon2 / Cosmax / AmorePacific and avoids the immediately prior C18 food-channel set using Binggrae / Lotte Wellfood / Pulmuone.

## 2. Price atlas basis

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Corporate-action contaminated windows are blocked by default. All three usable cases below use 2024 windows with no corporate-action candidate inside the trigger window for the selected symbol profiles.

## 3. External evidence spine

The external category spine is the 2024-2025 K-beauty global distribution cycle: Korean cosmetics exports and U.S. ecommerce/retail penetration accelerated, but the evidence also warns that online virality and channel expansion are not enough; durable performance needs physical-store sell-through, margin resilience, and continued demand. This run treats broad K-beauty distribution as a sector trigger and then tests whether each symbol has a company-specific price path consistent with Stage2-Actionable, Stage3, 4B, or 4C.

## 4. Cases

### Case 1 — VT / 브이티 / 018290 — positive with full 4B watch

```text
case_id = C20_VT_018290_2024_05_10_KBEAUTY_US_ECOMMERCE_BRAND_RETAIL_POSITIVE
trigger_date = 2024-05-10
entry_date = 2024-05-10
entry_price = 25,400
local_peak_date = 2024-06-19
local_peak_price = 40,000
local_mfe_pct = 57.48
full_peak_date = 2024-12-16
full_peak_price = 44,000
full_mfe_pct = 73.23
trough_date = 2024-05-13
trough_price = 23,400
mae_pct = -7.87
classification = positive_with_full_4b_watch
```

VT is useful because it separates a broad K-beauty keyword from an actual brand/product cycle. The price path confirms that the May 2024 K-beauty distribution/revision impulse could create durable MFE. But because the later full-window peak is far from the initial trigger and the stock becomes theme-sensitive, the rule should not blindly convert this into Green. It is better classified as Stage2-Actionable / Stage3-Yellow candidate with 4B watch unless sell-through and margin bridge are verified.

### Case 2 — Kolmar Korea / 한국콜마 / 161890 — ODM bridge positive, high-MAE watch

```text
case_id = C20_KOLMAR_161890_2024_05_10_KBEAUTY_ODM_MARGIN_REVISION_POSITIVE
trigger_date = 2024-05-10
entry_date = 2024-05-10
entry_price = 55,200
peak_date = 2024-09-30
peak_price = 78,700
mfe_pct = 42.57
trough_date = 2024-12-09
trough_price = 49,550
mae_pct = -10.24
classification = positive_high_mae_watch
```

Kolmar is the cleaner C20 bridge case because the K-beauty cycle is not just a consumer-brand label; ODM/contract manufacturing can translate broad industry demand into customer orders, utilization, and operating leverage. The path supports a positive classification, but the later drawdown still argues for a bridge requirement: without order/revision/OPM evidence, the model should keep this below automatic Green.

### Case 3 — Clio / 클리오 / 237880 — high-MFE / high-MAE counterexample

```text
case_id = C20_CLIO_237880_2024_05_10_BRAND_CHANNEL_EXPANSION_HIGH_MAE_COUNTEREXAMPLE
trigger_date = 2024-05-10
entry_date = 2024-05-10
entry_price = 34,850
peak_date = 2024-06-13
peak_price = 45,000
mfe_pct = 29.12
trough_date = 2024-12-09
trough_price = 15,790
mae_pct = -54.69
classification = high_mfe_high_mae_counterexample
```

Clio is the main residual-error case. It had enough early MFE to fool a price-and-theme model, but the full window becomes a severe drawdown. This is exactly why C20 needs a sell-through / reorder / OPM / channel-inventory bridge rather than a simple K-beauty or global-channel keyword. It should be treated as Stage2-Actionable only if non-price evidence confirms durable channel sell-through; otherwise it belongs in 4B watch or 4C if the fade is already visible.

## 5. Calibration interpretation

```text
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
verified_url_repair_needed_count = 2
```

The mechanism is simple: C20 should behave like a pipe, not a poster. A poster is the visible K-beauty story: viral product, Amazon ranking, retailer talks, global distribution headlines. A pipe is the hidden conversion path: reorder frequency, channel inventory, ASP/mix, OPM, and estimate revision. The residual errors appear when the profile sees the poster and assumes the pipe is already flowing.

## 6. Shadow rule candidate

```text
new_axis_proposed = c20_sellthrough_opm_revision_bridge_required_for_stage2_actionable_shadow_only
rule_scope = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
production_scoring_changed = false
shadow_weight_only = true
```

Rule candidate:

> For C20, global distribution / K-beauty / viral channel evidence cannot by itself qualify for Stage2-Actionable or Stage3. Require at least one of: repeat sell-through evidence, reorder/channel inventory normalization, OPM or gross-margin expansion, confirmed customer/order expansion, or estimate revision. If absent, cap at Stage2 watch or 4B price-only watch even when early MFE is strong.

Expected effect:

```text
- reduce false positives in brand-channel expansion spikes
- preserve positives where ODM/utilization/order/revision bridge exists
- classify high-MFE/high-MAE paths as 4B watch instead of Green
```

## 7. Machine-readable rows

### trigger_rows_representative.jsonl

```jsonl
{"schema": "e2r_v12_trigger_row", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_US_ECOMMERCE_GLOBAL_DISTRIBUTION_ODM_MARGIN_BRIDGE_VS_BRAND_CHANNEL_EXPANSION_HIGH_MAE_FADE", "case_id": "C20_VT_018290_2024_05_10_KBEAUTY_US_ECOMMERCE_BRAND_RETAIL_POSITIVE", "symbol": "018290", "name": "브이티", "trigger_type": "k_beauty_global_distribution_sellthrough_revision_bridge", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 25400, "peak_date": "2024-12-16", "peak_price": 44000, "mfe_pct": 73.23, "trough_date": "2024-05-13", "trough_price": 23400, "mae_pct": -7.87, "case_role": "positive", "classification": "positive_with_full_4b_watch", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "source_quality": "price_verified_broad_category_source_verified_company_specific_url_repair_needed_for_brands", "calibration_usable": true}
{"schema": "e2r_v12_trigger_row", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_US_ECOMMERCE_GLOBAL_DISTRIBUTION_ODM_MARGIN_BRIDGE_VS_BRAND_CHANNEL_EXPANSION_HIGH_MAE_FADE", "case_id": "C20_KOLMAR_161890_2024_05_10_KBEAUTY_ODM_MARGIN_REVISION_POSITIVE", "symbol": "161890", "name": "한국콜마", "trigger_type": "k_beauty_global_distribution_sellthrough_revision_bridge", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 55200, "peak_date": "2024-09-30", "peak_price": 78700, "mfe_pct": 42.57, "trough_date": "2024-12-09", "trough_price": 49550, "mae_pct": -10.24, "case_role": "positive", "classification": "positive_high_mae_watch", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "source_quality": "price_verified_broad_category_source_verified_company_specific_url_repair_needed_for_brands", "calibration_usable": true}
{"schema": "e2r_v12_trigger_row", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_US_ECOMMERCE_GLOBAL_DISTRIBUTION_ODM_MARGIN_BRIDGE_VS_BRAND_CHANNEL_EXPANSION_HIGH_MAE_FADE", "case_id": "C20_CLIO_237880_2024_05_10_BRAND_CHANNEL_EXPANSION_HIGH_MAE_COUNTEREXAMPLE", "symbol": "237880", "name": "클리오", "trigger_type": "k_beauty_global_distribution_sellthrough_revision_bridge", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 34850, "peak_date": "2024-06-13", "peak_price": 45000, "mfe_pct": 29.12, "trough_date": "2024-12-09", "trough_price": 15790, "mae_pct": -54.69, "case_role": "counterexample", "classification": "high_mfe_high_mae_counterexample", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "source_quality": "price_verified_broad_category_source_verified_company_specific_url_repair_needed_for_brands", "calibration_usable": true}
```

### score_simulation.jsonl

```jsonl
{"schema": "e2r_v12_score_simulation", "axis": "c20_sellthrough_opm_revision_bridge_required_for_stage2_actionable_shadow_only", "current_profile_failure": "global_distribution_or_kbeauty_keyword_overcredits_brand_channel_labels", "shadow_rule_effect": "requires sell-through/order/revision/OPM bridge before Stage2-Actionable or Stage3; routes broad channel/viral labels to 4B watch", "expected_false_positive_reduction": "medium_high", "production_scoring_changed": false}
```

### aggregate.json

```json
{
  "schema": "e2r_v12_aggregate",
  "selected_round": "R5",
  "selected_loop": 109,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
  "fine_archetype_id": "K_BEAUTY_US_ECOMMERCE_GLOBAL_DISTRIBUTION_ODM_MARGIN_BRIDGE_VS_BRAND_CHANNEL_EXPANSION_HIGH_MAE_FADE",
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 3,
  "verified_url_repair_needed_count": 2,
  "new_axis_proposed": "c20_sellthrough_opm_revision_bridge_required_for_stage2_actionable_shadow_only",
  "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to C20 K-beauty/global-distribution/brand-channel rallies"
}
```

## 8. Residual contribution

```text
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C20 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C20 K-beauty/global-distribution/brand-channel rallies
existing_axis_weakened = null
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.

When batch-applying v12 residual research MDs to stock_agent:
1. Read this file as a research artifact only.
2. Do not treat the proposed axis as production scoring until a maintainer explicitly approves.
3. Add the trigger rows to the calibration registry if they pass duplicate checks:
   - canonical_archetype_id + symbol + trigger_type + entry_date
4. Keep the new axis as shadow-only:
   c20_sellthrough_opm_revision_bridge_required_for_stage2_actionable_shadow_only
5. Use this run to strengthen C20-specific handling:
   - K-beauty/global-distribution keyword alone is not enough.
   - Require sell-through, reorder, channel-inventory, OPM, or revision evidence.
   - High-MFE/high-MAE brand-channel paths should become 4B watch or 4C, not Green.
6. Do not change production scoring from this single MD alone.
```

## 10. Final status

```text
selected_round = R5
selected_loop = 109
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
new_independent_case_count = 3
reused_case_count = 0
positive_case_count = 2
counterexample_count = 1
next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C22_INSURANCE_RATE_CYCLE_RESERVE
```
