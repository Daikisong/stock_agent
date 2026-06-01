# E2R Stock-Web v12 Residual Research — R6 Loop 75 / L6 / C21

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 75,
  "computed_next_round": "R7",
  "computed_next_loop": 75,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "financial_capital_return_guardrail",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R5 / loop 75.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 75
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
computed_next_round = R7
computed_next_loop = 75
```

R6 was routed to C21 because loop 74 used C22 insurance and C21 is the remaining financial capital-return bucket.  
This file avoids the top-covered mega-bank names and tests regional financial holdings plus a digital-finance PBR-beta counterexample.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C21 is concentrated in:

```text
105560, 323410, UNKNOWN_SYMBOL, 086790, 006220
```

This run uses three different symbols:

```text
175330 / JB금융지주 / regional financial ROE capital-return bridge
138930 / BNK금융지주 / regional bank capital-return bridge
377300 / 카카오페이 / digital-finance PBR beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
All three show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C21 is not “financial stock went up.”

The mechanism must be:

```text
low PBR / value-up attention
→ ROE quality or profitability bridge
→ capital buffer
→ dividend / buyback / treasury cancellation
→ durable rerating
```

A PBR discount is the closed spring.  
Capital return is the latch that lets it expand.

---

## Case 1 — Positive: 175330 / JB금융지주

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is ROE quality, payout path, treasury cancellation, capital buffer and shareholder-return evidence.

```text
evidence_family = REGIONAL_BANK_ROE_LOW_PBR_SHAREHOLDER_RETURN_TREASURY_CANCELLATION_BRIDGE
case_role = positive_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 11,520
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv`:

```text
2024-02-01,11520,12790,11520,12580
2024-03-05,13580,14100,13580,13900
2024-04-11,11400,12370,11390,12180
2024-06-03,14620,14890,14270,14330
2024-10-25,17630,18710,17630,18290
```

### Backtest

```text
MFE_30D  = +22.40%
MAE_30D  = +0.00%
MFE_90D  = +29.25%
MAE_90D  = -1.13%
MFE_180D = +62.41%
MAE_180D = -1.13%
peak_180 = 18,710 on 2024-10-25
trough_180 = 11,390 on 2024-04-11
peak_to_later_drawdown = -2.51%
```

### Interpretation

This is a strong C21 regional-bank positive.  
The price path is a textbook controlled-MAE rerating. But runtime promotion should wait for non-proxy capital-return evidence and share-count validation.

---

## Case 2 — Positive slow bridge: 138930 / BNK금융지주

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is regional-bank ROE, dividend/buyback, treasury cancellation, capital buffer and value-up evidence.

```text
evidence_family = REGIONAL_BANK_LOW_PBR_VALUEUP_ROE_DIVIDEND_TREASURY_BRIDGE
case_role = positive_slow_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,530
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv`:

```text
2024-02-01,7530,7960,7520,7870
2024-03-14,8040,8410,7960,8340
2024-05-20,8670,8750,8550,8590
2024-08-26,10040,10340,10010,10210
2024-09-25,9680,9700,9040,9040
```

### Backtest

```text
MFE_30D  = +11.69%
MAE_30D  = -2.79%
MFE_90D  = +16.20%
MAE_90D  = -2.79%
MFE_180D = +37.32%
MAE_180D = -2.79%
peak_180 = 10,340 on 2024-08-26
trough_180 = 7,320 on 2024-02-28
peak_to_later_drawdown = -12.57%
```

### Interpretation

This is the slower C21 positive.  
The key is not explosive MFE but low drawdown and persistent rerating.

C21 should preserve this kind of regional-bank compounder after source repair and share-count validation.

---

## Case 3 — Counterexample / local 4B: 377300 / 카카오페이

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests digital-finance/value-up PBR beta without ROE, profitability or capital-return bridge.

```text
evidence_family = DIGITAL_FINANCE_VALUEUP_PBR_BETA_WITH_WEAK_ROE_CAPITAL_RETURN_BRIDGE
case_role = counterexample_digital_finance_beta_local4b
trigger_date = 2024-01-10
entry_date = 2024-01-11
entry_price = 48,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv`:

```text
2024-01-11,48500,60200,48400,58000
2024-02-29,45400,45750,44050,44050
2024-04-11,36400,36800,35500,35500
2024-06-13,30300,30750,29250,29400
2024-08-05,24600,24850,21950,22600
2024-10-25,23800,23900,22850,23050
```

### Backtest

```text
MFE_30D  = +24.12%
MAE_30D  = -9.18%
MFE_90D  = +24.12%
MAE_90D  = -40.82%
MFE_180D = +24.12%
MAE_180D = -54.74%
peak_180 = 60,200 on 2024-01-11
trough_180 = 21,950 on 2024-08-05
peak_to_later_drawdown = -63.54%
```

### Interpretation

This is the C21 false-positive trap.  
The initial value-up/digital-finance move was tradable, but it did not have a durable ROE or capital-return bridge.

Correct treatment:

```text
digital finance PBR beta
→ no ROE/capital-return bridge
→ local 4B-watch
```

not Green.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C21_financial_valueup_weight = true
do_not_treat_all_low_PBR_financial_MFE_as_Green = true
do_not_convert_financial_beta_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE
```

This fine archetype covers:

```text
1. regional bank ROE / dividend / treasury cancellation bridge → Stage2 possible after source repair
2. regional financial holding low-MAE value-up rerating → Stage2 possible, share-count validation required
3. digital-finance PBR beta without profitability/capital-return bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "75", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "case_type": "financial_roe_pbr_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-RegionalFinancialROECapitalReturnBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should allow Stage2 when low-PBR/value-up attention connects to durable ROE, payout, treasury cancellation or capital-return bridge. JB Financial produced high MFE with controlled entry-basis MAE; share-count movement should be validated before runtime promotion.", "current_profile_verdict": "source_repair_and_sharecount_validation_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE, PBR, payout, buyback/cancellation, profitability and capital-buffer evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "75", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "case_type": "financial_roe_pbr_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-RegionalBankCapitalReturnBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should keep slower regional-bank capital return winners when ROE stability, dividend path, treasury cancellation and CET1/capital buffer support the rerating. BNK had modest early MFE but a durable low-MAE rerating path; share-count validation remains required.", "current_profile_verdict": "source_repair_and_sharecount_validation_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE, PBR, payout, buyback/cancellation, profitability and capital-buffer evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE", "symbol": "377300", "company_name": "카카오페이", "round": "R6", "loop": "75", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "case_type": "financial_roe_pbr_capital_return", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DigitalFinancePBRBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should not treat digital-finance/value-up beta as durable Stage2 unless ROE inflection, capital return, profitability and shareholder-return bridge are visible. KakaoPay produced an event spike but then entered a long high-MAE decline, making it a false Stage2/local 4B row.", "current_profile_verdict": "source_repair_and_sharecount_validation_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE, PBR, payout, buyback/cancellation, profitability and capital-buffer evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE", "case_id": "R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "75", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_capital_return_guardrail", "trigger_type": "Stage2-Actionable-RegionalFinancialROECapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11520.0, "evidence_available_at_that_date": "REGIONAL_BANK_ROE_LOW_PBR_SHAREHOLDER_RETURN_TREASURY_CANCELLATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:JB_FINANCIAL_2024_ROE_PBR_SHAREHOLDER_RETURN_TREASURY_CANCELLATION_PAYOUT_BRIDGE", "stage2_evidence_fields": ["low_PBR_valueup", "ROE_or_profitability_bridge_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "buyback_dividend_or_treasury_cancellation_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown", "digital_finance_beta_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.4, "MFE_90D_pct": 29.25, "MFE_180D_pct": 62.41, "MAE_30D_pct": 0.0, "MAE_90D_pct": -1.13, "MAE_180D_pct": -1.13, "peak_date": "2024-10-25", "peak_price": 18710.0, "drawdown_after_peak_pct": -2.51, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_profitability_capital_regulatory_or_credit_break", "trigger_outcome_label": "positive_with_sharecount_validation", "current_profile_verdict": "C21 should allow Stage2 when low-PBR/value-up attention connects to durable ROE, payout, treasury cancellation or capital-return bridge. JB Financial produced high MFE with controlled entry-basis MAE; share-count movement should be validated before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_FINANCIAL_VALUEUP_175330_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN", "case_id": "R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "75", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_capital_return_guardrail", "trigger_type": "Stage2-Actionable-RegionalBankCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7530.0, "evidence_available_at_that_date": "REGIONAL_BANK_LOW_PBR_VALUEUP_ROE_DIVIDEND_TREASURY_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:BNK_FINANCIAL_2024_LOW_PBR_VALUEUP_ROE_DIVIDEND_TREASURY_CAPITAL_BUFFER_BRIDGE", "stage2_evidence_fields": ["low_PBR_valueup", "ROE_or_profitability_bridge_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "buyback_dividend_or_treasury_cancellation_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown", "digital_finance_beta_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.69, "MFE_90D_pct": 16.2, "MFE_180D_pct": 37.32, "MAE_30D_pct": -2.79, "MAE_90D_pct": -2.79, "MAE_180D_pct": -2.79, "peak_date": "2024-08-26", "peak_price": 10340.0, "drawdown_after_peak_pct": -12.57, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_profitability_capital_regulatory_or_credit_break", "trigger_outcome_label": "positive_slow_with_sharecount_validation", "current_profile_verdict": "C21 should keep slower regional-bank capital return winners when ROE stability, dividend path, treasury cancellation and CET1/capital buffer support the rerating. BNK had modest early MFE but a durable low-MAE rerating path; share-count validation remains required.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_FINANCIAL_VALUEUP_138930_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE", "case_id": "R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE", "symbol": "377300", "company_name": "카카오페이", "round": "R6", "loop": "75", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_capital_return_guardrail", "trigger_type": "Stage2-FalsePositive / DigitalFinancePBRBetaFade", "trigger_date": "2024-01-10", "entry_date": "2024-01-11", "entry_price": 48500.0, "evidence_available_at_that_date": "DIGITAL_FINANCE_VALUEUP_PBR_BETA_WITH_WEAK_ROE_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KAKAOPAY_2024_DIGITAL_FINANCE_VALUEUP_ROE_PROFITABILITY_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["low_PBR_valueup", "ROE_or_profitability_bridge_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "buyback_dividend_or_treasury_cancellation_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown", "digital_finance_beta_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv", "profile_path": "atlas/symbol_profiles/377/377300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.12, "MFE_90D_pct": 24.12, "MFE_180D_pct": 24.12, "MAE_30D_pct": -9.18, "MAE_90D_pct": -40.82, "MAE_180D_pct": -54.74, "peak_date": "2024-01-11", "peak_price": 60200.0, "drawdown_after_peak_pct": -63.54, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_profitability_capital_regulatory_or_credit_break", "trigger_outcome_label": "counterexample_digital_finance_beta_local4b", "current_profile_verdict": "C21 should not treat digital-finance/value-up beta as durable Stage2 unless ROE inflection, capital return, profitability and shareholder-return bridge are visible. KakaoPay produced an event spike but then entered a long high-MAE decline, making it a false Stage2/local 4B row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_FINANCIAL_VALUEUP_377300_2024-01-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE", "trigger_id": "TRG_R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE", "symbol": "175330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_quality_score": 14, "PBR_valueup_score": 13, "capital_return_score": 14, "capital_buffer_score": 12, "profitability_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 5, "dilution_or_sharecount_validation_risk": 7, "source_confidence_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"ROE_quality_score": 16, "PBR_valueup_score": 12, "capital_return_score": 16, "capital_buffer_score": 14, "profitability_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 5, "dilution_or_sharecount_validation_risk": 9, "source_confidence_score": 2}, "weighted_score_after": 90, "stage_label_after": "Stage2/Green candidate after source repair + share-count validation", "changed_components": ["ROE_quality_score", "capital_return_score", "capital_buffer_score", "execution_risk_score", "dilution_or_sharecount_validation_risk"], "component_delta_explanation": "Reward only verified ROE quality, dividend/buyback/t treasury cancellation and capital buffer; cap digital-finance PBR beta when profitability and capital-return evidence are absent.", "MFE_90D_pct": 29.25, "MAE_90D_pct": -1.13, "score_return_alignment_label": "aligned_positive_with_sharecount_validation", "current_profile_verdict": "C21 should allow Stage2 when low-PBR/value-up attention connects to durable ROE, payout, treasury cancellation or capital-return bridge. JB Financial produced high MFE with controlled entry-basis MAE; share-count movement should be validated before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN", "trigger_id": "TRG_R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN", "symbol": "138930", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_quality_score": 14, "PBR_valueup_score": 13, "capital_return_score": 14, "capital_buffer_score": 12, "profitability_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 5, "dilution_or_sharecount_validation_risk": 7, "source_confidence_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"ROE_quality_score": 16, "PBR_valueup_score": 12, "capital_return_score": 16, "capital_buffer_score": 14, "profitability_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 5, "dilution_or_sharecount_validation_risk": 9, "source_confidence_score": 2}, "weighted_score_after": 90, "stage_label_after": "Stage2/Green candidate after source repair + share-count validation", "changed_components": ["ROE_quality_score", "capital_return_score", "capital_buffer_score", "execution_risk_score", "dilution_or_sharecount_validation_risk"], "component_delta_explanation": "Reward only verified ROE quality, dividend/buyback/t treasury cancellation and capital buffer; cap digital-finance PBR beta when profitability and capital-return evidence are absent.", "MFE_90D_pct": 16.2, "MAE_90D_pct": -2.79, "score_return_alignment_label": "aligned_positive_with_sharecount_validation", "current_profile_verdict": "C21 should keep slower regional-bank capital return winners when ROE stability, dividend path, treasury cancellation and CET1/capital buffer support the rerating. BNK had modest early MFE but a durable low-MAE rerating path; share-count validation remains required."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE", "trigger_id": "TRG_R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE", "symbol": "377300", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_quality_score": 3, "PBR_valueup_score": 8, "capital_return_score": 2, "capital_buffer_score": 3, "profitability_bridge_score": 2, "relative_strength_score": 7, "execution_risk_score": 18, "dilution_or_sharecount_validation_risk": 7, "source_confidence_score": 2}, "weighted_score_before": 53, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"ROE_quality_score": 2, "PBR_valueup_score": 4, "capital_return_score": 1, "capital_buffer_score": 2, "profitability_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 20, "dilution_or_sharecount_validation_risk": 9, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["ROE_quality_score", "capital_return_score", "capital_buffer_score", "execution_risk_score", "dilution_or_sharecount_validation_risk"], "component_delta_explanation": "Reward only verified ROE quality, dividend/buyback/t treasury cancellation and capital buffer; cap digital-finance PBR beta when profitability and capital-return evidence are absent.", "MFE_90D_pct": 24.12, "MAE_90D_pct": -40.82, "score_return_alignment_label": "false_positive_digital_finance_valueup_bridge_gap", "current_profile_verdict": "C21 should not treat digital-finance/value-up beta as durable Stage2 unless ROE inflection, capital return, profitability and shareholder-return bridge are visible. KakaoPay produced an event spike but then entered a long high-MAE decline, making it a false Stage2/local 4B row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 75, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C21 financial symbols outside top-covered mega-bank set, +3 regional-bank/digital-finance trigger families, +2 low-MAE capital-return positives, +1 digital-finance PBR beta fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 75, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "axis": "regional_financial_holding_roe_capital_return_vs_digital_finance_pbr_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C21 should split verified ROE/PBR capital-return rerating from generic financial or digital-finance PBR beta. Stage2 requires ROE quality, capital buffer, dividend, buyback, treasury cancellation or profitability bridge. If MFE fades and MAE/post-peak drawdown opens without the bridge, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["175330", "138930", "377300"], "share_count_validation_required": ["175330", "138930", "377300"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 75, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C21 needs ROE and capital-return proof. JB Financial and BNK Financial show regional financial holding positives after source repair and share-count validation; KakaoPay shows digital-finance/PBR beta fading into local 4B when profitability and capital-return bridge is absent."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
175330:
  corporate_action_candidate_dates = 2014-01-29, 2014-09-26, 2015-12-01, 2018-10-26
  selected window = 2024-02-01~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

138930:
  corporate_action_candidate_dates = 2014-07-25, 2016-02-05
  selected window = 2024-02-01~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

377300:
  corporate_action_candidate_dates = none
  selected window = 2024-01-11~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C21 rows are source_proxy_only / evidence_url_pending.
All three also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C21 rule-shape discovery,
but coding-agent promotion requires non-proxy ROE, PBR, payout, buyback/cancellation, profitability and capital-buffer evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R6/C21 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and share-count validation.

Candidate axis:
regional_financial_holding_roe_capital_return_vs_digital_finance_pbr_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 175330, 138930 and 377300.
4. Validate share-count changes inside each selected window.
5. Keep generic C21 financial value-up weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - ROE or profitability bridge is explicit,
   - capital buffer is visible,
   - dividend, buyback, treasury cancellation or shareholder-return bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is financial/digital low-PBR beta only,
   - ROE or capital-return evidence is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price profitability collapse, credit loss, capital impairment, regulatory or solvency break.
9. Emit before/after diagnostics and reject if verified regional-bank capital-return positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 75
next_round = R7
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

