# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C04 — Nuclear policy project legal-delay guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_SMALLCAP_PROJECT_CONTRACT_LEGAL_DELAY_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_nuclear_smallcap_project_delay_2024_research.md
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

This run avoids those top-covered C04 symbols and adds 032820, 105840, and 094820.  
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
032820 우리기술: 2024 forward window clean; corporate-action candidates are old, outside the test window.
105840 우진: 2024 forward window clean; corporate-action candidates are old, outside the test window.
094820 일진파워: 2024 forward window clean; corporate-action candidates are old, outside the test window.
```

## 3. Research thesis

C04 should not be a generic nuclear-policy momentum bucket. It should test whether a policy/project headline actually becomes company-level economic evidence:

```text
nuclear policy / preferred-bidder / project headline
→ legal finality and contract conversion
→ company-level scope and delivery schedule
→ margin and revision bridge
→ rerating
```

The failure mode is subtle. A policy headline is a bright flare, but a company only earns money when the flare becomes a contract, a scope table, a delivery schedule, and a margin line. Without that, the market is buying the glow rather than the grid connection.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C04_032820_WOORITECH_20240718_NUCLEAR_PROJECT_PREMIUM_LOCAL_4B | 032820 | protective_4b_success | 2024-07-18 | 2700 | 3300 on 2024-07-18 | 1621 on 2024-12-30 | 22.22% | 22.22% | 22.22% | -39.96% | -50.88% |
| C04_105840_WOOJIN_20240718_NUCLEAR_INSTRUMENTATION_PROJECT_DELAY_FALSE_GREEN | 105840 | nuclear_project_false_green_counterexample | 2024-07-18 | 9300 | 10950 on 2024-07-18 | 5630 on 2024-12-09 | 17.74% | 17.74% | 17.74% | -39.46% | -48.58% |
| C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_PROJECT_DELAY_FALSE_GREEN | 094820 | maintenance_service_project_false_green_counterexample | 2024-07-18 | 11980 | 13420 on 2024-07-18 | 6900 on 2024-12-09 | 12.02% | 12.02% | 12.02% | -42.4% | -48.58% |

## 5. Stage evidence split

### Stage2 / Stage3
- Nuclear policy/project attention is a valid research route.
- It is not a Green signal unless the evidence moves from national project headline to company-level contract conversion, legal finality, schedule, scope, margin and revision.

### Stage3 / Green
- C04 Green should require explicit company-level order or service scope.
- 105840 and 094820 are false-Green guards: instrumentation or maintenance/service adjacency can be real, but adjacency without scope and revision is not enough.

### 4B
- 032820 is the protective 4B anchor. The policy/project premium expanded violently on the event, then gave back most of the move.
- Local 4B should activate when price capitalizes project optionality before legal and contract evidence reaches the company P&L.

### 4C
- No hard 4C/legal-break row is asserted here.
- The break mode is legal/project conversion gap: the project story remains alive, but company-level revenue conversion does not arrive quickly enough to support the valuation.

## 6. Raw component score breakdown

```json
{
  "C04_032820_WOORITECH_20240718_NUCLEAR_PROJECT_PREMIUM_LOCAL_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_PROJECT_DELAY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C04_105840_WOOJIN_20240718_NUCLEAR_INSTRUMENTATION_PROJECT_DELAY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C04 guard:
```text
if nuclear_policy_project_headline and no company_level_contract_scope_schedule_margin_revision_bridge:
    cap_stage = Stage3-Yellow
    block_stage3_green = true

if nuclear_smallcap_policy_premium and no incremental_non_price_contract_conversion:
    route_to_local_4B_watch = true

if legal_delay_or_contract_scope_gap persists after project headline:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 105840 / 2024-07-18: instrumentation exposure can be over-promoted if the model treats nuclear-project policy heat as company-level order evidence.
- 094820 / 2024-07-18: maintenance/service adjacency can look like Green, but the later path argues for Yellow/local 4B unless contract scope and margin bridge are visible.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -39.96, "MAE_30D_pct": -33.33, "MAE_90D_pct": -33.33, "MFE_180D_pct": 22.22, "MFE_30D_pct": 22.22, "MFE_90D_pct": 22.22, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_032820_WOORITECH_20240718_NUCLEAR_PROJECT_PREMIUM_LOCAL_4B", "case_role": "protective_4b_success", "company_name": "우리기술", "corporate_action_window_status": "clean_2024_forward_window; old corporate-action candidates outside test window where present", "current_profile_error": false, "current_profile_verdict": "Local 4B was the useful signal after the nuclear project/policy premium had been capitalized; fresh Green should require company-level contract, legal finality, delivery scope, margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.88, "entry_date": "2024-07-18", "entry_price": 2700, "evidence_family": "nuclear_policy_project_preferred_bidder_price_premium_without_company_level_contract_conversion", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_PROJECT_CONTRACT_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-30", "low_price_180d": 1621, "peak_date": "2024-07-18", "peak_price": 3300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/032/032820.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C04_032820_WOORITECH_20240718_NUCLEAR_PROJECT_PREMIUM_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_attention", "preferred_bidder_or_project_award_route", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["company_level_contract_conversion_required", "legal_finality_and_project_schedule_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_project_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_delay_or_contract_scope_gap", "project_schedule_delay", "policy_headline_without_company_level_revenue_conversion"], "symbol": "032820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.46, "MAE_30D_pct": -23.44, "MAE_90D_pct": -23.44, "MFE_180D_pct": 17.74, "MFE_30D_pct": 17.74, "MFE_90D_pct": 17.74, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_105840_WOOJIN_20240718_NUCLEAR_INSTRUMENTATION_PROJECT_DELAY_FALSE_GREEN", "case_role": "nuclear_project_false_green_counterexample", "company_name": "우진", "corporate_action_window_status": "clean_2024_forward_window; old corporate-action candidates outside test window where present", "current_profile_error": true, "current_profile_verdict": "Nuclear instrumentation exposure should stay Yellow if the stock only has policy/project adjacency and lacks explicit order scope, contract schedule, margin and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.58, "entry_date": "2024-07-18", "entry_price": 9300, "evidence_family": "nuclear_instrumentation_policy_project_attention_without_order_scope_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_PROJECT_CONTRACT_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 5630, "peak_date": "2024-07-18", "peak_price": 10950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/105/105840.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C04_105840_WOOJIN_20240718_NUCLEAR_INSTRUMENTATION_PROJECT_DELAY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_attention", "preferred_bidder_or_project_award_route", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["company_level_contract_conversion_required", "legal_finality_and_project_schedule_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_project_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_delay_or_contract_scope_gap", "project_schedule_delay", "policy_headline_without_company_level_revenue_conversion"], "symbol": "105840", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -42.4, "MAE_30D_pct": -28.96, "MAE_90D_pct": -28.96, "MFE_180D_pct": 12.02, "MFE_30D_pct": 12.02, "MFE_90D_pct": 12.02, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_PROJECT_DELAY_FALSE_GREEN", "case_role": "maintenance_service_project_false_green_counterexample", "company_name": "일진파워", "corporate_action_window_status": "clean_2024_forward_window; old corporate-action candidates outside test window where present", "current_profile_error": true, "current_profile_verdict": "Nuclear maintenance/service names should not be promoted to Green unless project contract conversion, service scope, margin capture and revision bridge are explicit.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.58, "entry_date": "2024-07-18", "entry_price": 11980, "evidence_family": "nuclear_maintenance_service_policy_premium_without_contract_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_PROJECT_CONTRACT_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 6900, "peak_date": "2024-07-18", "peak_price": 13420, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/094/094820.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C04_094820_ILJINPOWER_20240718_NUCLEAR_MAINTENANCE_PROJECT_DELAY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_attention", "preferred_bidder_or_project_award_route", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["company_level_contract_conversion_required", "legal_finality_and_project_schedule_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["nuclear_project_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_delay_or_contract_scope_gap", "project_schedule_delay", "policy_headline_without_company_level_revenue_conversion"], "symbol": "094820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "NUCLEAR_SMALLCAP_PROJECT_CONTRACT_LEGAL_DELAY_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "nuclear_policy_project_smallcap_4b_false_green_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C04 nuclear-policy/project rows should cap at Stage3-Yellow or route to local 4B unless company-level contract conversion, legal finality, project schedule, scope, margin and revision bridge are explicit; preferred-bidder/project headlines alone should not become Green.",
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
3. Add C04-specific nuclear project / legal finality / contract-scope guard only as a shadow candidate until more rows exist.

Candidate rule:
- C04_GREEN_REQUIRES_COMPANY_LEVEL_CONTRACT_SCOPE_SCHEDULE_MARGIN_REVISION
- C04_NUCLEAR_POLICY_PROJECT_HEADLINE_STAGE3_CAP
- C04_NUCLEAR_SMALLCAP_PROJECT_PREMIUM_LOCAL_4B
- C04_LEGAL_DELAY_OR_SCOPE_GAP_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

