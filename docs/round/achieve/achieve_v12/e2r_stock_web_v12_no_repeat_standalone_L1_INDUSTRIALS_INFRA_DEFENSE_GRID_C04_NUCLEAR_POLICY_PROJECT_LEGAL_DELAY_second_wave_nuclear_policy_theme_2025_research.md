# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C04 — Nuclear policy project legal delay / second-wave nuclear theme conversion-gap 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: SECOND_WAVE_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD
loop_objective: coverage_gap_fill|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_gap_fill|second_wave_policy_to_company_contract_conversion_guard|local_vs_full_window_reacceleration_split|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_second_wave_nuclear_policy_theme_2025_research.md
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

This run avoids those top-covered C04 symbols and uses a new 2025 second-wave trigger family on 032820, 094820 and 046120.  
Each row uses a new `C04 + symbol + trigger_type + entry_date` hard key:
```text
C04 + 032820 + 4B-local-price-only + 2025-01-10
C04 + 094820 + Stage3-Yellow + 2025-01-10
C04 + 046120 + 4B-local-price-only + 2025-01-10
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
032820 우리기술: selected 2025 forward window clean; corporate-action candidates are historical and latest 2009-07-29, outside selected test window.
094820 일진파워: selected 2025 forward window clean; corporate-action candidates are 2011-09-08 and 2011-09-30, outside selected test window.
046120 오르비텍: selected 2025 forward window clean; corporate-action candidate is 2017-06-30, outside selected test window.
```

## 3. Research thesis

C04 should distinguish a second-wave nuclear policy theme from listed-company contract conversion:

```text
second-wave nuclear policy / project headline
→ direct company entitlement, contract scope or signed backlog
→ project finality, legal/protest timeline and financing
→ delivery schedule and revenue recognition
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A nuclear policy headline is a reactor bell. The second ring can attract more capital than the first, but Green should still require the bell to become contract scope, delivery schedule and margin revision for the listed company.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C04_032820_WOORITECH_20250110_SECOND_WAVE_NUCLEAR_CONTROL_THEME_4B | 032820 | protective_second_wave_nuclear_control_theme_4b_with_later_reacceleration_caveat | 2025-01-10 | 1836 | 5240 on 2025-07-01 | 1453 on 2025-04-09 | 29.08% | 41.34% | 185.4% | -20.86% | -34.06% |
| C04_094820_ILJINPOWER_20250110_SECOND_WAVE_NUCLEAR_MAINTENANCE_FALSE_GREEN | 094820 | second_wave_nuclear_maintenance_policy_theme_false_green_counterexample | 2025-01-10 | 8510 | 13790 on 2025-05-26 | 7320 on 2025-04-09 | 19.62% | 62.04% | 62.04% | -13.98% | -34.95% |
| C04_046120_ORBITECH_20250110_SECOND_WAVE_NUCLEAR_INSPECTION_4B | 046120 | second_wave_nuclear_inspection_policy_theme_price_premium_counterexample | 2025-01-10 | 2260 | 6570 on 2025-06-27 | 1986 on 2025-04-09 | 23.45% | 27.88% | 190.71% | -12.12% | -43.99% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C04 Green should require direct project role, legal/project finality, signed contract or delivery scope, revenue recognition and margin/revision confirmation.
- 094820 is the false-Green/Yellow guard: nuclear maintenance/theme price confirmation and later MFE were visible, but the company-level project-to-margin bridge was too weak at trigger time.
- 046120 is the service/inspection beta guard: later theme expansion does not convert the original trigger into a clean Green trigger without direct contract scope.

### 4B
- 032820 is the protective local 4B anchor. It later re-accelerated, but the initial January 2025 trigger first produced meaningful MAE and lacked direct project entitlement and margin proof.
- 094820 and 046120 show that a second-wave policy rally can be real and still remain local 4B/Yellow at entry because the evidence bridge is policy-to-company, not price-to-price.
- The core 4B rule is that later full-window recovery should not erase weak trigger-quality when the initial row is price/theme-driven.

### 4C
- No hard project cancellation, failed license, or legal rejection is asserted.
- The failure mode is policy-to-company conversion gap. Hard 4C should require clearer project failure, protest/legal loss, financing failure, contract loss or accounting break; absent that, local 4B/counterexample is the safer label.

## 6. Raw component score breakdown

```json
{
  "C04_032820_WOORITECH_20250110_SECOND_WAVE_NUCLEAR_CONTROL_THEME_4B": {
    "contract_delivery_scope": 2,
    "direct_project_entitlement": 2,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "nuclear_policy_event_salience": 9,
    "total": 25,
    "valuation_rerating_runway": 2
  },
  "C04_046120_ORBITECH_20250110_SECOND_WAVE_NUCLEAR_INSPECTION_4B": {
    "contract_delivery_scope": 1,
    "direct_project_entitlement": 1,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "nuclear_policy_event_salience": 8,
    "total": 23,
    "valuation_rerating_runway": 2
  },
  "C04_094820_ILJINPOWER_20250110_SECOND_WAVE_NUCLEAR_MAINTENANCE_FALSE_GREEN": {
    "contract_delivery_scope": 2,
    "direct_project_entitlement": 2,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "nuclear_policy_event_salience": 9,
    "total": 25,
    "valuation_rerating_runway": 2
  }
}
```

## 7. Current calibrated profile stress test

Suggested C04 guard:
```text
if second_wave_nuclear_policy_event and direct_company_contract_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if second_wave_nuclear_theme_price_premium and no direct_entitlement_project_finality_revenue_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if later_full_window_reacceleration and original_trigger_lacked_contract_bridge:
    preserve_original_yellow_or_4B_label = true
    do_not_relabel_as_clean_stage2_green = true
```

Residual errors:
```text
current_profile_error_count = 2
- 094820 / 2025-01-10: second-wave nuclear maintenance theme can be over-promoted if later price continuation substitutes for direct project contract and margin proof.
- 046120 / 2025-01-10: nuclear inspection/radiation-service theme can look actionable after later reacceleration, but fails the original trigger-evidence test without contract scope and revenue/margin conversion.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -20.86, "MAE_30D_pct": -0.27, "MAE_90D_pct": -20.86, "MFE_180D_pct": 185.4, "MFE_30D_pct": 29.08, "MFE_90D_pct": 41.34, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_032820_WOORITECH_20250110_SECOND_WAVE_NUCLEAR_CONTROL_THEME_4B", "case_role": "protective_second_wave_nuclear_control_theme_4b_with_later_reacceleration_caveat", "company_name": "우리기술", "corporate_action_window_status": "clean_2025_forward_window; corporate-action candidates are historical and latest 2009-07-29, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B/Yellow discipline was useful on the January 2025 second-wave nuclear policy/control-system theme: the stock later re-accelerated, but the trigger first suffered a material local drawdown and did not carry direct project entitlement, signed contract scope, legal finality, delivery schedule and margin/revision proof at entry. This row should preserve local 4B versus full-window recovery split.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.06, "entry_date": "2025-01-10", "entry_price": 1836, "evidence_family": "second_wave_nuclear_policy_control_system_theme_price_premium_without_direct_project_contract_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 1453, "peak_date": "2025-07-01", "peak_price": 5240, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/032/032820.json", "raw_component_score_breakdown": {"contract_delivery_scope": 2, "direct_project_entitlement": 2, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "nuclear_policy_event_salience": 9, "total": 25, "valuation_rerating_runway": 2}, "reuse_reason": null, "same_entry_group_id": "C04_032820_WOORITECH_20250110_SECOND_WAVE_NUCLEAR_CONTROL_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_nuclear_policy_project_attention", "direct_company_entitlement_or_contract_scope_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_role_required", "legal_delay_or_project_finality_required", "contract_revenue_margin_revision_bridge_required"], "stage4b_evidence_fields": ["second_wave_nuclear_policy_theme_price_premium", "policy_salience_already_capitalized", "local_vs_full_window_reacceleration_split"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "032820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2025.csv", "trigger_date": "2025-01-10", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -13.98, "MAE_30D_pct": -0.82, "MAE_90D_pct": -13.98, "MFE_180D_pct": 62.04, "MFE_30D_pct": 19.62, "MFE_90D_pct": 62.04, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_094820_ILJINPOWER_20250110_SECOND_WAVE_NUCLEAR_MAINTENANCE_FALSE_GREEN", "case_role": "second_wave_nuclear_maintenance_policy_theme_false_green_counterexample", "company_name": "일진파워", "corporate_action_window_status": "clean_2025_forward_window; corporate-action candidates are 2011-09-08 and 2011-09-30, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Second-wave nuclear maintenance/theme price confirmation should remain Yellow unless the policy event is mapped to direct project participation, contract backlog, delivery scope, legal/project finality and margin/revision evidence. The later rally does not remove the need for a contract-to-margin bridge at trigger time.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.95, "entry_date": "2025-01-10", "entry_price": 8510, "evidence_family": "second_wave_nuclear_maintenance_theme_price_confirmation_without_direct_project_contract_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 7320, "peak_date": "2025-05-26", "peak_price": 13790, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/094/094820.json", "raw_component_score_breakdown": {"contract_delivery_scope": 2, "direct_project_entitlement": 2, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "nuclear_policy_event_salience": 9, "total": 25, "valuation_rerating_runway": 2}, "reuse_reason": null, "same_entry_group_id": "C04_094820_ILJINPOWER_20250110_SECOND_WAVE_NUCLEAR_MAINTENANCE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_nuclear_policy_project_attention", "direct_company_entitlement_or_contract_scope_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_role_required", "legal_delay_or_project_finality_required", "contract_revenue_margin_revision_bridge_required"], "stage4b_evidence_fields": ["second_wave_nuclear_policy_theme_price_premium", "policy_salience_already_capitalized", "local_vs_full_window_reacceleration_split"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "094820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2025.csv", "trigger_date": "2025-01-10", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -12.12, "MAE_30D_pct": -10.18, "MAE_90D_pct": -12.12, "MFE_180D_pct": 190.71, "MFE_30D_pct": 23.45, "MFE_90D_pct": 27.88, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_046120_ORBITECH_20250110_SECOND_WAVE_NUCLEAR_INSPECTION_4B", "case_role": "second_wave_nuclear_inspection_policy_theme_price_premium_counterexample", "company_name": "오르비텍", "corporate_action_window_status": "clean_2025_forward_window; corporate-action candidate is 2017-06-30 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Second-wave nuclear inspection/radiation-service premium should route to local 4B or counterexample unless policy salience becomes direct contract scope, customer revenue, legal project finality and margin/revision evidence. The high full-window MFE required a later theme expansion, not a clean Green trigger at entry.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.99, "entry_date": "2025-01-10", "entry_price": 2260, "evidence_family": "second_wave_nuclear_inspection_policy_theme_price_premium_without_direct_project_revenue_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 1986, "peak_date": "2025-06-27", "peak_price": 6570, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/046/046120.json", "raw_component_score_breakdown": {"contract_delivery_scope": 1, "direct_project_entitlement": 1, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "nuclear_policy_event_salience": 8, "total": 23, "valuation_rerating_runway": 2}, "reuse_reason": null, "same_entry_group_id": "C04_046120_ORBITECH_20250110_SECOND_WAVE_NUCLEAR_INSPECTION_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_nuclear_policy_project_attention", "direct_company_entitlement_or_contract_scope_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_role_required", "legal_delay_or_project_finality_required", "contract_revenue_margin_revision_bridge_required"], "stage4b_evidence_fields": ["second_wave_nuclear_policy_theme_price_premium", "policy_salience_already_capitalized", "local_vs_full_window_reacceleration_split"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "046120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2025.csv", "trigger_date": "2025-01-10", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SECOND_WAVE_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "nuclear_policy_project_legal_delay_second_wave_theme_conversion_gap_2025",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C04 second-wave nuclear policy rows should preserve local 4B/Yellow discipline unless policy salience converts into direct company entitlement, signed contract scope, project/legal finality, delivery schedule and margin-revision evidence. Later full-window reacceleration must not retroactively relabel a price-only trigger as clean Stage2/Green.",
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
3. Preserve local 4B/Yellow trigger-quality even when later full-window reacceleration occurs.
4. Add C04-specific second-wave nuclear policy / legal-project-finality / company-entitlement / contract-scope / revenue-conversion / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C04_BLOCK_GREEN_WITHOUT_DIRECT_COMPANY_CONTRACT_REVENUE_MARGIN_BRIDGE
- C04_SECOND_WAVE_NUCLEAR_POLICY_THEME_PRICE_PREMIUM_LOCAL_4B
- C04_REQUIRE_PROJECT_FINALITY_LEGAL_TIMELINE_CONTRACT_SCOPE_REVISION
- C04_LATER_FULL_WINDOW_REACCELERATION_DOES_NOT_REWRITE_WEAK_TRIGGER_QUALITY

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

