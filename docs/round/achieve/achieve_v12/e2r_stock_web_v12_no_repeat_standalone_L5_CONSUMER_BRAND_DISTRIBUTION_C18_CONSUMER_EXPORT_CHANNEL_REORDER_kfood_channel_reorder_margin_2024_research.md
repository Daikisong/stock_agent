# E2R V12 No-Repeat Standalone Residual Research
## R5 / L5 / C18 — Consumer export channel-reorder / K-food margin guard

metadata:
```text
selected_round: R5
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_REVISION_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_kfood_channel_reorder_margin_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER current coverage:
rows=74, symbols=10, date range=2023-02-10~2024-12-16, good/bad S2=20/9, 4B/4C=4/5
top covered symbols: 003230(18), 005180(12), 004370(10), 383220(8), 161890(6)
```

This run avoids those top-covered C18 symbols and adds 097950, 271560, and 001680.  
Each row uses a new `C18 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
097950 CJ제일제당: corporate_action_candidate_count=0.
271560 오리온: corporate_action_candidate_count=0.
001680 대상: 2024 forward window clean; corporate-action candidates are old, outside the selected test window.
```

## 3. Research thesis

C18 should not treat every consumer export headline as a reorder cycle. It should test whether overseas attention becomes repeated channel pull:

```text
consumer export / K-food / global channel attention
→ sell-through and channel inventory quality
→ repeat order or reorder cadence
→ country mix and volume quality
→ margin and revision bridge
→ rerating
```

The first shipment is a photograph. The reorder is the film. C18 should pay for the film.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C18_097950_CJFOOD_20240416_KFOOD_EXPORT_CHANNEL_MARGIN_STAGE2 | 097950 | positive_kfood_export_channel_reorder_stage2_success_with_later_4b | 2024-04-16 | 332500 | 407500 on 2024-06-26 | 240500 on 2024-11-14 | 13.68% | 22.56% | 22.56% | -27.67% | -40.98% |
| C18_271560_ORION_20240617_GLOBAL_CHANNEL_REORDER_FALSE_GREEN | 271560 | channel_reorder_false_green_counterexample | 2024-06-17 | 104400 | 106700 on 2024-06-18 | 90100 on 2024-07-03 | 2.2% | 2.2% | 2.2% | -13.7% | -15.56% |
| C18_001680_DAESANG_20240612_SAUCE_EXPORT_REORDER_PRICE_PREMIUM_4B | 001680 | sauce_export_channel_reorder_price_premium_counterexample | 2024-06-12 | 28400 | 30900 on 2024-06-17 | 18730 on 2024-11-14 | 8.8% | 8.8% | 8.8% | -34.05% | -39.39% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- K-food export, global channel sell-through and margin-recovery attention can be valid Stage2 routes.
- 097950 is the positive anchor: the April 2024 move had enough export/channel and margin-recovery plausibility to produce a large MFE before the later drawdown demanded 4B discipline.

### Stage3 / Green
- C18 Green should require repeat orders, channel inventory quality, country mix, volume and margin/revision confirmation.
- 271560 is the false-Green guard. The June 2024 price confirmation looked like channel-reorder recovery, but the following path did not carry enough non-price evidence-weighted runway.

### 4B
- 001680 is the local 4B counterexample. The sauce/K-food export premium moved quickly, then failed when repeat-order and margin evidence did not keep expanding.
- C18 should treat export-channel price premium as a risk flag once sell-through and reorder cadence are not updated.

### 4C
- No hard accounting break is asserted.
- The C18 break mode is reorder failure: the product remains real, but channel inventory, repeat order, country mix, volume, and margin revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C18_001680_DAESANG_20240612_SAUCE_EXPORT_REORDER_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C18_097950_CJFOOD_20240416_KFOOD_EXPORT_CHANNEL_MARGIN_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 54,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  },
  "C18_271560_ORION_20240617_GLOBAL_CHANNEL_REORDER_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 3,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 30,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C18 guard:
```text
if consumer_export_attention and sell_through_margin_bridge_visible:
    allow_stage2_actionable = true

if export_channel_price_premium and no repeat_order_channel_inventory_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and reorder_or_country_mix_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 271560 / 2024-06-17: global snack/channel recovery can be over-promoted if the model treats price confirmation as repeat-order proof.
- 001680 / 2024-06-12: K-food sauce export price premium can become price-only when channel inventory, repeat order and margin revisions do not close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -27.67, "MAE_30D_pct": -3.16, "MAE_90D_pct": -4.66, "MFE_180D_pct": 22.56, "MFE_30D_pct": 13.68, "MFE_90D_pct": 22.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_097950_CJFOOD_20240416_KFOOD_EXPORT_CHANNEL_MARGIN_STAGE2", "case_role": "positive_kfood_export_channel_reorder_stage2_success_with_later_4b", "company_name": "CJ제일제당", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when K-food export/channel reorder and margin recovery could connect to revision leverage; Green still requires channel sell-through, reorder recurrence, input-cost/mix bridge and revision durability.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.98, "entry_date": "2024-04-16", "entry_price": 332500, "evidence_family": "kfood_export_channel_reorder_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-11-14", "low_price_180d": 240500, "peak_date": "2024-06-26", "peak_price": 407500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/097/097950.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 54, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C18_097950_CJFOOD_20240416_KFOOD_EXPORT_CHANNEL_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_or_global_channel_attention", "channel_sell_through_or_reorder_claim", "margin_mix_or_input_cost_recovery_signal"], "stage3_evidence_fields": ["repeat_order_and_channel_inventory_confirmation_required", "country_mix_or_sell_through_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_channel_reorder_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["channel_inventory_or_reorder_gap", "country_mix_or_volume_disappointment", "margin_revision_bridge_failure"], "symbol": "097950", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv", "trigger_date": "2024-04-16", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -13.7, "MAE_30D_pct": -13.7, "MAE_90D_pct": -13.7, "MFE_180D_pct": 2.2, "MFE_30D_pct": 2.2, "MFE_90D_pct": 2.2, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_271560_ORION_20240617_GLOBAL_CHANNEL_REORDER_FALSE_GREEN", "case_role": "channel_reorder_false_green_counterexample", "company_name": "오리온", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Global snack/channel reorder claims should stay Yellow if the stock has already priced recovery but sell-through, country mix, volume and margin/revision bridge are not improving.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -15.56, "entry_date": "2024-06-17", "entry_price": 104400, "evidence_family": "global_snack_channel_reorder_price_confirmation_without_volume_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-07-03", "low_price_180d": 90100, "peak_date": "2024-06-18", "peak_price": 106700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/271/271560.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 3, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 30, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C18_271560_ORION_20240617_GLOBAL_CHANNEL_REORDER_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_or_global_channel_attention", "channel_sell_through_or_reorder_claim", "margin_mix_or_input_cost_recovery_signal"], "stage3_evidence_fields": ["repeat_order_and_channel_inventory_confirmation_required", "country_mix_or_sell_through_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_channel_reorder_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["channel_inventory_or_reorder_gap", "country_mix_or_volume_disappointment", "margin_revision_bridge_failure"], "symbol": "271560", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv", "trigger_date": "2024-06-17", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -34.05, "MAE_30D_pct": -15.49, "MAE_90D_pct": -31.02, "MFE_180D_pct": 8.8, "MFE_30D_pct": 8.8, "MFE_90D_pct": 8.8, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_001680_DAESANG_20240612_SAUCE_EXPORT_REORDER_PRICE_PREMIUM_4B", "case_role": "sauce_export_channel_reorder_price_premium_counterexample", "company_name": "대상", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Sauce/K-food export price premium should route to local 4B or counterexample unless repeat orders, channel inventory, country mix and margin/revision evidence keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -39.39, "entry_date": "2024-06-12", "entry_price": 28400, "evidence_family": "sauce_kfood_export_channel_reorder_price_premium_without_repeat_order_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-11-14", "low_price_180d": 18730, "peak_date": "2024-06-17", "peak_price": 30900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001680.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C18_001680_DAESANG_20240612_SAUCE_EXPORT_REORDER_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_or_global_channel_attention", "channel_sell_through_or_reorder_claim", "margin_mix_or_input_cost_recovery_signal"], "stage3_evidence_fields": ["repeat_order_and_channel_inventory_confirmation_required", "country_mix_or_sell_through_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_channel_reorder_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["channel_inventory_or_reorder_gap", "country_mix_or_volume_disappointment", "margin_revision_bridge_failure"], "symbol": "001680", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv", "trigger_date": "2024-06-12", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "loop_contribution_label": "consumer_export_channel_reorder_kfood_margin_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R5",
  "shadow_rule_candidate": "C18 consumer export/channel reorder rows should allow Stage2 on early K-food export, channel sell-through and margin-recovery evidence, but Stage3 Green requires repeat orders, channel inventory quality, country mix, volume, margin and revision bridge; export-channel price premium without repeat-order proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C18 + symbol + trigger_type + entry_date.
3. Add C18-specific export/channel-reorder/sell-through/margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C18_STAGE2_ALLOWED_ON_EXPORT_SELLTHROUGH_MARGIN_RECOVERY
- C18_GREEN_REQUIRES_REPEAT_ORDER_CHANNEL_INVENTORY_COUNTRY_MIX_REVISION
- C18_EXPORT_CHANNEL_PRICE_PREMIUM_LOCAL_4B
- C18_KFOOD_REORDER_WITHOUT_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.

