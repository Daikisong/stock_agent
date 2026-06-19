# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_file": "e2r_stock_web_v12_residual_round_R1_loop_209_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md",
  "prompt_version": "E2R Historical Calibration Prompt v12 — Stock-Web OHLC Atlas / Sector-Archetype Residual Expansion / MD Handoff",
  "generated_at_kst": "2026-06-16",
  "selected_round": "R1",
  "selected_loop": 209,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 1 C05 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair",
  "round_schedule_status": "coverage_index_selected; prior C05 loop 208 exists so C05 advances to loop 209; recent R13/C31 repetitions avoided",
  "round_sector_consistency": "pass",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR",
  "loop_objective": "counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair",
  "primary_price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "live_scan_performed": false,
  "current_stock_discovery_allowed": false,
  "stock_agent_code_opened_or_patched": false
}
```

## 1. Current Calibrated Profile Assumption

The active proxy is `e2r_2_1_stock_web_calibrated_proxy`; this run is shadow-only and tests whether C05 EPC/result/backlog rows need a narrower margin-cash conversion ladder. Production scoring is not changed. The research does not perform live discovery or produce current investment recommendations.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
| --- | --- |
| selected_round | R1 |
| selected_loop | 209 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP |
| fine_archetype_id | C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR |
| loop_objective | counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair |
| scope verdict | R1/L1/C05 mapping is internally consistent |

## 3. Previous Coverage / Duplicate Avoidance Check

The no-repeat ledger is in quality-repair mode: every C01~C32 archetype is above the old row-count thresholds, so Priority 0 URL/proxy/MFE-MAE repair and Priority 1 balance repair drive selection. Recent returned outputs already covered C15, C05 loop 208, C01, C13, C10, C31 and several R13 compression axes. C05 is re-entered only with new exact duplicate keys and new event families.

| ledger_type | duplicate_key_or_rule |
| --- | --- |
| previous C05 loop 208 sample | C05|028050|Stage3-Green|2024-01-31 |
| previous C05 loop 208 sample | C05|006360|Stage2-Actionable|2024-04-03 |
| previous C05 loop 208 sample | C05|000720|Stage4B|2024-07-19 |
| new loop 209 | C05|047040|Stage4B|2025-02-07 |
| new loop 209 | C05|375500|Stage3-Yellow|2025-02-07 |
| new loop 209 | C05|028050|Stage3-Green|2024-07-26 |
| new loop 209 | C05|016250|Stage4B|2024-04-24 |
| new loop 209 | C05|003070|Stage2|2025-02-26 |
| new loop 209 | C05|005960|Stage2-Actionable|2025-05-16 |

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
| --- | --- |
| manifest_url | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json |
| schema_url | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json |
| stock_web_manifest_max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| price_adjustment_status | raw_unadjusted_marcap |
| tradable shard schema | d,o,h,l,c,v,a,mc,s,m |
| MFE/MAE rule | entry 이후 N개 tradable rows의 max high / min low |

## 5. Historical Eligibility Gate

| gate | result |
| --- | --- |
| historical trigger dates | pass; all trigger dates are before stock-web max date and have 180 forward tradable rows |
| entry rows in tradable shard | pass; actual entry OHLC rows are listed below |
| 180D forward window | pass; all representative trigger rows have 180 tradable rows |
| corporate action window | pass; selected D~D+180 windows are marked clean |
| required six MFE/MAE fields | pass; all trigger JSONL rows include MFE_30D_pct/MFE_90D_pct/MFE_180D_pct/MAE_30D_pct/MAE_90D_pct/MAE_180D_pct |
| canonical trigger_type | pass; Stage2-Watch was normalized to canonical Stage2 with watch-cap details moved to trigger_outcome_label |

## 6. Canonical Archetype Compression Map

C05 is not simply an order/backlog archetype. Its failure mode is a bridge problem: a backlog/result headline is only the first tile; the calibration signal becomes stronger only when the tile connects to margin, cost-rate, working-capital, and repeatability. The shadow map used here is: `event/result existence -> order/backlog quality -> margin/cost-rate proof -> working-capital/cash conversion -> persistence`.

## 7. Case Selection Summary

| case_id | symbol | company | trigger_date | entry_date | trigger_type | role | MFE90/MAE90 | MFE180/MAE180 | current_profile_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_L209_01_DAEWOO_EC_2024_ONEOFF_BEAT_NOT_HARD4C | 047040 | Daewoo E&C / 대우건설 | 2025-02-06 | 2025-02-07 | Stage4B | guardrail_positive_hard4c_false_negative_prevention | 44.29 / -11.71 | 44.29 / -11.71 | True |
| C05_L209_02_DLENC_2024_COST_RATE_RECOVERY_CONFIRMED | 375500 | DL E&C / DL이앤씨 | 2025-02-06 | 2025-02-07 | Stage3-Yellow | positive_margin_quality_and_order_recovery | 52.3 / -5.28 | 61.79 / -5.28 | False |
| C05_L209_03_SAMSUNG_EA_Q2_BACKLOG_GREEN_TRAP | 028050 | Samsung E&A / 삼성E&A | 2024-07-25 | 2024-07-26 | Stage3-Green | counterexample_backlog_and_consensus_beat_without_forward_conversion | 5.02 / -41.58 | 5.02 / -41.58 | True |
| C05_L209_04_SGC_EC_Q1_OP_DROP_LOCAL_4B_NOT_HARD_EXIT | 016250 | SGC E&C / SGC이앤씨 | 2024-04-23 | 2024-04-24 | Stage4B | counterexample_or_watch_cost_rate_pressure_with_later_rebound_then_decay | 20.51 / -9.97 | 20.51 / -24.31 | False |
| C05_L209_05_KOLON_GLOBAL_CORRECTION_SOURCE_QUALITY_CAP | 003070 | Kolon Global / 코오롱글로벌 | 2025-02-25 | 2025-02-26 | Stage2 | counterexample_source_quality_and_result_only_cap | 18.82 / -12.58 | 18.82 / -12.58 | True |
| C05_L209_06_DONGBU_EC_Q1_TURNAROUND_DIRECT_REPORT | 005960 | Dongbu Construction / 동부건설 | 2025-05-15 | 2025-05-16 | Stage2-Actionable | positive_turnaround_margin_cost_backlog_bridge | 56.77 / -3.53 | 56.77 / -3.53 | False |

## 8. Positive vs Counterexample Balance

| bucket | cases | interpretation |
| --- | --- | --- |
| positive / guardrail-positive | 3 | Daewoo E&C one-off bad result should be watch not hard 4C; DL E&C and Dongbu have explicit margin/cost/backlog bridges |
| counterexample / cap | 3 | Samsung E&A late-cycle backlog beat, SGC E&C result-pressure watch, and Kolon direct result disclosure without cash bridge |
| balance verdict | 3 positive vs 3 counterexample | enough for canonical-archetype-specific shadow candidate, not a global delta |

## 9. Evidence Source Map

| trigger_id | primary_evidence_url | source_quality | evidence_summary |
| --- | --- | --- | --- |
| C05_L209_T001_047040_STAGE4B_20250206 | https://pulse.mk.co.kr/news/english/11234023 | direct_public_news_plus_sellside_detail; not a pure company IR row but event date and numbers are explicit | 2024 annual operating profit fell sharply, but Q4 profit beat came from mixed/one-off factors; the analyst note separates housing completion, Vietnam land sale, civil cost additions, receivables impairment, and new-order guide miss. |
| C05_L209_T002_375500_STAGE3_YELLOW_20250206 | https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25783&keyword=&searchword= | direct_company_ir_news | Official 2024 performance release reported annual sales KRW8.3184T and OP KRW270.9B, Q4 sequential sales/OP/order improvement, cost-rate improvement, net cash, and 2025 OP/order guidance. |
| C05_L209_T003_028050_STAGE3_GREEN_20240725 | https://samsungena.com/en/newsroom/news/view?idx=15609 | direct_company_ir_news | Official Q2 2024 release showed revenue/OP/net profit above consensus and large new orders/backlog, but year-on-year profit declined and the future bridge depended on conversion of backlog quality. |
| C05_L209_T004_016250_STAGE4B_20240423 | https://securities.miraeasset.com/bbs/download/2125811.pdf?attachmentId=2125811 | sellside_report_with_embedded_news_event; direct DART/KRX preferred in future repair | Representative news in the report notes Q1 2024 provisional OP fell 68.27% YoY and revenue fell 35.17%. |
| C05_L209_T005_003070_STAGE2_WATCH_20250225 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250225000995&langTpCd=0&method=search&orgid=G&rcpno=20250225000995&tran=Y | direct_krx_disclosure_event; details require manual filing table extraction | KRX correction filing for 2024 result-change disclosure supplies a direct issuer/event trail, but the case is result-only and needs cash/margin decomposition before any Actionable bonus. |
| C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250515000436&docno=&method=search&viewerhost= | direct_krx_quarterly_report_plus_news_explanation | KRX quarterly report and company-related coverage show Q1 2025 operating profit turnaround; the news explains cost-structure improvement, high-profit new work, lower debt ratio, and order backlog around KRW10.3T. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | basis | adjustment | window_status |
| --- | --- | --- | --- | --- | --- |
| 047040 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv | atlas/symbol_profiles/047/047040.json | tradable_raw | raw_unadjusted_marcap | clean_180D_window |
| 375500 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv | atlas/symbol_profiles/375/375500.json | tradable_raw | raw_unadjusted_marcap | clean_180D_window |
| 028050 | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv, atlas/ohlcv_tradable_by_symbol_year/028/028050/2025.csv | atlas/symbol_profiles/028/028050.json | tradable_raw | raw_unadjusted_marcap | clean_180D_window |
| 016250 | atlas/ohlcv_tradable_by_symbol_year/016/016250/2024.csv, atlas/ohlcv_tradable_by_symbol_year/016/016250/2025.csv | atlas/symbol_profiles/016/016250.json | tradable_raw | raw_unadjusted_marcap | clean_180D_window |
| 003070 | atlas/ohlcv_tradable_by_symbol_year/003/003070/2025.csv | atlas/symbol_profiles/003/003070.json | tradable_raw | raw_unadjusted_marcap | clean_180D_window |
| 005960 | atlas/ohlcv_tradable_by_symbol_year/005/005960/2025.csv, atlas/ohlcv_tradable_by_symbol_year/005/005960/2026.csv | atlas/symbol_profiles/005/005960.json | tradable_raw | raw_unadjusted_marcap | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | stage2_fields | stage3_fields | 4B_fields | interpretation |
| --- | --- | --- | --- | --- |
| C05_L209_T001_047040_STAGE4B_20250206 | public_event_or_disclosure; backlog_or_margin bridge varies by case | financial_visibility only when margin/cost bridge exists | margin_or_backlog_slowdown for Stage4B rows | Bad headline and one-off beat are not automatically thesis death. The correct C05 reading is local 4B/watch unless repeated cost-rate/cash impairment appears. |
| C05_L209_T002_375500_STAGE3_YELLOW_20250206 | public_event_or_disclosure; backlog_or_margin bridge varies by case | financial_visibility only when margin/cost bridge exists | margin_or_backlog_slowdown for Stage4B rows | This is the clean constructive row: order award, profitability, cost rate, and balance-sheet bridge appear together. |
| C05_L209_T003_028050_STAGE3_GREEN_20240725 | public_event_or_disclosure; backlog_or_margin bridge varies by case | financial_visibility only when margin/cost bridge exists | margin_or_backlog_slowdown for Stage4B rows | This looks like Green if backlog and consensus beat are overweighted, but the price path shows a classic late-cycle green trap. |
| C05_L209_T004_016250_STAGE4B_20240423 | public_event_or_disclosure; backlog_or_margin bridge varies by case | financial_visibility only when margin/cost bridge exists | margin_or_backlog_slowdown for Stage4B rows | Correctly blocks Green; however, later rebound means the row should be local 4B/watch rather than automatic hard 4C. |
| C05_L209_T005_003070_STAGE2_WATCH_20250225 | public_event_or_disclosure; backlog_or_margin bridge varies by case | financial_visibility only when margin/cost bridge exists | margin_or_backlog_slowdown for Stage4B rows | A corrected result disclosure is an existence proof, not a conversion proof. The signal can be watched but should not receive the same bonus as direct margin/cash improvement. |
| C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515 | public_event_or_disclosure; backlog_or_margin bridge varies by case | financial_visibility only when margin/cost bridge exists | margin_or_backlog_slowdown for Stage4B rows | This is a better Stage2-Actionable row than generic order backlog because cost structure and balance-sheet bridge are explicit. |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Actual entry OHLC rows

| trigger_id | price_path | entry_date | entry_price | o | h | l | c | v | amount | market_cap | shares | market |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_L209_T001_047040_STAGE4B_20250206 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv | 2025-02-07 | 3330 | 3325 | 3405 | 3315 | 3330 | 1022156 | 3441005435 | 1384023384540 | 415622638 | KOSPI |
| C05_L209_T002_375500_STAGE3_YELLOW_20250206 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv | 2025-02-07 | 36900 | 35250 | 37100 | 34950 | 36900 | 699699 | 25566242550 | 1427794688700 | 38693623 | KOSPI |
| C05_L209_T003_028050_STAGE3_GREEN_20240725 | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv, atlas/ohlcv_tradable_by_symbol_year/028/028050/2025.csv | 2024-07-26 | 27900 | 26050 | 28550 | 26000 | 27900 | 6403200 | 177459783004 | 5468400000000 | 196000000 | KOSPI |
| C05_L209_T004_016250_STAGE4B_20240423 | atlas/ohlcv_tradable_by_symbol_year/016/016250/2024.csv, atlas/ohlcv_tradable_by_symbol_year/016/016250/2025.csv | 2024-04-24 | 15550 | 15460 | 15650 | 15360 | 15550 | 4142 | 63969880 | 50437746750 | 3243585 | KOSDAQ |
| C05_L209_T005_003070_STAGE2_WATCH_20250225 | atlas/ohlcv_tradable_by_symbol_year/003/003070/2025.csv | 2025-02-26 | 9140 | 8950 | 9160 | 8950 | 9140 | 28679 | 261157390 | 173044996820 | 18932713 | KOSPI |
| C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515 | atlas/ohlcv_tradable_by_symbol_year/005/005960/2025.csv, atlas/ohlcv_tradable_by_symbol_year/005/005960/2026.csv | 2025-05-16 | 4395 | 4250 | 4465 | 4240 | 4395 | 60609 | 265127715 | 100850583885 | 22946663 | KOSPI |

### 12.2 MFE/MAE path table

| trigger_id | entry_price | MFE30 | MAE30 | 30D_end | MFE90 | MAE90 | 90D_end | MFE180 | MAE180 | 180D_end | peak_date | peak_price | post_peak_DD | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_L209_T001_047040_STAGE4B_20250206 | 3330 | 12.91 | -3.9 | 2025-03-21 | 44.29 | -11.71 | 2025-06-20 | 44.29 | -11.71 | 2025-11-03 | 2025-06-05 | 4805 | -26.33 | positive_after_bad_result_headline_MFE90_44pct_with_MAE90_minus12pct |
| C05_L209_T002_375500_STAGE3_YELLOW_20250206 | 36900 | 27.24 | -5.28 | 2025-03-21 | 52.3 | -5.28 | 2025-06-20 | 61.79 | -5.28 | 2025-11-03 | 2025-06-26 | 59700 | -32.91 | positive_MFE180_61pct_with_low_MAE |
| C05_L209_T003_028050_STAGE3_GREEN_20240725 | 27900 | 5.02 | -15.95 | 2024-09-06 | 5.02 | -41.58 | 2024-12-09 | 5.02 | -41.58 | 2025-04-24 | 2024-07-30 | 29300 | -44.37 | counterexample_low_MFE_high_MAE_late_cycle_green_trap |
| C05_L209_T004_016250_STAGE4B_20240423 | 15550 | 8.04 | -1.22 | 2024-06-10 | 20.51 | -9.97 | 2024-09-03 | 20.51 | -24.31 | 2025-01-20 | 2024-08-05 | 18740 | -37.19 | mixed_local_rebound_MFE90_20pct_but_180D_close_negative |
| C05_L209_T005_003070_STAGE2_WATCH_20250225 | 9140 | 0.66 | -12.58 | 2025-04-09 | 18.82 | -12.58 | 2025-07-09 | 18.82 | -12.58 | 2025-11-20 | 2025-07-02 | 10860 | -21.18 | weak_positive_MFE180_but_high_initial_MAE_and_flat_close |
| C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515 | 4395 | 26.51 | -3.53 | 2025-06-30 | 56.77 | -3.53 | 2025-09-23 | 56.77 | -3.53 | 2026-02-06 | 2025-09-11 | 6890 | -24.09 | strong_positive_MFE180_56pct_low_MAE |

## 13. Current Calibrated Profile Stress Test

| trigger_id | trigger_type | score_before | score_after_shadow | current_profile_verdict | stress finding |
| --- | --- | --- | --- | --- | --- |
| C05_L209_T001_047040_STAGE4B_20250206 | Stage4B | 48.0 | 62.0 | current_profile_error | hard_4c_thesis_break_routes_to_4c may over-route if it treats one-off/cost-rate noise as permanent project thesis death. |
| C05_L209_T002_375500_STAGE3_YELLOW_20250206 | Stage3-Yellow | 84.0 | 86.5 | current_profile_correct | Current v12 likely lands around Yellow/near-Green; this is acceptable because the bridge is more than a headline. |
| C05_L209_T003_028050_STAGE3_GREEN_20240725 | Stage3-Green | 88.0 | 74.0 | current_profile_error | Stage3-Green would be a false positive if consensus/backlog points dominate without forward margin/cash freshness. |
| C05_L209_T004_016250_STAGE4B_20240423 | Stage4B | 55.0 | 57.0 | current_profile_correct | 4B watch is useful; hard exit requires additional thesis break evidence. |
| C05_L209_T005_003070_STAGE2_WATCH_20250225 | Stage2 | 72.0 | 63.0 | current_profile_error | Stage2 actionable bonus may be too generous when direct filing only proves result-change existence without margin-cash bridge. |
| C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515 | Stage2-Actionable | 79.0 | 82.5 | current_profile_correct | Stage2-Actionable is correct; Green requires persistence in later quarters. |

## 14. Stage2 / Yellow / Green Comparison

| stage | representative_rows | avg_MFE90 | avg_MAE90 | audit |
| --- | --- | --- | --- | --- |
| Stage2 / Stage2-Actionable | 003070, 005960 | 37.8 | -8.05 | Actionable is good only when cost/backlog/cash bridge exists; result-only Stage2 should remain watch-capped |
| Stage3-Yellow | 375500 | 52.3 | -5.28 | high-quality bridge; cost rate and net cash support Yellow |
| Stage3-Green | 028050 | 5.02 | -41.58 | late-cycle backlog/consensus beat is false-positive without forward margin/cash freshness |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | entry | MFE30 | MFE180 | post_peak_DD | 4B evidence type | timing verdict |
| --- | --- | --- | --- | --- | --- | --- |
| C05_L209_T001_047040_STAGE4B_20250206 | 3330.0 | 12.91 | 44.29 | -26.33 | margin_or_backlog_slowdown / oneoff_quality | local watch, not full 4B or hard 4C without non-price thesis break confirmation |
| C05_L209_T002_375500_STAGE3_YELLOW_20250206 | 36900.0 | 27.24 | 61.79 | -32.91 | not_applicable | not_applicable |
| C05_L209_T003_028050_STAGE3_GREEN_20240725 | 27900.0 | 5.02 | 5.02 | -44.37 | not_applicable | not_applicable |
| C05_L209_T004_016250_STAGE4B_20240423 | 15550.0 | 8.04 | 20.51 | -37.19 | margin_or_backlog_slowdown / oneoff_quality | local watch, not full 4B or hard 4C without non-price thesis break confirmation |
| C05_L209_T005_003070_STAGE2_WATCH_20250225 | 9140.0 | 0.66 | 18.82 | -21.18 | not_applicable | not_applicable |
| C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515 | 4395.0 | 26.51 | 56.77 | -24.09 | not_applicable | not_applicable |

## 16. 4C Protection Audit

No representative row is emitted as Stage4C in this loop. That absence is intentional: Daewoo and SGC show why a bad result or cost-rate shock should not automatically become hard 4C unless the non-price thesis actually breaks. The 4C guard is therefore tested as an over-routing risk, not as a new hard-exit success row.

## 17. Sector-Specific Rule Candidate

`L1_INDUSTRIALS_INFRA_DEFENSE_GRID` EPC/order/revenue evidence should be discounted unless it bridges to cost-rate control, working-capital conversion, and realizable margin. In construction/EPC, the headline is the front gate; margin and cash conversion are the turnstile. A company can stand in front of the gate without passing through.

## 18. Canonical-Archetype Rule Candidate

`C05_EPC_MEGA_CONTRACT_MARGIN_GAP` should use a result-quality ladder: order/backlog headline → margin/cost-rate proof → working-capital/cash conversion → persistence. Green should be capped when backlog and consensus beat are not connected to forward margin/cash freshness. One-off/kitchen-sink or cost-rate noise should be Stage4B watch first, not hard 4C, unless repeated non-price thesis damage confirms it.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | late_green_count | alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | current calibrated proxy | result/order/backlog can still over-promote two late/result-only rows | 6 | all six listed triggers | 32.95 | -14.11 | 34.53 | -16.5 | 3/6 residual errors | 1 late Green trap | mixed; too generous for result-only and backlog-only C05 rows |
| P0b e2r_2_0_baseline_reference | rollback reference | looser bridge requirement would accept more headline rows | 6 | all six listed triggers | 32.95 | -14.11 | 34.53 | -16.5 | worse than P0 | 1 late Green trap | weaker than calibrated profile |
| P1 L1 sector candidate | sector-specific | discount L1 order/result evidence unless cost-rate and cash conversion are explicit | 6 | Daewoo/DL/Samsung/SGC/Kolon/Dongbu | 32.95 | -14.11 | 34.53 | -16.5 | 2/6 residual errors after cap | 0 Green traps | better guardrail, but still broad |
| P2 C05 canonical candidate | canonical-archetype-specific | use result-quality ladder: order/backlog -> margin -> cost-rate -> working-capital -> persistence | 6 | DL/Dongbu promoted; Samsung/Kolon capped; Daewoo/SGC watch | 51.12 | -6.84 | 54.28 | -6.84 | 1/6 residual watch | 0 Green traps | best score-return alignment |
| P3 counterexample guard | guard profile | force direct margin/cash bridge before Stage2-Actionable and Green; one-off losses are watch unless thesis death repeats | 6 | same as P2 with stricter source-quality cap | 51.12 | -6.84 | 54.28 | -6.84 | 1/6 residual watch | 0 Green traps | safer but may delay true turnarounds |

## 20. Score-Return Alignment Matrix

| trigger_id | before_stage | after_stage | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| C05_L209_T001_047040_STAGE4B_20250206 | Stage4B | Stage2 | 44.29 | -11.71 | positive_after_bad_result_headline_MFE90_44pct_with_MAE90_minus12pct |
| C05_L209_T002_375500_STAGE3_YELLOW_20250206 | Stage3-Yellow | Stage3-Yellow | 52.3 | -5.28 | positive_MFE180_61pct_with_low_MAE |
| C05_L209_T003_028050_STAGE3_GREEN_20240725 | Stage3-Green | Stage2-Actionable | 5.02 | -41.58 | counterexample_low_MFE_high_MAE_late_cycle_green_trap |
| C05_L209_T004_016250_STAGE4B_20240423 | Stage2 | Stage2 | 20.51 | -9.97 | mixed_local_rebound_MFE90_20pct_but_180D_close_negative |
| C05_L209_T005_003070_STAGE2_WATCH_20250225 | Stage2-Actionable | Stage2 | 18.82 | -12.58 | weak_positive_MFE180_but_high_initial_MAE_and_flat_close |
| C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515 | Stage3-Yellow | Stage3-Yellow | 56.77 | -3.53 | strong_positive_MFE180_56pct_low_MAE |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR | 3 | 3 | 2 | 0 | 6 | 0 | 6 | 6 | 3 | yes | yes | direct URL/MFE-MAE repaired C05 rows added; future C05 should use new direct cashflow/working-capital rows only |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_green_revision_min; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: green_trap_from_backlog_consensus_beat_without_forward_cash_margin; stage2_actionable_too_early_for_direct_result_disclosure_without_cash_bridge; hard_4c_overroute_risk_on_oneoff_cost_noise
new_axis_proposed: c05_result_quality_margin_cash_conversion_ladder; c05_oneoff_cost_noise_4c_qualification_guard
existing_axis_strengthened: stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_qualified_for_oneoff_cost_noise_only
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L1 EPC/order/revenue evidence should be discounted unless cost-rate, working-capital, and realizable margin are visible.
canonical_archetype_rule_candidate: C05 requires result-quality ladder from headline to cash/margin persistence.
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 6 new independent cases, 3 counterexamples, and 3 residual errors for R1/L1/C05.

## 23. Validation Scope / Non-Validation Scope

Validated: historical event dates, entry dates, Stock-Web tradable OHLC rows, 30/90/180 trading-day MFE/MAE, canonical trigger labels, C05 duplicate keys. Not validated: live current rankings, production scoring, brokerage execution, current investment suitability, and any price beyond stock-web `2026-02-20`.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c05_result_quality_margin_cash_conversion_ladder,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,Require margin/cost-rate/cash bridge after order/backlog/result headline,Improves false-positive handling for Samsung/Kolon while preserving DL/Dongbu positives,C05_L209_T002_375500_STAGE3_YELLOW_20250206|C05_L209_T003_028050_STAGE3_GREEN_20240725|C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515,6,6,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c05_oneoff_cost_noise_4c_qualification_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,Do not hard-4C one-off result/cost noise without repeated non-price thesis break,Prevents Daewoo/SGC over-routing to hard 4C,C05_L209_T001_047040_STAGE4B_20250206|C05_L209_T004_016250_STAGE4B_20240423,6,6,3,medium,canonical_shadow_only,qualifies hard_4c axis only inside C05
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","manifest_tradable_row_count":14354401,"manifest_raw_row_count":15214118,"symbol_count":5414}
{"row_type":"case","case_id":"C05_L209_01_DAEWOO_EC_2024_ONEOFF_BEAT_NOT_HARD4C","symbol":"047040","company_name":"Daewoo E&C / 대우건설","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","case_type":"guardrail_positive_hard4c_false_negative_prevention","positive_or_counterexample":"positive","best_trigger":"C05_L209_T001_047040_STAGE4B_20250206","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_after_bad_result_headline_MFE90_44pct_with_MAE90_minus12pct","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"Bad headline and one-off beat are not automatically thesis death. The correct C05 reading is local 4B/watch unless repeated cost-rate/cash impairment appears."}
{"row_type":"case","case_id":"C05_L209_02_DLENC_2024_COST_RATE_RECOVERY_CONFIRMED","symbol":"375500","company_name":"DL E&C / DL이앤씨","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","case_type":"positive_margin_quality_and_order_recovery","positive_or_counterexample":"positive","best_trigger":"C05_L209_T002_375500_STAGE3_YELLOW_20250206","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE180_61pct_with_low_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"This is the clean constructive row: order award, profitability, cost rate, and balance-sheet bridge appear together."}
{"row_type":"case","case_id":"C05_L209_03_SAMSUNG_EA_Q2_BACKLOG_GREEN_TRAP","symbol":"028050","company_name":"Samsung E&A / 삼성E&A","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","case_type":"counterexample_backlog_and_consensus_beat_without_forward_conversion","positive_or_counterexample":"counterexample","best_trigger":"C05_L209_T003_028050_STAGE3_GREEN_20240725","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE_late_cycle_green_trap","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"This looks like Green if backlog and consensus beat are overweighted, but the price path shows a classic late-cycle green trap."}
{"row_type":"case","case_id":"C05_L209_04_SGC_EC_Q1_OP_DROP_LOCAL_4B_NOT_HARD_EXIT","symbol":"016250","company_name":"SGC E&C / SGC이앤씨","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","case_type":"counterexample_or_watch_cost_rate_pressure_with_later_rebound_then_decay","positive_or_counterexample":"counterexample","best_trigger":"C05_L209_T004_016250_STAGE4B_20240423","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_local_rebound_MFE90_20pct_but_180D_close_negative","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Correctly blocks Green; however, later rebound means the row should be local 4B/watch rather than automatic hard 4C."}
{"row_type":"case","case_id":"C05_L209_05_KOLON_GLOBAL_CORRECTION_SOURCE_QUALITY_CAP","symbol":"003070","company_name":"Kolon Global / 코오롱글로벌","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","case_type":"counterexample_source_quality_and_result_only_cap","positive_or_counterexample":"counterexample","best_trigger":"C05_L209_T005_003070_STAGE2_WATCH_20250225","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_positive_MFE180_but_high_initial_MAE_and_flat_close","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A corrected result disclosure is an existence proof, not a conversion proof. The signal can be watched but should not receive the same bonus as direct margin/cash improvement."}
{"row_type":"case","case_id":"C05_L209_06_DONGBU_EC_Q1_TURNAROUND_DIRECT_REPORT","symbol":"005960","company_name":"Dongbu Construction / 동부건설","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","case_type":"positive_turnaround_margin_cost_backlog_bridge","positive_or_counterexample":"positive","best_trigger":"C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_MFE180_56pct_low_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"This is a better Stage2-Actionable row than generic order backlog because cost structure and balance-sheet bridge are explicit."}
{"row_type":"trigger","trigger_id":"C05_L209_T001_047040_STAGE4B_20250206","case_id":"C05_L209_01_DAEWOO_EC_2024_ONEOFF_BEAT_NOT_HARD4C","symbol":"047040","company_name":"Daewoo E&C / 대우건설","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","sector":"EPC/building/infrastructure contractors","primary_archetype":"order/backlog/result headline vs margin/cash conversion gap","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair","trigger_type":"Stage4B","trigger_date":"2025-02-06","evidence_available_at_that_date":"2024 annual operating profit fell sharply, but Q4 profit beat came from mixed/one-off factors; the analyst note separates housing completion, Vietnam land sale, civil cost additions, receivables impairment, and new-order guide miss.","evidence_source":"https://pulse.mk.co.kr/news/english/11234023","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_phase_or_result_quality_watch","oneoff_adjustment_quality"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-07","entry_price":3330.0,"entry_ohlc_row":{"d":"2025-02-07","o":3325.0,"h":3405.0,"l":3315.0,"c":3330.0,"v":1022156,"a":3441005435.0,"mc":1384023384540.0,"s":415622638,"m":"KOSPI"},"MFE_30D_pct":12.91,"MFE_90D_pct":44.29,"MFE_180D_pct":44.29,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.9,"MAE_90D_pct":-11.71,"MAE_180D_pct":-11.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-05","peak_price":4805.0,"drawdown_after_peak_pct":-26.33,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_watch_not_full_4B_or_no_prior_stage2_anchor","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_after_bad_result_headline_mfe90_44pct_with_mae90_minus12pct","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|2025-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c05_shadow","case_id":"C05_L209_01_DAEWOO_EC_2024_ONEOFF_BEAT_NOT_HARD4C","trigger_id":"C05_L209_T001_047040_STAGE4B_20250206","symbol":"047040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":1,"revision_score":-2,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":5,"fcf_conversion_score":-3,"cost_rate_risk_score":-5,"source_quality_score":3,"oneoff_adjustment_quality_score":-3},"weighted_score_before":48.0,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":1,"revision_score":-1,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"order_intake_quality_score":5,"fcf_conversion_score":-3,"cost_rate_risk_score":-3,"source_quality_score":3,"oneoff_adjustment_quality_score":-2},"weighted_score_after":62.0,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","fcf_conversion_score","source_quality_score","cost_rate_risk_score"],"component_delta_explanation":"Stage4B local watch, not hard 4C. Require repeated cost-rate miss, receivables impairment, liquidity stress, or backlog collapse before hard 4C.","MFE_90D_pct":44.29,"MAE_90D_pct":-11.71,"score_return_alignment_label":"positive_after_bad_result_headline_MFE90_44pct_with_MAE90_minus12pct","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"trigger","trigger_id":"C05_L209_T002_375500_STAGE3_YELLOW_20250206","case_id":"C05_L209_02_DLENC_2024_COST_RATE_RECOVERY_CONFIRMED","symbol":"375500","company_name":"DL E&C / DL이앤씨","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","sector":"EPC/building/infrastructure contractors","primary_archetype":"order/backlog/result headline vs margin/cash conversion gap","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair","trigger_type":"Stage3-Yellow","trigger_date":"2025-02-06","evidence_available_at_that_date":"Official 2024 performance release reported annual sales KRW8.3184T and OP KRW270.9B, Q4 sequential sales/OP/order improvement, cost-rate improvement, net cash, and 2025 OP/order guidance.","evidence_source":"https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25783&keyword=&searchword=","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-07","entry_price":36900.0,"entry_ohlc_row":{"d":"2025-02-07","o":35250.0,"h":37100.0,"l":34950.0,"c":36900.0,"v":699699,"a":25566242550.0,"mc":1427794688700.0,"s":38693623,"m":"KOSPI"},"MFE_30D_pct":27.24,"MFE_90D_pct":52.3,"MFE_180D_pct":61.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.28,"MAE_90D_pct":-5.28,"MAE_180D_pct":-5.28,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-06-26","peak_price":59700.0,"drawdown_after_peak_pct":-32.91,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"positive_mfe180_61pct_with_low_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|2025-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c05_shadow","case_id":"C05_L209_02_DLENC_2024_COST_RATE_RECOVERY_CONFIRMED","trigger_id":"C05_L209_T002_375500_STAGE3_YELLOW_20250206","symbol":"375500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":7,"order_intake_quality_score":8,"fcf_conversion_score":7,"cost_rate_risk_score":2,"source_quality_score":5,"oneoff_adjustment_quality_score":2},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":9,"revision_score":11,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":7,"order_intake_quality_score":8,"fcf_conversion_score":8,"cost_rate_risk_score":2,"source_quality_score":5,"oneoff_adjustment_quality_score":2},"weighted_score_after":86.5,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","fcf_conversion_score","source_quality_score","cost_rate_risk_score"],"component_delta_explanation":"Permit high Yellow; promote to Green only after follow-up order/cash conversion or second cost-rate confirmation.","MFE_90D_pct":52.3,"MAE_90D_pct":-5.28,"score_return_alignment_label":"positive_MFE180_61pct_with_low_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"trigger","trigger_id":"C05_L209_T003_028050_STAGE3_GREEN_20240725","case_id":"C05_L209_03_SAMSUNG_EA_Q2_BACKLOG_GREEN_TRAP","symbol":"028050","company_name":"Samsung E&A / 삼성E&A","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","sector":"EPC/building/infrastructure contractors","primary_archetype":"order/backlog/result headline vs margin/cash conversion gap","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair","trigger_type":"Stage3-Green","trigger_date":"2024-07-25","evidence_available_at_that_date":"Official Q2 2024 release showed revenue/OP/net profit above consensus and large new orders/backlog, but year-on-year profit declined and the future bridge depended on conversion of backlog quality.","evidence_source":"https://samsungena.com/en/newsroom/news/view?idx=15609","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","large_order_backlog"],"stage3_evidence_fields":["financial_visibility","consensus_beat_without_forward_margin_freshness","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv, atlas/ohlcv_tradable_by_symbol_year/028/028050/2025.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-26","entry_price":27900.0,"entry_ohlc_row":{"d":"2024-07-26","o":26050.0,"h":28550.0,"l":26000.0,"c":27900.0,"v":6403200,"a":177459783004.0,"mc":5468400000000.0,"s":196000000,"m":"KOSPI"},"MFE_30D_pct":5.02,"MFE_90D_pct":5.02,"MFE_180D_pct":5.02,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.95,"MAE_90D_pct":-41.58,"MAE_180D_pct":-41.58,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":29300.0,"drawdown_after_peak_pct":-44.37,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"counterexample_low_mfe_high_mae_late_cycle_green_trap","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c05_shadow","case_id":"C05_L209_03_SAMSUNG_EA_Q2_BACKLOG_GREEN_TRAP","trigger_id":"C05_L209_T003_028050_STAGE3_GREEN_20240725","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":9,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":-3,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":-2,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"order_intake_quality_score":9,"fcf_conversion_score":1,"cost_rate_risk_score":-2,"source_quality_score":5,"oneoff_adjustment_quality_score":-1},"weighted_score_before":88.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":-3,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":-2,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"order_intake_quality_score":6,"fcf_conversion_score":-2,"cost_rate_risk_score":-2,"source_quality_score":5,"oneoff_adjustment_quality_score":-1},"weighted_score_after":74.0,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","fcf_conversion_score","source_quality_score","cost_rate_risk_score"],"component_delta_explanation":"Cap at Yellow after a local rally unless backlog quality turns into fresh order margin, working-capital conversion, or next-cycle OP durability.","MFE_90D_pct":5.02,"MAE_90D_pct":-41.58,"score_return_alignment_label":"counterexample_low_MFE_high_MAE_late_cycle_green_trap","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"trigger","trigger_id":"C05_L209_T004_016250_STAGE4B_20240423","case_id":"C05_L209_04_SGC_EC_Q1_OP_DROP_LOCAL_4B_NOT_HARD_EXIT","symbol":"016250","company_name":"SGC E&C / SGC이앤씨","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","sector":"EPC/building/infrastructure contractors","primary_archetype":"order/backlog/result headline vs margin/cash conversion gap","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair","trigger_type":"Stage4B","trigger_date":"2024-04-23","evidence_available_at_that_date":"Representative news in the report notes Q1 2024 provisional OP fell 68.27% YoY and revenue fell 35.17%.","evidence_source":"https://securities.miraeasset.com/bbs/download/2125811.pdf?attachmentId=2125811","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_phase_or_result_quality_watch","oneoff_adjustment_quality"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/016/016250/2024.csv, atlas/ohlcv_tradable_by_symbol_year/016/016250/2025.csv","profile_path":"atlas/symbol_profiles/016/016250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-24","entry_price":15550.0,"entry_ohlc_row":{"d":"2024-04-24","o":15460.0,"h":15650.0,"l":15360.0,"c":15550.0,"v":4142,"a":63969880.0,"mc":50437746750.0,"s":3243585,"m":"KOSDAQ"},"MFE_30D_pct":8.04,"MFE_90D_pct":20.51,"MFE_180D_pct":20.51,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.22,"MAE_90D_pct":-9.97,"MAE_180D_pct":-24.31,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-08-05","peak_price":18740.0,"drawdown_after_peak_pct":-37.19,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_watch_not_full_4B_or_no_prior_stage2_anchor","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"mixed_local_rebound_mfe90_20pct_but_180d_close_negative","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|016250|2024-04-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c05_shadow","case_id":"C05_L209_04_SGC_EC_Q1_OP_DROP_LOCAL_4B_NOT_HARD_EXIT","trigger_id":"C05_L209_T004_016250_STAGE4B_20240423","symbol":"016250","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":-3,"revision_score":-4,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":3,"fcf_conversion_score":-2,"cost_rate_risk_score":-6,"source_quality_score":1,"oneoff_adjustment_quality_score":-1},"weighted_score_before":55.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":-3,"revision_score":-4,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":3,"fcf_conversion_score":-2,"cost_rate_risk_score":-6,"source_quality_score":1,"oneoff_adjustment_quality_score":-1},"weighted_score_after":57.0,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","fcf_conversion_score","source_quality_score","cost_rate_risk_score"],"component_delta_explanation":"Keep as Stage4B/local watch. Do not promote to Stage2; do not hard-4C unless next reports confirm cash impairment or project loss recurrence.","MFE_90D_pct":20.51,"MAE_90D_pct":-9.97,"score_return_alignment_label":"mixed_local_rebound_MFE90_20pct_but_180D_close_negative","current_profile_verdict":"current_profile_correct"}
{"row_type":"trigger","trigger_id":"C05_L209_T005_003070_STAGE2_WATCH_20250225","case_id":"C05_L209_05_KOLON_GLOBAL_CORRECTION_SOURCE_QUALITY_CAP","symbol":"003070","company_name":"Kolon Global / 코오롱글로벌","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","sector":"EPC/building/infrastructure contractors","primary_archetype":"order/backlog/result headline vs margin/cash conversion gap","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair","trigger_type":"Stage2","trigger_date":"2025-02-25","evidence_available_at_that_date":"KRX correction filing for 2024 result-change disclosure supplies a direct issuer/event trail, but the case is result-only and needs cash/margin decomposition before any Actionable bonus.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250225000995&langTpCd=0&method=search&orgid=G&rcpno=20250225000995&tran=Y","stage2_evidence_fields":["public_event_or_disclosure","public_event_or_disclosure","source_quality_cap"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003070/2025.csv","profile_path":"atlas/symbol_profiles/003/003070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-26","entry_price":9140.0,"entry_ohlc_row":{"d":"2025-02-26","o":8950.0,"h":9160.0,"l":8950.0,"c":9140.0,"v":28679,"a":261157390.0,"mc":173044996820.0,"s":18932713,"m":"KOSPI"},"MFE_30D_pct":0.66,"MFE_90D_pct":18.82,"MFE_180D_pct":18.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.58,"MAE_90D_pct":-12.58,"MAE_180D_pct":-12.58,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-02","peak_price":10860.0,"drawdown_after_peak_pct":-21.18,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"weak_positive_mfe180_but_high_initial_mae_and_flat_close","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|003070|2025-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c05_shadow","case_id":"C05_L209_05_KOLON_GLOBAL_CORRECTION_SOURCE_QUALITY_CAP","trigger_id":"C05_L209_T005_003070_STAGE2_WATCH_20250225","symbol":"003070","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":-1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"order_intake_quality_score":2,"fcf_conversion_score":0,"cost_rate_risk_score":-3,"source_quality_score":4,"oneoff_adjustment_quality_score":-2},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":0,"revision_score":-2,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"order_intake_quality_score":2,"fcf_conversion_score":-1,"cost_rate_risk_score":-3,"source_quality_score":2,"oneoff_adjustment_quality_score":-2},"weighted_score_after":63.0,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","fcf_conversion_score","source_quality_score","cost_rate_risk_score"],"component_delta_explanation":"Stage2 watch cap. Require margin bridge, backlog quality, or cash conversion for Actionable/Yellow.","MFE_90D_pct":18.82,"MAE_90D_pct":-12.58,"score_return_alignment_label":"weak_positive_MFE180_but_high_initial_MAE_and_flat_close","current_profile_verdict":"current_profile_too_early"}
{"row_type":"trigger","trigger_id":"C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515","case_id":"C05_L209_06_DONGBU_EC_Q1_TURNAROUND_DIRECT_REPORT","symbol":"005960","company_name":"Dongbu Construction / 동부건설","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","sector":"EPC/building/infrastructure contractors","primary_archetype":"order/backlog/result headline vs margin/cash conversion gap","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair","trigger_type":"Stage2-Actionable","trigger_date":"2025-05-15","evidence_available_at_that_date":"KRX quarterly report and company-related coverage show Q1 2025 operating profit turnaround; the news explains cost-structure improvement, high-profit new work, lower debt ratio, and order backlog around KRW10.3T.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250515000436&docno=&method=search&viewerhost=","stage2_evidence_fields":["public_event_or_disclosure","margin_or_cost_structure_bridge","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005960/2025.csv, atlas/ohlcv_tradable_by_symbol_year/005/005960/2026.csv","profile_path":"atlas/symbol_profiles/005/005960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-05-16","entry_price":4395.0,"entry_ohlc_row":{"d":"2025-05-16","o":4250.0,"h":4465.0,"l":4240.0,"c":4395.0,"v":60609,"a":265127715.0,"mc":100850583885.0,"s":22946663,"m":"KOSPI"},"MFE_30D_pct":26.51,"MFE_90D_pct":56.77,"MFE_180D_pct":56.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.53,"MAE_90D_pct":-3.53,"MAE_180D_pct":-3.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-09-11","peak_price":6890.0,"drawdown_after_peak_pct":-24.09,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"strong_positive_mfe180_56pct_low_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|005960|2025-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c05_shadow","case_id":"C05_L209_06_DONGBU_EC_Q1_TURNAROUND_DIRECT_REPORT","trigger_id":"C05_L209_T006_005960_STAGE2_ACTIONABLE_20250515","symbol":"005960","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":8,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6,"order_intake_quality_score":8,"fcf_conversion_score":5,"cost_rate_risk_score":2,"source_quality_score":5,"oneoff_adjustment_quality_score":1},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6,"order_intake_quality_score":8,"fcf_conversion_score":6,"cost_rate_risk_score":2,"source_quality_score":5,"oneoff_adjustment_quality_score":1},"weighted_score_after":82.5,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","fcf_conversion_score","source_quality_score","cost_rate_risk_score"],"component_delta_explanation":"Keep Actionable/Yellow boundary open because margin, debt, and backlog conversion bridges are visible.","MFE_90D_pct":56.77,"MAE_90D_pct":-3.53,"score_return_alignment_label":"strong_positive_MFE180_56pct_low_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"aggregate","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ORDER_BACKLOG_RESULT_CASH_MARGIN_QUALITY_REPAIR","positive_case_count":3,"counterexample_count":3,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"new_trigger_family_count":6,"same_archetype_new_trigger_family_count":6,"calibration_usable_trigger_count":6,"representative_trigger_count":6,"current_profile_error_count":3,"sector_rule_candidate":"L1 EPC/order/revenue evidence should be discounted unless it bridges to cost-rate control, working-capital conversion, and realizable margin.","canonical_rule_candidate":"C05 requires a result-quality ladder from order/backlog headline through margin, cost-rate, working-capital, and persistence; 4B and 4C must be separated by thesis-break confirmation.","coverage_gap_after_this_loop":"C05 has additional direct URL/MFE-MAE repaired rows; next C05 should use only direct cashflow/working-capital rows."}
{"row_type":"residual_contribution","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["green_trap_from_backlog_consensus_beat_without_forward_cash_margin","stage2_actionable_too_early_for_direct_result_disclosure_without_cash_bridge","hard_4c_overroute_risk_on_oneoff_cost_noise"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"research_state","completed_round":"R1","completed_loop":209,"selection_basis":"docs/core/V12_Research_No_Repeat_Index.md","selected_priority_bucket":"Priority 1 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair","round_schedule_status":"coverage_index_selected","round_sector_consistency":"pass","do_not_repeat_keys":["C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage4B|2025-02-07","C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage3-Yellow|2025-02-07","C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage3-Green|2024-07-26","C05_EPC_MEGA_CONTRACT_MARGIN_GAP|016250|Stage4B|2024-04-24","C05_EPC_MEGA_CONTRACT_MARGIN_GAP|003070|Stage2|2025-02-26","C05_EPC_MEGA_CONTRACT_MARGIN_GAP|005960|Stage2-Actionable|2025-05-16"],"next_recommended_archetypes":["C01 only for backlog-to-FCF direct rows","C13 only for AMPC/utilization direct rows","C15 only for spread freshness direct rows","C10 only for fresh order-conversion rows","R13 only for non-duplicate taxonomy compression"]}
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
completed_round = R1
completed_loop = 209
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C05 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
next_recommended_archetypes = C01 direct backlog-to-FCF rows; C13 AMPC/utilization direct rows; C15 spread freshness rows; C10 order-conversion rows; R13 only for non-duplicate taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- DL E&C direct performance release: https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25783&keyword=&searchword=
- Samsung E&A direct Q2 2024 performance release: https://samsungena.com/en/newsroom/news/view?idx=15609
- Daewoo E&C result article: https://pulse.mk.co.kr/news/english/11234023
- Dongbu Construction KRX quarterly report: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250515000436&docno=&method=search&viewerhost=
- Kolon Global KRX correction filing: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250225000995&langTpCd=0&method=search&orgid=G&rcpno=20250225000995&tran=Y
- SGC E&C Mirae Asset embedded news PDF: https://securities.miraeasset.com/bbs/download/2125811.pdf?attachmentId=2125811
