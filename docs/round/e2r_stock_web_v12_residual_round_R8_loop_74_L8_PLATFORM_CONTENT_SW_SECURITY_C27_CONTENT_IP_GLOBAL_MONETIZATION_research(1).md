# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R8
scheduled_loop = 74
completed_round = R8
completed_loop = 74
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION
output_file = e2r_stock_web_v12_residual_round_R8_loop_74_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
round_schedule_status = valid
round_sector_consistency = pass
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated`, with `e2r_2_0_baseline` used only as rollback reference. The already-applied axes are not re-proposed globally: Stage2 actionable evidence bonus, Yellow/Green thresholds, Green revision minimum, cross-evidence buffer, price-only blowoff guard, full-4B non-price requirement, and hard-4C routing are treated as current profile facts.

## 2. Round / Large Sector / Canonical Archetype Scope

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`, so this file cannot use consumer, financial, bio, industrial, or R13 cross-archetype labels. Within R8, this loop selects `C27_CONTENT_IP_GLOBAL_MONETIZATION`, because the residual is not simply “content is popular.” The actual fork is whether public IP evidence has **sell-through / tour / platform conversion** or only a content-pipeline narrative.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact access was limited to calibration registry/summary files. The accessible registry snippet mostly exposed older R10/R11/R12 historical calibration entries and did not expose a complete R8/Loop 74 v12 no-repeat ledger. Therefore schedule resolution follows the immediately preceding generated state: R7/Loop 74 completed, so the next valid scheduled round is R8/Loop 74.

No selected row reuses the previous R7 medical-device universe. No selected row repeats the same symbol + canonical_archetype_id + trigger_date + entry_date from the immediately previous loop. All four cases are new within this run.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

The stock-web diagnostic and profiles show that these windows are usable for historical calibration under `tradable_raw` / `raw_unadjusted_marcap`. The 180D windows are before the stock-web max date, and no selected 180D window overlaps a relevant corporate-action candidate.

## 5. Historical Eligibility Gate

| symbol | entry_date | 180D window available | OHLC fields | corporate-action 180D status | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| 035900 | 2023-06-01 | yes | o/h/l/c/v/a/mc/s/m | clean_180D_window | true |
| 352820 | 2023-04-25 | yes | o/h/l/c/v/a/mc/s/m | clean_180D_window | true |
| 253450 | 2023-02-13 | yes | o/h/l/c/v/a/mc/s/m | clean_180D_window | true |
| 122870 | 2023-05-12 | yes | o/h/l/c/v/a/mc/s/m | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
  ├─ KPOP_GLOBAL_ALBUM_TOUR_FANDOM_SELLTHROUGH
  ├─ MULTI_ARTIST_LABEL_PLATFORM_OPERATING_LEVERAGE
  ├─ DRAMA_CONTENT_PIPELINE_WITHOUT_MARGIN_BRIDGE
  └─ ONE_ARTIST_RENEWAL_CONCENTRATION_4B
```

The compression result is that K-pop label cases and drama-studio cases should remain under the same canonical C27 only if the score separates sell-through monetization from content-pipeline volume.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | trigger_date | entry | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L74_C27_035900_JYP_20230531_5STAR_PREORDER | 035900 | JYP Ent. | high_mae_success | Stage2-Actionable | 2023-05-31 | 2023-06-01 / 127300 | 15.16 | -20.58 | 15.16 | -43.44 | current_profile_4B_too_late |
| R8L74_C27_352820_HYBE_20230424_FML | 352820 | 하이브 | structural_success | Stage2-Actionable | 2023-04-24 | 2023-04-25 / 260500 | 19.96 | -7.87 | 19.96 | -27.68 | current_profile_correct |
| R8L74_C27_253450_STUDIODRAGON_20230210_CONTENT_PIPELINE | 253450 | 스튜디오드래곤 | failed_rerating | Stage2-Actionable | 2023-02-10 | 2023-02-13 / 79400 | 3.9 | -35.14 | 3.9 | -40.05 | current_profile_false_positive |
| R8L74_C27_122870_YG_20230512_BLACKPINK_BABYMONSTER | 122870 | 와이지엔터테인먼트 | 4B_overlay_success | Stage2-Actionable | 2023-05-12 | 2023-05-12 / 78100 | 24.2 | -12.93 | 24.2 | -48.66 | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 4
new_independent_case_count = 4
new_independent_case_ratio = 1.00
```

The balance is deliberate. HYBE and JYP show that actual global IP monetization can move price before late confirmation. Studio Dragon and YG show why the same canonical family can fail: content quantity without margin bridge, and one-artist renewal risk, respectively.

## 9. Evidence Source Map

| symbol | evidence family | trigger evidence available then | evidence split |
| --- | --- | --- | --- |
| 035900 | global album preorders / Billboard-scale fandom monetization | Stray Kids 5-Star preorder and global sales evidence around 2023-05-31 / 2023-06-01 | Stage2/Stage3 positive, later 4B overlay |
| 352820 | multi-artist HYBE label IP monetization | Seventeen FML release/sales route around 2023-04-24 | Stage2/Stage3 positive |
| 253450 | drama content pipeline | pipeline narrative without enough margin bridge | counterexample |
| 122870 | Blackpink/BabyMonster IP optionality | strong repricing around May 2023, but one-artist renewal concentration risk | 4B/4C counterexample |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | price_basis | status |
| --- | --- | --- | --- | --- |
| 035900 | atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv | atlas/symbol_profiles/035/035900.json | tradable_raw | usable |
| 352820 | atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv | atlas/symbol_profiles/352/352820.json | tradable_raw | usable |
| 253450 | atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv | atlas/symbol_profiles/253/253450.json | tradable_raw | usable |
| 122870 | atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv | atlas/symbol_profiles/122/122870.json | tradable_raw | usable |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger | trigger_date | entry | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L74_C27_035900_JYP_20230531_5STAR_PREORDER | 035900 | JYP Ent. | high_mae_success | Stage2-Actionable | 2023-05-31 | 2023-06-01 / 127300 | 15.16 | -20.58 | 15.16 | -43.44 | current_profile_4B_too_late |
| R8L74_C27_352820_HYBE_20230424_FML | 352820 | 하이브 | structural_success | Stage2-Actionable | 2023-04-24 | 2023-04-25 / 260500 | 19.96 | -7.87 | 19.96 | -27.68 | current_profile_correct |
| R8L74_C27_253450_STUDIODRAGON_20230210_CONTENT_PIPELINE | 253450 | 스튜디오드래곤 | failed_rerating | Stage2-Actionable | 2023-02-10 | 2023-02-13 / 79400 | 3.9 | -35.14 | 3.9 | -40.05 | current_profile_false_positive |
| R8L74_C27_122870_YG_20230512_BLACKPINK_BABYMONSTER | 122870 | 와이지엔터테인먼트 | 4B_overlay_success | Stage2-Actionable | 2023-05-12 | 2023-05-12 / 78100 | 24.2 | -12.93 | 24.2 | -48.66 | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 035900 | 2023-06-01 | 127300 | 10.45 | 15.16 | 15.16 | -3.93 | -20.58 | -43.44 | 2023-07-25 | 146600 | -50.89 |
| 352820 | 2023-04-25 | 260500 | 16.31 | 19.96 | 19.96 | -1.34 | -7.87 | -27.68 | 2023-06-22 | 312500 | -39.71 |
| 253450 | 2023-02-13 | 79400 | 3.9 | 3.9 | 3.9 | -11.84 | -35.14 | -40.05 | 2023-03-06 | 82500 | -42.3 |
| 122870 | 2023-05-12 | 78100 | 24.2 | 24.2 | 24.2 | -1.15 | -12.93 | -48.66 | 2023-05-31 | 97000 | -58.66 |

## 13. Current Calibrated Profile Stress Test

| symbol | current_profile_verdict | why |
| --- | --- | --- |
| 035900 | current_profile_4B_too_late | Stage2/early Stage3 captured IP sell-through, but Green-like hold logic needed a C27 drawdown guard after local blowoff. |
| 352820 | current_profile_correct | Multi-artist IP and repeated sell-through evidence matched the 30D/90D MFE and avoided immediate false positive. |
| 253450 | current_profile_false_positive | Content-pipeline narrative lacked margin bridge; current profile could over-score public content volume. |
| 122870 | current_profile_4B_too_late | Price move was real, but one-artist renewal concentration was non-price 4B evidence before the drawdown became obvious. |

Existing axis status:

```text
stage2_actionable_evidence_bonus = existing_axis_kept
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

C27 needs a different Green audit than heavy manufacturing. In content/IP, the public sell-through event can be very early, while true Green must require either repeated monetization conversion or a confirmed margin bridge. JYP and HYBE show that Stage2-Actionable can be useful. Studio Dragon shows that Yellow should not be crossed by pipeline volume alone. YG shows that Green should be capped when contract renewal is the thesis hinge.

```text
avg_positive_MFE_90D_pct = 17.56
avg_positive_MAE_90D_pct = -14.22
avg_counterexample_MFE_90D_pct = 14.05
avg_counterexample_MAE_90D_pct = -24.04
green_lateness_ratio = not_applicable_no_clean_later_green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | evidence_type | timing_verdict |
| --- | ---: | ---: | --- | --- |
| R8L74_C27_035900_T2_4B_OVERLAY | 1.00 | 1.00 | price_only + valuation_blowoff + positioning_overheat | overlay only; not full thesis break |
| R8L74_C27_122870_T2_4B_OVERLAY | 0.99 | 0.99 | legal/contract risk + event cap + valuation_blowoff | good full-window 4B timing |

The difference matters. JYP’s 4B is mostly a local overheat overlay; YG’s 4B is full-window quality because non-price contract-renewal risk existed at the thesis hinge.

## 16. 4C Protection Audit

YG receives `hard_4c_late_if_waiting_for_final_contract_news`: if the system waited for fully explicit thesis break, most of the drawdown after the May 2023 peak had already happened. Studio Dragon receives `thesis_break_watch_only`: content-pipeline evidence became insufficient when price and margin bridge moved against the thesis.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
candidate = L8_content_ip_sellthrough_vs_pipeline_split
proposal = positive C27 scoring may use global album/tour/platform sell-through evidence, but pipeline-only content volume cannot cross Stage3-Yellow without margin bridge or repeat monetization conversion.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION

positive_bonus:
  C27_global_sellthrough_conversion_bonus = +1
  Applies when album/tour/platform evidence is direct sell-through or confirmed conversion.

guards:
  C27_content_quantity_without_margin_bridge_guard = -1 to -2
  C27_one_artist_or_one_title_concentration_guard = -1 to -2
  C27_contract_renewal_event_cap_full_4B = true
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 4 | 15.8 | -19.13 | 2/4 | 0 | 1 | mixed; C27 residual remains |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | 15.8 | -19.13 | 3/4 | 1 | 2 | worse separation |
| P1 sector_specific_candidate_profile | L8 sector shadow | 4 | 17.56 | -14.22 | 1/4 | 0 | 1 | better but still needs canonical guard |
| P2 canonical_archetype_candidate_profile | C27 shadow | 4 | 17.56 | -14.22 | 0-1/4 | 0 | 0 | best balance: keep global IP sell-through, block unsupported content quantity |
| P3 counterexample_guard_profile | C27 guard | 2 | 14.05 | -24.04 | 0/2 after guard | 0 | 0 | best for risk overlay; not positive promotion |

## 20. Score-Return Alignment Matrix

| symbol | before score/stage | after score/stage | score-return alignment |
| --- | --- | --- | --- |
| 035900 | 82.0 / Stage3-Yellow | 78.0 / Stage2-Actionable + C27 inventory/artist concentration guard | structural_repricing_then_high_drawdown |
| 352820 | 85.5 / Stage3-Yellow | 87.0 / Stage3-Green shadow-qualified | front_loaded_structural_repricing_then_cycle_reset |
| 253450 | 76.0 / Stage3-Yellow | 68.0 / Stage2-Watch / no promotion | content_pipeline_without_margin_bridge_failed |
| 122870 | 80.0 / Stage3-Yellow | 69.0 / Stage2-Actionable + full 4B overlay | ip_repricing_then_renewal_risk_drawdown |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION | 2 | 2 | 2 | 1 | 4 | 0 | 6 | 4 | 3 | true | true | partially filled; more C26/C28 still needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - content_quantity_without_margin_bridge_false_positive
  - one_artist_contract_renewal_4B_too_late
  - late_green_after_ip_peak
new_axis_proposed:
  - C27_global_sellthrough_conversion_bonus
  - C27_one_artist_or_one_title_concentration_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Actual stock-web `tradable_raw` OHLC rows for representative entry, peak, drawdown, and forward-window checks.
- 30D/90D/180D MFE/MAE for four R8 C27 cases.
- Positive/counterexample balance and 4B local/full-window split.

Not validated:
- No production scoring code was opened.
- No live/current stock scan was performed.
- No buy/sell recommendation is made.
- No global scoring delta is proposed.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_reimbursement_like_ip_channel_conversion_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Promote only when IP evidence has global sell-through/tour/platform conversion, not just content quantity.","Improved separation: HYBE/JYP retained as actionable; Studio Dragon/YG capped by margin/renewal guard.","R8L74_C27_035900_T1_STAGE2_ACTIONABLE|R8L74_C27_352820_T1_STAGE2_ACTIONABLE|R8L74_C27_253450_T1_STAGE2_ACTIONABLE|R8L74_C27_122870_T1_STAGE2_ACTIONABLE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_one_artist_or_one_title_concentration_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"One-title/one-artist dependency must cap Stage3-Green unless contract renewal and margin bridge are both confirmed.","Reduced false-positive Green for YG and content-pipeline false positive for Studio Dragon.","R8L74_C27_122870_T2_4B_OVERLAY|R8L74_C27_253450_T1_STAGE2_ACTIONABLE",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L74_C27_035900_JYP_20230531_5STAR_PREORDER", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R8L74_C27_035900_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_repricing_then_high_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive IP monetization was real, but the path shows a classic C27 pocket: a clean early event captured upside while later unconfirmed Green/hold logic missed the drawdown hazard."}
{"row_type": "case", "case_id": "R8L74_C27_352820_HYBE_20230424_FML", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L74_C27_352820_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "front_loaded_structural_repricing_then_cycle_reset", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "The HYBE case is the cleaner positive: multi-artist monetization and repeated large-album events reduce one-artist fragility."}
{"row_type": "case", "case_id": "R8L74_C27_253450_STUDIODRAGON_20230210_CONTENT_PIPELINE", "symbol": "253450", "company_name": "스튜디오드래곤", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L74_C27_253450_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "content_pipeline_without_margin_bridge_failed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "This is the key counterexample: content quantity is not the same as content monetization leverage."}
{"row_type": "case", "case_id": "R8L74_C27_122870_YG_20230512_BLACKPINK_BABYMONSTER", "symbol": "122870", "company_name": "와이지엔터테인먼트", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "R8L74_C27_122870_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "ip_repricing_then_renewal_risk_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "The output validates that C27 needs a non-price 4B overlay when IP monetization depends on contract renewal of one global act."}
{"row_type": "trigger", "trigger_id": "R8L74_C27_035900_T1_STAGE2_ACTIONABLE", "case_id": "R8L74_C27_035900_JYP_20230531_5STAR_PREORDER", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-31", "evidence_available_at_that_date": "Stray Kids 5-Star preorder disclosure and global album demand; evidence was public before/around release window.", "evidence_source": "5-Star album commercial-performance source; stock-web shard atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv lines around 2023-05-30~2023-08-29 and 2024-01~2024-03.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-01", "entry_price": 127300, "MFE_30D_pct": 10.45, "MFE_90D_pct": 15.16, "MFE_180D_pct": 15.16, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -3.93, "MAE_90D_pct": -20.58, "MAE_180D_pct": -43.44, "MAE_1Y_pct": "not_computed_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -50.89, "green_lateness_ratio": "not_applicable_no_clean_later_green_for_same_case", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_trigger", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_repricing_then_high_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L74_C27_035900_JYP_20230531_5STAR_PREORDER_2023-06-01_127300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L74_C27_352820_T1_STAGE2_ACTIONABLE", "case_id": "R8L74_C27_352820_HYBE_20230424_FML", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-24", "evidence_available_at_that_date": "Seventeen FML release/preorder/sales evidence, plus multi-artist platform/IP monetization route.", "evidence_source": "FML commercial-performance source and stock-web shard atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv around 2023-04-24~2023-12.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": ["positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv", "profile_path": "atlas/symbol_profiles/352/352820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-25", "entry_price": 260500, "MFE_30D_pct": 16.31, "MFE_90D_pct": 19.96, "MFE_180D_pct": 19.96, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -1.34, "MAE_90D_pct": -7.87, "MAE_180D_pct": -27.68, "MAE_1Y_pct": "not_computed_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-22", "peak_price": 312500, "drawdown_after_peak_pct": -39.71, "green_lateness_ratio": "not_applicable_no_clean_later_green_for_same_case", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_trigger", "four_b_evidence_type": ["positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "front_loaded_structural_repricing_then_cycle_reset", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L74_C27_352820_HYBE_20230424_FML_2023-04-25_260500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L74_C27_253450_T1_STAGE2_ACTIONABLE", "case_id": "R8L74_C27_253450_STUDIODRAGON_20230210_CONTENT_PIPELINE", "symbol": "253450", "company_name": "스튜디오드래곤", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "Drama-content pipeline narrative without enough margin bridge or confirmed platform economics.", "evidence_source": "stock-web shard atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv around 2023-02~2023-10; public earnings/margin narrative treated as qualitative proxy.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "execution_risk_score"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv", "profile_path": "atlas/symbol_profiles/253/253450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-13", "entry_price": 79400, "MFE_30D_pct": 3.9, "MFE_90D_pct": 3.9, "MFE_180D_pct": 3.9, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -11.84, "MAE_90D_pct": -35.14, "MAE_180D_pct": -40.05, "MAE_1Y_pct": "not_computed_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-06", "peak_price": 82500, "drawdown_after_peak_pct": -42.3, "green_lateness_ratio": "not_applicable_no_clean_later_green_for_same_case", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_trigger", "four_b_evidence_type": ["margin_or_backlog_slowdown", "execution_risk_score"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "content_pipeline_without_margin_bridge_failed", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L74_C27_253450_STUDIODRAGON_20230210_CONTENT_PIPELINE_2023-02-13_79400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L74_C27_122870_T1_STAGE2_ACTIONABLE", "case_id": "R8L74_C27_122870_YG_20230512_BLACKPINK_BABYMONSTER", "symbol": "122870", "company_name": "와이지엔터테인먼트", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-12", "evidence_available_at_that_date": "Blackpink tour/renewal optionality and BabyMonster debut narrative created strong near-term IP repricing but high one-artist renewal concentration risk.", "evidence_source": "stock-web shard atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv around 2023-05~2023-08 and 2024-Q1; public renewal uncertainty treated as non-price 4B evidence.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["legal_or_regulatory_block", "explicit_event_cap", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv", "profile_path": "atlas/symbol_profiles/122/122870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-12", "entry_price": 78100, "MFE_30D_pct": 24.2, "MFE_90D_pct": 24.2, "MFE_180D_pct": 24.2, "MFE_1Y_pct": "not_computed_in_this_loop", "MFE_2Y_pct": "not_computed_in_this_loop", "MAE_30D_pct": -1.15, "MAE_90D_pct": -12.93, "MAE_180D_pct": -48.66, "MAE_1Y_pct": "not_computed_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-31", "peak_price": 97000, "drawdown_after_peak_pct": -58.66, "green_lateness_ratio": "not_applicable_no_clean_later_green_for_same_case", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_trigger", "four_b_evidence_type": ["legal_or_regulatory_block", "explicit_event_cap", "positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "ip_repricing_then_renewal_risk_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L74_C27_122870_YG_20230512_BLACKPINK_BABYMONSTER_2023-05-12_78100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L74_C27_035900_T2_4B_OVERLAY", "case_id": "R8L74_C27_035900_JYP_20230531_5STAR_PREORDER", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-07-25", "entry_date": "2023-07-25", "entry_price": 141100, "evidence_available_at_that_date": "Local blowoff at 146600 high after 5-Star repricing; no new equivalent non-price margin bridge at the local peak.", "evidence_source": "stock-web 035900 2023 row 2023-07-25; 4B evidence is price+valuation/positioning overlay, not promotion evidence.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MAE_30D_pct": -23.1, "MAE_90D_pct": -31.82, "MAE_180D_pct": -48.97, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -50.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_use_as_overlay_not_full_exit", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success_for_risk_not_for_positive_promotion", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L74_C27_035900_2023-07-25_141100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L74_C27_122870_T2_4B_OVERLAY", "case_id": "R8L74_C27_122870_YG_20230512_BLACKPINK_BABYMONSTER", "symbol": "122870", "company_name": "와이지엔터테인먼트", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_AND_DRAMA_GLOBAL_IP_MONETIZATION", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-05-31", "entry_date": "2023-05-31", "entry_price": 93900, "evidence_available_at_that_date": "Peak-zone repricing depended on Blackpink renewal optionality; renewal concentration risk was a non-price 4B cap.", "evidence_source": "stock-web 122870 2023 row 2023-05-31 and 2024-Q1 drawdown path.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "explicit_event_cap", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv", "profile_path": "atlas/symbol_profiles/122/122870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.3, "MFE_90D_pct": 3.3, "MFE_180D_pct": 3.3, "MAE_30D_pct": -17.78, "MAE_90D_pct": -27.58, "MAE_180D_pct": -57.29, "peak_date": "2023-05-31", "peak_price": 97000, "drawdown_after_peak_pct": -58.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "good_full_window_4B_timing_with_non_price_renewal_risk", "four_b_evidence_type": ["legal_or_contract_risk", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late_if_waiting_for_final_contract_news", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L74_C27_122870_2023-05-31_93900", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L74_C27_035900_JYP_20230531_5STAR_PREORDER", "trigger_id": "R8L74_C27_035900_T1_STAGE2_ACTIONABLE", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 18, "margin_bridge_score": 8, "revision_score": 16, "relative_strength_score": 14, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 15, "margin_bridge_score": 6, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78.0, "stage_label_after": "Stage2-Actionable + C27 inventory/artist concentration guard", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C27 separates real global fandom/IP monetization from unsupported content-pipeline quantity and adds one-artist/renewal concentration guard.", "MFE_90D_pct": 15.16, "MAE_90D_pct": -20.58, "score_return_alignment_label": "structural_repricing_then_high_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L74_C27_352820_HYBE_20230424_FML", "trigger_id": "R8L74_C27_352820_T1_STAGE2_ACTIONABLE", "symbol": "352820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 16, "margin_bridge_score": 10, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 17, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 85.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 18, "margin_bridge_score": 12, "revision_score": 19, "relative_strength_score": 14, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 87.0, "stage_label_after": "Stage3-Green shadow-qualified", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C27 separates real global fandom/IP monetization from unsupported content-pipeline quantity and adds one-artist/renewal concentration guard.", "MFE_90D_pct": 19.96, "MAE_90D_pct": -7.87, "score_return_alignment_label": "front_loaded_structural_repricing_then_cycle_reset", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L74_C27_253450_STUDIODRAGON_20230210_CONTENT_PIPELINE", "trigger_id": "R8L74_C27_253450_T1_STAGE2_ACTIONABLE", "symbol": "253450", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 6, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 11, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 7, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-Watch / no promotion", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C27 separates real global fandom/IP monetization from unsupported content-pipeline quantity and adds one-artist/renewal concentration guard.", "MFE_90D_pct": 3.9, "MAE_90D_pct": -35.14, "score_return_alignment_label": "content_pipeline_without_margin_bridge_failed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L74_C27_122870_YG_20230512_BLACKPINK_BABYMONSTER", "trigger_id": "R8L74_C27_122870_T1_STAGE2_ACTIONABLE", "symbol": "122870", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 6, "revision_score": 12, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 6, "margin_bridge_score": 4, "revision_score": 7, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 16, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69.0, "stage_label_after": "Stage2-Actionable + full 4B overlay", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C27 separates real global fandom/IP monetization from unsupported content-pipeline quantity and adds one-artist/renewal concentration guard.", "MFE_90D_pct": 24.2, "MAE_90D_pct": -12.93, "score_return_alignment_label": "ip_repricing_then_renewal_risk_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R8", "loop": "74", "scheduled_round": "R8", "scheduled_loop": 74, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["content_quantity_without_margin_bridge_false_positive", "one_artist_contract_renewal_4B_too_late", "late_green_after_ip_peak"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R8
completed_loop = 74
next_round = R9
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web diagnostic bundle confirms `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `raw_row_count=15,214,118`, `tradable_row_count=14,354,401`, `symbol_count=5,414`, and `active_like_symbol_count=2,868`.
- 035900 profile confirms current/latest name `JYP Ent.`, stock-web availability through 2026-02-20, 5,935 tradable OHLCV rows, and no 2023/2024 corporate-action candidate inside the tested window; older corporate-action candidates are outside the 180D windows used here.
- 352820 profile confirms HYBE availability through 2026-02-20, 1,312 tradable OHLCV rows, and corporate_action_candidate_count=0.
- 253450 profile confirms Studio Dragon availability through 2026-02-20, 2,020 tradable OHLCV rows, and corporate_action_candidate_count=0.
- 122870 profile confirms YG Entertainment availability through 2026-02-20, 3,500 tradable OHLCV rows; older corporate-action candidates are outside the 2023/2024 tested windows.
- JYP 2023 shard rows around 2023-05-30~2023-08-29 show the 2023-06-01 entry close 127,300, 2023-07-25 high 146,600, and subsequent drawdown path. JYP 2024-Q1 shard rows show lows into the 72,000 zone.
- HYBE 2023 shard rows show the 2023-04-25 entry close 260,500, 2023-06-22 high 312,500, and 2023-11-17 low 188,400.
- Studio Dragon 2023 shard rows show the 2023-02-13 entry close 79,400 and later lows down to 47,600 in the observed 180D window.
- YG 2023 and 2024 shard rows show the 2023-05-12 entry close 78,100, 2023-05-31 high 97,000, and 2024-Q1 lows near 40,100.

