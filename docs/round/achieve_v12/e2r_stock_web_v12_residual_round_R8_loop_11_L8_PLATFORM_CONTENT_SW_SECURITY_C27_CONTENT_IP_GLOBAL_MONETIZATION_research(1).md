# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 11
sector = 플랫폼·콘텐츠·SW·보안
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = GLOBAL_MUSIC_LABEL_DISTRIBUTION_AND_CONTENT_STUDIO_MONETIZATION_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R8_loop_11_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not current/live candidate discovery, not an investment recommendation, not a `stock_agent` code patch, and not a production scoring promotion.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The already-applied global profile is treated as the starting state, not as a conclusion to re-prove. The applied diff already shows global Stage2, Yellow/Green, and non-price 4B/4C guardrails promoted from the first calibration set. fileciteturn278file0

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R8 |
| loop | 11 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| fine_archetype_id | GLOBAL_MUSIC_LABEL_DISTRIBUTION_AND_CONTENT_STUDIO_MONETIZATION_BRIDGE |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |

Canonical compression: this loop compresses music-label distribution, label M&A, streaming-content hit, and artist-contract concentration into C27. The unifying question is whether global IP attention becomes monetizable, recurring, and revision-visible economics.

## 3. Previous Coverage / Duplicate Avoidance Check

The ingest snapshot covers R1~R13 and loops 1~9, with 1,376 aggregate representative trigger rows and 3,215 rejected rows. It also shows all large sectors are present, so this loop uses a same-sector but new-canonical gap rather than adding another C26 platform ad-leverage study. fileciteturn277file0

Local prior MD state also already contains R8/C26, while no local R8/C27 file existed before this run. Therefore this loop is treated as same large sector but new canonical archetype coverage. No `src/e2r` code was opened or inferred.

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest validation:

| field | value |
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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The manifest explicitly states raw/unadjusted OHLC, zero-volume/zero-OHLC exclusion from calibration shards, and corporate-action contaminated windows blocked by default. fileciteturn280file0 The schema defines the tradable columns and MFE/MAE formulas used here. fileciteturn281file0

## 5. Historical Eligibility Gate

| case_id | symbol | profile status | 180D forward window | corporate-action status | calibration_usable |
|---|---:|---|---|---|---|
| R8L11-C27-HYBE-QC-20230210 | 352820 | active_like; no corporate-action candidates | available | clean_180D_window | true |
| R8L11-C27-JYP-5STAR-20230531 | 035900 | active_like; old corporate-action candidates only through 2013 | available | clean_180D_window | true |
| R8L11-C27-STUDIODRAGON-GLORY-20230103 | 253450 | active_like; no corporate-action candidates | available | clean_180D_window | true |
| R8L11-C27-YG-BLACKPINK-20230512 | 122870 | active_like; old corporate-action candidates only through 2014 | available | clean_180D_window | true |

Profiles confirm the relevant symbols, market status, available year files, and corporate-action candidate dates. fileciteturn283file0 fileciteturn284file0 fileciteturn285file0 fileciteturn286file0

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GLOBAL_LABEL_MA_ACCRETIVE_OPTIONALITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | M&A gives new catalog/label/channel option value, but accretion must be proven. |
| QUANTIFIED_GLOBAL_ALBUM_DEMAND_AND_US_DISTRIBUTION | C27_CONTENT_IP_GLOBAL_MONETIZATION | Album preorder/US distribution is stronger than narrative-only IP because demand is quantified. |
| GLOBAL_STREAMING_HIT_WITHOUT_MARGIN_BRIDGE | C27_CONTENT_IP_GLOBAL_MONETIZATION | Hit-title attention must not be equal to producer economics. |
| ARTIST_CONCENTRATION_IP_RUN_WITH_CONTRACT_OVERHANG | C27_CONTENT_IP_GLOBAL_MONETIZATION | One mega-IP can produce price momentum but also creates renewal cliffs. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | why selected |
|---|---:|---|---|---|---|
| R8L11-C27-HYBE-QC-20230210 | 352820 | 하이브 | positive / high_mae_success | U.S. label M&A | A direct global-label route generated large 90/180D MFE but with early MAE. |
| R8L11-C27-JYP-5STAR-20230531 | 035900 | JYP Ent. | positive / 4B_overlay_success | quantified album demand + U.S. distribution | Valid C27 upside, followed by cycle-cooling drawdown that tests 4B overlay. |
| R8L11-C27-STUDIODRAGON-GLORY-20230103 | 253450 | 스튜디오드래곤 | counterexample / failed_rerating | streaming hit without economics | A global hit did not translate into durable equity rerating. |
| R8L11-C27-YG-BLACKPINK-20230512 | 122870 | 와이지엔터테인먼트 | counterexample / 4B_overlay_success | artist concentration + contract cliff | The price run required non-price 4B once contract overhang became explicit. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
new_independent_case_count = 4
reused_case_count = 0
```

The point is not “K-pop good / drama bad.” The mechanism is sharper: global attention only matters when it closes into distribution, monetization, repeatability, and revision visibility. A stage system that cannot distinguish “crowd cheering outside the store” from “cash register ringing inside the store” will over-promote C27.

## 9. Evidence Source Map

HYBE’s Quality Control acquisition was announced/reported in February 2023 as a $300 million transaction led by HYBE America, giving HYBE a direct North American label/catalog route. citeturn474190news1 Stray Kids’ `5-Star` crossed record preorder thresholds before release and later topped the Billboard 200, making JYP’s demand evidence materially stronger than a vague fandom narrative. citeturn474190search0 The Glory was a global Netflix hit and became one of the most-watched non-English Netflix series, but that title success did not by itself prove Studio Dragon margin/revision capture. citeturn491501search3 Blackpink’s December 2023 group-renewal news left individual activities separate, illustrating why artist-contract concentration is non-price risk evidence, not just volatility. citeturn491501search1

## 10. Price Data Source Map

| symbol | profile_path | primary shard(s) used | key row citations |
|---:|---|---|---|
| 352820 | atlas/symbol_profiles/352/352820.json | atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv | Feb~Jun and Jul~Dec 2023 rows. fileciteturn290file0 fileciteturn291file0 |
| 035900 | atlas/symbol_profiles/035/035900.json | atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv; 2024.csv | May~Sep and Sep~Dec 2023 rows plus Jan~Mar 2024 drawdown rows. fileciteturn287file0 fileciteturn288file0 fileciteturn289file0 |
| 253450 | atlas/symbol_profiles/253/253450.json | atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv | Jan~Aug 2023 failure path. fileciteturn292file0 |
| 122870 | atlas/symbol_profiles/122/122870.json | atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv; 2024.csv | May~Sep, Sep~Dec 2023, and Jan~Mar 2024 overhang rows. fileciteturn293file0 fileciteturn294file0 fileciteturn295file0 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence | current_profile_verdict |
|---|---|---|---|---|---:|---|---|---|---|
| R8L11-C27-HYBE-T1 | HYBE-QC | Stage2-Actionable | 2023-02-09 | 2023-02-10 | 195,300 | M&A/public event; U.S. label route | multiple public sources, no revision close | execution-risk watch | current_profile_correct |
| R8L11-C27-JYP-T1 | JYP-5STAR | Stage2-Actionable | 2023-05-30 | 2023-05-31 | 122,000 | quantified preorder; global distribution; RS | watch for financial visibility | positioning/cycle cooling watch | current_profile_too_late |
| R8L11-C27-JYP-T2 | JYP-5STAR | Stage4B-Overlay | 2023-07-25 | 2023-07-25 | 141,100 | none | none | valuation/positioning/cycle overheat | current_profile_correct |
| R8L11-C27-SD-T1 | StudioDragon-Glory | Stage2-Watch | 2023-01-02 | 2023-01-03 | 85,300 | global streaming hit | multiple public sources only | margin/backlog slowdown watch | current_profile_false_positive |
| R8L11-C27-YG-T1 | YG-BLACKPINK | Stage2-PriceRun | 2023-05-12 | 2023-05-12 | 78,100 | relative strength; global artist IP | no contract/revision close | concentration risk | current_profile_4B_too_late |
| R8L11-C27-YG-T2 | YG-BLACKPINK | Stage4B-Overlay | 2023-09-21 | 2023-09-22 | 66,400 | none | none | explicit contract overhang | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| HYBE-T1 | 195,300 | 11.88% | -12.80% | 60.01% | -12.80% | 60.01% | -12.80% | 2023-06-22 | 312,500 | -35.36% |
| JYP-T1 | 122,000 | 15.25% | -2.95% | 20.16% | -17.13% | 20.16% | -40.98% | 2023-07-25 | 146,600 | -50.89% |
| JYP-T2 | 141,100 | 3.90% | -23.10% | 3.90% | -27.21% | 3.90% | -48.97% | 2023-07-25 | 146,600 | -50.89% |
| StudioDragon-T1 | 85,300 | 2.93% | -11.14% | 2.93% | -26.49% | 2.93% | -44.20% | 2023-01-03 | 87,800 | -45.79% |
| YG-T1 | 78,100 | 24.20% | -1.92% | 24.20% | -12.93% | 24.20% | -47.76% | 2023-05-31 | 97,000 | -57.94% |
| YG-T2 | 66,400 | 3.61% | -24.55% | 3.61% | -27.86% | 3.61% | -39.91% | 2023-09-25 | 68,800 | -41.72% |

## 13. Current Calibrated Profile Stress Test

| case | P0 likely behavior | actual OHLC verdict | residual |
|---|---|---|---|
| HYBE QC | Stage2/Yellow, not Green because revision not confirmed | correct: strong MFE but high early MAE | no new global change; C27 M&A route can remain Yellow until accretion |
| JYP 5-Star | Stage2/Yellow; Green likely waits for revision | slightly too late for early C27 demand capture | add C27 quantified-demand/distribution bonus, still not automatic Green |
| StudioDragon The Glory | possible false Yellow/Green if hit-title evidence overweighted | failed rerating | hit-without-economics guard needed |
| YG Blackpink | price run could look like Stage3 if artist IP overweighted | 4B came late; large post-peak drawdown | artist-contract concentration must activate non-price 4B |

## 14. Stage2 / Yellow / Green Comparison

C27 is a case where Stage2 evidence often arrives as “attention”: chart rank, Netflix rank, tour demand, M&A headlines. The calibration split is whether the attention is already tied to a cash channel.

HYBE and JYP have a channel bridge: label acquisition or global distributor/album economics. Studio Dragon and YG show why hit-title or single-IP momentum alone is brittle. Green should require one of three closures: quantified paid demand, repeat-order/channel conversion, or visible margin/revision bridge.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| JYP-T2 | valuation_blowoff; positioning_overheat; cycle cooling | 1.00 | 1.00 | good_full_window_4B_timing |
| YG-T2 | contract_delay; explicit_event_cap | 0.78 | 0.78 | good_full_window_4B_timing |
| YG-T1 | price run with latent contract overhang | 0.74 | 1.00 | non-price 4B needed after run |

This strengthens the existing full_4b_requires_non_price_evidence axis inside C27, not globally. Price-only peaks are noisy, but artist-contract risk, renewal ambiguity, or cycle-cooling evidence is exactly the kind of non-price 4B that protects after a valid IP run.

## 16. 4C Protection Audit

No full hard 4C row is proposed. YG-T2 is marked `thesis_break_watch_only`, not hard 4C, because the group renewal later partially preserved group-IP optionality even though individual activity economics weakened YG’s capture. This keeps 4C strict and avoids turning every contract scare into thesis-break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c27_paid_global_distribution_or_MA_bridge_bonus
proposal = +1 shadow-only to C27 score when global IP evidence is tied to a paid channel, label/distribution control, or quantified demand.
```

Rationale: HYBE and JYP both produced strong MFE when the global IP cue was attached to a cash channel. This does not apply to streaming-title fame alone.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c27_hit_without_financial_visibility_green_cap
proposal = cap C27 at Stage2/Yellow when global hit evidence lacks margin bridge, repeat slate economics, contract clarity, or revision confirmation.
```

Rationale: Studio Dragon and YG separate attention from monetization. In C27, the “audience” is not the “buyer” unless the company captures economics.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible representatives | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 4 | 26.83% | -17.34% | 26.83% | -36.44% | 50% | mixed; C27 false positives remain |
| P0b e2r_2_0_baseline_reference | old baseline | 4 | 26.83% | -17.34% | 26.83% | -36.44% | 50%+ | worse; weaker 4B/Green guard |
| P1 sector_specific_candidate_profile | L8 | 4 | 26.83% | -17.34% | 26.83% | -36.44% | 25~50% | useful but too broad for all L8 |
| P2 canonical_archetype_candidate_profile | C27 | 2 selected positives | 40.09% | -14.97% | 40.09% | -26.89% | 0% | best explanatory alignment |
| P3 counterexample_guard_profile | C27 guard | 4 scored, 2 capped | 40.09% on promoted rows | -14.97% | 40.09% | -26.89% | 0% | keeps global axes, adds C27 guard |

## 20. Score-Return Alignment Matrix

| case | P0 label | proposed C27 label | 90D return alignment | 180D drawdown lesson |
|---|---|---|---|---|
| HYBE | Stage3-Yellow | Stage3-Yellow with C27 M&A bridge | aligned | keep Green strict until accretion/revision |
| JYP | Stage3-Yellow | Stage3-Yellow+ with quantified-demand bonus | aligned early | add 4B cycle/positioning overlay |
| Studio Dragon | Stage3-Yellow risk | Stage2-Watch cap | improved | hit-title evidence was not monetization |
| YG | Stage3-Yellow risk | Stage2-Watch / 4B overlay | improved | contract concentration is non-price 4B |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | GLOBAL_MUSIC_LABEL_DISTRIBUTION_AND_CONTENT_STUDIO_MONETIZATION_BRIDGE | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 2 | false | true | C27 now has positive/counterexample/4B coverage; hard 4C still open |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage3_green_revision_min, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage]
residual_error_types_found: [content_hit_without_economics_false_positive, artist_contract_overhang_late_4B, album_cycle_local_peak_after_valid_stage2]
new_axis_proposed: [c27_paid_global_distribution_or_MA_bridge_bonus, c27_hit_without_financial_visibility_green_cap, c27_artist_contract_concentration_4b_overlay]
existing_axis_strengthened: [full_4b_requires_non_price_evidence within C27, stage3_green_revision_min within C27]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger-level OHLC using stock-web tradable_raw shards; 30D/90D/180D MFE/MAE; C27-specific positive/counterexample split; non-price 4B overlay timing.

Not validated: live candidate discovery, current 2026 recommendation, production scoring patch, broker connection, full 1Y/2Y extended-window calibration, hard 4C timing for C27.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_paid_global_distribution_or_MA_bridge_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,Quantified global distribution/M&A route with non-price evidence improved HYBE/JYP alignment without promoting hit-only cases.,Selected positive avg MFE90 40.09 pct vs MAE90 -14.97 pct; false positives excluded.,R8L11-C27-HYBE-T1|R8L11-C27-JYP-T1,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c27_hit_without_financial_visibility_green_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1 guard,Streaming or chart hit alone must cap at Stage2/Yellow until margin/revision/contract economics close.,Studio Dragon false positive reduced from Yellow to Stage2-Watch; YG run converted to 4B overlay.,R8L11-C27-SD-T1|R8L11-C27-YG-T1,4,4,2,medium,counterexample_guard,not production; post-calibrated residual
shadow_weight,c27_artist_contract_concentration_4b_overlay,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1 overlay,"Artist concentration or renewal uncertainty is non-price 4B evidence, not merely price volatility.",YG 4B overlay avoided large post-run drawdown; strengthens existing non-price 4B axis in C27.,R8L11-C27-YG-T2|R8L11-C27-JYP-T2,6,4,2,medium,4B_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R8L11-C27-HYBE-QC-20230210","symbol":"352820","company_name":"하이브","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_MUSIC_LABEL_DISTRIBUTION_AND_CONTENT_STUDIO_MONETIZATION_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R8L11-C27-HYBE-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Global IP M&A gave early but volatile Stage2; 90/180D MFE was strong, but revision/accumulation was not clean enough for early Green.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Global IP M&A gave early but volatile Stage2; 90/180D MFE was strong, but revision/accumulation was not clean enough for early Green."}
{"row_type":"case","case_id":"R8L11-C27-JYP-5STAR-20230531","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_MUSIC_LABEL_DISTRIBUTION_AND_CONTENT_STUDIO_MONETIZATION_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R8L11-C27-JYP-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Quantified global album demand and U.S. distribution route captured a valid Stage2/Yellow run, but later concentration/album-cycle cooling required 4B overlay.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Quantified global album demand and U.S. distribution route captured a valid Stage2/Yellow run, but later concentration/album-cycle cooling required 4B overlay."}
{"row_type":"case","case_id":"R8L11-C27-STUDIODRAGON-GLORY-20230103","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_MUSIC_LABEL_DISTRIBUTION_AND_CONTENT_STUDIO_MONETIZATION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R8L11-C27-SD-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Global hit attention did not close into financial visibility; content acclaim alone was not enough.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Global hit attention did not close into financial visibility; content acclaim alone was not enough."}
{"row_type":"case","case_id":"R8L11-C27-YG-BLACKPINK-20230512","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_MUSIC_LABEL_DISTRIBUTION_AND_CONTENT_STUDIO_MONETIZATION_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R8L11-C27-YG-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Blackpink IP drove a price run, but contract concentration and member-contract uncertainty became a non-price 4B/guard case.","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Blackpink IP drove a price run, but contract concentration and member-contract uncertainty became a non-price 4B/guard case."}
{"row_type":"trigger","trigger_id":"R8L11-C27-HYBE-T1","case_id":"R8L11-C27-HYBE-QC-20230210","symbol":"352820","company_name":"하이브","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_LABEL_MA_ACCRETIVE_OPTIONALITY","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"global label acquisition and IP portfolio expansion","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-09","entry_date":"2023-02-10","entry_price":195300,"evidence_available_at_that_date":"HYBE America / Scooter Braun-led Quality Control acquisition created a direct U.S. label/IP route but did not yet prove EPS accretion.","evidence_source":"Pitchfork / THR / NYT reports on QC acquisition; stock-web 352820 2023 shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["execution_risk_score_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv","profile_path":"atlas/symbol_profiles/352/352820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.88,"MFE_90D_pct":60.01,"MFE_180D_pct":60.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.8,"MAE_90D_pct":-12.8,"MAE_180D_pct":-12.8,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-22","peak_price":312500,"drawdown_after_peak_pct":-35.36,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"no_full_4B_at_entry","four_b_evidence_type":["execution_risk_score_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_MFE_high_MAE_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L11-C27-HYBE-EG1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L11-C27-JYP-T1","case_id":"R8L11-C27-JYP-5STAR-20230531","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"QUANTIFIED_GLOBAL_ALBUM_DEMAND_AND_US_DISTRIBUTION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"global album preorder and distribution channel conversion","loop_objective":"coverage_gap_fill|green_strictness_stress_test|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-30","entry_date":"2023-05-31","entry_price":122000,"evidence_available_at_that_date":"Stray Kids 5-Star preorder record and Republic/global distribution route provided quantified demand, but the evidence was still artist/album-cycle concentrated.","evidence_source":"5-Star preorder/Billboard record sources; stock-web 035900 2023/2024 shards","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility_watch"],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv","profile_path":"atlas/symbol_profiles/035/035900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.25,"MFE_90D_pct":20.16,"MFE_180D_pct":20.16,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.95,"MAE_90D_pct":-17.13,"MAE_180D_pct":-40.98,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2023-07-25","peak_price":146600,"drawdown_after_peak_pct":-50.89,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_cooling_confirmed","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"valid_stage2_but_requires_4B_overlay","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L11-C27-JYP-EG1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L11-C27-JYP-T2","case_id":"R8L11-C27-JYP-5STAR-20230531","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ALBUM_CYCLE_VALUATION_AND_POSITIONING_4B","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"global album cycle local peak overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-07-25","entry_date":"2023-07-25","entry_price":141100,"evidence_available_at_that_date":"Local price/valuation overheat after album-cycle momentum; treat as 4B overlay only when joined by cycle-cooling or revision-risk evidence, not as price-only full 4B.","evidence_source":"stock-web 035900 2023 shard","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv","profile_path":"atlas/symbol_profiles/035/035900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.9,"MFE_90D_pct":3.9,"MFE_180D_pct":3.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.1,"MAE_90D_pct":-27.21,"MAE_180D_pct":-48.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-25","peak_price":146600,"drawdown_after_peak_pct":-50.89,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L11-C27-JYP-4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L11-C27-SD-T1","case_id":"R8L11-C27-STUDIODRAGON-GLORY-20230103","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_STREAMING_HIT_WITHOUT_MARGIN_BRIDGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"streaming hit attention without producer economics confirmation","loop_objective":"counterexample_mining|residual_false_positive_mining|canonical_archetype_compression","trigger_type":"Stage2-Watch","trigger_date":"2023-01-02","entry_date":"2023-01-03","entry_price":85300,"evidence_available_at_that_date":"The Glory global Netflix success was visible, but direct producer economics, recurring slate economics, and margin bridge were not yet visible.","evidence_source":"Netflix/The Glory global Top 10 reporting; stock-web 253450 2023 shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.93,"MFE_90D_pct":2.93,"MFE_180D_pct":2.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.14,"MAE_90D_pct":-26.49,"MAE_180D_pct":-44.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-01-03","peak_price":87800,"drawdown_after_peak_pct":-45.79,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"false_positive_if_promoted_on_hit_only","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating_content_hit_without_economics","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L11-C27-SD-EG1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L11-C27-YG-T1","case_id":"R8L11-C27-YG-BLACKPINK-20230512","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_CONCENTRATION_IP_RUN_WITH_CONTRACT_OVERHANG","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"global artist IP momentum with renewal concentration risk","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-PriceRun","trigger_date":"2023-05-12","entry_date":"2023-05-12","entry_price":78100,"evidence_available_at_that_date":"Blackpink tour/solo/global IP momentum drove a sharp price run, but dependence on one group and renewal uncertainty were not yet resolved.","evidence_source":"Blackpink contract-renewal and individual-contract reporting; stock-web 122870 2023/2024 shards","stage2_evidence_fields":["relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["legal_or_regulatory_block","contract_delay","explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv","profile_path":"atlas/symbol_profiles/122/122870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.2,"MFE_90D_pct":24.2,"MFE_180D_pct":24.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.92,"MAE_90D_pct":-12.93,"MAE_180D_pct":-47.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2023-05-31","peak_price":97000,"drawdown_after_peak_pct":-57.94,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"non_price_contract_4B_needed_after_price_run","four_b_evidence_type":["contract_delay","explicit_event_cap","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_run_then_contract_overhang_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L11-C27-YG-EG1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L11-C27-YG-T2","case_id":"R8L11-C27-YG-BLACKPINK-20230512","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"BLACKPINK_CONTRACT_OVERHANG_4B","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"artist contract overhang as non-price 4B","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-09-21","entry_date":"2023-09-22","entry_price":66400,"evidence_available_at_that_date":"Contract uncertainty shifted from background risk to explicit non-price 4B overhang; later partial group renewal without individual-contract continuation supported guard logic.","evidence_source":"Blackpink renewal/individual contract reports; stock-web 122870 2023/2024 shards","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","legal_or_regulatory_block","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv","profile_path":"atlas/symbol_profiles/122/122870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.61,"MFE_90D_pct":3.61,"MFE_180D_pct":3.61,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.55,"MAE_90D_pct":-27.86,"MAE_180D_pct":-39.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-25","peak_price":68800,"drawdown_after_peak_pct":-41.72,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["contract_delay","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L11-C27-YG-4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L11-C27-HYBE-QC-20230210","trigger_id":"R8L11-C27-HYBE-T1","symbol":"352820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":72,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":45,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":76,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":45,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":50,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"M&A and U.S. label route bonus, but no Green because revision_score remains below 55.","MFE_90D_pct":60.01,"MAE_90D_pct":-12.8,"score_return_alignment_label":"good_MFE_but_high_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L11-C27-JYP-5STAR-20230531","trigger_id":"R8L11-C27-JYP-T1","symbol":"035900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":0,"margin_bridge_score":42,"revision_score":50,"relative_strength_score":80,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":66,"backlog_visibility_score":0,"margin_bridge_score":42,"revision_score":52,"relative_strength_score":80,"customer_quality_score":84,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow+","changed_components":["contract_score","revision_score","customer_quality_score"],"component_delta_explanation":"Quantified global demand adds C27 bonus but still waits for margin/revision confirmation before Green.","MFE_90D_pct":20.16,"MAE_90D_pct":-17.13,"score_return_alignment_label":"early_upside_then_4B_needed","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L11-C27-STUDIODRAGON-GLORY-20230103","trigger_id":"R8L11-C27-SD-T1","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":35,"relative_strength_score":40,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":25,"relative_strength_score":35,"customer_quality_score":64,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":58,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Hit-title evidence is capped when margin bridge and repeat slate monetization are absent.","MFE_90D_pct":2.93,"MAE_90D_pct":-26.49,"score_return_alignment_label":"false_positive_guarded","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L11-C27-YG-BLACKPINK-20230512","trigger_id":"R8L11-C27-YG-T1","symbol":"122870","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":38,"relative_strength_score":88,"customer_quality_score":76,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":0,"legal_or_contract_risk_score":42,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":32,"relative_strength_score":78,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":66,"legal_or_contract_risk_score":72,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-Watch / 4B-Overlay","changed_components":["revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Artist concentration and contract overhang cap promotion and activate 4B overlay.","MFE_90D_pct":24.2,"MAE_90D_pct":-12.93,"score_return_alignment_label":"price_run_counterexample","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage3_green_revision_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["content_hit_without_economics_false_positive","artist_contract_overhang_late_4B","album_cycle_local_peak_after_valid_stage2"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_round_primary = R8_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
next_round_secondary = R9_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE hard_4C follow-up
remaining_C27_gap = hard_4C case where global IP thesis actually breaks rather than only entering 4B watch
```

## 28. Source Notes

- Stock-web manifest and schema were read directly from `Songdaiki/stock-web`. fileciteturn280file0 fileciteturn281file0
- Symbol profiles were read for JYP, HYBE, Studio Dragon, and YG. fileciteturn283file0 fileciteturn284file0 fileciteturn285file0 fileciteturn286file0
- Actual OHLC rows were read from stock-web tradable shards and used for all reported MFE/MAE fields. fileciteturn287file0 fileciteturn288file0 fileciteturn289file0 fileciteturn290file0 fileciteturn291file0 fileciteturn292file0 fileciteturn293file0 fileciteturn294file0 fileciteturn295file0
- Public event/evidence sources were used only to establish what was visible at trigger time; price and calibration metrics come only from stock-web.
