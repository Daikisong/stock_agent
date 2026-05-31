# E2R V12 No-Repeat Standalone Residual Research
## R10 / L9 / C30 — Construction PF balance-sheet break guard

metadata:
```text
selected_round: R10
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_WORKOUT_SECTOR_DISCOUNT_NON_PF_EPC_GUARD
loop_objective: 4C_guard_validation|counterexample_mining|green_strictness_stress_test|coverage_gap_fill
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_pf_workout_sector_guard_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK current coverage:
rows=28, symbols=6, date range=2022-01-12~2024-08-27, good/bad S2=5/0, 4B/4C=0/4
top covered symbols: 006360(6), 294870(5), 375500(4), UNKNOWN_SYMBOL(3), 000720(2)
```

This run avoids the top repeated C30 symbols and adds 009410, 047040, and 028050.  
Each row uses a new `C30 + symbol + trigger_type + entry_date` hard key.

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
009410 태영건설: 2023 window clean; corporate-action candidates are 2007-05-03, 2020-09-22, 2024-10-31.
047040 대우건설: 2023 window clean; corporate-action candidates are old, outside the test window.
028050 삼성E&A: 2023 window clean; corporate-action candidates are old, outside the test window.
```

## 3. Research thesis

C30 should not be a generic construction-underperformance bucket. It should be a trust and balance-sheet break detector:

```text
PF / project exposure
→ liquidity, covenant, legal, defect, or refinancing evidence
→ balance-sheet trust break
→ hard 4C or 4C-watch
```

The residual issue is the boundary. A real PF/workout break should go hard 4C. A broad sector discount without company-specific break should stay Yellow/watch. Non-PF EPC/orderbook exposure can even be a relative safe-haven despite the same sector label.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C30_009410_TAEYOUNG_20231213_PF_WORKOUT_HARD_4C | 009410 | pf_hard_4c_success | 2023-12-13 | 3270 | 4110 on 2024-01-11 | 1935 on 2023-12-28 | 25.69% | -40.83% | -46.96% |
| C30_047040_DAEWOO_20230915_PF_SECTOR_WATCH_NOT_HARD_BREAK | 047040 | sector_pf_false_hard_4c_counterexample | 2023-09-15 | 4570 | 4675 on 2023-09-18 | 3865 on 2023-10-24 | 2.3% | -15.43% | -17.33% |
| C30_028050_SAMSUNGEA_20230131_NON_PF_EPC_SAFEHAVEN_CONTRAST | 028050 | non_pf_epc_safehaven_contrast | 2023-01-31 | 25850 | 32200 on 2023-03-31 | 22900 on 2023-10-31 | 24.56% | -11.41% | -28.88% |

## 5. Stage evidence split

### Stage2 / Stage3
- Broad construction-sector PF concern is enough to route a watch row.
- It is not enough to declare hard 4C without company-specific evidence.

### 4B
- Distressed rebounds after a PF collapse can be violent. C30 should not let that rebound erase the underlying hard 4C.
- Sector-discount relief rallies should stay local 4B/Yellow unless balance-sheet trust is restored.

### 4C
- 009410 is the hard 4C anchor: once PF liquidity becomes workout/balance-sheet risk, the thesis is broken.
- 047040 is the guardrail counterexample: sector PF discount alone is not the same as a hard balance-sheet break.
- 028050 is the contrast row: non-PF overseas EPC/orderbook exposure should not be automatically punished by the housing PF bucket.

## 6. Raw component score breakdown

```json
{
  "C30_009410_TAEYOUNG_20231213_PF_WORKOUT_HARD_4C": {
    "bottleneck_pricing_power": 1,
    "capital_allocation": 0,
    "eps_fcf_explosion": 1,
    "information_confidence": 5,
    "market_mispricing": 1,
    "total": 9,
    "valuation_rerating_runway": 0,
    "visibility_quality": 1
  },
  "C30_028050_SAMSUNGEA_20230131_NON_PF_EPC_SAFEHAVEN_CONTRAST": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 3,
    "eps_fcf_explosion": 9,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 53,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  },
  "C30_047040_DAEWOO_20230915_PF_SECTOR_WATCH_NOT_HARD_BREAK": {
    "bottleneck_pricing_power": 4,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 32,
    "valuation_rerating_runway": 6,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C30 guard:
```text
if construction_pf_stress and company_specific_liquidity_or_legal_break:
    stage = 4C or 4C-watch

if broad_sector_pf_discount and no company_specific_break:
    cap_stage = Stage3-Yellow / watch
    block_hard_4C = true

if non_pf_epc_orderbook_safehaven and balance_sheet_clean:
    do_not_route_to_pf_hard_break = true
```

Residual error:
```text
current_profile_error_count = 1
- 047040 / 2023-09-15: broad PF sector discount could be over-classified as hard 4C if company-specific break evidence is not required.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -40.83, "MAE_30D_pct": -40.83, "MAE_90D_pct": -33.33, "MFE_180D_pct": 25.69, "MFE_30D_pct": 25.69, "MFE_90D_pct": 25.69, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_009410_TAEYOUNG_20231213_PF_WORKOUT_HARD_4C", "case_role": "pf_hard_4c_success", "company_name": "태영건설", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Hard 4C is justified when PF liquidity stress turns into balance-sheet/workout risk; price rebound after the first collapse should not reset the thesis.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.96, "entry_date": "2023-12-13", "entry_price": 3270, "evidence_family": "pf_liquidity_workout_balance_sheet_break", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_SECTOR_DISCOUNT_NON_PF_EPC_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2023-12-28", "low_price_180d": 1935, "peak_date": "2024-01-11", "peak_price": 4110, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009410.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 1, "capital_allocation": 0, "eps_fcf_explosion": 1, "information_confidence": 5, "market_mispricing": 1, "total": 9, "valuation_rerating_runway": 0, "visibility_quality": 1}, "reuse_reason": null, "same_entry_group_id": "C30_009410_TAEYOUNG_20231213_PF_WORKOUT_HARD_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_sector_pf_attention", "balance_sheet_or_backlog_route_check", "relative_price_path"], "stage3_evidence_fields": ["company_specific_liquidity_or_legal_evidence_required", "pf_exposure_quality_required", "non_pf_orderbook_safehaven_separation_required"], "stage4b_evidence_fields": ["distressed_rebound_after_collapse", "sector_discount_reversal", "post_peak_drawdown"], "stage4c_evidence_fields": ["pf_liquidity_break", "workout_or_covenant_risk", "balance_sheet_trust_break"], "symbol": "009410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv", "trigger_date": "2023-12-13", "trigger_type": "Stage4C-Hard", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -15.43, "MAE_30D_pct": -9.85, "MAE_90D_pct": -15.43, "MFE_180D_pct": 2.3, "MFE_30D_pct": 2.3, "MFE_90D_pct": 2.3, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_047040_DAEWOO_20230915_PF_SECTOR_WATCH_NOT_HARD_BREAK", "case_role": "sector_pf_false_hard_4c_counterexample", "company_name": "대우건설", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Broad PF/sector discount should stay Yellow/watch unless company-specific liquidity, legal, defect, or covenant evidence appears.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -17.33, "entry_date": "2023-09-15", "entry_price": 4570, "evidence_family": "broad_construction_pf_sector_discount_without_company_specific_break", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_SECTOR_DISCOUNT_NON_PF_EPC_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2023-10-24", "low_price_180d": 3865, "peak_date": "2023-09-18", "peak_price": 4675, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/047/047040.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 6, "total": 32, "valuation_rerating_runway": 6, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C30_047040_DAEWOO_20230915_PF_SECTOR_WATCH_NOT_HARD_BREAK", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_sector_pf_attention", "balance_sheet_or_backlog_route_check", "relative_price_path"], "stage3_evidence_fields": ["company_specific_liquidity_or_legal_evidence_required", "pf_exposure_quality_required", "non_pf_orderbook_safehaven_separation_required"], "stage4b_evidence_fields": ["distressed_rebound_after_collapse", "sector_discount_reversal", "post_peak_drawdown"], "stage4c_evidence_fields": ["pf_liquidity_break", "workout_or_covenant_risk", "balance_sheet_trust_break"], "symbol": "047040", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv", "trigger_date": "2023-09-15", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -11.41, "MAE_30D_pct": -0.97, "MAE_90D_pct": 1.93, "MFE_180D_pct": 24.56, "MFE_30D_pct": 24.56, "MFE_90D_pct": 24.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_028050_SAMSUNGEA_20230131_NON_PF_EPC_SAFEHAVEN_CONTRAST", "case_role": "non_pf_epc_safehaven_contrast", "company_name": "삼성E&A", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "C30 must separate PF balance-sheet break from non-PF EPC/orderbook exposure; this type can be Stage2 positive but later 4B/Yellow if sector risk returns.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.88, "entry_date": "2023-01-31", "entry_price": 25850, "evidence_family": "non_pf_overseas_epc_backlog_balance_sheet_safe_haven", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_SECTOR_DISCOUNT_NON_PF_EPC_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "low_date_180d": "2023-10-31", "low_price_180d": 22900, "peak_date": "2023-03-31", "peak_price": 32200, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/028/028050.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 3, "eps_fcf_explosion": 9, "information_confidence": 4, "market_mispricing": 10, "total": 53, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C30_028050_SAMSUNGEA_20230131_NON_PF_EPC_SAFEHAVEN_CONTRAST", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_sector_pf_attention", "balance_sheet_or_backlog_route_check", "relative_price_path"], "stage3_evidence_fields": ["company_specific_liquidity_or_legal_evidence_required", "pf_exposure_quality_required", "non_pf_orderbook_safehaven_separation_required"], "stage4b_evidence_fields": ["distressed_rebound_after_collapse", "sector_discount_reversal", "post_peak_drawdown"], "stage4c_evidence_fields": ["pf_liquidity_break", "workout_or_covenant_risk", "balance_sheet_trust_break"], "symbol": "028050", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2023.csv", "trigger_date": "2023-01-31", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "PF_WORKOUT_SECTOR_DISCOUNT_NON_PF_EPC_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "loop_contribution_label": "4c_guard_and_false_hard_break_counterexample",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R10",
  "shadow_rule_candidate": "C30 should distinguish hard PF liquidity/workout breaks from broad construction-sector discounts and non-PF EPC safe-haven/orderbook cases; hard 4C requires company-specific balance-sheet, legal, defect, covenant, or trust-break evidence.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C30 + symbol + trigger_type + entry_date.
3. Add C30-specific split logic only as a shadow candidate until more rows exist.

Candidate rule:
- C30_HARD_4C_REQUIRES_COMPANY_SPECIFIC_PF_LIQUIDITY_OR_TRUST_BREAK
- C30_BROAD_SECTOR_PF_DISCOUNT_YELLOW_CAP
- C30_NON_PF_EPC_SAFEHAVEN_DO_NOT_HARD_BREAK

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

