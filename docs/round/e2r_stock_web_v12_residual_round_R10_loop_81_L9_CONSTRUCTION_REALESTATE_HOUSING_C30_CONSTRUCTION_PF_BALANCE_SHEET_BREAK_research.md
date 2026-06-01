# E2R Stock-Web v12 Residual Research — R10 Loop 81 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 81,
  "computed_next_round": "R11",
  "computed_next_loop": 81,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "PF_refinancing_liquidity_orderbook_boundary_guardrail",
    "mid_builder_orderbook_recovery_bridge",
    "small_builder_high_MAE_local4B",
    "bounded_large_builder_no_forced4B_no_hard4C",
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

Previous completed state in this interactive run: R9 / loop 81.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 81
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 81
```

R10 is the construction/PF balance-sheet-break round.  
This file avoids the top-covered C30 names and avoids loop-80 R10 names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C30 concentration in:

```text
006360, 294870, 375500, UNKNOWN_SYMBOL, 000720
```

This run uses three different symbols:

```text
014790 / HL D&I / mid-builder orderbook recovery candidate
002780 / 진흥기업 / small-builder PF high-MAE local 4B
047040 / 대우건설 / bounded large-builder no-forced-4B / no-hard-4C boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C30 is not “건설주가 빠졌다” and it is also not “건설주가 반등했다.”

The severity ladder remains:

```text
PF / refinancing / orderbook fear
→ RiskWatch

orderbook / housing recovery with controlled MAE
→ recovery candidate only after PF and liquidity source repair

PF / refinancing fear + high MAE or post-peak drawdown
→ local 4B-watch

default / refinancing failure / impairment / covenant / solvency break
→ full 4B or hard 4C
```

PF 우려는 지반의 물기다.  
C30이 보려는 것은 반등의 물결이 실제 수주잔고와 현금흐름으로 굳는지, 아니면 땅 밑 균열이 커지는지다.

---

## Case 1 — Recovery candidate: 014790 / HL D&I

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is orderbook quality, housing project mix, PF exposure, refinancing access, liquidity and margin bridge evidence.

```text
evidence_family = MID_BUILDER_ORDERBOOK_HOUSING_RECOVERY_PF_REFINANCING_LIQUIDITY_MARGIN_BRIDGE
case_role = positive_mid_builder_recovery_candidate_no_hard4c_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 2,045
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv`:

```text
2024-02-01,2045,2230,2000,2130
2024-03-12,2010,2010,1981,2005
2024-04-16,1958,1958,1935,1938
2024-06-04,2025,2390,2015,2105
2024-06-20,2285,2660,2250,2395
2024-07-19,2410,2645,2360,2540
2024-08-05,2445,2465,2210,2250
2024-08-23,2645,2880,2625,2870
2024-10-31,2370,2385,2300,2360
```

### Backtest

```text
MFE_30D  = +9.05%
MAE_30D  = -3.13%
MFE_90D  = +30.07%
MAE_90D  = -5.38%
MFE_180D = +40.83%
MAE_180D = -5.38%
peak_180 = 2,880 on 2024-08-23
trough_180 = 1,935 on 2024-04-16
peak_to_later_drawdown = -20.14%
```

### Interpretation

This is a C30 recovery candidate, not automatic durable recovery.  
The MFE and controlled MAE are useful, but PF/orderbook/liquidity proof must be repaired before runtime promotion.

Correct treatment:

```text
verified orderbook / housing project quality / PF liquidity bridge → recovery Stage2-Yellow possible
bridge stale after peak → lifecycle local 4B-watch
no hard 4C without non-price solvency break
```

---

## Case 2 — Local 4B risk: 002780 / 진흥기업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is small-builder PF exposure, refinancing access, orderbook, liquidity, covenant, impairment and solvency evidence.

```text
evidence_family = SMALL_BUILDER_PF_REFINANCING_ORDERBOOK_LIQUIDITY_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK
case_role = risk_positive_local4b_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,029
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv`:

```text
2024-02-01,1029,1049,1027,1046
2024-02-16,1068,1094,1068,1088
2024-02-26,1062,1149,1050,1063
2024-03-20,1005,1010,949,1005
2024-04-15,966,984,960,965
2024-08-05,890,893,797,820
2024-09-09,819,837,819,830
2024-10-25,752,753,720,727
2024-11-12,742,850,742,817
```

### Backtest

```text
MFE_30D  = +11.66%
MAE_30D  = -2.92%
MFE_90D  = +11.66%
MAE_90D  = -6.71%
MFE_180D = +11.66%
MAE_180D = -30.03%
peak_180 = 1,149 on 2024-02-26
trough_180 = 720 on 2024-10-25
peak_to_later_drawdown = -37.34%
```

### Interpretation

This is a C30 local 4B risk row.  
The price path had modest early MFE and then widened into high-MAE territory.

Correct treatment:

```text
small-builder PF/refinancing watch + MAE_180D <= -25%
→ local 4B-watch
→ no hard 4C without non-price refinancing/default/solvency break
```

---

## Case 3 — Bounded no-forced-4B boundary: 047040 / 대우건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF/orderbook exposure, liquidity, refinancing, capital buffer and solvency evidence.

```text
evidence_family = LARGE_BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK
case_role = overbearish_counterexample_bounded_no_forced4b_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,910
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv`:

```text
2024-02-01,3910,4005,3905,3965
2024-02-19,4055,4120,4030,4055
2024-03-14,3670,3785,3625,3730
2024-04-08,3775,3785,3710,3720
2024-08-05,3915,3945,3545,3640
2024-08-21,4130,4285,4085,4240
2024-08-26,4285,4320,4220,4260
2024-10-25,3630,3645,3585,3620
2024-10-31,3565,3575,3525,3535
```

### Backtest

```text
MFE_30D  = +5.37%
MAE_30D  = -7.29%
MFE_90D  = +5.37%
MAE_90D  = -7.29%
MFE_180D = +10.49%
MAE_180D = -9.85%
peak_180 = 4,320 on 2024-08-26
trough_180 = 3,525 on 2024-10-31
peak_to_later_drawdown = -18.40%
```

### Interpretation

This is not durable Stage2, but it is also not forced local 4B.  
The price path stayed too bounded to justify a price-only bearish escalation.

Correct treatment:

```text
PF / orderbook RiskWatch
bounded MAE
→ no forced 4B / no hard 4C
→ escalate only with refinancing, impairment, covenant, control or solvency evidence
```

---

## Cross-case residual finding

### What this strengthens

```text
hard_4c_confirmation = strengthen
local_4b_watch_guard = strengthen
recovery_no_hard4c_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
PF_orderbook_refinancing_bridge_required = strengthen
```

### What this does not justify

```text
do_not_treat_all_construction_drawdowns_as_hard_4C = true
do_not_use_price_only_MAE_as_default_or_refinancing_failure = true
do_not_force_4B_on_bounded_builder_rows = true
do_not_call_recovery_durable_without_orderbook_PF_liquidity_bridge = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C
```

This fine archetype covers:

```text
1. builder recovery with controlled MAE → recovery Stage2-Yellow only after PF/orderbook source repair
2. small-builder PF fear + MAE_180D <= -25% or post-peak drawdown <= -35% → local 4B-watch
3. large-builder bounded MAE → RiskWatch / no forced 4B / no hard 4C
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L81-C30-014790-HL-DNI-MID-BUILDER-ORDERBOOK-RECOVERY", "symbol": "014790", "company_name": "HL D&I", "round": "R10", "loop": "81", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "positive", "best_trigger": "RiskWatch-PositiveMidBuilderOrderbookRecoveryNeedsPFBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should allow builder recovery rows only when orderbook, housing project quality, PF exposure, refinancing access, liquidity and margin bridge are visible. HL D&I produced large MFE with controlled entry-basis MAE, but it cannot become durable recovery without PF/orderbook source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook quality, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L81-C30-002780-JINHEUNG-SMALL-BUILDER-HIGHMAE-LOCAL4B", "symbol": "002780", "company_name": "진흥기업", "round": "R10", "loop": "81", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SmallBuilderPFHighMAENoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should escalate small-builder/PF risk to local 4B when the path has little durable MFE and large 180D MAE, but hard 4C still needs non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook quality, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L81-C30-047040-DAEWOO-E&C-BOUNDED-BUILDER-NO-FORCED4B", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "81", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BoundedLargeBuilderPFNoForced4BNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should keep PF/orderbook monitoring active for bounded large builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing, liquidity or solvency break is confirmed.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook quality, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L81-C30-014790-HL-DNI-MID-BUILDER-ORDERBOOK-RECOVERY", "case_id": "R10L81-C30-014790-HL-DNI-MID-BUILDER-ORDERBOOK-RECOVERY", "symbol": "014790", "company_name": "HL D&I", "round": "R10", "loop": "81", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-PositiveMidBuilderOrderbookRecoveryNeedsPFBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 2045.0, "evidence_available_at_that_date": "MID_BUILDER_ORDERBOOK_HOUSING_RECOVERY_PF_REFINANCING_LIQUIDITY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HL_DNI_2024_BUILDER_ORDERBOOK_HOUSING_PF_REFINANCING_LIQUIDITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["PF_or_orderbook_watch", "recovery_or_bounded_MAE_candidate", "source_repair_required"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "bridge_stale_or_absent"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv", "profile_path": "atlas/symbol_profiles/014/014790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.05, "MFE_90D_pct": 30.07, "MFE_180D_pct": 40.83, "MAE_30D_pct": -3.13, "MAE_90D_pct": -5.38, "MAE_180D_pct": -5.38, "peak_date": "2024-08-23", "peak_price": 2880.0, "drawdown_after_peak_pct": -20.14, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "positive_mid_builder_recovery_candidate_no_hard4c_with_later_4b_watch", "current_profile_verdict": "C30 should allow builder recovery rows only when orderbook, housing project quality, PF exposure, refinancing access, liquidity and margin bridge are visible. HL D&I produced large MFE with controlled entry-basis MAE, but it cannot become durable recovery without PF/orderbook source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_SEVERITY_014790_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L81-C30-002780-JINHEUNG-SMALL-BUILDER-HIGHMAE-LOCAL4B", "case_id": "R10L81-C30-002780-JINHEUNG-SMALL-BUILDER-HIGHMAE-LOCAL4B", "symbol": "002780", "company_name": "진흥기업", "round": "R10", "loop": "81", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-SmallBuilderPFHighMAENoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1029.0, "evidence_available_at_that_date": "SMALL_BUILDER_PF_REFINANCING_ORDERBOOK_LIQUIDITY_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK", "evidence_source": "source_proxy_manual_verification_required:JINHEUNG_ENTERPRISE_2024_PF_REFINANCING_ORDERBOOK_LIQUIDITY_SOLVENCY_BRIDGE", "stage2_evidence_fields": ["PF_or_orderbook_watch", "recovery_or_bounded_MAE_candidate", "source_repair_required"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "bridge_stale_or_absent"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv", "profile_path": "atlas/symbol_profiles/002/002780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.66, "MFE_90D_pct": 11.66, "MFE_180D_pct": 11.66, "MAE_30D_pct": -2.92, "MAE_90D_pct": -6.71, "MAE_180D_pct": -30.03, "peak_date": "2024-02-26", "peak_price": 1149.0, "drawdown_after_peak_pct": -37.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_no_hard4c", "current_profile_verdict": "C30 should escalate small-builder/PF risk to local 4B when the path has little durable MFE and large 180D MAE, but hard 4C still needs non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_SEVERITY_002780_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L81-C30-047040-DAEWOO-E&C-BOUNDED-BUILDER-NO-FORCED4B", "case_id": "R10L81-C30-047040-DAEWOO-E&C-BOUNDED-BUILDER-NO-FORCED4B", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "81", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-BoundedLargeBuilderPFNoForced4BNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3910.0, "evidence_available_at_that_date": "LARGE_BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:DAEWOO_E&C_2024_BUILDER_PF_ORDERBOOK_LIQUIDITY_BUFFER_NO_FORCED4B", "stage2_evidence_fields": ["PF_or_orderbook_watch", "recovery_or_bounded_MAE_candidate", "source_repair_required"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "bridge_stale_or_absent"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.37, "MFE_90D_pct": 5.37, "MFE_180D_pct": 10.49, "MAE_30D_pct": -7.29, "MAE_90D_pct": -7.29, "MAE_180D_pct": -9.85, "peak_date": "2024-08-26", "peak_price": 4320.0, "drawdown_after_peak_pct": -18.4, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_bounded_no_forced4b_no_hard4c", "current_profile_verdict": "C30 should keep PF/orderbook monitoring active for bounded large builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing, liquidity or solvency break is confirmed.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_SEVERITY_047040_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L81-C30-014790-HL-DNI-MID-BUILDER-ORDERBOOK-RECOVERY", "trigger_id": "TRG_R10L81-C30-014790-HL-DNI-MID-BUILDER-ORDERBOOK-RECOVERY", "symbol": "014790", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 8, "orderbook_recovery_score": 14, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 8, "execution_risk_score": 12, "information_confidence": 2}, "weighted_score_before": 70, "stage_label_before": "Recovery candidate after source repair", "raw_component_scores_after": {"pf_liquidity_risk": 8, "orderbook_recovery_score": 15, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 9, "execution_risk_score": 13, "information_confidence": 2}, "weighted_score_after": 76, "stage_label_after": "Recovery Stage2-Yellow only after source repair", "changed_components": ["pf_liquidity_risk", "orderbook_recovery_score", "refinancing_break_score", "default_or_control_break_score", "capital_or_group_buffer_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; protect bounded rows from forced 4B; block hard 4C without explicit non-price balance-sheet break.", "MFE_90D_pct": 30.07, "MAE_90D_pct": -5.38, "score_return_alignment_label": "builder_recovery_candidate_with_source_repair", "current_profile_verdict": "C30 should allow builder recovery rows only when orderbook, housing project quality, PF exposure, refinancing access, liquidity and margin bridge are visible. HL D&I produced large MFE with controlled entry-basis MAE, but it cannot become durable recovery without PF/orderbook source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L81-C30-002780-JINHEUNG-SMALL-BUILDER-HIGHMAE-LOCAL4B", "trigger_id": "TRG_R10L81-C30-002780-JINHEUNG-SMALL-BUILDER-HIGHMAE-LOCAL4B", "symbol": "002780", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 18, "orderbook_recovery_score": 2, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 3, "execution_risk_score": 22, "information_confidence": 2}, "weighted_score_before": 31, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 20, "orderbook_recovery_score": 2, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 2, "execution_risk_score": 24, "information_confidence": 2}, "weighted_score_after": 28, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "orderbook_recovery_score", "refinancing_break_score", "default_or_control_break_score", "capital_or_group_buffer_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; protect bounded rows from forced 4B; block hard 4C without explicit non-price balance-sheet break.", "MFE_90D_pct": 11.66, "MAE_90D_pct": -6.71, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should escalate small-builder/PF risk to local 4B when the path has little durable MFE and large 180D MAE, but hard 4C still needs non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L81-C30-047040-DAEWOO-E&C-BOUNDED-BUILDER-NO-FORCED4B", "trigger_id": "TRG_R10L81-C30-047040-DAEWOO-E&C-BOUNDED-BUILDER-NO-FORCED4B", "symbol": "047040", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 7, "orderbook_recovery_score": 6, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 13, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 60, "stage_label_before": "RiskWatch / no forced 4B / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 6, "orderbook_recovery_score": 6, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 14, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 62, "stage_label_after": "RiskWatch / no forced 4B / no hard 4C", "changed_components": ["pf_liquidity_risk", "orderbook_recovery_score", "refinancing_break_score", "default_or_control_break_score", "capital_or_group_buffer_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; protect bounded rows from forced 4B; block hard 4C without explicit non-price balance-sheet break.", "MFE_90D_pct": 5.37, "MAE_90D_pct": -7.29, "score_return_alignment_label": "bounded_no_forced4b_no_hard4c", "current_profile_verdict": "C30 should keep PF/orderbook monitoring active for bounded large builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing, liquidity or solvency break is confirmed."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 81, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDERBOOK_RECOVERY_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "risk_positive_case_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C30 construction/PF symbols outside top-covered 006360/294870/375500/000720 set and outside loop-80 R10 names, +3 HL D&I/Jinheung/Daewoo E&C severity families, +1 recovery candidate, +1 high-MAE local-4B risk path, +1 bounded no-forced-4B boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 81, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "mid_builder_PF_orderbook_recovery_vs_small_builder_high_MAE_and_bounded_no_hard4C", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split mid-builder orderbook recovery candidates from high-MAE small-builder PF local 4B and bounded large-builder no-forced-4B/no-hard-4C rows. Recovery requires orderbook, PF exposure, refinancing, liquidity and margin proof. High MAE can trigger local 4B-watch, but full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["014790", "002780", "047040"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 81, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "recovery_no_hard4c_guard", "bounded_MAE_no_forced_4B_guard", "PF_orderbook_refinancing_bridge_required"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 severity split is strengthened. HL D&I shows a builder recovery candidate after PF/orderbook source repair; Jinheung Enterprise shows a small-builder high-MAE local 4B path; Daewoo E&C shows a bounded large-builder no-forced-4B/no-hard-4C row."}
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
014790:
  name = HL D&I from 2022-09-30, 한라 / 한라건설 before that
  corporate_action_candidate_dates = 1996-01-03, 1997-11-03, 1997-12-27, 1999-12-21, 2010-04-28, 2012-02-06
  selected window = 2024-02-01~D+180
  contamination = false

002780:
  name = 진흥기업
  corporate_action_candidate_dates = 1998-01-20, 2002-08-16, 2006-12-08, 2007-11-06, 2008-02-22, 2009-04-28, 2010-08-10, 2012-04-17, 2015-01-20, 2015-01-28
  selected window = 2024-02-01~D+180
  contamination = false

047040:
  name = 대우건설
  corporate_action_candidate_dates = 2001-07-13, 2003-11-18, 2011-01-18
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C30 severity-splitting discovery,
but coding-agent promotion requires non-proxy PF/refinancing/orderbook/liquidity/covenant/impairment/solvency evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R10/C30 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
mid_builder_PF_orderbook_recovery_vs_small_builder_high_MAE_and_bounded_no_hard4C

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 014790, 002780 and 047040.
4. Keep hard 4C evidence-based:
   - default,
   - court rehabilitation,
   - refinancing failure,
   - auditor/control break,
   - impairment, covenant or solvency break.
5. Use local 4B-watch when:
   - PF/liquidity/orderbook/financing risk is present,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - or post-peak drawdown <= -35%,
   - but hard-break evidence is not confirmed.
6. Keep RiskWatch/no-hard-4C/no-forced-4B when:
   - bounded MAE exists,
   - orderbook/capital/group/support buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
7. Allow recovery Stage2-Yellow only after:
   - orderbook quality,
   - housing project mix,
   - PF exposure,
   - refinancing access,
   - liquidity,
   - margin bridge are source-repaired.
8. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 81
next_round = R11
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

