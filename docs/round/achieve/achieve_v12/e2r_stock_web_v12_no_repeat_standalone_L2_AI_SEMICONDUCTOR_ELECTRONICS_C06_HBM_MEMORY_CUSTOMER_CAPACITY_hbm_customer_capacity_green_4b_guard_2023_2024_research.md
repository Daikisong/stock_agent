# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C06 — HBM memory customer-capacity / Green-to-4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_CUSTOMER_CAPACITY_GREEN_4B_GUARD
loop_objective: coverage_gap_fill|narrow_universe_soft_reuse|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_hbm_customer_capacity_green_4b_guard_2023_2024_research.md
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

C06 has a narrow listed-symbol universe. This run therefore accepts same-symbol soft reuse only where the trigger family, entry date, Stage transition and failure mode differ from existing rows.  
Each row uses a new `C06 + symbol + trigger_type + entry_date` hard key.

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
000660 SK하이닉스: 2023/2024 selected forward windows clean; corporate-action candidates are historical and outside selected test windows.
005930 삼성전자: 2024 selected forward window clean; latest corporate-action candidate is 2018-05-04 and outside selected test window.
```

## 3. Research thesis

C06 should not treat every HBM headline as Green. It should test whether HBM attention becomes allocated, qualified, high-margin capacity:

```text
HBM / AI server memory attention
→ customer qualification and allocation
→ qualified HBM capacity and yield
→ ASP/mix and margin bridge
→ capex timing and revision confirmation
→ rerating
```

HBM is not just a chip word; it is a reservation book for scarce qualified capacity. Stage2 can follow the first reservation. Green should require the customer name, table size, kitchen throughput and the bill.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C06_000660_SKHYNIX_20230525_HBM_CUSTOMER_CAPACITY_STAGE2 | 000660 | positive_hbm_customer_capacity_stage2_success | 2023-05-25 | 103500 | 143700 on 2023-12-22 | 101100 on 2023-05-25 | 17.0% | 24.64% | 38.84% | -2.32% | -3.13% |
| C06_005930_SAMSUNG_20240405_HBM_CATCHUP_FALSE_GREEN | 005930 | hbm_catchup_false_green_counterexample | 2024-04-05 | 84500 | 88800 on 2024-07-11 | 49900 on 2024-11-14 | 1.78% | 5.09% | 5.09% | -40.95% | -43.81% |
| C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B | 000660 | late_hbm_capacity_price_premium_counterexample | 2024-07-11 | 241000 | 248500 on 2024-07-11 | 144700 on 2024-09-19 | 3.11% | 3.11% | 3.11% | -39.96% | -41.77% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- HBM customer-capacity attention can be a valid Stage2 route when customer allocation and qualified capacity visibility appear before full EPS revision is priced.
- 000660 / 2023-05-25 is the positive anchor. The Nvidia/HBM demand route produced a low-MAE Stage2 entry and a large forward MFE before the later leadership premium matured.

### Stage3 / Green
- C06 Green should require qualified HBM capacity, customer allocation, yield, ASP/mix margin, capex timing and revision confirmation.
- 005930 / 2024-04-05 is the false-Green guard. Catch-up language and price strength were not enough when customer qualification, HBM3E mix, margin and revision evidence failed to carry the premium.

### 4B
- 000660 / 2024-07-11 is the local 4B row. The HBM leadership story was real, but the stock had already priced a large portion of scarce-capacity value. The following drawdown shows why incremental customer allocation and margin revision evidence had to be refreshed.
- This is exactly the transition C06 needs: the same HBM mechanism that creates Stage2 alpha can later become valuation risk.

### 4C
- No hard customer cancellation or HBM qualification failure is asserted.
- The C06 break mode is evidence exhaustion: the HBM story remains structurally valid, but incremental customer allocation, yield, ASP/mix, margin and revisions do not keep widening enough to support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C06_000660_SKHYNIX_20230525_HBM_CUSTOMER_CAPACITY_STAGE2": {
    "bottleneck_pricing_power": 11,
    "capital_allocation": 4,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 61,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  },
  "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 3,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 35,
    "valuation_rerating_runway": 2,
    "visibility_quality": 7
  },
  "C06_005930_SAMSUNG_20240405_HBM_CATCHUP_FALSE_GREEN": {
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

if hbm_catchup_or_leadership_price_premium and no incremental_allocation_yield_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and customer_allocation_or_ASP_mix_revision_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 005930 / 2024-04-05: HBM catch-up can be over-promoted if the model treats price confirmation as customer qualification and high-margin allocation proof.
- 000660 / 2024-07-11: HBM leadership can turn into local 4B if incremental allocation, yield, ASP/mix and revision evidence do not keep expanding after the price run.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -2.32, "MAE_30D_pct": -2.32, "MAE_90D_pct": -2.32, "MFE_180D_pct": 38.84, "MFE_30D_pct": 17.0, "MFE_90D_pct": 24.64, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_000660_SKHYNIX_20230525_HBM_CUSTOMER_CAPACITY_STAGE2", "case_role": "positive_hbm_customer_capacity_stage2_success", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_forward_window; corporate-action candidates are old and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when HBM customer/capacity visibility began to attach to a real AI-server demand path before the full earnings revision was priced. Green still requires qualified HBM capacity, customer allocation, ASP/mix, yield, capex timing and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -3.13, "entry_date": "2023-05-25", "entry_price": 103500, "evidence_family": "hbm_memory_customer_capacity_nvidia_ai_server_visibility_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_GREEN_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2023-05-25", "low_price_180d": 101100, "peak_date": "2023-12-22", "peak_price": 143700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 11, "capital_allocation": 4, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 10, "total": 61, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C06_000660_SKHYNIX_20230525_HBM_CUSTOMER_CAPACITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_customer_capacity_attention", "customer_allocation_or_qualification_visibility", "AI_server_memory_demand_revision_route"], "stage3_evidence_fields": ["qualified_HBM_capacity_required", "customer_allocation_yield_ASP_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_allocation_gap", "yield_capacity_or_ASP_mix_disappointment", "memory_margin_revision_bridge_failure"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv", "trigger_date": "2023-05-25", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -40.95, "MAE_30D_pct": -11.12, "MAE_90D_pct": -16.92, "MFE_180D_pct": 5.09, "MFE_30D_pct": 1.78, "MFE_90D_pct": 5.09, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_005930_SAMSUNG_20240405_HBM_CATCHUP_FALSE_GREEN", "case_role": "hbm_catchup_false_green_counterexample", "company_name": "삼성전자", "corporate_action_window_status": "clean_2024_forward_window; latest corporate-action candidate is 2018-05-04, outside selected test window", "current_profile_error": true, "current_profile_verdict": "HBM catch-up language should stay Yellow if customer qualification, HBM3E allocation, yield, ASP/mix, memory-margin and revision evidence do not keep improving after the price run. Price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.81, "entry_date": "2024-04-05", "entry_price": 84500, "evidence_family": "hbm_catchup_customer_qualification_claim_without_capacity_mix_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_GREEN_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-14", "low_price_180d": 49900, "peak_date": "2024-07-11", "peak_price": 88800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 3, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 33, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C06_005930_SAMSUNG_20240405_HBM_CATCHUP_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_customer_capacity_attention", "customer_allocation_or_qualification_visibility", "AI_server_memory_demand_revision_route"], "stage3_evidence_fields": ["qualified_HBM_capacity_required", "customer_allocation_yield_ASP_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_allocation_gap", "yield_capacity_or_ASP_mix_disappointment", "memory_margin_revision_bridge_failure"], "symbol": "005930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv", "trigger_date": "2024-04-05", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.96, "MAE_30D_pct": -37.1, "MAE_90D_pct": -39.96, "MFE_180D_pct": 3.11, "MFE_30D_pct": 3.11, "MFE_90D_pct": 3.11, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B", "case_role": "late_hbm_capacity_price_premium_counterexample", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_forward_window; corporate-action candidates are old and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late HBM capacity premium should route to local 4B or counterexample unless incremental customer allocation, capacity additions, yield, ASP/mix margin and revision evidence keep expanding after the stock has already capitalized the HBM leadership story.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.77, "entry_date": "2024-07-11", "entry_price": 241000, "evidence_family": "hbm_memory_capacity_price_premium_without_incremental_customer_allocation_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_GREEN_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-19", "low_price_180d": 144700, "peak_date": "2024-07-11", "peak_price": 248500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 3, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 4, "total": 35, "valuation_rerating_runway": 2, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_customer_capacity_attention", "customer_allocation_or_qualification_visibility", "AI_server_memory_demand_revision_route"], "stage3_evidence_fields": ["qualified_HBM_capacity_required", "customer_allocation_yield_ASP_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_allocation_gap", "yield_capacity_or_ASP_mix_disappointment", "memory_margin_revision_bridge_failure"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "trigger_date": "2024-07-11", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_GREEN_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_memory_customer_capacity_soft_reuse_new_dates_green_4b_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C06 HBM memory customer-capacity rows should allow Stage2 when HBM customer allocation/capacity visibility appears before the full earnings revision is priced, but Stage3 Green requires qualified capacity, customer allocation, yield, ASP/mix margin and revision bridge; late HBM price premium or catch-up narratives without incremental allocation proof should route to Yellow/local 4B or counterexample.",
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
3. Because C06 has a narrow listed-symbol universe, accept same-symbol soft reuse only when date, trigger family, Stage transition or failure mode differs.
4. Add C06-specific HBM customer-capacity / allocation / yield / ASP-mix / 4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C06_STAGE2_ALLOWED_ON_EARLY_HBM_CUSTOMER_ALLOCATION_CAPACITY_VISIBILITY
- C06_GREEN_REQUIRES_QUALIFIED_CAPACITY_CUSTOMER_ALLOCATION_YIELD_ASP_MIX_REVISION
- C06_HBM_LEADERSHIP_OR_CATCHUP_PRICE_PREMIUM_LOCAL_4B
- C06_HBM_CATCHUP_WITHOUT_CUSTOMER_QUALIFICATION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

