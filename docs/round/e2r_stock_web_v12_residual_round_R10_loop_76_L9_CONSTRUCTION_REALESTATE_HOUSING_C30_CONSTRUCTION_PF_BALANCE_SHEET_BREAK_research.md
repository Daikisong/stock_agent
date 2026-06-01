# E2R Stock-Web v12 Residual Research — R10 Loop 76 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 76,
  "computed_next_round": "R11",
  "computed_next_loop": 76,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4C_balance_sheet_break_guard",
    "4B_non_price_requirement_stress_test",
    "PF_financing_support_boundary_guardrail",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation",
    "corporate_action_validation_queue_creation"
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

Previous completed state in this interactive run: R9 / loop 76.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 76
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 76
```

R10 is the construction/PF balance-sheet-break round.  
This file avoids the top-covered C30 names and avoids the loop-75 R10 names.

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
001470 / 삼부토건 / builder financing-risk high-MAE local 4B
034300 / 신세계건설 / post-CA support/recovery no-hard-4C boundary
035890 / 서희건설 / orderbook/buffer bounded-MAE no-hard-4C boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
001470 shows share-count changes inside the selected window and requires coding-agent validation.
034300 has a 2024-02-06 corporate-action candidate, so the selected trigger starts 2024-02-07 after that candidate date.
```

## Research thesis

C30 is not “construction stock fell.”

The severity ladder is:

```text
PF / financing / orderbook fear
→ RiskWatch

PF / financing fear + high MAE or post-peak drawdown
→ local 4B-watch

default / refinancing failure / impairment / covenant / solvency break
→ full 4B or hard 4C
```

A falling construction stock is smoke.  
C30 must decide whether it is a burning building, or dust from a jobsite with a support beam still standing.

---

## Case 1 — Local 4B risk: 001470 / 삼부토건

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is PF exposure, financing access, liquidity, covenant, impairment, auditor/control and solvency evidence.

```text
evidence_family = BUILDER_FINANCING_RISK_THEME_WITH_HIGH_MAE_SHARECOUNT_VALIDATION_REQUIRED
case_role = risk_positive_local4b_no_hard4c_with_sharecount_validation
trigger_date = 2024-02-08
entry_date = 2024-02-13
entry_price = 2,155
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv`:

```text
2024-02-13,2155,2630,2100,2585
2024-03-15,2565,2865,2430,2690
2024-04-08,1670,1836,1510,1540
2024-08-05,1369,1369,1150,1259
2024-09-09,456,530,440,498
```

### Backtest

```text
MFE_30D  = +32.95%
MAE_30D  = -6.73%
MFE_90D  = +32.95%
MAE_90D  = -29.93%
MFE_180D = +32.95%
MAE_180D = -79.58%
peak_180 = 2,865 on 2024-03-15
trough_180 = 440 on 2024-09-09
peak_to_later_drawdown = -84.64%
```

### Interpretation

This is a local 4B risk row.  
The early spike was tradable, but later MAE and post-peak drawdown were severe.

Correct treatment:

```text
high-MAE builder/financing risk
→ local 4B-watch
→ no hard 4C without non-price default/refinancing/solvency break
```

---

## Case 2 — Post-CA support / no hard 4C: 034300 / 신세계건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
source_repair_required = true
```

The source-repair task is PF exposure, refinancing access, group/support buffer, orderbook quality, liquidity and solvency evidence.

```text
evidence_family = BUILDER_PF_FEAR_POST_CA_WITH_SUPPORT_RECOVERY_NO_CONFIRMED_SOLVENCY_BREAK
case_role = overbearish_counterexample_post_ca_no_hard4c
trigger_date = 2024-02-06
entry_date = 2024-02-07
entry_price = 11,310
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv`:

```text
2024-02-06,11870,11870,11310,11310
2024-02-07,11310,11550,11200,11460
2024-04-09,10490,10580,10410,10450
2024-09-30,18300,18340,18150,18160
2024-10-29,18110,18120,18100,18100
```

### Backtest

```text
MFE_30D  = +12.73%
MAE_30D  = -6.37%
MFE_90D  = +23.78%
MAE_90D  = -7.96%
MFE_180D = +62.16%
MAE_180D = -7.96%
peak_180 = 18,340 on 2024-09-30
trough_180 = 10,410 on 2024-04-09
peak_to_later_drawdown = -1.42%
```

### Interpretation

This is not a hard 4C row.  
It is a post-CA support/recovery boundary. PF fear deserves monitoring, but price action alone does not justify a balance-sheet-break label.

Correct treatment:

```text
RiskWatch
post-CA validation required
no hard 4C without non-price break
```

---

## Case 3 — Bounded-MAE buffer / no hard 4C: 035890 / 서희건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF/orderbook exposure, capital buffer, refinancing access, cash flow and solvency evidence.

```text
evidence_family = REGIONAL_BUILDER_PF_FEAR_WITH_BOUNDED_MAE_RECOVERY_ORDERBOOK_BUFFER
case_role = overbearish_counterexample_no_hard4c
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,278
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv`:

```text
2024-02-01,1278,1302,1270,1300
2024-03-22,1326,1341,1300,1341
2024-08-05,1315,1318,1190,1227
2024-10-10,1561,1621,1561,1577
2024-10-25,1418,1427,1392,1398
```

### Backtest

```text
MFE_30D  = +3.05%
MAE_30D  = -3.76%
MFE_90D  = +7.67%
MAE_90D  = -3.76%
MFE_180D = +26.84%
MAE_180D = -6.89%
peak_180 = 1,621 on 2024-10-10
trough_180 = 1,190 on 2024-08-05
peak_to_later_drawdown = -13.76%
```

### Interpretation

This is the bounded-MAE boundary.  
It is a RiskWatch row, not a Green row. But it is also not hard 4C.

Correct treatment:

```text
PF/orderbook watch
bounded MAE + recovery
→ no hard 4C without non-price break
```

---

## Cross-case residual finding

### What this strengthens

```text
hard_4c_confirmation = strengthen
local_4b_watch_guard = strengthen
overbearish_no_hard4c_guard = strengthen
share_count_validation_guard = strengthen
corporate_action_validation_guard = strengthen
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
BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C
```

This fine archetype covers:

```text
1. builder/financing risk + high MAE/post-peak drawdown → local 4B-watch
2. post-CA support/recovery builder → RiskWatch / no hard 4C
3. bounded-MAE regional builder → RiskWatch / no hard 4C
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B", "symbol": "001470", "company_name": "삼부토건", "round": "R10", "loop": "76", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-BuilderFinancingRiskHighMAE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should flag local 4B when a builder/financing-risk row produces a high-MFE but then opens severe MAE and post-peak drawdown. Sambu Construction had a tradable spike but later collapsed; however hard 4C still requires non-price default, refinancing, auditor/control, impairment, covenant or solvency evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "76", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BufferedBuilderPostCASupportNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not convert every PF fear or construction liquidity story into hard 4C when post-CA price action recovers and stabilizes. Shinsegae Construction requires post-corporate-action validation, but the post-CA window is a no-hard-4C boundary unless non-price solvency/refinancing break is confirmed.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
{"row_type": "case", "case_id": "R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C", "symbol": "035890", "company_name": "서희건설", "round": "R10", "loop": "76", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-OrderbookBufferBoundedMAENoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Seohee Construction showed a low-MAE recovery path; without non-price PF/refinancing or solvency break it should remain RiskWatch/no-hard-4C.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF exposure, orderbook, liquidity, refinancing, capital buffer, covenant, impairment and solvency evidence required before full 4B/4C promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B", "case_id": "R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B", "symbol": "001470", "company_name": "삼부토건", "round": "R10", "loop": "76", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-BuilderFinancingRiskHighMAE", "trigger_date": "2024-02-08", "entry_date": "2024-02-13", "entry_price": 2155.0, "evidence_available_at_that_date": "BUILDER_FINANCING_RISK_THEME_WITH_HIGH_MAE_SHARECOUNT_VALIDATION_REQUIRED", "evidence_source": "source_proxy_manual_verification_required:SAMBU_CONSTRUCTION_2024_BUILDER_FINANCING_PF_LIQUIDITY_RISK_SHARECOUNT_VALIDATION", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE", "post_peak_drawdown", "sharecount_or_CA_validation"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv", "profile_path": "atlas/symbol_profiles/001/001470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.95, "MFE_90D_pct": 32.95, "MFE_180D_pct": 32.95, "MAE_30D_pct": -6.73, "MAE_90D_pct": -29.93, "MAE_180D_pct": -79.58, "peak_date": "2024-03-15", "peak_price": 2865.0, "drawdown_after_peak_pct": -84.64, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "risk_positive_local4b_no_hard4c_with_sharecount_validation", "current_profile_verdict": "C30 should flag local 4B when a builder/financing-risk row produces a high-MFE but then opens severe MAE and post-peak drawdown. Sambu Construction had a tradable spike but later collapsed; however hard 4C still requires non-price default, refinancing, auditor/control, impairment, covenant or solvency evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validated_window_required", "share_count_change_inside_window": true, "same_entry_group_id": "C30_PF_BOUNDARY_001470_2024-02-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C", "case_id": "R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "76", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-BufferedBuilderPostCASupportNoHard4C", "trigger_date": "2024-02-06", "entry_date": "2024-02-07", "entry_price": 11310.0, "evidence_available_at_that_date": "BUILDER_PF_FEAR_POST_CA_WITH_SUPPORT_RECOVERY_NO_CONFIRMED_SOLVENCY_BREAK", "evidence_source": "source_proxy_manual_verification_required:SHINSEGAE_CONSTRUCTION_2024_PF_SUPPORT_POST_CA_ORDERBOOK_CAPITAL_BUFFER_NO_HARD4C", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE", "post_peak_drawdown", "sharecount_or_CA_validation"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.73, "MFE_90D_pct": 23.78, "MFE_180D_pct": 62.16, "MAE_30D_pct": -6.37, "MAE_90D_pct": -7.96, "MAE_180D_pct": -7.96, "peak_date": "2024-09-30", "peak_price": 18340.0, "drawdown_after_peak_pct": -1.42, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_post_ca_no_hard4c", "current_profile_verdict": "C30 should not convert every PF fear or construction liquidity story into hard 4C when post-CA price action recovers and stabilizes. Shinsegae Construction requires post-corporate-action validation, but the post-CA window is a no-hard-4C boundary unless non-price solvency/refinancing break is confirmed.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validated_window_required", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_034300_2024-02-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C", "case_id": "R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C", "symbol": "035890", "company_name": "서희건설", "round": "R10", "loop": "76", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "RiskWatch-OrderbookBufferBoundedMAENoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1278.0, "evidence_available_at_that_date": "REGIONAL_BUILDER_PF_FEAR_WITH_BOUNDED_MAE_RECOVERY_ORDERBOOK_BUFFER", "evidence_source": "source_proxy_manual_verification_required:SEOHEE_CONSTRUCTION_2024_PF_ORDERBOOK_BUFFER_BOUND_MAE_NO_HARD4C", "stage2_evidence_fields": ["PF_or_financing_fear", "orderbook_or_capital_buffer_watch", "recovery_or_bounded_MAE_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["PF_financing_or_liquidity_risk", "high_MAE", "post_peak_drawdown", "sharecount_or_CA_validation"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv", "profile_path": "atlas/symbol_profiles/035/035890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.05, "MFE_90D_pct": 7.67, "MFE_180D_pct": 26.84, "MAE_30D_pct": -3.76, "MAE_90D_pct": -3.76, "MAE_180D_pct": -6.89, "peak_date": "2024-10-10", "peak_price": 1621.0, "drawdown_after_peak_pct": -13.76, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_impairment_or_solvency_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_impairment_covenant_or_solvency_break", "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "current_profile_verdict": "C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Seohee Construction showed a low-MAE recovery path; without non-price PF/refinancing or solvency break it should remain RiskWatch/no-hard-4C.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validated_window_required", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BOUNDARY_035890_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B", "trigger_id": "TRG_R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B", "symbol": "001470", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 17, "refinancing_break_score": 3, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 3, "relative_strength_score": 2, "execution_risk_score": 18, "sharecount_or_CA_validation_risk": 10, "information_confidence": 2}, "weighted_score_before": 34, "stage_label_before": "Stage4B-local-watch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 18, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 2, "relative_strength_score": 1, "execution_risk_score": 20, "sharecount_or_CA_validation_risk": 12, "information_confidence": 2}, "weighted_score_after": 30, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/financing risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 32.95, "MAE_90D_pct": -29.93, "score_return_alignment_label": "local4b_risk_alignment", "current_profile_verdict": "C30 should flag local 4B when a builder/financing-risk row produces a high-MFE but then opens severe MAE and post-peak drawdown. Sambu Construction had a tradable spike but later collapsed; however hard 4C still requires non-price default, refinancing, auditor/control, impairment, covenant or solvency evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C", "trigger_id": "TRG_R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C", "symbol": "034300", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 7, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 13, "relative_strength_score": 7, "execution_risk_score": 7, "sharecount_or_CA_validation_risk": 10, "information_confidence": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 6, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "relative_strength_score": 7, "execution_risk_score": 6, "sharecount_or_CA_validation_risk": 12, "information_confidence": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/financing risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 23.78, "MAE_90D_pct": -7.96, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should not convert every PF fear or construction liquidity story into hard 4C when post-CA price action recovers and stabilizes. Shinsegae Construction requires post-corporate-action validation, but the post-CA window is a no-hard-4C boundary unless non-price solvency/refinancing break is confirmed."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C", "trigger_id": "TRG_R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C", "symbol": "035890", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 7, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 13, "relative_strength_score": 7, "execution_risk_score": 7, "sharecount_or_CA_validation_risk": 0, "information_confidence": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 6, "refinancing_break_score": 1, "default_or_control_break_score": 0, "capital_or_orderbook_buffer_score": 14, "relative_strength_score": 7, "execution_risk_score": 6, "sharecount_or_CA_validation_risk": 0, "information_confidence": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["pf_liquidity_risk", "capital_or_orderbook_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "Escalate local 4B when high MAE/post-peak drawdown aligns with PF/financing risk; block hard 4C without explicit default, refinancing, impairment, covenant, auditor/control or solvency break.", "MFE_90D_pct": 7.67, "MAE_90D_pct": -3.76, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should keep PF/orderbook RiskWatch active for builders, but bounded MAE and recovery rows should not be escalated into hard 4C. Seohee Construction showed a low-MAE recovery path; without non-price PF/refinancing or solvency break it should remain RiskWatch/no-hard-4C."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 76, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 1, "overbearish_counterexample_count": 2, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "post_corporate_action_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C30 builders outside top-covered PF set and outside loop-75 R10 names, +3 financing-risk/post-CA-support/orderbook-buffer trigger families, +1 local-4B high-MAE risk path, +2 no-hard-4C buffer boundaries, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_sharecount_and_post_CA_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 76, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "builder_pf_financing_risk_local4b_vs_buffered_support_no_hard4c", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should split high-MAE builder/PF/financing local 4B from buffered support or orderbook no-hard-4C boundaries. MAE deterioration and post-peak drawdown can trigger local 4B-watch, but full 4B or hard 4C requires non-price default, refinancing failure, court rehabilitation, auditor/control break, impairment, covenant or solvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["001470", "034300", "035890"], "share_count_validation_required": ["001470"], "post_corporate_action_validation_required": ["034300"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 76, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "overbearish_no_hard4c_guard", "share_count_validation_guard", "corporate_action_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 needs severity splitting. Sambu Construction shows a high-MAE builder financing-risk local 4B path; Shinsegae Construction and Seohee Construction show buffered or recovery RiskWatch/no-hard-4C boundaries where price action alone should not become balance-sheet break."}
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
001470:
  corporate_action_candidate_dates = 1996-01-03, 2016-05-13, 2016-12-23, 2017-10-31, 2018-09-18, 2019-05-02
  selected window = 2024-02-13~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

034300:
  corporate_action_candidate_dates = 1999-11-16, 2024-02-06
  selected window starts 2024-02-07 after 2024-02-06 candidate
  contamination = false after post-CA entry, but coding-agent validation required

035890:
  corporate_action_candidate_dates = 2000-10-23, 2000-11-07, 2003-12-10, 2004-11-19, 2005-05-17, 2006-02-17, 2007-07-19, 2012-01-06, 2012-07-12
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
001470 requires share-count validation.
034300 requires post-corporate-action validation.
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
This R10/C30 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair, 001470 needs share-count validation, and 034300 needs post-CA validation.

Candidate axis:
builder_pf_financing_risk_local4b_vs_buffered_support_no_hard4c

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 001470, 034300 and 035890.
4. Validate 001470 share-count changes inside the selected window.
5. Validate 034300 post-CA continuity after the 2024-02-06 corporate-action candidate.
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
8. Keep RiskWatch/no-hard-4C when:
   - recovery or bounded MAE exists,
   - orderbook/capital/group/support buffer may be credible,
   - price drawdown exists but non-price break is not confirmed.
9. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 76
next_round = R11
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

