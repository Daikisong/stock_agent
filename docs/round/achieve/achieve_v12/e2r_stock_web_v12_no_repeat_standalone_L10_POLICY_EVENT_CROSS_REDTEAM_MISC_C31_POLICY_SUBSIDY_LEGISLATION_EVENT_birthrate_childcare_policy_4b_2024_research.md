# E2R V12 No-Repeat Standalone Residual Research
## R11 / L10 / C31 — Policy subsidy legislation / birthrate-childcare direct-revenue guard

metadata:
```text
selected_round: R11
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: BIRTHRATE_CHILDCARE_POLICY_DIRECT_REVENUE_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_birthrate_childcare_policy_4b_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT current coverage:
rows=34, symbols=14, date range=2020-07-15~2024-07-18, good/bad S2=10/10, 4B/4C=1/0
top covered symbols: 112610(6), 034020(4), 336260(4), UNKNOWN_SYMBOL(4), 036460(3)
```

This run avoids those top-covered C31 symbols and adds 013990, 159580, and 407400.  
Each row uses a new `C31 + symbol + trigger_type + entry_date` hard key.

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
013990 아가방컴퍼니: 2024 forward window clean; corporate-action candidate is 2008-05-16 and outside selected test window.
159580 제로투세븐: 2024 forward window clean; corporate-action candidate is 2018-11-13 and outside selected test window.
407400 꿈비: 2024 forward window clean; corporate-action candidate is 2023-07-19 and outside selected test window.
```

## 3. Research thesis

C31 should not treat every policy headline as a direct earnings bridge. It should test whether the policy reaches the listed company's revenue and margin:

```text
policy / subsidy / legislation attention
→ direct beneficiary mapping
→ subsidy-to-revenue conversion
→ channel sell-through and inventory quality
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A policy headline is a public road sign. Green should not buy the sign; it should buy the toll booth that actually collects traffic.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C31_013990_AGABANG_20240103_BIRTHRATE_CHILDCARE_POLICY_THEME_4B | 013990 | protective_birthrate_childcare_policy_theme_4b_success | 2024-01-03 | 5630 | 7180 on 2024-01-18 | 4130 on 2024-01-03 | 27.53% | 27.53% | 27.53% | -26.64% | -40.88% |
| C31_159580_ZEROSEVEN_20240103_BIRTHRATE_POLICY_FALSE_GREEN | 159580 | birthrate_childcare_policy_false_green_counterexample | 2024-01-03 | 8020 | 8590 on 2024-01-18 | 4180 on 2024-09-24 | 7.11% | 7.11% | 7.11% | -47.88% | -51.34% |
| C31_407400_GGOOMBI_20240103_BIRTHRATE_INFANT_GOODS_POLICY_PREMIUM_4B | 407400 | infant_goods_policy_theme_price_premium_counterexample | 2024-01-03 | 13410 | 14700 on 2024-01-03 | 6750 on 2024-09-24 | 9.62% | 9.62% | 9.62% | -49.66% | -54.08% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as clean Stage2/Green positive.
- C31 Green should require direct beneficiary mapping, subsidy-to-revenue conversion, channel sell-through, inventory quality, gross margin and revision confirmation.
- 159580 is the false-Green/Yellow guard: a short price confirmation after the birthrate-policy event did not produce a durable revenue or margin bridge.

### 4B
- 013990 is the protective 4B anchor. The policy theme moved sharply, but the price path later required local 4B discipline because direct monetization evidence did not refresh.
- 407400 is the infant-goods price-premium counterexample. The trigger-day premium had limited forward upside and then drew down as policy-to-company evidence failed to close.
- The key guard is that a broad birthrate policy can be socially important while still being too indirect for company-level EPS rerating.

### 4C
- No hard policy repeal, subsidy cancellation, or accounting break is asserted.
- The C31 break mode is conversion gap: policy attention remains real, but direct subsidy-to-revenue, sell-through, inventory, gross margin and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C31_013990_AGABANG_20240103_BIRTHRATE_CHILDCARE_POLICY_THEME_4B": {
    "direct_beneficiary_quality": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "policy_catalyst_intensity": 8,
    "subsidy_revenue_conversion": 2,
    "total": 22,
    "valuation_rerating_runway": 1
  },
  "C31_159580_ZEROSEVEN_20240103_BIRTHRATE_POLICY_FALSE_GREEN": {
    "direct_beneficiary_quality": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "policy_catalyst_intensity": 7,
    "subsidy_revenue_conversion": 2,
    "total": 22,
    "valuation_rerating_runway": 1
  },
  "C31_407400_GGOOMBI_20240103_BIRTHRATE_INFANT_GOODS_POLICY_PREMIUM_4B": {
    "direct_beneficiary_quality": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "policy_catalyst_intensity": 7,
    "subsidy_revenue_conversion": 2,
    "total": 21,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C31 guard:
```text
if policy_theme_attention and no_direct_beneficiary_revenue_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_or_yellow = true

if policy_theme_price_premium and post_peak_drawdown_confirms:
    keep_as_counterexample_until_direct_conversion_evidence = true

if subsidy_to_revenue_bridge appears later:
    require fresh entry_date and new non-price evidence before Stage2/Green
```

Residual errors:
```text
current_profile_error_count = 2
- 159580 / 2024-01-03: birthrate-policy price confirmation can be over-promoted if the model treats policy salience as direct revenue and margin proof.
- 407400 / 2024-01-03: infant-goods policy theme premium can become price-only when channel sell-through, subsidy conversion and revision evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -26.64, "MAE_30D_pct": -26.64, "MAE_90D_pct": -26.64, "MFE_180D_pct": 27.53, "MFE_30D_pct": 27.53, "MFE_90D_pct": 27.53, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_013990_AGABANG_20240103_BIRTHRATE_CHILDCARE_POLICY_THEME_4B", "case_role": "protective_birthrate_childcare_policy_theme_4b_success", "company_name": "아가방컴퍼니", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2008-05-16 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when birthrate/childcare policy enthusiasm had already been capitalized but direct subsidy-to-revenue conversion, channel sell-through, inventory, margin and revision evidence did not support the premium. The case is not a Stage2/Green positive.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.88, "entry_date": "2024-01-03", "entry_price": 5630, "evidence_family": "birthrate_childcare_policy_theme_price_premium_without_direct_subsidy_revenue_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "BIRTHRATE_CHILDCARE_POLICY_DIRECT_REVENUE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-01-03", "low_price_180d": 4130, "peak_date": "2024-01-18", "peak_price": 7180, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/013/013990.json", "raw_component_score_breakdown": {"direct_beneficiary_quality": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "policy_catalyst_intensity": 8, "subsidy_revenue_conversion": 2, "total": 22, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C31_013990_AGABANG_20240103_BIRTHRATE_CHILDCARE_POLICY_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_or_legislation_attention", "direct_beneficiary_mapping_required", "subsidy_to_revenue_conversion_required"], "stage3_evidence_fields": ["direct_policy_revenue_bridge_required", "channel_sellthrough_inventory_quality_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_revenue_conversion_gap", "sellthrough_inventory_or_margin_disappointment", "revision_bridge_failure"], "symbol": "013990", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv", "trigger_date": "2024-01-03", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -47.88, "MAE_30D_pct": -19.2, "MAE_90D_pct": -32.42, "MFE_180D_pct": 7.11, "MFE_30D_pct": 7.11, "MFE_90D_pct": 7.11, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_159580_ZEROSEVEN_20240103_BIRTHRATE_POLICY_FALSE_GREEN", "case_role": "birthrate_childcare_policy_false_green_counterexample", "company_name": "제로투세븐", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2018-11-13 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Birthrate-policy price confirmation should stay Yellow when the non-price bridge from policy language to actual company revenue, sell-through, inventory quality, margin and revision evidence is absent.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.34, "entry_date": "2024-01-03", "entry_price": 8020, "evidence_family": "birthrate_policy_childcare_consumption_price_confirmation_without_subsidy_sellthrough_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "BIRTHRATE_CHILDCARE_POLICY_DIRECT_REVENUE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-09-24", "low_price_180d": 4180, "peak_date": "2024-01-18", "peak_price": 8590, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/159/159580.json", "raw_component_score_breakdown": {"direct_beneficiary_quality": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "policy_catalyst_intensity": 7, "subsidy_revenue_conversion": 2, "total": 22, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C31_159580_ZEROSEVEN_20240103_BIRTHRATE_POLICY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_or_legislation_attention", "direct_beneficiary_mapping_required", "subsidy_to_revenue_conversion_required"], "stage3_evidence_fields": ["direct_policy_revenue_bridge_required", "channel_sellthrough_inventory_quality_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_revenue_conversion_gap", "sellthrough_inventory_or_margin_disappointment", "revision_bridge_failure"], "symbol": "159580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/159/159580/2024.csv", "trigger_date": "2024-01-03", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -49.66, "MAE_30D_pct": -27.37, "MAE_90D_pct": -45.64, "MFE_180D_pct": 9.62, "MFE_30D_pct": 9.62, "MFE_90D_pct": 9.62, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_407400_GGOOMBI_20240103_BIRTHRATE_INFANT_GOODS_POLICY_PREMIUM_4B", "case_role": "infant_goods_policy_theme_price_premium_counterexample", "company_name": "꿈비", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2023-07-19 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Infant-goods birthrate-policy premium should route to local 4B or counterexample unless direct policy monetization, distributor/channel sell-through, inventory, gross margin and revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -54.08, "entry_date": "2024-01-03", "entry_price": 13410, "evidence_family": "infant_goods_policy_theme_price_premium_without_direct_subsidy_channel_inventory_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "BIRTHRATE_CHILDCARE_POLICY_DIRECT_REVENUE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-09-24", "low_price_180d": 6750, "peak_date": "2024-01-03", "peak_price": 14700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/407/407400.json", "raw_component_score_breakdown": {"direct_beneficiary_quality": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "policy_catalyst_intensity": 7, "subsidy_revenue_conversion": 2, "total": 21, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C31_407400_GGOOMBI_20240103_BIRTHRATE_INFANT_GOODS_POLICY_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_or_legislation_attention", "direct_beneficiary_mapping_required", "subsidy_to_revenue_conversion_required"], "stage3_evidence_fields": ["direct_policy_revenue_bridge_required", "channel_sellthrough_inventory_quality_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_revenue_conversion_gap", "sellthrough_inventory_or_margin_disappointment", "revision_bridge_failure"], "symbol": "407400", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/407/407400/2024.csv", "trigger_date": "2024-01-03", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "BIRTHRATE_CHILDCARE_POLICY_DIRECT_REVENUE_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "loop_contribution_label": "policy_subsidy_legislation_birthrate_childcare_theme_price_premium_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R11",
  "shadow_rule_candidate": "C31 policy/subsidy/legislation rows should block Stage3 Green when a policy theme lacks direct beneficiary mapping, subsidy-to-revenue conversion, sell-through, inventory quality, margin and revision bridge; childcare/birthrate policy theme price premium should route to local 4B or counterexample unless non-price monetization evidence appears.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C31 + symbol + trigger_type + entry_date.
3. Add C31-specific policy/subsidy direct-beneficiary / subsidy-to-revenue / sell-through / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C31_BLOCK_GREEN_WITHOUT_DIRECT_BENEFICIARY_REVENUE_MARGIN_BRIDGE
- C31_POLICY_THEME_PRICE_PREMIUM_LOCAL_4B
- C31_REQUIRE_SUBSIDY_TO_REVENUE_AND_SELLTHROUGH_EVIDENCE
- C31_POLICY_SALIENCE_WITHOUT_COMPANY_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

