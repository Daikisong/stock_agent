# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C12 — Battery customer contract / call-off risk guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: COPPERFOIL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_copperfoil_separator_calloff_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK current coverage:
rows=15, symbols=9, date range=2023-01-31~2024-07-25, good/bad S2=4/0, 4B/4C=0/0
top covered symbols: UNKNOWN_SYMBOL(4), 247540(2), 278280(2), 003670(1), 005070(1)
```

This run avoids the top-covered C12 symbols and adds 011790, 336370, and 393890.  
Some of these names can appear in other battery archetypes, but this run is not a hard duplicate because the canonical archetype, trigger purpose, and failure mode are different: C12 is specifically about customer contract / call-off / utilization conversion.

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
011790 SKC: 2023 forward window clean; corporate-action candidates are old, outside the test window.
336370 솔루스첨단소재: 2023 forward window clean; corporate-action candidates are in 2024, outside the 2023 test window.
393890 더블유씨피: corporate_action_candidate_count=0.
```

## 3. Research thesis

C12 should not treat contract/customer language as final proof. It should test whether a signed or narrated customer route actually converts:

```text
battery customer / contract / long-term supply story
→ call-off volume
→ utilization and shipment conversion
→ margin bridge
→ revision confirmation
→ rerating
```

The customer name is the invitation, not the revenue. In battery materials, the important line is not the contract headline; it is the call-off. Without call-off volume and utilization, the contract is a warehouse door painted on the wall.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C12_011790_SKC_20230331_COPPERFOIL_CUSTOMER_CALLOFF_FALSE_GREEN | 011790 | customer_calloff_margin_false_green_counterexample | 2023-03-31 | 114300 | 122300 on 2023-04-05 | 68000 on 2023-10-23 | 7.0% | 7.0% | 7.0% | -40.51% | -44.4% |
| C12_336370_SOLUS_20230222_COPPERFOIL_CONTRACT_CALLOFF_COUNTEREXAMPLE | 336370 | contract_visibility_false_green_counterexample | 2023-02-22 | 52200 | 54000 on 2023-02-22 | 21300 on 2023-11-01 | 3.45% | 3.45% | 3.45% | -59.2% | -60.56% |
| C12_393890_WCP_20230704_SEPARATOR_CONTRACT_CALLOFF_LOCAL_4B | 393890 | protective_calloff_risk_4b_success | 2023-07-04 | 73800 | 87500 on 2023-07-26 | 38300 on 2023-11-13 | 18.56% | 18.56% | 18.56% | -48.1% | -56.23% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Battery customer/contract attention is a valid research route.
- It is not sufficient for Green until call-off volume, utilization, shipment conversion, and margin/revision proof arrive.

### Stage3 / Green
- C12 Green should require company-level conversion, not just sector-level EV demand or customer-name credibility.
- SKC and 솔루스첨단소재 show the false-Green failure: copper-foil contract language can still lead to deep drawdown if utilization and margin recovery do not materialize.

### 4B
- 더블유씨피 is the protective 4B anchor. The separator/customer-contract price premium had expanded enough that risk control was more useful than fresh Green.
- Local 4B should activate when the market has already priced the contract story but the call-off bridge remains unproven.

### 4C
- No hard accounting break is asserted.
- The C12 break mode is conversion failure: customer language remains real enough to sound plausible, but call-off, utilization, shipments, margin, and revision do not carry the valuation.

## 6. Raw component score breakdown

```json
{
  "C12_011790_SKC_20230331_COPPERFOIL_CUSTOMER_CALLOFF_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 29,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C12_336370_SOLUS_20230222_COPPERFOIL_CONTRACT_CALLOFF_COUNTEREXAMPLE": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 29,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C12_393890_WCP_20230704_SEPARATOR_CONTRACT_CALLOFF_LOCAL_4B": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 34,
    "valuation_rerating_runway": 3,
    "visibility_quality": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C12 guard:
```text
if battery_customer_contract_attention and no calloff_utilization_shipment_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if contract_story_price_premium and no incremental_calloff_evidence:
    route_to_local_4B_watch = true

if post_peak_drawdown and customer_calloff_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 011790 / 2023-03-31: copper-foil/customer-contract language can be over-promoted if call-off and utilization are not required.
- 336370 / 2023-02-22: contract visibility without utilization and margin recovery created a deep drawdown path, arguing for Yellow/counterexample treatment.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -40.51, "MAE_30D_pct": -20.21, "MAE_90D_pct": -23.01, "MFE_180D_pct": 7.0, "MFE_30D_pct": 7.0, "MFE_90D_pct": 7.0, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_011790_SKC_20230331_COPPERFOIL_CUSTOMER_CALLOFF_FALSE_GREEN", "case_role": "customer_calloff_margin_false_green_counterexample", "company_name": "SKC", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Copper-foil customer/contract language should not become Green without call-off volume, utilization, spread/margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.4, "entry_date": "2023-03-31", "entry_price": 114300, "evidence_family": "copperfoil_customer_contract_without_calloff_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-23", "low_price_180d": 68000, "peak_date": "2023-04-05", "peak_price": 122300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011790.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 29, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C12_011790_SKC_20230331_COPPERFOIL_CUSTOMER_CALLOFF_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_attention", "named_customer_or_long_term_supply_claim", "price_relative_strength"], "stage3_evidence_fields": ["calloff_volume_confirmation_required", "utilization_and_shipments_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["contract_story_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_delay_or_customer_utilization_shortfall", "contract_without_shipments_or_margin", "revision_bridge_failure"], "symbol": "011790", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv", "trigger_date": "2023-03-31", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -59.2, "MAE_30D_pct": -21.74, "MAE_90D_pct": -32.57, "MFE_180D_pct": 3.45, "MFE_30D_pct": 3.45, "MFE_90D_pct": 3.45, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_336370_SOLUS_20230222_COPPERFOIL_CONTRACT_CALLOFF_COUNTEREXAMPLE", "case_role": "contract_visibility_false_green_counterexample", "company_name": "솔루스첨단소재", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "A copper-foil contract/customer story should stay Yellow when call-off pace, utilization and margin recovery are not visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.56, "entry_date": "2023-02-22", "entry_price": 52200, "evidence_family": "copperfoil_contract_visibility_without_customer_calloff_and_margin_recovery", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-01", "low_price_180d": 21300, "peak_date": "2023-02-22", "peak_price": 54000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336370.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 29, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C12_336370_SOLUS_20230222_COPPERFOIL_CONTRACT_CALLOFF_COUNTEREXAMPLE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_attention", "named_customer_or_long_term_supply_claim", "price_relative_strength"], "stage3_evidence_fields": ["calloff_volume_confirmation_required", "utilization_and_shipments_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["contract_story_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_delay_or_customer_utilization_shortfall", "contract_without_shipments_or_margin", "revision_bridge_failure"], "symbol": "336370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv", "trigger_date": "2023-02-22", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -48.1, "MAE_30D_pct": -10.98, "MAE_90D_pct": -37.47, "MFE_180D_pct": 18.56, "MFE_30D_pct": 18.56, "MFE_90D_pct": 18.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_393890_WCP_20230704_SEPARATOR_CONTRACT_CALLOFF_LOCAL_4B", "case_role": "protective_calloff_risk_4b_success", "company_name": "더블유씨피", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful after separator/customer-contract price premium expanded; fresh Green required incremental call-off, utilization and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -56.23, "entry_date": "2023-07-04", "entry_price": 73800, "evidence_family": "separator_customer_contract_price_run_calloff_risk_local_4b_guard", "evidence_url_pending": false, "fine_archetype_id": "COPPERFOIL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-13", "low_price_180d": 38300, "peak_date": "2023-07-26", "peak_price": 87500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 4, "total": 34, "valuation_rerating_runway": 3, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C12_393890_WCP_20230704_SEPARATOR_CONTRACT_CALLOFF_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_attention", "named_customer_or_long_term_supply_claim", "price_relative_strength"], "stage3_evidence_fields": ["calloff_volume_confirmation_required", "utilization_and_shipments_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["contract_story_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_delay_or_customer_utilization_shortfall", "contract_without_shipments_or_margin", "revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-04", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "COPPERFOIL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_customer_calloff_risk_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C12 battery customer/contract rows should cap at Stage2/Yellow unless call-off volume, utilization, shipments, margin and revision bridge close; contract-story price premium without shipment conversion should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C12 + symbol + trigger_type + entry_date.
3. Add C12-specific customer-contract / call-off / utilization / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C12_GREEN_REQUIRES_CALLOFF_UTILIZATION_SHIPMENT_MARGIN_REVISION
- C12_CUSTOMER_CONTRACT_ATTENTION_STAGE2_YELLOW_CAP
- C12_CONTRACT_STORY_PRICE_PREMIUM_LOCAL_4B
- C12_COPPERFOIL_SEPARATOR_CALLOFF_FAILURE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

