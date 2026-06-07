# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R7_loop_136_L7_BIO_HEALTHCARE_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
selected_round: R7
selected_loop: 136
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: US_FDA_APPROVAL_TO_COMMERCIALIZATION_REVENUE_RERATING_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_commercialization_timing_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This is the corrected valid run after a duplicate C17 loop135 materialization path was discarded. C17 reached the 30-row stability threshold at loop135, so this run moves to the next thin Priority 0 archetype: C23.

This loop adds 3 new independent C23 rows and moves C23 from static 29 rows to projected 32 rows. The 30-row minimum stability threshold is reached with a small buffer.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C23:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R7 -> L7_BIO_HEALTHCARE
C23 -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

C23 is the bio regulatory approval / commercialization archetype. Approval is the door opening; channel access, reimbursement, repeat orders, margin, revision and cash conversion are the people actually walking through the door.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C23 static rows | 29 |
| C23 need to 30 | 1 |
| C23 need to 50 | 21 |
| C23 investigation point | 승인 이후 상업화, 매출 전환, 보험/채널/가격 반례 |
| local previous C23 rows in this session | 0 |
| this loop projected rows | 32 |

Selected symbols avoid local R3 battery and R4 chemical threshold-completion symbols and move into new R7 bio/healthcare evidence.

| symbol | company | status |
|---|---|---|
| 145020 | 휴젤 | new local C23 approval-commercialization rerating |
| 302440 | SK바이오사이언스 | new local C23 post-approval commercialization false positive |
| 195940 | HK이노엔 | new local C23 commercialization revenue buffer |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate. The duplicate C17 loop135 materialization path created during this execution is rejected.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 145020 / 2024-03-06 | true | true | clean_entry_window_old_profile_caveat_but_2024_share_count_drift_watch | true, weight 0.90 |
| 302440 / 2024-03-06 | true | true | clean_entry_window_zero_corporate_action_candidates_but_2024_share_count_drift_watch | true, weight 0.90 |
| 195940 / 2024-03-06 | true | true | clean_180D_window_zero_corporate_action_candidates | true, weight 1.00 |

Corporate-action notes:

- 휴젤 has old corporate-action candidates in 2017/2020 only, but the 2024 row stream shows share-count drift after June; it is retained with reduced weight.
- SK바이오사이언스 has zero corporate-action candidates, but the 2024 row stream shows share-count drift after October; it is retained with reduced weight.
- HK이노엔 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| US_FDA_APPROVAL_TO_COMMERCIALIZATION_REVENUE_RERATING_4B_WATCH | C23 | regulatory approval can work as Stage2A, but Green needs channel revenue, margin and revision bridge |
| POST_APPROVAL_PLATFORM_LANGUAGE_WITHOUT_REVENUE_CHANNEL_CONVERSION | C23 | post-approval/platform language without revenue conversion is false-positive risk |
| APPROVED_DRUG_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER_STAGE2 | C23 | approved-product commercialization channel can block blanket 4C, but still needs sustained margin/revision for Green |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C23_HUGEL_145020_2024_03_06_US_FDA_APPROVAL_COMMERCIALIZATION_RERATING_4B | 145020 | 휴젤 | approval_commercialization_success_4B_overlay | positive | approval-to-commercialization route produced large full-window MFE |
| C23_SKBIO_302440_2024_03_06_POST_APPROVAL_PLATFORM_COMMERCIALIZATION_FAIL | 302440 | SK바이오사이언스 | failed_commercialization_rerating | counterexample | post-approval/platform language lacked revenue conversion and produced weak MFE |
| C23_HKINNO_195940_2024_03_06_APPROVAL_COMMERCIALIZATION_REVENUE_BUFFER | 195940 | HK이노엔 | commercialization_revenue_buffer | positive_boundary | channel/revenue bridge created later MFE and limited MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 1 |
| positive_boundary_case_count | 1 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| overblock_or_buffer_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 2 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 145020 | source_proxy_only | US approval and commercialization channel/revenue route | required before promotion |
| 302440 | source_proxy_only | post-approval/platform language but channel revenue/margin bridge absent | required; useful as counterexample |
| 195940 | source_proxy_only | approved-product commercialization and revenue-channel buffer | required before promotion |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | atlas/symbol_profiles/145/145020.json |
| 302440 | atlas/ohlcv_tradable_by_symbol_year/302/302440/2024.csv | atlas/symbol_profiles/302/302440.json |
| 195940 | atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv | atlas/symbol_profiles/195/195940.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HUGEL_145020_2024_03_06_STAGE2A_FDA_APPROVAL_COMMERCIALIZATION | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 209500 | approval-to-commercialization route |
| SKBIO_302440_2024_03_06_STAGE2_FALSE_POSITIVE_POST_APPROVAL_PLATFORM | Stage2 | 2024-03-06 | 2024-03-06 | 60600 | post-approval platform without revenue bridge |
| HKINNO_195940_2024_03_06_STAGE2A_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 39000 | commercialization revenue-channel buffer |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 145020 | 2024-03-06 | 209500 | 0.95 | -17.76 | 25.30 | -17.76 | 55.61 | -17.76 | 2024-11-07 | 326000 | -21.78 |
| 302440 | 2024-03-06 | 60600 | 4.13 | -2.81 | 4.13 | -18.07 | 4.13 | -27.48 | 2024-03-22 | 63100 | -30.35 |
| 195940 | 2024-03-06 | 39000 | 2.05 | -11.92 | 8.72 | -11.92 | 33.33 | -11.92 | 2024-10-07 | 52000 | -31.06 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 145020 | Stage2A possible; approval event risks overpromotion | large MFE but 4B commercialization audit still needed | current_profile_4B_too_late |
| 302440 | Stage2 risk if post-approval platform language is over-credited | weak MFE and deeper MAE | current_profile_false_positive |
| 195940 | hard 4C risk if approval commercialization is treated as event-only | overblock/revenue-buffer case | current_profile_overblocks_if_approval_commercialization_treated_as_event_only |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C23 interpretation:

- Regulatory approval can justify Stage2A only when commercialization channel and revenue conversion are visible.
- Approval/platform language without revenue, margin, revision and cash conversion should remain Stage1/Stage2-watch.
- Commercialization revenue buffers can prevent blanket 4C, but Green still requires sustained margin and revision confirmation.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 145020 | 0.64 | 1.00 | approval rerating / commercialization timing | 4B commercialization audit required |
| 302440 | 0.96 | 1.00 | weak platform follow-through / bridge absent | not Stage3 |
| 195940 | 0.75 | 1.00 | commercialization revenue buffer | Stage2-watch buffer, not Green |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 145020 | thesis_break_watch_only | not hard 4C, but approval-event overpromotion needs 4B audit |
| 302440 | hard_4c_late | channel revenue/margin/cash bridge absence should have capped Stage2 earlier |
| 195940 | overblock_counterexample_watch | blanket approval-event 4C would have missed revenue-channel buffer |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L7_BIO_HEALTHCARE
confidence = medium
```

Candidate:

> In L7 bio/healthcare names, regulatory approval should promote Stage2A only when channel access, reimbursement, revenue conversion, margin bridge, revision and cash conversion are visible. Approval or platform language alone should not become Yellow/Green. If an approved product has visible commercialization revenue buffer, avoid blanket hard 4C but keep Green blocked until margin/revision confirms.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
confidence = medium
```

Candidate C23 rule:

```text
C23_approval_commercialization_revenue_bridge_required =
  regulatory_approval_or_post_approval_route
  AND (channel_access OR reimbursement_path OR revenue_conversion OR margin_bridge OR confirmed_revision OR cash_conversion)

if approval_event_or_platform_language and revenue_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 20 and MFE_180D > 40:
    add C23_approval_commercialization_4B_audit = true

if MFE_90D < 5 and MAE_90D < -15 and bridge_absent:
    classify_as C23_post_approval_false_positive_guardrail

if approved_product_revenue_channel_buffer and not margin_revision_confirmed:
    classify_as C23_commercialization_buffer_stage2_watch
    do_not_route_blanket_4C = true

if share_count_drift_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / overblock | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 12.72 | -15.92 | 31.02 | -19.05 | 1 false positive + 1 overblock | useful but C23 commercialization bridge needed |
| P0b calibrated rollback | rollback | 3 | 12.72 | -15.92 | 31.02 | -19.05 | 1 false positive + 1 overblock | over-credits approval language or overblocks revenue buffer |
| P1 sector_specific_candidate_profile | L7 | 2 Stage2A/watch + 1 guard | 17.01 | -14.84 | 44.47 | -14.84 | 0 | better after commercialization bridge gate |
| P2 canonical_archetype_candidate_profile | C23 | 2 Stage2A/watch + 1 guard | 17.01 | -14.84 | 44.47 | -14.84 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C23 guard | 2 Stage2A/watch + 1 guard | 17.01 | -14.84 | 44.47 | -14.84 | 0 | adds post-approval false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 145020 | Stage2A aligned; 4B commercialization audit needed | current_profile_4B_too_late |
| 302440 | Stage2 false positive if commercialization bridge not enforced | current_profile_false_positive |
| 195940 | commercialization revenue buffer prevents blanket 4C | current_profile_overblocks_if_approval_commercialization_treated_as_event_only |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | positive boundary | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | mixed C23 fine ids | 1 | 1 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 29 -> projected 32; reaches minimum stability threshold |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
  - current_profile_overblocks_if_approval_commercialization_treated_as_event_only
new_axis_proposed: C23_approval_commercialization_revenue_bridge_required|C23_approval_commercialization_4B_audit|C23_post_approval_false_positive_guardrail|C23_commercialization_buffer_stage2_watch|share_count_drift_independent_weight_reduction
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses C23 Priority 0 coverage gap.
- Uses new local C23 symbols.
- Keeps 145020 and 302440 with reduced independent weights because 2024 share-count drift is visible.
- Treats 195940 as commercialization revenue buffer, not Green promotion.
- Discards the accidental duplicate C17 loop135 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.
- Does not count repeated C17 loop135 materialization as new evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_approval_commercialization_revenue_bridge_required,canonical_archetype_specific,L7_BIO_HEALTHCARE,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"302440 shows post-approval/platform language can fail without revenue/margin bridge while 145020/195940 require channel/revenue conversion to stay Stage2A","blocks one false positive while preserving approval-commercialization winners as Stage2A/watch","HUGEL_145020_2024_03_06_STAGE2A_FDA_APPROVAL_COMMERCIALIZATION|SKBIO_302440_2024_03_06_STAGE2_FALSE_POSITIVE_POST_APPROVAL_PLATFORM|HKINNO_195940_2024_03_06_STAGE2A_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C23_approval_commercialization_4B_audit,canonical_archetype_specific,L7_BIO_HEALTHCARE,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"145020 had large MFE after approval-to-commercialization rerating, but price-only peak still needs revenue/margin/revision proof before Green","adds 4B audit after C23 approval rerating without converting price-only peaks into Green","HUGEL_145020_2024_03_06_STAGE2A_FDA_APPROVAL_COMMERCIALIZATION",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration"
shadow_weight,C23_post_approval_false_positive_guardrail,canonical_archetype_specific,L7_BIO_HEALTHCARE,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"302440 had only 4.13% MFE and -18.07% 90D MAE after platform/post-approval narrative without channel revenue bridge","requires channel revenue, reimbursement, margin/revision and cash conversion before Stage2/Yellow promotion","SKBIO_302440_2024_03_06_STAGE2_FALSE_POSITIVE_POST_APPROVAL_PLATFORM",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,C23_commercialization_buffer_stage2_watch,canonical_archetype_specific,L7_BIO_HEALTHCARE,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"195940 shows approved-product commercialization revenue buffer can prevent blanket hard 4C, though it should not become Green without margin/revision confirmation","keeps commercialization-buffer cases as Stage2-watch rather than hard 4C or Green","HKINNO_195940_2024_03_06_STAGE2A_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER",1,1,0,medium,canonical_shadow_only,"overblock/buffer guard"
shadow_weight,share_count_drift_independent_weight_reduction,archetype_specific_quality_flag,L7_BIO_HEALTHCARE,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"145020/302440 show 2024 share-count drift after selected entries","keeps rows usable but lowers independent evidence weight","HUGEL_145020_2024_03_06_STAGE2A_FDA_APPROVAL_COMMERCIALIZATION|SKBIO_302440_2024_03_06_STAGE2_FALSE_POSITIVE_POST_APPROVAL_PLATFORM",2,2,1,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C23_HUGEL_145020_2024_03_06_US_FDA_APPROVAL_COMMERCIALIZATION_RERATING_4B","symbol":"145020","company_name":"휴젤","round":"R7","loop":"136","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_REVENUE_RERATING_4B_WATCH","case_type":"approval_commercialization_success_4B_overlay","positive_or_counterexample":"positive","best_trigger":"HUGEL_145020_2024_03_06_STAGE2A_FDA_APPROVAL_COMMERCIALIZATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2017/2020; selected 2024 window is clean except share-count drift after June, independent weight reduced","independent_evidence_weight":0.9,"score_price_alignment":"US regulatory approval and commercialization channel narrative captured a large full-window MFE, but later peak drawdown required C23 4B commercialization audit rather than immediate Green","current_profile_verdict":"current_profile_4B_too_late_if_approval_event_overpromoted_to_green","price_source":"Songdaiki/stock-web","notes":"new local C23 symbol; approval-to-commercialization success with validation-quality caveat"}
{"row_type":"case","case_id":"C23_SKBIO_302440_2024_03_06_POST_APPROVAL_PLATFORM_COMMERCIALIZATION_FAIL","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":"136","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"POST_APPROVAL_PLATFORM_LANGUAGE_WITHOUT_REVENUE_CHANNEL_CONVERSION","case_type":"failed_commercialization_rerating","positive_or_counterexample":"counterexample","best_trigger":"SKBIO_302440_2024_03_06_STAGE2_FALSE_POSITIVE_POST_APPROVAL_PLATFORM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"zero corporate-action candidates, but 2024 share-count drift appears after October; reduced weight for quality guard","independent_evidence_weight":0.9,"score_price_alignment":"post-approval/platform narrative had only a small MFE and later deep MAE without channel revenue, margin, revision or cash conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C23 symbol; clean profile baseline but later share-count drift watch"}
{"row_type":"case","case_id":"C23_HKINNO_195940_2024_03_06_APPROVAL_COMMERCIALIZATION_REVENUE_BUFFER","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"136","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVED_DRUG_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER_STAGE2","case_type":"commercialization_revenue_buffer","positive_or_counterexample":"positive_boundary","best_trigger":"HKINNO_195940_2024_03_06_STAGE2A_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approved-product commercialization and revenue-channel bridge produced a later full-window MFE with limited 180D MAE, so a blanket approval-event 4C would overblock revenue conversion","current_profile_verdict":"current_profile_overblocks_if_approval_commercialization_treated_as_event_only","price_source":"Songdaiki/stock-web","notes":"clean profile with zero corporate-action candidates; commercialization revenue buffer case"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HUGEL_145020_2024_03_06_STAGE2A_FDA_APPROVAL_COMMERCIALIZATION","case_id":"C23_HUGEL_145020_2024_03_06_US_FDA_APPROVAL_COMMERCIALIZATION_RERATING_4B","symbol":"145020","company_name":"휴젤","round":"R7","loop":"136","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_FDA_APPROVAL_TO_COMMERCIALIZATION_REVENUE_RERATING_4B_WATCH","sector":"bio / healthcare","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_commercialization_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":209500.0,"evidence_available_at_that_date":"source_proxy_only: US regulatory approval, commercialization channel setup, export/revenue conversion expectation and brand/channel optionality visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["US_FDA_approval","commercialization_channel_setup","export_revenue_expectation","relative_strength"],"stage3_evidence_fields":["commercialization_channel_partial","revenue_bridge_partial","margin_bridge_pending","revision_bridge_pending"],"stage4b_evidence_fields":["approval_rerating","commercialization_timing_peak_watch","share_count_drift_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.95,"MFE_90D_pct":25.3,"MFE_180D_pct":55.61,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-17.76,"MAE_90D_pct":-17.76,"MAE_180D_pct":-17.76,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000.0,"drawdown_after_peak_pct":-21.78,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.64,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"approval-to-commercialization rerating worked, but full Green needs realized channel revenue, margin and revision bridge","four_b_evidence_type":["regulatory_approval_rerating","commercialization_timing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_large_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late_if_approval_event_overpromoted_to_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_after_june_reduced_weight"],"corporate_action_window_status":"clean_entry_window_old_profile_caveat_but_2024_share_count_drift_watch","same_entry_group_id":"C23_145020_2024_03_06_209500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window; share-count drift after June","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SKBIO_302440_2024_03_06_STAGE2_FALSE_POSITIVE_POST_APPROVAL_PLATFORM","case_id":"C23_SKBIO_302440_2024_03_06_POST_APPROVAL_PLATFORM_COMMERCIALIZATION_FAIL","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":"136","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"POST_APPROVAL_PLATFORM_LANGUAGE_WITHOUT_REVENUE_CHANNEL_CONVERSION","sector":"bio / healthcare","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_commercialization_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":60600.0,"evidence_available_at_that_date":"source_proxy_only: post-approval vaccine/platform commercialization narrative visible, but channel revenue, order conversion, margin, revision and cash conversion absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["post_approval_platform_narrative","vaccine_commercialization_beta","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","platform_beta","bridge_absent","share_count_drift_watch"],"stage4c_evidence_fields":["commercial_revenue_bridge_absent","margin_bridge_absent","revision_bridge_absent","cash_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/302/302440/2024.csv","profile_path":"atlas/symbol_profiles/302/302440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.13,"MFE_90D_pct":4.13,"MFE_180D_pct":4.13,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-2.81,"MAE_90D_pct":-18.07,"MAE_180D_pct":-27.48,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-22","peak_price":63100.0,"drawdown_after_peak_pct":-30.35,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"post-approval/platform language not C23 Stage3 without commercial revenue and cash-conversion bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_after_october_reduced_weight"],"corporate_action_window_status":"clean_entry_window_zero_corporate_action_candidates_but_2024_share_count_drift_watch","same_entry_group_id":"C23_302440_2024_03_06_60600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"zero corporate-action candidates; share-count drift after October","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HKINNO_195940_2024_03_06_STAGE2A_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER","case_id":"C23_HKINNO_195940_2024_03_06_APPROVAL_COMMERCIALIZATION_REVENUE_BUFFER","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"136","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVED_DRUG_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER_STAGE2","sector":"bio / healthcare","primary_archetype":"bio_regulatory_approval_commercialization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_commercialization_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":39000.0,"evidence_available_at_that_date":"source_proxy_only: approved-product commercialization, channel/revenue conversion, domestic and overseas commercialization buffer visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["approved_product_commercialization","channel_revenue_conversion","commercial_buffer","relative_strength_recovery"],"stage3_evidence_fields":["revenue_bridge_partial","margin_bridge_partial","channel_conversion_partial","revision_bridge_pending"],"stage4b_evidence_fields":["commercialization_rerating_watch","valuation_peak_watch"],"stage4c_evidence_fields":["commercialization_delay_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv","profile_path":"atlas/symbol_profiles/195/195940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.05,"MFE_90D_pct":8.72,"MFE_180D_pct":33.33,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.92,"MAE_90D_pct":-11.92,"MAE_180D_pct":-11.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-07","peak_price":52000.0,"drawdown_after_peak_pct":-31.06,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"commercialization revenue buffer prevented blanket 4C, but full Green still needs sustained margin/revision evidence","four_b_evidence_type":["commercialization_revenue_buffer","valuation_peak_watch"],"four_c_protection_label":"overblock_counterexample_watch","trigger_outcome_label":"positive_boundary_commercialization_buffer","current_profile_verdict":"current_profile_overblocks_if_approval_commercialization_treated_as_event_only","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_zero_corporate_action_candidates","same_entry_group_id":"C23_195940_2024_03_06_39000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C23_HUGEL_145020_2024_03_06_US_FDA_APPROVAL_COMMERCIALIZATION_RERATING_4B","trigger_id":"HUGEL_145020_2024_03_06_STAGE2A_FDA_APPROVAL_COMMERCIALIZATION","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable / approval commercialization 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2A with C23 commercialization 4B audit","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Approval worked as rerating evidence, but Green requires realized channel revenue, margin/revision and clean share-count quality.","MFE_90D_pct":25.3,"MAE_90D_pct":-17.76,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late_if_approval_event_overpromoted_to_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C23_SKBIO_302440_2024_03_06_POST_APPROVAL_PLATFORM_COMMERCIALIZATION_FAIL","trigger_id":"SKBIO_302440_2024_03_06_STAGE2_FALSE_POSITIVE_POST_APPROVAL_PLATFORM","symbol":"302440","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage2 false-positive / post-approval platform risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":42,"stage_label_after":"Stage1/4C-watch, not C23 Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Platform/post-approval language lacked channel revenue, margin and cash-conversion bridge.","MFE_90D_pct":4.13,"MAE_90D_pct":-18.07,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C23_HKINNO_195940_2024_03_06_APPROVAL_COMMERCIALIZATION_REVENUE_BUFFER","trigger_id":"HKINNO_195940_2024_03_06_STAGE2A_COMMERCIALIZATION_REVENUE_CHANNEL_BUFFER","symbol":"195940","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-watch / commercialization revenue buffer","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-watch with C23 commercialization buffer, not Green","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Revenue/channel bridge prevents blanket 4C, but Green still needs sustained margin and revision confirmation.","MFE_90D_pct":8.72,"MAE_90D_pct":-11.92,"score_return_alignment_label":"commercialization_buffer_overblock_guard","current_profile_verdict":"current_profile_overblocks_if_approval_commercialization_treated_as_event_only"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"136","large_sector_id":"L7_BIO_HEALTHCARE","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive","current_profile_overblocks_if_approval_commercialization_treated_as_event_only"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_2 rolling calibrated profile.

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
completed_round = R7
completed_loop = 136
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

If this loop is accepted, C23 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C23 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/302/302440/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/145/145020.json
  - atlas/symbol_profiles/302/302440.json
  - atlas/symbol_profiles/195/195940.json
- Rejected duplicate materialization path:
  - e2r_stock_web_v12_residual_round_R4_loop_135_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
