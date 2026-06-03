# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C04 — Nuclear policy project legal-delay guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_SMALLCAP_EVENT_PREMIUM_LEGAL_DELAY_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_nuclear_smallcap_event_premium_2024_research.md
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

This run avoids those top-covered C04 symbols and adds 105840, 094820, and 032820.  
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
105840 우진: 2024/2025 forward window clean; corporate-action candidates are 2012-11-19 and 2012-12-11.
094820 일진파워: 2024/2025 forward window clean; corporate-action candidates are 2011-09-08 and 2011-09-30.
032820 우리기술: 2024/2025 forward window clean; corporate-action candidates are old, outside the test window.
```

## 3. Research thesis

C04 is not a generic nuclear-theme bucket. It is a policy-project and legal-delay guard:

```text
nuclear export / preferred-bidder / project event
→ event premium and relative strength
→ final contract, legal clarity, company-specific scope, and margin bridge must close
→ otherwise price spike should become Yellow/local 4B, not Green
```

The useful residual is the shape of the small-cap nuclear basket. It can jump like a spring when the policy event hits, but without a contract/revision bridge the spring snaps back into a deep drawdown path.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C04_105840_WOOJIN_20240717_NUCLEAR_POLICY_EVENT_PREMIUM_FADE | 105840 | nuclear_policy_false_green_counterexample | 2024-07-17 | 9490 | 10950 on 2024-07-18 | 6000 on 2025-04-09 | 15.38% | 15.38% | 15.38% | -36.78% | -45.21% |
| C04_094820_ILJINPOWER_20240717_NUCLEAR_EVENT_PREMIUM_LOCAL_4B | 094820 | local_4b_guard_success | 2024-07-17 | 12010 | 13420 on 2024-07-18 | 7320 on 2025-04-09 | 11.74% | 11.74% | 11.74% | -39.05% | -45.45% |
| C04_032820_WOORITECH_20240717_NUCLEAR_POLICY_PRICE_ONLY_BLOWOFF | 032820 | price_only_event_blowoff_counterexample | 2024-07-17 | 2645 | 3300 on 2024-07-18 | 1453 on 2025-04-09 | 24.76% | 24.76% | 24.76% | -45.07% | -55.97% |

## 5. Stage evidence split

### Stage2 / Stage2-EventPremium
- Nuclear export/project headlines and preferred-bidder attention can create a valid research route.
- The price path confirms that the market noticed the event: all three names produced immediate event-premium spikes.

### Stage3 / Green
- C04 Green should require final contract, legal clarity, company-specific scope, and margin/revision bridge.
- The selected rows do not close that bridge. They therefore should not be used as positive Green evidence.

### 4B
- The spike-and-fade pattern is the main lesson.
- 094820 is counted as the positive guard case because local 4B / legal-delay discipline would have protected after the event premium.

### 4C
- These rows are not hard accounting-break rows.
- The failure mode is event-premium mean reversion: the policy story remained real at the sector level, but the company-level earnings route stayed too thin.

## 6. Raw component score breakdown

```json
{
  "C04_032820_WOORITECH_20240717_NUCLEAR_POLICY_PRICE_ONLY_BLOWOFF": {
    "bottleneck_pricing_power": 4,
    "capital_allocation": 1,
    "eps_fcf_explosion": 3,
    "information_confidence": 2,
    "market_mispricing": 5,
    "total": 21,
    "valuation_rerating_runway": 3,
    "visibility_quality": 3
  },
  "C04_094820_ILJINPOWER_20240717_NUCLEAR_EVENT_PREMIUM_LOCAL_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 7,
    "total": 29,
    "valuation_rerating_runway": 4,
    "visibility_quality": 5
  },
  "C04_105840_WOOJIN_20240717_NUCLEAR_POLICY_EVENT_PREMIUM_FADE": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 27,
    "valuation_rerating_runway": 4,
    "visibility_quality": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C04 guard:
```text
if nuclear_policy_project_event and no final_contract_or_legal_clarity:
    cap_stage = Stage2-EventPremium or Stage3-Yellow
    block_stage3_green = true

if smallcap_nuclear_event_premium_spike and no company_specific_scope_award:
    route_to_local_4B_watch = true

if post_event_drawdown and no margin_revision_bridge:
    keep_as_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 105840 / 2024-07-17: small-cap nuclear event premium can be over-promoted if final contract/legal clarity is not required.
- 032820 / 2024-07-17: price-only nuclear policy blowoff should be local 4B/counterexample, not positive Green evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -36.78, "MAE_30D_pct": -24.97, "MAE_90D_pct": -24.97, "MFE_180D_pct": 15.38, "MFE_30D_pct": 15.38, "MFE_90D_pct": 15.38, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_105840_WOOJIN_20240717_NUCLEAR_POLICY_EVENT_PREMIUM_FADE", "case_role": "nuclear_policy_false_green_counterexample", "company_name": "우진", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Nuclear event premium should stay Yellow or local 4B unless project-specific contract, final legal clarity, and margin bridge close.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.21, "entry_date": "2024-07-17", "entry_price": 9490, "evidence_family": "nuclear_policy_project_event_premium_without_contract_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_EVENT_PREMIUM_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 6000, "peak_date": "2024-07-18", "peak_price": 10950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/105/105840.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 6, "total": 27, "valuation_rerating_runway": 4, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C04_105840_WOOJIN_20240717_NUCLEAR_POLICY_EVENT_PREMIUM_FADE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_event_premium", "preferred_bidder_or_export_project_attention", "relative_strength_before_final_contract"], "stage3_evidence_fields": ["final_contract_and_legal_clarity_required", "company_specific_scope_award_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["event_premium_spike", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_or_final_contract_delay", "no_company_specific_award_conversion", "event_premium_mean_reversion"], "symbol": "105840", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv", "trigger_date": "2024-07-17", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.05, "MAE_30D_pct": -29.14, "MAE_90D_pct": -29.14, "MFE_180D_pct": 11.74, "MFE_30D_pct": 11.74, "MFE_90D_pct": 11.74, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_094820_ILJINPOWER_20240717_NUCLEAR_EVENT_PREMIUM_LOCAL_4B", "case_role": "local_4b_guard_success", "company_name": "일진파워", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "The useful signal is not fresh Green; local 4B/legal-delay guard protects after the event premium spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.45, "entry_date": "2024-07-17", "entry_price": 12010, "evidence_family": "nuclear_smallcap_event_spike_legal_delay_local_4b_guard", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_EVENT_PREMIUM_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 7320, "peak_date": "2024-07-18", "peak_price": 13420, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/094/094820.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 7, "total": 29, "valuation_rerating_runway": 4, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C04_094820_ILJINPOWER_20240717_NUCLEAR_EVENT_PREMIUM_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_event_premium", "preferred_bidder_or_export_project_attention", "relative_strength_before_final_contract"], "stage3_evidence_fields": ["final_contract_and_legal_clarity_required", "company_specific_scope_award_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["event_premium_spike", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_or_final_contract_delay", "no_company_specific_award_conversion", "event_premium_mean_reversion"], "symbol": "094820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv", "trigger_date": "2024-07-17", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.07, "MAE_30D_pct": -31.95, "MAE_90D_pct": -31.95, "MFE_180D_pct": 24.76, "MFE_30D_pct": 24.76, "MFE_90D_pct": 24.76, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_032820_WOORITECH_20240717_NUCLEAR_POLICY_PRICE_ONLY_BLOWOFF", "case_role": "price_only_event_blowoff_counterexample", "company_name": "우리기술", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Price-only nuclear policy spike should be a 4B/counterexample row, not positive Stage2-to-Green evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.97, "entry_date": "2024-07-17", "entry_price": 2645, "evidence_family": "nuclear_control_system_policy_theme_price_only_without_award_conversion", "evidence_url_pending": false, "fine_archetype_id": "NUCLEAR_SMALLCAP_EVENT_PREMIUM_LEGAL_DELAY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2025-04-09", "low_price_180d": 1453, "peak_date": "2024-07-18", "peak_price": 3300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/032/032820.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 1, "eps_fcf_explosion": 3, "information_confidence": 2, "market_mispricing": 5, "total": 21, "valuation_rerating_runway": 3, "visibility_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C04_032820_WOORITECH_20240717_NUCLEAR_POLICY_PRICE_ONLY_BLOWOFF", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["nuclear_policy_or_project_event_premium", "preferred_bidder_or_export_project_attention", "relative_strength_before_final_contract"], "stage3_evidence_fields": ["final_contract_and_legal_clarity_required", "company_specific_scope_award_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["event_premium_spike", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["legal_or_final_contract_delay", "no_company_specific_award_conversion", "event_premium_mean_reversion"], "symbol": "032820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv", "trigger_date": "2024-07-17", "trigger_type": "Stage2-EventPremium", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "NUCLEAR_SMALLCAP_EVENT_PREMIUM_LEGAL_DELAY_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "nuclear_policy_legal_delay_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C04 nuclear policy/project rows should cap at Stage2/Yellow or local 4B until final contract, legal clarity, company-specific scope, and margin/revision bridge are confirmed; small-cap event premium spikes should not be positive Green evidence.",
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
3. Add C04-specific nuclear project / legal-delay guard only as a shadow candidate until more rows exist.

Candidate rule:
- C04_NUCLEAR_GREEN_REQUIRES_FINAL_CONTRACT_LEGAL_CLARITY
- C04_SMALLCAP_EVENT_PREMIUM_LOCAL_4B
- C04_POLICY_PROJECT_WITHOUT_SCOPE_AWARD_STAGE2_CAP

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

