# E2R Stock-Web v12 Residual Research — R6 Loop 78 / L6 / C22

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 78,
  "computed_next_round": "R7",
  "computed_next_loop": 78,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "insurance_rate_cycle_reserve_guardrail",
    "life_insurance_reserve_capital_return_bridge_vs_beta",
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

Previous completed state in this interactive run: R5 / loop 78.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 78
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
computed_next_round = R7
computed_next_loop = 78
```

R6 was routed to C22 because loop 77 used C21.  
This file tests life-insurance rate-cycle, CSM/reserve quality and capital-return bridges rather than generic financial value-up.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C22 is concentrated in:

```text
000810, 005830, 088350, 001450, 000400
```

This run uses three different symbols:

```text
032830 / 삼성생명 / life-insurance rate/reserve/capital-return bridge
082640 / 동양생명 / high-beta life-insurance reserve/capital-return bridge
085620 / 미래에셋생명 / life-insurance value-up beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C22 is not “보험주가 올랐다.”

The mechanism must pass through:

```text
rate cycle / insurance value-up attention
→ CSM or reserve quality
→ capital buffer and solvency comfort
→ dividend, buyback or shareholder-return bridge
→ earnings durability
→ durable rerating
```

보험주의 금리 사이클은 바람이다.  
C22가 보려는 것은 그 바람이 준비금, 자본비율, 배당·자사주, 이익 지속성이라는 돛을 실제로 밀어주는지다.

---

## Case 1 — Positive with lifecycle 4B: 032830 / 삼성생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is rate cycle, CSM/reserve quality, capital buffer, dividend/buyback and shareholder-return bridge evidence.

```text
evidence_family = LIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_BUFFER_DIVIDEND_BUYBACK_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 69,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv`:

```text
2024-02-01,69300,76800,68900,76000
2024-02-22,87800,93200,87100,92100
2024-02-28,91400,102900,89000,102900
2024-03-08,107200,108500,104200,105100
2024-04-19,77200,78000,76600,77300
2024-08-05,87400,88000,82500,84000
2024-11-01,102300,104900,101500,103800
```

### Backtest

```text
MFE_30D  = +56.57%
MAE_30D  = -0.58%
MFE_90D  = +56.57%
MAE_90D  = -0.58%
MFE_180D = +56.57%
MAE_180D = -0.58%
peak_180 = 108,500 on 2024-03-08
trough_180 = 68,900 on 2024-02-01
peak_to_later_drawdown = -29.40%
```

### Interpretation

This is the clean C22 life-insurance positive.  
The early move had high MFE and nearly no entry-basis MAE.

Correct treatment:

```text
verified reserve / capital buffer / shareholder-return bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — High-beta positive with lifecycle 4B: 082640 / 동양생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is reserve quality, rate-cycle leverage, capital buffer, shareholder-return and earnings bridge evidence.

```text
evidence_family = LIFE_INSURANCE_RATE_CYCLE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_HIGHBETA
case_role = positive_high_beta_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,925
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv`:

```text
2024-02-01,4925,5480,4810,5380
2024-03-08,6390,6500,6320,6350
2024-06-18,5240,6810,5140,6500
2024-07-31,7930,9440,7710,7970
2024-08-28,8500,8900,6900,6980
2024-10-02,5410,5410,5220,5260
2024-10-31,5940,6370,5900,6110
```

### Backtest

```text
MFE_30D  = +31.98%
MAE_30D  = -2.34%
MFE_90D  = +38.27%
MAE_90D  = -2.34%
MFE_180D = +91.68%
MAE_180D = -2.34%
peak_180 = 9,440 on 2024-07-31
trough_180 = 4,810 on 2024-02-01
peak_to_later_drawdown = -44.70%
```

### Interpretation

This is a high-beta C22 positive, not permanent Green.  
The MFE was very large, but the post-peak drawdown says reserve/capital-return evidence must refresh.

Correct treatment:

```text
Stage2 possible after source repair
high-beta lifecycle local 4B if reserve/capital/earnings bridge decays
```

---

## Case 3 — Counterexample / local 4B: 085620 / 미래에셋생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests life-insurance rate/value-up beta without enough reserve, capital-return and earnings bridge.

```text
evidence_family = LIFE_INSURANCE_RATE_CYCLE_THEME_WITH_WEAK_RESERVE_CAPITAL_RETURN_BRIDGE
case_role = counterexample_life_insurance_beta_local4b
trigger_date = 2024-01-30
entry_date = 2024-01-31
entry_price = 5,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv`:

```text
2024-01-31,5600,5800,5430,5780
2024-02-01,5670,6420,5610,5770
2024-02-06,6320,6500,6100,6240
2024-02-29,5070,5140,4750,4880
2024-03-20,4550,4560,4500,4500
2024-04-02,4535,4535,4425,4490
2024-06-27,4910,6140,4855,5350
```

### Backtest

```text
MFE_30D  = +16.07%
MAE_30D  = -19.55%
MFE_90D  = +16.07%
MAE_90D  = -20.98%
MFE_180D = +16.07%
MAE_180D = -20.98%
peak_180 = 6,500 on 2024-02-06
trough_180 = 4,425 on 2024-04-02
peak_to_later_drawdown = -31.92%
```

### Interpretation

This is the C22 false-positive boundary.  
The early MFE was tradable, but it did not validate durable reserve/capital-return rerating.

Correct treatment:

```text
life-insurance value-up beta
→ no verified reserve / capital-return / earnings bridge
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
```

### What this does not justify

```text
do_not_raise_generic_C22_insurance_beta_weight = true
do_not_treat_all_insurance_MFE_as_Green = true
do_not_convert_insurance_drawdown_to_hard_4C_without_non_price_reserve_or_capital_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE
```

This fine archetype covers:

```text
1. large-cap life-insurance reserve/capital-return bridge → Stage2 possible after source repair
2. high-beta life-insurance rate-cycle bridge → Stage2 possible, lifecycle-managed
3. life-insurance value-up beta without reserve/capital bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L78-C22-032830-SAMSUNG-LIFE-RATE-RESERVE-CAPITAL-RETURN", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "78", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-LifeInsuranceRateReserveCapitalReturnBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should allow life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback and shareholder-return bridge are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy rate cycle, CSM/reserve quality, capital buffer, dividend/buyback, shareholder-return and earnings bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L78-C22-082640-TONGYANG-LIFE-HIGHBETA-RESERVE-CAPITAL-RETURN", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": "78", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-HighBeta-LifeInsuranceReserveCapitalReturnBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 can allow high-beta life-insurance positives when reserve quality, rate-cycle leverage, capital buffer and shareholder-return bridge are explicit. Tong Yang Life produced very large MFE with low entry-basis MAE, but the post-peak drawdown shows high beta must be lifecycle-managed.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy rate cycle, CSM/reserve quality, capital buffer, dividend/buyback, shareholder-return and earnings bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L78-C22-085620-MIRAEASSET-LIFE-INSURANCE-BETA-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "78", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LifeInsuranceRateCycleBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should not treat life-insurance rate/value-up beta as durable Stage2 unless reserve quality, capital buffer, shareholder return and earnings bridge are visible. Mirae Asset Life had a tradable early MFE, then opened a high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy rate cycle, CSM/reserve quality, capital buffer, dividend/buyback, shareholder-return and earnings bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L78-C22-032830-SAMSUNG-LIFE-RATE-RESERVE-CAPITAL-RETURN", "case_id": "R6L78-C22-032830-SAMSUNG-LIFE-RATE-RESERVE-CAPITAL-RETURN", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "78", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-Actionable-LifeInsuranceRateReserveCapitalReturnBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 69300.0, "evidence_available_at_that_date": "LIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_BUFFER_DIVIDEND_BUYBACK_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SAMSUNG_LIFE_2024_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_DIVIDEND_BUYBACK_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_valueup_candidate", "CSM_reserve_capital_buffer_candidate", "shareholder_return_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "earnings_or_risk_loss_ratio_bridge_candidate"], "stage4b_evidence_fields": ["insurance_rate_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 56.57, "MFE_90D_pct": 56.57, "MFE_180D_pct": 56.57, "MAE_30D_pct": -0.58, "MAE_90D_pct": -0.58, "MAE_180D_pct": -0.58, "peak_date": "2024-03-08", "peak_price": 108500.0, "drawdown_after_peak_pct": -29.4, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_peak_if_reserve_capital_return_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_quality_break_capital_buffer_loss_regulatory_issue_or_return_cancellation", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C22 should allow life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback and shareholder-return bridge are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_032830_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L78-C22-082640-TONGYANG-LIFE-HIGHBETA-RESERVE-CAPITAL-RETURN", "case_id": "R6L78-C22-082640-TONGYANG-LIFE-HIGHBETA-RESERVE-CAPITAL-RETURN", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": "78", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-HighBeta-LifeInsuranceReserveCapitalReturnBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4925.0, "evidence_available_at_that_date": "LIFE_INSURANCE_RATE_CYCLE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_HIGHBETA", "evidence_source": "source_proxy_manual_verification_required:TONGYANG_LIFE_2024_RATE_CYCLE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_valueup_candidate", "CSM_reserve_capital_buffer_candidate", "shareholder_return_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "earnings_or_risk_loss_ratio_bridge_candidate"], "stage4b_evidence_fields": ["insurance_rate_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv", "profile_path": "atlas/symbol_profiles/082/082640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.98, "MFE_90D_pct": 38.27, "MFE_180D_pct": 91.68, "MAE_30D_pct": -2.34, "MAE_90D_pct": -2.34, "MAE_180D_pct": -2.34, "peak_date": "2024-07-31", "peak_price": 9440.0, "drawdown_after_peak_pct": -44.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_peak_if_reserve_capital_return_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_quality_break_capital_buffer_loss_regulatory_issue_or_return_cancellation", "trigger_outcome_label": "positive_high_beta_with_later_4b_watch", "current_profile_verdict": "C22 can allow high-beta life-insurance positives when reserve quality, rate-cycle leverage, capital buffer and shareholder-return bridge are explicit. Tong Yang Life produced very large MFE with low entry-basis MAE, but the post-peak drawdown shows high beta must be lifecycle-managed.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_082640_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L78-C22-085620-MIRAEASSET-LIFE-INSURANCE-BETA-FADE", "case_id": "R6L78-C22-085620-MIRAEASSET-LIFE-INSURANCE-BETA-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "78", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-FalsePositive / LifeInsuranceRateCycleBetaFade", "trigger_date": "2024-01-30", "entry_date": "2024-01-31", "entry_price": 5600.0, "evidence_available_at_that_date": "LIFE_INSURANCE_RATE_CYCLE_THEME_WITH_WEAK_RESERVE_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MIRAEASSET_LIFE_2024_RATE_CYCLE_RESERVE_CAPITAL_RETURN_EARNINGS_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_valueup_candidate", "CSM_reserve_capital_buffer_candidate", "shareholder_return_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "earnings_or_risk_loss_ratio_bridge_candidate"], "stage4b_evidence_fields": ["insurance_rate_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.07, "MFE_90D_pct": 16.07, "MFE_180D_pct": 16.07, "MAE_30D_pct": -19.55, "MAE_90D_pct": -20.98, "MAE_180D_pct": -20.98, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -31.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_peak_if_reserve_capital_return_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_quality_break_capital_buffer_loss_regulatory_issue_or_return_cancellation", "trigger_outcome_label": "counterexample_life_insurance_beta_local4b", "current_profile_verdict": "C22 should not treat life-insurance rate/value-up beta as durable Stage2 unless reserve quality, capital buffer, shareholder return and earnings bridge are visible. Mirae Asset Life had a tradable early MFE, then opened a high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_085620_2024-01-31", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L78-C22-032830-SAMSUNG-LIFE-RATE-RESERVE-CAPITAL-RETURN", "trigger_id": "TRG_R6L78-C22-032830-SAMSUNG-LIFE-RATE-RESERVE-CAPITAL-RETURN", "symbol": "032830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 14, "CSM_reserve_quality_score": 13, "capital_buffer_score": 14, "shareholder_return_score": 14, "earnings_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"rate_cycle_score": 16, "CSM_reserve_quality_score": 15, "capital_buffer_score": 16, "shareholder_return_score": 16, "earnings_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "capital_buffer_score", "shareholder_return_score", "earnings_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate cycle, CSM/reserve quality, capital buffer, earnings bridge and shareholder return; cap insurance value-up beta when evidence fails to refresh.", "MFE_90D_pct": 56.57, "MAE_90D_pct": -0.58, "score_return_alignment_label": "insurance_rate_cycle_positive_with_lifecycle_4b", "current_profile_verdict": "C22 should allow life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback and shareholder-return bridge are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L78-C22-082640-TONGYANG-LIFE-HIGHBETA-RESERVE-CAPITAL-RETURN", "trigger_id": "TRG_R6L78-C22-082640-TONGYANG-LIFE-HIGHBETA-RESERVE-CAPITAL-RETURN", "symbol": "082640", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 14, "CSM_reserve_quality_score": 13, "capital_buffer_score": 14, "shareholder_return_score": 14, "earnings_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"rate_cycle_score": 16, "CSM_reserve_quality_score": 15, "capital_buffer_score": 16, "shareholder_return_score": 16, "earnings_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "capital_buffer_score", "shareholder_return_score", "earnings_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate cycle, CSM/reserve quality, capital buffer, earnings bridge and shareholder return; cap insurance value-up beta when evidence fails to refresh.", "MFE_90D_pct": 38.27, "MAE_90D_pct": -2.34, "score_return_alignment_label": "insurance_rate_cycle_positive_with_lifecycle_4b", "current_profile_verdict": "C22 can allow high-beta life-insurance positives when reserve quality, rate-cycle leverage, capital buffer and shareholder-return bridge are explicit. Tong Yang Life produced very large MFE with low entry-basis MAE, but the post-peak drawdown shows high beta must be lifecycle-managed."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L78-C22-085620-MIRAEASSET-LIFE-INSURANCE-BETA-FADE", "trigger_id": "TRG_R6L78-C22-085620-MIRAEASSET-LIFE-INSURANCE-BETA-FADE", "symbol": "085620", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 6, "CSM_reserve_quality_score": 3, "capital_buffer_score": 3, "shareholder_return_score": 2, "earnings_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"rate_cycle_score": 4, "CSM_reserve_quality_score": 1, "capital_buffer_score": 1, "shareholder_return_score": 1, "earnings_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "capital_buffer_score", "shareholder_return_score", "earnings_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate cycle, CSM/reserve quality, capital buffer, earnings bridge and shareholder return; cap insurance value-up beta when evidence fails to refresh.", "MFE_90D_pct": 16.07, "MAE_90D_pct": -20.98, "score_return_alignment_label": "false_positive_insurance_rate_beta_bridge_gap", "current_profile_verdict": "C22 should not treat life-insurance rate/value-up beta as durable Stage2 unless reserve quality, capital buffer, shareholder return and earnings bridge are visible. Mirae Asset Life had a tradable early MFE, then opened a high-MAE drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 78, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C22 life-insurance symbols outside top-covered 000810/005830/088350/001450/000400 set, +3 Samsung/TongYang/Mirae life-insurance trigger families, +2 reserve/capital-return positives, +1 insurance beta local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 78, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "axis": "life_insurance_rate_reserve_capital_return_bridge_vs_life_insurance_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C22 should split verified insurance rate-cycle / reserve / capital-return rerating from generic insurance value-up beta. Stage2 requires rate-cycle leverage, CSM/reserve quality, capital buffer, earnings bridge and shareholder return. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["032830", "082640", "085620"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 78, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C22 needs rate-cycle, reserve quality and capital-return proof. Samsung Life and Tong Yang Life show life-insurance reserve/capital-return MFE candidates after source repair; Mirae Asset Life shows insurance value-up beta fading into local 4B when reserve/capital-return bridge is absent or stale."}
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
032830:
  name = 삼성생명
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

082640:
  name = 동양생명 from 2010-10-19
  corporate_action_candidate_dates = 2017-04-11
  selected window = 2024-02-01~D+180
  contamination = false

085620:
  name = 미래에셋생명
  corporate_action_candidate_dates = 2018-03-23
  selected window = 2024-01-31~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C22 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C22 rule-shape discovery,
but coding-agent promotion requires non-proxy rate cycle, CSM/reserve quality, capital buffer, dividend/buyback, shareholder-return and earnings bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R6/C22 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
life_insurance_rate_reserve_capital_return_bridge_vs_life_insurance_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 032830, 082640 and 085620.
4. Keep generic C22 insurance-rate/reserve weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - rate-cycle or insurance value-up attention is explicit,
   - CSM/reserve quality is visible,
   - capital buffer or solvency comfort is credible,
   - dividend/buyback/shareholder-return bridge exists,
   - earnings bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is insurance rate/value-up beta only,
   - reserve/capital-return/earnings evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -30~35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price reserve quality break, capital buffer loss, regulatory issue, shareholder-return cancellation, credit/claim shock or solvency evidence.
8. Emit before/after diagnostics and reject if verified low-MAE insurance reserve/capital-return positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 78
next_round = R7
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

