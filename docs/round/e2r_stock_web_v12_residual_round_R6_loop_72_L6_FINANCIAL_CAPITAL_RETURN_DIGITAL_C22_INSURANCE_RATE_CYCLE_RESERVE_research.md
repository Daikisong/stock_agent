# E2R Stock-Web v12 Residual Research — R6 Loop 72 / L6 / C22

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 72,
  "computed_next_round": "R7",
  "computed_next_loop": 72,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA",
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

Previous completed state in this interactive run: R5 / loop 72.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 72
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
computed_next_round = R7
computed_next_loop = 72
```

R6 was routed to C22 because loop 71 already produced a C21 bank/capital-return file.  
The goal is not another generic value-up run. This file tests whether insurance rerating needs a verified CSM/reserve/rate-cycle/capital-return bridge rather than price-only insurance beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat already shows C22 has substantial coverage and high top-symbol concentration.  
This run avoids the heaviest top-covered symbols such as 000810 and 005830, and adds:

```text
000370 / 한화손해보험 / small P&C CSM/value-up bridge
003690 / 코리안리 / reinsurance rate-cycle/reserve bridge
085620 / 미래에셋생명 / life-insurer price-only beta counterexample
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are marked source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C22 is not simply “insurance stocks went up.”

The proper mechanism is:

```text
IFRS17 / CSM / reserve quality / rate-cycle visibility
→ recurring ROE or underwriting earnings visibility
→ capital return or valuation normalization
→ durable rerating
```

A weaker pattern also exists:

```text
low-PBR insurance basket rally
→ price MFE
→ no verified CSM/reserve/capital-return bridge
→ reversal or high MAE
```

The system should not confuse the second pattern for the first.

---

## Case 1 — Positive after source repair: 000370 / 한화손해보험

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is IFRS17/CSM or ROE visibility plus shareholder-return/value-up bridge for a smaller P&C insurer.

```text
evidence_family = SMALL_PNC_INSURER_VALUEUP_CSM_ROE_CAPITAL_RETURN_RERATING
case_role = positive
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
peak_to_later_drawdown = -21.35%
```

### Interpretation

This is the clean positive price shape: high MFE and controlled MAE.  
But C22 should not treat the price path alone as evidence. The coding-agent must verify CSM/ROE/capital-return bridge before any runtime promotion.

---

## Case 2 — Positive slow anchor: 003690 / 코리안리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is reinsurance renewal/rate-cycle and reserve earnings visibility.

```text
evidence_family = REINSURANCE_RATE_CYCLE_RESERVE_EARNINGS_VISIBILITY
case_role = positive_slow
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,580
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv`:

```text
2024-02-01,7580,7960,7470,7810
2024-03-15,8350,8470,8320,8320
2024-08-26,8900,9000,8880,8930
2024-09-11,8340,8400,8190,8210
```

### Backtest

```text
MFE_30D  = +11.74%
MAE_30D  = -1.45%
MFE_90D  = +12.80%
MAE_90D  = -1.45%
MFE_180D = +18.73%
MAE_180D = -1.45%
peak_180 = 9,000 on 2024-08-26
trough_180 = 7,470 on 2024-02-01
peak_to_later_drawdown = -8.78%
```

### Interpretation

This is a slower but cleaner C22 path.  
The return is less explosive than 000370, but the MAE is controlled. This supports a distinct reinsurance sub-route:

```text
rate-cycle / reserve visibility → slow Stage2 candidate
```

Again, promotion requires non-proxy source repair.

---

## Case 3 — Counterexample: 085620 / 미래에셋생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The row tests life-insurer value-up beta without a verified CSM/reserve/capital-return bridge.

```text
evidence_family = LIFE_INSURER_VALUEUP_PRICE_BETA_WITH_WEAK_CSM_RESERVE_CAPITAL_RETURN_BRIDGE
case_role = counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,670
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv`:

```text
2024-02-01,5670,6420,5610,5770
2024-02-06,6320,6500,6100,6240
2024-04-02,4535,4535,4425,4490
2024-08-05,5050,5090,4660,4950
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

This is the C22 false-positive shape.  
The basket rally generated MFE, but not enough to compensate for the drawdown. Without verified CSM quality, reserve release, recurring ROE or capital return, the row should not become durable Stage2/Green.

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
do_not_raise_generic_C22_weight = true
do_not_treat_insurance_valueup_beta_as_Green = true
do_not_convert_life_insurer_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA
```

This fine archetype covers:

```text
1. small P&C insurer value-up + CSM/ROE/capital return → Stage2 possible
2. reinsurance rate-cycle/reserve visibility → slower Stage2 possible
3. life-insurer basket beta without CSM/reserve bridge → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R6", "loop": 72, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA", "case_id": "R6L72-C22-000370-HANWHA-GI-SMALL-PNC-VALUEUP-CSM-CAPITAL-RETURN", "symbol": "000370", "company": "한화손해보험", "trigger_type": "Stage2-Actionable-InsuranceValueupCSM", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4320.0, "mfe_30_pct": 42.82, "mae_30_pct": -3.94, "mfe_90_pct": 42.82, "mae_90_pct": -3.94, "mfe_180_pct": 44.21, "mae_180_pct": -3.94, "peak_price_180": 6230.0, "peak_date_180": "2024-08-20", "trough_price_180": 4150.0, "trough_date_180": "2024-02-01", "peak_to_later_drawdown_pct": -21.35, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "SMALL_PNC_INSURER_VALUEUP_CSM_ROE_CAPITAL_RETURN_RERATING", "evidence_url": "source_proxy_manual_verification_required:HANWHA_GENERAL_INSURANCE_2024_IFRS17_CSM_ROE_CAPITAL_RETURN_VALUEUP_BRIDGE", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R6", "loop": 72, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA", "case_id": "R6L72-C22-003690-KOREANRE-REINSURANCE-RATE-CYCLE-RESERVE-BRIDGE", "symbol": "003690", "company": "코리안리", "trigger_type": "Stage2-Actionable-ReinsuranceRateCycle", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7580.0, "mfe_30_pct": 11.74, "mae_30_pct": -1.45, "mfe_90_pct": 12.8, "mae_90_pct": -1.45, "mfe_180_pct": 18.73, "mae_180_pct": -1.45, "peak_price_180": 9000.0, "peak_date_180": "2024-08-26", "trough_price_180": 7470.0, "trough_date_180": "2024-02-01", "peak_to_later_drawdown_pct": -8.78, "case_role": "positive_slow", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "REINSURANCE_RATE_CYCLE_RESERVE_EARNINGS_VISIBILITY", "evidence_url": "source_proxy_manual_verification_required:KOREAN_RE_2024_REINSURANCE_RATE_CYCLE_RESERVE_UNDERWRITING_VISIBILITY", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R6", "loop": 72, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA", "case_id": "R6L72-C22-085620-MIRAE-LIFE-PRICEONLY-VALUEUP-BETA", "symbol": "085620", "company": "미래에셋생명", "trigger_type": "Stage2-FalsePositive / LifeInsurerPriceOnlyValueupBeta", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5670.0, "mfe_30_pct": 14.64, "mae_30_pct": -20.55, "mfe_90_pct": 14.64, "mae_90_pct": -21.96, "mfe_180_pct": 14.64, "mae_180_pct": -21.96, "peak_price_180": 6500.0, "peak_date_180": "2024-02-06", "trough_price_180": 4425.0, "trough_date_180": "2024-04-02", "peak_to_later_drawdown_pct": -31.92, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "LIFE_INSURER_VALUEUP_PRICE_BETA_WITH_WEAK_CSM_RESERVE_CAPITAL_RETURN_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:MIRAE_ASSET_LIFE_2024_PRICE_ONLY_VALUEUP_BETA_WEAK_RESERVE_CSM_BRIDGE", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R6L72-C22-000370-HANWHA-GI-SMALL-PNC-VALUEUP-CSM-CAPITAL-RETURN", "symbol": "000370", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 11, "earnings_visibility": 15, "bottleneck_pricing_power": 5, "market_mispricing": 14, "valuation_rerating": 15, "capital_allocation": 4, "information_confidence": 2}, "diagnostic_flags": ["insurance_rate_cycle_reserve", "valueup_or_rate_cycle", "csm_reserve_capital_return_bridge_present_after_source_repair", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable after source repair", "profile_stress_result": "C22 should allow Stage2 when a low-PBR non-life insurer has IFRS17/CSM or ROE visibility plus shareholder-return/value-up bridge. The stock-web path shows high MFE with controlled MAE, but source repair is required before runtime weight promotion."}
{"row_type": "score_simulation", "case_id": "R6L72-C22-003690-KOREANRE-REINSURANCE-RATE-CYCLE-RESERVE-BRIDGE", "symbol": "003690", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 11, "earnings_visibility": 15, "bottleneck_pricing_power": 5, "market_mispricing": 14, "valuation_rerating": 15, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["insurance_rate_cycle_reserve", "valueup_or_rate_cycle", "csm_reserve_capital_return_bridge_present_after_source_repair", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable after source repair", "profile_stress_result": "C22 should not be limited to domestic P&C value-up names. Reinsurance rate-cycle/renewal pricing can be a slower but cleaner Stage2 route if reserve and underwriting-cycle evidence are present."}
{"row_type": "score_simulation", "case_id": "R6L72-C22-085620-MIRAE-LIFE-PRICEONLY-VALUEUP-BETA", "symbol": "085620", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 6, "bottleneck_pricing_power": 5, "market_mispricing": 14, "valuation_rerating": 11, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["insurance_rate_cycle_reserve", "valueup_or_rate_cycle", "price_only_valueup_beta_weak_bridge", "source_proxy_only"], "expected_current_profile_stage": "Stage2-FalsePositive / local 4B-watch", "profile_stress_result": "Life-insurer value-up beta can spike with the insurance basket, but without CSM quality, reserve release, capital-return, or recurring ROE bridge it should not be treated as durable C22 Stage2/Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 72, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C22 symbols, +3 insurance trigger families, +2 positive CSM/rate-cycle anchors, +1 life-insurer price-only beta counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 72, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "axis": "small_insurer_valueup_csm_capital_return_vs_price_only_life_insurer_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C22 should split real CSM/reserve/rate-cycle/capital-return bridge from price-only value-up beta. Non-life and reinsurance cases can become Stage2 if bridge evidence is verified; life-insurer price beta without CSM/reserve/shareholder-return evidence should be capped or routed to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["000370", "003690", "085620"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 72, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C22 should not be a blanket insurance value-up beta. It needs to distinguish low-PBR non-life CSM/ROE/capital-return rerating, reinsurance rate-cycle/reserve earnings visibility, and life-insurer price-only beta with weak CSM/reserve bridge."}
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
This MD is useful for stock-web path calibration and source-repair queue creation,
but coding-agent promotion requires non-proxy company-level evidence.
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
small_insurer_valueup_csm_capital_return_vs_price_only_life_insurer_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 000370, 003690 and 085620.
4. Keep generic C22 weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - IFRS17/CSM quality is explicitly evidenced,
   - reserve or rate-cycle earnings visibility exists,
   - recurring ROE or capital return is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - MFE is mostly price-only insurance beta,
   - MAE_90D or peak-to-later drawdown widens,
   - CSM/reserve/capital-return bridge is weak or stale.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if C22 overblocks verified P&C/reinsurance positives.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 72
next_round = R7
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

