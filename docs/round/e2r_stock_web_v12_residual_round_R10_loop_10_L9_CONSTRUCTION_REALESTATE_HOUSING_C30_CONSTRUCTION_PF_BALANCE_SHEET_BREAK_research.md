# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R10
loop = 10
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = PF_GUARANTEE_BALANCE_SHEET_QUALITY_VS_OVERSEAS_BACKLOG_AND_LEGAL_DEFECT_BREAK
output_file = e2r_stock_web_v12_residual_round_R10_loop_10_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live watchlist, not current-stock discovery, not an investment recommendation, not brokerage/API work, and not a code patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-propose the global calibrated axes. It stress-tests whether C30 needs a narrower split between PF-safe construction positives and legal/PF-break false positives.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R10
loop = 10
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
loop_objective = residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill
```

C30 is not a normal backlog archetype. The causal chain is closer to a pressure vessel:

```text
housing/PF exposure
→ guarantee/liquidity/refinancing pressure
→ legal/safety/defect cost possibility
→ balance-sheet absorption or break
→ rating/financing/revision path
→ Stage promotion, 4B watch, or hard 4C routing
```

The residual tested here is that the current calibrated profile can still over-credit construction backlog while under-modeling PF guarantee quality and legal/defect loss absorption.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show R1~R13 and loops 1~9 already exist, with 398 discovered MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows. This loop therefore uses R10 loop 10 and five new independent C30 cases.

Already applied global axes are treated as baselines. The new candidate is scoped to C30:

```text
PF-safe overseas/backlog + balance-sheet quality = C30 positive bridge
housing backlog without PF/legal visibility = capped
hard legal/safety/defect or PF liquidity break = fast 4C protection
trading-gap/corporate-action contaminated PF-workout rows = narrative-only
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Manifest-confirmed context:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

## 5. Historical Eligibility Gate

Representative calibration rows satisfy:

```text
trigger_date is historical
entry_date exists in stock-web tradable shard
entry_date has at least 180 forward tradable rows before manifest max_date
OHLCV fields are positive and present
MFE/MAE 30D, 90D, 180D are computed from tradable_raw rows
corporate_action_window_status = clean_180D_window
```

Blocked/narrative-only handling:

```text
009410 Taeyoung Construction is a strong qualitative C30 4C case, but not quantitative calibration input.
Reason: forward tradable window crosses a long trading gap and the profile has a 2024-10-31 corporate-action candidate.
Usage: narrative_only / not_weight_calibration.
```

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype candidates compressed into C30:
- PF_SAFE_HAVEN_OVERSEAS_BACKLOG_BALANCE_SHEET
- PF_ESCAPE_OVERSEAS_EPC_NET_CASH_MARGIN_BRIDGE
- HOUSING_BACKLOG_FALSE_GREEN_LEGAL_DEFECT_UNPRICED
- CONSTRUCTION_SAFETY_ACCIDENT_LEGAL_THESIS_BREAK
- PF_WORKOUT_LIQUIDITY_BREAK_TRADING_GAP_CORP_ACTION_BLOCKED
```

## 7. Case Selection Summary

| case_id | symbol | company | role | usable | current_profile_verdict | notes |
|---|---:|---|---|---:|---|---|
| R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN | 000720 | 현대건설 | positive / structural_success | True | current_profile_too_late | Positive C30 control case: domestic PF stress existed at the sector level, but overseas/backlog visibility and stronger balance-sheet absorption made the signal different from generic housing exposure. |
| R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE | 028050 | 삼성E&A | positive / structural_success | True | current_profile_too_late | Positive C30 adjacent case: not a pure housing builder; overseas EPC backlog and balance-sheet quality made the sector PF discount too blunt. Kept under C30 only as PF-safe construction/EPC comparator. |
| R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK | 006360 | GS건설 | counterexample / false_positive_green | True | current_profile_false_positive | Counterexample: housing/backlog or valuation support could not protect against construction-quality/legal-cost break. Generic backlog should be capped when legal/defect evidence is rising. |
| R10L10_C30_294870_HDC_2022_COLLAPSE_LEGAL_THESIS_BREAK | 294870 | HDC현대산업개발 | counterexample / 4C_success | True | current_profile_4C_too_late | Counterexample and 4C protection case: safety/legal defect broke the thesis before any housing-cycle recovery logic could be trusted. |
| R10L10_C30_009410_TAEYOUNG_2023_PF_WORKOUT_LIQUIDITY_BREAK | 009410 | 태영건설 | counterexample / narrative_only | False | current_profile_data_insufficient | Important C30 narrative-only case. Stock-web profile includes a 2024-10-31 corporate-action candidate and the forward window crosses a suspended/irregular trading zone; therefore not used for quantitative weight calibration. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
calibration_usable_case_count = 4
narrative_only_case_count = 1
4B_or_4C_case_count = 3
new_independent_case_ratio = 1.00
```

The balance is intentional: C30 should not learn only from disaster rows. It also needs a control group showing when construction-sector PF fear was over-discounted because the issuer had stronger balance sheet, overseas backlog, or EPC exposure rather than domestic housing/PF concentration.

## 9. Evidence Source Map

| evidence family | positive use | counterexample / guard use |
|---|---|---|
| backlog_or_delivery_visibility | Positive only when tied to non-PF cash conversion and balance-sheet absorption | Capped if backlog is domestic housing-heavy and PF guarantee risk is unknown |
| margin_bridge | Required for Green; can support PF-safe overseas/EPC positives | Weak or broken margin bridge blocks Green |
| legal_or_regulatory_block | Usually absent/low in positives | Fast 4C when safety, defect, administrative, or legal-cost evidence appears |
| liquidity/PF workout | Not a positive score component | Hard 4C / narrative-only if forward price window is contaminated |
| price-only local peak | 4B watch only | Cannot train positive Stage2/3 |

## 10. Price Data Source Map

| symbol | profile_path | representative shard path(s) | profile caveat |
|---:|---|---|---|
| 000720 | atlas/symbol_profiles/000/000720.json | atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv | historical corporate-action candidates before 2005 only; 2023 window clean |
| 028050 | atlas/symbol_profiles/028/028050.json | atlas/ohlcv_tradable_by_symbol_year/028/028050/2023.csv | 2016 candidate before tested window; 2023 window clean |
| 006360 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | 2014 candidate before tested window; 2023 window clean |
| 294870 | atlas/symbol_profiles/294/294870.json | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | 2020 candidate before tested window; 2022 window clean |
| 009410 | atlas/symbol_profiles/009/009410.json | atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv; 2024.csv | narrative-only; 2024-10-31 corporate-action candidate and trading gap block clean weight calibration |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | verdict | role |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| TRG_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_STAGE2_ACTIONABLE_2023_04_11 | 000720 | Stage2-Actionable | 2023-04-11 | 38650 | 14.9 | -10.6 | 14.9 | -16.5 | current_profile_too_late | representative |
| TRG_HDEC_2023_POST_ORDER_PRICE_ONLY_4B_WATCH_2023_06_26 | 000720 | 4B-overlay/label-comparison | 2023-06-26 | 40800 | 8.8 | -15.3 | 8.8 | -19.0 | current_profile_4B_too_early | 4B_overlay_only |
| TRG_SAMSUNG_EA_2023_OVERSEAS_EPC_STAGE2_ACTIONABLE_2023_01_31 | 028050 | Stage2-Actionable | 2023-01-31 | 25850 | 25.3 | -2.1 | 44.1 | -2.1 | current_profile_too_late | representative |
| TRG_SAMSUNG_EA_2023_STAGE3_GREEN_LATE_4B_WATCH_2023_07_31 | 028050 | Stage3-Green/4B-overlay | 2023-07-31 | 37000 | 1.4 | -18.0 | 1.4 | -25.5 | current_profile_too_late | 4B_overlay_only |
| TRG_GS_EC_2023_FALSE_GREEN_PRE_DEFECT_STAGE3_2023_04_21 | 006360 | Stage3-Yellow/false-Green-test | 2023-04-21 | 22300 | 1.1 | -40.0 | 1.1 | -43.2 | current_profile_false_positive | representative |
| TRG_GS_EC_2023_HARD_4C_DEFECT_LOSS_2023_07_06 | 006360 | 4C | 2023-07-06 | 14520 | 19.8 | -12.7 | 19.8 | -12.7 | current_profile_4C_too_late | 4C_overlay_only |
| TRG_HDC_2022_COLLAPSE_HARD_4C_2022_01_12 | 294870 | 4C | 2022-01-12 | 20850 | 8.9 | -49.9 | 8.9 | -49.9 | current_profile_4C_too_late | representative |

## 12. Trigger-Level OHLC Backtest Tables

The OHLC calculations use:

```text
MFE_N_pct = (max high from entry_date through N trading rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading rows / entry_price - 1) * 100
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

Key interpretation:

```text
000720 and 028050 show that PF-safe construction/EPC cases can work, but the durable edge comes from balance-sheet/backlog/margin quality rather than generic construction exposure.
006360 and 294870 show that legal/safety/defect break should override backlog and valuation support.
009410 is directionally important but quantitatively blocked to avoid contaminated weight learning.
```

## 13. Current Calibrated Profile Stress Test

1. Current calibrated profile likely recognizes non-price evidence earlier than baseline, but C30 still needs a dedicated PF/legal split.
2. The positive cases fit only when backlog visibility is paired with balance-sheet quality and margin bridge.
3. Stage2 bonus is not too strong for 000720/028050, but it can be too generous for GS/HDC if legal/PF gates are not active.
4. Yellow threshold 75 is acceptable, but C30 Yellow should not progress without PF guarantee/liquidity visibility.
5. Green threshold 87 and revision 55 are directionally right; C30 also requires a legal/PF break override.
6. Price-only blowoff guard is appropriate and kept.
7. Full 4B non-price requirement is appropriate and kept.
8. Hard 4C routing is strengthened for legal/safety/PF liquidity break evidence.

## 14. Stage2 / Yellow / Green Comparison

```text
000720: Stage2 at 38,650 captured a modest but cleaner PF-safe upside before later price-only peak. Green after the order spike would be later and less attractive.
028050: Stage2 at 25,850 captured most of the rerating; late Green near 37,000 was effectively a 4B watch/label-comparison row.
006360: Stage3-like housing/backlog support before the defect break was a false positive. C30 needs a hard legal/defect cap.
294870: safety/legal break should skip positive Stage2/3 and route to 4C.
```

## 15. 4B Local vs Full-window Timing Audit

C30 4B rows are overlay rows only:

```text
000720 2023-06-26: local/full peak proximity = 1.00, but evidence type is price/order spike without confirmed margin/backlog slowdown. Do not treat as full 4B.
028050 2023-07-31: late Green/price peak proximity = 0.98, useful as a 4B watch but not a positive training row.
```

The existing `full_4b_requires_non_price_evidence` axis is strengthened but not re-proposed as new global logic.

## 16. 4C Protection Audit

Hard 4C rows:

```text
006360: false-positive row before defect/legal break suffered large MAE; 2023-07-06 hard 4C row is protection-only even though a later rebound occurred.
294870: 2022-01-12 safety/legal event suffered deep MAE and should block positive promotion.
009410: PF workout/liquidity break is a qualitative 4C case, but quantitative use is blocked by stock-web forward-window/corporate-action caveat.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c30_pf_balance_sheet_quality_gate
proposal = positive C30 promotion requires at least one of:
  - net-cash/low-net-debt or explicit liquidity absorption evidence
  - low PF guarantee/refinancing exposure evidence
  - overseas/EPC backlog with margin bridge and low domestic housing concentration
  - confirmed revision/margin bridge after PF-risk discount
```

This is not a production change. It is a shadow-only candidate for later batch aggregation.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = construction_defect_legal_risk_fast_4c
proposal = if safety/legal/defect/cost-overrun evidence is hard and company-specific:
  - block Stage2/Stage3 positive promotion
  - route to 4C or 4C-watch depending on evidence severity
  - use row for protection calibration only
  - do not train positive entry weights even if price later rebounds
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | none | 7 | -1.2 | -25.7 | high in legal/PF-break subset | mixed |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback_reference_only | 7 | -3.0 | -28.0 | very_high | worse |
| P1_c30_sector_pf_balance_sheet_candidate | sector_specific | pf_balance_sheet_quality_gate, pf_workout_liquidity_watch | 7 | 10.1 | -16.2 | reduced | improved |
| P2_c30_canonical_legal_defect_fast_4c | canonical_archetype_specific | construction_defect_legal_risk_fast_4c, positive_stage_block_on_hard_legal_break | 7 | 12.0 | -14.0 | low | best_shadow_candidate |
| P3_c30_counterexample_guard_profile | counterexample_guard | narrative_only_block_for_suspension_or_corporate_action_window | 7 | 12.0 | -14.0 | low | best_guarded |

## 20. Score-Return Alignment Matrix

| symbol | before_score | before_stage | after_score | after_stage | MFE90 | MAE90 | explanation |
|---:|---:|---|---:|---|---:|---:|---|
| 000720 | 76 | Stage3-Yellow | 82 | Stage3-Yellow/PF-safe-positive | 14.9 | -10.6 | C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection. |
| 028050 | 82 | Stage3-Yellow | 87 | Stage3-Green/PF-safe-EPC-comparator | 25.3 | -2.1 | C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection. |
| 006360 | 72 | Stage3-Yellow/false-Green-risk | 52 | 4C/legal-defect-watch | 1.1 | -40.0 | C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection. |
| 294870 | 65 | Stage2/false-recovery-risk | 38 | 4C/hard-legal-break | 8.9 | -49.9 | C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_GUARANTEE_BALANCE_SHEET_QUALITY_VS_OVERSEAS_BACKLOG_AND_LEGAL_DEFECT_BREAK | 2 | 3 | 2 | 3 | 5 | 0 | 7 | 4 | 4 | true | true | Remaining gap: regional/small-cap PF guarantor cases with clean 180D stock-web windows. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 4
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, stage3_green_revision_min
residual_error_types_found: housing_backlog_false_positive_when_legal_defect_break_exists, pf_safe_overseas_backlog_missed_structural, trading_gap_corporate_action_contaminated_pf_workout_case
new_axis_proposed: c30_pf_balance_sheet_quality_gate / construction_defect_legal_risk_fast_4c / pf_workout_liquidity_narrative_block
existing_axis_strengthened: hard_4c_thesis_break_routes_to_4c / full_4b_requires_non_price_evidence / price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus / stage3_yellow_total_min / stage3_green_total_min / stage3_green_revision_min / stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema checked
- 000720 / 028050 / 006360 / 294870 profiles checked
- representative OHLC rows read from stock-web tradable shards
- 009410 profile and 2023/2024 tradable rows checked for narrative-only block
- C30 positive vs counterexample split documented
```

Not validated:

```text
- no stock_agent src/e2r code opened
- no production scoring patch written
- no live scan or current candidate discovery performed
- no brokerage/API/trading workflow used
- no external price route explored beyond stock-web
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_pf_balance_sheet_quality_gate,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,Positive C30 should require balance-sheet/PF guarantee absorption, not merely housing backlog.,Improves separation between Hyundai E&C/Samsung E&A positives and GS/HDC legal/PF false positives.,TRG_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_STAGE2_ACTIONABLE_2023_04_11|TRG_SAMSUNG_EA_2023_OVERSEAS_EPC_STAGE2_ACTIONABLE_2023_01_31,4,5,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,construction_defect_legal_risk_fast_4c,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,Safety/legal/defect break should route to 4C before generic housing recovery or valuation support can promote.,Blocks GS/HDC false positives and treats 4C rows as protection only.,TRG_GS_EC_2023_FALSE_GREEN_PRE_DEFECT_STAGE3_2023_04_21|TRG_HDC_2022_COLLAPSE_HARD_4C_2022_01_12,4,5,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,pf_workout_liquidity_narrative_block,sector_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+0,Taeyoung is a strong qualitative 4C case but not clean for quantitative weight due to forward-window/corporate-action contamination.,Adds a non-weighted coverage flag so later implementation does not force contaminated rows into calibration.,TRG_TAEYOUNG_2023_PF_LIQUIDITY_HARD_4C_NARRATIVE_2023_12_13,0,1,1,low,narrative_guard_only,not production; not weight calibration
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_GUARANTEE_BALANCE_SHEET_QUALITY_VS_OVERSEAS_BACKLOG_AND_LEGAL_DEFECT_BREAK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_STAGE2_ACTIONABLE_2023_04_11", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive C30 control case: domestic PF stress existed at the sector level, but overseas/backlog visibility and stronger balance-sheet absorption made the signal different from generic housing exposure."}
{"row_type": "case", "case_id": "R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE", "symbol": "028050", "company_name": "삼성E&A", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_GUARANTEE_BALANCE_SHEET_QUALITY_VS_OVERSEAS_BACKLOG_AND_LEGAL_DEFECT_BREAK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_SAMSUNG_EA_2023_OVERSEAS_EPC_STAGE2_ACTIONABLE_2023_01_31", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive C30 adjacent case: not a pure housing builder; overseas EPC backlog and balance-sheet quality made the sector PF discount too blunt. Kept under C30 only as PF-safe construction/EPC comparator."}
{"row_type": "case", "case_id": "R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_GUARANTEE_BALANCE_SHEET_QUALITY_VS_OVERSEAS_BACKLOG_AND_LEGAL_DEFECT_BREAK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_GS_EC_2023_FALSE_GREEN_PRE_DEFECT_STAGE3_2023_04_21", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guard_needed_or_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample: housing/backlog or valuation support could not protect against construction-quality/legal-cost break. Generic backlog should be capped when legal/defect evidence is rising."}
{"row_type": "case", "case_id": "R10L10_C30_294870_HDC_2022_COLLAPSE_LEGAL_THESIS_BREAK", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_GUARANTEE_BALANCE_SHEET_QUALITY_VS_OVERSEAS_BACKLOG_AND_LEGAL_DEFECT_BREAK", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_HDC_2022_COLLAPSE_HARD_4C_2022_01_12", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guard_needed_or_false_positive", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Counterexample and 4C protection case: safety/legal defect broke the thesis before any housing-cycle recovery logic could be trusted."}
{"row_type": "case", "case_id": "R10L10_C30_009410_TAEYOUNG_2023_PF_WORKOUT_LIQUIDITY_BREAK", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_GUARANTEE_BALANCE_SHEET_QUALITY_VS_OVERSEAS_BACKLOG_AND_LEGAL_DEFECT_BREAK", "case_type": "narrative_only", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_TAEYOUNG_2023_PF_LIQUIDITY_HARD_4C_NARRATIVE_2023_12_13", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "narrative_4c_only", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "Important C30 narrative-only case. Stock-web profile includes a 2024-10-31 corporate-action candidate and the forward window crosses a suspended/irregular trading zone; therefore not used for quantitative weight calibration."}
{"row_type": "trigger", "trigger_id": "TRG_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_STAGE2_ACTIONABLE_2023_04_11", "case_id": "R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_SAFE_HAVEN_OVERSEAS_BACKLOG_BALANCE_SHEET", "sector": "건설·부동산·주택 / construction PF balance-sheet stress", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-11", "evidence_available_at_that_date": "Overseas order/backlog quality and balance-sheet absorption were visible while domestic PF stress was a sector discount rather than a company-specific liquidity break.", "evidence_source": "Historical company/disclosure/news/analyst-note proxy; price verified in stock-web 000720 2023 tradable shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-11", "entry_price": 38650, "MFE_30D_pct": 9.2, "MFE_90D_pct": 14.9, "MFE_180D_pct": 14.9, "MFE_1Y_pct": 14.9, "MFE_2Y_pct": null, "MAE_30D_pct": -1.4, "MAE_90D_pct": -10.6, "MAE_180D_pct": -16.5, "MAE_1Y_pct": -16.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-26", "peak_price": 44400, "drawdown_after_peak_pct": -22.2, "green_lateness_ratio": "0.37", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN__2023-04-11__38650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_HDEC_2023_POST_ORDER_PRICE_ONLY_4B_WATCH_2023_06_26", "case_id": "R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_SAFE_HAVEN_PRICE_LOCAL_PEAK_WATCH", "sector": "건설·부동산·주택 / construction PF balance-sheet stress", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill", "trigger_type": "4B-overlay/label-comparison", "trigger_date": "2023-06-26", "evidence_available_at_that_date": "Local price/order spike after the Stage2 thesis. Without margin/backlog slowdown this is a watch overlay, not a full 4B exit.", "evidence_source": "Historical order/news proxy; price verified in stock-web 000720 2023 tradable shard.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-26", "entry_price": 40800, "MFE_30D_pct": 8.8, "MFE_90D_pct": 8.8, "MFE_180D_pct": 8.8, "MFE_1Y_pct": 8.8, "MFE_2Y_pct": null, "MAE_30D_pct": -15.3, "MAE_90D_pct": -15.3, "MAE_180D_pct": -19.0, "MAE_1Y_pct": -19.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-26", "peak_price": 44400, "drawdown_after_peak_pct": -22.2, "green_lateness_ratio": "0.37", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN__2023-06-26__40800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_SAMSUNG_EA_2023_OVERSEAS_EPC_STAGE2_ACTIONABLE_2023_01_31", "case_id": "R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE", "symbol": "028050", "company_name": "삼성E&A", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_ESCAPE_OVERSEAS_EPC_NET_CASH_MARGIN_BRIDGE", "sector": "건설·부동산·주택 / construction PF balance-sheet stress", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-31", "evidence_available_at_that_date": "Overseas EPC backlog and margin bridge began to matter more than domestic PF housing risk. This is a construction-sector safe-haven comparator, not a housing PF positive.", "evidence_source": "Historical company/disclosure/news/analyst-note proxy; price verified in stock-web 028050 2023 tradable shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2023.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-01-31", "entry_price": 25850, "MFE_30D_pct": 18.0, "MFE_90D_pct": 25.3, "MFE_180D_pct": 44.1, "MFE_1Y_pct": 44.1, "MFE_2Y_pct": null, "MAE_30D_pct": -2.1, "MAE_90D_pct": -2.1, "MAE_180D_pct": -2.1, "MAE_1Y_pct": -2.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-31", "peak_price": 37250, "drawdown_after_peak_pct": -25.5, "green_lateness_ratio": "0.62", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE__2023-01-31__25850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_SAMSUNG_EA_2023_STAGE3_GREEN_LATE_4B_WATCH_2023_07_31", "case_id": "R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE", "symbol": "028050", "company_name": "삼성E&A", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_ESCAPE_LATE_GREEN_AFTER_REPRICING", "sector": "건설·부동산·주택 / construction PF balance-sheet stress", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill", "trigger_type": "Stage3-Green/4B-overlay", "trigger_date": "2023-07-31", "evidence_available_at_that_date": "By late July the overseas-EPC rerating was already largely priced. The row tests Green lateness and price-only 4B handling, not positive entry training.", "evidence_source": "Historical analyst-note proxy; price verified in stock-web 028050 2023 tradable shard.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2023.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-31", "entry_price": 37000, "MFE_30D_pct": 1.4, "MFE_90D_pct": 1.4, "MFE_180D_pct": 1.4, "MFE_1Y_pct": 1.4, "MFE_2Y_pct": null, "MAE_30D_pct": -12.0, "MAE_90D_pct": -18.0, "MAE_180D_pct": -25.5, "MAE_1Y_pct": -25.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-31", "peak_price": 37250, "drawdown_after_peak_pct": -25.5, "green_lateness_ratio": "0.98", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "late_green_near_full_window_peak_price_only_watch", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE__2023-07-31__37000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_GS_EC_2023_FALSE_GREEN_PRE_DEFECT_STAGE3_2023_04_21", "case_id": "R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HOUSING_BACKLOG_FALSE_GREEN_LEGAL_DEFECT_UNPRICED", "sector": "건설·부동산·주택 / construction PF balance-sheet stress", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill", "trigger_type": "Stage3-Yellow/false-Green-test", "trigger_date": "2023-04-21", "evidence_available_at_that_date": "Generic housing/backlog valuation looked optically supportable before the quality/legal break. C30 should cap positive score when defect/legal-risk indicators are rising or unknown.", "evidence_source": "Historical company/news proxy; price verified in stock-web 006360 2023 tradable shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["legal_or_regulatory_block", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-21", "entry_price": 22300, "MFE_30D_pct": 1.1, "MFE_90D_pct": 1.1, "MFE_180D_pct": 1.1, "MFE_1Y_pct": 1.1, "MFE_2Y_pct": null, "MAE_30D_pct": -9.4, "MAE_90D_pct": -40.0, "MAE_180D_pct": -43.2, "MAE_1Y_pct": -43.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-21", "peak_price": 22550, "drawdown_after_peak_pct": -43.8, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK__2023-04-21__22300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_GS_EC_2023_HARD_4C_DEFECT_LOSS_2023_07_06", "case_id": "R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_QUALITY_DEFECT_COST_HARD_4C", "sector": "건설·부동산·주택 / construction PF balance-sheet stress", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill", "trigger_type": "4C", "trigger_date": "2023-07-06", "evidence_available_at_that_date": "Hard defect/legal-cost evidence. This is a protection row only; it should not train positive entry weights even if a later rebound occurs.", "evidence_source": "Historical news/disclosure proxy; price verified in stock-web 006360 2023 tradable shard.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-06", "entry_price": 14520, "MFE_30D_pct": 3.9, "MFE_90D_pct": 19.8, "MFE_180D_pct": 19.8, "MFE_1Y_pct": 19.8, "MFE_2Y_pct": null, "MAE_30D_pct": -7.9, "MAE_90D_pct": -12.7, "MAE_180D_pct": -12.7, "MAE_1Y_pct": -12.7, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-23", "peak_price": 17400, "drawdown_after_peak_pct": -27.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_positive_training_hard_4C", "four_b_evidence_type": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK__2023-07-06__14520", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_HDC_2022_COLLAPSE_HARD_4C_2022_01_12", "case_id": "R10L10_C30_294870_HDC_2022_COLLAPSE_LEGAL_THESIS_BREAK", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "CONSTRUCTION_SAFETY_ACCIDENT_LEGAL_THESIS_BREAK", "sector": "건설·부동산·주택 / construction PF balance-sheet stress", "primary_archetype": "construction_pf_balance_sheet_break", "loop_objective": "residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill", "trigger_type": "4C", "trigger_date": "2022-01-12", "evidence_available_at_that_date": "Hard safety/legal evidence following the collapse event. Treat as 4C protection and false-positive guard, not as a housing-cycle or valuation entry.", "evidence_source": "Historical news/regulatory proxy; price verified in stock-web 294870 2022 tradable shard.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-01-12", "entry_price": 20850, "MFE_30D_pct": 8.9, "MFE_90D_pct": 8.9, "MFE_180D_pct": 8.9, "MFE_1Y_pct": 8.9, "MFE_2Y_pct": null, "MAE_30D_pct": -35.3, "MAE_90D_pct": -49.9, "MAE_180D_pct": -49.9, "MAE_1Y_pct": -49.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-12", "peak_price": 22700, "drawdown_after_peak_pct": -53.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_positive_training_hard_4C", "four_b_evidence_type": ["legal_or_regulatory_block", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L10_C30_294870_HDC_2022_COLLAPSE_LEGAL_THESIS_BREAK__2022-01-12__20850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN", "trigger_id": "TRG_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_STAGE2_ACTIONABLE_2023_04_11", "symbol": "000720", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 74, "backlog_visibility_score": 82, "margin_bridge_score": 66, "revision_score": 62, "relative_strength_score": 58, "customer_quality_score": 78, "policy_or_regulatory_score": 54, "valuation_repricing_score": 60, "execution_risk_score": 24, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 74, "backlog_visibility_score": 82, "margin_bridge_score": 66, "revision_score": 62, "relative_strength_score": 58, "customer_quality_score": 78, "policy_or_regulatory_score": 54, "valuation_repricing_score": 60, "execution_risk_score": 24, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8, "pf_balance_sheet_quality_score": 82, "overseas_backlog_quality_score": 84, "housing_pf_exposure_risk_score": 15}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow/PF-safe-positive", "changed_components": ["pf_balance_sheet_quality_bonus", "overseas_backlog_quality_bridge"], "component_delta_explanation": "C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection.", "MFE_90D_pct": 14.9, "MAE_90D_pct": -10.6, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_000720_HDEC_2023_OVERSEAS_BACKLOG_BALANCE_SHEET_SAFE_HAVEN", "trigger_id": "TRG_HDEC_2023_POST_ORDER_PRICE_ONLY_4B_WATCH_2023_06_26", "symbol": "000720", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 74, "backlog_visibility_score": 82, "margin_bridge_score": 66, "revision_score": 62, "relative_strength_score": 58, "customer_quality_score": 78, "policy_or_regulatory_score": 54, "valuation_repricing_score": 60, "execution_risk_score": 24, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 74, "backlog_visibility_score": 82, "margin_bridge_score": 66, "revision_score": 62, "relative_strength_score": 58, "customer_quality_score": 78, "policy_or_regulatory_score": 54, "valuation_repricing_score": 60, "execution_risk_score": 24, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8, "pf_balance_sheet_quality_score": 82, "overseas_backlog_quality_score": 84, "housing_pf_exposure_risk_score": 15}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow/PF-safe-positive", "changed_components": ["pf_balance_sheet_quality_bonus", "overseas_backlog_quality_bridge"], "component_delta_explanation": "C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection.", "MFE_90D_pct": 8.8, "MAE_90D_pct": -15.3, "score_return_alignment_label": "guard_needed_or_overlay_only", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE", "trigger_id": "TRG_SAMSUNG_EA_2023_OVERSEAS_EPC_STAGE2_ACTIONABLE_2023_01_31", "symbol": "028050", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 78, "backlog_visibility_score": 84, "margin_bridge_score": 72, "revision_score": 70, "relative_strength_score": 76, "customer_quality_score": 76, "policy_or_regulatory_score": 42, "valuation_repricing_score": 62, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 78, "backlog_visibility_score": 84, "margin_bridge_score": 72, "revision_score": 70, "relative_strength_score": 76, "customer_quality_score": 76, "policy_or_regulatory_score": 42, "valuation_repricing_score": 62, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8, "pf_balance_sheet_quality_score": 86, "overseas_backlog_quality_score": 88, "housing_pf_exposure_risk_score": 10}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green/PF-safe-EPC-comparator", "changed_components": ["overseas_e_pc_pf_escape_bridge", "margin_bridge_quality_bonus"], "component_delta_explanation": "C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection.", "MFE_90D_pct": 25.3, "MAE_90D_pct": -2.1, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_028050_SAMSUNG_EA_2023_OVERSEAS_EPC_NET_CASH_PF_ESCAPE", "trigger_id": "TRG_SAMSUNG_EA_2023_STAGE3_GREEN_LATE_4B_WATCH_2023_07_31", "symbol": "028050", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 78, "backlog_visibility_score": 84, "margin_bridge_score": 72, "revision_score": 70, "relative_strength_score": 76, "customer_quality_score": 76, "policy_or_regulatory_score": 42, "valuation_repricing_score": 62, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 78, "backlog_visibility_score": 84, "margin_bridge_score": 72, "revision_score": 70, "relative_strength_score": 76, "customer_quality_score": 76, "policy_or_regulatory_score": 42, "valuation_repricing_score": 62, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8, "pf_balance_sheet_quality_score": 86, "overseas_backlog_quality_score": 88, "housing_pf_exposure_risk_score": 10}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green/PF-safe-EPC-comparator", "changed_components": ["overseas_e_pc_pf_escape_bridge", "margin_bridge_quality_bonus"], "component_delta_explanation": "C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection.", "MFE_90D_pct": 1.4, "MAE_90D_pct": -18.0, "score_return_alignment_label": "guard_needed_or_overlay_only", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK", "trigger_id": "TRG_GS_EC_2023_FALSE_GREEN_PRE_DEFECT_STAGE3_2023_04_21", "symbol": "006360", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 42, "revision_score": 40, "relative_strength_score": 42, "customer_quality_score": 48, "policy_or_regulatory_score": 25, "valuation_repricing_score": 58, "execution_risk_score": 68, "legal_or_contract_risk_score": 82, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 18}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow/false-Green-risk", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 42, "revision_score": 40, "relative_strength_score": 42, "customer_quality_score": 48, "policy_or_regulatory_score": 25, "valuation_repricing_score": 58, "execution_risk_score": 68, "legal_or_contract_risk_score": 82, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 18, "construction_defect_legal_risk_score": 90, "pf_balance_sheet_or_legal_break_gate": 1, "positive_stage_block": true}, "weighted_score_after": 52, "stage_label_after": "4C/legal-defect-watch", "changed_components": ["construction_defect_legal_risk_cap", "pf_balance_sheet_unknown_penalty"], "component_delta_explanation": "C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection.", "MFE_90D_pct": 1.1, "MAE_90D_pct": -40.0, "score_return_alignment_label": "guard_needed_or_overlay_only", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_006360_GS_EC_2023_QUALITY_DEFECT_LEGAL_LOSS_BREAK", "trigger_id": "TRG_GS_EC_2023_HARD_4C_DEFECT_LOSS_2023_07_06", "symbol": "006360", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 42, "revision_score": 40, "relative_strength_score": 42, "customer_quality_score": 48, "policy_or_regulatory_score": 25, "valuation_repricing_score": 58, "execution_risk_score": 68, "legal_or_contract_risk_score": 82, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 18}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow/false-Green-risk", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 42, "revision_score": 40, "relative_strength_score": 42, "customer_quality_score": 48, "policy_or_regulatory_score": 25, "valuation_repricing_score": 58, "execution_risk_score": 68, "legal_or_contract_risk_score": 82, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 18, "construction_defect_legal_risk_score": 90, "pf_balance_sheet_or_legal_break_gate": 1, "positive_stage_block": true}, "weighted_score_after": 52, "stage_label_after": "4C/legal-defect-watch", "changed_components": ["construction_defect_legal_risk_cap", "pf_balance_sheet_unknown_penalty"], "component_delta_explanation": "C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection.", "MFE_90D_pct": 19.8, "MAE_90D_pct": -12.7, "score_return_alignment_label": "guard_needed_or_overlay_only", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10_C30_294870_HDC_2022_COLLAPSE_LEGAL_THESIS_BREAK", "trigger_id": "TRG_HDC_2022_COLLAPSE_HARD_4C_2022_01_12", "symbol": "294870", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 44, "margin_bridge_score": 28, "revision_score": 25, "relative_strength_score": 20, "customer_quality_score": 42, "policy_or_regulatory_score": 20, "valuation_repricing_score": 50, "execution_risk_score": 86, "legal_or_contract_risk_score": 94, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 20}, "weighted_score_before": 65, "stage_label_before": "Stage2/false-recovery-risk", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 44, "margin_bridge_score": 28, "revision_score": 25, "relative_strength_score": 20, "customer_quality_score": 42, "policy_or_regulatory_score": 20, "valuation_repricing_score": 50, "execution_risk_score": 86, "legal_or_contract_risk_score": 94, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 20, "construction_defect_legal_risk_score": 96, "pf_balance_sheet_or_legal_break_gate": 1, "positive_stage_block": true}, "weighted_score_after": 38, "stage_label_after": "4C/hard-legal-break", "changed_components": ["hard_legal_safety_break_fast_4c", "positive_stage_block"], "component_delta_explanation": "C30 shadow profile separates PF-safe overseas/backlog positives from housing/PF/legal-defect false positives; hard legal/safety evidence blocks positive promotion and routes to 4C protection.", "MFE_90D_pct": 8.9, "MAE_90D_pct": -49.9, "score_return_alignment_label": "guard_needed_or_overlay_only", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "narrative_only", "case_id": "R10L10_C30_009410_TAEYOUNG_2023_PF_WORKOUT_LIQUIDITY_BREAK", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_WORKOUT_LIQUIDITY_BREAK_TRADING_GAP_CORP_ACTION_BLOCKED", "reason": "evidence_available_but_forward_180D_window_crosses_suspension_gap_and_2024_10_31_corporate_action_candidate", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration", "profile_path": "atlas/symbol_profiles/009/009410.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv", "current_profile_verdict": "current_profile_data_insufficient", "notes": "태영건설 is a strong qualitative C30 4C example, but the stock-web forward window has a long tradable-row gap before the 2024-10-31 corporate-action candidate; therefore it is kept narrative-only."}
{"row_type": "residual_contribution", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["housing_backlog_false_positive_when_legal_defect_break_exists", "pf_safe_overseas_backlog_missed_structural", "trading_gap_corporate_action_contaminated_pf_workout_case"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R11_loop_10_or_C31_POLICY_SUBSIDY_LEGISLATION_EVENT
recommended_focus = policy/event rows where policy is a trigger route but not a score component unless earnings/contract visibility follows
carry_forward_block = do not use Taeyoung quantitative rows until clean post-corporate-action stock-web calibration window exists
```

## 28. Source Notes

```text
Stock-web manifest/schema checked:
- atlas/manifest.json
- atlas/schema.json

Stock-web profile files checked:
- atlas/symbol_profiles/000/000720.json
- atlas/symbol_profiles/028/028050.json
- atlas/symbol_profiles/006/006360.json
- atlas/symbol_profiles/294/294870.json
- atlas/symbol_profiles/009/009410.json

Stock-web OHLC shards checked:
- atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/028/028050/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv
- atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv
```
