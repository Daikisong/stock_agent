# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy / lithium supply direct-economics guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_RESOURCE_POLICY_SUPPLY_DIRECT_ECONOMICS_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_lithium_resource_direct_bridge_2023_research.md
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

This run avoids those top-covered C16 symbols and adds 005490, 001570, and 009520.  
Each row uses a new `C16 + symbol + trigger_type + entry_date` hard key.

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
005490 POSCO홀딩스: corporate_action_candidate_count=0.
001570 금양: selected 2023 forward window clean; corporate-action candidates are 1998/2000/2001/2003/2007 and outside selected test window.
009520 포스코엠텍: selected 2023 forward window clean; corporate-action candidates are 1999/2011/2012 and outside selected test window.
```

## 3. Research thesis

C16 should not treat every strategic-resource or lithium-policy headline as durable supply economics. It should test whether the policy theme becomes direct resource economics:

```text
strategic resource / lithium policy attention
→ direct resource ownership or qualified conversion capacity
→ permitting, project timing and capex funding
→ offtake or customer quality
→ lithium-price capture, margin and revision bridge
→ rerating
```

A resource headline is a map pin. Green should pay only when the map pin becomes a mine, a conversion plant, a customer contract and a margin bridge. Otherwise the pin can become a valuation flare: bright, hot, and short-lived.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C16_005490_POSCOHOLDINGS_20230330_LITHIUM_RESOURCE_POLICY_SUPPLY_STAGE2 | 005490 | positive_integrated_lithium_resource_policy_supply_stage2_success_with_later_4b | 2023-03-30 | 339500 | 764000 on 2023-07-26 | 335000 on 2023-03-30 | 28.42% | 125.04% | 125.04% | -1.33% | -45.62% |
| C16_001570_KUMYANG_20230726_LITHIUM_RESOURCE_EXPLORATION_PRICE_PREMIUM_4B | 001570 | lithium_resource_exploration_price_premium_counterexample | 2023-07-26 | 152200 | 194000 on 2023-07-26 | 83000 on 2023-10-27 | 27.46% | 27.46% | 27.46% | -45.47% | -57.22% |
| C16_009520_POSCOMTECH_20230726_LITHIUM_AFFILIATE_PRICE_PREMIUM_4B | 009520 | lithium_affiliate_supply_chain_price_premium_counterexample | 2023-07-26 | 39150 | 47000 on 2023-07-26 | 21050 on 2023-10-31 | 20.05% | 20.05% | 20.05% | -46.23% | -55.21% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Strategic-resource policy can be a valid Stage2 route when it is tied to direct resource ownership, conversion capacity, offtake/customer quality and a capex-to-revision bridge.
- 005490 is the positive anchor. The lithium/resource-policy route had a real integrated supply-chain body: resource exposure, conversion-capacity narrative, battery-materials customer relevance and balance-sheet ability to fund capex. The forward path produced a large MFE before the July 2023 blowoff became a risk-control problem.

### Stage3 / Green
- C16 Green should require resource grade/reserve proof, permitting, project timing, capex financing, offtake/customer quality, conversion yield, lithium-price capture, margin and revision confirmation.
- 001570 shows why exploration/resource optionality should not be promoted to Green when grade, reserve, permitting, offtake and financing evidence do not yet carry the valuation.
- 009520 shows the affiliate-supply-chain version: linkage to the resource theme is not the same as direct lithium economics.

### 4B
- 001570 is a clean local 4B counterexample. The price made the forward-window high on the trigger day, then entered a deep drawdown as direct resource economics did not keep validating the premium.
- 009520 fills the affiliate-premium 4B pocket. It had theme heat and group linkage, but no direct enough resource/capacity/margin bridge to justify the price already paid.
- 005490 also required later 4B discipline after a valid Stage2 route became a fully capitalized lithium-resource premium.

### 4C
- No hard resource cancellation, permitting denial, or reserve write-down is asserted.
- The C16 break mode is direct-economics exhaustion: the resource policy theme remains real, but grade, permitting, offtake, capex, conversion yield, lithium-price capture and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C16_001570_KUMYANG_20230726_LITHIUM_RESOURCE_EXPLORATION_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 23,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C16_005490_POSCOHOLDINGS_20230330_LITHIUM_RESOURCE_POLICY_SUPPLY_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 4,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 56,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  },
  "C16_009520_POSCOMTECH_20230726_LITHIUM_AFFILIATE_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 23,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_policy_attention and direct_resource_conversion_offtake_revision_bridge_visible:
    allow_stage2_actionable = true

if lithium_resource_theme_price_premium and no resource_grade_offtake_capex_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and direct_resource_economics_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 001570 / 2023-07-26: lithium resource exploration optionality can be over-promoted if the model treats price strength as reserve, permitting, offtake and financing proof.
- 009520 / 2023-07-26: lithium affiliate linkage can become price-only when direct resource capacity, conversion economics and revision evidence are absent.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -1.33, "MAE_30D_pct": -1.33, "MAE_90D_pct": -1.33, "MFE_180D_pct": 125.04, "MFE_30D_pct": 28.42, "MFE_90D_pct": 125.04, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_005490_POSCOHOLDINGS_20230330_LITHIUM_RESOURCE_POLICY_SUPPLY_STAGE2", "case_role": "positive_integrated_lithium_resource_policy_supply_stage2_success_with_later_4b", "company_name": "POSCO홀딩스", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2023_forward_window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when strategic lithium/resource-policy attention attached to direct resource ownership, downstream conversion capacity and a visible battery-materials supply-chain route. Green still requires project timing, offtake/customer quality, conversion yield, lithium-price sensitivity, capex burden and revision bridge; after the July 2023 blowoff, the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.62, "entry_date": "2023-03-30", "entry_price": 339500, "evidence_family": "integrated_lithium_resource_policy_supply_argentina_hydroxide_capacity_revision_route", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_DIRECT_ECONOMICS_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-03-30", "low_price_180d": 335000, "peak_date": "2023-07-26", "peak_price": 764000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 4, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 56, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C16_005490_POSCOHOLDINGS_20230330_LITHIUM_RESOURCE_POLICY_SUPPLY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_supply_chain_attention", "direct_resource_or_conversion_capacity_visibility", "offtake_customer_capex_or_revision_route"], "stage3_evidence_fields": ["resource_grade_reserve_and_project_timing_required", "offtake_customer_quality_and_permitting_required", "conversion_yield_lithium_price_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_theme_valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_grade_or_permitting_gap", "offtake_capex_financing_or_conversion_economics_failure", "lithium_price_margin_revision_bridge_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "trigger_date": "2023-03-30", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.47, "MAE_30D_pct": -30.75, "MAE_90D_pct": -45.47, "MFE_180D_pct": 27.46, "MFE_30D_pct": 27.46, "MFE_90D_pct": 27.46, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_001570_KUMYANG_20230726_LITHIUM_RESOURCE_EXPLORATION_PRICE_PREMIUM_4B", "case_role": "lithium_resource_exploration_price_premium_counterexample", "company_name": "금양", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 1998-12-01, 2000-04-17, 2001-11-29, 2003-08-01, 2007-10-23, all outside selected test window", "current_profile_error": true, "current_profile_verdict": "Lithium-resource exploration price premium should route to local 4B or counterexample unless resource grade/reserve proof, permitting, offtake, financing/capex plan, conversion economics and revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -57.22, "entry_date": "2023-07-26", "entry_price": 152200, "evidence_family": "lithium_resource_exploration_policy_theme_price_premium_without_resource_grade_offtake_capex_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_DIRECT_ECONOMICS_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-27", "low_price_180d": 83000, "peak_date": "2023-07-26", "peak_price": 194000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001570.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 23, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C16_001570_KUMYANG_20230726_LITHIUM_RESOURCE_EXPLORATION_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_supply_chain_attention", "direct_resource_or_conversion_capacity_visibility", "offtake_customer_capex_or_revision_route"], "stage3_evidence_fields": ["resource_grade_reserve_and_project_timing_required", "offtake_customer_quality_and_permitting_required", "conversion_yield_lithium_price_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_theme_valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_grade_or_permitting_gap", "offtake_capex_financing_or_conversion_economics_failure", "lithium_price_margin_revision_bridge_failure"], "symbol": "001570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -46.23, "MAE_30D_pct": -34.36, "MAE_90D_pct": -46.23, "MFE_180D_pct": 20.05, "MFE_30D_pct": 20.05, "MFE_90D_pct": 20.05, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_009520_POSCOMTECH_20230726_LITHIUM_AFFILIATE_PRICE_PREMIUM_4B", "case_role": "lithium_affiliate_supply_chain_price_premium_counterexample", "company_name": "포스코엠텍", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 1999-03-30, 1999-04-22, 2011-01-05, 2012-05-14, all outside selected test window", "current_profile_error": true, "current_profile_verdict": "Lithium-affiliate supply-chain price premium should route to local 4B or counterexample when the firm has theme linkage but lacks direct resource ownership, conversion capacity, offtake economics, lithium-price capture and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.21, "entry_date": "2023-07-26", "entry_price": 39150, "evidence_family": "lithium_affiliate_supply_chain_price_premium_without_direct_resource_capacity_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_DIRECT_ECONOMICS_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-31", "low_price_180d": 21050, "peak_date": "2023-07-26", "peak_price": 47000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009520.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 23, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C16_009520_POSCOMTECH_20230726_LITHIUM_AFFILIATE_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_supply_chain_attention", "direct_resource_or_conversion_capacity_visibility", "offtake_customer_capex_or_revision_route"], "stage3_evidence_fields": ["resource_grade_reserve_and_project_timing_required", "offtake_customer_quality_and_permitting_required", "conversion_yield_lithium_price_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_theme_valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_grade_or_permitting_gap", "offtake_capex_financing_or_conversion_economics_failure", "lithium_price_margin_revision_bridge_failure"], "symbol": "009520", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009520/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_DIRECT_ECONOMICS_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "strategic_resource_policy_supply_lithium_direct_economics_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource policy/supply rows should allow Stage2 when resource-policy attention is backed by direct resource ownership, conversion capacity, offtake/customer quality and capex-to-revision bridge, but Stage3 Green requires resource grade/reserve proof, permitting, conversion yield, lithium-price capture, margin and revision evidence; resource-theme price premium without direct economics should route to local 4B or counterexample.",
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
3. Add C16-specific strategic-resource / direct-resource-economics / lithium-policy / 4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_STAGE2_ALLOWED_ON_DIRECT_RESOURCE_CONVERSION_OFFTAKE_REVISION_BRIDGE
- C16_GREEN_REQUIRES_RESOURCE_GRADE_PERMITTING_CAPEX_OFFTAKE_CONVERSION_MARGIN_REVISION
- C16_LITHIUM_RESOURCE_THEME_PRICE_PREMIUM_LOCAL_4B
- C16_RESOURCE_POLICY_WITHOUT_DIRECT_ECONOMICS_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

