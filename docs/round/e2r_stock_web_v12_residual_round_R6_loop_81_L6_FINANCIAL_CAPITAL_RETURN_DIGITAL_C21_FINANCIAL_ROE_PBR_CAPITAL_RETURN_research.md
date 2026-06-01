# E2R Stock-Web v12 Residual Research — R6 Loop 81 / L6 / C21

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 81,
  "computed_next_round": "R7",
  "computed_next_loop": 81,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "financial_ROE_PBR_capital_return_guardrail",
    "brokerage_trading_volume_ROE_capital_return_bridge",
    "small_brokerage_valueup_theme_fade_boundary",
    "share_count_validation_queue_creation",
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
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R5 / loop 81.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 81
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
computed_next_round = R7
computed_next_loop = 81
```

R6 was routed to C21 because loop 80 R6 used C22 insurance.  
This file tests securities/brokerage ROE-PBR and capital-return bridges rather than insurance CSM/reserve rate-cycle rows.

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

This run uses three different securities/brokerage symbols outside that top-covered set:

```text
005940 / NH투자증권 / brokerage capital-return and ROE-PBR bridge
039490 / 키움증권 / retail brokerage trading-volume platform bridge
001510 / SK증권 / small brokerage value-up theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
005940 and 039490 show share-count changes inside the selected 2024 shard and require coding-agent validation before runtime promotion.
```

## Research thesis

C21 is not “금융 value-up이 올랐다.”

The mechanism must pass through:

```text
ROE / PBR / value-up premise
→ shareholder return policy
→ brokerage trading volume or financial earnings driver
→ capital buffer
→ earnings durability
→ durable rerating
```

증권주 value-up은 배당 문구가 아니라 거래대금, 자본완충, ROE, 주주환원이라는 네 개의 톱니가 맞물리는 기계다.

---

## Case 1 — Brokerage capital-return positive: 005940 / NH투자증권

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is dividend/buyback or payout policy, trading volume, retail brokerage, IB earnings, capital buffer and ROE/PBR bridge evidence.

```text
evidence_family = BROKERAGE_VALUEUP_CAPITAL_RETURN_DIVIDEND_BUYBACK_TRADING_VOLUME_IB_RETAIL_BROKERAGE_ROE_BRIDGE
case_role = positive_brokerage_capital_return_ROE_bridge_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 10,480
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv`:

```text
2024-02-01,10480,11150,10480,11130
2024-02-19,11590,11820,11550,11770
2024-03-13,12130,13000,12110,12840
2024-03-14,12850,13100,12730,13060
2024-07-24,13400,13570,13350,13500
2024-08-01,13860,14400,13760,14170
2024-08-05,13220,13220,12600,12710
2024-09-25,14170,14170,13120,13220
```

### Backtest

```text
MFE_30D  = +25.00%
MAE_30D  = +0.00%
MFE_90D  = +25.00%
MAE_90D  = +0.00%
MFE_180D = +37.40%
MAE_180D = +0.00%
peak_180 = 14,400 on 2024-08-01
trough_180 = 10,480 on 2024-02-01
peak_to_later_drawdown = -12.50%
```

### Interpretation

This is a C21 brokerage capital-return positive.  
The MFE was strong and entry-basis MAE was effectively absent.

Correct treatment:

```text
verified capital return / trading-volume / earnings / ROE bridge → Stage2-Yellow possible
share-count validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Retail brokerage platform positive: 039490 / 키움증권

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is retail brokerage trading volume, customer asset quality, platform earnings, credit balance, capital return and ROE/PBR bridge evidence.

```text
evidence_family = RETAIL_BROKERAGE_TRADING_VOLUME_PLATFORM_CUSTOMER_ASSET_ROE_CAPITAL_RETURN_EARNINGS_BRIDGE
case_role = positive_retail_brokerage_ROE_capital_return_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 96,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv`:

```text
2024-02-01,96100,108200,96100,107600
2024-02-23,122700,127500,121200,126400
2024-03-05,130100,135900,130000,134800
2024-03-15,133800,136600,129600,131300
2024-08-05,123500,124000,115200,118500
2024-08-26,137000,142400,136300,140500
2024-10-16,135500,140700,135500,139000
```

### Backtest

```text
MFE_30D  = +42.14%
MAE_30D  = +0.00%
MFE_90D  = +42.14%
MAE_90D  = +0.00%
MFE_180D = +48.18%
MAE_180D = +0.00%
peak_180 = 142,400 on 2024-08-26
trough_180 = 96,100 on 2024-02-01
peak_to_later_drawdown = -18.82%
```

### Interpretation

This is a C21 retail brokerage/platform positive.  
The price path says the value-up/ROE bridge deserves protection after source repair, not blanket overblocking.

Correct treatment:

```text
verified trading volume / customer asset / platform earnings / capital-return bridge → Stage2-Yellow possible
share-count validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 001510 / SK증권

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests small brokerage value-up beta without enough ROE, capital-return and earnings bridge.

```text
evidence_family = SMALL_BROKERAGE_VALUEUP_THEME_WITH_WEAK_ROE_CAPITAL_RETURN_EARNINGS_BRIDGE
case_role = counterexample_small_brokerage_valueup_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 625
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001510/2024.csv`:

```text
2024-02-01,625,655,624,647
2024-02-19,664,669,663,665
2024-03-14,626,632,623,632
2024-04-16,595,597,591,591
2024-08-05,536,551,496,501
2024-09-04,620,630,540,540
2024-10-25,502,509,501,501
```

### Backtest

```text
MFE_30D  = +7.04%
MAE_30D  = -0.16%
MFE_90D  = +7.04%
MAE_90D  = -5.44%
MFE_180D = +7.04%
MAE_180D = -20.64%
peak_180 = 669 on 2024-02-19
trough_180 = 496 on 2024-08-05
peak_to_later_drawdown = -25.86%
```

### Interpretation

This is a C21 false-positive / local-4B boundary.  
The small-brokerage value-up theme did not validate durable ROE or capital-return rerating.

Correct treatment:

```text
small brokerage value-up theme beta
→ no verified ROE / payout / earnings bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
ROE_PBR_capital_return_bridge_required = strengthen
brokerage_volume_earnings_bridge_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C21_financial_valueup_weight = true
do_not_treat_all_brokerage_MFE_as_Green = true
do_not_ingest_sharecount_changed_brokerage_rows_without_validation = true
do_not_convert_brokerage_drawdown_to_hard_4C_without_non_price_credit_capital_regulatory_or_earnings_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE
```

This fine archetype covers:

```text
1. securities capital-return / ROE-PBR bridge → Stage2-Yellow possible after source repair
2. retail brokerage trading-volume platform bridge → Stage2-Yellow possible after source repair and share-count validation
3. small brokerage value-up beta without ROE/capital-return bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L81-C21-005940-NH-INVESTMENT-BROKERAGE-CAPITAL-RETURN-BRIDGE", "symbol": "005940", "company_name": "NH투자증권", "round": "R6", "loop": "81", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BrokerageCapitalReturnROEPBRBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should protect securities/brokerage value-up positives when PBR/ROE rerating is backed by dividend or buyback policy, trading volume, retail brokerage, IB earnings and capital buffer. NH Investment had strong MFE with almost no entry-basis MAE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR, capital return, brokerage trading volume, customer asset, capital buffer and earnings bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L81-C21-039490-KIWOOM-BROKERAGE-TRADING-VOLUME-CAPITAL-RETURN", "symbol": "039490", "company_name": "키움증권", "round": "R6", "loop": "81", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-RetailBrokerageTradingVolumeROEPBRBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should allow brokerage platform positives when market turnover, customer asset quality, retail brokerage, credit balance, capital return and earnings bridge are visible. Kiwoom produced a very large MFE with controlled entry-basis MAE, but stock-web share count changes need validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR, capital return, brokerage trading volume, customer asset, capital buffer and earnings bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L81-C21-001510-SK-SECURITIES-SMALL-BROKERAGE-THEME-FADE", "symbol": "001510", "company_name": "SK증권", "round": "R6", "loop": "81", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE", "case_type": "financial_ROE_PBR_capital_return", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SmallBrokerageValueupThemeFadeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C21 should not treat small brokerage value-up theme beta as durable Stage2 unless ROE improvement, payout policy, trading-volume sensitivity, capital buffer and earnings bridge are visible. SK Securities had a small early MFE and then a persistent MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy ROE/PBR, capital return, brokerage trading volume, customer asset, capital buffer and earnings bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L81-C21-005940-NH-INVESTMENT-BROKERAGE-CAPITAL-RETURN-BRIDGE", "case_id": "R6L81-C21-005940-NH-INVESTMENT-BROKERAGE-CAPITAL-RETURN-BRIDGE", "symbol": "005940", "company_name": "NH투자증권", "round": "R6", "loop": "81", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail", "trigger_type": "Stage2-Actionable-BrokerageCapitalReturnROEPBRBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 10480.0, "evidence_available_at_that_date": "BROKERAGE_VALUEUP_CAPITAL_RETURN_DIVIDEND_BUYBACK_TRADING_VOLUME_IB_RETAIL_BROKERAGE_ROE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NH_INVESTMENT_SECURITIES_2024_VALUEUP_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_EARNINGS_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_or_valueup_candidate", "capital_return_candidate", "brokerage_trading_volume_earnings_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_asset_or_capital_buffer_candidate"], "stage4b_evidence_fields": ["financial_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005940/2024.csv", "profile_path": "atlas/symbol_profiles/005/005940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.0, "MFE_90D_pct": 25.0, "MFE_180D_pct": 37.4, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-08-01", "peak_price": 14400.0, "drawdown_after_peak_pct": -12.5, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_capital_return_trading_volume_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_credit_loss_capital_buffer_damage_regulatory_issue_payout_cut_or_earnings_break", "trigger_outcome_label": "positive_brokerage_capital_return_ROE_bridge_with_later_4b_watch", "current_profile_verdict": "C21 should protect securities/brokerage value-up positives when PBR/ROE rerating is backed by dividend or buyback policy, trading volume, retail brokerage, IB earnings and capital buffer. NH Investment had strong MFE with almost no entry-basis MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C21_BROKERAGE_CAPITAL_RETURN_005940_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L81-C21-039490-KIWOOM-BROKERAGE-TRADING-VOLUME-CAPITAL-RETURN", "case_id": "R6L81-C21-039490-KIWOOM-BROKERAGE-TRADING-VOLUME-CAPITAL-RETURN", "symbol": "039490", "company_name": "키움증권", "round": "R6", "loop": "81", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail", "trigger_type": "Stage2-Actionable-RetailBrokerageTradingVolumeROEPBRBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 96100.0, "evidence_available_at_that_date": "RETAIL_BROKERAGE_TRADING_VOLUME_PLATFORM_CUSTOMER_ASSET_ROE_CAPITAL_RETURN_EARNINGS_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KIWOOM_SECURITIES_2024_RETAIL_BROKERAGE_TRADING_VOLUME_PLATFORM_ROE_CAPITAL_RETURN_EARNINGS_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_or_valueup_candidate", "capital_return_candidate", "brokerage_trading_volume_earnings_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_asset_or_capital_buffer_candidate"], "stage4b_evidence_fields": ["financial_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv", "profile_path": "atlas/symbol_profiles/039/039490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.14, "MFE_90D_pct": 42.14, "MFE_180D_pct": 48.18, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-08-26", "peak_price": 142400.0, "drawdown_after_peak_pct": -18.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_capital_return_trading_volume_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_credit_loss_capital_buffer_damage_regulatory_issue_payout_cut_or_earnings_break", "trigger_outcome_label": "positive_retail_brokerage_ROE_capital_return_with_sharecount_validation", "current_profile_verdict": "C21 should allow brokerage platform positives when market turnover, customer asset quality, retail brokerage, credit balance, capital return and earnings bridge are visible. Kiwoom produced a very large MFE with controlled entry-basis MAE, but stock-web share count changes need validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C21_BROKERAGE_CAPITAL_RETURN_039490_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L81-C21-001510-SK-SECURITIES-SMALL-BROKERAGE-THEME-FADE", "case_id": "R6L81-C21-001510-SK-SECURITIES-SMALL-BROKERAGE-THEME-FADE", "symbol": "001510", "company_name": "SK증권", "round": "R6", "loop": "81", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|financial_ROE_PBR_capital_return_guardrail", "trigger_type": "Stage2-FalsePositive / SmallBrokerageValueupThemeFadeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 625.0, "evidence_available_at_that_date": "SMALL_BROKERAGE_VALUEUP_THEME_WITH_WEAK_ROE_CAPITAL_RETURN_EARNINGS_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SK_SECURITIES_2024_SMALL_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_EARNINGS_BRIDGE", "stage2_evidence_fields": ["ROE_PBR_or_valueup_candidate", "capital_return_candidate", "brokerage_trading_volume_earnings_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_asset_or_capital_buffer_candidate"], "stage4b_evidence_fields": ["financial_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001510/2024.csv", "profile_path": "atlas/symbol_profiles/001/001510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.04, "MFE_90D_pct": 7.04, "MFE_180D_pct": 7.04, "MAE_30D_pct": -0.16, "MAE_90D_pct": -5.44, "MAE_180D_pct": -20.64, "peak_date": "2024-02-19", "peak_price": 669.0, "drawdown_after_peak_pct": -25.86, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_financial_valueup_peak_if_ROE_capital_return_trading_volume_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_credit_loss_capital_buffer_damage_regulatory_issue_payout_cut_or_earnings_break", "trigger_outcome_label": "counterexample_small_brokerage_valueup_theme_local4b", "current_profile_verdict": "C21 should not treat small brokerage value-up theme beta as durable Stage2 unless ROE improvement, payout policy, trading-volume sensitivity, capital buffer and earnings bridge are visible. SK Securities had a small early MFE and then a persistent MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C21_BROKERAGE_CAPITAL_RETURN_001510_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L81-C21-005940-NH-INVESTMENT-BROKERAGE-CAPITAL-RETURN-BRIDGE", "trigger_id": "TRG_R6L81-C21-005940-NH-INVESTMENT-BROKERAGE-CAPITAL-RETURN-BRIDGE", "symbol": "005940", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_valueup_score": 14, "capital_return_score": 14, "brokerage_volume_score": 13, "earnings_bridge_score": 13, "capital_buffer_score": 12, "relative_strength_score": 12, "execution_risk_score": 10, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"ROE_PBR_valueup_score": 16, "capital_return_score": 16, "brokerage_volume_score": 15, "earnings_bridge_score": 15, "capital_buffer_score": 14, "relative_strength_score": 11, "execution_risk_score": 11, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["ROE_PBR_valueup_score", "capital_return_score", "brokerage_volume_score", "earnings_bridge_score", "capital_buffer_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ROE/PBR rerating, shareholder return, brokerage trading volume, earnings bridge and capital buffer; cap small-brokerage value-up theme beta when bridge fails to refresh.", "MFE_90D_pct": 25.0, "MAE_90D_pct": 0.0, "score_return_alignment_label": "brokerage_capital_return_positive_with_lifecycle_4b", "current_profile_verdict": "C21 should protect securities/brokerage value-up positives when PBR/ROE rerating is backed by dividend or buyback policy, trading volume, retail brokerage, IB earnings and capital buffer. NH Investment had strong MFE with almost no entry-basis MAE."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L81-C21-039490-KIWOOM-BROKERAGE-TRADING-VOLUME-CAPITAL-RETURN", "trigger_id": "TRG_R6L81-C21-039490-KIWOOM-BROKERAGE-TRADING-VOLUME-CAPITAL-RETURN", "symbol": "039490", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_valueup_score": 14, "capital_return_score": 14, "brokerage_volume_score": 13, "earnings_bridge_score": 13, "capital_buffer_score": 12, "relative_strength_score": 12, "execution_risk_score": 10, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"ROE_PBR_valueup_score": 16, "capital_return_score": 16, "brokerage_volume_score": 15, "earnings_bridge_score": 15, "capital_buffer_score": 14, "relative_strength_score": 11, "execution_risk_score": 11, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["ROE_PBR_valueup_score", "capital_return_score", "brokerage_volume_score", "earnings_bridge_score", "capital_buffer_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ROE/PBR rerating, shareholder return, brokerage trading volume, earnings bridge and capital buffer; cap small-brokerage value-up theme beta when bridge fails to refresh.", "MFE_90D_pct": 42.14, "MAE_90D_pct": 0.0, "score_return_alignment_label": "brokerage_capital_return_positive_with_lifecycle_4b", "current_profile_verdict": "C21 should allow brokerage platform positives when market turnover, customer asset quality, retail brokerage, credit balance, capital return and earnings bridge are visible. Kiwoom produced a very large MFE with controlled entry-basis MAE, but stock-web share count changes need validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L81-C21-001510-SK-SECURITIES-SMALL-BROKERAGE-THEME-FADE", "trigger_id": "TRG_R6L81-C21-001510-SK-SECURITIES-SMALL-BROKERAGE-THEME-FADE", "symbol": "001510", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"ROE_PBR_valueup_score": 5, "capital_return_score": 2, "brokerage_volume_score": 4, "earnings_bridge_score": 2, "capital_buffer_score": 3, "relative_strength_score": 3, "execution_risk_score": 23, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"ROE_PBR_valueup_score": 3, "capital_return_score": 1, "brokerage_volume_score": 2, "earnings_bridge_score": 1, "capital_buffer_score": 1, "relative_strength_score": 3, "execution_risk_score": 25, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["ROE_PBR_valueup_score", "capital_return_score", "brokerage_volume_score", "earnings_bridge_score", "capital_buffer_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified ROE/PBR rerating, shareholder return, brokerage trading volume, earnings bridge and capital buffer; cap small-brokerage value-up theme beta when bridge fails to refresh.", "MFE_90D_pct": 7.04, "MAE_90D_pct": -5.44, "score_return_alignment_label": "false_positive_small_brokerage_bridge_gap", "current_profile_verdict": "C21 should not treat small brokerage value-up theme beta as durable Stage2 unless ROE improvement, payout policy, trading-volume sensitivity, capital buffer and earnings bridge are visible. SK Securities had a small early MFE and then a persistent MAE path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 81, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_CAPITAL_RETURN_TRADING_VOLUME_ROE_PBR_BRIDGE_VS_SMALL_BROKERAGE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C21 brokerage/securities symbols outside top-covered 105560/323410/086790/006220 set, +3 NH/Kiwoom/SK Securities trigger families, +2 brokerage capital-return positives, +1 small brokerage local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 81, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "axis": "brokerage_capital_return_trading_volume_ROE_PBR_bridge_vs_small_brokerage_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C21 should split verified securities/brokerage ROE-PBR and capital-return rerating from generic value-up or small-brokerage theme beta. Stage2 requires ROE/PBR rerating premise, dividend/buyback or payout policy, trading-volume or platform earnings bridge, capital buffer and earnings durability. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["005940", "039490", "001510"], "share_count_validation_required": ["005940", "039490"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 81, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "existing_axis_strengthened": ["stage2_required_bridge", "ROE_PBR_capital_return_bridge_required", "brokerage_volume_earnings_bridge_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C21 needs financial value-up to map into ROE/PBR, shareholder return, brokerage trading volume, earnings durability and capital-buffer proof. NH Investment and Kiwoom show brokerage capital-return positives after source repair; SK Securities shows small brokerage value-up theme fading into local 4B."}
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
005940:
  name = NH투자증권 from 2015-01-20
  corporate_action_candidate_dates = 1999-04-14, 1999-11-01, 2000-01-31, 2011-12-08, 2015-01-20
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

039490:
  name = 키움증권 from 2006-01-31
  corporate_action_candidate_dates = 2008-12-24
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

001510:
  name = SK증권 from 1998-01-21
  corporate_action_candidate_dates = 1998-03-28, 1999-01-08, 1999-08-27, 1999-10-21, 2018-12-24
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C21 rows are source_proxy_only / evidence_url_pending.
005940 and 039490 require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C21 brokerage/financial value-up rule-shape discovery,
but coding-agent promotion requires non-proxy ROE/PBR, capital return, brokerage trading volume, customer asset, capital buffer and earnings evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R6/C21 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 005940/039490 need share-count validation.

Candidate axis:
brokerage_capital_return_trading_volume_ROE_PBR_bridge_vs_small_brokerage_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 005940, 039490 and 001510.
4. Validate 005940 and 039490 share-count changes inside the selected window.
5. Keep generic C21 financial value-up weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - ROE/PBR or value-up premise is explicit,
   - dividend / buyback / payout policy is visible,
   - brokerage trading volume or platform earnings bridge exists,
   - capital buffer is credible,
   - earnings durability is visible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is financial value-up or small brokerage theme beta only,
   - capital-return / trading-volume / ROE / earnings evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price credit loss, capital-buffer damage, regulatory issue, payout cut or earnings-quality break.
9. Emit before/after diagnostics and reject if verified brokerage capital-return positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 81
next_round = R7
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

