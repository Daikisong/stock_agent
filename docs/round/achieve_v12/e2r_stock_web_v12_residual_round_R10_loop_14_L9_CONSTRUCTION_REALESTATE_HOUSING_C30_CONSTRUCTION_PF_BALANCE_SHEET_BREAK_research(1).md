# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R10_loop_14_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
scheduled_round = R10
scheduled_loop = 14
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = CONSTRUCTION_PF_QUALITY_COST_TRUST_BREAK
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
stock_web_price_atlas_access_required = true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`.

Existing axes tested, not blindly re-proposed:

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

The residual question for R10/C30 is not “does 4C need non-price evidence?” That is already accepted. The sharper question is whether **sector-level PF panic** should ever become a company-level Hard 4C without a company-specific default, accounting/trust break, cost quantification, legal sanction, or hard contract failure.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R10 |
| scheduled_loop | 14 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| fine_archetype_id | CONSTRUCTION_PF_QUALITY_COST_TRUST_BREAK |
| round_sector_consistency | pass |
| round_schedule_status | valid |
| next_round | R11 |
| next_loop | 14 |

R10 maps to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The selected canonical archetype is `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`, because the cases separate real thesis breaks from sector-spread fear.

## 3. Previous Coverage / Duplicate Avoidance Check

Search for a direct prior `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` residual file did not return a competing current-loop file in the accessible GitHub search path during this session. The immediately previous locally generated state was R9/Loop 14, which computed the next round as R10/Loop 14. This MD therefore fills the next sequential round.

Novelty gate:

| Gate | Result |
|---|---:|
| minimum_new_independent_case_ratio | pass: 3/3 usable cases |
| minimum_new_symbol_count | pass: 3 |
| minimum_counterexample_count | pass: 1 |
| minimum_positive_case_count | pass: 2 |
| wrong_round_penalty | 0 |
| repeated_same_symbol_penalty | 0 |

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest confirms `FinanceData/marcap` as the upstream source, `raw_unadjusted_marcap` as price adjustment status, min_date `1995-05-02`, max_date `2026-02-20`, and `tradable_row_count` 14,354,401. fileciteturn1048file0L4-L13

The manifest also confirms the calibration shard root `atlas/ohlcv_tradable_by_symbol_year` and raw shard root `atlas/ohlcv_raw_by_symbol_year`. fileciteturn1048file0L39-L45 The schema confirms the tradable shard columns `d,o,h,l,c,v,a,mc,s,m`, and defines MFE/MAE as max-high/min-low from entry_date through N tradable rows. fileciteturn1049file0L17-L28 fileciteturn1049file0L60-L68

| symbol | company | profile_path | profile status |
|---|---|---|---|
| 294870 | HDC현대산업개발 | atlas/symbol_profiles/294/294870.json | active_like, 1888 tradable rows, last_date 2026-02-20, no 2022 window corporate-action contamination |
| 006360 | GS건설 | atlas/symbol_profiles/006/006360.json | active_like, 7761 tradable rows, last_date 2026-02-20, no 2023/2024 window corporate-action contamination |
| 000720 | 현대건설 | atlas/symbol_profiles/000/000720.json | active_like, 7740 tradable rows, last_date 2026-02-20, no 2022/2023 window corporate-action contamination |
| 009410 | 태영건설 | atlas/symbol_profiles/009/009410.json | narrative-only: 2024-10-31 corporate-action candidate blocks extended clean calibration |

HDC’s profile confirms first_date 2018-06-12, last_date 2026-02-20, 1888 tradable rows, and only a 2020-03-26 corporate-action candidate, outside the 2022 window used here. fileciteturn1051file0L23-L38 fileciteturn1051file0L90-L103 GS건설’s profile confirms 7761 tradable rows and no relevant 2023 window corporate-action candidate. fileciteturn1050file0L33-L39 fileciteturn1050file0L215-L230 현대건설’s profile confirms 7740 tradable rows and no relevant 2022/2023 window corporate-action candidate. fileciteturn1052file0L23-L29 fileciteturn1052file0L205-L224

## 5. Historical Eligibility Gate

| case_id | entry row exists | 180D forward rows | 180D corporate-action clean | calibration_usable |
|---|---:|---:|---:|---:|
| C30_HDC_2022_GWANGJU_COLLAPSE | yes | yes | yes | true |
| C30_GS_2023_GEOMDAN_QUALITY_COST_BREAK | yes | yes | yes | true |
| C30_HYUNDAI_EC_2022_PF_SECTOR_SHOCK_COUNTER | yes | yes | yes | true |
| C30_TAEYOUNG_2023_WORKOUT | yes | blocked | no / extended window contaminated | false |

The Taeyoung row is deliberately `narrative_only`: the profile shows a 2024-10-31 corporate-action candidate. fileciteturn1065file0L3-L9 The 2024 shard also has a long tradable gap between 2024-03-13 and 2024-10-31, followed by the corporate-action candidate region. fileciteturn1067file0L47-L54

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| CONSTRUCTION_QUALITY_ACCIDENT_THESIS_BREAK | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Quality accident becomes C30 only when it creates legal, trust, contract, or cost-overrun balance-sheet risk. |
| CONSTRUCTION_QUALITY_ACCIDENT_COST_QUANTIFICATION | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Watch-only site defect should not be promoted until cost/regulatory confirmation appears. |
| CONSTRUCTION_SECTOR_PF_SPREAD_SHOCK_WITHOUT_COMPANY_BREAK | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Sector PF panic is a risk overlay, not Hard 4C, without company-specific break. |
| CONSTRUCTION_WORKOUT_PF_LIQUIDITY_BREAK | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Company workout/default path is direct C30 but requires clean OHLC window for quantitative use. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best trigger | usable | current profile verdict |
|---|---:|---|---|---|---:|---|
| C30_HDC_2022_GWANGJU_COLLAPSE | 294870 | HDC현대산업개발 | 4C_success | 2022-01-12 Hard 4C | true | current_profile_correct |
| C30_GS_2023_GEOMDAN_QUALITY_COST_BREAK | 006360 | GS건설 | 4C_success with timing split | 2023-07-06 Hard 4C | true | current_profile_too_early on watch-only row |
| C30_HYUNDAI_EC_2022_PF_SECTOR_SHOCK_COUNTER | 000720 | 현대건설 | false_positive_green / false 4C | 2022-10-24 sector PF shock | true | current_profile_false_positive |
| C30_TAEYOUNG_2023_WORKOUT | 009410 | 태영건설 | narrative_only | 2023-12-28 workout/liquidity event | false | current_profile_data_insufficient |

HDC event source: the Gwangju Hwajeong I-Park exterior wall collapse occurred on 2022-01-11 and is described as involving HDC Hyundai Development, government investigation, and later findings of faulty methods/materials. citeturn702237search0

Legoland source: the FT result notes that the developer of Legoland Korea defaulted in 2022, triggering a wider corporate credit crunch in South Korea. citeturn930424news0 Taeyoung context source: Reuters reported that Taeyoung Engineering & Construction planned to reschedule debt in December 2023, raising concerns about liquidity trouble at other construction firms. citeturn542068news0

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive hard 4C / risk protection | 2 | HDC현대산업개발, GS건설 |
| counterexample / false 4C | 1 | 현대건설 |
| narrative-only but not weight calibration | 1 | 태영건설 |
| calibration-usable representative cases | 3 | HDC, GS, Hyundai E&C |

## 9. Evidence Source Map

| evidence family | HDC | GS | Hyundai E&C | Taeyoung |
|---|---|---|---|---|
| public event/disclosure | collapse event | Geomdan quality/cost event label | Legoland-sector credit shock | workout/debt rescheduling |
| legal/regulatory option | high | high | sector-only, not company-specific | high |
| cost / balance sheet bridge | implied by trust/orderbook break | confirmed only after cost/reconstruction path | absent | direct liquidity-break but blocked price window |
| company-specific thesis break | yes | yes after cost quantification | no | yes but narrative-only |
| price-only / sector-only risk | no | early stage partly | yes | no |

## 10. Price Data Source Map

| symbol | year | shard |
|---:|---:|---|
| 294870 | 2022 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv |
| 006360 | 2023 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv |
| 006360 | 2024 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv |
| 000720 | 2022 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2022.csv |
| 000720 | 2023 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv |
| 009410 | 2023 | atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv |
| 009410 | 2024 | atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | date | entry | entry_price | Stage2 evidence | Stage4C evidence | representative |
|---|---|---:|---:|---:|---|---|---:|
| HDC_2022_GWANGJU_COLLAPSE_4C | Stage4C | 2022-01-11 | 2022-01-12 | 20850 | public event, regulatory | thesis/trust break | true |
| GS_2023_GEOMDAN_STAGE2_WATCH | Stage2-Actionable | 2023-06-29 | 2023-06-29 | 18600 | public quality event, early risk | none | false |
| GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C | Stage4C | 2023-07-05 | 2023-07-06 | 14520 | public event | cost/trust break | true |
| HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER | Stage4C-Counterexample | 2022-10-24 | 2022-10-24 | 34950 | sector policy/liquidity risk | none | true |
| TAEYOUNG_2023_WORKOUT_NARRATIVE_ONLY | Stage4C-NarrativeOnly | 2023-12-28 | 2023-12-28 | 2315 | public event | liquidity thesis break | false |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| HDC_2022_GWANGJU_COLLAPSE_4C | 20850 | 8.87 | -35.25 | 8.87 | -36.93 | 8.87 | -50.84 | 2022-01-12 | 22700 |
| GS_2023_GEOMDAN_STAGE2_WATCH | 18600 | 3.44 | -28.12 | 3.44 | -31.88 | 3.44 | -31.88 | 2023-07-03 | 19240 |
| GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C | 14520 | 10.12 | -7.92 | 10.12 | -12.74 | 19.83 | -12.74 | 2023-11-23 | 17400 |
| HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER | 34950 | 27.18 | -5.58 | 27.18 | -6.87 | 27.18 | -6.87 | 2022-11-14 | 44450 |
| TAEYOUNG_2023_WORKOUT_NARRATIVE_ONLY | 2315 | 77.54 | -16.41 | null | null | null | null | 2024-01-11 | 4110 |

OHLC row anchors:

- HDC had entry_date 2022-01-12 close 20,850 and immediate low/high path after the 2022-01-11 event. fileciteturn1053file0L10-L18 Later lows through the same 2022 window reached the 10,250~9,790 zone. fileciteturn1055file0L11-L30
- GS건설 had the pre-4C quality-watch row on 2023-06-29 close 18,600, then 2023-07-06 close 14,520 after the hard break row. fileciteturn1056file0L6-L12 The later 2023 path shows recovery highs into November but a prolonged post-event drawdown channel. fileciteturn1057file0L34-L40
- Hyundai E&C had entry_date 2022-10-24 close 34,950, a shallow local low, and recovery to 44,450 by 2022-11-14. fileciteturn1059file0L41-L57
- Taeyoung had entry_date 2023-12-28 close 2,315 and extreme volatility, but the clean quantitative window is blocked. fileciteturn1066file0L27-L29 fileciteturn1067file0L4-L12

## 13. Current Calibrated Profile Stress Test

| case | current profile behavior | actual path | verdict |
|---|---|---|---|
| HDC | Hard 4C on collapse/trust break | severe forward MAE and persistent damage | current_profile_correct |
| GS watch row | may promote watch-only quality event too early | large MAE before cost confirmation | current_profile_too_early |
| GS 4C row | Hard 4C after cost/trust quantification | additional MAE lower than watch row, but gap-down already occurred | current_profile_correct |
| Hyundai E&C | sector PF shock could be overread as 4C | strong MFE and modest MAE | current_profile_false_positive |
| Taeyoung | would be Hard 4C but price-window blocked | not calibration usable | current_profile_data_insufficient |

Answers to required stress-test questions:

1. Current calibrated profile correctly catches true company-specific C30 breaks in HDC and GS hard 4C rows.
2. It can overfire when sector PF panic is mapped to a company-level thesis break.
3. Stage2 bonus is not the issue; the problem is company-specific evidence quality.
4. Yellow 75 is too permissive for C30 when the trigger is sector-only and not company-specific.
5. Green 87 / revision 55 is not the main axis in these risk cases.
6. price-only blowoff guard remains appropriate.
7. full 4B non-price requirement is strengthened.
8. hard 4C routing is correct only when the evidence is company-specific and balance-sheet/trust/contract related.

## 14. Stage2 / Yellow / Green Comparison

| comparison | result |
|---|---|
| GS Stage2-watch vs GS Hard 4C | Watch row entered at 18,600 and produced -31.88% 180D MAE; hard 4C entered at 14,520 and produced -12.74% 180D MAE. |
| HDC Green | no confirmed Green trigger; this is a hard 4C risk case. |
| Hyundai Green/4C false positive | sector panic had positive 180D MFE +27.18%; hard 4C would have overblocked. |

`green_lateness_ratio = not_applicable` for all representative rows because these are 4C/guardrail cases, not confirmed Stage3-Green long triggers.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| HDC_2022_GWANGJU_COLLAPSE_4C | legal/regulatory, trust break | null | null | not 4B; direct 4C |
| GS_2023_GEOMDAN_STAGE2_WATCH | legal/regulatory watch | null | null | watch-only until cost/legal quantification |
| GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C | cost/trust break | null | null | not 4B; direct 4C |
| HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER | price_only + sector spread shock | null | null | do not treat as full 4B/4C |
| TAEYOUNG_2023_WORKOUT_NARRATIVE_ONLY | liquidity/workout | null | null | narrative-only due blocked window |

## 16. 4C Protection Audit

| trigger_id | 4C label | protection interpretation |
|---|---|---|
| HDC_2022_GWANGJU_COLLAPSE_4C | hard_4c_success | Caught severe post-event drawdown. |
| GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C | hard_4c_success | Correctly classified a hard cost/trust break, though the earlier watch row shows lateness. |
| HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER | false_break | Sector-wide shock without company-specific break should not become Hard 4C. |
| TAEYOUNG_2023_WORKOUT_NARRATIVE_ONLY | thesis_break_watch_only | Good narrative sample, not clean quantitative evidence. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_candidate = L9_C30_sector_pf_shock_company_specific_break_gate
```

A construction-sector PF spread shock should be treated as a sector risk overlay unless one of the following is also present:

```text
- company-specific debt rescheduling / workout / covenant breach
- confirmed project-level cost overrun that can affect equity value
- formal sanction, license suspension, or contract cancellation
- accounting/trust break
- forced liquidity event or capital structure impairment
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_candidate = C30_company_specific_thesis_break_required_for_hard_4c
```

For `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`, the proposed shadow rule is:

```text
if trigger is sector_pf_spread_shock_only and no company_specific_thesis_break:
    max_stage = Stage2-Watch
    block_Hard_4C = true

if construction_quality_event and no quantified cost/regulatory/contract consequence:
    max_stage = Stage2-Actionable Risk Watch
    block_positive_Green = true
    block_Hard_4C = true

if construction_quality_event plus quantified reconstruction cost, sanction, license risk, major contract risk, trust/accounting break:
    allow_Hard_4C = true
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | selected representative cases | avg MFE_90D | avg MAE_90D | avg MFE_180D | avg MAE_180D | false_positive_rate | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | HDC, GS, Hyundai | 15.39 | -18.85 | 18.63 | -23.48 | 33.3% | catches true breaks but overreads sector PF shock |
| P0b e2r_2_0_baseline_reference | 3 | HDC, GS, Hyundai | 15.39 | -18.85 | 18.63 | -23.48 | 33.3% | less precise C30 split |
| P1 sector_specific_candidate_profile | 3 | HDC, GS only for Hard 4C; Hyundai watch-only | 9.50 | -24.84 | 14.35 | -31.79 | 0.0% | improves false positive control |
| P2 canonical_archetype_candidate_profile | 3 | company-specific break required | 9.50 | -24.84 | 14.35 | -31.79 | 0.0% | preferred |
| P3 counterexample_guard_profile | 3 | Hyundai blocked from 4C | 9.50 | -24.84 | 14.35 | -31.79 | 0.0% | strongest guard, lower recall risk on Taeyoung-like cases requires narrative-only queue |

## 20. Score-Return Alignment Matrix

| trigger_id | before score | before label | after score | after label | alignment |
|---|---:|---|---:|---|---|
| HDC_2022_GWANGJU_COLLAPSE_4C | 91 | Hard 4C | 96 | Hard 4C | aligned |
| GS_2023_GEOMDAN_STAGE2_WATCH | 76 | Stage3-Yellow/4C-watch | 69 | Stage2-Actionable Risk Watch | improved |
| GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C | 88 | Hard 4C | 93 | Hard 4C | aligned |
| HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER | 78 | Stage3-Yellow false risk / 4C-watch | 58 | Stage2-Watch only | improved |
| TAEYOUNG_2023_WORKOUT_NARRATIVE_ONLY | 92 | Hard 4C narrative-only | 92 | Hard 4C narrative-only | not_weight_calibration |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | CONSTRUCTION_PF_QUALITY_COST_TRUST_BREAK | 2 | 1 | 0 | 2 | 3 | 0 | 4 | 3 | 2 | true | true | still needs more PF workout clean-window samples and more non-accident counterexamples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - company_specific_vs_sector_pf_false_positive
  - quality_watch_vs_cost_quantified_4c_timing
new_axis_proposed:
  - c30_company_specific_thesis_break_required_for_hard_4c
  - c30_quality_watch_requires_cost_or_regulatory_confirmation
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web OHLC entry rows for HDC, GS, Hyundai E&C, Taeyoung
- 30D/90D/180D MFE/MAE for 3 calibration-usable representative cases
- profile-level corporate-action candidate checks
- C30 company-specific break vs sector-only shock distinction
```

Not validated:

```text
- production scoring code
- live candidate scan
- any 2026 current recommendation
- broker or trading path
- Taeyoung quantitative calibration due blocked clean forward window
- formal external source attachment for GS event label; this should be attached in ingestion before promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_company_specific_thesis_break_required_for_hard_4c,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Sector PF panic alone produced a false 4C on Hyundai E&C; HDC/GS show true company-specific break.","reduced false positive while keeping true 4C cases","HDC_2022_GWANGJU_COLLAPSE_4C|GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C|HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_quality_watch_requires_cost_or_regulatory_confirmation,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"GS Stage2-watch row had poor forward MAE before hard cost/trust confirmation.","separates watch-only quality news from hard 4C cost break","GS_2023_GEOMDAN_STAGE2_WATCH|GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C",2,1,0,low,canonical_shadow_only,"needs formal event-source attachment before promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C30_HDC_2022_GWANGJU_COLLAPSE","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_QUALITY_ACCIDENT_THESIS_BREAK","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"HDC_2022_GWANGJU_COLLAPSE_4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C signal aligned with severe forward drawdown","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Clean 180D; construction quality accident generated durable trust/orderbook break."}
{"row_type":"case","case_id":"C30_GS_2023_GEOMDAN_QUALITY_COST_BREAK","symbol":"006360","company_name":"GS건설","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_QUALITY_ACCIDENT_COST_QUANTIFICATION","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C cost-quantification trigger better than early quality-watch trigger","current_profile_verdict":"current_profile_too_early_on_watch_only_evidence","price_source":"Songdaiki/stock-web","notes":"Stage2-watch had large MAE; hard 4C needs cost/legal/trust confirmation."}
{"row_type":"case","case_id":"C30_HYUNDAI_EC_2022_PF_SECTOR_SHOCK_COUNTER","symbol":"000720","company_name":"현대건설","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SECTOR_PF_SPREAD_SHOCK_WITHOUT_COMPANY_BREAK","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Sector PF panic without company-specific break produced positive forward MFE and modest MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A sector credit shock should be watch/risk overlay, not hard company 4C."}
{"row_type":"case","case_id":"C30_TAEYOUNG_2023_WORKOUT","symbol":"009410","company_name":"태영건설","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_WORKOUT_PF_LIQUIDITY_BREAK","case_type":"narrative_only","positive_or_counterexample":"positive_context_only","best_trigger":"TAEYOUNG_2023_WORKOUT_NARRATIVE_ONLY","calibration_usable":false,"is_new_independent_case":false,"reuse_reason":"blocked by insufficient clean 180D window and corporate-action candidate","independent_evidence_weight":0.0,"score_price_alignment":"not_weight_calibration","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Useful for source taxonomy only; not counted as quantitative evidence."}
{"row_type":"trigger","trigger_id":"HDC_2022_GWANGJU_COLLAPSE_4C","case_id":"C30_HDC_2022_GWANGJU_COLLAPSE","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_QUALITY_ACCIDENT_THESIS_BREAK","sector":"construction_real_estate","primary_archetype":"construction quality / brand trust / balance-sheet risk","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2022-01-11","entry_date":"2022-01-12","entry_price":20850,"evidence_available_at_that_date":"Gwangju Hwajeong I-Park exterior wall collapse occurred on 2022-01-11; public safety, investigation, brand trust and orderbook-cancellation risk were immediately relevant.","evidence_source":"Gwangju Hwajeong I-Park exterior wall collapse public event summary; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","legal_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break","forced_liquidation_or_crash"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.87,"MFE_90D_pct":8.87,"MFE_180D_pct":8.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-35.25,"MAE_90D_pct":-36.93,"MAE_180D_pct":-50.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700,"drawdown_after_peak_pct":-56.87,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_full_4C_thesis_break","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_protected_against_large_forward_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HDC_2022_4C_2022-01-12_20850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"GS_2023_GEOMDAN_STAGE2_WATCH","case_id":"C30_GS_2023_GEOMDAN_QUALITY_COST_BREAK","symbol":"006360","company_name":"GS건설","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_QUALITY_ACCIDENT_COST_QUANTIFICATION","sector":"construction_real_estate","primary_archetype":"construction quality / cost overrun / regulatory risk","loop_objective":"yellow_threshold_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-29","entry_date":"2023-06-29","entry_price":18600,"evidence_available_at_that_date":"Geumdan/Geomdan site quality issue had become market-visible before final cost quantification; price collapsed before the July full reconstruction row.","evidence_source":"public event label; formal article/disclosure source should be attached by ingestion agent; stock-web OHLC rows validate price timing.","stage2_evidence_fields":["public_event_or_disclosure","legal_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","legal_or_regulatory_block"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.44,"MFE_90D_pct":3.44,"MFE_180D_pct":3.44,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.12,"MAE_90D_pct":-31.88,"MAE_180D_pct":-31.88,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-03","peak_price":19240,"drawdown_after_peak_pct":-34.15,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only_until_cost_or_thesis_break_confirmation","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"early_quality_event_without_final_cost_quantification_had_bad_forward_MAE","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GS_2023_STAGE2_2023-06-29_18600","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C","case_id":"C30_GS_2023_GEOMDAN_QUALITY_COST_BREAK","symbol":"006360","company_name":"GS건설","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_QUALITY_ACCIDENT_COST_QUANTIFICATION","sector":"construction_real_estate","primary_archetype":"construction quality / cost overrun / regulatory risk","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2023-07-05","entry_date":"2023-07-06","entry_price":14520,"evidence_available_at_that_date":"Full reconstruction/cost-quantification path turned the event from quality-watch into hard cost/trust thesis break.","evidence_source":"public event label; formal article/disclosure source should be attached by ingestion agent; stock-web OHLC rows validate price timing.","stage2_evidence_fields":["public_event_or_disclosure","legal_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.12,"MFE_90D_pct":10.12,"MFE_180D_pct":19.83,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.92,"MAE_90D_pct":-12.74,"MAE_180D_pct":-12.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-23","peak_price":17400,"drawdown_after_peak_pct":-19.54,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_full_4C_cost_trust_break","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_after_cost_quantification_reduced_additional_MAE_but_arrived_after_initial_gap_down","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GS_2023_4C_2023-07-06_14520","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER","case_id":"C30_HYUNDAI_EC_2022_PF_SECTOR_SHOCK_COUNTER","symbol":"000720","company_name":"현대건설","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SECTOR_PF_SPREAD_SHOCK_WITHOUT_COMPANY_BREAK","sector":"construction_real_estate","primary_archetype":"sector PF spread shock / no company-specific thesis break","loop_objective":"residual_false_positive_mining","trigger_type":"Stage4C-Counterexample","trigger_date":"2022-10-24","entry_date":"2022-10-24","entry_price":34950,"evidence_available_at_that_date":"Legoland-related Korean credit-market shock created sector PF fear, but this row intentionally lacks company-specific default, accounting break, or hard contract cancellation evidence for Hyundai E&C.","evidence_source":"Legoland Korea credit crunch source; stock-web OHLC rows.","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2022.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.18,"MFE_90D_pct":27.18,"MFE_180D_pct":27.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.58,"MAE_90D_pct":-6.87,"MAE_180D_pct":-6.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-11-14","peak_price":44450,"drawdown_after_peak_pct":-26.77,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"sector_shock_price_only_or_policy_rescue_not_full_4C","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break","trigger_outcome_label":"false_positive_4C_counterexample_positive_forward_return","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HYUNDAI_2022_COUNTER_2022-10-24_34950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TAEYOUNG_2023_WORKOUT_NARRATIVE_ONLY","case_id":"C30_TAEYOUNG_2023_WORKOUT","symbol":"009410","company_name":"태영건설","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_WORKOUT_PF_LIQUIDITY_BREAK","sector":"construction_real_estate","primary_archetype":"workout / PF liquidity break","loop_objective":"coverage_gap_fill","trigger_type":"Stage4C-NarrativeOnly","trigger_date":"2023-12-28","entry_date":"2023-12-28","entry_price":2315,"evidence_available_at_that_date":"Taeyoung E&C debt rescheduling/workout concern raised as a company-specific builder liquidity event, but stock-web 180D window is blocked by trading gap and 2024 corporate-action candidate.","evidence_source":"Reuters 2024 construction liquidity context; stock-web profile and OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["capital_raise_or_overhang","legal_or_regulatory_block"],"stage4c_evidence_fields":["forced_liquidation_or_crash","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv","profile_path":"atlas/symbol_profiles/009/009410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":77.54,"MFE_90D_pct":null,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.41,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":null,"peak_date":"2024-01-11","peak_price":4110,"drawdown_after_peak_pct":null,"green_lateness_ratio":"not_applicable:narrative_only","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"blocked_by_trading_gap_and_corporate_action_candidate","four_b_evidence_type":["capital_raise_or_overhang","legal_or_regulatory_block"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"narrative_only_price_window_blocked","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":false,"forward_window_trading_days":null,"calibration_block_reasons":["insufficient_clean_forward_180D_window_in_stock_web","corporate_action_candidate_2024-10-31_if_window_extended"],"corporate_action_window_status":"blocked_or_unavailable_180D_window","same_entry_group_id":"TAEYOUNG_2023_4C_2023-12-28_2315","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"narrative_only_blocked_window","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_HDC_2022_GWANGJU_COLLAPSE","trigger_id":"HDC_2022_GWANGJU_COLLAPSE_4C","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-5,"revision_score":-5,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":22,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":22},"weighted_score_before":91,"stage_label_before":"Hard 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-5,"revision_score":-5,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":24,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":24},"weighted_score_after":96,"stage_label_after":"Hard 4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Research proxy only. Proposed C30 guard requires company-specific thesis break for Hard 4C and downgrades sector-only PF panic to watch/risk overlay.","MFE_90D_pct":8.87,"MAE_90D_pct":-36.93,"score_return_alignment_label":"hard_4c_protected_against_large_forward_drawdown","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_GS_2023_GEOMDAN_QUALITY_COST_BREAK","trigger_id":"GS_2023_GEOMDAN_STAGE2_WATCH","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":-2,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":18,"legal_or_contract_risk_score":16,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow/4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":-2,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":15,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable Risk Watch","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Research proxy only. Proposed C30 guard requires company-specific thesis break for Hard 4C and downgrades sector-only PF panic to watch/risk overlay.","MFE_90D_pct":3.44,"MAE_90D_pct":-31.88,"score_return_alignment_label":"early_quality_event_without_final_cost_quantification_had_bad_forward_MAE","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_GS_2023_GEOMDAN_QUALITY_COST_BREAK","trigger_id":"GS_2023_GEOMDAN_FULL_RECONSTRUCTION_4C","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-8,"revision_score":-4,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":22,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":18},"weighted_score_before":88,"stage_label_before":"Hard 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-8,"revision_score":-4,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":24,"legal_or_contract_risk_score":24,"dilution_cb_risk_score":0,"accounting_trust_risk_score":20},"weighted_score_after":93,"stage_label_after":"Hard 4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Research proxy only. Proposed C30 guard requires company-specific thesis break for Hard 4C and downgrades sector-only PF panic to watch/risk overlay.","MFE_90D_pct":10.12,"MAE_90D_pct":-12.74,"score_return_alignment_label":"4C_after_cost_quantification_reduced_additional_MAE_but_arrived_after_initial_gap_down","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_HYUNDAI_EC_2022_PF_SECTOR_SHOCK_COUNTER","trigger_id":"HYUNDAI_EC_2022_LEGOLAND_PF_SECTOR_SHOCK_COUNTER","symbol":"000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow false risk / 4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-Watch only","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Research proxy only. Proposed C30 guard requires company-specific thesis break for Hard 4C and downgrades sector-only PF panic to watch/risk overlay.","MFE_90D_pct":27.18,"MAE_90D_pct":-6.87,"score_return_alignment_label":"false_positive_4C_counterexample_positive_forward_return","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_TAEYOUNG_2023_WORKOUT","trigger_id":"TAEYOUNG_2023_WORKOUT_NARRATIVE_ONLY","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":24,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":14,"accounting_trust_risk_score":18},"weighted_score_before":92,"stage_label_before":"Hard 4C narrative-only","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":24,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":14,"accounting_trust_risk_score":18},"weighted_score_after":92,"stage_label_after":"Hard 4C narrative-only","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Research proxy only. Proposed C30 guard requires company-specific thesis break for Hard 4C and downgrades sector-only PF panic to watch/risk overlay.","MFE_90D_pct":null,"MAE_90D_pct":null,"score_return_alignment_label":"narrative_only_price_window_blocked","current_profile_verdict":"current_profile_data_insufficient"}
{"row_type":"residual_contribution","round":"R10","loop":"14","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["hard_4c_thesis_break_routes_to_4c","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["company_specific_vs_sector_pf_false_positive","quality_watch_vs_cost_quantified_4c_timing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C30_TAEYOUNG_2023_WORKOUT","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"evidence_available_but_forward_180D_unavailable_or_stock_web_price_window_blocked","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R10
completed_loop = 14
next_round = R11
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest and schema were used as the price source authority.
- HDC event source was retrieved through web search and used only to anchor trigger timing, not as investment evidence.
- Legoland and Taeyoung external sources were retrieved to distinguish sector-wide PF spread shock from company-specific liquidity break.
- GS event label needs formal article/disclosure attachment during ingestion. The OHLC path itself is validated from stock-web, but source confidence for the narrative label is marked lower than HDC/Hyundai/Taeyoung.
- No live scan, recommendation, or production scoring patch was performed.
