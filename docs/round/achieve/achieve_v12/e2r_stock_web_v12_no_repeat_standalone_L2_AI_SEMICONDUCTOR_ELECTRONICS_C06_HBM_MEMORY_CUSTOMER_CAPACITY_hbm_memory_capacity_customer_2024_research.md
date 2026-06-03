# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C06 — HBM memory customer-capacity guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_SHARE_MIX_REVISION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_4C_guard_validation|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_hbm_memory_capacity_customer_2024_research.md
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

C06 has a structurally narrow listed-symbol universe. This run therefore does not pretend to add a new memory-primary symbol. It avoids hard duplicates by selecting new `canonical_archetype_id + symbol + trigger_type + entry_date` keys and by splitting:
```text
early HBM customer/capacity visibility → Stage2 success
late HBM capacity price premium → local 4B / false-Green guard
customer qualification without mix/revision proof → counterexample
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
000660 SK하이닉스: 2024 forward window clean; corporate-action candidates are old, outside the test window.
005930 삼성전자: 2024 forward window clean; corporate-action candidates are old or 2018, outside the selected 2024 test window.
```

## 3. Research thesis

C06 should not be a generic memory-upcycle bucket. It should test whether HBM customer/capacity evidence becomes confirmed, margin-rich supply:

```text
HBM customer / qualification / capacity attention
→ confirmed customer share or allocation
→ capacity yield and ramp
→ HBM mix margin
→ EPS/revision bridge
→ rerating
```

The useful metaphor is a reservation book. Early reservations matter, but by late cycle the market needs seated customers, working kitchen capacity, and paid bills. A full reservation book without confirmed customer share, yield and margin is not yet earnings.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C06_000660_SKHYNIX_20240119_HBM_CUSTOMER_CAPACITY_STAGE2 | 000660 | positive_hbm_customer_capacity_stage2_success_with_later_4b | 2024-01-19 | 141300 | 248500 on 2024-07-11 | 131700 on 2024-02-01 | 18.97% | 48.62% | 75.87% | -6.79% | -41.77% |
| C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PREMIUM_LOCAL_4B | 000660 | hbm_capacity_price_premium_4b_counterexample | 2024-07-11 | 241000 | 248500 on 2024-07-11 | 144700 on 2024-09-19 | 3.11% | 3.11% | 3.11% | -39.96% | -41.77% |
| C06_005930_SAMSUNG_20240705_HBM_CUSTOMER_CAPACITY_FALSE_GREEN | 005930 | hbm_customer_qualification_false_green_counterexample | 2024-07-05 | 87100 | 88800 on 2024-07-11 | 49900 on 2024-11-14 | 1.95% | 1.95% | 1.95% | -42.71% | -43.81% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- HBM customer allocation, qualification and capacity-ramp visibility can be valid Stage2 routes.
- 000660 on 2024-01-19 is the positive anchor: early relative strength and customer/capacity visibility produced a large forward MFE before the late-July drawdown.

### Stage3 / Green
- C06 Green should require confirmed customer share, capacity yield/ramp, HBM mix margin and revision confirmation.
- 005930 on 2024-07-05 is the false-Green guard: a headline customer/capacity improvement route did not protect the stock when qualification/share/mix evidence stayed unresolved.

### 4B
- 000660 on 2024-07-11 is the local 4B row: the HBM capacity/customer story was real, but the price had already capitalized much of the evidence.
- A valid early HBM thesis can mature into risk-control mode. The signal changes from “buy the ramp” to “verify incremental ramp.”

### 4C
- No hard accounting break is asserted.
- The C06 break mode is evidence exhaustion: customer and capacity words remain attractive, but confirmed allocation, yield, mix margin and revisions do not keep expanding fast enough to carry valuation.

## 6. Raw component score breakdown

```json
{
  "C06_000660_SKHYNIX_20240119_HBM_CUSTOMER_CAPACITY_STAGE2": {
    "bottleneck_pricing_power": 12,
    "capital_allocation": 3,
    "eps_fcf_explosion": 12,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 65,
    "valuation_rerating_runway": 10,
    "visibility_quality": 13
  },
  "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PREMIUM_LOCAL_4B": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 8,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 36,
    "valuation_rerating_runway": 2,
    "visibility_quality": 8
  },
  "C06_005930_SAMSUNG_20240705_HBM_CUSTOMER_CAPACITY_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 3,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 33,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C06 guard:
```text
if hbm_customer_capacity_attention and early_customer_allocation_capacity_visibility:
    allow_stage2_actionable = true

if hbm_capacity_price_premium and no incremental_customer_share_capacity_yield_mix_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if customer_qualification_headline and no confirmed_share_or_mix_margin_revision:
    cap_stage = Stage3-Yellow
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 000660 / 2024-07-11: late HBM capacity premium can be over-promoted if the model does not require incremental customer share, yield and revision evidence after the price run.
- 005930 / 2024-07-05: HBM qualification/capacity headline can look like Green, but the following path argues for Yellow/counterexample when customer share and mix-margin bridge are unresolved.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -6.79, "MAE_30D_pct": -6.79, "MAE_90D_pct": -6.79, "MFE_180D_pct": 75.87, "MFE_30D_pct": 18.97, "MFE_90D_pct": 48.62, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_000660_SKHYNIX_20240119_HBM_CUSTOMER_CAPACITY_STAGE2", "case_role": "positive_hbm_customer_capacity_stage2_success_with_later_4b", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when HBM customer allocation and capacity visibility began to separate SK하이닉스 from generic memory beta, but Green still requires customer share, capacity ramp, mix margin and revision confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.77, "entry_date": "2024-01-19", "entry_price": 141300, "evidence_family": "hbm_customer_capacity_allocation_visibility_to_memory_rerating", "evidence_url_pending": false, "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_SHARE_MIX_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-02-01", "low_price_180d": 131700, "peak_date": "2024-07-11", "peak_price": 248500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 12, "capital_allocation": 3, "eps_fcf_explosion": 12, "information_confidence": 4, "market_mispricing": 11, "total": 65, "valuation_rerating_runway": 10, "visibility_quality": 13}, "reuse_reason": null, "same_entry_group_id": "C06_000660_SKHYNIX_20240119_HBM_CUSTOMER_CAPACITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_customer_capacity_attention", "customer_allocation_or_qualification_claim", "capacity_ramp_or_mix_margin_visibility_signal"], "stage3_evidence_fields": ["confirmed_customer_share_required", "capacity_yield_and_ramp_required", "hbm_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["hbm_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_share_gap", "capacity_yield_or_ramp_delay", "mix_margin_or_revision_bridge_failure"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "trigger_date": "2024-01-19", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.96, "MAE_30D_pct": -37.1, "MAE_90D_pct": -39.96, "MFE_180D_pct": 3.11, "MFE_30D_pct": 3.11, "MFE_90D_pct": 3.11, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PREMIUM_LOCAL_4B", "case_role": "hbm_capacity_price_premium_4b_counterexample", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late HBM capacity/customer premium should route to local 4B unless incremental capacity, customer allocation, mix margin and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.77, "entry_date": "2024-07-11", "entry_price": 241000, "evidence_family": "hbm_customer_capacity_price_premium_without_incremental_capacity_revision_runway", "evidence_url_pending": false, "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_SHARE_MIX_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-19", "low_price_180d": 144700, "peak_date": "2024-07-11", "peak_price": 248500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 8, "information_confidence": 3, "market_mispricing": 4, "total": 36, "valuation_rerating_runway": 2, "visibility_quality": 8}, "reuse_reason": null, "same_entry_group_id": "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PREMIUM_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_customer_capacity_attention", "customer_allocation_or_qualification_claim", "capacity_ramp_or_mix_margin_visibility_signal"], "stage3_evidence_fields": ["confirmed_customer_share_required", "capacity_yield_and_ramp_required", "hbm_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["hbm_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_share_gap", "capacity_yield_or_ramp_delay", "mix_margin_or_revision_bridge_failure"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "trigger_date": "2024-07-11", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -42.71, "MAE_30D_pct": -19.4, "MAE_90D_pct": -42.71, "MFE_180D_pct": 1.95, "MFE_30D_pct": 1.95, "MFE_90D_pct": 1.95, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_005930_SAMSUNG_20240705_HBM_CUSTOMER_CAPACITY_FALSE_GREEN", "case_role": "hbm_customer_qualification_false_green_counterexample", "company_name": "삼성전자", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "HBM qualification/customer-capacity headlines should stay Yellow if customer share, capacity yield, mix margin and revision bridge remain unresolved; price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.81, "entry_date": "2024-07-05", "entry_price": 87100, "evidence_family": "hbm_customer_qualification_capacity_claim_without_share_mix_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_SHARE_MIX_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-14", "low_price_180d": 49900, "peak_date": "2024-07-11", "peak_price": 88800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 3, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 33, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C06_005930_SAMSUNG_20240705_HBM_CUSTOMER_CAPACITY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["hbm_customer_capacity_attention", "customer_allocation_or_qualification_claim", "capacity_ramp_or_mix_margin_visibility_signal"], "stage3_evidence_fields": ["confirmed_customer_share_required", "capacity_yield_and_ramp_required", "hbm_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["hbm_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_share_gap", "capacity_yield_or_ramp_delay", "mix_margin_or_revision_bridge_failure"], "symbol": "005930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv", "trigger_date": "2024-07-05", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_SHARE_MIX_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_memory_customer_capacity_4b_false_green_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C06 HBM memory customer/capacity rows should allow Stage2 when customer allocation and capacity-ramp visibility emerge early, but Stage3 Green requires confirmed customer share, capacity yield/ramp, HBM mix margin and revision bridge; late capacity price premium should route to local 4B or counterexample.",
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
3. Because C06 has a narrow listed-symbol universe, accept same-symbol soft duplicates only when date, trigger family, Stage transition, or failure mode differs.
4. Add C06-specific HBM customer/capacity/share/mix-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C06_STAGE2_ALLOWED_ON_EARLY_HBM_CUSTOMER_CAPACITY_VISIBILITY
- C06_GREEN_REQUIRES_CUSTOMER_SHARE_CAPACITY_YIELD_MIX_REVISION
- C06_LATE_HBM_CAPACITY_PREMIUM_LOCAL_4B
- C06_QUALIFICATION_WITHOUT_SHARE_MIX_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

