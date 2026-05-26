# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 16
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_HOLDOUT
output_file = e2r_stock_web_v12_residual_round_R13_loop_16_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
```

This file is historical calibration research only. It is not a live candidate scan, not a recommendation, and not a repository patch.

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

The tested question is not whether Stage2 tends to precede Green. The residual question is narrower: in platform/content names, when does user-traffic or ad-optionality become actual ad inventory / operating leverage evidence, and when is it only a price-led re-rating story?

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R13 |
| loop | 16 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| fine_archetype_id | PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_HOLDOUT |
| loop_objective | holdout_validation; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; coverage_gap_fill |
| selected symbols | 067160 SOOP, 035420 NAVER, 035720 카카오 |
| rule_scope | canonical_archetype_specific with L8 sector guard |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were read only for coverage and duplicate avoidance. The ingest summary reports 107 parsed result MDs, 1,940 validated trigger rows, 1,376 aggregate representative trigger rows, and full R1-R13 coverage. The applied scoring diff already globalized Stage2 actionable bonus, stricter Green gates, price-only blowoff guard, non-price 4B requirement, and hard 4C thesis-break routing. This loop therefore avoids re-proposing those as global rules.

Novelty basis:

| Case | New symbol? | New trigger family? | New residual type? | Counted new? |
|---|---:|---:|---:|---:|
| C26_SOOP_2023_TWITCH_EXIT_MIGRATION | true | user migration to ad/gift inventory | missed structural Stage2 if only revision evidence is accepted | true |
| C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY | true | search-ad margin bridge + streaming optionality | partial MFE but poor 180D durability | true |
| C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY | true | platform ad relief without durable margin bridge | residual false positive after price-led relief rally | true |

```text
required_new_independent_case_ratio = 0.60
calibration_usable_case_count = 3
new_independent_case_count = 3
new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web source fields checked from `atlas/manifest.json` and `atlas/schema.json`:

| manifest/schema field | value |
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
| price_basis | tradable_raw |

Schema confirms tradable columns: `d,o,h,l,c,v,a,mc,s,m`. The MFE/MAE formula is the stock-web schema formula: max high or min low from entry date through N tradable rows divided by entry close.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | profile caveat | 180D forward window | corporate action overlap in tested 180D? | calibration_usable |
|---|---|---|---|---:|---:|---:|
| C26_SOOP_2023_TWITCH_EXIT_MIGRATION | 067160 | atlas/symbol_profiles/067/067160.json | corporate-action candidates exist only in old windows: 2005, 2007, 2008, 2011 | available to 2026-02-20 | false | true |
| C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY | 035420 | atlas/symbol_profiles/035/035420.json | corporate-action candidates through 2018; tested 2023-2024 window clean | available to 2026-02-20 | false | true |
| C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY | 035720 | atlas/symbol_profiles/035/035720.json | corporate-action candidates through 2021; tested 2023-2024 window clean | available to 2026-02-20 | false | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression rationale |
|---|---|---|
| TWITCH_EXIT_USER_MIGRATION_TO_STREAMING_AD_INVENTORY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | User migration only matters if it becomes monetizable inventory and operating leverage. |
| SEARCH_AD_MARGIN_BRIDGE_WITH_NEW_STREAMING_OPTIONALITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Search/platform ad margin bridge is the monetization engine; streaming optionality is only a support signal. |
| TALKBIZ_RELIEF_RALLY_WITH_WEAK_DURABLE_MARGIN | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | TalkBiz recovery without durable margin conversion is a C26 false-positive route. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | calibration_usable |
|---|---|---|---|---|---|---|---:|
| C26_SOOP_2023_TWITCH_EXIT_MIGRATION | 067160 | SOOP / former AfreecaTV | structural_success | positive | TRG_C26_SOOP_2023_12_07_STAGE2A | current_profile_missed_structural | true |
| C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY | 035420 | NAVER | high_mae_success | mixed_positive | TRG_C26_NAVER_2023_11_06_STAGE2A | current_profile_too_early | true |
| C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY | 035720 | 카카오 | failed_rerating | counterexample | TRG_C26_KAKAO_2023_11_10_STAGE2A | current_profile_false_positive | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
mixed_positive_case_count = 1
counterexample_count = 1
4B_case_count = 2
4C_case_count = 0
minimum_positive_case_count = 1 satisfied
minimum_counterexample_count = 1 satisfied
minimum_calibration_usable_case_count = 3 satisfied
```

SOOP is the clean positive. NAVER produced tradable upside but weak durability; it is counted as mixed rather than a clean structural positive. Kakao is the counterexample: strong price relief but insufficient durable platform ad operating-leverage evidence.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | evidence caveat |
|---|---|---|---|---|
| C26_SOOP_2023_TWITCH_EXIT_MIGRATION | 2023-12-06 | Twitch announced it would exit South Korea effective 2024-02-27; this created a direct migration option for domestic streaming platforms. | public Twitch Korea exit announcement; stock-web price shard confirms immediate next-day tradable entry. | User migration is not the same as monetization; later ad/gift conversion must be verified for Green. |
| C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY | 2023-11-03 | NAVER Q3 2023 relief around search/platform earnings plus later CHZZK optionality after Twitch exit. | earnings/event map plus stock-web price shard. | CHZZK optionality should not automatically raise ad operating-leverage score until inventory/revenue evidence is visible. |
| C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY | 2023-11-09 | Platform/TalkBiz relief and restructuring narrative after Q3 2023 earnings window. | earnings/event map plus stock-web price shard. | Relief rally lacked durable margin/revision bridge; legal/governance/regulatory overhang remained a guard input. |

## 10. Price Data Source Map

| symbol | price_shard_path(s) used | profile_path | stock_web_manifest_max_date |
|---|---|---|---|
| 067160 | atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv; atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv | atlas/symbol_profiles/067/067160.json | 2026-02-20 |
| 035420 | atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv; atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv | atlas/symbol_profiles/035/035420.json | 2026-02-20 |
| 035720 | atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv; atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv | atlas/symbol_profiles/035/035720.json | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B evidence | current_profile_verdict |
|---|---|---|---|---|---:|---|---|---|---|
| TRG_C26_SOOP_2023_12_07_STAGE2A | C26_SOOP_2023_TWITCH_EXIT_MIGRATION | Stage2-Actionable | 2023-12-06 | 2023-12-07 | 76600 | public_event_or_disclosure; customer_or_order_quality; relative_strength; capacity_or_volume_route | no confirmed revision yet | none | current_profile_missed_structural |
| TRG_C26_SOOP_2024_07_11_4B | C26_SOOP_2023_TWITCH_EXIT_MIGRATION | 4B | 2024-07-11 | 2024-07-11 | 134600 | none | financial_visibility partial | valuation_blowoff; positioning_overheat | current_profile_4B_too_late |
| TRG_C26_NAVER_2023_11_06_STAGE2A | C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY | Stage2-Actionable | 2023-11-03 | 2023-11-06 | 205500 | public_event_or_disclosure; early_revision_signal | partial margin bridge | none | current_profile_too_early |
| TRG_C26_NAVER_2024_01_16_4B | C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY | 4B | 2024-01-16 | 2024-01-16 | 230000 | none | partial | price_only; valuation_blowoff | current_profile_4B_too_late |
| TRG_C26_KAKAO_2023_11_10_STAGE2A | C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY | Stage2-Actionable | 2023-11-09 | 2023-11-10 | 45650 | public_event_or_disclosure; relative_strength; early_revision_signal | weak confirmed revision | legal_or_contract_risk; accounting_or_trust_risk | current_profile_false_positive |
| TRG_C26_KAKAO_2024_01_11_4B | C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY | 4B | 2024-01-11 | 2024-01-11 | 60800 | none | weak | valuation_blowoff; legal_or_contract_risk; positioning_overheat | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

Representative rows use deduped entry groups. 4B rows are overlay-only and are not counted as positive entry representatives.

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| TRG_C26_SOOP_2023_12_07_STAGE2A | 2023-12-07 | 76600 | 45.43 | -6.01 | 82.25 | -6.01 | 87.73 | -6.01 | 2024-07-11 | 143800 | -51.32 | true |
| TRG_C26_NAVER_2023_11_06_STAGE2A | 2023-11-06 | 205500 | 10.22 | -6.33 | 14.60 | -10.85 | 14.60 | -22.34 | 2024-01-16 | 235500 | -32.23 | true |
| TRG_C26_KAKAO_2023_11_10_STAGE2A | 2023-11-10 | 45650 | 20.48 | -1.64 | 35.60 | -1.64 | 35.60 | -16.54 | 2024-01-11 | 61900 | -38.45 | true |

Observed stock-web rows anchoring the calculations:

```text
067160: 2023-12-07 close 76600; 2024-01-17 high 111400; 2024-02-28 high 139600; 2024-07-11 high 143800.
035420: 2023-11-06 close 205500; 2023-12-15 high 226500; 2024-01-16 high 235500; 2024-07-02 low 159600.
035720: 2023-11-10 close 45650; 2023-12-15 high 55000; 2024-01-11 high 61900; 2024-07-24 low 38100.
```

## 13. Current Calibrated Profile Stress Test

### C26_SOOP_2023_TWITCH_EXIT_MIGRATION

The current global profile would likely avoid Green until revenue/revision proof was available. That is correct for Stage3-Green, but too late for Stage2-Actionable in this specific archetype because the evidence was not a vague theme: a direct competitor exit created observable user-migration optionality. The 180D MFE of 87.73% with only -6.01% MAE supports a C26-specific Stage2 bridge when a traffic source is forcibly displaced and the receiving platform already has monetization rails.

Verdict: `current_profile_missed_structural`.

### C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY

NAVER produced tradable upside but the 180D path deteriorated. The MFE was front-loaded and the later MAE reached -22.34%. The current profile was too willing to read platform optionality as structural operating leverage when the new streaming product still lacked confirmed monetization data.

Verdict: `current_profile_too_early`.

### C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY

Kakao's price path rewarded the initial relief rally, but the eventual drawdown after the January 2024 peak was large. The case shows why price-led relief plus weak ad evidence should not become a positive Stage3 route without durable TalkBiz/ad margin conversion and governance/legal risk checks.

Verdict: `current_profile_false_positive`.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2-Actionable entry | Green-like confirmation status | green_lateness_ratio | interpretation |
|---|---:|---|---:|---|
| C26_SOOP_2023_TWITCH_EXIT_MIGRATION | 76600 | no clean Green at entry; later monetization proof lagged price | not_applicable | Stage2-specific bridge needed; Green should remain strict. |
| C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY | 205500 | not clean Green; revision bridge incomplete | not_applicable | Do not promote optionality alone. |
| C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY | 45650 | false Green risk if price and relief narrative over-weighted | not_applicable | TalkBiz recovery needs margin/revision proof. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry price | 4B entry price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TRG_C26_SOOP_2024_07_11_4B | 76600 | 134600 | 143800 | 143800 | 0.86 | 0.86 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing if supported by non-price slowdown; otherwise watch-only |
| TRG_C26_NAVER_2024_01_16_4B | 205500 | 230000 | 235500 | 235500 | 0.82 | 0.82 | price_only; valuation_blowoff | price_only_local_4B_too_early unless revision slowdown is visible |
| TRG_C26_KAKAO_2024_01_11_4B | 45650 | 60800 | 61900 | 61900 | 0.93 | 0.93 | valuation_blowoff; legal_or_contract_risk; positioning_overheat | good_full_window_4B_timing |

## 16. 4C Protection Audit

No clean hard-4C trigger is trained in this loop. The correct treatment is watch/overlay unless a thesis-break route appears: ad conversion failure, governance/legal break, or explicit platform monetization failure. 4C rows are therefore omitted from positive calibration.

```text
four_c_protection_label = thesis_break_watch_only
```

## 17. Sector-Specific Rule Candidate

### Candidate: L8 platform ad operating-leverage bridge

```text
rule_scope = sector_specific
axis = l8_platform_forced_user_migration_stage2_bridge
baseline_value = 0
shadow_tested_value = +1.5
condition = forced traffic displacement + receiving platform with existing monetization rails + positive relative strength
negative_guard = no Green unless revenue/revision/margin bridge is confirmed
```

Rationale: platform businesses can absorb displaced users faster than industrial order-book businesses absorb backlog. But user traffic is still only raw ore; it must pass through monetization rails before it becomes EPS metal. The shadow bridge should help Stage2-Actionable only, not Stage3-Green.

## 18. Canonical-Archetype Rule Candidate

### Candidate: C26 ad revenue without margin bridge cap

```text
rule_scope = canonical_archetype_specific
axis = c26_ad_revenue_without_margin_bridge_cap
baseline_value = 0
shadow_tested_value = -2.0 to Green promotion score
condition = platform/ad narrative present but no confirmed margin bridge, no durable revision, and governance/legal/execution risk remains elevated
```

Rationale: NAVER and Kakao both show that price can move before durable operating leverage. SOOP was different because the exogenous user-flow event was directly tied to an existing live-streaming monetization system.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | 3 | SOOP, NAVER, KAKAO | 44.15 | -6.17 | 45.98 | -14.96 | 0.33 | 1 | 1 | mixed: misses SOOP, too loose for Kakao/NAVER optionality |
| P0b_e2r_2_0_baseline_reference | rollback reference | 3 | SOOP, NAVER, KAKAO | 44.15 | -6.17 | 45.98 | -14.96 | 0.67 | 1 | 0 | worse false-positive discipline |
| P1_L8_sector_specific_candidate_profile | sector shadow | 3 | SOOP only promoted; NAVER/KAKAO capped | 82.25 | -6.01 | 87.73 | -6.01 | 0.00 | 0 | 1 | best risk-adjusted alignment |
| P2_C26_canonical_candidate_profile | canonical shadow | 3 | SOOP promoted, NAVER Yellow, Kakao blocked | 82.25 | -6.01 | 87.73 | -6.01 | 0.00 | 0 | 1 | best explanatory compression |
| P3_counterexample_guard_profile | guard shadow | 3 | blocks price-only/platform optionality without margin bridge | 82.25 | -6.01 | 87.73 | -6.01 | 0.00 | 0 | 1 | keeps upside where evidence is forced-migration + monetization rails |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| C26_SOOP_2023_TWITCH_EXIT_MIGRATION | 74 | Stage2 | 79 | Stage2-Actionable | 82.25 | -6.01 | improved: bridge captures real structural move |
| C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY | 76 | Stage3-Yellow | 72 | Stage2-Watch | 14.60 | -10.85 | improved: avoids over-promoting optionality |
| C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY | 78 | Stage3-Yellow | 68 | Watch/Blocked | 35.60 | -1.64 | improved: positive MFE existed, but durability/overhang made Green unsafe |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_HOLDOUT | 1 | 1 | 3 | 0 | 3 | 0 | 6 | 3 | 3 | true | true | Need more C26 cases outside mega platforms, especially software-ad hybrids and retention-driven platform monetization. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [missed_forced_user_migration_stage2, optionality_overpromotion, relief_rally_false_positive, price_only_4b_watch_only]
new_axis_proposed: [l8_platform_forced_user_migration_stage2_bridge, c26_ad_revenue_without_margin_bridge_cap]
existing_axis_strengthened: [stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_cross_evidence_green_buffer, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema fields
- symbol profile availability and corporate action caveats
- actual stock-web tradable OHLC rows around entry and forward windows
- trigger-level MFE/MAE using tradable_raw basis
- same-entry dedupe for aggregate representatives
- 4B local vs full-window separation
```

Not validated:

```text
- current/live candidate scan
- investment suitability
- brokerage/API data
- exact production scoring code
- src/e2r implementation details
- accounting restatement or full analyst consensus database
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,l8_platform_forced_user_migration_stage2_bridge,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1.5,+1.5,"Forced user migration to a monetized platform can be Stage2-Actionable before formal revision.","Captures SOOP while keeping Green strict.","TRG_C26_SOOP_2023_12_07_STAGE2A",1,1,0,medium,sector_shadow_only,"not production; requires later batch implementation"
shadow_weight,c26_ad_revenue_without_margin_bridge_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,-2.0,-2.0,"Ad/platform optionality without margin/revision bridge over-promotes NAVER/Kakao-like relief rallies.","Blocks false Green and weak Yellow-to-Green transitions.","TRG_C26_NAVER_2023_11_06_STAGE2A|TRG_C26_KAKAO_2023_11_10_STAGE2A",2,2,1,medium,archetype_shadow_only,"not production; canonical C26 guard"
shadow_weight,c26_full_4b_requires_non_price_slowdown_or_risk,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Platform names often make price-only local peaks; full 4B needs valuation plus margin/revision/legal risk.","Improves overlay timing for Kakao; keeps NAVER price-only 4B watch-only.","TRG_C26_NAVER_2024_01_16_4B|TRG_C26_KAKAO_2024_01_11_4B|TRG_C26_SOOP_2024_07_11_4B",3,3,1,low,archetype_shadow_only,"strengthens existing 4B non-price requirement only within C26"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C26_SOOP_2023_TWITCH_EXIT_MIGRATION","symbol":"067160","company_name":"SOOP","round":"R13","loop":"16","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TWITCH_EXIT_USER_MIGRATION_TO_STREAMING_AD_INVENTORY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C26_SOOP_2023_12_07_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"forced migration plus monetization rails matched high 90D/180D MFE with controlled MAE","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Stage2 bridge only; Green still requires monetization/revision confirmation."}
{"row_type":"case","case_id":"C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY","symbol":"035420","company_name":"NAVER","round":"R13","loop":"16","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_AD_MARGIN_BRIDGE_WITH_NEW_STREAMING_OPTIONALITY","case_type":"high_mae_success","positive_or_counterexample":"mixed_positive","best_trigger":"TRG_C26_NAVER_2023_11_06_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"modest 90D MFE but poor 180D durability","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Optionality should not substitute for confirmed ad revenue and margin bridge."}
{"row_type":"case","case_id":"C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY","symbol":"035720","company_name":"카카오","round":"R13","loop":"16","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALKBIZ_RELIEF_RALLY_WITH_WEAK_DURABLE_MARGIN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C26_KAKAO_2023_11_10_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"large relief rally but later drawdown shows weak durable Stage3 quality","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Governance/legal overhang and weak margin bridge should cap positive promotion."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_C26_SOOP_2023_12_07_STAGE2A","case_id":"C26_SOOP_2023_TWITCH_EXIT_MIGRATION","symbol":"067160","company_name":"SOOP","round":"R13","loop":"16","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TWITCH_EXIT_USER_MIGRATION_TO_STREAMING_AD_INVENTORY","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform ad revenue operating leverage","loop_objective":"holdout_validation|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-06","evidence_available_at_that_date":"Twitch Korea exit announcement created direct user migration optionality for domestic live-streaming platforms.","evidence_source":"public event; stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv|atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-07","entry_price":76600,"MFE_30D_pct":45.43,"MFE_90D_pct":82.25,"MFE_180D_pct":87.73,"MFE_1Y_pct":87.73,"MFE_2Y_pct":87.73,"MAE_30D_pct":-6.01,"MAE_90D_pct":-6.01,"MAE_180D_pct":-6.01,"MAE_1Y_pct":-6.01,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-51.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_SOOP_2023_12_07_76600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C26_SOOP_2024_07_11_4B","case_id":"C26_SOOP_2023_TWITCH_EXIT_MIGRATION","symbol":"067160","company_name":"SOOP","round":"R13","loop":"16","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TWITCH_EXIT_USER_MIGRATION_TO_STREAMING_AD_INVENTORY","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform ad revenue operating leverage","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B","trigger_date":"2024-07-11","evidence_available_at_that_date":"Price was near full observed window peak after a major migration rally; non-price slowdown evidence would be required for full 4B.","evidence_source":"stock-web tradable shard; narrative overlay","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-11","entry_price":134600,"MFE_30D_pct":6.84,"MFE_90D_pct":6.84,"MFE_180D_pct":6.84,"MFE_1Y_pct":6.84,"MFE_2Y_pct":6.84,"MAE_30D_pct":-28.60,"MAE_90D_pct":-35.20,"MAE_180D_pct":-48.00,"MAE_1Y_pct":-51.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-51.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_SOOP_2024_07_11_134600","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_C26_NAVER_2023_11_06_STAGE2A","case_id":"C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY","symbol":"035420","company_name":"NAVER","round":"R13","loop":"16","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_AD_MARGIN_BRIDGE_WITH_NEW_STREAMING_OPTIONALITY","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform ad revenue operating leverage","loop_objective":"residual_false_positive_mining|holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-03","evidence_available_at_that_date":"Q3 earnings relief and early platform/search ad margin narrative; later CHZZK optionality remained unconfirmed for monetization.","evidence_source":"earnings/event map; stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv|atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-06","entry_price":205500,"MFE_30D_pct":10.22,"MFE_90D_pct":14.60,"MFE_180D_pct":14.60,"MFE_1Y_pct":14.60,"MFE_2Y_pct":23.84,"MAE_30D_pct":-6.33,"MAE_90D_pct":-10.85,"MAE_180D_pct":-22.34,"MAE_1Y_pct":-22.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":235500,"drawdown_after_peak_pct":-32.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_NAVER_2023_11_06_205500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C26_KAKAO_2023_11_10_STAGE2A","case_id":"C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY","symbol":"035720","company_name":"카카오","round":"R13","loop":"16","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALKBIZ_RELIEF_RALLY_WITH_WEAK_DURABLE_MARGIN","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform ad revenue operating leverage","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-09","evidence_available_at_that_date":"TalkBiz/platform relief rally but incomplete durable margin and revision bridge.","evidence_source":"earnings/event map; stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_contract_risk","accounting_or_trust_break"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv|atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-10","entry_price":45650,"MFE_30D_pct":20.48,"MFE_90D_pct":35.60,"MFE_180D_pct":35.60,"MFE_1Y_pct":35.60,"MFE_2Y_pct":35.60,"MAE_30D_pct":-1.64,"MAE_90D_pct":-1.64,"MAE_180D_pct":-16.54,"MAE_1Y_pct":-16.54,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":false,"peak_date":"2024-01-11","peak_price":61900,"drawdown_after_peak_pct":-38.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_KAKAO_2023_11_10_45650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_SOOP_2023_TWITCH_EXIT_MIGRATION","trigger_id":"TRG_C26_SOOP_2023_12_07_STAGE2A","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"user_migration_score":20,"monetization_rails_score":18},"weighted_score_before":74,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"user_migration_score":24,"monetization_rails_score":20},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","changed_components":["user_migration_score","monetization_rails_score"],"component_delta_explanation":"Forced competitor exit plus monetization rails adds Stage2 bridge, not Green.","MFE_90D_pct":82.25,"MAE_90D_pct":-6.01,"score_return_alignment_label":"improved","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_NAVER_2023_SEARCH_CHZZK_OPTIONALITY","trigger_id":"TRG_C26_NAVER_2023_11_06_STAGE2A","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":17,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"new_platform_optionality_score":14},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":15,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"new_platform_optionality_score":6},"weighted_score_after":72,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","new_platform_optionality_score"],"component_delta_explanation":"CHZZK optionality is capped until monetization/revision evidence appears.","MFE_90D_pct":14.60,"MAE_90D_pct":-10.85,"score_return_alignment_label":"improved_guard","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_KAKAO_2023_TALKBIZ_RELIEF_RALLY","trigger_id":"TRG_C26_KAKAO_2023_11_10_STAGE2A","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":12,"revision_score":16,"relative_strength_score":18,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":12,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12,"talkbiz_recovery_score":18},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":14,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":14,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":16,"talkbiz_recovery_score":8},"weighted_score_after":68,"stage_label_after":"Watch/Blocked","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","legal_or_contract_risk_score","accounting_trust_risk_score","talkbiz_recovery_score"],"component_delta_explanation":"Relief rally is capped by weak durable margin bridge and elevated trust/legal risk.","MFE_90D_pct":35.60,"MAE_90D_pct":-1.64,"score_return_alignment_label":"improved_false_positive_guard","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See CSV in Section 24.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"16","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["missed_forced_user_migration_stage2","optionality_overpromotion","relief_rally_false_positive","price_only_4b_watch_only"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"C26_CHZZK_STANDALONE_2024","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reason":"CHZZK launch optionality is treated as support evidence only unless ad inventory/revenue conversion is independently visible.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R13_loop_17_or_batch_implementation
recommended_next_scope = L8_PLATFORM_CONTENT_SW_SECURITY / C27_CONTENT_IP_GLOBAL_MONETIZATION or L6_FINANCIAL_CAPITAL_RETURN_DIGITAL / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
reason = continue residual expansion into adjacent platform/content or capital-return archetype without repeating C26.
```

## 28. Source Notes

- Stock-Web manifest checked: `atlas/manifest.json`; manifest max date `2026-02-20`.
- Stock-Web schema checked: `atlas/schema.json`; MFE/MAE formula and tradable/raw column definitions followed.
- Profiles checked: `atlas/symbol_profiles/067/067160.json`, `atlas/symbol_profiles/035/035420.json`, `atlas/symbol_profiles/035/035720.json`.
- Price shards checked: `atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv`, `atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv`, `atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/035/035720/2023.csv`, `atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv`.
- External evidence context was used only to classify public-event timing, not for live screening.
