# E2R V12 No-Repeat Standalone Residual Research
## R6 / L6 / C21 — Financial ROE/PBR capital-return guard

metadata:
```text
selected_round: R6
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L6_FINANCIALS_CAPITAL_RETURN
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: REGIONAL_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L6_FINANCIALS_CAPITAL_RETURN_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_regional_bank_capital_return_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN current coverage:
rows=150, symbols=19, date range=2021-08-06~2025-05-26, good/bad S2=52/16, 4B/4C=7/0
top covered symbols: 105560(42), 323410(22), UNKNOWN_SYMBOL(21), 086790(19), 006220(11)
```

This run avoids those top-covered C21 symbols and adds 138930, 175330, and 024110.  
Each row uses a new `C21 + symbol + trigger_type + entry_date` hard key.

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
138930 BNK금융지주: 2024 forward window clean; corporate-action candidates are 2014/2016 and outside the selected test window.
175330 JB금융지주: 2024 forward window clean; corporate-action candidates are 2014/2015/2018 and outside the selected test window.
024110 기업은행: 2024 forward window clean; corporate-action candidates are old and outside the selected test window.
```

## 3. Research thesis

C21 should not treat every low-PBR bank rally as automatic Green. It should test whether the discount can be converted into durable capital return:

```text
low-PBR / value-up / capital-return attention
→ repeatable ROE
→ credit-cost and asset-quality stability
→ CET1 or capital-buffer room
→ payout execution and revision bridge
→ rerating
```

The mechanism is like a bank vault with two locks. The first lock is valuation: the stock is cheap. The second lock is capital return: management can return cash without weakening the balance sheet. Green should open only when both locks turn.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C21_138930_BNK_20240201_REGIONAL_BANK_VALUEUP_STAGE2 | 138930 | positive_regional_bank_capital_return_stage2_success_with_later_4b | 2024-02-01 | 7870 | 10050 on 2024-10-25 | 7320 on 2024-02-28 | 6.86% | 10.93% | 27.7% | -6.99% | -9.95% |
| C21_175330_JBFG_20240201_REGIONAL_BANK_CAPITAL_RETURN_STAGE2 | 175330 | positive_capital_return_execution_stage2_success | 2024-02-01 | 12580 | 18710 on 2024-10-25 | 11560 on 2024-02-05 | 27.27% | 28.38% | 48.73% | -8.11% | -7.06% |
| C21_024110_IBK_20240314_PUBLIC_BANK_VALUEUP_PRICE_PREMIUM_FALSE_GREEN | 024110 | public_bank_valueup_false_green_counterexample | 2024-03-14 | 15700 | 16010 on 2024-03-15 | 12790 on 2024-08-05 | 1.97% | 1.97% | 1.97% | -18.54% | -20.11% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Low-PBR/value-up attention and capital-return optionality can be valid Stage2 routes.
- BNK금융지주 and JB금융지주 are the positive anchors: both gave a tradable rerating path when regional-bank discount, shareholder-return execution and ROE/credit-cost evidence moved together.

### Stage3 / Green
- C21 Green should require repeatable ROE, credit-cost containment, CET1/capital-buffer room, payout cadence and revision confirmation.
- Policy attention alone should not be enough. A cheap bank can stay cheap if credit cost rises or payout capacity is capped.

### 4B
- BNK and JB both required later risk control after the value-up/capital-return rerating became widely priced.
- 기업은행 is the explicit false-Green guard. The March 2024 public-bank value-up premium moved first, but the forward path shows that price confirmation without incremental ROE/payout/revision evidence was a weak bridge.

### 4C
- No hard solvency/accounting break is asserted.
- The C21 break mode is capital-return disappointment: the valuation gap remains visible, but asset quality, credit cost, capital buffer or payout execution does not justify a higher multiple.

## 6. Raw component score breakdown

```json
{
  "C21_024110_IBK_20240314_PUBLIC_BANK_VALUEUP_PRICE_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 4,
    "capital_allocation": 3,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 30,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  },
  "C21_138930_BNK_20240201_REGIONAL_BANK_VALUEUP_STAGE2": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 5,
    "eps_fcf_explosion": 8,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 55,
    "valuation_rerating_runway": 10,
    "visibility_quality": 10
  },
  "C21_175330_JBFG_20240201_REGIONAL_BANK_CAPITAL_RETURN_STAGE2": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 5,
    "eps_fcf_explosion": 9,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 57,
    "valuation_rerating_runway": 10,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C21 guard:
```text
if low_pbr_valueup_attention and capital_return_execution_plus_roe_visibility:
    allow_stage2_actionable = true

if bank_price_premium and no incremental_ROE_credit_cost_CET1_payout_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if public_bank_or_policy_bank_valueup_rally and payout_capacity_is_not_flexible:
    cap_stage = Stage3-Yellow
    route_to_counterexample = true
```

Residual error:
```text
current_profile_error_count = 1
- 024110 / 2024-03-14: public-bank low-PBR/value-up premium can be over-promoted if the model treats policy beta as repeatable ROE and payout execution.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -6.99, "MAE_30D_pct": -6.99, "MAE_90D_pct": -6.99, "MFE_180D_pct": 27.7, "MFE_30D_pct": 6.86, "MFE_90D_pct": 10.93, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "case_id": "C21_138930_BNK_20240201_REGIONAL_BANK_VALUEUP_STAGE2", "case_role": "positive_regional_bank_capital_return_stage2_success_with_later_4b", "company_name": "BNK금융지주", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when low-PBR policy attention plus regional-bank capital-return optionality created a rerating route, but Green still requires ROE durability, credit-cost containment, CET1/buffer quality and payout execution.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -9.95, "entry_date": "2024-02-01", "entry_price": 7870, "evidence_family": "regional_bank_low_pbr_valueup_capital_return_roa_roe_rerating_route", "evidence_url_pending": false, "fine_archetype_id": "REGIONAL_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L6_FINANCIALS_CAPITAL_RETURN", "low_date_180d": "2024-02-28", "low_price_180d": 7320, "peak_date": "2024-10-25", "peak_price": 10050, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/138/138930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 5, "eps_fcf_explosion": 8, "information_confidence": 4, "market_mispricing": 12, "total": 55, "valuation_rerating_runway": 10, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C21_138930_BNK_20240201_REGIONAL_BANK_VALUEUP_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R6", "source_proxy_only": false, "stage2_evidence_fields": ["low_pbr_valueup_policy_attention", "capital_return_or_payout_execution_claim", "ROE_or_credit_cost_visibility_signal"], "stage3_evidence_fields": ["repeatable_ROE_required", "credit_cost_and_asset_quality_required", "CET1_capital_room_and_payout_cadence_required"], "stage4b_evidence_fields": ["low_pbr_capital_return_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["credit_cost_or_NPL_upturn", "capital_buffer_or_payout_constraint", "ROE_revision_bridge_failure"], "symbol": "138930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv", "trigger_date": "2024-02-01", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -8.11, "MAE_30D_pct": -8.11, "MAE_90D_pct": -8.11, "MFE_180D_pct": 48.73, "MFE_30D_pct": 27.27, "MFE_90D_pct": 28.38, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "case_id": "C21_175330_JBFG_20240201_REGIONAL_BANK_CAPITAL_RETURN_STAGE2", "case_role": "positive_capital_return_execution_stage2_success", "company_name": "JB금융지주", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful where shareholder-return execution and low-PBR rerating attention converged; Green still needs repeatable ROE, credit quality, CET1 room and payout cadence rather than policy heat alone.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -7.06, "entry_date": "2024-02-01", "entry_price": 12580, "evidence_family": "regional_bank_shareholder_return_low_pbr_policy_roe_rerating", "evidence_url_pending": false, "fine_archetype_id": "REGIONAL_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L6_FINANCIALS_CAPITAL_RETURN", "low_date_180d": "2024-02-05", "low_price_180d": 11560, "peak_date": "2024-10-25", "peak_price": 18710, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/175/175330.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 5, "eps_fcf_explosion": 9, "information_confidence": 4, "market_mispricing": 12, "total": 57, "valuation_rerating_runway": 10, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C21_175330_JBFG_20240201_REGIONAL_BANK_CAPITAL_RETURN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R6", "source_proxy_only": false, "stage2_evidence_fields": ["low_pbr_valueup_policy_attention", "capital_return_or_payout_execution_claim", "ROE_or_credit_cost_visibility_signal"], "stage3_evidence_fields": ["repeatable_ROE_required", "credit_cost_and_asset_quality_required", "CET1_capital_room_and_payout_cadence_required"], "stage4b_evidence_fields": ["low_pbr_capital_return_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["credit_cost_or_NPL_upturn", "capital_buffer_or_payout_constraint", "ROE_revision_bridge_failure"], "symbol": "175330", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv", "trigger_date": "2024-02-01", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -18.54, "MAE_30D_pct": -16.37, "MAE_90D_pct": -18.54, "MFE_180D_pct": 1.97, "MFE_30D_pct": 1.97, "MFE_90D_pct": 1.97, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "case_id": "C21_024110_IBK_20240314_PUBLIC_BANK_VALUEUP_PRICE_PREMIUM_FALSE_GREEN", "case_role": "public_bank_valueup_false_green_counterexample", "company_name": "기업은행", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Public-bank low-PBR/value-up price premium should stay Yellow or local 4B unless ROE durability, credit-cost quality, CET1 room, payout policy and revision bridge remain visible after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -20.11, "entry_date": "2024-03-14", "entry_price": 15700, "evidence_family": "state_policy_bank_low_pbr_price_premium_without_roe_credit_payout_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "REGIONAL_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L6_FINANCIALS_CAPITAL_RETURN", "low_date_180d": "2024-08-05", "low_price_180d": 12790, "peak_date": "2024-03-15", "peak_price": 16010, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/024/024110.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 3, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 6, "total": 30, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C21_024110_IBK_20240314_PUBLIC_BANK_VALUEUP_PRICE_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R6", "source_proxy_only": false, "stage2_evidence_fields": ["low_pbr_valueup_policy_attention", "capital_return_or_payout_execution_claim", "ROE_or_credit_cost_visibility_signal"], "stage3_evidence_fields": ["repeatable_ROE_required", "credit_cost_and_asset_quality_required", "CET1_capital_room_and_payout_cadence_required"], "stage4b_evidence_fields": ["low_pbr_capital_return_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["credit_cost_or_NPL_upturn", "capital_buffer_or_payout_constraint", "ROE_revision_bridge_failure"], "symbol": "024110", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv", "trigger_date": "2024-03-14", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "REGIONAL_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L6_FINANCIALS_CAPITAL_RETURN",
  "loop_contribution_label": "regional_bank_valueup_capital_return_new_symbols_and_public_bank_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R6",
  "shadow_rule_candidate": "C21 financial ROE/PBR/capital-return rows should allow Stage2 when low-PBR value-up policy, capital-return execution and ROE/credit-cost visibility align, but Stage3 Green requires repeatable ROE, asset-quality discipline, CET1 room, payout cadence and revision bridge; public-bank policy price premium without ROE durability should route to Yellow/local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C21 + symbol + trigger_type + entry_date.
3. Add C21-specific low-PBR / ROE / CET1 / capital-return execution guard only as a shadow candidate until more rows exist.

Candidate rule:
- C21_STAGE2_ALLOWED_ON_LOW_PBR_VALUEUP_WITH_CAPITAL_RETURN_EXECUTION
- C21_GREEN_REQUIRES_REPEATABLE_ROE_CREDIT_COST_CET1_PAYOUT_REVISION
- C21_PUBLIC_BANK_POLICY_BETA_STAGE3_CAP
- C21_LOW_PBR_PREMIUM_WITHOUT_ROE_PAYOUT_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R6/L6_FINANCIALS_CAPITAL_RETURN/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

