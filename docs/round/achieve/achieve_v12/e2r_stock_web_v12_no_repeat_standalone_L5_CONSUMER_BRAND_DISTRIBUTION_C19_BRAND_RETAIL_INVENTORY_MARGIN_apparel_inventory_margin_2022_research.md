# E2R V12 No-Repeat Standalone Residual Research
## R5 / L5 / C19 — Apparel brand-retail inventory margin guard

metadata:
```text
selected_round: R5
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_apparel_inventory_margin_2022_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C19_BRAND_RETAIL_INVENTORY_MARGIN current coverage:
rows=39, symbols=8, date range=2022-05-16~2024-10-02, good/bad S2=8/8, 4B/4C=7/4
top covered symbols: UNKNOWN_SYMBOL(8), 036620(6), 298540(6), 383220(6), 337930(5)
```

This run avoids those top-covered C19 symbols and adds 020000, 111770, and 093050.  
Each row uses a new `C19 + symbol + trigger_type + entry_date` hard key.

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
020000 한섬: 2022 forward window clean; corporate-action candidates are old, outside the test window.
111770 영원무역: corporate_action_candidate_count=0.
093050 LF: corporate_action_candidate_count=0.
```

## 3. Research thesis

C19 should not treat every reopening or brand-retail bounce as durable rerating. The mechanism must close:

```text
brand / retail / apparel demand attention
→ sell-through and channel quality
→ inventory normalization
→ gross-margin or OEM-margin bridge
→ revision confirmation
→ rerating
```

The apparel basket shows why the gate matters. A store can look crowded at the entrance, but if inventory piles up in the back room, the margin bridge collapses.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C19_020000_HANSAEM_20220516_APPAREL_REOPENING_INVENTORY_FALSE_GREEN | 020000 | false_green_counterexample | 2022-05-16 | 37900 | 39550 on 2022-06-03 | 25400 on 2022-11-28 | 4.35% | 4.35% | 4.35% | -32.98% | -35.78% |
| C19_111770_YOUNGONE_20220630_APPAREL_OEM_MARGIN_STAGE2_RECOVERY | 111770 | positive_margin_recovery_stage2 | 2022-06-30 | 38400 | 50200 on 2022-11-22 | 36650 on 2022-07-15 | 7.94% | 30.73% | 30.73% | -4.56% | -11.75% |
| C19_093050_LF_20220516_APPAREL_CHANNEL_REOPENING_MARGIN_FADE | 093050 | inventory_margin_fade_counterexample | 2022-05-16 | 19050 | 20350 on 2022-05-18 | 14900 on 2022-07-12 | 6.82% | 6.82% | 6.82% | -21.78% | -26.78% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Reopening demand, apparel OEM margin, and brand-retail valuation recovery can create valid Stage2 attention.
- 111770 is the positive anchor because a later recovery path existed when margin and export/OEM quality were less fragile.

### Stage3 / Green
- C19 Green should require inventory normalization, sell-through, and margin/revision bridge.
- 020000 and 093050 show why short post-reopening strength should stay Yellow without those bridges.

### 4B
- Retail reopening strength can become a local 4B if price runs ahead of inventory and sell-through proof.
- 111770 also needs later 4B discipline after the recovery validates.

### 4C
- The failure mode is not a sudden accounting break.
- It is inventory and margin fade: the store-front story survives, but the balance of stock, discounting, and revision quality weakens.

## 6. Raw component score breakdown

```json
{
  "C19_020000_HANSAEM_20220516_APPAREL_REOPENING_INVENTORY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 32,
    "valuation_rerating_runway": 5,
    "visibility_quality": 6
  },
  "C19_093050_LF_20220516_APPAREL_CHANNEL_REOPENING_MARGIN_FADE": {
    "bottleneck_pricing_power": 4,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 30,
    "valuation_rerating_runway": 5,
    "visibility_quality": 5
  },
  "C19_111770_YOUNGONE_20220630_APPAREL_OEM_MARGIN_STAGE2_RECOVERY": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 54,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C19 guard:
```text
if brand_retail_reopening_attention and no inventory_normalization_or_sell_through_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if price_strength but inventory_or_margin_evidence_fades:
    route_to_counterexample_or_local_4B_watch = true

if margin_revision_break_after_reopening:
    route_to_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 020000 / 2022-05-16: post-reopening apparel strength could be over-promoted if inventory and sell-through gates are not required.
- 093050 / 2022-05-16: short price confirmation was followed by deep drawdown, showing false-Green risk.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -32.98, "MAE_30D_pct": -19.13, "MAE_90D_pct": -25.73, "MFE_180D_pct": 4.35, "MFE_30D_pct": 4.35, "MFE_90D_pct": 4.35, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_020000_HANSAEM_20220516_APPAREL_REOPENING_INVENTORY_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "한섬", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Reopening/brand-retail price strength should not become Green unless sell-through, inventory normalization, and margin/revision bridge close.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -35.78, "entry_date": "2022-05-16", "entry_price": 37900, "evidence_family": "apparel_reopening_inventory_margin_false_green", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2022-11-28", "low_price_180d": 25400, "peak_date": "2022-06-03", "peak_price": 39550, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020000.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 6, "total": 32, "valuation_rerating_runway": 5, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C19_020000_HANSAEM_20220516_APPAREL_REOPENING_INVENTORY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_retail_or_apparel_reopening_attention", "sell_through_or_oem_margin_claim", "relative_strength_or_valuation_recovery"], "stage3_evidence_fields": ["inventory_normalization_required", "channel_sell_through_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["retail_reopening_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["inventory_overhang", "sell_through_fade", "margin_or_revision_break"], "symbol": "020000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020000/2022.csv", "trigger_date": "2022-05-16", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -4.56, "MAE_30D_pct": -4.56, "MAE_90D_pct": -4.56, "MFE_180D_pct": 30.73, "MFE_30D_pct": 7.94, "MFE_90D_pct": 30.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_111770_YOUNGONE_20220630_APPAREL_OEM_MARGIN_STAGE2_RECOVERY", "case_role": "positive_margin_recovery_stage2", "company_name": "영원무역", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 can be valid when apparel OEM/export margin recovers, but Green still requires sell-through, inventory quality, and revision durability.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -11.75, "entry_date": "2022-06-30", "entry_price": 38400, "evidence_family": "apparel_oem_export_margin_inventory_recovery", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2022-07-15", "low_price_180d": 36650, "peak_date": "2022-11-22", "peak_price": 50200, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/111/111770.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 54, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C19_111770_YOUNGONE_20220630_APPAREL_OEM_MARGIN_STAGE2_RECOVERY", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_retail_or_apparel_reopening_attention", "sell_through_or_oem_margin_claim", "relative_strength_or_valuation_recovery"], "stage3_evidence_fields": ["inventory_normalization_required", "channel_sell_through_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["retail_reopening_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["inventory_overhang", "sell_through_fade", "margin_or_revision_break"], "symbol": "111770", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/111/111770/2022.csv", "trigger_date": "2022-06-30", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -21.78, "MAE_30D_pct": -21.52, "MAE_90D_pct": -21.78, "MFE_180D_pct": 6.82, "MFE_30D_pct": 6.82, "MFE_90D_pct": 6.82, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_093050_LF_20220516_APPAREL_CHANNEL_REOPENING_MARGIN_FADE", "case_role": "inventory_margin_fade_counterexample", "company_name": "LF", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Retail-channel reopening without inventory and margin proof should stay Yellow; price confirmation alone becomes a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -26.78, "entry_date": "2022-05-16", "entry_price": 19050, "evidence_family": "brand_retail_reopening_without_inventory_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2022-07-12", "low_price_180d": 14900, "peak_date": "2022-05-18", "peak_price": 20350, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/093/093050.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 6, "total": 30, "valuation_rerating_runway": 5, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C19_093050_LF_20220516_APPAREL_CHANNEL_REOPENING_MARGIN_FADE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_retail_or_apparel_reopening_attention", "sell_through_or_oem_margin_claim", "relative_strength_or_valuation_recovery"], "stage3_evidence_fields": ["inventory_normalization_required", "channel_sell_through_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["retail_reopening_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["inventory_overhang", "sell_through_fade", "margin_or_revision_break"], "symbol": "093050", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/093/093050/2022.csv", "trigger_date": "2022-05-16", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "APPAREL_BRAND_RETAIL_INVENTORY_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "loop_contribution_label": "brand_retail_inventory_margin_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R5",
  "shadow_rule_candidate": "C19 brand-retail/apparel rerating should cap at Stage2/Yellow unless inventory normalization, sell-through, margin and revision bridge are confirmed; reopening price strength without inventory proof should route to counterexample or local 4B watch.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C19 + symbol + trigger_type + entry_date.
3. Add C19-specific inventory/sell-through/margin bridge logic only as a shadow candidate until more rows exist.

Candidate rule:
- C19_GREEN_REQUIRES_INVENTORY_SELLTHROUGH_MARGIN_REVISION
- C19_REOPENING_PRICE_STRENGTH_STAGE2_CAP
- C19_INVENTORY_MARGIN_FADE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.

