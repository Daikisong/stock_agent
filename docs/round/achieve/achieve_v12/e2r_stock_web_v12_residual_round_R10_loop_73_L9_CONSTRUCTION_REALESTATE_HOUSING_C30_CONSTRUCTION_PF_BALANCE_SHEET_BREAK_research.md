# E2R Stock-Web v12 Residual Research — R10 Loop 73 / L9 / C30

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 73,
  "computed_next_round": "R11",
  "computed_next_loop": 73,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C",
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
```

## Round / scope resolution

Previous completed state in this interactive run: R9 / loop 73.

Therefore:

```text
scheduled_round = R10
scheduled_loop = 73
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 73
```

R10 was routed to C30 because R10 is the construction/PF balance-sheet break round.  
Loop 72 already used 삼부토건, 동부건설, 계룡건설. This file therefore uses a new set:

```text
034300 / 신세계건설
004960 / 한신공영
047040 / 대우건설
```

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat already shows C30 concentration in the larger repeated set.  
This file adds a recapitalization-buffer row, a local PF-risk row, and a large-builder no-hard-4C boundary row.

Data-quality note:

```text
All three rows are stock-web calibration usable as 2024 historical price paths.
All three rows are source_proxy_only=true / evidence_url_pending=true.
034300 has a 2024-02-06 corporate-action candidate and share-count change; this artifact uses 2024-02-07 entry but still requires coding-agent validation before runtime promotion.
```

## Research thesis

C30 is not “construction balance-sheet fear.”

The model needs severity splitting:

```text
PF/liquidity fear
→ local 4B-watch if MAE opens and MFE is weak
→ no-hard-4C if recapitalization, tender floor, orderbook or capital buffer exists
→ hard 4C only if default, refinancing failure, auditor/control break, impairment or insolvency evidence appears
```

A balance sheet is a dam.  
Cracks justify inspection.  
Water through the wall is local 4B.  
The dam breaking is 4C.  
A new concrete wall from the parent changes the classification.

---

## Case 1 — Overbearish counterexample with recap buffer: 034300 / 신세계건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is PF-liquidity stress, parent recapitalization, tender/de-listing or capital-buffer evidence.

```text
evidence_family = PF_LIQUIDITY_STRESS_PARENT_RECAPITALIZATION_TENDER_BUFFER
case_role = overbearish_counterexample_with_recapitalization_buffer
trigger_date = 2024-02-06
entry_date = 2024-02-07
entry_price = 11,310
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv`:

```text
2024-02-07,11310,11550,11200,11460
2024-04-26,10370,10720,9850,10450
2024-05-30,15540,18650,14100,14700
2024-08-05,12220,12580,11150,11420
2024-09-30,18300,18340,18150,18160
```

### Backtest

```text
MFE_30D  = +13.00%
MAE_30D  = -7.96%
MFE_90D  = +64.90%
MAE_90D  = -12.91%
MFE_180D = +64.90%
MAE_180D = -12.91%
peak_180 = 18,650 on 2024-05-30
trough_180 = 9,850 on 2024-04-26
peak_to_later_drawdown = -40.21%
```

### Interpretation

This is the C30 “do not overclassify” row.  
The PF stress was serious enough to watch, but the price path did not behave like a hard 4C collapse after the recapitalization candidate.

C30 should require the bridge:

```text
default / refinancing failure / auditor-control break / insolvency
```

before using hard 4C.

---

## Case 2 — Local 4B risk: 004960 / 한신공영

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is PF exposure, orderbook quality, regional housing exposure, margin pressure and liquidity evidence.

```text
evidence_family = PF_EXPOSURE_REGIONAL_HOUSING_ORDERBOOK_MARGIN_LIQUIDITY_RISK
case_role = risk_positive
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 7,370
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv`:

```text
2024-02-01,7370,7770,7370,7720
2024-02-02,7810,7810,7500,7630
2024-04-17,6280,6350,6160,6160
2024-07-30,7190,7560,6890,7340
2024-08-05,6970,6970,6160,6300
```

### Backtest

```text
MFE_30D  = +5.97%
MAE_30D  = -3.12%
MFE_90D  = +5.97%
MAE_90D  = -16.42%
MFE_180D = +5.97%
MAE_180D = -16.42%
peak_180 = 7,810 on 2024-02-02
trough_180 = 6,160 on 2024-04-17
peak_to_later_drawdown = -21.13%
```

### Interpretation

This is a local 4B-watch boundary, not hard 4C.  
The stock did not produce enough MFE to reward the risk, and MAE widened. But there is still no price-only reason to call a hard balance-sheet break.

The rule candidate is:

```text
PF/orderbook/margin risk + weak MFE + widening MAE = local 4B-watch
hard 4C = only after non-price break evidence
```

---

## Case 3 — Large-builder buffer / no full 4B: 047040 / 대우건설

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is large-builder PF fear, overseas/orderbook buffer and capital-buffer evidence.

```text
evidence_family = LARGE_BUILDER_PF_FEAR_WITH_OVERSEAS_ORDERBOOK_CAPITAL_BUFFER
case_role = overbearish_counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,910
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv`:

```text
2024-02-01,3910,4005,3905,3965
2024-03-14,3670,3785,3625,3730
2024-07-18,4865,4965,4220,4250
2024-08-05,3915,3945,3545,3640
```

### Backtest

```text
MFE_30D  = +5.37%
MAE_30D  = -7.29%
MFE_90D  = +5.37%
MAE_90D  = -7.29%
MFE_180D = +26.98%
MAE_180D = -9.34%
peak_180 = 4,965 on 2024-07-18
trough_180 = 3,545 on 2024-08-05
peak_to_later_drawdown = -28.60%
```

### Interpretation

This is a no-full-4B guardrail.  
PF fear existed at sector level, but the price path does not confirm a balance-sheet break. For larger builders, orderbook mix, overseas exposure, capital buffer or refinancing access must be considered before escalating.

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
do_not_ignore_recapitalization_or_tender_buffer = true
do_not_call_large_builder_risk_full_4B_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C
```

This fine archetype covers:

```text
1. PF-liquidity stress + parent recap/tender buffer → RiskWatch / no hard 4C
2. regional builder PF/orderbook/margin risk → local 4B-watch
3. large builder PF fear + orderbook/capital buffer → RiskWatch / no full 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "73", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-RiskWatch / RecapitalizationBufferNoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should not convert every PF-liquidity headline into hard 4C when parent recapitalization, tender/de-listing path, or capital buffer changes the equity path. The stock-web path had large MFE after the recapitalization candidate, so this is a no-hard-4C buffer row, not a hard break row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF/liquidity/refinancing/orderbook/capital-buffer evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "73", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-PFOrderbookMarginRisk", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 local 4B-watch should fire when PF/orderbook/margin risk prevents a durable MFE path, even if the stock does not show a hard 4C collapse. 한신공영 is a local-risk boundary row: MAE opens and MFE is small, but full 4B/4C still needs explicit non-price deterioration.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF/liquidity/refinancing/orderbook/capital-buffer evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "73", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "case_type": "construction_pf_balance_sheet_break", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-RiskWatch / LargeBuilderNoFull4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C30 should distinguish large-builder PF fear from a balance-sheet break. 대우건설 had bounded MAE and later tradable MFE, so it should remain RiskWatch/no-full-4B unless explicit impairment/refinancing/default evidence appears.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy PF/liquidity/refinancing/orderbook/capital-buffer evidence must be attached before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER", "case_id": "R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "73", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage2-RiskWatch / RecapitalizationBufferNoHard4C", "trigger_date": "2024-02-06", "entry_date": "2024-02-07", "entry_price": 11310.0, "evidence_available_at_that_date": "PF_LIQUIDITY_STRESS_PARENT_RECAPITALIZATION_TENDER_BUFFER", "evidence_source": "source_proxy_manual_verification_required:SHINSEGAE_CONSTRUCTION_2024_PF_LIQUIDITY_PARENT_RECAPITALIZATION_TENDER_BUFFER", "stage2_evidence_fields": ["pf_risk", "balance_sheet_watch", "capital_buffer_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_or_drawdown_watch", "pf_orderbook_or_liquidity_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.0, "MFE_90D_pct": 64.9, "MFE_180D_pct": 64.9, "MAE_30D_pct": -7.96, "MAE_90D_pct": -12.91, "MAE_180D_pct": -12.91, "peak_date": "2024-05-30", "peak_price": 18650.0, "drawdown_after_peak_pct": -40.21, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_or_impairment_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_break", "trigger_outcome_label": "overbearish_counterexample_with_recapitalization_buffer", "current_profile_verdict": "C30 should not convert every PF-liquidity headline into hard 4C when parent recapitalization, tender/de-listing path, or capital buffer changes the equity path. The stock-web path had large MFE after the recapitalization candidate, so this is a no-hard-4C buffer row, not a hard break row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C30_PF_BS_034300_2024-02-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B", "case_id": "R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "73", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage4B-Local-PFOrderbookMarginRisk", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7370.0, "evidence_available_at_that_date": "PF_EXPOSURE_REGIONAL_HOUSING_ORDERBOOK_MARGIN_LIQUIDITY_RISK", "evidence_source": "source_proxy_manual_verification_required:HANSHIN_CONSTRUCTION_2024_PF_ORDERBOOK_MARGIN_LIQUIDITY_RISK", "stage2_evidence_fields": ["pf_risk", "balance_sheet_watch", "capital_buffer_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_or_drawdown_watch", "pf_orderbook_or_liquidity_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv", "profile_path": "atlas/symbol_profiles/004/004960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.97, "MFE_90D_pct": 5.97, "MFE_180D_pct": 5.97, "MAE_30D_pct": -3.12, "MAE_90D_pct": -16.42, "MAE_180D_pct": -16.42, "peak_date": "2024-02-02", "peak_price": 7810.0, "drawdown_after_peak_pct": -21.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_or_impairment_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_break", "trigger_outcome_label": "risk_positive", "current_profile_verdict": "C30 local 4B-watch should fire when PF/orderbook/margin risk prevents a durable MFE path, even if the stock does not show a hard 4C collapse. 한신공영 is a local-risk boundary row: MAE opens and MFE is small, but full 4B/4C still needs explicit non-price deterioration.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BS_004960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B", "case_id": "R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": "73", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "loop_objective": "coverage_gap_fill|4B_non_price_requirement_stress_test|4C_balance_sheet_break_guard", "trigger_type": "Stage2-RiskWatch / LargeBuilderNoFull4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3910.0, "evidence_available_at_that_date": "LARGE_BUILDER_PF_FEAR_WITH_OVERSEAS_ORDERBOOK_CAPITAL_BUFFER", "evidence_source": "source_proxy_manual_verification_required:DAEWOO_EC_2024_LARGE_BUILDER_PF_FEAR_OVERSEAS_ORDERBOOK_CAPITAL_BUFFER", "stage2_evidence_fields": ["pf_risk", "balance_sheet_watch", "capital_buffer_candidate"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_or_drawdown_watch", "pf_orderbook_or_liquidity_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.37, "MFE_90D_pct": 5.37, "MFE_180D_pct": 26.98, "MAE_30D_pct": -7.29, "MAE_90D_pct": -7.29, "MAE_180D_pct": -9.34, "peak_date": "2024-07-18", "peak_price": 4965.0, "drawdown_after_peak_pct": -28.6, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_only_unless_refinancing_or_impairment_break", "four_b_full_window_peak_proximity": "full_4b_or_4c_requires_non_price_default_refinancing_control_break", "trigger_outcome_label": "overbearish_counterexample", "current_profile_verdict": "C30 should distinguish large-builder PF fear from a balance-sheet break. 대우건설 had bounded MAE and later tradable MFE, so it should remain RiskWatch/no-full-4B unless explicit impairment/refinancing/default evidence appears.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C30_PF_BS_047040_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER", "trigger_id": "TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER", "symbol": "034300", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 10, "refinancing_break_score": 3, "default_or_control_break_score": 0, "capital_buffer_score": 10, "orderbook_buffer_score": 4, "relative_strength_score": 8, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 52, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 8, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_buffer_score": 12, "orderbook_buffer_score": 4, "relative_strength_score": 7, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 55, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["capital_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "C30 hard 4C is blocked without explicit default/refinancing/control break; capital-buffer or recapitalization evidence should keep cases in RiskWatch/no-full-4B.", "MFE_90D_pct": 64.9, "MAE_90D_pct": -12.91, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should not convert every PF-liquidity headline into hard 4C when parent recapitalization, tender/de-listing path, or capital buffer changes the equity path. The stock-web path had large MFE after the recapitalization candidate, so this is a no-hard-4C buffer row, not a hard break row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B", "trigger_id": "TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B", "symbol": "004960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 14, "refinancing_break_score": 3, "default_or_control_break_score": 0, "capital_buffer_score": 4, "orderbook_buffer_score": 4, "relative_strength_score": 4, "execution_risk_score": 12, "information_confidence": 2}, "weighted_score_before": 48, "stage_label_before": "Stage4B-local-watch", "raw_component_scores_after": {"pf_liquidity_risk": 14, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_buffer_score": 3, "orderbook_buffer_score": 4, "relative_strength_score": 3, "execution_risk_score": 13, "information_confidence": 2}, "weighted_score_after": 44, "stage_label_after": "Stage4B-local-watch / no hard 4C", "changed_components": ["capital_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "C30 hard 4C is blocked without explicit default/refinancing/control break; capital-buffer or recapitalization evidence should keep cases in RiskWatch/no-full-4B.", "MFE_90D_pct": 5.97, "MAE_90D_pct": -16.42, "score_return_alignment_label": "risk_positive_alignment", "current_profile_verdict": "C30 local 4B-watch should fire when PF/orderbook/margin risk prevents a durable MFE path, even if the stock does not show a hard 4C collapse. 한신공영 is a local-risk boundary row: MAE opens and MFE is small, but full 4B/4C still needs explicit non-price deterioration."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B", "trigger_id": "TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B", "symbol": "047040", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"pf_liquidity_risk": 10, "refinancing_break_score": 3, "default_or_control_break_score": 0, "capital_buffer_score": 10, "orderbook_buffer_score": 8, "relative_strength_score": 8, "execution_risk_score": 8, "information_confidence": 2}, "weighted_score_before": 52, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"pf_liquidity_risk": 8, "refinancing_break_score": 2, "default_or_control_break_score": 0, "capital_buffer_score": 12, "orderbook_buffer_score": 10, "relative_strength_score": 7, "execution_risk_score": 7, "information_confidence": 2}, "weighted_score_after": 55, "stage_label_after": "RiskWatch / overbearish no-hard-4C guard", "changed_components": ["capital_buffer_score", "refinancing_break_score", "default_or_control_break_score", "execution_risk_score"], "component_delta_explanation": "C30 hard 4C is blocked without explicit default/refinancing/control break; capital-buffer or recapitalization evidence should keep cases in RiskWatch/no-full-4B.", "MFE_90D_pct": 5.37, "MAE_90D_pct": -7.29, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C30 should distinguish large-builder PF fear from a balance-sheet break. 대우건설 had bounded MAE and later tradable MFE, so it should remain RiskWatch/no-full-4B unless explicit impairment/refinancing/default evidence appears."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R10", "loop": 73, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "risk_positive_case_count": 1, "overbearish_counterexample_count": 2, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C30 symbols, +3 PF/recap/orderbook trigger families, +1 local-4B risk path, +2 overbearish no-hard-4C buffer paths, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": 73, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "axis": "pf_liquidity_stress_recapitalization_buffer_vs_local_riskwatch_no_hard4c", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C30 should separate PF-liquidity fear, local 4B risk and hard 4C break. Parent recapitalization, tender/de-listing floor, orderbook or large-builder capital buffer should prevent hard 4C. Local 4B can fire on PF/orderbook/margin risk with weak MFE or widening MAE. Full 4B/4C requires non-price default, refinancing failure, auditor/control break, impairment or insolvency evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["034300", "004960", "047040"], "share_count_validation_required": ["034300"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": 73, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "existing_axis_strengthened": ["hard_4c_confirmation", "local_4b_watch_guard", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C30 needs severity splitting. Shinsegae Construction shows recapitalization/tender-buffer no-hard-4C, Hanshin shows local PF risk without hard break, and Daewoo E&C shows large-builder orderbook/capital buffer. Hard 4C remains non-price evidence based."}
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
034300:
  corporate_action_candidate_dates = 1999-11-16, 2024-02-06
  selected window = 2024-02-07~D+180
  contamination = false after the 2024-02-06 candidate, but share-count validation is required
  status_inferred = inactive_or_delisted_like

004960:
  corporate_action_candidate_dates = 1998-09-19, 2001-06-20, 2002-04-03, 2002-05-24, 2002-11-14
  selected window = 2024-02-01~D+180
  contamination = false

047040:
  corporate_action_candidate_dates = 2001-07-13, 2003-11-18, 2011-01-18
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C30 rows are source_proxy_only / evidence_url_pending.
034300 also requires share-count and tender/de-listing validation.
This MD is useful for stock-web path calibration and C30 rule-shape discovery,
but coding-agent promotion requires non-proxy PF/refinancing/capital-buffer evidence.
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
pf_liquidity_stress_recapitalization_buffer_vs_local_riskwatch_no_hard4c

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 034300, 004960 and 047040.
4. Validate 034300 share-count change, recapitalization and tender/de-listing basis.
5. Keep hard 4C evidence-based:
   - default,
   - court rehabilitation,
   - refinancing failure,
   - auditor/control break,
   - covenant or insolvency signal.
6. Use local 4B-watch when:
   - PF/liquidity/orderbook/margin risk is present,
   - MFE remains small or temporary,
   - MAE widens,
   - but hard-break evidence is not confirmed.
7. Keep RiskWatch/no-full-4B when:
   - recapitalization, tender floor, parent support, orderbook or capital buffer is credible,
   - price drawdown exists but non-price break is not confirmed.
8. Emit before/after diagnostics and reject if C30 overblocks buffered builders or underflags true hard-break cases.
```

---

## Final round state

```text
completed_round = R10
completed_loop = 73
next_round = R11
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

