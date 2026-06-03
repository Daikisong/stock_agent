# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
scheduled_round = R11
scheduled_loop = 13
completed_round = R11
completed_loop = 13
next_round = R12
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA
output_file = e2r_stock_web_v12_residual_round_R11_loop_13_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 current-profile residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question is not whether public events can move stocks. They can. The question is whether the event has a pipe into company economics. A policy/disaster shock is like rain on different roofs: 씨젠 and 수젠텍 had gutters connected to diagnostic demand; 오공 and 웰크론 mostly had a wet roof and a crowd looking up.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 13
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA
round_sector_consistency = pass
```

R11 is used as a policy/event checkpoint. C31 is used because the trigger family is not a normal sector earnings cycle; it is a public-health policy/disaster event that either transmits into orders and revisions or burns out as headline beta.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 result files show Loop 13 has completed R1 through R10 and points next to R11/Loop 13. Prior R11 loops already covered C32 control-premium/tender-cap and one C31 policy-value-up/oil-gas headline set. This loop avoids those symbols and trigger families.

```text
selected_scope = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
prior_R11_C31_symbols_avoided = 005380|402340|316140|036460|004090|024060
prior_R11_C32_symbols_avoided = 041510|010130|011200|008930|048260
same_symbol_same_trigger_duplicate = none
minimum_new_symbol_count = 4
minimum_counterexample_count = 2
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
price_basis = tradable_raw
```

The schema uses `d,o,h,l,c,v,a,mc,s,m` for tradable shards and computes `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100` and `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`. This MD uses tradable rows only for calibration.

## 5. Historical Eligibility Gate

|Symbol|Company|Entry date|180D forward available|Corporate action status|Calibration usable|Profile path|
|---|---|---|---|---|---|---|
|096530|씨젠|2020-02-18|yes|clean_180D_window|true|atlas/symbol_profiles/096/096530.json|
|253840|수젠텍|2020-02-20|yes|clean_180D_window|true|atlas/symbol_profiles/253/253840.json|
|045060|오공|2020-01-20|yes|clean_180D_window|true|atlas/symbol_profiles/045/045060.json|
|065950|웰크론|2020-01-20|yes|clean_180D_window|true|atlas/symbol_profiles/065/065950.json|


All representative rows have at least 180 forward trading rows by stock-web max date. Corporate-action candidates in these profiles are outside the 180D windows or absent.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rationale |
|---|---|---|
| COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Public-health policy/disaster event with direct diagnostic capacity and later revenue/revision conversion. |
| COVID_MASK_THEME_EVENT_ONLY | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Same public-health event, but missing company-level order/subsidy/margin conversion; should compress into C31 as counterexample/4B overlay, not a separate global rule. |
| PUBLIC_HEALTH_4B_THEME_BLOWOFF | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Event-premium exhaustion belongs to 4B timing, not Stage3 promotion. |

## 7. Case Selection Summary

|Symbol|Company|Role|Trigger|Entry price|Outcome|Current profile verdict|
|---|---|---|---|---|---|---|
|096530|씨젠|structural_success|2020-02-18|35550|real_demand_policy_event_structural_success|current_profile_correct|
|253840|수젠텍|high_mae_success|2020-02-20|6980|real_demand_but_early_blowoff_high_mae_success|current_profile_4B_too_late|
|045060|오공|price_moved_without_evidence|2020-01-20|4775|headline_theme_blowoff_without_durable_policy_transmission|current_profile_false_positive|
|065950|웰크론|price_moved_without_evidence|2020-01-20|4855|headline_theme_blowoff_without_durable_policy_transmission|current_profile_false_positive|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 3
4C_case_count = 0
calibration_usable_case_count = 4
representative_trigger_count = 4
calibration_usable_trigger_count = 7
```

Two cases show real policy/disaster transmission into diagnostic demand. Two cases show event-only mask theme beta: high MFE, but no durable evidence bridge and deep drawdown after the local peak.

## 9. Evidence Source Map

| Case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 씨젠 | public-health event, diagnostic capacity, RS | later revision/financial visibility | later valuation blowoff | none |
| 수젠텍 | public-health event, diagnostic optionality, RS | partial later conversion | valuation/positioning blowoff | none |
| 오공 | public-health event and mask theme RS | not supported | price-only local peak, positioning overheat | theme-only thesis break watch |
| 웰크론 | public-health event and protective-materials theme RS | not supported | price-only local peak, positioning overheat | theme-only thesis break watch |

## 10. Price Data Source Map

|Symbol|Company|Price shard|Profile|OHLC anchor note|
|---|---|---|---|---|
|096530|씨젠|atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv|atlas/symbol_profiles/096/096530.json|2020-02-18 close 35,550; 2020-08-10 high 322,200; profile corporate-action candidates are 2021-04-23/2021-05-20, outside 180D window.|
|253840|수젠텍|atlas/ohlcv_tradable_by_symbol_year/253/253840/2020.csv|atlas/symbol_profiles/253/253840.json|2020-02-20 close 6,980; 2020-03-31 high 36,550; later 2020-04-16 low 17,750.|
|045060|오공|atlas/ohlcv_tradable_by_symbol_year/045/045060/2020.csv|atlas/symbol_profiles/045/045060.json|2020-01-20 close 4,775; 2020-02-21 high 14,350; 2020-03-23 low 4,015 after the theme broke.|
|065950|웰크론|atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv|atlas/symbol_profiles/065/065950.json|2020-01-20 close 4,855; 2020-02-21 high 10,700; 2020-03-19 low 5,050 after peak.|


## 11. Case-by-Case Trigger Grid

|Symbol|Company|Trigger type|Trigger date|Entry date|Entry price|MFE90|MAE90|MFE180|MAE180|Peak date|Peak price|Outcome|Current profile verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|096530|씨젠|Stage2-Actionable|2020-02-18|2020-02-18|35550|297.75|-10.27|806.33|-10.27|2020-08-10|322200|real_demand_policy_event_structural_success|current_profile_correct|
|253840|수젠텍|Stage2-Actionable|2020-02-20|2020-02-20|6980|423.64|-12.46|423.64|-12.46|2020-03-31|36550|real_demand_but_early_blowoff_high_mae_success|current_profile_4B_too_late|
|045060|오공|Stage2-Actionable|2020-01-20|2020-01-20|4775|200.52|-21.36|200.52|-21.36|2020-02-21|14350|headline_theme_blowoff_without_durable_policy_transmission|current_profile_false_positive|
|065950|웰크론|Stage2-Actionable|2020-01-20|2020-01-20|4855|120.39|-16.17|120.39|-16.17|2020-02-21|10700|headline_theme_blowoff_without_durable_policy_transmission|current_profile_false_positive|


## 12. Trigger-Level OHLC Backtest Tables

|Symbol|Company|Entry date|Entry price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|Peak date|Peak price|Drawdown after peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|096530|씨젠|2020-02-18|35550|297.75|297.75|806.33|-10.27|-10.27|-10.27|2020-08-10|322200|-33.77|
|253840|수젠텍|2020-02-20|6980|423.64|423.64|423.64|-12.46|-12.46|-12.46|2020-03-31|36550|-51.44|
|045060|오공|2020-01-20|4775|200.52|200.52|200.52|-21.36|-21.36|-21.36|2020-02-21|14350|-72.02|
|065950|웰크론|2020-01-20|4855|120.39|120.39|120.39|-16.17|-16.17|-16.17|2020-02-21|10700|-52.8|


## 13. Current Calibrated Profile Stress Test

1. The current profile should correctly permit Stage2-Actionable for 씨젠 because the event had a diagnostic-capacity path. The later price path validates the early entry, with +806.33% 180D MFE and only -10.27% MAE.
2. The current profile is too late on 4B for 수젠텍. The policy/demand route was real, but the same row needs a positioning/valuation overlay after the March blowoff.
3. The current profile is vulnerable to false positives in 오공 and 웰크론 if public-health event + relative strength is allowed to promote without company-level demand evidence.
4. Stage2 bonus is useful for real demand transmission but too generous for theme-only event beta.
5. Yellow threshold 75 is acceptable only after a capacity/revision bridge is visible.
6. Green 87 / revision 55 remains appropriate: none of the theme-only mask rows should be Green.
7. Price-only blowoff guard is strengthened.
8. Full 4B non-price requirement is kept for structural exits, but C31 should add a theme-only event-cap overlay for public-health policy/disaster spikes.

## 14. Stage2 / Yellow / Green Comparison

| Case | Stage2 entry | Yellow/Green issue | green_lateness_ratio | Interpretation |
|---|---:|---|---:|---|
| 씨젠 | 35,550 | Green should wait for revision but not block Stage2 | 0.31 | Stage2 captures most of the move; Green confirmation is later but acceptable. |
| 수젠텍 | 6,980 | Green must not ignore 4B blowoff | 0.74 | Confirmed demand arrives late relative to the peak; 4B overlay is needed. |
| 오공 | 4,775 | No Green without company evidence | not_applicable | Event-only price spike. |
| 웰크론 | 4,855 | No Green without company evidence | not_applicable | Event-only price spike. |

## 15. 4B Local vs Full-window Timing Audit

| Trigger | Stage2 price | 4B entry price | Local peak | Full-window peak | local proximity | full-window proximity | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| 수젠텍 2020-03-31 | 6,980 | 32,250 | 36,550 | 36,550 | 1.00 | 1.00 | good_full_window_4B_timing |
| 오공 2020-02-20 | 4,775 | 12,300 | 14,350 | 14,350 | 0.79 | 0.79 | price_only_local_4B_too_early_for_full_4B_but_valid_theme_overlay |
| 웰크론 2020-02-20 | 4,855 | 9,190 | 10,700 | 10,700 | 0.74 | 0.74 | price_only_local_4B_too_early_for_full_4B_but_valid_theme_overlay |

For C31 public-health events, a price-only theme peak should not be a full thesis-breaking 4B for real diagnostic names. It is, however, a valid event-cap overlay for theme-only mask names.

## 16. 4C Protection Audit

No hard 4C row is proposed. The mask-theme cases are `thesis_break_watch_only`, because there is no explicit company-level thesis to break; the missing element is the company-level evidence bridge. The protection layer should therefore downgrade positive-stage promotion rather than claim a hard thesis failure.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
axis = L10_PUBLIC_HEALTH_THEME_ONLY_4B_ROUTER
proposal_type = sector_shadow_only
```

For L10 public-health/disaster events, theme-only names may need a sector-level 4B event-cap router. This is not a global rule: it is tied to public panic/shortage headlines where price can move before company economics appear.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
axis = C31_POLICY_EVENT_TRANSMISSION_QUALITY_GATE
proposal_type = canonical_shadow_only
```

C31 should split public-event triggers into two buckets:

- **Economic transmission bucket**: capacity/order/subsidy/revision bridge exists or appears quickly. Stage2 is valid and later Yellow/Green can follow.
- **Headline beta bucket**: no company-level bridge. Price movement can be recorded, but it must not promote Stage3 and should be eligible for 4B theme overlay.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|changed_thresholds|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_4B_local|avg_4B_full|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|global current proxy|Allows Stage2 on public event + RS; Green still needs revision|none|current thresholds|4|260.57|-15.07|387.72|-15.07|0.5|0|1|0.53|None|None|mixed: catches real demand but over-scores mask themes|
|P0b e2r_2_0_baseline_reference|rollback reference|Older baseline overweights event/RS and under-separates blowoff|none|old proxy|4|260.57|-15.07|387.72|-15.07|0.5|1|2|0.63|None|None|weaker alignment; too much event beta|
|P1 L10 public-health event shadow|sector specific|Route public-health theme-only names to 4B watch unless capacity/order evidence exists|theme_only_penalty +35|no production change|4|260.57|-15.07|387.72|-15.07|0.25|0|1|0.43|0.84|0.84|better: reduces false positives|
|P2 C31 transmission-quality shadow|canonical specific|Promote only when policy shock has company-level capacity/revision bridge|policy_execution_score + capacity_or_shipment_score|no production change|4|260.57|-15.07|387.72|-15.07|0.0|0|1|0.31|0.84|0.84|best: separates real demand from headline beta|
|P3 counterexample guard profile|guardrail|Cap price-only event spikes as 4B overlay and forbid Green without non-price evidence|price_only_theme_block true|no production change|4|260.57|-15.07|387.72|-15.07|0.0|1|0|0.0|0.84|0.84|safe but may miss early positive diagnostic demand|


## 20. Score-Return Alignment Matrix

| Symbol | Before stage | After stage | MFE90 | MAE90 | Alignment verdict |
|---|---|---|---:|---:|---|
| 096530 | Stage3-Yellow | Stage3-Yellow / later Green watch | 297.75 | -10.27 | positive event transmission aligned |
| 253840 | Stage3-Yellow | Stage3-Yellow + 4B overlay | 423.64 | -12.46 | positive but 4B timing required |
| 045060 | Stage2-Actionable | 4B theme-only watch | 200.52 | -21.36 | event-only false positive if promoted |
| 065950 | Stage2-Actionable | 4B theme-only watch | 120.39 | -16.17 | event-only false positive if promoted |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA | 2 | 2 | 3 | 0 | 4 | 0 | 7 | 4 | 3 | true | true | Adds COVID public-health policy/disaster event split; hard 4C still under-covered. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_false_positive|current_profile_4B_too_late
new_axis_proposed: C31_POLICY_EVENT_TRANSMISSION_QUALITY_GATE|L10_PUBLIC_HEALTH_THEME_ONLY_4B_ROUTER
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence_for_full_4B
existing_axis_weakened: none
existing_axis_kept: stage3_green_revision_min|hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- historical trigger-level OHLC validation using Songdaiki/stock-web tradable rows,
- 30D/90D/180D MFE/MAE and peak/drawdown checks,
- C31 public-health event transmission vs theme-only event beta split,
- shadow-only rule proposal for later batch ingestion.

Non-validation scope:

- no live candidate scan,
- no investment recommendation,
- no broker/API connection,
- no stock_agent source-code inspection,
- no production scoring change,
- no claim that these public-event proxies are complete without later source enrichment.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_POLICY_EVENT_TRANSMISSION_QUALITY_GATE,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy/disaster event requires company-level capacity/order/revision bridge before positive Stage3 promotion","Keeps 씨젠/수젠텍 positive while downgrading 오공/웰크론",R11L13_C31_096530_20200218_T1|R11L13_C31_253840_20200220_T1|R11L13_C31_045060_20200120_T1|R11L13_C31_065950_20200120_T1,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L10_PUBLIC_HEALTH_THEME_ONLY_4B_ROUTER,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Public-health shortage themes can have large MFE but poor durable alignment without company evidence","Improves 4B event-cap timing for theme-only names",R11L13_C31_253840_20200331_4B|R11L13_C31_045060_20200220_4B|R11L13_C31_065950_20200220_4B,3,2,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R11L13_C31_SEEGENE_2020_COVID_PCR_REAL_DEMAND","symbol":"096530","company_name":"씨젠","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R11L13_C31_096530_20200218_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"real_demand_policy_event_structural_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2020-02-18 close 35,550; 2020-08-10 high 322,200; profile corporate-action candidates are 2021-04-23/2021-05-20, outside 180D window."}
{"row_type":"case","case_id":"R11L13_C31_SUGENTECH_2020_COVID_RAPID_TEST_HIGH_MAE","symbol":"253840","company_name":"수젠텍","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R11L13_C31_253840_20200220_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"real_demand_but_early_blowoff_high_mae_success","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"2020-02-20 close 6,980; 2020-03-31 high 36,550; later 2020-04-16 low 17,750."}
{"row_type":"case","case_id":"R11L13_C31_OGONG_2020_MASK_THEME_EVENT_ONLY","symbol":"045060","company_name":"오공","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R11L13_C31_045060_20200120_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"headline_theme_blowoff_without_durable_policy_transmission","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2020-01-20 close 4,775; 2020-02-21 high 14,350; 2020-03-23 low 4,015 after the theme broke."}
{"row_type":"case","case_id":"R11L13_C31_WELCRON_2020_MASK_THEME_EVENT_ONLY","symbol":"065950","company_name":"웰크론","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R11L13_C31_065950_20200120_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"headline_theme_blowoff_without_durable_policy_transmission","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2020-01-20 close 4,855; 2020-02-21 high 10,700; 2020-03-19 low 5,050 after peak."}
{"row_type":"trigger","trigger_id":"R11L13_C31_096530_20200218_T1","case_id":"R11L13_C31_SEEGENE_2020_COVID_PCR_REAL_DEMAND","symbol":"096530","company_name":"씨젠","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy/subsidy/public-health event transmission","loop_objective":"residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2020-02-18","entry_date":"2020-02-18","entry_price":35550,"evidence_available_at_that_date":"Korea COVID cluster growth made PCR testing capacity a public-health bottleneck; 씨젠 had molecular-diagnostic production capacity and later converted the shock into large revenue/revision evidence.","evidence_source":"Public-health COVID shock plus stock-web OHLC; production handoff should enrich with KCDC/MFDS/export-disclosure sources before promotion.","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["confirmed_revision:later","financial_visibility:later","multiple_public_sources:later"],"stage4b_evidence_fields":["valuation_blowoff:later"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv","profile_path":"atlas/symbol_profiles/096/096530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":297.75,"MFE_90D_pct":297.75,"MFE_180D_pct":806.33,"MFE_1Y_pct":"not_calibrated_in_this_loop","MFE_2Y_pct":"not_calibrated_in_this_loop","MAE_30D_pct":-10.27,"MAE_90D_pct":-10.27,"MAE_180D_pct":-10.27,"MAE_1Y_pct":"not_calibrated_in_this_loop","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-10","peak_price":322200,"drawdown_after_peak_pct":-33.77,"green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"real_demand_policy_event_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_SEEGENE_2020_COVID_PCR_REAL_DEMAND-entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_253840_20200220_T1","case_id":"R11L13_C31_SUGENTECH_2020_COVID_RAPID_TEST_HIGH_MAE","symbol":"253840","company_name":"수젠텍","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy/subsidy/public-health event transmission","loop_objective":"residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2020-02-20","entry_date":"2020-02-20","entry_price":6980,"evidence_available_at_that_date":"COVID diagnostic-supply optionality became a public-health event route; the share path repriced quickly but needed 4B risk overlay because the peak arrived before durable long-cycle visibility.","evidence_source":"Public-health COVID shock plus stock-web OHLC; production handoff should enrich with diagnostic-kit authorization/export sources.","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion:partial_later","financial_visibility:later","low_red_team_risk:false"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","execution_risk_score"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253840/2020.csv","profile_path":"atlas/symbol_profiles/253/253840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":423.64,"MFE_90D_pct":423.64,"MFE_180D_pct":423.64,"MFE_1Y_pct":"not_calibrated_in_this_loop","MFE_2Y_pct":"not_calibrated_in_this_loop","MAE_30D_pct":-12.46,"MAE_90D_pct":-12.46,"MAE_180D_pct":-12.46,"MAE_1Y_pct":"not_calibrated_in_this_loop","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-03-31","peak_price":36550,"drawdown_after_peak_pct":-51.44,"green_lateness_ratio":0.74,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"real_demand_but_early_blowoff_high_mae_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_SUGENTECH_2020_COVID_RAPID_TEST_HIGH_MAE-entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_045060_20200120_T1","case_id":"R11L13_C31_OGONG_2020_MASK_THEME_EVENT_ONLY","symbol":"045060","company_name":"오공","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy/subsidy/public-health event transmission","loop_objective":"residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2020-01-20","entry_date":"2020-01-20","entry_price":4775,"evidence_available_at_that_date":"First domestic COVID case and mask-shortage narrative ignited a thematic trading route, but company-level subsidy/order/revision evidence was not visible at the trigger.","evidence_source":"Public-health COVID shock plus stock-web OHLC; production handoff should enrich with company-specific mask revenue/order evidence before any positive scoring.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision:not_supported","financial_visibility:not_supported","repeat_order_or_conversion:not_supported"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken:theme_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/045/045060/2020.csv","profile_path":"atlas/symbol_profiles/045/045060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":200.52,"MFE_90D_pct":200.52,"MFE_180D_pct":200.52,"MFE_1Y_pct":"not_calibrated_in_this_loop","MFE_2Y_pct":"not_calibrated_in_this_loop","MAE_30D_pct":-21.36,"MAE_90D_pct":-21.36,"MAE_180D_pct":-21.36,"MAE_1Y_pct":"not_calibrated_in_this_loop","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-02-21","peak_price":14350,"drawdown_after_peak_pct":-72.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"headline_theme_blowoff_without_durable_policy_transmission","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_OGONG_2020_MASK_THEME_EVENT_ONLY-entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_065950_20200120_T1","case_id":"R11L13_C31_WELCRON_2020_MASK_THEME_EVENT_ONLY","symbol":"065950","company_name":"웰크론","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy/subsidy/public-health event transmission","loop_objective":"residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2020-01-20","entry_date":"2020-01-20","entry_price":4855,"evidence_available_at_that_date":"Mask/protective-materials narrative was linked to public-health policy demand, but the trigger lacked company-level backlog, subsidy, or margin-bridge evidence.","evidence_source":"Public-health COVID shock plus stock-web OHLC; production handoff should enrich with company-specific order/margin data before any positive scoring.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision:not_supported","financial_visibility:not_supported","repeat_order_or_conversion:not_supported"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken:theme_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv","profile_path":"atlas/symbol_profiles/065/065950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":120.39,"MFE_90D_pct":120.39,"MFE_180D_pct":120.39,"MFE_1Y_pct":"not_calibrated_in_this_loop","MFE_2Y_pct":"not_calibrated_in_this_loop","MAE_30D_pct":-16.17,"MAE_90D_pct":-16.17,"MAE_180D_pct":-16.17,"MAE_1Y_pct":"not_calibrated_in_this_loop","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-02-21","peak_price":10700,"drawdown_after_peak_pct":-52.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"headline_theme_blowoff_without_durable_policy_transmission","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_WELCRON_2020_MASK_THEME_EVENT_ONLY-entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_253840_20200331_4B","case_id":"R11L13_C31_SUGENTECH_2020_COVID_RAPID_TEST_HIGH_MAE","symbol":"253840","company_name":"수젠텍","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy/public-health event 4B overlay","loop_objective":"residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4B","trigger_date":"2020-03-31","entry_date":"2020-03-31","entry_price":32250,"evidence_available_at_that_date":"Extreme diagnostic-theme valuation/positioning after rapid rise; 4B overlay should appear even while the Stage2 demand thesis remains valid.","evidence_source":"Public-health COVID shock plus stock-web OHLC; production handoff should enrich with diagnostic-kit authorization/export sources.","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion:partial_later","financial_visibility:later","low_red_team_risk:false"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","execution_risk_score"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253840/2020.csv","profile_path":"atlas/symbol_profiles/253/253840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.33,"MFE_90D_pct":13.33,"MFE_180D_pct":13.33,"MFE_1Y_pct":"not_calibrated_in_this_loop","MFE_2Y_pct":"not_calibrated_in_this_loop","MAE_30D_pct":-44.96,"MAE_90D_pct":-44.96,"MAE_180D_pct":-44.96,"MAE_1Y_pct":"not_calibrated_in_this_loop","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-03-31","peak_price":36550,"drawdown_after_peak_pct":-51.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"real_demand_but_early_blowoff_high_mae_success_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_SUGENTECH_2020_COVID_RAPID_TEST_HIGH_MAE-4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case; separate 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R11L13_C31_045060_20200220_4B","case_id":"R11L13_C31_OGONG_2020_MASK_THEME_EVENT_ONLY","symbol":"045060","company_name":"오공","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy/public-health event 4B overlay","loop_objective":"residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4B","trigger_date":"2020-02-20","entry_date":"2020-02-20","entry_price":12300,"evidence_available_at_that_date":"Price-only mask-theme local peak without company-specific order/revision evidence.","evidence_source":"Public-health COVID shock plus stock-web OHLC; production handoff should enrich with company-specific mask revenue/order evidence before any positive scoring.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision:not_supported","financial_visibility:not_supported","repeat_order_or_conversion:not_supported"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken:theme_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/045/045060/2020.csv","profile_path":"atlas/symbol_profiles/045/045060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.67,"MFE_90D_pct":16.67,"MFE_180D_pct":16.67,"MFE_1Y_pct":"not_calibrated_in_this_loop","MFE_2Y_pct":"not_calibrated_in_this_loop","MAE_30D_pct":-67.36,"MAE_90D_pct":-67.36,"MAE_180D_pct":-67.36,"MAE_1Y_pct":"not_calibrated_in_this_loop","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-02-21","peak_price":14350,"drawdown_after_peak_pct":-72.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":0.79,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"headline_theme_blowoff_without_durable_policy_transmission_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_OGONG_2020_MASK_THEME_EVENT_ONLY-4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case; separate 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R11L13_C31_065950_20200220_4B","case_id":"R11L13_C31_WELCRON_2020_MASK_THEME_EVENT_ONLY","symbol":"065950","company_name":"웰크론","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"COVID_PUBLIC_HEALTH_POLICY_REAL_DEMAND_VS_THEME_BETA","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy/public-health event 4B overlay","loop_objective":"residual_false_positive_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"4B","trigger_date":"2020-02-20","entry_date":"2020-02-20","entry_price":9190,"evidence_available_at_that_date":"Price-only mask-theme local peak without company-specific order/revision evidence.","evidence_source":"Public-health COVID shock plus stock-web OHLC; production handoff should enrich with company-specific order/margin data before any positive scoring.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision:not_supported","financial_visibility:not_supported","repeat_order_or_conversion:not_supported"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken:theme_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/065/065950/2020.csv","profile_path":"atlas/symbol_profiles/065/065950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.43,"MFE_90D_pct":16.43,"MFE_180D_pct":16.43,"MFE_1Y_pct":"not_calibrated_in_this_loop","MFE_2Y_pct":"not_calibrated_in_this_loop","MAE_30D_pct":-45.05,"MAE_90D_pct":-45.05,"MAE_180D_pct":-45.05,"MAE_1Y_pct":"not_calibrated_in_this_loop","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-02-21","peak_price":10700,"drawdown_after_peak_pct":-52.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"headline_theme_blowoff_without_durable_policy_transmission_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_WELCRON_2020_MASK_THEME_EVENT_ONLY-4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case; separate 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_SEEGENE_2020_COVID_PCR_REAL_DEMAND","trigger_id":"R11L13_C31_096530_20200218_T1","symbol":"096530","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":20,"relative_strength_score":55,"customer_quality_score":45,"policy_or_regulatory_score":68,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.2,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":48,"relative_strength_score":55,"customer_quality_score":45,"policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":82,"policy_execution_score":72,"theme_only_penalty":0},"weighted_score_after":86.5,"stage_label_after":"Stage3-Yellow / later Green watch","changed_components":["policy_execution_score","capacity_or_shipment_score","positioning_overheat_score","theme_only_penalty"],"component_delta_explanation":"Real diagnostic capacity + later revision converts public-health policy shock into economic transmission.","MFE_90D_pct":297.75,"MAE_90D_pct":-10.27,"score_return_alignment_label":"real_demand_policy_event_structural_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_SUGENTECH_2020_COVID_RAPID_TEST_HIGH_MAE","trigger_id":"R11L13_C31_253840_20200220_T1","symbol":"253840","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":15,"relative_strength_score":65,"customer_quality_score":25,"policy_or_regulatory_score":62,"valuation_repricing_score":72,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":65,"customer_quality_score":25,"policy_or_regulatory_score":62,"valuation_repricing_score":72,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":60,"policy_execution_score":62,"positioning_overheat_score":78,"theme_only_penalty":10},"weighted_score_after":80.3,"stage_label_after":"Stage3-Yellow + 4B overlay","changed_components":["policy_execution_score","capacity_or_shipment_score","positioning_overheat_score","theme_only_penalty"],"component_delta_explanation":"Rapid demand route is real, but 4B overlay is needed because valuation/positioning peaks ahead of durable visibility.","MFE_90D_pct":423.64,"MAE_90D_pct":-12.46,"score_return_alignment_label":"real_demand_but_early_blowoff_high_mae_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_OGONG_2020_MASK_THEME_EVENT_ONLY","trigger_id":"R11L13_C31_045060_20200120_T1","symbol":"045060","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":50,"valuation_repricing_score":80,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":50,"valuation_repricing_score":80,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":10,"policy_execution_score":18,"positioning_overheat_score":85,"theme_only_penalty":35},"weighted_score_after":58.5,"stage_label_after":"4B theme-only watch","changed_components":["policy_execution_score","capacity_or_shipment_score","positioning_overheat_score","theme_only_penalty"],"component_delta_explanation":"Headline/public-health policy beta without company-level order, subsidy, or margin bridge should be blocked from positive Stage3 promotion.","MFE_90D_pct":200.52,"MAE_90D_pct":-21.36,"score_return_alignment_label":"headline_theme_blowoff_without_durable_policy_transmission","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_WELCRON_2020_MASK_THEME_EVENT_ONLY","trigger_id":"R11L13_C31_065950_20200120_T1","symbol":"065950","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":50,"valuation_repricing_score":80,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":50,"valuation_repricing_score":80,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":10,"policy_execution_score":18,"positioning_overheat_score":85,"theme_only_penalty":35},"weighted_score_after":58.5,"stage_label_after":"4B theme-only watch","changed_components":["policy_execution_score","capacity_or_shipment_score","positioning_overheat_score","theme_only_penalty"],"component_delta_explanation":"Headline/public-health policy beta without company-level order, subsidy, or margin bridge should be blocked from positive Stage3 promotion.","MFE_90D_pct":120.39,"MAE_90D_pct":-16.17,"score_return_alignment_label":"headline_theme_blowoff_without_durable_policy_transmission","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"shadow_weight","axis":"C31_POLICY_EVENT_TRANSMISSION_QUALITY_GATE","scope":"canonical_archetype_specific","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","baseline_value":0,"tested_value":1,"delta":"+1","reason":"COVID public-health event shows that policy/disaster headlines require a company-level capacity/order/revision bridge before Stage3 promotion.","backtest_effect":"Keeps 씨젠/수젠텍 as positive while downgrading 오공/웰크론 to theme-only 4B watch.","trigger_ids":"R11L13_C31_096530_20200218_T1|R11L13_C31_253840_20200220_T1|R11L13_C31_045060_20200120_T1|R11L13_C31_065950_20200120_T1","calibration_usable_count":4,"new_independent_case_count":4,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"L10_PUBLIC_HEALTH_THEME_ONLY_4B_ROUTER","scope":"sector_specific","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Mask/protective-material theme names can have high MFE but poor durable alignment without company-specific evidence.","backtest_effect":"Improves 4B timing for 오공/웰크론 and prevents price-only event beta from becoming Green.","trigger_ids":"R11L13_C31_045060_20200220_4B|R11L13_C31_065950_20200220_4B|R11L13_C31_253840_20200331_4B","calibration_usable_count":3,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium","proposal_type":"sector_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"residual_contribution","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R11
completed_loop = 13
next_round = R12
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Manifest checked: `atlas/manifest.json`, max_date `2026-02-20`, price basis `tradable_raw`, adjustment `raw_unadjusted_marcap`.
- Schema checked: `atlas/schema.json`, tradable columns `d,o,h,l,c,v,a,mc,s,m`, MFE/MAE formula as specified.
- Profiles checked: `096530`, `253840`, `045060`, `065950`.
- Tradable OHLC shards checked: `096/096530/2020.csv`, `253/253840/2020.csv`, `045/045060/2020.csv`, `065/065950/2020.csv`.
- This MD intentionally uses historical public-health event cases and does not make current/live investment claims.
