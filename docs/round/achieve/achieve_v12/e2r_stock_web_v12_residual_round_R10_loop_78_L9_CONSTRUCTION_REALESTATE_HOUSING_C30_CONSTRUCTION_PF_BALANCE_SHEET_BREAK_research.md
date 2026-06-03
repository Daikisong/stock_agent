# E2R Stock-Web v12 Residual Research — R10 Loop 78 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 78,
  "computed_next_round": "R11",
  "computed_next_loop": 78,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "PF_refinancing_liquidity_orderbook_boundary_guardrail",
    "small_builder_high_MAE_local4B",
    "mid_builder_bounded_RiskWatch_no_hard4C",
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

Previous completed state in this interactive run: R9 / loop 78.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 78
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 78
```

R10 is the construction/PF balance-sheet-break round.  
This file avoids the top-covered C30 names and avoids the loop-77 R10 names.

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
002990 / 금호건설 / small-mid builder high-MAE local 4B
004960 / 한신공영 / bounded PF RiskWatch no-hard-4C
010780 / 아이에스동서 / recovery-spike PF no-hard-4C with share-count validation
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
010780 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C30 is not “건설주가 빠졌다.”

The severity ladder remains:

```text
PF / refinancing / orderbook fear
→ RiskWatch

PF / refinancing fear + high MAE or post-peak drawdown
→ local 4B-watch

default / refinancing failure / impairment / covenant / solvency break
→ full 4B or hard 4C
```

건설주 하락은 균열처럼 보인다.  
C30은 그 균열이 표면 페인트인지, 구조 기둥이 꺾이는 소리인지 구분해야 한다.

---

## Case 1 — Local 4B risk: 002990 / 금호건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, refinancing access, orderbook, liquidity, covenant, impairment and solvency evidence.

```text
evidence_family = SMALL_MID_BUILDER_PF_REFINANCING_ORDERBOOK_LIQUIDITY_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK
case_role = risk_positive_local4b_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,250
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv`:

```text
2024-02-01,5250,5280,5190,5200
2024-03-15,4710,4735,4615,4615
2024-06-13,3890,3890,3645,3710
2024-06-18,3720,4780,3710,3980
2024-08-05,3580,3595,3205,3205
2024-10-25,2920,2990,2850,2870
2024-11-01,2900,2905,2800,2830
```

### Backtest

```text
MFE_30D  = +0.57%
MAE_30D  = -12.10%
MFE_90D  = +0.57%
MAE_90D  = -30.57%
MFE_180D = +0.57%
MAE_180D = -46.67%
peak_180 = 5,280 on 2024-02-01
trough_180 = 2,800 on 2024-11-01
peak_to_later_drawdown = -46.97%
```

### Interpretation

This is a local 4B risk row.  
The price did not validate recovery and leaked into a high-MAE path.

Correct treatment:

```text
small/mid builder PF and refinancing risk
→ local 4B-watch
→ no hard 4C without non-price default/refinancing/solvency break
```

---

## Case 2 — Bounded RiskWatch / no hard 4C: 004960 / 한신공영

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF/orderbook exposure, liquidity, refinancing, capital buffer and solvency evidence.

```text
evidence_family = MID_BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK
case_role = overbearish_counterexample_bounded_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,370
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv`:

```text
2024-02-01,7370,7770,7370,7720
2024-02-02,7810,7810,7500,7630
2024-04-12,6490,6500,6310,6320
2024-07-30,7190,7560,6890,7340
2024-08-05,6970,6970,6160,6300
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

This is not a hard 4C row.  
PF/orderbook watch remains appropriate, but bounded MAE blocks a price-only balance-sheet-break label.

Correct treatment:

```text
RiskWatch
bounded MAE
→ no hard 4C without non-price refinancing, impairment, covenant or solvency break
```

---

## Case 3 — Recovery-spike / no hard 4C: 010780 / 아이에스동서

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is developer/PF exposure, liquidity, orderbook, refinancing access, balance-sheet buffer and solvency evidence.

```text
evidence_family = BUILDER_DEVELOPER_PF_FEAR_WITH_RECOVERY_SPIKE_AND_NO_CONFIRMED_SOLVENCY_BREAK
case_role = overbearish_counterexample_recovery_spike_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 25,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv`:

```text
2024-02-01,25400,26050,25100,25750
2024-03-08,28000,30300,27750,30100
2024-03-22,29100,31200,29050,30450
2024-04-12,25050,25350,24650,24950
2024-08-05,23500,23700,20350,20600
2024-10-31,20150,20700,19800,20200
```

### Backtest

```text
MFE_30D  = +19.29%
MAE_30D  = -1.18%
MFE_90D  = +22.83%
MAE_90D  = -3.35%
MFE_180D = +22.83%
MAE_180D = -22.05%
peak_180 = 31,200 on 2024-03-22
trough_180 = 19,800 on 2024-10-31
peak_to_later_drawdown = -36.54%
```

### Interpretation

This is PF RiskWatch, not hard 4C.  
The recovery spike and bounded early MAE mean price action alone is insufficient to call a confirmed balance-sheet break.

Correct treatment:

```text
PF/developer watch
share-count validation first
recovery spike + no confirmed solvency break
→ RiskWatch / no hard 4C
```

---

## Cross-case residual finding

### What this strengthens

```text
hard_4c_confirmation = strengthen
local_4b_watch_guard = strengthen
overbearish_no_hard4c_guard = strengthen
share_count_validation_guard = strengthen
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
SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C
```

This fine archetype covers:

```text
1. small/mid builder PF fear + high MAE → local 4B-watch
2. mid-builder PF fear + bounded MAE → RiskWatch / no hard 4C
3. developer recovery spike + no confirmed solvency break → RiskWatch / no hard 4C
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L78-C30-002990-KUMHO-E&C-SMALLBUILDER-HIGH-MAE-LOCAL4B", "symbol": "002990", "company_name": "금호건설", "round": "R10", "loop": "78", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SmallMidBuilderPFHighMAE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should flag local 4B when construction/PF fear aligns with persistent MAE and drawdown, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Kumho E&C produced almost no MFE and then a deep drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L78-C30-004960-HANSHIN-E&C-PF-RISKWATCH-BOUNDED-NO-HARD4C", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "78", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-MidBuilderPFBoundedMAENoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should keep PF/orderbook watch active for mid-builders, but bounded MAE and a non-collapsing price path should not become hard 4C without explicit refinancing, impairment, covenant, auditor/control or solvency break evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L78-C30-010780-ISDONGSEO-PF-RECOVERY-SPIKE-NO-HARD4C", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": "78", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-RecoverySpikePFNoHard4CWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not over-convert builder/developer PF fear into hard 4C when the path produces recovery MFE and entry-basis MAE remains bounded. IS Dongseo needs PF/liquidity/orderbook monitoring, but price alone is not confirmed balance-sheet break evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L78-C30-002990-KUMHO-E&C-SMALLBUILDER-HIGH-MAE-LOCAL4B", "case_id": "R10L78-C30-002990-KUMHO-E&C-SMALLBUILDER-HIGH-MAE-LOCAL4B", "symbol": "002990", "company_name": "금호건설", "round": "R10", "loop": "78", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-SmallMidBuilderPFHighMAE", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5250.0, "evidence_available_at_that_date": "SMALL_MID_BUILDER_PF_REFINANCING_ORDERBOOK_LIQUIDITY_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK", "evidence_source": "source_proxy_manual_verification_required:KUMHO_E&C_2024_PF_REFINANCING_ORDERBOOK_LIQUIDITY_SOLVENCY_BRIDGE", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv", "profile_path": "atlas/symbol_profiles/002/002990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.57, "MFE_90D_pct": 0.57, "MFE_180D_pct": 0.57, "MAE_30D_pct": -12.1, "MAE_90D_pct": -30.57, "MAE_180D_pct": -46.67, "peak_date": "2024-02-01", "peak_price": 5280.0, "drawdown_after_peak_pct": -46.97, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_no_hard4c", "current_profile_verdict": "C30 should flag local 4B when construction/PF fear aligns with persistent MAE and drawdown, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Kumho E&C produced almost no MFE and then a deep drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_002990_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L78-C30-004960-HANSHIN-E&C-PF-RISKWATCH-BOUNDED-NO-HARD4C", "case_id": "R10L78-C30-004960-HANSHIN-E&C-PF-RISKWATCH-BOUNDED-NO-HARD4C", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "78", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-MidBuilderPFBoundedMAENoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7370.0, "evidence_available_at_that_date": "MID_BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:HANSHIN_E&C_2024_PF_ORDERBOOK_LIQUIDITY_BUFFER_NO_HARD4C", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv", "profile_path": "atlas/symbol_profiles/004/004960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.97, "MFE_90D_pct": 5.97, "MFE_180D_pct": 5.97, "MAE_30D_pct": -5.16, "MAE_90D_pct": -15.33, "MAE_180D_pct": -16.42, "peak_date": "2024-02-02", "peak_price": 7810.0, "drawdown_after_peak_pct": -21.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_bounded_no_hard4c", "current_profile_verdict": "C30 should keep PF/orderbook watch active for mid-builders, but bounded MAE and a non-collapsing price path should not become hard 4C without explicit refinancing, impairment, covenant, auditor/control or solvency break evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_004960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L78-C30-010780-ISDONGSEO-PF-RECOVERY-SPIKE-NO-HARD4C", "case_id": "R10L78-C30-010780-ISDONGSEO-PF-RECOVERY-SPIKE-NO-HARD4C", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": "78", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-RecoverySpikePFNoHard4CWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 25400.0, "evidence_available_at_that_date": "BUILDER_DEVELOPER_PF_FEAR_WITH_RECOVERY_SPIKE_AND_NO_CONFIRMED_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:IS_DONGSEO_2024_BUILDER_DEVELOPER_PF_LIQUIDITY_ORDERBOOK_BUFFER_NO_HARD4C", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv", "profile_path": "atlas/symbol_profiles/010/010780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.29, "MFE_90D_pct": 22.83, "MFE_180D_pct": 22.83, "MAE_30D_pct": -1.18, "MAE_90D_pct": -3.35, "MAE_180D_pct": -22.05, "peak_date": "2024-03-22", "peak_price": 31200.0, "drawdown_after_peak_pct": -36.54, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_recovery_spike_no_hard4c", "current_profile_verdict": "C30 should not over-convert builder/developer PF fear into hard 4C when the path produces recovery MFE and entry-basis MAE remains bounded. IS Dongseo needs PF/liquidity/orderbook monitoring, but price alone is not confirmed balance-sheet break evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C30_PF_BOUNDARY_010780_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L78-C30-002990-KUMHO-E&C-SMALLBUILDER-HIGH-MAE-LOCAL4B", "trigger_id": "TRG_R10L78-C30-002990-KUMHO-E&C-SMALLBUILDER-HIGH-MAE-LOCAL4B", "symbol": "002990", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 17, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 2, "relative_strength_score": 1, "execution_risk_score": 21, "share_count_validation_risk": 0, "information_confidence": 2}, "weighted_score_before": 30, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 19, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 1, "relative_strength_score": 1, "execution_risk_score": 23, "share_count_validation_risk": 0, "information_confidence": 2}, "weighted_score_after": 27, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 0.57, "MAE_90D_pct": -30.57, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should flag local 4B when construction/PF fear aligns with persistent MAE and drawdown, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Kumho E&C produced almost no MFE and then a deep drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L78-C30-004960-HANSHIN-E&C-PF-RISKWATCH-BOUNDED-NO-HARD4C", "trigger_id": "TRG_R10L78-C30-004960-HANSHIN-E&C-PF-RISKWATCH-BOUNDED-NO-HARD4C", "symbol": "004960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 7, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 12, "relative_strength_score": 8, "execution_risk_score": 8, "share_count_validation_risk": 0, "information_confidence": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 6, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "relative_strength_score": 8, "execution_risk_score": 7, "share_count_validation_risk": 0, "information_confidence": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 5.97, "MAE_90D_pct": -15.33, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should keep PF/orderbook watch active for mid-builders, but bounded MAE and a non-collapsing price path should not become hard 4C without explicit refinancing, impairment, covenant, auditor/control or solvency break evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L78-C30-010780-ISDONGSEO-PF-RECOVERY-SPIKE-NO-HARD4C", "trigger_id": "TRG_R10L78-C30-010780-ISDONGSEO-PF-RECOVERY-SPIKE-NO-HARD4C", "symbol": "010780", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 7, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 12, "relative_strength_score": 8, "execution_risk_score": 8, "share_count_validation_risk": 8, "information_confidence": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 6, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "relative_strength_score": 8, "execution_risk_score": 7, "share_count_validation_risk": 10, "information_confidence": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 22.83, "MAE_90D_pct": -3.35, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should not over-convert builder/developer PF fear into hard 4C when the path produces recovery MFE and entry-basis MAE remains bounded. IS Dongseo needs PF/liquidity/orderbook monitoring, but price alone is not confirmed balance-sheet break evidence."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 78, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_HIGH_MAE_LOCAL4B_VS_BOUNDED_RISKWATCH_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 1, "overbearish_counterexample_count": 2, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "post_corporate_action_validation_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C30 construction/PF symbols outside top-covered 006360/294870/375500/000720 set and outside loop-77 R10 names, +3 small-mid builder/bounded risk/recovery-spike trigger families, +1 high-MAE local-4B risk path, +2 no-hard-4C boundaries, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 78, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "small_mid_builder_high_MAE_local4B_vs_bounded_RiskWatch_no_hard4C", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split high-MAE small/mid builder local 4B from bounded/recovery RiskWatch no-hard-4C boundaries. MAE deterioration and post-peak drawdown can trigger local 4B-watch, but full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["002990", "004960", "010780"], "share_count_validation_required": ["010780"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 78, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "overbearish_no_hard4c_guard", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 severity split is strengthened. Kumho E&C shows a high-MAE small/mid-builder local 4B path; Hanshin E&C and IS Dongseo show RiskWatch/no-hard-4C boundaries where PF fear needs monitoring but price action alone is not confirmed balance-sheet break evidence."}
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
002990:
  name = 금호건설 from 2021-04-13, 금호산업 before that
  corporate_action_candidate_dates = 1999-03-22, 2000-01-11, 2010-04-29, 2010-11-24, 2012-03-22, 2013-03-28, 2013-11-07
  selected window = 2024-02-01~D+180
  contamination = false

004960:
  name = 한신공영
  corporate_action_candidate_dates = 1998-09-19, 2001-06-20, 2002-04-03, 2002-05-24, 2002-11-14
  selected window = 2024-02-01~D+180
  contamination = false

010780:
  name = 아이에스동서 from 2008-08-08, 동서산업 before that
  corporate_action_candidate_dates = 1997-01-03, 1999-08-10, 2002-03-18, 2002-05-20, 2004-06-15, 2005-06-17, 2005-09-15, 2005-10-10, 2008-08-08, 2011-07-29
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
010780 also requires share-count validation before runtime promotion.
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
This R10/C30 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 010780 needs share-count validation.

Candidate axis:
small_mid_builder_high_MAE_local4B_vs_bounded_RiskWatch_no_hard4C

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 002990, 004960 and 010780.
4. Validate 010780 share-count changes inside the selected window.
5. Keep hard 4C evidence-based:
   - default,
   - court rehabilitation,
   - refinancing failure,
   - auditor/control break,
   - impairment, covenant or solvency break.
6. Use local 4B-watch when:
   - PF/liquidity/orderbook/financing risk is present,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - or post-peak drawdown <= -35%,
   - but hard-break evidence is not confirmed.
7. Keep RiskWatch/no-hard-4C when:
   - recovery or bounded MAE exists,
   - orderbook/capital/group/support buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
8. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 78
next_round = R11
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

