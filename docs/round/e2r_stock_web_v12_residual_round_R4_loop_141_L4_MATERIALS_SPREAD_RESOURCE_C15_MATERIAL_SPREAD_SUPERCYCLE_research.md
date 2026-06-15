# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
output_file = e2r_stock_web_v12_residual_round_R4_loop_141_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
selected_round = R4
selected_loop = 141
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / over_50_rows_quality_repair / C15 rows 73
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 1. Current Calibrated Profile Assumption

This loop assumes `e2r_2_1_stock_web_calibrated_proxy` as the current profile and uses the already-applied global axes only as stress-test targets. No production score is changed. The loop is not a live candidate scan. It only creates a standalone historical calibration MD.

## 2. Round / Large Sector / Canonical Archetype Scope

C15 belongs to `R4 / L4_MATERIALS_SPREAD_RESOURCE`. The fine/deep sub-archetype is `STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE`.

Mechanism under test:

```text
input = benchmark spread / commodity price / freight-rate expansion
bridge = company-specific volume, ASP, inventory, cost, margin, FCF conversion
failure = late record-profit confirmation after peak, or supercycle mean reversion
shadow rule = early spread + margin bridge can promote; late spread proof needs 4B/profit-lock guard
```

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C15 as Priority 2: more than 50 rows already exist, so this loop is not a quantity fill. It is a quality-repair loop targeting URL/source repair, spread reversal, and 4B timing. Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

The current session previously covered C16, C20, C21, C30, C29, C32, C26, C18, C31, C19, C08, C27, C23, C05, C12, C28, C01, C11, C07, C06, C10, C14, C09, and C02. C15 has not been emitted in this session, so the canonical axis is new to this continuation segment.

## 4. Stock-Web OHLC Input / Price Source Validation

The price basis is stock-web `tradable_raw`, `raw_unadjusted_marcap`, with shard paths under `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`. The manifest max date is `2026-02-20`; no prices after that date are used.

Profiles checked through stock-web metadata show no 2020~2022 corporate-action window issue for POSCO Holdings and Poongsan. Hyundai Steel and Pan Ocean have old corporate-action candidate dates before this research window. S-Oil has an old candidate date in 2001. HMM is kept as narrative-only because the profile lists `2021-11-16` as a corporate-action candidate date inside the 180D window from the 2021-08-13 container freight trigger.

## 5. Historical Eligibility Gate

All eight representative trigger rows below have `forward_window_trading_days >= 180`, entry price from the entry-date `c` column, complete 30/90/180D MFE/MAE fields, and `corporate_action_window_status = clean_180D_window`. HMM is excluded from trigger rows and appears only as narrative-only.

## 6. Canonical Archetype Compression Map

| fine/deep label | canonical compression | why |
|---|---|---|
| copper-price fabricated margin | C15_MATERIAL_SPREAD_SUPERCYCLE | commodity price/spread flows into material margin and inventory gain |
| steel price / hot-rolled spread | C15_MATERIAL_SPREAD_SUPERCYCLE | steel ASP and raw-material cost spread drive OP cycle |
| dry-bulk freight spread | C15_MATERIAL_SPREAD_SUPERCYCLE | freight spread behaves like a material-cycle margin spread for shippers |
| refining crack spread | C15_MATERIAL_SPREAD_SUPERCYCLE | product spread over crude maps directly into refining margin |
| record-profit confirmation after peak | C15_MATERIAL_SPREAD_SUPERCYCLE with 4B guard | thesis is true but timing is late and mean reversion dominates |

## 7. Case Selection Summary

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | role | current profile verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 103140_20201207_stage2_actionable | 103140 풍산 | Stage2-Actionable | 2020-12-07 | 29300 | 35.49 | -8.70 | 70.48 | -8.70 | positive | current_profile_too_late_if_requires_full_year_confirmation |
| 005490_20210125_stage2_actionable | 005490 POSCO홀딩스 | Stage2-Actionable | 2021-01-25 | 264500 | 56.33 | -8.32 | 56.33 | -8.32 | positive | current_profile_too_late_if_waits_for_2021_earnings_release |
| 028670_20210514_stage2_actionable | 028670 팬오션 | Stage2-Actionable | 2021-05-14 | 6870 | 29.84 | -8.88 | 29.84 | -31.44 | positive | current_profile_correct_on_stage2_but_needs_local_4b_after_fast_reprice |
| 010950_20220427_stage2_actionable | 010950 S-Oil | Stage2-Actionable | 2022-04-27 | 105000 | 17.14 | -19.24 | 17.14 | -26.57 | positive | current_profile_correct_on_stage2_but_underweights_4b_spread_mean_reversion |
| 004020_20210427_stage2_watch | 004020 현대제철 | Stage2 | 2021-04-27 | 56700 | 11.11 | -20.19 | 11.11 | -34.66 | counterexample | current_profile_false_positive_if_spread_headline_promoted_without_reprice_context |
| 005490_20210722_stage3_yellow | 005490 POSCO홀딩스 | Stage3-Yellow | 2021-07-22 | 346000 | 9.68 | -24.86 | 9.68 | -26.01 | counterexample | current_profile_too_late_if_Stage3_waits_for_full_confirmation |
| 028670_20210813_stage3_yellow | 028670 팬오션 | Stage3-Yellow | 2021-08-13 | 7410 | 12.69 | -31.44 | 12.69 | -36.44 | counterexample | current_profile_too_late_if_Q2_result_used_as_fresh_Yellow |
| 004020_20211028_stage3_yellow | 004020 현대제철 | Stage3-Yellow | 2021-10-28 | 44600 | 5.83 | -16.93 | 5.83 | -31.28 | counterexample | current_profile_false_positive_if_record_profit_confirmation_treated_as_new_Yellow |


## 8. Positive vs Counterexample Balance

Positive/control rows are Poongsan 2020-12-07, POSCO 2021-01-25, Pan Ocean 2021-05-14, and S-Oil 2022-04-27. Counterexample/guardrail rows are Hyundai Steel 2021-04-27, POSCO 2021-07-22, Pan Ocean 2021-08-13, and Hyundai Steel 2021-10-28.

The positive side says that spread signals work before full confirmation when they include visible price/volume/margin transmission. The counterexample side says that after a supercycle is obvious enough to print record quarterly profit, the stock often behaves less like an unlock and more like a hot stove: it still glows, but touching it late burns the entry.

## 9. Evidence Source Map

| symbol | date | evidence route | source |
|---|---:|---|---|
| 103140 Poongsan | 2020-12-07 | copper price strength expected to improve 2021 operating profit | https://www.businesspost.co.kr/BP?command=article_view&num=207472 |
| 103140 Poongsan | 2021/2022 confirmation | record-high 2021 earnings, copper ASP and copper-alloy sales growth | https://securities.miraeasset.com/bbs/download/2091868.pdf?attachmentId=2091868 |
| 005490 POSCO | 2021-01-25 | Q4 profit estimate supported by China steel demand and steel price hikes | https://en.yna.co.kr/view/AEN20210122006600320 |
| 005490 POSCO | 2021 earnings confirmation | market rebound, domestic/high-end sales expansion, 2021 production/sales recovery | https://www.posco.co.kr/homepage/servlet/FileDownLoad?fileCategory=irDataFd&fileNum=407 |
| 028670 Pan Ocean | 2021-05-14 | Q1 sales/OP growth, BDI up about 194% YoY, spot/fleet effort | https://www.panocean.com/kor/NewsView?i=49&p=3 |
| 028670 Pan Ocean | 2021-08-13 | Q2 OP above KRW 100bn after BDI supercycle | https://www.panocean.com/kor/NewsView?i=76&p=4 |
| 010950 S-Oil | 2022-04-27 | strong cracking margin, inventory gains, refining OP during supply shock | https://en.yna.co.kr/view/AEN20220427005752320 |
| 004020 Hyundai Steel | 2021-10-28 | record operating profit, high demand and solid pricing | https://koreajoongangdaily.joins.com/2021/10/28/business/industry/hyundai-steel-third-quarter-steel/20211028163045983.html |
| 011200 HMM | narrative-only | freight supercycle useful, but corporate-action window blocks trigger calibration | https://koreajoongangdaily.joins.com/2021/11/14/business/industry/hmm-pan-ocean-container-cargo/20211114163629781.html |

## 10. Price Data Source Map

| symbol | profile_path | shard years used | corporate-action status in tested window |
|---|---|---|---|
| 103140 | atlas/symbol_profiles/103/103140.json | 2020, 2021 | clean_180D_window |
| 005490 | atlas/symbol_profiles/005/005490.json | 2021, 2022 | clean_180D_window |
| 028670 | atlas/symbol_profiles/028/028670.json | 2021, 2022 | clean_180D_window |
| 010950 | atlas/symbol_profiles/010/010950.json | 2022, 2023 | clean_180D_window |
| 004020 | atlas/symbol_profiles/004/004020.json | 2021, 2022 | clean_180D_window |
| 011200 | atlas/symbol_profiles/011/011200.json | narrative-only | blocked: 2021-11-16 corporate-action candidate inside 180D window |

## 11. Case-by-Case Trigger Grid

### 11.1 Positive/control: early spread bridge

Poongsan and POSCO are the cleanest early spread positives. In both cases, the market had enough non-price evidence before full-year proof: copper or steel price strength, demand recovery, and a company-specific route to sales/OP. Waiting for full-year proof would have made the model behave like a thermometer that confirms summer after the harvest is already over.

Pan Ocean and S-Oil are high-MAE positives: they prove the spread mechanism, but also show the danger of letting spread supercycle names sit without a local 4B/profit-lock overlay.

### 11.2 Counterexamples: late confirmation and mean reversion

Hyundai Steel 2021-04-27 and 2021-10-28 both show that true steel spread improvement does not automatically create a good entry if the stock is already near the cycle window. POSCO 2021-07-22 and Pan Ocean 2021-08-13 are classic Stage3-Yellow lateness rows: the evidence was very real, but the price path after confirmation had far worse asymmetry than the early Stage2 rows.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | role | current profile verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 103140_20201207_stage2_actionable | 103140 풍산 | Stage2-Actionable | 2020-12-07 | 29300 | 35.49 | -8.70 | 70.48 | -8.70 | positive | current_profile_too_late_if_requires_full_year_confirmation |
| 005490_20210125_stage2_actionable | 005490 POSCO홀딩스 | Stage2-Actionable | 2021-01-25 | 264500 | 56.33 | -8.32 | 56.33 | -8.32 | positive | current_profile_too_late_if_waits_for_2021_earnings_release |
| 028670_20210514_stage2_actionable | 028670 팬오션 | Stage2-Actionable | 2021-05-14 | 6870 | 29.84 | -8.88 | 29.84 | -31.44 | positive | current_profile_correct_on_stage2_but_needs_local_4b_after_fast_reprice |
| 010950_20220427_stage2_actionable | 010950 S-Oil | Stage2-Actionable | 2022-04-27 | 105000 | 17.14 | -19.24 | 17.14 | -26.57 | positive | current_profile_correct_on_stage2_but_underweights_4b_spread_mean_reversion |
| 004020_20210427_stage2_watch | 004020 현대제철 | Stage2 | 2021-04-27 | 56700 | 11.11 | -20.19 | 11.11 | -34.66 | counterexample | current_profile_false_positive_if_spread_headline_promoted_without_reprice_context |
| 005490_20210722_stage3_yellow | 005490 POSCO홀딩스 | Stage3-Yellow | 2021-07-22 | 346000 | 9.68 | -24.86 | 9.68 | -26.01 | counterexample | current_profile_too_late_if_Stage3_waits_for_full_confirmation |
| 028670_20210813_stage3_yellow | 028670 팬오션 | Stage3-Yellow | 2021-08-13 | 7410 | 12.69 | -31.44 | 12.69 | -36.44 | counterexample | current_profile_too_late_if_Q2_result_used_as_fresh_Yellow |
| 004020_20211028_stage3_yellow | 004020 현대제철 | Stage3-Yellow | 2021-10-28 | 44600 | 5.83 | -16.93 | 5.83 | -31.28 | counterexample | current_profile_false_positive_if_record_profit_confirmation_treated_as_new_Yellow |


MFE/MAE calculation follows the prompt formula: entry date close as `entry_price`, high/low over 30/90/180 trading-day windows from stock-web tradable rows.

## 13. Current Calibrated Profile Stress Test

| question | finding |
|---|---|
| Does current calibrated Stage2 bridge work? | Yes for early POSCO/Poongsan/Pan Ocean/S-Oil rows when spread has company-specific conversion. |
| Does current profile still err? | Yes. It can still overcredit late record-profit proof in spread supercycles. |
| Was Stage2-Actionable bonus too high? | Not globally. It is useful early, but should be gated by reprice context and spread reversal risk. |
| Was Yellow threshold too late? | In C15, Yellow based on record profit often fires after most asymmetry is gone. |
| Does Green need loosening? | No. C15 should not loosen Green; it needs earlier Stage2 plus faster 4B/profit-lock once spread mean reversion risk appears. |

## 14. Stage2 / Yellow / Green Comparison

| bucket | rows | avg MFE90 | avg MAE90 | interpretation |
|---|---:|---:|---:|---|
| early Stage2/Actionable positives | 4 | 34.70 | -11.29 | good enough to preserve early bridge credit |
| late Stage2/Yellows and proof-after-peak rows | 4 | 9.83 | -23.36 | confirmation without timing context becomes false-positive risk |
| all representative rows | 8 | 22.26 | -17.32 | mixed; rule needs timing split, not global promotion |

Green is not the target in this loop. C15 benefits from earlier Stage2 recognition and sharper 4B overlay, not Green threshold relaxation.

## 15. 4B Local vs Full-window Timing Audit

| symbol | entry | peak_date | MFE180 | drawdown_after_peak | 4B audit |
|---|---:|---:|---:|---:|---|
| 103140 | 2020-12-07 | 2021-05-12 | 70.48 | -34.53 | successful Stage2 but requires post-peak profit-lock |
| 005490 early | 2021-01-25 | 2021-05-10 | 56.33 | -26.00 | 4B watch after steel cycle peak, not before |
| 028670 early | 2021-05-14 | 2021-06-29 | 29.84 | -47.20 | strong local 4B need after fast BDI reprice |
| 010950 | 2022-04-27 | 2022-06-13 | 17.14 | -37.32 | refining spread supercycle needs mean-reversion guard |
| 004020 late | 2021-10-28 | 2022-01-13 | 5.83 | -35.06 | record-profit proof is not an unlock; it is a guardrail |

## 16. 4C Protection Audit

No hard 4C trigger is proposed. The failure mode is not immediate thesis break; it is late-cycle spread mean reversion. Therefore the candidate protection is `Stage4B / local profit-lock / spread reversal watch`, not hard 4C.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L4_SPREAD_SUPERCYCLE_REQUIRES_SPREAD_TO_MARGIN_BRIDGE_AND_REPRICE_CONTEXT_GATE
```

Rule mechanics:

1. Give Stage2-Actionable when benchmark spread/commodity price/freight rate is visible and company-specific ASP, volume, inventory, margin, or FCF route exists.
2. Do not promote late record-profit confirmation into fresh Yellow if price already repriced and spread reversal risk is rising.
3. Require local 4B/profit-lock overlay when MFE is front-loaded and peak-to-trough drawdown risk exceeds roughly 30% in the 180D window.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C15_SPREAD_SUPERCYCLE_STAGE2_REQUIRES_MARGIN_CONVERSION_AND_LATE_CONFIRMATION_GETS_4B_GUARD
```

This is not a global rule. It is specific to C15 because material spread cycles have a clock inside them. The same evidence that is powerful at the start of the spread expansion becomes stale evidence near the top.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | false-positive risk | verdict |
|---|---|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 8 | 22.26 | -17.32 | medium | mixed; early bridge works but late proof overcredited |
| P0b_e2r_2_0_baseline_reference | rollback | 8 | lower early capture | less signal | high missed structural | too slow for Poongsan/POSCO early rows |
| P1_L4_sector_spread_reversal_candidate | sector | 8 | improves selection | lowers late-cycle drawdown | lower | best sector timing split |
| P2_C15_canonical_spread_supercycle_candidate | canonical | 8 | best after filtering late proof | lower counterexample rate | lowest | candidate rule |

## 20. Score-Return Alignment Matrix

| alignment label | examples | decision |
|---|---|---|
| positive_direct_bridge | 103140, 005490 early | keep Stage2-Actionable bridge |
| high_mae_success | 028670 early, 010950 | retain signal but add 4B/profit-lock overlay |
| late_confirmation_counterexample | 005490 July, 028670 August, 004020 October | cap as Yellow-late or 4B watch, not fresh Green |
| failed_rerating | 004020 April | require reprice context and spread durability |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable_trigger | representative | current_profile_error | sector_rule | canonical_rule | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE | 4 | 4 | 4 | 0 | 8 | 0 | 8 | 8 | 6 | L4_SPREAD_SUPERCYCLE_REQUIRES_SPREAD_TO_MARGIN_BRIDGE_AND_REPRICE_CONTEXT_GATE | C15_SPREAD_SUPERCYCLE_STAGE2_REQUIRES_MARGIN_CONVERSION_AND_LATE_CONFIRMATION_GETS_4B_GUARD | C15 static 73 + 8 local representative usable rows = 81 after commit if accepted; quality-repair, not quantity fill. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_required_bridge, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: late_spread_confirmation_false_positive, spread_supercycle_mean_reversion_high_MAE, freight_rate_and_refining_margin_post_peak_drawdown, record_profit_after_peak_green_lateness
new_axis_proposed: C15_SPREAD_SUPERCYCLE_STAGE2_REQUIRES_MARGIN_CONVERSION_AND_LATE_CONFIRMATION_GETS_4B_GUARD
existing_axis_strengthened: stage2_required_bridge, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c should not fire on simple spread reversal without thesis break
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: L4_SPREAD_SUPERCYCLE_REQUIRES_SPREAD_TO_MARGIN_BRIDGE_AND_REPRICE_CONTEXT_GATE
canonical_archetype_rule_candidate: C15_SPREAD_SUPERCYCLE_STAGE2_REQUIRES_MARGIN_CONVERSION_AND_LATE_CONFIRMATION_GETS_4B_GUARD
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 8 new independent cases, 4 counterexamples, and 6 residual errors for R4/L4/C15.

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows for 103140, 005490, 028670, 010950, 004020
- 30/90/180D MFE/MAE from entry close
- clean 180D forward windows for all emitted trigger rows
- narrative-only block for HMM due corporate-action contamination risk
```

Not validated:

```text
- intraday evidence timestamp precision
- adjusted-price total return
- live/current candidate status
- production score changes
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,spread_margin_conversion_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"early spread needs company-specific margin bridge","keeps POSCO/Poongsan while filtering late confirmations","103140_20201207_stage2_actionable|005490_20210125_stage2_actionable|005490_20210722_stage3_yellow",8,8,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,spread_reversal_4b_guard,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"front-loaded MFE followed by >30pct peak drawdown requires local 4B/profit-lock","reduces Pan Ocean/S-Oil/Hyundai late-cycle false positives","028670_20210514_stage2_actionable|010950_20220427_stage2_actionable|004020_20211028_stage3_yellow",8,8,4,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C15_103140_20201207_COPPER_PRICE_STAGE2","symbol":"103140","company_name":"풍산","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"103140_20201207_stage2_actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_direct_bridge","current_profile_verdict":"current_profile_too_late_if_requires_full_year_confirmation","price_source":"Songdaiki/stock-web","notes":"Copper price rise + fabricated copper margin recovery expectation before full 2021 earnings confirmation."}
{"row_type":"case","case_id":"C15_005490_20210125_STEEL_SPREAD_STAGE2","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"005490_20210125_stage2_actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_direct_bridge","current_profile_verdict":"current_profile_too_late_if_waits_for_2021_earnings_release","price_source":"Songdaiki/stock-web","notes":"Steel demand and price hikes visible before full-year 2021 margin confirmation."}
{"row_type":"case","case_id":"C15_028670_20210514_BDI_STAGE2","symbol":"028670","company_name":"팬오션","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"028670_20210514_stage2_actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_direct_bridge","current_profile_verdict":"current_profile_correct_on_stage2_but_needs_local_4b_after_fast_reprice","price_source":"Songdaiki/stock-web","notes":"BDI up sharply; spot operation and fleet expansion provided early freight-spread leverage, before Q2 2021 supercycle proof."}
{"row_type":"case","case_id":"C15_010950_20220427_REFINING_MARGIN_STAGE2","symbol":"010950","company_name":"S-Oil","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"010950_20220427_stage2_actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_direct_bridge","current_profile_verdict":"current_profile_correct_on_stage2_but_underweights_4b_spread_mean_reversion","price_source":"Songdaiki/stock-web","notes":"Q1 2022 earnings showed strong cracking margin, inventory gains and refining operating profit during the Russia-Ukraine supply shock."}
{"row_type":"case","case_id":"C15_004020_20210427_STEEL_PRICE_LATE_STAGE2","symbol":"004020","company_name":"현대제철","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"004020_20210427_stage2_watch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_guardrail","current_profile_verdict":"current_profile_false_positive_if_spread_headline_promoted_without_reprice_context","price_source":"Songdaiki/stock-web","notes":"Steel price upcycle was visible, but entry after sector reprice had poor MFE/MAE; margin spread headline alone did not protect drawdown."}
{"row_type":"case","case_id":"C15_005490_20210722_STEEL_RECORD_LATE_YELLOW","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","case_type":"late_confirmation_counterexample","positive_or_counterexample":"counterexample","best_trigger":"005490_20210722_stage3_yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_guardrail","current_profile_verdict":"current_profile_too_late_if_Stage3_waits_for_full_confirmation","price_source":"Songdaiki/stock-web","notes":"Q2/2021 record steel earnings confirmed the thesis after much of the price move had already occurred."}
{"row_type":"case","case_id":"C15_028670_20210813_Q2_BDI_LATE_YELLOW","symbol":"028670","company_name":"팬오션","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","case_type":"late_confirmation_counterexample","positive_or_counterexample":"counterexample","best_trigger":"028670_20210813_stage3_yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_guardrail","current_profile_verdict":"current_profile_too_late_if_Q2_result_used_as_fresh_Yellow","price_source":"Songdaiki/stock-web","notes":"Q2 earnings proved dry-bulk supercycle leverage, but stock-web path shows low incremental upside and large 90/180D MAE after confirmation."}
{"row_type":"case","case_id":"C15_004020_20211028_RECORD_PROFIT_LATE_YELLOW","symbol":"004020","company_name":"현대제철","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","case_type":"late_confirmation_counterexample","positive_or_counterexample":"counterexample","best_trigger":"004020_20211028_stage3_yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_guardrail","current_profile_verdict":"current_profile_false_positive_if_record_profit_confirmation_treated_as_new_Yellow","price_source":"Songdaiki/stock-web","notes":"Record Q3 operating profit and solid pricing were confirmed after the steel spread trade had lost asymmetry."}
{"row_type":"trigger","trigger_id":"103140_20201207_stage2_actionable","case_id":"C15_103140_20201207_COPPER_PRICE_STAGE2","symbol":"103140","company_name":"풍산","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","sector":"materials_spread_resource","primary_archetype":"material_spread_supercycle","loop_objective":"quality_repair|spread_reversal_repair|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2020-12-07","entry_date":"2020-12-07","entry_price":29300.0,"evidence_available_at_that_date":"Copper price rise + fabricated copper margin recovery expectation before full 2021 earnings confirmation.","evidence_source":"https://www.businesspost.co.kr/BP?command=article_view&num=207472","stage2_evidence_fields":["copper_price_strength","fabricated_copper_margin_route","2021_estimate_revision"],"stage3_evidence_fields":["2021_record_earnings_later_confirmed","copper_alloy_sales_growth"],"stage4b_evidence_fields":["post_peak_spread_reversal_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2020.csv","profile_path":"atlas/symbol_profiles/103/103140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.73,"MFE_90D_pct":35.49,"MFE_180D_pct":70.48,"MAE_30D_pct":-8.7,"MAE_90D_pct":-8.7,"MAE_180D_pct":-8.7,"peak_date":"2021-05-12","peak_price":49950.0,"drawdown_after_peak_pct":-34.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4b_profit_lock","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"copper_price_fabricated_margin_positive","current_profile_verdict":"current_profile_too_late_if_requires_full_year_confirmation","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE_103140_2020-12-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"005490_20210125_stage2_actionable","case_id":"C15_005490_20210125_STEEL_SPREAD_STAGE2","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","sector":"materials_spread_resource","primary_archetype":"material_spread_supercycle","loop_objective":"quality_repair|spread_reversal_repair|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-25","entry_date":"2021-01-25","entry_price":264500.0,"evidence_available_at_that_date":"Steel demand and price hikes visible before full-year 2021 margin confirmation.","evidence_source":"https://en.yna.co.kr/view/AEN20210122006600320","stage2_evidence_fields":["steel_price_hike","China_demand_recovery","Q4_profit_estimate_revision"],"stage3_evidence_fields":["2021_earnings_release_later_confirms_market_rebound","high_end_product_sales_expansion"],"stage4b_evidence_fields":["spread_supercycle_post_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.28,"MFE_90D_pct":56.33,"MFE_180D_pct":56.33,"MAE_30D_pct":-8.32,"MAE_90D_pct":-8.32,"MAE_180D_pct":-8.32,"peak_date":"2021-05-10","peak_price":413500.0,"drawdown_after_peak_pct":-26.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"steel_price_demand_margin_positive","current_profile_verdict":"current_profile_too_late_if_waits_for_2021_earnings_release","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE_005490_2021-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"028670_20210514_stage2_actionable","case_id":"C15_028670_20210514_BDI_STAGE2","symbol":"028670","company_name":"팬오션","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","sector":"materials_spread_resource","primary_archetype":"material_spread_supercycle","loop_objective":"quality_repair|spread_reversal_repair|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-05-14","entry_date":"2021-05-14","entry_price":6870.0,"evidence_available_at_that_date":"BDI up sharply; spot operation and fleet expansion provided early freight-spread leverage, before Q2 2021 supercycle proof.","evidence_source":"https://www.panocean.com/kor/NewsView?i=49&p=3","stage2_evidence_fields":["BDI_up_approximately_194pct_YoY","spot_operation_expansion","fleet_expansion"],"stage3_evidence_fields":["Q2_2021_OP_above_100bn_KRW_later_confirmed"],"stage4b_evidence_fields":["post_peak_freight_rate_reversal_risk","local_peak_after_fast_reprice"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv","profile_path":"atlas/symbol_profiles/028/028670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.26,"MFE_90D_pct":29.84,"MFE_180D_pct":29.84,"MAE_30D_pct":-8.88,"MAE_90D_pct":-8.88,"MAE_180D_pct":-31.44,"peak_date":"2021-06-29","peak_price":8920.0,"drawdown_after_peak_pct":-47.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4b_profit_lock","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"drybulk_freight_spread_positive_with_profit_lock_needed","current_profile_verdict":"current_profile_correct_on_stage2_but_needs_local_4b_after_fast_reprice","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE_028670_2021-05-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"010950_20220427_stage2_actionable","case_id":"C15_010950_20220427_REFINING_MARGIN_STAGE2","symbol":"010950","company_name":"S-Oil","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","sector":"materials_spread_resource","primary_archetype":"material_spread_supercycle","loop_objective":"quality_repair|spread_reversal_repair|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-04-27","entry_date":"2022-04-27","entry_price":105000.0,"evidence_available_at_that_date":"Q1 2022 earnings showed strong cracking margin, inventory gains and refining operating profit during the Russia-Ukraine supply shock.","evidence_source":"https://en.yna.co.kr/view/AEN20220427005752320","stage2_evidence_fields":["strong_cracking_margin","inventory_related_gain","supply_shortage_from_Russia_Ukraine_crisis"],"stage3_evidence_fields":["refining_segment_OP_1_2trn_KRW"],"stage4b_evidence_fields":["spread_mean_reversion_risk","oil_price_inventory_loss_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010950/2022.csv","profile_path":"atlas/symbol_profiles/010/010950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.19,"MFE_90D_pct":17.14,"MFE_180D_pct":17.14,"MAE_30D_pct":-3.81,"MAE_90D_pct":-19.24,"MAE_180D_pct":-26.57,"peak_date":"2022-06-13","peak_price":123000.0,"drawdown_after_peak_pct":-37.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4b_profit_lock","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"refining_crack_spread_positive_but_reversal_risk","current_profile_verdict":"current_profile_correct_on_stage2_but_underweights_4b_spread_mean_reversion","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE_010950_2022-04-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"004020_20210427_stage2_watch","case_id":"C15_004020_20210427_STEEL_PRICE_LATE_STAGE2","symbol":"004020","company_name":"현대제철","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","sector":"materials_spread_resource","primary_archetype":"material_spread_supercycle","loop_objective":"quality_repair|spread_reversal_repair|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2021-04-27","entry_date":"2021-04-27","entry_price":56700.0,"evidence_available_at_that_date":"Steel price upcycle was visible, but entry after sector reprice had poor MFE/MAE; margin spread headline alone did not protect drawdown.","evidence_source":"https://koreajoongangdaily.joins.com/2021/10/28/business/industry/hyundai-steel-third-quarter-steel/20211028163045983.html","stage2_evidence_fields":["steel_demand_and_price_cycle"],"stage3_evidence_fields":["record_profit_confirmed_later_but_after_reprice"],"stage4b_evidence_fields":["already_repriced","cost_raw_material_pressure_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv","profile_path":"atlas/symbol_profiles/004/004020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.11,"MFE_90D_pct":11.11,"MFE_180D_pct":11.11,"MAE_30D_pct":-10.76,"MAE_90D_pct":-20.19,"MAE_180D_pct":-34.66,"peak_date":"2021-05-11","peak_price":63000.0,"drawdown_after_peak_pct":-41.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4b_profit_lock","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"steel_price_headline_late_entry_counterexample","current_profile_verdict":"current_profile_false_positive_if_spread_headline_promoted_without_reprice_context","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE_004020_2021-04-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"005490_20210722_stage3_yellow","case_id":"C15_005490_20210722_STEEL_RECORD_LATE_YELLOW","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","sector":"materials_spread_resource","primary_archetype":"material_spread_supercycle","loop_objective":"quality_repair|spread_reversal_repair|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2021-07-22","entry_date":"2021-07-22","entry_price":346000.0,"evidence_available_at_that_date":"Q2/2021 record steel earnings confirmed the thesis after much of the price move had already occurred.","evidence_source":"https://www.posco.co.kr/homepage/servlet/FileDownLoad?fileCategory=irDataFd&fileNum=407","stage2_evidence_fields":["steel_price_upcycle_already_known"],"stage3_evidence_fields":["record_earnings_confirmation","market_rebound_sales_expansion"],"stage4b_evidence_fields":["cycle_peak_reversion_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.94,"MFE_90D_pct":9.68,"MFE_180D_pct":9.68,"MAE_30D_pct":-11.56,"MAE_90D_pct":-24.86,"MAE_180D_pct":-26.01,"peak_date":"2021-09-14","peak_price":379500.0,"drawdown_after_peak_pct":-32.54,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"late_confirmation_audit_required","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4b_profit_lock","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"steel_earnings_confirmation_late_yellow_counterexample","current_profile_verdict":"current_profile_too_late_if_Stage3_waits_for_full_confirmation","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE_005490_2021-07-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"028670_20210813_stage3_yellow","case_id":"C15_028670_20210813_Q2_BDI_LATE_YELLOW","symbol":"028670","company_name":"팬오션","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","sector":"materials_spread_resource","primary_archetype":"material_spread_supercycle","loop_objective":"quality_repair|spread_reversal_repair|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2021-08-13","entry_date":"2021-08-13","entry_price":7410.0,"evidence_available_at_that_date":"Q2 earnings proved dry-bulk supercycle leverage, but stock-web path shows low incremental upside and large 90/180D MAE after confirmation.","evidence_source":"https://www.panocean.com/kor/NewsView?i=76&p=4","stage2_evidence_fields":["BDI_freight_rate_strength_already_visible"],"stage3_evidence_fields":["Q2_OP_112bn_KRW","post_2008_supercycle_level_profit"],"stage4b_evidence_fields":["BDI_peak_reversal_risk","local_peak_after_fast_reprice"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv","profile_path":"atlas/symbol_profiles/028/028670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.69,"MFE_90D_pct":12.69,"MFE_180D_pct":12.69,"MAE_30D_pct":-4.45,"MAE_90D_pct":-31.44,"MAE_180D_pct":-36.44,"peak_date":"2021-08-24","peak_price":8350.0,"drawdown_after_peak_pct":-43.59,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"late_confirmation_audit_required","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4b_profit_lock","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"drybulk_supercycle_late_confirmation_counterexample","current_profile_verdict":"current_profile_too_late_if_Q2_result_used_as_fresh_Yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE_028670_2021-08-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"004020_20211028_stage3_yellow","case_id":"C15_004020_20211028_RECORD_PROFIT_LATE_YELLOW","symbol":"004020","company_name":"현대제철","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_COPPER_REFINING_SHIPPING_SPREAD_SUPERCYCLE_REVERSAL_GATE","sector":"materials_spread_resource","primary_archetype":"material_spread_supercycle","loop_objective":"quality_repair|spread_reversal_repair|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage3-Yellow","trigger_date":"2021-10-28","entry_date":"2021-10-28","entry_price":44600.0,"evidence_available_at_that_date":"Record Q3 operating profit and solid pricing were confirmed after the steel spread trade had lost asymmetry.","evidence_source":"https://koreajoongangdaily.joins.com/2021/10/28/business/industry/hyundai-steel-third-quarter-steel/20211028163045983.html","stage2_evidence_fields":["steel_demand_price_upcycle"],"stage3_evidence_fields":["record_Q3_OP","solid_pricing"],"stage4b_evidence_fields":["post_peak_drawdown_risk","steel_margin_squeeze_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv","profile_path":"atlas/symbol_profiles/004/004020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.69,"MFE_90D_pct":5.83,"MFE_180D_pct":5.83,"MAE_30D_pct":-16.93,"MAE_90D_pct":-16.93,"MAE_180D_pct":-31.28,"peak_date":"2022-01-13","peak_price":47200.0,"drawdown_after_peak_pct":-35.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"green_lateness_ratio":"late_confirmation_audit_required","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4b_profit_lock","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"record_profit_after_peak_counterexample","current_profile_verdict":"current_profile_false_positive_if_record_profit_confirmation_treated_as_new_Yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_MATERIAL_SPREAD_SUPERCYCLE_004020_2021-10-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"aggregate_C15_loop_141","trigger_id":"aggregate_C15_loop_141","symbol":"MULTI","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":6,"spread_reversal_risk_score":2,"fcf_conversion_score":0,"positioning_overheat_score":2},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":7,"spread_reversal_risk_score":5,"fcf_conversion_score":0,"positioning_overheat_score":4},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["asp_or_spread_score","margin_bridge_score","spread_reversal_risk_score","positioning_overheat_score"],"component_delta_explanation":"Current profile gives Stage2 bridge credit but still overcredits late spread confirmation.","MFE_90D_pct":22.26,"MAE_90D_pct":-17.32,"score_return_alignment_label":"mixed","current_profile_verdict":"current_profile_error_or_guardrail_found"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","case_id":"aggregate_C15_loop_141","trigger_id":"aggregate_C15_loop_141","symbol":"MULTI","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":6,"spread_reversal_risk_score":2,"fcf_conversion_score":0,"positioning_overheat_score":2},"weighted_score_before":71,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":6,"spread_reversal_risk_score":4,"fcf_conversion_score":0,"positioning_overheat_score":3},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":["asp_or_spread_score","margin_bridge_score","spread_reversal_risk_score","positioning_overheat_score"],"component_delta_explanation":"Older baseline waits for stronger confirmation and misses early spread-positive entries.","MFE_90D_pct":22.26,"MAE_90D_pct":-17.32,"score_return_alignment_label":"too_late","current_profile_verdict":"shadow_only"}
{"row_type":"score_simulation","profile_id":"P1_L4_sector_spread_reversal_candidate","case_id":"aggregate_C15_loop_141","trigger_id":"aggregate_C15_loop_141","symbol":"MULTI","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":6,"spread_reversal_risk_score":2,"fcf_conversion_score":0,"positioning_overheat_score":2},"weighted_score_before":73,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":8,"spread_reversal_risk_score":6,"fcf_conversion_score":0,"positioning_overheat_score":5},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["asp_or_spread_score","margin_bridge_score","spread_reversal_risk_score","positioning_overheat_score"],"component_delta_explanation":"Require spread-to-margin bridge and add local 4B profit-lock after fast reprice.","MFE_90D_pct":22.26,"MAE_90D_pct":-17.32,"score_return_alignment_label":"improves_alignment","current_profile_verdict":"shadow_only"}
{"row_type":"score_simulation","profile_id":"P2_C15_canonical_spread_supercycle_candidate","case_id":"aggregate_C15_loop_141","trigger_id":"aggregate_C15_loop_141","symbol":"MULTI","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":6,"spread_reversal_risk_score":2,"fcf_conversion_score":0,"positioning_overheat_score":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":9,"spread_reversal_risk_score":7,"fcf_conversion_score":0,"positioning_overheat_score":6},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_for_early_positive_only","changed_components":["asp_or_spread_score","margin_bridge_score","spread_reversal_risk_score","positioning_overheat_score"],"component_delta_explanation":"Promote early benchmark spread + volume route; cap late record-profit proof after peak.","MFE_90D_pct":22.26,"MAE_90D_pct":-17.32,"score_return_alignment_label":"best_alignment","current_profile_verdict":"shadow_only"}
{"row_type":"residual_contribution","round":"R4","loop":"141","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["late_spread_confirmation_false_positive","spread_supercycle_mean_reversion_high_MAE","freight_rate_and_refining_margin_post_peak_drawdown","record_profit_after_peak_green_lateness"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C15_011200_20210813_CONTAINER_FREIGHT_BLOCKED","symbol":"011200","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reason":"HMM container freight supercycle is analytically relevant but the stock-web profile lists a corporate-action candidate date on 2021-11-16 inside the 180D forward window from the 2021-08-13 earnings trigger; therefore this loop does not emit a calibration trigger row for HMM.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R4
completed_loop = 141
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / over_50_rows_quality_repair / C15 rows 73
next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_4C_REPAIR, C22_INSURANCE_RATE_CYCLE_RESERVE_URL_REPAIR, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_REVERSAL_REPAIR, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_quality_repair, C24_BIO_TRIAL_DATA_EVENT_RISK_quality_repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

The source notes are URLs embedded in the evidence map and JSONL `evidence_source` fields. External sources are used only for historical event timing and evidence-family classification. Price calculations are from stock-web tradable OHLC shards.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
