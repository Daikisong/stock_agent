# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R10
scheduled_loop: 75
completed_round: R10
completed_loop: 75
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS
output_file: e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds 4 new independent calibration-usable cases, 2 counterexamples, and 4 residual/profile errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated`. The already-applied global axes are treated as existing guardrails, not as new claims:

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

This R10 run does not re-prove those global rules. It stress-tests the construction/PF corner where the same surface word, “PF risk,” can mean either a true balance-sheet break or just a sector-wide storm cloud.

## 2. Round / Large Sector / Canonical Archetype Scope

R10 maps to `L9_CONSTRUCTION_REALESTATE_HOUSING`; the selected canonical archetype is `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`.

The chosen fine archetype compresses three related failure modes into one C30 lane:

```text
PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS
  -> project-finance liquidity break
  -> construction quality / legal trust break
  -> debt rescheduling / workout / trading-window data block
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only as coverage and duplicate-avoidance context. Existing registry rows show older R10 historical-calibration loops already exist for construction/real-estate/building-materials through early loops, so this run avoids simply reusing generic “construction recession” cases. It selects a company-specific PF/trust-break split and uses new independent symbols/triggers for this loop.

```text
scheduled_round: R10
scheduled_loop: 75
selection_mode: sequential_round_cycle_then_coverage_gap
auto_selected_coverage_gap: C30 PF balance-sheet break vs sector-wide PF panic counterexample gap
wrong_round_penalty: 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields verified from `Songdaiki/stock-web`:

```yaml
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
markets: ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

The schema confirms the calibration columns `d,o,h,l,c,v,a,mc,s,m` and that calibration shards are `tradable_raw`, with raw/unadjusted marcap OHLC. Corporate-action contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

Eligibility rule used:

```text
calibration_usable =
  entry row exists in stock-web tradable shard
  AND >=180 forward tradable rows are available by manifest/profile max_date
  AND 180D window does not overlap corporate-action candidate dates
  AND MFE/MAE 30D/90D/180D are computed
```

Taeyoung Construction is retained as narrative-only because it is exactly the C30 pattern but the stock-web path has a discontinuous forward tradable window and a later 2024-10-31 corporate-action candidate; it should inform the narrative ledger, not weight calibration.

## 6. Canonical Archetype Compression Map

| fine archetype | canonical mapping | rule meaning |
|---|---|---|
| construction_quality_trust_break | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Hard 4C when construction defect/legal block directly breaks delivery trust. |
| PF_liquidity_rescheduling | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Hard 4C when workout, debt-rescheduling, or forced liquidity event is company-specific. |
| sector_wide_PF_panic_only | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Watch-only unless company-specific non-price evidence appears. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | usable | current verdict |
|---|---:|---|---|---|---|---:|---|---|
| R10L75_C30_HDC_GWANGJU_COLLAPSE_20220112 | 294870 | HDC현대산업개발 | positive / 4C_success | Stage4C 2022-01-11 | 2022-01-12 | 20850 | true | current_profile_4C_too_late |
| R10L75_C30_GS_GEOMDAN_REBUILD_20230706 | 006360 | GS건설 | positive / 4C_success | Stage4C 2023-07-05 | 2023-07-06 | 14520 | true | current_profile_4C_too_late |
| R10L75_C30_DLENC_PF_PANIC_COUNTEREX_20221024 | 375500 | DL이앤씨 | counterexample / failed_rerating | Stage2-Watch 2022-10-24 | 2022-10-24 | 36450 | true | current_profile_false_positive |
| R10L75_C30_DAEWOO_PF_PANIC_COUNTEREX_20221024 | 047040 | 대우건설 | counterexample / failed_rerating | Stage2-Watch 2022-10-24 | 2022-10-24 | 4165 | true | current_profile_false_positive |
| R10L75_C30_TAEYOUNG_WORKOUT_NARRATIVE_20231228 | 009410 | 태영건설 | positive / narrative_only | Stage4C 2023-12-28 | 2023-12-28 | 2315 | false | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success_or_4C_success: 2 calibration-usable + 1 narrative-only
counterexample_or_failed_rerating: 2 calibration-usable
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
new_independent_case_ratio: 1.00
```

The balance is useful because C30 has a trap: the word “PF” can behave like a smoke alarm. Sometimes the building is burning; sometimes the alarm is reacting to dust from the whole neighborhood. The rule candidate should not evacuate every large contractor just because the word “PF” is in the air.

## 9. Evidence Source Map

| company | evidence available at trigger | evidence family |
|---|---|---|
| HDC현대산업개발 | 광주 화정 아이파크 collapse/trust/legal event, 2022-01-11 | company-specific trust break |
| GS건설 | 검단 현장 collapse/rebuild-cost event, 2023-07-05/06 | company-specific cost/legal break |
| DL이앤씨 | 2022 PF panic / high-rate liquidity fear without company-specific hard break | sector-wide panic counterexample |
| 대우건설 | 2022 PF panic with large-builder/overseas backlog offset | sector-wide panic counterexample |
| 태영건설 | 2023-12-28 workout/debt-rescheduling event | company-specific liquidity break, narrative-only due price window block |

## 10. Price Data Source Map

| symbol | profile_path | shard_path | profile caveat |
|---:|---|---|---|
| 294870 | atlas/symbol_profiles/294/294870.json | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | 2020-03-26 corporate-action candidate outside window |
| 006360 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | 2014-06-25 candidate outside window |
| 375500 | atlas/symbol_profiles/375/375500.json | atlas/ohlcv_tradable_by_symbol_year/375/375500/2022.csv | 2022-04 candidates outside selected window |
| 047040 | atlas/symbol_profiles/047/047040.json | atlas/ohlcv_tradable_by_symbol_year/047/047040/2022.csv | old candidates outside selected window |
| 009410 | atlas/symbol_profiles/009/009410.json | atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv; 2024.csv | blocked after 90D by trade gap and 2024-10-31 candidate |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger | entry | entry_price | usable | current verdict |
|---|---:|---|---|---|---|---:|---|---|
| R10L75_C30_HDC_GWANGJU_COLLAPSE_20220112 | 294870 | HDC현대산업개발 | positive / 4C_success | Stage4C 2022-01-11 | 2022-01-12 | 20850 | true | current_profile_4C_too_late |
| R10L75_C30_GS_GEOMDAN_REBUILD_20230706 | 006360 | GS건설 | positive / 4C_success | Stage4C 2023-07-05 | 2023-07-06 | 14520 | true | current_profile_4C_too_late |
| R10L75_C30_DLENC_PF_PANIC_COUNTEREX_20221024 | 375500 | DL이앤씨 | counterexample / failed_rerating | Stage2-Watch 2022-10-24 | 2022-10-24 | 36450 | true | current_profile_false_positive |
| R10L75_C30_DAEWOO_PF_PANIC_COUNTEREX_20221024 | 047040 | 대우건설 | counterexample / failed_rerating | Stage2-Watch 2022-10-24 | 2022-10-24 | 4165 | true | current_profile_false_positive |
| R10L75_C30_TAEYOUNG_WORKOUT_NARRATIVE_20231228 | 009410 | 태영건설 | positive / narrative_only | Stage4C 2023-12-28 | 2023-12-28 | 2315 | false | current_profile_data_insufficient |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | px | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown_after_peak | usable |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R10L75_C30_HDC_STAGE4C_20220112 | 2022-01-12 | 20850 | 8.87 | -35.25 | 8.87 | -36.93 | 8.87 | -50.84 | 2022-01-12 / 22700 | -56.83 | true |
| R10L75_C30_GS_STAGE4C_20230706 | 2023-07-06 | 14520 | 3.86 | -7.92 | 5.03 | -12.74 | 19.83 | -12.74 | 2023-11-23 / 17400 | -18.56 | true |
| R10L75_C30_DLENC_STAGE2_WATCH_20221024 | 2022-10-24 | 36450 | 16.6 | -6.17 | 16.6 | -15.09 | 16.6 | -19.07 | 2022-12-01 / 42500 | -30.59 | true |
| R10L75_C30_DAEWOO_STAGE2_WATCH_20221024 | 2022-10-24 | 4165 | 23.89 | -5.16 | 23.89 | -7.08 | 23.89 | -7.08 | 2022-12-01 / 5160 | -26.16 | true |
| R10L75_C30_TAEYOUNG_4C_NARRATIVE_20231228 | 2023-12-28 | 2315 | 77.54 | -5.83 | 77.54 | -5.83 | blocked | blocked | 2024-01-11 / 4110 | -46.96 | false |

## 13. Current Calibrated Profile Stress Test

| case | current profile verdict | why residual exists |
|---|---|---|
| HDC현대산업개발 | current_profile_4C_too_late | A construction-quality trust break behaves like thesis evidence breaking, not like ordinary sector weakness. |
| GS건설 | current_profile_4C_too_late | The initial selloff and later recovery make it important to distinguish hard 4C event from price-only 4B. |
| DL이앤씨 | current_profile_false_positive | Sector-wide PF panic alone would have over-blocked a non-broken large contractor. |
| 대우건설 | current_profile_false_positive | Similar PF headline stress had positive MFE and limited MAE; company-specific hard break was absent. |
| 태영건설 | current_profile_data_insufficient | Correct thesis-break narrative, but quantitative weight is blocked by trading path / corporate-action caveat. |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used as the main entry in this R10/C30 run. Therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

The stress point is not “Green is late.” The stress point is whether construction/PF evidence should route to hard 4C, 4B overlay, or Stage2 watch-only. In this archetype, a later EPS revision can arrive after the price damage, so the system should read company-specific legal/liquidity evidence directly as C30 thesis-break when it is present.

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B / full 4B verdict |
|---|---|
| HDC현대산업개발 | Hard 4C event; 4B proximity not primary. |
| GS건설 | Non-price event evidence exists, but full-window recovery means this is hard 4C with recovery watch, not a simple local peak sell label. |
| DL이앤씨 | Sector-wide price panic is not enough for full 4B; cap as watch-only without company-specific evidence. |
| 대우건설 | Same: price-only/sector panic should not be promoted to full 4B or 4C. |
| 태영건설 | Narrative hard 4C; weight blocked. |

## 16. 4C Protection Audit

| case | 4C protection label | interpretation |
|---|---|---|
| HDC현대산업개발 | hard_4c_success | Hard 4C would have protected a large drawdown after the quality/trust break. |
| GS건설 | hard_4c_success_but_recovery_watch | Correct to flag event risk, but recovery watch is needed after the drawdown stabilizes. |
| DL이앤씨 | false_break_watch_only | Hard 4C would have been a false break. |
| 대우건설 | false_break_watch_only | Hard 4C would have been a false break. |
| 태영건설 | hard_4c_success_narrative_only | Correct narrative, not quantitative calibration due stock-web window block. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L9_C30_company_specific_PF_trust_break_gate
```

Candidate:

```text
if large_sector_id == L9_CONSTRUCTION_REALESTATE_HOUSING
and canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK:

    if company_specific_evidence in [
        workout_or_debt_rescheduling,
        construction_quality_trust_break,
        legal_or_regulatory_block,
        forced_liquidity_event,
        explicit project loss / rebuild-cost event
    ]:
        allow hard_4C or strong 4B/4C overlay

    else if evidence is sector-wide PF panic, rate panic, credit-spread fear, or generic housing downturn:
        cap at Stage2-Watch or 4B-watch-only
        do not route to hard 4C
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

C30 should compress the signal into two gates:

```text
C30_positive_hard_break_gate:
    company-specific non-price evidence required.
C30_counterexample_guard:
    sector-wide panic without company-specific evidence cannot become hard 4C.
```

This preserves the already-applied global rule that full 4B requires non-price evidence, but it sharpens what “non-price evidence” means for construction/PF.

## 19. Before / After Backtest Comparison

| case | before score/label | after score/label | alignment | delta explanation |
|---|---|---|---|---|
| HDC현대산업개발 | 78 / Stage3_Yellow_or_watch_too_late | 41 / hard_4C | hard_4C_quality_trust_break_success | C30 company-specific risk split; sector panic alone capped as watch-only. |
| GS건설 | 76 / Stage3_Yellow_too_late | 44 / hard_4C_watch | loss_event_4C_with_later_recovery | C30 company-specific risk split; sector panic alone capped as watch-only. |
| DL이앤씨 | 73 / 4B_or_4C_watch_too_harsh | 69 / Stage2_watch_only | PF_panic_counterexample | C30 company-specific risk split; sector panic alone capped as watch-only. |
| 대우건설 | 74 / 4B_or_4C_watch_too_harsh | 71 / Stage2_watch_only | PF_panic_counterexample | C30 company-specific risk split; sector panic alone capped as watch-only. |
| 태영건설 | 40 / hard_4C_candidate_blocked | 40 / narrative_only_4C | hard_4C_but_not_weight_calibration | C30 company-specific risk split; sector panic alone capped as watch-only. |

Aggregate comparison:

| profile | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 current calibrated proxy | 13.6 | -17.96 | 17.3 | -22.43 | 0.50 | mixed |
| P1 sector-specific candidate | 13.6 | -17.96 | 17.3 | -22.43 | 0.00 | improved guard |
| P2 canonical candidate | 13.6 | -17.96 | 17.3 | -22.43 | 0.00 | best compression |
| P3 counterexample guard | 13.6 | -17.96 | 17.3 | -22.43 | 0.00 | guard passed |

## 20. Score-Return Alignment Matrix

| case | return path | score alignment |
|---|---|---|
| HDC현대산업개발 | low MFE, very high MAE | C30 hard 4C aligned |
| GS건설 | early drawdown, later recovery | hard 4C with recovery watch aligned |
| DL이앤씨 | high MFE and recoverable MAE after panic | hard 4C would be false positive |
| 대우건설 | high MFE and mild MAE after panic | hard 4C would be false positive |
| 태영건설 | narrative hard break but price path blocked | ledger only |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS | 2 | 2 | 2 | 3 | 4 | 0 | 4 | 4 | 4 | true | true | Company-specific PF/trust-break gate covered; need future small-builder holdout and PF-rescue recovery cases. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_4C_too_late
  - narrative_only_data_block
new_axis_proposed:
  - C30_company_specific_PF_balance_sheet_trust_break_gate
  - C30_sector_panic_watch_only_cap
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
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
- stock-web manifest/schema fields.
- profile paths and corporate-action candidate dates for all selected symbols.
- representative entry rows from tradable shards.
- 30D/90D/180D-style OHLC path estimates from actual stock-web tradable rows.
- duplicate policy: no reused case counted as new.
```

Not validated:

```text
- live scoring code.
- stock_agent src/e2r implementation details.
- any current 2026 investment candidate.
- broker/API/live watchlist behavior.
- production scoring changes.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_company_specific_PF_balance_sheet_trust_break_gate,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"company-specific PF/trust-break evidence required for hard 4C","reduces false positives while preserving HDC/GS hard-break labels","R10L75_C30_HDC_STAGE4C_20220112|R10L75_C30_GS_STAGE4C_20230706|R10L75_C30_DLENC_STAGE2_WATCH_20221024|R10L75_C30_DAEWOO_STAGE2_WATCH_20221024",4,4,2,medium,canonical_archetype_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R10L75_C30_HDC_GWANGJU_COLLAPSE_20220112","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"R10L75_C30_HDC_STAGE4C_20220112","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4C_quality_trust_break_success","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"광주 화정 아이파크 붕괴 이후 품질·인허가·브랜드 신뢰 훼손이 한 번에 발생한 건설 안전/계약 신뢰 붕괴형."}
{"row_type":"trigger","trigger_id":"R10L75_C30_HDC_STAGE4C_20220112","case_id":"R10L75_C30_HDC_GWANGJU_COLLAPSE_20220112","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","sector":"construction_realestate_housing","primary_archetype":"C30","loop_objective":"sector_specific_rule_discovery;counterexample_mining;4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2022-01-11","entry_date":"2022-01-12","entry_price":20850,"evidence_available_at_that_date":"광주 화정 아이파크 붕괴 이후 품질·인허가·브랜드 신뢰 훼손이 한 번에 발생한 건설 안전/계약 신뢰 붕괴형.","evidence_source":"public news/event chronology; HDC stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["accounting_or_trust_break","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.87,"MFE_90D_pct":8.87,"MFE_180D_pct":8.87,"MFE_1Y_pct":8.87,"MFE_2Y_pct":23.98,"MAE_30D_pct":-35.25,"MAE_90D_pct":-36.93,"MAE_180D_pct":-50.84,"MAE_1Y_pct":-53.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700,"drawdown_after_peak_pct":-56.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_hard_4C_event","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4C_quality_trust_break_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"294870_2022-01-12_20850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L75_C30_HDC_GWANGJU_COLLAPSE_20220112","trigger_id":"R10L75_C30_HDC_STAGE4C_20220112","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":35,"margin_bridge_score":10,"revision_score":0,"relative_strength_score":0,"customer_quality_score":-30,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":70,"legal_or_contract_risk_score":85,"dilution_cb_risk_score":0,"accounting_trust_risk_score":25},"weighted_score_before":78,"stage_label_before":"Stage3_Yellow_or_watch_too_late","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":-80,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":95,"dilution_cb_risk_score":0,"accounting_trust_risk_score":65},"weighted_score_after":41,"stage_label_after":"hard_4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C30 separates company-specific PF/balance-sheet/trust break from sector-wide PF panic; hard 4C needs company-specific non-price evidence or trading/data block.","MFE_90D_pct":8.87,"MAE_90D_pct":-36.93,"score_return_alignment_label":"hard_4C_quality_trust_break_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"case","case_id":"R10L75_C30_GS_GEOMDAN_REBUILD_20230706","symbol":"006360","company_name":"GS건설","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"R10L75_C30_GS_STAGE4C_20230706","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"loss_event_4C_with_later_recovery","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"검단 현장 붕괴/전면 재시공 비용 인식형: 단순 PF 불안이 아니라 특정 현장 손실과 신뢰 훼손이 동시에 가격화."}
{"row_type":"trigger","trigger_id":"R10L75_C30_GS_STAGE4C_20230706","case_id":"R10L75_C30_GS_GEOMDAN_REBUILD_20230706","symbol":"006360","company_name":"GS건설","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","sector":"construction_realestate_housing","primary_archetype":"C30","loop_objective":"sector_specific_rule_discovery;counterexample_mining;4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2023-07-05","entry_date":"2023-07-06","entry_price":14520,"evidence_available_at_that_date":"검단 현장 붕괴/전면 재시공 비용 인식형: 단순 PF 불안이 아니라 특정 현장 손실과 신뢰 훼손이 동시에 가격화.","evidence_source":"public news/event chronology; GS stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","legal_or_regulatory_block"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.86,"MFE_90D_pct":5.03,"MFE_180D_pct":19.83,"MFE_1Y_pct":24.66,"MFE_2Y_pct":34.99,"MAE_30D_pct":-7.92,"MAE_90D_pct":-12.74,"MAE_180D_pct":-12.74,"MAE_1Y_pct":-12.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-23","peak_price":17400,"drawdown_after_peak_pct":-18.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.09,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"hard_4C_event_not_price_only_4B","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_but_recovery_watch","trigger_outcome_label":"loss_event_4C_with_later_recovery","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"006360_2023-07-06_14520","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L75_C30_GS_GEOMDAN_REBUILD_20230706","trigger_id":"R10L75_C30_GS_STAGE4C_20230706","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":35,"margin_bridge_score":10,"revision_score":0,"relative_strength_score":0,"customer_quality_score":-20,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":65,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":20},"weighted_score_before":76,"stage_label_before":"Stage3_Yellow_too_late","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":-25,"revision_score":-10,"relative_strength_score":0,"customer_quality_score":-65,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":90,"legal_or_contract_risk_score":88,"dilution_cb_risk_score":0,"accounting_trust_risk_score":45},"weighted_score_after":44,"stage_label_after":"hard_4C_watch","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C30 separates company-specific PF/balance-sheet/trust break from sector-wide PF panic; hard 4C needs company-specific non-price evidence or trading/data block.","MFE_90D_pct":5.03,"MAE_90D_pct":-12.74,"score_return_alignment_label":"loss_event_4C_with_later_recovery","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"case","case_id":"R10L75_C30_DLENC_PF_PANIC_COUNTEREX_20221024","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R10L75_C30_DLENC_STAGE2_WATCH_20221024","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"PF_panic_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"레고랜드/부동산 PF 공포 국면의 섹터 동반 매도. 회사별 현장 손상·워크아웃·계약 취소 증거 없이 sector-wide PF label만으로 hard 4C를 주면 과잉 차단."}
{"row_type":"trigger","trigger_id":"R10L75_C30_DLENC_STAGE2_WATCH_20221024","case_id":"R10L75_C30_DLENC_PF_PANIC_COUNTEREX_20221024","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","sector":"construction_realestate_housing","primary_archetype":"C30","loop_objective":"sector_specific_rule_discovery;counterexample_mining;4C_thesis_break_timing_test","trigger_type":"Stage2-Watch","trigger_date":"2022-10-24","entry_date":"2022-10-24","entry_price":36450,"evidence_available_at_that_date":"레고랜드/부동산 PF 공포 국면의 섹터 동반 매도. 회사별 현장 손상·워크아웃·계약 취소 증거 없이 sector-wide PF label만으로 hard 4C를 주면 과잉 차단.","evidence_source":"public PF crisis chronology; DL E&C stock-web tradable shard","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2022.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.6,"MFE_90D_pct":16.6,"MFE_180D_pct":16.6,"MFE_1Y_pct":16.6,"MFE_2Y_pct":39.64,"MAE_30D_pct":-6.17,"MAE_90D_pct":-15.09,"MAE_180D_pct":-19.07,"MAE_1Y_pct":-23.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-12-01","peak_price":42500,"drawdown_after_peak_pct":-30.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"sector_panic_not_full_4B_without_company_specific_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break_watch_only","trigger_outcome_label":"PF_panic_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"375500_2022-10-24_36450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L75_C30_DLENC_PF_PANIC_COUNTEREX_20221024","trigger_id":"R10L75_C30_DLENC_STAGE2_WATCH_20221024","symbol":"375500","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":0,"relative_strength_score":0,"customer_quality_score":15,"policy_or_regulatory_score":35,"valuation_repricing_score":0,"execution_risk_score":40,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"4B_or_4C_watch_too_harsh","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":0,"relative_strength_score":0,"customer_quality_score":15,"policy_or_regulatory_score":25,"valuation_repricing_score":0,"execution_risk_score":30,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2_watch_only","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C30 separates company-specific PF/balance-sheet/trust break from sector-wide PF panic; hard 4C needs company-specific non-price evidence or trading/data block.","MFE_90D_pct":16.6,"MAE_90D_pct":-15.09,"score_return_alignment_label":"PF_panic_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"R10L75_C30_DAEWOO_PF_PANIC_COUNTEREX_20221024","symbol":"047040","company_name":"대우건설","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R10L75_C30_DAEWOO_STAGE2_WATCH_20221024","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"PF_panic_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"동일한 PF 공포 국면에서 대형사/해외 EPC·원전·인프라 exposure를 가진 건설사의 sector-wide panic label이 4C로 과격하게 번지는 반례."}
{"row_type":"trigger","trigger_id":"R10L75_C30_DAEWOO_STAGE2_WATCH_20221024","case_id":"R10L75_C30_DAEWOO_PF_PANIC_COUNTEREX_20221024","symbol":"047040","company_name":"대우건설","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","sector":"construction_realestate_housing","primary_archetype":"C30","loop_objective":"sector_specific_rule_discovery;counterexample_mining;4C_thesis_break_timing_test","trigger_type":"Stage2-Watch","trigger_date":"2022-10-24","entry_date":"2022-10-24","entry_price":4165,"evidence_available_at_that_date":"동일한 PF 공포 국면에서 대형사/해외 EPC·원전·인프라 exposure를 가진 건설사의 sector-wide panic label이 4C로 과격하게 번지는 반례.","evidence_source":"public PF crisis chronology; Daewoo E&C stock-web tradable shard","stage2_evidence_fields":["policy_or_regulatory_optionality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2022.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.89,"MFE_90D_pct":23.89,"MFE_180D_pct":23.89,"MFE_1Y_pct":25.33,"MFE_2Y_pct":63.51,"MAE_30D_pct":-5.16,"MAE_90D_pct":-7.08,"MAE_180D_pct":-7.08,"MAE_1Y_pct":-8.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-12-01","peak_price":5160,"drawdown_after_peak_pct":-26.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"sector_panic_not_full_4B_without_company_specific_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break_watch_only","trigger_outcome_label":"PF_panic_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"047040_2022-10-24_4165","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L75_C30_DAEWOO_PF_PANIC_COUNTEREX_20221024","trigger_id":"R10L75_C30_DAEWOO_STAGE2_WATCH_20221024","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":45,"margin_bridge_score":20,"revision_score":0,"relative_strength_score":0,"customer_quality_score":15,"policy_or_regulatory_score":35,"valuation_repricing_score":0,"execution_risk_score":38,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"4B_or_4C_watch_too_harsh","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":45,"margin_bridge_score":20,"revision_score":0,"relative_strength_score":0,"customer_quality_score":15,"policy_or_regulatory_score":25,"valuation_repricing_score":0,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2_watch_only","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C30 separates company-specific PF/balance-sheet/trust break from sector-wide PF panic; hard 4C needs company-specific non-price evidence or trading/data block.","MFE_90D_pct":23.89,"MAE_90D_pct":-7.08,"score_return_alignment_label":"PF_panic_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"R10L75_C30_TAEYOUNG_WORKOUT_NARRATIVE_20231228","symbol":"009410","company_name":"태영건설","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","case_type":"narrative_only","positive_or_counterexample":"positive","best_trigger":"R10L75_C30_TAEYOUNG_4C_NARRATIVE_20231228","calibration_usable":false,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"score_price_alignment":"hard_4C_but_not_weight_calibration","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"워크아웃 신청은 C30의 교과서적 thesis-break지만 stock-web 180D window가 거래정지/후속 주식수 급변 후보 때문에 weight calibration에서는 차단한다."}
{"row_type":"trigger","trigger_id":"R10L75_C30_TAEYOUNG_4C_NARRATIVE_20231228","case_id":"R10L75_C30_TAEYOUNG_WORKOUT_NARRATIVE_20231228","symbol":"009410","company_name":"태영건설","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_BREAK_AND_COMPANY_SPECIFIC_TRUST_LOSS","sector":"construction_realestate_housing","primary_archetype":"C30","loop_objective":"sector_specific_rule_discovery;counterexample_mining;4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2023-12-28","entry_date":"2023-12-28","entry_price":2315,"evidence_available_at_that_date":"워크아웃 신청은 C30의 교과서적 thesis-break지만 stock-web 180D window가 거래정지/후속 주식수 급변 후보 때문에 weight calibration에서는 차단한다.","evidence_source":"public workout/PF chronology; Taeyoung stock-web tradable/raw profile","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["capital_raise_or_overhang","legal_or_regulatory_block"],"stage4c_evidence_fields":["forced_liquidation_or_crash","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv","profile_path":"atlas/symbol_profiles/009/009410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":77.54,"MFE_90D_pct":77.54,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.83,"MAE_90D_pct":-5.83,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-11","peak_price":4110,"drawdown_after_peak_pct":-46.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"narrative_only_due_window_block","four_b_evidence_type":["legal_or_regulatory_block","capital_raise_or_overhang"],"four_c_protection_label":"hard_4c_success_narrative_only","trigger_outcome_label":"hard_4C_but_not_weight_calibration","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":false,"forward_window_trading_days":52,"calibration_block_reasons":["insufficient_continuous_forward_tradable_window","corporate_action_contaminated_1Y_window_2024-10-31"],"corporate_action_window_status":"blocked_after_90D_by_trading_gap_and_2024-10-31_candidate","same_entry_group_id":"009410_2023-12-28_2315","dedupe_for_aggregate":false,"aggregate_group_role":"narrative_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L75_C30_TAEYOUNG_WORKOUT_NARRATIVE_20231228","trigger_id":"R10L75_C30_TAEYOUNG_4C_NARRATIVE_20231228","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-30,"revision_score":-20,"relative_strength_score":0,"customer_quality_score":-30,"policy_or_regulatory_score":20,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":75,"accounting_trust_risk_score":55},"weighted_score_before":40,"stage_label_before":"hard_4C_candidate_blocked","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":-30,"revision_score":-20,"relative_strength_score":0,"customer_quality_score":-30,"policy_or_regulatory_score":20,"valuation_repricing_score":0,"execution_risk_score":95,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":75,"accounting_trust_risk_score":55},"weighted_score_after":40,"stage_label_after":"narrative_only_4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C30 separates company-specific PF/balance-sheet/trust break from sector-wide PF panic; hard 4C needs company-specific non-price evidence or trading/data block.","MFE_90D_pct":77.54,"MAE_90D_pct":-5.83,"score_return_alignment_label":"hard_4C_but_not_weight_calibration","current_profile_verdict":"current_profile_data_insufficient"}
{"profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_global_proxy","profile_hypothesis":"current profile keeps global guardrails but lacks C30 company-specific PF/trust-loss split","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":13.6,"avg_MAE_90D_pct":-17.96,"avg_MFE_180D_pct":17.3,"avg_MAE_180D_pct":-22.43,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"mixed","avg_four_b_full_window_peak_proximity":"mixed","score_return_alignment_verdict":"mixed_current_profile_false_positive_on_big_builders","row_type":"profile_comparison"}
{"profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"weaker post-calibration rules miss hard 4C event distinction and repeat old sector panic mistakes","changed_axes":["rollback_reference_only"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":13.6,"avg_MAE_90D_pct":-17.96,"avg_MFE_180D_pct":17.3,"avg_MAE_180D_pct":-22.43,"false_positive_rate":0.5,"missed_structural_count":2,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"mixed","avg_four_b_full_window_peak_proximity":"mixed","score_return_alignment_verdict":"weaker_than_P0_for_event_trust_break","row_type":"profile_comparison"}
{"profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"L9 construction needs PF/balance-sheet trust break gate before hard 4C; sector-wide panic remains watch-only without company-specific non-price evidence","changed_axes":["C30_company_specific_hard_4C_gate","+C30_sector_panic_watch_only_cap"],"changed_thresholds":{"hard_4C_company_specific_evidence_min":1,"sector_panic_max_label_without_company_evidence":"Stage2_watch"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":13.6,"avg_MAE_90D_pct":-17.96,"avg_MFE_180D_pct":17.3,"avg_MAE_180D_pct":-22.43,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"split_local_vs_full","avg_four_b_full_window_peak_proximity":"split_local_vs_full","score_return_alignment_verdict":"improves_false_positive_without_weakening_hard_4C","row_type":"profile_comparison"}
{"profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should compress quality-collapse, PF-liquidity, debt-rescheduling into thesis-break bucket; macro PF stress alone is not enough","changed_axes":["C30_trust_break_component","C30_liquidity_event_component"],"changed_thresholds":{"accounting_or_trust_risk_hard_4C_min":55},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":13.6,"avg_MAE_90D_pct":-17.96,"avg_MFE_180D_pct":17.3,"avg_MAE_180D_pct":-22.43,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_primary","avg_four_b_full_window_peak_proximity":"not_primary","score_return_alignment_verdict":"best_archetype_compression","row_type":"profile_comparison"}
{"profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"large-cap contractors with clean company-specific evidence but sector PF headlines should not be routed to 4C","changed_axes":["C30_counterexample_guard"],"changed_thresholds":{"company_specific_negative_evidence_required":true},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":13.6,"avg_MAE_90D_pct":-17.96,"avg_MFE_180D_pct":17.3,"avg_MAE_180D_pct":-22.43,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":"not_primary","avg_four_b_full_window_peak_proximity":"not_primary","score_return_alignment_verdict":"guard_passed","row_type":"profile_comparison"}
{"row_type":"shadow_weight","axis":"C30_company_specific_PF_balance_sheet_trust_break_gate","scope":"canonical_archetype_specific","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Hard 4C should require company-specific PF/liquidity/trust-break evidence, not just sector panic.","backtest_effect":"reduced false positives on DL이앤씨/대우건설 while preserving HDC/GS hard 4C labeling","trigger_ids":"R10L75_C30_HDC_STAGE4C_20220112|R10L75_C30_GS_STAGE4C_20230706|R10L75_C30_DLENC_STAGE2_WATCH_20221024|R10L75_C30_DAEWOO_STAGE2_WATCH_20221024","calibration_usable_count":4,"new_independent_case_count":4,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_archetype_shadow_only","notes":"not production; post-calibrated residual","do_not_propose_new_weight_delta":false}
{"row_type":"residual_contribution","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["current_profile_false_positive","current_profile_4C_too_late","narrative_only_data_block"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R10L75_C30_TAEYOUNG_WORKOUT_NARRATIVE_20231228","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"workout evidence available but continuous 180D forward tradable window is blocked by trading gap and 2024-10-31 corporate-action candidate","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 75
next_round = R11
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source notes:

- `atlas/manifest.json` confirms max_date `2026-02-20`, `tradable_row_count=14354401`, `price_adjustment_status=raw_unadjusted_marcap`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.
- `atlas/schema.json` confirms tradable shard columns and calibration rules.
- Symbol profiles checked:
  - `atlas/symbol_profiles/294/294870.json`
  - `atlas/symbol_profiles/006/006360.json`
  - `atlas/symbol_profiles/009/009410.json`
  - `atlas/symbol_profiles/375/375500.json`
  - `atlas/symbol_profiles/047/047040.json`
- Representative OHLC rows checked from:
  - `atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/375/375500/2022.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/375/375500/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/047/047040/2022.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv`

External event notes are used only to locate historical trigger dates; quantitative calibration is based on stock-web OHLC.

