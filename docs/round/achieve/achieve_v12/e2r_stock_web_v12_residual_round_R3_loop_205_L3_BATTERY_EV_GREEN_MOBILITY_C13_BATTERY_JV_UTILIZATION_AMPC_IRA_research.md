# E2R Stock-Web v12 Residual Research — R3 / L3_BATTERY_EV_GREEN_MOBILITY / C13_BATTERY_JV_UTILIZATION_AMPC_IRA

```text
created_at_kst: 2026-06-16
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 205
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / C13 AMPC-IRA-JV utilization quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Coverage-index selection / novelty check

C13 is not under-covered by raw row count, but the current No-Repeat snapshot still marks it as a Priority 1 balance-reinforcement target: AMPC/IRA persistence and JV utilization failure cases need better direct rows. This run therefore avoids repeating previous C13 rows and focuses on ex-subsidy margin, utilization collapse, customer pull, and offset-quality splits.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count: 8
new_independent_trigger_count: 8
unique_symbol_count: 8
same_archetype_new_trigger_family_count: 5
source_proxy_only_count: 2
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
calibration_usable_trigger_count: 8
ready_for_batch_ingest: true
```

## 2. Stock-Web price atlas validation

The run uses `atlas/ohlcv_tradable_by_symbol_year/<pre>/<ticker>/<year>.csv` only. Entry is the evidence date if it is tradable, otherwise the next tradable date. MFE/MAE are calculated from entry close against the maximum high / minimum low through the next 30, 90, and 180 tradable rows. All usable rows have a full 180D window before the stock-web manifest max date of `2026-02-20`.

```text
manifest.max_date: 2026-02-20
tradable_schema: d,o,h,l,c,v,a,mc,s,m
price_adjustment_status: raw_unadjusted_marcap
corporate_action_policy: block if candidate date overlaps entry_date~D+180
profile_check_summary: no modern corporate-action candidate overlaps these 180D windows; 006400/011790 legacy events are far outside selected windows
```

## 3. Case set

| # | Symbol | Name | Trigger | Entry date | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Evidence role |
|---:|---|---|---|---|---:|---:|---:|---:|---|
| 1 | `373220` | LG Energy Solution | Stage4B | 2024-10-28 | 416,500 | 4.56/-10.92 | 4.56/-21.37 | 4.56/-36.13 | AMPC-supported OP / ex-credit loss 4B |
| 2 | `006400` | Samsung SDI | Stage4B | 2024-07-30 | 330,500 | 14.98/-10.89 | 19.06/-28.74 | 19.06/-48.56 | EV weakness with ESS offset 4B |
| 3 | `361610` | SK IE Technology | Stage4C | 2024-04-30 | 59,100 | 5.25/-27.75 | 5.25/-48.73 | 5.25/-63.03 | utilization collapse hard 4C |
| 4 | `011790` | SKC | Stage4B | 2024-05-08 | 119,200 | 67.79/-15.02 | 67.79/-15.02 | 67.79/-24.24 | loss segment with enterprise optionality 4B |
| 5 | `020150` | LOTTE Energy Materials | Stage4C | 2024-11-01 | 36,300 | 3.44/-42.42 | 3.44/-44.21 | 3.44/-46.39 | copper-foil loss / weak offset hard 4C |
| 6 | `278280` | Chunbo | Stage2 | 2024-05-31 | 73,500 | 11.84/-3.40 | 11.84/-33.33 | 11.84/-53.27 | long-lead additive route capped Stage2 |
| 7 | `247540` | EcoPro BM | Stage4C | 2024-07-30 | 187,500 | 2.35/-20.69 | 3.73/-35.79 | 3.73/-53.60 | inventory/downstream break 4C |
| 8 | `066970` | L&F | Stage2-Actionable | 2024-11-04 | 112,000 | 12.77/-17.68 | 12.77/-37.41 | 12.77/-58.04 | direct customer bridge, high-MAE cap |

## 4. Entry OHLCV and forward path details

| Symbol | Entry OHLCV | Peak 180D | Trough 180D | 180D end | Calibration usability |
|---|---|---|---|---|---|
| `373220` | o=403,000, h=417,500, l=403,000, c=416,500, v=360,352 | 2024-11-11 | 2025-05-23 | 2025-07-23 | usable |
| `006400` | o=333,000, h=344,500, l=330,500, c=330,500, v=423,808 | 2024-09-30 | 2025-04-09 | 2025-04-28 | usable |
| `361610` | o=62,100, h=62,200, l=58,600, c=59,100, v=661,182 | 2024-04-30 | 2025-01-02 | 2025-01-24 | usable |
| `011790` | o=115,800, h=119,400, l=115,000, c=119,200, v=312,097 | 2024-06-18 | 2024-12-09 | 2025-02-05 | usable |
| `020150` | o=37,300, h=37,550, l=35,600, c=36,300, v=141,288 | 2024-11-01 | 2025-05-22 | 2025-07-29 | usable |
| `278280` | o=71,800, h=74,800, l=71,800, c=73,500, v=31,353 | 2024-06-12 | 2025-02-03 | 2025-02-27 | usable |
| `247540` | o=177,100, h=190,000, l=176,100, c=187,500, v=927,485 | 2024-10-10 | 2025-04-03 | 2025-04-28 | usable |
| `066970` | o=114,800, h=119,000, l=108,300, c=112,000, v=750,031 | 2024-11-12 | 2025-05-26 | 2025-07-30 | usable |

## 5. Trigger-level evidence notes

### 373220 LG Energy Solution — Stage4B / 2024-10-28

- Evidence: 3Q24 OP included KRW466bn IRA credit; ex-IRA loss KRW17.7bn; EV demand outlook/capex discipline.
- Interpretation: LG Energy Solution 3Q24 is a clean AMPC quality split. Reported OP was positive, but IRA tax credit exceeded operating profit, leaving ex-credit loss. This should be Stage4B/watch, not Green, because the economics were not yet self-powered.
- Evidence URL: https://news.lgensol.com/company-news/press-releases/3343/

### 006400 Samsung SDI — Stage4B / 2024-07-30

- Evidence: 2Q24 revenue down 24% YoY, EV utilization/sales declined, but ESS rebound and future projects offset.
- Interpretation: Samsung SDI 2Q24 shows EV weakness and revenue decline, but ESS profitability and future-project commentary create an offset. The right route is Stage4B/watch, not sticky hard 4C and not positive escalation.
- Evidence URL: https://www.samsungsdi.com/sdi-now/sdi-news/3862.html

### 361610 SK IE Technology — Stage4C / 2024-04-30

- Evidence: 1Q24 revenue -73% QoQ, operating loss KRW67.4bn, utilization/shipment collapse tied to SK On demand.
- Interpretation: SK IE Technology 1Q24 is a direct utilization-collapse row. Revenue fell sharply QoQ, operating loss widened, and separator shipment/utilization tied to customer demand broke. This is the clean hard-4C control row in the batch.
- Evidence URL: https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220

### 011790 SKC — Stage4B / 2024-05-08

- Evidence: SK Nexilis copper foil remained biggest loss, but SKC multi-segment / glass substrate / rebound optionality made hard 4C sticky risk.
- Interpretation: SKC/SK Nexilis remains a copper-foil loss watch case, but enterprise-level optionality and other segment narratives make hard 4C too sticky if no issuer-level total-thesis collapse is confirmed.
- Evidence URL: https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2322478

### 020150 LOTTE Energy Materials — Stage4C / 2024-11-01

- Evidence: 3Q24 operating loss KRW31.7bn after production/sales decline, FX and inventory valuation losses; North America growth only medium-term offset.
- Interpretation: LOTTE Energy Materials 3Q24 has operating loss, production/sales decline, FX and inventory valuation pressure. North America growth is an offset, but too medium-term to rescue the trigger from hard 4C / severe watch.
- Evidence URL: https://lotteenergymaterials.com/en/pr/promotion_detail.do?seq=108

### 278280 Chunbo — Stage2 / 2024-05-31

- Evidence: Potential North American OEM electrolyte-additive route via Saemangeum discussed, but no realized shipment/margin bridge.
- Interpretation: Chunbo has a possible North America-bound electrolyte-additive route, but the trigger is still more pipeline/profile than realized shipment or margin. It should be capped at Stage2 until conversion appears.
- Evidence URL: https://securities.miraeasset.com/bbs/download/2127818.pdf?attachmentId=2127818

### 247540 EcoPro BM — Stage4C / 2024-07-30

- Evidence: 2Q24/2024 battery-material weakness, inventory valuation burden and downstream slowdown; no utilization/ex-margin bridge.
- Interpretation: EcoPro BM 2Q24/2024 weakness remains an inventory/downstream demand break row. The path confirms that without utilization and ex-margin recovery, positive battery-material language should not reopen Actionable.
- Evidence URL: https://www.ecopro.co.kr/eng/ir

### 066970 L&F — Stage2-Actionable / 2024-11-04

- Evidence: High-nickel cathode supply route to Tesla/affiliates; direct customer bridge but severe forward MAE keeps Yellow/Green blocked.
- Interpretation: L&F has a direct high-nickel cathode customer bridge, preserving Stage2-Actionable. But the severe 90D/180D MAE means Yellow/Green must remain blocked until actual shipment/margin conversion is visible.
- Evidence URL: https://www.kedglobal.com/batteries/newsView/ked202411030003

## 6. Current calibrated-profile stress test

C13 current archetype weight vector in the No-Repeat coverage matrix is `20/18/14/12/10/10/16`. This run does not change production scoring. The purpose is to stress whether the profile still over-credits subsidy/JV/customer language before utilization, shipment, and ex-subsidy margin conversion are visible.

| Symbol | Trigger | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Sim total | Current-profile residual |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `373220` | Stage4B | 6 | 7 | 3 | 5 | 3 | 4 | 9 | 37 | Green must be blocked: reported OP is IRA-credit supported and ex-credit loss remains. |
| `006400` | Stage4B | 5 | 6 | 4 | 5 | 3 | 4 | 8 | 35 | Hard 4C sticky risk: ESS/project offset exists, but EV utilization weakness blocks positive escalation. |
| `361610` | Stage4C | 1 | 2 | 1 | 3 | 2 | 2 | 8 | 19 | Confirmed utilization/shipment collapse supports hard 4C. |
| `011790` | Stage4B | 3 | 4 | 3 | 7 | 5 | 4 | 6 | 32 | Loss segment is severe, but enterprise optionality makes sticky hard 4C unsafe. |
| `020150` | Stage4C | 2 | 3 | 2 | 3 | 2 | 3 | 8 | 23 | Operating loss plus weak near-term offset supports hard 4C. |
| `278280` | Stage2 | 3 | 3 | 4 | 5 | 3 | 3 | 6 | 27 | North America route is not enough for Actionable without realized shipment/margin. |
| `247540` | Stage4C | 2 | 3 | 2 | 3 | 2 | 3 | 7 | 22 | Inventory/downstream weakness with weak offset quality supports 4C/watch. |
| `066970` | Stage2-Actionable | 6 | 6 | 6 | 6 | 4 | 4 | 8 | 40 | Direct customer bridge preserves Actionable, but high MAE blocks Yellow/Green. |

## 7. Residual contribution summary

```text
rule_candidate: C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_GATE_V5
sector_rule_candidate: L3_BATTERY_EX_SUBSIDY_UTILIZATION_AND_OFFSET_QUALITY_GATE
loop_contribution_label: C13_AMPC_IRA_JV_quality_repair
new_axis_proposed: no_global_axis
existing_axis_strengthened: stage2_required_bridge, stage3_green_not_loosened, hard_4c_thesis_break_quality
existing_axis_weakened: none
production_scoring_changed: false
shadow_weight_only: true
```

Core residual rules:

1. AMPC / IRA / JV / North America / customer-diversification language alone does not create Stage2-Actionable or Yellow.
2. Stage2-Actionable requires at least one direct second bridge: eligible production volume, utilization rebound, customer pull/call-off, shipment conversion, ex-subsidy margin, or order/backlog-to-revenue conversion.
3. If tax credits materially prop up reported operating profit, Stage3-Green remains blocked until ex-credit economics or utilization recovery is visible.
4. Battery operating loss, inventory adjustment, or utilization break with explicit ESS/North-America/JV/new-model offset routes to Stage4B/watch before sticky hard 4C.
5. Hard 4C requires utilization/call-off/margin thesis break plus weak offset quality.
6. High MAE on a valid direct-bridge row blocks Yellow/Green first; it does not erase Stage2-Actionable.

## 8. Machine-readable JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","case_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA::373220::Stage4B::2024-10-28","symbol":"373220","name":"LG Energy Solution","trigger_type":"Stage4B","evidence_date":"2024-10-28","entry_date":"2024-10-28","entry_price":416500.0,"entry_ohlcv":{"o":403000.0,"h":417500.0,"l":403000.0,"c":416500.0,"v":360352.0,"a":148639841500.0,"mc":97461000000000.0,"s":234000000,"m":"KOSPI"},"mfe_30d_pct":4.56,"mae_30d_pct":-10.92,"peak_30d_date":"2024-11-11","trough_30d_date":"2024-11-15","end_30d_date":"2024-12-06","mfe_90d_pct":4.56,"mae_90d_pct":-21.37,"peak_90d_date":"2024-11-11","trough_90d_date":"2025-03-05","end_90d_date":"2025-03-12","mfe_180d_pct":4.56,"mae_180d_pct":-36.13,"peak_180d_date":"2024-11-11","trough_180d_date":"2025-05-23","end_180d_date":"2025-07-23","calibration_usable":true,"calibration_unusable_reason":null,"price_source_validation":{"source":"Songdaiki/stock-web","basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false},"evidence_summary":"3Q24 OP included KRW466bn IRA credit; ex-IRA loss KRW17.7bn; EV demand outlook/capex discipline.","evidence_url":"https://news.lgensol.com/company-news/press-releases/3343/","source_proxy_only":false,"evidence_url_pending":false,"score_simulation":{"eps_fcf_explosion":6,"earnings_visibility":7,"bottleneck_pricing":3,"market_mispricing":5,"valuation_rerating":3,"capital_allocation":4,"information_confidence":9,"total":37,"profile_error":"Green must be blocked: reported OP is IRA-credit supported and ex-credit loss remains."},"residual_label":"C13_AMPC_IRA_JV_direct_bridge_quality_repair"}
{"row_type":"trigger","schema_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","case_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA::006400::Stage4B::2024-07-30","symbol":"006400","name":"Samsung SDI","trigger_type":"Stage4B","evidence_date":"2024-07-30","entry_date":"2024-07-30","entry_price":330500.0,"entry_ohlcv":{"o":333000.0,"h":344500.0,"l":330500.0,"c":330500.0,"v":423808.0,"a":141982847000.0,"mc":22726677165000.0,"s":68764530,"m":"KOSPI"},"mfe_30d_pct":14.98,"mae_30d_pct":-10.89,"peak_30d_date":"2024-09-03","trough_30d_date":"2024-08-05","end_30d_date":"2024-09-10","mfe_90d_pct":19.06,"mae_90d_pct":-28.74,"peak_90d_date":"2024-09-30","trough_90d_date":"2024-11-15","end_90d_date":"2024-12-11","mfe_180d_pct":19.06,"mae_180d_pct":-48.56,"peak_180d_date":"2024-09-30","trough_180d_date":"2025-04-09","end_180d_date":"2025-04-28","calibration_usable":true,"calibration_unusable_reason":null,"price_source_validation":{"source":"Songdaiki/stock-web","basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false},"evidence_summary":"2Q24 revenue down 24% YoY, EV utilization/sales declined, but ESS rebound and future projects offset.","evidence_url":"https://www.samsungsdi.com/sdi-now/sdi-news/3862.html","source_proxy_only":false,"evidence_url_pending":false,"score_simulation":{"eps_fcf_explosion":5,"earnings_visibility":6,"bottleneck_pricing":4,"market_mispricing":5,"valuation_rerating":3,"capital_allocation":4,"information_confidence":8,"total":35,"profile_error":"Hard 4C sticky risk: ESS/project offset exists, but EV utilization weakness blocks positive escalation."},"residual_label":"C13_AMPC_IRA_JV_direct_bridge_quality_repair"}
{"row_type":"trigger","schema_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","case_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA::361610::Stage4C::2024-04-30","symbol":"361610","name":"SK IE Technology","trigger_type":"Stage4C","evidence_date":"2024-04-30","entry_date":"2024-04-30","entry_price":59100.0,"entry_ohlcv":{"o":62100.0,"h":62200.0,"l":58600.0,"c":59100.0,"v":661182.0,"a":39337486300.0,"mc":4213687687200.0,"s":71297592,"m":"KOSPI"},"mfe_30d_pct":5.25,"mae_30d_pct":-27.75,"peak_30d_date":"2024-04-30","trough_30d_date":"2024-06-04","end_30d_date":"2024-06-14","mfe_90d_pct":5.25,"mae_90d_pct":-48.73,"peak_90d_date":"2024-04-30","trough_90d_date":"2024-09-09","end_90d_date":"2024-09-09","mfe_180d_pct":5.25,"mae_180d_pct":-63.03,"peak_180d_date":"2024-04-30","trough_180d_date":"2025-01-02","end_180d_date":"2025-01-24","calibration_usable":true,"calibration_unusable_reason":null,"price_source_validation":{"source":"Songdaiki/stock-web","basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false},"evidence_summary":"1Q24 revenue -73% QoQ, operating loss KRW67.4bn, utilization/shipment collapse tied to SK On demand.","evidence_url":"https://securities.miraeasset.com/bbs/download/2126220.pdf?attachmentId=2126220","source_proxy_only":false,"evidence_url_pending":false,"score_simulation":{"eps_fcf_explosion":1,"earnings_visibility":2,"bottleneck_pricing":1,"market_mispricing":3,"valuation_rerating":2,"capital_allocation":2,"information_confidence":8,"total":19,"profile_error":"Confirmed utilization/shipment collapse supports hard 4C."},"residual_label":"C13_AMPC_IRA_JV_direct_bridge_quality_repair"}
{"row_type":"trigger","schema_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","case_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA::011790::Stage4B::2024-05-08","symbol":"011790","name":"SKC","trigger_type":"Stage4B","evidence_date":"2024-05-08","entry_date":"2024-05-08","entry_price":119200.0,"entry_ohlcv":{"o":115800.0,"h":119400.0,"l":115000.0,"c":119200.0,"v":312097.0,"a":36766004900.0,"mc":4513901121600.0,"s":37868298,"m":"KOSPI"},"mfe_30d_pct":67.79,"mae_30d_pct":-15.02,"peak_30d_date":"2024-06-18","trough_30d_date":"2024-05-17","end_30d_date":"2024-06-20","mfe_90d_pct":67.79,"mae_90d_pct":-15.02,"peak_90d_date":"2024-06-18","trough_90d_date":"2024-05-17","end_90d_date":"2024-09-13","mfe_180d_pct":67.79,"mae_180d_pct":-24.24,"peak_180d_date":"2024-06-18","trough_180d_date":"2024-12-09","end_180d_date":"2025-02-05","calibration_usable":true,"calibration_unusable_reason":null,"price_source_validation":{"source":"Songdaiki/stock-web","basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false},"evidence_summary":"SK Nexilis copper foil remained biggest loss, but SKC multi-segment / glass substrate / rebound optionality made hard 4C sticky risk.","evidence_url":"https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2322478","source_proxy_only":true,"evidence_url_pending":false,"score_simulation":{"eps_fcf_explosion":3,"earnings_visibility":4,"bottleneck_pricing":3,"market_mispricing":7,"valuation_rerating":5,"capital_allocation":4,"information_confidence":6,"total":32,"profile_error":"Loss segment is severe, but enterprise optionality makes sticky hard 4C unsafe."},"residual_label":"C13_AMPC_IRA_JV_direct_bridge_quality_repair"}
{"row_type":"trigger","schema_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","case_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA::020150::Stage4C::2024-11-01","symbol":"020150","name":"LOTTE Energy Materials","trigger_type":"Stage4C","evidence_date":"2024-11-01","entry_date":"2024-11-01","entry_price":36300.0,"entry_ohlcv":{"o":37300.0,"h":37550.0,"l":35600.0,"c":36300.0,"v":141288.0,"a":5150177000.0,"mc":1673823310500.0,"s":46110835,"m":"KOSPI"},"mfe_30d_pct":3.44,"mae_30d_pct":-42.42,"peak_30d_date":"2024-11-01","trough_30d_date":"2024-12-09","end_30d_date":"2024-12-12","mfe_90d_pct":3.44,"mae_90d_pct":-44.21,"peak_90d_date":"2024-11-01","trough_90d_date":"2025-02-03","end_90d_date":"2025-03-18","mfe_180d_pct":3.44,"mae_180d_pct":-46.39,"peak_180d_date":"2024-11-01","trough_180d_date":"2025-05-22","end_180d_date":"2025-07-29","calibration_usable":true,"calibration_unusable_reason":null,"price_source_validation":{"source":"Songdaiki/stock-web","basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false},"evidence_summary":"3Q24 operating loss KRW31.7bn after production/sales decline, FX and inventory valuation losses; North America growth only medium-term offset.","evidence_url":"https://lotteenergymaterials.com/en/pr/promotion_detail.do?seq=108","source_proxy_only":false,"evidence_url_pending":false,"score_simulation":{"eps_fcf_explosion":2,"earnings_visibility":3,"bottleneck_pricing":2,"market_mispricing":3,"valuation_rerating":2,"capital_allocation":3,"information_confidence":8,"total":23,"profile_error":"Operating loss plus weak near-term offset supports hard 4C."},"residual_label":"C13_AMPC_IRA_JV_direct_bridge_quality_repair"}
{"row_type":"trigger","schema_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","case_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA::278280::Stage2::2024-05-31","symbol":"278280","name":"Chunbo","trigger_type":"Stage2","evidence_date":"2024-05-31","entry_date":"2024-05-31","entry_price":73500.0,"entry_ohlcv":{"o":71800.0,"h":74800.0,"l":71800.0,"c":73500.0,"v":31353.0,"a":2302336800.0,"mc":735000000000.0,"s":10000000,"m":"KOSDAQ GLOBAL"},"mfe_30d_pct":11.84,"mae_30d_pct":-3.4,"peak_30d_date":"2024-06-12","trough_30d_date":"2024-06-25","end_30d_date":"2024-07-12","mfe_90d_pct":11.84,"mae_90d_pct":-33.33,"peak_90d_date":"2024-06-12","trough_90d_date":"2024-08-05","end_90d_date":"2024-10-15","mfe_180d_pct":11.84,"mae_180d_pct":-53.27,"peak_180d_date":"2024-06-12","trough_180d_date":"2025-02-03","end_180d_date":"2025-02-27","calibration_usable":true,"calibration_unusable_reason":null,"price_source_validation":{"source":"Songdaiki/stock-web","basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false},"evidence_summary":"Potential North American OEM electrolyte-additive route via Saemangeum discussed, but no realized shipment/margin bridge.","evidence_url":"https://securities.miraeasset.com/bbs/download/2127818.pdf?attachmentId=2127818","source_proxy_only":true,"evidence_url_pending":false,"score_simulation":{"eps_fcf_explosion":3,"earnings_visibility":3,"bottleneck_pricing":4,"market_mispricing":5,"valuation_rerating":3,"capital_allocation":3,"information_confidence":6,"total":27,"profile_error":"North America route is not enough for Actionable without realized shipment/margin."},"residual_label":"C13_AMPC_IRA_JV_direct_bridge_quality_repair"}
{"row_type":"trigger","schema_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","case_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA::247540::Stage4C::2024-07-30","symbol":"247540","name":"EcoPro BM","trigger_type":"Stage4C","evidence_date":"2024-07-30","entry_date":"2024-07-30","entry_price":187500.0,"entry_ohlcv":{"o":177100.0,"h":190000.0,"l":176100.0,"c":187500.0,"v":927485.0,"a":173052220500.0,"mc":18337752000000.0,"s":97801344,"m":"KOSDAQ GLOBAL"},"mfe_30d_pct":2.35,"mae_30d_pct":-20.69,"peak_30d_date":"2024-08-16","trough_30d_date":"2024-09-10","end_30d_date":"2024-09-10","mfe_90d_pct":3.73,"mae_90d_pct":-35.79,"peak_90d_date":"2024-10-10","trough_90d_date":"2024-11-15","end_90d_date":"2024-12-11","mfe_180d_pct":3.73,"mae_180d_pct":-53.6,"peak_180d_date":"2024-10-10","trough_180d_date":"2025-04-03","end_180d_date":"2025-04-28","calibration_usable":true,"calibration_unusable_reason":null,"price_source_validation":{"source":"Songdaiki/stock-web","basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false},"evidence_summary":"2Q24/2024 battery-material weakness, inventory valuation burden and downstream slowdown; no utilization/ex-margin bridge.","evidence_url":"https://www.ecopro.co.kr/eng/ir","source_proxy_only":false,"evidence_url_pending":false,"score_simulation":{"eps_fcf_explosion":2,"earnings_visibility":3,"bottleneck_pricing":2,"market_mispricing":3,"valuation_rerating":2,"capital_allocation":3,"information_confidence":7,"total":22,"profile_error":"Inventory/downstream weakness with weak offset quality supports 4C/watch."},"residual_label":"C13_AMPC_IRA_JV_direct_bridge_quality_repair"}
{"row_type":"trigger","schema_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R3_loop_205_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","case_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA::066970::Stage2-Actionable::2024-11-04","symbol":"066970","name":"L&F","trigger_type":"Stage2-Actionable","evidence_date":"2024-11-04","entry_date":"2024-11-04","entry_price":112000.0,"entry_ohlcv":{"o":114800.0,"h":119000.0,"l":108300.0,"c":112000.0,"v":750031.0,"a":84784648800.0,"mc":4065189856000.0,"s":36296338,"m":"KOSPI"},"mfe_30d_pct":12.77,"mae_30d_pct":-17.68,"peak_30d_date":"2024-11-12","trough_30d_date":"2024-12-09","end_30d_date":"2024-12-13","mfe_90d_pct":12.77,"mae_90d_pct":-37.41,"peak_90d_date":"2024-11-12","trough_90d_date":"2025-03-07","end_90d_date":"2025-03-19","mfe_180d_pct":12.77,"mae_180d_pct":-58.04,"peak_180d_date":"2024-11-12","trough_180d_date":"2025-05-26","end_180d_date":"2025-07-30","calibration_usable":true,"calibration_unusable_reason":null,"price_source_validation":{"source":"Songdaiki/stock-web","basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false},"evidence_summary":"High-nickel cathode supply route to Tesla/affiliates; direct customer bridge but severe forward MAE keeps Yellow/Green blocked.","evidence_url":"https://www.kedglobal.com/batteries/newsView/ked202411030003","source_proxy_only":false,"evidence_url_pending":false,"score_simulation":{"eps_fcf_explosion":6,"earnings_visibility":6,"bottleneck_pricing":6,"market_mispricing":6,"valuation_rerating":4,"capital_allocation":4,"information_confidence":8,"total":40,"profile_error":"Direct customer bridge preserves Actionable, but high MAE blocks Yellow/Green."},"residual_label":"C13_AMPC_IRA_JV_direct_bridge_quality_repair"}
{"row_type":"aggregate","schema_version":"v12","selected_round":"R3","selected_loop":205,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V5","new_independent_case_count":8,"new_independent_trigger_count":8,"unique_symbol_count":8,"positive_or_reopen_case_count":2,"stage4b_count":3,"stage4c_count":3,"stage2_count":1,"stage2_actionable_count":1,"source_proxy_only_count":2,"evidence_url_pending_count":0,"missing_required_mfe_mae_count":0,"corporate_action_contaminated_180D_count":0,"insufficient_forward_window_180D_count":0,"production_scoring_changed":false,"shadow_weight_only":true,"rule_candidate":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_GATE_V5"}
{"row_type":"shadow_weight","schema_version":"v12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","current_weight_vector":"20/18/14/12/10/10/16","proposed_shadow_direction":"increase bridge-quality gate, no global weight change","production_scoring_changed":false,"do_not_apply_now":true}
```

## 9. Batch Ingest Self-Audit

```text
standard_v12_filename: pass
filename_round_matches_metadata_round: pass
filename_loop_matches_metadata_loop: pass
round_sector_consistency: pass
selected_archetype_drives_round: pass
hard_duplicate_key_check: pass
actual_stock_web_1D_OHLC_used: pass
entry_price_present_for_all_usable_rows: pass
30_90_180_mfe_mae_present_for_all_usable_rows: pass
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
source_proxy_only_count: 2
evidence_url_pending_count: 0
production_scoring_changed: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.
Later coding-agent task: ingest this MD with the rest of docs/round and evaluate whether C13 needs a scoped guardrail that requires direct utilization / shipment / ex-subsidy margin evidence before Stage2-Actionable, Yellow, or Green. Do not loosen Stage3-Green globally. Do not use future MFE/MAE at runtime. Treat all proposed changes as shadow candidates until batch validation passes.
```

## 11. Next Research State

```text
completed_round: R3
completed_loop: 205
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
