# E2R Stock-Web v12 Residual Research — R6 Loop 73 / L6 / C21

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 73,
  "computed_next_round": "R7",
  "computed_next_loop": 73,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
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

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## Round / scope resolution

Previous completed state in this interactive run: R5 / loop 73.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 73
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
computed_next_round = R7
computed_next_loop = 73
```

R6 was routed to C21 because loop 72 already covered C22 insurance rate/reserve.  
This run avoids the top-covered C21 symbols and tests lower-repeat bank/securities value-up routes.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C21 is concentrated in `105560`, `323410`, `UNKNOWN_SYMBOL`, `086790`, and `006220`.  
This run uses:

```text
316140 / 우리금융지주 / bank value-up capital-return bridge
024110 / 기업은행 / high-dividend low-PBR ROE bridge
006800 / 미래에셋증권 / brokerage value-up beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
316140 and 006800 have share-count changes inside the selected window and need validation before runtime promotion.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C21 is not “financial stocks went up.”

The mechanism is:

```text
low PBR / value-up attention
→ capital policy evidence
→ dividend, buyback, cancellation, CET1/capital discipline
→ ROE or distribution visibility
→ durable rerating
```

A low PBR screen is the map.  
Capital return is the road.  
Without the road, price beta can make dust but not a durable rerating.

---

## Case 1 — Positive after source and share-count repair: 316140 / 우리금융지주

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is shareholder-return, buyback/cancellation, dividend, CET1/capital discipline and ROE bridge evidence.

```text
evidence_family = BANK_VALUEUP_ROE_PBR_BUYBACK_CANCELLATION_DIVIDEND_BRIDGE
case_role = positive_with_sharecount_validation
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
```

### Backtest

```text
MFE_30D  = +11.43%
MAE_30D  = -2.23%
MFE_90D  = +16.68%
MAE_90D  = -2.23%
MFE_180D = +21.93%
MAE_180D = -2.23%
peak_180 = 16,960 on 2024-07-29
trough_180 = 13,600 on 2024-02-07
peak_to_later_drawdown = -18.99%
```

### Interpretation

This is a C21 positive-shaped path.  
MAE stayed controlled, and the rerating moved beyond a one-day value-up spike.

But because share count changes inside the window, this row should be promoted only after the coding-agent validates whether that change is the capital-return bridge itself or a data artifact.

---

## Case 2 — Positive slow anchor: 024110 / 기업은행

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is high dividend, low PBR, stable ROE, capital discipline and state-bank shareholder-return policy evidence.

```text
evidence_family = STATE_BANK_HIGH_DIVIDEND_LOW_PBR_ROE_CAPITAL_RETURN_BRIDGE
case_role = positive_slow
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 12,530
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv`:

```text
2024-02-01,12530,13240,12530,13130
2024-02-19,13740,14230,13740,14020
2024-03-15,15700,16010,15250,15250
2024-08-05,13520,13560,12790,12910
```

### Backtest

```text
MFE_30D  = +27.77%
MAE_30D  = +0.00%
MFE_90D  = +27.77%
MAE_90D  = +0.00%
MFE_180D = +27.77%
MAE_180D = +0.00%
peak_180 = 16,010 on 2024-03-15
trough_180 = 12,530 on 2024-02-01
peak_to_later_drawdown = -20.11%
```

### Interpretation

This is the cleanest C21 path in this set.  
The MFE arrived without entry-basis MAE. It supports a slower bank value-up route where high dividend and ROE/PBR evidence matters more than headline beta.

---

## Case 3 — Counterexample / RiskWatch: 006800 / 미래에셋증권

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests brokerage/value-up beta without enough recurring ROE or capital-return bridge.

```text
evidence_family = SECURITIES_VALUEUP_BROKERAGE_BETA_WITH_WEAK_ROE_CAPITAL_RETURN_BRIDGE
case_role = counterexample_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,830
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv`:

```text
2024-02-01,7830,8300,7830,8290
2024-02-23,9080,9200,8900,8950
2024-03-15,8110,8430,8020,8020
2024-08-05,7250,7250,6600,6660
```

### Backtest

```text
MFE_30D  = +17.50%
MAE_30D  = +0.00%
MFE_90D  = +17.50%
MAE_90D  = -15.71%
MFE_180D = +17.50%
MAE_180D = -15.71%
peak_180 = 9,200 on 2024-02-23
trough_180 = 6,600 on 2024-08-05
peak_to_later_drawdown = -28.26%
```

### Interpretation

This is not a catastrophic failure.  
It is the C21 warning case: brokerage beta can move with value-up attention, but if recurring ROE and capital-return proof do not refresh, it should not remain durable Green.

Because share count changes inside the window, this is also a validation row.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C21_valueup_weight = true
do_not_treat_all_low_PBR_financial_beta_as_Green = true
do_not_convert_brokerage_fade_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA
```

This fine archetype covers:

```text
1. bank value-up + dividend/buyback/cancellation/ROE bridge → Stage2 possible after source repair
2. high-dividend low-PBR bank rerating → slow Stage2 possible
3. brokerage value-up beta without recurring ROE/capital-return bridge → false Stage2 / RiskWatch-local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE", "symbol": "316140", "company_name": "우리금융지주", "round": "R6", "loop": "73", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "case_type": "financial_roe_pbr_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BankValueupCapitalReturn", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should allow Stage2 when low-PBR bank rerating is backed by shareholder-return, buyback/cancellation, dividend and ROE bridge. Woori produced controlled MAE and later MFE, but share-count change inside the window needs coding-agent validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR/capital-return evidence and share-count validation required before runtime promotion."}
{"row_type": "case", "case_id": "R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "73", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "case_type": "financial_roe_pbr_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-HighDividendPBRBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should include slower high-dividend/value-up bank paths when dividend yield, low PBR, capital discipline and stable ROE support the rerating. IBK produced strong MFE with essentially no entry-basis MAE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR/capital-return evidence and share-count validation required before runtime promotion."}
{"row_type": "case", "case_id": "R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE", "symbol": "006800", "company_name": "미래에셋증권", "round": "R6", "loop": "73", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "case_type": "financial_roe_pbr_capital_return", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BrokerageValueupBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should not treat brokerage/value-up beta as durable Green unless recurring ROE, capital return, treasury-stock cancellation or distribution bridge is verified. Mirae generated MFE but later faded and needs local 4B/RiskWatch rather than durable Stage2.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR/capital-return evidence and share-count validation required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE", "case_id": "R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE", "symbol": "316140", "company_name": "우리금융지주", "round": "R6", "loop": "73", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-BankValueupCapitalReturn", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 13910.0, "evidence_available_at_that_date": "BANK_VALUEUP_ROE_PBR_BUYBACK_CANCELLATION_DIVIDEND_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WOORI_FINANCIAL_2024_VALUEUP_BUYBACK_CANCELLATION_DIVIDEND_ROE_BRIDGE", "stage2_evidence_fields": ["low_pbr", "roe_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "shareholder_return_bridge_candidate"], "stage4b_evidence_fields": ["later_local_4b_if_capital_return_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv", "profile_path": "atlas/symbol_profiles/316/316140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.43, "MFE_90D_pct": 16.68, "MFE_180D_pct": 21.93, "MAE_30D_pct": -2.23, "MAE_90D_pct": -2.23, "MAE_180D_pct": -2.23, "peak_date": "2024-07-29", "peak_price": 16960.0, "drawdown_after_peak_pct": -18.99, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_capital_return_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_roe_or_capital_return_break", "trigger_outcome_label": "positive_with_sharecount_validation", "current_profile_verdict": "C21 should allow Stage2 when low-PBR bank rerating is backed by shareholder-return, buyback/cancellation, dividend and ROE bridge. Woori produced controlled MAE and later MFE, but share-count change inside the window needs coding-agent validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_VALUEUP_316140_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE", "case_id": "R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "73", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-HighDividendPBRBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 12530.0, "evidence_available_at_that_date": "STATE_BANK_HIGH_DIVIDEND_LOW_PBR_ROE_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:IBK_2024_HIGH_DIVIDEND_LOW_PBR_ROE_VALUEUP_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["low_pbr", "roe_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "shareholder_return_bridge_candidate"], "stage4b_evidence_fields": ["later_local_4b_if_capital_return_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv", "profile_path": "atlas/symbol_profiles/024/024110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.77, "MFE_90D_pct": 27.77, "MFE_180D_pct": 27.77, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-03-15", "peak_price": 16010.0, "drawdown_after_peak_pct": -20.11, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_capital_return_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_roe_or_capital_return_break", "trigger_outcome_label": "positive_slow", "current_profile_verdict": "C21 should include slower high-dividend/value-up bank paths when dividend yield, low PBR, capital discipline and stable ROE support the rerating. IBK produced strong MFE with essentially no entry-basis MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C21_VALUEUP_024110_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE", "case_id": "R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE", "symbol": "006800", "company_name": "미래에셋증권", "round": "R6", "loop": "73", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / BrokerageValueupBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7830.0, "evidence_available_at_that_date": "SECURITIES_VALUEUP_BROKERAGE_BETA_WITH_WEAK_ROE_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MIRAE_ASSET_SECURITIES_2024_BROKERAGE_VALUEUP_BETA_WEAK_ROE_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["low_pbr", "roe_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "shareholder_return_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006800/2024.csv", "profile_path": "atlas/symbol_profiles/006/006800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.5, "MFE_90D_pct": 17.5, "MFE_180D_pct": 17.5, "MAE_30D_pct": 0.0, "MAE_90D_pct": -15.71, "MAE_180D_pct": -15.71, "peak_date": "2024-02-23", "peak_price": 9200.0, "drawdown_after_peak_pct": -28.26, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_capital_return_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_roe_or_capital_return_break", "trigger_outcome_label": "counterexample_with_sharecount_validation", "current_profile_verdict": "C21 should not treat brokerage/value-up beta as durable Green unless recurring ROE, capital return, treasury-stock cancellation or distribution bridge is verified. Mirae generated MFE but later faded and needs local 4B/RiskWatch rather than durable Stage2.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C21_VALUEUP_006800_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE", "trigger_id": "TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE", "symbol": "316140", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 15, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capital_return_score": 15, "roe_visibility_score": 12}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 14, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capital_return_score": 16, "roe_visibility_score": 13}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["capital_return_score", "roe_visibility_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified ROE/PBR/capital-return bridge; cap brokerage/value-up beta when shareholder-return evidence is weak or stale.", "MFE_90D_pct": 16.68, "MAE_90D_pct": -2.23, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C21 should allow Stage2 when low-PBR bank rerating is backed by shareholder-return, buyback/cancellation, dividend and ROE bridge. Woori produced controlled MAE and later MFE, but share-count change inside the window needs coding-agent validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE", "trigger_id": "TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE", "symbol": "024110", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 15, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capital_return_score": 15, "roe_visibility_score": 12}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 9, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 14, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capital_return_score": 16, "roe_visibility_score": 13}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["capital_return_score", "roe_visibility_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified ROE/PBR/capital-return bridge; cap brokerage/value-up beta when shareholder-return evidence is weak or stale.", "MFE_90D_pct": 27.77, "MAE_90D_pct": 0.0, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C21 should include slower high-dividend/value-up bank paths when dividend yield, low PBR, capital discipline and stable ROE support the rerating. IBK produced strong MFE with essentially no entry-basis MAE."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE", "trigger_id": "TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE", "symbol": "006800", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 15, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capital_return_score": 6, "roe_visibility_score": 5}, "weighted_score_before": 56, "stage_label_before": "Stage2-FalsePositive / RiskWatch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 6, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capital_return_score": 4, "roe_visibility_score": 4}, "weighted_score_after": 45, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["capital_return_score", "roe_visibility_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified ROE/PBR/capital-return bridge; cap brokerage/value-up beta when shareholder-return evidence is weak or stale.", "MFE_90D_pct": 17.5, "MAE_90D_pct": -15.71, "score_return_alignment_label": "false_positive_capital_return_bridge_gap", "current_profile_verdict": "C21 should not treat brokerage/value-up beta as durable Green unless recurring ROE, capital return, treasury-stock cancellation or distribution bridge is verified. Mirae generated MFE but later faded and needs local 4B/RiskWatch rather than durable Stage2."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 73, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C21 symbols, +3 bank/securities value-up trigger families, +2 bank capital-return positives, +1 brokerage beta fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 73, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "axis": "bank_and_securities_valueup_capital_return_bridge_vs_price_only_brokerage_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C21 should split verified ROE/PBR/capital-return bridge from generic value-up or brokerage beta. Stage2 requires dividend, buyback/cancellation, CET1/capital discipline, ROE visibility or distribution-policy evidence. If price-only value-up beta fades without bridge refresh, route to RiskWatch/local 4B.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["316140", "024110", "006800"], "share_count_validation_required": ["316140", "006800"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 73, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C21 should not be blanket value-up beta. Woori and IBK show bank capital-return/PBR positives, while Mirae Securities shows brokerage beta fading without enough recurring ROE/capital-return bridge. Share-count changes require validation."}
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
316140:
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false by stock-web profile
  share_count_change_inside_window = true → coding-agent validation required

024110:
  corporate_action_candidate_dates = 1998-10-27, 1998-11-05, 2000-02-02, 2003-12-24
  selected window = 2024-02-01~D+180
  contamination = false
  share_count_change_inside_window = false

006800:
  corporate_action_candidate_dates = 1999-09-27, 1999-10-14, 2000-05-22, 2001-11-23, 2011-11-16, 2017-01-20
  selected window = 2024-02-01~D+180
  contamination = false by stock-web profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C21 rows are source_proxy_only / evidence_url_pending.
316140 and 006800 also require share-count validation.
This MD is useful for stock-web path calibration and C21 rule-shape discovery,
but coding-agent promotion requires non-proxy ROE/PBR/capital-return evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R6/C21 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
bank_and_securities_valueup_capital_return_bridge_vs_price_only_brokerage_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 316140, 024110 and 006800.
4. Validate share-count changes for 316140 and 006800.
5. Keep generic C21 value-up weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - low PBR/valuation gap is explicit,
   - ROE or distribution capacity is visible,
   - dividend, buyback/cancellation, CET1/capital discipline or shareholder-return policy is verified,
   - MAE remains controlled.
7. Consider RiskWatch/local 4B when:
   - the trigger is price-only financial/value-up beta,
   - capital-return or ROE evidence fails to refresh,
   - post-peak drawdown opens,
   - brokerage beta fades without recurring earnings bridge.
8. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
9. Emit before/after diagnostics and reject if verified bank capital-return positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 73
next_round = R7
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

