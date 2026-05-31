# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C04 — Nuclear policy project legal-delay / second-wave nuclear policy 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: SECOND_WAVE_NUCLEAR_POLICY_PROJECT_4B_GUARD
loop_objective: coverage_gap_fill|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_refresh_second_wave_policy_premium|policy_to_contract_conversion_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_second_wave_nuclear_policy_4b_2024_research.md
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

This run uses a new second-wave trigger family for 006910, 032820 and 105840.  
Each row uses a new `C04 + symbol + trigger_type + entry_date` hard key:
```text
C04 + 006910 + 4B-local-price-only + 2024-09-12
C04 + 032820 + Stage3-Yellow + 2024-09-12
C04 + 105840 + 4B-local-price-only + 2024-09-12
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
006910 보성파워텍: selected 2024 forward window clean; corporate-action candidates are historical and latest 2016-08-29, outside selected test window.
032820 우리기술: selected 2024 forward window clean; corporate-action candidates are historical and latest 2009-07-29, outside selected test window.
105840 우진: selected 2024 forward window clean; corporate-action candidates are 2012-11-19 and 2012-12-11, outside selected test window.
```

## 3. Research thesis

C04 should not treat a repeated nuclear policy rally as a fresh project-level orderbook. It should test whether the policy headline becomes signed supplier allocation, legal finality and margin:

```text
second-wave nuclear policy / project award attention
→ direct supplier allocation or signed contract
→ legal finality, financing and project schedule
→ delivery schedule and revenue-recognition path
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A second policy rally is a second flash on the grid. Green should require the wire into the company: named allocation, signed order, final project gate, delivery date and margin invoice.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C04_006910_BOSUNG_20240912_NUCLEAR_POLICY_SECOND_WAVE_4B | 006910 | protective_second_wave_nuclear_policy_theme_4b_success | 2024-09-12 | 3580 | 3885 on 2024-09-13 | 2290 on 2024-12-09 | 8.52% | 8.52% | 8.52% | -36.03% | -41.06% |
| C04_032820_WOORITECH_20240912_NUCLEAR_CONTROL_SYSTEM_FALSE_GREEN | 032820 | second_wave_nuclear_control_system_false_green_counterexample | 2024-09-12 | 2335 | 2570 on 2024-09-13 | 1650 on 2024-12-09 | 10.06% | 10.06% | 10.06% | -29.34% | -35.8% |
| C04_105840_WOOJIN_20240912_NUCLEAR_INSTRUMENTATION_SECOND_WAVE_4B | 105840 | nuclear_instrumentation_second_wave_price_premium_counterexample | 2024-09-12 | 8130 | 8230 on 2024-09-13 | 5630 on 2024-12-09 | 1.23% | 1.23% | 1.23% | -30.75% | -31.59% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C04 Green should require direct supplier allocation or signed contract, legal/project finality, financing clarity, delivery schedule, revenue recognition and margin/revision confirmation.
- 032820 is the false-Green/Yellow guard: control-system policy salience and price confirmation did not protect the forward path once direct order and delivery-margin evidence failed to refresh.

### 4B
- 006910 is the protective 4B anchor. The September second-wave policy spike was real as a trading event, but it needed direct project conversion evidence to remain actionable.
- 105840 is the nuclear instrumentation price-premium counterexample. The trigger produced little durable additional MFE and then a much larger MAE once direct contract and project-finality evidence did not refresh.
- The key rule is that repeated nuclear policy salience must not be substituted for supplier allocation, signed order, delivery schedule and margin revisions.

### 4C
- No hard project cancellation, legal rejection or contract loss is asserted.
- The failure mode is policy-to-company conversion gap: the project headline can remain important while listed small-cap themes fail to convert it into direct, margin-accretive backlog.

## 6. Raw component score breakdown

```json
{
  "C04_006910_BOSUNG_20240912_NUCLEAR_POLICY_SECOND_WAVE_4B": {
    "direct_contract_visibility": 2,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "policy_project_catalyst": 8,
    "supplier_allocation_delivery_bridge": 2,
    "total": 24,
    "valuation_rerating_runway": 1
  },
  "C04_032820_WOORITECH_20240912_NUCLEAR_CONTROL_SYSTEM_FALSE_GREEN": {
    "direct_contract_visibility": 2,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "policy_project_catalyst": 8,
    "supplier_allocation_delivery_bridge": 2,
    "total": 25,
    "valuation_rerating_runway": 1
  },
  "C04_105840_WOOJIN_20240912_NUCLEAR_INSTRUMENTATION_SECOND_WAVE_4B": {
    "direct_contract_visibility": 2,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "policy_project_catalyst": 7,
    "supplier_allocation_delivery_bridge": 2,
    "total": 23,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C04 guard:
```text
if nuclear_policy_project_attention and direct_supplier_allocation_contract_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if second_wave_nuclear_policy_theme_price_premium and no direct_contract_legal_finality_delivery_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and policy_to_company_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 032820 / 2024-09-12: second-wave nuclear policy confirmation can be over-promoted if price action substitutes for supplier allocation, delivery schedule and margin proof.
- 105840 / 2024-09-12: nuclear instrumentation second-wave premium can become price-only when direct contract and project-finality evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -36.03, "MAE_30D_pct": -17.6, "MAE_90D_pct": -36.03, "MFE_180D_pct": 8.52, "MFE_30D_pct": 8.52, "MFE_90D_pct": 8.52, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_006910_BOSUNG_20240912_NUCLEAR_POLICY_SECOND_WAVE_4B", "case_role": "protective_second_wave_nuclear_policy_theme_4b_success", "company_name": "보성파워텍", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and latest 2016-08-29, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B remained useful on the second-wave nuclear policy/theme rally. The stock could spike again, but without direct supplier allocation, signed contract, legal/project finality, delivery schedule, revenue-recognition path and margin/revision bridge, the premium was not a clean Stage2/Green positive.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.06, "entry_date": "2024-09-12", "entry_price": 3580, "evidence_family": "second_wave_nuclear_policy_theme_price_premium_without_direct_supplier_contract_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_NUCLEAR_POLICY_PROJECT_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 2290, "peak_date": "2024-09-13", "peak_price": 3885, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006910.json", "raw_component_score_breakdown": {"direct_contract_visibility": 2, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "policy_project_catalyst": 8, "supplier_allocation_delivery_bridge": 2, "total": 24, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_006910_BOSUNG_20240912_NUCLEAR_POLICY_SECOND_WAVE_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_nuclear_policy_project_attention", "direct_supplier_allocation_or_signed_contract_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_contract_or_supplier_allocation_required", "legal_finality_and_financing_required", "delivery_schedule_revenue_recognition_margin_revision_required"], "stage4b_evidence_fields": ["second_wave_nuclear_policy_project_theme_price_premium", "policy_theme_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "supplier_allocation_or_contract_absence", "margin_revision_bridge_failure"], "symbol": "006910", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv", "trigger_date": "2024-09-12", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -29.34, "MAE_30D_pct": -8.14, "MAE_90D_pct": -29.34, "MFE_180D_pct": 10.06, "MFE_30D_pct": 10.06, "MFE_90D_pct": 10.06, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_032820_WOORITECH_20240912_NUCLEAR_CONTROL_SYSTEM_FALSE_GREEN", "case_role": "second_wave_nuclear_control_system_false_green_counterexample", "company_name": "우리기술", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and latest 2009-07-29, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Nuclear control-system price confirmation should stay Yellow when the second-wave policy rally lacks direct project order, supplier allocation, legal/project finality, delivery cadence and margin/revision evidence. Price confirmation alone did not prevent the later drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -35.8, "entry_date": "2024-09-12", "entry_price": 2335, "evidence_family": "second_wave_nuclear_control_system_price_confirmation_without_supplier_allocation_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_NUCLEAR_POLICY_PROJECT_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 1650, "peak_date": "2024-09-13", "peak_price": 2570, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/032/032820.json", "raw_component_score_breakdown": {"direct_contract_visibility": 2, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "policy_project_catalyst": 8, "supplier_allocation_delivery_bridge": 2, "total": 25, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_032820_WOORITECH_20240912_NUCLEAR_CONTROL_SYSTEM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_nuclear_policy_project_attention", "direct_supplier_allocation_or_signed_contract_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_contract_or_supplier_allocation_required", "legal_finality_and_financing_required", "delivery_schedule_revenue_recognition_margin_revision_required"], "stage4b_evidence_fields": ["second_wave_nuclear_policy_project_theme_price_premium", "policy_theme_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "supplier_allocation_or_contract_absence", "margin_revision_bridge_failure"], "symbol": "032820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv", "trigger_date": "2024-09-12", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -30.75, "MAE_30D_pct": -6.77, "MAE_90D_pct": -30.75, "MFE_180D_pct": 1.23, "MFE_30D_pct": 1.23, "MFE_90D_pct": 1.23, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_105840_WOOJIN_20240912_NUCLEAR_INSTRUMENTATION_SECOND_WAVE_4B", "case_role": "nuclear_instrumentation_second_wave_price_premium_counterexample", "company_name": "우진", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2012-11-19 and 2012-12-11, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Nuclear instrumentation second-wave policy premium should route to local 4B or counterexample unless direct project participation, signed order, legal finality, delivery schedule, revenue-recognition path and margin/revision evidence refresh after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.59, "entry_date": "2024-09-12", "entry_price": 8130, "evidence_family": "second_wave_nuclear_instrumentation_policy_premium_without_direct_contract_delivery_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_NUCLEAR_POLICY_PROJECT_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 5630, "peak_date": "2024-09-13", "peak_price": 8230, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/105/105840.json", "raw_component_score_breakdown": {"direct_contract_visibility": 2, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "policy_project_catalyst": 7, "supplier_allocation_delivery_bridge": 2, "total": 23, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_105840_WOOJIN_20240912_NUCLEAR_INSTRUMENTATION_SECOND_WAVE_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_nuclear_policy_project_attention", "direct_supplier_allocation_or_signed_contract_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_contract_or_supplier_allocation_required", "legal_finality_and_financing_required", "delivery_schedule_revenue_recognition_margin_revision_required"], "stage4b_evidence_fields": ["second_wave_nuclear_policy_project_theme_price_premium", "policy_theme_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "supplier_allocation_or_contract_absence", "margin_revision_bridge_failure"], "symbol": "105840", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv", "trigger_date": "2024-09-12", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SECOND_WAVE_NUCLEAR_POLICY_PROJECT_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "nuclear_policy_project_second_wave_theme_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C04 nuclear policy/project rows should block Stage3 Green when a second-wave policy/project rally lacks direct supplier allocation, signed contract, legal finality, delivery schedule, revenue-recognition path and margin/revision bridge; second-wave nuclear theme price premiums should route to local 4B or counterexample unless non-price conversion evidence refreshes.",
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
3. Add C04-specific second-wave nuclear policy/project / direct supplier allocation / legal finality / delivery-margin / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C04_BLOCK_GREEN_WITHOUT_DIRECT_SUPPLIER_CONTRACT_DELIVERY_MARGIN_BRIDGE
- C04_SECOND_WAVE_NUCLEAR_POLICY_THEME_PRICE_PREMIUM_LOCAL_4B
- C04_REQUIRE_LEGAL_FINALITY_FINANCING_REVENUE_RECOGNITION_REVISION
- C04_REPEATED_POLICY_SALIENCE_WITHOUT_COMPANY_BACKLOG_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

