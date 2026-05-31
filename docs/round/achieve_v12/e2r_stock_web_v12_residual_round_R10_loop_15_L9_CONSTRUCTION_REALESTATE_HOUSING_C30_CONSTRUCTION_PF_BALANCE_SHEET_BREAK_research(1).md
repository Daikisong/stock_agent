# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R10
scheduled_loop: 15
completed_round: R10
completed_loop: 15
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD
output_file: e2r_stock_web_v12_residual_round_R10_loop_15_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **4** new independent cases, **2** counterexamples, and **4** residual errors for **R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK**.

## 1. Current Calibrated Profile Assumption

| axis | assumed current value | status in this MD |
|---|---:|---|
| stage2_actionable_evidence_bonus | +2.0 | existing_axis_tested |
| stage3_yellow_total_min | 75.0 | existing_axis_kept |
| stage3_green_total_min | 87.0 | existing_axis_kept |
| stage3_green_revision_min | 55.0 | existing_axis_kept |
| stage3_cross_evidence_green_buffer | +1.5 | existing_axis_kept |
| price_only_blowoff_blocks_positive_stage | true | existing_axis_strengthened |
| full_4b_requires_non_price_evidence | true | existing_axis_strengthened |
| hard_4c_thesis_break_routes_to_4c | true | existing_axis_kept |

This MD does not re-prove the global Stage2 bonus. The residual question is narrower: in C30, can a broad PF-policy headline or construction/property price spike be promoted as positive evidence without company-specific survival, refinancing, margin, or trust-repair evidence? The backtest says no.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R10 |
| scheduled_loop | 15 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| fine_archetype_id | CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD |
| round_sector_consistency | pass |
| R10 mapping rationale | R10 is the required construction / real-estate / housing round. C30 is the canonical PF-balance-sheet and thesis-break archetype. |

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 registry shows R10 Loop 10~14 already used HDC현대산업개발, GS건설, 태영건설, 대우건설, 신세계건설, DL이앤씨, 계룡건설, 동부건설, and 현대건설. This loop avoids those symbols and selects four new symbols in the same canonical archetype.

| prior R10 coverage | dominant symbol family | avoided in this loop |
|---|---|---|
| Loop 10 | HDC / GS / Taeyoung quality and workout | yes |
| Loop 11 | Daewoo / Shinsegae / DL / Kyeryong / Dongbu policy support | yes |
| Loop 12 | Hyundai E&C / Daewoo / GS / HDC / Taeyoung | yes |
| Loop 13 | HDC / GS / Daewoo / Hyundai E&C / Taeyoung | yes |
| Loop 14 | HDC / GS / Hyundai E&C / Taeyoung | yes |
| Loop 15 | Seohee / Hanshin / Kumho / Kolon Global | new symbols |

```text
minimum_new_independent_case_ratio = 1.00
minimum_new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
reused_case_count = 0
wrong_round_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | observed value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The schema confirms tradable shard columns `d,o,h,l,c,v,a,mc,s,m`. MFE and MAE are computed from max high / min low from entry date through N tradable rows. This MD uses `tradable_raw` only for quantitative rows.

## 5. Historical Eligibility Gate

| symbol | company | profile path | profile status | representative entry | 180D usable? | corporate-action status |
|---:|---|---|---|---|---:|---|
| 035890 | 서희건설 | atlas/symbol_profiles/035/035890.json | old corporate-action candidates end 2012-07-12; tradable rows through 2025-08-11 | 2024-08-16 | true | clean_180D_window |
| 004960 | 한신공영 | atlas/symbol_profiles/004/004960.json | old corporate-action candidates end 2002-11-14; tradable rows through 2026-02-20 | 2024-07-16 | true | clean_180D_window |
| 002990 | 금호건설 | atlas/symbol_profiles/002/002990.json | old corporate-action candidates end 2013-11-07; tradable rows through 2026-02-20 | 2024-03-27 | true | clean_180D_window |
| 003070 | 코오롱글로벌 | atlas/symbol_profiles/003/003070.json | corporate-action candidates include 2023-01-31 and 2025-12-11; 2024-06-20~D+180 is clean | 2024-06-20 | true | clean_180D_window |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| CONSTRUCTION_SURVIVOR_MARGIN_REPAIR_AFTER_PF_RESTRUCTURING | C30 | positive path requires company-specific survival/margin evidence, not just sector policy |
| PUBLIC_WORKS_BALANCE_SHEET_SURVIVOR_HIGH_MAE | C30 | public-work/policy support can work but small-cap construction requires MAE guard |
| POLICY_BETA_WITHOUT_COMPANY_REPAIR_FALSE_POSITIVE | C30 | broad government support is watch evidence unless refinancing/margin repair is company-specific |
| PRICE_ONLY_PROPERTY_THEME_BLOWOFF | C30 | property-theme price spikes are 4B-watch only and cannot promote Stage2/3 |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | polarity | best trigger | calibration_usable | current profile verdict |
|---|---:|---|---|---|---|---:|---|
| R10L15_C30_SEOHEE_202408_H1_SURVIVOR_MARGIN_REPAIR | 035890 | 서희건설 | structural_success | positive | R10L15_T01_SEOHEE_STAGE2_H1_SURVIVOR_MARGIN_REPAIR | true | current_profile_missed_structural |
| R10L15_C30_HANSHIN_202407_PUBLIC_WORKS_HIGH_MAE_SUCCESS | 004960 | 한신공영 | high_mae_success | positive | R10L15_T02_HANSHIN_STAGE2_PUBLIC_WORKS_BALANCE_SURVIVOR | true | current_profile_too_early |
| R10L15_C30_KUMHO_202403_POLICY_BETA_FALSE_POSITIVE | 002990 | 금호건설 | failed_rerating | counterexample | R10L15_T03_KUMHO_STAGE2_POLICY_BETA_FALSE_POSITIVE | true | current_profile_false_positive |
| R10L15_C30_KOLON_202406_PRICE_ONLY_PROPERTY_THEME_BLOWOFF | 003070 | 코오롱글로벌 | price_moved_without_evidence | counterexample | R10L15_T04_KOLON_4B_PRICE_ONLY_PROPERTY_THEME_BLOWOFF | true | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive structural / survivor success | 1 | 서희건설 |
| positive but high-MAE success | 1 | 한신공영 |
| counterexample / policy-only failed rerating | 1 | 금호건설 |
| counterexample / price-only blowoff failed | 1 | 코오롱글로벌 |
| 4B case count | 2 | 한신공영 watch, 코오롱글로벌 blowoff |
| 4C case count | 0 | no new hard 4C; this loop is focused on avoiding false positive promotion |

The balance is usable: two positive paths show that C30 should not mechanically reject construction survivors; two counterexamples show why the rule must demand company-specific evidence.

## 9. Evidence Source Map

| case | trigger_date | evidence at trigger | Stage2 | Stage3 | 4B | 4C |
|---|---|---|---|---|---|---|
| 서희건설 | 2024-08-16 | mid-August H1 filing / survivor-margin repair after PF restructuring rules | public_event_or_disclosure, relative_strength, financial_visibility | margin_bridge, financial_visibility | none | none |
| 한신공영 | 2024-07-16 | H2 public-sector/construction support context; small-cap survivor setup | public_event_or_disclosure, policy option, relative strength | limited financial visibility | positioning_overheat | none |
| 금호건설 | 2024-03-27 | builder liquidity support headline without company-specific repair | public_event_or_disclosure, policy option | none | margin/backlog slowdown watch | none |
| 코오롱글로벌 | 2024-06-20 | price-only property/construction blowoff without verified company repair | relative strength only | none | valuation_blowoff, positioning_overheat, price_only_local_peak | none |

External source anchors used for context:
- Reuters, 2024-03-27: Korea prepared support for builders through guarantees, loans, and market-stabilization support.
- Reuters, 2024-05-13: Korea tightened real-estate PF restructuring assessments and noted rising project-financing delinquency.
- Reuters, 2024-07-03: Korea announced additional public-sector investment and policy financing to revive construction.
- Reuters, 2024-07-18: Korea aimed to stabilize housing and accelerate PF restructuring.

Company-specific filing URLs should be attached by the later ingestion agent; this MD uses those sources only as historical context plus Stock-Web OHLC for return validation.

## 10. Price Data Source Map

| symbol | price shard checked | sample row anchors used |
|---:|---|---|
| 035890 | atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv and 2025.csv | 2024-08-16 close 1377; 2024-12-18 high 1680; 2025-04-22 high 1791 |
| 004960 | atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv and 2025.csv | 2024-07-16 close 6790; 2024-11-12 high 7970; 2025-03-31 low 5770 |
| 002990 | atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv | 2024-03-27 close 4520; 2024-06-18 high 4780; 2024-10-18 low approx 3055 |
| 003070 | atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv | 2024-06-20 close 15740; 2024-06-21 high 16110; 2024-08-05 low 8500 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| R10L15_T01_SEOHEE_STAGE2_H1_SURVIVOR_MARGIN_REPAIR | 035890 | 서희건설 | Stage2-Actionable | 2024-08-16 | 1,377 | 14.16% | -1.16% | 22.00% | -1.45% | 30.07% | -1.45% | current_profile_missed_structural |
| R10L15_T02_HANSHIN_STAGE2_PUBLIC_WORKS_BALANCE_SURVIVOR | 004960 | 한신공영 | Stage2-Actionable | 2024-07-16 | 6,790 | 11.34% | -9.28% | 17.38% | -9.28% | 17.38% | -15.02% | current_profile_too_early |
| R10L15_T03_KUMHO_STAGE2_POLICY_BETA_FALSE_POSITIVE | 002990 | 금호건설 | Stage2-Actionable | 2024-03-27 | 4,520 | 0.88% | -9.96% | 5.75% | -29.09% | 5.75% | -32.41% | current_profile_false_positive |
| R10L15_T04_KOLON_4B_PRICE_ONLY_PROPERTY_THEME_BLOWOFF | 003070 | 코오롱글로벌 | Stage4B-Watch | 2024-06-20 | 15,740 | 2.35% | -38.50% | 2.35% | -46.00% | 2.35% | -46.00% | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger rows

| symbol | entry | 30D high / low | 90D high / low | 180D high / low | peak | drawdown after peak |
|---:|---|---|---|---|---|---:|
| 035890 | 2024-08-16 / 1,377 | 1,572 / 1,361 | 1,680 / 1,357 | 1,791 / 1,357 | 2025-04-22 / 1,791 | -23.12% |
| 004960 | 2024-07-16 / 6,790 | 7,560 / 6,160 | 7,970 / 6,160 | 7,970 / 5,770 | 2024-11-12 / 7,970 | -27.60% |
| 002990 | 2024-03-27 / 4,520 | 4,560 / 4,070 | 4,780 / 3,205 | 4,780 / 3,055 | 2024-06-18 / 4,780 | -36.09% |
| 003070 | 2024-06-20 / 15,740 | 16,110 / 9,680 | 16,110 / 8,500 | 16,110 / 8,500 | 2024-06-21 / 16,110 | -47.24% |

`MFE_1Y_pct` and `MFE_2Y_pct` are left null in machine rows for this MD because the promoted quantitative scope is 30D/90D/180D. This prevents accidental use of mixed 1Y/2Y windows when the loop objective is residual trigger calibration.

## 13. Current Calibrated Profile Stress Test

| case | current profile would likely do | actual alignment | residual verdict |
|---|---|---|---|
| 서희건설 | under-promote because revision evidence is still partial | 90D MFE 22.00% with MAE -1.45% | current_profile_missed_structural |
| 한신공영 | promote too quickly on policy/relative strength | positive MFE but MAE -15.02% by 180D | current_profile_too_early |
| 금호건설 | over-promote broad builder support as Stage2/Yellow | 180D MFE 5.75% vs MAE -32.41% | current_profile_false_positive |
| 코오롱글로벌 | over-promote price momentum / property theme | 90D MFE 2.35% vs MAE -46.00% | current_profile_false_positive |

Answers to required stress questions:
1. Current calibrated profile is directionally right on price-only guards but too permissive on broad policy beta inside C30.
2. The survivor case aligned with returns; policy-only and price-only cases did not.
3. Stage2 bonus is useful only after company-level survival evidence.
4. Yellow threshold 75 is too low for C30 policy-only headlines.
5. Green 87 / revision 55 should remain strict; this loop does not weaken it.
6. Price-only blowoff guard is appropriate and strengthened.
7. Full 4B non-price requirement remains correct; price-only is watch/overlay, not full thesis exit.
8. Hard 4C routing is not changed here; no new hard 4C row is proposed.

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 / watch row | Stage3-Yellow risk | Green audit |
|---:|---|---|---|
| 035890 | Stage2-Actionable survivor repair worked | Yellow would be justified after margin evidence | no confirmed Green row; lateness not calculated |
| 004960 | Stage2 worked but with high MAE | Yellow should be capped below Green until financing spread improves | no confirmed Green row |
| 002990 | broad policy Stage2 failed | Yellow would be false positive | Green blocked |
| 003070 | price-only Stage2/Yellow failed | price-only blowoff should be 4B-watch | Green blocked |

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local proximity | full-window proximity | verdict |
|---:|---|---:|---:|---|
| 035890 | none | null | null | not_4B_entry_stage_positive |
| 004960 | price_only / positioning_overheat | 0.99 | 0.99 | price spike requires non-price confirmation before full 4B |
| 002990 | margin/backlog slowdown watch | 0.99 | 0.99 | broad policy beta should be 4B-watch, not positive Stage2 |
| 003070 | price_only / valuation_blowoff / positioning_overheat | 0.98 | 0.98 | good 4B-watch; not positive Stage2/3 |

The split matters: 코오롱글로벌 had near-perfect local/full-window peak proximity, but the evidence type was price-only. It is a good risk overlay, not a positive calibration row.

## 16. 4C Protection Audit

No new hard 4C row is proposed. Gold-label 4C cases were already covered in prior R10 loops. This loop contributes a different residual: false positive prevention before a row becomes Hard 4C. `four_c_protection_label` is therefore `not_applicable`, `thesis_break_watch_only`, or `false_break_watch_only`.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_sector_specific_rule
sector_specific_rule_candidate = false
```

The evidence is all within L9, but the sharper contribution is canonical C30-specific. A sector-level rule would be too coarse because one positive survivor and one high-MAE survivor coexist with two severe false positives.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
new_axis_proposed = c30_survivor_repair_boost_and_policy_price_only_guard
```

Candidate rule:

```text
For C30, broad construction/PF policy support is Stage2-watch only unless at least one company-specific survivor signal exists:
- refinancing / guarantee / debt maturity relief tied to the issuer,
- margin or cash-flow recovery,
- backlog/order visibility that can absorb PF stress,
- clear quality/legal trust repair after prior break.

Price-only property-theme blowoff cannot promote Stage2/Stage3. It can only create 4B-watch unless non-price evidence confirms durable rerating.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | score-return alignment |
|---|---|---:|---:|---:|---:|---:|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 11.87% | -21.46% | 13.89% | -23.72% | 2/4 | mixed: positive survivor found but policy/price-only false positives remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 11.87% | -21.46% | 13.89% | -23.72% | 3/4 | worse: price-only blowoff and policy beta overpromoted |
| P1_sector_specific_candidate_profile | sector_specific | 3 | 15.04% | -13.27% | 17.73% | -16.29% | 1/3 | improves by excluding pure price-only blowoff |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 2 | 19.69% | -5.37% | 23.73% | -8.24% | 0/2 | best score-return alignment on this loop |
| P3_counterexample_guard_profile | guard_profile | 1 | 22.00% | -1.45% | 30.07% | -1.45% | 0/1 | safest but too restrictive |

## 20. Score-Return Alignment Matrix

| symbol | company | before score | before stage | after score | after stage | MFE90 | MAE90 | alignment |
|---:|---|---:|---|---:|---|---:|---:|---|
| 035890 | 서희건설 | 76 | Stage3-Yellow borderline / not Green | 84 | Stage3-Yellow survivor-positive shadow | 22.00% | -1.45% | good_score_return_alignment |
| 004960 | 한신공영 | 78 | Stage3-Yellow early | 74 | Stage2-Actionable high-MAE watch | 17.38% | -9.28% | positive_but_mae_guard_required |
| 002990 | 금호건설 | 77 | Stage3-Yellow false positive | 59 | Stage2-Watch / no positive promotion | 5.75% | -29.09% | false_positive_policy_beta |
| 003070 | 코오롱글로벌 | 82 | Stage3-Yellow false price-momentum promotion | 55 | 4B-Watch / no Stage2-3 promotion | 2.35% | -46.00% | price_only_guard_aligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD | 2 | 2 | 2 | 0 | 4 | 0 | 4 | 4 | 4 | false | true | fewer small/mid-cap C30 policy-only false positives remain; add future cases if new clean windows appear |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_too_early
  - current_profile_false_positive
new_axis_proposed:
  - c30_survivor_repair_boost_and_policy_price_only_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Scheduled round: R10 / Loop 15.
- Round-sector pair: R10 maps to L9.
- Stock-Web manifest/schema.
- Symbol profiles for 035890, 004960, 002990, 003070.
- Tradable raw OHLC rows around each entry and forward 180D windows.
- 30D/90D/180D MFE/MAE and peak/drawdown.
- Positive/counterexample balance.
- Current calibrated profile stress test.
- Raw component score breakdown.

Not validated:
- No live candidate discovery.
- No stock_agent source code opened.
- No production scoring changed.
- No brokerage/API or auto-trading logic.
- No 1Y/2Y quantitative calibration used in this loop.
- Company-specific DART filing URLs are source-enrichment tasks for the later ingestion agent.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_survivor_repair_requires_company_specific_margin_or_liquidity_evidence,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"서희건설 worked only after company-level survivor/margin evidence; 금호건설 failed when only broad policy beta existed.","raises alignment by selecting survivor repair and blocking policy-only promotion","R10L15_T01_SEOHEE_STAGE2_H1_SURVIVOR_MARGIN_REPAIR|R10L15_T03_KUMHO_STAGE2_POLICY_BETA_FALSE_POSITIVE",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_price_only_property_theme_blowoff_blocks_stage2_stage3_promotion,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"코오롱글로벌 blowoff had 2.35% MFE90 but -46.00% MAE90; price-only relative strength must be 4B-watch, not positive stage.","reduces false positive and high-MAE entries","R10L15_T04_KOLON_4B_PRICE_ONLY_PROPERTY_THEME_BLOWOFF",4,4,1,medium,canonical_shadow_only,"strengthens existing price-only blowoff guard within C30"
shadow_weight,c30_high_mae_smallcap_construction_success_caps_green,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"한신공영 positive return came with -15.02% MAE180; small-cap construction survivor rows need watch sizing until financing spread tightens.","keeps positive but prevents premature Green","R10L15_T02_HANSHIN_STAGE2_PUBLIC_WORKS_BALANCE_SURVIVOR",4,4,0,low,canonical_shadow_only,"risk-size/Green cap only; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R10L15_C30_SEOHEE_202408_H1_SURVIVOR_MARGIN_REPAIR","symbol":"035890","company_name":"서희건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R10L15_T01_SEOHEE_STAGE2_H1_SURVIVOR_MARGIN_REPAIR","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_score_return_alignment","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"survivor_margin_repair_positive"}
{"row_type":"case","case_id":"R10L15_C30_HANSHIN_202407_PUBLIC_WORKS_HIGH_MAE_SUCCESS","symbol":"004960","company_name":"한신공영","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R10L15_T02_HANSHIN_STAGE2_PUBLIC_WORKS_BALANCE_SURVIVOR","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_mae_guard_required","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"positive_but_high_mae_success"}
{"row_type":"case","case_id":"R10L15_C30_KUMHO_202403_POLICY_BETA_FALSE_POSITIVE","symbol":"002990","company_name":"금호건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R10L15_T03_KUMHO_STAGE2_POLICY_BETA_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_policy_beta","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"policy_headline_without_company_repair_failed"}
{"row_type":"case","case_id":"R10L15_C30_KOLON_202406_PRICE_ONLY_PROPERTY_THEME_BLOWOFF","symbol":"003070","company_name":"코오롱글로벌","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R10L15_T04_KOLON_4B_PRICE_ONLY_PROPERTY_THEME_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_only_guard_aligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"price_only_blowoff_large_forward_drawdown"}
{"row_type":"trigger","trigger_id":"R10L15_T01_SEOHEE_STAGE2_H1_SURVIVOR_MARGIN_REPAIR","case_id":"R10L15_C30_SEOHEE_202408_H1_SURVIVOR_MARGIN_REPAIR","symbol":"035890","company_name":"서희건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD","sector":"construction_real_estate_housing","primary_archetype":"construction PF / survivor balance sheet / price-only property theme guard","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-16","evidence_available_at_that_date":"mid-August 2024 semiannual filing / market-visible survival signal after the May PF restructuring rules; stock began to price a self-funded survivor rather than generic sector beta.","evidence_source":"DART semiannual filing timing label; Reuters 2024-05-13 PF restructuring context; Stock-Web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","financial_visibility","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv","profile_path":"atlas/symbol_profiles/035/035890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-16","entry_price":1377,"MFE_30D_pct":14.16,"MFE_90D_pct":22.0,"MFE_180D_pct":30.07,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.16,"MAE_90D_pct":-1.45,"MAE_180D_pct":-1.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-04-22","peak_price":1791,"drawdown_after_peak_pct":-23.12,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry_stage_positive","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"survivor_margin_repair_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L15_035890_2024-08-16_1377","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L15_T02_HANSHIN_STAGE2_PUBLIC_WORKS_BALANCE_SURVIVOR","case_id":"R10L15_C30_HANSHIN_202407_PUBLIC_WORKS_HIGH_MAE_SUCCESS","symbol":"004960","company_name":"한신공영","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD","sector":"construction_real_estate_housing","primary_archetype":"construction PF / survivor balance sheet / price-only property theme guard","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-16","evidence_available_at_that_date":"second-half policy/public-work support and balance-sheet survivor setup became visible, but liquidity and small-cap construction beta created a deep interim drawdown.","evidence_source":"Reuters 2024-07-03 public-sector investment / construction support context; Stock-Web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv","profile_path":"atlas/symbol_profiles/004/004960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-16","entry_price":6790,"MFE_30D_pct":11.34,"MFE_90D_pct":17.38,"MFE_180D_pct":17.38,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.28,"MAE_90D_pct":-9.28,"MAE_180D_pct":-15.02,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":7970,"drawdown_after_peak_pct":-27.6,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"price_spike_needs_non_price_confirmation_before_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_but_high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L15_004960_2024-07-16_6790","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L15_T03_KUMHO_STAGE2_POLICY_BETA_FALSE_POSITIVE","case_id":"R10L15_C30_KUMHO_202403_POLICY_BETA_FALSE_POSITIVE","symbol":"002990","company_name":"금호건설","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD","sector":"construction_real_estate_housing","primary_archetype":"construction PF / survivor balance sheet / price-only property theme guard","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","evidence_available_at_that_date":"government liquidity support for builders was public, but company-level margin/PF repair was not independently confirmed; broad policy beta failed to protect against large drawdown.","evidence_source":"Reuters 2024-03-27 builder support context; Stock-Web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv","profile_path":"atlas/symbol_profiles/002/002990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":4520,"MFE_30D_pct":0.88,"MFE_90D_pct":5.75,"MFE_180D_pct":5.75,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.96,"MAE_90D_pct":-29.09,"MAE_180D_pct":-32.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":4780,"drawdown_after_peak_pct":-36.09,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"policy_beta_should_be_4B_watch_not_positive_stage","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_headline_without_company_repair_failed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L15_002990_2024-03-27_4520","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L15_T04_KOLON_4B_PRICE_ONLY_PROPERTY_THEME_BLOWOFF","case_id":"R10L15_C30_KOLON_202406_PRICE_ONLY_PROPERTY_THEME_BLOWOFF","symbol":"003070","company_name":"코오롱글로벌","round":"R10","loop":"15","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_SURVIVOR_POLICY_BETA_AND_PRICE_ONLY_BLOWOFF_GUARD","sector":"construction_real_estate_housing","primary_archetype":"construction PF / survivor balance sheet / price-only property theme guard","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage4B-Watch","trigger_date":"2024-06-20","evidence_available_at_that_date":"sharp construction/property-theme price blowoff without a verified company-specific PF repair, contract conversion, or balance-sheet thesis repair.","evidence_source":"Stock-Web OHLC rows; Reuters 2024-05-13/2024-07-18 PF restructuring and housing-supply policy context; formal company-specific source enrichment required.","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv","profile_path":"atlas/symbol_profiles/003/003070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-20","entry_price":15740,"MFE_30D_pct":2.35,"MFE_90D_pct":2.35,"MFE_180D_pct":2.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-38.5,"MAE_90D_pct":-46.0,"MAE_180D_pct":-46.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":16110,"drawdown_after_peak_pct":-47.24,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_4B_watch_price_only_not_positive_stage","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"false_break_watch_only","trigger_outcome_label":"price_only_blowoff_large_forward_drawdown","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L15_003070_2024-06-20_15740","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L15_C30_SEOHEE_202408_H1_SURVIVOR_MARGIN_REPAIR","trigger_id":"R10L15_T01_SEOHEE_STAGE2_H1_SURVIVOR_MARGIN_REPAIR","symbol":"035890","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":14,"revision_score":8,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow borderline / not Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":18,"revision_score":10,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":9,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow survivor-positive shadow","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Research proxy only. C30 shadow separates self-funded survivor repair from generic policy beta and blocks price-only property-theme blowoff from Stage2/Stage3 promotion.","MFE_90D_pct":22.0,"MAE_90D_pct":-1.45,"score_return_alignment_label":"good_score_return_alignment","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L15_C30_HANSHIN_202407_PUBLIC_WORKS_HIGH_MAE_SUCCESS","trigger_id":"R10L15_T02_HANSHIN_STAGE2_PUBLIC_WORKS_BALANCE_SURVIVOR","symbol":"004960","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":9,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow early","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":8,"margin_bridge_score":7,"revision_score":4,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":9,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable high-MAE watch","changed_components":["policy_or_regulatory_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Research proxy only. C30 shadow separates self-funded survivor repair from generic policy beta and blocks price-only property-theme blowoff from Stage2/Stage3 promotion.","MFE_90D_pct":17.38,"MAE_90D_pct":-9.28,"score_return_alignment_label":"positive_but_mae_guard_required","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L15_C30_KUMHO_202403_POLICY_BETA_FALSE_POSITIVE","trigger_id":"R10L15_T03_KUMHO_STAGE2_POLICY_BETA_FALSE_POSITIVE","symbol":"002990","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":10,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow false positive","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":14,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59,"stage_label_after":"Stage2-Watch / no positive promotion","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Research proxy only. C30 shadow separates self-funded survivor repair from generic policy beta and blocks price-only property-theme blowoff from Stage2/Stage3 promotion.","MFE_90D_pct":5.75,"MAE_90D_pct":-29.09,"score_return_alignment_label":"false_positive_policy_beta","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L15_C30_KOLON_202406_PRICE_ONLY_PROPERTY_THEME_BLOWOFF","trigger_id":"R10L15_T04_KOLON_4B_PRICE_ONLY_PROPERTY_THEME_BLOWOFF","symbol":"003070","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":18,"execution_risk_score":10,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow false price-momentum promotion","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"4B-Watch / no Stage2-3 promotion","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Research proxy only. C30 shadow separates self-funded survivor repair from generic policy beta and blocks price-only property-theme blowoff from Stage2/Stage3 promotion.","MFE_90D_pct":2.35,"MAE_90D_pct":-46.0,"score_return_alignment_label":"price_only_guard_aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R10","loop":"15","scheduled_round":"R10","scheduled_loop":15,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_beta_false_positive","price_only_blowoff_false_promotion","high_mae_success","missed_survivor_repair"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

Stock-Web:
- Repository: https://github.com/Songdaiki/stock-web
- Manifest: atlas/manifest.json
- Schema: atlas/schema.json
- Price basis: tradable_raw
- Price adjustment status: raw_unadjusted_marcap
- Manifest max_date used for forward-window judgment: 2026-02-20

External context:
- Reuters 2024-03-27: South Korea prepared builder and SME financial support, including guarantees/loans and market-stabilization support for real-estate projects.
- Reuters 2024-05-13: Korean regulators tightened real-estate PF restructuring assessments and highlighted rising PF delinquency.
- Reuters 2024-07-03: Korea announced additional public-sector investment and policy financing to support construction.
- Reuters 2024-07-18: Korea planned housing supply / PF restructuring measures amid Seoul-area house-price volatility.

This MD is historical calibration research only. It is not an investment recommendation.
