# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R13
scheduled_loop: 11
completed_round: R13
completed_loop: 11
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD
output_file: e2r_stock_web_v12_residual_round_R13_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
source_rows_reused_for_r13_holdout: 8
new_independent_case_count_for_r13_aggregate: 8
```

This loop adds **8** R13 cross-audit independent holdout cases, **4** counterexamples, and **6** residual errors for `R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`.

R13 is a checkpoint, not a disguised sector round. The object is not consumer, bio, battery, construction, or policy research. The object is the red-team guard itself: when MFE looks good but MAE is violent, when Green is technically plausible but the path is unstable, and when price/event evidence tries to impersonate durable revision evidence.

## 1. Current Calibrated Profile Assumption

`P0 = e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes remain infrastructure, not new discoveries:

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

This R13 loop stress-tests those axes against a narrower residual: **high-MAE paths can still produce high MFE, so the model needs a separate cross-archetype size/Green cap rather than a simple success/failure label.**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R13 |
| scheduled_loop | 11 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL |
| fine_archetype_id | CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD |
| loop_objective | holdout_validation; counterexample_mining; yellow_threshold_stress_test; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R13 is valid only because it uses `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` and a cross-archetype canonical scope. It does not produce an ordinary R5/R6/R7/R8 sector-specific file.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent artifact reviewed: `reports/e2r_calibration/by_round/R13.md`. Existing R13 calibration coverage is already broad, with 111 representative triggers, 30 unique cases, and a mix of Stage2, Stage3, Stage4B, and Stage4C rows. Therefore this file does **not** repeat the previous R13 Loop 10 4B/4C red-team logic. It creates a new R13 Loop 11 guard focused on cross-sector high-MAE/false-Green paths.

Schedule resolution from local v12 artifacts:

```text
loop_11 R1 through R12 present = true
previous completed round = R12 / loop 11
scheduled_round = R13
scheduled_loop = 11
computed_next_round = R1
computed_next_loop = 12
```

Duplicate policy:

```text
source rows reused only as = R13 holdout validation / cross-archetype red-team
same symbol + trigger date reuse = allowed only because source canonical is remapped into R13 guardrail scope
independent_evidence_weight = 0.5 per source case
new sector-specific evidence = false
R13 aggregate evidence = true
```

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The stock-web schema defines tradable columns as `d,o,h,l,c,v,a,mc,s,m`. The MFE/MAE formulas use tradable rows only. Raw shards remain diagnostic only and are not used for weight calibration.

## 5. Historical Eligibility Gate

All representative R13 holdout rows pass the historical gate at their original source-row level:

| gate | status |
|---|---|
| trigger_date is historical | pass |
| entry row exists in stock-web tradable shard | pass |
| at least 180 forward tradable rows available | pass |
| MFE/MAE 30D, 90D, 180D computed | pass |
| price basis | tradable_raw |
| price adjustment status | raw_unadjusted_marcap |
| contaminated 180D corporate-action window | no selected source row is marked contaminated |

The R13 layer does not create fresh price rows. It remaps already stock-web-validated Loop 11 rows into a cross-archetype holdout ledger.

## 6. Canonical Archetype Compression Map

| R13 guard bucket | Source canonical archetypes compressed | Mechanism | R13 interpretation |
|---|---|---|---|
| High-MAE structural success | C17, C20, C31 | MFE can be high while path risk is also high | Stage2/Yellow allowed; Green/size capped until confirmation |
| False Green / label mimicry | C17, C23 | cycle or binary event label looks like evidence | reject Green unless durable bridge exists |
| Price-only or event spike | C30, C31 | large MFE comes from tape/event premium, not cash-flow bridge | 4B/watch overlay, not positive promotion |
| Thesis break after rerating | C14 | price peak turns into order/demand quality break | 4B-to-4C route must be faster |

## 7. Case Selection Summary

|case_id|src_round|symbol|company|src_canonical|case_type|balance|trigger_type|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|R13 verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L11_HIGHMAE_X01_011780_C17|R4|011780|금호석유화학|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|high_mae_success|positive|Stage2-Actionable|2020-11-06|153500|91.21|-19.22|94.46|-19.22|current_profile_correct_but_size_cap_needed|
|R13L11_HIGHMAE_X02_218150_C31|R12|218150|미래생명자원|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|high_mae_success|positive|Stage2-Actionable|2022-02-24|8090|59.46|-19.04|59.46|-42.71|current_profile_correct_but_size_cap_needed|
|R13L11_HIGHMAE_X03_192820_C20|R5|192820|코스맥스|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|high_mae_success|positive|Stage2-Actionable|2024-05-14|160500|29.6|-27.7|29.6|-27.7|current_profile_too_early|
|R13L11_HIGHMAE_X04_028300_C23|R7|028300|HLB|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|false_positive_green|counterexample|Stage3-Green-candidate-false-positive|2024-05-16|95800|11.59|-52.87|11.59|-52.87|current_profile_false_positive|
|R13L11_HIGHMAE_X05_006650_C17|R4|006650|대한유화|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|false_positive_green|counterexample|Stage3-Green|2021-02-16|393500|3.05|-35.32|3.05|-53.37|current_profile_false_positive|
|R13L11_HIGHMAE_X06_066970_C14|R3|066970|엘앤에프|C14_EV_DEMAND_SLOWDOWN_4B_4C|4C_late|counterexample|Stage4B_to_4C_watch|2023-07-26|263000|20.91|-51.37|20.91|-51.37|current_profile_4C_too_late|
|R13L11_HIGHMAE_X07_039610_C31|R11|039610|화성밸브|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|stage2_watch_success_not_green|positive|Stage2_event_premium_risk_watch|2024-06-04|8630|77.52|-21.21|78.68|-21.21|current_profile_too_late_for_watch_but_not_green|
|R13L11_HIGHMAE_X08_003070_C30|R10|003070|코오롱글로벌|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|4B_too_late|counterexample|Stage2-Actionable|2024-01-25|9130|76.45|-10.51|76.45|-10.51|current_profile_4B_too_late|


## 8. Positive vs Counterexample Balance

| count field | value |
|---|---:|
| positive_case_count | 4 |
| counterexample_count | 4 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 8 |
| calibration_usable_trigger_count | 8 |
| new_independent_case_count_for_R13_aggregate | 8 |
| source_rows_reused_for_R13_holdout | 8 |
| current_profile_error_count | 6 |

The positive rows are positive **for the guardrail**, not investment recommendations. They show where Stage2 or Yellow can still be useful despite high MAE. The counterexample rows show why Green or full-size promotion becomes dangerous when the evidence bridge is missing.

## 9. Evidence Source Map

|R13 bucket|source cases|mechanism|guard decision|
|---|---|---|---|
|structural_success_with_high_MAE_size_cap|011780, 218150, 192820|Thesis can be right, yet the path has deep MAE before or after MFE.|Allow Stage2/Yellow, cap Green/size until bridge confirmation.|
|binary_event_false_green_high_MAE|028300|Binary approval/regulatory setup can collapse faster than revision evidence can catch up.|Block Green; route to hard event-risk or 4C watch.|
|commodity_spread_false_green_high_MAE|006650|Cycle label without durable spread/revision bridge is not enough.|Downgrade to watch/reject unless spread bridge is live.|
|rerating_failed_then_order_quality_break|066970|Price-only rerating peak turns into demand/order-quality break.|Treat as 4B/4C overlay, not positive re-entry.|
|peripheral_policy_success_not_green|039610|Peripheral policy names can have real MFE but weak direct cash-flow route.|Stage2-event watch only; no Green.|
|PF_recovery_price_only_spike_4B_overlay|003070|Balance-sheet sector rebound can spike without repaired PF/margin evidence.|4B overlay near spike; block Green.|


## 10. Price Data Source Map

|R13 trigger_id|source_trigger_id|symbol|profile_path|price_shard_path|price_basis|corporate_action_window_status|
|---|---|---|---|---|---|---|
|R13L11_HIGHMAE_X01_011780_STAGE2A_20201106|R4L11_C17_KUMHO_20201106_S2A|011780|atlas/symbol_profiles/011/011780.json|atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv|tradable_raw|clean_180D_window|
|R13L11_HIGHMAE_X02_218150_STAGE2A_20220224|R12L11_C31_218150_STAGE2A_20220224|218150|atlas/symbol_profiles/218/218150.json|atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv|tradable_raw|clean_180D_window|
|R13L11_HIGHMAE_X03_192820_STAGE2A_20240514|R5L11-C20-COSMAX-STAGE2A-20240514|192820|atlas/symbol_profiles/192/192820.json|atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv|tradable_raw|clean_180D_window|
|R13L11_HIGHMAE_X04_028300_FALSEGREEN_20240516|R7L11-C23-028300-T1-pre-pdufa-false-green|028300|atlas/symbol_profiles/028/028300.json|atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv|tradable_raw|clean_180D_window|
|R13L11_HIGHMAE_X05_006650_FALSEGREEN_20210216|R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE|006650|atlas/symbol_profiles/006/006650.json|atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv|tradable_raw|clean_180D_window|
|R13L11_HIGHMAE_X06_066970_4B4C_20230726|R3L11-C14-LNF-4C-20230726|066970|atlas/symbol_profiles/066/066970.json|atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv|tradable_raw|clean_180D_window|
|R13L11_HIGHMAE_X07_039610_STAGE2WATCH_20240604|TR_R11L11_HSVALVE_STAGE2_2024_06_03|039610|atlas/symbol_profiles/039/039610.json|atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv|tradable_raw|clean_180D_window|
|R13L11_HIGHMAE_X08_003070_STAGE2A_20240125|R10L11-C30-KOLON-STAGE2-20240125|003070|atlas/symbol_profiles/003/003070.json|atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv|tradable_raw|clean_180D_window|


## 11. Case-by-Case Trigger Grid

|case_id|src_round|symbol|company|src_canonical|case_type|balance|trigger_type|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|R13 verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L11_HIGHMAE_X01_011780_C17|R4|011780|금호석유화학|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|high_mae_success|positive|Stage2-Actionable|2020-11-06|153500|91.21|-19.22|94.46|-19.22|current_profile_correct_but_size_cap_needed|
|R13L11_HIGHMAE_X02_218150_C31|R12|218150|미래생명자원|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|high_mae_success|positive|Stage2-Actionable|2022-02-24|8090|59.46|-19.04|59.46|-42.71|current_profile_correct_but_size_cap_needed|
|R13L11_HIGHMAE_X03_192820_C20|R5|192820|코스맥스|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|high_mae_success|positive|Stage2-Actionable|2024-05-14|160500|29.6|-27.7|29.6|-27.7|current_profile_too_early|
|R13L11_HIGHMAE_X04_028300_C23|R7|028300|HLB|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|false_positive_green|counterexample|Stage3-Green-candidate-false-positive|2024-05-16|95800|11.59|-52.87|11.59|-52.87|current_profile_false_positive|
|R13L11_HIGHMAE_X05_006650_C17|R4|006650|대한유화|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|false_positive_green|counterexample|Stage3-Green|2021-02-16|393500|3.05|-35.32|3.05|-53.37|current_profile_false_positive|
|R13L11_HIGHMAE_X06_066970_C14|R3|066970|엘앤에프|C14_EV_DEMAND_SLOWDOWN_4B_4C|4C_late|counterexample|Stage4B_to_4C_watch|2023-07-26|263000|20.91|-51.37|20.91|-51.37|current_profile_4C_too_late|
|R13L11_HIGHMAE_X07_039610_C31|R11|039610|화성밸브|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|stage2_watch_success_not_green|positive|Stage2_event_premium_risk_watch|2024-06-04|8630|77.52|-21.21|78.68|-21.21|current_profile_too_late_for_watch_but_not_green|
|R13L11_HIGHMAE_X08_003070_C30|R10|003070|코오롱글로벌|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|4B_too_late|counterexample|Stage2-Actionable|2024-01-25|9130|76.45|-10.51|76.45|-10.51|current_profile_4B_too_late|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|src_canonical|symbol|entry|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|drawdown_after_peak|R13 bucket|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L11_HIGHMAE_X01_011780_STAGE2A_20201106|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|2020-11-06 @ 153500|1.95|-19.22|91.21|-19.22|94.46|-19.22|2021-05-06|298500|-32.16|structural_success_with_high_MAE_size_cap|
|R13L11_HIGHMAE_X02_218150_STAGE2A_20220224|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|218150|2022-02-24 @ 8090|53.28|-19.04|59.46|-19.04|59.46|-42.71|2022-04-19|12900|-64.07|event_success_with_180D_drawdown_cap|
|R13L11_HIGHMAE_X03_192820_STAGE2A_20240514|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|192820|2024-05-14 @ 160500|29.60|-3.90|29.60|-27.70|29.60|-27.70|2024-06-14|208000|-44.20|consumer_export_success_but_green_too_early|
|R13L11_HIGHMAE_X04_028300_FALSEGREEN_20240516|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|028300|2024-05-16 @ 95800|11.59|-52.87|11.59|-52.87|11.59|-52.87|2024-05-16|106900|-57.76|binary_event_false_green_high_MAE|
|R13L11_HIGHMAE_X05_006650_FALSEGREEN_20210216|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|006650|2021-02-16 @ 393500|3.05|-25.79|3.05|-35.32|3.05|-53.37|2021-02-17|405500|-54.75|commodity_spread_false_green_high_MAE|
|R13L11_HIGHMAE_X06_066970_4B4C_20230726|C14_EV_DEMAND_SLOWDOWN_4B_4C|066970|2023-07-26 @ 263000|20.91|-24.68|20.91|-51.37|20.91|-51.37|2023-07-26|318000|-59.78|rerating_failed_then_order_quality_break|
|R13L11_HIGHMAE_X07_039610_STAGE2WATCH_20240604|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|039610|2024-06-04 @ 8630|28.39|-21.21|77.52|-21.21|78.68|-21.21|2024-08-23|15420|-46.76|peripheral_policy_success_not_green|
|R13L11_HIGHMAE_X08_003070_STAGE2A_20240125|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|003070|2024-01-25 @ 9130|17.20|-3.61|76.45|-10.51|76.45|-10.51|2024-06-21|16110|-47.24|PF_recovery_price_only_spike_4B_overlay|


## 13. Current Calibrated Profile Stress Test

| Required question | R13 answer |
|---|---|
| How would current profile judge these cases? | It catches the clean winners and some existing 4B/4C guards, but still leaves 6/8 residual errors around high-MAE success, false Green, late 4B, and late 4C. |
| Did that judgment match actual MFE/MAE? | Partially. Average MFE_90D is 46.22%, but average MAE_90D is -29.65%, so outcome success alone hides path risk. |
| Was Stage2 bonus too high? | Not globally. It is useful for structural winners, but should be size-capped when MAE guard or event-only evidence is active. |
| Was Yellow 75 too low/high? | Kept. R13 recommends an overlay, not a threshold rewrite. |
| Was Green 87 / revision 55 too strict? | Kept and effectively strengthened: high-MAE or binary event rows should need stronger confirmation before Green. |
| Was price-only blowoff guard appropriate? | Yes. R13 strengthens its use as a risk overlay rather than a positive-stage signal. |
| Was full 4B non-price requirement appropriate? | Kept. Price-only local peaks remain watch/overlay unless valuation, positioning, overhang, revision slowdown, or thesis-break evidence appears. |
| Was hard 4C routing too late or too harsh? | Too late in selected residuals; hard 4C should dominate when demand/order/regulatory/legal evidence breaks. |

Conclusion set:

```text
current_profile_correct_but_size_cap_needed = 2
current_profile_too_early = 1
current_profile_false_positive = 2
current_profile_4B_too_late = 1
current_profile_4C_too_late = 1
current_profile_too_late_for_watch_but_not_green = 1
```

## 14. Stage2 / Yellow / Green Comparison

R13 does not repeat the generic claim that Stage2 is earlier than Green. The narrower finding is this:

```text
If MFE is high but MAE_90D <= -20% or MAE_180D <= -35%, then Stage2/Yellow may remain valid, but Stage3-Green or full-size promotion should require fresh confirmation from the source canonical bridge.
```

| path type | Stage2/Yellow treatment | Green treatment | R13 reason |
|---|---|---|---|
| structural high-MAE success | keep, but size-cap | require confirmation | thesis can be right but path is hazardous |
| false Green high-MAE | reject or watch | block | label or event is not durable evidence |
| event/watch success | allow watch/overlay | block Green | price MFE does not prove cash-flow route |
| 4B-to-4C break | route risk faster | no positive relabel | thesis break dominates rebound optics |

## 15. 4B Local vs Full-window Timing Audit

| source bucket | local-vs-full issue | R13 verdict |
|---|---|---|
| 003070 PF recovery spike | local spike generated large MFE but lacked repaired PF/margin bridge | price-only local 4B should fire as overlay, not Green |
| 039610 peripheral policy event | policy/event MFE occurred but direct revenue bridge remained weak | Stage2-event watch only |
| 066970 EV material rerating failure | price peak preceded order-quality/demand break | 4B-to-4C route should be faster |
| 218150 food/feed shock | full-window drawdown after event winner was severe | size-cap even when Stage2 is correct |

No row in this R13 file treats price-only local peak as a full positive 4B. Price-only rows can lower exposure or block Green; they cannot promote Stage2/3.

## 16. 4C Protection Audit

| symbol | source canonical | 4C label | R13 read |
|---|---|---|---|
| 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | hard_4c_late | rerating failed and demand/order quality break should override prior Stage3 optimism |
| 028300 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | hard_event_false_green | binary regulatory rejection/CRL-style event should block Green even before ordinary financial confirmation exists |
| 003070 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | thesis_break_watch_only | PF recovery spike requires balance-sheet bridge; otherwise risk overlay dominates |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

R13 is not a sector round. The row set spans materials, consumer, bio, battery, construction, policy-event, and PF-sensitive cases. The rule is therefore not proposed as a new R4/R5/R7/R10/R12 sector rule.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = R13 cross-archetype guardrail
new_axis_proposed = R13_high_MAE_success_size_cap
```

Rule candidate:

```text
If MAE_90D <= -20% or MAE_180D <= -35% in a historically similar trigger family, do not let high MFE alone upgrade a row to Stage3-Green or full positive sizing. Keep the row at Stage2/Yellow/watch unless the source canonical bridge is hard-confirmed: margin/revision for commodity and consumer, order-quality/demand for battery/materials, regulatory/commercialization for bio, balance-sheet bridge for construction/PF, direct cash-flow route for policy/event cases.
```

This is shadow-only. It should enter the batch ledger as a cross-archetype residual rule candidate, not as production scoring.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|current profile; no additional high-MAE cap|none|8|46.22|-29.65|46.77|-34.87|4/8|2|2|0.42|mixed; catches structural winners but leaves false Green/high-MAE overpromotion|
|P0b|e2r_2_0_baseline_reference|pre-stock-web baseline proxy|looser Stage2/Green and weaker 4B/4C guards|8|46.22|-29.65|46.77|-34.87|5/8|3|3|0.55|worse; would promote too many theme/event rows|
|P1|R13_cross_high_MAE_size_cap_profile|cross-archetype MAE cap before Green/size-up|new high_MAE_size_cap_score; no threshold change|8|46.22|-29.65|46.77|-34.87|2/8|1|1|0.39|improved; keeps winners as Stage2/Yellow while blocking false Green|
|P2|canonical_archetype_bridge_profile|requires each source canonical to show its own bridge before Green|margin/revision/customer/regulatory bridge confirmation|8|46.22|-29.65|46.77|-34.87|2/8|1|1|0.39|improved; same direction as P1 but encoded per canonical|
|P3|counterexample_guard_profile|blocks price/event false Green and hard-routes 4C|strengthen price-only and hard-4C axes only|8|46.22|-29.65|46.77|-34.87|1/8|1|0|0.35|best for red-team guard, but may under-credit high-MFE winners|


## 20. Score-Return Alignment Matrix

| alignment bucket | cases | observed price path | score implication |
|---|---|---|---|
| high_MFE_high_MAE_success | 011780, 218150, 192820 | high MFE but MAE from -19% to -43% | keep Stage2/Yellow; cap Green/size |
| false_green_high_MAE | 028300, 006650 | low MFE and MAE below -50% | reject Green / hard event guard |
| late_4B_or_4C | 066970, 003070 | post-peak collapse after local spike | risk overlay before damage is obvious |
| event_watch_success_not_green | 039610 | high MFE but weak direct bridge and -21% MAE | watch-only, not Green |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD|4|4|2|2|8|8|8|8|6|false|true|R13 loop11 high-MAE guardrail now has 8 cross-sector holdout rows; still needs batch aggregation before production promotion.|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 8
reused_case_ids: R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020, R12L11_C31_218150_FEED, R5L11-C20-COSMAX-202405, R7L11-C23-028300-hlb-crl-pdufa, R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021, R3L11-C14-LNF-20230726, R11L11_C31_HSVALVE_PERIPHERAL_EQUIPMENT_OPTIONALITY, R10L11-C30-KOLON-20240125
new_symbol_count: 8
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: current_profile_too_early; current_profile_false_positive; current_profile_4B_too_late; current_profile_4C_too_late; high_MAE_success_size_cap_needed
new_axis_proposed: R13_high_MAE_success_size_cap
existing_axis_strengthened: stage3_green_revision_min; stage3_cross_evidence_green_buffer; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 8 new R13 holdout cases, 4 counterexamples, and 6 residual errors for `R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`.

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Actual stock-web OHLC-derived MFE/MAE fields from Loop 11 source trigger rows.
- R13 schedule and round-sector consistency.
- Cross-archetype residual pattern over 8 symbols and 7 source canonical archetypes.
- Positive/counterexample balance for high-MAE guardrail.
```

Not validated:

```text
- No live candidate search.
- No current stock recommendation.
- No stock_agent source-code inspection.
- No production scoring change.
- No broker, auto-trading, or watchlist output.
- No new external price route exploration.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_high_MAE_success_size_cap,cross_archetype_shadow,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,1,+1,"When MAE_90D <= -20% or MAE_180D <= -35%, require post-entry confirmation or keep Stage2/Yellow size-capped unless margin/revision/customer/regulatory bridge is already hard evidence.","Reduces false Green/high-MAE overpromotion across materials, battery, bio, consumer, construction, policy-event and PF cases while preserving Stage2 watch for high-MFE winners.","R13L11_HIGHMAE_X01_011780_STAGE2A_20201106|R13L11_HIGHMAE_X02_218150_STAGE2A_20220224|R13L11_HIGHMAE_X03_192820_STAGE2A_20240514|R13L11_HIGHMAE_X04_028300_FALSEGREEN_20240516|R13L11_HIGHMAE_X05_006650_FALSEGREEN_20210216|R13L11_HIGHMAE_X06_066970_4B4C_20230726|R13L11_HIGHMAE_X07_039610_STAGE2WATCH_20240604|R13L11_HIGHMAE_X08_003070_STAGE2A_20240125",8,8,4,medium,shadow_only,"R13 checkpoint only; not production; requires batch-ledger aggregation before promotion."
```

Interpretation:

```text
proposal_type = shadow_only
confidence = medium
promotion_condition = batch aggregation confirms similar high-MAE residual across later R13 loops without killing clean low-MAE structural winners
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13L11_HIGHMAE_X01_011780_C17","source_case_id":"R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020","source_trigger_id":"R4L11_C17_KUMHO_20201106_S2A","symbol":"011780","company_name":"금호석유화학","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R13L11_HIGHMAE_X01_011780_STAGE2A_20201106","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"R13 holdout validation: source Loop 11 trigger reused only for cross-archetype high-MAE guardrail; not counted as new sector-specific evidence.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"structural_success_with_high_MAE_size_cap","current_profile_verdict":"current_profile_correct_but_size_cap_needed","price_source":"Songdaiki/stock-web","notes":"Spread thesis eventually worked, but -19% 90D MAE means R13 should separate thesis-valid Stage2 from unrestricted Green sizing."}
{"row_type":"trigger","trigger_id":"R13L11_HIGHMAE_X01_011780_STAGE2A_20201106","case_id":"R13L11_HIGHMAE_X01_011780_C17","symbol":"011780","company_name":"금호석유화학","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","sector":"cross_archetype_redteam_checkpoint","primary_archetype":"R13 cross-archetype high-MAE / false-Green / size-cap guardrail","loop_objective":"holdout_validation|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-11-06","entry_date":"2020-11-06","entry_price":153500,"evidence_available_at_that_date":"R13 holdout reuse of source evidence: Q3/early-Q4 2020 specialty synthetic-rubber/NBR-latex margin bridge became public enough to distinguish from generic chemical beta; customer-demand route tied to glove/medical demand, not just commodity rebound.","evidence_source":"source loop11 row R4L11_C17_KUMHO_20201106_S2A from R4/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD; stock-web OHLC path preserved","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.95,"MFE_90D_pct":91.21,"MFE_180D_pct":94.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.22,"MAE_90D_pct":-19.22,"MAE_180D_pct":-19.22,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-32.16,"green_lateness_ratio":"not_applicable: representative Stage2 trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_with_high_MAE_size_cap","current_profile_verdict":"current_profile_correct_but_size_cap_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L11:011780:2020-11-06:153500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"R13 cross-archetype holdout validation; source row reused with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_trigger_id":"R4L11_C17_KUMHO_20201106_S2A","source_case_id":"R4L11_C17_KUMHO_NBR_LATEX_SPREAD_2020","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_R13_high_mae_guard","case_id":"R13L11_HIGHMAE_X01_011780_C17","trigger_id":"R13L11_HIGHMAE_X01_011780_STAGE2A_20201106","symbol":"011780","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable_or_Stage3-Yellow_under_P0","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":0},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable_Size_Capped_until_confirmation","changed_components":["high_mae_size_cap_score","execution_risk_score","valuation_repricing_score","revision_score","margin_bridge_score"],"component_delta_explanation":"R13 high-MAE guard caps Green/size when MAE is severe or when MFE is mostly price/event rerating without durable margin, revision, contract, regulatory, or customer conversion bridge.","MFE_90D_pct":91.21,"MAE_90D_pct":-19.22,"score_return_alignment_label":"improved_cross_archetype_high_MAE_alignment","current_profile_verdict":"current_profile_correct_but_size_cap_needed"}
{"row_type":"case","case_id":"R13L11_HIGHMAE_X02_218150_C31","source_case_id":"R12L11_C31_218150_FEED","source_trigger_id":"R12L11_C31_218150_STAGE2A_20220224","symbol":"218150","company_name":"미래생명자원","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R13L11_HIGHMAE_X02_218150_STAGE2A_20220224","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"R13 holdout validation: source Loop 11 trigger reused only for cross-archetype high-MAE guardrail; not counted as new sector-specific evidence.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"event_success_with_180D_drawdown_cap","current_profile_verdict":"current_profile_correct_but_size_cap_needed","price_source":"Songdaiki/stock-web","notes":"Food/feed shock produced large upside but also a -42.7% 180D adverse path, so event Stage2 should not automatically size like clean Green."}
{"row_type":"trigger","trigger_id":"R13L11_HIGHMAE_X02_218150_STAGE2A_20220224","case_id":"R13L11_HIGHMAE_X02_218150_C31","symbol":"218150","company_name":"미래생명자원","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","sector":"cross_archetype_redteam_checkpoint","primary_archetype":"R13 cross-archetype high-MAE / false-Green / size-cap guardrail","loop_objective":"holdout_validation|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-02-24","evidence_available_at_that_date":"R13 holdout reuse of source evidence: Feed/additive supply-security route moved with the grain shock, but high MAE shows C31 needs risk sizing and not a blind Green promotion.","evidence_source":"source loop11 row R12L11_C31_218150_STAGE2A_20220224 from R12/C31_POLICY_SUBSIDY_LEGISLATION_EVENT; stock-web OHLC path preserved","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv","profile_path":"atlas/symbol_profiles/218/218150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-02-24","entry_price":8090,"MFE_30D_pct":53.28,"MFE_90D_pct":59.46,"MFE_180D_pct":59.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.04,"MAE_90D_pct":-19.04,"MAE_180D_pct":-42.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-19","peak_price":12900,"drawdown_after_peak_pct":-64.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"event_success_with_180D_drawdown_cap","current_profile_verdict":"current_profile_correct_but_size_cap_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L11:218150:2022-02-24:8090","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"R13 cross-archetype holdout validation; source row reused with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_trigger_id":"R12L11_C31_218150_STAGE2A_20220224","source_case_id":"R12L11_C31_218150_FEED","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_R13_high_mae_guard","case_id":"R13L11_HIGHMAE_X02_218150_C31","trigger_id":"R13L11_HIGHMAE_X02_218150_STAGE2A_20220224","symbol":"218150","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":85},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable_or_Stage3-Yellow_under_P0","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":45,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":85},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable_Size_Capped_until_confirmation","changed_components":["high_mae_size_cap_score","execution_risk_score","valuation_repricing_score","revision_score","margin_bridge_score"],"component_delta_explanation":"R13 high-MAE guard caps Green/size when MAE is severe or when MFE is mostly price/event rerating without durable margin, revision, contract, regulatory, or customer conversion bridge.","MFE_90D_pct":59.46,"MAE_90D_pct":-19.04,"score_return_alignment_label":"improved_cross_archetype_high_MAE_alignment","current_profile_verdict":"current_profile_correct_but_size_cap_needed"}
{"row_type":"case","case_id":"R13L11_HIGHMAE_X03_192820_C20","source_case_id":"R5L11-C20-COSMAX-202405","source_trigger_id":"R5L11-C20-COSMAX-STAGE2A-20240514","symbol":"192820","company_name":"코스맥스","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R13L11_HIGHMAE_X03_192820_STAGE2A_20240514","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"R13 holdout validation: source Loop 11 trigger reused only for cross-archetype high-MAE guardrail; not counted as new sector-specific evidence.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"consumer_export_success_but_green_too_early","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"K-beauty export evidence was real, but -27.7% 90D MAE supports a cross-archetype size/confirmation guard after sharp Stage2 entries."}
{"trigger_id":"R13L11_HIGHMAE_X03_192820_STAGE2A_20240514","case_id":"R13L11_HIGHMAE_X03_192820_C20","symbol":"192820","company_name":"코스맥스","sector":"cross_archetype_redteam_checkpoint","primary_archetype":"R13 cross-archetype high-MAE / false-Green / size-cap guardrail","loop_objective":"holdout_validation|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-13","entry_date":"2024-05-14","entry_price":160500,"evidence_available_at_that_date":"R13 holdout reuse of source evidence: 1Q24 earnings/revision evidence existed, but 180D path later exposed high-MAE sensitivity; treat as positive with guard, not clean Green promotion.","evidence_source":"source loop11 row R5L11-C20-COSMAX-STAGE2A-20240514 from R5/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION; stock-web OHLC path preserved","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","profile_path":"atlas/symbol_profiles/192/192820.json","MFE_30D_pct":29.6,"MFE_90D_pct":29.6,"MFE_180D_pct":29.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.9,"MAE_90D_pct":-27.7,"MAE_180D_pct":-27.7,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":208000,"drawdown_after_peak_pct":-44.2,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"consumer_export_success_but_green_too_early","current_profile_verdict":"current_profile_too_early","same_entry_group_id":"R13L11:192820:2024-05-14:160500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"R13 cross-archetype holdout validation; source row reused with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"row_type":"trigger","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","source_trigger_id":"R5L11-C20-COSMAX-STAGE2A-20240514","source_case_id":"R5L11-C20-COSMAX-202405","source_canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_R13_high_mae_guard","case_id":"R13L11_HIGHMAE_X03_192820_C20","trigger_id":"R13L11_HIGHMAE_X03_192820_STAGE2A_20240514","symbol":"192820","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":70},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable_or_Stage3-Yellow_under_P0","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":45,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":70},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable_Size_Capped_until_confirmation","changed_components":["high_mae_size_cap_score","execution_risk_score","valuation_repricing_score","revision_score","margin_bridge_score"],"component_delta_explanation":"R13 high-MAE guard caps Green/size when MAE is severe or when MFE is mostly price/event rerating without durable margin, revision, contract, regulatory, or customer conversion bridge.","MFE_90D_pct":29.6,"MAE_90D_pct":-27.7,"score_return_alignment_label":"improved_cross_archetype_high_MAE_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"case","case_id":"R13L11_HIGHMAE_X04_028300_C23","source_case_id":"R7L11-C23-028300-hlb-crl-pdufa","source_trigger_id":"R7L11-C23-028300-T1-pre-pdufa-false-green","symbol":"028300","company_name":"HLB","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13L11_HIGHMAE_X04_028300_FALSEGREEN_20240516","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"R13 holdout validation: source Loop 11 trigger reused only for cross-archetype high-MAE guardrail; not counted as new sector-specific evidence.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"binary_event_false_green_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Binary regulatory/event risk produced -52.9% 90D MAE; this is the archetypal Green-block case even when pre-event narrative is strong."}
{"trigger_id":"R13L11_HIGHMAE_X04_028300_FALSEGREEN_20240516","case_id":"R13L11_HIGHMAE_X04_028300_C23","symbol":"028300","company_name":"HLB","sector":"cross_archetype_redteam_checkpoint","primary_archetype":"R13 cross-archetype high-MAE / false-Green / size-cap guardrail","trigger_type":"Stage3-Green-candidate-false-positive","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"evidence_available_at_that_date":"R13 holdout reuse of source evidence: Pre-decision PDUFA anticipation and price strength existed, but actual approval evidence was absent; this is the canonical C23 false-positive pattern.","evidence_source":"source loop11 row R7L11-C23-028300-T1-pre-pdufa-false-green from R7/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION; stock-web OHLC path preserved","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"MFE_30D_pct":11.59,"MFE_90D_pct":11.59,"MFE_180D_pct":11.59,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"pre_event_price_only_not_full_4B","four_b_evidence_type":["price_only","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"binary_event_false_green_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_block_reasons":[],"same_entry_group_id":"R13L11:028300:2024-05-16:95800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"R13 cross-archetype holdout validation; source row reused with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","row_type":"trigger","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","loop_objective":"holdout_validation|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","source_trigger_id":"R7L11-C23-028300-T1-pre-pdufa-false-green","source_case_id":"R7L11-C23-028300-hlb-crl-pdufa","source_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_R13_high_mae_guard","case_id":"R13L11_HIGHMAE_X04_028300_C23","trigger_id":"R13L11_HIGHMAE_X04_028300_FALSEGREEN_20240516","symbol":"028300","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":35,"relative_strength_score":65,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":55,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":85},"weighted_score_before":72,"stage_label_before":"Stage2-Watch_or_Event_Premium_under_P0","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":65,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":82,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":85,"high_mae_size_cap_score":85},"weighted_score_after":54,"stage_label_after":"Rejected_or_Stage4C_Hard_Break","changed_components":["high_mae_size_cap_score","execution_risk_score","valuation_repricing_score","revision_score","margin_bridge_score"],"component_delta_explanation":"R13 high-MAE guard caps Green/size when MAE is severe or when MFE is mostly price/event rerating without durable margin, revision, contract, regulatory, or customer conversion bridge.","MFE_90D_pct":11.59,"MAE_90D_pct":-52.87,"score_return_alignment_label":"improved_cross_archetype_high_MAE_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"R13L11_HIGHMAE_X05_006650_C17","source_case_id":"R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021","source_trigger_id":"R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE","symbol":"006650","company_name":"대한유화","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13L11_HIGHMAE_X05_006650_FALSEGREEN_20210216","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"R13 holdout validation: source Loop 11 trigger reused only for cross-archetype high-MAE guardrail; not counted as new sector-specific evidence.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"commodity_spread_false_green_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Commodity spread label looked plausible, but low MFE and -53.4% 180D MAE show why Green needs spread/revision bridge, not cycle label."}
{"row_type":"trigger","trigger_id":"R13L11_HIGHMAE_X05_006650_FALSEGREEN_20210216","case_id":"R13L11_HIGHMAE_X05_006650_C17","symbol":"006650","company_name":"대한유화","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","sector":"cross_archetype_redteam_checkpoint","primary_archetype":"R13 cross-archetype high-MAE / false-Green / size-cap guardrail","loop_objective":"holdout_validation|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage3-Green","trigger_date":"2021-02-16","entry_date":"2021-02-16","entry_price":393500,"evidence_available_at_that_date":"R13 holdout reuse of source evidence: NCC spread recovery plus abrupt price/volume looked like Green, but the company had a commodity-only spread exposure without durable specialty-margin or customer-quality evidence; the entry was effectively at local spread-cycle exhaustion.","evidence_source":"source loop11 row R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE from R4/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD; stock-web OHLC path preserved","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.05,"MFE_90D_pct":3.05,"MFE_180D_pct":3.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.79,"MAE_90D_pct":-35.32,"MAE_180D_pct":-53.37,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-17","peak_price":405500,"drawdown_after_peak_pct":-54.75,"green_lateness_ratio":1.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_peak_not_full_4B_without_spread_slowdown","four_b_evidence_type":["price_only_local_peak","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_if_waiting_for_explicit_default","trigger_outcome_label":"commodity_spread_false_green_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L11:006650:2021-02-16:393500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"R13 cross-archetype holdout validation; source row reused with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_trigger_id":"R4L11_C17_DAEHAN_20210216_GREEN_FALSE_POSITIVE","source_case_id":"R4L11_C17_DAEHAN_NCC_SPREAD_FALSE_GREEN_2021","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_R13_high_mae_guard","case_id":"R13L11_HIGHMAE_X05_006650_C17","trigger_id":"R13L11_HIGHMAE_X05_006650_FALSEGREEN_20210216","symbol":"006650","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":35,"relative_strength_score":65,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":55,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":85},"weighted_score_before":72,"stage_label_before":"Stage2-Watch_or_Event_Premium_under_P0","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":65,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":82,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":85,"high_mae_size_cap_score":85},"weighted_score_after":54,"stage_label_after":"Rejected_or_Stage4C_Hard_Break","changed_components":["high_mae_size_cap_score","execution_risk_score","valuation_repricing_score","revision_score","margin_bridge_score"],"component_delta_explanation":"R13 high-MAE guard caps Green/size when MAE is severe or when MFE is mostly price/event rerating without durable margin, revision, contract, regulatory, or customer conversion bridge.","MFE_90D_pct":3.05,"MAE_90D_pct":-35.32,"score_return_alignment_label":"improved_cross_archetype_high_MAE_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"R13L11_HIGHMAE_X06_066970_C14","source_case_id":"R3L11-C14-LNF-20230726","source_trigger_id":"R3L11-C14-LNF-4C-20230726","symbol":"066970","company_name":"엘앤에프","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"R13L11_HIGHMAE_X06_066970_4B4C_20230726","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"R13 holdout validation: source Loop 11 trigger reused only for cross-archetype high-MAE guardrail; not counted as new sector-specific evidence.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"rerating_failed_then_order_quality_break","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"EV material rerating failed after price-only peak; -51% MAE shows why demand/order-quality break must route to 4C faster."}
{"row_type":"trigger","trigger_id":"R13L11_HIGHMAE_X06_066970_4B4C_20230726","case_id":"R13L11_HIGHMAE_X06_066970_C14","symbol":"066970","company_name":"엘앤에프","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","sector":"cross_archetype_redteam_checkpoint","primary_archetype":"R13 cross-archetype high-MAE / false-Green / size-cap guardrail","loop_objective":"holdout_validation|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B_to_4C_watch","trigger_date":"2023-07-26","evidence_available_at_that_date":"R13 holdout reuse of source evidence: Theme squeeze exhausted while customer-concentration and cathode ASP sensitivity were already visible; later price path confirms this should not be treated as durable Stage3-Green without order-quality conversion.","evidence_source":"source loop11 row R3L11-C14-LNF-4C-20230726 from R3/C14_EV_DEMAND_SLOWDOWN_4B_4C; stock-web OHLC path preserved","stage2_evidence_fields":["relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":263000,"MFE_30D_pct":20.91,"MFE_90D_pct":20.91,"MFE_180D_pct":20.91,"MFE_1Y_pct":20.91,"MFE_2Y_pct":null,"MAE_30D_pct":-24.68,"MAE_90D_pct":-51.37,"MAE_180D_pct":-51.37,"MAE_1Y_pct":-51.37,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":318000,"drawdown_after_peak_pct":-59.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown","price_only"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"rerating_failed_then_order_quality_break","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L11:066970:2023-07-26:263000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"R13 cross-archetype holdout validation; source row reused with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_trigger_id":"R3L11-C14-LNF-4C-20230726","source_case_id":"R3L11-C14-LNF-20230726","source_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_R13_high_mae_guard","case_id":"R13L11_HIGHMAE_X06_066970_C14","trigger_id":"R13L11_HIGHMAE_X06_066970_4B4C_20230726","symbol":"066970","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":78,"legal_or_contract_risk_score":72,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":75,"high_mae_size_cap_score":85},"weighted_score_before":68,"stage_label_before":"Stage4B_or_4C_watch_under_P0","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":82,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":85,"high_mae_size_cap_score":85},"weighted_score_after":54,"stage_label_after":"Rejected_or_Stage4C_Hard_Break","changed_components":["high_mae_size_cap_score","execution_risk_score","valuation_repricing_score","revision_score","margin_bridge_score"],"component_delta_explanation":"R13 high-MAE guard caps Green/size when MAE is severe or when MFE is mostly price/event rerating without durable margin, revision, contract, regulatory, or customer conversion bridge.","MFE_90D_pct":20.91,"MAE_90D_pct":-51.37,"score_return_alignment_label":"improved_cross_archetype_high_MAE_alignment","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"case","case_id":"R13L11_HIGHMAE_X07_039610_C31","source_case_id":"R11L11_C31_HSVALVE_PERIPHERAL_EQUIPMENT_OPTIONALITY","source_trigger_id":"TR_R11L11_HSVALVE_STAGE2_2024_06_03","symbol":"039610","company_name":"화성밸브","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","case_type":"stage2_watch_success_not_green","positive_or_counterexample":"positive","best_trigger":"R13L11_HIGHMAE_X07_039610_STAGE2WATCH_20240604","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"R13 holdout validation: source Loop 11 trigger reused only for cross-archetype high-MAE guardrail; not counted as new sector-specific evidence.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"peripheral_policy_success_not_green","current_profile_verdict":"current_profile_too_late_for_watch_but_not_green","price_source":"Songdaiki/stock-web","notes":"Peripheral policy equipment produced upside, but -21.2% MAE and weak direct cash-flow route argue for Stage2-watch/overlay, not Green."}
{"row_type":"trigger","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","sector":"cross_archetype_redteam_checkpoint","primary_archetype":"R13 cross-archetype high-MAE / false-Green / size-cap guardrail","loop_objective":"holdout_validation|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_id":"R13L11_HIGHMAE_X07_039610_STAGE2WATCH_20240604","case_id":"R13L11_HIGHMAE_X07_039610_C31","symbol":"039610","company_name":"화성밸브","trigger_type":"Stage2_event_premium_risk_watch","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":8630,"evidence_available_at_that_date":"R13 holdout reuse of source evidence: Valve-equipment theme attached to gas exploration policy; no company-specific order or backlog confirmation at trigger.","evidence_source":"source loop11 row TR_R11L11_HSVALVE_STAGE2_2024_06_03 from R11/C31_POLICY_SUBSIDY_LEGISLATION_EVENT; stock-web OHLC path preserved","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv","profile_path":"atlas/symbol_profiles/039/039610.json","MFE_30D_pct":28.39,"MFE_90D_pct":77.52,"MFE_180D_pct":78.68,"MFE_1Y_pct":78.68,"MFE_2Y_pct":null,"MAE_30D_pct":-21.21,"MAE_90D_pct":-21.21,"MAE_180D_pct":-21.21,"MAE_1Y_pct":-21.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-23","peak_price":15420,"drawdown_after_peak_pct":-46.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"peripheral_policy_success_not_green","current_profile_verdict":"current_profile_too_late_for_watch_but_not_green","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L11:039610:2024-06-04:8630","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"reuse_reason":"R13 cross-archetype holdout validation; source row reused with independent_evidence_weight=0.5.","source_trigger_id":"TR_R11L11_HSVALVE_STAGE2_2024_06_03","source_case_id":"R11L11_C31_HSVALVE_PERIPHERAL_EQUIPMENT_OPTIONALITY","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_R13_high_mae_guard","case_id":"R13L11_HIGHMAE_X07_039610_C31","trigger_id":"R13L11_HIGHMAE_X07_039610_STAGE2WATCH_20240604","symbol":"039610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":70},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable_or_Stage3-Yellow_under_P0","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":48,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":45,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0,"high_mae_size_cap_score":70},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable_Size_Capped_until_confirmation","changed_components":["high_mae_size_cap_score","execution_risk_score","valuation_repricing_score","revision_score","margin_bridge_score"],"component_delta_explanation":"R13 high-MAE guard caps Green/size when MAE is severe or when MFE is mostly price/event rerating without durable margin, revision, contract, regulatory, or customer conversion bridge.","MFE_90D_pct":77.52,"MAE_90D_pct":-21.21,"score_return_alignment_label":"improved_cross_archetype_high_MAE_alignment","current_profile_verdict":"current_profile_too_late_for_watch_but_not_green"}
{"row_type":"case","case_id":"R13L11_HIGHMAE_X08_003070_C30","source_case_id":"R10L11-C30-KOLON-20240125","source_trigger_id":"R10L11-C30-KOLON-STAGE2-20240125","symbol":"003070","company_name":"코오롱글로벌","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","case_type":"4B_too_late","positive_or_counterexample":"counterexample","best_trigger":"R13L11_HIGHMAE_X08_003070_STAGE2A_20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"R13 holdout validation: source Loop 11 trigger reused only for cross-archetype high-MAE guardrail; not counted as new sector-specific evidence.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"score_price_alignment":"PF_recovery_price_only_spike_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Construction/PF recovery spike had large MFE but was price-only; full positive promotion needs balance-sheet bridge and 4B overlay near the spike."}
{"row_type":"trigger","trigger_id":"R13L11_HIGHMAE_X08_003070_STAGE2A_20240125","case_id":"R13L11_HIGHMAE_X08_003070_C30","symbol":"003070","company_name":"코오롱글로벌","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"CROSS_ARCHETYPE_HIGH_MAE_STAGE2_SIZE_CAP_GREEN_BRIDGE_GUARD","sector":"cross_archetype_redteam_checkpoint","primary_archetype":"R13 cross-archetype high-MAE / false-Green / size-cap guardrail","loop_objective":"holdout_validation|counterexample_mining|yellow_threshold_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"R13 holdout reuse of source evidence: historical public-event proxy: 2024 early PF/real-estate policy relief and construction-sector value/bounce watch; stock-web row fixes timing","evidence_source":"source loop11 row R10L11-C30-KOLON-STAGE2-20240125 from R10/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK; stock-web OHLC path preserved","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv","profile_path":"atlas/symbol_profiles/003/003070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":9130,"MFE_30D_pct":17.2,"MFE_90D_pct":76.45,"MFE_180D_pct":76.45,"MFE_1Y_pct":76.45,"MFE_2Y_pct":null,"MAE_30D_pct":-3.61,"MAE_90D_pct":-10.51,"MAE_180D_pct":-10.51,"MAE_1Y_pct":-10.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":16110,"drawdown_after_peak_pct":-47.24,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"price_only_spike_should_be_4B_overlay_not_positive_Green","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable_entry_trigger","trigger_outcome_label":"PF_recovery_price_only_spike_4B_overlay","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L11:003070:2024-01-25:9130","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"R13 cross-archetype holdout validation; source row reused with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_trigger_id":"R10L11-C30-KOLON-STAGE2-20240125","source_case_id":"R10L11-C30-KOLON-20240125","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_R13_high_mae_guard","case_id":"R13L11_HIGHMAE_X08_003070_C30","trigger_id":"R13L11_HIGHMAE_X08_003070_STAGE2A_20240125","symbol":"003070","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":65,"thesis_break_score":0,"high_mae_size_cap_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Watch_or_Event_Premium_under_P0","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":82,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":65,"thesis_break_score":0,"high_mae_size_cap_score":0},"weighted_score_after":63,"stage_label_after":"Stage4B_Risk_Overlay_Not_Green","changed_components":["high_mae_size_cap_score","execution_risk_score","valuation_repricing_score","revision_score","margin_bridge_score"],"component_delta_explanation":"R13 high-MAE guard caps Green/size when MAE is severe or when MFE is mostly price/event rerating without durable margin, revision, contract, regulatory, or customer conversion bridge.","MFE_90D_pct":76.45,"MAE_90D_pct":-10.51,"score_return_alignment_label":"improved_cross_archetype_high_MAE_alignment","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R13","loop":"11","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","new_independent_case_count":8,"reused_case_count":8,"new_symbol_count":8,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_early","current_profile_false_positive","current_profile_4B_too_late","current_profile_4C_too_late","high_MAE_success_size_cap_needed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R13
completed_loop = 11
next_round = R1
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
computed_next_round = R1
computed_next_loop = 12
```

## 28. Source Notes

```text
stock_web_manifest_path = atlas/manifest.json
stock_web_schema_path = atlas/schema.json
stock_agent_allowed_artifact_reviewed = reports/e2r_calibration/by_round/R13.md
source_loop11_rows = local v12 research MDs for R3/R4/R5/R7/R10/R11/R12
source_price_basis = tradable_raw
source_price_adjustment_status = raw_unadjusted_marcap
```

No investment recommendation is made or implied. This is a historical calibration artifact only.

