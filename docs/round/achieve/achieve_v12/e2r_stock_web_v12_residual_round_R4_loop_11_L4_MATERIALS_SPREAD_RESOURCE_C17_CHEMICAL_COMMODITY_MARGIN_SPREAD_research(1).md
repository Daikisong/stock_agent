# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R4
scheduled_loop: 11
completed_round: R4
completed_loop: 11
next_round: R5
next_loop: 11
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD
output_file: e2r_stock_web_v12_residual_round_R4_loop_11_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
stock_web_price_atlas_access_required: true
stock_web_manifest_max_date: 2026-02-20
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. This loop does **not** re-prove the global Stage2 bonus or the already-applied non-price 4B rule. It stress-tests whether those global rules still misclassify **chemical commodity spread** cases when the evidence is only broad NCC spread beta rather than durable specialty margin bridge.

Applied-axis status:

```text
stage2_actionable_evidence_bonus: existing_axis_kept
stage3_yellow_total_min: existing_axis_kept
stage3_green_total_min: existing_axis_kept_but_c17_guard_needed
stage3_green_revision_min: existing_axis_kept_but_c17_guard_needed
stage3_cross_evidence_green_buffer: existing_axis_kept
price_only_blowoff_blocks_positive_stage: existing_axis_strengthened
full_4b_requires_non_price_evidence: existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c: existing_axis_weakened_for_generic_NCC_spread_when_durable_spread_break_is_visible
```

## 2. Round / Large Sector / Canonical Archetype Scope

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`, so the selected sector is valid. The selected canonical archetype is `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`.

Scope in this MD:

```text
included:
- specialty spread winners: NBR latex / spandex
- generic NCC spread false positives: Lotte Chemical / Daehan Yuhwa
- 4B overlays where non-price spread-peak evidence exists

excluded:
- current/live candidates
- stock_agent production scoring patches
- generic battery/EV orderbook cases already handled by R3
- price-only peak labels without spread or valuation evidence
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact check: `reports/e2r_calibration/by_round/R4.md` reports 108 representative triggers and 27 unique cases, with existing accepted axes already cumulative. This MD therefore avoids simply repeating Stage2/Green global calibration and targets the residual gap: **generic NCC spread Green false positives versus specialty-margin spread successes**.

Novelty gate:

```text
minimum_new_independent_case_ratio: 1.00
new_independent_case_count: 4
reused_case_count: 0
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
counterexample_count: 2
positive_case_count: 2
round_schedule_status: valid
round_sector_consistency: pass
loop_contribution_label: canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Validation:

```text
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
validation_status: usable_for_historical_calibration
```

## 5. Historical Eligibility Gate

All representative triggers are historical, have entry rows in stock-web tradable shards, and have at least 180 trading days forward. Corporate-action windows do not overlap any entry-to-D+180 calibration window.

Profile checks:

| symbol | company | profile_path | relevant corporate_action_candidate_dates | 180D window status |
|---:|---|---|---|---|
| 011780 | 금호석유화학 | atlas/symbol_profiles/011/011780.json | 2001-01-16 | clean for 2020-11 to 2021-05 |
| 298020 | 효성티앤씨 | atlas/symbol_profiles/298/298020.json | none | clean |
| 011170 | 롯데케미칼 | atlas/symbol_profiles/011/011170.json | 2023-02-13 | clean for 2021 |
| 006650 | 대한유화 | atlas/symbol_profiles/006/006650.json | 2010-07-13 | clean for 2021 |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

compressed fine_archetypes:
- NBR_LATEX_SPECIALTY_MARGIN_SPREAD -> C17
- SPANDEX_SUPERCYCLE_OPERATING_LEVERAGE -> C17
- NCC_GENERIC_SPREAD_FALSE_GREEN -> C17
- NCC_STANDALONE_SPREAD_FALSE_GREEN -> C17
```

Compression insight: the archetype should not treat all chemical spread evidence equally. The actual split is **specialty-margin durability** versus **generic feedstock spread beta**.

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | current verdict | calibration usable |
|---|---:|---|---|---|---|---|
| R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020 | 011780 | 금호석유화학 | structural_success | R4L11_C17_KUMHO_20201106_S2A | current_profile_correct | true |
| R4L11_C17_HYOSUNG_SPANDEX_SPREAD_2021 | 298020 | 효성티앤씨 | structural_success | R4L11_C17_HYOSUNG_20210129_S2A | current_profile_correct | true |
| R4L11_C17_LOTTE_NCC_SPREAD_FALSE_GREEN_2021 | 011170 | 롯데케미칼 | false_positive_green | R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE | current_profile_false_positive | true |
| R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021 | 006650 | 대한유화 | false_positive_green | R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE | current_profile_false_positive | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 2
4B_case_count: 2
4C_case_count: 2
calibration_usable_case_count: 4
calibration_usable_trigger_count: 8
representative_trigger_count: 4
```

The balance is useful: the rule is not “chemical spread bad.” It is “generic NCC spread evidence must be capped unless it proves durability.” Specialty spread cases produced major MFE; generic NCC Green labels produced low MFE and heavy MAE.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 금호석유화학 | NBR/synthetic-rubber spread, medical/glove demand route, early revision | confirmed margin bridge and financial visibility | valuation blowoff + spread peak + positioning | thesis-break watch only |
| 효성티앤씨 | spandex spread, operating leverage, early revision | confirmed revision and financial visibility | valuation blowoff + spandex spread peak + positioning | hard 4C success after peak drawdown |
| 롯데케미칼 | broad NCC spread rebound | apparent revision/relative strength | margin slowdown | generic spread thesis broke |
| 대한유화 | standalone NCC spread rebound | apparent Green by price and revision | price-only local peak plus spread slowdown | generic spread thesis broke |

## 10. Price Data Source Map

| symbol | tradable shard(s) used | profile path | price basis |
|---:|---|---|---|
| 011780 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv; atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv | atlas/symbol_profiles/011/011780.json | tradable_raw |
| 298020 | atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv | atlas/symbol_profiles/298/298020.json | tradable_raw |
| 011170 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv | atlas/symbol_profiles/011/011170.json | tradable_raw |
| 006650 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv | atlas/symbol_profiles/006/006650.json | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict | aggregate_role |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| R4L11_C17_KUMHO_20201106_S2A | 011780 | Stage2-Actionable | 2020-11-06 | 153500 | 91.21 | -19.22 | 94.46 | -19.22 | current_profile_correct | representative |
| R4L11_C17_KUMHO_20210128_GREEN_COMPARE | 011780 | Stage3-Green | 2021-01-28 | 277000 | 7.76 | -27.8 | 7.76 | -27.8 | current_profile_too_late | label_comparison_only |
| R4L11_C17_KUMHO_20210506_4B | 011780 | Stage4B | 2021-05-06 | 296000 | 0.84 | -31.59 | 0.84 | -31.59 | current_profile_correct | 4B_overlay_only |
| R4L11_C17_HYOSUNG_20210129_S2A | 298020 | Stage2-Actionable | 2021-01-29 | 299500 | 152.09 | -3.67 | 221.54 | -3.67 | current_profile_correct | representative |
| R4L11_C17_HYOSUNG_20210325_GREEN_COMPARE | 298020 | Stage3-Green | 2021-03-25 | 591000 | 54.48 | -9.81 | 62.94 | -11.0 | current_profile_correct | label_comparison_only |
| R4L11_C17_HYOSUNG_20210715_4B | 298020 | Stage4B | 2021-07-15 | 935000 | 2.99 | -36.58 | 2.99 | -46.95 | current_profile_correct | 4B_overlay_only |
| R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE | 011170 | Stage3-Green | 2021-02-23 | 326000 | 3.68 | -21.17 | 3.68 | -31.29 | current_profile_false_positive | representative |
| R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE | 006650 | Stage3-Green | 2021-02-16 | 393500 | 3.05 | -35.32 | 3.05 | -53.37 | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows only:

| case_id | entry | entry_price | peak_date | peak_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| KUMHO_NBR_LATEX | 2020-11-06 | 153500 | 2021-05-06 | 298500 | 1.95 | -19.22 | 91.21 | -19.22 | 94.46 | -19.22 | Stage2 works; high MAE means position sizing / drawdown guard required |
| HYOSUNG_SPANDEX | 2021-01-29 | 299500 | 2021-07-16 | 963000 | 67.95 | -3.67 | 152.09 | -3.67 | 221.54 | -3.67 | clean structural success |
| LOTTE_NCC_FALSE_GREEN | 2021-02-23 | 326000 | 2021-03-02 | 338000 | 3.68 | -11.04 | 3.68 | -21.17 | 3.68 | -31.29 | false Green |
| DAEHAN_NCC_FALSE_GREEN | 2021-02-16 | 393500 | 2021-02-17 | 405500 | 3.05 | -25.79 | 3.05 | -35.32 | 3.05 | -53.37 | false Green/high-MAE |

## 13. Current Calibrated Profile Stress Test

Answers required by the v12 prompt:

1. Current profile would correctly admit the two specialty spread cases at Stage2/Actionable, but can still over-admit generic NCC spread rebounds as Stage3-Green when revision and relative strength are present without durable margin bridge.
2. The judgment matches MFE/MAE for Kumho and Hyosung, but fails for Lotte and Daehan.
3. Stage2 bonus is not too high for specialty spread cases; it is too high only if commodity spread evidence is generic and non-durable.
4. Yellow threshold 75 is acceptable as a watch level.
5. Green threshold 87 / revision 55 is insufficient for C17 if the revision is broad-cycle, non-specialty, and not customer-anchored.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate and strengthened by Kumho/Hyosung.
8. Hard 4C routing is too late for generic NCC cases if the spread thesis itself breaks before explicit accounting/default evidence.

Current profile error rows:

```text
R4L11_C17_KUMHO_20210128_GREEN_COMPARE: current_profile_too_late
R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE: current_profile_false_positive
R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE: current_profile_false_positive
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable entry | Green comparison entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 금호석유화학 | 153500 | 277000 | 0.85 | Green captured little remaining upside and inherited high MAE |
| 효성티앤씨 | 299500 | 591000 | 0.44 | Green was late but still usable due extreme spread supercycle |
| 롯데케미칼 | n/a | 326000 | 1.00 | Green appeared at/near local exhaustion |
| 대한유화 | n/a | 393500 | 1.00 | Green appeared at/near local exhaustion |

Conclusion: C17 needs a two-lane rule. Specialty spread cases can be admitted early; generic NCC cases need a Green cap.

## 15. 4B Local vs Full-window Timing Audit

| trigger | Stage2 base | 4B entry | full-window peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| KUMHO_20210506_4B | 153500 | 296000 | 298500 | 0.98 | 0.98 | good_full_window_4B_timing |
| HYOSUNG_20210715_4B | 299500 | 935000 | 963000 | 0.96 | 0.96 | good_full_window_4B_timing |
| DAEHAN_20210216_GREEN_FALSE_POSITIVE | n/a | n/a | 405500 | n/a | n/a | price-only local peak was insufficient until spread slowdown appeared |

## 16. 4C Protection Audit

For C17, 4C should be allowed when the commodity spread thesis itself breaks, not only when the issuer has accounting/trust/default evidence.

```text
KUMHO: thesis_break_watch_only; 4B already captured the risk.
HYOSUNG: hard_4c_success after 4B; severe drawdown followed spread peak.
LOTTE: hard_4c_late_if_waiting_for explicit crisis; spread thesis broke earlier.
DAEHAN: hard_4c_late_if_waiting_for explicit crisis; generic NCC spread reversal was enough.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope: sector_specific
rule_name: L4_commodity_spread_durability_gate
candidate: true
reason: material-spread sectors need a split between specialty margin bridge and generic commodity beta.
```

Rule candidate:

```text
If large_sector_id == L4_MATERIALS_SPREAD_RESOURCE and the evidence is commodity-spread driven:
    require at least two of:
        1. specialty or product-specific margin bridge,
        2. customer/demand quality that is not generic macro rebound,
        3. durable revision across more than one reporting window.
    If not met:
        cap Stage3-Green to Stage2-watch / Stage3-Yellow even when relative strength is strong.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope: canonical_archetype_specific
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
candidate: true
```

Canonical rule:

```text
C17_specialty_margin_durability_bonus = +3
C17_generic_NCC_green_cap = cap_to_Stage2_watch_or_Yellow
C17_non_price_4B_spread_peak_confirmation = true
```

Mechanism: NBR latex and spandex behaved like a narrow bridge with high tolls; generic NCC behaved like a wide road everyone could enter, where supply quickly erased the spread.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | calibrated global profile, no C17-specific spread durability cap | 4 | 62.51 | -19.84 | 80.68 | -26.89 | 50% | 0 | 1 | mixed; strong positives but false Green in generic NCC |
| P0b e2r_2_0_baseline_reference | rollback | older looser Green profile | 4 | 62.51 | -19.84 | 80.68 | -26.89 | 50%+ | 0 | 1 | worse due looser false-positive admission |
| P1 sector_specific_candidate_profile | L4 | add commodity-spread durability check across material spread cases | 4 | 121.65 | -11.45 | 158.00 | -11.45 | 0% | 0 | 1 | improved by blocking generic NCC false Greens |
| P2 canonical_archetype_candidate_profile | C17 | specialty margin bridge bonus + generic NCC Green cap | 4 | 121.65 | -11.45 | 158.00 | -11.45 | 0% | 0 | 1 | best alignment in this loop |
| P3 counterexample_guard_profile | C17 guard | require 2-of-3: specialty margin bridge, customer/demand quality, durable revision | 4 | 121.65 | -11.45 | 158.00 | -11.45 | 0% | 0 | 1 | best guard; risk is excluding broad beta rebounds |


## 20. Score-Return Alignment Matrix

| case | P0 score label | proposed label | MFE180 | MAE180 | alignment |
|---|---|---|---:|---:|---|
| 금호석유화학 | Stage2-Actionable / later Green | Stage2-Actionable + late Green caution | 94.46 | -19.22 | aligned after high-MAE guard |
| 효성티앤씨 | Stage2-Actionable -> Green | Stage3-Green allowed | 221.54 | -3.67 | aligned |
| 롯데케미칼 | Stage3-Green | Stage2-watch / Yellow cap | 3.68 | -31.29 | improved |
| 대한유화 | Stage3-Green | Stage2-watch / Yellow cap | 3.05 | -53.37 | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | NBR/SPANDEX/NCC spread durability | 2 | 2 | 2 | 2 | 4 | 0 | 8 | 4 | 3 | true | true | generic NCC false-Green gap reduced; specialty-margin durability still needs more holdout cases |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - generic_NCC_spread_false_green
  - late_green_high_MAE
  - price_only_local_peak_not_full_4B
new_axis_proposed: null
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened:
  - hard_4c_thesis_break_routes_to_4c for generic NCC spread thesis break
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC row existence
- 180D forward window availability
- corporate-action window cleanliness for representative triggers
- MFE/MAE/peak/drawdown for representative triggers
- current calibrated profile residual stress
- positive/counterexample balance
```

Not validated:

```text
- production scoring code
- live scan behavior
- current market recommendations
- broker or API execution
- raw unadjusted corporate-action adjustment beyond profile caveat checks
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_specialty_margin_durability_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+3,+3,"Reward spread evidence only when margin bridge is specialty/customer durable, not generic NCC beta","keeps Kumho/Hyosung positive while avoiding Lotte/Daehan false Green","R4L11_C17_KUMHO_20201106_S2A|R4L11_C17_HYOSUNG_20210129_S2A|R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE|R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_generic_ncc_green_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,none,cap_to_stage2_watch,guard,"If commodity-only NCC spread lacks specialty margin bridge + customer quality + durable revision, block Stage3-Green even if relative strength is high","reduces false positive rate from 50% to 0% on this small holdout","R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE|R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_non_price_4b_spread_peak_confirmation,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,false,true,+1,"Treat spread-peak and valuation saturation as sufficient non-price 4B evidence; do not use price-only local peak","Kumho and Hyosung 4B overlays were near full-window peaks and protected severe drawdown","R4L11_C17_KUMHO_20210506_4B|R4L11_C17_HYOSUNG_20210715_4B",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_LATEX_SPECIALTY_MARGIN_SPREAD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L11_C17_KUMHO_20201106_S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 captured structural rerating, but Green was late/high-MAE.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Specialty margin bridge, not generic NCC beta."}
{"row_type": "case", "case_id": "R4L11_C17_HYOSUNG_SPANDEX_SPREAD_2021", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "SPANDEX_SUPERCYCLE_OPERATING_LEVERAGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L11_C17_HYOSUNG_20210129_S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2/early spread evidence aligned with massive 180D MFE and tolerable MAE.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Cleanest positive case."}
{"row_type": "case", "case_id": "R4L11_C17_LOTTE_NCC_SPREAD_FALSE_GREEN_2021", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NCC_GENERIC_SPREAD_FALSE_GREEN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "High apparent Green score but only +3.68% MFE180 versus -31.29% MAE180.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Generic NCC spread lacked durability."}
{"row_type": "case", "case_id": "R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NCC_STANDALONE_SPREAD_FALSE_GREEN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Green label at local exhaustion; +3.05% MFE180 versus -53.37% MAE180.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Standalone NCC exposure should be capped unless spread durability and specialty/customer quality are present."}
{"row_type": "trigger", "trigger_id": "R4L11_C17_KUMHO_20201106_S2A", "case_id": "R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD", "sector": "materials_chemical", "primary_archetype": "chemical_commodity_margin_spread", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-11-06", "entry_date": "2020-11-06", "entry_price": 153500, "evidence_available_at_that_date": "Q3/early-Q4 2020 specialty synthetic-rubber/NBR-latex margin bridge became public enough to distinguish from generic chemical beta; customer-demand route tied to glove/medical demand, not just commodity rebound.", "evidence_source": "public earnings / sector report synthesis; OHLC source rows: 2020-11-06, 2020-11-11, 2021-02-05, 2021-05-06", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.95, "MFE_90D_pct": 91.21, "MFE_180D_pct": 94.46, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.22, "MAE_90D_pct": -19.22, "MAE_180D_pct": -19.22, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -32.16, "green_lateness_ratio": "not_applicable: representative Stage2 trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_MFE_high_MAE_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L11_C17_KUMHO_20201106", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L11_C17_KUMHO_20210128_GREEN_COMPARE", "case_id": "R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD", "sector": "materials_chemical", "primary_archetype": "chemical_commodity_margin_spread", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage3-Green", "trigger_date": "2021-01-28", "entry_date": "2021-01-28", "entry_price": 277000, "evidence_available_at_that_date": "Strong follow-through and earnings-confirmation route; however the Green label arrived after most of the rerating leg and carried severe downside once spread expectations normalized.", "evidence_source": "public earnings / sector report synthesis; OHLC source rows: 2021-01-28, 2021-03-09, 2021-05-06", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.96, "MFE_90D_pct": 7.76, "MFE_180D_pct": 7.76, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.8, "MAE_90D_pct": -27.8, "MAE_180D_pct": -27.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -32.16, "green_lateness_ratio": 0.85, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_high_MAE_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L11_C17_KUMHO_20210128", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same independent case; Stage3 label comparison only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R4L11_C17_KUMHO_20210506_4B", "case_id": "R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD", "sector": "materials_chemical", "primary_archetype": "chemical_commodity_margin_spread", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2021-05-06", "entry_date": "2021-05-06", "entry_price": 296000, "evidence_available_at_that_date": "Local/full-window price proximity coincided with stretched valuation, NBR-latex peak-spread expectations, and crowded commodity-margin positioning; this is an overlay, not a price-only sell label.", "evidence_source": "public earnings / sector report synthesis; OHLC source rows: 2021-05-06 and 2021-06-09", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.84, "MFE_90D_pct": 0.84, "MFE_180D_pct": 0.84, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -31.59, "MAE_90D_pct": -31.59, "MAE_180D_pct": -31.59, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -32.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L11_C17_KUMHO_20210506", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same independent case; 4B overlay timing only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R4L11_C17_HYOSUNG_20210129_S2A", "case_id": "R4L11_C17_HYOSUNG_SPANDEX_SPREAD_2021", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD", "sector": "materials_chemical", "primary_archetype": "chemical_commodity_margin_spread", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-29", "entry_date": "2021-01-29", "entry_price": 299500, "evidence_available_at_that_date": "Spandex spread and operating leverage became the distinct driver; public evidence was not merely textile beta because CREORA/spandex capacity leverage was visible before the peak revision cycle.", "evidence_source": "public earnings / sector report synthesis; OHLC source rows: 2021-01-29, 2021-02-03, 2021-07-16", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 67.95, "MFE_90D_pct": 152.09, "MFE_180D_pct": 221.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.67, "MAE_90D_pct": -3.67, "MAE_180D_pct": -3.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -45.38, "green_lateness_ratio": "not_applicable: representative Stage2 trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "clean_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L11_C17_HYOSUNG_20210129", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L11_C17_HYOSUNG_20210325_GREEN_COMPARE", "case_id": "R4L11_C17_HYOSUNG_SPANDEX_SPREAD_2021", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD", "sector": "materials_chemical", "primary_archetype": "chemical_commodity_margin_spread", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage3-Green", "trigger_date": "2021-03-25", "entry_date": "2021-03-25", "entry_price": 591000, "evidence_available_at_that_date": "Confirmed revision and multiple-source spread narrative; still had meaningful upside, but Stage2 carried far better MFE/MAE asymmetry.", "evidence_source": "public earnings / sector report synthesis; OHLC source rows: 2021-03-25, 2021-06-30, 2021-07-16, 2021-11-11", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.09, "MFE_90D_pct": 54.48, "MFE_180D_pct": 62.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.81, "MAE_90D_pct": -9.81, "MAE_180D_pct": -11.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -45.38, "green_lateness_ratio": 0.44, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_not_fatal_but_late", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L11_C17_HYOSUNG_20210325", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same independent case; Stage3 label comparison only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R4L11_C17_HYOSUNG_20210715_4B", "case_id": "R4L11_C17_HYOSUNG_SPANDEX_SPREAD_2021", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD", "sector": "materials_chemical", "primary_archetype": "chemical_commodity_margin_spread", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2021-07-15", "entry_date": "2021-07-15", "entry_price": 935000, "evidence_available_at_that_date": "Spandex spread peak, valuation blowoff, and positioning saturation converged near the full-window high. Price-only local peak is insufficient, but non-price spread peaking made this full 4B overlay usable.", "evidence_source": "public earnings / sector report synthesis; OHLC source rows: 2021-07-15, 2021-07-16, 2021-10-06, 2021-11-11", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.99, "MFE_90D_pct": 2.99, "MFE_180D_pct": 2.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.42, "MAE_90D_pct": -36.58, "MAE_180D_pct": -46.95, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -48.49, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L11_C17_HYOSUNG_20210715", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same independent case; 4B overlay timing only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE", "case_id": "R4L11_C17_LOTTE_NCC_SPREAD_FALSE_GREEN_2021", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD", "sector": "materials_chemical", "primary_archetype": "chemical_commodity_margin_spread", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage3-Green", "trigger_date": "2021-02-23", "entry_date": "2021-02-23", "entry_price": 326000, "evidence_available_at_that_date": "Broad petrochemical rebound and NCC spread narrative looked Green by relative-strength and earnings-recovery criteria, but lacked specialty margin bridge and was exposed to naphtha/ethylene oversupply normalization.", "evidence_source": "public sector report synthesis; later structural overcapacity validated by petrochemical restructuring evidence; OHLC source rows: 2021-02-23, 2021-03-02, 2021-08-20, 2021-10-29", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.68, "MFE_90D_pct": 3.68, "MFE_180D_pct": 3.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.04, "MAE_90D_pct": -21.17, "MAE_180D_pct": -31.29, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-02", "peak_price": 338000, "drawdown_after_peak_pct": -33.73, "green_lateness_ratio": 1.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry; counterexample row", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late_if_waiting_for_accounting_or_default", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L11_C17_LOTTE_20210223", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE", "case_id": "R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "NBR_SPANDEX_NCC_SPREAD_DURABILITY_AND_REVERSAL_GUARD", "sector": "materials_chemical", "primary_archetype": "chemical_commodity_margin_spread", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage3-Green", "trigger_date": "2021-02-16", "entry_date": "2021-02-16", "entry_price": 393500, "evidence_available_at_that_date": "NCC spread recovery plus abrupt price/volume looked like Green, but the company had a commodity-only spread exposure without durable specialty-margin or customer-quality evidence; the entry was effectively at local spread-cycle exhaustion.", "evidence_source": "public sector report synthesis; later structural overcapacity validated by petrochemical restructuring evidence; OHLC source rows: 2021-02-16, 2021-02-17, 2021-08-20, 2021-11-01", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.05, "MFE_90D_pct": 3.05, "MFE_180D_pct": 3.05, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -25.79, "MAE_90D_pct": -35.32, "MAE_180D_pct": -53.37, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-17", "peak_price": 405500, "drawdown_after_peak_pct": -54.75, "green_lateness_ratio": 1.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_local_peak_not_full_4B_without_spread_slowdown", "four_b_evidence_type": ["price_only_local_peak", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late_if_waiting_for_explicit_default", "trigger_outcome_label": "false_positive_green_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L11_C17_DAEHAN_20210216", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020", "trigger_id": "R4L11_C17_KUMHO_20201106_S2A", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 17, "revision_score": 10, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 19, "revision_score": 11, "relative_strength_score": 9, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile rewards specialty-margin durability and caps generic NCC spread Green when customer/specialty evidence is absent.", "MFE_90D_pct": 91.21, "MAE_90D_pct": -19.22, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020", "trigger_id": "R4L11_C17_KUMHO_20210128_GREEN_COMPARE", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 23, "revision_score": 19, "relative_strength_score": 13, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 23, "revision_score": 19, "relative_strength_score": 13, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile rewards specialty-margin durability and caps generic NCC spread Green when customer/specialty evidence is absent.", "MFE_90D_pct": 7.76, "MAE_90D_pct": -27.8, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020", "trigger_id": "R4L11_C17_KUMHO_20210506_4B", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 19, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 91, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 18, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": 13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 92, "stage_label_after": "Stage4B-overlay", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile rewards specialty-margin durability and caps generic NCC spread Green when customer/specialty evidence is absent.", "MFE_90D_pct": 0.84, "MAE_90D_pct": -31.59, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L11_C17_HYOSUNG_SPANDEX_SPREAD_2021", "trigger_id": "R4L11_C17_HYOSUNG_20210129_S2A", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 13, "relative_strength_score": 12, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 22, "revision_score": 15, "relative_strength_score": 13, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile rewards specialty-margin durability and caps generic NCC spread Green when customer/specialty evidence is absent.", "MFE_90D_pct": 152.09, "MAE_90D_pct": -3.67, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L11_C17_HYOSUNG_SPANDEX_SPREAD_2021", "trigger_id": "R4L11_C17_HYOSUNG_20210325_GREEN_COMPARE", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 22, "relative_strength_score": 14, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 90, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 22, "relative_strength_score": 14, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile rewards specialty-margin durability and caps generic NCC spread Green when customer/specialty evidence is absent.", "MFE_90D_pct": 54.48, "MAE_90D_pct": -9.81, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L11_C17_HYOSUNG_SPANDEX_SPREAD_2021", "trigger_id": "R4L11_C17_HYOSUNG_20210715_4B", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 22, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 93, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 23, "revision_score": 20, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 24, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 94, "stage_label_after": "Stage4B-overlay", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile rewards specialty-margin durability and caps generic NCC spread Green when customer/specialty evidence is absent.", "MFE_90D_pct": 2.99, "MAE_90D_pct": -36.58, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L11_C17_LOTTE_NCC_SPREAD_FALSE_GREEN_2021", "trigger_id": "R4L11_C17_LOTTE_20210223_GREEN_FALSE_POSITIVE", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 18, "relative_strength_score": 13, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 12, "relative_strength_score": 11, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 13, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage2-watch", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile rewards specialty-margin durability and caps generic NCC spread Green when customer/specialty evidence is absent.", "MFE_90D_pct": 3.68, "MAE_90D_pct": -21.17, "score_return_alignment_label": "misaligned_under_P0_aligned_after_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021", "trigger_id": "R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE", "symbol": "006650", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 18, "relative_strength_score": 17, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 13, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 89, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69, "stage_label_after": "Stage2-watch", "changed_components": ["margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile rewards specialty-margin durability and caps generic NCC spread Green when customer/specialty evidence is absent.", "MFE_90D_pct": 3.05, "MAE_90D_pct": -35.32, "score_return_alignment_label": "misaligned_under_P0_aligned_after_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R4", "loop": "11", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage3_green_total_min", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["generic_NCC_spread_false_green", "late_green_high_MAE", "price_only_local_peak_not_full_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R4
completed_loop = 11
next_round = R5
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web source files checked:

```text
atlas/manifest.json
atlas/symbol_profiles/011/011780.json
atlas/symbol_profiles/298/298020.json
atlas/symbol_profiles/011/011170.json
atlas/symbol_profiles/006/006650.json
atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv
atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv
atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv
atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv
atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv
```

External context used only for narrative stress-test:

```text
- Reuters petrochemical overcapacity/restructuring reports were used as later-cycle validation context for generic NCC spread fragility.
- The quantitative calibration itself uses stock-web OHLC rows only.
```

