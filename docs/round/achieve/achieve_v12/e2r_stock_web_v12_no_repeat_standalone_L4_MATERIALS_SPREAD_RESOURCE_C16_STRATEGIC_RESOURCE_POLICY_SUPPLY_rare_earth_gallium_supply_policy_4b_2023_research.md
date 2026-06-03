# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy supply / rare-earth·gallium 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_EARTH_GALLIUM_SUPPLY_POLICY_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|policy_to_company_resource_exposure_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_rare_earth_gallium_supply_policy_4b_2023_research.md
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

This run avoids those top-covered C16 symbols and adds 000910, 075970, and 081150.  
Each row uses a new `C16 + symbol + trigger_type + entry_date` hard key:
```text
C16 + 000910 + Stage2-Actionable + 2023-03-27
C16 + 075970 + 4B-local-price-only + 2023-05-03
C16 + 081150 + Stage3-Yellow + 2023-08-21
```

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
active_like_symbol_count: 2868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
000910 유니온: selected post-2008 forward window clean; corporate-action candidates are 1997-01-03 and 2008-05-07, outside selected trigger window.
075970 동국알앤에스: selected post-2008 forward window clean; corporate-action candidates are historical/latest 2008-06-10, outside selected trigger window.
081150 티플랙스: selected post-2012 forward window clean; corporate-action candidates are 2012-10-04 and 2012-10-25, outside selected trigger window.
```

## 3. Research thesis

C16 should separate strategic-resource policy discovery from strategic-resource theme beta already paid in price:

```text
rare-earth / rare-metal / gallium policy salience
→ resource specificity
→ direct company exposure
→ customer/offtake or substitution bridge
→ policy durability
→ volume, margin and revision confirmation
→ Stage2/Green or local 4B cap
```

A resource policy shock is a locked gate in the supply chain. Stage2 can buy the first key when the company actually owns a useful door. Green should not pay for every company standing near the gate after the crowd has already bid up the theme.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C16_000910_UNION_20230327_RARE_EARTH_SUPPLY_POLICY_STAGE2 | 000910 | positive_rare_earth_supply_policy_stage2_success_with_later_4b_refresh | 2023-03-27 | 6060 | 12040 on 2023-05-03 | 4735 on 2023-10-31 | 98.68% | 98.68% | 98.68% | -21.86% | -60.67% |
| C16_075970_DONGKUKRNS_20230503_RARE_EARTH_POLICY_PREMIUM_4B | 075970 | rare_earth_policy_price_premium_counterexample | 2023-05-03 | 6460 | 6870 on 2023-05-03 | 3025 on 2023-10-31 | 6.35% | 6.35% | 6.35% | -53.17% | -55.97% |
| C16_081150_TFLEX_20230821_RARE_METAL_GALLIUM_POLICY_FALSE_GREEN | 081150 | rare_metal_gallium_policy_false_green_counterexample | 2023-08-21 | 5390 | 5790 on 2023-08-21 | 3170 on 2023-10-31 | 7.42% | 7.42% | 7.42% | -41.19% | -45.25% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 000910 is the positive anchor. Rare-earth/supply-chain policy pressure produced a strong 30D/90D/180D MFE before the later premium required 4B refresh discipline.
- Stage2 is allowed only when policy salience maps to resource specificity, direct company exposure, customer/offtake or substitution route, policy durability and margin/revision visibility.

### Stage3 / Green
- C16 Green should require direct company exposure, policy durability, product/resource specificity, customer/offtake or substitution conversion, and margin/revision confirmation.
- 081150 is the false-Green/Yellow guard: rare-metal/gallium policy price confirmation was visible, but the stock lacked enough direct exposure-to-margin evidence and the forward drawdown overwhelmed residual upside.

### 4B
- 075970 fills the rare-earth policy price-premium 4B pocket. The May 2023 trigger had almost no residual runway and a large forward drawdown.
- 081150 shows the same failure in rare-metal/gallium form: policy beta can remain real while the company-level earnings bridge is too weak for Green.
- 000910 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the strategic-resource option.

### 4C
- No hard license loss, resource supply cancellation, customer loss, or accounting break is asserted.
- The C16 break mode here is policy-to-company bridge exhaustion: the policy may remain directionally real, but incremental direct exposure, offtake, volume and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C16_000910_UNION_20230327_RARE_EARTH_SUPPLY_POLICY_STAGE2": {
    "customer_offtake_or_substitution_bridge": 5,
    "direct_company_exposure": 6,
    "information_confidence": 4,
    "margin_revision_bridge": 4,
    "market_mispricing": 9,
    "policy_durability": 7,
    "resource_specificity": 8,
    "strategic_resource_policy_salience": 10,
    "total": 61,
    "valuation_rerating_runway": 8
  },
  "C16_075970_DONGKUKRNS_20230503_RARE_EARTH_POLICY_PREMIUM_4B": {
    "customer_offtake_or_substitution_bridge": 2,
    "direct_company_exposure": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 4,
    "policy_durability": 6,
    "resource_specificity": 5,
    "strategic_resource_policy_salience": 9,
    "total": 34,
    "valuation_rerating_runway": 1
  },
  "C16_081150_TFLEX_20230821_RARE_METAL_GALLIUM_POLICY_FALSE_GREEN": {
    "customer_offtake_or_substitution_bridge": 2,
    "direct_company_exposure": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 4,
    "policy_durability": 5,
    "resource_specificity": 5,
    "strategic_resource_policy_salience": 8,
    "total": 32,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_policy and direct_exposure_resource_specificity_offtake_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if rare_earth_or_gallium_policy_price_premium and no incremental_direct_exposure_offtake_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and policy_to_company_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 075970 / 2023-05-03: rare-earth policy premium can be over-promoted if price strength substitutes for direct exposure, offtake and margin proof.
- 081150 / 2023-08-21: rare-metal/gallium policy confirmation can look like Yellow-to-Green, but fails without renewed direct exposure and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -21.86, "MAE_30D_pct": -8.91, "MAE_90D_pct": -10.73, "MFE_180D_pct": 98.68, "MFE_30D_pct": 98.68, "MFE_90D_pct": 98.68, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_000910_UNION_20230327_RARE_EARTH_SUPPLY_POLICY_STAGE2", "case_role": "positive_rare_earth_supply_policy_stage2_success_with_later_4b_refresh", "company_name": "유니온", "corporate_action_window_status": "selected post-2008 forward window clean; corporate-action candidates are 1997-01-03 and 2008-05-07, outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when strategic-resource policy salience, rare-earth substitution optionality and supply-chain localization pressure were visible before the rerating was fully capitalized. Green still requires direct company exposure, resource/product specificity, customer or offtake path, policy durability and margin/revision bridge; after the May 2023 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.67, "entry_date": "2023-03-27", "entry_price": 6060, "evidence_family": "rare_earth_supply_chain_policy_export_control_substitution_optional_value_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "RARE_EARTH_GALLIUM_SUPPLY_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-31", "low_price_180d": 4735, "peak_date": "2023-05-03", "peak_price": 12040, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000910.json", "raw_component_score_breakdown": {"customer_offtake_or_substitution_bridge": 5, "direct_company_exposure": 6, "information_confidence": 4, "margin_revision_bridge": 4, "market_mispricing": 9, "policy_durability": 7, "resource_specificity": 8, "strategic_resource_policy_salience": 10, "total": 61, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C16_000910_UNION_20230327_RARE_EARTH_SUPPLY_POLICY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_salience", "resource_specificity_and_direct_company_exposure", "customer_offtake_policy_durability_margin_revision_route"], "stage3_evidence_fields": ["direct_company_resource_exposure_required", "customer_offtake_or_substitution_conversion_required", "margin_revision_and_policy_durability_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_exposure_gap", "resource_supply_theme_not_converted_to_volume_or_offtake", "margin_revision_bridge_failure"], "symbol": "000910", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv", "trigger_date": "2023-03-27", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -53.17, "MAE_30D_pct": -31.89, "MAE_90D_pct": -44.2, "MFE_180D_pct": 6.35, "MFE_30D_pct": 6.35, "MFE_90D_pct": 6.35, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_075970_DONGKUKRNS_20230503_RARE_EARTH_POLICY_PREMIUM_4B", "case_role": "rare_earth_policy_price_premium_counterexample", "company_name": "동국알앤에스", "corporate_action_window_status": "selected post-2008 forward window clean; corporate-action candidates are historical/latest 2008-06-10, outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Rare-earth policy premium should route to local 4B or counterexample when the market has already capitalized supply-chain optionality and incremental direct exposure, customer/offtake conversion, resource specificity and margin/revision evidence do not keep expanding. The May 2023 trigger had almost no residual runway and a large forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.97, "entry_date": "2023-05-03", "entry_price": 6460, "evidence_family": "rare_earth_policy_supply_theme_price_premium_without_direct_offtake_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "RARE_EARTH_GALLIUM_SUPPLY_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-31", "low_price_180d": 3025, "peak_date": "2023-05-03", "peak_price": 6870, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/075/075970.json", "raw_component_score_breakdown": {"customer_offtake_or_substitution_bridge": 2, "direct_company_exposure": 3, "information_confidence": 3, "margin_revision_bridge": 1, "market_mispricing": 4, "policy_durability": 6, "resource_specificity": 5, "strategic_resource_policy_salience": 9, "total": 34, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_075970_DONGKUKRNS_20230503_RARE_EARTH_POLICY_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_salience", "resource_specificity_and_direct_company_exposure", "customer_offtake_policy_durability_margin_revision_route"], "stage3_evidence_fields": ["direct_company_resource_exposure_required", "customer_offtake_or_substitution_conversion_required", "margin_revision_and_policy_durability_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_exposure_gap", "resource_supply_theme_not_converted_to_volume_or_offtake", "margin_revision_bridge_failure"], "symbol": "075970", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075970/2023.csv", "trigger_date": "2023-05-03", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.19, "MAE_30D_pct": -31.91, "MAE_90D_pct": -41.19, "MFE_180D_pct": 7.42, "MFE_30D_pct": 7.42, "MFE_90D_pct": 7.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_081150_TFLEX_20230821_RARE_METAL_GALLIUM_POLICY_FALSE_GREEN", "case_role": "rare_metal_gallium_policy_false_green_counterexample", "company_name": "티플랙스", "corporate_action_window_status": "selected post-2012 forward window clean; corporate-action candidates are 2012-10-04 and 2012-10-25, outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Rare-metal/gallium policy price confirmation should remain Yellow or local 4B when the stock lacks fresh direct resource exposure, customer/offtake conversion, volume bridge, inventory quality and margin/revision proof. The August 2023 trigger had small residual upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.25, "entry_date": "2023-08-21", "entry_price": 5390, "evidence_family": "rare_metal_gallium_export_control_price_confirmation_without_direct_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "RARE_EARTH_GALLIUM_SUPPLY_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-31", "low_price_180d": 3170, "peak_date": "2023-08-21", "peak_price": 5790, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/081/081150.json", "raw_component_score_breakdown": {"customer_offtake_or_substitution_bridge": 2, "direct_company_exposure": 3, "information_confidence": 3, "margin_revision_bridge": 1, "market_mispricing": 4, "policy_durability": 5, "resource_specificity": 5, "strategic_resource_policy_salience": 8, "total": 32, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_081150_TFLEX_20230821_RARE_METAL_GALLIUM_POLICY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_salience", "resource_specificity_and_direct_company_exposure", "customer_offtake_policy_durability_margin_revision_route"], "stage3_evidence_fields": ["direct_company_resource_exposure_required", "customer_offtake_or_substitution_conversion_required", "margin_revision_and_policy_durability_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_exposure_gap", "resource_supply_theme_not_converted_to_volume_or_offtake", "margin_revision_bridge_failure"], "symbol": "081150", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081150/2023.csv", "trigger_date": "2023-08-21", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "RARE_EARTH_GALLIUM_SUPPLY_POLICY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "strategic_resource_policy_supply_rare_earth_gallium_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource policy rows should allow Stage2 only when policy salience maps to resource specificity, direct company exposure, customer/offtake or substitution bridge, policy durability and margin-revision evidence; rare-earth/gallium price premiums should route to Yellow/local 4B when the policy-to-company earnings bridge has not refreshed.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C16 + symbol + trigger_type + entry_date.
3. Add C16-specific strategic-resource policy / direct exposure / resource specificity / customer-offtake / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_STAGE2_ALLOWED_ON_DIRECT_RESOURCE_EXPOSURE_OFFTAKE_MARGIN_REVISION_BRIDGE
- C16_GREEN_REQUIRES_RESOURCE_SPECIFICITY_POLICY_DURABILITY_AND_EARNINGS_CONVERSION
- C16_RARE_EARTH_GALLIUM_POLICY_PRICE_PREMIUM_LOCAL_4B
- C16_PRICE_CONFIRMATION_WITHOUT_POLICY_TO_COMPANY_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

