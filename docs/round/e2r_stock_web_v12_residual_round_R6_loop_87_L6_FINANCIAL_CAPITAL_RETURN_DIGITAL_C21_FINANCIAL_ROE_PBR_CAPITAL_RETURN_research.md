# E2R Stock-Web v12 Residual Research — R6 Loop 87 / L6 / C21

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 87,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 87,
  "computed_next_round": "R7",
  "computed_next_loop": 87,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "BROKERAGE_HOLDCO_CARD_DIGITAL_FINANCE_ROE_PBR_PAYOUT_CAPITAL_BUFFER_REVENUE_MIX_BRIDGE_VS_VALUEUP_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "financial_ROE_PBR_capital_return_guardrail",
    "brokerage_holdco_card_payout_to_ROE_quality_bridge_test",
    "digital_finance_valueup_theme_vs_monetization_capital_buffer_bridge_test",
    "local_4B_timing_after_financial_valueup_MFE",
    "hard_4C_non_price_ROE_payout_capital_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 87
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
computed_next_round = R7
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R6 is the financial / capital return / digital finance round. This run selects C21 because loop86 R6 used C22 insurance, and the present route tests brokerage/holding, card finance and digital-finance value-up beta rather than repeating the top-covered bank names.

The tested mechanism:

```text
financial value-up / PBR / capital-return headline
→ ROE quality and recurring profit
→ capital buffer and risk-cost control
→ payout execution
→ revenue mix quality
→ durable rerating or digital-finance beta fade
```

C21 is the capital account. A value-up candle opens the vault, but ROE quality, capital buffer and payout execution decide whether the vault contains distributable cash.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C21 top-covered symbols include `105560`, `323410`, `086790`, `UNKNOWN_SYMBOL`, `006220`, and `055550`. This run avoids that top-covered set and uses:

```text
071050 / 한국금융지주
029780 / 삼성카드
377300 / 카카오페이
```

All three are treated as new independent C21 financial ROE/PBR/capital-return cases for this loop.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 071050 | 한국금융지주 | `atlas/symbol_profiles/071/071050.json` | no profile-level CA candidate |
| 029780 | 삼성카드 | `atlas/symbol_profiles/029/029780.json` | no profile-level CA candidate |
| 377300 | 카카오페이 | `atlas/symbol_profiles/377/377300.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R6L87-C21-01 | 071050 | 2024-02-13 | 65,900 | 180D | clean | true |
| R6L87-C21-02 | 029780 | 2024-02-13 | 36,200 | 180D | clean | true |
| R6L87-C21-03 | 377300 | 2024-02-13 | 48,650 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BROKERAGE_HOLDCO_ROE_PBR_VALUEUP | keep Stage2 with ROE quality, revenue mix, capital buffer and payout bridge |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | CARD_FINANCE_PAYOUT_CAPITAL_RETURN | keep Stage2 with payout execution, credit-cost stability and capital adequacy bridge |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | DIGITAL_FINANCE_VALUEUP_BETA_FADE | reject digital-finance value-up MFE without monetization, recurring profit, capital buffer and payout bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R6L87-C21-01 | 071050 | 한국금융지주 | Stage2-Actionable | 2024-02-13 | 65,900 | 17.91 | -4.55 | current_profile_partially_correct_ROE_payout_bridge_needed |
| R6L87-C21-02 | 029780 | 삼성카드 | Stage2-Actionable | 2024-02-13 | 36,200 | 25.83 | -1.8 | current_profile_partially_correct_controlled_MAE_but_payout_bridge_needed |
| R6L87-C21-03 | 377300 | 카카오페이 | Stage2-FalsePositive | 2024-02-13 | 48,650 | 6.47 | -54.88 | current_profile_false_positive_high_MAE_digital_finance_beta |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C21 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: ROE quality, capital buffer, risk-cost control, payout execution, revenue mix, recurring profit, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 071050 | `atlas/ohlcv_tradable_by_symbol_year/071/071050/2024.csv` | `atlas/symbol_profiles/071/071050.json` |
| 029780 | `atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv` | `atlas/symbol_profiles/029/029780.json` |
| 377300 | `atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv` | `atlas/symbol_profiles/377/377300.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 071050 / 한국금융지주

C21 brokerage/financial holding positive with local 4B watch. The February trigger produced a moderate MFE into July. It is kept as Stage2-Actionable, but clean Green requires ROE quality, recurring revenue mix, risk-cost control, capital buffer and payout source repair.

### Case 2 — 029780 / 삼성카드

C21 card-finance payout/capital-return positive with controlled MAE. The price path had a relatively clean drawdown profile and later MFE into August. This is useful because even controlled-MAE positives still need payout execution and capital-buffer bridge before Green.

### Case 3 — 377300 / 카카오페이

C21 digital-finance value-up false positive. The February MFE was small and the later MAE was severe. This rejects digital-finance value-up beta unless monetization, recurring profit, capital buffer and shareholder-return bridge are explicit.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 071050 | 65,900 | 14.11 | -1.06 | 14.11 | -1.06 | 17.91 | -4.55 | 2024-07-17 / 77,700 | -19.05 |
| 029780 | 36,200 | 12.98 | -1.80 | 14.92 | -1.80 | 25.83 | -1.80 | 2024-08-26 / 45,550 | -11.64 |
| 377300 | 48,650 | 6.47 | -21.79 | 6.47 | -44.91 | 6.47 | -54.88 | 2024-02-15 / 51,800 | -57.63 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R6L87-C21-01 | Stage2-Actionable if ROE/payout bridge exists | moderate MFE, controlled MAE | partially correct; ROE/payout bridge needed |
| R6L87-C21-02 | Stage2-Actionable if payout bridge exists | clean MFE, controlled MAE | partially correct; capital-buffer bridge still required |
| R6L87-C21-03 | risk of treating digital value-up beta as Stage2 | low MFE / severe MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C21, the residual is whether value-up/PBR MFE becomes clean Stage2/Green before ROE quality, capital buffer, payout execution and recurring profit bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R6L87-C21-01 | 0.70 | 0.60 | local 4B watch after brokerage holdco MFE if ROE/payout bridge stalls |
| R6L87-C21-02 | 0.70 | 0.60 | card-finance MFE allowed only with payout/ROE/capital-buffer bridge watch |
| R6L87-C21-03 | 0.35 | 0.30 | digital finance MFE rejected without monetization/profit/capital bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_ROE_payout_capital_or_profit_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C21 hard 4C requires confirmed ROE collapse, payout reversal, capital-buffer break, credit-cost shock, recurring-profit deterioration or monetization thesis break.

## 17. Sector / Canonical Rule Candidate

```text
rule_scope = no_new_global_rule
canonical_archetype_rule_candidate = C21_financial_ROE_quality_payout_capital_buffer_profit_bridge_required
confidence = low
production_scoring_changed = false
shadow_weight_only = true
```

## 18. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 11.83 | -15.92 | may over-credit digital-finance value-up beta | needs C21 ROE/payout/capital bridge repair |
| P1 canonical shadow bridge profile | 3 | keeps 071050/029780 with watch | demotes 377300 | better alignment, source repair required |

## 19. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | canonical rule |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BROKERAGE_HOLDCO_CARD_DIGITAL_FINANCE_ROE_PBR_PAYOUT_CAPITAL_BUFFER_REVENUE_MIX_BRIDGE_VS_VALUEUP_BETA_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 1 | yes |

## 20. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - digital_finance_valueup_false_positive_high_MAE
  - ROE_quality_payout_capital_buffer_bridge_required
  - controlled_MAE_financial_positive_still_needs_payout_bridge
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_ROE_payout_capital_profit_break
new_axis_proposed: false
existing_axis_strengthened:
  - C21_financial_ROE_quality_payout_capital_buffer_profit_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
do_not_propose_new_weight_delta: true
```

## 21. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- ROE quality and recurring profit evidence
- capital buffer and risk-cost evidence
- payout/dividend execution
- monetization evidence for digital finance
- production scoring implementation
```

## 22. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_financial_ROE_quality_payout_capital_buffer_profit_bridge_required,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Require ROE quality, capital buffer, payout execution, revenue mix, recurring profit and risk-cost control before clean Stage2/Green","keeps 071050/029780 with ROE-payout bridge watch; demotes 377300 digital-finance value-up false positive","R6L87-C21-01-S2A-20240213|R6L87-C21-02-S2A-20240213|R6L87-C21-03-S2FP-20240213",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 23. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L87-C21-01", "symbol": "071050", "company_name": "한국금융지주", "round": "R6", "loop": 87, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_HOLDCO_CARD_DIGITAL_FINANCE_ROE_PBR_PAYOUT_CAPITAL_BUFFER_REVENUE_MIX_BRIDGE_VS_VALUEUP_BETA_FADE", "case_type": "brokerage_financial_holdco_ROE_PBR_capital_return_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L87-C21-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "financial_holdco_MFE_positive_but_ROE_payout_capital_buffer_bridge_required", "current_profile_verdict": "current_profile_partially_correct_ROE_payout_bridge_needed", "price_source": "Songdaiki/stock-web", "notes": "C21 brokerage/financial-holdco positives need ROE quality, recurring revenue mix, risk-cost control, capital buffer and payout execution before clean Green."}
{"row_type": "trigger", "trigger_id": "R6L87-C21-01-S2A-20240213", "case_id": "R6L87-C21-01", "symbol": "071050", "company_name": "한국금융지주", "round": "R6", "loop": 87, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_HOLDCO_CARD_DIGITAL_FINANCE_ROE_PBR_PAYOUT_CAPITAL_BUFFER_REVENUE_MIX_BRIDGE_VS_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail|ROE_quality_payout_capital_buffer_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "brokerage/financial holding ROE recovery, value-up/PBR rerating and capital-return proxy; primary ROE quality, payout and capital-buffer evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["ROE_PBR_valueup_proxy", "capital_return_proxy", "financial_beta_proxy"], "stage3_evidence_fields": ["ROE_quality", "capital_buffer", "payout_execution", "revenue_mix", "risk_cost_control", "recurring_profit_quality"], "stage4b_evidence_fields": ["financial_MFE_without_ROE_payout_bridge", "valueup_beta_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_ROE_payout_capital_buffer_or_profit_quality_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071050/2024.csv", "profile_path": "atlas/symbol_profiles/071/071050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 65900, "MFE_30D_pct": 14.11, "MAE_30D_pct": -1.06, "MFE_90D_pct": 14.11, "MAE_90D_pct": -1.06, "MFE_180D_pct": 17.91, "MAE_180D_pct": -4.55, "peak_date": "2024-07-17", "peak_price": 77700, "drawdown_after_peak_pct": -19.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.7, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "local_4B_watch_after_brokerage_holdco_MFE_if_ROE_quality_payout_capital_bridge_stalls", "four_b_evidence_type": ["financial_valueup_MFE_without_ROE_payout_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_ROE_payout_capital_or_profit_break", "trigger_outcome_label": "financial_holdco_MFE_positive_but_ROE_payout_capital_buffer_bridge_required", "current_profile_verdict": "current_profile_partially_correct_ROE_payout_bridge_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R6L87-C21-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L87-C21-01", "trigger_id": "R6L87-C21-01-S2A-20240213", "symbol": "071050", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_quality_score": 50, "PBR_repricing_score": 45, "capital_buffer_score": 45, "payout_execution_score": 40, "revenue_mix_score": 40, "risk_cost_control_score": 40, "recurring_profit_score": 40, "relative_strength_score": 60, "valuation_blowoff_risk_score": 45, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"ROE_quality_score": 50, "PBR_repricing_score": 45, "capital_buffer_score": 45, "payout_execution_score": 40, "revenue_mix_score": 40, "risk_cost_control_score": 40, "recurring_profit_score": 40, "relative_strength_score": 60, "valuation_blowoff_risk_score": 55, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 75, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/ROE-payout bridge watch", "changed_components": ["ROE_quality_score", "capital_buffer_score", "payout_execution_score", "revenue_mix_score", "risk_cost_control_score", "recurring_profit_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C21 requires financial value-up MFE to convert into ROE quality, capital buffer, payout execution, recurring profit, revenue mix and risk-cost control before clean Stage2/Green.", "MFE_90D_pct": 14.11, "MAE_90D_pct": -1.06, "score_return_alignment_label": "financial_holdco_MFE_positive_but_ROE_payout_capital_buffer_bridge_required", "current_profile_verdict": "current_profile_partially_correct_ROE_payout_bridge_needed"}
{"row_type": "case", "case_id": "R6L87-C21-02", "symbol": "029780", "company_name": "삼성카드", "round": "R6", "loop": 87, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_HOLDCO_CARD_DIGITAL_FINANCE_ROE_PBR_PAYOUT_CAPITAL_BUFFER_REVENUE_MIX_BRIDGE_VS_VALUEUP_BETA_FADE", "case_type": "card_finance_payout_capital_return_positive_with_controlled_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L87-C21-02-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "card_finance_capital_return_MFE_positive_but_payout_ROE_bridge_required", "current_profile_verdict": "current_profile_partially_correct_controlled_MAE_but_payout_bridge_needed", "price_source": "Songdaiki/stock-web", "notes": "C21 card-finance positives need payout execution, credit-cost stability, capital adequacy, recurring ROE quality and margin/spread bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R6L87-C21-02-S2A-20240213", "case_id": "R6L87-C21-02", "symbol": "029780", "company_name": "삼성카드", "round": "R6", "loop": 87, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_HOLDCO_CARD_DIGITAL_FINANCE_ROE_PBR_PAYOUT_CAPITAL_BUFFER_REVENUE_MIX_BRIDGE_VS_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail|ROE_quality_payout_capital_buffer_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "card finance dividend/capital return, stable ROE and low-PBR value-up proxy; primary payout execution and capital-buffer evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["ROE_PBR_valueup_proxy", "capital_return_proxy", "financial_beta_proxy"], "stage3_evidence_fields": ["ROE_quality", "capital_buffer", "payout_execution", "revenue_mix", "risk_cost_control", "recurring_profit_quality"], "stage4b_evidence_fields": ["financial_MFE_without_ROE_payout_bridge", "valueup_beta_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_ROE_payout_capital_buffer_or_profit_quality_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv", "profile_path": "atlas/symbol_profiles/029/029780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 36200, "MFE_30D_pct": 12.98, "MAE_30D_pct": -1.8, "MFE_90D_pct": 14.92, "MAE_90D_pct": -1.8, "MFE_180D_pct": 25.83, "MAE_180D_pct": -1.8, "peak_date": "2024-08-26", "peak_price": 45550, "drawdown_after_peak_pct": -11.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.7, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "card_finance_MFE_allowed_only_with_payout_ROE_capital_buffer_bridge_watch", "four_b_evidence_type": ["financial_valueup_MFE_without_ROE_payout_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_ROE_payout_capital_or_profit_break", "trigger_outcome_label": "card_finance_capital_return_MFE_positive_but_payout_ROE_bridge_required", "current_profile_verdict": "current_profile_partially_correct_controlled_MAE_but_payout_bridge_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R6L87-C21-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L87-C21-02", "trigger_id": "R6L87-C21-02-S2A-20240213", "symbol": "029780", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_quality_score": 50, "PBR_repricing_score": 45, "capital_buffer_score": 45, "payout_execution_score": 40, "revenue_mix_score": 40, "risk_cost_control_score": 40, "recurring_profit_score": 40, "relative_strength_score": 60, "valuation_blowoff_risk_score": 45, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"ROE_quality_score": 50, "PBR_repricing_score": 45, "capital_buffer_score": 45, "payout_execution_score": 40, "revenue_mix_score": 40, "risk_cost_control_score": 40, "recurring_profit_score": 40, "relative_strength_score": 60, "valuation_blowoff_risk_score": 55, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 75, "4C_watch_score": 25}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable + local 4B/ROE-payout bridge watch", "changed_components": ["ROE_quality_score", "capital_buffer_score", "payout_execution_score", "revenue_mix_score", "risk_cost_control_score", "recurring_profit_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C21 requires financial value-up MFE to convert into ROE quality, capital buffer, payout execution, recurring profit, revenue mix and risk-cost control before clean Stage2/Green.", "MFE_90D_pct": 14.92, "MAE_90D_pct": -1.8, "score_return_alignment_label": "card_finance_capital_return_MFE_positive_but_payout_ROE_bridge_required", "current_profile_verdict": "current_profile_partially_correct_controlled_MAE_but_payout_bridge_needed"}
{"row_type": "case", "case_id": "R6L87-C21-03", "symbol": "377300", "company_name": "카카오페이", "round": "R6", "loop": 87, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_HOLDCO_CARD_DIGITAL_FINANCE_ROE_PBR_PAYOUT_CAPITAL_BUFFER_REVENUE_MIX_BRIDGE_VS_VALUEUP_BETA_FADE", "case_type": "digital_finance_valueup_monetization_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R6L87-C21-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "digital_finance_MFE_then_deep_MAE_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_digital_finance_beta", "price_source": "Songdaiki/stock-web", "notes": "Digital-finance value-up theme should remain RiskWatch unless monetization, recurring profit quality, capital buffer and shareholder-return bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R6L87-C21-03-S2FP-20240213", "case_id": "R6L87-C21-03", "symbol": "377300", "company_name": "카카오페이", "round": "R6", "loop": 87, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_HOLDCO_CARD_DIGITAL_FINANCE_ROE_PBR_PAYOUT_CAPITAL_BUFFER_REVENUE_MIX_BRIDGE_VS_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail|ROE_quality_payout_capital_buffer_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "digital finance/payment platform value-up and monetization theme proxy without confirmed ROE, payout, capital buffer or profit-quality bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["ROE_PBR_valueup_proxy", "capital_return_proxy", "financial_beta_proxy"], "stage3_evidence_fields": ["ROE_quality", "capital_buffer", "payout_execution", "revenue_mix", "risk_cost_control", "recurring_profit_quality"], "stage4b_evidence_fields": ["financial_MFE_without_ROE_payout_bridge", "valueup_beta_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_ROE_payout_capital_buffer_or_profit_quality_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv", "profile_path": "atlas/symbol_profiles/377/377300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 48650, "MFE_30D_pct": 6.47, "MAE_30D_pct": -21.79, "MFE_90D_pct": 6.47, "MAE_90D_pct": -44.91, "MFE_180D_pct": 6.47, "MAE_180D_pct": -54.88, "peak_date": "2024-02-15", "peak_price": 51800, "drawdown_after_peak_pct": -57.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "digital_finance_valueup_MFE_rejected_without_ROE_monetization_capital_buffer_profit_bridge", "four_b_evidence_type": ["financial_valueup_MFE_without_ROE_payout_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_ROE_payout_capital_or_profit_break", "trigger_outcome_label": "digital_finance_MFE_then_deep_MAE_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_digital_finance_beta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R6L87-C21-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L87-C21-03", "trigger_id": "R6L87-C21-03-S2FP-20240213", "symbol": "377300", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_quality_score": 10, "PBR_repricing_score": 35, "capital_buffer_score": 10, "payout_execution_score": 0, "revenue_mix_score": 15, "risk_cost_control_score": 10, "recurring_profit_score": 5, "relative_strength_score": 25, "valuation_blowoff_risk_score": 80, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 85, "4C_watch_score": 50}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"ROE_quality_score": 0, "PBR_repricing_score": 35, "capital_buffer_score": 0, "payout_execution_score": 0, "revenue_mix_score": 15, "risk_cost_control_score": 0, "recurring_profit_score": 0, "relative_strength_score": 25, "valuation_blowoff_risk_score": 80, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 95, "4C_watch_score": 70}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Digital-finance value-up RiskWatch", "changed_components": ["ROE_quality_score", "capital_buffer_score", "payout_execution_score", "revenue_mix_score", "risk_cost_control_score", "recurring_profit_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C21 requires financial value-up MFE to convert into ROE quality, capital buffer, payout execution, recurring profit, revenue mix and risk-cost control before clean Stage2/Green.", "MFE_90D_pct": 6.47, "MAE_90D_pct": -44.91, "score_return_alignment_label": "digital_finance_MFE_then_deep_MAE_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_digital_finance_beta"}
{"row_type": "shadow_weight", "axis": "C21_financial_ROE_quality_payout_capital_buffer_profit_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Financial value-up/PBR rerating requires ROE quality, capital buffer, payout execution, revenue mix, recurring profit and risk-cost control; digital-finance beta MFE without monetization/profit bridge fades into high MAE.", "backtest_effect": "keeps 071050/029780 with ROE-payout bridge watch; demotes 377300 digital-finance value-up false positive", "trigger_ids": "R6L87-C21-01-S2A-20240213|R6L87-C21-02-S2A-20240213|R6L87-C21-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R6", "loop": 87, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["digital_finance_valueup_false_positive_high_MAE", "ROE_quality_payout_capital_buffer_bridge_required", "controlled_MAE_financial_positive_still_needs_payout_bridge", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_ROE_payout_capital_profit_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 24. Deferred Coding Agent Handoff Prompt

Use only `calibration_usable=true` rows. Do not treat `source_proxy_only/evidence_url_pending` rows as runtime promotion-ready. For C21, test a canonical guard requiring ROE quality, capital buffer, payout execution, revenue mix, recurring profit and risk-cost control before clean Stage2/Green.

## 25. Next Round State

```text
completed_round = R6
completed_loop = 87
next_round = R7
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 26. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
