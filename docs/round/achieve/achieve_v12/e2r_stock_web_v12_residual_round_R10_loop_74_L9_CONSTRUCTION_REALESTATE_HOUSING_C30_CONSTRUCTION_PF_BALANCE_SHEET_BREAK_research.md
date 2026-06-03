# E2R Stock-Web v12 Residual Research — R10 Loop 74 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 74,
  "computed_next_round": "R11",
  "computed_next_loop": 74,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
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
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R9 / loop 74.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 74
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 74
```

R10 is the construction/PF balance-sheet break round.  
This file avoids the top-covered C30 set and the prior R10 loop-73 names.

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
002990 / 금호건설 / mid-builder PF/orderbook/liquidity local 4B
021320 / KCC건설 / buffered regional-builder RiskWatch / no hard 4C
002410 / 범양건영 / severe small-builder PF/liquidity local 4B
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a 2024 corporate-action candidate inside the selected window by profile.
```

## Research thesis

C30 is not “construction stock fell.”

The mechanism needs severity splitting:

```text
PF / orderbook / liquidity fear
→ local 4B-watch when MFE is weak and MAE opens
→ RiskWatch/no-hard-4C when buffer or non-break evidence exists
→ hard 4C only after non-price break evidence
```

A balance sheet is a bridge.  
Local 4B is the warning sign when the lane starts cracking.  
Hard 4C is the bridge closed by an engineer, not just a scary price candle.

---

## Case 1 — Local 4B risk: 002990 / 금호건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, orderbook quality, refinancing access, margin pressure, liquidity and covenant/solvency evidence.

```text
evidence_family = MID_BUILDER_PF_EXPOSURE_ORDERBOOK_MARGIN_LIQUIDITY_RISK
case_role = risk_positive_local4b_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,250
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv`:

```text
2024-02-01,5250,5280,5190,5200
2024-03-19,4550,4560,4380,4390
2024-06-13,3890,3890,3645,3710
2024-08-05,3580,3595,3205,3205
2024-10-25,2920,2990,2850,2870
```

### Backtest

```text
MFE_30D  = +0.57%
MAE_30D  = -12.10%
MFE_90D  = +0.57%
MAE_90D  = -30.57%
MFE_180D = +0.57%
MAE_180D = -45.71%
peak_180 = 5,280 on 2024-02-01
trough_180 = 2,850 on 2024-10-25
peak_to_later_drawdown = -46.02%
```

### Interpretation

This is a clear local 4B-watch row.  
The MFE was almost nonexistent and MAE opened quickly. But the price path alone should still not become hard 4C. The model needs non-price refinancing, impairment, default, covenant or solvency evidence before hard 4C.

---

## Case 2 — RiskWatch / no hard 4C: 021320 / KCC건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, orderbook buffer, group/capital buffer and refinancing evidence.

```text
evidence_family = REGIONAL_BUILDER_PF_FEAR_WITH_ORDERBOOK_OR_GROUP_BUFFER_NO_HARD_BREAK
case_role = overbearish_counterexample_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,850
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv`:

```text
2024-02-01,4850,4950,4785,4915
2024-02-02,5070,5070,4840,4970
2024-04-08,4515,5750,4465,4615
2024-08-05,4250,4470,4170,4180
2024-08-27,4850,4965,4755,4895
```

### Backtest

```text
MFE_30D  = +4.54%
MAE_30D  = -5.88%
MFE_90D  = +18.56%
MAE_90D  = -8.87%
MFE_180D = +18.56%
MAE_180D = -14.02%
peak_180 = 5,750 on 2024-04-08
trough_180 = 4,170 on 2024-08-05
peak_to_later_drawdown = -27.48%
```

### Interpretation

This is not a positive Green row.  
But it is also not full 4B or hard 4C.

KCC Construction sits in the middle: PF fear deserves RiskWatch, but the bounded MAE and recovery argue against overclassifying it as a confirmed balance-sheet break.

---

## Case 3 — Severe local 4B risk: 002410 / 범양건영

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is small-builder PF exposure, liquidity, refinancing, orderbook, margin and solvency evidence.

```text
evidence_family = SMALL_BUILDER_PF_LIQUIDITY_ORDERBOOK_MARGIN_RISK_WITH_SEVERE_PRICE_PATH
case_role = risk_positive_local4b_severe_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,767
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv`:

```text
2024-02-01,1767,1784,1750,1767
2024-02-02,1780,1803,1767,1787
2024-04-08,1399,1432,1367,1421
2024-08-05,1323,1347,1198,1198
2024-10-24,1062,1070,1000,1022
```

### Backtest

```text
MFE_30D  = +2.04%
MAE_30D  = -9.11%
MFE_90D  = +2.04%
MAE_90D  = -22.64%
MFE_180D = +2.04%
MAE_180D = -43.41%
peak_180 = 1,803 on 2024-02-02
trough_180 = 1,000 on 2024-10-24
peak_to_later_drawdown = -44.54%
```

### Interpretation

This is the severe local 4B version of C30.  
The price path says the model should not stay neutral. But hard 4C remains evidence-based: local 4B is a guardrail, not a bankruptcy verdict.

---

## Cross-case residual finding

### What this strengthens

```text
hard_4c_confirmation = strengthen
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
```

### What this does not justify

```text
do_not_treat_all_construction_pf_fear_as_hard_4C = true
do_not_use_price_collapse_alone_as_hard_4C = true
do_not_ignore_bounded_MAE_or_buffered_recovery_cases = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C
```

This fine archetype covers:

```text
1. mid-builder PF/orderbook/liquidity risk + weak MFE/high MAE → local 4B-watch
2. regional-builder PF fear + bounded MAE/recovery → RiskWatch / no hard 4C
3. small-builder severe MAE/drawdown → severe local 4B-watch, still no hard 4C without non-price break
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B", "symbol": "002990", "company_name": "금호건설", "round": "R10", "loop": "74", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-PFOrderbookLiquidityRisk", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 local 4B-watch should fire when mid-builder PF/orderbook/liquidity risk produces weak MFE and persistent MAE, but hard 4C still requires explicit non-price default, refinancing failure, court rehabilitation, auditor/control or solvency break.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, refinancing, orderbook, liquidity, margin and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C", "symbol": "021320", "company_name": "KCC건설", "round": "R10", "loop": "74", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "Stage2-RiskWatch / BufferedBuilderNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not convert every regional-builder PF fear into full 4B or hard 4C when the price path has moderate MAE, tradable MFE and no confirmed non-price break. KCC Construction is a RiskWatch/no-hard-4C boundary row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, refinancing, orderbook, liquidity, margin and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE", "symbol": "002410", "company_name": "범양건영", "round": "R10", "loop": "74", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SeverePFLiquidityRiskNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should catch severe small-builder PF/liquidity/local 4B risk when MAE and drawdown become large, but hard 4C still needs non-price proof. Bumyang Construction shows the price-path severity that should raise local 4B-watch, not a price-only hard 4C.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, refinancing, orderbook, liquidity, margin and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B", "case_id": "R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B", "symbol": "002990", "company_name": "금호건설", "round": "R10", "loop": "74", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-PFOrderbookLiquidityRisk", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5250.0, "evidence_available_at_that_date": "MID_BUILDER_PF_EXPOSURE_ORDERBOOK_MARGIN_LIQUIDITY_RISK", "evidence_source": "source_proxy_manual_verification_required:KUMHO_CONSTRUCTION_2024_PF_ORDERBOOK_MARGIN_LIQUIDITY_REFINANCING_RISK", "stage2_evidence_fields": ["pf_risk", "orderbook_watch", "capital_or_liquidity_buffer_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_widening", "PF_orderbook_or_liquidity_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv", "profile_path": "atlas/symbol_profiles/002/002990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.57, "MFE_90D_pct": 0.57, "MFE_180D_pct": 0.57, "MAE_30D_pct": -12.1, "MAE_90D_pct": -30.57, "MAE_180D_pct": -45.71, "peak_date": "2024-02-01", "peak_price": 5280.0, "drawdown_after_peak_pct": -46.02, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_or_impairment_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_no_hard4c", "current_profile_verdict": "C30 local 4B-watch should fire when mid-builder PF/orderbook/liquidity risk produces weak MFE and persistent MAE, but hard 4C still requires explicit non-price default, refinancing failure, court rehabilitation, auditor/control or solvency break.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BS_002990_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C", "case_id": "R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C", "symbol": "021320", "company_name": "KCC건설", "round": "R10", "loop": "74", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage2-RiskWatch / BufferedBuilderNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4850.0, "evidence_available_at_that_date": "REGIONAL_BUILDER_PF_FEAR_WITH_ORDERBOOK_OR_GROUP_BUFFER_NO_HARD_BREAK", "evidence_source": "source_proxy_manual_verification_required:KCC_CONSTRUCTION_2024_PF_ORDERBOOK_GROUP_BUFFER_NO_HARD_BREAK", "stage2_evidence_fields": ["pf_risk", "orderbook_watch", "capital_or_liquidity_buffer_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_widening", "PF_orderbook_or_liquidity_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv", "profile_path": "atlas/symbol_profiles/021/021320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.54, "MFE_90D_pct": 18.56, "MFE_180D_pct": 18.56, "MAE_30D_pct": -5.88, "MAE_90D_pct": -8.87, "MAE_180D_pct": -14.02, "peak_date": "2024-04-08", "peak_price": 5750.0, "drawdown_after_peak_pct": -27.48, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_or_impairment_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "current_profile_verdict": "C30 should not convert every regional-builder PF fear into full 4B or hard 4C when the price path has moderate MAE, tradable MFE and no confirmed non-price break. KCC Construction is a RiskWatch/no-hard-4C boundary row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BS_021320_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE", "case_id": "R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE", "symbol": "002410", "company_name": "범양건영", "round": "R10", "loop": "74", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-SeverePFLiquidityRiskNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1767.0, "evidence_available_at_that_date": "SMALL_BUILDER_PF_LIQUIDITY_ORDERBOOK_MARGIN_RISK_WITH_SEVERE_PRICE_PATH", "evidence_source": "source_proxy_manual_verification_required:BUMYANG_CONSTRUCTION_2024_PF_LIQUIDITY_ORDERBOOK_MARGIN_REFINANCING_RISK", "stage2_evidence_fields": ["pf_risk", "orderbook_watch", "capital_or_liquidity_buffer_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_widening", "PF_orderbook_or_liquidity_risk", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv", "profile_path": "atlas/symbol_profiles/002/002410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.04, "MFE_90D_pct": 2.04, "MFE_180D_pct": 2.04, "MAE_30D_pct": -9.11, "MAE_90D_pct": -22.64, "MAE_180D_pct": -43.41, "peak_date": "2024-02-02", "peak_price": 1803.0, "drawdown_after_peak_pct": -44.54, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_or_impairment_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_severe_no_hard4c", "current_profile_verdict": "C30 should catch severe small-builder PF/liquidity/local 4B risk when MAE and drawdown become large, but hard 4C still needs non-price proof. Bumyang Construction shows the price-path severity that should raise local 4B-watch, not a price-only hard 4C.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BS_002410_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B", "trigger_id": "TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B", "symbol": "002990", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 15, "refinancing_break_score": 3, "default_or_control_break_score": 0, "capital_buffer_score": 3, "orderbook_buffer_score": 4, "relative_strength_score": 2, "execution_risk_score": 15, "information_confidence": 2}, "weighted_score_before": 42, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 16, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_buffer_score": 2, "orderbook_buffer_score": 3, "relative_strength_score": 1, "execution_risk_score": 16, "information_confidence": 2}, "weighted_score_after": 38, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "capital_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when PF/orderbook/liquidity risk opens MAE; block hard 4C without explicit default, refinancing, impairment, auditor/control or solvency break.", "MFE_90D_pct": 0.57, "MAE_90D_pct": -30.57, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 local 4B-watch should fire when mid-builder PF/orderbook/liquidity risk produces weak MFE and persistent MAE, but hard 4C still requires explicit non-price default, refinancing failure, court rehabilitation, auditor/control or solvency break."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C", "trigger_id": "TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C", "symbol": "021320", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 8, "refinancing_break_score": 3, "default_or_control_break_score": 0, "capital_buffer_score": 10, "orderbook_buffer_score": 9, "relative_strength_score": 6, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 55, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 7, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_buffer_score": 12, "orderbook_buffer_score": 10, "relative_strength_score": 5, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 57, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when PF/orderbook/liquidity risk opens MAE; block hard 4C without explicit default, refinancing, impairment, auditor/control or solvency break.", "MFE_90D_pct": 18.56, "MAE_90D_pct": -8.87, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should not convert every regional-builder PF fear into full 4B or hard 4C when the price path has moderate MAE, tradable MFE and no confirmed non-price break. KCC Construction is a RiskWatch/no-hard-4C boundary row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE", "trigger_id": "TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE", "symbol": "002410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 15, "refinancing_break_score": 3, "default_or_control_break_score": 0, "capital_buffer_score": 3, "orderbook_buffer_score": 4, "relative_strength_score": 2, "execution_risk_score": 15, "information_confidence": 2}, "weighted_score_before": 42, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 16, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_buffer_score": 2, "orderbook_buffer_score": 3, "relative_strength_score": 1, "execution_risk_score": 16, "information_confidence": 2}, "weighted_score_after": 38, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "capital_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when PF/orderbook/liquidity risk opens MAE; block hard 4C without explicit default, refinancing, impairment, auditor/control or solvency break.", "MFE_90D_pct": 2.04, "MAE_90D_pct": -22.64, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should catch severe small-builder PF/liquidity/local 4B risk when MAE and drawdown become large, but hard 4C still needs non-price proof. Bumyang Construction shows the price-path severity that should raise local 4B-watch, not a price-only hard 4C."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 74, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 2, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C30 builders outside top-covered PF set, +3 PF/orderbook/liquidity trigger families, +2 local-4B risk paths, +1 no-hard-4C buffer boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 74, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "mid_small_builder_pf_orderbook_liquidity_local4b_vs_buffered_no_hard4c", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split local PF/orderbook/liquidity risk from hard balance-sheet break. Weak MFE, widening MAE and post-peak drawdown can trigger local 4B-watch. Full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["002990", "021320", "002410"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 74, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 needs severity splitting. Kumho Construction and Bumyang Construction show local PF/liquidity 4B risk; KCC Construction shows a buffered RiskWatch/no-hard-4C boundary. Hard 4C remains non-price evidence based."}
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
  corporate_action_candidate_dates = 1999-03-22, 2000-01-11, 2010-04-29, 2010-11-24, 2012-03-22, 2013-03-28, 2013-11-07
  selected window = 2024-02-01~D+180
  contamination = false

021320:
  corporate_action_candidate_dates = 2014-05-12, 2014-07-09
  selected window = 2024-02-01~D+180
  contamination = false

002410:
  corporate_action_candidate_dates = 1996-01-03, 2009-12-21, 2014-07-07, 2015-07-09, 2015-12-30, 2017-12-06
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C30 rule-shape discovery,
but coding-agent promotion requires non-proxy PF/refinancing/orderbook/liquidity/margin/solvency evidence.
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
mid_small_builder_pf_orderbook_liquidity_local4b_vs_buffered_no_hard4c

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 002990, 021320 and 002410.
4. Keep hard 4C evidence-based:
   - default,
   - court rehabilitation,
   - refinancing failure,
   - auditor/control break,
   - impairment, covenant or solvency break.
5. Use local 4B-watch when:
   - PF/liquidity/orderbook/margin risk is present,
   - MFE remains weak or temporary,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%,
   - but hard-break evidence is not confirmed.
6. Keep RiskWatch/no-hard-4C when:
   - recovery or bounded MAE exists,
   - orderbook/capital/group buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
7. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 74
next_round = R11
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

