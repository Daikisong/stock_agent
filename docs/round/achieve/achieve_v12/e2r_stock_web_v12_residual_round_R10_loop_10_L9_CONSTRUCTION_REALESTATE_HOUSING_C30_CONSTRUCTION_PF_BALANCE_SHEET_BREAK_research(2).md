# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R10
scheduled_loop: 10
round_schedule_status: valid
round_sector_consistency: pass
completed_round: R10
completed_loop: 10
computed_next_round: R11
computed_next_loop: 10
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - green_strictness_stress_test
  - 4C_thesis_break_timing_test
  - canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`, not the old E2R 2.0 baseline.

Already-applied global axes are treated as existing controls, not re-proposed:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This R10/C30 loop stress-tests whether the current profile still lets construction/PF cases cross into Green too easily when valuation, capital return, or price bounce evidence is present but PF/liquidity/legal evidence remains unresolved.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R10 |
| loop | 10 |
| large_sector_id | `L9_CONSTRUCTION_REALESTATE_HOUSING` |
| canonical_archetype_id | `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` |
| fine_archetype_id | `PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD` |
| scheduled next | `R11 / loop 10` |

R10 is mapped to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The selected canonical archetype is `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`, so the target pattern is not ordinary cyclical construction recovery. The core object is the **balance-sheet wall**: PF exposure, unsold inventory, legal/quality liabilities, workout risk, and whether valuation recovery can cross that wall.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent artifact used: `reports/e2r_calibration/by_round/R10.md`.

R10 already has 93 representative triggers and 28 unique cases in the accumulated calibration report. It includes Stage2, Stage2-Actionable, Stage3-Green, Stage4B, Stage4C and 4C-late rows. Therefore this loop does not repeat the broad global conclusion. It fills a narrower residual gap: **C30-specific separation between survivor Stage2/Yellow recovery and false Green caused by valuation, capital-return, or price-only bounce.**

Duplicate avoidance decision:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
same_symbol_new_trigger_family = not used except narrative_only blocked Taeyoung
new_symbol_count = 5
new_independent_case_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest values used:

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
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The schema defines the tradable shard columns as `d,o,h,l,c,v,a,mc,s,m`. The MFE/MAE formulas follow stock-web schema definitions:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | clean 180D? | usable? | block reason |
|---|---:|---:|---:|---:|---|
| R10L10-C30-HDC-20240125 | 294870 | 2024-01-25 | yes | yes | none |
| R10L10-C30-HDCON-20240125 | 000720 | 2024-01-25 | yes | yes | none |
| R10L10-C30-DLEC-20240110 | 375500 | 2024-01-10 | yes | yes | none |
| R10L10-C30-GS-20230706 | 006360 | 2023-07-06 | yes | yes | none |
| R10L10-C30-TAEYOUNG-20231228 | 009410 | 2023-12-28 | no | no | long tradable gap + 2024-10-31 corporate-action candidate |

Quantitative calibration uses only the first four cases.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | All cases compress into C30 because the discriminant is PF/legal/quality-liability balance-sheet survivability, not ordinary order backlog. |
| survivor_recovery_after_quality_overhang | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | HDC case allows Stage2/Yellow recovery but not automatic Green. |
| valuation_capital_return_without_margin_PF_clearance | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | DL E&C style false Green risk. |
| legal_quality_thesis_break | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | GS Construction hard 4C/watch evidence. |
| workout_forced_liquidity_break | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Taeyoung narrative-only hard 4C guard. |

## 7. Case Selection Summary

| case_id | symbol | company | role | usable | current_profile_verdict |
|---|---:|---|---|---:|---|
| R10L10-C30-HDC-20240125 | 294870 | HDC현대산업개발 | structural_success | true | current_profile_correct |
| R10L10-C30-HDCON-20240125 | 000720 | 현대건설 | stage2_promote_candidate | true | current_profile_correct |
| R10L10-C30-DLEC-20240110 | 375500 | DL이앤씨 | false_positive_green | true | current_profile_false_positive |
| R10L10-C30-GS-20230706 | 006360 | GS건설 | 4C_success | true | current_profile_4C_too_late |
| R10L10-C30-TAEYOUNG-20231228 | 009410 | 태영건설 | narrative_only | false | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
narrative_only_case_count = 1
```

The two positive cases are deliberately not treated as immediate Green. They are **survivor recovery** cases where Stage2/Yellow can be useful. The two quantitative counterexamples show why R10/C30 needs its own guard: valuation bounce and construction-quality/legal shock produce very different paths from ordinary industrial orderbook cases.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---:|---|---|---|---|---|
| 294870 | post-accident recovery watch with surviving liquidity, Seoul/housing sentiment rebound, and price/volume confirmation; still requires balance-sheet guard before Green | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | financial_visibility, multiple_public_sources | price_only_local_peak, positioning_overheat | - |
| 000720 | large-contractor balance-sheet survivor watch; overseas/orderbook quality offsets but does not erase Korean housing/PF cycle drag | customer_or_order_quality, backlog_or_delivery_visibility, relative_strength | multiple_public_sources, financial_visibility | price_only_local_peak | - |
| 375500 | capital-return / valuation bounce without enough housing-margin and PF-risk resolution | valuation_repricing_score, relative_strength | financial_visibility | price_only_local_peak, margin_or_backlog_slowdown | - |
| 006360 | quality/legal incident converts ordinary construction-cycle risk into thesis-break watch; positive valuation labels should be blocked | - | - | legal_or_regulatory_block, margin_or_backlog_slowdown | legal_or_regulatory_block, accounting_or_trust_break, thesis_evidence_broken |
| 009410 | workout / PF liquidity break: useful narrative 4C guard case but blocked quantitatively by trading-window discontinuity and later corporate-action candidate | - | - | capital_raise_or_overhang, legal_or_regulatory_block | forced_liquidation_or_crash, accounting_or_trust_break, thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path |
|---:|---|---|---|
| 294870 | HDC현대산업개발 | `atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv` | `atlas/symbol_profiles/294/294870.json` |
| 000720 | 현대건설 | `atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv` | `atlas/symbol_profiles/000/000720.json` |
| 375500 | DL이앤씨 | `atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv` | `atlas/symbol_profiles/375/375500.json` |
| 006360 | GS건설 | `atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv` | `atlas/symbol_profiles/006/006360.json` |
| 009410 | 태영건설 | `atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv` | `atlas/symbol_profiles/009/009410.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | current_profile_verdict | trigger_outcome_label |
|---|---|---:|---:|---:|---|---|
| R10L10-C30-HDC-STAGE2-20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 16180 | current_profile_correct | survivor_recovery_with_clean_180D_path |
| R10L10-C30-HDCON-STAGE2-20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 32050 | current_profile_correct | limited_survivor_bounce_then_sector_drawdown |
| R10L10-C30-DLEC-STAGE2-20240110 | Stage2-Actionable | 2024-01-10 | 2024-01-10 | 40750 | current_profile_false_positive | valuation_repricing_failed_to_hold |
| R10L10-C30-GS-4C-20230706 | Stage4C | 2023-07-06 | 2023-07-06 | 14520 | current_profile_4C_too_late | legal_quality_thesis_break_prevents_false_green |
| R10L10-C30-TAEYOUNG-4C-20231228 | Stage4C | 2023-12-28 | 2023-12-28 | 2315 | current_profile_data_insufficient | PF_workout_thesis_break_quant_blocked |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 294870 | 2024-01-25 | 16180 | 28.24 | -4.14 | 28.24 | -4.2 | 52.04 | -4.2 | 2024-07-31 | 24600 | -30.28 |
| 000720 | 2024-01-25 | 32050 | 10.76 | -2.65 | 12.32 | -2.65 | 12.32 | -13.26 | 2024-05-09 | 36000 | -33.06 |
| 375500 | 2024-01-10 | 40750 | 8.34 | -7.73 | 8.34 | -21.6 | 8.34 | -27.85 | 2024-02-02 | 44150 | -33.41 |
| 006360 | 2023-07-06 | 14520 | 3.86 | -6.96 | 5.03 | -12.74 | 19.83 | -12.74 | 2023-11-23 | 17400 | -13.22 |
| 009410 | 2023-12-28 | 2315 | 77.54 | -16.41 | None | None | None | None | 2024-01-11 | 4110 | None |

## 13. Current Calibrated Profile Stress Test

### Finding

The current global profile is directionally safer than E2R 2.0, but R10/C30 still needs a local guard. The mechanism is simple: in construction, valuation and relative strength are not enough because the hidden variable is often balance-sheet duration. A contractor can look cheap the way a dam looks calm from the road; the important question is whether water is already pushing through the cracks behind it.

### Case verdicts

| symbol | verdict | explanation |
|---:|---|---|
| 294870 | current_profile_correct | Good C30 case where Stage2/Yellow can work if Green is withheld until balance-sheet/legal overhang clears. |
| 000720 | current_profile_correct | Positive only as survivor Stage2/Yellow; 180D MAE argues against automatic Green in C30. |
| 375500 | current_profile_false_positive | C30 counterexample: valuation/capital-return language cannot replace housing-margin/PF risk bridge. |
| 006360 | current_profile_4C_too_late | Legal/quality break should route to 4C/watch before later price recovery is considered. |
| 009410 | current_profile_data_insufficient | Strong narrative 4C case, but not included in quantitative weight calibration. |

### Existing calibrated axis assessment

| existing axis | result in this loop |
|---|---|
| stage2_actionable_evidence_bonus | existing_axis_strengthened for C30 only when PF/liquidity/legal guard is not broken |
| stage3_yellow_total_min | existing_axis_kept |
| stage3_green_total_min | existing_axis_strengthened locally: C30 needs PF/legal clearance before Green |
| stage3_green_revision_min | existing_axis_kept |
| price_only_blowoff_blocks_positive_stage | existing_axis_kept |
| full_4b_requires_non_price_evidence | existing_axis_strengthened for C30 local-vs-full 4B split |
| hard_4c_thesis_break_routes_to_4c | existing_axis_strengthened when workout/legal quality break appears |

## 14. Stage2 / Yellow / Green Comparison

For C30, Stage2/Yellow is often the correct maximum label when price confirms a recovery but PF/legal evidence is unresolved.

| symbol | proxy before | proxy after | interpretation |
|---:|---|---|---|
| 294870 | Stage3-Yellow / 76 | Stage3-Yellow / 82 | Good C30 case where Stage2/Yellow can work if Green is withheld until balance-sheet/legal overhang clears. |
| 000720 | Stage2-Actionable / 74 | Stage3-Yellow / 78 | Positive only as survivor Stage2/Yellow; 180D MAE argues against automatic Green in C30. |
| 375500 | Stage3-Yellow / 79 | Stage2-Actionable / 70 | C30 counterexample: valuation/capital-return language cannot replace housing-margin/PF risk bridge. |
| 006360 | Stage2 / 68 | Stage4C / 49 | Legal/quality break should route to 4C/watch before later price recovery is considered. |
| 009410 | Stage4C-watch / 42 | Stage4C / 35 | Strong narrative 4C case, but not included in quantitative weight calibration. |

`green_lateness_ratio` is not applicable for this loop because the main point is not that Green was late; it is that C30 Green should often be refused until the balance-sheet/liquidity wall is crossed.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local proximity | full-window proximity | verdict |
|---:|---:|---:|---|
| 294870 | 0.92 | 0.92 | price_run_requires_non_price_4B_confirmation |
| 000720 | 0.88 | 0.88 | local_peak_but_full_4B_requires_non_price_evidence |
| 375500 | 0.98 | 0.98 | good_local_risk_watch_but_not_full_4B_without_margin_slowdown_evidence |
| 006360 | None | None | not_applicable_4C |
| 009410 | None | None | not_for_weight_calibration |

C30 confirms the v12 split: price-only local peaks can mark risk watch, but full 4B should require non-price evidence such as margin slowdown, PF deterioration, legal block, dilution, or financing stress.

## 16. 4C Protection Audit

| symbol | 4C label | reason |
|---:|---|---|
| 294870 | not_applicable | - |
| 000720 | not_applicable | - |
| 375500 | thesis_break_watch_only | - |
| 006360 | hard_4c_success | legal_or_regulatory_block, accounting_or_trust_break, thesis_evidence_broken |
| 009410 | hard_4c_success_but_quant_blocked | forced_liquidation_or_crash, accounting_or_trust_break, thesis_evidence_broken |

GS Construction and Taeyoung Construction show why hard 4C routing must remain strong in construction/PF archetypes. HDC and Hyundai Construction show the opposite: recovery is possible, but it should pass through survivor Stage2/Yellow, not automatic Green.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
candidate = housing/PF survivor recovery can receive Stage2/Yellow, but Green requires explicit PF/legal/liquidity clearance.
```

Proposed sector shadow rule:

```text
if large_sector_id == L9_CONSTRUCTION_REALESTATE_HOUSING
and evidence includes valuation_repricing or relative_strength
but lacks PF_liquidity_clearance / legal_quality_clearance / margin_bridge:
    cap_positive_stage = Stage2-Actionable or Stage3-Yellow
    block_Stage3_Green = true
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
candidate = C30 Green requires PF/liquidity/legal guard.
```

Proposed C30 guard:

```text
C30_green_bridge_required:
  required_any:
    - explicit PF exposure reduction
    - liquidity maturity wall cleared
    - no unresolved workout / covenant / refinancing stress
    - legal / quality liability quantified and absorbed
    - margin bridge visible after housing-cost normalization
  block_if_any:
    - workout application
    - major quality/legal incident not quantified
    - valuation-only bounce
    - capital-return headline without housing-margin bridge
    - price-only local peak
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | default proxy | 4 | 13.48 | -10.3 | 23.13 | -14.51 | 2/4 | directionally useful, but C30 still needs PF/legal guard |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | 13.48 | -10.3 | 23.13 | -14.51 | likely 3/4 | too permissive for valuation/PF bounce |
| P1 sector_specific_candidate_profile | L9 sector shadow | 4 | 13.48 | -10.3 | 23.13 | -14.51 | 1/4 | better risk separation |
| P2 canonical_archetype_candidate_profile | C30 shadow | 4 | 13.48 | -10.3 | 23.13 | -14.51 | 0~1/4 | best aligned: permits HDC recovery, blocks DL/GS false Green |
| P3 counterexample_guard_profile | C30 guardrail | 4 | 13.48 | -10.3 | 23.13 | -14.51 | 0/4 for hard-break rows | conservative; useful for 4C protection not entry promotion |

## 20. Score-Return Alignment Matrix

| symbol | before_score | before_stage | after_score | after_stage | MFE180 | MAE180 | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 294870 | 76 | Stage3-Yellow | 82 | Stage3-Yellow | 52.04 | -4.2 | survivor_recovery_with_clean_180D_path |
| 000720 | 74 | Stage2-Actionable | 78 | Stage3-Yellow | 12.32 | -13.26 | limited_survivor_bounce_then_sector_drawdown |
| 375500 | 79 | Stage3-Yellow | 70 | Stage2-Actionable | 8.34 | -27.85 | valuation_repricing_failed_to_hold |
| 006360 | 68 | Stage2 | 49 | Stage4C | 19.83 | -12.74 | legal_quality_thesis_break_prevents_false_green |
| 009410 | 42 | Stage4C-watch | 35 | Stage4C | None | None | PF_workout_thesis_break_quant_blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD | 2 | 2 | 2 | 2 | 4 | 0 | 4 | 4 | 2 | true | true | lower: C30 now has survivor vs false-Green split |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - valuation_bounce_false_positive
  - legal_quality_break_4C_timing
  - PF_workout_quant_blocked
  - survivor_stage2_not_green
new_axis_proposed: null
existing_axis_strengthened:
  - C30-specific PF/liquidity/legal Green bridge
  - C30 local-vs-full 4B split
  - C30 hard 4C routing for legal/workout break
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema checked
- symbol profiles checked for row availability and corporate-action candidates
- tradable shard paths recorded
- 30D/90D/180D MFE/MAE computed for usable rows
- same_entry_group_id dedupe fields included
- positive/counterexample balance met
```

Not validated:

```text
- no live candidate scan
- no production scoring change
- no brokerage/API/trading action
- no stock_agent src/e2r code access
- no price route discovery outside Songdaiki/stock-web
- no weight promotion beyond shadow proposal
```

## 24. Shadow Weight Calibration

| row_type | axis | scope | large_sector_id | canonical_archetype_id | baseline_value | tested_value | delta | confidence | proposal_type |
|---|---|---|---|---|---|---|---|---|---|
| shadow_weight | pf_liquidity_guard_required_for_C30_green | canonical_archetype_specific | L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 0 | 1 | +1 guard | medium_low | canonical_archetype_shadow_only |
| shadow_weight | C30_price_only_local_peak_not_full_4B | canonical_archetype_specific | L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | full_4B_requires_non_price_evidence | kept_plus_C30_local_peak_split | 0 global / +C30 annotation | medium | canonical_archetype_shadow_only |

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L10-C30-HDC-20240125", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R10L10-C30-HDC-STAGE2-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "survivor_recovery_with_clean_180D_path", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Good C30 case where Stage2/Yellow can work if Green is withheld until balance-sheet/legal overhang clears."}
{"row_type": "case", "case_id": "R10L10-C30-HDCON-20240125", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R10L10-C30-HDCON-STAGE2-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "limited_survivor_bounce_then_sector_drawdown", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Positive only as survivor Stage2/Yellow; 180D MAE argues against automatic Green in C30."}
{"row_type": "case", "case_id": "R10L10-C30-DLEC-20240110", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R10L10-C30-DLEC-STAGE2-20240110", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "valuation_repricing_failed_to_hold", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C30 counterexample: valuation/capital-return language cannot replace housing-margin/PF risk bridge."}
{"row_type": "case", "case_id": "R10L10-C30-GS-20230706", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R10L10-C30-GS-4C-20230706", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "legal_quality_thesis_break_prevents_false_green", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Legal/quality break should route to 4C/watch before later price recovery is considered."}
{"row_type": "case", "case_id": "R10L10-C30-TAEYOUNG-20231228", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "case_type": "narrative_only", "positive_or_counterexample": "counterexample", "best_trigger": "R10L10-C30-TAEYOUNG-4C-20231228", "calibration_usable": false, "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "score_price_alignment": "PF_workout_thesis_break_quant_blocked", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "Strong narrative 4C case, but not included in quantitative weight calibration."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L10-C30-HDC-STAGE2-20240125", "case_id": "R10L10-C30-HDC-20240125", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "sector": "construction_real_estate_housing", "primary_archetype": "PF balance-sheet break / survivor recovery guard", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "entry_date": "2024-01-25", "entry_price": 16180, "evidence_available_at_that_date": "post-accident recovery watch with surviving liquidity, Seoul/housing sentiment rebound, and price/volume confirmation; still requires balance-sheet guard before Green", "evidence_source": "historical public-event proxy; stock-web price row used for timing", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.24, "MFE_90D_pct": 28.24, "MFE_180D_pct": 52.04, "MFE_1Y_pct": 52.04, "MFE_2Y_pct": null, "MAE_30D_pct": -4.14, "MAE_90D_pct": -4.2, "MAE_180D_pct": -4.2, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-31", "peak_price": 24600, "drawdown_after_peak_pct": -30.28, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "price_run_requires_non_price_4B_confirmation", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "survivor_recovery_with_clean_180D_path", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "294870:2024-01-25:16180", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L10-C30-HDCON-STAGE2-20240125", "case_id": "R10L10-C30-HDCON-20240125", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "sector": "construction_real_estate_housing", "primary_archetype": "PF balance-sheet break / survivor recovery guard", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "entry_date": "2024-01-25", "entry_price": 32050, "evidence_available_at_that_date": "large-contractor balance-sheet survivor watch; overseas/orderbook quality offsets but does not erase Korean housing/PF cycle drag", "evidence_source": "historical public-event proxy; stock-web price row used for timing", "stage2_evidence_fields": ["customer_or_order_quality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.76, "MFE_90D_pct": 12.32, "MFE_180D_pct": 12.32, "MFE_1Y_pct": 12.32, "MFE_2Y_pct": null, "MAE_30D_pct": -2.65, "MAE_90D_pct": -2.65, "MAE_180D_pct": -13.26, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-09", "peak_price": 36000, "drawdown_after_peak_pct": -33.06, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "local_peak_but_full_4B_requires_non_price_evidence", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "limited_survivor_bounce_then_sector_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000720:2024-01-25:32050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L10-C30-DLEC-STAGE2-20240110", "case_id": "R10L10-C30-DLEC-20240110", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "sector": "construction_real_estate_housing", "primary_archetype": "PF balance-sheet break / survivor recovery guard", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 40750, "evidence_available_at_that_date": "capital-return / valuation bounce without enough housing-margin and PF-risk resolution", "evidence_source": "historical public-event proxy; stock-web price row used for timing", "stage2_evidence_fields": ["valuation_repricing_score", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.34, "MFE_90D_pct": 8.34, "MFE_180D_pct": 8.34, "MFE_1Y_pct": 8.34, "MFE_2Y_pct": null, "MAE_30D_pct": -7.73, "MAE_90D_pct": -21.6, "MAE_180D_pct": -27.85, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 44150, "drawdown_after_peak_pct": -33.41, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_local_risk_watch_but_not_full_4B_without_margin_slowdown_evidence", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "valuation_repricing_failed_to_hold", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "375500:2024-01-10:40750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L10-C30-GS-4C-20230706", "case_id": "R10L10-C30-GS-20230706", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "sector": "construction_real_estate_housing", "primary_archetype": "PF balance-sheet break / survivor recovery guard", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2023-07-06", "entry_date": "2023-07-06", "entry_price": 14520, "evidence_available_at_that_date": "quality/legal incident converts ordinary construction-cycle risk into thesis-break watch; positive valuation labels should be blocked", "evidence_source": "historical public-event proxy; stock-web price row used for timing", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "accounting_or_trust_break", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.86, "MFE_90D_pct": 5.03, "MFE_180D_pct": 19.83, "MFE_1Y_pct": 19.83, "MFE_2Y_pct": null, "MAE_30D_pct": -6.96, "MAE_90D_pct": -12.74, "MAE_180D_pct": -12.74, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-23", "peak_price": 17400, "drawdown_after_peak_pct": -13.22, "green_lateness_ratio": "not_applicable:4C_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_4C", "four_b_evidence_type": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "legal_quality_thesis_break_prevents_false_green", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "006360:2023-07-06:14520", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L10-C30-TAEYOUNG-4C-20231228", "case_id": "R10L10-C30-TAEYOUNG-20231228", "symbol": "009410", "company_name": "태영건설", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_QUALITY_LEGAL_WORKOUT_GUARD", "sector": "construction_real_estate_housing", "primary_archetype": "PF balance-sheet break / survivor recovery guard", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2023-12-28", "entry_date": "2023-12-28", "entry_price": 2315, "evidence_available_at_that_date": "workout / PF liquidity break: useful narrative 4C guard case but blocked quantitatively by trading-window discontinuity and later corporate-action candidate", "evidence_source": "historical public-event proxy; stock-web price row used for timing", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["forced_liquidation_or_crash", "accounting_or_trust_break", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv", "profile_path": "atlas/symbol_profiles/009/009410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 77.54, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.41, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": null, "peak_date": "2024-01-11", "peak_price": 4110, "drawdown_after_peak_pct": null, "green_lateness_ratio": "not_applicable:4C_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_for_weight_calibration", "four_b_evidence_type": ["legal_or_regulatory_block", "capital_raise_or_overhang"], "four_c_protection_label": "hard_4c_success_but_quant_blocked", "trigger_outcome_label": "PF_workout_thesis_break_quant_blocked", "current_profile_verdict": "current_profile_data_insufficient", "calibration_usable": false, "forward_window_trading_days": null, "calibration_block_reasons": ["insufficient_forward_window_in_stock_web_due_to_long_gap", "corporate_action_candidate_2024-10-31_blocks_1Y_2Y"], "corporate_action_window_status": "blocked_after_partial_window", "same_entry_group_id": "009410:2023-12-28:2315", "dedupe_for_aggregate": false, "aggregate_group_role": "narrative_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10-C30-HDC-20240125", "trigger_id": "R10L10-C30-HDC-STAGE2-20240125", "symbol": "294870", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 7, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 12, "customer_quality_score": 4, "policy_or_regulatory_score": 8, "valuation_repricing_score": 11, "execution_risk_score": -8, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -2, "supplemental_pf_liquidity_guard_score": 6}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 12, "customer_quality_score": 4, "policy_or_regulatory_score": 8, "valuation_repricing_score": 11, "execution_risk_score": -5, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -1, "supplemental_pf_liquidity_guard_score": 8}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["supplemental_pf_liquidity_guard_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "C30 shadow profile raises the burden for Green and routes legal/PF/workout breaks into 4C/watch; survivor recovery is allowed only as Stage2/Yellow.", "MFE_90D_pct": 28.24, "MAE_90D_pct": -4.2, "score_return_alignment_label": "survivor_recovery_with_clean_180D_path", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10-C30-HDCON-20240125", "trigger_id": "R10L10-C30-HDCON-STAGE2-20240125", "symbol": "000720", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 12, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 5, "valuation_repricing_score": 7, "execution_risk_score": -5, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "supplemental_pf_liquidity_guard_score": 5}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 12, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 5, "valuation_repricing_score": 7, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "supplemental_pf_liquidity_guard_score": 8}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["supplemental_pf_liquidity_guard_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "C30 shadow profile raises the burden for Green and routes legal/PF/workout breaks into 4C/watch; survivor recovery is allowed only as Stage2/Yellow.", "MFE_90D_pct": 12.32, "MAE_90D_pct": -2.65, "score_return_alignment_label": "limited_survivor_bounce_then_sector_drawdown", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10-C30-DLEC-20240110", "trigger_id": "R10L10-C30-DLEC-STAGE2-20240110", "symbol": "375500", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 4, "valuation_repricing_score": 13, "execution_risk_score": -6, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "supplemental_pf_liquidity_guard_score": 3}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 3, "valuation_repricing_score": 10, "execution_risk_score": -9, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "supplemental_pf_liquidity_guard_score": 1}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable", "changed_components": ["supplemental_pf_liquidity_guard_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "C30 shadow profile raises the burden for Green and routes legal/PF/workout breaks into 4C/watch; survivor recovery is allowed only as Stage2/Yellow.", "MFE_90D_pct": 8.34, "MAE_90D_pct": -21.6, "score_return_alignment_label": "valuation_repricing_failed_to_hold", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10-C30-GS-20230706", "trigger_id": "R10L10-C30-GS-4C-20230706", "symbol": "006360", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 7, "execution_risk_score": -8, "legal_or_contract_risk_score": -12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -4, "supplemental_pf_liquidity_guard_score": 2}, "weighted_score_before": 68, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 0, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": -12, "legal_or_contract_risk_score": -20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -8, "supplemental_pf_liquidity_guard_score": 0}, "weighted_score_after": 49, "stage_label_after": "Stage4C", "changed_components": ["supplemental_pf_liquidity_guard_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "C30 shadow profile raises the burden for Green and routes legal/PF/workout breaks into 4C/watch; survivor recovery is allowed only as Stage2/Yellow.", "MFE_90D_pct": 5.03, "MAE_90D_pct": -12.74, "score_return_alignment_label": "legal_quality_thesis_break_prevents_false_green", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L10-C30-TAEYOUNG-20231228", "trigger_id": "R10L10-C30-TAEYOUNG-4C-20231228", "symbol": "009410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": -18, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": -10, "accounting_trust_risk_score": -8, "supplemental_pf_liquidity_guard_score": -15}, "weighted_score_before": 42, "stage_label_before": "Stage4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -20, "legal_or_contract_risk_score": -20, "dilution_cb_risk_score": -12, "accounting_trust_risk_score": -10, "supplemental_pf_liquidity_guard_score": -20}, "weighted_score_after": 35, "stage_label_after": "Stage4C", "changed_components": ["supplemental_pf_liquidity_guard_score", "execution_risk_score", "legal_or_contract_risk_score", "margin_bridge_score"], "component_delta_explanation": "C30 shadow profile raises the burden for Green and routes legal/PF/workout breaks into 4C/watch; survivor recovery is allowed only as Stage2/Yellow.", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "PF_workout_thesis_break_quant_blocked", "current_profile_verdict": "current_profile_data_insufficient"}
```

### 25.5 shadow_weight rows

```jsonl
{"row_type": "shadow_weight", "axis": "pf_liquidity_guard_required_for_C30_green", "scope": "canonical_archetype_specific", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "baseline_value": 0, "tested_value": 1, "delta": "+1 guard", "reason": "C30 positive cases only worked when PF/legal liquidity risk was not thesis-breaking; valuation-only and capital-return labels failed.", "backtest_effect": "keeps HDC/HDCON in Stage2/Yellow, downgrades DL-style valuation bounce, routes GS/Taeyoung-style legal/PF break to 4C/watch", "trigger_ids": "R10L10-C30-HDC-STAGE2-20240125|R10L10-C30-HDCON-STAGE2-20240125|R10L10-C30-DLEC-STAGE2-20240110|R10L10-C30-GS-4C-20230706", "calibration_usable_count": 4, "new_independent_case_count": 4, "counterexample_count": 2, "confidence": "medium_low", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "shadow_weight", "axis": "C30_price_only_local_peak_not_full_4B", "scope": "canonical_archetype_specific", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "baseline_value": "full_4B_requires_non_price_evidence", "tested_value": "kept_plus_C30_local_peak_split", "delta": "0 global / +C30 annotation", "reason": "HDC and Hyundai local peaks did not prove full-cycle 4B without non-price margin/PF evidence.", "backtest_effect": "prevents early 4B exit while still blocks Green if PF bridge is missing", "trigger_ids": "R10L10-C30-HDC-STAGE2-20240125|R10L10-C30-HDCON-STAGE2-20240125", "calibration_usable_count": 2, "new_independent_case_count": 2, "counterexample_count": 0, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "10", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["valuation_bounce_false_positive", "legal_quality_break_4C_timing", "PF_workout_quant_blocked", "survivor_stage2_not_green"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type": "narrative_only", "case_id": "R10L10-C30-TAEYOUNG-20231228", "symbol": "009410", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "reason": "evidence_available_but_forward_180D_unavailable_or_stock_web_price_window_blocked", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R10
completed_loop = 10
next_round = R11
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files consulted:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/000/000720.json
atlas/symbol_profiles/006/006360.json
atlas/symbol_profiles/294/294870.json
atlas/symbol_profiles/009/009410.json
atlas/symbol_profiles/375/375500.json
atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv
atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv
atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv
atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv
atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv
```

Allowed stock_agent research artifact consulted:

```text
reports/e2r_calibration/by_round/R10.md
```

No stock_agent source code was opened or patched.

