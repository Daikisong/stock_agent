# E2R Stock-Web v12 Residual Research — R6 Loop 77 / L6 / C21

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 77,
  "computed_next_round": "R7",
  "computed_next_loop": 77,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "financial_valueup_capital_return_guardrail",
    "ROE_PBR_dividend_buyback_bridge_vs_valueup_beta",
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

Previous completed state in this interactive run: R5 / loop 77.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 77
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
computed_next_round = R7
computed_next_loop = 77
```

R6 was routed to C21 because loop 76 used C22.  
This file tests financial ROE/PBR and shareholder-return bridges while avoiding the top-covered KB/KakaoBank/Hana/Jeju concentration.

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
175330 / JB금융지주 / regional-bank ROE/PBR capital-return bridge
138930 / BNK금융지주 / slow regional-bank capital-return bridge
030210 / 다올투자증권 / brokerage value-up beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
175330 and 138930 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C21 is not “금융 value-up 주가가 올랐다.”

The mechanism must pass through:

```text
PBR discount / value-up attention
→ sustainable ROE and balance-sheet quality
→ CET1 or capital buffer
→ dividend, buyback or shareholder-return policy
→ durable rerating
```

금융주의 PBR 할인은 잠긴 금고처럼 보인다.  
C21이 보려는 것은 그 금고가 ROE, 자본비율, 배당·자사주라는 열쇠로 실제로 열리는지다.

---

## Case 1 — Positive with lifecycle watch: 175330 / JB금융지주

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is sustainable ROE, PBR discount, CET1/capital buffer, dividend/buyback and shareholder-return bridge evidence.

```text
evidence_family = REGIONAL_BANK_ROE_PBR_VALUEUP_DIVIDEND_BUYBACK_CAPITAL_RETURN_BRIDGE
case_role = positive_with_later_lifecycle_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 11,520
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv`:

```text
2024-02-01,11520,12790,11520,12580
2024-02-27,13390,13930,13100,13610
2024-08-05,14000,14000,12980,13480
2024-10-17,16280,17210,16240,17150
2024-10-25,17630,18710,17630,18290
2024-11-04,17850,17850,17320,17760
```

### Backtest

```text
MFE_30D  = +20.92%
MAE_30D  = +0.00%
MFE_90D  = +22.40%
MAE_90D  = +0.00%
MFE_180D = +62.41%
MAE_180D = +0.00%
peak_180 = 18,710 on 2024-10-25
trough_180 = 11,520 on 2024-02-01
peak_to_later_drawdown = -7.43%
```

### Interpretation

This is a clean C21 capital-return positive after source repair.  
The path shows high MFE and no entry-basis MAE.

Correct treatment:

```text
ROE/PBR + capital buffer + dividend/buyback verified → Stage2 possible
share-count validation first
lifecycle watch if shareholder-return bridge fades
```

---

## Case 2 — Slow positive with validation: 138930 / BNK금융지주

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is sustainable ROE, PBR discount, CET1/capital buffer, dividend policy and buyback/cancellation evidence.

```text
evidence_family = REGIONAL_BANK_VALUEUP_ROE_PBR_CET1_DIVIDEND_CAPITAL_RETURN_BRIDGE
case_role = positive_slow_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,530
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv`:

```text
2024-02-01,7530,7960,7520,7870
2024-02-19,7950,8070,7880,8020
2024-03-14,8040,8410,7960,8340
2024-08-05,9170,9400,8600,8720
2024-08-26,10040,10340,10010,10210
2024-09-25,9680,9700,9040,9040
```

### Backtest

```text
MFE_30D  = +7.17%
MAE_30D  = -0.80%
MFE_90D  = +11.69%
MAE_90D  = -2.79%
MFE_180D = +37.32%
MAE_180D = -2.79%
peak_180 = 10,340 on 2024-08-26
trough_180 = 7,320 on 2024-02-28
peak_to_later_drawdown = -12.57%
```

### Interpretation

This is a slow regional-bank rerating row.  
It should not be overblocked only because it is not explosive.

Correct treatment:

```text
Stage2-Yellow possible after source repair
share-count validation required
protect if dividend/buyback/capital-return bridge is confirmed
```

---

## Case 3 — Counterexample / local 4B-watch: 030210 / 다올투자증권

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests brokerage / value-up beta without enough ROE recovery, balance-sheet quality and capital-return bridge.

```text
evidence_family = BROKERAGE_VALUEUP_BETA_WITH_WEAK_ROE_CAPITAL_RETURN_BALANCE_SHEET_BRIDGE
case_role = counterexample_brokerage_valueup_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,545
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/030/030210/2024.csv`:

```text
2024-02-01,3545,3800,3545,3775
2024-03-05,3660,3905,3655,3815
2024-03-08,3740,3915,3725,3785
2024-04-08,3130,3150,3050,3095
2024-08-05,3110,3140,2880,2890
2024-11-07,2795,2825,2750,2760
```

### Backtest

```text
MFE_30D  = +10.16%
MAE_30D  = -2.12%
MFE_90D  = +10.44%
MAE_90D  = -13.96%
MFE_180D = +10.44%
MAE_180D = -22.43%
peak_180 = 3,915 on 2024-03-08
trough_180 = 2,750 on 2024-11-07
peak_to_later_drawdown = -29.76%
```

### Interpretation

This is the C21 brokerage beta boundary.  
It did not validate a durable capital-return rerating.

Correct treatment:

```text
brokerage / value-up beta
→ no ROE / balance-sheet / capital-return bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C21_financial_valueup_weight = true
do_not_treat_all_valueup_MFE_as_Green = true
do_not_convert_financial_drawdown_to_hard_4C_without_non_price_capital_or_credit_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE
```

This fine archetype covers:

```text
1. regional-bank ROE/PBR + capital-return bridge → Stage2 possible after source repair
2. slow regional-bank capital-return bridge → Stage2-Yellow possible with share-count validation
3. brokerage value-up beta without ROE/capital bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "77", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-RegionalBankROEPBRCapitalReturnBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should allow regional-bank value-up positives when PBR discount, sustainable ROE, CET1/capital buffer, dividend/buyback and shareholder-return bridge are visible. JB Financial produced high MFE with essentially no entry-basis MAE; it should be protected after source repair while still requiring lifecycle monitoring if capital-return evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR, CET1/capital buffer, dividend/buyback, balance-sheet and shareholder-return evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "77", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-RegionalBankROEPBRCapitalReturnBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should preserve slow regional-financial rerating rows when sustainable ROE, PBR discount, CET1/capital buffer, dividend policy and capital-return bridge are visible. BNK produced slow controlled-MAE MFE and share-count movement that likely relates to capital policy, but runtime promotion requires share-count validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR, CET1/capital buffer, dividend/buyback, balance-sheet and shareholder-return evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE", "symbol": "030210", "company_name": "다올투자증권", "round": "R6", "loop": "77", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BrokerageValueupBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should not treat brokerage/value-up beta as durable Stage2 unless ROE recovery, capital buffer, shareholder return, balance-sheet risk reduction and earnings bridge are visible. Daol Investment had only a small MFE, then drifted into a prolonged drawdown, making it a local 4B-watch boundary rather than a capital-return Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR, CET1/capital buffer, dividend/buyback, balance-sheet and shareholder-return evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "case_id": "R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "77", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_valueup_capital_return_guardrail", "trigger_type": "Stage2-Actionable-RegionalBankROEPBRCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11520.0, "evidence_available_at_that_date": "REGIONAL_BANK_ROE_PBR_VALUEUP_DIVIDEND_BUYBACK_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:JB_FINANCIAL_2024_ROE_PBR_VALUEUP_DIVIDEND_BUYBACK_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_or_valueup_candidate", "capital_buffer_or_CET1_candidate", "dividend_buyback_capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "balance_sheet_or_shareholder_return_bridge_candidate"], "stage4b_evidence_fields": ["financial_valueup_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.92, "MFE_90D_pct": 22.4, "MFE_180D_pct": 62.41, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-10-25", "peak_price": 18710.0, "drawdown_after_peak_pct": -7.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_ROE_collapse_capital_buffer_break_credit_cost_loss_or_return_cancellation", "trigger_outcome_label": "positive_with_later_lifecycle_watch", "current_profile_verdict": "C21 should allow regional-bank value-up positives when PBR discount, sustainable ROE, CET1/capital buffer, dividend/buyback and shareholder-return bridge are visible. JB Financial produced high MFE with essentially no entry-basis MAE; it should be protected after source repair while still requiring lifecycle monitoring if capital-return evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_FINANCIAL_CAPRETURN_175330_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "case_id": "R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "77", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_valueup_capital_return_guardrail", "trigger_type": "Stage2-SlowPositive-RegionalBankROEPBRCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7530.0, "evidence_available_at_that_date": "REGIONAL_BANK_VALUEUP_ROE_PBR_CET1_DIVIDEND_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:BNK_FINANCIAL_2024_VALUEUP_ROE_PBR_CET1_DIVIDEND_BUYBACK_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_or_valueup_candidate", "capital_buffer_or_CET1_candidate", "dividend_buyback_capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "balance_sheet_or_shareholder_return_bridge_candidate"], "stage4b_evidence_fields": ["financial_valueup_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.17, "MFE_90D_pct": 11.69, "MFE_180D_pct": 37.32, "MAE_30D_pct": -0.8, "MAE_90D_pct": -2.79, "MAE_180D_pct": -2.79, "peak_date": "2024-08-26", "peak_price": 10340.0, "drawdown_after_peak_pct": -12.57, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_ROE_collapse_capital_buffer_break_credit_cost_loss_or_return_cancellation", "trigger_outcome_label": "positive_slow_with_sharecount_validation", "current_profile_verdict": "C21 should preserve slow regional-financial rerating rows when sustainable ROE, PBR discount, CET1/capital buffer, dividend policy and capital-return bridge are visible. BNK produced slow controlled-MAE MFE and share-count movement that likely relates to capital policy, but runtime promotion requires share-count validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_FINANCIAL_CAPRETURN_138930_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE", "case_id": "R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE", "symbol": "030210", "company_name": "다올투자증권", "round": "R6", "loop": "77", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_valueup_capital_return_guardrail", "trigger_type": "Stage2-FalsePositive / BrokerageValueupBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3545.0, "evidence_available_at_that_date": "BROKERAGE_VALUEUP_BETA_WITH_WEAK_ROE_CAPITAL_RETURN_BALANCE_SHEET_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DAOL_INVESTMENT_SECURITIES_2024_BROKERAGE_VALUEUP_ROE_BALANCE_SHEET_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_or_valueup_candidate", "capital_buffer_or_CET1_candidate", "dividend_buyback_capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "balance_sheet_or_shareholder_return_bridge_candidate"], "stage4b_evidence_fields": ["financial_valueup_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/030/030210/2024.csv", "profile_path": "atlas/symbol_profiles/030/030210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.16, "MFE_90D_pct": 10.44, "MFE_180D_pct": 10.44, "MAE_30D_pct": -2.12, "MAE_90D_pct": -13.96, "MAE_180D_pct": -22.43, "peak_date": "2024-03-08", "peak_price": 3915.0, "drawdown_after_peak_pct": -29.76, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_ROE_collapse_capital_buffer_break_credit_cost_loss_or_return_cancellation", "trigger_outcome_label": "counterexample_brokerage_valueup_beta_local4b", "current_profile_verdict": "C21 should not treat brokerage/value-up beta as durable Stage2 unless ROE recovery, capital buffer, shareholder return, balance-sheet risk reduction and earnings bridge are visible. Daol Investment had only a small MFE, then drifted into a prolonged drawdown, making it a local 4B-watch boundary rather than a capital-return Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C21_FINANCIAL_CAPRETURN_030210_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "trigger_id": "TRG_R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "symbol": "175330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_score": 14, "capital_buffer_score": 13, "dividend_buyback_score": 14, "shareholder_return_score": 13, "balance_sheet_quality_score": 12, "relative_strength_score": 13, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"ROE_PBR_score": 16, "capital_buffer_score": 15, "dividend_buyback_score": 16, "shareholder_return_score": 15, "balance_sheet_quality_score": 14, "relative_strength_score": 12, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["ROE_PBR_score", "capital_buffer_score", "dividend_buyback_score", "shareholder_return_score", "balance_sheet_quality_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ROE/PBR discount, CET1/capital buffer, dividend/buyback, balance-sheet quality and shareholder-return bridge; cap financial value-up beta when evidence fails to refresh.", "MFE_90D_pct": 22.4, "MAE_90D_pct": 0.0, "score_return_alignment_label": "financial_capital_return_positive_with_lifecycle_4b", "current_profile_verdict": "C21 should allow regional-bank value-up positives when PBR discount, sustainable ROE, CET1/capital buffer, dividend/buyback and shareholder-return bridge are visible. JB Financial produced high MFE with essentially no entry-basis MAE; it should be protected after source repair while still requiring lifecycle monitoring if capital-return evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "trigger_id": "TRG_R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "symbol": "138930", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_score": 14, "capital_buffer_score": 13, "dividend_buyback_score": 14, "shareholder_return_score": 13, "balance_sheet_quality_score": 12, "relative_strength_score": 13, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"ROE_PBR_score": 16, "capital_buffer_score": 15, "dividend_buyback_score": 16, "shareholder_return_score": 15, "balance_sheet_quality_score": 14, "relative_strength_score": 12, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["ROE_PBR_score", "capital_buffer_score", "dividend_buyback_score", "shareholder_return_score", "balance_sheet_quality_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ROE/PBR discount, CET1/capital buffer, dividend/buyback, balance-sheet quality and shareholder-return bridge; cap financial value-up beta when evidence fails to refresh.", "MFE_90D_pct": 11.69, "MAE_90D_pct": -2.79, "score_return_alignment_label": "financial_capital_return_positive_with_lifecycle_4b", "current_profile_verdict": "C21 should preserve slow regional-financial rerating rows when sustainable ROE, PBR discount, CET1/capital buffer, dividend policy and capital-return bridge are visible. BNK produced slow controlled-MAE MFE and share-count movement that likely relates to capital policy, but runtime promotion requires share-count validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE", "trigger_id": "TRG_R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE", "symbol": "030210", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_score": 5, "capital_buffer_score": 3, "dividend_buyback_score": 2, "shareholder_return_score": 2, "balance_sheet_quality_score": 3, "relative_strength_score": 4, "execution_risk_score": 19, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"ROE_PBR_score": 3, "capital_buffer_score": 2, "dividend_buyback_score": 1, "shareholder_return_score": 1, "balance_sheet_quality_score": 1, "relative_strength_score": 3, "execution_risk_score": 22, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 36, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["ROE_PBR_score", "capital_buffer_score", "dividend_buyback_score", "shareholder_return_score", "balance_sheet_quality_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ROE/PBR discount, CET1/capital buffer, dividend/buyback, balance-sheet quality and shareholder-return bridge; cap financial value-up beta when evidence fails to refresh.", "MFE_90D_pct": 10.44, "MAE_90D_pct": -13.96, "score_return_alignment_label": "false_positive_financial_valueup_bridge_gap", "current_profile_verdict": "C21 should not treat brokerage/value-up beta as durable Stage2 unless ROE recovery, capital buffer, shareholder return, balance-sheet risk reduction and earnings bridge are visible. Daol Investment had only a small MFE, then drifted into a prolonged drawdown, making it a local 4B-watch boundary rather than a capital-return Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 77, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C21 financial symbols outside top-covered KB/KakaoBank/Hana/Jeju set, +3 regional-bank/capital-return/brokerage-beta trigger families, +2 ROE-PBR capital-return positives, +1 brokerage value-up local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 77, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "axis": "regional_bank_ROE_PBR_capital_return_bridge_vs_brokerage_valueup_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C21 should split verified financial ROE/PBR capital-return rerating from generic value-up beta. Stage2 requires sustainable ROE, PBR discount, CET1/capital buffer, dividend/buyback/shareholder-return bridge and balance-sheet quality. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["175330", "138930", "030210"], "share_count_validation_required": ["175330", "138930"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 77, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C21 needs ROE/PBR and capital-return proof. JB Financial and BNK Financial show regional-bank capital-return positives after source repair; Daol Investment Securities shows brokerage/value-up beta fading into local 4B when ROE, balance-sheet and shareholder-return bridge are absent."}
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
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

138930:
  corporate_action_candidate_dates = 2014-07-25, 2016-02-05
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

030210:
  name = 다올투자증권 from 2022-04-06
  corporate_action_candidate_dates = 1997-01-03, 1999-05-24, 1999-07-30
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C21 rows are source_proxy_only / evidence_url_pending.
175330 and 138930 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C21 rule-shape discovery,
but coding-agent promotion requires non-proxy ROE/PBR, CET1/capital buffer, dividend/buyback, balance-sheet quality and shareholder-return evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R6/C21 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and two rows need share-count validation.

Candidate axis:
regional_bank_ROE_PBR_capital_return_bridge_vs_brokerage_valueup_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 175330, 138930 and 030210.
4. Validate 175330 and 138930 share-count changes inside the selected window.
5. Keep generic C21 financial value-up weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - PBR discount / value-up attention is explicit,
   - sustainable ROE and balance-sheet quality are visible,
   - CET1/capital buffer or risk buffer is credible,
   - dividend, buyback, cancellation or shareholder-return bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is financial/brokerage value-up beta only,
   - ROE/capital-return/balance-sheet evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -25~35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price ROE collapse, CET1/capital break, credit cost spike, shareholder-return cancellation, regulatory issue or solvency evidence.
9. Emit before/after diagnostics and reject if verified low-MAE regional-bank capital-return positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 77
next_round = R7
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

