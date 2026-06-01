# E2R Stock-Web v12 Residual Research — R11 Loop 82 / L10 / C32

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 82,
  "computed_next_round": "R12",
  "computed_next_loop": 82,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "governance_control_premium_tender_cap_guardrail",
    "holdco_restructuring_valueup_control_discount_event_bridge",
    "holding_company_theme_whipsaw_boundary",
    "share_count_validation_queue_creation",
    "event_mechanics_validation_queue_creation",
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

Previous completed state in this interactive run: R10 / loop 82.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 82
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
computed_next_round = R12
computed_next_loop = 82
```

R11 was routed to C32 because this run focuses on governance / control-premium / holding-company restructuring event mechanics rather than a normal sector research round.  
This file avoids the top-covered C32 names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C32 concentration in:

```text
010130, 041510, 011200, 008930, UNKNOWN_SYMBOL, 000240
```

This run uses three different governance/holdco symbols:

```text
000150 / 두산 / holdco restructuring and control-discount value-unlock lifecycle
034730 / SK / holdco value-up / control-discount whipsaw with share-count validation
003550 / LG / bounded holdco value-up RiskWatch / no forced 4B
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
034730 shows share-count changes inside the selected 2024 shard and requires coding-agent validation.
000150 and 034730 require event-mechanics validation before runtime promotion.
```

## Research thesis

C32 is not “지주사/지배구조 테마가 올랐다.”

The mechanism must pass through:

```text
governance / restructuring / value-up headline
→ event mechanics
→ NAV or asset-value bridge
→ control-premium or discount-closing logic
→ shareholder process, timing and completion probability
→ downside cap
→ durable rerating
```

지배구조 이벤트는 소문이 아니라 계약서의 조건표다.  
C32가 보려는 것은 headline의 열기가 실제 절차, 권리, 가격 하한, 주주총회·이사회·공개매수 구조로 굳는지다.

---

## Case 1 — Holdco restructuring lifecycle candidate: 000150 / 두산

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
event_mechanics_validation_required = true
source_repair_required = true
```

The source-repair task is portfolio restructuring mechanics, board/shareholder process, asset/NAV bridge, control-discount closing logic, timing and downside cap evidence.

```text
evidence_family = HOLDCO_RESTRUCTURING_PORTFOLIO_VALUE_UNLOCK_CONTROL_DISCOUNT_GOVERNANCE_EVENT_NAV_BRIDGE
case_role = positive_holdco_restructuring_control_discount_lifecycle_with_event_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 90,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000150/2024.csv`:

```text
2024-02-01,90200,97100,88500,97000
2024-03-07,92900,110900,92100,107900
2024-03-15,132600,159000,130300,145000
2024-03-29,153300,178200,153300,155500
2024-07-24,205000,213000,195000,195000
2024-08-05,142200,143000,122000,128100
2024-10-17,198000,210000,194400,210000
2024-10-29,212500,218500,199900,202000
2024-10-31,198500,200500,192600,200500
```

### Backtest

```text
MFE_30D  = +76.27%
MAE_30D  = -1.88%
MFE_90D  = +97.56%
MAE_90D  = -1.88%
MFE_180D = +142.24%
MAE_180D = -1.88%
peak_180 = 218,500 on 2024-10-29
trough_180 = 88,500 on 2024-02-01
peak_to_later_drawdown = -11.85%
```

### Interpretation

This is a C32 high-MFE governance/restructuring lifecycle candidate after source repair.  
The price path is strong enough to protect, but the row cannot become runtime Green until event mechanics and NAV/control-premium bridge are verified.

Correct treatment:

```text
verified restructuring mechanics / NAV bridge / shareholder process / downside cap → Stage2 possible
event mechanics validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Governance theme whipsaw: 034730 / SK

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
event_mechanics_validation_required = true
source_repair_required = true
```

This row tests holding-company value-up / control-discount theme beta without enough NAV, event-mechanics and downside-cap bridge.

```text
evidence_family = HOLDCO_VALUEUP_CONTROL_DISCOUNT_CAPITAL_ALLOCATION_EVENT_WITH_WEAK_NAV_TIMING_DOWNSIDE_CAP_BRIDGE
case_role = counterexample_holdco_valueup_theme_whipsaw_local4b_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 182,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/034/034730/2024.csv`:

```text
2024-02-01,182600,198300,180900,197000
2024-02-19,195800,209500,195500,207500
2024-02-23,206500,212000,201000,204000
2024-05-30,143300,167700,143200,158100
2024-06-03,176200,192900,176000,178800
2024-06-20,165100,166900,156900,160500
2024-08-05,142400,143000,128400,131300
2024-09-20,149600,156700,147500,154000
2024-10-31,150200,150200,147300,148200
```

### Backtest

```text
MFE_30D  = +16.10%
MAE_30D  = -2.35%
MFE_90D  = +16.10%
MAE_90D  = -21.58%
MFE_180D = +16.10%
MAE_180D = -29.68%
peak_180 = 212,000 on 2024-02-23
trough_180 = 128,400 on 2024-08-05
peak_to_later_drawdown = -39.43%
```

### Interpretation

This is a C32 governance/value-up theme-whipsaw boundary.  
The early MFE was not enough because the event mechanics, NAV bridge and downside cap were not verified, and the later MAE widened.

Correct treatment:

```text
holdco value-up / control-discount theme beta
→ no verified event mechanics / NAV bridge / downside cap
→ local 4B-watch
→ share-count and event-mechanics validation before runtime ingestion
```

---

## Case 3 — Bounded no-forced-4B boundary: 003550 / LG

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests bounded holding-company value-up / shareholder-return theme with incomplete event bridge.

```text
evidence_family = HOLDCO_VALUEUP_CONTROL_DISCOUNT_SHAREHOLDER_RETURN_THEME_WITH_BOUNDED_MAE_AND_WEAK_EVENT_BRIDGE
case_role = overbearish_counterexample_bounded_holdco_valueup_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 81,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003550/2024.csv`:

```text
2024-02-01,81800,93700,81200,88100
2024-02-19,98000,103600,96800,103500
2024-03-14,100200,101500,98200,101400
2024-04-05,80500,81500,78700,80100
2024-08-05,83800,83800,77400,78100
2024-09-03,79700,85900,79500,85400
2024-10-25,76000,76100,74900,75400
2024-10-31,77800,77800,75500,75700
```

### Backtest

```text
MFE_30D  = +26.65%
MAE_30D  = -0.73%
MFE_90D  = +26.65%
MAE_90D  = -5.38%
MFE_180D = +26.65%
MAE_180D = -8.44%
peak_180 = 103,600 on 2024-02-19
trough_180 = 74,900 on 2024-10-25
peak_to_later_drawdown = -27.70%
```

### Interpretation

This is not durable Stage2 without source repair, but it is also not forced local 4B.  
The MAE stayed bounded enough that the model should not create a price-only bearish escalation.

Correct treatment:

```text
holding-company value-up / shareholder-return watch
bounded MAE
→ no durable Stage2 without event mechanics / NAV / downside cap bridge
→ no forced 4B without non-price event failure
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
governance_event_mechanics_required = strengthen
NAV_control_premium_downside_cap_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
share_count_validation_guard = strengthen
event_mechanics_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C32_holdco_valueup_weight = true
do_not_treat_all_governance_MFE_as_Green = true
do_not_ingest_sharecount_or_event_sensitive_rows_without_validation = true
do_not_force_4B_on_bounded_holdco_rows_without_non_price_event_failure = true
do_not_convert_governance_drawdown_to_hard_4C_without_non_price_tender_failure_control_break_event_cancelled_regulatory_or_financing_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW
```

This fine archetype covers:

```text
1. holdco restructuring / NAV bridge / event mechanics → Stage2 possible after source repair
2. holdco value-up / control-discount beta without bridge → false Stage2 / local 4B
3. bounded holding-company value-up watch → RiskWatch / no durable Stage2 / no forced 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L82-C32-000150-DOOSAN-HOLDCO-RESTRUCTURING-CONTROL-DISCOUNT-LIFECYCLE", "symbol": "000150", "company_name": "두산", "round": "R11", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-HoldcoRestructuringControlDiscountValueUnlockBridgeWithEventValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should protect governance/restructuring positives only when event mechanics, board/shareholder process, asset/NAV bridge, control-premium logic, timing and downside cap are visible. Doosan produced very large MFE with shallow entry-basis MAE, but the row still needs source repair and event-mechanics validation before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy event mechanics, shareholder process, control-premium logic, NAV/asset bridge, timing and downside cap evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L82-C32-034730-SK-HOLDCO-VALUEUP-SHARECOUNT-WHIPSAW", "symbol": "034730", "company_name": "SK", "round": "R11", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / HoldcoValueupControlDiscountEventWhipsawWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should not treat holding-company value-up or control-discount beta as durable Stage2 unless event mechanics, asset/NAV bridge, capital allocation, shareholder process, timing and downside cap are visible. SK had early MFE but then a deep MAE path and stock-web share-count movement, so validation is mandatory.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy event mechanics, shareholder process, control-premium logic, NAV/asset bridge, timing and downside cap evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L82-C32-003550-LG-HOLDCO-VALUEUP-BOUNDED-NO-FORCED4B", "symbol": "003550", "company_name": "LG", "round": "R11", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW", "case_type": "governance_control_premium_tender_cap", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BoundedHoldcoValueupControlDiscountNoDurableStage2NoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C32 should not force bounded holding-company value-up rows into 4B when no non-price event break is confirmed, but it also should not call durable Stage2 without explicit event mechanics, NAV bridge, shareholder process and downside cap. LG is a bounded RiskWatch/no-forced-4B row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy event mechanics, shareholder process, control-premium logic, NAV/asset bridge, timing and downside cap evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L82-C32-000150-DOOSAN-HOLDCO-RESTRUCTURING-CONTROL-DISCOUNT-LIFECYCLE", "case_id": "R11L82-C32-000150-DOOSAN-HOLDCO-RESTRUCTURING-CONTROL-DISCOUNT-LIFECYCLE", "symbol": "000150", "company_name": "두산", "round": "R11", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail", "trigger_type": "Stage2-Lifecycle-HoldcoRestructuringControlDiscountValueUnlockBridgeWithEventValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 90200.0, "evidence_available_at_that_date": "HOLDCO_RESTRUCTURING_PORTFOLIO_VALUE_UNLOCK_CONTROL_DISCOUNT_GOVERNANCE_EVENT_NAV_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DOOSAN_2024_HOLDCO_RESTRUCTURING_PORTFOLIO_VALUE_UNLOCK_CONTROL_DISCOUNT_EVENT_NAV_BRIDGE", "stage2_evidence_fields": ["event_mechanics_candidate", "NAV_or_control_premium_bridge_candidate", "shareholder_process_downside_cap_candidate"], "stage3_evidence_fields": ["relative_strength", "timing_or_completion_probability_candidate"], "stage4b_evidence_fields": ["governance_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000150/2024.csv", "profile_path": "atlas/symbol_profiles/000/000150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 76.27, "MFE_90D_pct": 97.56, "MFE_180D_pct": 142.24, "MAE_30D_pct": -1.88, "MAE_90D_pct": -1.88, "MAE_180D_pct": -1.88, "peak_date": "2024-10-29", "peak_price": 218500.0, "drawdown_after_peak_pct": -11.85, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_governance_event_peak_if_event_mechanics_NAV_or_downside_cap_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_tender_failure_control_break_event_cancelled_regulatory_or_financing_break", "trigger_outcome_label": "positive_holdco_restructuring_control_discount_lifecycle_with_event_validation", "current_profile_verdict": "C32 should protect governance/restructuring positives only when event mechanics, board/shareholder process, asset/NAV bridge, control-premium logic, timing and downside cap are visible. Doosan produced very large MFE with shallow entry-basis MAE, but the row still needs source repair and event-mechanics validation before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_event_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOVERNANCE_EVENT_000150_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L82-C32-034730-SK-HOLDCO-VALUEUP-SHARECOUNT-WHIPSAW", "case_id": "R11L82-C32-034730-SK-HOLDCO-VALUEUP-SHARECOUNT-WHIPSAW", "symbol": "034730", "company_name": "SK", "round": "R11", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail", "trigger_type": "Stage2-FalsePositive / HoldcoValueupControlDiscountEventWhipsawWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 182600.0, "evidence_available_at_that_date": "HOLDCO_VALUEUP_CONTROL_DISCOUNT_CAPITAL_ALLOCATION_EVENT_WITH_WEAK_NAV_TIMING_DOWNSIDE_CAP_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SK_2024_HOLDCO_VALUEUP_CONTROL_DISCOUNT_CAPITAL_ALLOCATION_EVENT_NAV_TIMING_DOWNSIDE_CAP_BRIDGE", "stage2_evidence_fields": ["event_mechanics_candidate", "NAV_or_control_premium_bridge_candidate", "shareholder_process_downside_cap_candidate"], "stage3_evidence_fields": ["relative_strength", "timing_or_completion_probability_candidate"], "stage4b_evidence_fields": ["governance_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034730/2024.csv", "profile_path": "atlas/symbol_profiles/034/034730.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.1, "MFE_90D_pct": 16.1, "MFE_180D_pct": 16.1, "MAE_30D_pct": -2.35, "MAE_90D_pct": -21.58, "MAE_180D_pct": -29.68, "peak_date": "2024-02-23", "peak_price": 212000.0, "drawdown_after_peak_pct": -39.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_governance_event_peak_if_event_mechanics_NAV_or_downside_cap_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_tender_failure_control_break_event_cancelled_regulatory_or_financing_break", "trigger_outcome_label": "counterexample_holdco_valueup_theme_whipsaw_local4b_with_sharecount_validation", "current_profile_verdict": "C32 should not treat holding-company value-up or control-discount beta as durable Stage2 unless event mechanics, asset/NAV bridge, capital allocation, shareholder process, timing and downside cap are visible. SK had early MFE but then a deep MAE path and stock-web share-count movement, so validation is mandatory.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_event_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C32_GOVERNANCE_EVENT_034730_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L82-C32-003550-LG-HOLDCO-VALUEUP-BOUNDED-NO-FORCED4B", "case_id": "R11L82-C32-003550-LG-HOLDCO-VALUEUP-BOUNDED-NO-FORCED4B", "symbol": "003550", "company_name": "LG", "round": "R11", "loop": "82", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW", "loop_objective": "coverage_gap_fill|counterexample_mining|governance_control_premium_tender_cap_guardrail", "trigger_type": "RiskWatch-BoundedHoldcoValueupControlDiscountNoDurableStage2NoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 81800.0, "evidence_available_at_that_date": "HOLDCO_VALUEUP_CONTROL_DISCOUNT_SHAREHOLDER_RETURN_THEME_WITH_BOUNDED_MAE_AND_WEAK_EVENT_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LG_2024_HOLDCO_VALUEUP_CONTROL_DISCOUNT_SHAREHOLDER_RETURN_NAV_EVENT_DOWNSIDE_CAP_BRIDGE", "stage2_evidence_fields": ["event_mechanics_candidate", "NAV_or_control_premium_bridge_candidate", "shareholder_process_downside_cap_candidate"], "stage3_evidence_fields": ["relative_strength", "timing_or_completion_probability_candidate"], "stage4b_evidence_fields": ["governance_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003550/2024.csv", "profile_path": "atlas/symbol_profiles/003/003550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.65, "MFE_90D_pct": 26.65, "MFE_180D_pct": 26.65, "MAE_30D_pct": -0.73, "MAE_90D_pct": -5.38, "MAE_180D_pct": -8.44, "peak_date": "2024-02-19", "peak_price": 103600.0, "drawdown_after_peak_pct": -27.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_governance_event_peak_if_event_mechanics_NAV_or_downside_cap_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_tender_failure_control_break_event_cancelled_regulatory_or_financing_break", "trigger_outcome_label": "overbearish_counterexample_bounded_holdco_valueup_no_forced4b", "current_profile_verdict": "C32 should not force bounded holding-company value-up rows into 4B when no non-price event break is confirmed, but it also should not call durable Stage2 without explicit event mechanics, NAV bridge, shareholder process and downside cap. LG is a bounded RiskWatch/no-forced-4B row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_event_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C32_GOVERNANCE_EVENT_003550_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L82-C32-000150-DOOSAN-HOLDCO-RESTRUCTURING-CONTROL-DISCOUNT-LIFECYCLE", "trigger_id": "TRG_R11L82-C32-000150-DOOSAN-HOLDCO-RESTRUCTURING-CONTROL-DISCOUNT-LIFECYCLE", "symbol": "000150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"event_mechanics_score": 14, "NAV_asset_bridge_score": 14, "control_premium_score": 13, "shareholder_process_score": 12, "timing_downside_cap_score": 12, "relative_strength_score": 14, "sharecount_or_event_validation_risk": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair and event validation", "raw_component_scores_after": {"event_mechanics_score": 16, "NAV_asset_bridge_score": 16, "control_premium_score": 15, "shareholder_process_score": 14, "timing_downside_cap_score": 14, "relative_strength_score": 13, "sharecount_or_event_validation_risk": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + event validation + lifecycle 4B", "changed_components": ["event_mechanics_score", "NAV_asset_bridge_score", "control_premium_score", "shareholder_process_score", "timing_downside_cap_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified event mechanics, NAV/asset bridge, control-premium logic, shareholder process, timing and downside cap; cap governance/value-up theme beta when mechanics fail to refresh while protecting bounded holdco rows from forced 4B.", "MFE_90D_pct": 97.56, "MAE_90D_pct": -1.88, "score_return_alignment_label": "governance_event_lifecycle_positive", "current_profile_verdict": "C32 should protect governance/restructuring positives only when event mechanics, board/shareholder process, asset/NAV bridge, control-premium logic, timing and downside cap are visible. Doosan produced very large MFE with shallow entry-basis MAE, but the row still needs source repair and event-mechanics validation before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L82-C32-034730-SK-HOLDCO-VALUEUP-SHARECOUNT-WHIPSAW", "trigger_id": "TRG_R11L82-C32-034730-SK-HOLDCO-VALUEUP-SHARECOUNT-WHIPSAW", "symbol": "034730", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"event_mechanics_score": 4, "NAV_asset_bridge_score": 3, "control_premium_score": 3, "shareholder_process_score": 2, "timing_downside_cap_score": 2, "relative_strength_score": 6, "sharecount_or_event_validation_risk": 10, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"event_mechanics_score": 2, "NAV_asset_bridge_score": 1, "control_premium_score": 1, "shareholder_process_score": 1, "timing_downside_cap_score": 1, "relative_strength_score": 3, "sharecount_or_event_validation_risk": 12, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["event_mechanics_score", "NAV_asset_bridge_score", "control_premium_score", "shareholder_process_score", "timing_downside_cap_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified event mechanics, NAV/asset bridge, control-premium logic, shareholder process, timing and downside cap; cap governance/value-up theme beta when mechanics fail to refresh while protecting bounded holdco rows from forced 4B.", "MFE_90D_pct": 16.1, "MAE_90D_pct": -21.58, "score_return_alignment_label": "false_positive_governance_theme_bridge_gap", "current_profile_verdict": "C32 should not treat holding-company value-up or control-discount beta as durable Stage2 unless event mechanics, asset/NAV bridge, capital allocation, shareholder process, timing and downside cap are visible. SK had early MFE but then a deep MAE path and stock-web share-count movement, so validation is mandatory."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L82-C32-003550-LG-HOLDCO-VALUEUP-BOUNDED-NO-FORCED4B", "trigger_id": "TRG_R11L82-C32-003550-LG-HOLDCO-VALUEUP-BOUNDED-NO-FORCED4B", "symbol": "003550", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"event_mechanics_score": 5, "NAV_asset_bridge_score": 6, "control_premium_score": 5, "shareholder_process_score": 5, "timing_downside_cap_score": 5, "relative_strength_score": 6, "sharecount_or_event_validation_risk": 0, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no forced 4B", "raw_component_scores_after": {"event_mechanics_score": 5, "NAV_asset_bridge_score": 5, "control_premium_score": 4, "shareholder_process_score": 4, "timing_downside_cap_score": 4, "relative_strength_score": 5, "sharecount_or_event_validation_risk": 0, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / no durable Stage2 and no forced 4B", "changed_components": ["event_mechanics_score", "NAV_asset_bridge_score", "control_premium_score", "shareholder_process_score", "timing_downside_cap_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified event mechanics, NAV/asset bridge, control-premium logic, shareholder process, timing and downside cap; cap governance/value-up theme beta when mechanics fail to refresh while protecting bounded holdco rows from forced 4B.", "MFE_90D_pct": 26.65, "MAE_90D_pct": -5.38, "score_return_alignment_label": "bounded_holdco_no_forced4b", "current_profile_verdict": "C32 should not force bounded holding-company value-up rows into 4B when no non-price event break is confirmed, but it also should not call durable Stage2 without explicit event mechanics, NAV bridge, shareholder process and downside cap. LG is a bounded RiskWatch/no-forced-4B row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 82, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_RESTRUCTURING_VALUEUP_CONTROL_DISCOUNT_EVENT_BRIDGE_VS_HOLDING_THEME_WHIPSAW", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "event_mechanics_validation_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C32 governance/holdco symbols outside top-covered 010130/041510/011200/008930/000240 set, +3 Doosan/SK/LG holdco restructuring-control-discount trigger families, +1 lifecycle positive, +1 governance whipsaw local-4B counterexample, +1 bounded no-forced-4B boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_event_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 82, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "axis": "holdco_restructuring_valueup_control_discount_event_bridge_vs_holding_theme_whipsaw", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C32 should split verified governance/restructuring/control-premium event mechanics from generic holding-company value-up theme beta. Stage2 requires event mechanics, NAV/asset bridge, control-premium logic, shareholder process, timing and downside cap. If MFE fades and MAE/post-peak drawdown opens without event-bridge refresh, route to local 4B-watch. Bounded holdco rows should not be forced into 4B without non-price event failure.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["000150", "034730", "003550"], "share_count_validation_required": ["034730"], "event_mechanics_validation_required": ["000150", "034730"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 82, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "existing_axis_strengthened": ["stage2_required_bridge", "governance_event_mechanics_required", "NAV_control_premium_downside_cap_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_MAE_no_forced_4B_guard", "share_count_validation_guard", "event_mechanics_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C32 needs governance/holdco MFE to map into event mechanics, NAV/asset bridge, control-premium logic, shareholder process, timing and downside-cap proof. Doosan is a high-MFE holdco restructuring candidate after event validation; SK is a value-up/control-discount whipsaw requiring share-count and event validation; LG is a bounded holdco row where forced 4B would be too harsh."}
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
000150:
  name = 두산 from 1998-09-15, legacy names before that
  corporate_action_candidate_dates = 1997-10-22, 1998-10-09, 1999-12-03
  selected window = 2024-02-01~D+180
  contamination = false
  event_mechanics_validation_required = true

034730:
  name = SK from 2015-08-17, SK C&C before that
  corporate_action_candidate_dates = 2015-08-17
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
  event_mechanics_validation_required = true

003550:
  name = LG from 2003-03-11, LGCI / LG화학 lineage before that
  corporate_action_candidate_dates = 1999-04-23, 2001-04-25, 2001-09-20, 2002-01-02, 2003-03-11, 2004-08-05
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C32 rows are source_proxy_only / evidence_url_pending.
034730 requires share-count validation before runtime promotion.
000150 and 034730 require event-mechanics validation before runtime promotion.
This MD is useful for stock-web path calibration and C32 governance/control-premium/tender-cap rule-shape discovery,
but coding-agent promotion requires non-proxy event mechanics, shareholder process, control-premium logic, NAV/asset bridge, timing and downside-cap evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C32 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair, 034730 needs share-count validation, and 000150/034730 need event-mechanics validation.

Candidate axis:
holdco_restructuring_valueup_control_discount_event_bridge_vs_holding_theme_whipsaw

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 000150, 034730 and 003550.
4. Validate 034730 share-count changes inside the selected window.
5. Validate 000150 and 034730 event mechanics before runtime promotion.
6. Keep generic C32 governance/value-up weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - governance or restructuring event mechanics are explicit,
   - NAV/asset-value bridge is visible,
   - control-premium or discount-closing logic is credible,
   - shareholder process and timing are visible,
   - downside cap is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
8. Consider local 4B-watch when:
   - the trigger is governance/value-up/holdco theme beta only,
   - event mechanics / NAV / downside cap evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not force local 4B when bounded holdco rows have controlled MAE and no confirmed non-price event failure.
10. Do not convert local 4B-watch into full 4B/4C without non-price tender failure, control break, event cancellation, regulatory issue, financing or legal break.
11. Emit before/after diagnostics and reject if verified governance/event positives or bounded holdco rows are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 82
next_round = R12
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

