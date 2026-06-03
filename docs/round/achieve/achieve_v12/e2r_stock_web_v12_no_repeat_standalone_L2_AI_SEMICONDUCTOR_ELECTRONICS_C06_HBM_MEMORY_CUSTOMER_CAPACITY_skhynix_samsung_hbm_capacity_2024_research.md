# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C06 — HBM customer-capacity lock vs generic memory recovery guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_CUSTOMER_CAPACITY_LOCK_VS_GENERIC_MEMORY_RECOVERY_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_skhynix_samsung_hbm_capacity_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY current coverage:
rows=10, symbols=2, date range=2023-10-27~2024-10-08, good/bad S2=2/2, 4B/4C=0/1
top covered symbols: UNKNOWN_SYMBOL(5), 000660(3), 005930(2)
```

C06 is structurally under-covered and necessarily has a narrow symbol universe. This run avoids exact hard-duplicate keys by using new trigger-date / trigger-family combinations:
```text
C06 + 000660 + Stage2-Actionable + 2023-05-26
C06 + 000660 + 4B-local-price-only + 2024-07-11
C06 + 005930 + Stage3-Yellow + 2024-04-02
```

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
000660 SK하이닉스: 2023/2024 forward windows clean; corporate-action candidates are old, outside the test window.
005930 삼성전자: 2024 forward window clean; corporate-action candidates are old or 2018, outside the test window.
```

## 3. Research thesis

C06 is not a generic memory-cycle bucket. It should test whether the HBM story has actually become customer-capacity lock:

```text
HBM demand shock
→ customer qualification / allocation / capacity share
→ HBM mix and margin bridge
→ EPS revision
→ valuation rerating
```

The core residual is transfer risk. SK Hynix's HBM path can be a true customer-capacity rerating, but the same HBM label should not automatically promote a laggard or generic memory recovery name. When the market already prices the customer lock, the correct state should also shift from fresh Green to 4B watch.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C06_000660_SKHYNIX_20230526_HBM_CUSTOMER_CAPACITY_STAGE2 | 000660 | positive_customer_capacity_stage2_success | 2023-05-26 | 109200 | 166900 on 2024-02-23 | 106100 on 2023-05-26 | 10.9% | 18.13% | 52.84% | -2.84% | -7.67% |
| C06_000660_SKHYNIX_20240711_HBM_CAPACITY_LOCAL_4B | 000660 | protective_4b_success | 2024-07-11 | 241000 | 248500 on 2024-07-11 | 150500 on 2024-09-09 | 3.11% | 3.11% | 3.11% | -37.55% | -39.44% |
| C06_005930_SAMSUNG_20240402_HBM_LAGGARD_FALSE_GREEN | 005930 | false_green_counterexample | 2024-04-02 | 85000 | 88800 on 2024-07-11 | 61500 on 2024-09-30 | 0.59% | 4.24% | 4.47% | -27.65% | -30.74% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 000660 in May 2023 is the useful early route: the price path already separated from ordinary memory recovery before the later HBM revision wave.
- This is Stage2-Actionable because the path requires customer-capacity verification, not because price moved alone.

### Stage3 / Green
- C06 Green should require customer qualification, allocation/capacity share, HBM mix, and EPS revision bridge.
- 000660 can satisfy this once the customer-capacity lock is visible.
- 005930 should not inherit C06 credit just because it is a memory major; without customer qualification and HBM-share evidence, it remains Yellow.

### 4B
- 000660 / 2024-07-11 is a protective 4B case. The HBM thesis was real, but the price path had already capitalized a large part of the evidence.
- Full 4B should require non-price evidence of saturation or revision deceleration; local 4B can activate on peak proximity and drawdown risk.

### 4C
- No hard 4C/accounting break is asserted here.
- The 005930 failure mode is a qualification/share gap: HBM theme heat did not close into the same customer-capacity proof.

## 6. Raw component score breakdown

```json
{
  "C06_000660_SKHYNIX_20230526_HBM_CUSTOMER_CAPACITY_STAGE2": {
    "bottleneck_pricing_power": 13,
    "capital_allocation": 2,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 65,
    "valuation_rerating_runway": 11,
    "visibility_quality": 12
  },
  "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_LOCAL_4B": {
    "bottleneck_pricing_power": 14,
    "capital_allocation": 2,
    "eps_fcf_explosion": 13,
    "information_confidence": 4,
    "market_mispricing": 5,
    "total": 55,
    "valuation_rerating_runway": 3,
    "visibility_quality": 14
  },
  "C06_005930_SAMSUNG_20240402_HBM_LAGGARD_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 3,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 34,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C06 guard:
```text
if hbm_customer_capacity_attention and customer_lock_or_allocation_bridge_confirmed:
    allow_stage3_green_candidate = true

if generic_memory_recovery_or_laggard_hbm_headline and no customer_qualification_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if hbm_capacity_rerating_is_mature and price_peak_proximity_high:
    route_to_local_4B_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 005930 / 2024-04-02: HBM label plus broad memory recovery can be over-promoted if C06 customer-capacity proof is not required at company level.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -2.84, "MAE_30D_pct": -2.84, "MAE_90D_pct": -2.84, "MFE_180D_pct": 52.84, "MFE_30D_pct": 10.9, "MFE_90D_pct": 18.13, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_000660_SKHYNIX_20230526_HBM_CUSTOMER_CAPACITY_STAGE2", "case_role": "positive_customer_capacity_stage2_success", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful because customer-capacity visibility was beginning to separate from generic memory recovery; Green still required customer lock and revision confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -7.67, "entry_date": "2023-05-26", "entry_price": 109200, "evidence_family": "hbm_customer_capacity_visibility_stage2_before_full_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_LOCK_VS_GENERIC_MEMORY_RECOVERY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2023-05-26", "low_price_180d": 106100, "peak_date": "2024-02-23", "peak_price": 166900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 13, "capital_allocation": 2, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 12, "total": 65, "valuation_rerating_runway": 11, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C06_000660_SKHYNIX_20230526_HBM_CUSTOMER_CAPACITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_customer_capacity_attention", "customer_qualification_or_allocation_claim", "relative_strength_vs_generic_memory"], "stage3_evidence_fields": ["customer_lock_confirmation_required", "capacity_share_and_hbm_mix_required", "revision_bridge_required"], "stage4b_evidence_fields": ["hbm_capacity_rerating_matured", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_gap", "generic_memory_recovery_without_hbm_lock", "revision_or_capacity_share_break"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv", "trigger_date": "2023-05-26", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -37.55, "MAE_30D_pct": -37.1, "MAE_90D_pct": -37.55, "MFE_180D_pct": 3.11, "MFE_30D_pct": 3.11, "MFE_90D_pct": 3.11, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_LOCAL_4B", "case_role": "protective_4b_success", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "By the July 2024 peak, HBM customer-capacity evidence was already heavily capitalized; local 4B discipline was more useful than fresh Green promotion.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -39.44, "entry_date": "2024-07-11", "entry_price": 241000, "evidence_family": "hbm_capacity_rerating_mature_peak_proximity_local_4b_guard", "evidence_url_pending": false, "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_LOCK_VS_GENERIC_MEMORY_RECOVERY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 150500, "peak_date": "2024-07-11", "peak_price": 248500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 14, "capital_allocation": 2, "eps_fcf_explosion": 13, "information_confidence": 4, "market_mispricing": 5, "total": 55, "valuation_rerating_runway": 3, "visibility_quality": 14}, "reuse_reason": null, "same_entry_group_id": "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_customer_capacity_attention", "customer_qualification_or_allocation_claim", "relative_strength_vs_generic_memory"], "stage3_evidence_fields": ["customer_lock_confirmation_required", "capacity_share_and_hbm_mix_required", "revision_bridge_required"], "stage4b_evidence_fields": ["hbm_capacity_rerating_matured", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_gap", "generic_memory_recovery_without_hbm_lock", "revision_or_capacity_share_break"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "trigger_date": "2024-07-11", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -27.65, "MAE_30D_pct": -11.65, "MAE_90D_pct": -13.53, "MFE_180D_pct": 4.47, "MFE_30D_pct": 0.59, "MFE_90D_pct": 4.24, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_005930_SAMSUNG_20240402_HBM_LAGGARD_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "삼성전자", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "HBM/customer-capacity credit should not transfer from SK Hynix to Samsung unless customer qualification, capacity share, and revision evidence close; otherwise it remains Yellow/counterexample.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.74, "entry_date": "2024-04-02", "entry_price": 85000, "evidence_family": "hbm_laggard_generic_memory_recovery_without_customer_qualification_lock", "evidence_url_pending": false, "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_LOCK_VS_GENERIC_MEMORY_RECOVERY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-30", "low_price_180d": 61500, "peak_date": "2024-07-11", "peak_price": 88800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 3, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 5, "total": 34, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C06_005930_SAMSUNG_20240402_HBM_LAGGARD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_customer_capacity_attention", "customer_qualification_or_allocation_claim", "relative_strength_vs_generic_memory"], "stage3_evidence_fields": ["customer_lock_confirmation_required", "capacity_share_and_hbm_mix_required", "revision_bridge_required"], "stage4b_evidence_fields": ["hbm_capacity_rerating_matured", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_gap", "generic_memory_recovery_without_hbm_lock", "revision_or_capacity_share_break"], "symbol": "005930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv", "trigger_date": "2024-04-02", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_LOCK_VS_GENERIC_MEMORY_RECOVERY_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_customer_capacity_positive_and_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C06 HBM/customer-capacity credit should require customer lock, capacity allocation/share, HBM mix, and revision bridge; generic memory recovery or laggard HBM headlines should cap at Yellow/counterexample, while mature SK Hynix HBM rerating should route to local 4B.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C06 + symbol + trigger_type + entry_date.
3. Add C06-specific customer-capacity lock / laggard-transfer guard only as a shadow candidate until more rows exist.

Candidate rule:
- C06_GREEN_REQUIRES_CUSTOMER_LOCK_ALLOCATION_HBM_MIX_REVISION
- C06_GENERIC_MEMORY_OR_LAGGARD_HBM_STAGE2_YELLOW_CAP
- C06_MATURE_HBM_CAPACITY_RERATING_LOCAL_4B

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

