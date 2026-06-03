# E2R Stock-Web v12 Residual Research — R10 Loop 80 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 80,
  "computed_next_round": "R11",
  "computed_next_loop": 80,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "PF_refinancing_liquidity_orderbook_boundary_guardrail",
    "small_builder_high_MAE_local4B",
    "recovery_spike_no_hard4C_boundary",
    "bounded_builder_RiskWatch_no_forced4B_boundary",
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

Previous completed state in this interactive run: R9 / loop 80.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 80
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 80
```

R10 is the construction/PF balance-sheet-break round.  
This file avoids top-covered C30 names and avoids the loop-79 R10 names.

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
002410 / 범양건영 / small-builder PF high-MAE local 4B
013360 / 일성건설 / recovery spike no-hard-4C boundary
013580 / 계룡건설 / bounded PF RiskWatch no-forced-4B boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
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

건설주의 PF 우려는 지반의 물기다.  
C30이 보려는 것은 물기가 발목까지 찼는지, 아니면 기초가 꺼지는 균열인지다.

---

## Case 1 — Local 4B risk: 002410 / 범양건영

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, refinancing access, orderbook, liquidity, covenant, impairment and solvency evidence.

```text
evidence_family = SMALL_BUILDER_PF_REFINANCING_ORDERBOOK_LIQUIDITY_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK
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
2024-09-09,1150,1166,1125,1156
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

This is a C30 local 4B risk row.  
The path had almost no upside and then leaked into severe MAE territory.

Correct treatment:

```text
small-builder PF/refinancing watch + high MAE
→ local 4B-watch
→ no hard 4C without non-price refinancing/default/solvency break
```

---

## Case 2 — Recovery-spike / no hard 4C: 013360 / 일성건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is small-builder PF exposure, orderbook, liquidity, refinancing access, capital buffer and solvency evidence.

```text
evidence_family = SMALL_BUILDER_PF_FEAR_WITH_RECOVERY_SPIKE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK
case_role = overbearish_counterexample_recovery_spike_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv`:

```text
2024-02-01,1300,1304,1286,1294
2024-02-19,1315,1350,1312,1320
2024-03-07,1187,1205,1110,1176
2024-04-11,1395,1583,1285,1380
2024-07-25,1663,1697,1510,1530
2024-08-05,1500,1500,1288,1340
2024-10-25,1215,1221,1178,1178
```

### Backtest

```text
MFE_30D  = +4.38%
MAE_30D  = -14.62%
MFE_90D  = +21.77%
MAE_90D  = -14.62%
MFE_180D = +30.54%
MAE_180D = -14.62%
peak_180 = 1,697 on 2024-07-25
trough_180 = 1,110 on 2024-03-07
peak_to_later_drawdown = -30.58%
```

### Interpretation

This is PF RiskWatch with recovery-spike evidence, not hard 4C.  
The later weakness justifies monitoring, but price action alone does not prove a balance-sheet break.

Correct treatment:

```text
small-builder PF watch
recovery spike + no confirmed solvency break
→ RiskWatch / no hard 4C
→ local 4B only if non-price refinancing/liquidity bridge worsens
```

---

## Case 3 — Bounded RiskWatch / no forced 4B: 013580 / 계룡건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF/orderbook exposure, liquidity, refinancing, capital buffer and solvency evidence.

```text
evidence_family = BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK
case_role = overbearish_counterexample_bounded_no_forced4b_no_hard4c
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
2024-04-15,12930,13040,12800,12800
2024-08-21,15140,15580,14980,15470
2024-09-10,13800,13900,13640,13670
2024-10-25,13460,13470,13200,13330
```

### Backtest

```text
MFE_30D  = +6.71%
MAE_30D  = -4.56%
MFE_90D  = +6.71%
MAE_90D  = -11.48%
MFE_180D = +7.75%
MAE_180D = -11.48%
peak_180 = 15,580 on 2024-08-21
trough_180 = 12,800 on 2024-04-15
peak_to_later_drawdown = -15.28%
```

### Interpretation

This is not hard 4C and not forced local 4B.  
PF/orderbook watch remains appropriate, but bounded MAE blocks a price-only balance-sheet-break label.

Correct treatment:

```text
RiskWatch
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
overbearish_no_hard4c_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
```

### What this does not justify

```text
do_not_treat_all_construction_drawdowns_as_hard_4C = true
do_not_use_price_only_MAE_as_default_or_refinancing_failure = true
do_not_force_4B_on_bounded_builder_rows = true
do_not_ignore_high_MAE_local4B_risk = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B
```

This fine archetype covers:

```text
1. small-builder PF fear + MAE_90D <= -20% or MAE_180D <= -25% → local 4B-watch
2. recovery spike with no confirmed solvency break → RiskWatch / no hard 4C
3. bounded MAE builder PF fear → no forced 4B / no hard 4C
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L80-C30-002410-BEOMYANG-E&C-PF-HIGHMAE-LOCAL4B", "symbol": "002410", "company_name": "범양건영", "round": "R10", "loop": "80", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SmallBuilderPFHighMAENoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should flag local 4B when small-builder/PF fear aligns with persistent high MAE and weak recovery, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L80-C30-013360-ILSEONG-E&C-RECOVERY-SPIKE-NO-HARD4C", "symbol": "013360", "company_name": "일성건설", "round": "R10", "loop": "80", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-RecoverySpikeSmallBuilderPFNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not convert small-builder/PF fear into hard 4C when the path still produces a recovery spike and MAE remains below severe threshold. Price action alone is not balance-sheet-break evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L80-C30-013580-KYERYONG-E&C-BOUNDED-RISKWATCH-NO-FORCED4B", "symbol": "013580", "company_name": "계룡건설", "round": "R10", "loop": "80", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BoundedBuilderPFNoForced4BNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L80-C30-002410-BEOMYANG-E&C-PF-HIGHMAE-LOCAL4B", "case_id": "R10L80-C30-002410-BEOMYANG-E&C-PF-HIGHMAE-LOCAL4B", "symbol": "002410", "company_name": "범양건영", "round": "R10", "loop": "80", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-SmallBuilderPFHighMAENoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1767.0, "evidence_available_at_that_date": "SMALL_BUILDER_PF_REFINANCING_ORDERBOOK_LIQUIDITY_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK", "evidence_source": "source_proxy_manual_verification_required:BEOMYANG_E&C_2024_PF_REFINANCING_ORDERBOOK_LIQUIDITY_SOLVENCY_BRIDGE", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv", "profile_path": "atlas/symbol_profiles/002/002410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.04, "MFE_90D_pct": 2.04, "MFE_180D_pct": 2.04, "MAE_30D_pct": -5.66, "MAE_90D_pct": -22.64, "MAE_180D_pct": -43.41, "peak_date": "2024-02-02", "peak_price": 1803.0, "drawdown_after_peak_pct": -44.54, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_no_hard4c", "current_profile_verdict": "C30 should flag local 4B when small-builder/PF fear aligns with persistent high MAE and weak recovery, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_002410_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L80-C30-013360-ILSEONG-E&C-RECOVERY-SPIKE-NO-HARD4C", "case_id": "R10L80-C30-013360-ILSEONG-E&C-RECOVERY-SPIKE-NO-HARD4C", "symbol": "013360", "company_name": "일성건설", "round": "R10", "loop": "80", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-RecoverySpikeSmallBuilderPFNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1300.0, "evidence_available_at_that_date": "SMALL_BUILDER_PF_FEAR_WITH_RECOVERY_SPIKE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:ILSEONG_E&C_2024_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_BUFFER_NO_HARD4C", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv", "profile_path": "atlas/symbol_profiles/013/013360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.38, "MFE_90D_pct": 21.77, "MFE_180D_pct": 30.54, "MAE_30D_pct": -14.62, "MAE_90D_pct": -14.62, "MAE_180D_pct": -14.62, "peak_date": "2024-07-25", "peak_price": 1697.0, "drawdown_after_peak_pct": -30.58, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_recovery_spike_no_hard4c", "current_profile_verdict": "C30 should not convert small-builder/PF fear into hard 4C when the path still produces a recovery spike and MAE remains below severe threshold. Price action alone is not balance-sheet-break evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_013360_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L80-C30-013580-KYERYONG-E&C-BOUNDED-RISKWATCH-NO-FORCED4B", "case_id": "R10L80-C30-013580-KYERYONG-E&C-BOUNDED-RISKWATCH-NO-FORCED4B", "symbol": "013580", "company_name": "계룡건설", "round": "R10", "loop": "80", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-BoundedBuilderPFNoForced4BNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 14460.0, "evidence_available_at_that_date": "BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:KYERYONG_E&C_2024_BUILDER_PF_ORDERBOOK_LIQUIDITY_BUFFER_NO_FORCED4B", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv", "profile_path": "atlas/symbol_profiles/013/013580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.71, "MFE_90D_pct": 6.71, "MFE_180D_pct": 7.75, "MAE_30D_pct": -4.56, "MAE_90D_pct": -11.48, "MAE_180D_pct": -11.48, "peak_date": "2024-08-21", "peak_price": 15580.0, "drawdown_after_peak_pct": -15.28, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_bounded_no_forced4b_no_hard4c", "current_profile_verdict": "C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_013580_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L80-C30-002410-BEOMYANG-E&C-PF-HIGHMAE-LOCAL4B", "trigger_id": "TRG_R10L80-C30-002410-BEOMYANG-E&C-PF-HIGHMAE-LOCAL4B", "symbol": "002410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 18, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 3, "recovery_or_bounded_MAE_score": 2, "execution_risk_score": 22, "information_confidence": 2}, "weighted_score_before": 31, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 20, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 2, "recovery_or_bounded_MAE_score": 2, "execution_risk_score": 24, "information_confidence": 2}, "weighted_score_after": 28, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "recovery_or_bounded_MAE_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 2.04, "MAE_90D_pct": -22.64, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should flag local 4B when small-builder/PF fear aligns with persistent high MAE and weak recovery, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L80-C30-013360-ILSEONG-E&C-RECOVERY-SPIKE-NO-HARD4C", "trigger_id": "TRG_R10L80-C30-013360-ILSEONG-E&C-RECOVERY-SPIKE-NO-HARD4C", "symbol": "013360", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 8, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 13, "recovery_or_bounded_MAE_score": 14, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 60, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 7, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "recovery_or_bounded_MAE_score": 15, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 62, "stage_label_after": "RiskWatch / no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "recovery_or_bounded_MAE_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 21.77, "MAE_90D_pct": -14.62, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should not convert small-builder/PF fear into hard 4C when the path still produces a recovery spike and MAE remains below severe threshold. Price action alone is not balance-sheet-break evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L80-C30-013580-KYERYONG-E&C-BOUNDED-RISKWATCH-NO-FORCED4B", "trigger_id": "TRG_R10L80-C30-013580-KYERYONG-E&C-BOUNDED-RISKWATCH-NO-FORCED4B", "symbol": "013580", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 8, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 13, "recovery_or_bounded_MAE_score": 14, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 60, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 7, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "recovery_or_bounded_MAE_score": 15, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 62, "stage_label_after": "RiskWatch / no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "recovery_or_bounded_MAE_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 6.71, "MAE_90D_pct": -11.48, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 80, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_PF_HIGH_MAE_VS_RECOVERY_SPIKE_AND_BOUNDED_NO_FORCED4B", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 1, "overbearish_counterexample_count": 2, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C30 construction/PF symbols outside top-covered 006360/294870/375500/000720 set and outside loop-79 R10 names, +3 Beomyang/Ilseong/Kyeryong trigger families, +1 high-MAE local-4B risk path, +2 recovery/bounded no-hard-4C boundaries, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 80, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "small_builder_PF_high_MAE_vs_recovery_spike_and_bounded_no_forced4B", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split high-MAE small-builder PF local 4B from recovery-spike / bounded RiskWatch no-hard-4C boundaries. MAE deterioration can trigger local 4B-watch, but full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["002410", "013360", "013580"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 80, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "overbearish_no_hard4c_guard", "bounded_MAE_no_forced_4B_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 severity split is strengthened. Beomyang E&C shows a small-builder high-MAE local 4B path; Ilseong E&C and Kyeryong Construction show recovery-spike / bounded RiskWatch no-hard-4C boundaries where PF fear requires monitoring but price action alone is not confirmed balance-sheet break evidence."}
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
  name = 범양건영 from 1996-07-31, 범양건업 before that
  corporate_action_candidate_dates = 1996-01-03, 2009-12-21, 2014-07-07, 2015-07-09, 2015-12-30, 2017-12-06
  selected window = 2024-02-01~D+180
  contamination = false

013360:
  name = 일성건설 from 1996-11-25, 일성종합건설 before that
  corporate_action_candidate_dates = 1996-01-03, 1998-12-21, 2000-04-21, 2000-08-18, 2003-01-07, 2017-05-18
  selected window = 2024-02-01~D+180
  contamination = false

013580:
  name = 계룡건설
  corporate_action_candidate_dates = 1999-07-16
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
small_builder_PF_high_MAE_vs_recovery_spike_and_bounded_no_forced4B

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 002410, 013360 and 013580.
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
   - recovery spike or bounded MAE exists,
   - orderbook/capital/group/support buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
7. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 80
next_round = R11
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

