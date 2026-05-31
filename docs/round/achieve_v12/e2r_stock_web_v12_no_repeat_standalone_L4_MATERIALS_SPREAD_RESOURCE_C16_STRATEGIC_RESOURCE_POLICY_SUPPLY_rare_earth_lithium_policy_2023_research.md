# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy supply conversion guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_EARTH_LITHIUM_POLICY_SUPPLY_CONVERSION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_rare_earth_lithium_policy_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY current coverage:
rows=7, symbols=4, date range=2019-05-20~2023-10-23, good/bad S2=2/0, 4B/4C=0/0
top covered symbols: 005290(2), 027580(2), 047400(2), 093370(1)
```

This run adds three new symbols not listed as top-covered C16 symbols: 009520, 075970, and 000910.

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

Selected shards:
```text
009520: atlas/ohlcv_tradable_by_symbol_year/009/009520/2023.csv
075970: atlas/ohlcv_tradable_by_symbol_year/075/075970/2023.csv
000910: atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv
```

## 3. Research thesis

C16 should separate strategic-resource policy optionality from actual supply conversion:

```text
policy/export-control/resource scarcity headline
→ resource-supply-chain attention
→ price rerating attempt
→ Green only if company-specific supply, offtake, capacity, margin, or revision bridge closes
```

The residual failure mode is policy beta being mistaken for structural resource supply. These cases show why C16 needs a conversion guard.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C16_009520_POSCO_MTECH_20230306_LITHIUM_RESOURCE_AFFILIATE_RERATING_4B | 009520 | 4B_overlay_success | 2023-03-06 | 11550 | 39600 on 2023-04-18 | 10540 on 2023-03-14 | 242.86% | -8.74% | -51.01% |
| C16_075970_DONGKUKRNS_20230704_RARE_EARTH_EXPORT_CONTROL_FALSE_GREEN | 075970 | failed_rerating | 2023-07-04 | 4930 | 6350 on 2023-07-07 | 3025 on 2023-10-31 | 28.8% | -38.64% | -52.36% |
| C16_000910_UNION_20230425_RARE_EARTH_POLICY_PRICE_ONLY_4B | 000910 | price_moved_without_evidence | 2023-04-25 | 9800 | 12040 on 2023-05-03 | 6120 on 2023-06-29 | 22.86% | -37.55% | -49.17% |

## 5. Stage evidence split

### Stage2 / Stage2-Watch
- Strategic-resource policy events and export-control headlines can create valid Stage2 attention.
- Relative strength confirms that the market noticed the resource theme.

### Stage3 / Green
- C16 Green should require company-specific evidence: resource supply contract, offtake, capacity route, processing margin, or confirmed revision.
- Policy headlines alone do not create durable EPS/FCF bodyweight change.

### 4B
- 009520 and 000910 both show large policy/resource beta moves that later required 4B discipline.
- 075970 shows a smaller but cleaner false-Green path: quick rare-earth/export-control rally, then deep fade.

### 4C
- These are not hard accounting-break cases.
- The 4C-like failure is a thesis conversion failure: no evidence that policy scarcity translated into durable company-level earnings.

## 6. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_policy_event and no company_specific_supply_or_margin_bridge:
    cap_stage = Stage2-Watch or Stage3-Yellow
    block_stage3_green = true
    allow_local_4b_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 075970: export-control / rare-earth theme can be over-promoted without company-specific supply economics.
- 000910: price-only rare-earth rally should be a local 4B/counterexample row, not positive Stage2/Green.
```

## 7. Machine-readable rows

```jsonl
{"MAE_180D_pct": -8.74, "MAE_30D_pct": -8.74, "MAE_90D_pct": -8.74, "MFE_180D_pct": 242.86, "MFE_30D_pct": 242.86, "MFE_90D_pct": 242.86, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_009520_POSCO_MTECH_20230306_LITHIUM_RESOURCE_AFFILIATE_RERATING_4B", "case_role": "4B_overlay_success", "company_name": "포스코엠텍", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2/Yellow early signal worked, but full Green needs project-specific offtake or earnings bridge; full 4B after blowoff requires non-price evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.01, "entry_date": "2023-03-06", "entry_price": 11550, "evidence_family": "lithium_resource_affiliate_policy_supply_chain_rerating", "evidence_url_pending": false, "fine_archetype_id": "RARE_EARTH_LITHIUM_POLICY_SUPPLY_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-03-14", "low_price_180d": 10540, "peak_date": "2023-04-18", "peak_price": 39600, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009520.json", "reuse_reason": null, "same_entry_group_id": "C16_009520_POSCO_MTECH_20230306_LITHIUM_RESOURCE_AFFILIATE_RERATING_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_event", "relative_strength", "resource_supply_chain_optionality"], "stage3_evidence_fields": ["company_specific_supply_contract_required", "offtake_or_capacity_route_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["valuation_or_theme_blowoff", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_theme_without_conversion", "no_company_specific_earnings_bridge", "resource_theme_fade"], "symbol": "009520", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009520/2023.csv", "trigger_date": "2023-03-06", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.64, "MAE_30D_pct": -4.36, "MAE_90D_pct": -38.64, "MFE_180D_pct": 28.8, "MFE_30D_pct": 28.8, "MFE_90D_pct": 28.8, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_075970_DONGKUKRNS_20230704_RARE_EARTH_EXPORT_CONTROL_FALSE_GREEN", "case_role": "failed_rerating", "company_name": "동국알앤에스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Policy/export-control beta should remain Stage2-Watch or local 4B, not Green, without company-specific supply or earnings bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.36, "entry_date": "2023-07-04", "entry_price": 4930, "evidence_family": "rare_earth_export_control_theme_without_supply_contract_or_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "RARE_EARTH_LITHIUM_POLICY_SUPPLY_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-31", "low_price_180d": 3025, "peak_date": "2023-07-07", "peak_price": 6350, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/075/075970.json", "reuse_reason": null, "same_entry_group_id": "C16_075970_DONGKUKRNS_20230704_RARE_EARTH_EXPORT_CONTROL_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_event", "relative_strength", "resource_supply_chain_optionality"], "stage3_evidence_fields": ["company_specific_supply_contract_required", "offtake_or_capacity_route_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["valuation_or_theme_blowoff", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_theme_without_conversion", "no_company_specific_earnings_bridge", "resource_theme_fade"], "symbol": "075970", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075970/2023.csv", "trigger_date": "2023-07-04", "trigger_type": "Stage2-Watch", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -37.55, "MAE_30D_pct": -37.55, "MAE_90D_pct": -37.55, "MFE_180D_pct": 22.86, "MFE_30D_pct": 22.86, "MFE_90D_pct": 22.86, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_000910_UNION_20230425_RARE_EARTH_POLICY_PRICE_ONLY_4B", "case_role": "price_moved_without_evidence", "company_name": "유니온", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Price-only strategic-resource theme should not be promoted as Stage2/Green positive evidence; it is a local 4B/counterexample row.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.17, "entry_date": "2023-04-25", "entry_price": 9800, "evidence_family": "rare_earth_policy_theme_price_only_without_conversion", "evidence_url_pending": false, "fine_archetype_id": "RARE_EARTH_LITHIUM_POLICY_SUPPLY_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-06-29", "low_price_180d": 6120, "peak_date": "2023-05-03", "peak_price": 12040, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000910.json", "reuse_reason": null, "same_entry_group_id": "C16_000910_UNION_20230425_RARE_EARTH_POLICY_PRICE_ONLY_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_event", "relative_strength", "resource_supply_chain_optionality"], "stage3_evidence_fields": ["company_specific_supply_contract_required", "offtake_or_capacity_route_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["valuation_or_theme_blowoff", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_theme_without_conversion", "no_company_specific_earnings_bridge", "resource_theme_fade"], "symbol": "000910", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv", "trigger_date": "2023-04-25", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 8. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "RARE_EARTH_LITHIUM_POLICY_SUPPLY_CONVERSION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource policy/export-control themes should be capped at Stage2-Watch/Yellow unless company-specific supply contract, offtake, capacity, margin, or revision evidence closes.",
  "source_proxy_only_count": 0
}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C16 + symbol + trigger_type + entry_date.
3. Add C16-specific conversion guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_STRATEGIC_RESOURCE_POLICY_REQUIRES_COMPANY_SPECIFIC_CONVERSION
- C16_EXPORT_CONTROL_THEME_STAGE2_CAP
- C16_PRICE_ONLY_RESOURCE_THEME_LOCAL_4B_ONLY

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 10. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

