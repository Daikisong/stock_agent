# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semi test socket customer quality guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_GUARD
loop_objective: counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|coverage_gap_fill
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_test_socket_probe_card_2024_research.md
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
top symbols: 058470, 131290, 리노공업, 티에스이, 095340
```

This run avoids the crowded exact keys and adds three new independent rows around test-socket/probe-card adjacent names. None of the rows uses an existing `canonical_archetype_id + symbol + trigger_type + entry_date` key from the index.

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

Profiles:
```text
425420 티에프이: first_date=2022-11-17, last_date=2026-02-20, corporate_action_candidate_count=0.
080580 오킨스전자: 2021 corporate-action candidates only; 2024 window clean.
219130 타이거일렉: first_date=2015-09-25, last_date=2026-02-20, corporate_action_candidate_count=0.
```

## 3. Research thesis

C08 should identify durable customer quality in semi test socket / probe / test interface suppliers. The failure mode is subtle:

```text
AI/HBM/CXL attention
→ socket/probe-card relative strength
→ valuation or theme rally
→ but no verified customer quality, repeat demand, margin bridge, or revision
→ high-MAE / false-Green / local 4B risk
```

The current calibrated profile already blocks price-only promotion, but C08 needs an archetype-specific Green guard: test-socket theme plus short relative strength is not equivalent to customer quality.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C08_219130_TIGERELEC_20240214_PROBE_TEST_PCB_HIGH_MAE_SUCCESS | 219130 | high_mae_success | 2024-02-14 | 31550 | 45300 on 2024-05-14 | 19800 on 2024-07-25 | 43.58% | -37.24% | -56.29% |
| C08_425420_TFE_20240208_TEST_SOCKET_THEME_FALSE_GREEN | 425420 | failed_rerating | 2024-02-08 | 35200 | 43850 on 2024-03-20 | 11550 on 2024-11-18 | 24.57% | -67.19% | -73.66% |
| C08_080580_OKINS_20240122_CXL_SOCKET_PRICE_ONLY_BLOWOFF | 080580 | price_moved_without_evidence | 2024-01-22 | 12930 | 14910 on 2024-01-23 | 7750 on 2024-04-09 | 15.31% | -40.06% | -48.02% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Relative strength and semiconductor theme attention are enough to route research.
- The selected rows are valid Stage2/Stage2-Watch candidates because the price path confirms attention.

### Stage3 / Green
- C08 Green should require durable customer quality, repeat demand, and margin/revision evidence.
- Theme labels such as CXL, AI socket, probe-card, or HBM adjacency are not enough.

### 4B
- 425420 and 080580 show local blowoff behavior without enough non-price evidence.
- These should remain local 4B watch / price-only guard rows, not full-window 4B success.

### 4C
- The failure is mostly a slow visibility gap, not necessarily a hard accounting break.
- 425420's post-peak drawdown and 080580's fast reversal are useful counterexamples for C08 Green strictness.

## 6. Current calibrated profile stress test

Current profile should keep C08 strict:
```text
if test_socket_theme and relative_strength but no customer_quality_confirmation:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true
    4B_local_watch_allowed = true
    full_4B_requires_non_price_evidence = true
```

Residual errors:
```text
current_profile_error_count = 2
- 425420: false-Green risk if TFE's theme/relative-strength leg is treated as durable customer quality.
- 080580: price-only CXL/socket blowoff should be watch/counterexample, not positive Stage2/Green evidence.
```

## 7. Machine-readable rows

```jsonl
{"MAE_180D_pct": -37.24, "MAE_30D_pct": -12.2, "MAE_90D_pct": -37.24, "MFE_180D_pct": 43.58, "MFE_30D_pct": 43.58, "MFE_90D_pct": 43.58, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_219130_TIGERELEC_20240214_PROBE_TEST_PCB_HIGH_MAE_SUCCESS", "case_role": "high_mae_success", "company_name": "타이거일렉", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": false, "current_profile_verdict": "Stage2-Actionable or Stage3-Yellow only until customer-quality and margin/revision bridge close", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -56.29, "entry_date": "2024-02-14", "entry_price": 31550, "evidence_family": "probe_test_pcb_socket_quality_relative_strength_with_customer_quality_inference", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-07-25", "low_price_180d": 19800, "peak_date": "2024-05-14", "peak_price": 45300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/219/219130.json", "reuse_reason": null, "same_entry_group_id": "C08_219130_TIGERELEC_20240214_PROBE_TEST_PCB_HIGH_MAE_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_card_theme", "relative_strength", "ai_hbm_cxl_semiconductor_attention"], "stage3_evidence_fields": ["customer_quality_confirmation_required", "margin_or_revision_bridge_required", "repeat_demand_visibility_required"], "stage4b_evidence_fields": ["valuation_beta_rally", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["theme_without_revenue_conversion", "customer_quality_gap", "revision_fade_or_no_revision_confirmation"], "symbol": "219130", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv", "trigger_date": "2024-02-14", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -67.19, "MAE_30D_pct": -11.36, "MAE_90D_pct": -13.07, "MFE_180D_pct": 24.57, "MFE_30D_pct": 24.57, "MFE_90D_pct": 24.57, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_425420_TFE_20240208_TEST_SOCKET_THEME_FALSE_GREEN", "case_role": "failed_rerating", "company_name": "티에프이", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": true, "current_profile_verdict": "false Green risk if socket theme plus short relative strength is treated as customer quality", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -73.66, "entry_date": "2024-02-08", "entry_price": 35200, "evidence_family": "test_socket_hbm_theme_without_durable_customer_or_revision_confirmation", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-18", "low_price_180d": 11550, "peak_date": "2024-03-20", "peak_price": 43850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/425/425420.json", "reuse_reason": null, "same_entry_group_id": "C08_425420_TFE_20240208_TEST_SOCKET_THEME_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_card_theme", "relative_strength", "ai_hbm_cxl_semiconductor_attention"], "stage3_evidence_fields": ["customer_quality_confirmation_required", "margin_or_revision_bridge_required", "repeat_demand_visibility_required"], "stage4b_evidence_fields": ["valuation_beta_rally", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["theme_without_revenue_conversion", "customer_quality_gap", "revision_fade_or_no_revision_confirmation"], "symbol": "425420", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv", "trigger_date": "2024-02-08", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -40.06, "MAE_30D_pct": -19.49, "MAE_90D_pct": -40.06, "MFE_180D_pct": 15.31, "MFE_30D_pct": 15.31, "MFE_90D_pct": 15.31, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_080580_OKINS_20240122_CXL_SOCKET_PRICE_ONLY_BLOWOFF", "case_role": "price_moved_without_evidence", "company_name": "오킨스전자", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": true, "current_profile_verdict": "current profile should block positive promotion and treat only as local 4B/price-only watch", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.02, "entry_date": "2024-01-22", "entry_price": 12930, "evidence_family": "cxl_socket_theme_price_only_without_customer_revenue_bridge", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-04-09", "low_price_180d": 7750, "peak_date": "2024-01-23", "peak_price": 14910, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/080/080580.json", "reuse_reason": null, "same_entry_group_id": "C08_080580_OKINS_20240122_CXL_SOCKET_PRICE_ONLY_BLOWOFF", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_card_theme", "relative_strength", "ai_hbm_cxl_semiconductor_attention"], "stage3_evidence_fields": ["customer_quality_confirmation_required", "margin_or_revision_bridge_required", "repeat_demand_visibility_required"], "stage4b_evidence_fields": ["valuation_beta_rally", "positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["theme_without_revenue_conversion", "customer_quality_gap", "revision_fade_or_no_revision_confirmation"], "symbol": "080580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "trigger_date": "2024-01-22", "trigger_type": "Stage2-Watch", "upstream_source": "FinanceData/marcap"}
```

## 8. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 should not upgrade from Stage2/Yellow to Green on test-socket/probe-card theme or relative strength alone; require customer-quality, repeat demand, and margin/revision bridge.",
  "source_proxy_only_count": 0
}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C08 + symbol + trigger_type + entry_date.
3. Add C08-specific strictness only as a shadow candidate until more rows exist.

Candidate rule:
- C08_STAGE3_GREEN_CUSTOMER_QUALITY_REQUIRED
- C08_PRICE_ONLY_SOCKET_THEME_LOCAL_4B_ONLY
- C08_TEST_SOCKET_RELATIVE_STRENGTH_STAGE2_CAP

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 10. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

