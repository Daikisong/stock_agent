# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 11
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = CONTENT_IP_GLOBAL_FANDOM_MONETIZATION_VS_EVENT_PREMIUM_AND_PRODUCTION_COST
loop_objective = residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R8_loop_11_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This Markdown is a standalone v12 historical calibration research artifact. It is not live candidate research, not an investment recommendation, and not a `stock_agent` implementation patch.

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

The working question is not whether the global calibrated profile is better than E2R 2.0 baseline. That has already been absorbed. This loop asks a narrower residual question: in content/IP businesses, what separates global IP monetization that can compound through album/tour/merch/platform leverage from one-off event premium, control-premium squeeze, and cost-heavy drama production that does not convert into durable operating leverage?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R8 |
| loop | 11 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| fine_archetype_id | CONTENT_IP_GLOBAL_FANDOM_MONETIZATION_VS_EVENT_PREMIUM_AND_PRODUCTION_COST |
| sector | 플랫폼·콘텐츠·SW·보안 |
| primary_archetype | content_ip_global_monetization |

Canonical compression rule for this loop:

```text
C27 = owned/repeatable content IP monetization
      + global channel/fandom conversion
      + operating leverage or royalty/merch/tour/platform take-rate bridge
      - event-only control premium
      - production-cost inflation without library economics
      - artist-renewal binary risk not backed by diversified roster
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for coverage and duplicate avoidance. The cumulative ingest summary covers R1~R13 and loops 1~9 with 4,951 raw trigger rows, 1,940 validated rows, and 1,376 aggregate representative rows. The applied global axes already include Stage2 actionable bonus, stricter Green, non-price 4B requirement, and hard 4C routing.

This loop is new because it uses a canonical content/IP residual not previously isolated in the current post-calibrated sequence:

```text
new_independent_case_count = 5
reused_case_count = 0
required_new_independent_case_ratio = 1.00
previous_loop_overlap = none in this session for C27
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
stock_web_manifest_max_date = 2026-02-20
```

Manifest fields confirmed for this loop:

| field | value |
|---|---:|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |

Stock-Web schema confirms that tradable shards use `d,o,h,l,c,v,a,mc,s,m`, raw shards additionally include `rs`, and MFE/MAE are computed from tradable rows as:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative rows in this MD satisfy the minimum 180-trading-day forward-window eligibility check against stock-web profile max date. Corporate action candidate dates were checked at the profile level and did not overlap the representative 180D windows used for weight calibration.

| case_id | symbol | profile_path | corporate_action_window_status | forward_window_trading_days | calibration_usable |
|---|---:|---|---|---:|---|
| C27_JYP_20210517_GLOBAL_FANDOM | 035900 | atlas/symbol_profiles/035/035900.json | clean_180D_window | 180 | true |
| C27_HYBE_20210618_WEVERSE_IP | 352820 | atlas/symbol_profiles/352/352820.json | clean_180D_window | 180 | true |
| C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT | 253450 | atlas/symbol_profiles/253/253450.json | clean_180D_window | 180 | true |
| C27_YG_20230512_ARTIST_RENEWAL_RISK | 122870 | atlas/symbol_profiles/122/122870.json | clean_180D_window | 180 | true |
| C27_SM_20230210_CONTROL_PREMIUM_EVENT | 041510 | atlas/symbol_profiles/041/041510.json | clean_180D_window | 180 | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| GLOBAL_FANDOM_ALBUM_TOUR_MERCH_OPERATING_LEVERAGE | C27_CONTENT_IP_GLOBAL_MONETIZATION | repeatable fandom monetization and margin leverage |
| PLATFORM_FANDOM_SUBSCRIPTION_COMMERCE_IP_EXTENSION | C27_CONTENT_IP_GLOBAL_MONETIZATION | owned fan platform / IP commerce route |
| OTT_LIBRARY_PRODUCTION_COST_WITHOUT_MARGIN_LEVERAGE | C27_CONTENT_IP_GLOBAL_MONETIZATION | counterexample: revenue visibility without operating leverage |
| ARTIST_RENEWAL_EVENT_PREMIUM_SINGLE_ROSTER_DEPENDENCY | C27_CONTENT_IP_GLOBAL_MONETIZATION | counterexample: one IP concentration / contract cliff |
| CONTROL_PREMIUM_TENDER_EVENT_NOT_CONTENT_RERATING | C27_CONTENT_IP_GLOBAL_MONETIZATION | guard: governance/control premium must not become content-IP Green |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | best_trigger | current_profile_verdict |
|---|---:|---|---|---|---|
| C27_JYP_20210517_GLOBAL_FANDOM | 035900 | JYP Ent. | structural_success | JYP_STAGE2_20210517 | current_profile_too_late |
| C27_HYBE_20210618_WEVERSE_IP | 352820 | 하이브 | structural_success / 4B_overlay_success | HYBE_STAGE2_20210618 | current_profile_correct |
| C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT | 253450 | 스튜디오드래곤 | false_positive_green | SD_STAGE3_FALSE_20210120 | current_profile_false_positive |
| C27_YG_20230512_ARTIST_RENEWAL_RISK | 122870 | 와이지엔터테인먼트 | 4C_late / failed_rerating | YG_STAGE2_20230512 | current_profile_4C_too_late |
| C27_SM_20230210_CONTROL_PREMIUM_EVENT | 041510 | 에스엠 | price_moved_without_evidence / 4B_overlay_success | SM_EVENT_20230210 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 5
calibration_usable_trigger_count = 8
```

The loop intentionally tilts toward counterexamples because C27 often fools a generic E2R engine: a stock can have famous IP, visible news, and strong price momentum, while the actual earnings bridge is either event-capped, artist-dependent, or eaten by production cost.

## 9. Evidence Source Map

| case_id | evidence_source | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| C27_JYP_20210517_GLOBAL_FANDOM | public earnings/news/report proxy at trigger date | global fandom growth, album/tour visibility, relative strength | revision and margin bridge later confirmed | none at entry |
| C27_HYBE_20210618_WEVERSE_IP | public news/report proxy at trigger date | BTS/IP monetization, Weverse/platform optionality, customer/fandom quality | multi-source revision and platform commerce bridge | valuation blowoff later |
| C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT | public OTT/content cycle narrative | Netflix/OTT demand and production slate | insufficient margin bridge | production cost and no durable rerating |
| C27_YG_20230512_ARTIST_RENEWAL_RISK | public tour/artist activity narrative | Blackpink tour/event monetization | weak durable roster diversification | artist renewal risk and thesis cliff |
| C27_SM_20230210_CONTROL_PREMIUM_EVENT | public control/tender/governance event | control premium, governance option | not content monetization Green | event cap / price-only blowoff |

## 10. Price Data Source Map

| symbol | company_name | entry_years_opened | tradable shard path | profile path |
|---:|---|---|---|---|
| 035900 | JYP Ent. | 2021 | atlas/ohlcv_tradable_by_symbol_year/035/035900/2021.csv | atlas/symbol_profiles/035/035900.json |
| 352820 | 하이브 | 2021 | atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv | atlas/symbol_profiles/352/352820.json |
| 253450 | 스튜디오드래곤 | 2021 | atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv | atlas/symbol_profiles/253/253450.json |
| 122870 | 와이지엔터테인먼트 | 2023 | atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv | atlas/symbol_profiles/122/122870.json |
| 041510 | 에스엠 | 2023 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage intent | dedupe_for_aggregate |
|---|---|---|---|---|---:|---|---|
| JYP_STAGE2_20210517 | C27_JYP_20210517_GLOBAL_FANDOM | Stage2-Actionable | 2021-05-17 | 2021-05-17 | 37650 | early non-price IP/fandom route | true |
| JYP_STAGE3_20211020 | C27_JYP_20210517_GLOBAL_FANDOM | Stage3-Green label comparison | 2021-10-20 | 2021-10-20 | 48950 | confirmed revision but late | false |
| HYBE_STAGE2_20210618 | C27_HYBE_20210618_WEVERSE_IP | Stage2-Actionable | 2021-06-18 | 2021-06-18 | 313000 | IP/platform route | true |
| HYBE_4B_20211117 | C27_HYBE_20210618_WEVERSE_IP | 4B overlay | 2021-11-17 | 2021-11-17 | 414000 | valuation/positioning blowoff | false |
| SD_STAGE3_FALSE_20210120 | C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT | Stage3-Yellow/false Green | 2021-01-20 | 2021-01-20 | 106900 | OTT demand but weak margin bridge | true |
| YG_STAGE2_20230512 | C27_YG_20230512_ARTIST_RENEWAL_RISK | Stage2-Actionable | 2023-05-12 | 2023-05-12 | 78100 | tour/event monetization | true |
| YG_4C_20230607 | C27_YG_20230512_ARTIST_RENEWAL_RISK | 4C thesis break watch | 2023-06-07 | 2023-06-07 | 84600 | artist renewal / single-IP cliff watch | false |
| SM_EVENT_20230210 | C27_SM_20230210_CONTROL_PREMIUM_EVENT | 4B/event overlay | 2023-02-10 | 2023-02-10 | 114700 | control premium, not IP rerating | true |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE values are rounded to 1 decimal percentage points. All representative 30D/90D/180D rows are based on stock-web tradable_raw OHLC paths. 1Y/2Y fields are included as forward-window context and should be revalidated mechanically by the later parser before promotion.

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| JYP_STAGE2_20210517 | 37650 | 19.3 | -5.4 | 20.1 | -5.4 | 55.4 | -5.4 | 76.0 | 245.0 | 2021-11-17 | 58500 | -22.9 |
| JYP_STAGE3_20211020 | 48950 | 19.5 | -7.9 | 19.5 | -10.7 | 35.0 | -12.2 | 55.0 | 165.0 | 2021-11-17 | 58500 | -22.9 |
| HYBE_STAGE2_20210618 | 313000 | 7.7 | -8.5 | 8.0 | -19.8 | 34.7 | -19.8 | 34.7 | 34.7 | 2021-11-17 | 421500 | -22.1 |
| HYBE_4B_20211117 | 414000 | 1.8 | -20.5 | 1.8 | -36.9 | 1.8 | -46.7 | 1.8 | 1.8 | 2021-11-17 | 421500 | -46.7 |
| SD_STAGE3_FALSE_20210120 | 106900 | 5.7 | -11.0 | 5.7 | -13.0 | 5.7 | -14.2 | 5.7 | 5.7 | 2021-01-21 | 113000 | -18.9 |
| YG_STAGE2_20230512 | 78100 | 24.2 | -8.7 | 24.2 | -12.9 | 24.2 | -42.4 | 24.2 | 24.2 | 2023-05-31 | 97000 | -42.4 |
| YG_4C_20230607 | 84600 | 1.7 | -14.5 | 1.7 | -20.3 | 1.7 | -46.8 | 1.7 | 1.7 | 2023-06-09 | 86000 | -46.8 |
| SM_EVENT_20230210 | 114700 | 40.5 | -9.2 | 40.5 | -23.6 | 40.5 | -23.6 | 40.5 | 40.5 | 2023-03-08 | 161200 | -45.7 |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected decision | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| C27_JYP_20210517_GLOBAL_FANDOM | likely waits for stronger Green revision | Stage2 had good upside before Green confirmation | current_profile_too_late |
| C27_HYBE_20210618_WEVERSE_IP | Stage2/Yellow correct, Green later, 4B only with non-price evidence | positive but high volatility; 4B later useful | current_profile_correct |
| C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT | could over-score content demand as visibility | weak MFE, material MAE | current_profile_false_positive |
| C27_YG_20230512_ARTIST_RENEWAL_RISK | could treat tour event as IP monetization | sharp upside but reversal once renewal cliff mattered | current_profile_4C_too_late |
| C27_SM_20230210_CONTROL_PREMIUM_EVENT | could mistake event premium for content rerating if event field leaks | MFE was event-driven and capped; not durable IP evidence | current_profile_false_positive |

Calibrated-axis checks:

```text
stage2_actionable_evidence_bonus: kept; helpful for JYP/HYBE, dangerous if event-only rows are not guarded.
stage3_yellow_total_min_75: kept; but C27 requires a margin/conversion bridge, not only famous IP.
stage3_green_total_min_87: kept; stricter Green is necessary for cost-heavy or event-heavy C27 cases.
stage3_green_revision_min_55: strengthened at C27 scope; Green should require IP-to-revenue revision, not only price/press.
price_only_blowoff_blocks_positive_stage: strengthened.
full_4b_requires_non_price_evidence: strengthened; 4B needs valuation, event cap, artist risk, or revision slowdown.
hard_4c_thesis_break_routes_to_4c: strengthened for artist renewal and platform/production thesis breaks.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3/Green entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| C27_JYP_20210517_GLOBAL_FANDOM | 37650 | 48950 | 0.54 | Green was useful but surrendered much of early rerating |
| C27_HYBE_20210618_WEVERSE_IP | 313000 | 348500 | 0.33 | Green was only moderately late; volatility required risk sizing |
| C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT | 106900 | n/a | n/a | no confirmed Green; cost bridge missing |
| C27_YG_20230512_ARTIST_RENEWAL_RISK | 78100 | n/a | n/a | no durable Green; event/artist risk dominates |
| C27_SM_20230210_CONTROL_PREMIUM_EVENT | 114700 | n/a | n/a | control premium should be routed to event cap / governance, not C27 Green |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local peak proximity | full-window peak proximity | timing verdict |
|---|---|---:|---:|---|
| HYBE_4B_20211117 | valuation_blowoff / positioning_overheat / revision_risk | 0.93 | 0.93 | good_full_window_4B_timing |
| SM_EVENT_20230210 | control_premium_or_event_premium / price_only | 0.00 at entry, 1.00 by 2023-03-08 | 1.00 | event premium cap, not content 4B |
| YG_4C_20230607 | artist_contract_risk / margin_or_backlog_slowdown proxy | 0.25 | 0.25 | thesis-break watch, 4C not 4B |

Residual finding: C27 4B should not be only “high price.” For content/IP names, full-window 4B becomes meaningful when at least one of these appears: valuation blowoff vs revised earnings, artist renewal/contract cliff, roster concentration, event cap, margin slowdown, or production-cost escalation.

## 16. 4C Protection Audit

| case_id | 4C trigger | four_c_protection_label | note |
|---|---|---|---|
| C27_YG_20230512_ARTIST_RENEWAL_RISK | YG_4C_20230607 | hard_4c_late | artist renewal risk should have moved from 4B-watch to 4C-watch earlier |
| C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT | n/a | thesis_break_watch_only | no hard break, but no margin bridge; do not promote to Green |
| C27_SM_20230210_CONTROL_PREMIUM_EVENT | SM_EVENT_20230210 | false_break_for_C27 | event cap is not a content-IP thesis break; it is a routing error |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
axis = L8_content_ip_monetization_quality_gate
candidate_delta = +1 to +2 on conversion/margin bridge, -2 to -4 on event-only premium without recurring monetization
confidence = medium-low
```

Sector rule candidate:

```text
For L8 content/IP names, positive Stage2/Yellow may use public IP momentum, but Stage3-Green requires at least two of:
1. confirmed revenue revision from album/tour/merch/subscription/licensing,
2. margin bridge or operating leverage evidence,
3. diversified roster or repeatable IP release slate,
4. global distribution/fandom conversion evidence,
5. low event-cap or renewal-risk score.

If price move is driven mainly by tender/control premium, single-artist comeback, or binary renewal narrative, route to event/4B/4C overlay and do not allow C27 Green promotion.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
axis = c27_recurring_ip_monetization_bridge_required
candidate_delta = +2 when bridge exists; -3 when absent but price/press is strong
confidence = medium
```

Canonical rule candidate:

```text
C27 should distinguish “IP popularity” from “IP monetization bridge.”
Popularity alone is a theme/event field.
Monetization bridge requires conversion into revenue and operating leverage.
Production companies need margin/library economics, not simply OTT demand.
Entertainment agencies need roster diversification and renewal-risk control, not only one global artist event.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current calibrated | 5 | 19.5 | -15.1 | 0.60 | 1 | mixed; too permissive for event/control/cost-heavy content |
| P0b_e2r_2_0_baseline_reference | old baseline | 5 | 19.5 | -15.1 | 0.80 | 0 | worse; price/press likely over-promotes C27 |
| P1_L8_sector_specific_candidate | sector shadow | 5 | 25.5 | -12.6 | 0.40 | 0 | improves by filtering event-only and cost-heavy rows |
| P2_C27_archetype_candidate | archetype shadow | 5 | 25.5 | -12.6 | 0.40 | 0 | best explanation quality; keeps JYP/HYBE, blocks StudioDragon/SM |
| P3_counterexample_guard_profile | guard-only | 5 | 20.0 | -13.8 | 0.20 | 1 | safer but may miss early JYP-like structural cases |

## 20. Score-Return Alignment Matrix

| case_id | raw current score proxy | current stage proxy | proposed score proxy | proposed stage proxy | score_return_alignment_label |
|---|---:|---|---:|---|---|
| C27_JYP_20210517_GLOBAL_FANDOM | 73 | Stage2 | 78 | Stage3-Yellow | under-scored early structural IP bridge |
| C27_HYBE_20210618_WEVERSE_IP | 79 | Stage3-Yellow | 82 | Stage3-Yellow / 4B-watch later | aligned, but volatility high |
| C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT | 78 | Stage3-Yellow | 64 | Stage2/Watch | current false positive |
| C27_YG_20230512_ARTIST_RENEWAL_RISK | 75 | Stage3-Yellow | 63 | Event/4C-watch | current 4C too late |
| C27_SM_20230210_CONTROL_PREMIUM_EVENT | 80 | Stage3-Yellow if misrouted | 58 | Event/Control-premium overlay | current false positive if treated as C27 |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | CONTENT_IP_GLOBAL_FANDOM_MONETIZATION_VS_EVENT_PREMIUM_AND_PRODUCTION_COST | 2 | 3 | 2 | 1 | 5 | 0 | 8 | 5 | 4 | true | true | lower; needs more game/IP and music-label holdout cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [event_premium_misrouted_as_content_ip, production_cost_without_margin_bridge, single_artist_renewal_cliff, late_green_for_recurring_fandom_monetization]
new_axis_proposed: [c27_recurring_ip_monetization_bridge_required, c27_event_control_premium_cap, c27_artist_concentration_renewal_risk_guard, c27_production_cost_margin_bridge_required]
existing_axis_strengthened: [full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest/schema fields.
- Symbol profiles for JYP, HYBE, Studio Dragon, YG, SM.
- Entry-date close prices from stock-web tradable shards.
- 30D/90D/180D MFE/MAE directional behavior from stock-web tradable OHLC rows.
- Corporate action profile-level contamination check for representative 180D windows.
```

Not validated in this loop:

```text
- Production code behavior in stock_agent.
- Any live/current candidate status.
- Any brokerage/API behavior.
- Final production weight deltas.
- Mechanical parser re-ingestion of this MD.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_recurring_ip_monetization_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+2,"JYP/HYBE worked when global IP converted to repeat revenue and operating leverage; StudioDragon/YG/SM failed or reversed when bridge was absent","improves false-positive filtering while keeping structural positives","JYP_STAGE2_20210517|HYBE_STAGE2_20210618|SD_STAGE3_FALSE_20210120|YG_STAGE2_20230512|SM_EVENT_20230210",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c27_event_control_premium_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"SM tender/control premium and YG event risk should not promote C27 Green","routes event premium to overlay instead of positive score","SM_EVENT_20230210|YG_STAGE2_20230512",2,2,2,medium,guard_shadow_only,"not production; event/control premium guard"
shadow_weight,c27_production_cost_margin_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"OTT/content demand without margin/library economics produced weak MFE and notable MAE in Studio Dragon","reduces false Green for production-cost-heavy content companies","SD_STAGE3_FALSE_20210120",1,1,1,low,canonical_shadow_only,"needs more drama/production-company cases"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C27_JYP_20210517_GLOBAL_FANDOM","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_FANDOM_ALBUM_TOUR_MERCH_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"JYP_STAGE2_20210517","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current profile under-scored early structural monetization","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Global fandom and repeat monetization route preceded Green confirmation."}
{"row_type":"case","case_id":"C27_HYBE_20210618_WEVERSE_IP","symbol":"352820","company_name":"하이브","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"PLATFORM_FANDOM_SUBSCRIPTION_COMMERCE_IP_EXTENSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"HYBE_STAGE2_20210618","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive but high volatility; 4B overlay needed later","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"IP/platform route worked but required valuation and positioning discipline."}
{"row_type":"case","case_id":"C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"OTT_LIBRARY_PRODUCTION_COST_WITHOUT_MARGIN_LEVERAGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"SD_STAGE3_FALSE_20210120","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"content demand did not translate into durable rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Production cost and weak margin bridge should cap C27 Green."}
{"row_type":"case","case_id":"C27_YG_20230512_ARTIST_RENEWAL_RISK","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_RENEWAL_EVENT_PREMIUM_SINGLE_ROSTER_DEPENDENCY","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"YG_STAGE2_20230512","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"tour/event upside reversed when renewal concentration risk mattered","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Single artist renewal cliff should be explicit C27 risk."}
{"row_type":"case","case_id":"C27_SM_20230210_CONTROL_PREMIUM_EVENT","symbol":"041510","company_name":"에스엠","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTROL_PREMIUM_TENDER_EVENT_NOT_CONTENT_RERATING","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"SM_EVENT_20230210","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event premium produced MFE but should not train C27 positive weights","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Governance/control premium belongs to event overlay, not content-IP Green."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"JYP_STAGE2_20210517","case_id":"C27_JYP_20210517_GLOBAL_FANDOM","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_FANDOM_ALBUM_TOUR_MERCH_OPERATING_LEVERAGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"content_ip_global_monetization","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2021-05-17","evidence_available_at_that_date":"global fandom and album/tour monetization route visible before full revision confirmation","evidence_source":"public earnings/news/report proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2021.csv","profile_path":"atlas/symbol_profiles/035/035900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-17","entry_price":37650,"MFE_30D_pct":19.3,"MFE_90D_pct":20.1,"MFE_180D_pct":55.4,"MFE_1Y_pct":76.0,"MFE_2Y_pct":245.0,"MAE_30D_pct":-5.4,"MAE_90D_pct":-5.4,"MAE_180D_pct":-5.4,"MAE_1Y_pct":-7.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":58500,"drawdown_after_peak_pct":-22.9,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_JYP_20210517_37650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"JYP_STAGE3_20211020","case_id":"C27_JYP_20210517_GLOBAL_FANDOM","symbol":"035900","company_name":"JYP Ent.","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_FANDOM_ALBUM_TOUR_MERCH_OPERATING_LEVERAGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"content_ip_global_monetization","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2021-10-20","evidence_available_at_that_date":"confirmed revision/relative strength arrived after Stage2 move","evidence_source":"public earnings/news/report proxy","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2021.csv","profile_path":"atlas/symbol_profiles/035/035900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-10-20","entry_price":48950,"MFE_30D_pct":19.5,"MFE_90D_pct":19.5,"MFE_180D_pct":35.0,"MFE_1Y_pct":55.0,"MFE_2Y_pct":165.0,"MAE_30D_pct":-7.9,"MAE_90D_pct":-10.7,"MAE_180D_pct":-12.2,"MAE_1Y_pct":-12.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":58500,"drawdown_after_peak_pct":-22.9,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"label_comparison_late_green","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_JYP_20211020_48950","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same case Stage3 label comparison","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"HYBE_STAGE2_20210618","case_id":"C27_HYBE_20210618_WEVERSE_IP","symbol":"352820","company_name":"하이브","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"PLATFORM_FANDOM_SUBSCRIPTION_COMMERCE_IP_EXTENSION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"content_ip_global_monetization","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2021-06-18","evidence_available_at_that_date":"global IP and owned fan-platform monetization route visible","evidence_source":"public earnings/news/report proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv","profile_path":"atlas/symbol_profiles/352/352820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-06-18","entry_price":313000,"MFE_30D_pct":7.7,"MFE_90D_pct":8.0,"MFE_180D_pct":34.7,"MFE_1Y_pct":34.7,"MFE_2Y_pct":34.7,"MAE_30D_pct":-8.5,"MAE_90D_pct":-19.8,"MAE_180D_pct":-19.8,"MAE_1Y_pct":-46.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":421500,"drawdown_after_peak_pct":-46.7,"green_lateness_ratio":0.33,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_HYBE_20210618_313000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HYBE_4B_20211117","case_id":"C27_HYBE_20210618_WEVERSE_IP","symbol":"352820","company_name":"하이브","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"PLATFORM_FANDOM_SUBSCRIPTION_COMMERCE_IP_EXTENSION","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"content_ip_global_monetization","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B","trigger_date":"2021-11-17","evidence_available_at_that_date":"valuation and positioning blowoff after IP/platform rerating","evidence_source":"public market/report proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv","profile_path":"atlas/symbol_profiles/352/352820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-17","entry_price":414000,"MFE_30D_pct":1.8,"MFE_90D_pct":1.8,"MFE_180D_pct":1.8,"MFE_1Y_pct":1.8,"MFE_2Y_pct":1.8,"MAE_30D_pct":-20.5,"MAE_90D_pct":-36.9,"MAE_180D_pct":-46.7,"MAE_1Y_pct":-46.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":421500,"drawdown_after_peak_pct":-46.7,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_HYBE_20211117_414000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case 4B overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"SD_STAGE3_FALSE_20210120","case_id":"C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"OTT_LIBRARY_PRODUCTION_COST_WITHOUT_MARGIN_LEVERAGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"content_ip_global_monetization","loop_objective":"residual_false_positive_mining","trigger_type":"Stage3-Yellow","trigger_date":"2021-01-20","evidence_available_at_that_date":"OTT/content demand and slate visibility but no clean margin bridge","evidence_source":"public content/report proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-20","entry_price":106900,"MFE_30D_pct":5.7,"MFE_90D_pct":5.7,"MFE_180D_pct":5.7,"MFE_1Y_pct":5.7,"MFE_2Y_pct":5.7,"MAE_30D_pct":-11.0,"MAE_90D_pct":-13.0,"MAE_180D_pct":-14.2,"MAE_1Y_pct":-18.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-21","peak_price":113000,"drawdown_after_peak_pct":-18.9,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_SD_20210120_106900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"YG_STAGE2_20230512","case_id":"C27_YG_20230512_ARTIST_RENEWAL_RISK","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_RENEWAL_EVENT_PREMIUM_SINGLE_ROSTER_DEPENDENCY","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"content_ip_global_monetization","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-12","evidence_available_at_that_date":"tour/event monetization visible, but renewal and concentration risk not resolved","evidence_source":"public news/report proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv","profile_path":"atlas/symbol_profiles/122/122870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-12","entry_price":78100,"MFE_30D_pct":24.2,"MFE_90D_pct":24.2,"MFE_180D_pct":24.2,"MFE_1Y_pct":24.2,"MFE_2Y_pct":24.2,"MAE_30D_pct":-8.7,"MAE_90D_pct":-12.9,"MAE_180D_pct":-42.4,"MAE_1Y_pct":-42.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-31","peak_price":97000,"drawdown_after_peak_pct":-42.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.63,"four_b_full_window_peak_proximity":0.63,"four_b_timing_verdict":"event_premium_not_full_4B_without_contract_risk","four_b_evidence_type":["positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_YG_20230512_78100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"YG_4C_20230607","case_id":"C27_YG_20230512_ARTIST_RENEWAL_RISK","symbol":"122870","company_name":"와이지엔터테인먼트","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_RENEWAL_EVENT_PREMIUM_SINGLE_ROSTER_DEPENDENCY","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"content_ip_global_monetization","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C","trigger_date":"2023-06-07","evidence_available_at_that_date":"renewal and single-IP concentration risk begins to dominate event monetization","evidence_source":"public news/report proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv","profile_path":"atlas/symbol_profiles/122/122870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-07","entry_price":84600,"MFE_30D_pct":1.7,"MFE_90D_pct":1.7,"MFE_180D_pct":1.7,"MFE_1Y_pct":1.7,"MFE_2Y_pct":1.7,"MAE_30D_pct":-14.5,"MAE_90D_pct":-20.3,"MAE_180D_pct":-46.8,"MAE_1Y_pct":-46.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-09","peak_price":86000,"drawdown_after_peak_pct":-46.8,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.25,"four_b_full_window_peak_proximity":0.25,"four_b_timing_verdict":"4C_watch_more_important_than_4B","four_b_evidence_type":["explicit_event_cap"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_YG_20230607_84600","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same case 4C overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"SM_EVENT_20230210","case_id":"C27_SM_20230210_CONTROL_PREMIUM_EVENT","symbol":"041510","company_name":"에스엠","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTROL_PREMIUM_TENDER_EVENT_NOT_CONTENT_RERATING","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"content_ip_global_monetization","loop_objective":"residual_false_positive_mining","trigger_type":"Event/4B-overlay","trigger_date":"2023-02-10","evidence_available_at_that_date":"control premium/tender/gov event; content IP quality not independently confirmed","evidence_source":"public market/governance event proxy","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["control_premium_or_event_premium","valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-10","entry_price":114700,"MFE_30D_pct":40.5,"MFE_90D_pct":40.5,"MFE_180D_pct":40.5,"MFE_1Y_pct":40.5,"MFE_2Y_pct":40.5,"MAE_30D_pct":-9.2,"MAE_90D_pct":-23.6,"MAE_180D_pct":-23.6,"MAE_1Y_pct":-45.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.7,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"event_premium_cap_not_content_ip_green","four_b_evidence_type":["control_premium_or_event_premium","valuation_blowoff"],"four_c_protection_label":"false_break_for_C27","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_SM_20230210_114700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_JYP_20210517_GLOBAL_FANDOM","trigger_id":"JYP_STAGE2_20210517","symbol":"035900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":30,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":75,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":70,"content_ip_monetization_score":75},"weighted_score_before":73,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":65,"revision_score":58,"relative_strength_score":75,"customer_quality_score":85,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":18,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":78,"content_ip_monetization_score":85},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","content_ip_monetization_score"],"component_delta_explanation":"Recurring fandom monetization bridge deserves C27-specific early credit.","MFE_90D_pct":20.1,"MAE_90D_pct":-5.4,"score_return_alignment_label":"under_scored_structural","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_HYBE_20210618_WEVERSE_IP","trigger_id":"HYBE_STAGE2_20210618","symbol":"352820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":25,"margin_bridge_score":55,"revision_score":62,"relative_strength_score":70,"customer_quality_score":90,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_fandom_score":80,"content_ip_monetization_score":82},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":30,"margin_bridge_score":60,"revision_score":65,"relative_strength_score":70,"customer_quality_score":90,"policy_or_regulatory_score":0,"valuation_repricing_score":42,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"platform_fandom_score":88,"content_ip_monetization_score":88},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow / 4B-watch later","changed_components":["platform_fandom_score","content_ip_monetization_score","valuation_repricing_score"],"component_delta_explanation":"Platform/fandom route is real, but valuation risk suppresses Green acceleration.","MFE_90D_pct":8.0,"MAE_90D_pct":-19.8,"score_return_alignment_label":"aligned_high_volatility","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_STUDIO_DRAGON_20210120_COST_HEAVY_OTT","trigger_id":"SD_STAGE3_FALSE_20210120","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":50,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":65,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":45,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"production_cost_risk_score":65,"content_ip_monetization_score":60},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":35,"relative_strength_score":55,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":40,"execution_risk_score":55,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"production_cost_risk_score":80,"content_ip_monetization_score":40},"weighted_score_after":64,"stage_label_after":"Stage2/Watch","changed_components":["margin_bridge_score","production_cost_risk_score","content_ip_monetization_score"],"component_delta_explanation":"OTT demand without margin/library economics should not become C27 Green.","MFE_90D_pct":5.7,"MAE_90D_pct":-13.0,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_YG_20230512_ARTIST_RENEWAL_RISK","trigger_id":"YG_STAGE2_20230512","symbol":"122870","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":20,"margin_bridge_score":45,"revision_score":55,"relative_strength_score":85,"customer_quality_score":75,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"artist_concentration_risk_score":85,"content_ip_monetization_score":55},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":15,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":70,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":75,"legal_or_contract_risk_score":85,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"artist_concentration_risk_score":95,"content_ip_monetization_score":35},"weighted_score_after":63,"stage_label_after":"Event/4C-watch","changed_components":["legal_or_contract_risk_score","artist_concentration_risk_score","content_ip_monetization_score"],"component_delta_explanation":"Single-artist renewal cliff caps Stage3 despite event/tour upside.","MFE_90D_pct":24.2,"MAE_90D_pct":-12.9,"score_return_alignment_label":"event_upside_but_failed_rerating","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C27_SM_20230210_CONTROL_PREMIUM_EVENT","trigger_id":"SM_EVENT_20230210","symbol":"041510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":15,"margin_bridge_score":40,"revision_score":45,"relative_strength_score":95,"customer_quality_score":75,"policy_or_regulatory_score":45,"valuation_repricing_score":55,"execution_risk_score":60,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_or_event_premium_score":95,"content_ip_monetization_score":45},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow if misrouted","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":25,"revision_score":35,"relative_strength_score":70,"customer_quality_score":70,"policy_or_regulatory_score":45,"valuation_repricing_score":40,"execution_risk_score":75,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"control_premium_or_event_premium_score":100,"content_ip_monetization_score":20},"weighted_score_after":58,"stage_label_after":"Event/Control-premium overlay","changed_components":["control_premium_or_event_premium_score","content_ip_monetization_score","margin_bridge_score"],"component_delta_explanation":"Control premium can produce MFE but must not train C27 content-IP entry weights.","MFE_90D_pct":40.5,"MAE_90D_pct":-23.6,"score_return_alignment_label":"event_premium_not_content_ip","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"11","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["event_premium_misrouted_as_content_ip","production_cost_without_margin_bridge","single_artist_renewal_cliff","late_green_for_recurring_fandom_monetization"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"NONE","symbol":null,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","reason":"all selected cases have calibration_usable representative triggers","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
- Do not apply global deltas unless multiple `large_sector_id` values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
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
next_round = R8_loop_12_or_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
preferred_next_scope = L8_PLATFORM_CONTENT_SW_SECURITY / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
carry_forward_guardrails = [event premium cannot train content-IP positive weights, IP popularity must become monetization bridge, production-cost-heavy content needs margin/library economics]
```

## 28. Source Notes

Stock-web files consulted in this loop:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/035/035900.json
atlas/symbol_profiles/352/352820.json
atlas/symbol_profiles/253/253450.json
atlas/symbol_profiles/122/122870.json
atlas/symbol_profiles/041/041510.json
atlas/ohlcv_tradable_by_symbol_year/035/035900/2021.csv
atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv
atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv
atlas/ohlcv_tradable_by_symbol_year/122/122870/2023.csv
atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv
```

Allowed stock_agent research artifacts consulted only for duplicate avoidance / existing applied-axis awareness:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/applied_scoring_diff.md
```
