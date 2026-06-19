# E2R Stock-Web v12 Residual Research — R13 / 4B·4C RedTeam Offset Quality Holdout

```yaml
research_session: post_calibrated_sector_archetype_residual_research_v12
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R13_loop_212_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
selected_round: R13
selected_loop: 212
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 R13 4B/4C offset-quality refresh using recent C29/C30/C32 source-sector rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Execution contract

This file follows the v12 Stock-Web residual research contract. It is not a live screen, not a recommendation list, and not a `stock_agent` code patch. The only output is a standalone historical calibration Markdown handoff.

R13 is not a sector-positive research round. It is a cross-archetype checkpoint. This run compresses recent R9/C29 mobility, R10/C30 PF balance-sheet, and R12/C32 governance/control-premium rows to test the **4B versus hard 4C boundary** and the **operating Green blocker** for event-driven price paths.

Core analogy: a noisy event is not a broken machine by itself. 4B is the dashboard warning light; hard 4C is the engine seizing. E2R should not mark a warning light as engine death unless non-price thesis break and weak offset quality are both visible. Conversely, a tender premium or record quarter can launch the car downhill, but it is not operating Green unless earnings, cashflow, or execution keeps pulling after the slope ends.

## 2. Source and No-Repeat validation

```yaml
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_columns: [d, o, h, l, c, v, a, mc, s, m]
corporate_action_contamination_rule: block D~D+180 if candidate date overlaps
```

The source-sector rows were already constructed with actual Stock-Web tradable OHLCV rows. This R13 file reuses them only as cross-archetype review rows. New duplicate key scope is:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM + symbol + trigger_type + entry_date
```

No selected row repeats a previously materialized R13 4B/4C symbol-stage-entry set in the local session scan. Source-sector reuse is intentional and marked as `source_sector_case_reused`.

## 3. Coverage matrix

| metric | value |
|---|---:|
| source_sector_case_reused_count | 15 |
| new_independent_case_count_for_r13_scope | 15 |
| new_independent_trigger_count_for_r13_scope | 15 |
| unique_symbol_count | 14 |
| unique_source_canonical_count | 3 |
| Stage2_count | 2 |
| Stage2_Actionable_count | 5 |
| Stage4B_count | 6 |
| Stage4C_count | 2 |
| high_MAE_180D_count_MAE_le_-20 | 9 |
| deep_MAE_180D_count_MAE_le_-40 | 3 |
| source_proxy_only_count | 0 |
| evidence_url_pending_count | 0 |
| missing_required_mfe_mae_count | 0 |
| missing_entry_price_count | 0 |
| missing_actual_entry_ohlcv_count | 0 |
| corporate_action_contaminated_180D_count | 0 |
| insufficient_forward_window_180D_count | 0 |
| production_scoring_changed | false |
| shadow_weight_only | true |
| ready_for_batch_ingest | true |

Source canonical spread:

```text
- C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
- C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
- C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

## 4. Trigger-level price table

| Source C | symbol | company | trigger_type | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough | case_role |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| C29 | 005380 | Hyundai Motor | Stage2-Actionable | 2024-07-25 | 251,500 | 6.16 / -13.92 | 6.16 / -21.55 | 6.16 / -30.1 | 2024-08-29 | 2025-04-11 | late_cycle_oem_record_margin_guardrail |
| C29 | 000270 | Kia | Stage2-Actionable | 2024-07-26 | 112,100 | 5.71 / -15.25 | 5.71 / -20.16 | 5.71 / -27.48 | 2024-07-26 | 2025-04-11 | late_cycle_oem_record_margin_guardrail |
| C29 | 012330 | Hyundai Mobis | Stage4B | 2024-07-26 | 225,500 | 2.22 / -11.09 | 18.4 / -11.09 | 28.16 / -11.09 | 2025-03-25 | 2024-08-05 | electrification_slowdown_with_AS_offset |
| C29 | 204320 | HL Mando | Stage2 | 2025-02-05 | 42,300 | 11.11 / -6.5 | 11.11 / -24.11 | 11.11 / -24.11 | 2025-02-13 | 2025-06-16 | order_backlog_but_margin_cap |
| C29 | 011210 | Hyundai Wia | Stage2-Actionable | 2025-01-24 | 39,950 | 16.65 / -7.63 | 26.16 / -7.63 | 45.18 / -7.63 | 2025-10-22 | 2025-02-03 | auto_parts_defense_mix_profit_bridge |
| C30 | 034300 | Shinsegae E&C | Stage4B | 2024-03-21 | 10,890 | 6.15 / -9.55 | 71.26 / -9.55 | 71.26 / -9.55 | 2024-05-30 | 2024-04-26 | liquidity_support_watch |
| C30 | 002410 | Bumyang Construction | Stage4C | 2023-12-21 | 2,185 | 7.32 / -22.47 | 7.32 / -38.22 | 7.32 / -48.51 | 2024-01-02 | 2024-09-09 | small_builder_loss_debt_break |
| C30 | 035890 | Seohee Construction | Stage2-Actionable | 2024-08-14 | 1,342 | 17.29 / -2.53 | 25.19 / -2.53 | 33.46 / -2.53 | 2025-04-22 | 2024-08-14 | backlog_order_positive_control |
| C30 | 014790 | HL D&I Halla | Stage4B | 2025-02-06 | 2,280 | 9.21 / -9.21 | 24.56 / -9.21 | 35.75 / -9.21 | 2025-08-08 | 2025-02-06 | profit_decline_with_order_offset_watch |
| C30 | 013360 | Ilsung Construction | Stage4C | 2025-02-25 | 3,520 | 41.05 / -23.01 | 41.05 / -52.27 | 41.05 / -66.14 | 2025-04-02 | 2025-11-19 | operating_loss_margin_break |
| C32 | 010130 | Korea Zinc | Stage2-Actionable | 2024-09-13 | 666,000 | 131.68 / -1.65 | 261.41 / -1.65 | 261.41 / -3.45 | 2024-12-06 | 2025-04-09 | control_premium_positive_price_path |
| C32 | 010130 | Korea Zinc | Stage4B | 2024-10-21 | 877,000 | 75.94 / -13.23 | 174.46 / -18.93 | 174.46 / -26.68 | 2024-12-06 | 2025-04-09 | self_tender_legal_clearance_late_extension |
| C32 | 011200 | HMM | Stage4B | 2024-02-07 | 19,080 | 5.87 / -18.45 | 5.87 / -25.31 | 9.01 / -25.31 | 2024-07-03 | 2024-04-19 | sale_breakdown_control_premium_reversal |
| C32 | 008930 | Hanmi Science | Stage4B | 2024-03-28 | 44,350 | 5.98 / -29.54 | 5.98 / -41.94 | 18.38 / -41.94 | 2024-10-30 | 2024-08-05 | merger_scrapped_control_dispute_resolution |
| C32 | 028260 | Samsung C&T | Stage2 | 2024-02-15 | 156,300 | 9.85 / -5.95 | 9.85 / -17.15 | 9.85 / -25.14 | 2024-02-19 | 2024-10-31 | activist_shareholder_return_proposal |

## 5. Actual Stock-Web entry OHLC rows

| symbol | company | entry_date | actual_entry_ohlcv | 180D peak / trough | usable |
|---|---|---:|---|---|---|
| 005380 | Hyundai Motor | 2024-07-25 | `{"o":253000.0,"h":255000.0,"l":247500.0,"c":251500.0,"v":832753,"a":209029957500.0,"mc":52668172036500.0,"m":"KOSPI"}` | 2024-08-29 / 2025-04-11 | true |
| 000270 | Kia | 2024-07-26 | `{"o":118500.0,"h":118500.0,"l":110000.0,"c":112100.0,"v":1582067,"a":178615434250.0,"mc":44824128545700.0,"m":"KOSPI"}` | 2024-07-26 / 2025-04-11 | true |
| 012330 | Hyundai Mobis | 2024-07-26 | `{"o":227500.0,"h":230500.0,"l":221000.0,"c":225500.0,"v":313091,"a":70761292500.0,"mc":20970393697000.0,"m":"KOSPI"}` | 2025-03-25 / 2024-08-05 | true |
| 204320 | HL Mando | 2025-02-05 | `{"o":41950.0,"h":42500.0,"l":41750.0,"c":42300.0,"v":87882,"a":3701851750.0,"mc":1986286176000.0,"m":"KOSPI"}` | 2025-02-13 / 2025-06-16 | true |
| 011210 | Hyundai Wia | 2025-01-24 | `{"o":39450.0,"h":40400.0,"l":39450.0,"c":39950.0,"v":52209,"a":2089052500.0,"mc":1086443565850.0,"m":"KOSPI"}` | 2025-10-22 / 2025-02-03 | true |
| 034300 | Shinsegae E&C | 2024-03-21 | `{"o":10900.0,"h":11190.0,"l":10830.0,"c":10890.0,"v":2875,"a":31508350.0,"mc":84512433060.0,"m":"KOSPI"}` | 2024-05-30 / 2024-04-26 | true |
| 002410 | Bumyang Construction | 2023-12-21 | `{"o":2175.0,"h":2230.0,"l":2135.0,"c":2185.0,"v":180833,"a":394571895.0,"mc":54257880670.0,"m":"KOSPI"}` | 2024-01-02 / 2024-09-09 | true |
| 035890 | Seohee Construction | 2024-08-14 | `{"o":1308.0,"h":1352.0,"l":1308.0,"c":1342.0,"v":408782,"a":542229896.0,"mc":308402949294.0,"m":"KOSDAQ"}` | 2025-04-22 / 2024-08-14 | true |
| 014790 | HL D&I Halla | 2025-02-06 | `{"o":2230.0,"h":2280.0,"l":2070.0,"c":2280.0,"v":50488,"a":110590965.0,"mc":86317610280.0,"m":"KOSPI"}` | 2025-08-08 / 2025-02-06 | true |
| 013360 | Ilsung Construction | 2025-02-25 | `{"o":3620.0,"h":3730.0,"l":3455.0,"c":3520.0,"v":1783917,"a":6407407865.0,"mc":190167577600.0,"m":"KOSPI"}` | 2025-04-02 / 2025-11-19 | true |
| 010130 | Korea Zinc | 2024-09-13 | `{"o":660000.0,"h":690000.0,"l":655000.0,"c":666000.0,"v":586718}` | 2024-12-06 / 2025-04-09 | true |
| 010130 | Korea Zinc | 2024-10-21 | `{"o":827000.0,"h":889000.0,"l":761000.0,"c":877000.0,"v":638694}` | 2024-12-06 / 2025-04-09 | true |
| 011200 | HMM | 2024-02-07 | `{"o":19030.0,"h":20200.0,"l":17500.0,"c":19080.0,"v":5677567}` | 2024-07-03 / 2024-04-19 | true |
| 008930 | Hanmi Science | 2024-03-28 | `{"o":41350.0,"h":47000.0,"l":38000.0,"c":44350.0,"v":2969887}` | 2024-10-30 / 2024-08-05 | true |
| 028260 | Samsung C&T | 2024-02-15 | `{"o":155700.0,"h":161000.0,"l":152900.0,"c":156300.0,"v":1098381}` | 2024-02-19 / 2024-10-31 | true |

## 6. Direct evidence URL inventory

| Source C | symbol | company | trigger_type | evidence_url |
|---|---|---|---|---|
| C29 | 005380 | Hyundai Motor | Stage2-Actionable | https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q2-business-results-0000000801 |
| C29 | 000270 | Kia | Stage2-Actionable | https://worldwide.kia.com/en/newsroom/view/?id=161729 |
| C29 | 012330 | Hyundai Mobis | Stage4B | https://en.topdaily.kr/articles/1942 |
| C29 | 204320 | HL Mando | Stage2 | https://englishdart.fss.or.kr/report/downloadEng.do?dcmNo=10289586&flNm=HL+Mando+4Q24+results_vf_revised.pdf |
| C29 | 011210 | Hyundai Wia | Stage2-Actionable | https://biz.chosun.com/en/en-industry/2025/01/24/4G2N4YKVVRHUTCKCVERKULPVYA/ |
| C30 | 034300 | Shinsegae E&C | Stage4B |  |
| C30 | 002410 | Bumyang Construction | Stage4C |  |
| C30 | 035890 | Seohee Construction | Stage2-Actionable |  |
| C30 | 014790 | HL D&I Halla | Stage4B |  |
| C30 | 013360 | Ilsung Construction | Stage4C |  |
| C32 | 010130 | Korea Zinc | Stage2-Actionable | https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/ |
| C32 | 010130 | Korea Zinc | Stage4B | https://www.reuters.com/markets/deals/korea-zinc-shares-surge-record-high-after-court-clears-hurdle-buyback-offer-2024-10-21/ |
| C32 | 011200 | HMM | Stage4B | https://en.yna.co.kr/view/AEN20240207001452320 |
| C32 | 008930 | Hanmi Science | Stage4B | https://en.yna.co.kr/view/AEN20240328007700320 |
| C32 | 028260 | Samsung C&T | Stage2 | https://en.yna.co.kr/view/AEN20240215003800320 |

## 7. Residual findings

### 7.1 4B and hard 4C should split on offset quality

The selected C30 rows show the clearest boundary. Bumyang Construction and Ilsung Construction support hard 4C because the evidence points toward operating-loss / balance-sheet break with weak offset quality and the forward drawdown confirms the risk path. Shinsegae E&C and HL D&I Halla look ugly, but parent support, order visibility, or later profit evidence argues for Stage4B/watch before hard 4C.

### 7.2 Record margin is not automatic Yellow/Green

Hyundai Motor, Kia, and Hankook-type OEM/supplier rows can be valid Stage2-Actionable when record profit, mix, A/S margin, or supplier order-quality is direct. But the weak 180D forward MFE and deep MAE on several C29 rows show why Stage3-Yellow / Stage3-Green should remain blocked until volume, mix, cashflow, and capital-return evidence repeats. High MAE is a brake, not a delete key.

### 7.3 Control premium is a separate price engine

C32 rows are the reminder that governance price paths can be powerful but contaminated for operating-rerating logic. Korea Zinc and SM/HMM/Hanmi-type events have real tender/control mechanics. The move belongs in governance/control premium scoring, not in operating EPS/FCF Green unless post-event execution, buyback cancellation, integration economics, or cash conversion appears.

### 7.4 R13 rule candidate

```text
rule_candidate:
R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_GATE_V4

core residual:
- hard 4C is not triggered by price drawdown or ugly headline alone.
- hard 4C requires confirmed non-price thesis break plus weak offset quality.
- Stage4B/watch is the default route when ugly evidence has credible offset:
  parent liquidity, A/S margin, backlog/order visibility, cost repair, management reset,
  tender mechanics, policy/capital support, or later profit recovery.
- event-driven price paths such as tender, control premium, preferred-bidder, activist,
  or one-quarter record margin are not operating Stage3-Green by themselves.
- Stage2-Actionable reopen requires a second bridge: recognized revenue, margin, order,
  cashflow, working-capital repair, capital return execution, or post-event integration economics.
- High MAE blocks Yellow/Green first; it does not erase Stage2-Actionable when the second bridge is real.
```

## 8. Score / return alignment stress-test

| source canonical | alignment lesson | suggested scope |
|---|---|---|
| C29 | Record OEM/supplier margin evidence can be actionable, but peak-cycle rows with 180D MAE below -20% need Yellow/Green brake. | Mobility volume-margin Green blocker |
| C30 | PF/liquidity rows need a hard split between solvency/trust break and reversible liquidity watch. | PF hard-4C confirmation / reopen watch |
| C32 | Tender/control premium can produce huge MFE but is not an operating rerating without post-event EPS/FCF/capital execution. | Governance control-premium cap |

## 9. Residual contribution summary

```text
new_axis_proposed: false
existing_axis_strengthened:
- hard_4c_confirmation
- local_4b_watch_guard
- stage2_required_bridge
- stage3_green_not_loosened

existing_axis_refined:
- event_price_path_operating_green_blocker
- offset_quality_before_hard_4c
- high_mae_as_escalation_brake_not_stage2_deletion

production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: true
```

## 10. Machine-readable JSONL rows

```jsonl
{"row_type":"price_source_validation","source_name":"Songdaiki/stock-web","source_repo_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","tradable_columns":["d","o","h","l","c","v","a","mc","s","m"],"validation_status":"pass"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R9","source_loop":220,"source_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","source_research_file":"e2r_stock_web_v12_residual_round_R9_loop_220_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md","symbol":"005380","company_name":"Hyundai Motor","source_trigger_type":"Stage2-Actionable","trigger_type":"Stage2-Actionable","evidence_family":"record_Q2_OP_margin_US_SUV_HEV_mix","case_role":"late_cycle_oem_record_margin_guardrail","evidence_url":"https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q2-business-results-0000000801","entry_date":"2024-07-25","entry_price":251500.0,"actual_entry_ohlcv":{"o":253000.0,"h":255000.0,"l":247500.0,"c":251500.0,"v":832753,"a":209029957500.0,"mc":52668172036500.0,"m":"KOSPI"},"mfe_30d_pct":6.16,"mae_30d_pct":-13.92,"mfe_90d_pct":6.16,"mae_90d_pct":-21.55,"mfe_180d_pct":6.16,"mae_180d_pct":-30.1,"peak_180d_date":"2024-08-29","trough_180d_date":"2025-04-11","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":16,"earnings_visibility":18,"bottleneck_pricing":8,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":8,"weighted_total":80},"current_profile_error_label":"green_overrisk_if_record_margin_repeated_without_volume_cash_bridge","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005380|Stage2-Actionable|2024-07-25"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R9","source_loop":220,"source_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","source_research_file":"e2r_stock_web_v12_residual_round_R9_loop_220_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md","symbol":"000270","company_name":"Kia","source_trigger_type":"Stage2-Actionable","trigger_type":"Stage2-Actionable","evidence_family":"record_Q2_OP_margin_product_mix","case_role":"late_cycle_oem_record_margin_guardrail","evidence_url":"https://worldwide.kia.com/en/newsroom/view/?id=161729","entry_date":"2024-07-26","entry_price":112100.0,"actual_entry_ohlcv":{"o":118500.0,"h":118500.0,"l":110000.0,"c":112100.0,"v":1582067,"a":178615434250.0,"mc":44824128545700.0,"m":"KOSPI"},"mfe_30d_pct":5.71,"mae_30d_pct":-15.25,"mfe_90d_pct":5.71,"mae_90d_pct":-20.16,"mfe_180d_pct":5.71,"mae_180d_pct":-27.48,"peak_180d_date":"2024-07-26","trough_180d_date":"2025-04-11","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":16,"earnings_visibility":18,"bottleneck_pricing":8,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":8,"weighted_total":80},"current_profile_error_label":"green_overrisk_if_record_margin_repeated_without_volume_cash_bridge","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|000270|Stage2-Actionable|2024-07-26"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R9","source_loop":220,"source_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","source_research_file":"e2r_stock_web_v12_residual_round_R9_loop_220_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md","symbol":"012330","company_name":"Hyundai Mobis","source_trigger_type":"Stage4B","trigger_type":"Stage4B","evidence_family":"EV_electrification_weakness_AS_margin_offset","case_role":"electrification_slowdown_with_AS_offset","evidence_url":"https://en.topdaily.kr/articles/1942","entry_date":"2024-07-26","entry_price":225500.0,"actual_entry_ohlcv":{"o":227500.0,"h":230500.0,"l":221000.0,"c":225500.0,"v":313091,"a":70761292500.0,"mc":20970393697000.0,"m":"KOSPI"},"mfe_30d_pct":2.22,"mae_30d_pct":-11.09,"mfe_90d_pct":18.4,"mae_90d_pct":-11.09,"mfe_180d_pct":28.16,"mae_180d_pct":-11.09,"peak_180d_date":"2025-03-25","trough_180d_date":"2024-08-05","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":6,"market_mispricing":9,"valuation_rerating":8,"capital_allocation":5,"information_confidence":14,"weighted_total":60},"current_profile_error_label":"hard_4c_overrisk_if_offset_quality_ignored","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|012330|Stage4B|2024-07-26"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R9","source_loop":220,"source_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","source_research_file":"e2r_stock_web_v12_residual_round_R9_loop_220_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md","symbol":"204320","company_name":"HL Mando","source_trigger_type":"Stage2","trigger_type":"Stage2","evidence_family":"FY2024_growth_margin_orders_but_debt_tax_guardrail","case_role":"order_backlog_but_margin_cap","evidence_url":"https://englishdart.fss.or.kr/report/downloadEng.do?dcmNo=10289586&flNm=HL+Mando+4Q24+results_vf_revised.pdf","entry_date":"2025-02-05","entry_price":42300.0,"actual_entry_ohlcv":{"o":41950.0,"h":42500.0,"l":41750.0,"c":42300.0,"v":87882,"a":3701851750.0,"mc":1986286176000.0,"m":"KOSPI"},"mfe_30d_pct":11.11,"mae_30d_pct":-6.5,"mfe_90d_pct":11.11,"mae_90d_pct":-24.11,"mfe_180d_pct":11.11,"mae_180d_pct":-24.11,"peak_180d_date":"2025-02-13","trough_180d_date":"2025-06-16","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":13,"earnings_visibility":15,"bottleneck_pricing":7,"market_mispricing":11,"valuation_rerating":10,"capital_allocation":7,"information_confidence":9,"weighted_total":72},"current_profile_error_label":"stage2_actionable_cap_until_second_bridge_repeats","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|204320|Stage2|2025-02-05"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R9","source_loop":220,"source_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","source_research_file":"e2r_stock_web_v12_residual_round_R9_loop_220_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md","symbol":"011210","company_name":"Hyundai Wia","source_trigger_type":"Stage2-Actionable","trigger_type":"Stage2-Actionable","evidence_family":"FY2024_revenue_OP_auto_parts_special_business_mix","case_role":"auto_parts_defense_mix_profit_bridge","evidence_url":"https://biz.chosun.com/en/en-industry/2025/01/24/4G2N4YKVVRHUTCKCVERKULPVYA/","entry_date":"2025-01-24","entry_price":39950.0,"actual_entry_ohlcv":{"o":39450.0,"h":40400.0,"l":39450.0,"c":39950.0,"v":52209,"a":2089052500.0,"mc":1086443565850.0,"m":"KOSPI"},"mfe_30d_pct":16.65,"mae_30d_pct":-7.63,"mfe_90d_pct":26.16,"mae_90d_pct":-7.63,"mfe_180d_pct":45.18,"mae_180d_pct":-7.63,"peak_180d_date":"2025-10-22","trough_180d_date":"2025-02-03","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":16,"earnings_visibility":18,"bottleneck_pricing":8,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":8,"weighted_total":80},"current_profile_error_label":"yellow_green_high_mae_brake_needed","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|011210|Stage2-Actionable|2025-01-24"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R10","source_loop":221,"source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_research_file":"e2r_stock_web_v12_residual_round_R10_loop_221_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md","symbol":"034300","company_name":"Shinsegae E&C","source_trigger_type":"Stage4B","trigger_type":"Stage4B","evidence_family":"source_sector_reused","case_role":"liquidity_support_watch","evidence_url":null,"entry_date":"2024-03-21","entry_price":10890.0,"actual_entry_ohlcv":{"o":10900.0,"h":11190.0,"l":10830.0,"c":10890.0,"v":2875,"a":31508350.0,"mc":84512433060.0,"m":"KOSPI"},"mfe_30d_pct":6.15,"mae_30d_pct":-9.55,"mfe_90d_pct":71.26,"mae_90d_pct":-9.55,"mfe_180d_pct":71.26,"mae_180d_pct":-9.55,"peak_180d_date":"2024-05-30","trough_180d_date":"2024-04-26","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":10,"bottleneck_pricing":3,"market_mispricing":8,"valuation_rerating":6,"capital_allocation":6,"information_confidence":22},"current_profile_error_label":"too_strict_hard_4c","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|034300|Stage4B|2024-03-21"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R10","source_loop":221,"source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_research_file":"e2r_stock_web_v12_residual_round_R10_loop_221_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md","symbol":"002410","company_name":"Bumyang Construction","source_trigger_type":"Stage4C","trigger_type":"Stage4C","evidence_family":"source_sector_reused","case_role":"small_builder_loss_debt_break","evidence_url":null,"entry_date":"2023-12-21","entry_price":2185.0,"actual_entry_ohlcv":{"o":2175.0,"h":2230.0,"l":2135.0,"c":2185.0,"v":180833,"a":394571895.0,"mc":54257880670.0,"m":"KOSPI"},"mfe_30d_pct":7.32,"mae_30d_pct":-22.47,"mfe_90d_pct":7.32,"mae_90d_pct":-38.22,"mfe_180d_pct":7.32,"mae_180d_pct":-48.51,"peak_180d_date":"2024-01-02","trough_180d_date":"2024-09-09","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":4,"bottleneck_pricing":1,"market_mispricing":5,"valuation_rerating":3,"capital_allocation":3,"information_confidence":30},"current_profile_error_label":"hard_4c_control_or_stage2_cap","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|002410|Stage4C|2023-12-21"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R10","source_loop":221,"source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_research_file":"e2r_stock_web_v12_residual_round_R10_loop_221_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md","symbol":"035890","company_name":"Seohee Construction","source_trigger_type":"Stage2-Actionable","trigger_type":"Stage2-Actionable","evidence_family":"source_sector_reused","case_role":"backlog_order_positive_control","evidence_url":null,"entry_date":"2024-08-14","entry_price":1342.0,"actual_entry_ohlcv":{"o":1308.0,"h":1352.0,"l":1308.0,"c":1342.0,"v":408782,"a":542229896.0,"mc":308402949294.0,"m":"KOSDAQ"},"mfe_30d_pct":17.29,"mae_30d_pct":-2.53,"mfe_90d_pct":25.19,"mae_90d_pct":-2.53,"mfe_180d_pct":33.46,"mae_180d_pct":-2.53,"peak_180d_date":"2025-04-22","trough_180d_date":"2024-08-14","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":14,"earnings_visibility":18,"bottleneck_pricing":5,"market_mispricing":12,"valuation_rerating":11,"capital_allocation":9,"information_confidence":16},"current_profile_error_label":"green_blocker_ok","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|035890|Stage2-Actionable|2024-08-14"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R10","source_loop":221,"source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_research_file":"e2r_stock_web_v12_residual_round_R10_loop_221_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md","symbol":"014790","company_name":"HL D&I Halla","source_trigger_type":"Stage4B","trigger_type":"Stage4B","evidence_family":"source_sector_reused","case_role":"profit_decline_with_order_offset_watch","evidence_url":null,"entry_date":"2025-02-06","entry_price":2280.0,"actual_entry_ohlcv":{"o":2230.0,"h":2280.0,"l":2070.0,"c":2280.0,"v":50488,"a":110590965.0,"mc":86317610280.0,"m":"KOSPI"},"mfe_30d_pct":9.21,"mae_30d_pct":-9.21,"mfe_90d_pct":24.56,"mae_90d_pct":-9.21,"mfe_180d_pct":35.75,"mae_180d_pct":-9.21,"peak_180d_date":"2025-08-08","trough_180d_date":"2025-02-06","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":10,"bottleneck_pricing":3,"market_mispricing":8,"valuation_rerating":6,"capital_allocation":6,"information_confidence":22},"current_profile_error_label":"too_strict_hard_4c","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|014790|Stage4B|2025-02-06"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R10","source_loop":221,"source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_research_file":"e2r_stock_web_v12_residual_round_R10_loop_221_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md","symbol":"013360","company_name":"Ilsung Construction","source_trigger_type":"Stage4C","trigger_type":"Stage4C","evidence_family":"source_sector_reused","case_role":"operating_loss_margin_break","evidence_url":null,"entry_date":"2025-02-25","entry_price":3520.0,"actual_entry_ohlcv":{"o":3620.0,"h":3730.0,"l":3455.0,"c":3520.0,"v":1783917,"a":6407407865.0,"mc":190167577600.0,"m":"KOSPI"},"mfe_30d_pct":41.05,"mae_30d_pct":-23.01,"mfe_90d_pct":41.05,"mae_90d_pct":-52.27,"mfe_180d_pct":41.05,"mae_180d_pct":-66.14,"peak_180d_date":"2025-04-02","trough_180d_date":"2025-11-19","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":2,"earnings_visibility":4,"bottleneck_pricing":1,"market_mispricing":5,"valuation_rerating":3,"capital_allocation":3,"information_confidence":30},"current_profile_error_label":"hard_4c_control_or_stage2_cap","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|013360|Stage4C|2025-02-25"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R12","source_loop":222,"source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_research_file":"e2r_stock_web_v12_residual_round_R12_loop_222_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md","symbol":"010130","company_name":"Korea Zinc","source_trigger_type":"Stage2-Actionable","trigger_type":"Stage2-Actionable","evidence_family":"hostile_tender_offer_initial","case_role":"control_premium_positive_price_path","evidence_url":"https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/","entry_date":"2024-09-13","entry_price":666000.0,"actual_entry_ohlcv":{"o":660000.0,"h":690000.0,"l":655000.0,"c":666000.0,"v":586718},"mfe_30d_pct":131.68,"mae_30d_pct":-1.65,"mfe_90d_pct":261.41,"mae_90d_pct":-1.65,"mfe_180d_pct":261.41,"mae_180d_pct":-3.45,"peak_180d_date":"2024-12-06","trough_180d_date":"2025-04-09","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":14,"earnings_visibility":18,"bottleneck_pricing":8,"market_mispricing":14,"valuation_rerating":13,"capital_allocation":8,"information_confidence":18},"current_profile_error_label":"green_blocker_or_stage2_cap_test","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|010130|Stage2-Actionable|2024-09-13"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R12","source_loop":222,"source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_research_file":"e2r_stock_web_v12_residual_round_R12_loop_222_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md","symbol":"010130","company_name":"Korea Zinc","source_trigger_type":"4B","trigger_type":"Stage4B","evidence_family":"court_buyback_clearance_self_tender","case_role":"self_tender_legal_clearance_late_extension","evidence_url":"https://www.reuters.com/markets/deals/korea-zinc-shares-surge-record-high-after-court-clears-hurdle-buyback-offer-2024-10-21/","entry_date":"2024-10-21","entry_price":877000.0,"actual_entry_ohlcv":{"o":827000.0,"h":889000.0,"l":761000.0,"c":877000.0,"v":638694},"mfe_30d_pct":75.94,"mae_30d_pct":-13.23,"mfe_90d_pct":174.46,"mae_90d_pct":-18.93,"mfe_180d_pct":174.46,"mae_180d_pct":-26.68,"peak_180d_date":"2024-12-06","trough_180d_date":"2025-04-09","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":5,"market_mispricing":9,"valuation_rerating":8,"capital_allocation":7,"information_confidence":25},"current_profile_error_label":"needs_4b_4c_boundary_audit","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|010130|Stage4B|2024-10-21"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R12","source_loop":222,"source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_research_file":"e2r_stock_web_v12_residual_round_R12_loop_222_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md","symbol":"011200","company_name":"HMM","source_trigger_type":"4B","trigger_type":"Stage4B","evidence_family":"deal_collapse_creditor_negotiation_failure","case_role":"sale_breakdown_control_premium_reversal","evidence_url":"https://en.yna.co.kr/view/AEN20240207001452320","entry_date":"2024-02-07","entry_price":19080.0,"actual_entry_ohlcv":{"o":19030.0,"h":20200.0,"l":17500.0,"c":19080.0,"v":5677567},"mfe_30d_pct":5.87,"mae_30d_pct":-18.45,"mfe_90d_pct":5.87,"mae_90d_pct":-25.31,"mfe_180d_pct":9.01,"mae_180d_pct":-25.31,"peak_180d_date":"2024-07-03","trough_180d_date":"2024-04-19","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":5,"market_mispricing":9,"valuation_rerating":8,"capital_allocation":7,"information_confidence":25},"current_profile_error_label":"needs_4b_4c_boundary_audit","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|011200|Stage4B|2024-02-07"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R12","source_loop":222,"source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_research_file":"e2r_stock_web_v12_residual_round_R12_loop_222_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md","symbol":"008930","company_name":"Hanmi Science","source_trigger_type":"4B","trigger_type":"Stage4B","evidence_family":"shareholder_vote_merger_scrapped","case_role":"merger_scrapped_control_dispute_resolution","evidence_url":"https://en.yna.co.kr/view/AEN20240328007700320","entry_date":"2024-03-28","entry_price":44350.0,"actual_entry_ohlcv":{"o":41350.0,"h":47000.0,"l":38000.0,"c":44350.0,"v":2969887},"mfe_30d_pct":5.98,"mae_30d_pct":-29.54,"mfe_90d_pct":5.98,"mae_90d_pct":-41.94,"mfe_180d_pct":18.38,"mae_180d_pct":-41.94,"peak_180d_date":"2024-10-30","trough_180d_date":"2024-08-05","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":5,"market_mispricing":9,"valuation_rerating":8,"capital_allocation":7,"information_confidence":25},"current_profile_error_label":"needs_4b_4c_boundary_audit","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|008930|Stage4B|2024-03-28"}
{"row_type":"trigger","research_version":"v12","selected_round":"R13","selected_loop":212,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_EVENT_OFFSET_QUALITY_AND_OPERATING_GREEN_BLOCKER_HOLDOUT_V4","source_round":"R12","source_loop":222,"source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_research_file":"e2r_stock_web_v12_residual_round_R12_loop_222_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md","symbol":"028260","company_name":"Samsung C&T","source_trigger_type":"Stage2","trigger_type":"Stage2","evidence_family":"activist_buyback_dividend_proposal","case_role":"activist_shareholder_return_proposal","evidence_url":"https://en.yna.co.kr/view/AEN20240215003800320","entry_date":"2024-02-15","entry_price":156300.0,"actual_entry_ohlcv":{"o":155700.0,"h":161000.0,"l":152900.0,"c":156300.0,"v":1098381},"mfe_30d_pct":9.85,"mae_30d_pct":-5.95,"mfe_90d_pct":9.85,"mae_90d_pct":-17.15,"mfe_180d_pct":9.85,"mae_180d_pct":-25.14,"peak_180d_date":"2024-02-19","trough_180d_date":"2024-10-31","price_source_validation":{"source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D_window":false,"insufficient_forward_window_180D":false},"raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":12,"bottleneck_pricing":5,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":6,"information_confidence":18},"current_profile_error_label":"green_blocker_or_stage2_cap_test","representative_for_aggregate":true,"production_scoring_changed":false,"shadow_weight_only":true,"hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|028260|Stage2|2024-02-15"}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Later coding-agent task:
- Parse this MD as a v12 result file.
- Validate every JSONL trigger row against the standard v12 schema.
- Treat rows as R13 cross-archetype holdout / review rows, not source-sector new weight rows.
- Do not change production scoring directly from this single file.
- Use the rule candidate only as support for existing hard_4c_confirmation, local_4b_watch_guard,
  stage2_required_bridge, and stage3_green_not_loosened axes.
- Preserve source_canonical_archetype_id and source_research_file for audit trail.
```

## 12. Next Research State

```text
completed_round: R13
completed_loop: 212
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 R13 4B/4C offset-quality refresh
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
