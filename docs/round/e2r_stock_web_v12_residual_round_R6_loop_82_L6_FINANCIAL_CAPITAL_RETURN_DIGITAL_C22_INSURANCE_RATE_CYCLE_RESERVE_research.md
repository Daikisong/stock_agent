# E2R Stock-Web v12 Residual Research — R6 Loop 82 / L6 / C22

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 82,
  "computed_next_round": "R7",
  "computed_next_loop": 82,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "fine_archetype_id": "REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "insurance_rate_cycle_reserve_guardrail",
    "reinsurance_life_insurance_reserve_CSM_capital_return_bridge",
    "rate_cut_or_payout_fade_boundary",
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

Previous completed state in this interactive run: R5 / loop 82.

Therefore:

```text
scheduled_round = R6
scheduled_loop = 82
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
computed_next_round = R7
computed_next_loop = 82
```

R6 was routed to C22 because loop 82 R5 used C18 and loop 81 R6 used C21.  
This file tests insurance rate-cycle / CSM / reserve / capital-return bridge boundaries.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C22 concentration in:

```text
000810, 005830, 088350, 001450, 000400, 032830
```

This run uses three different symbols:

```text
003690 / 코리안리 / reinsurance rate-cycle capital-return bridge
082640 / 동양생명 / life-insurance rate-cycle event whipsaw
085620 / 미래에셋생명 / life-insurance rate-cycle payout fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected 180D window.
082640 has event-mechanics validation requirement before runtime promotion.
```

## Research thesis

C22 is not “보험 value-up이 올랐다.”

The mechanism must pass through:

```text
insurance rate-cycle / value-up / reserve headline
→ CSM or reserve quality
→ loss ratio, risk cost or capital buffer
→ payout policy and solvency
→ ROE/PBR bridge
→ durable rerating
```

보험주는 금리표의 숫자가 아니라 준비금과 자본완충, 그리고 배당 여력의 압력계다.  
C22가 보려는 것은 headline이 실제 CSM, 손해율, 지급여력, 주주환원, ROE로 이어지는지다.

---

## Case 1 — Reinsurance positive: 003690 / 코리안리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is reinsurance rate-cycle pricing, reserve adequacy, loss ratio, capital buffer, shareholder return and ROE/PBR bridge evidence.

```text
evidence_family = REINSURANCE_RATE_CYCLE_RESERVE_LOSS_RATIO_CAPITAL_RETURN_ROE_PBR_BRIDGE
case_role = positive_reinsurance_rate_cycle_capital_return_with_bounded_MAE
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,580
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv`:

```text
2024-02-01,7580,7960,7470,7810
2024-02-19,8010,8330,8010,8190
2024-03-07,8130,8420,8080,8350
2024-07-30,8220,8500,8200,8440
2024-08-05,8100,8100,7800,7880
2024-08-26,8900,9000,8880,8930
2024-09-11,8340,8400,8190,8210
2024-10-31,9320,9440,9250,9440
```

### Backtest

```text
MFE_30D  = +9.89%
MAE_30D  = -1.45%
MFE_90D  = +11.08%
MAE_90D  = -1.45%
MFE_180D = +24.54%
MAE_180D = -1.45%
peak_180 = 9,440 on 2024-10-31
trough_180 = 7,470 on 2024-02-01
peak_to_later_drawdown = +0.00%
```

### Interpretation

This is a C22 reinsurance rate-cycle positive after source repair.  
The entry-basis MAE was very controlled, so the model should not overblock it once the non-price bridge is verified.

Correct treatment:

```text
verified reinsurance rate cycle / reserve / loss-ratio / capital-return / ROE bridge → Stage2-Yellow possible
bounded MAE → protect from overblocking
```

---

## Case 2 — Life-insurance event lifecycle: 082640 / 동양생명

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
event_mechanics_validation_required = true
source_repair_required = true
```

The source-repair task is life-insurance CSM/reserve quality, rate-cycle sensitivity, capital-return bridge, payout policy, event mechanics and solvency evidence.

```text
evidence_family = LIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_EVENT_WITH_BRIDGE_VALIDATION
case_role = positive_life_insurance_rate_cycle_event_lifecycle_with_whipsaw_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,925
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv`:

```text
2024-02-01,4925,5480,4810,5380
2024-03-06,6150,6440,6070,6360
2024-03-27,6080,6110,5700,5770
2024-07-31,7930,9440,7710,7970
2024-08-05,8400,8460,7700,7920
2024-08-28,8500,8900,6900,6980
2024-09-11,6000,6030,5700,5780
2024-10-31,5940,6370,5900,6110
```

### Backtest

```text
MFE_30D  = +31.98%
MAE_30D  = -2.34%
MFE_90D  = +31.98%
MAE_90D  = -2.34%
MFE_180D = +91.68%
MAE_180D = -2.34%
peak_180 = 9,440 on 2024-07-31
trough_180 = 4,810 on 2024-02-01
peak_to_later_drawdown = -42.69%
```

### Interpretation

This is a C22 lifecycle/event-whipsaw positive candidate, not a clean permanent Green.  
The MFE was very large, but event mechanics and reserve/capital-return bridge must be validated.

Correct treatment:

```text
verified CSM / reserve / capital-return / payout bridge → Stage2 possible
event mechanics validation first
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

This row tests life-insurance rate-cycle / value-up beta without enough CSM, reserve, solvency and payout bridge.

```text
evidence_family = LIFE_INSURANCE_VALUEUP_RATE_CYCLE_THEME_WITH_WEAK_CSM_RESERVE_CAPITAL_RETURN_BRIDGE
case_role = counterexample_life_insurance_rate_cycle_payout_theme_local4b
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
2024-04-02,4535,4535,4425,4490
2024-08-05,5050,5090,4660,4950
2024-09-12,5300,5300,5180,5290
2024-10-31,5260,5330,5250,5270
```

### Backtest

```text
MFE_30D  = +14.64%
MAE_30D  = -11.82%
MFE_90D  = +14.64%
MAE_90D  = -21.96%
MFE_180D = +14.64%
MAE_180D = -21.96%
peak_180 = 6,500 on 2024-02-06
trough_180 = 4,425 on 2024-04-02
peak_to_later_drawdown = -31.92%
```

### Interpretation

This is a C22 false-positive / local-4B boundary.  
The early insurance value-up spike did not validate durable CSM/reserve/capital-return rerating.

Correct treatment:

```text
life-insurance rate-cycle / value-up beta
→ no verified CSM / reserve / solvency / payout bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
insurance_rate_cycle_CSM_reserve_bridge_required = strengthen
capital_return_ROE_PBR_bridge_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
event_mechanics_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C22_insurance_valueup_weight = true
do_not_treat_all_insurance_MFE_as_Green = true
do_not_convert_insurance_drawdown_to_hard_4C_without_non_price_reserve_solvency_payout_or_regulatory_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE
```

This fine archetype covers:

```text
1. reinsurance rate-cycle / loss-ratio / capital-return bridge → Stage2-Yellow possible after source repair
2. life-insurance CSM/reserve/capital-return event lifecycle → Stage2 possible after event validation
3. life-insurance value-up/rate-cycle beta without reserve/payout bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L82-C22-003690-KOREAN-RE-REINSURANCE-RATE-CYCLE-CAPITAL-RETURN", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": "82", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Yellow-ReinsuranceRateCycleReserveCapitalReturnBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should allow reinsurance positives when rate-cycle pricing, reserve adequacy, loss ratio, capital buffer, shareholder return and ROE/PBR bridge are visible. Korean Re had controlled entry-basis MAE and steady later MFE, so it is a protected positive after source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve quality, rate-cycle sensitivity, loss ratio, solvency/capital buffer, payout policy and ROE/PBR bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L82-C22-082640-TONGLIFE-LIFE-INSURANCE-RATE-CYCLE-EVENT-WHIPSAW", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": "82", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-LifeInsuranceRateCycleCapitalReturnEventWhipsawWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 can protect life-insurance positives when CSM/reserve quality, rate-cycle sensitivity, capital return and payout bridge are visible. Tongyang Life had very large MFE but also a violent post-peak whipsaw, so event mechanics and bridge refresh are required.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve quality, rate-cycle sensitivity, loss ratio, solvency/capital buffer, payout policy and ROE/PBR bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R6L82-C22-085620-MIRAE-ASSET-LIFE-RATE-CYCLE-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "82", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE", "case_type": "insurance_rate_cycle_reserve", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LifeInsuranceRateCyclePayoutFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM quality, reserve adequacy, payout policy, solvency ratio and ROE bridge are visible. Mirae Asset Life had an early spike and then persistent MAE, so it is a local-4B fade candidate.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy CSM/reserve quality, rate-cycle sensitivity, loss ratio, solvency/capital buffer, payout policy and ROE/PBR bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L82-C22-003690-KOREAN-RE-REINSURANCE-RATE-CYCLE-CAPITAL-RETURN", "case_id": "R6L82-C22-003690-KOREAN-RE-REINSURANCE-RATE-CYCLE-CAPITAL-RETURN", "symbol": "003690", "company_name": "코리안리", "round": "R6", "loop": "82", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-Yellow-ReinsuranceRateCycleReserveCapitalReturnBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7580.0, "evidence_available_at_that_date": "REINSURANCE_RATE_CYCLE_RESERVE_LOSS_RATIO_CAPITAL_RETURN_ROE_PBR_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KOREAN_RE_2024_REINSURANCE_RATE_CYCLE_RESERVE_LOSS_RATIO_CAPITAL_RETURN_ROE_PBR_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_CSM_candidate", "reserve_or_loss_ratio_candidate", "capital_return_ROE_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "solvency_or_capital_buffer_candidate"], "stage4b_evidence_fields": ["insurance_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv", "profile_path": "atlas/symbol_profiles/003/003690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.89, "MFE_90D_pct": 11.08, "MFE_180D_pct": 24.54, "MAE_30D_pct": -1.45, "MAE_90D_pct": -1.45, "MAE_180D_pct": -1.45, "peak_date": "2024-10-31", "peak_price": 9440.0, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_cycle_peak_if_CSM_reserve_payout_or_ROE_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_strengthening_loss_ratio_shock_solvency_damage_payout_cut_or_regulatory_break", "trigger_outcome_label": "positive_reinsurance_rate_cycle_capital_return_with_bounded_MAE", "current_profile_verdict": "C22 should allow reinsurance positives when rate-cycle pricing, reserve adequacy, loss ratio, capital buffer, shareholder return and ROE/PBR bridge are visible. Korean Re had controlled entry-basis MAE and steady later MFE, so it is a protected positive after source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_event_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_003690_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L82-C22-082640-TONGLIFE-LIFE-INSURANCE-RATE-CYCLE-EVENT-WHIPSAW", "case_id": "R6L82-C22-082640-TONGLIFE-LIFE-INSURANCE-RATE-CYCLE-EVENT-WHIPSAW", "symbol": "082640", "company_name": "동양생명", "round": "R6", "loop": "82", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-Lifecycle-LifeInsuranceRateCycleCapitalReturnEventWhipsawWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4925.0, "evidence_available_at_that_date": "LIFE_INSURANCE_RATE_CYCLE_CSM_RESERVE_CAPITAL_RETURN_EVENT_WITH_BRIDGE_VALIDATION", "evidence_source": "source_proxy_manual_verification_required:TONGYANG_LIFE_2024_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_EVENT_PAYOUT_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_CSM_candidate", "reserve_or_loss_ratio_candidate", "capital_return_ROE_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "solvency_or_capital_buffer_candidate"], "stage4b_evidence_fields": ["insurance_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv", "profile_path": "atlas/symbol_profiles/082/082640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.98, "MFE_90D_pct": 31.98, "MFE_180D_pct": 91.68, "MAE_30D_pct": -2.34, "MAE_90D_pct": -2.34, "MAE_180D_pct": -2.34, "peak_date": "2024-07-31", "peak_price": 9440.0, "drawdown_after_peak_pct": -42.69, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_cycle_peak_if_CSM_reserve_payout_or_ROE_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_strengthening_loss_ratio_shock_solvency_damage_payout_cut_or_regulatory_break", "trigger_outcome_label": "positive_life_insurance_rate_cycle_event_lifecycle_with_whipsaw_validation", "current_profile_verdict": "C22 can protect life-insurance positives when CSM/reserve quality, rate-cycle sensitivity, capital return and payout bridge are visible. Tongyang Life had very large MFE but also a violent post-peak whipsaw, so event mechanics and bridge refresh are required.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_event_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_082640_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R6L82-C22-085620-MIRAE-ASSET-LIFE-RATE-CYCLE-FADE", "case_id": "R6L82-C22-085620-MIRAE-ASSET-LIFE-RATE-CYCLE-FADE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "82", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|insurance_rate_cycle_reserve_guardrail", "trigger_type": "Stage2-FalsePositive / LifeInsuranceRateCyclePayoutFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5670.0, "evidence_available_at_that_date": "LIFE_INSURANCE_VALUEUP_RATE_CYCLE_THEME_WITH_WEAK_CSM_RESERVE_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MIRAE_ASSET_LIFE_2024_CSM_RESERVE_RATE_CYCLE_PAYOUT_SOLVENCY_ROE_BRIDGE", "stage2_evidence_fields": ["rate_cycle_or_CSM_candidate", "reserve_or_loss_ratio_candidate", "capital_return_ROE_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "solvency_or_capital_buffer_candidate"], "stage4b_evidence_fields": ["insurance_valueup_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.64, "MFE_90D_pct": 14.64, "MFE_180D_pct": 14.64, "MAE_30D_pct": -11.82, "MAE_90D_pct": -21.96, "MAE_180D_pct": -21.96, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -31.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_insurance_rate_cycle_peak_if_CSM_reserve_payout_or_ROE_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reserve_strengthening_loss_ratio_shock_solvency_damage_payout_cut_or_regulatory_break", "trigger_outcome_label": "counterexample_life_insurance_rate_cycle_payout_theme_local4b", "current_profile_verdict": "C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM quality, reserve adequacy, payout policy, solvency ratio and ROE bridge are visible. Mirae Asset Life had an early spike and then persistent MAE, so it is a local-4B fade candidate.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_event_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_085620_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L82-C22-003690-KOREAN-RE-REINSURANCE-RATE-CYCLE-CAPITAL-RETURN", "trigger_id": "TRG_R6L82-C22-003690-KOREAN-RE-REINSURANCE-RATE-CYCLE-CAPITAL-RETURN", "symbol": "003690", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 14, "CSM_reserve_quality_score": 14, "loss_ratio_or_risk_score": 12, "capital_return_score": 13, "ROE_PBR_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"rate_cycle_score": 16, "CSM_reserve_quality_score": 16, "loss_ratio_or_risk_score": 14, "capital_return_score": 15, "ROE_PBR_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "loss_ratio_or_risk_score", "capital_return_score", "ROE_PBR_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate-cycle/CSM/reserve quality, capital buffer, payout policy and ROE/PBR bridge; cap insurance value-up/rate-cycle theme beta when bridge fails to refresh.", "MFE_90D_pct": 11.08, "MAE_90D_pct": -1.45, "score_return_alignment_label": "insurance_rate_cycle_positive_with_lifecycle_4b", "current_profile_verdict": "C22 should allow reinsurance positives when rate-cycle pricing, reserve adequacy, loss ratio, capital buffer, shareholder return and ROE/PBR bridge are visible. Korean Re had controlled entry-basis MAE and steady later MFE, so it is a protected positive after source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L82-C22-082640-TONGLIFE-LIFE-INSURANCE-RATE-CYCLE-EVENT-WHIPSAW", "trigger_id": "TRG_R6L82-C22-082640-TONGLIFE-LIFE-INSURANCE-RATE-CYCLE-EVENT-WHIPSAW", "symbol": "082640", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 14, "CSM_reserve_quality_score": 14, "loss_ratio_or_risk_score": 12, "capital_return_score": 13, "ROE_PBR_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"rate_cycle_score": 16, "CSM_reserve_quality_score": 16, "loss_ratio_or_risk_score": 14, "capital_return_score": 15, "ROE_PBR_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "loss_ratio_or_risk_score", "capital_return_score", "ROE_PBR_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate-cycle/CSM/reserve quality, capital buffer, payout policy and ROE/PBR bridge; cap insurance value-up/rate-cycle theme beta when bridge fails to refresh.", "MFE_90D_pct": 31.98, "MAE_90D_pct": -2.34, "score_return_alignment_label": "insurance_rate_cycle_positive_with_lifecycle_4b", "current_profile_verdict": "C22 can protect life-insurance positives when CSM/reserve quality, rate-cycle sensitivity, capital return and payout bridge are visible. Tongyang Life had very large MFE but also a violent post-peak whipsaw, so event mechanics and bridge refresh are required."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L82-C22-085620-MIRAE-ASSET-LIFE-RATE-CYCLE-FADE", "trigger_id": "TRG_R6L82-C22-085620-MIRAE-ASSET-LIFE-RATE-CYCLE-FADE", "symbol": "085620", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"rate_cycle_score": 5, "CSM_reserve_quality_score": 3, "loss_ratio_or_risk_score": 3, "capital_return_score": 2, "ROE_PBR_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"rate_cycle_score": 3, "CSM_reserve_quality_score": 1, "loss_ratio_or_risk_score": 1, "capital_return_score": 1, "ROE_PBR_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["rate_cycle_score", "CSM_reserve_quality_score", "loss_ratio_or_risk_score", "capital_return_score", "ROE_PBR_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rate-cycle/CSM/reserve quality, capital buffer, payout policy and ROE/PBR bridge; cap insurance value-up/rate-cycle theme beta when bridge fails to refresh.", "MFE_90D_pct": 14.64, "MAE_90D_pct": -21.96, "score_return_alignment_label": "false_positive_insurance_rate_cycle_bridge_gap", "current_profile_verdict": "C22 should not treat life-insurance value-up/rate-cycle beta as durable Stage2 unless CSM quality, reserve adequacy, payout policy, solvency ratio and ROE bridge are visible. Mirae Asset Life had an early spike and then persistent MAE, so it is a local-4B fade candidate."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R6", "loop": 82, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "REINSURANCE_LIFE_INSURANCE_RATE_CYCLE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_RATE_CUT_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "event_mechanics_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C22 insurance symbols outside top-covered 000810/005830/088350/001450/000400/032830 set, +3 reinsurance/life-insurance/rate-cycle trigger families, +2 insurance rate-cycle positives, +1 life-insurance payout/rate-cycle local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_event_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R6", "loop": 82, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "axis": "reinsurance_life_insurance_rate_cycle_reserve_CSM_capital_return_bridge_vs_rate_cut_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C22 should split verified reinsurance/life-insurance CSM-reserve-capital-return rerating from generic insurance value-up/rate-cycle beta. Stage2 requires rate-cycle premise, CSM/reserve quality, loss-ratio or risk-cost control, solvency/capital buffer, payout policy and ROE/PBR bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Event-whipsaw rows need event-mechanics validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["003690", "082640", "085620"], "event_mechanics_validation_required": ["082640"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": 82, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "existing_axis_strengthened": ["stage2_required_bridge", "insurance_rate_cycle_CSM_reserve_bridge_required", "capital_return_ROE_PBR_bridge_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "event_mechanics_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C22 needs insurance value-up/rate-cycle MFE to map into CSM/reserve quality, loss ratio or risk-cost control, capital buffer, payout policy and ROE/PBR proof. Korean Re and Tongyang Life are positives after source repair and validation; Mirae Asset Life shows early value-up/rate-cycle beta fading into local 4B when the bridge is weak."}
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
003690:
  name = 코리안리 from 2002-07-02, 대한재보험 before that
  corporate_action_candidate_dates = 1997-03-29, 2004-07-20
  selected window = 2024-02-01~D+180
  contamination = false

082640:
  name = 동양생명 from 2010-10-19, 동양생명보험 before that
  corporate_action_candidate_dates = 2017-04-11
  selected window = 2024-02-01~D+180
  contamination = false
  event_mechanics_validation_required = true

085620:
  name = 미래에셋생명
  corporate_action_candidate_dates = 2018-03-23
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C22 rows are source_proxy_only / evidence_url_pending.
082640 requires event-mechanics validation before runtime promotion.
This MD is useful for stock-web path calibration and C22 insurance-rate-cycle rule-shape discovery,
but coding-agent promotion requires non-proxy CSM/reserve quality, loss ratio or risk-cost control, capital buffer, payout policy and ROE/PBR evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R6/C22 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 082640 needs event-mechanics validation.

Candidate axis:
reinsurance_life_insurance_rate_cycle_reserve_CSM_capital_return_bridge_vs_rate_cut_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 003690, 082640 and 085620.
4. Validate 082640 event mechanics and source availability before runtime promotion.
5. Keep generic C22 insurance value-up/rate-cycle weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - rate-cycle or CSM/reserve premise is explicit,
   - reserve quality / loss-ratio / risk-cost evidence is visible,
   - solvency or capital buffer is credible,
   - payout policy and ROE/PBR bridge exist,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is insurance value-up / rate-cycle theme beta only,
   - CSM/reserve/capital-return/ROE evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price reserve strengthening, loss-ratio shock, solvency damage, payout cut, regulatory issue or earnings-quality break.
9. Emit before/after diagnostics and reject if verified insurance-rate-cycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R6
completed_loop = 82
next_round = R7
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

