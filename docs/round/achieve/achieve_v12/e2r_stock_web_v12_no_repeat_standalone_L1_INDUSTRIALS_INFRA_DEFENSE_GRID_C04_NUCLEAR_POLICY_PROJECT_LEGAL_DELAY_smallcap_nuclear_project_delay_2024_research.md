# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C04 — Nuclear policy project legal-delay guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: SMALLCAP_NUCLEAR_PROJECT_SCOPE_LEGAL_DELAY_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_smallcap_nuclear_project_delay_2024_research.md
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

This run avoids those top-covered C04 symbols and adds 032820, 094820, and 189860.  
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
032820 우리기술: 2024/2025 selected forward window clean; corporate-action candidates are historical and outside selected test window.
094820 일진파워: 2024/2025 selected forward window clean; corporate-action candidates are 2011-09-08 and 2011-09-30, outside selected test window.
189860 서전기전: 2024/2025 selected forward window clean; corporate-action candidate is 2018-11-16 and outside selected test window.
```

## 3. Research thesis

C04 should not treat a nuclear export project or policy headline as immediate earnings for every peripheral nuclear stock. It should ask whether the theme becomes direct scope:

```text
nuclear policy / export project attention
→ signed scope and customer allocation
→ legal/project timing clarity
→ delivery schedule and acceptance
→ margin and revision bridge
→ rerating or local 4B cap
```

A nuclear project headline is a lighthouse; it can guide attention, but it is not the ship. Green should require the ship: signed scope, delivery slots, legal timing and a margin invoice.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C04_032820_WOORITECH_20240718_NUCLEAR_PROJECT_PERIPHERAL_4B | 032820 | protective_smallcap_nuclear_policy_project_premium_4b_success | 2024-07-18 | 2700 | 3300 on 2024-07-18 | 1453 on 2025-04-09 | 22.22% | 22.22% | 22.22% | -46.19% | -55.97% |
| C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_EXPORT_FALSE_GREEN | 094820 | nuclear_maintenance_project_false_green_counterexample | 2024-07-18 | 11980 | 13420 on 2024-07-18 | 7320 on 2025-04-09 | 12.02% | 12.02% | 12.02% | -38.9% | -45.45% |
| C04_189860_SEOJEON_20240718_NUCLEAR_SWITCHGEAR_LEGAL_DELAY_4B | 189860 | nuclear_switchgear_project_price_premium_counterexample | 2024-07-18 | 6740 | 8270 on 2024-07-18 | 3290 on 2024-12-09 | 22.7% | 22.7% | 22.7% | -51.19% | -60.22% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a Stage2/Green positive. The cases are project-scope and legal-delay guards.
- C04 Green should require signed scope, customer allocation, delivery schedule, legal/project timing clarity, margin and revision confirmation.
- 094820 shows why maintenance/project exposure should stay Yellow when the stock reacts to the policy event but signed backlog and margin evidence do not expand.

### 4B
- 032820 is the protective 4B anchor. The trigger-day price premium had a strong intraday high but then developed a deep post-peak drawdown.
- 189860 is the switchgear/peripheral equipment version. Theme heat without direct contract-scope evidence became a local 4B/counterexample row.
- For both rows, the error to avoid is treating the policy lighthouse as the company-specific ship.

### 4C
- No hard contract cancellation or legal rejection is asserted for these rows.
- The C04 break mode is project-scope/benefit delay: the nuclear project remains real, but peripheral-company contract conversion, legal timing, delivery cadence, margin and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C04_032820_WOORITECH_20240718_NUCLEAR_PROJECT_PERIPHERAL_4B": {
    "customer_delivery_margin_bridge": 3,
    "information_confidence": 3,
    "legal_delay_risk": 8,
    "market_mispricing": 3,
    "project_policy_catalyst": 8,
    "signed_scope_visibility": 3,
    "total": 29,
    "valuation_rerating_runway": 1
  },
  "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_EXPORT_FALSE_GREEN": {
    "customer_delivery_margin_bridge": 3,
    "information_confidence": 3,
    "legal_delay_risk": 7,
    "market_mispricing": 4,
    "project_policy_catalyst": 7,
    "signed_scope_visibility": 3,
    "total": 29,
    "valuation_rerating_runway": 2
  },
  "C04_189860_SEOJEON_20240718_NUCLEAR_SWITCHGEAR_LEGAL_DELAY_4B": {
    "customer_delivery_margin_bridge": 2,
    "information_confidence": 3,
    "legal_delay_risk": 8,
    "market_mispricing": 3,
    "project_policy_catalyst": 7,
    "signed_scope_visibility": 2,
    "total": 26,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C04 guard:
```text
if nuclear_policy_project_attention and no_direct_signed_scope_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_or_yellow = true

if peripheral_smallcap_nuclear_price_premium and legal_project_timing_not_resolved:
    require_non_price_contract_scope_evidence = true

if post_peak_drawdown confirms:
    keep_as_counterexample_until_signed_scope_or_revision_bridge_appears = true
```

Residual errors:
```text
current_profile_error_count = 2
- 094820 / 2024-07-18: nuclear maintenance/export-project attention can be over-promoted if price confirmation substitutes for signed backlog and delivery-margin proof.
- 189860 / 2024-07-18: nuclear switchgear policy premium can become price-only when direct contract scope and revision evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -46.19, "MAE_30D_pct": -33.33, "MAE_90D_pct": -33.33, "MFE_180D_pct": 22.22, "MFE_30D_pct": 22.22, "MFE_90D_pct": 22.22, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_032820_WOORITECH_20240718_NUCLEAR_PROJECT_PERIPHERAL_4B", "case_role": "protective_smallcap_nuclear_policy_project_premium_4b_success", "company_name": "우리기술", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidates are 2003-10-28, 2005-06-07, 2007-07-03, 2007-07-31, 2009-07-29, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when nuclear-export project/policy enthusiasm was already capitalized in a peripheral control-system name but signed scope, customer allocation, delivery schedule, legal/project timing and revision evidence had not expanded enough to support the premium.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.97, "entry_date": "2024-07-18", "entry_price": 2700, "evidence_family": "nuclear_export_project_policy_peripheral_control_system_price_premium_without_signed_scope_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "SMALLCAP_NUCLEAR_PROJECT_SCOPE_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 1453, "peak_date": "2024-07-18", "peak_price": 3300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/032/032820.json", "raw_component_score_breakdown": {"customer_delivery_margin_bridge": 3, "information_confidence": 3, "legal_delay_risk": 8, "market_mispricing": 3, "project_policy_catalyst": 8, "signed_scope_visibility": 3, "total": 29, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_032820_WOORITECH_20240718_NUCLEAR_PROJECT_PERIPHERAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_project_attention", "direct_contract_scope_required", "legal_project_timing_and_delivery_visibility_required"], "stage3_evidence_fields": ["signed_scope_and_customer_allocation_required", "project_legal_delay_risk_resolution_required", "delivery_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_project_policy_price_premium", "peripheral_smallcap_theme_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_delay_or_project_scope_break", "signed_contract_conversion_gap", "delivery_margin_revision_bridge_failure"], "symbol": "032820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.9, "MAE_30D_pct": -28.96, "MAE_90D_pct": -28.96, "MFE_180D_pct": 12.02, "MFE_30D_pct": 12.02, "MFE_90D_pct": 12.02, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_EXPORT_FALSE_GREEN", "case_role": "nuclear_maintenance_project_false_green_counterexample", "company_name": "일진파워", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidates are 2011-09-08 and 2011-09-30, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Nuclear maintenance/export project attention should stay Yellow when price confirmation is not followed by signed backlog, project scope, delivery schedule, legal/project timing clarity, margin and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.45, "entry_date": "2024-07-18", "entry_price": 11980, "evidence_family": "nuclear_maintenance_export_project_attention_without_signed_backlog_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SMALLCAP_NUCLEAR_PROJECT_SCOPE_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 7320, "peak_date": "2024-07-18", "peak_price": 13420, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/094/094820.json", "raw_component_score_breakdown": {"customer_delivery_margin_bridge": 3, "information_confidence": 3, "legal_delay_risk": 7, "market_mispricing": 4, "project_policy_catalyst": 7, "signed_scope_visibility": 3, "total": 29, "valuation_rerating_runway": 2}, "reuse_reason": null, "same_entry_group_id": "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_EXPORT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_project_attention", "direct_contract_scope_required", "legal_project_timing_and_delivery_visibility_required"], "stage3_evidence_fields": ["signed_scope_and_customer_allocation_required", "project_legal_delay_risk_resolution_required", "delivery_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_project_policy_price_premium", "peripheral_smallcap_theme_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_delay_or_project_scope_break", "signed_contract_conversion_gap", "delivery_margin_revision_bridge_failure"], "symbol": "094820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -51.19, "MAE_30D_pct": -33.09, "MAE_90D_pct": -40.58, "MFE_180D_pct": 22.7, "MFE_30D_pct": 22.7, "MFE_90D_pct": 22.7, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_189860_SEOJEON_20240718_NUCLEAR_SWITCHGEAR_LEGAL_DELAY_4B", "case_role": "nuclear_switchgear_project_price_premium_counterexample", "company_name": "서전기전", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidate is 2018-11-16 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Nuclear switchgear/peripheral equipment price premium should route to local 4B or counterexample unless direct contract scope, project allocation, delivery schedule, legal timing, margin and revision evidence keep expanding after the policy spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.22, "entry_date": "2024-07-18", "entry_price": 6740, "evidence_family": "nuclear_switchgear_policy_project_price_premium_without_direct_contract_project_scope_revision", "evidence_url_pending": false, "fine_archetype_id": "SMALLCAP_NUCLEAR_PROJECT_SCOPE_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 3290, "peak_date": "2024-07-18", "peak_price": 8270, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/189/189860.json", "raw_component_score_breakdown": {"customer_delivery_margin_bridge": 2, "information_confidence": 3, "legal_delay_risk": 8, "market_mispricing": 3, "project_policy_catalyst": 7, "signed_scope_visibility": 2, "total": 26, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_189860_SEOJEON_20240718_NUCLEAR_SWITCHGEAR_LEGAL_DELAY_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_project_attention", "direct_contract_scope_required", "legal_project_timing_and_delivery_visibility_required"], "stage3_evidence_fields": ["signed_scope_and_customer_allocation_required", "project_legal_delay_risk_resolution_required", "delivery_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_project_policy_price_premium", "peripheral_smallcap_theme_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_delay_or_project_scope_break", "signed_contract_conversion_gap", "delivery_margin_revision_bridge_failure"], "symbol": "189860", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SMALLCAP_NUCLEAR_PROJECT_SCOPE_LEGAL_DELAY_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "nuclear_policy_project_legal_delay_smallcap_peripheral_contract_scope_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C04 nuclear policy/project rows should route peripheral/small-cap policy spikes to local 4B or Yellow unless direct signed contract scope, customer allocation, legal/project timing, delivery schedule, margin and revision evidence keep expanding after the price run.",
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
3. Add C04-specific nuclear policy / project-scope / legal-delay / peripheral-smallcap 4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C04_BLOCK_GREEN_WITHOUT_DIRECT_SIGNED_SCOPE_DELIVERY_MARGIN_REVISION
- C04_PERIPHERAL_NUCLEAR_POLICY_SPIKE_LOCAL_4B
- C04_REQUIRE_PROJECT_LEGAL_TIMING_AND_CUSTOMER_ALLOCATION_BRIDGE
- C04_SMALLCAP_NUCLEAR_POLICY_WITHOUT_CONTRACT_SCOPE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

