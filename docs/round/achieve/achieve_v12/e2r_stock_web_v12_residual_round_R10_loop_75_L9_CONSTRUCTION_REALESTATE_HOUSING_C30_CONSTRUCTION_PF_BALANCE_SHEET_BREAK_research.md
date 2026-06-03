# E2R Stock-Web v12 Residual Research — R10 Loop 75 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 75,
  "computed_next_round": "R11",
  "computed_next_loop": 75,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "PF_orderbook_liquidity_guardrail",
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

Previous completed state in this interactive run: R9 / loop 75.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 75
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 75
```

R10 is the construction/PF balance-sheet-break round.  
This file avoids both the top-covered C30 names and the loop-74 C30 names.

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
005960 / 동부건설 / weak-MFE PF/orderbook/liquidity local 4B
013580 / 계룡건설 / buffered RiskWatch / no hard 4C
004960 / 한신공영 / bounded-MAE recovery / no hard 4C
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
005960 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C30 is not “construction stock fell.”

The rule must split three states:

```text
PF/orderbook/liquidity risk + weak MFE + widening MAE
→ local 4B-watch

bounded MAE / recovery / buffer evidence
→ RiskWatch / no hard 4C

default / refinancing failure / impairment / covenant / solvency break
→ full 4B or hard 4C
```

A falling share price is smoke.  
C30 needs to decide whether the building is burning, or whether the smoke is from dust at the construction site.

---

## Case 1 — Local 4B risk: 005960 / 동부건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is PF exposure, orderbook quality, refinancing access, liquidity, margin pressure, covenant and solvency evidence.

```text
evidence_family = MID_BUILDER_PF_ORDERBOOK_LIQUIDITY_MARGIN_RISK_WITH_WEAK_MFE
case_role = risk_positive_local4b_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv`:

```text
2024-02-01,5350,5470,5330,5430
2024-02-19,5400,5500,5360,5430
2024-03-19,5110,5130,5040,5060
2024-08-05,4840,4845,4365,4435
2024-09-09,4200,4400,4175,4330
2024-10-25,4095,4100,3970,4000
```

### Backtest

```text
MFE_30D  = +2.80%
MAE_30D  = -5.79%
MFE_90D  = +2.80%
MAE_90D  = -9.53%
MFE_180D = +2.80%
MAE_180D = -25.79%
peak_180 = 5,500 on 2024-02-19
trough_180 = 3,970 on 2024-10-25
peak_to_later_drawdown = -27.82%
```

### Interpretation

This is a local 4B-watch row.  
The upside was almost nonexistent and the later MAE exceeded the C30 watch threshold. But price alone still does not prove hard 4C.

The correct label is:

```text
local 4B-watch / no hard 4C
```

until non-price refinancing, impairment, covenant or solvency evidence appears.

---

## Case 2 — Buffered RiskWatch / no hard 4C: 013580 / 계룡건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, orderbook visibility, capital buffer, refinancing access and margin evidence.

```text
evidence_family = REGIONAL_BUILDER_PF_FEAR_WITH_ORDERBOOK_AND_CAPITAL_BUFFER_NO_CONFIRMED_BREAK
case_role = overbearish_counterexample_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 14,460
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv`:

```text
2024-02-01,14460,14990,14300,14900
2024-02-19,15190,15430,15110,15330
2024-04-12,13300,13390,12950,12960
2024-08-05,14500,14500,13210,13630
2024-08-21,15140,15580,14980,15470
2024-10-25,13460,13470,13200,13330
```

### Backtest

```text
MFE_30D  = +6.71%
MAE_30D  = -5.60%
MFE_90D  = +6.71%
MAE_90D  = -10.44%
MFE_180D = +7.75%
MAE_180D = -10.44%
peak_180 = 15,580 on 2024-08-21
trough_180 = 12,950 on 2024-04-12
peak_to_later_drawdown = -15.28%
```

### Interpretation

This is a C30 overbearish-boundary case.  
PF fear deserves monitoring, but the price path does not justify full 4B or hard 4C.

Correct treatment:

```text
RiskWatch
no hard 4C without non-price break
```

---

## Case 3 — Bounded-MAE recovery / no hard 4C: 004960 / 한신공영

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, orderbook buffer, recovery quality, liquidity and solvency evidence.

```text
evidence_family = BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_RECOVERY_NO_CONFIRMED_SOLVENCY_BREAK
case_role = overbearish_counterexample_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,370
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv`:

```text
2024-02-01,7370,7770,7370,7720
2024-02-27,7090,7210,6990,7090
2024-04-12,6490,6500,6310,6320
2024-07-30,7190,7560,6890,7340
2024-08-05,6970,6970,6160,6300
2024-10-25,6740,6800,6570,6790
```

### Backtest

```text
MFE_30D  = +5.43%
MAE_30D  = -5.16%
MFE_90D  = +5.43%
MAE_90D  = -14.38%
MFE_180D = +5.43%
MAE_180D = -16.42%
peak_180 = 7,770 on 2024-02-01
trough_180 = 6,160 on 2024-08-05
peak_to_later_drawdown = -20.72%
```

### Interpretation

This is not Green.  
But it is also not a hard balance-sheet break. The row says C30 should keep a RiskWatch state when PF fear exists, while avoiding price-only hard 4C.

---

## Cross-case residual finding

### What this strengthens

```text
hard_4c_confirmation = strengthen
local_4b_watch_guard = strengthen
overbearish_no_hard4c_guard = strengthen
stage2_required_bridge = strengthen
```

### What this does not justify

```text
do_not_treat_all_construction_drawdowns_as_hard_4C = true
do_not_use_price_only_MAE_as_default_or_refinancing_failure = true
do_not_ignore_weak_MFE_local4B_risk = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C
```

This fine archetype covers:

```text
1. weak-MFE builder + PF/orderbook/liquidity risk + MAE widening → local 4B-watch
2. regional builder with bounded MAE and recovery → RiskWatch / no hard 4C
3. builder PF fear with recovery/buffer behavior → no hard 4C without non-price break
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "75", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-PFOrderbookLiquidityWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should flag local 4B when mid-builder PF/orderbook/liquidity risk produces weak MFE and widening MAE. Dongbu Construction had almost no upside and a later -25% MAE path, but hard 4C still requires explicit non-price refinancing, default, impairment, auditor/control or solvency break.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C", "symbol": "013580", "company_name": "계룡건설", "round": "R10", "loop": "75", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "Stage2-RiskWatch / BufferedBuilderNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not convert every regional-builder PF fear into full 4B or hard 4C when MAE is bounded and the stock shows recovery/sideways behavior. Kyeryong Construction is a buffered RiskWatch row: PF/orderbook watch is allowed, but hard balance-sheet break is not price-only.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "75", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "Stage2-RiskWatch / BuilderPFBoundedMAERecovery", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Hanshin Construction shows PF fear but also rebound behavior; full 4B or hard 4C requires non-price break evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B", "case_id": "R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "75", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-PFOrderbookLiquidityWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5350.0, "evidence_available_at_that_date": "MID_BUILDER_PF_ORDERBOOK_LIQUIDITY_MARGIN_RISK_WITH_WEAK_MFE", "evidence_source": "source_proxy_manual_verification_required:DONGBU_CONSTRUCTION_2024_PF_ORDERBOOK_LIQUIDITY_REFINANCING_MARGIN_RISK", "stage2_evidence_fields": ["PF_risk_or_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_orderbook_or_liquidity_risk", "weak_MFE", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv", "profile_path": "atlas/symbol_profiles/005/005960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.8, "MFE_90D_pct": 2.8, "MFE_180D_pct": 2.8, "MAE_30D_pct": -5.79, "MAE_90D_pct": -9.53, "MAE_180D_pct": -25.79, "peak_date": "2024-02-19", "peak_price": 5500.0, "drawdown_after_peak_pct": -27.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_no_hard4c", "current_profile_verdict": "C30 should flag local 4B when mid-builder PF/orderbook/liquidity risk produces weak MFE and widening MAE. Dongbu Construction had almost no upside and a later -25% MAE path, but hard 4C still requires explicit non-price refinancing, default, impairment, auditor/control or solvency break.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C30_PF_BUFFER_005960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C", "case_id": "R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C", "symbol": "013580", "company_name": "계룡건설", "round": "R10", "loop": "75", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage2-RiskWatch / BufferedBuilderNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 14460.0, "evidence_available_at_that_date": "REGIONAL_BUILDER_PF_FEAR_WITH_ORDERBOOK_AND_CAPITAL_BUFFER_NO_CONFIRMED_BREAK", "evidence_source": "source_proxy_manual_verification_required:KYERYONG_CONSTRUCTION_2024_PF_ORDERBOOK_CAPITAL_BUFFER_NO_HARD_BREAK", "stage2_evidence_fields": ["PF_risk_or_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_orderbook_or_liquidity_risk", "weak_MFE", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv", "profile_path": "atlas/symbol_profiles/013/013580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.71, "MFE_90D_pct": 6.71, "MFE_180D_pct": 7.75, "MAE_30D_pct": -5.6, "MAE_90D_pct": -10.44, "MAE_180D_pct": -10.44, "peak_date": "2024-08-21", "peak_price": 15580.0, "drawdown_after_peak_pct": -15.28, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "current_profile_verdict": "C30 should not convert every regional-builder PF fear into full 4B or hard 4C when MAE is bounded and the stock shows recovery/sideways behavior. Kyeryong Construction is a buffered RiskWatch row: PF/orderbook watch is allowed, but hard balance-sheet break is not price-only.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BUFFER_013580_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C", "case_id": "R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "75", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage2-RiskWatch / BuilderPFBoundedMAERecovery", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7370.0, "evidence_available_at_that_date": "BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_RECOVERY_NO_CONFIRMED_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:HANSHIN_CONSTRUCTION_2024_PF_ORDERBOOK_BUFFER_RECOVERY_NO_SOLVENCY_BREAK", "stage2_evidence_fields": ["PF_risk_or_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_orderbook_or_liquidity_risk", "weak_MFE", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv", "profile_path": "atlas/symbol_profiles/004/004960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.43, "MFE_90D_pct": 5.43, "MFE_180D_pct": 5.43, "MAE_30D_pct": -5.16, "MAE_90D_pct": -14.38, "MAE_180D_pct": -16.42, "peak_date": "2024-02-01", "peak_price": 7770.0, "drawdown_after_peak_pct": -20.72, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "current_profile_verdict": "C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Hanshin Construction shows PF fear but also rebound behavior; full 4B or hard 4C requires non-price break evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BUFFER_004960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B", "trigger_id": "TRG_R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B", "symbol": "005960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 14, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 4, "relative_strength_score": 1, "execution_risk_score": 16, "information_confidence": 2}, "weighted_score_before": 40, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 16, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 3, "relative_strength_score": 1, "execution_risk_score": 17, "information_confidence": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when weak MFE and widening MAE align with PF/orderbook/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 2.8, "MAE_90D_pct": -9.53, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should flag local 4B when mid-builder PF/orderbook/liquidity risk produces weak MFE and widening MAE. Dongbu Construction had almost no upside and a later -25% MAE path, but hard 4C still requires explicit non-price refinancing, default, impairment, auditor/control or solvency break."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C", "trigger_id": "TRG_R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C", "symbol": "013580", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 8, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 11, "relative_strength_score": 5, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 56, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 7, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 12, "relative_strength_score": 5, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 58, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when weak MFE and widening MAE align with PF/orderbook/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 6.71, "MAE_90D_pct": -10.44, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should not convert every regional-builder PF fear into full 4B or hard 4C when MAE is bounded and the stock shows recovery/sideways behavior. Kyeryong Construction is a buffered RiskWatch row: PF/orderbook watch is allowed, but hard balance-sheet break is not price-only."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C", "trigger_id": "TRG_R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C", "symbol": "004960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 8, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 11, "relative_strength_score": 5, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 56, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 7, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 12, "relative_strength_score": 5, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 58, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when weak MFE and widening MAE align with PF/orderbook/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 5.43, "MAE_90D_pct": -14.38, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Hanshin Construction shows PF fear but also rebound behavior; full 4B or hard 4C requires non-price break evidence."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 75, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 1, "overbearish_counterexample_count": 2, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C30 builders outside top-covered PF set and outside loop-74 names, +3 PF/orderbook/liquidity-buffer trigger families, +1 local-4B risk path, +2 no-hard-4C buffer boundaries, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 75, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "mid_builder_orderbook_liquidity_local4b_vs_buffered_no_hard4c", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split weak-MFE PF/orderbook/liquidity local 4B from buffered builder RiskWatch. MAE deterioration can trigger local 4B-watch, but full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["005960", "013580", "004960"], "share_count_validation_required": ["005960"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 75, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "overbearish_no_hard4c_guard", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 needs severity splitting. Dongbu Construction shows weak-MFE local 4B PF/orderbook risk; Kyeryong Construction and Hanshin Construction show buffered RiskWatch/no-hard-4C boundaries where price drawdown alone should not become balance-sheet break."}
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
005960:
  corporate_action_candidate_dates = 1997-01-31, 1999-06-16, 2000-02-22, 2012-09-10, 2014-05-16, 2015-09-04, 2016-11-04
  selected window = 2024-02-01~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

013580:
  corporate_action_candidate_dates = 1999-07-16
  selected window = 2024-02-01~D+180
  contamination = false

004960:
  corporate_action_candidate_dates = 1998-09-19, 2001-06-20, 2002-04-03, 2002-05-24, 2002-11-14
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
005960 also requires share-count validation before runtime promotion.
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
This R10/C30 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 005960 needs share-count validation.

Candidate axis:
mid_builder_orderbook_liquidity_local4b_vs_buffered_no_hard4c

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 005960, 013580 and 004960.
4. Validate 005960 share-count changes inside the selected window.
5. Keep hard 4C evidence-based:
   - default,
   - court rehabilitation,
   - refinancing failure,
   - auditor/control break,
   - impairment, covenant or solvency break.
6. Use local 4B-watch when:
   - PF/liquidity/orderbook/margin risk is present,
   - MFE remains weak or temporary,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - or post-peak drawdown <= -35%,
   - but hard-break evidence is not confirmed.
7. Keep RiskWatch/no-hard-4C when:
   - recovery or bounded MAE exists,
   - orderbook/capital/group buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
8. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 75
next_round = R11
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

