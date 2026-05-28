# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
scheduled_round: R10
scheduled_loop: 15
completed_round: R10
completed_loop: 15
next_round: R11
next_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING
loop_objective: coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 1. Current Calibrated Profile Assumption

`current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy`.

Applied axis assumptions:

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

This MD does not re-prove those global axes. It stress-tests whether C30 needs an archetype-specific split between balance-sheet-safe construction rerating and hard PF/safety thesis breaks.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R10`
- scheduled_loop: `15`
- large_sector_id: `L9_CONSTRUCTION_REALESTATE_HOUSING`
- canonical_archetype_id: `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`
- fine_archetype_id: `K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING`

R10 is consistent with L9 construction/real-estate/housing. This is not R13 and does not use cross-archetype naming.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact check:

- `data/e2r/calibration/md_registry.jsonl` shows existing legacy R10 entries through older `e2r_stock_web_historical_calibration_round_R10_loop_*` filenames, including loops 1~9.
- Search for `e2r_stock_web_v12_residual_round_R10_loop` returned no v12 residual file in the repository.
- The previous local v12 output in this conversation completed R9/Loop 15 and set `next_round = R10`, `next_loop = 15`.

Duplicate-avoidance result:

```text
scheduled_round: R10
scheduled_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
same_symbol_same_trigger_date_research: avoided
same_canonical_archetype_research: allowed
new_symbol_count: 3
new_trigger_family_count: 3
```

Selected trigger families:

1. balance-sheet-safe incumbent rerating: Hyundai E&C.
2. execution-quality/safety cost thesis break: GS E&C.
3. fatal safety/legal trust break: HDC Hyundai Development.
4. PF workout/liquidity break: Taeyoung Construction, narrative-only due contaminated/sparse forward path.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields checked from `Songdaiki/stock-web`:

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

Schema fields checked:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Quantitative rows use `tradable_raw` only.

## 5. Historical Eligibility Gate

| symbol | company | entry row exists | 180D forward path | corporate action in 180D | calibration usable |
|---:|---|---:|---:|---:|---:|
| 000720 | 현대건설 | true | true | false | true |
| 006360 | GS건설 | true | true | false | true |
| 294870 | HDC현대산업개발 | true | true | false | true |
| 009410 | 태영건설 | true | blocked/sparse | true, 2024-10-31 candidate | false |

Taeyoung Construction is included as narrative-only because the symbol profile flags a 2024-10-31 corporate-action candidate and the 2024 tradable path has a large sparse/suspended interval.

## 6. Canonical Archetype Compression Map

```text
fine_archetype:
  K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING
maps_to:
  C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
subroutes:
  A. balance_sheet_safe_housing_volume_positive
  B. safety_quality_legal_cost_4C
  C. PF_liquidity_workout_4C
  D. valuation_rebound_false_positive_guard
```

Compression claim: C30 should not be a single bearish bucket. It needs a positive route for balance-sheet-safe backlog/volume recovery and a separate hard 4C route when safety/legal/PF evidence breaks the thesis.

## 7. Case Selection Summary

| case_id | symbol | company | role | representative trigger | usable | new independent | current profile verdict |
|---|---:|---|---|---|---:|---:|---|
| R10L15_C30_000720_POS_20210405 | 000720 | 현대건설 | structural_success / positive | R10L15_T001 | true | true | current_profile_too_late |
| R10L15_C30_006360_NEG_20230629 | 006360 | GS건설 | 4C_success / counterexample | R10L15_T002 | true | true | current_profile_4C_too_late |
| R10L15_C30_294870_NEG_20220112 | 294870 | HDC현대산업개발 | 4C_success / counterexample | R10L15_T003 | true | true | current_profile_4C_too_late |
| R10L15_C30_009410_NARR_20231228 | 009410 | 태영건설 | narrative_only / counterexample | R10L15_T004 | false | false | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
narrative_only_counterexample_count = 1
calibration_usable_case_count = 3
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

Positive side is deliberately narrow: only the balance-sheet-safe incumbent route is allowed to promote. Construction accidents, PF workout, or explicit regulatory/legal break cannot be converted into Stage2 merely because valuation looks cheap.

## 9. Evidence Source Map

| evidence family | case | trigger date | role |
|---|---|---:|---|
| balance-sheet-safe housing/order visibility | 현대건설 | 2021-04-05 | positive Stage2-Actionable |
| execution-quality / safety-cost break | GS건설 | 2023-06-29 | 4C protection |
| fatal safety/legal trust break | HDC현대산업개발 | 2022-01-11 | hard 4C |
| PF liquidity/workout | 태영건설 | 2023-12-28 | narrative-only 4C |

## 10. Price Data Source Map

| symbol | shard path | profile path | stock-web row evidence used |
|---:|---|---|---|
| 000720 | `atlas/ohlcv_tradable_by_symbol_year/000/000720/2021.csv` | `atlas/symbol_profiles/000/000720.json` | entry 2021-04-05 close 44,900; peak row 2021-07-06 high 61,900 |
| 006360 | `atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv` | `atlas/symbol_profiles/006/006360.json` | entry 2023-06-29 close 18,600; 2023-07-10 low 13,370 |
| 294870 | `atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv` | `atlas/symbol_profiles/294/294870.json` | entry 2022-01-12 close 20,850; 2022-09-28 low 10,250 |
| 009410 | `atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv`, `2024.csv` | `atlas/symbol_profiles/009/009410.json` | entry 2023-12-28 close 2,315; blocked by 2024-10-31 corporate-action candidate |

## 11. Case-by-Case Trigger Grid

| trigger_id | case | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | outcome | current verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R10L15_T001 | 000720 현대건설 | Stage2-Actionable | 2021-04-05 | 2021-04-05 | 44900 | 22.27 | 37.86 | 37.86 | -3.12 | -3.12 | -6.46 | structural_success | current_profile_too_late |
| R10L15_T001G | 000720 현대건설 | Stage3-Green | 2021-05-27 | 2021-05-27 | 56300 | 10.03 | 10.03 | 10.03 | -3.91 | -24.33 | -29.84 | late_green_success_but_upside_reduced | current_profile_too_late |
| R10L15_T002 | 006360 GS건설 | 4C | 2023-06-29 | 2023-06-29 | 18600 | 2.26 | 2.26 | 2.26 | -28.12 | -28.12 | -28.12 | 4C_success | current_profile_4C_too_late |
| R10L15_T003 | 294870 HDC현대산업개발 | 4C | 2022-01-11 | 2022-01-12 | 20850 | 8.87 | 8.87 | 8.87 | -35.25 | -35.25 | -50.84 | 4C_success | current_profile_4C_too_late |
| R10L15_T004 | 009410 태영건설 | 4C | 2023-12-28 | 2023-12-28 | 2315 | 77.54 | 77.54 | None | -5.83 | -2.38 | None | narrative_only_blocked | current_profile_data_insufficient |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows only:

| case | entry | peak | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---:|---:|---|---|---|---|
| 현대건설 | 44,900 | 61,900 | +22.27% / -3.12% | +37.86% / -3.12% | +37.86% / -6.46% | clean positive structural rerating |
| GS건설 | 18,600 | 19,020 | +2.26% / -28.12% | +2.26% / -28.12% | +2.26% / -28.12% | 4C protection beats rebound thesis |
| HDC현대산업개발 | 20,850 | 22,700 | +8.87% / -35.25% | +8.87% / -35.25% | +8.87% / -50.84% | hard 4C safety/legal break |
| 태영건설 | 2,315 | 4,110 | +77.54% / -5.83% | +77.54% / -2.38% | blocked | narrative-only: spike is not calibration evidence |

## 13. Current Calibrated Profile Stress Test

| case | current profile behavior | actual path alignment | residual verdict |
|---|---|---|---|
| 현대건설 | would wait for stricter Green confirmation after Stage2/Yellow | early Stage2 gave most of the MFE; Green was later | current_profile_too_late |
| GS건설 | global 4C guard exists but C30-specific execution-quality break is not explicit enough | large MAE followed non-price safety/cost evidence | current_profile_4C_too_late |
| HDC현대산업개발 | hard 4C route exists but needs construction-safety trust-break specificity | drawdown was immediate and deep | current_profile_4C_too_late |
| 태영건설 | should not train weights due contaminated/sparse path | narrative supports guard direction only | current_profile_data_insufficient |

Answers to the required stress questions:

1. Current calibrated profile is directionally right but not C30-specific enough.
2. Actual MFE/MAE supports positive promotion only when balance-sheet quality and backlog/order visibility are both present.
3. Stage2 bonus is not excessive for Hyundai E&C; it would be excessive for GS/HDC if legal/safety risk is not a hard blocker.
4. Yellow threshold 75 is acceptable.
5. Green threshold 87 / revision 55 is acceptable but late for clean cyclical construction turns.
6. Price-only blowoff guard is kept.
7. Full 4B non-price requirement is kept; GS/HDC are not mere 4B overlays.
8. Hard 4C routing should be strengthened with C30 safety/legal/PF routes.

## 14. Stage2 / Yellow / Green Comparison

Hyundai E&C:

```text
Stage2-Actionable entry = 2021-04-05 close 44,900
Stage3-Green comparison entry = 2021-05-27 close 56,300
full observed peak = 2021-07-06 high 61,900
green_lateness_ratio = (56,300 - 44,900) / (61,900 - 44,900) = 0.67
```

Interpretation: Green was useful as confirmation, but it consumed roughly two-thirds of the Stage2-to-peak upside. The proposed rule does not lower Green globally. It allows a C30-specific Stage2-Actionable route for balance-sheet-safe incumbents.

## 15. 4B Local vs Full-window Timing Audit

| case | Stage2/actionable anchor | 4B/4C entry | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---|
| GS건설 | 18,600 | 18,600 | 0.08 | 0.08 | not a 4B sell overlay; hard 4C |
| HDC현대산업개발 | 20,850 | 20,850 | 0.00 | 0.00 | hard 4C, not price-only 4B |
| 태영건설 | 2,315 | 2,315 | n/a | n/a | narrative-only, blocked |

C30 residual finding: severe construction-safety/legal/PF events should not wait for valuation blowoff proximity. They are thesis-break rows.

## 16. 4C Protection Audit

| case | 4C label | MAE after 4C | prior peak drawdown | protection verdict |
|---|---|---:|---:|---|
| GS건설 | hard_4c_success | -28.12% | -29.71% | success |
| HDC현대산업개발 | hard_4c_success | -50.84% | -54.85% | success |
| 태영건설 | thesis_break_watch_only | blocked | blocked | narrative-only |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = only one large sector is tested here; keep as C30 canonical shadow rule until more L9 cases and adjacent L10/R11 policy-event spillovers are added.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Candidate rules:

1. `C30_balance_sheet_quality_bonus`
   - Add a small positive shadow bonus only when backlog/order visibility and balance-sheet/PF cleanliness are both supported.
   - Do not apply to cheap but impaired constructors.

2. `C30_safety_legal_trust_break_hard_4C`
   - If safety/legal/regulatory evidence breaks trust, route to 4C even if valuation appears cheap.

3. `C30_valuation_rebound_cap_when_pf_or_safety_break`
   - Cap valuation-repricing score when PF workout, safety failure, or legal/regulatory block is present.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE 90D | avg MAE 90D | false positive | late green | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 3 | 16.33 | -22.16 | 0.33 | 1 | mixed; positive okay but 4C safety/PF risks late |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 3 | 16.33 | -22.16 | 0.67 | 1 | worse; valuation rebound can leak into Stage2 |
| P1_L9_sector_specific_candidate_profile | sector_specific | 3 | 16.33 | -22.16 | 0.0 | 1 | better protection; sample still small for sector globalization |
| P2_C30_canonical_candidate_profile | canonical_archetype_specific | 3 | 16.33 | -22.16 | 0.0 | 1 | best explanatory compression for C30 |
| P3_counterexample_guard_profile | guard | 3 | 16.33 | -22.16 | 0.0 | 1 | good guardrail; narrower than full C30 rule |

## 20. Score-Return Alignment Matrix

| trigger | before label | after label | MFE_90D | MAE_90D | alignment |
|---|---|---|---:|---:|---|
| R10L15_T001 | Stage3-Yellow | Stage2-Actionable / early structural watch | +37.86 | -3.12 | aligned positive but Green late |
| R10L15_T002 | Stage2 false-rebound risk | 4C | +2.26 | -28.12 | aligned 4C protection |
| R10L15_T003 | 4B/Watch | 4C | +8.87 | -35.25 | aligned 4C protection |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING | 1 | 2 | 0 | 2 | 3 | 0 | 3 | 3 | 3 | false | true | C30 still needs more positive survivor cases, but hard safety/PF 4C guard now has clean examples |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late
  - current_profile_4C_too_late
  - valuation_rebound_false_positive_risk
new_axis_proposed:
  - C30_balance_sheet_quality_bonus
  - C30_safety_legal_trust_break_hard_4C
  - C30_valuation_rebound_cap_when_pf_or_safety_break
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema basis.
- 3 calibration-usable representative triggers.
- 30D/90D/180D MFE/MAE directionality.
- Current calibrated profile residual errors.
- C30-specific shadow rule candidates.
```

Not validated:

```text
- live candidate scan.
- current 2026 recommendations.
- stock_agent production code.
- brokerage API.
- global scoring change.
- Taeyoung Construction as quantitative weight evidence.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_balance_sheet_quality_bonus,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,+1,+1,"Balance-sheet-safe backlog/order visibility separated Hyundai E&C positive from PF/safety breaks","kept positive Stage2 without loosening Green","R10L15_T001",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C30_safety_legal_trust_break_hard_4C,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,+2,+2,"Fatal safety/legal execution failures dominated valuation/backlog and protected against 35~50% drawdowns","rerouted GS/HDC to 4C instead of rebound watch","R10L15_T002|R10L15_T003",3,3,2,medium,canonical_shadow_only,"not production; 4C/protection only"
shadow_weight,C30_valuation_rebound_cap_when_pf_or_safety_break,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,+1,+1,"Cheap valuation bounce after thesis break created false positive risk","reduced false positive rate from 0.33/0.67 to 0 in sample","R10L15_T002|R10L15_T003|R10L15_T004",3,3,2,low,guard_shadow_only,"Taeyoung narrative-only supports direction but is not counted quantitatively"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L15_C30_000720_POS_20210405","symbol":"000720","company_name":"현대건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R10L15_T001","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"balance-sheet-safe housing/order visibility worked as Stage2-Actionable; Green confirmation would be late but not fatal","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Representative positive: clean balance-sheet incumbent rerated during 2021 housing/order recovery; used as non-PF-break positive contrast."}
{"row_type":"case","case_id":"R10L15_C30_006360_NEG_20230629","symbol":"006360","company_name":"GS건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"R10L15_T002","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"non-price safety/cost evidence overrode cheap valuation; current profile should route to 4C rather than Stage2 rebound","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Representative 4C/protection case: execution-quality evidence broke housing rerating thesis before price fully stabilized."}
{"row_type":"case","case_id":"R10L15_C30_294870_NEG_20220112","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"R10L15_T003","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard construction-safety thesis break correctly dominated backlog/valuation arguments","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Representative legal/safety 4C case after Gwangju Hwajeong I-Park collapse."}
{"row_type":"case","case_id":"R10L15_C30_009410_NARR_20231228","symbol":"009410","company_name":"태영건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","case_type":"narrative_only","positive_or_counterexample":"counterexample","best_trigger":"R10L15_T004","calibration_usable":false,"is_new_independent_case":false,"reuse_reason":"blocked_by_corporate_action_candidate_and_trading_gap_in_forward_window","independent_evidence_weight":0.0,"score_price_alignment":"workout/PF liquidity event is narratively important but not quantitative weight-calibration usable","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Narrative-only: 2024-10-31 corporate-action candidate in profile overlaps the post-trigger observed path."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R10L15_T001","case_id":"R10L15_C30_000720_POS_20210405","symbol":"000720","company_name":"현대건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","sector":"건설·부동산·주택","primary_archetype":"balance_sheet_safe_housing_volume_and_order_visibility","loop_objective":"coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-04-05","evidence_available_at_that_date":"주택/건축 수주와 분양 회복, 대형사 PF·유동성 리스크 상대 우위, 건설업종 리레이팅이 가격보다 먼저 확인된 구간","evidence_source":"historical company/sector event map + stock-web tradable OHLC rows","stage2_evidence_fields":["relative_strength","backlog_or_delivery_visibility","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2021.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-04-05","entry_price":44900,"MFE_30D_pct":22.27,"MFE_90D_pct":37.86,"MFE_180D_pct":37.86,"MFE_1Y_pct":37.86,"MFE_2Y_pct":37.86,"MAE_30D_pct":-3.12,"MAE_90D_pct":-3.12,"MAE_180D_pct":-6.46,"MAE_1Y_pct":-15.37,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-06","peak_price":61900,"drawdown_after_peak_pct":-32.15,"green_lateness_ratio":0.47,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_positive_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L15_G001_000720_20210405","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L15_T001G","case_id":"R10L15_C30_000720_POS_20210405","symbol":"000720","company_name":"현대건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","sector":"건설·부동산·주택","primary_archetype":"balance_sheet_safe_housing_volume_and_order_visibility","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2021-05-27","evidence_available_at_that_date":"상승 후 수주·실적 가시성이 더 넓게 확인된 Green 비교용 label row","evidence_source":"stock-web tradable OHLC rows","stage2_evidence_fields":["relative_strength","backlog_or_delivery_visibility"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2021.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-27","entry_price":56300,"MFE_30D_pct":10.03,"MFE_90D_pct":10.03,"MFE_180D_pct":10.03,"MFE_1Y_pct":10.03,"MFE_2Y_pct":10.03,"MAE_30D_pct":-3.91,"MAE_90D_pct":-24.33,"MAE_180D_pct":-29.84,"MAE_1Y_pct":-33.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-06","peak_price":61900,"drawdown_after_peak_pct":-32.15,"green_lateness_ratio":0.67,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"green_label_comparison_only","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_success_but_upside_reduced","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L15_G001G_000720_20210527","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same case Green lateness audit only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R10L15_T002","case_id":"R10L15_C30_006360_NEG_20230629","symbol":"006360","company_name":"GS건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","sector":"건설·부동산·주택","primary_archetype":"execution_quality_cost_overrun_4C","loop_objective":"4C_thesis_break_timing_test | counterexample_mining","trigger_type":"4C","trigger_date":"2023-06-29","evidence_available_at_that_date":"검단 아파트 지하주차장 붕괴 조사/재시공 비용 우려가 가격보다 명확한 thesis-break로 작동한 구간","evidence_source":"historical event map + stock-web tradable OHLC rows","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","legal_or_regulatory_block"],"stage4c_evidence_fields":["qualification_failure","legal_or_contract_risk","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-29","entry_price":18600,"MFE_30D_pct":2.26,"MFE_90D_pct":2.26,"MFE_180D_pct":2.26,"MFE_1Y_pct":23.39,"MFE_2Y_pct":23.39,"MAE_30D_pct":-28.12,"MAE_90D_pct":-28.12,"MAE_180D_pct":-28.12,"MAE_1Y_pct":-31.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-03","peak_price":19020,"drawdown_after_peak_pct":-29.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.08,"four_b_full_window_peak_proximity":0.08,"four_b_timing_verdict":"4C_not_4B_execution_thesis_break","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L15_G002_006360_20230629","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L15_T003","case_id":"R10L15_C30_294870_NEG_20220112","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","sector":"건설·부동산·주택","primary_archetype":"construction_safety_legal_trust_break","loop_objective":"4C_thesis_break_timing_test | counterexample_mining","trigger_type":"4C","trigger_date":"2022-01-11","evidence_available_at_that_date":"광주 화정아이파크 외벽 붕괴 직후, 안전·법적 리스크가 backlog/valuation thesis를 압도","evidence_source":"historical event map + stock-web tradable OHLC rows","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken","regulatory_rejection","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-12","entry_price":20850,"MFE_30D_pct":8.87,"MFE_90D_pct":8.87,"MFE_180D_pct":8.87,"MFE_1Y_pct":8.87,"MFE_2Y_pct":51.08,"MAE_30D_pct":-35.25,"MAE_90D_pct":-35.25,"MAE_180D_pct":-50.84,"MAE_1Y_pct":-50.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700,"drawdown_after_peak_pct":-54.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"hard_4C_not_sell_overlay","four_b_evidence_type":["legal_or_regulatory_block","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L15_G003_294870_20220112","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L15_T004","case_id":"R10L15_C30_009410_NARR_20231228","symbol":"009410","company_name":"태영건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"K_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_AND_SAFETY_COST_ROUTING","sector":"건설·부동산·PF","primary_archetype":"PF_liquidity_workout_thesis_break","loop_objective":"narrative_only | 4C_thesis_break_timing_test","trigger_type":"4C","trigger_date":"2023-12-28","evidence_available_at_that_date":"PF liquidity stress/workout 신청 이벤트","evidence_source":"historical event map + stock-web tradable/raw profile fields","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["capital_raise_or_overhang","legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["forced_liquidation_or_crash","thesis_evidence_broken","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv","profile_path":"atlas/symbol_profiles/009/009410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-28","entry_price":2315,"MFE_30D_pct":77.54,"MFE_90D_pct":77.54,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.83,"MAE_90D_pct":-2.38,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-11","peak_price":4110,"drawdown_after_peak_pct":-46.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"blocked_for_quantitative_calibration","four_b_evidence_type":["capital_raise_or_overhang","legal_or_regulatory_block"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"narrative_only_blocked","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":false,"forward_window_trading_days":null,"calibration_block_reasons":["corporate_action_contaminated_180D_window","suspended_or_sparse_tradable_forward_path"],"corporate_action_window_status":"blocked_180D_window_2024-10-31_candidate","same_entry_group_id":"R10L15_G004_009410_20231228","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"narrative_only_corporate_action_candidate_overlap","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L15_C30_000720_POS_20210405","trigger_id":"R10L15_T001","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":16,"margin_bridge_score":12,"revision_score":12,"relative_strength_score":14,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"pf_balance_sheet_quality_score":14,"housing_delivery_visibility_score":12},"weighted_score_before":78.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":17,"margin_bridge_score":13,"revision_score":12,"relative_strength_score":14,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"pf_balance_sheet_quality_score":18,"housing_delivery_visibility_score":13},"weighted_score_after":83.0,"stage_label_after":"Stage2-Actionable / early structural watch","changed_components":["pf_balance_sheet_quality_score","+C30_balance_sheet_safe_order_visibility_bonus"],"component_delta_explanation":"Positive construction rerating required non-price backlog and balance-sheet cleanliness; Green still waits for confirmed revision.","MFE_90D_pct":37.86,"MAE_90D_pct":-3.12,"score_return_alignment_label":"aligned_positive_but_green_late","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L15_C30_006360_NEG_20230629","trigger_id":"R10L15_T002","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":-10,"revision_score":-8,"relative_strength_score":-12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-20,"legal_or_contract_risk_score":-18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-6,"safety_quality_break_score":-25,"pf_balance_sheet_quality_score":-6},"weighted_score_before":42.0,"stage_label_before":"Stage2 false-rebound risk if valuation overweighted","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-16,"revision_score":-12,"relative_strength_score":-14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-28,"legal_or_contract_risk_score":-30,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-8,"safety_quality_break_score":-35,"pf_balance_sheet_quality_score":-10},"weighted_score_after":18.0,"stage_label_after":"4C","changed_components":["safety_quality_break_score","legal_or_contract_risk_score","margin_bridge_score"],"component_delta_explanation":"Execution-quality failure should cap or override cheap valuation/rebound signals.","MFE_90D_pct":2.26,"MAE_90D_pct":-28.12,"score_return_alignment_label":"aligned_4C_protection","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L15_C30_294870_NEG_20220112","trigger_id":"R10L15_T003","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":-8,"revision_score":-10,"relative_strength_score":-16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-25,"legal_or_contract_risk_score":-24,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-12,"safety_quality_break_score":-35,"brand_trust_break_score":-25},"weighted_score_before":28.0,"stage_label_before":"4B/Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-14,"revision_score":-14,"relative_strength_score":-18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-34,"legal_or_contract_risk_score":-36,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-18,"safety_quality_break_score":-45,"brand_trust_break_score":-35},"weighted_score_after":8.0,"stage_label_after":"4C","changed_components":["hard_4C_safety_trust_break_route","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Fatal safety/legal thesis break is not a valuation 4B; it is hard 4C protection.","MFE_90D_pct":8.87,"MAE_90D_pct":-35.25,"score_return_alignment_label":"aligned_4C_protection","current_profile_verdict":"current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_balance_sheet_quality_bonus,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,+1,+1,"Balance-sheet-safe backlog/order visibility separated Hyundai E&C positive from PF/safety breaks","kept positive Stage2 without loosening Green","R10L15_T001",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C30_safety_legal_trust_break_hard_4C,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,+2,+2,"Fatal safety/legal execution failures dominated valuation/backlog and protected against 35~50% drawdowns","rerouted GS/HDC to 4C instead of rebound watch","R10L15_T002|R10L15_T003",3,3,2,medium,canonical_shadow_only,"not production; 4C/protection only"
shadow_weight,C30_valuation_rebound_cap_when_pf_or_safety_break,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,+1,+1,"Cheap valuation bounce after thesis break created false positive risk","reduced false positive rate from 0.33/0.67 to 0 in sample","R10L15_T002|R10L15_T003|R10L15_T004",3,3,2,low,guard_shadow_only,"Taeyoung narrative-only supports direction but is not counted quantitatively"

```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","scheduled_round":"R10","scheduled_loop":"15","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage3_green_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_4C_too_late","valuation_rebound_false_positive_risk"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R10L15_C30_009410_NARR_20231228","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"workout/PF thesis-break evidence available but stock-web forward 180D window is blocked by corporate-action candidate and sparse/suspended tradable path","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 15
next_round = R11
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files inspected:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/000/000720.json
atlas/symbol_profiles/006/006360.json
atlas/symbol_profiles/294/294870.json
atlas/symbol_profiles/009/009410.json
atlas/ohlcv_tradable_by_symbol_year/000/000720/2021.csv
atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv
atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv
atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv
atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv
```

Allowed stock_agent research artifact inspected:

```text
data/e2r/calibration/md_registry.jsonl
reports/e2r_calibration/calibrated_profile_report.md
data/e2r/calibration/trigger_rows_representative.jsonl
```

No `src/e2r` path was opened and no production scoring was changed.

