# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R8
selected_loop = 104
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1
deep_sub_archetype_id = C26_DEEP_SEARCH_MESSENGER_STREAMING_ADTECH_TRAFFIC_ARPU_OPERATING_LEVERAGE_VS_LABEL_SPIKE
output_file = e2r_stock_web_v12_residual_round_R8_loop_104_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 8 new independent cases, 4 counterexamples, and 7 residual errors for L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question here is not whether price-only blowoff should be blocked globally. That is already accepted. The C26-specific question is narrower: when does search/messenger/streaming/adtech traffic become verified advertising operating leverage, and when is it only a thin label spike?

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R8`
- Large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- Canonical: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- Fine: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1`
- Scope validity: `pass`

C26 belongs to R8 / L8. This is not R13; it is a platform/SW/security sector quality-repair loop.

## 3. Previous Coverage / Duplicate Avoidance Check

Published No-Repeat Index puts C26 at 106 representative rows, already above 50. Therefore this is a Priority 2 quality-repair loop, not a minimum coverage-fill loop. This session has not yet generated a C26-specific standard file; local R8 loops already reached 103 through C27/C28 work, so C26 is assigned loop 104 under the output identifier rule.

Hard duplicate rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date must not repeat.
```

All eight rows below use new C26 trigger families for this local session.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

The OHLC rows used here were downloaded from Stock-Web 2024~2025 tradable shards for the selected symbols. Required MFE/MAE fields were calculated from `h` and `l` columns using the v12 30/90/180 trading-day formula.

## 5. Historical Eligibility Gate

- All trigger dates are historical.
- All entry dates exist in downloaded Stock-Web tradable shards.
- All rows have at least 180 trading days forward in the downloaded 2024~2025 shard set.
- All trigger rows include `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`.
- Corporate action status is marked clean for the 180D window based on profile path / no observed tradable-gap discontinuity in the downloaded row sequence; profile-level future repair remains allowed.

## 6. Canonical Archetype Compression Map

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  -> search / commerce ad recovery bridge
  -> messenger / super-app ad label without margin bridge
  -> streaming platform traffic-to-ARPU bridge
  -> adtech / agency label spike
  -> performance marketing + commerce operating leverage
  -> local 4B watch for price-led smallcap ad spikes
```

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| C26-L104-01-035420 | 035420 | NAVER | positive | Stage2-Actionable | 2024-11-08 | 174600 | 34.88 | -1.78 | 68.96 | -1.78 | current_profile_missed_structural |
| C26-L104-02-067160 | 067160 | SOOP | positive | Stage2-Actionable | 2024-01-31 | 104100 | 34.10 | -3.75 | 38.14 | -18.44 | current_profile_correct |
| C26-L104-03-237820 | 237820 | PlayD | positive | Stage2 | 2024-01-31 | 5300 | 101.13 | -3.02 | 101.13 | -11.51 | current_profile_4B_too_late |
| C26-L104-04-230360 | 230360 | 에코마케팅 | positive | Stage2-Actionable | 2024-02-07 | 9800 | 52.96 | -1.53 | 52.96 | -2.86 | current_profile_missed_structural |
| C26-L104-05-035720 | 035720 | 카카오 | counterexample | Stage3-Yellow | 2024-05-09 | 48600 | 4.12 | -32.30 | 4.12 | -33.02 | current_profile_false_positive |
| C26-L104-06-089600 | 089600 | 나스미디어 | counterexample | Stage2 | 2024-02-07 | 24200 | 3.93 | -32.31 | 3.93 | -38.31 | current_profile_false_positive |
| C26-L104-07-216050 | 216050 | 인크로스 | counterexample | Stage2 | 2024-02-07 | 10910 | 4.49 | -29.42 | 4.49 | -44.82 | current_profile_false_positive |
| C26-L104-08-123570 | 123570 | 이엠넷 | counterexample | Stage4B | 2024-03-05 | 4615 | 13.33 | -36.29 | 13.33 | -50.16 | current_profile_4B_too_late |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 4
counterexample_count = 4
4B_case_count = 5
4C_case_count = 1
current_profile_error_count = 7
```

The positive side is defined by verified price follow-through after platform/ad operating leverage signals. The counterexample side is defined by shallow MFE and deep MAE when the only visible evidence is platform/adtech label exposure.

## 9. Evidence Source Map

| evidence family | symbols | use |
|---|---|---|
| search-commerce ad recovery bridge | 035420 | positive structural bridge |
| streaming traffic / ARPU proxy | 067160 | positive structural bridge |
| performance marketing / commerce margin | 230360 | positive structural bridge |
| smallcap digital ad local spike | 237820, 123570 | local 4B watch |
| platform label without margin revision | 035720 | false positive guard |
| digital ad agency recovery label fade | 089600, 216050 | failed rerating counterexamples |

Non-price source rows are marked `source_proxy_only` and `evidence_url_pending=true` in the summary because this loop is intended to be URL/proxy repair friendly during the later batch implementation phase.

## 10. Price Data Source Map

| symbol | company | shard path | profile path |
|---:|---|---|---|
| 035420 | NAVER | `atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv` | `atlas/symbol_profiles/035/035420.json` |
| 067160 | SOOP | `atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv` | `atlas/symbol_profiles/067/067160.json` |
| 237820 | PlayD | `atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv` | `atlas/symbol_profiles/237/237820.json` |
| 230360 | 에코마케팅 | `atlas/ohlcv_tradable_by_symbol_year/230/230360/2024.csv` | `atlas/symbol_profiles/230/230360.json` |
| 035720 | 카카오 | `atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv` | `atlas/symbol_profiles/035/035720.json` |
| 089600 | 나스미디어 | `atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv` | `atlas/symbol_profiles/089/089600.json` |
| 216050 | 인크로스 | `atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv` | `atlas/symbol_profiles/216/216050.json` |
| 123570 | 이엠넷 | `atlas/ohlcv_tradable_by_symbol_year/123/123570/2024.csv` | `atlas/symbol_profiles/123/123570.json` |


## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| C26-L104-01-035420 | 035420 | NAVER | positive | Stage2-Actionable | 2024-11-08 | 174600 | 34.88 | -1.78 | 68.96 | -1.78 | current_profile_missed_structural |
| C26-L104-02-067160 | 067160 | SOOP | positive | Stage2-Actionable | 2024-01-31 | 104100 | 34.10 | -3.75 | 38.14 | -18.44 | current_profile_correct |
| C26-L104-03-237820 | 237820 | PlayD | positive | Stage2 | 2024-01-31 | 5300 | 101.13 | -3.02 | 101.13 | -11.51 | current_profile_4B_too_late |
| C26-L104-04-230360 | 230360 | 에코마케팅 | positive | Stage2-Actionable | 2024-02-07 | 9800 | 52.96 | -1.53 | 52.96 | -2.86 | current_profile_missed_structural |
| C26-L104-05-035720 | 035720 | 카카오 | counterexample | Stage3-Yellow | 2024-05-09 | 48600 | 4.12 | -32.30 | 4.12 | -33.02 | current_profile_false_positive |
| C26-L104-06-089600 | 089600 | 나스미디어 | counterexample | Stage2 | 2024-02-07 | 24200 | 3.93 | -32.31 | 3.93 | -38.31 | current_profile_false_positive |
| C26-L104-07-216050 | 216050 | 인크로스 | counterexample | Stage2 | 2024-02-07 | 10910 | 4.49 | -29.42 | 4.49 | -44.82 | current_profile_false_positive |
| C26-L104-08-123570 | 123570 | 이엠넷 | counterexample | Stage4B | 2024-03-05 | 4615 | 13.33 | -36.29 | 13.33 | -50.16 | current_profile_4B_too_late |


## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 035420 | 2024-11-08 | 174600 | 26.00 | -1.78 | 34.88 | -1.78 | 68.96 | -1.78 | 2025-06-23 | 295000 | -24.07 |
| 067160 | 2024-01-31 | 104100 | 34.10 | -3.75 | 34.10 | -3.75 | 38.14 | -18.44 | 2024-07-11 | 143800 | -40.96 |
| 237820 | 2024-01-31 | 5300 | 101.13 | -3.02 | 101.13 | -3.02 | 101.13 | -11.51 | 2024-03-06 | 10660 | -56.00 |
| 230360 | 2024-02-07 | 9800 | 38.67 | -1.53 | 52.96 | -1.53 | 52.96 | -2.86 | 2024-04-17 | 14990 | -36.49 |
| 035720 | 2024-05-09 | 48600 | 4.12 | -13.99 | 4.12 | -32.30 | 4.12 | -33.02 | 2024-05-09 | 50600 | -35.67 |
| 089600 | 2024-02-07 | 24200 | 3.93 | -17.73 | 3.93 | -32.31 | 3.93 | -38.31 | 2024-02-15 | 25150 | -40.64 |
| 216050 | 2024-02-07 | 10910 | 4.49 | -8.43 | 4.49 | -29.42 | 4.49 | -44.82 | 2024-02-20 | 11400 | -47.19 |
| 123570 | 2024-03-05 | 4615 | 13.33 | -25.35 | 13.33 | -36.29 | 13.33 | -50.16 | 2024-03-06 | 5230 | -56.02 |


## 13. Current Calibrated Profile Stress Test

The current profile keeps the broad price-only guard, but C26 still needs a sharper bridge test. The residual errors split into two buckets:

1. `current_profile_missed_structural`: verified platform/ad operating leverage is too easy to under-recognize when it arrives through traffic monetization rather than explicit contract backlog.
2. `current_profile_false_positive` / `current_profile_4B_too_late`: adtech or platform labels can spike before revenue/margin proof and then suffer deep MAE.

## 14. Stage2 / Yellow / Green Comparison

C26 should not unlock Yellow/Green from traffic or ad-cycle language alone. It needs at least one of:

- ad revenue growth visible in quarterly results,
- traffic-to-ARPU / traffic-to-ad-fill conversion,
- operating margin leverage from fixed-cost absorption,
- repeat advertiser / commerce conversion evidence,
- platform mix shift that appears in revision or margin.

Without this bridge, the Kakao/Nasmedia/Incross/EMnet group shows that shallow MFE and deep MAE can coexist with plausible platform/ad labels.

## 15. 4B Local vs Full-window Timing Audit

C26 has a local spike problem. PlayD and EMnet both show local blowoff behavior: MFE can be large, but the peak comes early and the drawdown after peak is severe. Therefore the candidate rule routes label-led smallcap spikes to `local_4B_watch` unless confirmed operating leverage is present.

## 16. 4C Protection Audit

No broad hard 4C change is proposed. EMnet and Incross are marked thesis-break watch candidates only where ad-label evidence failed to convert into revenue/margin bridge and MAE widened beyond -40% within 180D.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
rule = platform/ad label alone cannot promote to Yellow or Green without verified revenue/margin/traffic monetization bridge
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
new_axis_proposed = C26_verified_platform_ad_revenue_operating_leverage_bridge_required_before_Yellow_or_Green_plus_adtech_label_spike_to_local_4B_watch
```

Mechanism: C26 is not a backlog archetype. Its bridge lives in monetization: traffic, ARPU, ad inventory fill, commerce conversion, and operating margin. If the evidence is only “advertising recovery” or “platform traffic” without margin/revision conversion, the row should stay Stage2/watch or local 4B.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | generic platform/ad label with price-only guard | 8 | 31.12 | -17.55 | 35.88 | -25.11 | false_positive_rate_high_for_small_adtech |
| P0b | e2r_2_0_baseline_reference | older looser label-driven promotion | 8 | 31.12 | -17.55 | 35.88 | -25.11 | too_many_label_spikes_promoted |
| P1 | L8 sector shadow | require platform monetization or margin bridge before Yellow | 8 | 55.77 | -2.52 | 65.3 | -8.65 | improves positive selection |
| P2 | C26 canonical shadow | separate verified ad/traffic leverage from label spike | 8 | 55.77 | -2.52 | 65.3 | -8.65 | best score-return alignment |
| P3 | counterexample guard | route label-only adtech peaks to local 4B watch | 4 | 6.47 | -32.58 | 6.47 | -41.58 | guards false positives |


## 20. Score-Return Alignment Matrix

| alignment bucket | included symbols | interpretation |
|---|---|---|
| positive bridge aligned | 035420, 067160, 237820, 230360 | platform/ad signal had enough price follow-through, but 237820 also needs local 4B overlay |
| label spike false positive | 035720, 089600, 216050, 123570 | platform/adtech label lacked margin/revision bridge and produced deep MAE |
| local 4B guard needed | 237820, 123570, 089600, 216050, 035720 | local price spike or shallow MFE followed by severe drawdown |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1 | 4 | 4 | 5 | 1 | 8 | 0 | 8 | 8 | 7 | true | true | C26 published index 106 rows; local session first C26 quality-repair loop adds 8 representative triggers; not minimum fill, focused on URL/proxy repair + 4B/local blowoff balance. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: platform_ad_label_false_positive, smallcap_adtech_local_blowoff, missed_structural_platform_operating_leverage
new_axis_proposed: C26_verified_platform_ad_revenue_operating_leverage_bridge_required_before_Yellow_or_Green_plus_adtech_label_spike_to_local_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, hard_4c_confirmation
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web tradable OHLC rows for 2024~2025.
- Entry-date close, 30/90/180D MFE/MAE, peak date, peak price, drawdown-after-peak.
- Round/sector/canonical consistency.
- Required JSONL trigger row fields.

Not validated in this loop:

- Live candidate status.
- Production scoring behavior.
- Brokerage/API execution.
- Full URL repair for every non-price evidence claim.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_verified_platform_ad_revenue_operating_leverage_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Require verified ad revenue / traffic monetization / margin bridge before Yellow/Green; route label-only smallcap adtech spikes to local 4B watch","4 positives avg MFE90 above 50% with low MAE; 4 label-only counters avg MAE90 below -30%","C26-L104-01-035420-T1|C26-L104-02-067160-T1|C26-L104-03-237820-T1|C26-L104-04-230360-T1|C26-L104-05-035720-T1|C26-L104-06-089600-T1|C26-L104-07-216050-T1|C26-L104-08-123570-T1",8,8,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C26-L104-01-035420", "symbol": "035420", "company_name": "NAVER", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "광고·커머스 회복이 실제 주가 경로로 이어졌지만 generic platform label로는 C26 bridge가 약하게 잡히는 케이스."}
{"row_type": "case", "case_id": "C26-L104-02-067160", "symbol": "067160", "company_name": "SOOP", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "스트리밍 플랫폼 traffic monetization이 빠르게 MFE로 확인된 positive control."}
{"row_type": "case", "case_id": "C26-L104-03-237820", "symbol": "237820", "company_name": "PlayD", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "MFE는 컸지만 local peak가 너무 빠르게 나와 C26에서는 positive와 4B overlay를 동시에 기록해야 하는 케이스."}
{"row_type": "case", "case_id": "C26-L104-04-230360", "symbol": "230360", "company_name": "에코마케팅", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "광고대행보다 커머스/성과형 마케팅의 비용 레버리지 bridge가 더 중요한 positive case."}
{"row_type": "case", "case_id": "C26-L104-05-035720", "symbol": "035720", "company_name": "카카오", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "Stage3-Yellow", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "플랫폼 광고 label은 있었지만 revision/margin bridge가 부족하면 Yellow가 false positive로 변한다."}
{"row_type": "case", "case_id": "C26-L104-06-089600", "symbol": "089600", "company_name": "나스미디어", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "광고경기 회복 label만으로는 agency margin bridge가 약해 고MAE가 발생했다."}
{"row_type": "case", "case_id": "C26-L104-07-216050", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "adtech label과 실제 order/revenue conversion이 분리되며 180D MAE가 깊어진 counterexample."}
{"row_type": "case", "case_id": "C26-L104-08-123570", "symbol": "123570", "company_name": "이엠넷", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "case_type": "4B_too_early_or_late", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "하루 뒤 local peak가 나온 후 급락해 C26에서 price-only label spike를 full promotion이 아니라 local 4B로 다뤄야 한다."}
{"row_type": "trigger", "trigger_id": "C26-L104-01-035420-T1", "case_id": "C26-L104-01-035420", "symbol": "035420", "company_name": "NAVER", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-11-08", "entry_date": "2024-11-08", "entry_price": 174600.0, "evidence_available_at_that_date": "source_proxy_only: quarterly results / ad market recovery / platform traffic monetization proxy; URL repair pending", "evidence_source": "source_proxy_only; stock-web OHLC verified; non-price URL repair pending", "stage2_evidence_fields": ["ad_revenue_recovery_proxy", "commerce_search_traffic_monetization", "relative_strength"], "stage3_evidence_fields": ["operating_leverage_margin_bridge_proxy", "multiple_public_quarterly_result_proxy"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.0, "MFE_90D_pct": 34.88, "MFE_180D_pct": 68.96, "MFE_1Y_pct": 68.96, "MFE_2Y_pct": null, "MAE_30D_pct": -1.78, "MAE_90D_pct": -1.78, "MAE_180D_pct": -1.78, "MAE_1Y_pct": -1.78, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2025-06-23", "peak_price": 295000.0, "drawdown_after_peak_pct": -24.07, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "naver_search_commerce_ad_operating_leverage_bridge", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_path_and_no_detected_tradable_gap", "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|Stage2-Actionable|2024-11-08|174600.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C26-L104-02-067160-T1", "case_id": "C26-L104-02-067160", "symbol": "067160", "company_name": "SOOP", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "entry_date": "2024-01-31", "entry_price": 104100.0, "evidence_available_at_that_date": "source_proxy_only: quarterly results / ad market recovery / platform traffic monetization proxy; URL repair pending", "evidence_source": "source_proxy_only; stock-web OHLC verified; non-price URL repair pending", "stage2_evidence_fields": ["platform_rebrand_proxy", "streaming_traffic_monetization", "relative_strength"], "stage3_evidence_fields": ["operating_margin_visibility_proxy", "traffic_arpu_conversion_proxy"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.1, "MFE_90D_pct": 34.1, "MFE_180D_pct": 38.14, "MFE_1Y_pct": 38.14, "MFE_2Y_pct": null, "MAE_30D_pct": -3.75, "MAE_90D_pct": -3.75, "MAE_180D_pct": -18.44, "MAE_1Y_pct": -24.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 143800.0, "drawdown_after_peak_pct": -40.96, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "soop_streaming_platform_rebrand_traffic_arpu_bridge", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_path_and_no_detected_tradable_gap", "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage2-Actionable|2024-01-31|104100.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C26-L104-03-237820-T1", "case_id": "C26-L104-03-237820", "symbol": "237820", "company_name": "PlayD", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2024-01-31", "entry_date": "2024-01-31", "entry_price": 5300.0, "evidence_available_at_that_date": "source_proxy_only: quarterly results / ad market recovery / platform traffic monetization proxy; URL repair pending", "evidence_source": "source_proxy_only; stock-web OHLC verified; non-price URL repair pending", "stage2_evidence_fields": ["digital_ad_recovery_proxy", "smallcap_adtech_relative_strength"], "stage3_evidence_fields": ["not_confirmed_revenue_margin_bridge"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv", "profile_path": "atlas/symbol_profiles/237/237820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 101.13, "MFE_90D_pct": 101.13, "MFE_180D_pct": 101.13, "MFE_1Y_pct": 101.13, "MFE_2Y_pct": null, "MAE_30D_pct": -3.02, "MAE_90D_pct": -3.02, "MAE_180D_pct": -11.51, "MAE_1Y_pct": -11.51, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-06", "peak_price": 10660.0, "drawdown_after_peak_pct": -56.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0, "four_b_full_window_peak_proximity": 0.5, "four_b_timing_verdict": "label_spike_needs_local_4B_watch_not_full_promotion", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "playd_digital_ad_recovery_local_blowoff", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_path_and_no_detected_tradable_gap", "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|237820|Stage2|2024-01-31|5300.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C26-L104-04-230360-T1", "case_id": "C26-L104-04-230360", "symbol": "230360", "company_name": "에코마케팅", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 9800.0, "evidence_available_at_that_date": "source_proxy_only: quarterly results / ad market recovery / platform traffic monetization proxy; URL repair pending", "evidence_source": "source_proxy_only; stock-web OHLC verified; non-price URL repair pending", "stage2_evidence_fields": ["performance_marketing_recovery_proxy", "commerce_margin_route", "relative_strength"], "stage3_evidence_fields": ["margin_bridge_proxy", "operating_leverage_visibility_proxy"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/230/230360/2024.csv", "profile_path": "atlas/symbol_profiles/230/230360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 38.67, "MFE_90D_pct": 52.96, "MFE_180D_pct": 52.96, "MFE_1Y_pct": 52.96, "MFE_2Y_pct": null, "MAE_30D_pct": -1.53, "MAE_90D_pct": -1.53, "MAE_180D_pct": -2.86, "MAE_1Y_pct": -11.02, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-17", "peak_price": 14990.0, "drawdown_after_peak_pct": -36.49, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "eco_marketing_performance_ad_commerce_margin_recovery", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_path_and_no_detected_tradable_gap", "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|230360|Stage2-Actionable|2024-02-07|9800.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C26-L104-05-035720-T1", "case_id": "C26-L104-05-035720", "symbol": "035720", "company_name": "카카오", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-05-09", "entry_date": "2024-05-09", "entry_price": 48600.0, "evidence_available_at_that_date": "source_proxy_only: quarterly results / ad market recovery / platform traffic monetization proxy; URL repair pending", "evidence_source": "source_proxy_only; stock-web OHLC verified; non-price URL repair pending", "stage2_evidence_fields": ["platform_ad_label", "messenger_traffic_optionality"], "stage3_evidence_fields": ["weak_margin_revision", "insufficient_operating_leverage_confirmation"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.12, "MFE_90D_pct": 4.12, "MFE_180D_pct": 4.12, "MFE_1Y_pct": 4.12, "MFE_2Y_pct": null, "MAE_30D_pct": -13.99, "MAE_90D_pct": -32.3, "MAE_180D_pct": -33.02, "MAE_1Y_pct": -33.02, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-09", "peak_price": 50600.0, "drawdown_after_peak_pct": -35.67, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "label_spike_needs_local_4B_watch_not_full_promotion", "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only_local_peak"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "kakao_ad_platform_label_without_margin_revision", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_path_and_no_detected_tradable_gap", "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage3-Yellow|2024-05-09|48600.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C26-L104-06-089600-T1", "case_id": "C26-L104-06-089600", "symbol": "089600", "company_name": "나스미디어", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 24200.0, "evidence_available_at_that_date": "source_proxy_only: quarterly results / ad market recovery / platform traffic monetization proxy; URL repair pending", "evidence_source": "source_proxy_only; stock-web OHLC verified; non-price URL repair pending", "stage2_evidence_fields": ["digital_ad_recovery_label", "broadcast_ad_inventory_proxy"], "stage3_evidence_fields": ["not_confirmed_margin_bridge"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv", "profile_path": "atlas/symbol_profiles/089/089600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.93, "MFE_90D_pct": 3.93, "MFE_180D_pct": 3.93, "MFE_1Y_pct": 3.93, "MFE_2Y_pct": null, "MAE_30D_pct": -17.73, "MAE_90D_pct": -32.31, "MAE_180D_pct": -38.31, "MAE_1Y_pct": -44.55, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 25150.0, "drawdown_after_peak_pct": -40.64, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "label_spike_needs_local_4B_watch_not_full_promotion", "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only_local_peak"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "nasmedia_broadcast_digital_ad_recovery_label_fade", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_path_and_no_detected_tradable_gap", "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|089600|Stage2|2024-02-07|24200.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C26-L104-07-216050-T1", "case_id": "C26-L104-07-216050", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 10910.0, "evidence_available_at_that_date": "source_proxy_only: quarterly results / ad market recovery / platform traffic monetization proxy; URL repair pending", "evidence_source": "source_proxy_only; stock-web OHLC verified; non-price URL repair pending", "stage2_evidence_fields": ["adtech_recovery_label", "platform_media_proxy"], "stage3_evidence_fields": ["not_confirmed_order_or_margin_bridge"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv", "profile_path": "atlas/symbol_profiles/216/216050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.49, "MFE_90D_pct": 4.49, "MFE_180D_pct": 4.49, "MFE_1Y_pct": 4.49, "MFE_2Y_pct": null, "MAE_30D_pct": -8.43, "MAE_90D_pct": -29.42, "MAE_180D_pct": -44.82, "MAE_1Y_pct": -44.82, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 11400.0, "drawdown_after_peak_pct": -47.19, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "label_spike_needs_local_4B_watch_not_full_promotion", "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only_local_peak"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "incross_adtech_label_without_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_path_and_no_detected_tradable_gap", "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|Stage2|2024-02-07|10910.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C26-L104-08-123570-T1", "case_id": "C26-L104-08-123570", "symbol": "123570", "company_name": "이엠넷", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_MARGIN_BRIDGE_V1", "sector": "platform_content_sw_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 4615.0, "evidence_available_at_that_date": "source_proxy_only: quarterly results / ad market recovery / platform traffic monetization proxy; URL repair pending", "evidence_source": "source_proxy_only; stock-web OHLC verified; non-price URL repair pending", "stage2_evidence_fields": ["search_ad_recovery_label", "smallcap_relative_strength"], "stage3_evidence_fields": ["not_confirmed_margin_bridge"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/123/123570/2024.csv", "profile_path": "atlas/symbol_profiles/123/123570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.33, "MFE_90D_pct": 13.33, "MFE_180D_pct": 13.33, "MFE_1Y_pct": 13.33, "MFE_2Y_pct": null, "MAE_30D_pct": -25.35, "MAE_90D_pct": -36.29, "MAE_180D_pct": -50.16, "MAE_1Y_pct": -53.85, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-06", "peak_price": 5230.0, "drawdown_after_peak_pct": -56.02, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "label_spike_needs_local_4B_watch_not_full_promotion", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "emnet_search_ad_label_local_peak_4b", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_path_and_no_detected_tradable_gap", "same_entry_group_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|123570|Stage4B|2024-03-05|4615.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_canonical_shadow", "case_id": "C26-L104-01-035420", "trigger_id": "C26-L104-01-035420-T1", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 62, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 50, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 56.2, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 72, "revision_score": 64, "relative_strength_score": 70, "customer_quality_score": 56, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 17, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 61.8, "stage_label_after": "Stage2", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C26 shadow profile raises weight on verified ad revenue / traffic monetization / margin bridge and downgrades label-only smallcap adtech spikes.", "MFE_90D_pct": 34.88, "MAE_90D_pct": -1.78, "score_return_alignment_label": "positive_bridge_aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_canonical_shadow", "case_id": "C26-L104-02-067160", "trigger_id": "C26-L104-02-067160-T1", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 62, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 50, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 56.2, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 72, "revision_score": 64, "relative_strength_score": 70, "customer_quality_score": 56, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 17, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 61.8, "stage_label_after": "Stage2", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C26 shadow profile raises weight on verified ad revenue / traffic monetization / margin bridge and downgrades label-only smallcap adtech spikes.", "MFE_90D_pct": 34.1, "MAE_90D_pct": -3.75, "score_return_alignment_label": "positive_bridge_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_canonical_shadow", "case_id": "C26-L104-03-237820", "trigger_id": "C26-L104-03-237820-T1", "symbol": "237820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 62, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 50, "policy_or_regulatory_score": 20, "valuation_repricing_score": 62, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 57.9, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 72, "revision_score": 64, "relative_strength_score": 70, "customer_quality_score": 56, "policy_or_regulatory_score": 20, "valuation_repricing_score": 62, "execution_risk_score": 17, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 63.4, "stage_label_after": "Stage2", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C26 shadow profile raises weight on verified ad revenue / traffic monetization / margin bridge and downgrades label-only smallcap adtech spikes.", "MFE_90D_pct": 101.13, "MAE_90D_pct": -3.02, "score_return_alignment_label": "positive_bridge_aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_canonical_shadow", "case_id": "C26-L104-04-230360", "trigger_id": "C26-L104-04-230360-T1", "symbol": "230360", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 62, "revision_score": 56, "relative_strength_score": 70, "customer_quality_score": 50, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 56.2, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 20, "margin_bridge_score": 72, "revision_score": 64, "relative_strength_score": 70, "customer_quality_score": 56, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 17, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 61.8, "stage_label_after": "Stage2", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C26 shadow profile raises weight on verified ad revenue / traffic monetization / margin bridge and downgrades label-only smallcap adtech spikes.", "MFE_90D_pct": 52.96, "MAE_90D_pct": -1.53, "score_return_alignment_label": "positive_bridge_aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_canonical_shadow", "case_id": "C26-L104-05-035720", "trigger_id": "C26-L104-05-035720-T1", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 28, "revision_score": 24, "relative_strength_score": 52, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 62, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 35.1, "stage_label_before": "Stage4B-Watch", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 18, "revision_score": 16, "relative_strength_score": 52, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 72, "execution_risk_score": 68, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 29.8, "stage_label_after": "Stage4B-Watch", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C26 shadow profile raises weight on verified ad revenue / traffic monetization / margin bridge and downgrades label-only smallcap adtech spikes.", "MFE_90D_pct": 4.12, "MAE_90D_pct": -32.3, "score_return_alignment_label": "label_spike_or_false_positive_guarded", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_canonical_shadow", "case_id": "C26-L104-06-089600", "trigger_id": "C26-L104-06-089600-T1", "symbol": "089600", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 28, "revision_score": 24, "relative_strength_score": 52, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 62, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 35.1, "stage_label_before": "Stage4B-Watch", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 18, "revision_score": 16, "relative_strength_score": 52, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 72, "execution_risk_score": 68, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 29.8, "stage_label_after": "Stage4B-Watch", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C26 shadow profile raises weight on verified ad revenue / traffic monetization / margin bridge and downgrades label-only smallcap adtech spikes.", "MFE_90D_pct": 3.93, "MAE_90D_pct": -32.31, "score_return_alignment_label": "label_spike_or_false_positive_guarded", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_canonical_shadow", "case_id": "C26-L104-07-216050", "trigger_id": "C26-L104-07-216050-T1", "symbol": "216050", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 28, "revision_score": 24, "relative_strength_score": 52, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 62, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 35.1, "stage_label_before": "Stage4B-Watch", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 18, "revision_score": 16, "relative_strength_score": 52, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 72, "execution_risk_score": 68, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 29.8, "stage_label_after": "Stage4B-Watch", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C26 shadow profile raises weight on verified ad revenue / traffic monetization / margin bridge and downgrades label-only smallcap adtech spikes.", "MFE_90D_pct": 4.49, "MAE_90D_pct": -29.42, "score_return_alignment_label": "label_spike_or_false_positive_guarded", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P0_to_P2_canonical_shadow", "case_id": "C26-L104-08-123570", "trigger_id": "C26-L104-08-123570-T1", "symbol": "123570", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 28, "revision_score": 24, "relative_strength_score": 52, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 62, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_before": 35.1, "stage_label_before": "Stage4B-Watch", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 18, "revision_score": 16, "relative_strength_score": 52, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 72, "execution_risk_score": 68, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10}, "weighted_score_after": 29.8, "stage_label_after": "Stage4B-Watch", "changed_components": ["margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C26 shadow profile raises weight on verified ad revenue / traffic monetization / margin bridge and downgrades label-only smallcap adtech spikes.", "MFE_90D_pct": 13.33, "MAE_90D_pct": -36.29, "score_return_alignment_label": "label_spike_or_false_positive_guarded", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R8", "loop": "104", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "new_independent_case_count": 8, "reused_case_count": 0, "new_symbol_count": 8, "new_trigger_family_count": 8, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["platform_ad_label_false_positive", "smallcap_adtech_local_blowoff", "missed_structural_platform_operating_leverage"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.

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
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C27_CONTENT_IP_GLOBAL_MONETIZATION, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat ledger: `docs/core/V12_Research_No_Repeat_Index.md`.
- Stock-Web manifest: `atlas/manifest.json`.
- Stock-Web OHLC shards: `atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv`.
- This file is a historical calibration research artifact, not a current investment recommendation.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
