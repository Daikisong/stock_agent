# E2R Stock-Web v12 Residual Research — R10 Loop 82 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 82,
  "computed_next_round": "R11",
  "computed_next_loop": 82,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "PF_refinancing_liquidity_orderbook_boundary_guardrail",
    "mid_builder_housing_orderbook_recovery_with_sharecount_validation",
    "small_builder_high_MAE_local4B_no_price_only_hard4C",
    "bounded_builder_no_forced4B_guard",
    "share_count_validation_queue_creation",
    "status_validation_queue_creation",
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

Previous completed state in this interactive run: R9 / loop 82.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 82
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 82
```

R10 is the construction/PF balance-sheet-break round.  
This file avoids the top-covered C30 names and avoids loop-81 R10 names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C30 concentration in:

```text
006360, UNKNOWN_SYMBOL, 294870, 047040, 000720, 375500
```

This run uses three different symbols:

```text
010780 / 아이에스동서 / mid-builder housing recovery candidate with share-count validation
004960 / 한신공영 / bounded builder PF RiskWatch / no forced 4B
001470 / 삼부토건 / small-builder high-MAE local 4B / no price-only hard 4C
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
010780 and 001470 show share-count changes inside the selected 2024 shard and require coding-agent validation.
001470 also requires extended status validation before longer-horizon ingestion.
```

## Research thesis

C30 is not “건설주가 반등했다” and it is also not “건설주가 빠졌다.”

The severity ladder remains:

```text
PF / refinancing / orderbook fear
→ RiskWatch

orderbook / housing recovery with controlled or explainable MAE
→ recovery candidate only after PF and liquidity source repair

PF / refinancing fear + high MAE or post-peak drawdown
→ local 4B-watch

default / refinancing failure / impairment / covenant / solvency break
→ full 4B or hard 4C
```

PF 우려는 지반 속 물기다.  
C30이 보려는 것은 반등의 표면이 아니라 수주잔고, PF 노출, 차환, 유동성, 마진이라는 기초공사가 버티는지다.

---

## Case 1 — Recovery candidate with validation: 010780 / 아이에스동서

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is housing project quality, orderbook, PF exposure, refinancing access, liquidity and margin bridge evidence.

```text
evidence_family = MID_BUILDER_HOUSING_RECOVERY_PF_EXPOSURE_REFINANCING_LIQUIDITY_ORDERBOOK_MARGIN_BRIDGE
case_role = positive_mid_builder_housing_recovery_candidate_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 25,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv`:

```text
2024-02-01,25400,26050,25100,25750
2024-02-07,26550,28850,26550,28400
2024-03-08,28000,30300,27750,30100
2024-03-22,29100,31200,29050,30450
2024-04-15,24500,25650,24450,25450
2024-05-30,24650,24850,24400,24600
2024-08-05,23500,23700,20350,20600
2024-10-31,20150,20700,19800,20200
```

### Backtest

```text
MFE_30D  = +19.29%
MAE_30D  = -1.18%
MFE_90D  = +22.83%
MAE_90D  = -3.94%
MFE_180D = +22.83%
MAE_180D = -22.05%
peak_180 = 31,200 on 2024-03-22
trough_180 = 19,800 on 2024-10-31
peak_to_later_drawdown = -36.54%
```

### Interpretation

This is a C30 recovery candidate with validation blockers.  
The early MFE and controlled early MAE are useful, but the later drawdown and share-count movement block runtime promotion until source repair and validation pass.

Correct treatment:

```text
verified housing orderbook / PF exposure / refinancing / liquidity / margin bridge → recovery Stage2-Yellow possible
share-count validation first
bridge stale after peak → lifecycle local 4B-watch
no hard 4C without non-price solvency break
```

---

## Case 2 — Bounded no-forced-4B boundary: 004960 / 한신공영

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests builder PF/orderbook watch with bounded MAE but incomplete recovery bridge.

```text
evidence_family = BUILDER_PF_ORDERBOOK_LIQUIDITY_RISK_WITH_BOUNDED_MAE_AND_WEAK_RECOVERY_BRIDGE
case_role = overbearish_counterexample_bounded_builder_no_forced4b_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,370
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv`:

```text
2024-02-01,7370,7770,7370,7720
2024-02-02,7810,7810,7500,7630
2024-02-27,7090,7210,6990,7090
2024-04-15,6320,6390,6240,approx_stock_web_row
2024-07-30,7190,7560,6890,7340
2024-08-05,6970,6970,6160,6300
2024-09-09,6730,6920,6700,6920
2024-10-25,6740,6800,6570,6790
```

### Backtest

```text
MFE_30D  = +5.97%
MAE_30D  = -5.16%
MFE_90D  = +5.97%
MAE_90D  = -15.33%
MFE_180D = +5.97%
MAE_180D = -16.42%
peak_180 = 7,810 on 2024-02-02
trough_180 = 6,160 on 2024-08-05
peak_to_later_drawdown = -21.13%
```

### Interpretation

This is not durable Stage2, but it is also not forced local 4B.  
The path is weak but still bounded relative to true hard-break examples.

Correct treatment:

```text
builder PF/orderbook RiskWatch
bounded MAE
→ no durable Stage2 without orderbook/PF/liquidity/margin bridge
→ no forced 4B without non-price refinancing or solvency deterioration
```

---

## Case 3 — Local 4B risk / no price-only hard 4C: 001470 / 삼부토건

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
extended_status_validation_required = true
source_repair_required = true
```

The source-repair task is small-builder PF exposure, refinancing access, orderbook, liquidity, covenant, impairment and solvency evidence.

```text
evidence_family = SMALL_BUILDER_PF_REFINANCING_LIQUIDITY_ORDERBOOK_SOLVENCY_RISK_WITH_HIGH_MAE_AND_STATUS_VALIDATION
case_role = risk_positive_local4b_no_price_only_hard4c_with_sharecount_and_status_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,990
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv`:

```text
2024-02-01,1990,2070,1974,2060
2024-02-13,2155,2630,2100,2585
2024-03-15,2565,2865,2430,2690
2024-04-08,1670,1836,1510,1540
2024-07-31,1541,1590,1490,1498
2024-08-05,1369,1369,1150,1259
2024-08-28,672,673,615,625
2024-10-28,448,480,440,476
```

### Backtest

```text
MFE_30D  = +43.97%
MAE_30D  = -0.80%
MFE_90D  = +43.97%
MAE_90D  = -24.12%
MFE_180D = +43.97%
MAE_180D = -77.89%
peak_180 = 2,865 on 2024-03-15
trough_180 = 440 on 2024-10-28
peak_to_later_drawdown = -84.64%
```

### Interpretation

This is a C30 high-MAE local-4B row.  
It is severe enough to require local 4B-watch, share-count validation and status validation, but not enough to emit hard 4C from price alone.

Correct treatment:

```text
small-builder PF/refinancing watch + MAE_180D <= -25%
→ local 4B-watch
→ no hard 4C without default/refinancing failure/covenant/impairment/solvency evidence
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
share_count_validation_guard = strengthen
status_validation_guard = strengthen
```

### What this does not justify

```text
do_not_treat_all_construction_drawdowns_as_hard_4C = true
do_not_use_price_only_MAE_as_default_or_refinancing_failure = true
do_not_force_4B_on_bounded_builder_rows = true
do_not_call_recovery_durable_without_orderbook_PF_liquidity_bridge = true
do_not_ingest_sharecount_or_status_sensitive_rows_without_validation = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B
```

This fine archetype covers:

```text
1. housing/orderbook recovery with validation blocker → recovery Stage2-Yellow only after PF/source repair
2. bounded builder PF watch → RiskWatch / no durable Stage2 / no forced 4B
3. small-builder high-MAE PF risk → local 4B-watch / no price-only hard 4C
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L82-C30-010780-ISDONGSEO-PF-HOUSING-RECOVERY-SHARECOUNT", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": "82", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "positive", "best_trigger": "RiskWatch-PositiveMidBuilderHousingRecoveryPFBridgeWithSharecountValidationAndLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should allow builder recovery rows only when housing project quality, orderbook, PF exposure, refinancing access, liquidity and margin bridge are visible. IS Dongseo produced tradable MFE but later post-peak drawdown and stock-web share-count movement require lifecycle 4B discipline and validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook quality, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L82-C30-004960-HANSHIN-BUILDER-BOUNDED-PF-RISKWATCH", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "82", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BoundedBuilderPFNoDurableStage2NoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not force bounded builder/PF watch rows into 4B when no refinancing, liquidity or solvency break is confirmed, but it also should not call durable Stage2 without orderbook, PF and margin recovery bridge. Hanshin Construction is a bounded RiskWatch row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook quality, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L82-C30-001470-SAMBU-SMALL-BUILDER-HIGHMAE-SHARECOUNT-STATUS", "symbol": "001470", "company_name": "삼부토건", "round": "R10", "loop": "82", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SmallBuilderPFHighMAENoPriceOnlyHard4CWithSharecountStatusValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should escalate small-builder/PF risk to local 4B when the price path shows severe MAE and persistent drawdown, but hard 4C still requires non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence. Sambu also requires share-count and status continuity validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook quality, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L82-C30-010780-ISDONGSEO-PF-HOUSING-RECOVERY-SHARECOUNT", "case_id": "R10L82-C30-010780-ISDONGSEO-PF-HOUSING-RECOVERY-SHARECOUNT", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": "82", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-PositiveMidBuilderHousingRecoveryPFBridgeWithSharecountValidationAndLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 25400.0, "evidence_available_at_that_date": "MID_BUILDER_HOUSING_RECOVERY_PF_EXPOSURE_REFINANCING_LIQUIDITY_ORDERBOOK_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:IS_DONGSEO_2024_HOUSING_ORDERBOOK_PF_EXPOSURE_REFINANCING_LIQUIDITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["PF_or_orderbook_watch", "recovery_or_bounded_MAE_candidate", "source_repair_required"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "bridge_stale_or_absent"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv", "profile_path": "atlas/symbol_profiles/010/010780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.29, "MFE_90D_pct": 22.83, "MFE_180D_pct": 22.83, "MAE_30D_pct": -1.18, "MAE_90D_pct": -3.94, "MAE_180D_pct": -22.05, "peak_date": "2024-03-22", "peak_price": 31200.0, "drawdown_after_peak_pct": -36.54, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "positive_mid_builder_housing_recovery_candidate_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C30 should allow builder recovery rows only when housing project quality, orderbook, PF exposure, refinancing access, liquidity and margin bridge are visible. IS Dongseo produced tradable MFE but later post-peak drawdown and stock-web share-count movement require lifecycle 4B discipline and validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_status_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C30_PF_SEVERITY_010780_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L82-C30-004960-HANSHIN-BUILDER-BOUNDED-PF-RISKWATCH", "case_id": "R10L82-C30-004960-HANSHIN-BUILDER-BOUNDED-PF-RISKWATCH", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "82", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-BoundedBuilderPFNoDurableStage2NoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7370.0, "evidence_available_at_that_date": "BUILDER_PF_ORDERBOOK_LIQUIDITY_RISK_WITH_BOUNDED_MAE_AND_WEAK_RECOVERY_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANSHIN_CONSTRUCTION_2024_BUILDER_PF_ORDERBOOK_LIQUIDITY_REFINANCING_MARGIN_BRIDGE", "stage2_evidence_fields": ["PF_or_orderbook_watch", "recovery_or_bounded_MAE_candidate", "source_repair_required"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "bridge_stale_or_absent"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv", "profile_path": "atlas/symbol_profiles/004/004960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.97, "MFE_90D_pct": 5.97, "MFE_180D_pct": 5.97, "MAE_30D_pct": -5.16, "MAE_90D_pct": -15.33, "MAE_180D_pct": -16.42, "peak_date": "2024-02-02", "peak_price": 7810.0, "drawdown_after_peak_pct": -21.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_bounded_builder_no_forced4b_no_hard4c", "current_profile_verdict": "C30 should not force bounded builder/PF watch rows into 4B when no refinancing, liquidity or solvency break is confirmed, but it also should not call durable Stage2 without orderbook, PF and margin recovery bridge. Hanshin Construction is a bounded RiskWatch row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_status_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_SEVERITY_004960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L82-C30-001470-SAMBU-SMALL-BUILDER-HIGHMAE-SHARECOUNT-STATUS", "case_id": "R10L82-C30-001470-SAMBU-SMALL-BUILDER-HIGHMAE-SHARECOUNT-STATUS", "symbol": "001470", "company_name": "삼부토건", "round": "R10", "loop": "82", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-SmallBuilderPFHighMAENoPriceOnlyHard4CWithSharecountStatusValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1990.0, "evidence_available_at_that_date": "SMALL_BUILDER_PF_REFINANCING_LIQUIDITY_ORDERBOOK_SOLVENCY_RISK_WITH_HIGH_MAE_AND_STATUS_VALIDATION", "evidence_source": "source_proxy_manual_verification_required:SAMBU_CONSTRUCTION_2024_PF_REFINANCING_LIQUIDITY_ORDERBOOK_SOLVENCY_BREAK_VALIDATION", "stage2_evidence_fields": ["PF_or_orderbook_watch", "recovery_or_bounded_MAE_candidate", "source_repair_required"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "bridge_stale_or_absent"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv", "profile_path": "atlas/symbol_profiles/001/001470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 43.97, "MFE_90D_pct": 43.97, "MFE_180D_pct": 43.97, "MAE_30D_pct": -0.8, "MAE_90D_pct": -24.12, "MAE_180D_pct": -77.89, "peak_date": "2024-03-15", "peak_price": 2865.0, "drawdown_after_peak_pct": -84.64, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_no_price_only_hard4c_with_sharecount_and_status_validation", "current_profile_verdict": "C30 should escalate small-builder/PF risk to local 4B when the price path shows severe MAE and persistent drawdown, but hard 4C still requires non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence. Sambu also requires share-count and status continuity validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_status_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C30_PF_SEVERITY_001470_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L82-C30-010780-ISDONGSEO-PF-HOUSING-RECOVERY-SHARECOUNT", "trigger_id": "TRG_R10L82-C30-010780-ISDONGSEO-PF-HOUSING-RECOVERY-SHARECOUNT", "symbol": "010780", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 10, "orderbook_recovery_score": 14, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 8, "sharecount_or_status_validation_risk": 12, "execution_risk_score": 13, "information_confidence": 2}, "weighted_score_before": 70, "stage_label_before": "Recovery candidate after source repair + validation", "raw_component_scores_after": {"pf_liquidity_risk": 10, "orderbook_recovery_score": 16, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 8, "sharecount_or_status_validation_risk": 14, "execution_risk_score": 14, "information_confidence": 2}, "weighted_score_after": 76, "stage_label_after": "Recovery Stage2-Yellow only after source repair + validation", "changed_components": ["pf_liquidity_risk", "orderbook_recovery_score", "refinancing_break_score", "default_or_control_break_score", "capital_or_group_buffer_score", "sharecount_or_status_validation_risk", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; protect bounded rows from forced 4B; block hard 4C without explicit non-price balance-sheet break.", "MFE_90D_pct": 22.83, "MAE_90D_pct": -3.94, "score_return_alignment_label": "builder_recovery_candidate_with_source_repair_and_validation", "current_profile_verdict": "C30 should allow builder recovery rows only when housing project quality, orderbook, PF exposure, refinancing access, liquidity and margin bridge are visible. IS Dongseo produced tradable MFE but later post-peak drawdown and stock-web share-count movement require lifecycle 4B discipline and validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L82-C30-004960-HANSHIN-BUILDER-BOUNDED-PF-RISKWATCH", "trigger_id": "TRG_R10L82-C30-004960-HANSHIN-BUILDER-BOUNDED-PF-RISKWATCH", "symbol": "004960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 7, "orderbook_recovery_score": 5, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 12, "sharecount_or_status_validation_risk": 0, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 60, "stage_label_before": "RiskWatch / no forced 4B / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 6, "orderbook_recovery_score": 5, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 13, "sharecount_or_status_validation_risk": 0, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 62, "stage_label_after": "RiskWatch / no forced 4B / no hard 4C", "changed_components": ["pf_liquidity_risk", "orderbook_recovery_score", "refinancing_break_score", "default_or_control_break_score", "capital_or_group_buffer_score", "sharecount_or_status_validation_risk", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; protect bounded rows from forced 4B; block hard 4C without explicit non-price balance-sheet break.", "MFE_90D_pct": 5.97, "MAE_90D_pct": -15.33, "score_return_alignment_label": "bounded_no_forced4b_no_hard4c", "current_profile_verdict": "C30 should not force bounded builder/PF watch rows into 4B when no refinancing, liquidity or solvency break is confirmed, but it also should not call durable Stage2 without orderbook, PF and margin recovery bridge. Hanshin Construction is a bounded RiskWatch row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L82-C30-001470-SAMBU-SMALL-BUILDER-HIGHMAE-SHARECOUNT-STATUS", "trigger_id": "TRG_R10L82-C30-001470-SAMBU-SMALL-BUILDER-HIGHMAE-SHARECOUNT-STATUS", "symbol": "001470", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 22, "orderbook_recovery_score": 2, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 2, "sharecount_or_status_validation_risk": 12, "execution_risk_score": 25, "information_confidence": 2}, "weighted_score_before": 26, "stage_label_before": "Stage4B-local-watch / no price-only hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 24, "orderbook_recovery_score": 2, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_group_buffer_score": 1, "sharecount_or_status_validation_risk": 14, "execution_risk_score": 27, "information_confidence": 2}, "weighted_score_after": 22, "stage_label_after": "Stage4B-local-watch / no hard 4C without non-price break", "changed_components": ["pf_liquidity_risk", "orderbook_recovery_score", "refinancing_break_score", "default_or_control_break_score", "capital_or_group_buffer_score", "sharecount_or_status_validation_risk", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; protect bounded rows from forced 4B; block hard 4C without explicit non-price balance-sheet break.", "MFE_90D_pct": 43.97, "MAE_90D_pct": -24.12, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should escalate small-builder/PF risk to local 4B when the price path shows severe MAE and persistent drawdown, but hard 4C still requires non-price refinancing failure, default, impairment, covenant, auditor/control or solvency evidence. Sambu also requires share-count and status continuity validation."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 82, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_HOUSING_RECOVERY_SHARECOUNT_VS_SMALL_BUILDER_HIGH_MAE_AND_BOUNDED_NO_FORCED4B", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "risk_positive_case_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "extended_status_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C30 construction/PF symbols outside top-covered 006360/UNKNOWN/294870/047040/000720/375500 set and outside loop-81 HL D&I/Jinheung/Daewoo names, +3 IS Dongseo/Hanshin/Sambu severity families, +1 recovery candidate with validation, +1 bounded no-forced-4B boundary, +1 high-MAE local-4B risk path, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_sharecount_status_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 82, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "mid_builder_housing_recovery_sharecount_vs_small_builder_high_MAE_and_bounded_no_forced4B", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split mid-builder housing/orderbook recovery candidates from high-MAE small-builder PF local 4B and bounded no-forced-4B rows. Recovery requires orderbook, PF exposure, refinancing, liquidity and margin proof. High MAE can trigger local 4B-watch, but full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence. Share-count and status flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["010780", "004960", "001470"], "share_count_validation_required": ["010780", "001470"], "extended_status_validation_required": ["001470"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 82, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "recovery_no_hard4c_guard", "bounded_MAE_no_forced_4B_guard", "PF_orderbook_refinancing_bridge_required", "share_count_validation_guard", "status_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 severity split is strengthened. IS Dongseo shows a validated-before-promotion housing recovery candidate; Hanshin Construction is a bounded no-forced-4B row; Sambu Construction shows a severe high-MAE local-4B path where price alone still cannot create hard 4C."}
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
010780:
  name = 아이에스동서 from 2008-08-08, 동서산업 before that
  corporate_action_candidate_dates = 1997-01-03, 1999-08-10, 2002-03-18, 2002-05-20, 2004-06-15, 2005-06-17, 2005-09-15, 2005-10-10, 2008-08-08, 2011-07-29
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

004960:
  name = 한신공영
  corporate_action_candidate_dates = 1998-09-19, 2001-06-20, 2002-04-03, 2002-05-24, 2002-11-14
  selected window = 2024-02-01~D+180
  contamination = false

001470:
  name = 삼부토건
  corporate_action_candidate_dates = 1996-01-03, 2016-05-13, 2016-12-23, 2017-10-31, 2018-09-18, 2019-05-02
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
  extended_status_validation_required = true
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
010780 and 001470 require share-count validation before runtime promotion.
001470 also requires extended status validation before longer-horizon ingestion.
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
This R10/C30 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair, 010780/001470 need share-count validation, and 001470 needs extended status validation.

Candidate axis:
mid_builder_housing_recovery_sharecount_vs_small_builder_high_MAE_and_bounded_no_forced4B

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 010780, 004960 and 001470.
4. Validate 010780 and 001470 share-count changes inside the selected window.
5. Validate 001470 status continuity before longer-horizon ingestion.
6. Keep hard 4C evidence-based:
   - default,
   - court rehabilitation,
   - refinancing failure,
   - auditor/control break,
   - impairment, covenant or solvency break.
7. Use local 4B-watch when:
   - PF/liquidity/orderbook/financing risk is present,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - or post-peak drawdown <= -35%,
   - but hard-break evidence is not confirmed.
8. Keep RiskWatch/no-hard-4C/no-forced-4B when:
   - bounded MAE exists,
   - orderbook/capital/group/support buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
9. Allow recovery Stage2-Yellow only after:
   - orderbook quality,
   - housing project mix,
   - PF exposure,
   - refinancing access,
   - liquidity,
   - margin bridge are source-repaired.
10. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 82
next_round = R11
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

