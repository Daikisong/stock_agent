# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semi test socket customer-quality guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_REORDER_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_test_socket_probe_quality_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY current coverage:
rows=10, symbols=3, date range=2024-03-08~2024-04-26, good/bad S2=4/0, 4B/4C=0/0
top covered symbols: 058470(2), 131290(2), 리노공업(2), 티에스이(2), 095340(1)
```

This run avoids those top-covered C08 symbols and adds 425420, 098120, and 252990.  
Each row uses a new `C08 + symbol + trigger_type + entry_date` hard key.

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
425420 티에프이: corporate_action_candidate_count=0.
098120 마이크로컨텍솔: 2024 forward window clean; corporate-action candidates are old, outside the test window.
252990 샘씨엔에스: corporate_action_candidate_count=0.
```

## 3. Research thesis

C08 should not be a generic “semiconductor small-cap parts” bucket. It should test whether the customer-quality loop closes:

```text
test socket / probe card / ceramic component attention
→ customer qualification or quality acceptance
→ repeat order and utilization
→ ASP or mix improvement
→ margin and revision bridge
→ rerating
```

The residual problem is that quality language is sticky. Once a stock is described as a “customer-quality beneficiary,” the market can keep paying for a qualification that has not yet become reorder. In this archetype, the second purchase order matters more than the first rumor.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C08_425420_TFE_20240320_TEST_SOCKET_QUALITY_THEME_LOCAL_4B | 425420 | protective_4b_success | 2024-03-20 | 43100 | 43950 on 2024-03-21 | 14720 on 2024-09-09 | 1.97% | 1.97% | 1.97% | -65.85% | -66.51% |
| C08_098120_MICROCONTACT_20240308_TEST_SOCKET_CUSTOMER_QUALITY_FALSE_GREEN | 098120 | false_green_counterexample | 2024-03-08 | 11450 | 11700 on 2024-03-08 | 4965 on 2024-09-09 | 2.18% | 2.18% | 2.18% | -56.64% | -57.56% |
| C08_252990_SEMCNS_20240418_PROBE_CARD_CERAMIC_CUSTOMER_QUALITY_FALSE_GREEN | 252990 | probe_card_component_false_green_counterexample | 2024-04-18 | 8590 | 9280 on 2024-04-18 | 4750 on 2024-09-11 | 8.03% | 8.03% | 8.03% | -44.7% | -48.81% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Test socket, probe-card, and customer-quality attention can route a Stage2 research row.
- But a Stage2 row is only a queue ticket. It is not Green until qualification, repeat order, ASP/mix, and revision close.

### Stage3 / Green
- C08 Green should require customer qualification and repeat-order evidence. A socket/probe component stock does not deserve Green just because the AI/HBM equipment theme is hot.
- 098120 and 252990 show the false-Green failure: the price spike existed, but it did not carry enough evidence-weighted runway.

### 4B
- 425420 is the protective 4B anchor. After the price already capitalized the socket-quality theme, the useful signal was not fresh entry but risk control.
- Local 4B should activate when price runs ahead of confirmed reorder and margin revision.

### 4C
- No hard accounting break is asserted.
- The C08 break mode is a qualification/reorder gap: the story keeps saying “quality,” but the market later discovers that quality without volume, ASP/mix, and margin is only a label.

## 6. Raw component score breakdown

```json
{
  "C08_098120_MICROCONTACT_20240308_TEST_SOCKET_CUSTOMER_QUALITY_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 29,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C08_252990_SEMCNS_20240418_PROBE_CARD_CERAMIC_CUSTOMER_QUALITY_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 29,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C08_425420_TFE_20240320_TEST_SOCKET_QUALITY_THEME_LOCAL_4B": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 8,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 36,
    "valuation_rerating_runway": 2,
    "visibility_quality": 8
  }
}
```

## 7. Current calibrated profile stress test

Suggested C08 guard:
```text
if test_socket_or_probe_card_attention and no customer_qualification_reorder_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if customer_quality_theme_price_run and no incremental_non_price_reorder_evidence:
    route_to_local_4B_watch = true

if post_peak_drawdown and reorder_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 098120 / 2024-03-08: test-socket theme heat could be over-promoted if the model treats quality labels as customer-qualified revenue.
- 252990 / 2024-04-18: probe-card component relative strength can become a false Green without repeat order and revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -65.85, "MAE_30D_pct": -24.25, "MAE_90D_pct": -49.54, "MFE_180D_pct": 1.97, "MFE_30D_pct": 1.97, "MFE_90D_pct": 1.97, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_425420_TFE_20240320_TEST_SOCKET_QUALITY_THEME_LOCAL_4B", "case_role": "protective_4b_success", "company_name": "티에프이", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "The correct useful signal is local 4B after the test-socket/customer-quality story had been priced; this should not be fresh Green unless incremental customer qualification and reorder evidence arrive.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -66.51, "entry_date": "2024-03-20", "entry_price": 43100, "evidence_family": "test_socket_hbm_quality_theme_price_run_without_incremental_customer_quality_bridge", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_REORDER_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 14720, "peak_date": "2024-03-21", "peak_price": 43950, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/425/425420.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 8, "information_confidence": 3, "market_mispricing": 4, "total": 36, "valuation_rerating_runway": 2, "visibility_quality": 8}, "reuse_reason": null, "same_entry_group_id": "C08_425420_TFE_20240320_TEST_SOCKET_QUALITY_THEME_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_or_probe_card_attention", "customer_quality_or_qualification_claim", "relative_strength"], "stage3_evidence_fields": ["customer_qualification_confirmation_required", "repeat_order_or_reorder_visibility_required", "asp_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["customer_quality_theme_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["qualification_or_reorder_gap", "socket_probe_component_beta_mean_reversion", "margin_or_revision_bridge_failure"], "symbol": "425420", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv", "trigger_date": "2024-03-20", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -56.64, "MAE_30D_pct": -21.31, "MAE_90D_pct": -37.12, "MFE_180D_pct": 2.18, "MFE_30D_pct": 2.18, "MFE_90D_pct": 2.18, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_098120_MICROCONTACT_20240308_TEST_SOCKET_CUSTOMER_QUALITY_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "마이크로컨텍솔", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Socket/customer-quality labels should stay Yellow when qualification, repeat order, ASP/mix, and margin/revision bridge are not visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -57.56, "entry_date": "2024-03-08", "entry_price": 11450, "evidence_family": "test_socket_theme_without_customer_quality_reorder_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_REORDER_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 4965, "peak_date": "2024-03-08", "peak_price": 11700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/098/098120.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 29, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C08_098120_MICROCONTACT_20240308_TEST_SOCKET_CUSTOMER_QUALITY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_or_probe_card_attention", "customer_quality_or_qualification_claim", "relative_strength"], "stage3_evidence_fields": ["customer_qualification_confirmation_required", "repeat_order_or_reorder_visibility_required", "asp_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["customer_quality_theme_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["qualification_or_reorder_gap", "socket_probe_component_beta_mean_reversion", "margin_or_revision_bridge_failure"], "symbol": "098120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "trigger_date": "2024-03-08", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.7, "MAE_30D_pct": -18.98, "MAE_90D_pct": -37.37, "MFE_180D_pct": 8.03, "MFE_30D_pct": 8.03, "MFE_90D_pct": 8.03, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_252990_SEMCNS_20240418_PROBE_CARD_CERAMIC_CUSTOMER_QUALITY_FALSE_GREEN", "case_role": "probe_card_component_false_green_counterexample", "company_name": "샘씨엔에스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Probe-card component relative strength should not become Green without customer qualification, utilization/reorder, and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.81, "entry_date": "2024-04-18", "entry_price": 8590, "evidence_family": "probe_card_ceramic_component_theme_without_customer_qualification_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_REORDER_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-11", "low_price_180d": 4750, "peak_date": "2024-04-18", "peak_price": 9280, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/252/252990.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 29, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C08_252990_SEMCNS_20240418_PROBE_CARD_CERAMIC_CUSTOMER_QUALITY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_or_probe_card_attention", "customer_quality_or_qualification_claim", "relative_strength"], "stage3_evidence_fields": ["customer_qualification_confirmation_required", "repeat_order_or_reorder_visibility_required", "asp_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["customer_quality_theme_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["qualification_or_reorder_gap", "socket_probe_component_beta_mean_reversion", "margin_or_revision_bridge_failure"], "symbol": "252990", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv", "trigger_date": "2024-04-18", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_REORDER_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "test_socket_customer_quality_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 semi test-socket/probe-card rows should cap at Stage2/Yellow unless customer qualification, repeat order, ASP/mix, margin and revision bridge are confirmed; price runs without incremental quality evidence should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C08 + symbol + trigger_type + entry_date.
3. Add C08-specific customer-qualification / reorder / ASP-mix / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C08_GREEN_REQUIRES_CUSTOMER_QUALIFICATION_REORDER_MARGIN_REVISION
- C08_CUSTOMER_QUALITY_THEME_STAGE2_YELLOW_CAP
- C08_TEST_SOCKET_PRICE_RUN_LOCAL_4B
- C08_PROBE_SOCKET_REORDER_GAP_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

