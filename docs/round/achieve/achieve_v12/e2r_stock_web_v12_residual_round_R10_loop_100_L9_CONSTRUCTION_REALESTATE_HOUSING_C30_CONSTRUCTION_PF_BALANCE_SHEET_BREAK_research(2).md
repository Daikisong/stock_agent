# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R10
selected_loop: 100
round_schedule_status: coverage_index_selected
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: mixed_C30_construction_pf_balance_sheet_break_set
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_filename: e2r_stock_web_v12_residual_round_R10_loop_100_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_code_patch_included: false
production_scoring_patch_applied: false
```

This round is a C30 residual calibration pass for construction / PF / balance-sheet break cases. The No-Repeat ledger shows C30 as under-covered, and prior C30 representative symbols are avoided. The case set deliberately leans counterexample-heavy because this archetype is a drawdown / trust-break guardrail: the rule must separate a genuine balance-sheet repair from a verbal PF-risk rebuttal or a hard construction-quality 4C event.

## 1. Current Calibrated Profile Assumption

Assumed active profile: `e2r_2_2_rolling_calibrated` / active selector `e2r_2_2`.

Relevant active guardrails assumed during stress test:

- `hard_4c_thesis_break_routes_to_4c`
- `full_4b_requires_non_price_evidence`
- `price_only_blowoff_blocks_positive_stage`
- `archetype_classification_required`
- `archetype_large_sector_fallback_allowed: false`

No production profile is changed in this document. All scoring deltas are shadow-candidate rows only.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| selected_round | R10 |
| selected_loop | 100 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| canonical focus | construction quality break, PF liability scale, liquidity rebuttal, balance-sheet strength, credit/funding trust |
| excluded scope | live recommendation, stock_agent code patch, production scoring change, non-C30 sector proxy |

Round consistency check: R10 maps to L9 / C30. The selected file name follows the standard long V12 result filename and does not use compact filename form.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat ledger state used only as a duplicate and coverage ledger:

| Check | Result |
|---|---|
| existing C30 rows | 3 |
| existing C30 symbols | 3 |
| existing C30 top covered symbols | 009410, 034300, 183190 |
| selected symbols in this round | 006360, 294870, 005960, 035890, 002990 |
| hard duplicate key repeated? | false |
| expected C30 rows after acceptance | 8 |

Hard duplicate key checked: `canonical_archetype_id + symbol + trigger_type + entry_date`.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web source: `Songdaiki/stock-web`, tradable shard root `atlas/ohlcv_tradable_by_symbol_year`.

Price methodology:

- Entry price uses stock-web close on the selected entry row.
- If public evidence timing is not guaranteed to be intraday actionable, entry is next tradable row.
- MFE/MAE is calculated from entry row through N tradable rows using high/low path.
- Corporate-action contamination screen: 180D window checked for large shares-outstanding jumps and extreme close-price ratio discontinuities; none found for selected rows.

## 5. Historical Eligibility Gate

| Gate | Status |
|---|---|
| evidence date precedes or equals entry date | pass |
| entry date exists in tradable shard | pass |
| 180 forward tradable rows available | pass for all 5 rows |
| MFE/MAE 30D/90D/180D complete | pass |
| corporate-action contamination candidate | none detected |
| source_proxy_only row | 0 |
| future data leakage detected | false |

## 6. Canonical Archetype Compression Map

| Fine / deep sub-archetype | Canonical compression | Mechanism |
|---|---|---|
| C30_CONSTRUCTION_QUALITY_REBUILD_COST_TRUST_BREAK | C30 | full rebuild cost and trust break should route to 4C, not bargain-stage rebound |
| C30_FULL_DEMOLITION_REBUILD_BALANCE_SHEET_TRUST_BREAK | C30 | demolition/rebuild decision converts accident into balance-sheet and reputation break |
| C30_PF_LIQUIDITY_REBUTTAL_WITH_UNRESOLVED_MARKET_DISCOUNT | C30 | liquidity rebuttal alone is not a positive rerating without cash-flow/funding confirmation |
| C30_NEGATIVE_NET_DEBT_PF_CONTROLLED_REBOUND | C30 | true balance-sheet strength can produce positive rerating inside distressed sector |
| C30_PF_CONTINGENT_LIABILITY_EQUITY_COVERAGE_GUARD | C30 | PF liability near equity plus profit collapse should activate 4B/high-MAE guard |

## 7. Case Selection Summary

| trigger_id | symbol | name | role | trigger_type | fine_archetype_id | entry_date | MFE_180D | MAE_180D |
|---|---:|---|---|---|---|---|---:|---:|
| C30-100-001 | 006360 | GS건설 | counterexample | Stage4C | C30_CONSTRUCTION_QUALITY_REBUILD_COST_TRUST_BREAK | 2023-07-06 | 19.83% | -12.74% |
| C30-100-002 | 294870 | HDC현대산업개발 | counterexample | Stage4C | C30_FULL_DEMOLITION_REBUILD_BALANCE_SHEET_TRUST_BREAK | 2022-05-06 | 1.99% | -38.48% |
| C30-100-003 | 005960 | 동부건설 | counterexample | Stage2-RedWatch | C30_PF_LIQUIDITY_REBUTTAL_WITH_UNRESOLVED_MARKET_DISCOUNT | 2024-01-08 | 1.60% | -25.58% |
| C30-100-004 | 035890 | 서희건설 | positive | Stage2-Actionable | C30_NEGATIVE_NET_DEBT_PF_CONTROLLED_REBOUND | 2024-06-24 | 27.37% | -9.78% |
| C30-100-005 | 002990 | 금호건설 | counterexample | Stage4B | C30_PF_CONTINGENT_LIABILITY_EQUITY_COVERAGE_GUARD | 2024-03-13 | 1.66% | -44.28% |

Diversity summary: 5 new symbols / 5 fine trigger families / positive 1 + counterexample 4 + 4B 1 + 4C 2.

## 8. Positive vs Counterexample Balance

| Bucket | Count | Notes |
|---|---:|---|
| positive | 1 | 서희건설: verified balance-sheet strength with 90D/180D MFE |
| counterexample | 4 | GS건설, HDC현대산업개발, 동부건설, 금호건설 |
| 4B | 1 | 금호건설: liability scale / profit collapse blocks positive stage |
| 4C | 2 | GS건설, HDC현대산업개발: rebuild/trust-break events |
| calibration_usable | 5 | all rows include complete 30D/90D/180D MFE/MAE |

C30 is intentionally red-risk heavy. A balanced 2/2 sample would under-sample the actual failure surface of PF/liability/trust-break archetypes. The minimum positive requirement is satisfied by the balance-sheet-strength case; the residual value of this round is mainly 4B/4C protection.

## 9. Evidence Source Map

| trigger_id | source basis | evidence date | entry date policy |
|---|---|---|---|
| C30-100-001 | The Bell / Yonhap coverage of GS건설 Geomdan full rebuild and cost burden | 2023-07-05~07 | next tradable row used: 2023-07-06 |
| C30-100-002 | Yonhap coverage of HDC현대산업개발 Hwa-jeong full demolition/rebuild and expected cost | 2022-05-04 | 2022-05-05 holiday, next tradable row used: 2022-05-06 |
| C30-100-003 | CEOscoreDaily coverage of 동부건설 liquidity/PF-risk rebuttal | 2024-01-05 | next tradable row used: 2024-01-08 |
| C30-100-004 | KIS Rating report on 서희건설 leverage, negative net debt, and cash exceeding borrowings | 2024-06-21 | next tradable row used: 2024-06-24 |
| C30-100-005 | IB Tomato coverage of 금호건설 profit collapse and PF contingent liability scale | 2024-03-12 | next tradable row used: 2024-03-13 |

## 10. Price Data Source Map

| symbol | shard paths |
|---:|---|
| 006360 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv; atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv |
| 294870 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv; atlas/ohlcv_tradable_by_symbol_year/294/294870/2023.csv |
| 005960 | atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv; atlas/ohlcv_tradable_by_symbol_year/005/005960/2025.csv |
| 035890 | atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv; atlas/ohlcv_tradable_by_symbol_year/035/035890/2025.csv |
| 002990 | atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv; atlas/ohlcv_tradable_by_symbol_year/002/002990/2025.csv |

## 11. Case-by-Case Trigger Grid

### C30-100-001 / 006360 / GS건설

- Trigger: full rebuild / cost burden / trust break after Geomdan incident.
- Compression: C30 hard trust-break 4C; a later rebound does not retroactively make the initial trigger positive.
- Profile stress: current hard 4C guardrail broadly works, but C30 should explicitly route full-rebuild construction-quality events to 4C.

### C30-100-002 / 294870 / HDC현대산업개발

- Trigger: Hwa-jeong I-Park full demolition and rebuild decision.
- Compression: rebuild decision creates a cost-and-trust thesis break; the forward path shows near-zero MFE and deep MAE.
- Profile stress: without an explicit `full_demolition_rebuild` gate, a low-PBR construction rebound model can be too slow to route 4C.

### C30-100-003 / 005960 / 동부건설

- Trigger: liquidity/PF-risk rebuttal.
- Compression: verbal liquidity defense is not enough for a positive stage when cash-flow and funding-market confirmation are missing.
- Profile stress: Stage2 should require post-rebuttal evidence of funding access or cash-flow stabilization.

### C30-100-004 / 035890 / 서희건설

- Trigger: rating evidence of negative net debt, low leverage, and cash exceeding borrowings.
- Compression: this is the constructive C30 path: verified balance-sheet strength inside a distressed sector.
- Profile stress: if C30 is treated only as a red-risk archetype, genuine balance-sheet rerating is missed.

### C30-100-005 / 002990 / 금호건설

- Trigger: profit collapse with large PF contingent-liability scale despite verbal PF-risk management.
- Compression: non-price 4B should block positive stage before the full-window drawdown appears.
- Profile stress: PF exposure relative to equity and earnings collapse must override generic SOC/orderbook optimism.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C30-100-001 | 006360 | 2023-07-06 | 14520 | 10.12% | -7.92% | 10.12% | -12.74% | 19.83% | -12.74% | 28.24% | -12.74% |
| C30-100-002 | 294870 | 2022-05-06 | 15100 | 1.99% | -26.49% | 1.99% | -30.79% | 1.99% | -38.48% | 1.99% | -38.48% |
| C30-100-003 | 005960 | 2024-01-08 | 5610 | 1.60% | -7.31% | 1.60% | -14.53% | 1.60% | -25.58% | 1.60% | -36.36% |
| C30-100-004 | 035890 | 2024-06-24 | 1319 | 4.40% | -9.78% | 22.90% | -9.78% | 27.37% | -9.78% | 58.45% | -9.78% |
| C30-100-005 | 002990 | 2024-03-13 | 4810 | 1.66% | -15.38% | 1.66% | -24.22% | 1.66% | -44.28% | 1.66% | -52.08% |

## 13. Current Calibrated Profile Stress Test

| trigger_id | symbol | P0 active proxy | P1 C30 balance-sheet gate | P2 C30 4B/4C guard | P3 combined shadow | residual verdict |
|---|---:|---|---|---|---|---|
| C30-100-001 | 006360 | Stage4C / 49 | Stage3-Red / 41 | Stage4C / 20 | Stage4C / 18 | current_profile_correct_but_requires_c30_explicit_4c_route |
| C30-100-002 | 294870 | Stage3-Red / 49 | Stage3-Red / 41 | Stage4C / 20 | Stage4C / 18 | current_profile_4c_too_late_without_explicit_full_rebuild_gate |
| C30-100-003 | 005960 | Stage2 / 66 | Stage1/Watch / 55 | Stage3-Red / 50 | Stage3-Red / 48 | current_profile_false_positive_if_liquidity_rebuttal_gets_stage2_without_cashflow_confirmation |
| C30-100-004 | 035890 | Stage2 / 71 | Stage3-Yellow / 79 | Stage3-Yellow / 76 | Stage3-Yellow / 81 | current_profile_missed_structural_positive_if_c30_only_treated_as_pf_red_flag |
| C30-100-005 | 002990 | Stage2 / 64 | Stage3-Red / 45 | Stage4B / 32 | Stage4B / 30 | current_profile_false_positive_if_pf_risk_comment_overrides_profit_and_liability_scale |

Interpretation: P3 reduces false positive exposure in HDC/Dongbu/Kumho while preserving the Seohee positive. It treats GS/HDC as hard 4C if rebuild/trust break is public, and it treats verbal PF rebuttal as insufficient for positive staging unless cash-flow, funding access, and liability scale are also favorable.

## 14. Stage2 / Yellow / Green Comparison

| Stage | C30-specific requirement | Cases passing |
|---|---|---|
| Stage2 | public balance-sheet signal plus tradable price row; no hard 4C | 005960, 035890, 002990 |
| Stage3-Yellow | verified balance-sheet strength, cash above borrowings, low/declining leverage, acceptable MAE | 035890 only |
| Stage3-Green | repeated cash-flow visibility plus low red-team risk | none; this round does not claim Green |
| Stage4B | profit/cash-flow deterioration, PF liability scale, or funding discount blocks positive stage | 002990, soft watch for 005960 |
| Stage4C | full rebuild/demolition, trust break, contract/quality thesis break | 006360, 294870 |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | 4B/4C timing | price-path audit |
|---|---|---|
| C30-100-001 | 4C at trigger; later partial rebound allowed but not positive-stage evidence | MFE_180D 19.83%, MAE_180D -12.74%, post-peak drawdown -20.34% |
| C30-100-002 | 4C at trigger | MFE_180D 1.99%, MAE_180D -38.48%; peak effectively at entry |
| C30-100-003 | 4B/red-watch should activate after rebuttal fails to attract durable bid | MFE_180D 1.60%, MAE_180D -25.58% |
| C30-100-004 | no 4B; positive balance-sheet rerating | MFE_180D 27.37%, MAE_180D -9.78% |
| C30-100-005 | 4B at trigger | MFE_180D 1.66%, MAE_180D -44.28%; full-window peak at entry |

## 16. 4C Protection Audit

Hard 4C route should be explicit for:

- full reconstruction / full demolition decisions;
- construction-quality trust break with large future cost burden;
- business suspension / qualification / project execution block if present at the trigger date;
- PF or funding event that becomes a solvency or trust break rather than a liquidity rumor.

This round does not convert every weak PF case into 4C. Dongbu and Kumho are better treated as 4B/red-watch unless default, accounting, or legal trust-break evidence becomes public.

## 17. Sector-Specific Rule Candidate

`L9_C30_PF_DISTRESS_REBUTTAL_REQUIRES_CASHFLOW_AND_LIABILITY_SCALE`

Rule candidate:

```text
For L9/C30, a public PF-risk or liquidity rebuttal may open Stage2-RedWatch, but it must not graduate to Stage3-Yellow unless at least two of the following are present: cash exceeds short-term debt, net debt is negative or sharply falling, PF contingent liabilities are small versus equity, operating cash flow or margins stabilize, and rating/funding-market evidence confirms access. If profit collapses or PF contingent liabilities approach equity, route to 4B even if management states PF risk is manageable.
```

## 18. Canonical-Archetype Rule Candidate

`C30_BALANCE_SHEET_BREAK_AND_REBUILD_COST_GATE`

Candidate compression:

```text
C30 positive path = verified balance-sheet strength + low liability scale + funding confidence + acceptable MAE.
C30 4B path = verbal rebuttal without cash-flow confirmation, profit collapse, liability scale near equity, or funding-market discount.
C30 4C path = full rebuild/demolition, construction-quality trust break, legal/regulatory execution block, or hard solvency/trust break.
```

## 19. Before / After Backtest Comparison

| Profile | Positive preserved | False positives blocked | 4C routed early | Net effect |
|---|---:|---:|---:|---|
| P0 active proxy | partial | partial | partial | misses distinction between real balance-sheet strength and verbal rebuttal |
| P1 balance-sheet gate | yes | medium | low | improves Seohee/Dongbu split but not enough for HDC/GS |
| P2 4B/4C guard | partial | high | high | strong protection but may under-reward true balance-sheet positives |
| P3 combined shadow | yes | high | high | best fit for this sample |

## 20. Score-Return Alignment Matrix

| Bucket | Return signature | Correct stage behavior |
|---|---|---|
| verified balance-sheet strength | MFE_90D/180D > 20%, MAE around -10% | Stage2-Actionable → Yellow candidate |
| verbal PF rebuttal only | low MFE, worsening MAE | Stage2-RedWatch, no Yellow |
| liability near equity + profit collapse | MFE near zero, MAE worse than -40% | 4B guardrail |
| full rebuild / demolition trust break | high uncertainty; often large MAE or unstable rebound | hard 4C route |

## 21. Coverage Matrix

| Metric | Before | Added | Expected after acceptance |
|---|---:|---:|---:|
| C30 representative rows | 3 | 5 | 8 |
| C30 unique symbols | 3 | 5 | 8 |
| positive rows | 1 | 1 | 2 |
| counterexample rows | 2 | 4 | 6 |
| 4B rows | 0 | 1 | 1 |
| 4C rows | 0 | 2 | 2 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 1
counterexample_count: 4
current_profile_error_count: 4
diversity_score_summary: 5 new symbols / 5 fine trigger families / positive 1 + counterexample 4 + 4B 1 + 4C 2
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C30 rows 3 -> expected 8 after acceptance
sector_specific_rule_candidate: L9_C30_PF_DISTRESS_REBUTTAL_REQUIRES_CASHFLOW_AND_LIABILITY_SCALE
canonical_archetype_rule_candidate: C30_BALANCE_SHEET_BREAK_AND_REBUILD_COST_GATE
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C30_DISTRESS_REBUTTAL_EARNINGS_CASHFLOW_CONFIRMATION_GATE | C30_HARD_REBUILD_COST_TRUST_BREAK_4C_ROUTE | C30_NEGATIVE_NET_DEBT_BALANCE_SHEET_POSITIVE_GATE
existing_axis_strengthened: hard_4c_thesis_break_routes_to_4c | full_4b_requires_non_price_evidence | price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
```

## 23. Validation Scope / Non-Validation Scope

Validated in this document:

- historical public-evidence trigger date and next-tradable entry date logic;
- stock-web OHLC forward-path MFE/MAE for 30D/90D/180D;
- no duplicate against current C30 representative symbols;
- C30-specific stage behavior and shadow rule candidate.

Not validated in this document:

- live trading suitability;
- production code behavior;
- production scoring patch safety;
- full market universe scan;
- intraday reaction timing.

## 24. Shadow Weight Calibration

```csv
profile_id,large_sector_id,canonical_archetype_id,component,delta,reason
P3_c30_combined_shadow,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,information_confidence,+0.06,C30 needs explicit split between verified balance-sheet strength and verbal PF rebuttal
P3_c30_combined_shadow,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,capital_allocation,+0.04,negative-net-debt/cash-above-borrowings cases should be rewarded more than generic low-PBR
P3_c30_combined_shadow,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,earnings_visibility,+0.03,positive C30 requires cash-flow and margin confirmation
P3_c30_combined_shadow,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,market_mispricing,-0.04,cheapness alone frequently created high-MAE false positives
P3_c30_combined_shadow,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,valuation_rerating,-0.03,sector rebound should not override PF/liability/trust evidence
P3_c30_combined_shadow,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,hard_4c_route,+1,full rebuild/trust break should force 4C before valuation stage
P3_c30_combined_shadow,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,soft_4b_route,+1,PF liability near equity plus profit collapse should block positive stage
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","round":"R10","loop":100,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","price_data_repo":"Songdaiki/stock-web","price_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","price_adjustment_status":"raw_unadjusted_marcap","mfe_mae_formula":"MFE_N=(max high from entry row through N tradable rows / entry_price - 1)*100; MAE_N=(min low / entry_price - 1)*100","corporate_action_screen":"180D window screened for >=20% shares change or extreme close ratio; no candidates detected in selected rows","calibration_usable_rows":5}
{"row_type":"trigger","trigger_id":"C30-100-001","case_id":"C30-R10-L100-001","symbol":"006360","company_name":"GS건설","round":"R10","loop":100,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CONSTRUCTION_QUALITY_REBUILD_COST_TRUST_BREAK","sector":"construction_realestate_housing","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2023-07-05","evidence_available_at_that_date":true,"evidence_source":"The Bell / Yonhap, 2023-07-05~2023-07-07, Geomdan full rebuild and cost burden coverage","source_url":"https://m.thebell.co.kr/m/newsview.asp?newskey=202307071447108800109610","stage2_evidence_fields":["public_negative_event","large_project_quality_issue","sector_trust_discount"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["project_cost_uncertainty","margin_backlog_slowdown_risk","valuation_rebound_not_sufficient"],"stage4c_evidence_fields":["construction_quality_trust_break","full_rebuild_cost_burden","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web tradable OHLCV shard","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv ; atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"close_entry_high_low_path","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-06","entry_price":14520.0,"MFE_30D_pct":10.12,"MAE_30D_pct":-7.92,"MFE_90D_pct":10.12,"MAE_90D_pct":-12.74,"MFE_180D_pct":19.83,"MAE_180D_pct":-12.74,"MFE_1Y_pct":28.24,"MAE_1Y_pct":-12.74,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2023-11-23","peak_price":17400.0,"drawdown_after_peak_pct":-20.34,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"not_peak_locked","four_b_full_window_peak_proximity":"local_rebound_after_trust_break_not_full_window_positive","four_b_timing_verdict":"local_rebound_after_trust_break_not_full_window_positive","four_b_evidence_type":["project_cost_uncertainty","margin_backlog_slowdown_risk","valuation_rebound_not_sufficient"],"four_c_protection_label":"hard_4c_protection_success","trigger_outcome_label":"4c_then_partial_rebound_not_green","current_profile_verdict":"current_profile_correct_but_requires_c30_explicit_4c_route","calibration_usable":true,"forward_window_trading_days":362,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidates_180D":[],"same_entry_group_id":"C30-100-001","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","trigger_id":"C30-100-001","case_id":"C30-R10-L100-001","symbol":"006360","profile_id":"P0_active_e2r_2_2_proxy","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":0,"market_mispricing":25,"valuation_rerating":10,"capital_allocation":5,"information_confidence":18},"simulated_total_score":49,"simulated_stage":"Stage4C","actual_MFE_180D_pct":19.83,"actual_MAE_180D_pct":-12.74,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-001","case_id":"C30-R10-L100-001","symbol":"006360","profile_id":"P1_c30_balance_sheet_gate","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":0,"market_mispricing":25,"valuation_rerating":10,"capital_allocation":5,"information_confidence":18},"simulated_total_score":41,"simulated_stage":"Stage3-Red","actual_MFE_180D_pct":19.83,"actual_MAE_180D_pct":-12.74,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-001","case_id":"C30-R10-L100-001","symbol":"006360","profile_id":"P2_c30_4b4c_guard","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":0,"market_mispricing":25,"valuation_rerating":10,"capital_allocation":5,"information_confidence":18},"simulated_total_score":20,"simulated_stage":"Stage4C","actual_MFE_180D_pct":19.83,"actual_MAE_180D_pct":-12.74,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-001","case_id":"C30-R10-L100-001","symbol":"006360","profile_id":"P3_c30_combined_shadow","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":0,"market_mispricing":25,"valuation_rerating":10,"capital_allocation":5,"information_confidence":18},"simulated_total_score":18,"simulated_stage":"Stage4C","actual_MFE_180D_pct":19.83,"actual_MAE_180D_pct":-12.74,"alignment_label":"aligned"}
{"row_type":"trigger","trigger_id":"C30-100-002","case_id":"C30-R10-L100-002","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":100,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_FULL_DEMOLITION_REBUILD_BALANCE_SHEET_TRUST_BREAK","sector":"construction_realestate_housing","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2022-05-04","evidence_available_at_that_date":true,"evidence_source":"Yonhap, 2022-05-04, HDC full demolition/rebuild and expected additional cost coverage","source_url":"https://www.yna.co.kr/view/AKR20220504082651003","stage2_evidence_fields":["public_negative_event","construction_quality_issue","large_project_rebuild_cost"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["administrative_sanction_risk","project_cost_uncertainty","financing_trust_discount"],"stage4c_evidence_fields":["full_demolition_rebuild_decision","trust_break","balance_sheet_cost_burden"],"price_data_source":"Songdaiki/stock-web tradable OHLCV shard","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv ; atlas/ohlcv_tradable_by_symbol_year/294/294870/2023.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"close_entry_high_low_path","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-05-06","entry_price":15100.0,"MFE_30D_pct":1.99,"MAE_30D_pct":-26.49,"MFE_90D_pct":1.99,"MAE_90D_pct":-30.79,"MFE_180D_pct":1.99,"MAE_180D_pct":-38.48,"MFE_1Y_pct":1.99,"MAE_1Y_pct":-38.48,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2022-05-06","peak_price":15400.0,"drawdown_after_peak_pct":-39.68,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"entry_peak","four_b_full_window_peak_proximity":"4c_precedes_any_valid_4b_rebound","four_b_timing_verdict":"4c_precedes_any_valid_4b_rebound","four_b_evidence_type":["administrative_sanction_risk","project_cost_uncertainty","financing_trust_discount"],"four_c_protection_label":"hard_4c_protection_success","trigger_outcome_label":"hard_4c_with_near_zero_mfe_and_high_mae","current_profile_verdict":"current_profile_4c_too_late_without_explicit_full_rebuild_gate","calibration_usable":true,"forward_window_trading_days":407,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidates_180D":[],"same_entry_group_id":"C30-100-002","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","trigger_id":"C30-100-002","case_id":"C30-R10-L100-002","symbol":"294870","profile_id":"P0_active_e2r_2_2_proxy","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":0,"market_mispricing":25,"valuation_rerating":10,"capital_allocation":5,"information_confidence":18},"simulated_total_score":49,"simulated_stage":"Stage3-Red","actual_MFE_180D_pct":1.99,"actual_MAE_180D_pct":-38.48,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-002","case_id":"C30-R10-L100-002","symbol":"294870","profile_id":"P1_c30_balance_sheet_gate","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":0,"market_mispricing":25,"valuation_rerating":10,"capital_allocation":5,"information_confidence":18},"simulated_total_score":41,"simulated_stage":"Stage3-Red","actual_MFE_180D_pct":1.99,"actual_MAE_180D_pct":-38.48,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-002","case_id":"C30-R10-L100-002","symbol":"294870","profile_id":"P2_c30_4b4c_guard","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":0,"market_mispricing":25,"valuation_rerating":10,"capital_allocation":5,"information_confidence":18},"simulated_total_score":20,"simulated_stage":"Stage4C","actual_MFE_180D_pct":1.99,"actual_MAE_180D_pct":-38.48,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-002","case_id":"C30-R10-L100-002","symbol":"294870","profile_id":"P3_c30_combined_shadow","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":0,"market_mispricing":25,"valuation_rerating":10,"capital_allocation":5,"information_confidence":18},"simulated_total_score":18,"simulated_stage":"Stage4C","actual_MFE_180D_pct":1.99,"actual_MAE_180D_pct":-38.48,"alignment_label":"aligned"}
{"row_type":"trigger","trigger_id":"C30-100-003","case_id":"C30-R10-L100-003","symbol":"005960","company_name":"동부건설","round":"R10","loop":100,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_PF_LIQUIDITY_REBUTTAL_WITH_UNRESOLVED_MARKET_DISCOUNT","sector":"construction_realestate_housing","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression","trigger_type":"Stage2-RedWatch","trigger_date":"2024-01-05","evidence_available_at_that_date":true,"evidence_source":"CEOscoreDaily, 2024-01-05, Dongbu liquidity/PF risk rebuttal coverage","source_url":"https://ceoscoredaily.com/page/view/2024010510544420218","stage2_evidence_fields":["liquidity_rebuttal","pf_risk_limited_claim","public_balance_sheet_defense"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["funding_market_discount","earnings_cashflow_confirmation_missing","negative_reaction_after_rebuttal"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web tradable OHLCV shard","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv ; atlas/ohlcv_tradable_by_symbol_year/005/005960/2025.csv","profile_path":"atlas/symbol_profiles/005/005960.json","price_basis":"close_entry_high_low_path","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-08","entry_price":5610.0,"MFE_30D_pct":1.6,"MAE_30D_pct":-7.31,"MFE_90D_pct":1.6,"MAE_90D_pct":-14.53,"MFE_180D_pct":1.6,"MAE_180D_pct":-25.58,"MFE_1Y_pct":1.6,"MAE_1Y_pct":-36.36,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-01-09","peak_price":5700.0,"drawdown_after_peak_pct":-26.75,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"not_peak_locked","four_b_full_window_peak_proximity":"full_window_drawdown_dominates_local_rebuttal_event","four_b_timing_verdict":"full_window_drawdown_dominates_local_rebuttal_event","four_b_evidence_type":["funding_market_discount","earnings_cashflow_confirmation_missing","negative_reaction_after_rebuttal"],"four_c_protection_label":"no_hard_4c_but_red_watch_required","trigger_outcome_label":"rebuttal_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive_if_liquidity_rebuttal_gets_stage2_without_cashflow_confirmation","calibration_usable":true,"forward_window_trading_days":481,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidates_180D":[],"same_entry_group_id":"C30-100-003","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","trigger_id":"C30-100-003","case_id":"C30-R10-L100-003","symbol":"005960","profile_id":"P0_active_e2r_2_2_proxy","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":20,"earnings_visibility":28,"bottleneck_pricing":0,"market_mispricing":55,"valuation_rerating":35,"capital_allocation":30,"information_confidence":42},"simulated_total_score":66,"simulated_stage":"Stage2","actual_MFE_180D_pct":1.6,"actual_MAE_180D_pct":-25.58,"alignment_label":"misaligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-003","case_id":"C30-R10-L100-003","symbol":"005960","profile_id":"P1_c30_balance_sheet_gate","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":20,"earnings_visibility":28,"bottleneck_pricing":0,"market_mispricing":55,"valuation_rerating":35,"capital_allocation":30,"information_confidence":42},"simulated_total_score":55,"simulated_stage":"Stage1/Watch","actual_MFE_180D_pct":1.6,"actual_MAE_180D_pct":-25.58,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-003","case_id":"C30-R10-L100-003","symbol":"005960","profile_id":"P2_c30_4b4c_guard","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":20,"earnings_visibility":28,"bottleneck_pricing":0,"market_mispricing":55,"valuation_rerating":35,"capital_allocation":30,"information_confidence":42},"simulated_total_score":50,"simulated_stage":"Stage3-Red","actual_MFE_180D_pct":1.6,"actual_MAE_180D_pct":-25.58,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-003","case_id":"C30-R10-L100-003","symbol":"005960","profile_id":"P3_c30_combined_shadow","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":20,"earnings_visibility":28,"bottleneck_pricing":0,"market_mispricing":55,"valuation_rerating":35,"capital_allocation":30,"information_confidence":42},"simulated_total_score":48,"simulated_stage":"Stage3-Red","actual_MFE_180D_pct":1.6,"actual_MAE_180D_pct":-25.58,"alignment_label":"aligned"}
{"row_type":"trigger","trigger_id":"C30-100-004","case_id":"C30-R10-L100-004","symbol":"035890","company_name":"서희건설","round":"R10","loop":100,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_NEGATIVE_NET_DEBT_PF_CONTROLLED_REBOUND","sector":"construction_realestate_housing","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-21","evidence_available_at_that_date":true,"evidence_source":"KIS Rating, 2024-06-21, Seohee credit opinion / rating report","source_url":"https://m.kisrating.com/fileDown.do?fileName=rs20240621-39.pdf&gubun=2&menuCd=R8","stage2_evidence_fields":["negative_net_debt","debt_ratio_improvement","cash_exceeds_borrowings","sector_discount_context"],"stage3_evidence_fields":["balance_sheet_visibility","low_financial_risk","repeatable_local_housing_cash_generation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web tradable OHLCV shard","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv ; atlas/ohlcv_tradable_by_symbol_year/035/035890/2025.csv","profile_path":"atlas/symbol_profiles/035/035890.json","price_basis":"close_entry_high_low_path","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-24","entry_price":1319.0,"MFE_30D_pct":4.4,"MAE_30D_pct":-9.78,"MFE_90D_pct":22.9,"MAE_90D_pct":-9.78,"MFE_180D_pct":27.37,"MAE_180D_pct":-9.78,"MFE_1Y_pct":58.45,"MAE_1Y_pct":-9.78,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-12-18","peak_price":1680.0,"drawdown_after_peak_pct":-13.15,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"not_peak_locked","four_b_full_window_peak_proximity":"no_4b; drawdown_within_acceptable_c30_positive_band","four_b_timing_verdict":"no_4b; drawdown_within_acceptable_c30_positive_band","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_positive_balance_sheet_case","trigger_outcome_label":"balance_sheet_positive_with_90d_180d_mfe","current_profile_verdict":"current_profile_missed_structural_positive_if_c30_only_treated_as_pf_red_flag","calibration_usable":true,"forward_window_trading_days":275,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidates_180D":[],"same_entry_group_id":"C30-100-004","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","trigger_id":"C30-100-004","case_id":"C30-R10-L100-004","symbol":"035890","profile_id":"P0_active_e2r_2_2_proxy","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":46,"earnings_visibility":58,"bottleneck_pricing":22,"market_mispricing":68,"valuation_rerating":60,"capital_allocation":72,"information_confidence":76},"simulated_total_score":71,"simulated_stage":"Stage2","actual_MFE_180D_pct":27.37,"actual_MAE_180D_pct":-9.78,"alignment_label":"misaligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-004","case_id":"C30-R10-L100-004","symbol":"035890","profile_id":"P1_c30_balance_sheet_gate","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":46,"earnings_visibility":58,"bottleneck_pricing":22,"market_mispricing":68,"valuation_rerating":60,"capital_allocation":72,"information_confidence":76},"simulated_total_score":79,"simulated_stage":"Stage3-Yellow","actual_MFE_180D_pct":27.37,"actual_MAE_180D_pct":-9.78,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-004","case_id":"C30-R10-L100-004","symbol":"035890","profile_id":"P2_c30_4b4c_guard","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":46,"earnings_visibility":58,"bottleneck_pricing":22,"market_mispricing":68,"valuation_rerating":60,"capital_allocation":72,"information_confidence":76},"simulated_total_score":76,"simulated_stage":"Stage3-Yellow","actual_MFE_180D_pct":27.37,"actual_MAE_180D_pct":-9.78,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-004","case_id":"C30-R10-L100-004","symbol":"035890","profile_id":"P3_c30_combined_shadow","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":46,"earnings_visibility":58,"bottleneck_pricing":22,"market_mispricing":68,"valuation_rerating":60,"capital_allocation":72,"information_confidence":76},"simulated_total_score":81,"simulated_stage":"Stage3-Yellow","actual_MFE_180D_pct":27.37,"actual_MAE_180D_pct":-9.78,"alignment_label":"aligned"}
{"row_type":"trigger","trigger_id":"C30-100-005","case_id":"C30-R10-L100-005","symbol":"002990","company_name":"금호건설","round":"R10","loop":100,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_PF_CONTINGENT_LIABILITY_EQUITY_COVERAGE_GUARD","sector":"construction_realestate_housing","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-03-12","evidence_available_at_that_date":true,"evidence_source":"IB Tomato, 2024-03-12, Kumho E&C profit drop and PF contingent liability coverage","source_url":"https://www.ibtomato.com/ExternalView.aspx?no=11736&type=1","stage2_evidence_fields":["pf_risk_rebuttal_claim","soc_orderbook_reorientation"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["profit_collapse","pf_contingent_liability_near_equity","cashflow_credit_risk","high_mae_warning"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web tradable OHLCV shard","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv ; atlas/ohlcv_tradable_by_symbol_year/002/002990/2025.csv","profile_path":"atlas/symbol_profiles/002/002990.json","price_basis":"close_entry_high_low_path","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-13","entry_price":4810.0,"MFE_30D_pct":1.66,"MAE_30D_pct":-15.38,"MFE_90D_pct":1.66,"MAE_90D_pct":-24.22,"MFE_180D_pct":1.66,"MAE_180D_pct":-44.28,"MFE_1Y_pct":1.66,"MAE_1Y_pct":-52.08,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-03-13","peak_price":4890.0,"drawdown_after_peak_pct":-45.19,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"entry_peak","four_b_full_window_peak_proximity":"local_and_full_window_peak_at_entry; 4b_should_block_positive_stage","four_b_timing_verdict":"local_and_full_window_peak_at_entry; 4b_should_block_positive_stage","four_b_evidence_type":["profit_collapse","pf_contingent_liability_near_equity","cashflow_credit_risk","high_mae_warning"],"four_c_protection_label":"soft_4b_not_hard_4c_until_default_or_trust_break","trigger_outcome_label":"4b_high_mae_guardrail_success","current_profile_verdict":"current_profile_false_positive_if_pf_risk_comment_overrides_profit_and_liability_scale","calibration_usable":true,"forward_window_trading_days":437,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidates_180D":[],"same_entry_group_id":"C30-100-005","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","trigger_id":"C30-100-005","case_id":"C30-R10-L100-005","symbol":"002990","profile_id":"P0_active_e2r_2_2_proxy","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":0,"market_mispricing":48,"valuation_rerating":22,"capital_allocation":12,"information_confidence":30},"simulated_total_score":64,"simulated_stage":"Stage2","actual_MFE_180D_pct":1.66,"actual_MAE_180D_pct":-44.28,"alignment_label":"misaligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-005","case_id":"C30-R10-L100-005","symbol":"002990","profile_id":"P1_c30_balance_sheet_gate","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":0,"market_mispricing":48,"valuation_rerating":22,"capital_allocation":12,"information_confidence":30},"simulated_total_score":45,"simulated_stage":"Stage3-Red","actual_MFE_180D_pct":1.66,"actual_MAE_180D_pct":-44.28,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-005","case_id":"C30-R10-L100-005","symbol":"002990","profile_id":"P2_c30_4b4c_guard","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":0,"market_mispricing":48,"valuation_rerating":22,"capital_allocation":12,"information_confidence":30},"simulated_total_score":32,"simulated_stage":"Stage4B","actual_MFE_180D_pct":1.66,"actual_MAE_180D_pct":-44.28,"alignment_label":"aligned"}
{"row_type":"score_simulation","trigger_id":"C30-100-005","case_id":"C30-R10-L100-005","symbol":"002990","profile_id":"P3_c30_combined_shadow","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_proxy":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":0,"market_mispricing":48,"valuation_rerating":22,"capital_allocation":12,"information_confidence":30},"simulated_total_score":30,"simulated_stage":"Stage4B","actual_MFE_180D_pct":1.66,"actual_MAE_180D_pct":-44.28,"alignment_label":"aligned"}
{"row_type":"residual_contribution","round":"R10","loop":100,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":5,"calibration_usable_trigger_count":5,"positive_case_count":1,"counterexample_count":4,"four_b_case_count":1,"four_c_case_count":2,"current_profile_error_count":4,"coverage_before_rows":3,"expected_coverage_after_acceptance":8,"sector_specific_rule_candidate":"L9_C30_PF_DISTRESS_REBUTTAL_REQUIRES_CASHFLOW_AND_LIABILITY_SCALE","canonical_archetype_rule_candidate":"C30_BALANCE_SHEET_BREAK_AND_REBUILD_COST_GATE","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for stock_agent E2R v12 calibration ingest. Do not alter production scoring directly from this markdown. First ingest this file as a standard v12 research result. Validate that filename metadata matches selected_round=R10, selected_loop=100, large_sector_id=L9_CONSTRUCTION_REALESTATE_HOUSING, canonical_archetype_id=C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK. Parse all row_type=trigger rows and enforce required fields: entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct, large_sector_id, canonical_archetype_id, evidence_source/source_url. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date. If accepted, add five representative rows to C30 and evaluate shadow rule C30_BALANCE_SHEET_BREAK_AND_REBUILD_COST_GATE against existing C30 and adjacent L9 rows. Treat shadow_weight rows as proposal only; do not patch production profile unless batch-level validation passes.
```

## 27. Next Round State

```yaml
completed_round: R10
completed_loop: 100
completed_large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
completed_canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
next_recommended_archetype: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
supplementary_next: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
reason: C31 and C32 remain very thin priority-0 coverage areas; R13 high-MAE guardrail has zero dedicated cross-scope rows.
```

## 28. Source Notes

Evidence source URLs used:

- GS건설 / Geomdan rebuild: https://m.thebell.co.kr/m/newsview.asp?newskey=202307071447108800109610
- HDC현대산업개발 / Hwa-jeong full demolition and rebuild: https://www.yna.co.kr/view/AKR20220504082651003
- 동부건설 / liquidity and PF-risk rebuttal: https://ceoscoredaily.com/page/view/2024010510544420218
- 서희건설 / KIS Rating credit opinion: https://m.kisrating.com/fileDown.do?fileName=rs20240621-39.pdf&gubun=2&menuCd=R8
- 금호건설 / profit and PF contingent-liability article: https://www.ibtomato.com/ExternalView.aspx?no=11736&type=1

Stock-web raw OHLCV paths follow the documented tradable shard root: `atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv`.

## Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
future_data_leakage_detected: false
production_code_patch_included: false
production_scoring_patch_applied: false
```
