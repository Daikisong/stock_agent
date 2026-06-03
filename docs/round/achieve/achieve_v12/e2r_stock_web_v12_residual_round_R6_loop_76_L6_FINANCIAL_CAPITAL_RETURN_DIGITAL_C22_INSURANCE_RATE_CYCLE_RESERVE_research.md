# E2R Stock-Web v12 Residual Research — R6 Loop 76 / L6 / C22

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 76,
  "computed_next_round": "R7",
  "computed_next_loop": 76,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "insurance_rate_cycle_reserve_capital_return_guardrail",
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

Previous completed state in this interactive run: R5 / loop 76.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 76
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
computed_next_round = R7
computed_next_loop = 76
```

R6 was routed to C22 because loop 76 R5 used C19 and loop 75 R6 used C21.  
This file tests insurance reserve / rate-cycle / capital-return bridges while avoiding the top-covered C22 mega-insurer set.

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
000370 / 한화손해보험 / non-life loss ratio and capital-return bridge
003690 / 코리안리 / reinsurance reserve and capital-return bridge
085620 / 미래에셋생명 / life-insurance value-up beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate.
```

## Research thesis

C22 is not “보험주가 올랐다.”

The mechanism must pass through:

```text
rate cycle / value-up attention
→ loss-ratio or reserve/CSM quality
→ K-ICS capital buffer
→ dividend / buyback / capital return
→ durable rerating
```

보험주는 금리와 제도라는 바람을 타지만, 실제 돛은 준비금 품질과 자본정책이다.

---

## Case 1 — Positive with lifecycle 4B: 000370 / 한화손해보험

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is loss ratio, IFRS17 CSM/reserve quality, K-ICS buffer, underwriting margin and capital-return evidence.

```text
evidence_family = NONLIFE_INSURANCE_LOSS_RATIO_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,320
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv`:

```text
2024-02-01,4320,5640,4150,5120
2024-02-13,5590,6170,5380,5520
2024-08-20,5840,6230,5810,6190
2024-09-25,5160,5180,4920,4960
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

This is a C22 positive.  
The entry-basis risk was controlled and the price path validated a non-life insurance cycle rerating candidate.

Correct treatment:

```text
reserve/CSM + loss ratio + K-ICS + capital return verified → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Slow positive: 003690 / 코리안리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is reinsurance rate hardening, reserve adequacy, K-ICS buffer, dividend/capital-return evidence.

```text
evidence_family = REINSURANCE_RATE_HARDENING_RESERVE_KICS_DIVIDEND_CAPITAL_RETURN_BRIDGE
case_role = positive_slow_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,580
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv`:

```text
2024-02-01,7580,7960,7470,7810
2024-03-22,8360,8550,8340,8510
2024-08-20,8850,8960,8800,8890
2024-10-25,9120,9230,9050,9200
2024-11-05,9280,9550,9280,9520
2024-11-06,8080,8120,7890,proxy_close_pending
```

### Backtest

```text
MFE_30D  = +9.89%
MAE_30D  = -1.45%
MFE_90D  = +12.80%
MAE_90D  = -1.45%
MFE_180D = +26.00%
MAE_180D = -1.45%
peak_180 = 9,550 on 2024-11-05
trough_180 = 7,470 on 2024-02-01
peak_to_later_drawdown = -17.38%
```

### Interpretation

This is the slow C22 compounding row.  
It is not an explosive rerating, but low MAE plus persistent MFE matters.

Correct treatment:

```text
Stage2-Yellow possible after source repair
protect slow reinsurance/capital-return winners
```

---

## Case 3 — Counterexample / local 4B: 085620 / 미래에셋생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests life-insurance value-up beta without durable reserve/CSM and capital-return bridge.

```text
evidence_family = LIFE_INSURANCE_VALUEUP_RATE_BETA_WITH_WEAK_RESERVE_CAPITAL_RETURN_BRIDGE
case_role = counterexample_life_insurance_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,670
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv`:

```text
2024-02-01,5670,6420,5610,5770
2024-02-06,6320,6500,6100,6240
2024-02-23,5660,5730,5210,5300
2024-03-20,4550,4560,4500,4500
2024-08-05,5050,5090,4660,4950
```

### Backtest

```text
MFE_30D  = +14.64%
MAE_30D  = -11.82%
MFE_90D  = +14.64%
MAE_90D  = -20.63%
MFE_180D = +14.64%
MAE_180D = -20.63%
peak_180 = 6,500 on 2024-02-06
trough_180 = 4,500 on 2024-03-20
peak_to_later_drawdown = -30.77%
```

### Interpretation

This is the C22 false-positive boundary.  
The first spike was tradable, but the path quickly opened high MAE.

Correct treatment:

```text
life-insurance value-up beta
→ no CSM/K-ICS/capital-return bridge
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
overbearish_no_hard4c_guard = keep
```

### What this does not justify

```text
do_not_raise_generic_C22_insurance_valueup_weight = true
do_not_treat_all_insurance_MFE_as_Green = true
do_not_convert_insurance_drawdown_to_hard_4C_without_non_price_reserve_or_capital_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE
```

This fine archetype covers:

```text
1. non-life loss ratio / reserve / capital-return bridge → Stage2 possible after source repair
2. reinsurance reserve / rate hardening / dividend bridge → slow Stage2 possible
3. life-insurance value-up beta without CSM/K-ICS bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-NonlifeLossRatioCapitalReturnBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should allow non-life insurers when value-up and rate-cycle attention connects to loss-ratio improvement, CSM/IFRS17 reserve quality, K-ICS capital buffer, dividend/buyback or capital-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy loss-ratio/rate-cycle, reserve/CSM, K-ICS, dividend/buyback/capital-return evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-ReinsuranceReserveCapitalReturnBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should preserve reinsurance reserve/capital-return rows when underwriting cycle, reinsurance rate hardening, reserve adequacy, K-ICS buffer and shareholder-return bridge are visible. Korean Re produced slow low-MAE rerating, not explosive beta; the model should not overblock these compounding C22 rows.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy loss-ratio/rate-cycle, reserve/CSM, K-ICS, dividend/buyback/capital-return evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LifeInsuranceValueupReserveBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should not treat life-insurance value-up beta as durable Stage2 unless CSM/IFRS17 reserve quality, K-ICS buffer, new-business margin, capital return and shareholder-return evidence refreshes. Mirae Asset Life had a tradable spike but then opened high MAE, making it a local 4B row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy loss-ratio/rate-cycle, reserve/CSM, K-ICS, dividend/buyback/capital-return evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN", "case_id": "R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_capital_return_guardrail", "trigger_type": "Stage2-Actionable-NonlifeLossRatioCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4320.0, "evidence_available_at_that_date": "NONLIFE_INSURANCE_LOSS_RATIO_RATE_CYCLE_CSM_KICS_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANWHA_GENERAL_INSURANCE_2024_LOSS_RATIO_IFRS17_CSM_KICS_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["insurance_rate_cycle_or_valueup", "reserve_CSM_or_KICS_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "loss_ratio_or_underwriting_margin_bridge_candidate"], "stage4b_evidence_fields": ["valueup_beta", "reserve_or_capital_return_bridge_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv", "profile_path": "atlas/symbol_profiles/000/000370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.82, "MFE_90D_pct": 42.82, "MFE_180D_pct": 44.21, "MAE_30D_pct": -3.94, "MAE_90D_pct": -3.94, "MAE_180D_pct": -3.94, "peak_date": "2024-08-20", "peak_price": 6230.0, "drawdown_after_peak_pct": -25.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_cycle_peak_if_reserve_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_CSM_KICS_loss_ratio_capital_or_regulatory_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C22 should allow non-life insurers when value-up and rate-cycle attention connects to loss-ratio improvement, CSM/IFRS17 reserve quality, K-ICS capital buffer, dividend/buyback or capital-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_000370_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN", "case_id": "R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_capital_return_guardrail", "trigger_type": "Stage2-SlowPositive-ReinsuranceReserveCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7580.0, "evidence_available_at_that_date": "REINSURANCE_RATE_HARDENING_RESERVE_KICS_DIVIDEND_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KOREAN_RE_2024_REINSURANCE_RATE_RESERVE_ADEQUACY_KICS_DIVIDEND_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["insurance_rate_cycle_or_valueup", "reserve_CSM_or_KICS_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "loss_ratio_or_underwriting_margin_bridge_candidate"], "stage4b_evidence_fields": ["valueup_beta", "reserve_or_capital_return_bridge_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv", "profile_path": "atlas/symbol_profiles/003/003690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.89, "MFE_90D_pct": 12.8, "MFE_180D_pct": 26.0, "MAE_30D_pct": -1.45, "MAE_90D_pct": -1.45, "MAE_180D_pct": -1.45, "peak_date": "2024-11-05", "peak_price": 9550.0, "drawdown_after_peak_pct": -17.38, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_cycle_peak_if_reserve_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_CSM_KICS_loss_ratio_capital_or_regulatory_break", "trigger_outcome_label": "positive_slow_with_later_4b_watch", "current_profile_verdict": "C22 should preserve reinsurance reserve/capital-return rows when underwriting cycle, reinsurance rate hardening, reserve adequacy, K-ICS buffer and shareholder-return bridge are visible. Korean Re produced slow low-MAE rerating, not explosive beta; the model should not overblock these compounding C22 rows.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_003690_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE", "case_id": "R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_capital_return_guardrail", "trigger_type": "Stage2-FalsePositive / LifeInsuranceValueupReserveBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5670.0, "evidence_available_at_that_date": "LIFE_INSURANCE_VALUEUP_RATE_BETA_WITH_WEAK_RESERVE_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MIRAE_ASSET_LIFE_2024_VALUEUP_LIFE_INSURANCE_CSM_KICS_RESERVE_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["insurance_rate_cycle_or_valueup", "reserve_CSM_or_KICS_candidate", "capital_return_candidate"], "stage3_evidence_fields": ["relative_strength", "loss_ratio_or_underwriting_margin_bridge_candidate"], "stage4b_evidence_fields": ["valueup_beta", "reserve_or_capital_return_bridge_stale", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.64, "MFE_90D_pct": 14.64, "MFE_180D_pct": 14.64, "MAE_30D_pct": -11.82, "MAE_90D_pct": -20.63, "MAE_180D_pct": -20.63, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -30.77, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_cycle_peak_if_reserve_or_capital_return_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_CSM_KICS_loss_ratio_capital_or_regulatory_break", "trigger_outcome_label": "counterexample_life_insurance_beta_local4b", "current_profile_verdict": "C22 should not treat life-insurance value-up beta as durable Stage2 unless CSM/IFRS17 reserve quality, K-ICS buffer, new-business margin, capital return and shareholder-return evidence refreshes. Mirae Asset Life had a tradable spike but then opened high MAE, making it a local 4B row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_085620_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN", "trigger_id": "TRG_R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN", "symbol": "000370", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"insurance_cycle_score": 13, "reserve_CSM_quality_score": 13, "KICS_capital_buffer_score": 12, "capital_return_score": 13, "loss_ratio_underwriting_score": 12, "relative_strength_score": 13, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"insurance_cycle_score": 13, "reserve_CSM_quality_score": 15, "KICS_capital_buffer_score": 14, "capital_return_score": 15, "loss_ratio_underwriting_score": 14, "relative_strength_score": 12, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["reserve_CSM_quality_score", "KICS_capital_buffer_score", "capital_return_score", "loss_ratio_underwriting_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified reserve/CSM quality, K-ICS capital buffer, loss-ratio/underwriting improvement and capital-return bridge; cap value-up beta without those bridges.", "MFE_90D_pct": 42.82, "MAE_90D_pct": -3.94, "score_return_alignment_label": "insurance_cycle_positive_with_lifecycle_4b", "current_profile_verdict": "C22 should allow non-life insurers when value-up and rate-cycle attention connects to loss-ratio improvement, CSM/IFRS17 reserve quality, K-ICS capital buffer, dividend/buyback or capital-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if reserve/capital-return evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN", "trigger_id": "TRG_R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN", "symbol": "003690", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"insurance_cycle_score": 13, "reserve_CSM_quality_score": 13, "KICS_capital_buffer_score": 12, "capital_return_score": 13, "loss_ratio_underwriting_score": 12, "relative_strength_score": 13, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"insurance_cycle_score": 13, "reserve_CSM_quality_score": 15, "KICS_capital_buffer_score": 14, "capital_return_score": 15, "loss_ratio_underwriting_score": 14, "relative_strength_score": 12, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["reserve_CSM_quality_score", "KICS_capital_buffer_score", "capital_return_score", "loss_ratio_underwriting_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified reserve/CSM quality, K-ICS capital buffer, loss-ratio/underwriting improvement and capital-return bridge; cap value-up beta without those bridges.", "MFE_90D_pct": 12.8, "MAE_90D_pct": -1.45, "score_return_alignment_label": "insurance_cycle_positive_with_lifecycle_4b", "current_profile_verdict": "C22 should preserve reinsurance reserve/capital-return rows when underwriting cycle, reinsurance rate hardening, reserve adequacy, K-ICS buffer and shareholder-return bridge are visible. Korean Re produced slow low-MAE rerating, not explosive beta; the model should not overblock these compounding C22 rows."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE", "trigger_id": "TRG_R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE", "symbol": "085620", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"insurance_cycle_score": 6, "reserve_CSM_quality_score": 3, "KICS_capital_buffer_score": 3, "capital_return_score": 2, "loss_ratio_underwriting_score": 3, "relative_strength_score": 6, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 49, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"insurance_cycle_score": 4, "reserve_CSM_quality_score": 2, "KICS_capital_buffer_score": 1, "capital_return_score": 1, "loss_ratio_underwriting_score": 2, "relative_strength_score": 3, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["reserve_CSM_quality_score", "KICS_capital_buffer_score", "capital_return_score", "loss_ratio_underwriting_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified reserve/CSM quality, K-ICS capital buffer, loss-ratio/underwriting improvement and capital-return bridge; cap value-up beta without those bridges.", "MFE_90D_pct": 14.64, "MAE_90D_pct": -20.63, "score_return_alignment_label": "false_positive_life_insurance_valueup_bridge_gap", "current_profile_verdict": "C22 should not treat life-insurance value-up beta as durable Stage2 unless CSM/IFRS17 reserve quality, K-ICS buffer, new-business margin, capital return and shareholder-return evidence refreshes. Mirae Asset Life had a tradable spike but then opened high MAE, making it a local 4B row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 76, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C22 insurer/reinsurer symbols outside top-covered Samsung/DB/HanwhaLife/Hyundai/Lotte set, +3 nonlife/reinsurance/life trigger families, +2 capital-return positives, +1 life-insurance value-up local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 76, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "axis": "nonlife_reinsurance_life_capital_return_reserve_bridge_vs_valueup_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C22 should split verified insurance reserve/capital-return rerating from value-up beta. Stage2 requires reserve/CSM quality, K-ICS buffer, loss-ratio or underwriting improvement, dividend/buyback/capital-return bridge. If MAE widens or post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["000370", "003690", "085620"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 76, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "overbearish_no_hard4c_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C22 needs reserve/capital-return proof. Hanwha General Insurance and Korean Re show insurance-cycle/capital-return positives after source repair; Mirae Asset Life shows life-insurance value-up beta fading into local 4B when reserve, K-ICS and capital-return bridge is absent."}
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
000370:
  corporate_action_candidate_dates = 2001-01-16, 2003-02-27, 2004-04-28, 2007-03-06, 2010-01-20, 2013-11-28, 2017-11-23
  selected window = 2024-02-01~D+180
  contamination = false

003690:
  corporate_action_candidate_dates = 1997-03-29, 2004-07-20
  selected window = 2024-02-01~D+180
  contamination = false

085620:
  corporate_action_candidate_dates = 2018-03-23
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C22 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C22 rule-shape discovery,
but coding-agent promotion requires non-proxy reserve/CSM, K-ICS, loss-ratio, underwriting margin and capital-return evidence.
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
nonlife_reinsurance_life_capital_return_reserve_bridge_vs_valueup_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 000370, 003690 and 085620.
4. Keep generic C22 insurance value-up weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - rate-cycle or value-up attention is explicit,
   - reserve/CSM quality or K-ICS capital buffer is visible,
   - loss ratio / underwriting margin or reinsurance rate bridge exists,
   - dividend, buyback or capital return bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is insurance value-up beta only,
   - reserve/CSM/K-ICS/capital-return evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -25~35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price reserve impairment, K-ICS capital break, regulatory issue, loss-ratio deterioration, capital return cancellation or solvency evidence.
8. Emit before/after diagnostics and reject if verified slow insurance capital-return positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 76
next_round = R7
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

