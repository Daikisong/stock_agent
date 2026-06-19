# E2R Stock-Web v12 Residual Research — R4 / L4 / C16 Strategic Resource Policy Supply

```text
selected_round: R4
selected_loop: 207
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: C16_DIRECT_OFFTAKE_POSITIVE_CONTROL_AND_PROXY_BASKET_REPAIR_V3
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 URL/proxy-quality cleanup + C16 direct-offtake positive-control sidecar
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Loop Objective

```text
loop_objective: direct_offtake_positive_control_vs_proxy_basket_guardrail
research_question: In C16, when does strategic-resource policy/supply evidence become a real issuer-level Stage2-Actionable bridge, and when is it only long-lead capacity, preliminary talk, or governance-contaminated price action?
```

This loop keeps the C16 strategic-resource frame but deliberately avoids pure rare-earth keyword baskets. The batch is built around direct supply routes: rare-earth oxide supply, nickel mine offtake, lithium hydroxide capacity and cathode input supply, antimony discussions, and nickel-sulfate national-strategic-technology support. The goal is to separate a real issuer-level bridge from a macro/policy label that only paints the ticker with the right color.

## 2. Coverage / No-Repeat Interpretation

| Check | Result |
|---|---|
| Scheduler | coverage-index-first; selected archetype drives round |
| C16 status in No-Repeat Index | 217 rows / 63 symbols / positives-counter 24-51 / 4B-4C 41-0 |
| Reason to select C16 despite over-80 coverage | C16 has many proxy/policy rows and no hard-4C row; direct URL and direct bridge quality remain the valuable residual target. |
| Hard duplicate key | `canonical_archetype_id + symbol + trigger_type + entry_date` |
| Session duplicate avoidance | Avoided the immediately preceding C16 proxy rows such as Union / Union Materials / Hyundai BNG Steel and reused no identical C16 symbol-trigger-entry duplicate key. |

## 3. Price Source Validation

```text
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_schema: d,o,h,l,c,v,a,mc,s,m
manifest_max_date: 2026-02-20
mfe_mae_formula: entry close vs forward window max high / min low
```

All usable trigger rows below have complete 30D/90D/180D forward trading windows inside the stock-web manifest max date. No row in this batch is marked corporate-action contaminated for the 180D window.

## 4. Trigger-Level Price Path Table

| # | Symbol | Company | Trigger | Entry | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak / trough | Role |
|---:|---|---|---|---|---:|---:|---:|---:|---|---|
| 1 | 229640 | LS Eco Energy | Stage2-Actionable | 2024-01-10 | 20,900 | 11.96 / -14.31 | 113.88 / -16.41 | 116.75 / -16.41 | 2024-05-30 / 2024-04-17 | direct_rare_earth_supply_positive_control |
| 2 | 001120 | LX International | Stage2-Actionable | 2024-01-16 | 27,850 | 5.57 / -5.57 | 29.08 / -8.80 | 29.08 / -8.80 | 2024-05-21 / 2024-04-19 | direct_mine_control_and_offtake_positive_control |
| 3 | 005490 | POSCO Holdings | Stage2 | 2024-11-22 | 303,500 | 2.31 / -18.12 | 11.04 / -25.04 | 12.69 / -25.04 | 2025-07-23 / 2025-02-10 | long_lead_capacity_completion_stage2_cap |
| 4 | 003670 | POSCO Future M | Stage2-Actionable | 2024-12-06 | 165,200 | 5.45 / -17.49 | 5.45 / -34.62 | 5.45 / -40.38 | 2024-12-12 / 2025-05-27 | direct_internal_supply_bridge_high_mae |
| 5 | 010130 | Korea Zinc | Stage2 | 2025-01-09 | 927,000 | 0.22 / -20.28 | 17.58 / -30.64 | 19.09 / -30.64 | 2025-09-15 / 2025-04-09 | strategic_mineral_discussion_stage2_cap |
| 6 | 010130 | Korea Zinc | Stage2-Actionable | 2025-01-17 | 840,000 | 10.36 / -15.95 | 29.76 / -23.45 | 88.10 / -23.45 | 2025-10-15 / 2025-04-09 | direct_technology_policy_positive_control_with_governance_noise |

## 5. Evidence Notes

- **229640 LS Eco Energy / Stage2-Actionable / 2024-01-10** — LS Eco Energy disclosed a rare-earth oxide supply route from Vietnam, with neodymium/dysprosium refined by Hung Thinh Mineral and planned supply volumes stepping up from 2024 to 2025. Source: https://www.lscns.co.kr/en/pr/news_view.asp?brd_id=news1&idx=117409&lang_cd=en&mode=MOD&pageNo=1&searchKey=1&searchValue=.
- **001120 LX International / Stage2-Actionable / 2024-01-16** — LX International completed acquisition of 60% control in Indonesia AKP nickel mine; prior official release specified the right to acquire the entire production output under offtake. Source: https://www.businesskorea.co.kr/news/articleView.html?idxno=209704. Secondary: https://www.lxinternational.com/en/news/press_view?seq=434
- **005490 POSCO Holdings / Stage2 / 2024-11-22** — POSCO Group completed domestic lithium hydroxide capacity and disclosed supply to POSCO Future M plus an SK On contract, but the issuer-level stock path remained weak after the capacity event. Source: https://newsroom.posco.com/en/posco-holdings-leads-the-charge-in-rechargeable-battery-material-sovereignty-with-the-comprehensive-completion-of-the-korean-lithium-hydroxide-plant/.
- **003670 POSCO Future M / Stage2-Actionable / 2024-12-06** — POSCO Future M disclosed a lithium hydroxide sourcing deal from POSCO-Pilbara Lithium Solution, reducing China reliance and tying upstream lithium capacity to cathode input supply. Source: https://www.poscofuturem.com/en/pr/list.do?m=&topic=26&y=2024.
- **010130 Korea Zinc / Stage2 / 2025-01-09** — Korea Zinc disclosed preliminary talks with U.S. entities to supply antimony after China export restrictions, but the trigger remained early discussion rather than booked order or margin bridge. Source: https://campaign.koreazinc.co.kr/newsroom_en/korea-zinc-in-talks-with-us-buyers-to-supply-antimony-chairman-says/.
- **010130 Korea Zinc / Stage2-Actionable / 2025-01-17** — Korea Zinc disclosed nickel sulfate manufacturing technology recognition as national strategic technology, with future tax-credit benefits for a nickel refinery expected from 2026 full-scale operation. Source: https://www.asiae.co.kr/en/article/2025011709225936994. Secondary: https://www.prnewswire.com/news-releases/korea-zincs-nickel-sulfate-manufacturing-technology-is-recognized-as-national-strategic-technology-302354155.html

## 6. Score Simulation Snapshot

| Symbol | Trigger | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Total proxy | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 229640 | Stage2-Actionable | 11 | 13 | 16 | 8 | 7 | 5 | 13 | 73 | green_overpromotion_risk_after_direct_supply_headline |
| 001120 | Stage2-Actionable | 12 | 14 | 15 | 8 | 7 | 7 | 13 | 76 | none_stage2_actionable_preserved |
| 005490 | Stage2 | 9 | 11 | 13 | 5 | 5 | 7 | 13 | 63 | stage2_actionable_overpromotion_risk_if_capacity_completion_treated_as_cashflow |
| 003670 | Stage2-Actionable | 10 | 12 | 14 | 6 | 5 | 6 | 13 | 66 | high_mae_green_blocker_required |
| 010130 | Stage2 | 8 | 10 | 15 | 6 | 5 | 5 | 13 | 62 | actionable_overpromotion_risk_if_preliminary_talks_count_as_order |
| 010130 | Stage2-Actionable | 11 | 13 | 14 | 7 | 6 | 8 | 13 | 72 | green_blocker_high_mae_and_governance_noise_required |

## 7. Residual Contribution

```text
rule_candidate: C16_DIRECT_OFFTAKE_TO_CASHFLOW_AND_GOVERNANCE_CONTAMINATION_GATE_V3
sector_rule_candidate: L4_STRATEGIC_RESOURCE_DIRECT_BRIDGE_VS_POLICY_PROXY_GATE
production_scoring_changed: false
shadow_weight_only: true
do_not_apply_immediately: true
```

Core residual:

- Direct mine ownership, offtake rights, supply contract, or customer-linked material route can justify Stage2-Actionable.
- Long-lead capacity completion, preliminary buyer talks, or national-strategic-technology designation should stay capped until shipment, margin, or cashflow conversion appears.
- A strong 180D MFE after direct-resource evidence does not automatically create Stage3-Yellow/Green when interim MAE is deep or when the path is governance/control-premium contaminated.
- C16 Green should require at least two evidence families: direct supply bridge plus realized margin/cashflow or customer shipment conversion.
- Pure proxy baskets and parent-company keyword exposure remain Stage2 cap or local 4B/watch; direct URL does not mean direct economics.

## 8. Batch Ingest Self-Audit

```json
{
  "new_independent_case_count": 6,
  "new_independent_trigger_count": 6,
  "unique_symbol_count": 5,
  "calibration_usable_trigger_count": 6,
  "stage2_count": 2,
  "stage2_actionable_count": 4,
  "stage4b_count": 0,
  "stage4c_count": 0,
  "positive_control_count": 4,
  "counterexample_or_guardrail_case_count": 4,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "missing_entry_price_count": 0,
  "missing_actual_entry_ohlcv_count": 0,
  "corporate_action_contaminated_180D_count": 0,
  "insufficient_forward_window_180D_count": 0,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "ready_for_batch_ingest": true
}
```

## 9. Machine-Readable JSONL Trigger Rows

```jsonl
{"row_type":"trigger","case_id":"C16_207_229640_20240110_RARE_EARTH_OXIDE_CONTRACT","symbol":"229640","company":"LS Eco Energy","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":20900.0,"actual_entry_ohlcv":{"d":"2024-01-10","o":22100.0,"h":22500.0,"l":20300.0,"c":20900.0,"v":3053365,"a":65051923850,"mc":640059971100,"s":30624879,"m":"KOSPI"},"MFE_30D_pct":11.96,"MAE_30D_pct":-14.31,"peak_30D_date":"2024-02-13","peak_30D_price":23400.0,"trough_30D_date":"2024-02-07","trough_30D_price":17910.0,"window_30D_end":"2024-02-22","MFE_90D_pct":113.88,"MAE_90D_pct":-16.41,"peak_90D_date":"2024-05-22","peak_90D_price":44700.0,"trough_90D_date":"2024-04-17","trough_90D_price":17470.0,"window_90D_end":"2024-05-23","MFE_180D_pct":116.75,"MAE_180D_pct":-16.41,"peak_180D_date":"2024-05-30","peak_180D_price":45300.0,"trough_180D_date":"2024-04-17","trough_180D_price":17470.0,"window_180D_end":"2024-10-07","drawdown_after_peak_pct":-51.88,"source_url":"https://www.lscns.co.kr/en/pr/news_view.asp?brd_id=news1&idx=117409&lang_cd=en&mode=MOD&pageNo=1&searchKey=1&searchValue=","evidence_summary":"LS Eco Energy disclosed a rare-earth oxide supply route from Vietnam, with neodymium/dysprosium refined by Hung Thinh Mineral and planned supply volumes stepping up from 2024 to 2025.","case_role":"direct_rare_earth_supply_positive_control","case_type":"positive_control_high_volatility","evidence_family":"rare_earth_oxide_supply_contract","component_scores":{"eps_fcf_explosion":11,"earnings_visibility":13,"bottleneck_pricing":16,"market_mispricing":8,"valuation_rerating":7,"capital_allocation":5,"information_confidence":13},"profile_error":"green_overpromotion_risk_after_direct_supply_headline","residual_label":"direct_supply_actionable_but_not_green_without_margin_cash_bridge","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","selected_round":"R4","selected_loop":207,"fine_archetype_id":"C16_DIRECT_OFFTAKE_POSITIVE_CONTROL_AND_PROXY_BASKET_REPAIR_V3","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"forward_window_trading_days_required":180,"trigger_duplicate_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|229640|Stage2-Actionable|2024-01-10","score_total_proxy":73,"usable_for_promotion":"hold_for_quality"}
{"row_type":"trigger","case_id":"C16_207_001120_20240116_AKP_NICKEL_MINE_COMPLETION","symbol":"001120","company":"LX International","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-16","entry_date":"2024-01-16","entry_price":27850.0,"actual_entry_ohlcv":{"d":"2024-01-16","o":26600.0,"h":27950.0,"l":26300.0,"c":27850.0,"v":386632,"a":10529307350,"mc":1079466000000,"s":38760000,"m":"KOSPI"},"MFE_30D_pct":5.57,"MAE_30D_pct":-5.57,"peak_30D_date":"2024-02-01","peak_30D_price":29400.0,"trough_30D_date":"2024-01-16","trough_30D_price":26300.0,"window_30D_end":"2024-02-28","MFE_90D_pct":29.08,"MAE_90D_pct":-8.8,"peak_90D_date":"2024-05-21","peak_90D_price":35950.0,"trough_90D_date":"2024-04-19","trough_90D_price":25400.0,"window_90D_end":"2024-05-29","MFE_180D_pct":29.08,"MAE_180D_pct":-8.8,"peak_180D_date":"2024-05-21","peak_180D_price":35950.0,"trough_180D_date":"2024-04-19","trough_180D_price":25400.0,"window_180D_end":"2024-10-14","drawdown_after_peak_pct":-27.12,"source_url":"https://www.businesskorea.co.kr/news/articleView.html?idxno=209704","secondary_source_url":"https://www.lxinternational.com/en/news/press_view?seq=434","evidence_summary":"LX International completed acquisition of 60% control in Indonesia AKP nickel mine; prior official release specified the right to acquire the entire production output under offtake.","case_role":"direct_mine_control_and_offtake_positive_control","case_type":"positive","evidence_family":"nickel_mine_acquisition_and_offtake","component_scores":{"eps_fcf_explosion":12,"earnings_visibility":14,"bottleneck_pricing":15,"market_mispricing":8,"valuation_rerating":7,"capital_allocation":7,"information_confidence":13},"profile_error":"none_stage2_actionable_preserved","residual_label":"direct_mine_offtake_actionable_not_yellow_without_margin_fcf","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","selected_round":"R4","selected_loop":207,"fine_archetype_id":"C16_DIRECT_OFFTAKE_POSITIVE_CONTROL_AND_PROXY_BASKET_REPAIR_V3","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"forward_window_trading_days_required":180,"trigger_duplicate_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001120|Stage2-Actionable|2024-01-16","score_total_proxy":76,"usable_for_promotion":"yes_with_green_blocker"}
{"row_type":"trigger","case_id":"C16_207_005490_20241122_LITHIUM_HYDROXIDE_CAPACITY_COMPLETION","symbol":"005490","company":"POSCO Holdings","trigger_type":"Stage2","trigger_date":"2024-11-22","entry_date":"2024-11-22","entry_price":303500.0,"actual_entry_ohlcv":{"d":"2024-11-22","o":306500.0,"h":310500.0,"l":302000.0,"c":303500.0,"v":223888,"a":68585980500,"mc":25076498419500,"s":82624377,"m":"KOSPI"},"MFE_30D_pct":2.31,"MAE_30D_pct":-18.12,"peak_30D_date":"2024-11-22","peak_30D_price":310500.0,"trough_30D_date":"2025-01-02","trough_30D_price":248500.0,"window_30D_end":"2025-01-07","MFE_90D_pct":11.04,"MAE_90D_pct":-25.04,"peak_90D_date":"2025-03-20","peak_90D_price":337000.0,"trough_90D_date":"2025-02-10","trough_90D_price":227500.0,"window_90D_end":"2025-04-08","MFE_180D_pct":12.69,"MAE_180D_pct":-25.04,"peak_180D_date":"2025-07-23","peak_180D_price":342000.0,"trough_180D_date":"2025-02-10","trough_180D_price":227500.0,"window_180D_end":"2025-08-20","drawdown_after_peak_pct":-16.23,"source_url":"https://newsroom.posco.com/en/posco-holdings-leads-the-charge-in-rechargeable-battery-material-sovereignty-with-the-comprehensive-completion-of-the-korean-lithium-hydroxide-plant/","evidence_summary":"POSCO Group completed domestic lithium hydroxide capacity and disclosed supply to POSCO Future M plus an SK On contract, but the issuer-level stock path remained weak after the capacity event.","case_role":"long_lead_capacity_completion_stage2_cap","case_type":"counterexample_or_cap","evidence_family":"lithium_hydroxide_capacity_completion_and_supply_plan","component_scores":{"eps_fcf_explosion":9,"earnings_visibility":11,"bottleneck_pricing":13,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":7,"information_confidence":13},"profile_error":"stage2_actionable_overpromotion_risk_if_capacity_completion_treated_as_cashflow","residual_label":"capacity_completion_without_margin_cash_conversion","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","selected_round":"R4","selected_loop":207,"fine_archetype_id":"C16_DIRECT_OFFTAKE_POSITIVE_CONTROL_AND_PROXY_BASKET_REPAIR_V3","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"forward_window_trading_days_required":180,"trigger_duplicate_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|Stage2|2024-11-22","score_total_proxy":63,"usable_for_promotion":"hold_for_quality"}
{"row_type":"trigger","case_id":"C16_207_003670_20241206_LITHIUM_SUPPLY_TO_CATHODE","symbol":"003670","company":"POSCO Future M","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-06","entry_date":"2024-12-06","entry_price":165200.0,"actual_entry_ohlcv":{"d":"2024-12-06","o":163200.0,"h":166500.0,"l":157200.0,"c":165200.0,"v":344431,"a":56041489300,"mc":12796923944000,"s":77463220,"m":"KOSPI"},"MFE_30D_pct":5.45,"MAE_30D_pct":-17.49,"peak_30D_date":"2024-12-12","peak_30D_price":174200.0,"trough_30D_date":"2025-01-02","trough_30D_price":136300.0,"window_30D_end":"2025-01-21","MFE_90D_pct":5.45,"MAE_90D_pct":-34.62,"peak_90D_date":"2024-12-12","peak_90D_price":174200.0,"trough_90D_date":"2025-04-03","trough_90D_price":108000.0,"window_90D_end":"2025-04-22","MFE_180D_pct":5.45,"MAE_180D_pct":-40.38,"peak_180D_date":"2024-12-12","peak_180D_price":174200.0,"trough_180D_date":"2025-05-27","trough_180D_price":98500.0,"window_180D_end":"2025-09-03","drawdown_after_peak_pct":-43.46,"source_url":"https://www.poscofuturem.com/en/pr/list.do?m=&topic=26&y=2024","evidence_summary":"POSCO Future M disclosed a lithium hydroxide sourcing deal from POSCO-Pilbara Lithium Solution, reducing China reliance and tying upstream lithium capacity to cathode input supply.","case_role":"direct_internal_supply_bridge_high_mae","case_type":"positive_but_guardrailed","evidence_family":"lithium_hydroxide_supply_to_cathode_materials","component_scores":{"eps_fcf_explosion":10,"earnings_visibility":12,"bottleneck_pricing":14,"market_mispricing":6,"valuation_rerating":5,"capital_allocation":6,"information_confidence":13},"profile_error":"high_mae_green_blocker_required","residual_label":"direct_supply_bridge_but_equity_path_rejects_yellow_green","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","selected_round":"R4","selected_loop":207,"fine_archetype_id":"C16_DIRECT_OFFTAKE_POSITIVE_CONTROL_AND_PROXY_BASKET_REPAIR_V3","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"forward_window_trading_days_required":180,"trigger_duplicate_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|003670|Stage2-Actionable|2024-12-06","score_total_proxy":66,"usable_for_promotion":"hold_for_quality"}
{"row_type":"trigger","case_id":"C16_207_010130_20250109_ANTIMONY_US_BUYERS_TALK","symbol":"010130","company":"Korea Zinc","trigger_type":"Stage2","trigger_date":"2025-01-09","entry_date":"2025-01-09","entry_price":927000.0,"actual_entry_ohlcv":{"d":"2025-01-09","o":900000.0,"h":929000.0,"l":886000.0,"c":927000.0,"v":84336,"a":77465411000,"mc":19191943341000,"s":20703283,"m":"KOSPI"},"MFE_30D_pct":0.22,"MAE_30D_pct":-20.28,"peak_30D_date":"2025-01-09","peak_30D_price":929000.0,"trough_30D_date":"2025-01-22","trough_30D_price":739000.0,"window_30D_end":"2025-02-25","MFE_90D_pct":17.58,"MAE_90D_pct":-30.64,"peak_90D_date":"2025-03-13","peak_90D_price":1090000.0,"trough_90D_date":"2025-04-09","trough_90D_price":643000.0,"window_90D_end":"2025-05-26","MFE_180D_pct":19.09,"MAE_180D_pct":-30.64,"peak_180D_date":"2025-09-15","peak_180D_price":1104000.0,"trough_180D_date":"2025-04-09","trough_180D_price":643000.0,"window_180D_end":"2025-10-02","drawdown_after_peak_pct":-17.75,"source_url":"https://campaign.koreazinc.co.kr/newsroom_en/korea-zinc-in-talks-with-us-buyers-to-supply-antimony-chairman-says/","evidence_summary":"Korea Zinc disclosed preliminary talks with U.S. entities to supply antimony after China export restrictions, but the trigger remained early discussion rather than booked order or margin bridge.","case_role":"strategic_mineral_discussion_stage2_cap","case_type":"guardrail","evidence_family":"antimony_export_control_supply_discussion","component_scores":{"eps_fcf_explosion":8,"earnings_visibility":10,"bottleneck_pricing":15,"market_mispricing":6,"valuation_rerating":5,"capital_allocation":5,"information_confidence":13},"profile_error":"actionable_overpromotion_risk_if_preliminary_talks_count_as_order","residual_label":"strategic_mineral_talks_without_signed_contract_stage2_cap","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","selected_round":"R4","selected_loop":207,"fine_archetype_id":"C16_DIRECT_OFFTAKE_POSITIVE_CONTROL_AND_PROXY_BASKET_REPAIR_V3","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"forward_window_trading_days_required":180,"trigger_duplicate_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|Stage2|2025-01-09","score_total_proxy":62,"usable_for_promotion":"hold_for_quality"}
{"row_type":"trigger","case_id":"C16_207_010130_20250117_NICKEL_SULFATE_STRATEGIC_TECH","symbol":"010130","company":"Korea Zinc","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-17","entry_date":"2025-01-17","entry_price":840000.0,"actual_entry_ohlcv":{"d":"2025-01-17","o":809000.0,"h":863000.0,"l":808000.0,"c":840000.0,"v":68053,"a":57642419000,"mc":17390757720000,"s":20703283,"m":"KOSPI"},"MFE_30D_pct":10.36,"MAE_30D_pct":-15.95,"peak_30D_date":"2025-01-20","peak_30D_price":927000.0,"trough_30D_date":"2025-03-06","trough_30D_price":706000.0,"window_30D_end":"2025-03-06","MFE_90D_pct":29.76,"MAE_90D_pct":-23.45,"peak_90D_date":"2025-03-13","peak_90D_price":1090000.0,"trough_90D_date":"2025-04-09","trough_90D_price":643000.0,"window_90D_end":"2025-06-04","MFE_180D_pct":88.1,"MAE_180D_pct":-23.45,"peak_180D_date":"2025-10-15","peak_180D_price":1580000.0,"trough_180D_date":"2025-04-09","trough_180D_price":643000.0,"window_180D_end":"2025-10-17","drawdown_after_peak_pct":-23.67,"source_url":"https://www.asiae.co.kr/en/article/2025011709225936994","secondary_source_url":"https://www.prnewswire.com/news-releases/korea-zincs-nickel-sulfate-manufacturing-technology-is-recognized-as-national-strategic-technology-302354155.html","evidence_summary":"Korea Zinc disclosed nickel sulfate manufacturing technology recognition as national strategic technology, with future tax-credit benefits for a nickel refinery expected from 2026 full-scale operation.","case_role":"direct_technology_policy_positive_control_with_governance_noise","case_type":"positive_but_high_mae","evidence_family":"national_strategic_technology_and_nickel_refinery_tax_credit","component_scores":{"eps_fcf_explosion":11,"earnings_visibility":13,"bottleneck_pricing":14,"market_mispricing":7,"valuation_rerating":6,"capital_allocation":8,"information_confidence":13},"profile_error":"green_blocker_high_mae_and_governance_noise_required","residual_label":"direct_policy_technology_actionable_but_not_green_without_revenue_margin","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","selected_round":"R4","selected_loop":207,"fine_archetype_id":"C16_DIRECT_OFFTAKE_POSITIVE_CONTROL_AND_PROXY_BASKET_REPAIR_V3","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"forward_window_trading_days_required":180,"trigger_duplicate_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|Stage2-Actionable|2025-01-17","score_total_proxy":72,"usable_for_promotion":"hold_for_quality"}
```

## 10. Aggregate JSONL Row

```jsonl
{"row_type":"aggregate","selected_round":"R4","selected_loop":207,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_DIRECT_OFFTAKE_POSITIVE_CONTROL_AND_PROXY_BASKET_REPAIR_V3","new_independent_case_count":6,"new_independent_trigger_count":6,"unique_symbol_count":5,"calibration_usable_trigger_count":6,"stage2_count":2,"stage2_actionable_count":4,"stage4b_count":0,"stage4c_count":0,"positive_control_count":4,"counterexample_or_guardrail_case_count":4,"source_proxy_only_count":0,"evidence_url_pending_count":0,"missing_required_mfe_mae_count":0,"missing_entry_price_count":0,"missing_actual_entry_ohlcv_count":0,"corporate_action_contaminated_180D_count":0,"insufficient_forward_window_180D_count":0,"production_scoring_changed":false,"shadow_weight_only":true,"ready_for_batch_ingest":true,"aggregate_MFE_180D_avg_pct":45.19,"aggregate_MAE_180D_avg_pct":-24.12,"residual_rule_candidate":"C16_DIRECT_OFFTAKE_TO_CASHFLOW_AND_GOVERNANCE_CONTAMINATION_GATE_V3"}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring directly from this single MD. In a later batch-coding session, ingest this MD together with other v12 rows and test whether C16 direct-offtake rows justify a scoped guardrail: Stage2-Actionable requires issuer-level supply/offtake/order/shipment bridge; Yellow/Green require realized margin/cashflow or shipment conversion; policy/proxy/governance-only price paths stay capped or 4B/watch.
```

## 12. Next Research State

```text
completed_round: R4
completed_loop: 207
completed_large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
completed_canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
