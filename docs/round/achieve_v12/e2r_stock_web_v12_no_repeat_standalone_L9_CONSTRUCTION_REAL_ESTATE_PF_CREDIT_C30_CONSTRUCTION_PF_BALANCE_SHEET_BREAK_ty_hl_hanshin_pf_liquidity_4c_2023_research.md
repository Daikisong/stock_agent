# E2R V12 No-Repeat Standalone Residual Research
## R11 / L9 / C30 — Construction PF balance-sheet break / TY-HL-Hanshin 4B·4C guard

metadata:
```text
selected_round: R11
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L9_CONSTRUCTION_REAL_ESTATE_PF_CREDIT
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: TY_HL_HANSHIN_PF_LIQUIDITY_BALANCE_SHEET_4C_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_4C_gap_fill|PF_liquidity_to_balance_sheet_repair_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L9_CONSTRUCTION_REAL_ESTATE_PF_CREDIT_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_ty_hl_hanshin_pf_liquidity_4c_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK current coverage:
rows=28, symbols=6, date range=2022-01-12~2024-08-27, good/bad S2=5/0, 4B/4C=0/4
top covered symbols: 006360(6), 294870(5), 375500(4), UNKNOWN_SYMBOL(3), 000720(2)
```

This run avoids those top-covered C30 symbols and adds 009410, 014790, and 004960.  
Each row uses a new `C30 + symbol + trigger_type + entry_date` hard key:
```text
C30 + 009410 + 4C-watch + 2023-12-13
C30 + 014790 + Stage3-Yellow + 2023-09-25
C30 + 004960 + 4B-local-price-only + 2023-09-15
```

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
active_like_symbol_count: 2868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
009410 태영건설: selected 2023/2024 event window has trading-halt/workout caveat; historical corporate-action candidates are outside selected trigger window.
014790 HL D&I: selected 2023/2024 forward window clean against historical corporate-action candidates; one suspicious OHLC repair candidate in profile is outside selected trigger logic.
004960 한신공영: selected 2023/2024 forward window clean; historical corporate-action candidates are before selected trigger window.
```

## 3. Research thesis

C30 should distinguish true balance-sheet repair from local price rebound inside a construction PF credit event:

```text
construction PF / balance-sheet stress
→ project exposure and impairment clarity
→ debt maturity extension and creditor/workout finality
→ cash-flow coverage and backlog cash conversion
→ capital-structure repair
→ margin/revision bridge
→ Stage2/Green or local 4B / 4C-watch
```

A PF crisis is not a normal price dip; it is a frozen funding pipe. Stage2 can only buy when the pipe is thawing—creditors, maturities, impairments and cash conversion are visible. A bounce without those repairs is just steam above the ice.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C30_009410_TAEYOUNG_20231213_PF_LIQUIDITY_BREAK_4C_WATCH | 009410 | protective_PF_liquidity_break_4C_watch_success_with_event_gap_caveat | 2023-12-13 | 3270 | 4110 on 2024-01-11 | 1935 on 2023-12-28 | 25.69% | 25.69% | 25.69% | -40.83% | -46.96% |
| C30_014790_HLDNI_20230925_PF_BALANCE_SHEET_YELLOW_FALSE_GREEN | 014790 | PF_balance_sheet_yellow_false_green_counterexample | 2023-09-25 | 2275 | 2310 on 2023-09-25 | 1946 on 2024-04-15 | 1.54% | 1.54% | 1.54% | -14.46% | -15.76% |
| C30_004960_HANSHIN_20230915_PF_CREDIT_PRICE_PREMIUM_4B | 004960 | PF_credit_price_premium_local_4B_counterexample | 2023-09-15 | 7770 | 7800 on 2023-09-22 | 6160 on 2024-04-17 | 0.39% | 0.39% | 0.39% | -20.72% | -21.03% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C30 Green should require PF exposure clarity, debt rollover or workout finality, project impairment sizing, backlog cash conversion, capital-structure repair and margin/revision confirmation.
- 014790 is the false-Green/Yellow guard: balance-sheet/PF risk had not been repaired, and the price path offered almost no residual upside before further drawdown.
- 004960 is the local 4B guard: price firmness did not equal balance-sheet repair or cash-flow coverage.

### 4B
- 004960 fills the construction PF credit price-premium 4B pocket. The move had nearly flat MFE and larger forward drawdown.
- 014790 shows that even subdued price confirmation should not be upgraded without debt maturity, project impairment and cash conversion proof.
- The core 4B rule is that construction credit rebounds should not substitute for balance-sheet repair.

### 4C
- 009410 is the protective 4C-watch anchor. It has an event-gap/trading-halt caveat, but that caveat is the point: the trigger path was not clean momentum but PF liquidity/workout event risk.
- Hard 4C should require PF liquidity break, workout/creditor uncertainty, covenant/debt rollover failure, project impairment shock or capital-structure break. Absent hard failure, use local 4B/Yellow rather than Green.

## 6. Raw component score breakdown

```json
{
  "C30_004960_HANSHIN_20230915_PF_CREDIT_PRICE_PREMIUM_4B": {
    "PF_liquidity_break_salience": 6,
    "capital_structure_repair": 2,
    "cashflow_coverage_quality": 2,
    "creditor_workout_or_covenant_risk": 5,
    "debt_rollover_visibility": 2,
    "information_confidence": 3,
    "market_mispricing": 3,
    "project_impairment_visibility": 4,
    "total": 28,
    "valuation_rerating_runway": 1
  },
  "C30_009410_TAEYOUNG_20231213_PF_LIQUIDITY_BREAK_4C_WATCH": {
    "PF_liquidity_break_salience": 12,
    "capital_structure_repair": 2,
    "cashflow_coverage_quality": 2,
    "creditor_workout_or_covenant_risk": 11,
    "debt_rollover_visibility": 2,
    "information_confidence": 4,
    "market_mispricing": 2,
    "project_impairment_visibility": 8,
    "total": 43,
    "valuation_rerating_runway": 0
  },
  "C30_014790_HLDNI_20230925_PF_BALANCE_SHEET_YELLOW_FALSE_GREEN": {
    "PF_liquidity_break_salience": 7,
    "capital_structure_repair": 2,
    "cashflow_coverage_quality": 2,
    "creditor_workout_or_covenant_risk": 6,
    "debt_rollover_visibility": 2,
    "information_confidence": 3,
    "market_mispricing": 3,
    "project_impairment_visibility": 5,
    "total": 31,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C30 guard:
```text
if construction_PF_price_rebound and no debt_rollover_creditor_project_impairment_cashflow_repair:
    block_stage2_green_positive = true
    route_to_stage3_yellow_or_local_4B = true

if PF_liquidity_break or workout_event_gap:
    route_to_4C_watch = true
    add_event_gap_caveat = true

if balance_sheet_repair_cash_conversion_margin_revision_visible:
    allow_stage2_actionable = true
```

Residual errors:
```text
current_profile_error_count = 2
- 014790 / 2023-09-25: PF/balance-sheet confirmation can be over-promoted if price stability substitutes for debt rollover and cash-flow repair.
- 004960 / 2023-09-15: construction PF credit premium can look like recovery, but fails without balance-sheet repair and margin/cash conversion proof.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -40.83, "MAE_30D_pct": -40.83, "MAE_90D_pct": -40.83, "MFE_180D_pct": 25.69, "MFE_30D_pct": 25.69, "MFE_90D_pct": 25.69, "calibration_caveat": "event_gap_trading_halt_workout_caveat; use as 4C-watch evidence not clean continuous 180D calibration", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": false, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_009410_TAEYOUNG_20231213_PF_LIQUIDITY_BREAK_4C_WATCH", "case_role": "protective_PF_liquidity_break_4C_watch_success_with_event_gap_caveat", "company_name": "태영건설", "corporate_action_window_status": "selected 2023/2024 event window caveated by trading-halt/gap; historical corporate-action candidates are outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "4C-watch routing was useful: the trigger was not a normal value-rebound setup but a PF liquidity/workout event-risk path. The stock had tradable rebounds, yet the immediate MAE and event-gap/trading-halt structure mean price strength should not be promoted to Stage2/Green without creditor agreement finality, debt rollover visibility, project impairment sizing, cash-flow coverage and capital-structure repair evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.96, "entry_date": "2023-12-13", "entry_price": 3270, "evidence_family": "construction_PF_liquidity_crisis_workout_creditor_support_event_risk_4C_watch", "evidence_url_pending": false, "fine_archetype_id": "TY_HL_HANSHIN_PF_LIQUIDITY_BALANCE_SHEET_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REAL_ESTATE_PF_CREDIT", "low_date_180d": "2023-12-28", "low_price_180d": 1935, "peak_date": "2024-01-11", "peak_price": 4110, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009410.json", "raw_component_score_breakdown": {"PF_liquidity_break_salience": 12, "capital_structure_repair": 2, "cashflow_coverage_quality": 2, "creditor_workout_or_covenant_risk": 11, "debt_rollover_visibility": 2, "information_confidence": 4, "market_mispricing": 2, "project_impairment_visibility": 8, "total": 43, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C30_009410_TAEYOUNG_20231213_PF_LIQUIDITY_BREAK_4C_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["PF_risk_absence_or_repair_required_for_positive", "debt_rollover_and_creditor_visibility_required", "cashflow_coverage_margin_repair_route_required"], "stage3_evidence_fields": ["PF_exposure_and_project_impairment_clarity_required", "debt_maturity_extension_or_workout_finality_required", "cash_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["PF_credit_price_premium_or_rebound", "balance_sheet_repair_not_yet_visible", "local_rebound_vs_full_event_path_split"], "stage4c_evidence_fields": ["PF_liquidity_break", "creditor_workout_or_covenant_risk", "project_impairment_cashflow_capital_structure_break"], "symbol": "009410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv", "trigger_date": "2023-12-13", "trigger_type": "4C-watch", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -14.46, "MAE_30D_pct": -13.14, "MAE_90D_pct": -13.14, "MFE_180D_pct": 1.54, "MFE_30D_pct": 1.54, "MFE_90D_pct": 1.54, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_014790_HLDNI_20230925_PF_BALANCE_SHEET_YELLOW_FALSE_GREEN", "case_role": "PF_balance_sheet_yellow_false_green_counterexample", "company_name": "HL D&I", "corporate_action_window_status": "selected 2023/2024 forward window clean against historical corporate-action candidates; one suspicious OHLC repair candidate in profile is outside selected trigger logic", "current_profile_error": true, "current_profile_verdict": "PF/balance-sheet price confirmation should remain Yellow or local 4B when the stock lacks creditor-risk normalization, debt rollover proof, project impairment clarity, backlog cash-flow quality and margin/revision repair. The September 2023 trigger had almost no residual MFE and a larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -15.76, "entry_date": "2023-09-25", "entry_price": 2275, "evidence_family": "construction_PF_balance_sheet_price_confirmation_without_debt_rollover_cashflow_margin_repair", "evidence_url_pending": false, "fine_archetype_id": "TY_HL_HANSHIN_PF_LIQUIDITY_BALANCE_SHEET_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REAL_ESTATE_PF_CREDIT", "low_date_180d": "2024-04-15", "low_price_180d": 1946, "peak_date": "2023-09-25", "peak_price": 2310, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/014/014790.json", "raw_component_score_breakdown": {"PF_liquidity_break_salience": 7, "capital_structure_repair": 2, "cashflow_coverage_quality": 2, "creditor_workout_or_covenant_risk": 6, "debt_rollover_visibility": 2, "information_confidence": 3, "market_mispricing": 3, "project_impairment_visibility": 5, "total": 31, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C30_014790_HLDNI_20230925_PF_BALANCE_SHEET_YELLOW_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["PF_risk_absence_or_repair_required_for_positive", "debt_rollover_and_creditor_visibility_required", "cashflow_coverage_margin_repair_route_required"], "stage3_evidence_fields": ["PF_exposure_and_project_impairment_clarity_required", "debt_maturity_extension_or_workout_finality_required", "cash_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["PF_credit_price_premium_or_rebound", "balance_sheet_repair_not_yet_visible", "local_rebound_vs_full_event_path_split"], "stage4c_evidence_fields": ["PF_liquidity_break", "creditor_workout_or_covenant_risk", "project_impairment_cashflow_capital_structure_break"], "symbol": "014790", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014790/2023.csv", "trigger_date": "2023-09-25", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -20.72, "MAE_30D_pct": -10.94, "MAE_90D_pct": -10.94, "MFE_180D_pct": 0.39, "MFE_30D_pct": 0.39, "MFE_90D_pct": 0.39, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_004960_HANSHIN_20230915_PF_CREDIT_PRICE_PREMIUM_4B", "case_role": "PF_credit_price_premium_local_4B_counterexample", "company_name": "한신공영", "corporate_action_window_status": "selected 2023/2024 forward window clean; historical corporate-action candidates are before selected trigger window", "current_profile_error": true, "current_profile_verdict": "Construction PF/credit price premium should route to local 4B or counterexample when price strength is not backed by debt maturity extension, PF exposure reduction, project impairment visibility, backlog cash conversion and margin/revision repair. The September 2023 trigger had nearly flat residual MFE and materially larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -21.03, "entry_date": "2023-09-15", "entry_price": 7770, "evidence_family": "construction_PF_credit_price_premium_without_balance_sheet_repair_cashflow_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "TY_HL_HANSHIN_PF_LIQUIDITY_BALANCE_SHEET_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REAL_ESTATE_PF_CREDIT", "low_date_180d": "2024-04-17", "low_price_180d": 6160, "peak_date": "2023-09-22", "peak_price": 7800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/004/004960.json", "raw_component_score_breakdown": {"PF_liquidity_break_salience": 6, "capital_structure_repair": 2, "cashflow_coverage_quality": 2, "creditor_workout_or_covenant_risk": 5, "debt_rollover_visibility": 2, "information_confidence": 3, "market_mispricing": 3, "project_impairment_visibility": 4, "total": 28, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C30_004960_HANSHIN_20230915_PF_CREDIT_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["PF_risk_absence_or_repair_required_for_positive", "debt_rollover_and_creditor_visibility_required", "cashflow_coverage_margin_repair_route_required"], "stage3_evidence_fields": ["PF_exposure_and_project_impairment_clarity_required", "debt_maturity_extension_or_workout_finality_required", "cash_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["PF_credit_price_premium_or_rebound", "balance_sheet_repair_not_yet_visible", "local_rebound_vs_full_event_path_split"], "stage4c_evidence_fields": ["PF_liquidity_break", "creditor_workout_or_covenant_risk", "project_impairment_cashflow_capital_structure_break"], "symbol": "004960", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004960/2023.csv", "trigger_date": "2023-09-15", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 2,
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "caveated_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TY_HL_HANSHIN_PF_LIQUIDITY_BALANCE_SHEET_4C_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L9_CONSTRUCTION_REAL_ESTATE_PF_CREDIT",
  "loop_contribution_label": "construction_PF_balance_sheet_break_new_symbols_ty_hl_hanshin_4b_4c_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R11",
  "shadow_rule_candidate": "C30 construction PF rows should block Stage2/Green when PF liquidity, debt rollover, creditor/workout, project impairment and cash-flow coverage risks dominate; local rebounds should route to Yellow/local 4B or 4C-watch until balance-sheet repair and margin/cash conversion evidence is visible.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C30 + symbol + trigger_type + entry_date.
3. Treat 009410 as caveated because trading-halt/workout event gaps need separate event-risk handling.
4. Add C30-specific PF liquidity / debt rollover / creditor workout / project impairment / cash-flow coverage / capital-structure repair / margin-revision / 4B-4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C30_BLOCK_GREEN_WITHOUT_DEBT_ROLLOVER_CREDITOR_PROJECT_IMPAIRMENT_CASHFLOW_REPAIR
- C30_PF_CREDIT_PRICE_REBOUND_LOCAL_4B
- C30_PF_LIQUIDITY_BREAK_ROUTES_TO_4C_WATCH_WITH_EVENT_GAP_CAVEAT
- C30_GREEN_REQUIRES_BALANCE_SHEET_REPAIR_CASH_CONVERSION_MARGIN_REVISION

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R11/L9_CONSTRUCTION_REAL_ESTATE_PF_CREDIT/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

