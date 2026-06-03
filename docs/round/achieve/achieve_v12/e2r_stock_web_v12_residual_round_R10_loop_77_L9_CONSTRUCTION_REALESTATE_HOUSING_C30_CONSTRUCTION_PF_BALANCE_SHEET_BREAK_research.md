# E2R Stock-Web v12 Residual Research — R10 Loop 77 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 77,
  "computed_next_round": "R11",
  "computed_next_loop": 77,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "PF_financing_support_boundary_guardrail",
    "largecap_builder_buffer_no_hard4c",
    "small_builder_financing_high_MAE_local4b",
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

Previous completed state in this interactive run: R9 / loop 77.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 77
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 77
```

R10 is the construction/PF balance-sheet-break round.  
This file avoids the top-covered C30 names and avoids the loop-76 R10 names.

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
002410 / 범양건영 / small-builder high-MAE local 4B
047040 / 대우건설 / large-cap PF RiskWatch no-hard-4C boundary
003070 / 코오롱글로벌 / PF recovery-spike no-hard-4C boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C30 is not “건설주가 빠졌다.”

The severity ladder is:

```text
PF / financing / orderbook fear
→ RiskWatch

PF / financing fear + high MAE or post-peak drawdown
→ local 4B-watch

default / refinancing failure / impairment / covenant / solvency break
→ full 4B or hard 4C
```

건설주 하락은 먼지다.  
C30은 그 먼지가 단순 공사장 흙먼지인지, 기둥이 꺾이는 소리인지 구분해야 한다.

---

## Case 1 — Local 4B risk: 002410 / 범양건영

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, financing access, orderbook, liquidity, covenant, impairment and solvency evidence.

```text
evidence_family = SMALL_BUILDER_PF_FINANCING_ORDERBOOK_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK
case_role = risk_positive_local4b_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,767
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv`:

```text
2024-02-01,1767,1784,1750,1767
2024-02-02,1780,1803,1767,1787
2024-03-05,1701,1709,1667,1667
2024-04-08,1399,1432,1367,1421
2024-08-05,1323,1347,1198,1198
2024-10-24,1062,1070,1000,1022
2024-10-25,1016,1025,1000,1010
```

### Backtest

```text
MFE_30D  = +2.04%
MAE_30D  = -5.66%
MFE_90D  = +2.04%
MAE_90D  = -22.64%
MFE_180D = +2.04%
MAE_180D = -43.41%
peak_180 = 1,803 on 2024-02-02
trough_180 = 1,000 on 2024-10-24~2024-10-25
peak_to_later_drawdown = -44.54%
```

### Interpretation

This is a local 4B risk row.  
The price did not validate a recovery; it leaked lower into a high-MAE path.

Correct treatment:

```text
small builder / financing risk
→ local 4B-watch
→ no hard 4C without non-price default/refinancing/solvency break
```

---

## Case 2 — Large-cap RiskWatch / no hard 4C: 047040 / 대우건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, orderbook, capital buffer, refinancing access, liquidity and solvency evidence.

```text
evidence_family = LARGECAP_BUILDER_PF_FEAR_WITH_BOUNDED_MAE_ORDERBOOK_CAPITAL_BUFFER_NO_SOLVENCY_BREAK
case_role = overbearish_counterexample_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,910
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv`:

```text
2024-02-01,3910,4005,3905,3965
2024-02-19,4055,4120,4030,4055
2024-08-05,3915,3945,3545,3640
2024-08-26,4285,4320,4220,4260
2024-10-02,3800,3825,3745,3765
2024-10-25,3630,3645,3585,3620
```

### Backtest

```text
MFE_30D  = +5.37%
MAE_30D  = -0.13%
MFE_90D  = +5.37%
MAE_90D  = -6.01%
MFE_180D = +10.49%
MAE_180D = -9.34%
peak_180 = 4,320 on 2024-08-26
trough_180 = 3,545 on 2024-08-05
peak_to_later_drawdown = -12.85%
```

### Interpretation

This is not a hard 4C row.  
PF/orderbook watch remains appropriate, but bounded MAE blocks a price-only balance-sheet-break label.

Correct treatment:

```text
RiskWatch
no hard 4C without non-price refinancing, impairment, covenant or solvency break
```

---

## Case 3 — Recovery-spike / no hard 4C: 003070 / 코오롱글로벌

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF/orderbook exposure, liquidity, refinancing, capital buffer and solvency evidence.

```text
evidence_family = BUILDER_PF_ORDERBOOK_FEAR_WITH_RECOVERY_SPIKE_AND_NO_CONFIRMED_SOLVENCY_BREAK
case_role = overbearish_counterexample_recovery_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 9,370
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv`:

```text
2024-02-01,9370,9760,9370,9750
2024-02-19,10110,10240,10090,10120
2024-04-12,8770,8940,8480,8600
2024-08-05,9610,9620,8500,8800
2024-08-27,11400,12890,11340,11530
2024-10-25,8930,9130,8660,8980
```

### Backtest

```text
MFE_30D  = +9.28%
MAE_30D  = -3.95%
MFE_90D  = +9.28%
MAE_90D  = -9.50%
MFE_180D = +37.57%
MAE_180D = -9.50%
peak_180 = 12,890 on 2024-08-27
trough_180 = 8,480 on 2024-04-12
peak_to_later_drawdown = -32.82%
```

### Interpretation

This is a PF RiskWatch row, not a hard 4C row.  
A recovery spike and bounded entry-basis MAE mean the model should not overbearishly label it as a confirmed balance-sheet break.

Correct treatment:

```text
PF/orderbook watch
bounded MAE + recovery spike
→ no hard 4C without non-price break
```

---

## Cross-case residual finding

### What this strengthens

```text
hard_4c_confirmation = strengthen
local_4b_watch_guard = strengthen
overbearish_no_hard4c_guard = strengthen
corporate_action_validation_guard = keep
```

### What this does not justify

```text
do_not_treat_all_construction_drawdowns_as_hard_4C = true
do_not_use_price_only_MAE_as_default_or_refinancing_failure = true
do_not_ignore_high_MAE_local4B_risk = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C
```

This fine archetype covers:

```text
1. small builder / financing fear + high MAE → local 4B-watch
2. large-cap builder PF fear + bounded MAE → RiskWatch / no hard 4C
3. builder recovery spike + no confirmed solvency break → RiskWatch / no hard 4C
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B", "symbol": "002410", "company_name": "범양건영", "round": "R10", "loop": "77", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SmallBuilderFinancingHighMAE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should flag local 4B when a small-builder/PF-financing row opens severe MAE and persistent drawdown, but hard 4C still requires non-price default, refinancing failure, court rehabilitation, impairment, covenant or solvency evidence. Beomyang Construction produced minimal MFE and then a deep drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "77", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-LargeCapBuilderPFBufferNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should keep PF/orderbook RiskWatch active for large builders, but bounded MAE and recovery/sideways price action should not become hard 4C without refinancing, impairment, covenant, auditor/control or solvency break evidence. Daewoo E&C is a no-hard-4C boundary row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C", "symbol": "003070", "company_name": "코오롱글로벌", "round": "R10", "loop": "77", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BuilderPFRecoveryNoHard4CWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not over-convert builder/PF fear into hard 4C when price produces a recovery spike and MAE remains bounded. Kolon Global still needs PF/orderbook/liquidity monitoring, but the price path is a RiskWatch/no-hard-4C boundary unless non-price refinancing or solvency evidence breaks.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B", "case_id": "R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B", "symbol": "002410", "company_name": "범양건영", "round": "R10", "loop": "77", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-SmallBuilderFinancingHighMAE", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1767.0, "evidence_available_at_that_date": "SMALL_BUILDER_PF_FINANCING_ORDERBOOK_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK", "evidence_source": "source_proxy_manual_verification_required:BEOMYANG_CONSTRUCTION_2024_SMALL_BUILDER_PF_FINANCING_ORDERBOOK_LIQUIDITY_SOLVENCY_BRIDGE", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv", "profile_path": "atlas/symbol_profiles/002/002410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.04, "MFE_90D_pct": 2.04, "MFE_180D_pct": 2.04, "MAE_30D_pct": -5.66, "MAE_90D_pct": -22.64, "MAE_180D_pct": -43.41, "peak_date": "2024-02-02", "peak_price": 1803.0, "drawdown_after_peak_pct": -44.54, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_no_hard4c", "current_profile_verdict": "C30 should flag local 4B when a small-builder/PF-financing row opens severe MAE and persistent drawdown, but hard 4C still requires non-price default, refinancing failure, court rehabilitation, impairment, covenant or solvency evidence. Beomyang Construction produced minimal MFE and then a deep drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_002410_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C", "case_id": "R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "77", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-LargeCapBuilderPFBufferNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3910.0, "evidence_available_at_that_date": "LARGECAP_BUILDER_PF_FEAR_WITH_BOUNDED_MAE_ORDERBOOK_CAPITAL_BUFFER_NO_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:DAEWOO_E&C_2024_LARGECAP_BUILDER_PF_ORDERBOOK_CAPITAL_BUFFER_NO_HARD4C", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.37, "MFE_90D_pct": 5.37, "MFE_180D_pct": 10.49, "MAE_30D_pct": -0.13, "MAE_90D_pct": -6.01, "MAE_180D_pct": -9.34, "peak_date": "2024-08-26", "peak_price": 4320.0, "drawdown_after_peak_pct": -12.85, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "current_profile_verdict": "C30 should keep PF/orderbook RiskWatch active for large builders, but bounded MAE and recovery/sideways price action should not become hard 4C without refinancing, impairment, covenant, auditor/control or solvency break evidence. Daewoo E&C is a no-hard-4C boundary row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_047040_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C", "case_id": "R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C", "symbol": "003070", "company_name": "코오롱글로벌", "round": "R10", "loop": "77", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-BuilderPFRecoveryNoHard4CWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 9370.0, "evidence_available_at_that_date": "BUILDER_PF_ORDERBOOK_FEAR_WITH_RECOVERY_SPIKE_AND_NO_CONFIRMED_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:KOLON_GLOBAL_2024_BUILDER_PF_ORDERBOOK_LIQUIDITY_BUFFER_NO_HARD4C", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv", "profile_path": "atlas/symbol_profiles/003/003070.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.28, "MFE_90D_pct": 9.28, "MFE_180D_pct": 37.57, "MAE_30D_pct": -3.95, "MAE_90D_pct": -9.5, "MAE_180D_pct": -9.5, "peak_date": "2024-08-27", "peak_price": 12890.0, "drawdown_after_peak_pct": -32.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_recovery_no_hard4c", "current_profile_verdict": "C30 should not over-convert builder/PF fear into hard 4C when price produces a recovery spike and MAE remains bounded. Kolon Global still needs PF/orderbook/liquidity monitoring, but the price path is a RiskWatch/no-hard-4C boundary unless non-price refinancing or solvency evidence breaks.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_003070_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B", "trigger_id": "TRG_R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B", "symbol": "002410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 16, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 3, "relative_strength_score": 2, "execution_risk_score": 19, "information_confidence": 2}, "weighted_score_before": 32, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 18, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 2, "relative_strength_score": 1, "execution_risk_score": 22, "information_confidence": 2}, "weighted_score_after": 28, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/financing risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 2.04, "MAE_90D_pct": -22.64, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should flag local 4B when a small-builder/PF-financing row opens severe MAE and persistent drawdown, but hard 4C still requires non-price default, refinancing failure, court rehabilitation, impairment, covenant or solvency evidence. Beomyang Construction produced minimal MFE and then a deep drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C", "trigger_id": "TRG_R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C", "symbol": "047040", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 7, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 13, "relative_strength_score": 7, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 6, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "relative_strength_score": 7, "execution_risk_score": 6, "information_confidence": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/financing risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 5.37, "MAE_90D_pct": -6.01, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should keep PF/orderbook RiskWatch active for large builders, but bounded MAE and recovery/sideways price action should not become hard 4C without refinancing, impairment, covenant, auditor/control or solvency break evidence. Daewoo E&C is a no-hard-4C boundary row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C", "trigger_id": "TRG_R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C", "symbol": "003070", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 7, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 13, "relative_strength_score": 7, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 6, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "relative_strength_score": 7, "execution_risk_score": 6, "information_confidence": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/financing risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 9.28, "MAE_90D_pct": -9.5, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should not over-convert builder/PF fear into hard 4C when price produces a recovery spike and MAE remains bounded. Kolon Global still needs PF/orderbook/liquidity monitoring, but the price path is a RiskWatch/no-hard-4C boundary unless non-price refinancing or solvency evidence breaks."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 77, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 1, "overbearish_counterexample_count": 2, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "post_corporate_action_validation_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C30 builders outside top-covered PF set and outside loop-76 R10 names, +3 small-builder/largecap-buffer/recovery-spike trigger families, +1 high-MAE local-4B risk path, +2 no-hard-4C buffer boundaries, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 77, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "small_builder_high_MAE_local4B_vs_largecap_buffered_no_hard4C", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split small-builder high-MAE local 4B from large-cap/buffered RiskWatch no-hard-4C boundaries. MAE deterioration and post-peak drawdown can trigger local 4B-watch, but full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["002410", "047040", "003070"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 77, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "overbearish_no_hard4c_guard", "corporate_action_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 severity split is strengthened. Beomyang Construction shows a small-builder high-MAE local 4B path; Daewoo E&C and Kolon Global show RiskWatch/no-hard-4C boundaries where PF fear needs monitoring but price action alone is not balance-sheet break evidence."}
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
002410:
  corporate_action_candidate_dates = 1996-01-03, 2009-12-21, 2014-07-07, 2015-07-09, 2015-12-30, 2017-12-06
  selected window = 2024-02-01~D+180
  contamination = false

047040:
  corporate_action_candidate_dates = 2001-07-13, 2003-11-18, 2011-01-18
  selected window = 2024-02-01~D+180
  contamination = false

003070:
  corporate_action_candidate_dates = 1997-01-03, 1999-10-22, 2004-12-30, 2010-11-23, 2012-01-11, 2014-05-23, 2017-08-01, 2023-01-31, 2025-12-11
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C30 severity-splitting discovery,
but coding-agent promotion requires non-proxy PF/refinancing/orderbook/liquidity/margin/covenant/solvency evidence.
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
small_builder_high_MAE_local4B_vs_largecap_buffered_no_hard4C

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 002410, 047040 and 003070.
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
6. Keep RiskWatch/no-hard-4C when:
   - recovery or bounded MAE exists,
   - orderbook/capital/group/support buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
7. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 77
next_round = R11
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

