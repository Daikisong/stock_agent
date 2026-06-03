# E2R Stock-Web v12 Residual Research — R6 Loop 80 / L6 / C22

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 80,
  "computed_next_round": "R7",
  "computed_next_loop": 80,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "insurance_rate_cycle_reserve_guardrail",
    "life_nonlife_CSM_reserve_capital_return_bridge",
    "life_insurance_theme_fade_boundary",
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

Previous completed state in this interactive run: R5 / loop 80.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 80
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
computed_next_round = R7
computed_next_loop = 80
```

R6 was routed to C22 because loop 79 R6 used C21 bank/financial value-up.  
This file tests insurance rate-cycle / CSM / reserve / capital-return bridges.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C22 concentration in:

```text
000810, 005830, 088350, 001450, 000400
```

This run uses three different symbols:

```text
032830 / 삼성생명 / life-insurance rate-cycle and capital-return bridge
000370 / 한화손해보험 / non-life insurance rate-cycle and reserve bridge
085620 / 미래에셋생명 / life-insurance theme fade / local 4B boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C22 is not “보험 value-up이 올랐다.”

The mechanism must pass through:

```text
rate cycle or value-up trigger
→ CSM / reserve quality or loss-ratio improvement
→ capital buffer
→ dividend, buyback or payout policy
→ investment spread and earnings durability
→ durable rerating
```

보험주의 상승은 지급준비금 위에 놓인 저울이다.  
C22가 보려는 것은 저울이 실제 자본, CSM, 손해율, 배당 여력, 이익 지속성으로 균형을 잡는지다.

---

## Case 1 — Life-insurance positive: 032830 / 삼성생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is life-insurance rate cycle, CSM/reserve quality, capital buffer, shareholder return, investment spread and earnings bridge evidence.

```text
evidence_family = LIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_VALUEUP_EARNINGS_BRIDGE
case_role = positive_life_insurance_capital_return_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 69,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv`:

```text
2024-02-01,69300,76800,68900,76000
2024-02-23,94500,97300,93900,95600
2024-03-05,101600,107800,101100,104500
2024-03-08,107200,108500,104200,105100
2024-04-19,77200,78000,76600,77300
2024-07-04,88300,95200,87000,91400
2024-10-31,102000,102300,99800,101500
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

This is a C22 life-insurance positive.  
The MFE was large and entry-basis MAE was nearly absent.

Correct treatment:

```text
verified CSM / reserve quality / capital-return / earnings bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Non-life insurance positive: 000370 / 한화손해보험

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is loss-ratio improvement, rate cycle, reserve adequacy, capital buffer, payout policy and earnings bridge evidence.

```text
evidence_family = NONLIFE_INSURANCE_LOSS_RATIO_RATE_CYCLE_RESERVE_CAPITAL_RETURN_EARNINGS_BRIDGE
case_role = positive_nonlife_insurance_rate_cycle_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,320
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv`:

```text
2024-02-01,4320,5640,4150,5120
2024-02-13,5590,6170,5380,5520
2024-03-29,4550,4995,4365,4405
2024-07-31,5390,5720,5360,5650
2024-08-20,5840,6230,5810,6190
2024-10-25,4675,4775,4620,4720
```

### Backtest

```text
MFE_30D  = +42.82%
MAE_30D  = -3.94%
MFE_90D  = +42.82%
MAE_90D  = -3.94%
MFE_180D = +44.21%
MAE_180D = -3.94%
peak_180 = 6,230 on 2024-08-20
trough_180 = 4,150 on 2024-02-01
peak_to_later_drawdown = -25.84%
```

### Interpretation

This is a C22 non-life insurance positive.  
It had strong MFE with bounded entry-basis MAE.

Correct treatment:

```text
verified loss-ratio / reserve / capital-return / earnings bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 085620 / 미래에셋생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests life-insurance rate-cycle / value-up theme beta without enough CSM, capital-return and earnings bridge.

```text
evidence_family = LIFE_INSURANCE_RATE_CYCLE_VALUEUP_THEME_WITH_WEAK_CSM_CAPITAL_RETURN_EARNINGS_BRIDGE
case_role = counterexample_life_insurance_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,670
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv`:

```text
2024-02-01,5670,6420,5610,5770
2024-02-06,6320,6500,6100,6240
2024-02-29,5070,5140,4750,4880
2024-04-02,4535,4535,4425,4490
2024-08-05,5050,5090,4660,4950
2024-10-31,5260,5330,5250,5270
```

### Backtest

```text
MFE_30D  = +14.64%
MAE_30D  = -20.55%
MFE_90D  = +14.64%
MAE_90D  = -21.96%
MFE_180D = +14.64%
MAE_180D = -21.96%
peak_180 = 6,500 on 2024-02-06
trough_180 = 4,425 on 2024-04-02
peak_to_later_drawdown = -31.92%
```

### Interpretation

This is a C22 local-4B boundary.  
The early theme spike did not become durable insurance rate-cycle rerating.

Correct treatment:

```text
life-insurance value-up/rate-cycle beta
→ no verified CSM / capital-return / earnings bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
insurance_valueup_theme_bridge_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C22_insurance_valueup_weight = true
do_not_treat_all_insurance_MFE_as_Green = true
do_not_convert_insurance_drawdown_to_hard_4C_without_non_price_reserve_capital_or_regulatory_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE
```

This fine archetype covers:

```text
1. life insurance CSM/reserve/capital-return bridge → Stage2 possible after source repair
2. non-life insurance loss-ratio/reserve/capital-return bridge → Stage2 possible, lifecycle-managed
3. life-insurance value-up beta without CSM/earnings bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L80-C22-032830-SAMSUNG-LIFE-RATE-CYCLE-CAPITAL-RETURN", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "80", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-LifeInsuranceRateCycleCapitalReturnBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should preserve life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback policy and earnings durability are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle monitoring.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve quality, loss ratio, rate cycle, capital buffer, investment spread, dividend/buyback and earnings bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L80-C22-000370-HANWHA-GENERAL-INSURANCE-RATE-CYCLE", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": "80", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-NonlifeInsuranceRateCycleReserveCapitalBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should allow non-life insurance positives when loss ratio, reserve adequacy, rate cycle, capital buffer and shareholder-return bridge are visible. Hanwha General Insurance had strong early MFE with bounded entry-basis MAE, then a lifecycle drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve quality, loss ratio, rate cycle, capital buffer, investment spread, dividend/buyback and earnings bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L80-C22-085620-MIRAE-ASSET-LIFE-THEME-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "80", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LifeInsuranceRateThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM, reserve quality, capital return, investment spread and earnings bridge are visible. Mirae Asset Life had an initial spike, then a high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve quality, loss ratio, rate cycle, capital buffer, investment spread, dividend/buyback and earnings bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L80-C22-032830-SAMSUNG-LIFE-RATE-CYCLE-CAPITAL-RETURN", "case_id": "R6L80-C22-032830-SAMSUNG-LIFE-RATE-CYCLE-CAPITAL-RETURN", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "80", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-Actionable-LifeInsuranceRateCycleCapitalReturnBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 69300.0, "evidence_available_at_that_date": "LIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_VALUEUP_EARNINGS_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SAMSUNG_LIFE_2024_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_EARNINGS_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_valueup_candidate", "CSM_reserve_or_loss_ratio_candidate", "capital_return_earnings_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "capital_buffer_or_investment_spread_candidate"], "stage4b_evidence_fields": ["insurance_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 56.57, "MFE_90D_pct": 56.57, "MFE_180D_pct": 56.57, "MAE_30D_pct": -0.58, "MAE_90D_pct": -0.58, "MAE_180D_pct": -0.58, "peak_date": "2024-03-08", "peak_price": 108500.0, "drawdown_after_peak_pct": -29.4, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_valueup_peak_if_CSM_reserve_capital_return_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_loss_capital_buffer_credit_spread_or_regulatory_break", "trigger_outcome_label": "positive_life_insurance_capital_return_with_later_4b_watch", "current_profile_verdict": "C22 should preserve life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback policy and earnings durability are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle monitoring.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_032830_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L80-C22-000370-HANWHA-GENERAL-INSURANCE-RATE-CYCLE", "case_id": "R6L80-C22-000370-HANWHA-GENERAL-INSURANCE-RATE-CYCLE", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": "80", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-Actionable-NonlifeInsuranceRateCycleReserveCapitalBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4320.0, "evidence_available_at_that_date": "NONLIFE_INSURANCE_LOSS_RATIO_RATE_CYCLE_RESERVE_CAPITAL_RETURN_EARNINGS_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANWHA_GENERAL_INSURANCE_2024_LOSS_RATIO_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_valueup_candidate", "CSM_reserve_or_loss_ratio_candidate", "capital_return_earnings_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "capital_buffer_or_investment_spread_candidate"], "stage4b_evidence_fields": ["insurance_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv", "profile_path": "atlas/symbol_profiles/000/000370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.82, "MFE_90D_pct": 42.82, "MFE_180D_pct": 44.21, "MAE_30D_pct": -3.94, "MAE_90D_pct": -3.94, "MAE_180D_pct": -3.94, "peak_date": "2024-08-20", "peak_price": 6230.0, "drawdown_after_peak_pct": -25.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_valueup_peak_if_CSM_reserve_capital_return_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_loss_capital_buffer_credit_spread_or_regulatory_break", "trigger_outcome_label": "positive_nonlife_insurance_rate_cycle_with_later_4b_watch", "current_profile_verdict": "C22 should allow non-life insurance positives when loss ratio, reserve adequacy, rate cycle, capital buffer and shareholder-return bridge are visible. Hanwha General Insurance had strong early MFE with bounded entry-basis MAE, then a lifecycle drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_000370_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L80-C22-085620-MIRAE-ASSET-LIFE-THEME-FADE", "case_id": "R6L80-C22-085620-MIRAE-ASSET-LIFE-THEME-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "80", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-FalsePositive / LifeInsuranceRateThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5670.0, "evidence_available_at_that_date": "LIFE_INSURANCE_RATE_CYCLE_VALUEUP_THEME_WITH_WEAK_CSM_CAPITAL_RETURN_EARNINGS_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MIRAE_ASSET_LIFE_2024_CSM_RESERVE_CAPITAL_RETURN_INVESTMENT_SPREAD_EARNINGS_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_valueup_candidate", "CSM_reserve_or_loss_ratio_candidate", "capital_return_earnings_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "capital_buffer_or_investment_spread_candidate"], "stage4b_evidence_fields": ["insurance_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.64, "MFE_90D_pct": 14.64, "MFE_180D_pct": 14.64, "MAE_30D_pct": -20.55, "MAE_90D_pct": -21.96, "MAE_180D_pct": -21.96, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -31.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_valueup_peak_if_CSM_reserve_capital_return_or_earnings_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_loss_capital_buffer_credit_spread_or_regulatory_break", "trigger_outcome_label": "counterexample_life_insurance_theme_local4b", "current_profile_verdict": "C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM, reserve quality, capital return, investment spread and earnings bridge are visible. Mirae Asset Life had an initial spike, then a high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_085620_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L80-C22-032830-SAMSUNG-LIFE-RATE-CYCLE-CAPITAL-RETURN", "trigger_id": "TRG_R6L80-C22-032830-SAMSUNG-LIFE-RATE-CYCLE-CAPITAL-RETURN", "symbol": "032830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 14, "CSM_reserve_quality_score": 14, "capital_buffer_score": 13, "capital_return_score": 13, "earnings_durability_score": 13, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"rate_cycle_score": 16, "CSM_reserve_quality_score": 16, "capital_buffer_score": 15, "capital_return_score": 15, "earnings_durability_score": 15, "relative_strength_score": 11, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "capital_buffer_score", "capital_return_score", "earnings_durability_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate-cycle/CSM/reserve/capital-return/earnings bridge; cap insurance value-up theme beta when bridge fails to refresh.", "MFE_90D_pct": 56.57, "MAE_90D_pct": -0.58, "score_return_alignment_label": "insurance_rate_cycle_positive_with_lifecycle_4b", "current_profile_verdict": "C22 should preserve life-insurance positives when rate cycle, CSM/reserve quality, capital buffer, dividend/buyback policy and earnings durability are visible. Samsung Life produced large MFE with almost no entry-basis MAE, but later drawdown requires lifecycle monitoring."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L80-C22-000370-HANWHA-GENERAL-INSURANCE-RATE-CYCLE", "trigger_id": "TRG_R6L80-C22-000370-HANWHA-GENERAL-INSURANCE-RATE-CYCLE", "symbol": "000370", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 14, "CSM_reserve_quality_score": 14, "capital_buffer_score": 13, "capital_return_score": 13, "earnings_durability_score": 13, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"rate_cycle_score": 16, "CSM_reserve_quality_score": 16, "capital_buffer_score": 15, "capital_return_score": 15, "earnings_durability_score": 15, "relative_strength_score": 11, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "capital_buffer_score", "capital_return_score", "earnings_durability_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate-cycle/CSM/reserve/capital-return/earnings bridge; cap insurance value-up theme beta when bridge fails to refresh.", "MFE_90D_pct": 42.82, "MAE_90D_pct": -3.94, "score_return_alignment_label": "insurance_rate_cycle_positive_with_lifecycle_4b", "current_profile_verdict": "C22 should allow non-life insurance positives when loss ratio, reserve adequacy, rate cycle, capital buffer and shareholder-return bridge are visible. Hanwha General Insurance had strong early MFE with bounded entry-basis MAE, then a lifecycle drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L80-C22-085620-MIRAE-ASSET-LIFE-THEME-FADE", "trigger_id": "TRG_R6L80-C22-085620-MIRAE-ASSET-LIFE-THEME-FADE", "symbol": "085620", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 6, "CSM_reserve_quality_score": 3, "capital_buffer_score": 4, "capital_return_score": 2, "earnings_durability_score": 2, "relative_strength_score": 4, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 45, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"rate_cycle_score": 4, "CSM_reserve_quality_score": 1, "capital_buffer_score": 2, "capital_return_score": 1, "earnings_durability_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "capital_buffer_score", "capital_return_score", "earnings_durability_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate-cycle/CSM/reserve/capital-return/earnings bridge; cap insurance value-up theme beta when bridge fails to refresh.", "MFE_90D_pct": 14.64, "MAE_90D_pct": -21.96, "score_return_alignment_label": "false_positive_life_insurance_theme_bridge_gap", "current_profile_verdict": "C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM, reserve quality, capital return, investment spread and earnings bridge are visible. Mirae Asset Life had an initial spike, then a high-MAE fade."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 80, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_NONLIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_VS_LIFE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C22 insurance symbols outside top-covered 000810/005830/088350/001450/000400 set, +3 Samsung Life/Hanwha GI/Mirae Life trigger families, +2 insurance rate-cycle positives, +1 life-insurance theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 80, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "axis": "life_nonlife_insurance_rate_cycle_CSM_reserve_capital_return_bridge_vs_life_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C22 should split verified life/non-life insurance rate-cycle, CSM/reserve and capital-return rerating from generic insurance value-up theme beta. Stage2 requires CSM/reserve quality or loss-ratio improvement, capital buffer, dividend/buyback or payout policy, investment spread and earnings bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["032830", "000370", "085620"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 80, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "insurance_valueup_theme_bridge_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C22 needs rate cycle, CSM/reserve or loss-ratio quality, capital buffer, shareholder-return and earnings proof. Samsung Life and Hanwha General Insurance show insurance value-up positives after source repair; Mirae Asset Life shows a life-insurance theme spike fading into local 4B when CSM/capital-return/earnings bridge is weak."}
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

000370:
  name = 한화손해보험 from 2007-01-16, 신동아화재 before that
  corporate_action_candidate_dates = 2001-01-16, 2003-02-27, 2004-04-28, 2007-03-06, 2010-01-20, 2013-11-28, 2017-11-23
  selected window = 2024-02-01~D+180
  contamination = false

085620:
  name = 미래에셋생명
  corporate_action_candidate_dates = 2018-03-23
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C22 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C22 rule-shape discovery,
but coding-agent promotion requires non-proxy CSM/reserve quality, loss ratio, rate cycle, capital buffer, investment spread, dividend/buyback and earnings evidence.
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
life_nonlife_insurance_rate_cycle_CSM_reserve_capital_return_bridge_vs_life_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 032830, 000370 and 085620.
4. Keep generic C22 insurance/rate-cycle weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - rate cycle or value-up premise is explicit,
   - CSM/reserve quality or loss-ratio improvement is visible,
   - capital buffer is credible,
   - dividend / buyback / payout bridge exists,
   - investment spread and earnings bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is insurance value-up/rate-cycle theme beta only,
   - CSM/reserve/capital-return/earnings evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price reserve loss, capital-buffer damage, credit-spread shock, regulatory issue, shareholder-return cancellation or earnings-quality break.
8. Emit before/after diagnostics and reject if verified insurance rate-cycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 80
next_round = R7
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

