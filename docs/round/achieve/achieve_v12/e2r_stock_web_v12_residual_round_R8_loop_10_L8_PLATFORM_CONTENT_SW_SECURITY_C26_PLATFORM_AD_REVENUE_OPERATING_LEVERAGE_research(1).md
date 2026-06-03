# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 10
sector = 플랫폼·콘텐츠·SW·보안
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG
output_file = e2r_stock_web_v12_residual_round_R8_loop_10_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not current/live candidate discovery, not a stock recommendation, not a `stock_agent` code patch, and not a production scoring promotion.

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

This loop does not re-prove the global Stage2/Green/4B/4C axes. It stress-tests them inside C26, where platform traffic migration, ad recovery, cost control, and governance risk can look similar at Stage2 but diverge sharply by 180D.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R8 |
| loop | 10 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| fine_archetype_id | LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG |
| loop_objective | counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; coverage_gap_fill |

Canonical compression: SOOP/AfreecaTV, NAVER, and Kakao are not the same business model, but all three pass through the C26 question: does a traffic/revenue recovery narrative actually become operating leverage, or is it merely beta, AI narrative, or governance relief?

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts show R8 was covered in loops 1~8, while the global calibration ingest snapshot covers R1~R13 and loops 1~9. R8 therefore should not reuse generic platform/software conclusions; this loop adds a specific C26 residual split: live-streaming migration success versus portal/platform recovery with weak durable confirmation and governance overhang. The registry shows R8 historical MDs across platform/content/software/security loops, so this loop is treated as same large sector but new fine split and new trigger family, not a schema rematerialization. fileciteturn43file0

The global applied axes are already promoted from the first Stock-Web calibration; this loop treats them as existing axes to stress-test, not as new global deltas. fileciteturn30file0

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

The manifest explicitly marks the atlas as raw/unadjusted OHLC and notes that zero-volume and zero-OHLC rows are excluded from calibration shards, while corporate-action-contaminated windows are blocked by default. fileciteturn31file0

The schema defines tradable shard columns as `d,o,h,l,c,v,a,mc,s,m`, calibration basis as `tradable_raw`, price adjustment status as `raw_unadjusted_marcap`, and MFE/MAE formulas based on max high/min low from the entry date through N tradable rows. fileciteturn32file0

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward window | OHLC rows | corporate-action window | calibration_usable |
|---|---:|---|---|---|---|---|
| R8L10_C26_SOOP_20231207 | 067160 | 2023-12-07 | available | present | clean_180D_window; historical CA dates only 2005/2007/2008/2011 | true |
| R8L10_C26_NAVER_20231103 | 035420 | 2023-11-03 | available | present | clean_180D_window; latest CA date 2018-10-12 | true |
| R8L10_C26_KAKAO_20231109 | 035720 | 2023-11-09 | available | present | clean_180D_window; latest CA date 2021-04-15 | true |

SOOP profile confirms current/latest name SOOP, 2023~2026 available years, latest market KOSDAQ GLOBAL, and corporate-action candidates only in older historical periods, outside this loop's 2023-12~2024-09 calibration window. fileciteturn44file0 NAVER and Kakao profiles likewise provide available years through 2026 and corporate-action candidate dates outside the tested 2023-11~2024-07 windows. fileciteturn45file0turn46file0

## 6. Canonical Archetype Compression Map

| symbol | company_name | fine route | canonical_archetype_id | role |
|---:|---|---|---|---|
| 067160 | SOOP / former AfreecaTV | Twitch Korea exit -> streamer/user migration -> platform monetization optionality | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | structural_success + 4B overlay |
| 035420 | NAVER | search/commerce/ad cost discipline + CHZZK optionality | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | moderate_positive / Stage2-to-Yellow only |
| 035720 | Kakao | Talk Biz/platform recovery narrative with governance/regulatory overhang | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | counterexample / false positive if promoted to Green |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | novelty |
|---|---:|---|---|---|---|---|
| R8L10_C26_SOOP_20231207 | 067160 | SOOP | structural_success | positive | SOOP_STAGE2_TWITCH_EXIT_MIGRATION_20231207 | new symbol in this loop; new event-driven traffic migration trigger |
| R8L10_C26_NAVER_20231103 | 035420 | NAVER | stage2_promote_candidate | positive | NAVER_STAGE2_Q3_COST_AD_RECOVERY_20231103 | new symbol; platform operating leverage but modest 180D outcome |
| R8L10_C26_KAKAO_20231109 | 035720 | Kakao | failed_rerating / false_positive_green | counterexample | KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109 | new symbol; governance/regulatory overhang counterexample |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 3 |
| representative_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

The positive sample is intentionally split into one strong structural migration case and one moderate platform operating-leverage case. The counterexample is Kakao, where the early rally looked like C26 recovery but 180D path exposed governance/regulatory and durable-revision weakness.

## 9. Evidence Source Map

| case_id | trigger_date | evidence summary | evidence_source | timing rule |
|---|---|---|---|---|
| R8L10_C26_SOOP_20231207 | 2023-12-06 | Twitch announced it would exit South Korea effective 2024-02-27, creating a migration event for domestic live-streaming platforms. | public report / Twitch Korea exit reference; search source notes | announcement-date event, entry next tradable day close |
| R8L10_C26_NAVER_20231103 | 2023-11-03 | Q3 2023 platform earnings/cost-discipline setup plus later CHZZK optionality after Twitch exit. | earnings/news source map; CHZZK/Twitch reference | same-day close because market reacted during session |
| R8L10_C26_KAKAO_20231109 | 2023-11-09 | Q3 recovery narrative in Talk Biz/platform segments, later constrained by governance/regulatory and legal overhang. | earnings/news source map; Reuters governance overhang reference | same-day close because market reacted during session |

Twitch's South Korea exit date and effective date are supported by the web evidence source: it announced the exit on 2023-12-06, effective 2024-02-27. citeturn614316search0turn405844search5 CHZZK was started after the Twitch exit and became part of the same traffic-migration context. citeturn614316search2 Kakao's governance/legal overhang is supported by the 2024 Reuters report on the founder indictment and stock-manipulation charges. citeturn405844news0

## 10. Price Data Source Map

| symbol | profile_path | representative shard paths | profile status |
|---:|---|---|---|
| 067160 | atlas/symbol_profiles/067/067160.json | atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv; atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv | active_like; no CA overlap |
| 035420 | atlas/symbol_profiles/035/035420.json | atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv; atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv | active_like; no CA overlap |
| 035720 | atlas/symbol_profiles/035/035720.json | atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv; atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv | active_like; no CA overlap |

SOOP entry and immediate event response are visible in the 2023 shard: 2023-12-06 high/close 83,400 and 2023-12-07 close 76,600. fileciteturn47file0 SOOP's 2024 continuation path shows highs through 143,800 on 2024-07-11 and later drawdown into September/October. fileciteturn48file0turn50file0turn49file0 NAVER's 2023 entry row and 2024 path are visible in the corresponding shards. fileciteturn51file0turn52file0 Kakao's entry row and 2024 decay path are likewise visible in stock-web shards. fileciteturn53file0turn54file0

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence | current_profile_verdict |
|---|---|---:|---|---|---|---:|---|---|---|---|
| SOOP_STAGE2_TWITCH_EXIT_MIGRATION_20231207 | R8L10_C26_SOOP_20231207 | 067160 | Stage2-Actionable | 2023-12-06 | 2023-12-07 | 76,600 | public_event_or_disclosure; customer_or_order_quality; relative_strength; capacity_or_volume_route | not yet confirmed | none | current_profile_correct |
| SOOP_STAGE3_MONETIZATION_CONFIRMATION_20240214 | R8L10_C26_SOOP_20231207 | 067160 | Stage3-Yellow | 2024-02-14 | 2024-02-14 | 118,000 | traffic migration | relative_strength; multiple_public_sources; low_red_team_risk | none | current_profile_correct |
| SOOP_4B_LOCAL_REPRICE_20240228 | R8L10_C26_SOOP_20231207 | 067160 | Stage4B-local | 2024-02-28 | 2024-02-28 | 129,900 | none | none | valuation_blowoff; positioning_overheat | current_profile_4B_too_early_if_price_only |
| NAVER_STAGE2_Q3_COST_AD_RECOVERY_20231103 | R8L10_C26_NAVER_20231103 | 035420 | Stage2-Actionable | 2023-11-03 | 2023-11-03 | 200,500 | public_event_or_disclosure; early_revision_signal; policy_or_regulatory_optionality | partial financial visibility | none | current_profile_correct |
| KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109 | R8L10_C26_KAKAO_20231109 | 035720 | Stage2-Actionable / false Green stress | 2023-11-09 | 2023-11-09 | 45,600 | public_event_or_disclosure; early_revision_signal; relative_strength | weak durable confirmation | legal_or_regulatory_block; accounting_or_trust_break | current_profile_false_positive |
| KAKAO_4B_VALUATION_GOVERNANCE_CAP_20240111 | R8L10_C26_KAKAO_20231109 | 035720 | Stage4B-overlay | 2024-01-11 | 2024-01-11 | 60,800 | none | none | valuation_blowoff; legal_or_regulatory_block; positioning_overheat | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative positive/counterexample triggers

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| SOOP_STAGE2_TWITCH_EXIT_MIGRATION_20231207 | 76,600 | 45.43 | -6.01 | 82.25 | -6.01 | 87.73 | -6.01 | 2024-07-11 | 143,800 | -39.85 | structural_success |
| NAVER_STAGE2_Q3_COST_AD_RECOVERY_20231103 | 200,500 | 12.22 | -3.99 | 17.46 | -7.23 | 17.46 | -20.40 | 2024-01-16 | 235,500 | -32.23 | moderate_positive_then_fade |
| KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109 | 45,600 | 20.61 | -4.71 | 35.75 | -4.71 | 35.75 | -16.45 | 2024-01-11 | 61,900 | -38.45 | false_positive_green_if_uncapped |

### 12.2 Overlay triggers

| trigger_id | entry_price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| SOOP_4B_LOCAL_REPRICE_20240228 | 129,900 | 139,600 | 143,800 | 0.85 | 0.79 | good_overlay_but_not_price_only_full_4B |
| KAKAO_4B_VALUATION_GOVERNANCE_CAP_20240111 | 60,800 | 61,900 | 61,900 | 0.93 | 0.93 | good_full_window_4B_timing_if_governance_non_price_evidence_used |

## 13. Current Calibrated Profile Stress Test

| case_id | current proxy likely label | actual path | stress verdict | why |
|---|---|---|---|---|
| R8L10_C26_SOOP_20231207 | Stage2-Actionable, later Yellow | high MFE with contained MAE; 180D MFE 87.73% | current_profile_correct | non-price migration event was real; price-only guard does not block positive entry because evidence is not price-only |
| R8L10_C26_NAVER_20231103 | Stage2/Yellow, no Green unless revision confirms | 90D MFE 17.46%, 180D MAE -20.40% | current_profile_correct | current stricter Green threshold/revision gate should prevent broad Green promotion |
| R8L10_C26_KAKAO_20231109 | risk of Yellow/Green if platform recovery overweights beta | 30D/90D positive but 180D MAE -16.45% and later governance overhang | current_profile_false_positive | platform recovery score needs governance/regulatory cap and realized margin confirmation |

Axis status:

| existing axis | tested/kept/changed | conclusion |
|---|---|---|
| stage2_actionable_evidence_bonus | existing_axis_kept | SOOP supports Stage2 when non-price platform migration is identifiable |
| stage3_yellow_total_min | existing_axis_kept | NAVER/Kakao can deserve Yellow stress-test, but not Green |
| stage3_green_total_min | existing_axis_strengthened_in_C26_only | C26 Green should require realized monetization/margin, not just traffic/AI/growth narrative |
| stage3_green_revision_min | existing_axis_strengthened_in_C26_only | C26 needs segment-level revenue/OP leverage evidence |
| price_only_blowoff_blocks_positive_stage | existing_axis_kept | SOOP/Kakao overlay rows should not train positive entry weights |
| full_4b_requires_non_price_evidence | existing_axis_kept | Kakao 4B works only when governance/legal evidence is included |
| hard_4c_thesis_break_routes_to_4c | existing_axis_kept | no hard 4C row in this loop |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Yellow/Green proxy | green_lateness_ratio | interpretation |
|---|---:|---|---:|---|
| SOOP | 76,600 | Yellow at 118,000 on 2024-02-14 | 0.62 | Yellow/Green confirmation would have missed most of the first upside; Stage2 event evidence was valuable |
| NAVER | 200,500 | no confirmed Green | not_applicable | Green should not be forced because 180D path did not validate a durable rerating |
| Kakao | 45,600 | false Green risk near 60,800/61,900 | 0.93 | if treated as Green near the peak, most upside had already been consumed |

SOOP's lateness ratio uses `(118,000 - 76,600) / (143,800 - 76,600) = 0.62`. Kakao's false-Green ratio uses `(60,800 - 45,600) / (61,900 - 45,600) = 0.93`.

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---|---:|---:|---|---|
| SOOP | SOOP_4B_LOCAL_REPRICE_20240228 | 0.85 | 0.79 | valuation_blowoff; positioning_overheat | keep as overlay, not full exit unless non-price slowdown appears |
| Kakao | KAKAO_4B_VALUATION_GOVERNANCE_CAP_20240111 | 0.93 | 0.93 | valuation_blowoff; legal_or_regulatory_block; accounting_or_trust_break | good full-window 4B timing when governance evidence is included |

C26-specific lesson: a local 4B can be early in a true migration winner, but late enough in a governance-capped platform where the beta rebound already used the available upside.

## 16. 4C Protection Audit

No hard 4C row is promoted in this loop. Kakao receives `thesis_break_watch_only`, not hard 4C, because the route is a governance/regulatory cap plus weaker durability rather than a single confirmed business-model break at the initial trigger date.

| case_id | four_c_protection_label | note |
|---|---|---|
| SOOP | not_applicable | no thesis break inside 180D window |
| NAVER | thesis_break_watch_only | post-peak drawdown reflected weak operating leverage follow-through, not hard 4C |
| Kakao | thesis_break_watch_only | legal/regulatory overhang should cap Green and accelerate 4B overlay, but not necessarily 4C at initial trigger |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
axis = platform_operating_leverage_green_requires_realized_monetization
baseline_value = absent
shadow_tested_value = +1 C26/L8 gate
```

Proposed L8 rule candidate:

> In platform/content/SW names, traffic migration, AI/product launch, or advertising recovery can support Stage2-Actionable, but Stage3-Green should require realized monetization or segment-level operating leverage evidence. If the case is still traffic-only, beta-only, or narrative-only, cap at Yellow.

Backtest effect in this loop: preserves SOOP Stage2, prevents Kakao false Green, and keeps NAVER as Stage2/Yellow rather than forcing Green.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
axis_1 = c26_realized_monetization_confirmation_required_for_green
axis_2 = c26_governance_regulatory_overhang_caps_green
```

C26-specific compression:

1. **Traffic migration event**: good Stage2 evidence when the user/customer route is externally verifiable, as in SOOP after Twitch Korea exit.
2. **Operating leverage confirmation**: needed for Green; otherwise NAVER-like cases remain moderate/Yellow.
3. **Governance/regulatory cap**: if legal/regulatory/governance risk is active, Kakao-like cases should cap at Yellow/4B overlay even if early MFE is strong.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | selected entries | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 3 | 45.15 | -5.98 | 46.98 | -14.29 | 0.33 | 0 | good but C26 false-Green risk remains |
| P0b e2r_2_0_baseline_reference | rollback reference | 3 | 45.15 | -5.98 | 46.98 | -14.29 | 0.67 | 0 | weaker because Green cap/revision guard less strict |
| P1 L8_sector_candidate_profile | sector shadow | 3 | 45.15 | -5.98 | 46.98 | -14.29 | 0.00 | 0 | best balance: Stage2 allowed, Green capped without monetization |
| P2 C26_archetype_candidate_profile | archetype shadow | 3 | 45.15 | -5.98 | 46.98 | -14.29 | 0.00 | 0 | same as P1 but more precise |
| P3 counterexample_guard_profile | guard-only | 3 | 45.15 | -5.98 | 46.98 | -14.29 | 0.00 | 0 | preserves Kakao cap; less informative for SOOP upside |

## 20. Score-Return Alignment Matrix

| case_id | raw proxy score before | stage before | raw proxy score after | stage after | price alignment |
|---|---:|---|---:|---|---|
| SOOP | 78 | Stage2-Actionable / Yellow | 82 | Stage2-Actionable / Yellow, Green after monetization confirmation | aligned_positive |
| NAVER | 74 | Stage2 / Yellow | 72 | Stage2 / Yellow, no Green | aligned_moderate |
| Kakao | 77 | possible Yellow/false Green | 65 | Yellow cap / 4B watch | aligned_counterexample |

Component logic: SOOP gets high relative-strength and platform-migration/customer-route scores; NAVER gets cost/operating leverage but lower realized monetization; Kakao gets early recovery score but receives a governance/regulatory cap.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG | 2 | 1 | 2 | 0 | 3 | 0 | 6 | 3 | 1 | true | true | remaining gap: add pure ad-tech/SaaS contract-retention examples and a hard 4C platform case |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [c26_false_green_from_platform_recovery_without_governance_cap, c26_traffic_migration_stage2_success]
new_axis_proposed: [platform_operating_leverage_green_requires_realized_monetization, c26_governance_regulatory_overhang_caps_green]
existing_axis_strengthened: [stage3_green_revision_min in C26 only]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R8/C26 undercovered platform operating leverage with governance overhang counterexample
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest/schema and raw/unadjusted/tradable basis.
- Symbol profiles for 067160, 035420, 035720.
- Entry rows and forward OHLC windows from stock-web tradable shards.
- 30D/90D/180D MFE/MAE based on max high/min low.
- Positive/counterexample balance and same-entry dedupe flags.

Not validated:

- Production `stock_agent` code behavior.
- Live 2026 candidate status.
- Brokerage execution.
- Full 1Y/2Y calibration for promotion. 1Y/2Y fields are left as `null` in machine rows where not needed for the 180D historical gate.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,platform_operating_leverage_green_requires_realized_monetization,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"C26 traffic or ad recovery can support Stage2 but Green needs realized monetization/segment operating leverage","Preserves SOOP Stage2; keeps NAVER moderate; prevents Kakao false Green","SOOP_STAGE2_TWITCH_EXIT_MIGRATION_20231207|NAVER_STAGE2_Q3_COST_AD_RECOVERY_20231103|KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109",3,3,1,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_governance_regulatory_overhang_caps_green,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Governance/legal overhang makes platform recovery beta unstable and should cap Green","Kakao early MFE looked strong but 180D path failed after 4B-like peak","KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109|KAKAO_4B_VALUATION_GOVERNANCE_CAP_20240111",2,1,1,medium,archetype_shadow_only,"not production; cap Green rather than reverse Stage2"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L10_C26_SOOP_20231207","symbol":"067160","company_name":"SOOP","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"SOOP_STAGE2_TWITCH_EXIT_MIGRATION_20231207","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Twitch Korea exit created externally verifiable traffic migration route; high 180D MFE with low MAE."}
{"row_type":"case","case_id":"R8L10_C26_NAVER_20231103","symbol":"035420","company_name":"NAVER","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"NAVER_STAGE2_Q3_COST_AD_RECOVERY_20231103","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_moderate","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Moderate platform operating-leverage path; should stay Stage2/Yellow without forcing Green."}
{"row_type":"case","case_id":"R8L10_C26_KAKAO_20231109","symbol":"035720","company_name":"Kakao","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample_after_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Early recovery rally failed by 180D; governance/regulatory cap should prevent Green."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SOOP_STAGE2_TWITCH_EXIT_MIGRATION_20231207","case_id":"R8L10_C26_SOOP_20231207","symbol":"067160","company_name":"SOOP","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"live_streaming_platform_migration","loop_objective":"counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-06","entry_date":"2023-12-07","entry_price":76600,"evidence_available_at_that_date":"Twitch Korea exit announced; streamer/user migration optionality visible","evidence_source":"public event / Twitch Korea exit source map","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv|atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.43,"MFE_90D_pct":82.25,"MFE_180D_pct":87.73,"MFE_1Y_pct":87.73,"MFE_2Y_pct":null,"MAE_30D_pct":-6.01,"MAE_90D_pct":-6.01,"MAE_180D_pct":-6.01,"MAE_1Y_pct":-6.01,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-39.85,"green_lateness_ratio":0.62,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"067160_2023-12-07_76600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SOOP_STAGE3_MONETIZATION_CONFIRMATION_20240214","case_id":"R8L10_C26_SOOP_20231207","symbol":"067160","company_name":"SOOP","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"live_streaming_platform_migration","loop_objective":"yellow_threshold_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":118000,"evidence_available_at_that_date":"price/revision/traffic confirmation phase after migration event","evidence_source":"stock-web OHLC plus public migration narrative source map","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.31,"MFE_90D_pct":18.31,"MFE_180D_pct":21.86,"MFE_1Y_pct":21.86,"MFE_2Y_pct":null,"MAE_30D_pct":-7.71,"MAE_90D_pct":-11.44,"MAE_180D_pct":-26.69,"MAE_1Y_pct":-26.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-39.85,"green_lateness_ratio":0.62,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_confirmation_but_still_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"067160_2024-02-14_118000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_label_comparison","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"SOOP_4B_LOCAL_REPRICE_20240228","case_id":"R8L10_C26_SOOP_20231207","symbol":"067160","company_name":"SOOP","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"live_streaming_platform_migration","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-local","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":129900,"evidence_available_at_that_date":"local valuation/positioning reprice after sharp migration rally","evidence_source":"stock-web OHLC; public migration narrative source map","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MFE_90D_pct":10.70,"MFE_180D_pct":10.70,"MFE_1Y_pct":10.70,"MFE_2Y_pct":null,"MAE_30D_pct":-9.85,"MAE_90D_pct":-18.40,"MAE_180D_pct":-33.41,"MAE_1Y_pct":-33.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-39.85,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.79,"four_b_timing_verdict":"good_overlay_but_not_price_only_full_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early_if_price_only","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"067160_2024-02-28_129900","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4B_overlay","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"NAVER_STAGE2_Q3_COST_AD_RECOVERY_20231103","case_id":"R8L10_C26_NAVER_20231103","symbol":"035420","company_name":"NAVER","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"portal_ad_operating_leverage","loop_objective":"sector_specific_rule_discovery|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-03","entry_date":"2023-11-03","entry_price":200500,"evidence_available_at_that_date":"Q3 cost/ad recovery setup and later CHZZK optionality, but no immediate durable Green confirmation","evidence_source":"earnings/news source map; stock-web OHLC","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv|atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.22,"MFE_90D_pct":17.46,"MFE_180D_pct":17.46,"MFE_1Y_pct":17.46,"MFE_2Y_pct":null,"MAE_30D_pct":-3.99,"MAE_90D_pct":-7.23,"MAE_180D_pct":-20.40,"MAE_1Y_pct":-20.40,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":235500,"drawdown_after_peak_pct":-32.23,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"moderate_positive_then_fade","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"035420_2023-11-03_200500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109","case_id":"R8L10_C26_KAKAO_20231109","symbol":"035720","company_name":"Kakao","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform_recovery_governance_overhang","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-09","entry_date":"2023-11-09","entry_price":45600,"evidence_available_at_that_date":"platform recovery narrative; governance/legal overhang still unresolved","evidence_source":"earnings/news source map; Reuters governance source; stock-web OHLC","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":["accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv|atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.61,"MFE_90D_pct":35.75,"MFE_180D_pct":35.75,"MFE_1Y_pct":35.75,"MFE_2Y_pct":null,"MAE_30D_pct":-4.71,"MAE_90D_pct":-4.71,"MAE_180D_pct":-16.45,"MAE_1Y_pct":-16.45,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-01-11","peak_price":61900,"drawdown_after_peak_pct":-38.45,"green_lateness_ratio":0.93,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["legal_or_regulatory_block"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green_if_uncapped","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"035720_2023-11-09_45600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KAKAO_4B_VALUATION_GOVERNANCE_CAP_20240111","case_id":"R8L10_C26_KAKAO_20231109","symbol":"035720","company_name":"Kakao","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_AND_AD_OPERATING_LEVERAGE_VS_GOVERNANCE_OVERHANG","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform_recovery_governance_overhang","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":60800,"evidence_available_at_that_date":"valuation/positioning rally near peak while governance/legal overhang remained active","evidence_source":"Reuters governance source; stock-web OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","legal_or_regulatory_block","positioning_overheat"],"stage4c_evidence_fields":["accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.81,"MFE_90D_pct":1.81,"MFE_180D_pct":1.81,"MFE_1Y_pct":1.81,"MFE_2Y_pct":null,"MAE_30D_pct":-15.30,"MAE_90D_pct":-23.36,"MAE_180D_pct":-37.34,"MAE_1Y_pct":-37.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-11","peak_price":61900,"drawdown_after_peak_pct":-38.45,"green_lateness_ratio":0.93,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_governance_evidence_used","four_b_evidence_type":["valuation_blowoff","legal_or_regulatory_block","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"035720_2024-01-11_60800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4B_overlay","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C26_SOOP_20231207","trigger_id":"SOOP_STAGE2_TWITCH_EXIT_MIGRATION_20231207","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":55,"revision_score":45,"relative_strength_score":95,"customer_quality_score":80,"policy_or_regulatory_score":50,"valuation_repricing_score":60,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"traffic_migration_score":95,"monetization_confirmation_score":55},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Stage3-Yellow watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":60,"revision_score":50,"relative_strength_score":95,"customer_quality_score":85,"policy_or_regulatory_score":50,"valuation_repricing_score":65,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"traffic_migration_score":95,"monetization_confirmation_score":65},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable/Yellow; Green only after monetization confirmation","changed_components":["monetization_confirmation_score","customer_quality_score"],"component_delta_explanation":"External traffic migration event is strong Stage2; Green remains tied to monetization confirmation.","MFE_90D_pct":82.25,"MAE_90D_pct":-6.01,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C26_NAVER_20231103","trigger_id":"NAVER_STAGE2_Q3_COST_AD_RECOVERY_20231103","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":60,"revision_score":55,"relative_strength_score":55,"customer_quality_score":65,"policy_or_regulatory_score":35,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"traffic_migration_score":45,"monetization_confirmation_score":50},"weighted_score_before":74,"stage_label_before":"Stage2/Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":45,"customer_quality_score":65,"policy_or_regulatory_score":35,"valuation_repricing_score":45,"execution_risk_score":40,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"traffic_migration_score":45,"monetization_confirmation_score":45},"weighted_score_after":72,"stage_label_after":"Stage2/Yellow cap; no Green","changed_components":["monetization_confirmation_score","relative_strength_score"],"component_delta_explanation":"Moderate MFE but poor 180D MAE supports no-Green cap until realized operating leverage is clearer.","MFE_90D_pct":17.46,"MAE_90D_pct":-7.23,"score_return_alignment_label":"aligned_moderate","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C26_KAKAO_20231109","trigger_id":"KAKAO_STAGE2_Q3_RECOVERY_GOV_OVERHANG_20231109","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":55,"revision_score":55,"relative_strength_score":75,"customer_quality_score":65,"policy_or_regulatory_score":35,"valuation_repricing_score":65,"execution_risk_score":55,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":0,"accounting_trust_risk_score":55,"traffic_migration_score":20,"monetization_confirmation_score":45},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow / false Green risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":65,"customer_quality_score":60,"policy_or_regulatory_score":30,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":0,"accounting_trust_risk_score":70,"traffic_migration_score":20,"monetization_confirmation_score":35},"weighted_score_after":65,"stage_label_after":"Yellow cap / 4B watch","changed_components":["legal_or_contract_risk_score","accounting_trust_risk_score","monetization_confirmation_score"],"component_delta_explanation":"Governance/regulatory overhang and weak durable monetization evidence cap Green despite early MFE.","MFE_90D_pct":35.75,"MAE_90D_pct":-4.71,"score_return_alignment_label":"aligned_counterexample_after_guard","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See section 24.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"new_canonical_archetype_count":0,"new_trigger_family_count":3,"same_archetype_new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["c26_false_green_from_platform_recovery_without_governance_cap","c26_traffic_migration_stage2_success"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R8/C26 undercovered platform operating leverage with governance overhang counterexample","diversity_score_summary":"high_total_55_avg_18.3"}
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
next_round_candidate = R8 or R9
next_large_sector_options = [L8_PLATFORM_CONTENT_SW_SECURITY, L9_CONSTRUCTION_REALESTATE_HOUSING]
next_canonical_archetype_options = [C27_CONTENT_IP_GLOBAL_MONETIZATION, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE]
remaining_gap = add hard 4C platform case; add pure software/security contract-retention cases; add content-IP monetization counterexamples
```

## 28. Source Notes

- Stock-agent ingest summary and registry were used only for coverage/duplicate avoidance. fileciteturn29file0turn43file0
- Applied global calibration axes were treated as already promoted, not newly proposed. fileciteturn30file0
- Stock-web manifest/schema/profiles/shards were used as the sole price basis. fileciteturn31file0turn32file0turn44file0turn45file0turn46file0turn47file0turn48file0turn50file0turn49file0turn51file0turn52file0turn53file0turn54file0
- External event evidence: Twitch Korea exit and CHZZK migration context were used as historical trigger context; Kakao governance/legal overhang was used as counterexample risk context. citeturn614316search0turn614316search2turn405844news0
