# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- selected_round: `R2`
- selected_loop: `112`
- selected_priority_bucket: `Priority 1-under-50 after local-session adjustment; published index Priority 0`
- round_schedule_status: `coverage_index_selected`
- round_sector_consistency: `pass`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
- fine_archetype_id: `C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE`
- deep_sub_archetype_id: `C06_DEEP_PACKAGE_SUBSTRATE_OSAT_RELIABILITY_TEST_AND_AI_SERVER_PCB_PROXY_VS_DIRECT_CUSTOMER_CAPACITY_LOCK`
- loop_objective: `coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery`
- output_file: `e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md`
- production_scoring_changed: `false`
- shadow_weight_only: `true`

This loop adds 7 new independent cases, 4 counterexamples, and 7 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are treated as baseline assumptions, not as discoveries: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, and `hard_4c_thesis_break_routes_to_4c=true`.

This MD does not recommend any live trade or live watchlist. It only tests historical Stage2-Actionable C06 proxy rows against the stock-web 1D OHLCV path.

## 2. Round / Large Sector / Canonical Archetype Scope

C06 belongs to R2 / L2. The scope is not generic semiconductor equipment; it is HBM memory/customer/capacity exposure and adjacent supply-chain proxy compression. The new fine archetype compresses package substrate, OSAT, reliability test, and AI server PCB proxy rows into a C06-specific question:

> Does the HBM-adjacent proxy have direct customer capacity lock, verified shipment/revenue/margin bridge, or only a hot label?

## 3. Previous Coverage / Duplicate Avoidance Check

Published `V12_Research_No_Repeat_Index.md` shows C06 at 17 rows, needing 13 to reach 30 and 33 to reach 50. This session already added C06 loop108, loop109, loop110, and loop111, bringing the local-session adjusted count to about 45. This loop adds 7 new representative triggers and lifts C06 to about 52 local-session rows.

Excluded prior C06 symbol groups from this session: `000660`, `005930`, `042700`, `089030`, `232140`, `217190`, `222800`, `131290`, `095340`, `353200`, `005290`, `067310`, `036540`, `131970`, `033160`, `272290`, `080580`, `357780`, `007660`-adjacent direct memory-maker reuse was avoided. This loop uses a new proxy basket: `007660`, `330860`, `405100`, `007810`, `033640`, `061970`, `356860`. Although `007660` is an AI server PCB rather than memory maker, it has not been used in the prior C06 loop set and is treated as an HBM/customer-capacity proxy, not direct memory capacity.

Hard duplicate check: no reused `canonical_archetype_id + symbol + trigger_type + entry_date` group from this session.

## 4. Stock-Web OHLC Input / Price Source Validation

- price_data_source: `Songdaiki/stock-web`
- upstream_source: `FinanceData/marcap`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- stock_web_manifest_max_date: `2026-02-20`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- raw_shard_root: `atlas/ohlcv_raw_by_symbol_year`

All representative trigger rows use 2024 tradable shards. Entry dates are early enough to preserve a full 180-trading-day forward window inside stock-web data. Profile paths are recorded per symbol. Corporate-action candidates visible in profile metadata for these symbols are outside the 2024 entry-to-D+180 windows used here; `061970` has a 2025-02-21 candidate, outside the selected 2024 180D window.

## 5. Historical Eligibility Gate

| gate | result |
|---|---|
| trigger dates are historical | pass |
| entry dates exist in tradable shards | pass |
| forward window >= 180 trading days | pass |
| all 30/90/180D MFE/MAE fields present | pass |
| corporate-action contaminated 180D windows | none used |
| price source is stock-web tradable_raw | pass |
| calibration_usable trigger count | 7 |

## 6. Canonical Archetype Compression Map

| fine/deep route | compressed canonical | rule implication |
|---|---|---|
| AI server PCB / HBM traffic proxy | C06 | can remain Stage2-Actionable when MFE validates and drawdown is controlled |
| OSAT / package test capacity proxy | C06 | needs customer pull or revenue/margin confirmation before Yellow |
| reliability / qualification test proxy | C06 | may capture MFE but must carry local 4B watch after blowoff |
| package substrate / PCB label | C06 | not enough for Yellow/Green without verified HBM/customer bridge |
| advanced packaging label without revenue bridge | C06 | false-positive guard candidate |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---:|---|
| C06_L112_CASE_01_007660 | 007660 | 이수페타시스 | structural_success | positive | 103.33 | -2.41 | 121.11 | -2.41 | current_profile_missed_structural |
| C06_L112_CASE_02_330860 | 330860 | 네패스아크 | high_mae_success | positive | 90.55 | -5.13 | 90.55 | -50.72 | current_profile_4B_too_late |
| C06_L112_CASE_03_405100 | 405100 | 큐알티 | high_mae_success | positive | 173.58 | -1.7 | 173.58 | -25.03 | current_profile_4B_too_late |
| C06_L112_CASE_04_007810 | 007810 | 코리아써키트 | failed_rerating | counterexample | 7.49 | -31.79 | 7.49 | -56.04 | current_profile_false_positive |
| C06_L112_CASE_05_033640 | 033640 | 네패스 | failed_rerating | counterexample | 19.14 | -16.25 | 19.14 | -59.76 | current_profile_false_positive |
| C06_L112_CASE_06_061970 | 061970 | LB세미콘 | high_mae_counterexample | counterexample | 31.06 | -25.77 | 31.06 | -57.66 | current_profile_4B_too_late |
| C06_L112_CASE_07_356860 | 356860 | 티엘비 | failed_rerating | counterexample | 34.23 | -6.19 | 34.23 | -53.53 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: `3`
- counterexample_count: `4`
- high-MAE / local 4B watch paths: `6`
- current_profile_error_count: `7`

This loop intentionally does not prove that every HBM-adjacent proxy should be upgraded. It shows the opposite: C06 needs two gates. First, a bridge gate for direct capacity/customer/shipment/revenue/margin evidence. Second, a local 4B watch for proxy labels that produce fast MFE and then collapse.

## 9. Evidence Source Map

| symbol | evidence family | source quality | promotion status |
|---|---|---|---|
| 007660 | AI server PCB / HBM traffic capacity proxy | source_proxy_only | blocked until URL repair |
| 330860 | OSAT test capacity / HBM qualification proxy | source_proxy_only | blocked until URL repair |
| 405100 | reliability test / HBM qualification proxy | source_proxy_only | blocked until URL repair |
| 007810 | package substrate label without customer lock | source_proxy_only | counterexample usable for guard, not promotion |
| 033640 | advanced packaging label without revenue bridge | source_proxy_only | counterexample usable for guard, not promotion |
| 061970 | OSAT proxy local MFE without durable pull | source_proxy_only | counterexample / 4B watch |
| 356860 | memory PCB proxy without margin FCF bridge | source_proxy_only | counterexample / 4B watch |

## 10. Price Data Source Map

| symbol | shard | profile | entry_date | entry_price |
|---|---|---|---|---:|
| 007660 | `atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv` | `atlas/symbol_profiles/007/007660.json` | 2024-02-01 | 27000 |
| 330860 | `atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv` | `atlas/symbol_profiles/330/330860.json` | 2024-02-01 | 24350 |
| 405100 | `atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv` | `atlas/symbol_profiles/405/405100.json` | 2024-01-15 | 15900 |
| 007810 | `atlas/ohlcv_tradable_by_symbol_year/007/007810/2024.csv` | `atlas/symbol_profiles/007/007810.json` | 2024-02-15 | 20700 |
| 033640 | `atlas/ohlcv_tradable_by_symbol_year/033/033640/2024.csv` | `atlas/symbol_profiles/033/033640.json` | 2024-02-01 | 18340 |
| 061970 | `atlas/ohlcv_tradable_by_symbol_year/061/061970/2024.csv` | `atlas/symbol_profiles/061/061970.json` | 2024-03-15 | 7180 |
| 356860 | `atlas/ohlcv_tradable_by_symbol_year/356/356860/2024.csv` | `atlas/symbol_profiles/356/356860.json` | 2024-02-01 | 24250 |


## 11. Case-by-Case Trigger Grid

| symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict | outcome |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 007660 | 이수페타시스 | Stage2-Actionable | 2024-02-01 | 27000 | 57.59 | -2.41 | 103.33 | -2.41 | 121.11 | -2.41 | current_profile_missed_structural | ai_server_pcb_capacity_proxy_structural_success |
| 330860 | 네패스아크 | Stage2-Actionable | 2024-02-01 | 24350 | 90.55 | -5.13 | 90.55 | -5.13 | 90.55 | -50.72 | current_profile_4B_too_late | test_capacity_proxy_success_but_needs_4B_watch |
| 405100 | 큐알티 | Stage2-Actionable | 2024-01-15 | 15900 | 144.03 | -1.7 | 173.58 | -1.7 | 173.58 | -25.03 | current_profile_4B_too_late | reliability_qualification_proxy_success_then_blowoff |
| 007810 | 코리아써키트 | Stage2-Actionable | 2024-02-15 | 20700 | 7.49 | -14.98 | 7.49 | -31.79 | 7.49 | -56.04 | current_profile_false_positive | package_substrate_label_failed_rerating |
| 033640 | 네패스 | Stage2-Actionable | 2024-02-01 | 18340 | 19.14 | -4.8 | 19.14 | -16.25 | 19.14 | -59.76 | current_profile_false_positive | advanced_packaging_label_failed_rerating |
| 061970 | LB세미콘 | Stage2-Actionable | 2024-03-15 | 7180 | 31.06 | -1.81 | 31.06 | -25.77 | 31.06 | -57.66 | current_profile_4B_too_late | osat_proxy_local_mfe_then_deep_drawdown |
| 356860 | 티엘비 | Stage2-Actionable | 2024-02-01 | 24250 | 30.31 | -6.19 | 34.23 | -6.19 | 34.23 | -53.53 | current_profile_false_positive | memory_pcb_proxy_failed_after_midterm_mfe |

## 12. Trigger-Level OHLC Backtest Tables

All MFE/MAE values are calculated from the entry-date close using the 2024 stock-web tradable shard. Formula: `MFE_N_pct = max(high[entry:D+N]) / entry_price - 1`, `MAE_N_pct = min(low[entry:D+N]) / entry_price - 1`.

| symbol | peak_date | peak_price | drawdown_after_peak_pct | below_entry_30D | below_entry_90D | corporate_action_window_status |
|---|---|---:|---:|---|---|---|
| 007660 | 2024-07-03 | 59700 | -48.24 | false | false | clean_180D_window |
| 330860 | 2024-03-12 | 46400 | -74.14 | true | true | clean_180D_window |
| 405100 | 2024-03-05 | 43500 | -72.6 | false | false | clean_180D_window |
| 007810 | 2024-02-15 | 22250 | -59.1 | true | true | clean_180D_window |
| 033640 | 2024-03-12 | 21850 | -66.22 | true | true | clean_180D_window |
| 061970 | 2024-03-25 | 9410 | -67.69 | true | true | clean_180D_window |
| 356860 | 2024-05-09 | 32550 | -65.38 | true | true | clean_180D_window |


## 13. Current Calibrated Profile Stress Test

| residual type | affected symbols | interpretation |
|---|---|---|
| missed structural proxy success | 007660 | too strict if a proxy has clear customer-capacity path and strong MFE with low MAE |
| 4B too late after proxy blowoff | 330860, 405100, 061970, 356860 | fast MFE followed by deep peak-to-trough drawdown needs local 4B watch |
| false positive from HBM/package label | 007810, 033640 | label without verified customer lock / margin bridge should not become Yellow/Green |

Current profile error count is 7 because each case exposes either a missed positive, a false positive, or a too-late local 4B overlay inside C06.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is asserted from later outcomes. Green lateness is therefore `not_applicable:no_confirmed_Stage3_Green_trigger` for representative rows. The useful comparison is Stage2-Actionable vs post-entry path:

- Stage2-Actionable works for `007660`, `330860`, and `405100`, but `330860` and `405100` need local 4B watch after the blowoff.
- Stage2-Actionable is too permissive for `007810`, `033640`, `061970`, and `356860` if it is based only on an HBM-adjacent proxy label.
- Stage3-Yellow should require verified capacity/customer/revenue/margin bridge, not only a 2024 HBM label.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | timing verdict | drawdown_after_peak_pct |
|---|---|---|---:|
| 007660 | none | not_applicable_at_representative_entry | -48.24 |
| 330860 | price_only,positioning_overheat | needs_local_4B_watch_after_proxy_blowoff | -74.14 |
| 405100 | price_only,positioning_overheat | needs_local_4B_watch_after_proxy_blowoff | -72.6 |
| 007810 | price_only,positioning_overheat | needs_local_4B_watch_after_proxy_blowoff | -59.1 |
| 033640 | price_only,positioning_overheat | needs_local_4B_watch_after_proxy_blowoff | -66.22 |
| 061970 | price_only,positioning_overheat | needs_local_4B_watch_after_proxy_blowoff | -67.69 |
| 356860 | price_only,positioning_overheat | needs_local_4B_watch_after_proxy_blowoff | -65.38 |


A C06 proxy can produce very large MFE before the bridge is proven. That does not justify a full 4B unless non-price evidence deteriorates. But it does justify a local 4B watch when valuation/positioning overheat and the bridge is still proxy-only.

## 16. 4C Protection Audit

No hard Stage4C row is emitted in this loop. The drawdown paths are treated as local 4B / high-MAE guardrail evidence, not thesis-break 4C evidence. `four_c_protection_label=not_applicable_no_hard_4c` for all representative triggers.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate=true`, but the preferred scope is canonical-specific, because the same L2 semiconductor sector contains C07/C09/C10 where proxy equipment labels behave differently.

Candidate sector note: HBM-adjacent supply-chain names need proof of customer pull or shipment/revenue conversion before Yellow/Green; otherwise they remain Stage2-watch even when relative strength is high.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate=true`

Proposed C06 rule:

```text
C06_direct_HBM_customer_capacity_or_verified_proxy_revenue_margin_bridge_required_before_Yellow_or_Green_plus_proxy_blowoff_local_4B_watch
```

Mechanism:

1. Direct memory-maker customer/capacity/ASP/mix evidence can support Stage2-Actionable and possibly Yellow.
2. Proxy rows such as OSAT, package substrate, reliability test, PCB, or advanced packaging need at least one bridge: shipment, revenue, margin, customer lock, or verified capacity allocation.
3. If proxy-only rows generate fast MFE without bridge confirmation, do not promote to Green; attach local 4B watch after blowoff/positioning overheat.

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | existing bridge guard, but C06 proxy still noisy | 7 | 65.63 | -12.75 | 68.17 | -43.59 | 0.57 | noisy alignment |
| P0b e2r_2_0_baseline_reference | too permissive on RS / theme proxy | 7 | same | same | same | same | 0.71 | worse false positives |
| P1 sector_specific_candidate_profile | L2 proxy bridge guard | 7 | same sample | same sample | same sample | same sample | 0.43 | useful but broad |
| P2 canonical_C06_candidate_profile | direct/proxy bridge + local 4B watch | 7 | same sample | same sample | same sample | same sample | 0.29 | best explanatory fit |
| P3 counterexample_guard_profile | blocks all proxy labels until URL-verified | 7 | lower positive capture | better MAE | lower upside capture | better drawdown | 0.14 | too strict; misses 007660/405100 style positives |

## 20. Score-Return Alignment Matrix

| symbol | P0 judgement | P2 judgement | score_return_alignment |
|---|---|---|---|
| 007660 | too strict / missed structural proxy | keep Stage2-Actionable, allow Yellow after URL/revenue bridge | improved |
| 330860 | 4B too late | keep Stage2-Actionable but add local 4B watch | improved |
| 405100 | 4B too late | keep positive capture, add local 4B watch | improved |
| 007810 | false positive risk | Stage2-watch only until customer bridge | improved |
| 033640 | false positive risk | Stage2-watch only until margin/revenue bridge | improved |
| 061970 | local MFE then deep drawdown | local 4B watch after proxy blowoff | improved |
| 356860 | local MFE then deep drawdown | local 4B watch / no Yellow without FCF bridge | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE | 3 | 4 | 6 | 0 | 7 | 0 | 7 | 7 | 7 | true | true | local-session adjusted about 52; 50-row practical calibration band reached |

## 22. Residual Contribution Summary

- new_independent_case_count: `7`
- reused_case_count: `0`
- reused_case_ids: `[]`
- new_symbol_count: `7`
- new_canonical_archetype_count: `0`
- new_fine_archetype_count: `1`
- new_trigger_family_count: `7`
- tested_existing_calibrated_axes: `stage2_required_bridge`, `local_4b_watch_guard`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`
- residual_error_types_found: `proxy_label_false_positive`, `missed_structural_proxy_success`, `high_MAE_after_local_HBM_proxy_blowoff`
- new_axis_proposed: `C06_direct_HBM_customer_capacity_or_verified_proxy_revenue_margin_bridge_required_before_Yellow_or_Green_plus_proxy_blowoff_local_4B_watch`
- existing_axis_strengthened: `stage2_required_bridge`, `local_4b_watch_guard`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`
- existing_axis_weakened: `null`
- existing_axis_kept: `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `hard_4c_thesis_break_routes_to_4c`
- sector_specific_rule_candidate: `true`
- canonical_archetype_rule_candidate: `true`
- no_new_signal_reason: `null`
- loop_contribution_label: `canonical_archetype_rule_candidate`
- do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope

Validated:

- 2024 stock-web tradable shard presence.
- Entry-date close, 30/90/180D MFE and MAE.
- 180-trading-day forward window.
- Round/sector/canonical consistency.
- Representative trigger JSONL completeness.

Not validated in this MD:

- Production scoring code.
- Live watchlist or current candidate quality.
- Direct external evidence URLs for every proxy narrative. These rows are marked `source_proxy_only` and `promotion_blocked_until_url_repair=true` where applicable.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_customer_capacity_or_verified_proxy_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Proxy labels require direct customer capacity lock or verified shipment/revenue/margin bridge before Yellow/Green","reduces 4 false positives while keeping 3 structural/high-MFE cases","C06_L112_TRG_01_007660_STAGE2A|C06_L112_TRG_02_330860_STAGE2A|C06_L112_TRG_03_405100_STAGE2A|C06_L112_TRG_04_007810_STAGE2A|C06_L112_TRG_05_033640_STAGE2A|C06_L112_TRG_06_061970_STAGE2A|C06_L112_TRG_07_356860_STAGE2A",7,7,4,medium,canonical_shadow_only,"not production; URL repair needed for source_proxy rows"
shadow_weight,C06_proxy_blowoff_local_4B_watch,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"HBM-adjacent proxy names with local MFE but deep post-peak drawdown need local 4B watch, not full 4B without non-price evidence","flags 6 high-MAE paths without blocking direct capacity successes","C06_L112_TRG_02_330860_STAGE2A|C06_L112_TRG_03_405100_STAGE2A|C06_L112_TRG_04_007810_STAGE2A|C06_L112_TRG_05_033640_STAGE2A|C06_L112_TRG_06_061970_STAGE2A|C06_L112_TRG_07_356860_STAGE2A",7,7,4,medium,canonical_shadow_only,"overlay only; no global threshold change"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C06_L112_CASE_01_007660","symbol":"007660","company_name":"이수페타시스","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C06_L112_TRG_01_007660_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_with_high_MFE","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"direct-ish capacity proxy with strong price confirmation; needs URL repair"}
{"row_type":"case","case_id":"C06_L112_CASE_02_330860","symbol":"330860","company_name":"네패스아크","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C06_L112_TRG_02_330860_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_with_high_MFE","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"test/qualification proxy had strong MFE but later deep drawdown"}
{"row_type":"case","case_id":"C06_L112_CASE_03_405100","symbol":"405100","company_name":"큐알티","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C06_L112_TRG_03_405100_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_with_high_MFE","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"qualification/reliability proxy with exceptional MFE; later fade requires local 4B guard"}
{"row_type":"case","case_id":"C06_L112_CASE_04_007810","symbol":"007810","company_name":"코리아써키트","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_L112_TRG_04_007810_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE_or_low_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"substrate label did not convert into durable 90/180D outcome"}
{"row_type":"case","case_id":"C06_L112_CASE_05_033640","symbol":"033640","company_name":"네패스","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_L112_TRG_05_033640_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE_or_low_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"advanced packaging label lacked verified revenue/margin bridge"}
{"row_type":"case","case_id":"C06_L112_CASE_06_061970","symbol":"061970","company_name":"LB세미콘","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","case_type":"high_mae_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C06_L112_TRG_06_061970_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE_or_low_MFE","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"local MFE existed but later MAE implies proxy-only label needs 4B watch"}
{"row_type":"case","case_id":"C06_L112_CASE_07_356860","symbol":"356860","company_name":"티엘비","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_L112_TRG_07_356860_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE_or_low_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"memory/PCB proxy produced some MFE but not durable enough vs drawdown"}
{"row_type":"trigger","trigger_id":"C06_L112_TRG_01_007660_STAGE2A","case_id":"C06_L112_CASE_01_007660","symbol":"007660","company_name":"이수페타시스","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":27000.0,"evidence_available_at_that_date":"source_proxy_only: AI_SERVER_PCB_HBM_TRAFFIC_CAPACITY_PROXY; direct URL repair required before promotion","evidence_source":"source_proxy_only; stock-web price path verified; URL evidence repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion_proxy","financial_visibility_pending_url_repair"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv","profile_path":"atlas/symbol_profiles/007/007660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":57.59,"MFE_90D_pct":103.33,"MFE_180D_pct":121.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.41,"MAE_90D_pct":-2.41,"MAE_180D_pct":-2.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-03","peak_price":59700.0,"drawdown_after_peak_pct":-48.24,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_at_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"ai_server_pcb_capacity_proxy_structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_L112_007660_2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_L112_TRG_02_330860_STAGE2A","case_id":"C06_L112_CASE_02_330860","symbol":"330860","company_name":"네패스아크","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":24350.0,"evidence_available_at_that_date":"source_proxy_only: OSAT_TEST_CAPACITY_HBM_QUALIFICATION_PROXY; direct URL repair required before promotion","evidence_source":"source_proxy_only; stock-web price path verified; URL evidence repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion_proxy","financial_visibility_pending_url_repair"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","margin_or_backlog_slowdown_proxy"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv","profile_path":"atlas/symbol_profiles/330/330860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":90.55,"MFE_90D_pct":90.55,"MFE_180D_pct":90.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.13,"MAE_90D_pct":-5.13,"MAE_180D_pct":-50.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":46400.0,"drawdown_after_peak_pct":-74.14,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4B_watch_after_proxy_blowoff","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"test_capacity_proxy_success_but_needs_4B_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_L112_330860_2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_L112_TRG_03_405100_STAGE2A","case_id":"C06_L112_CASE_03_405100","symbol":"405100","company_name":"큐알티","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-12","entry_date":"2024-01-15","entry_price":15900.0,"evidence_available_at_that_date":"source_proxy_only: RELIABILITY_TEST_HBM_QUALIFICATION_PROXY; direct URL repair required before promotion","evidence_source":"source_proxy_only; stock-web price path verified; URL evidence repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion_proxy","financial_visibility_pending_url_repair"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","margin_or_backlog_slowdown_proxy"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv","profile_path":"atlas/symbol_profiles/405/405100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":144.03,"MFE_90D_pct":173.58,"MFE_180D_pct":173.58,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.7,"MAE_90D_pct":-1.7,"MAE_180D_pct":-25.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-03-05","peak_price":43500.0,"drawdown_after_peak_pct":-72.6,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4B_watch_after_proxy_blowoff","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"reliability_qualification_proxy_success_then_blowoff","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_L112_405100_2024-01-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_L112_TRG_04_007810_STAGE2A","case_id":"C06_L112_CASE_04_007810","symbol":"007810","company_name":"코리아써키트","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","entry_date":"2024-02-15","entry_price":20700.0,"evidence_available_at_that_date":"source_proxy_only: PACKAGE_SUBSTRATE_HBM_LABEL_WITHOUT_CONFIRMED_CUSTOMER_LOCK; direct URL repair required before promotion","evidence_source":"source_proxy_only; stock-web price path verified; URL evidence repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","margin_or_backlog_slowdown_proxy"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007810/2024.csv","profile_path":"atlas/symbol_profiles/007/007810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.49,"MFE_90D_pct":7.49,"MFE_180D_pct":7.49,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.98,"MAE_90D_pct":-31.79,"MAE_180D_pct":-56.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":22250.0,"drawdown_after_peak_pct":-59.1,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4B_watch_after_proxy_blowoff","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"package_substrate_label_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_L112_007810_2024-02-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_L112_TRG_05_033640_STAGE2A","case_id":"C06_L112_CASE_05_033640","symbol":"033640","company_name":"네패스","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":18340.0,"evidence_available_at_that_date":"source_proxy_only: ADVANCED_PACKAGING_LABEL_WITHOUT_CAPACITY_REVENUE_BRIDGE; direct URL repair required before promotion","evidence_source":"source_proxy_only; stock-web price path verified; URL evidence repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","margin_or_backlog_slowdown_proxy"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033640/2024.csv","profile_path":"atlas/symbol_profiles/033/033640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.14,"MFE_90D_pct":19.14,"MFE_180D_pct":19.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.8,"MAE_90D_pct":-16.25,"MAE_180D_pct":-59.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":21850.0,"drawdown_after_peak_pct":-66.22,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4B_watch_after_proxy_blowoff","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"advanced_packaging_label_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_L112_033640_2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_L112_TRG_06_061970_STAGE2A","case_id":"C06_L112_CASE_06_061970","symbol":"061970","company_name":"LB세미콘","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":7180.0,"evidence_available_at_that_date":"source_proxy_only: OSAT_PROXY_LOCAL_MFE_WITHOUT_DURABLE_CUSTOMER_PULL; direct URL repair required before promotion","evidence_source":"source_proxy_only; stock-web price path verified; URL evidence repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","margin_or_backlog_slowdown_proxy"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/061/061970/2024.csv","profile_path":"atlas/symbol_profiles/061/061970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.06,"MFE_90D_pct":31.06,"MFE_180D_pct":31.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.81,"MAE_90D_pct":-25.77,"MAE_180D_pct":-57.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":9410.0,"drawdown_after_peak_pct":-67.69,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4B_watch_after_proxy_blowoff","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"osat_proxy_local_mfe_then_deep_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_L112_061970_2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_L112_TRG_07_356860_STAGE2A","case_id":"C06_L112_CASE_07_356860","symbol":"356860","company_name":"티엘비","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_PACKAGE_SUBSTRATE_OSAT_TEST_QUALIFICATION_CAPACITY_PROXY_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":24250.0,"evidence_available_at_that_date":"source_proxy_only: MEMORY_PCB_PROXY_WITHOUT_MARGIN_FCF_BRIDGE; direct URL repair required before promotion","evidence_source":"source_proxy_only; stock-web price path verified; URL evidence repair required","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","margin_or_backlog_slowdown_proxy"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/356/356860/2024.csv","profile_path":"atlas/symbol_profiles/356/356860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.31,"MFE_90D_pct":34.23,"MFE_180D_pct":34.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.19,"MAE_90D_pct":-6.19,"MAE_180D_pct":-53.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-09","peak_price":32550.0,"drawdown_after_peak_pct":-65.38,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"needs_local_4B_watch_after_proxy_blowoff","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"memory_pcb_proxy_failed_after_midterm_mfe","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_L112_356860_2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C06_canonical_shadow_profile_loop112","case_id":"C06_L112_CASE_01_007660","trigger_id":"C06_L112_TRG_01_007660_STAGE2A","symbol":"007660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":62,"backlog_visibility_score":58,"margin_bridge_score":48,"revision_score":50,"relative_strength_score":82,"customer_quality_score":60,"policy_or_regulatory_score":15,"valuation_repricing_score":68,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":8,"accounting_trust_risk_score":8},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":62,"backlog_visibility_score":58,"margin_bridge_score":54,"revision_score":50,"relative_strength_score":82,"customer_quality_score":68,"policy_or_regulatory_score":15,"valuation_repricing_score":68,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":8,"accounting_trust_risk_score":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C06 shadow rule separates direct/customer-capacity evidence from OSAT/substrate/test proxy labels; proxy-only rows require revenue/margin bridge or stay Stage2-watch/local-4B-watch.","MFE_90D_pct":103.33,"MAE_90D_pct":-2.41,"score_return_alignment_label":"positive_kept","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"C06_canonical_shadow_profile_loop112","case_id":"C06_L112_CASE_02_330860","trigger_id":"C06_L112_TRG_02_330860_STAGE2A","symbol":"330860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":62,"backlog_visibility_score":58,"margin_bridge_score":48,"revision_score":50,"relative_strength_score":82,"customer_quality_score":60,"policy_or_regulatory_score":15,"valuation_repricing_score":68,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":8,"accounting_trust_risk_score":8},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":62,"backlog_visibility_score":58,"margin_bridge_score":54,"revision_score":50,"relative_strength_score":82,"customer_quality_score":68,"policy_or_regulatory_score":15,"valuation_repricing_score":68,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":8,"accounting_trust_risk_score":8},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable+4B_watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C06 shadow rule separates direct/customer-capacity evidence from OSAT/substrate/test proxy labels; proxy-only rows require revenue/margin bridge or stay Stage2-watch/local-4B-watch.","MFE_90D_pct":90.55,"MAE_90D_pct":-5.13,"score_return_alignment_label":"positive_kept_but_4B_watch_added","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C06_canonical_shadow_profile_loop112","case_id":"C06_L112_CASE_03_405100","trigger_id":"C06_L112_TRG_03_405100_STAGE2A","symbol":"405100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":62,"backlog_visibility_score":58,"margin_bridge_score":48,"revision_score":50,"relative_strength_score":82,"customer_quality_score":60,"policy_or_regulatory_score":15,"valuation_repricing_score":68,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":8,"accounting_trust_risk_score":8},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":62,"backlog_visibility_score":58,"margin_bridge_score":54,"revision_score":50,"relative_strength_score":82,"customer_quality_score":68,"policy_or_regulatory_score":15,"valuation_repricing_score":68,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":8,"accounting_trust_risk_score":8},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C06 shadow rule separates direct/customer-capacity evidence from OSAT/substrate/test proxy labels; proxy-only rows require revenue/margin bridge or stay Stage2-watch/local-4B-watch.","MFE_90D_pct":173.58,"MAE_90D_pct":-1.7,"score_return_alignment_label":"positive_kept_but_4B_watch_added","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C06_canonical_shadow_profile_loop112","case_id":"C06_L112_CASE_04_007810","trigger_id":"C06_L112_TRG_04_007810_STAGE2A","symbol":"007810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":18,"revision_score":22,"relative_strength_score":68,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":75,"execution_risk_score":58,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable_or_Stage3-Yellow_false_positive","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":13,"revision_score":22,"relative_strength_score":68,"customer_quality_score":27,"policy_or_regulatory_score":10,"valuation_repricing_score":57,"execution_risk_score":68,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_after":64,"stage_label_after":"Stage2-watch_or_4B_local_watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C06 shadow rule separates direct/customer-capacity evidence from OSAT/substrate/test proxy labels; proxy-only rows require revenue/margin bridge or stay Stage2-watch/local-4B-watch.","MFE_90D_pct":7.49,"MAE_90D_pct":-31.79,"score_return_alignment_label":"false_positive_reduced_by_bridge_requirement","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C06_canonical_shadow_profile_loop112","case_id":"C06_L112_CASE_05_033640","trigger_id":"C06_L112_TRG_05_033640_STAGE2A","symbol":"033640","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":18,"revision_score":22,"relative_strength_score":68,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":75,"execution_risk_score":58,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable_or_Stage3-Yellow_false_positive","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":13,"revision_score":22,"relative_strength_score":68,"customer_quality_score":27,"policy_or_regulatory_score":10,"valuation_repricing_score":57,"execution_risk_score":68,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_after":64,"stage_label_after":"Stage2-watch_or_4B_local_watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C06 shadow rule separates direct/customer-capacity evidence from OSAT/substrate/test proxy labels; proxy-only rows require revenue/margin bridge or stay Stage2-watch/local-4B-watch.","MFE_90D_pct":19.14,"MAE_90D_pct":-16.25,"score_return_alignment_label":"false_positive_reduced_by_bridge_requirement","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C06_canonical_shadow_profile_loop112","case_id":"C06_L112_CASE_06_061970","trigger_id":"C06_L112_TRG_06_061970_STAGE2A","symbol":"061970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":18,"revision_score":22,"relative_strength_score":68,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":75,"execution_risk_score":58,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable_or_Stage3-Yellow_false_positive","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":13,"revision_score":22,"relative_strength_score":68,"customer_quality_score":27,"policy_or_regulatory_score":10,"valuation_repricing_score":57,"execution_risk_score":68,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_after":64,"stage_label_after":"Stage2-watch_or_4B_local_watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C06 shadow rule separates direct/customer-capacity evidence from OSAT/substrate/test proxy labels; proxy-only rows require revenue/margin bridge or stay Stage2-watch/local-4B-watch.","MFE_90D_pct":31.06,"MAE_90D_pct":-25.77,"score_return_alignment_label":"false_positive_reduced_by_bridge_requirement","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C06_canonical_shadow_profile_loop112","case_id":"C06_L112_CASE_07_356860","trigger_id":"C06_L112_TRG_07_356860_STAGE2A","symbol":"356860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":18,"revision_score":22,"relative_strength_score":68,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":75,"execution_risk_score":58,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable_or_Stage3-Yellow_false_positive","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":13,"revision_score":22,"relative_strength_score":68,"customer_quality_score":27,"policy_or_regulatory_score":10,"valuation_repricing_score":57,"execution_risk_score":68,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_after":64,"stage_label_after":"Stage2-watch_or_4B_local_watch","changed_components":["customer_quality_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C06 shadow rule separates direct/customer-capacity evidence from OSAT/substrate/test proxy labels; proxy-only rows require revenue/margin bridge or stay Stage2-watch/local-4B-watch.","MFE_90D_pct":34.23,"MAE_90D_pct":-6.19,"score_return_alignment_label":"false_positive_reduced_by_bridge_requirement","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["proxy_label_false_positive","missed_structural_proxy_success","high_MAE_after_local_HBM_proxy_blowoff"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

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

completed_round = `R2`
completed_loop = `112`
selection_basis = `docs/core/V12_Research_No_Repeat_Index.md`
selected_priority_bucket = `Priority 1-under-50 after local-session adjustment; published index Priority 0`
next_recommended_archetypes = `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`, `C19_BRAND_RETAIL_INVENTORY_MARGIN`, `C13_BATTERY_JV_UTILIZATION_AMPC_IRA`, `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT`, `C22_INSURANCE_RATE_CYCLE_RESERVE`, `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
round_schedule_status = `coverage_index_selected`
round_sector_consistency = `pass`

Next execution should again read the published No-Repeat Index first, then adjust with this session's local generated MDs. If local-session rows are accepted, all originally Priority 0 and Priority 1 archetypes touched in this session have reached at least the 50-row practical band, so the next useful move is either quality repair for exactly-50 published archetypes or URL/proxy repair in high-proxy sectors.

## 28. Source Notes

- Main execution prompt used: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat ledger used only for coverage and duplicate avoidance: `docs/core/V12_Research_No_Repeat_Index.md`.
- Stock-Web manifest: `atlas/manifest.json`, max date `2026-02-20`.
- Price calculation uses local downloaded 2024 tradable shards from `Songdaiki/stock-web` for the seven listed symbols.

## Batch Ingest Self-Audit

expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
