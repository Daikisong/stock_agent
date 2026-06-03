# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R8
scheduled_loop: 71
completed_round: R8
completed_loop: 71
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK
loop_objective:
  - counterexample_mining
  - residual_false_positive_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
  - canonical_archetype_compression
  - coverage_gap_fill
round_schedule_status: valid
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption

Baseline current proxy is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are kept as assumptions, not re-proposed: Stage2 actionable evidence bonus, Yellow 75, Green 87/revision 55, cross-evidence Green buffer, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing.

This R8/C27 loop does **not** argue that content IP should be promoted on price alone. It tests a narrower residual: when K-pop/content IP monetization shows album/tour/platform momentum, the current profile still needs a stronger distinction between repeatable monetization and single-asset/contract-renewal risk.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R8 |
| allowed large sector | L8_PLATFORM_CONTENT_SW_SECURITY |
| selected canonical | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| selected fine/deep sub-archetype | KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK |
| why R8-valid | platform/content/IP monetization; not consumer, not financial, not healthcare |
| scope style | canonical_archetype_specific |

Canonical compression map:

```text
KPOP_ALBUM_PREORDER_AND_TOUR_SCALE             -> C27_CONTENT_IP_GLOBAL_MONETIZATION
SINGLE_GROUP_CONTRACT_RENEWAL_RISK             -> C27_CONTENT_IP_GLOBAL_MONETIZATION
FANDOM_PLATFORM_SUBSCRIPTION_OPERATING_LEVERAGE -> C27_CONTENT_IP_GLOBAL_MONETIZATION
PRICE_ONLY_ENTERTAINMENT_THEME_BLOWOFF         -> C27_CONTENT_IP_GLOBAL_MONETIZATION, but only as 4B/4C guardrail evidence
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used as duplicate-avoidance ledger only:

- Global representative rows: 3148; unique symbols: 473.
- C27 existing coverage: 93 rows / 23 symbols / good-bad Stage2 31/8 / 4B-4C 24/7.
- High-repeat C27 names include 035900, 352820, 194480, 253450, 122870, and 293490.

The selected cases avoid exact hard duplicates by using non-repeated `canonical_archetype_id + symbol + trigger_type + entry_date` combinations. 122870 is reused only as a different residual path: not “good Stage2 proof,” but a 4B/4C contract-renewal risk counterexample.

| case | symbol | no-repeat status | reuse reason |
|---|---:|---|---|
| CUBE_I_FEEL_HIGH_MAE | 182360 | new symbol within C27 registry search | new symbol / high-MAE content hit |
| YG_BLACKPINK_CONTRACT_4C | 122870 | soft duplicate risk | new trigger family: contract-renewal 4B/4C path |
| DEARU_PLATFORM_SUBSCRIPTION_OVERHEAT | 376300 | new symbol within C27 registry search | platform monetization / overheat reset |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest and schema assumptions read for this execution:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The researched symbols have post-entry windows after their stock-profile corporate-action candidates, or no corporate-action candidates in the measured 180D windows.

| symbol | company | profile path | relevant caveat |
|---:|---|---|---|
| 182360 | 큐브엔터 | atlas/symbol_profiles/182/182360.json | old SPAC/capital-action dates are before 2023 window |
| 122870 | 와이지엔터테인먼트 | atlas/symbol_profiles/122/122870.json | older corporate-action dates are before 2023 window |
| 376300 | 디어유 | atlas/symbol_profiles/376/376300.json | no corporate-action candidates |

## 5. Historical Eligibility Gate

All representative triggers below use Stock-Web tradable close as entry price and have at least 180 tradable rows before manifest max date. 1Y/2Y fields are not used for promotion in this loop; the quantitative gate is 30D/90D/180D.

| trigger_id | entry row exists | 180D available | corporate-action window | calibration usable |
|---|---|---|---|---|
| TRG_CUBE_STAGE2_2023_05_15 | yes | yes | clean_180D_window | true |
| TRG_YG_STAGE2_2023_05_12 | yes | yes | clean_180D_window | true |
| TRG_DEARU_STAGE2_2023_01_11 | yes | yes | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

C27 is compressed here as an **IP monetization quality gate** rather than a generic entertainment momentum bucket.

| fine/deep signal | Stage2 use | Stage3/Green use | 4B/4C use |
|---|---|---|---|
| album pre-order / chart hit | weak-to-medium | only with repeat order + margin visibility | if single-IP concentration grows |
| world tour / global fandom | medium | with contract duration + schedule visibility | if contract renewal uncertainty appears |
| platform subscription | medium | with paid-subscriber retention + ARPU | if platform multiple detaches from retention evidence |
| control/contract headline only | no positive use | no Green | 4B/4C watch |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger date | entry date | entry price | selected reason |
|---|---:|---|---|---|---|---:|---|
| CUBE_I_FEEL_HIGH_MAE | 182360 | 큐브엔터 | high_mae_success / current_profile_too_early | 2023-05-14 | 2023-05-15 | 24300 | album pre-order hit worked briefly, but single-IP concentration caused high MAE |
| YG_BLACKPINK_CONTRACT_4C | 122870 | 와이지엔터테인먼트 | 4C_late / false_positive_green | 2023-05-12 | 2023-05-12 | 78100 | strong IP monetization without contract renewal visibility became 4B/4C risk |
| DEARU_PLATFORM_SUBSCRIPTION_OVERHEAT | 376300 | 디어유 | 4B_overlay_success / counterexample_added | 2023-01-11 | 2023-01-11 | 34900 | platform monetization rerated quickly, then subscriber/ARPU persistence needed stricter guard |

## 8. Positive vs Counterexample Balance

| bucket | count | case ids |
|---|---:|---|
| positive structural success | 1 | DEARU_PLATFORM_SUBSCRIPTION_OVERHEAT, but only as Stage2-to-4B timing, not Green loosening |
| counterexample / failed durable rerating | 2 | CUBE_I_FEEL_HIGH_MAE, YG_BLACKPINK_CONTRACT_4C |
| 4B / 4C case | 2 | YG_BLACKPINK_CONTRACT_4C, DEARU_PLATFORM_SUBSCRIPTION_OVERHEAT |
| calibration usable representative triggers | 3 | all representative triggers |

## 9. Evidence Source Map

The evidence layer is treated conservatively. Some music-industry source items are proxy sources rather than direct company filings, so the proposed rule is a shadow guardrail, not production promotion.

| case | evidence available at trigger | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| CUBE_I_FEEL_HIGH_MAE | I Feel / Queencard pre-order and album-release cycle in May 2023 | album pre-order, chart momentum, world-tour expectation | weak; repeat monetization not yet proven | single-IP concentration, later high-MAE drawdown |
| YG_BLACKPINK_CONTRACT_4C | Blackpink/Jisoo/tour monetization around May 2023 | global IP monetization | weak unless contract duration visible | renewal uncertainty and group-concentration thesis break |
| DEARU_PLATFORM_SUBSCRIPTION_OVERHEAT | Bubble/fandom-platform monetization rerating in early 2023 | subscription platform monetization | only if paid-user retention + ARPU conversion confirmed | valuation/platform overheat without retention proof |

## 10. Price Data Source Map

| symbol | shard(s) used | profile used |
|---:|---|---|
| 182360 | atlas/ohlcv_tradable_by_symbol_year/182/182360/2023.csv | atlas/symbol_profiles/182/182360.json |
| 122870 | atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv | atlas/symbol_profiles/122/122870.json |
| 376300 | atlas/ohlcv_tradable_by_symbol_year/376/376300/2023.csv | atlas/symbol_profiles/376/376300.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | stage label tested | trigger type | evidence family | current profile verdict | outcome label |
|---|---|---|---|---|---|
| TRG_CUBE_STAGE2_2023_05_15 | Stage2-Actionable | Stage2-Actionable | album_preorder_hit | current_profile_too_early | high_mae_success |
| TRG_YG_STAGE2_2023_05_12 | Stage2-Actionable | Stage2-Actionable | global_ip_tour_album | current_profile_false_positive | 4C_late |
| TRG_DEARU_STAGE2_2023_01_11 | Stage2-Actionable | Stage2-Actionable | subscription_platform | current_profile_correct_then_4B_needed | 4B_overlay_success |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE are measured from Stock-Web tradable close at entry date.

| trigger_id | entry date | entry price | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | peak date | peak price | drawdown after peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TRG_CUBE_STAGE2_2023_05_15 | 2023-05-15 | 24300 | +16.05% | -19.09% | +16.05% | -21.44% | +16.05% | -44.07% | 2023-06-21 | 28200 | -51.81% |
| TRG_YG_STAGE2_2023_05_12 | 2023-05-12 | 78100 | +24.20% | -1.92% | +24.20% | -11.52% | +24.20% | -38.67% | 2023-05-31 | 97000 | -50.62% |
| TRG_DEARU_STAGE2_2023_01_11 | 2023-01-11 | 34900 | +66.19% | -1.00% | +66.19% | -1.00% | +66.19% | -1.00% | 2023-02-10 | 58000 | -45.09% |

## 13. Current Calibrated Profile Stress Test

| question | answer for this loop |
|---|---|
| Would current profile allow Stage2? | Yes for all three, because each had public non-price evidence. |
| Was Stage3-Green safe? | Not for CUBE/YG; Green needed contract/retention durability. |
| Was Stage2 bonus too loose? | For C27, bonus is acceptable only as Stage2 watch, not Green bridge. |
| Was Yellow 75 too strict/loose? | Kept. Yellow can absorb C27 evidence without Green. |
| Was Green 87/revision 55 too strict/loose? | Kept or strengthened with repeat-IP/contract-duration guard. |
| Was price-only blowoff guard useful? | Yes; DEARU and YG show 4B needed after price/valuation acceleration. |
| Was full 4B non-price requirement useful? | Yes; contract renewal or retention slowdown is better than price peak alone. |
| Was hard 4C routing late? | YG suggests hard 4C can be late if contract duration breaks after the peak. |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 interpretation | Yellow interpretation | Green interpretation |
|---|---|---|---|
| CUBE | valid Stage2 watch on album/tour momentum | possible Yellow after sales confirmation | Green too early without repeat-IP and contract durability |
| YG | valid Stage2 watch on global IP monetization | possible Yellow only until contract issue | Green false positive if renewal visibility missing |
| DEARU | valid Stage2 on subscription-platform rerating | Yellow if paid-user retention improves | Green only with retention/ARPU proof, otherwise 4B watch |

`green_lateness_ratio` is not computed as a precise Green trigger because this loop deliberately avoids outcome-driven Green relabeling. Green is treated as blocked/late-label comparison for CUBE/YG and watch-only for DEARU.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B evidence type | local peak proximity | full-window peak proximity | verdict |
|---|---|---:|---:|---|
| CUBE | single-IP concentration + price drawdown | n/a | n/a | not full 4B at Stage2; later guard should stop Green |
| YG | contract renewal / IP concentration | 0.80 proxy | 0.80 proxy | non-price 4B should have activated before hard 4C |
| DEARU | platform valuation overheat + retention proof gap | 0.90 proxy | 0.90 proxy | good 4B overlay after fast rerating |

## 16. 4C Protection Audit

| case | 4C label | protection interpretation |
|---|---|---|
| CUBE | thesis_break_watch_only | high-MAE after a valid hit implies Green guard, not automatic hard 4C |
| YG | hard_4c_late | contract uncertainty after IP peak shows hard 4C routing can lag in C27 |
| DEARU | false_break risk if too early | subscription model can recover; use 4B watch before hard 4C |

## 17. Sector-Specific Rule Candidate

No L8-wide global sector rule is proposed. R8 contains platform, content, software, and security models with different quality gates.

```text
sector_specific_rule_candidate = false
reason = C27-only content/IP evidence does not generalize to C26 platform advertising or C28 software/security retention.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C27_CONTENT_IP_GLOBAL_MONETIZATION
candidate_rule = Content/IP Stage2 can use album, tour, fandom platform, or global IP monetization evidence, but Stage3-Green requires at least one durability bridge: repeat-IP pipeline, contract duration/renewal visibility, paid-user retention, ARPU conversion, or margin/royalty conversion. If the trigger is single-IP or contract-renewal dependent, route to Yellow/watch and add 4B watch after price acceleration.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE 90D | avg MAE 90D | false-positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | +35.48% | -11.32% | 0.67 | catches Stage2 but over-allows Green interpretation |
| P1 sector_specific_candidate_profile | 3 | +35.48% | -11.32% | 0.67 | no L8-wide change proposed |
| P2 canonical_archetype_candidate_profile | 3 | +35.48% | -11.32% | 0.33 | blocks Green unless durability bridge exists |
| P3 counterexample_guard_profile | 3 | +35.48% | -11.32% | 0.33 | adds 4B watch for contract/retention risk |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | component explanation |
|---|---|---|
| CUBE | misaligned after 30D | revenue hit was real, but concentration and repeat-IP proof were underweighted |
| YG | misaligned after 90D/180D | global IP was real, but contract duration risk dominated the later path |
| DEARU | aligned for Stage2, not Green | platform rerating was strong, but valuation/retention guard was needed quickly |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK | 1 | 2 | 2 | 1 | 3 | 0 | 3 | 3 | 2 | false | true | needs more non-K-pop content/platform cases |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_early
  - current_profile_false_positive
  - current_profile_4C_too_late
new_axis_proposed: C27_repeat_ip_contract_retention_green_gate
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_watch_before_confirmation
existing_axis_weakened: []
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Stock-Web tradable raw OHLC rows.
- 30D/90D/180D MFE/MAE.
- C27-specific residual behavior in content/IP monetization.
- 4B/4C timing logic for contract/retention risk.

Non-validation scope:

- No production scoring patch.
- No live candidate discovery.
- No current investment view.
- No generalization from K-pop/IP cases to all R8 software/security names.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,repeat_ip_contract_retention_green_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Green requires repeat-IP/contract/retention durability bridge","reduces CUBE/YG false Green risk while keeping DEARU Stage2",TRG_CUBE_STAGE2_2023_05_15|TRG_YG_STAGE2_2023_05_12|TRG_DEARU_STAGE2_2023_01_11,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,single_ip_or_contract_dependency_4b_watch,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"single-group or contract renewal dependency should raise 4B watch after rerating","captures YG drawdown and CUBE high-MAE path",TRG_CUBE_STAGE2_2023_05_15|TRG_YG_STAGE2_2023_05_12,2,2,2,medium,canonical_shadow_only,"4B watch, not hard 4C by itself"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"CUBE_I_FEEL_HIGH_MAE","symbol":"182360","company_name":"큐브엔터","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_CUBE_STAGE2_2023_05_15","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 worked briefly but Green would be too early","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"single-IP hit needs repeat-IP/contract durability before Green"}
{"row_type":"case","case_id":"YG_BLACKPINK_CONTRACT_4C","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"TRG_YG_STAGE2_2023_05_12","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"global IP monetization did not survive contract-renewal uncertainty","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"contract-renewal risk should be non-price 4B watch"}
{"row_type":"case","case_id":"DEARU_PLATFORM_SUBSCRIPTION_OVERHEAT","symbol":"376300","company_name":"디어유","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"TRG_DEARU_STAGE2_2023_01_11","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 was aligned; 4B guard needed after fast platform multiple expansion","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"subscription-platform evidence should require retention/ARPU for Green"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_CUBE_STAGE2_2023_05_15","case_id":"CUBE_I_FEEL_HIGH_MAE","symbol":"182360","company_name":"큐브엔터","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK","sector":"content/IP","primary_archetype":"K-pop album and tour IP monetization","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-14","evidence_available_at_that_date":"I Feel pre-order / Queencard release cycle","evidence_source":"public music-industry source proxy; filing-quality source not asserted","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/182/182360/2023.csv","profile_path":"atlas/symbol_profiles/182/182360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-15","entry_price":24300,"MFE_30D_pct":16.05,"MFE_90D_pct":16.05,"MFE_180D_pct":16.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.09,"MAE_90D_pct":-21.44,"MAE_180D_pct":-44.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-21","peak_price":28200,"drawdown_after_peak_pct":-51.81,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"green_guard_needed_after_high_mae","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"182360_2023-05-15_24300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_YG_STAGE2_2023_05_12","case_id":"YG_BLACKPINK_CONTRACT_4C","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK","sector":"content/IP","primary_archetype":"global artist IP monetization and contract renewal risk","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-12","evidence_available_at_that_date":"Jisoo/Blackpink/tour monetization evidence with contract-duration risk unresolved","evidence_source":"public music-industry source proxy; filing-quality source not asserted","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat","contract_delay"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv","profile_path":"atlas/symbol_profiles/122/122870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-12","entry_price":78100,"MFE_30D_pct":24.20,"MFE_90D_pct":24.20,"MFE_180D_pct":24.20,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.92,"MAE_90D_pct":-11.52,"MAE_180D_pct":-38.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-31","peak_price":97000,"drawdown_after_peak_pct":-50.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.8,"four_b_full_window_peak_proximity":0.8,"four_b_timing_verdict":"non_price_4b_should_precede_hard_4c","four_b_evidence_type":["positioning_overheat","contract_delay","explicit_event_cap"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"122870_2023-05-12_78100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_DEARU_STAGE2_2023_01_11","case_id":"DEARU_PLATFORM_SUBSCRIPTION_OVERHEAT","symbol":"376300","company_name":"디어유","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK","sector":"platform/content subscription","primary_archetype":"fandom platform subscription monetization","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-11","evidence_available_at_that_date":"fandom platform/subscription monetization rerating evidence","evidence_source":"public source proxy; filing-quality source not asserted","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/376/376300/2023.csv","profile_path":"atlas/symbol_profiles/376/376300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-11","entry_price":34900,"MFE_30D_pct":66.19,"MFE_90D_pct":66.19,"MFE_180D_pct":66.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.00,"MAE_90D_pct":-1.00,"MAE_180D_pct":-1.00,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-10","peak_price":58000,"drawdown_after_peak_pct":-45.09,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_local_4b_watch_timing_after_platform_multiple_expansion","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"false_break_risk_if_too_early","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"376300_2023-01-11_34900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CUBE_I_FEEL_HIGH_MAE","trigger_id":"TRG_CUBE_STAGE2_2023_05_15","symbol":"182360","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":45,"relative_strength_score":70,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":45,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":40,"relative_strength_score":60,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable_watch","changed_components":["contract_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"single-IP hit lacks repeat-IP/contract durability; keep Stage2 but block Green","MFE_90D_pct":16.05,"MAE_90D_pct":-21.44,"score_return_alignment_label":"misaligned_if_green","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"YG_BLACKPINK_CONTRACT_4C","trigger_id":"TRG_YG_STAGE2_2023_05_12","symbol":"122870","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":10,"margin_bridge_score":25,"revision_score":55,"relative_strength_score":85,"customer_quality_score":75,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":35,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow_to_Green_candidate","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":20,"revision_score":45,"relative_strength_score":75,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":70,"legal_or_contract_risk_score":85,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable_with_4B_watch","changed_components":["contract_score","legal_or_contract_risk_score","execution_risk_score"],"component_delta_explanation":"global IP monetization remains valid Stage2 evidence but contract-renewal uncertainty blocks Green and adds 4B watch","MFE_90D_pct":24.20,"MAE_90D_pct":-11.52,"score_return_alignment_label":"false_green_avoided","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"DEARU_PLATFORM_SUBSCRIPTION_OVERHEAT","trigger_id":"TRG_DEARU_STAGE2_2023_01_11","symbol":"376300","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":15,"margin_bridge_score":35,"revision_score":55,"relative_strength_score":85,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":75,"execution_risk_score":40,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":15,"margin_bridge_score":35,"revision_score":50,"relative_strength_score":75,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":55,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow_with_4B_watch","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"subscription platform can rerate but needs retention/ARPU proof before Green; 4B watch after fast multiple expansion","MFE_90D_pct":66.19,"MAE_90D_pct":-1.00,"score_return_alignment_label":"stage2_aligned_4b_needed","current_profile_verdict":"current_profile_correct"}
```

### 25.5 residual_contribution rows

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_early","current_profile_false_positive","current_profile_4C_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown file is a v12 post-calibrated residual research output produced using the Songdaiki/stock-web OHLC atlas.

This MD is not live candidate research. It is historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile with a C27-specific shadow guard.

### Price source context

- Primary historical price source: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not treat music-industry source-proxy evidence as direct filing-quality evidence.
- Do not promote C27 to Green without repeat-IP, contract-duration, retention/ARPU, or margin/royalty conversion evidence.
- Price-only entertainment momentum cannot promote Stage2/Stage3.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Preserve global calibrated thresholds unless a later promotion batch explicitly asks for broader changes.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate `R8 -> L8_PLATFORM_CONTENT_SW_SECURITY` consistency.
4. Validate C27 canonical archetype scope.
5. Check hard duplicate key: canonical_archetype_id + symbol + trigger_type + entry_date.
6. Aggregate by C27.
7. Add this loop as C27 shadow guard evidence, not as global Stage3 loosening.
8. Report C27 content/IP residual error types.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 71
next_round = R9
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest max date used for this research: 2026-02-20.
- Stock-Web profile checks were performed for 182360, 122870, and 376300.
- Stock-Web 2023 tradable shard rows were used for entry prices and 30D/90D/180D windows.
- Evidence-source quality is intentionally conservative; where not direct filing-quality, rows remain shadow-only and should be treated as residual calibration evidence rather than immediate production promotion.

## Final Automation Summary

```yaml
scheduled_round: R8
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: KPOP_IP_REPEAT_ALBUM_TOUR_MONETIZATION_VS_CONTRACT_AND_HIT_RISK
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_trigger_family_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
diversity_score_summary: high_new_symbol_and_counterexample_value_with_soft_proxy_evidence_caveat
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C27 needs contract/retention/hit-risk guard beyond global 4B rule
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C27_repeat_ip_contract_retention_green_gate
existing_axis_strengthened: full_4b_requires_non_price_evidence; hard_4c_thesis_break_watch_before_confirmation
existing_axis_weakened: null
next_round: R9
```
