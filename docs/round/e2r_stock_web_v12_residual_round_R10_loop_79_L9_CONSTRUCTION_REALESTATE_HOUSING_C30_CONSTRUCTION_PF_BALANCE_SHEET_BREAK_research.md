# E2R Stock-Web v12 Residual Research — R10 Loop 79 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 79,
  "computed_next_round": "R11",
  "computed_next_loop": 79,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "PF_refinancing_liquidity_orderbook_boundary_guardrail",
    "small_mid_builder_high_MAE_local4B",
    "recovery_spike_no_hard4C_boundary",
    "bounded_builder_RiskWatch_no_forced4B_boundary",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R9 / loop 79.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 79
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 79
```

R10 is the construction/PF balance-sheet-break round.  
This file avoids the top-covered C30 names and avoids the loop-78 R10 names.

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
005960 / 동부건설 / builder PF high-MAE local 4B
003070 / 코오롱글로벌 / PF recovery spike no-hard-4C boundary
021320 / KCC건설 / bounded PF RiskWatch no-forced-4B boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
005960 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
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

건설주의 PF 우려는 빗물 자국처럼 번진다.  
C30이 보려는 것은 벽지가 젖은 정도인지, 기초 콘크리트가 갈라지는 소리인지다.

---

## Case 1 — Local 4B risk: 005960 / 동부건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is PF exposure, refinancing access, orderbook, liquidity, covenant, impairment and solvency evidence.

```text
evidence_family = BUILDER_PF_REFINANCING_ORDERBOOK_LIQUIDITY_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK
case_role = risk_positive_local4b_with_sharecount_validation_no_hard4c
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
2024-06-13,4950,4980,4750,4855
2024-08-05,4840,4845,4365,4435
2024-09-09,4200,4400,4175,4330
2024-10-25,4095,4100,3970,4000
```

### Backtest

```text
MFE_30D  = +2.80%
MAE_30D  = -5.79%
MFE_90D  = +2.80%
MAE_90D  = -11.21%
MFE_180D = +2.80%
MAE_180D = -25.79%
peak_180 = 5,500 on 2024-02-19
trough_180 = 3,970 on 2024-10-25
peak_to_later_drawdown = -27.82%
```

### Interpretation

This is a C30 local 4B risk row.  
The path had almost no upside and then leaked into high-MAE territory.

Correct treatment:

```text
builder PF/refinancing watch + high MAE
→ local 4B-watch
→ no hard 4C without non-price refinancing/default/solvency break
```

---

## Case 2 — Recovery-spike / no hard 4C: 003070 / 코오롱글로벌

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is builder/developer PF exposure, orderbook, liquidity, refinancing access, capital buffer and solvency evidence.

```text
evidence_family = BUILDER_DEVELOPER_PF_FEAR_WITH_RECOVERY_SPIKE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK
case_role = overbearish_counterexample_recovery_spike_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 9,370
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv`:

```text
2024-02-01,9370,9760,9370,9750
2024-02-19,10110,10240,10090,10120
2024-03-08,9100,9170,8800,9140
2024-04-19,8210,8400,8170,8360
2024-06-13,13870,15240,12690,12800
2024-06-21,15740,16110,14040,14090
2024-08-05,9610,9620,8500,8800
```

### Backtest

```text
MFE_30D  = +9.28%
MAE_30D  = -6.08%
MFE_90D  = +62.65%
MAE_90D  = -12.81%
MFE_180D = +71.93%
MAE_180D = -12.81%
peak_180 = 16,110 on 2024-06-21
trough_180 = 8,170 on 2024-04-19
peak_to_later_drawdown = -47.24%
```

### Interpretation

This is PF RiskWatch with a recovery spike, not hard 4C.  
The later drawdown justifies monitoring, but the recovery spike blocks price-only balance-sheet-break labeling.

Correct treatment:

```text
PF/developer watch
recovery spike + no confirmed solvency break
→ RiskWatch / no hard 4C
→ local 4B only if non-price refinancing/liquidity bridge worsens
```

---

## Case 3 — Bounded RiskWatch / no forced 4B: 021320 / KCC건설

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
entry_price = 4,850
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv`:

```text
2024-02-01,4850,4950,4785,4915
2024-02-02,5070,5070,4840,4970
2024-03-07,4580,4655,4565,4620
2024-04-08,4515,5750,4465,4615
2024-08-05,4250,4470,4170,4180
2024-10-16,4315,4315,4230,4230
2024-10-31,4230,4325,4105,4325
```

### Backtest

```text
MFE_30D  = +4.54%
MAE_30D  = -5.88%
MFE_90D  = +18.56%
MAE_90D  = -8.87%
MFE_180D = +18.56%
MAE_180D = -15.36%
peak_180 = 5,750 on 2024-04-08
trough_180 = 4,105 on 2024-10-31
peak_to_later_drawdown = -28.61%
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
share_count_validation_guard = strengthen
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
BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C
```

This fine archetype covers:

```text
1. builder PF fear + MAE_180D <= -25% → local 4B-watch
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
{"row_type": "case", "case_id": "R10L79-C30-005960-DONGBU-E&C-PF-HIGHMAE-LOCAL4B", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "79", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-BuilderPFHighMAEWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should flag local 4B when builder/PF fear aligns with persistent MAE and liquidity/orderbook risk, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Dongbu E&C leaked into a high-MAE path with very limited MFE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L79-C30-003070-KOLON-GLOBAL-PF-RECOVERY-SPIKE-NO-HARD4C", "symbol": "003070", "company_name": "코오롱글로벌", "round": "R10", "loop": "79", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-RecoverySpikePFNoHard4CWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not over-convert builder/PF fear into hard 4C when the path produces a strong recovery spike. Kolon Global needs PF/orderbook/liquidity monitoring, but price action alone is not confirmed balance-sheet break evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L79-C30-021320-KCC-E&C-PF-BOUNDED-RISKWATCH-NO-FORCED4B", "symbol": "021320", "company_name": "KCC건설", "round": "R10", "loop": "79", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BoundedBuilderPFNoForced4BNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed. KCC E&C is a boundary row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, refinancing access, liquidity, covenant, impairment, auditor/control and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L79-C30-005960-DONGBU-E&C-PF-HIGHMAE-LOCAL4B", "case_id": "R10L79-C30-005960-DONGBU-E&C-PF-HIGHMAE-LOCAL4B", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "79", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-BuilderPFHighMAEWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5350.0, "evidence_available_at_that_date": "BUILDER_PF_REFINANCING_ORDERBOOK_LIQUIDITY_RISK_WITH_HIGH_MAE_NO_CONFIRMED_HARD_BREAK", "evidence_source": "source_proxy_manual_verification_required:DONGBU_E&C_2024_PF_REFINANCING_ORDERBOOK_LIQUIDITY_SOLVENCY_BRIDGE", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv", "profile_path": "atlas/symbol_profiles/005/005960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.8, "MFE_90D_pct": 2.8, "MFE_180D_pct": 2.8, "MAE_30D_pct": -5.79, "MAE_90D_pct": -11.21, "MAE_180D_pct": -25.79, "peak_date": "2024-02-19", "peak_price": 5500.0, "drawdown_after_peak_pct": -27.82, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_with_sharecount_validation_no_hard4c", "current_profile_verdict": "C30 should flag local 4B when builder/PF fear aligns with persistent MAE and liquidity/orderbook risk, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Dongbu E&C leaked into a high-MAE path with very limited MFE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C30_PF_BOUNDARY_005960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L79-C30-003070-KOLON-GLOBAL-PF-RECOVERY-SPIKE-NO-HARD4C", "case_id": "R10L79-C30-003070-KOLON-GLOBAL-PF-RECOVERY-SPIKE-NO-HARD4C", "symbol": "003070", "company_name": "코오롱글로벌", "round": "R10", "loop": "79", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-RecoverySpikePFNoHard4CWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 9370.0, "evidence_available_at_that_date": "BUILDER_DEVELOPER_PF_FEAR_WITH_RECOVERY_SPIKE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:KOLON_GLOBAL_2024_BUILDER_PF_ORDERBOOK_LIQUIDITY_BUFFER_NO_HARD4C", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv", "profile_path": "atlas/symbol_profiles/003/003070.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.28, "MFE_90D_pct": 62.65, "MFE_180D_pct": 71.93, "MAE_30D_pct": -6.08, "MAE_90D_pct": -12.81, "MAE_180D_pct": -12.81, "peak_date": "2024-06-21", "peak_price": 16110.0, "drawdown_after_peak_pct": -47.24, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_recovery_spike_no_hard4c", "current_profile_verdict": "C30 should not over-convert builder/PF fear into hard 4C when the path produces a strong recovery spike. Kolon Global needs PF/orderbook/liquidity monitoring, but price action alone is not confirmed balance-sheet break evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_003070_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L79-C30-021320-KCC-E&C-PF-BOUNDED-RISKWATCH-NO-FORCED4B", "case_id": "R10L79-C30-021320-KCC-E&C-PF-BOUNDED-RISKWATCH-NO-FORCED4B", "symbol": "021320", "company_name": "KCC건설", "round": "R10", "loop": "79", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-BoundedBuilderPFNoForced4BNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4850.0, "evidence_available_at_that_date": "BUILDER_PF_ORDERBOOK_FEAR_WITH_BOUNDED_MAE_AND_NO_CONFIRMED_REFINANCING_OR_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:KCC_E&C_2024_BUILDER_PF_ORDERBOOK_LIQUIDITY_BUFFER_NO_FORCED4B", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_liquidity_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE_or_post_peak_drawdown", "source_repair_required"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv", "profile_path": "atlas/symbol_profiles/021/021320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.54, "MFE_90D_pct": 18.56, "MFE_180D_pct": 18.56, "MAE_30D_pct": -5.88, "MAE_90D_pct": -8.87, "MAE_180D_pct": -15.36, "peak_date": "2024-04-08", "peak_price": 5750.0, "drawdown_after_peak_pct": -28.61, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_bounded_no_forced4b_no_hard4c", "current_profile_verdict": "C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed. KCC E&C is a boundary row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_021320_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L79-C30-005960-DONGBU-E&C-PF-HIGHMAE-LOCAL4B", "trigger_id": "TRG_R10L79-C30-005960-DONGBU-E&C-PF-HIGHMAE-LOCAL4B", "symbol": "005960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 17, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 3, "recovery_or_bounded_MAE_score": 2, "execution_risk_score": 21, "share_count_validation_risk": 8, "information_confidence": 2}, "weighted_score_before": 32, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 19, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 2, "recovery_or_bounded_MAE_score": 2, "execution_risk_score": 23, "share_count_validation_risk": 10, "information_confidence": 2}, "weighted_score_after": 29, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "recovery_or_bounded_MAE_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 2.8, "MAE_90D_pct": -11.21, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should flag local 4B when builder/PF fear aligns with persistent MAE and liquidity/orderbook risk, but hard 4C still requires non-price refinancing failure, default, covenant, impairment, auditor/control or solvency evidence. Dongbu E&C leaked into a high-MAE path with very limited MFE."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L79-C30-003070-KOLON-GLOBAL-PF-RECOVERY-SPIKE-NO-HARD4C", "trigger_id": "TRG_R10L79-C30-003070-KOLON-GLOBAL-PF-RECOVERY-SPIKE-NO-HARD4C", "symbol": "003070", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 8, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 12, "recovery_or_bounded_MAE_score": 14, "execution_risk_score": 8, "share_count_validation_risk": 0, "information_confidence": 2}, "weighted_score_before": 60, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 7, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "recovery_or_bounded_MAE_score": 15, "execution_risk_score": 7, "share_count_validation_risk": 0, "information_confidence": 2}, "weighted_score_after": 62, "stage_label_after": "RiskWatch / no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "recovery_or_bounded_MAE_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 62.65, "MAE_90D_pct": -12.81, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should not over-convert builder/PF fear into hard 4C when the path produces a strong recovery spike. Kolon Global needs PF/orderbook/liquidity monitoring, but price action alone is not confirmed balance-sheet break evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L79-C30-021320-KCC-E&C-PF-BOUNDED-RISKWATCH-NO-FORCED4B", "trigger_id": "TRG_R10L79-C30-021320-KCC-E&C-PF-BOUNDED-RISKWATCH-NO-FORCED4B", "symbol": "021320", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 8, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 12, "recovery_or_bounded_MAE_score": 14, "execution_risk_score": 8, "share_count_validation_risk": 0, "information_confidence": 2}, "weighted_score_before": 60, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 7, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "recovery_or_bounded_MAE_score": 15, "execution_risk_score": 7, "share_count_validation_risk": 0, "information_confidence": 2}, "weighted_score_after": 62, "stage_label_after": "RiskWatch / no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "recovery_or_bounded_MAE_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE aligns with PF/refinancing/liquidity risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 18.56, "MAE_90D_pct": -8.87, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should keep PF/orderbook monitoring active for bounded builders, but should not force local 4B or hard 4C when MAE is contained and no non-price refinancing or solvency break is confirmed. KCC E&C is a boundary row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 79, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_HIGH_MAE_LOCAL4B_VS_RECOVERY_SPIKE_AND_BOUNDED_RISKWATCH_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 1, "overbearish_counterexample_count": 2, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C30 construction/PF symbols outside top-covered 006360/294870/375500/000720 set and outside loop-78 R10 names, +3 Dongbu/Kolon/KCC trigger families, +1 high-MAE local-4B risk path, +2 recovery/bounded no-hard-4C boundaries, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 79, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "builder_PF_high_MAE_local4B_vs_recovery_spike_and_bounded_RiskWatch_no_hard4C", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split high-MAE builder PF local 4B from recovery-spike / bounded RiskWatch no-hard-4C boundaries. MAE deterioration can trigger local 4B-watch, but full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["005960", "003070", "021320"], "share_count_validation_required": ["005960"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 79, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "overbearish_no_hard4c_guard", "bounded_MAE_no_forced_4B_guard", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 severity split is strengthened. Dongbu E&C shows a builder PF high-MAE local 4B path; Kolon Global and KCC E&C show recovery-spike / bounded RiskWatch no-hard-4C boundaries where PF fear requires monitoring but price action alone is not confirmed balance-sheet break evidence."}
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
  name = 동부건설
  corporate_action_candidate_dates = 1997-01-31, 1999-06-16, 2000-02-22, 2012-09-10, 2014-05-16, 2015-09-04, 2016-11-04
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

003070:
  name = 코오롱글로벌 from 2012-01-11, 코오롱건설 before that
  corporate_action_candidate_dates = 1997-01-03, 1999-10-22, 2004-12-30, 2010-11-23, 2012-01-11, 2014-05-23, 2017-08-01, 2023-01-31, 2025-12-11
  selected window = 2024-02-01~D+180
  contamination = false

021320:
  name = KCC건설 from 2005-04-04, 금강종합건설 before that
  corporate_action_candidate_dates = 2014-05-12, 2014-07-09
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
005960 also requires share-count validation before runtime promotion.
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
This R10/C30 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 005960 needs share-count validation.

Candidate axis:
builder_PF_high_MAE_local4B_vs_recovery_spike_and_bounded_RiskWatch_no_hard4C

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 005960, 003070 and 021320.
4. Validate 005960 share-count changes inside the selected window.
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
7. Keep RiskWatch/no-hard-4C/no-forced-4B when:
   - recovery spike or bounded MAE exists,
   - orderbook/capital/group/support buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
8. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 79
next_round = R11
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

