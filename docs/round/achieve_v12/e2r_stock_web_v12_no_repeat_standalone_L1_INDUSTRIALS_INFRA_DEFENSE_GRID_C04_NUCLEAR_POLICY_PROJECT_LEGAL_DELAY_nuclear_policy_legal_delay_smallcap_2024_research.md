# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C04 — Nuclear policy / project legal-delay small-cap supplier guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_POLICY_LEGAL_DELAY_SMALLCAP_SUPPLIER_SCOPE_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_nuclear_policy_legal_delay_smallcap_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY current coverage:
rows=9, symbols=5, date range=2024-07-18~2024-12-03, good/bad S2=1/5, 4B/4C=1/0
top covered symbols: 034020(3), 051600(2), 052690(2), 000720(1), 083650(1)
```

This run avoids those top-covered C04 symbols and adds 006910, 094820, and 105840.  
Each row uses a new `C04 + symbol + trigger_type + entry_date` hard key.

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
006910 보성파워텍: 2024/2025 forward window clean; latest corporate-action candidate is 2016-08-29, outside the selected test window.
094820 일진파워: 2024/2025 forward window clean; corporate-action candidates are 2011-09-08 and 2011-09-30, outside the selected test window.
105840 우진: 2024/2025 forward window clean; corporate-action candidates are 2012-11-19 and 2012-12-11, outside the selected test window.
```

## 3. Research thesis

C04 should not treat a nuclear policy award as immediate supplier EPS. It should test whether a policy/project headline crosses into signed supplier economics:

```text
nuclear policy / project award headline
→ legal-delay or protest clearance
→ signed scope and supplier allocation
→ delivery schedule and contract conversion
→ margin and revision bridge
→ rerating
```

The policy award is the gate opening. The supplier still needs a ticket, a seat number, and a paid itinerary. Small-cap nuclear suppliers often trade as if the whole plant has already become their backlog, but the evidence bridge is much narrower.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C04_006910_BOSUNG_20240718_CZECH_NUCLEAR_POLICY_PREMIUM_4B | 006910 | protective_nuclear_policy_smallcap_4b_success | 2024-07-18 | 3630 | 4280 on 2024-07-18 | 2100 on 2025-04-04 | 17.91% | 17.91% | 17.91% | -42.15% | -50.93% |
| C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_POLICY_LEGAL_DELAY_FALSE_GREEN | 094820 | nuclear_maintenance_policy_false_green_counterexample | 2024-07-18 | 11980 | 13420 on 2024-07-18 | 7320 on 2025-04-09 | 12.02% | 12.02% | 12.02% | -38.9% | -45.45% |
| C04_105840_WOOJIN_20240718_NUCLEAR_INSTRUMENT_POLICY_PREMIUM_4B | 105840 | nuclear_instrumentation_policy_premium_counterexample | 2024-07-18 | 9300 | 10950 on 2024-07-18 | 5630 on 2024-12-09 | 17.74% | 17.74% | 17.74% | -39.46% | -48.58% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD should be treated as a clean Stage2/Green positive.
- A project award headline can justify research routing, but not Green, unless supplier scope, contract timing, delivery schedule, legal-delay clearance, margin and revision evidence are visible.
- The 2024-07-18 rows show why price confirmation alone is weak: the same-day highs became the forward peaks, while MAE widened quickly.

### 4B
- 006910 is the protective 4B anchor. The signal was not "buy the policy headline"; it was "the policy headline has already been capitalized intraday, require scope proof."
- 094820 and 105840 are false-Green / local 4B counterexamples. Both had a project-policy spike but then followed deep drawdown paths as supplier-order and revision evidence did not close.

### 4C
- No hard contract cancellation or legal defeat is asserted in this MD.
- The C04 break mode is project-to-supplier conversion failure: policy remains real, but legal delay, contract scope, supplier allocation, delivery schedule and margin revisions do not arrive fast enough to support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C04_006910_BOSUNG_20240718_CZECH_NUCLEAR_POLICY_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 22,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_POLICY_LEGAL_DELAY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 22,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C04_105840_WOOJIN_20240718_NUCLEAR_INSTRUMENT_POLICY_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 22,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C04 guard:
```text
if nuclear_policy_award_headline and no signed_supplier_scope_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if smallcap_supplier_price_premium and legal_delay_or_project_scope_unclear:
    require_non_price_supplier_order_evidence = true

if post_peak_drawdown and supplier_contract_conversion_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 094820 / 2024-07-18: nuclear maintenance/project policy attention can be over-promoted if signed scope, legal-delay clearance and revision evidence are not required.
- 105840 / 2024-07-18: nuclear instrumentation/supplier premium can become price-only when supplier allocation and delivery schedule evidence do not close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -42.15, "MAE_30D_pct": -29.48, "MAE_90D_pct": -29.48, "MFE_180D_pct": 17.91, "MFE_30D_pct": 17.91, "MFE_90D_pct": 17.91, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_006910_BOSUNG_20240718_CZECH_NUCLEAR_POLICY_PREMIUM_4B", "case_role": "protective_nuclear_policy_smallcap_4b_success", "company_name": "보성파워텍", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when the nuclear policy/project award headline had already been capitalized intraday but signed scope, supplier allocation, legal protest risk, delivery schedule, margin and revision evidence had not closed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.93, "entry_date": "2024-07-18", "entry_price": 3630, "evidence_family": "nuclear_policy_award_smallcap_price_premium_without_signed_scope_delivery_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_POLICY_LEGAL_DELAY_SMALLCAP_SUPPLIER_SCOPE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-04", "low_price_180d": 2100, "peak_date": "2024-07-18", "peak_price": 4280, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006910.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 22, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C04_006910_BOSUNG_20240718_CZECH_NUCLEAR_POLICY_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_award_attention", "supplier_scope_or_project_schedule_claim", "signed_contract_or_revision_bridge_required_before_positive_green"], "stage3_evidence_fields": ["legal_delay_or_protest_clearance_required", "signed_scope_and_supplier_allocation_required", "delivery_schedule_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_policy_smallcap_price_premium", "project_award_headline_without_scope", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_scope_not_converting_to_supplier_order", "legal_delay_or_contract_timing_gap", "margin_revision_bridge_failure"], "symbol": "006910", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.9, "MAE_30D_pct": -28.96, "MAE_90D_pct": -28.96, "MFE_180D_pct": 12.02, "MFE_30D_pct": 12.02, "MFE_90D_pct": 12.02, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_POLICY_LEGAL_DELAY_FALSE_GREEN", "case_role": "nuclear_maintenance_policy_false_green_counterexample", "company_name": "일진파워", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Nuclear maintenance/project policy attention should stay Yellow or local 4B unless signed contract scope, project schedule, legal-delay/protest clearance, margin and revision bridge are visible after the policy headline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.45, "entry_date": "2024-07-18", "entry_price": 11980, "evidence_family": "nuclear_maintenance_project_award_theme_without_contract_scope_legal_delay_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_POLICY_LEGAL_DELAY_SMALLCAP_SUPPLIER_SCOPE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 7320, "peak_date": "2024-07-18", "peak_price": 13420, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/094/094820.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 22, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_POLICY_LEGAL_DELAY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_award_attention", "supplier_scope_or_project_schedule_claim", "signed_contract_or_revision_bridge_required_before_positive_green"], "stage3_evidence_fields": ["legal_delay_or_protest_clearance_required", "signed_scope_and_supplier_allocation_required", "delivery_schedule_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_policy_smallcap_price_premium", "project_award_headline_without_scope", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_scope_not_converting_to_supplier_order", "legal_delay_or_contract_timing_gap", "margin_revision_bridge_failure"], "symbol": "094820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.46, "MAE_30D_pct": -23.44, "MAE_90D_pct": -23.44, "MFE_180D_pct": 17.74, "MFE_30D_pct": 17.74, "MFE_90D_pct": 17.74, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_105840_WOOJIN_20240718_NUCLEAR_INSTRUMENT_POLICY_PREMIUM_4B", "case_role": "nuclear_instrumentation_policy_premium_counterexample", "company_name": "우진", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Nuclear instrumentation/supplier price premium should route to local 4B or counterexample when policy award attention is not followed by explicit supplier scope, project timing, legal-delay clearance, margin and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.58, "entry_date": "2024-07-18", "entry_price": 9300, "evidence_family": "nuclear_instrumentation_supplier_policy_premium_without_project_scope_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_POLICY_LEGAL_DELAY_SMALLCAP_SUPPLIER_SCOPE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 5630, "peak_date": "2024-07-18", "peak_price": 10950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/105/105840.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 22, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C04_105840_WOOJIN_20240718_NUCLEAR_INSTRUMENT_POLICY_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_award_attention", "supplier_scope_or_project_schedule_claim", "signed_contract_or_revision_bridge_required_before_positive_green"], "stage3_evidence_fields": ["legal_delay_or_protest_clearance_required", "signed_scope_and_supplier_allocation_required", "delivery_schedule_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_policy_smallcap_price_premium", "project_award_headline_without_scope", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_scope_not_converting_to_supplier_order", "legal_delay_or_contract_timing_gap", "margin_revision_bridge_failure"], "symbol": "105840", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "NUCLEAR_POLICY_LEGAL_DELAY_SMALLCAP_SUPPLIER_SCOPE_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "nuclear_policy_project_legal_delay_smallcap_supplier_scope_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C04 nuclear policy/project legal-delay rows should route small-cap supplier/theme price premiums to local 4B unless signed project scope, supplier allocation, legal-delay/protest clearance, delivery schedule, margin and revision bridge are explicit; policy award headlines alone should not become Stage2/Green.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C04 + symbol + trigger_type + entry_date.
3. Add C04-specific nuclear policy / legal-delay / supplier-scope / delivery-margin guard only as a shadow candidate until more rows exist.

Candidate rule:
- C04_POLICY_AWARD_HEADLINE_BLOCKS_GREEN_WITHOUT_SIGNED_SUPPLIER_SCOPE
- C04_SMALLCAP_SUPPLIER_PRICE_PREMIUM_LOCAL_4B
- C04_LEGAL_DELAY_OR_PROJECT_SCOPE_UNCLEAR_REQUIRES_NON_PRICE_ORDER_EVIDENCE
- C04_PROJECT_TO_SUPPLIER_CONVERSION_FAILURE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

