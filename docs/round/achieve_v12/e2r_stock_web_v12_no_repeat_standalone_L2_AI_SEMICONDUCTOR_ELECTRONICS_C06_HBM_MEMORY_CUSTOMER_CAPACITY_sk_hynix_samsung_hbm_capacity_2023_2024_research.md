# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C06 — HBM memory customer-capacity qualification / 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_4B_GUARD
loop_objective: coverage_gap_fill|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_after_stage2_success|qualification_lag_false_green|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_sk_hynix_samsung_hbm_capacity_2023_2024_research.md
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

C06 is structurally concentrated because Korea has only a few direct listed memory makers. This run therefore uses new trigger-date / trigger-family combinations rather than inventing weak proxy symbols:
```text
C06 + 000660 + Stage2-Actionable + 2023-05-26
C06 + 000660 + 4B-local-price-only + 2024-07-11
C06 + 005930 + Stage3-Yellow + 2024-07-11
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
000660 SK하이닉스: selected 2023/2024 forward windows clean; corporate-action candidates are historical and latest 2003-04-21, outside selected test windows.
005930 삼성전자: selected 2024 forward window clean; corporate-action candidates are 1996-01-03, 1997-01-03, 2018-05-04, outside selected test window.
```

## 3. Research thesis

C06 should split fresh HBM customer-capacity evidence from a fully priced HBM premium:

```text
HBM memory customer-capacity attention
→ customer qualification and allocation share
→ capacity ramp, yield and shipment cadence
→ ASP/mix and gross margin bridge
→ memory-cycle revision confirmation
→ rerating or local 4B cap
```

HBM capacity is a scarce seat at the AI table. Stage2 can buy the first confirmed seat assignment, but Green should not keep buying the same seat after the market has priced the whole banquet.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C06_000660_SKHYNIX_20230526_HBM_CUSTOMER_CAPACITY_STAGE2 | 000660 | positive_hbm_customer_capacity_stage2_success | 2023-05-26 | 109200 | 166900 on 2024-02-23 | 106000 on 2023-06-01 | 10.9% | 19.78% | 52.84% | -2.93% | -8.15% |
| C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B | 000660 | hbm_capacity_price_premium_4b_refresh_counterexample | 2024-07-11 | 241000 | 248500 on 2024-07-11 | 144700 on 2024-09-19 | 3.11% | 3.11% | 3.11% | -39.96% | -41.77% |
| C06_005930_SAMSUNG_20240711_HBM_QUALIFICATION_LAG_FALSE_GREEN | 005930 | hbm_qualification_lag_false_green_counterexample | 2024-07-11 | 87600 | 88800 on 2024-07-11 | 49900 on 2024-11-14 | 1.37% | 1.37% | 1.37% | -43.04% | -43.81% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 000660 / 2023-05-26 is the positive anchor. It captured the early HBM customer-capacity rerating when the AI memory path had not yet been fully capitalized.
- Stage2 is allowed only when non-price evidence connects HBM demand to customer qualification/allocation, capacity tightness, shipment cadence, ASP/mix and revisions.

### Stage3 / Green
- C06 Green should require customer qualification, allocation share, capacity ramp, yield, shipment cadence, ASP/mix, gross margin and revision confirmation.
- 005930 / 2024-07-11 is the false-Green guard. Memory beta and HBM expectation were present, but customer qualification/allocation and revision bridge lagged the price-implied expectation.

### 4B
- 000660 / 2024-07-11 is the rerating-refresh 4B row. Earlier Stage2 evidence was valid, but by July 2024 the market had priced a large amount of HBM capacity value.
- The key 4B test is whether new allocation, yield or revision evidence arrives after the premium. Without it, the model should not confuse price strength with fresh evidence.

### 4C
- No hard customer cancellation or memory-cycle thesis break is asserted.
- The C06 break mode here is qualification/allocation evidence exhaustion: HBM demand remains real, but the stock price may already have capitalized more allocation, yield and margin than the evidence supports.

## 6. Raw component score breakdown

```json
{
  "C06_000660_SKHYNIX_20230526_HBM_CUSTOMER_CAPACITY_STAGE2": {
    "ASP_mix_bridge": 9,
    "capacity_allocation_tightness": 10,
    "hbm_customer_visibility": 11,
    "information_confidence": 4,
    "margin_revision_bridge": 9,
    "market_mispricing": 10,
    "shipment_yield_cadence": 8,
    "total": 69,
    "valuation_rerating_runway": 8
  },
  "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B": {
    "ASP_mix_bridge": 5,
    "capacity_allocation_tightness": 6,
    "hbm_customer_visibility": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 4,
    "market_mispricing": 4,
    "shipment_yield_cadence": 5,
    "total": 35,
    "valuation_rerating_runway": 1
  },
  "C06_005930_SAMSUNG_20240711_HBM_QUALIFICATION_LAG_FALSE_GREEN": {
    "ASP_mix_bridge": 4,
    "capacity_allocation_tightness": 4,
    "hbm_customer_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 5,
    "shipment_yield_cadence": 3,
    "total": 28,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C06 guard:
```text
if HBM_customer_capacity and qualification_allocation_yield_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if HBM_memory_price_premium and no incremental_customer_allocation_yield_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if memory_beta_price_confirmation and qualification_or_allocation_lags:
    keep_stage3_yellow_or_counterexample = true
```

Residual errors:
```text
current_profile_error_count = 2
- 000660 / 2024-07-11: a valid earlier HBM Stage2 can become a 4B refresh problem once capacity value is capitalized.
- 005930 / 2024-07-11: memory/HBM price confirmation can be over-promoted if customer qualification and allocation evidence lag the price.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -2.93, "MAE_30D_pct": -2.93, "MAE_90D_pct": -2.93, "MFE_180D_pct": 52.84, "MFE_30D_pct": 10.9, "MFE_90D_pct": 19.78, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_000660_SKHYNIX_20230526_HBM_CUSTOMER_CAPACITY_STAGE2", "case_role": "positive_hbm_customer_capacity_stage2_success", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_2023_2024_forward_window; profile corporate-action candidates are historical and latest 2003-04-21, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when HBM customer allocation, capacity tightness and AI memory mix visibility began to separate from generic memory-cycle beta. Green still requires customer qualification, capacity allocation, ASP/mix, shipment cadence, capex/yield and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -8.15, "entry_date": "2023-05-26", "entry_price": 109200, "evidence_family": "hbm_customer_capacity_memory_customer_allocation_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2023-06-01", "low_price_180d": 106000, "peak_date": "2024-02-23", "peak_price": 166900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"ASP_mix_bridge": 9, "capacity_allocation_tightness": 10, "hbm_customer_visibility": 11, "information_confidence": 4, "margin_revision_bridge": 9, "market_mispricing": 10, "shipment_yield_cadence": 8, "total": 69, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C06_000660_SKHYNIX_20230526_HBM_CUSTOMER_CAPACITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_customer_capacity_attention", "customer_qualification_or_allocation_visibility", "ASP_mix_yield_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_allocation_share_required", "HBM_capacity_ramp_yield_required", "ASP_mix_shipment_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_memory_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_allocation_gap", "capacity_ramp_yield_disappointment", "margin_revision_bridge_failure"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv", "trigger_date": "2023-05-26", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.96, "MAE_30D_pct": -37.1, "MAE_90D_pct": -39.96, "MFE_180D_pct": 3.11, "MFE_30D_pct": 3.11, "MFE_90D_pct": 3.11, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B", "case_role": "hbm_capacity_price_premium_4b_refresh_counterexample", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_2024_forward_window; profile corporate-action candidates are historical and latest 2003-04-21, outside selected test window", "current_profile_error": true, "current_profile_verdict": "A valid HBM Stage2 can become a 4B refresh problem once price has capitalized customer capacity tightness. At the July 2024 premium, Green needed fresh customer allocation, capacity ramp, ASP/mix, yield and margin revision evidence rather than price momentum alone.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.77, "entry_date": "2024-07-11", "entry_price": 241000, "evidence_family": "hbm_capacity_price_premium_without_incremental_customer_allocation_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-19", "low_price_180d": 144700, "peak_date": "2024-07-11", "peak_price": 248500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"ASP_mix_bridge": 5, "capacity_allocation_tightness": 6, "hbm_customer_visibility": 7, "information_confidence": 3, "margin_revision_bridge": 4, "market_mispricing": 4, "shipment_yield_cadence": 5, "total": 35, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C06_000660_SKHYNIX_20240711_HBM_CAPACITY_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_customer_capacity_attention", "customer_qualification_or_allocation_visibility", "ASP_mix_yield_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_allocation_share_required", "HBM_capacity_ramp_yield_required", "ASP_mix_shipment_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_memory_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_allocation_gap", "capacity_ramp_yield_disappointment", "margin_revision_bridge_failure"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "trigger_date": "2024-07-11", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -43.04, "MAE_30D_pct": -19.86, "MAE_90D_pct": -43.04, "MFE_180D_pct": 1.37, "MFE_30D_pct": 1.37, "MFE_90D_pct": 1.37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "case_id": "C06_005930_SAMSUNG_20240711_HBM_QUALIFICATION_LAG_FALSE_GREEN", "case_role": "hbm_qualification_lag_false_green_counterexample", "company_name": "삼성전자", "corporate_action_window_status": "clean_2024_forward_window; profile corporate-action candidates are 1996-01-03, 1997-01-03, 2018-05-04, all outside selected test window", "current_profile_error": true, "current_profile_verdict": "HBM memory-cycle price confirmation should stay Yellow when customer qualification, allocation share, capacity ramp, yield, ASP/mix and revision evidence are weaker than the price-implied expectation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.81, "entry_date": "2024-07-11", "entry_price": 87600, "evidence_family": "hbm_memory_customer_capacity_price_confirmation_without_qualification_allocation_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-14", "low_price_180d": 49900, "peak_date": "2024-07-11", "peak_price": 88800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005930.json", "raw_component_score_breakdown": {"ASP_mix_bridge": 4, "capacity_allocation_tightness": 4, "hbm_customer_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 5, "shipment_yield_cadence": 3, "total": 28, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C06_005930_SAMSUNG_20240711_HBM_QUALIFICATION_LAG_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_customer_capacity_attention", "customer_qualification_or_allocation_visibility", "ASP_mix_yield_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_allocation_share_required", "HBM_capacity_ramp_yield_required", "ASP_mix_shipment_margin_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_memory_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_allocation_gap", "capacity_ramp_yield_disappointment", "margin_revision_bridge_failure"], "symbol": "005930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv", "trigger_date": "2024-07-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_memory_customer_capacity_sk_hynix_samsung_qualification_4b_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C06 HBM memory capacity rows should allow Stage2 when customer qualification/allocation, capacity tightness, ASP/mix, shipment cadence, yield and margin-revision bridge are visible, but should route to local 4B or Yellow when price already capitalizes HBM capacity and incremental customer allocation or qualification evidence has not refreshed.",
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
3. Add C06-specific HBM customer-capacity / qualification / allocation / yield / ASP-mix / margin-revision / local-4B refresh guard only as a shadow candidate until more rows exist.

Candidate rule:
- C06_STAGE2_ALLOWED_ON_QUALIFICATION_ALLOCATION_YIELD_MARGIN_REVISION_BRIDGE
- C06_GREEN_REQUIRES_CUSTOMER_ALLOCATION_CAPACITY_RAMP_YIELD_ASP_MIX_REVISION
- C06_HBM_PRICE_PREMIUM_LOCAL_4B_REFRESH
- C06_MEMORY_BETA_WITHOUT_QUALIFICATION_ALLOCATION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

