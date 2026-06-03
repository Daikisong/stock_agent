# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C04 — Nuclear policy project legal delay / Czech nuclear theme conversion-gap 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|policy_to_company_contract_conversion_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_czech_nuclear_theme_conversion_gap_2024_research.md
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

This run avoids those top-covered C04 symbols and adds 032820, 094820, and 046120.  
Each row uses a new `C04 + symbol + trigger_type + entry_date` hard key:
```text
C04 + 032820 + 4B-local-price-only + 2024-07-18
C04 + 094820 + Stage3-Yellow + 2024-07-18
C04 + 046120 + 4B-local-price-only + 2024-07-18
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
032820 우리기술: selected 2024/2025 forward window clean; corporate-action candidates are historical and latest 2009-07-29, outside selected test window.
094820 일진파워: selected 2024/2025 forward window clean; corporate-action candidates are 2011-09-08 and 2011-09-30, outside selected test window.
046120 오르비텍: selected 2024/2025 forward window clean; corporate-action candidate is 2017-06-30, outside selected test window.
```

## 3. Research thesis

C04 should distinguish a nuclear-policy project event from a listed-company earnings bridge:

```text
nuclear policy / overseas project headline
→ direct company entitlement, contract scope or signed backlog
→ project finality, legal/protest timeline and financing
→ delivery schedule and revenue recognition
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A nuclear policy headline is a reactor bell. It tells the market that a project exists, but Green should require the bell to become contract scope, delivery schedule and margin revision for the listed company.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C04_032820_WOORITECH_20240718_CZECH_NUCLEAR_POLICY_THEME_4B | 032820 | protective_czech_nuclear_policy_theme_4b_success | 2024-07-18 | 2700 | 3300 on 2024-07-18 | 1453 on 2025-04-09 | 22.22% | 22.22% | 22.22% | -46.19% | -55.97% |
| C04_094820_ILJINPOWER_20240718_CZECH_NUCLEAR_POLICY_FALSE_GREEN | 094820 | nuclear_maintenance_policy_theme_false_green_counterexample | 2024-07-18 | 11980 | 13420 on 2024-07-18 | 6900 on 2024-12-09 | 12.02% | 12.02% | 12.02% | -42.4% | -48.58% |
| C04_046120_ORBITECH_20240718_CZECH_NUCLEAR_INSPECTION_THEME_4B | 046120 | nuclear_inspection_theme_price_premium_counterexample | 2024-07-18 | 2795 | 3200 on 2024-07-18 | 1906 on 2025-01-02 | 14.49% | 14.49% | 14.49% | -31.81% | -40.44% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C04 Green should require direct project role, legal/project finality, signed contract or delivery scope, revenue recognition and margin/revision confirmation.
- 094820 is the false-Green/Yellow guard: nuclear maintenance/theme price confirmation was visible, but the company-level project-to-margin bridge was too weak for Green.

### 4B
- 032820 is the protective 4B anchor. The Czech nuclear policy event was real as a trading catalyst, but the immediate spike was not enough to prove direct company-level earnings conversion.
- 046120 shows the nuclear inspection/radiation-service version of the same failure: policy beta does not automatically create direct contract scope or margin revision.
- The core 4B rule is that policy salience must not substitute for direct entitlement, project finality, contract delivery and margin revisions.

### 4C
- No hard project cancellation, failed license, or legal rejection is asserted.
- The failure mode is policy-to-company conversion gap. Hard 4C should require clearer project failure, protest/legal loss, financing failure, contract loss or accounting break; absent that, local 4B/counterexample is the safer label.

## 6. Raw component score breakdown

```json
{
  "C04_032820_WOORITECH_20240718_CZECH_NUCLEAR_POLICY_THEME_4B": {
    "contract_delivery_scope": 2,
    "direct_project_entitlement": 2,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "nuclear_policy_event_salience": 10,
    "total": 25,
    "valuation_rerating_runway": 1
  },
  "C04_046120_ORBITECH_20240718_CZECH_NUCLEAR_INSPECTION_THEME_4B": {
    "contract_delivery_scope": 1,
    "direct_project_entitlement": 1,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "nuclear_policy_event_salience": 8,
    "total": 21,
    "valuation_rerating_runway": 1
  },
  "C04_094820_ILJINPOWER_20240718_CZECH_NUCLEAR_POLICY_FALSE_GREEN": {
    "contract_delivery_scope": 2,
    "direct_project_entitlement": 2,
    "information_confidence": 3,
    "legal_project_finality": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "nuclear_policy_event_salience": 9,
    "total": 24,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C04 guard:
```text
if nuclear_policy_event and direct_company_contract_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if nuclear_policy_theme_price_premium and no direct_entitlement_project_finality_revenue_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and policy_to_company_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 094820 / 2024-07-18: nuclear maintenance policy theme can be over-promoted if price confirmation substitutes for direct project contract and margin proof.
- 046120 / 2024-07-18: nuclear inspection/radiation-service theme can look like actionable policy leverage, but fails without contract scope and revenue/margin conversion.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -46.19, "MAE_30D_pct": -33.33, "MAE_90D_pct": -33.33, "MFE_180D_pct": 22.22, "MFE_30D_pct": 22.22, "MFE_90D_pct": 22.22, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_032820_WOORITECH_20240718_CZECH_NUCLEAR_POLICY_THEME_4B", "case_role": "protective_czech_nuclear_policy_theme_4b_success", "company_name": "우리기술", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidates are historical and latest 2009-07-29, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when the Czech nuclear policy event produced a sharp control-system/theme spike, but direct listed-company conversion evidence was not visible enough. Without direct project entitlement, signed contract, delivery scope, project finality/legal timeline and margin/revision bridge, the spike should not be promoted to Stage2 or Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.97, "entry_date": "2024-07-18", "entry_price": 2700, "evidence_family": "czech_nuclear_policy_event_theme_price_premium_without_direct_project_contract_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 1453, "peak_date": "2024-07-18", "peak_price": 3300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/032/032820.json", "raw_component_score_breakdown": {"contract_delivery_scope": 2, "direct_project_entitlement": 2, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "nuclear_policy_event_salience": 10, "total": 25, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_032820_WOORITECH_20240718_CZECH_NUCLEAR_POLICY_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_project_attention", "direct_company_entitlement_or_contract_scope_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_role_required", "legal_delay_or_project_finality_required", "contract_revenue_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_policy_theme_price_premium", "policy_salience_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "032820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -42.4, "MAE_30D_pct": -28.96, "MAE_90D_pct": -28.88, "MFE_180D_pct": 12.02, "MFE_30D_pct": 12.02, "MFE_90D_pct": 12.02, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_094820_ILJINPOWER_20240718_CZECH_NUCLEAR_POLICY_FALSE_GREEN", "case_role": "nuclear_maintenance_policy_theme_false_green_counterexample", "company_name": "일진파워", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidates are 2011-09-08 and 2011-09-30, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Nuclear maintenance/theme price confirmation should stay Yellow or local 4B when policy salience is not mapped to direct project participation, signed backlog, delivery schedule, legal/project finality and margin/revision evidence. The trigger had limited residual upside and a much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.58, "entry_date": "2024-07-18", "entry_price": 11980, "evidence_family": "nuclear_maintenance_policy_theme_price_confirmation_without_direct_project_contract_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 6900, "peak_date": "2024-07-18", "peak_price": 13420, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/094/094820.json", "raw_component_score_breakdown": {"contract_delivery_scope": 2, "direct_project_entitlement": 2, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "nuclear_policy_event_salience": 9, "total": 24, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_094820_ILJINPOWER_20240718_CZECH_NUCLEAR_POLICY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_project_attention", "direct_company_entitlement_or_contract_scope_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_role_required", "legal_delay_or_project_finality_required", "contract_revenue_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_policy_theme_price_premium", "policy_salience_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "094820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -31.81, "MAE_30D_pct": -27.01, "MAE_90D_pct": -25.22, "MFE_180D_pct": 14.49, "MFE_30D_pct": 14.49, "MFE_90D_pct": 14.49, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_046120_ORBITECH_20240718_CZECH_NUCLEAR_INSPECTION_THEME_4B", "case_role": "nuclear_inspection_theme_price_premium_counterexample", "company_name": "오르비텍", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidate is 2017-06-30 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Nuclear inspection/radiation-service theme premium should route to local 4B or counterexample unless the policy event is converted into direct contract scope, customer revenue, legal project finality and margin/revision evidence. Policy beta did not protect the forward path.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.44, "entry_date": "2024-07-18", "entry_price": 2795, "evidence_family": "nuclear_inspection_policy_theme_price_premium_without_direct_project_revenue_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-01-02", "low_price_180d": 1906, "peak_date": "2024-07-18", "peak_price": 3200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/046/046120.json", "raw_component_score_breakdown": {"contract_delivery_scope": 1, "direct_project_entitlement": 1, "information_confidence": 3, "legal_project_finality": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "nuclear_policy_event_salience": 8, "total": 21, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C04_046120_ORBITECH_20240718_CZECH_NUCLEAR_INSPECTION_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_project_attention", "direct_company_entitlement_or_contract_scope_required", "legal_project_finality_delivery_margin_revision_route"], "stage3_evidence_fields": ["direct_project_role_required", "legal_delay_or_project_finality_required", "contract_revenue_margin_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_policy_theme_price_premium", "policy_salience_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_legal_delay_or_finality_gap", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "046120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CZECH_NUCLEAR_POLICY_THEME_PROJECT_CONVERSION_GAP_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "nuclear_policy_project_legal_delay_czech_theme_conversion_gap_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C04 nuclear policy rows should block Stage2/Green when policy/project salience lacks direct company entitlement, signed contract scope, legal/project finality, delivery schedule and margin-revision bridge; theme price premiums should route to local 4B/counterexample even when the nuclear policy event itself is real.",
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
3. Add C04-specific nuclear policy / legal-project-finality / company-entitlement / contract-scope / revenue-conversion / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C04_BLOCK_GREEN_WITHOUT_DIRECT_COMPANY_CONTRACT_REVENUE_MARGIN_BRIDGE
- C04_NUCLEAR_POLICY_THEME_PRICE_PREMIUM_LOCAL_4B
- C04_REQUIRE_PROJECT_FINALITY_LEGAL_TIMELINE_CONTRACT_SCOPE_REVISION
- C04_POLICY_SALIENCE_WITHOUT_COMPANY_CONVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

