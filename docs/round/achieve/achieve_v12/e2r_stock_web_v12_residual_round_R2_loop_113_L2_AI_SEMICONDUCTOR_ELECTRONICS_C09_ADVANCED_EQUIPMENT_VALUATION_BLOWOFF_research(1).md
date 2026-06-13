# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Metadata

```yaml
selected_round: R2
selected_loop: 113
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: mixed_C09_advanced_equipment_valuation_blowoff_set
research_file_name: e2r_stock_web_v12_residual_round_R2_loop_113_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
previous_index_state: C09 rows 10 / symbols 10 / positive 0 / counterexample 10 / 4B 3 / 4C 0 / need_to_30 20
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective: coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
stock_web_price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_count: 3
current_profile_error_count: 4
source_proxy_only_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
```

## 1. Current Calibrated Profile Assumption

Active profile assumed: `e2r_2_2_rolling_calibrated`.

The current C09 profile already has valuation-blowoff awareness, but this loop stresses the remaining split between:

1. real advanced-equipment order/customer/margin conversion, and
2. optionality narratives that peak quickly and leave a deep 180D MAE tail.

C09 is not a generic semiconductor-equipment bucket. It is the expensive edge of equipment: overlay/metrology, inspection, EUV mask/pellicle, advanced etch, advanced frontend process equipment. The calibration question is whether the evidence has crossed from “technology optionality” to “signed order + shipment + margin bridge.”

## 2. Scope

```text
included: historical C09 advanced-equipment triggers with stock-web tradable OHLC path
included: Stage2 / Stage2-Actionable / Stage4B comparison
included: positive cases, counterexamples, 4B timing audit, high-MAE guardrail
excluded: live watchlist, current recommendation, production scoring patch, stock_agent code changes
excluded: price-only trigger construction without non-price evidence
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index ledger state used only as a duplicate/coverage ledger. The current index shows C09 as a Priority 0 under-covered canonical with 10 rows and top covered symbols `031980`, `036810`, `039030`, `042700`, `079370`, `089030`.

This loop intentionally avoids those top-covered C09 symbols and adds five independent symbols:

```text
322310 오로스테크놀로지
348210 넥스틴
240810 원익IPS
319660 피에스케이
101490 에스앤에스텍
```

Duplicate hard-key check applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row repeats the top-covered C09 symbol set shown in the index. This does not claim the entire registry has never seen the symbols in another canonical; it only asserts no deliberate reuse of the known C09 top-covered keys and no reuse from this session's recent generated files.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest state used for all price rows:

```yaml
source_repo: https://github.com/Songdaiki/stock-web
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
mfe_mae_formula: high/low from entry_date through N trading days versus entry_date close
entry_price_rule: entry_date c column
```

| symbol | profile_path | price_shard_path | status |
|---|---|---|---|
| 322310 | `atlas/symbol_profiles/322/322310.json` | `atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv` + next-year shard where needed | tradable_raw / 180D usable / no_overlap_180D_window |
| 348210 | `atlas/symbol_profiles/348/348210.json` | `atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv` + next-year shard where needed | tradable_raw / 180D usable / no_overlap_180D_window |
| 240810 | `atlas/symbol_profiles/240/240810.json` | `atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv` + next-year shard where needed | tradable_raw / 180D usable / no_overlap_180D_window |
| 319660 | `atlas/symbol_profiles/319/319660.json` | `atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv` + next-year shard where needed | tradable_raw / 180D usable / no_overlap_180D_window |
| 101490 | `atlas/symbol_profiles/101/101490.json` | `atlas/ohlcv_tradable_by_symbol_year/101/101490/2024.csv` + next-year shard where needed | tradable_raw / 180D usable / no_overlap_180D_window |


## 5. Historical Eligibility Gate

All five representative rows pass the V12 trigger-row hard gate:

```yaml
trigger_date_is_historical: true
entry_date_in_stock_web_tradable_shard: true
entry_price_is_entry_date_close: true
forward_window_trading_days_gte_180: true
MFE_30D_pct_present: true
MFE_90D_pct_present: true
MFE_180D_pct_present: true
MAE_30D_pct_present: true
MAE_90D_pct_present: true
MAE_180D_pct_present: true
corporate_action_window_status: no_overlap_180D_window
calibration_usable: true
```

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep sub-archetype in this loop | compression rule |
|---|---|---|
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | overlay metrology customer expansion | Stage2 allowed if customer/order route exists; Green blocked until margin bridge survives peak drawdown |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | inspection equipment China order reopen | cap at Stage2 unless signed order/backlog and shipment timing visible |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | broad frontend equipment loss-narrowing | loss reduction is not Stage3; require operating profit and capex timing confirmation |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | estimate-cut 4B too early | estimate cut alone should not become hard 4B/4C if customer/new equipment evidence remains alive |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | EUV mask/pellicle optional revenue delay | optional EUV revenue needs qualification/ramp/revenue timing before Green |

## 7. Case Selection Summary

| # | symbol | company | trigger_type | trigger_date | entry_date | entry_price | role | verdict | outcome |
|---:|---|---|---|---|---|---:|---|---|---|
| 1 | 322310 | 오로스테크놀로지 | Stage2-Actionable | 2024-01-16 | 2024-01-17 | 26950 | positive | current_profile_correct | overlay_metrology_customer_expansion_positive_but_stage3_green_needs_post_peak_4B_guard |
| 2 | 348210 | 넥스틴 | Stage2-Actionable | 2024-01-10 | 2024-01-11 | 71700 | counterexample | current_profile_false_positive | china_order_reopen_high_mae_false_positive_without_signed_order_bridge |
| 3 | 240810 | 원익IPS | Stage2 | 2024-08-09 | 2024-08-12 | 35950 | counterexample | current_profile_false_positive | loss_reduction_and_memory_capa_rebound_false_positive_without_actual_profit_bridge |
| 4 | 319660 | 피에스케이 | Stage4B | 2024-11-20 | 2024-11-21 | 17540 | positive | current_profile_4B_too_early | estimate_cut_4b_too_early_positive_follow_through_when_non_price_thesis_survives |
| 5 | 101490 | 에스앤에스텍 | Stage2-Actionable | 2024-01-26 | 2024-01-29 | 43750 | counterexample | current_profile_false_positive | euv_optional_revenue_delay_counterexample_high_mae_after_stage2_hype |


## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 2
counterexample_count: 3
positive_cases:
  - 322310: positive Stage2-Actionable with 51.21% 180D MFE, but Green needs 4B post-peak guard because 180D MAE reached -43.86%.
  - 319660: Stage4B too-early counter-guard; estimate cut did not break the thesis and 180D MFE reached 29.70% with MAE contained at -11.35%.
counterexamples:
  - 348210: China/JV order-reopen narrative peaked fast and produced -43.72% 180D MAE.
  - 240810: loss-reduction / H2 recovery trigger produced only 7.09% 180D MFE and -42.14% 180D MAE.
  - 101490: EUV optionality trigger produced only 12.91% 180D MFE and -49.26% 180D MAE.
```

## 9. Evidence Source Map

| symbol | source | as-of evidence used |
|---|---|---|
| 322310 | https://www.sisajournal-e.com/news/articleView.html?idxno=307121 ; https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%98%A4%EB%A1%9C%EC%8A%A4%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80.pdf | 2024-01-16 article reported expected record revenue, new overlay metrology product sales, Samsung/China customer diversification, and packaging overlay expansion; 2024-03-27 report later confirmed HBM inspection/metrology benefit but also noted high 2024E valuation. |
| 348210 | https://www.inews24.com/view/1674592 ; https://securities.miraeasset.com/bbs/download/2128178.pdf?attachmentId=2128178 | 2024-01-10 coverage cited expected H2 order increase from China JV visibility, new fabs, domestic customer investment restart, and a target price hike. |
| 240810 | https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/08/08/IPS_240809.pdf | 2024-08-09 earnings review showed 2Q24 revenue +15% YoY and narrower operating loss, with DRAM equipment driving sales, but also continued operating loss, foundry schedule delay, and slow NAND recovery. |
| 319660 | https://www.businesspost.co.kr/BP?command=article_view&num=373456 | 2024-11-20 article reported target price cut and 2024/2025 estimate reductions, but also noted 3Q OP beat, overseas customer demand, Chinese customer expansion, and new etch equipment expectation. |
| 101490 | https://ssl.pstatic.net/imgstock/upload/research/company/1706230717692.pdf ; https://www.newsis.com/view/NISX20240730_0002830526 | 2024-01-26 SK report projected 2024/2025 sales and earnings growth from blank mask supplier advantage and EUV-related revenue, while later 2024-07-30 coverage reported EUV pellicle/blank mask revenue recognition delay to 2026. |


## 10. Price Data Source Map

See Section 4 for profile/shard paths. Entry dates are next stock-web tradable dates because publication time was either unknown or not cleanly available for same-day close eligibility.

## 11. Case-by-Case Trigger Grid

| symbol | Stage2 evidence | Stage3 evidence | Stage4B evidence | Stage4C evidence | residual conclusion |
|---|---|---|---|---|---|
| 322310 | record revenue estimate, new overlay product, Samsung/China customer expansion | profit-turnaround estimate and customer diversification | early peak then -62.87% post-peak drawdown | none | Stage2 positive; Green should be blocked until conversion survives local blowoff |
| 348210 | target hike, China JV visibility, H2 order expectation | no signed order/shipment/margin bridge at trigger | local peak within 30D, -43.72% 180D MAE | none | optional China order reopen is not Stage3 |
| 240810 | consensus beat and loss narrowing | still operating loss and delayed foundry | high MAE and capex timing mismatch | none | loss narrowing is Stage2 ceiling, not Green |
| 319660 | overseas customers and new etch equipment remain alive | 3Q OP beat and 2025 OP growth expectation | target cut and estimate reduction | none | estimate cut is 4B watch, not thesis break |
| 101490 | blank mask supplier advantage and EUV revenue estimate | no customer qualification/ramp/revenue timing confirmed | optional revenue delay risk and later delay validation | none | EUV optionality should be capped below Stage3 |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | forward_window_trading_days |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 322310 | 2024-01-17 | 26950 | 51.21 | -2.23 | 51.21 | -14.29 | 51.21 | -43.86 | 2024-02-27 | 40750 | -62.87 | 475 |
| 348210 | 2024-01-11 | 71700 | 9.90 | -7.81 | 9.90 | -22.59 | 9.90 | -43.72 | 2024-01-25 | 78800 | -48.79 | 479 |
| 240810 | 2024-08-12 | 35950 | 7.09 | -23.09 | 7.09 | -41.17 | 7.09 | -42.14 | 2024-08-21 | 38500 | -45.97 | 335 |
| 319660 | 2024-11-21 | 17540 | 9.52 | -11.35 | 29.70 | -11.35 | 29.70 | -11.35 | 2025-03-24 | 22750 | -28.44 | 269 |
| 101490 | 2024-01-29 | 43750 | 12.91 | -13.03 | 12.91 | -13.03 | 12.91 | -49.26 | 2024-03-13 | 49400 | -55.06 | 467 |


MFE/MAE calculation uses entry-date close as entry price and max high / min low from entry date through each N-trading-day window.

## 13. Current Calibrated Profile Stress Test

| symbol | expected current-profile action | observed path | stress result |
|---|---|---|---|
| 322310 | Stage2-Actionable allowed, Green delayed | 51.21% MFE but -43.86% 180D MAE | current profile mostly correct, but needs post-peak guard |
| 348210 | Stage2 cap / avoid Green | 9.90% MFE vs -43.72% MAE | false-positive risk if China narrative gets Stage3 weight |
| 240810 | Stage2 cap / avoid Green | 7.09% MFE vs -42.14% MAE | false-positive risk if loss narrowing is over-weighted |
| 319660 | 4B watch but no thesis-break route | 29.70% 180D MFE, -11.35% MAE | 4B too early if estimate cut dominates surviving customer evidence |
| 101490 | Stage2 cap / 4B watch after local peak | 12.91% MFE vs -49.26% MAE | false positive if EUV optionality gets Green treatment |

## 14. Stage2 / Yellow / Green Comparison

C09 should separate three rungs:

```text
Stage2: credible technology/customer/order optionality exists.
Stage2-Actionable: customer route plus near-term order/shipment/margin bridge is plausible.
Stage3-Yellow: backlog/order/shipment/revision is confirmed but valuation or timing risk remains.
Stage3-Green: order-to-revenue and margin conversion are confirmed, with drawdown and timing risk contained.
```

This loop does not produce a clean Stage3-Green row. That is itself useful: C09's under-covered matrix had many counterexamples and few positives; the clean positive profile should remain narrow.

## 15. 4B Timing Audit

| symbol | 4B timing verdict | reason |
|---|---|---|
| 322310 | 4B after local peak needed | 51.21% MFE came early; subsequent post-peak drawdown reached -62.87% |
| 348210 | 4B local peak guard missing | peak on 2024-01-25, followed by -48.79% post-peak drawdown |
| 240810 | 4B needed after failed loss-turn bridge | early peak on 2024-08-21, then -45.97% post-peak drawdown |
| 319660 | 4B too early | estimate cut did not break overseas customer/new-equipment thesis; 180D MAE was contained |
| 101490 | 4B after optionality-delay signal needed | EUV optional revenue did not convert; later delay narrative validated the cap |

## 16. 4C Protection Audit

No hard 4C route is proposed in this loop.

```text
No row contains order cancellation, customer qualification failure, accounting/trust break, regulatory rejection, or equipment thesis break.
```

The important correction is therefore not stronger 4C. It is a cleaner 4B split:

```text
optional advanced-equipment narrative -> Stage2 cap / 4B watch
confirmed order-to-margin conversion -> Stage2-Actionable / Yellow
estimate cut while customer thesis survives -> not hard 4B/4C
```

## 17. Sector-specific Rule Candidate

```yaml
sector_specific_rule_candidate: L2_C09_ADVANCED_EQUIPMENT_ORDER_MARGIN_BRIDGE_VS_OPTIONALITY_BLOWOFF_SPLIT
rule_text: >
  In L2 advanced equipment, Stage3 requires visible signed order, backlog/shipment timing, or revision/margin conversion.
  Technology optionality, China localization narrative, EUV qualification expectation, and loss-narrowing alone must remain capped at Stage2/Stage2-Actionable.
  If peak occurs within 30-60 trading days and no new non-price confirmation appears, activate 4B timing watch even when the original thesis remains credible.
```

## 18. Canonical-archetype Rule Candidate

```yaml
canonical_archetype_rule_candidate: C09_SIGNED_ORDER_MARGIN_BRIDGE_AND_OPTIONALITY_4B_CAP
positive_gate:
  - named customer/order route
  - shipment/backlog timing visibility
  - revision or OP-margin conversion
  - no immediate valuation-only blowoff
counterexample_gate:
  - target price raise without signed order
  - China/JV/localization narrative without shipment timing
  - EUV optional revenue without qualification/ramp/revenue timing
  - loss-narrowing while still operating-loss negative
4B_gate:
  - local peak within 30-60D
  - 180D MAE below -30%
  - post-peak no incremental non-price confirmation
4B_too_early_exception:
  - estimate cut only
  - overseas customer/new-equipment evidence survives
  - 180D MAE contained and MFE persists
```

## 19. Before/After Backtest Comparison

| rule state | false-positive pressure | missed-positive pressure | expected improvement |
|---|---:|---:|---|
| before C09 split | high for optionality headlines | moderate for estimate-cut recovery | Stage3 too easy when narrative is advanced/technical |
| after C09 split | lower for 348210/240810/101490 type rows | lower for 319660 type row | better distinction between optionality blowoff and true order-margin bridge |

## 20. Score-Return Alignment Matrix

| symbol | 180D MFE | 180D MAE | desired score alignment |
|---|---:|---:|---|
| 322310 | 51.21 | -43.86 | Stage2 positive but Green blocked by drawdown/valuation guard |
| 348210 | 9.90 | -43.72 | low Stage2 / 4B watch |
| 240810 | 7.09 | -42.14 | Stage2 ceiling, no Stage3 |
| 319660 | 29.70 | -11.35 | avoid over-penalizing estimate cut if customer thesis survives |
| 101490 | 12.91 | -49.26 | optional EUV revenue cap below Stage3 |

## 21. Coverage Matrix

```yaml
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
previous_index_rows: 10
new_representative_rows_this_loop: 5
expected_rows_after_acceptance: 15
new_symbols:
  - 322310
  - 348210
  - 240810
  - 319660
  - 101490
new_fine_trigger_families:
  - overlay_metrology_customer_expansion_with_blowoff_risk
  - inspection_equipment_china_order_reopen_high_MAE_counterexample
  - broad_frontend_equipment_loss_reduction_false_positive
  - frontend_equipment_estimate_cut_4B_too_early_recovery
  - EUV_mask_pellicle_optional_revenue_delay_counterexample
```

## 22. Residual Contribution Summary

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed:
  - C09_SIGNED_ORDER_MARGIN_BRIDGE_AND_OPTIONALITY_4B_CAP
  - C09_ESTIMATE_CUT_NOT_HARD_4B_IF_CUSTOMER_THESIS_SURVIVES
  - C09_EUV_OPTIONAL_REVENUE_DELAY_CAP
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable shard entry date
- entry price as entry-date close
- 30D/90D/180D MFE and MAE
- 180D corporate-action window non-contamination based on symbol profiles
- canonical/round/large-sector consistency
```

Not validated:

```text
- intraday publication time for same-day entry eligibility
- adjusted-price restatement after future corporate-action logic
- production scoring impact
- current live attractiveness of any symbol
```

## 24. Shadow Weight Calibration

```csv
row_type,round,loop,large_sector_id,canonical_archetype_id,weight_axis,proposed_delta,reason
shadow_weight,R2,113,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,earnings_visibility,+0.03,"Stage3 should require order/shipment/revision or operating-profit conversion rather than optionality narrative."
shadow_weight,R2,113,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,information_confidence,+0.02,"EUV/China/localization claims need explicit confirmation before Green."
shadow_weight,R2,113,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,valuation_rerating,-0.02,"Valuation rerating alone created multiple high-MAE paths."
shadow_weight,R2,113,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,market_mispricing,-0.01,"Optionality narratives should not receive full mispricing credit without margin bridge."
```

## 25. Machine-Readable Rows

### trigger_rows_representative.jsonl

```jsonl
{"row_type":"trigger","trigger_id":"T-C09-R2-L113-01-322310-2024-01-17","case_id":"C09_R2_L113_322310_20240117","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_OVERLAY_METROLOGY_CUSTOMER_EXPANSION_WITH_BLOWOFF_RISK","sector":"semiconductor_equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-16","evidence_available_at_that_date":"2024-01-16 article reported expected record revenue, new overlay metrology product sales, Samsung/China customer diversification, and packaging overlay expansion; 2024-03-27 report later confirmed HBM inspection/metrology benefit but also noted high 2024E valuation.","evidence_source":"https://www.sisajournal-e.com/news/articleView.html?idxno=307121 ; https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%98%A4%EB%A1%9C%EC%8A%A4%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80.pdf","stage2_evidence_fields":"record_revenue_estimate; overlay_metrology_new_product; samsung_china_customer_expansion; packaging_overlay_expansion","stage3_evidence_fields":"profit_turnaround_estimate; 2024_consensus_revenue_OP_step_up; customer_diversification_visible","stage4b_evidence_fields":"180D_MAE_deep_after_early_peak; valuation_multiple_high_after_theme_rally; post_peak_drawdown_requires_4B_overlay","stage4c_evidence_fields":"none","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","profile_path":"atlas/symbol_profiles/322/322310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-17","entry_price":26950.0,"MFE_30D_pct":51.21,"MFE_90D_pct":51.21,"MFE_180D_pct":51.21,"MFE_1Y_pct":51.21,"MFE_2Y_pct":null,"MAE_30D_pct":-2.23,"MAE_90D_pct":-14.29,"MAE_180D_pct":-43.86,"MAE_1Y_pct":-51.09,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":40750.0,"drawdown_after_peak_pct":-62.87,"green_lateness_ratio":null,"four_b_local_peak_proximity":-33.87,"four_b_full_window_peak_proximity":-33.87,"four_b_timing_verdict":"4B_after_local_peak_needed","four_b_evidence_type":"non_price_required; valuation_or_estimate_timing_not_price_only","four_c_protection_label":"not_4C_no_hard_thesis_break","trigger_outcome_label":"overlay_metrology_customer_expansion_positive_but_stage3_green_needs_post_peak_4B_guard","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":475,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"322310_2024-01-17_26950.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive","residual_contribution":"Positive Stage2-Actionable was justified, but Green should stay gated by durable order-to-margin conversion and post-peak drawdown guard.","aggregate_metric_inclusion":true}
{"row_type":"trigger","trigger_id":"T-C09-R2-L113-02-348210-2024-01-11","case_id":"C09_R2_L113_348210_20240111","symbol":"348210","company_name":"넥스틴","round":"R2","loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_INSPECTION_EQUIPMENT_CHINA_ORDER_REOPEN_HIGH_MAE_COUNTEREXAMPLE","sector":"semiconductor_equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","evidence_available_at_that_date":"2024-01-10 coverage cited expected H2 order increase from China JV visibility, new fabs, domestic customer investment restart, and a target price hike.","evidence_source":"https://www.inews24.com/view/1674592 ; https://securities.miraeasset.com/bbs/download/2128178.pdf?attachmentId=2128178","stage2_evidence_fields":"target_price_raise; china_JV_visibility; domestic_customer_investment_reopen; H2_order_increase_expectation","stage3_evidence_fields":"none_confirmed_at_trigger; no_actual_order_backlog_margin_bridge_in_trigger_evidence","stage4b_evidence_fields":"local_peak_within_30D; 180D_MAE_minus_43_72; positive_news_without_signed_order_or_margin_conversion","stage4c_evidence_fields":"none","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv","profile_path":"atlas/symbol_profiles/348/348210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-11","entry_price":71700.0,"MFE_30D_pct":9.9,"MFE_90D_pct":9.9,"MFE_180D_pct":9.9,"MFE_1Y_pct":9.9,"MFE_2Y_pct":null,"MAE_30D_pct":-7.81,"MAE_90D_pct":-22.59,"MAE_180D_pct":-43.72,"MAE_1Y_pct":-43.72,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-25","peak_price":78800.0,"drawdown_after_peak_pct":-48.79,"green_lateness_ratio":null,"four_b_local_peak_proximity":-9.01,"four_b_full_window_peak_proximity":-9.01,"four_b_timing_verdict":"4B_after_local_peak_needed","four_b_evidence_type":"non_price_required; valuation_or_estimate_timing_not_price_only","four_c_protection_label":"not_4C_no_hard_thesis_break","trigger_outcome_label":"china_order_reopen_high_mae_false_positive_without_signed_order_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":479,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"348210_2024-01-11_71700.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","residual_contribution":"C09 should not treat China/JV/localization narrative as Stage3 unless backlog, shipment timing, and margin conversion are already visible.","aggregate_metric_inclusion":true}
{"row_type":"trigger","trigger_id":"T-C09-R2-L113-03-240810-2024-08-12","case_id":"C09_R2_L113_240810_20240812","symbol":"240810","company_name":"원익IPS","round":"R2","loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_BROAD_FRONTEND_EQUIPMENT_LOSS_REDUCTION_FALSE_POSITIVE","sector":"semiconductor_equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-08-09","evidence_available_at_that_date":"2024-08-09 earnings review showed 2Q24 revenue +15% YoY and narrower operating loss, with DRAM equipment driving sales, but also continued operating loss, foundry schedule delay, and slow NAND recovery.","evidence_source":"https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/08/08/IPS_240809.pdf","stage2_evidence_fields":"2Q24_consensus_beat; loss_reduction; DRAM_equipment_sales_rebound; H2_profit_turn_expectation","stage3_evidence_fields":"none_confirmed; still_operating_loss; foundry_delay; NAND_recovery_slow","stage4b_evidence_fields":"operating_loss_continued; customer_capex_timing_mismatch; early_peak_then_high_MAE","stage4c_evidence_fields":"none","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-12","entry_price":35950.0,"MFE_30D_pct":7.09,"MFE_90D_pct":7.09,"MFE_180D_pct":7.09,"MFE_1Y_pct":20.58,"MFE_2Y_pct":null,"MAE_30D_pct":-23.09,"MAE_90D_pct":-41.17,"MAE_180D_pct":-42.14,"MAE_1Y_pct":-42.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-21","peak_price":38500.0,"drawdown_after_peak_pct":-45.97,"green_lateness_ratio":null,"four_b_local_peak_proximity":-6.62,"four_b_full_window_peak_proximity":-6.62,"four_b_timing_verdict":"4B_after_local_peak_needed","four_b_evidence_type":"non_price_required; valuation_or_estimate_timing_not_price_only","four_c_protection_label":"not_4C_no_hard_thesis_break","trigger_outcome_label":"loss_reduction_and_memory_capa_rebound_false_positive_without_actual_profit_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":335,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"240810_2024-08-12_35950.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","residual_contribution":"For broad frontend equipment, Stage2 should remain capped when the trigger is loss-narrowing rather than confirmed operating profit and backlog-to-revenue conversion.","aggregate_metric_inclusion":true}
{"row_type":"trigger","trigger_id":"T-C09-R2-L113-04-319660-2024-11-21","case_id":"C09_R2_L113_319660_20241121","symbol":"319660","company_name":"피에스케이","round":"R2","loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_FRONTEND_EQUIPMENT_ESTIMATE_CUT_4B_TOO_EARLY_RECOVERY","sector":"semiconductor_equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-11-20","evidence_available_at_that_date":"2024-11-20 article reported target price cut and 2024/2025 estimate reductions, but also noted 3Q OP beat, overseas customer demand, Chinese customer expansion, and new etch equipment expectation.","evidence_source":"https://www.businesspost.co.kr/BP?command=article_view&num=373456","stage2_evidence_fields":"overseas_customer_order_expectation; new_etch_equipment_completion_expectation; china_customer_expansion","stage3_evidence_fields":"3Q24_OP_above_market_expectation; 2025_OP_growth_forecast; overseas_customer_demand_increase","stage4b_evidence_fields":"target_price_cut; estimate_revision_down; domestic_capa_expansion_not_visible","stage4c_evidence_fields":"none; negative_estimate_revision_not_thesis_break_because_overseas_customer_and_new_equipment_optionalities_remained","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-21","entry_price":17540.0,"MFE_30D_pct":9.52,"MFE_90D_pct":29.7,"MFE_180D_pct":29.7,"MFE_1Y_pct":136.03,"MFE_2Y_pct":null,"MAE_30D_pct":-11.35,"MAE_90D_pct":-11.35,"MAE_180D_pct":-11.35,"MAE_1Y_pct":-11.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-24","peak_price":22750.0,"drawdown_after_peak_pct":-28.44,"green_lateness_ratio":null,"four_b_local_peak_proximity":-22.9,"four_b_full_window_peak_proximity":-22.9,"four_b_timing_verdict":"4B_too_early","four_b_evidence_type":"non_price_required; valuation_or_estimate_timing_not_price_only","four_c_protection_label":"not_4C_no_hard_thesis_break","trigger_outcome_label":"estimate_cut_4b_too_early_positive_follow_through_when_non_price_thesis_survives","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":269,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"319660_2024-11-21_17540.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive","residual_contribution":"Estimate cuts alone should create 4B watch, not thesis-break routing, when order/customer/new-equipment evidence remains alive and MAE is contained.","aggregate_metric_inclusion":true}
{"row_type":"trigger","trigger_id":"T-C09-R2-L113-05-101490-2024-01-29","case_id":"C09_R2_L113_101490_20240129","symbol":"101490","company_name":"에스앤에스텍","round":"R2","loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_EUV_MASK_PELLICLE_OPTIONAL_REVENUE_DELAY_COUNTEREXAMPLE","sector":"semiconductor_equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","evidence_available_at_that_date":"2024-01-26 SK report projected 2024/2025 sales and earnings growth from blank mask supplier advantage and EUV-related revenue, while later 2024-07-30 coverage reported EUV pellicle/blank mask revenue recognition delay to 2026.","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1706230717692.pdf ; https://www.newsis.com/view/NISX20240730_0002830526","stage2_evidence_fields":"blank_mask_supplier_advantage; EUV_blank_mask_and_pellicle_revenue_forecast; china_blank_mask_growth; margin_forecast","stage3_evidence_fields":"none_confirmed_at_trigger; 2025_EUV_revenue_optional_and_not_order_confirmed","stage4b_evidence_fields":"optional_EUV_revenue_timing_risk; valuation_multiple_high; later_EUV_timing_delay_validated","stage4c_evidence_fields":"none","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101490/2024.csv","profile_path":"atlas/symbol_profiles/101/101490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-29","entry_price":43750.0,"MFE_30D_pct":12.91,"MFE_90D_pct":12.91,"MFE_180D_pct":12.91,"MFE_1Y_pct":12.91,"MFE_2Y_pct":null,"MAE_30D_pct":-13.03,"MAE_90D_pct":-13.03,"MAE_180D_pct":-49.26,"MAE_1Y_pct":-56.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":49400.0,"drawdown_after_peak_pct":-55.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":-11.44,"four_b_full_window_peak_proximity":-11.44,"four_b_timing_verdict":"4B_after_local_peak_needed","four_b_evidence_type":"non_price_required; valuation_or_estimate_timing_not_price_only","four_c_protection_label":"not_4C_no_hard_thesis_break","trigger_outcome_label":"euv_optional_revenue_delay_counterexample_high_mae_after_stage2_hype","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":467,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"101490_2024-01-29_43750.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","residual_contribution":"EUV optionality should be capped below Stage3 until customer qualification, production ramp, and revenue timing are confirmed.","aggregate_metric_inclusion":true}
```

### aggregate.jsonl

```jsonl
{"row_type":"aggregate","aggregate_id":"AGG-C09-R2-L113","round":"R2","loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","representative_trigger_count":5,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":4,"current_profile_false_positive_count":3,"median_MFE_180D_pct":12.91,"median_MAE_180D_pct":-43.72,"rule_candidate":"C09_SIGNED_ORDER_MARGIN_BRIDGE_AND_OPTIONALITY_4B_CAP","calibration_usable_rows":5}
```

### residual_contribution.jsonl

```jsonl
{"row_type":"residual_contribution","residual_id":"RES-C09-R2-L113","round":"R2","loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_axis_proposed":"C09_SIGNED_ORDER_MARGIN_BRIDGE_AND_OPTIONALITY_4B_CAP | C09_ESTIMATE_CUT_NOT_HARD_4B_IF_CUSTOMER_THESIS_SURVIVES | C09_EUV_OPTIONAL_REVENUE_DELAY_CAP","existing_axis_strengthened":"price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence","existing_axis_weakened":"none","summary":"C09 needs stronger separation between confirmed advanced-equipment order-to-margin conversion and optionality/valuation headline rallies."}
```

## 26. Deferred Coding Agent Handoff Prompt

```text
Working directory: /home/eorb915/projects/stock_agent

Goal:
Ingest this standalone V12 residual research MD as a C09 advanced-equipment valuation-blowoff calibration addition.

Required checks:
1. Verify filename matches metadata exactly.
2. Parse five row_type=trigger JSONL rows.
3. Confirm canonical_archetype_id=C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF and large_sector_id=L2_AI_SEMICONDUCTOR_ELECTRONICS.
4. Confirm each row has entry_date, entry_price, MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
5. Confirm corporate_action_window_status=no_overlap_180D_window.
6. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
7. Add rows only if no existing registry row has the same hard key.
8. Treat proposed weights as shadow candidates only; do not auto-apply production scoring without aggregate batch support.

Candidate implementation note:
If batch support accepts this loop, test C09_SIGNED_ORDER_MARGIN_BRIDGE_AND_OPTIONALITY_4B_CAP as a shadow rule:
- raise Stage3 threshold for C09 rows lacking signed order/backlog/shipment/margin conversion;
- activate 4B timing watch for optionality narratives with early peak and 180D MAE <= -30%;
- avoid hard 4B/4C routing for estimate-cut-only cases where customer/new-equipment evidence survives.
```

## 27. Next Round State

```yaml
next_recommended_archetype: C14_EV_DEMAND_SLOWDOWN_4B_4C
supplementary_next:
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
reason: C09 would move from 10 to 15 expected rows after acceptance; C14/C10 remain Priority 0 under-covered and are suitable for 4B/4C residual mining.
```

## 28. Source Notes

Primary procedure sources:

```text
MAIN EXECUTION PROMPT:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md

STOCK-WEB MANIFEST:
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json

STOCK-WEB SCHEMA:
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
```

Evidence sources are listed in Sections 9 and 25. Price rows were computed directly from stock-web tradable CSV shards downloaded from `atlas/ohlcv_tradable_by_symbol_year`.

## Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
metadata_round_loop_matches_filename: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
future_data_leakage_detected: false
production_code_patch_included: false
production_scoring_patch_applied: false
```
