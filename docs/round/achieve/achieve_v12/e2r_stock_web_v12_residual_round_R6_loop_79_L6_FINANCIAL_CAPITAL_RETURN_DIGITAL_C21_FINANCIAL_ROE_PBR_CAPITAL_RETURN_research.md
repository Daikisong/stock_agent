# E2R Stock-Web v12 Residual Research — R6 Loop 79 / L6 / C21

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 79,
  "computed_next_round": "R7",
  "computed_next_loop": 79,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "financial_ROE_PBR_capital_return_guardrail",
    "bank_holding_ROE_shareholder_return_bridge",
    "regional_bank_valueup_bounded_no_forced4B_boundary",
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

Previous completed state in this interactive run: R5 / loop 79.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 79
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
computed_next_round = R7
computed_next_loop = 79
```

R6 was routed to C21 because loop 78 used C22.  
This file tests bank-holding ROE/PBR and capital-return bridges rather than insurance reserve/rate-cycle bridges.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C21 concentration in:

```text
105560, 323410, UNKNOWN_SYMBOL, 086790, 006220
```

This run uses three different symbols:

```text
055550 / 신한지주 / bank-holdco ROE/PBR capital-return bridge
316140 / 우리금융지주 / bank-holdco PBR/capital-return bridge
138930 / BNK금융지주 / regional-bank value-up bounded no-forced-4B boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
All three rows show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C21 is not “금융주 value-up이 올랐다.”

The mechanism must pass through:

```text
ROE / PBR discount
→ capital buffer or CET1 comfort
→ dividend, buyback, treasury cancellation or payout policy
→ earnings quality and credit-cost stability
→ durable rerating
```

금융주의 자본환원은 물길이다.  
C21이 보려는 것은 그 물길이 단순 기대감이 아니라 자본비율, 배당·자사주, 이익 지속성으로 실제 흘러가는지다.

---

## Case 1 — Bank-holdco positive: 055550 / 신한지주

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is ROE/PBR value-up, capital buffer, dividend/buyback, treasury cancellation and earnings-quality bridge evidence.

```text
evidence_family = BANK_HOLDCO_ROE_PBR_VALUEUP_CAPITAL_BUFFER_DIVIDEND_BUYBACK_TREASURY_CANCELLATION_BRIDGE
case_role = positive_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 41,150
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv`:

```text
2024-02-01,41150,42500,41000,42500
2024-02-02,43350,45450,41500,45300
2024-02-26,42450,42500,39850,41350
2024-03-14,47650,51500,47600,51500
2024-07-29,58400,64200,58100,60700
2024-08-26,59800,64600,59500,61400
2024-10-31,53800,54200,51300,51300
```

### Backtest

```text
MFE_30D  = +25.15%
MAE_30D  = -3.16%
MFE_90D  = +25.15%
MAE_90D  = -3.16%
MFE_180D = +56.99%
MAE_180D = -3.16%
peak_180 = 64,600 on 2024-08-26
trough_180 = 39,850 on 2024-02-26
peak_to_later_drawdown = -20.59%
```

### Interpretation

This is a C21 bank-holdco capital-return positive.  
The MFE was large and entry-basis MAE was bounded.

Correct treatment:

```text
verified ROE/PBR + capital buffer + shareholder-return bridge → Stage2 possible
share-count validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Bank-holdco positive: 316140 / 우리금융지주

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is PBR discount, capital ratio, dividend/buyback, earnings quality and credit-cost bridge evidence.

```text
evidence_family = BANK_HOLDCO_VALUEUP_PBR_CAPITAL_RATIO_DIVIDEND_BUYBACK_EARNINGS_BRIDGE
case_role = positive_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 13,910
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv`:

```text
2024-02-01,13910,14490,13880,14410
2024-02-07,14200,14620,13600,14500
2024-03-15,15170,15500,15060,15230
2024-07-29,16110,16960,16010,16330
2024-08-05,14700,14780,13740,13980
2024-10-25,16700,17100,16660,17080
2024-10-31,15900,15940,15430,15430
```

### Backtest

```text
MFE_30D  = +9.27%
MAE_30D  = -2.23%
MFE_90D  = +11.43%
MAE_90D  = -2.23%
MFE_180D = +22.93%
MAE_180D = -2.23%
peak_180 = 17,100 on 2024-10-25
trough_180 = 13,600 on 2024-02-07
peak_to_later_drawdown = -9.77%
```

### Interpretation

This is a controlled-MAE C21 positive.  
The path supports bank-holdco PBR/capital-return rerating after source repair.

Correct treatment:

```text
verified capital buffer / shareholder return / earnings bridge → Stage2 possible
share-count validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Bounded regional-bank boundary: 138930 / BNK금융지주

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests regional-bank value-up beta with bounded MAE and recovery MFE but incomplete bridge proof.

```text
evidence_family = REGIONAL_BANK_VALUEUP_PBR_CAPITAL_RETURN_BETA_WITH_BOUNDED_MAE_AND_REQUIRES_ROE_CREDIT_COST_BRIDGE
case_role = overbearish_counterexample_bounded_no_forced4b_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,530
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv`:

```text
2024-02-01,7530,7960,7520,7870
2024-02-19,7950,8070,7880,8020
2024-02-28,7400,7520,7320,7500
2024-03-14,8040,8410,7960,8340
2024-08-26,10040,10340,10010,10210
2024-09-11,9920,9920,9090,9180
2024-10-02,8970,9090,8920,8980
```

### Backtest

```text
MFE_30D  = +7.57%
MAE_30D  = -2.79%
MFE_90D  = +11.69%
MAE_90D  = -2.79%
MFE_180D = +37.32%
MAE_180D = -2.79%
peak_180 = 10,340 on 2024-08-26
trough_180 = 7,320 on 2024-02-28
peak_to_later_drawdown = -13.73%
```

### Interpretation

This is not forced local 4B.  
It is also not durable Stage2 without ROE, credit-cost, capital-buffer and shareholder-return bridge verification.

Correct treatment:

```text
regional-bank value-up watch
bounded MAE + recovery MFE
→ no forced 4B
→ no durable Stage2 without ROE / capital-return / credit-cost bridge
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_valueup_no_forced_4B_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C21_financial_valueup_weight = true
do_not_treat_all_ROE_PBR_MFE_as_Green = true
do_not_force_4B_on_bounded_regional_bank_rows = true
do_not_convert_financial_drawdown_to_hard_4C_without_non_price_capital_credit_or_regulatory_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY
```

This fine archetype covers:

```text
1. bank-holdco ROE/PBR + capital-return bridge → Stage2 possible after source repair
2. bank-holdco PBR/capital-ratio bridge → Stage2 possible, share-count validated
3. regional-bank value-up beta with bounded MAE → RiskWatch / no durable Stage2 / no forced 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L79-C21-055550-SHINHAN-BANK-HOLDCO-CAPITAL-RETURN", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "79", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BankHoldcoROEPBRCapitalReturnBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should protect bank-holding positives when ROE/PBR rerating maps to capital buffer, dividend, buyback, treasury cancellation and earnings-quality bridge. Shinhan produced large MFE with bounded entry-basis MAE, but raw share-count changes inside the window require validation before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE, PBR, capital buffer, credit-cost, dividend, buyback, treasury-cancellation and earnings-quality bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L79-C21-316140-WOORI-BANK-HOLDCO-CAPITAL-RETURN", "symbol": "316140", "company_name": "우리금융지주", "round": "R6", "loop": "79", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BankHoldcoPBRCapitalReturnBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should preserve bank-holdco capital-return rows when PBR discount, capital ratio, shareholder-return policy, earnings durability and buyback/cancellation evidence are visible. Woori Financial produced a controlled-MAE MFE path, but share-count changes inside the raw shard require validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE, PBR, capital buffer, credit-cost, dividend, buyback, treasury-cancellation and earnings-quality bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L79-C21-138930-BNK-REGIONAL-BANK-VALUEUP-BOUNDARY", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "79", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-RegionalBankValueupCapitalReturnBoundedNoForced4BWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should avoid forcing regional-bank value-up rows into 4B when entry-basis MAE is bounded and recovery MFE is meaningful. BNK needs ROE, credit-cost, capital buffer and shareholder-return source repair before Stage2, but price action alone does not support hard local 4B.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE, PBR, capital buffer, credit-cost, dividend, buyback, treasury-cancellation and earnings-quality bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L79-C21-055550-SHINHAN-BANK-HOLDCO-CAPITAL-RETURN", "case_id": "R6L79-C21-055550-SHINHAN-BANK-HOLDCO-CAPITAL-RETURN", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "79", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail", "trigger_type": "Stage2-Actionable-BankHoldcoROEPBRCapitalReturnBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 41150.0, "evidence_available_at_that_date": "BANK_HOLDCO_ROE_PBR_VALUEUP_CAPITAL_BUFFER_DIVIDEND_BUYBACK_TREASURY_CANCELLATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SHINHAN_FINANCIAL_2024_ROE_PBR_CAPITAL_BUFFER_DIVIDEND_BUYBACK_TREASURY_CANCELLATION_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_valueup_candidate", "capital_buffer_or_CET1_candidate", "shareholder_return_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "earnings_quality_or_credit_cost_bridge_candidate"], "stage4b_evidence_fields": ["financial_valueup_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.15, "MFE_90D_pct": 25.15, "MFE_180D_pct": 56.99, "MAE_30D_pct": -3.16, "MAE_90D_pct": -3.16, "MAE_180D_pct": -3.16, "peak_date": "2024-08-26", "peak_price": 64600.0, "drawdown_after_peak_pct": -20.59, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_capital_return_ROE_or_credit_cost_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_capital_buffer_loss_credit_cost_shock_regulatory_issue_or_return_cancellation", "trigger_outcome_label": "positive_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C21 should protect bank-holding positives when ROE/PBR rerating maps to capital buffer, dividend, buyback, treasury cancellation and earnings-quality bridge. Shinhan produced large MFE with bounded entry-basis MAE, but raw share-count changes inside the window require validation before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_BANK_HOLDCO_055550_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L79-C21-316140-WOORI-BANK-HOLDCO-CAPITAL-RETURN", "case_id": "R6L79-C21-316140-WOORI-BANK-HOLDCO-CAPITAL-RETURN", "symbol": "316140", "company_name": "우리금융지주", "round": "R6", "loop": "79", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail", "trigger_type": "Stage2-Actionable-BankHoldcoPBRCapitalReturnBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 13910.0, "evidence_available_at_that_date": "BANK_HOLDCO_VALUEUP_PBR_CAPITAL_RATIO_DIVIDEND_BUYBACK_EARNINGS_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WOORI_FINANCIAL_2024_VALUEUP_PBR_CAPITAL_RATIO_DIVIDEND_BUYBACK_EARNINGS_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_valueup_candidate", "capital_buffer_or_CET1_candidate", "shareholder_return_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "earnings_quality_or_credit_cost_bridge_candidate"], "stage4b_evidence_fields": ["financial_valueup_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv", "profile_path": "atlas/symbol_profiles/316/316140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.27, "MFE_90D_pct": 11.43, "MFE_180D_pct": 22.93, "MAE_30D_pct": -2.23, "MAE_90D_pct": -2.23, "MAE_180D_pct": -2.23, "peak_date": "2024-10-25", "peak_price": 17100.0, "drawdown_after_peak_pct": -9.77, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_capital_return_ROE_or_credit_cost_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_capital_buffer_loss_credit_cost_shock_regulatory_issue_or_return_cancellation", "trigger_outcome_label": "positive_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C21 should preserve bank-holdco capital-return rows when PBR discount, capital ratio, shareholder-return policy, earnings durability and buyback/cancellation evidence are visible. Woori Financial produced a controlled-MAE MFE path, but share-count changes inside the raw shard require validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_BANK_HOLDCO_316140_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L79-C21-138930-BNK-REGIONAL-BANK-VALUEUP-BOUNDARY", "case_id": "R6L79-C21-138930-BNK-REGIONAL-BANK-VALUEUP-BOUNDARY", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "79", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail", "trigger_type": "RiskWatch-RegionalBankValueupCapitalReturnBoundedNoForced4BWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7530.0, "evidence_available_at_that_date": "REGIONAL_BANK_VALUEUP_PBR_CAPITAL_RETURN_BETA_WITH_BOUNDED_MAE_AND_REQUIRES_ROE_CREDIT_COST_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:BNK_FINANCIAL_2024_REGIONAL_BANK_VALUEUP_PBR_CAPITAL_RETURN_ROE_CREDIT_COST_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_valueup_candidate", "capital_buffer_or_CET1_candidate", "shareholder_return_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "earnings_quality_or_credit_cost_bridge_candidate"], "stage4b_evidence_fields": ["financial_valueup_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.57, "MFE_90D_pct": 11.69, "MFE_180D_pct": 37.32, "MAE_30D_pct": -2.79, "MAE_90D_pct": -2.79, "MAE_180D_pct": -2.79, "peak_date": "2024-08-26", "peak_price": 10340.0, "drawdown_after_peak_pct": -13.73, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_capital_return_ROE_or_credit_cost_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_capital_buffer_loss_credit_cost_shock_regulatory_issue_or_return_cancellation", "trigger_outcome_label": "overbearish_counterexample_bounded_no_forced4b_with_sharecount_validation", "current_profile_verdict": "C21 should avoid forcing regional-bank value-up rows into 4B when entry-basis MAE is bounded and recovery MFE is meaningful. BNK needs ROE, credit-cost, capital buffer and shareholder-return source repair before Stage2, but price action alone does not support hard local 4B.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_BANK_HOLDCO_138930_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L79-C21-055550-SHINHAN-BANK-HOLDCO-CAPITAL-RETURN", "trigger_id": "TRG_R6L79-C21-055550-SHINHAN-BANK-HOLDCO-CAPITAL-RETURN", "symbol": "055550", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_score": 14, "capital_buffer_score": 14, "shareholder_return_score": 14, "earnings_quality_score": 12, "credit_cost_risk_score": 6, "relative_strength_score": 13, "execution_risk_score": 9, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"ROE_PBR_score": 16, "capital_buffer_score": 16, "shareholder_return_score": 16, "earnings_quality_score": 14, "credit_cost_risk_score": 7, "relative_strength_score": 12, "execution_risk_score": 10, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["ROE_PBR_score", "capital_buffer_score", "shareholder_return_score", "earnings_quality_score", "credit_cost_risk_score", "sharecount_validation_risk"], "component_delta_explanation": "Reward only verified ROE/PBR, capital buffer, shareholder return, earnings quality and credit-cost bridge; avoid forced 4B when value-up beta has bounded MAE and recovery MFE but lacks complete bridge proof.", "MFE_90D_pct": 25.15, "MAE_90D_pct": -3.16, "score_return_alignment_label": "bank_holdco_capital_return_positive_with_lifecycle_4b", "current_profile_verdict": "C21 should protect bank-holding positives when ROE/PBR rerating maps to capital buffer, dividend, buyback, treasury cancellation and earnings-quality bridge. Shinhan produced large MFE with bounded entry-basis MAE, but raw share-count changes inside the window require validation before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L79-C21-316140-WOORI-BANK-HOLDCO-CAPITAL-RETURN", "trigger_id": "TRG_R6L79-C21-316140-WOORI-BANK-HOLDCO-CAPITAL-RETURN", "symbol": "316140", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_score": 14, "capital_buffer_score": 14, "shareholder_return_score": 14, "earnings_quality_score": 12, "credit_cost_risk_score": 6, "relative_strength_score": 6, "execution_risk_score": 9, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"ROE_PBR_score": 16, "capital_buffer_score": 16, "shareholder_return_score": 16, "earnings_quality_score": 14, "credit_cost_risk_score": 7, "relative_strength_score": 12, "execution_risk_score": 10, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["ROE_PBR_score", "capital_buffer_score", "shareholder_return_score", "earnings_quality_score", "credit_cost_risk_score", "sharecount_validation_risk"], "component_delta_explanation": "Reward only verified ROE/PBR, capital buffer, shareholder return, earnings quality and credit-cost bridge; avoid forced 4B when value-up beta has bounded MAE and recovery MFE but lacks complete bridge proof.", "MFE_90D_pct": 11.43, "MAE_90D_pct": -2.23, "score_return_alignment_label": "bank_holdco_capital_return_positive_with_lifecycle_4b", "current_profile_verdict": "C21 should preserve bank-holdco capital-return rows when PBR discount, capital ratio, shareholder-return policy, earnings durability and buyback/cancellation evidence are visible. Woori Financial produced a controlled-MAE MFE path, but share-count changes inside the raw shard require validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L79-C21-138930-BNK-REGIONAL-BANK-VALUEUP-BOUNDARY", "trigger_id": "TRG_R6L79-C21-138930-BNK-REGIONAL-BANK-VALUEUP-BOUNDARY", "symbol": "138930", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_score": 8, "capital_buffer_score": 8, "shareholder_return_score": 7, "earnings_quality_score": 5, "credit_cost_risk_score": 10, "relative_strength_score": 13, "execution_risk_score": 12, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no forced 4B", "raw_component_scores_after": {"ROE_PBR_score": 7, "capital_buffer_score": 7, "shareholder_return_score": 6, "earnings_quality_score": 4, "credit_cost_risk_score": 11, "relative_strength_score": 7, "execution_risk_score": 11, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / bounded no-forced-4B", "changed_components": ["ROE_PBR_score", "capital_buffer_score", "shareholder_return_score", "earnings_quality_score", "credit_cost_risk_score", "sharecount_validation_risk"], "component_delta_explanation": "Reward only verified ROE/PBR, capital buffer, shareholder return, earnings quality and credit-cost bridge; avoid forced 4B when value-up beta has bounded MAE and recovery MFE but lacks complete bridge proof.", "MFE_90D_pct": 11.69, "MAE_90D_pct": -2.79, "score_return_alignment_label": "regional_bank_valueup_bounded_no_forced4b", "current_profile_verdict": "C21 should avoid forcing regional-bank value-up rows into 4B when entry-basis MAE is bounded and recovery MFE is meaningful. BNK needs ROE, credit-cost, capital buffer and shareholder-return source repair before Stage2, but price action alone does not support hard local 4B."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 79, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_SHARECOUNT_BRIDGE_VS_REGIONAL_BANK_BETA_BOUNDARY", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 C21 bank/financial-holdco symbols outside top-covered 105560/323410/086790/006220 set, +3 Shinhan/Woori/BNK capital-return trigger families, +2 bank-holdco positives, +1 regional-bank bounded no-forced-4B boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 79, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "axis": "bank_holdco_ROE_PBR_capital_return_sharecount_bridge_vs_regional_bank_beta_boundary", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C21 should split verified bank-holdco ROE/PBR/capital-return rerating from generic financial value-up beta. Stage2 requires ROE/PBR discount, capital buffer, dividend/buyback/cancellation, earnings-quality and credit-cost bridge. If MFE fades and post-peak drawdown opens without bridge refresh, route to local 4B-watch. Bounded regional-bank value-up rows should remain RiskWatch/no forced 4B until non-price bridge breaks.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["055550", "316140", "138930"], "share_count_validation_required": ["055550", "316140", "138930"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 79, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_valueup_no_forced_4B_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C21 needs ROE/PBR, capital buffer, shareholder-return and earnings-quality proof. Shinhan and Woori show bank-holdco capital-return positives after source repair and share-count validation; BNK shows a regional-bank value-up boundary where bounded MAE and recovery MFE block forced 4B but source repair is still required before durable Stage2."}
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
055550:
  name = 신한지주
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

316140:
  name = 우리금융지주
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

138930:
  name = BNK금융지주 from 2015-04-21, BS금융지주 before that
  corporate_action_candidate_dates = 2014-07-25, 2016-02-05
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C21 rows are source_proxy_only / evidence_url_pending.
All three rows also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C21 rule-shape discovery,
but coding-agent promotion requires non-proxy ROE, PBR, capital buffer, credit-cost, dividend, buyback, treasury-cancellation and earnings-quality evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R6/C21 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and all three rows need share-count validation.

Candidate axis:
bank_holdco_ROE_PBR_capital_return_sharecount_bridge_vs_regional_bank_beta_boundary

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 055550, 316140 and 138930.
4. Validate share-count changes inside the selected window for all three rows.
5. Keep generic C21 value-up/financial capital-return weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - ROE/PBR rerating premise is explicit,
   - capital buffer or CET1 comfort is visible,
   - dividend / buyback / treasury-cancellation bridge exists,
   - earnings quality and credit-cost bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is financial value-up beta only,
   - capital-return/earnings/credit-cost evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not force local 4B when regional-bank value-up rows have bounded MAE and no confirmed capital/credit break.
9. Do not convert local 4B-watch into full 4B/4C without non-price capital buffer loss, credit-cost shock, regulatory issue, shareholder-return cancellation or earnings-quality break.
10. Emit before/after diagnostics and reject if verified bank-holdco capital-return positives or bounded regional-bank rows are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 79
next_round = R7
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

