# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 126
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = mixed_c09_advanced_equipment_blowoff_leaf_set
selected_priority_bucket = Priority 0
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
output_filename = e2r_stock_web_v12_residual_round_R2_loop_126_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
```

이번 loop는 R1~R13 순환이 아니라 coverage-index-first 선택이다. 최신 No-Repeat Index에서 C02와 C09가 10 rows로 Priority 0 최저권이었고, 직전 local 산출물이 C02였기 때문에 이번에는 C09를 선택했다. C09의 기존 대표 row는 10개, symbols 10개, positives/counter 0/10, 4B/4C 3/0이므로 positive 예외와 4C timing을 같이 보강한다.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C09_advanced_equipment_shadow_profile
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

C09에서는 이미 적용된 global guardrail 자체를 반복 증명하는 것이 목표가 아니다. 잔여 문제는 “첨단 장비 + HBM/AI 키워드 + 상대강도”가 Stage2 evidence처럼 보이지만, named order, shipment revenue recognition, margin bridge가 없는 경우다. 반대로 동일 장비 narrative라도 named customer contract 또는 durable order/margin bridge가 생기면 pure blowoff가 아니라 Stage2-Actionable 예외로 남겨야 한다.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R2 |
| selected_loop | 126 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF |
| sector | AI / semiconductor / advanced equipment |
| scope | HBM, inspection/metrology, laser annealing, wafer tester, AFM equipment |
| non-scope | memory customer capacity C06, HBM equipment order RS C07, test socket quality C08, memory recovery cycle C10 |

C09는 장비 자체의 기술 우수성을 부정하는 taxonomy가 아니다. 같은 기술 leaf라도 가격이 먼저 과열되고 order/revenue/margin bridge가 뒤따르지 않으면 C09로 분류한다. bridge가 확인되면 C07/C08/C10 또는 C09의 positive exception으로 압축한다.

## 3. Previous Coverage / Duplicate Avoidance Check

| check | result |
|---|---|
| No-Repeat priority | C09 Priority 0, rows 10, need to 30 = 20, need to 50 = 40 |
| existing C09 top covered symbols | 031980, 036810, 039030, 042700, 079370, 089030 shown in Index snapshot |
| selected symbols | 110990, 232140, 140860, 322310, 064290 |
| exact duplicate key avoided | canonical_archetype_id + symbol + trigger_type + entry_date not repeated from visible top list |
| same symbol reuse | 110990 has two different trigger families; 064290 has Stage4B and later Stage4C timing row |
| minimum new symbol count | 5 >= 2 |
| minimum positive/counter balance | positive 2, counterexample 4 |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| manifest_max_date | 2026-02-20 |
| MFE/MAE method | max high / min low from entry_date through 30/90/180 tradable rows |
| corporate action policy | 180D contaminated windows blocked; selected windows clean |

## 5. Historical Eligibility Gate

All trigger rows are historical. Each entry_date exists in a stock-web tradable shard. Every trigger has at least 180 forward trading rows by the manifest max date. Required MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct are present in the table and JSONL rows. No selected 180D window overlaps a corporate-action candidate date.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| LASER_ANNEALING_HBM_EXPECTATION_PRICE_BLOWOFF | C09 | HBM laser annealing narrative without confirmed new order/revenue bridge at trigger |
| LASER_ANNEALING_SKHYNIX_ORDER_BACKED_EXCEPTION | C09 | Same technology leaf, but named customer contract creates positive exception inside C09 |
| AFM_METROLOGY_ORDER_GROWTH_BACKED_RERATING | C09 | Advanced metrology quality case; positive control group for non-blowoff equipment rerating |
| HBM_WAFER_TESTER_DELIVERY_START_VALUATION_RISK | C09 | Delivery-start narrative after prior price expansion, conversion not yet durable |
| OVERLAY_METROLOGY_HBM_WARPAGE_HIGH_VALUATION | C09 | Report explicitly notes high valuation while HBM contribution remains expected |
| HBM_MODULE_INSPECTION_PILOT_NOT_PO_BLOWOFF | C09 | Pilot/possible PO is not equivalent to confirmed order/revenue bridge |
| HBM_INSPECTION_REVENUE_BRIDGE_FAILS_AND_LOSS_CONFIRMS | C09 | 4C timing leaf for failed conversion after initial pilot narrative |

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|MFE_180D_pct|MAE_180D_pct|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|C09_110990_DIT_20240417_BLOWOFF|110990|디아이티|valuation_blowoff_false_positive|counterexample|R2L126_C09_110990_20240417_4B|15.12|-65.48|current_profile_false_positive|
|C09_110990_DIT_20250114_ORDER_BACKED|110990|디아이티|order_backed_exception|positive|R2L126_C09_110990_20250114_S2A|34.28|-23.66|current_profile_correct|
|C09_140860_PARKSYSTEMS_20240507_AFM_STRUCTURAL|140860|파크시스템스|structural_success|positive|R2L126_C09_140860_20240507_S2A|60.77|-3.86|current_profile_correct|
|C09_232140_YC_20240816_HBM_TESTER_TOO_EARLY|232140|와이씨|stage2_too_early|counterexample|R2L126_C09_232140_20240816_S2|1.86|-50.45|current_profile_false_positive|
|C09_322310_AUROS_20240327_HIGH_VALUATION|322310|오로스테크놀로지|valuation_blowoff_false_positive|counterexample|R2L126_C09_322310_20240327_4B|5|-62.34|current_profile_false_positive|
|C09_064290_INTEKPLUS_2024_HBM_PILOT_TO_LOSS|064290|인텍플러스|pilot_to_loss_counterexample|counterexample|R2L126_C09_064290_20240221_4B/R2L126_C09_064290_20240716_4C|12.05|-72.88|current_profile_4C_too_late|

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive / structural or order-backed exception | 2 | DIT 2025 named SK hynix order, Park Systems AFM/metrology structural rerating |
| counterexample / false positive / 4C timing | 4 | DIT 2024 expectation blowoff, YC delivery-start too early, Auros high valuation, Intekplus pilot-to-loss |
| Stage4B rows | 3 | DIT 2024, Auros 2024, Intekplus 2024 pilot |
| Stage4C rows | 1 | Intekplus 2024 loss confirmation |
| current profile error rows | 5 | false positive or 4C too late rows |

## 9. Evidence Source Map

|symbol|company|trigger_date|source_summary|source_url|
|---|---|---|---|---|
|110990|디아이티|2024-04-17|TheBigDataNews 2024-04-17: Nvidia B100/HBM3E laser annealing beneficiary narrative; order expectation exceeded confirmed revenue bridge.|https://www.thebigdata.co.kr/view.php?ud=202404170511366621cd1e7f0bdf_23|
|110990|디아이티|2025-01-14|TheElec 2025-01-14: SK hynix laser annealing equipment supply contract KRW 20.52bn, 19.17% of recent annual revenue; laser solution mix rising.|https://www.thelec.kr/news/articleView.html?idxno=32286|
|140860|파크시스템스|2024-05-07|MiraeAsset 2024-05-07: global AFM leader, semiconductor miniaturization/HBM demand, order backlog and product demand visibility.|https://securities.miraeasset.com/bbs/download/2126453.pdf?attachmentId=2126453|
|232140|와이씨|2024-08-16|YC-hosted Hyundai report 2024-08-16: 4Q HBM tester delivery start; 2Q24 sales down YoY but operating profit turned positive.|https://yccorp.com/bbs/bbs_download.php?download=1&idx=256|
|322310|오로스테크놀로지|2024-03-27|eBEST 2024-03-27: HBM inspection/metrology localization beneficiary; 2024E sales/OP growth but 2024E PER around 34x high valuation.|https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%98%A4%EB%A1%9C%EC%8A%A4%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80.pdf|
|064290|인텍플러스|2024-02-21|TheBell 2024-02-20/21: SK hynix HBM module inspection pilot/supply negotiation, possible PO; company had 2023 revenue decline and operating loss.|https://www.thebell.co.kr/front/newsview.asp?key=202402201210212520106824|
|064290|인텍플러스|2024-07-16|DailyInvest 2024-07-16: 1Q24 operating loss remained; 2023 revenue fell 37.1% and operating profit turned to KRW 11.09bn loss; some analysts still expected HBM/2.5D upside.|https://www.dailyinvest.kr/news/articleView.html?idxno=59633|

## 10. Price Data Source Map

|symbol|company_name|profile_path|price_shards|corporate_action_window_status|
|---|---|---|---|---|
|110990|디아이티|atlas/symbol_profiles/110/110990.json|atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv / atlas/ohlcv_tradable_by_symbol_year/110/110990/2025.csv|clean_180D_window|
|232140|와이씨|atlas/symbol_profiles/232/232140.json|atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv|clean_180D_window__profile_has_2017_corporate_action_outside_window|
|140860|파크시스템스|atlas/symbol_profiles/140/140860.json|atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv|clean_180D_window|
|322310|오로스테크놀로지|atlas/symbol_profiles/322/322310.json|atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv|clean_180D_window|
|064290|인텍플러스|atlas/symbol_profiles/064/064290.json|atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv|clean_180D_window|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|drawdown_after_peak_pct|current_profile_verdict|trigger_outcome_label|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R2L126_C09_110990_20240417_4B|110990|디아이티|Stage4B|2024-04-17|2024-04-17|28100|15.12|-20.82|15.12|-51.25|15.12|-65.48|2024-04-26|-70.02|current_profile_false_positive|price_only_hbm_laser_anneal_blowoff_counterexample|
|R2L126_C09_110990_20250114_S2A|110990|디아이티|Stage2-Actionable|2025-01-14|2025-01-14|14500|34.28|-2.9|34.28|-20.34|34.28|-23.66|2025-01-22|-43.14|current_profile_correct|order_backed_hbm_equipment_exception_positive_but_volatile|
|R2L126_C09_140860_20240507_S2A|140860|파크시스템스|Stage2-Actionable|2024-05-07|2024-05-07|155500|23.67|-1.74|27.85|-3.86|60.77|-3.86|2025-01-22|-11|current_profile_correct|advanced_metrology_order_quality_positive|
|R2L126_C09_232140_20240816_S2|232140|와이씨|Stage2|2024-08-16|2024-08-16|16690|1.86|-35.11|1.86|-50.45|1.86|-50.45|2024-08-16|-51.35|current_profile_false_positive|hbm_tester_delivery_start_too_early_counterexample|
|R2L126_C09_322310_20240327_4B|322310|오로스테크놀로지|Stage4B|2024-03-27|2024-03-27|35000|5|-25.71|5|-53.43|5|-62.34|2024-03-28|-64.14|current_profile_false_positive|high_valuation_hbm_metrology_blowoff_counterexample|
|R2L126_C09_064290_20240221_4B|064290|인텍플러스|Stage4B|2024-02-21|2024-02-21|36500|12.05|-7.12|12.05|-42.47|12.05|-72.88|2024-03-07|-75.79|current_profile_false_positive|pilot_supply_discussion_price_blowoff_counterexample|
|R2L126_C09_064290_20240716_4C|064290|인텍플러스|Stage4C|2024-07-16|2024-07-16|21600|1.39|-31.44|1.39|-57.31|1.39|-63.06|2024-07-16|-63.56|current_profile_4C_too_late|loss_confirmation_hard_4c_after_hbm_pilot_hype|

## 12. Trigger-Level OHLC Backtest Tables

The OHLC computation used entry_date close as entry_price. If evidence was pre-market or intraday with market reaction possible, same-day close was used. If evidence availability was treated as next-trading-day usable, the next tradable close was used.

|trigger_id|price_shard_path|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|below_entry_price_flag_30D|below_entry_price_flag_90D|below_entry_price_flag_180D|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R2L126_C09_110990_20240417_4B|atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv|2024-04-17|28100|15.12|-20.82|15.12|-51.25|15.12|-65.48|True|True|True|2024-04-26|32350|-70.02|
|R2L126_C09_110990_20250114_S2A|atlas/ohlcv_tradable_by_symbol_year/110/110990/2025.csv|2025-01-14|14500|34.28|-2.9|34.28|-20.34|34.28|-23.66|False|True|True|2025-01-22|19470|-43.14|
|R2L126_C09_140860_20240507_S2A|atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv|2024-05-07|155500|23.67|-1.74|27.85|-3.86|60.77|-3.86|False|True|True|2025-01-22|250000|-11|
|R2L126_C09_232140_20240816_S2|atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv|2024-08-16|16690|1.86|-35.11|1.86|-50.45|1.86|-50.45|True|True|True|2024-08-16|17000|-51.35|
|R2L126_C09_322310_20240327_4B|atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv|2024-03-27|35000|5|-25.71|5|-53.43|5|-62.34|True|True|True|2024-03-28|36750|-64.14|
|R2L126_C09_064290_20240221_4B|atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv|2024-02-21|36500|12.05|-7.12|12.05|-42.47|12.05|-72.88|True|True|True|2024-03-07|40900|-75.79|
|R2L126_C09_064290_20240716_4C|atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv|2024-07-16|21600|1.39|-31.44|1.39|-57.31|1.39|-63.06|True|True|True|2024-07-16|21900|-63.56|

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| Would current profile catch all cases? | Not fully. It has global price-only blowoff and 4B non-price guard, but C09 still needs a stricter advanced-equipment valuation bridge. |
| Was Stage2 bonus too strong? | Too strong for YC delivery-start and Intekplus pilot-only narratives; appropriate for DIT 2025 and Park Systems. |
| Was Yellow 75 too high/low? | Appropriate for positives; too loose if relative strength plus HBM vocabulary pushes a non-order case toward Yellow. |
| Was Green 87/revision 55 too strict? | Appropriate. None of the C09 positives should become Green solely on early technology narrative. |
| Was price-only blowoff guard appropriate? | Yes, but C09 needs explicit valuation/order bridge interpretation, not just price-only detection. |
| Was full 4B non-price requirement appropriate? | Yes. C09 full 4B should require evidence of non-price thesis exhaustion, not only a high price. |
| Was hard 4C routing late? | In Intekplus, yes. Loss persistence and CB reset after pilot hype should route to 4C earlier. |

## 14. Stage2 / Yellow / Green Comparison

| symbol | trigger | suggested before | suggested after shadow C09 gate | reason |
|---|---|---|---|---|
| 110990 | 2024 expectation blowoff | Stage2 or Stage4B-Watch | Stage4B-Watch | HBM laser annealing narrative was plausible but not order-backed at trigger; MAE180 -65.52%. |
| 110990 | 2025 named SK hynix order | Stage2-Actionable | Stage2-Actionable | Named customer, KRW 20.52bn contract, revenue percentage disclosed; keep below Green due volatility. |
| 140860 | AFM structural rerating | Stage2-Actionable | Stage2-Actionable / Yellow watch | Order/product quality and low MAE support positive exception; Green still waits for revision durability. |
| 232140 | delivery-start narrative | Stage2 | Stage2-Watch or 4B-Watch | Delivery timing without annual bridge produced MAE180 -50.39%. |
| 322310 | high valuation metrology narrative | Stage2 | Stage4B-Watch | Report explicitly acknowledged high valuation; price path collapsed after trigger. |
| 064290 | pilot/possible PO | Stage2 | Stage4B-Watch → 4C on loss confirmation | Pilot is not order. Persistent loss later confirms thesis break. |

## 15. 4B Local vs Full-window Timing Audit

|trigger_id|symbol|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_180D_pct|MAE_180D_pct|four_b_local_peak_proximity|four_b_full_window_peak_proximity|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|
|R2L126_C09_110990_20240417_4B|110990|2024-04-17|28100|15.12|-20.82|15.12|-65.48|-13.14|-13.14|-70.02|
|R2L126_C09_322310_20240327_4B|322310|2024-03-27|35000|5|-25.71|5|-62.34|-4.76|-4.76|-64.14|
|R2L126_C09_064290_20240221_4B|064290|2024-02-21|36500|12.05|-7.12|12.05|-72.88|-10.76|-10.76|-75.79|

C09 4B should not mean “all expensive equipment is bad.” It means the stage engine should put a yellow tape around price extension when evidence is still an order expectation, pilot, or valuation-rich report. In this set, 4B rows have poor 90D/180D MAE and the peak is local, not a durable rerating path.

## 16. 4C Protection Audit

| case | 4C evidence | timing read |
|---|---|---|
| Intekplus 064290 | Continued operating losses, weak demand commentary, conversion-bond reset after price decline | The initial HBM pilot row should not remain a Stage2 watch indefinitely. Once loss/CB reset data appeared, route to 4C. |
| DIT 2024 | Price collapsed after expectation-only trigger but later real contracts arrived in 2025 | Do not hard-4C the technology leaf itself; 4C applies to the specific expectation trigger, not the company forever. |
| Auros 2024 | High valuation corrected hard, but later 2025 results improved | Prefer 4B-watch for initial valuation blowoff; avoid permanent 4C if later order/revenue conversion arrives. |

## 17. Sector-Specific Rule Candidate

```text
rule_id = L2_C09_ADVANCED_EQUIPMENT_ORDER_OR_MARGIN_BRIDGE_GATE_V1
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS / C09
proposal_type = sector_specific_shadow_only
production_scoring_changed = false
```

If an advanced equipment case is promoted by HBM/AI/advanced packaging vocabulary, require at least one of the following before Stage2-Actionable: named customer order, disclosed contract size, shipment/revenue recognition timing, or margin/revision bridge. If the evidence is pilot, possible PO, “beneficiary” vocabulary, or a report that explicitly flags high valuation, keep it at Stage2-Watch or Stage4B-Watch.

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C09_ORDER_BACKED_EXCEPTION_VS_VALUATION_BLOWOFF_GATE_V1
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
positive_exception = named_order_or_durable_margin_bridge
negative_gate = pilot_only_or_high_valuation_or_delivery_start_without_revenue_bridge
4c_escalation = operating_loss_persistence_or_cb_reset_after_failed_conversion
```

The same fine leaf can migrate within C09: DIT 2024 was expectation-only and failed; DIT 2025 was named-order backed and worked better. The classifier should not overfit company name. It should read the evidence object: expectation, order, revenue, margin, or thesis break.

## 19. Before / After Backtest Comparison

| metric | before C09 shadow gate | after C09 shadow gate |
|---|---|---|
| false-positive rows in this loop | 5 | expected 1-2 |
| positive rows preserved | uncertain | 2 preserved |
| 4B watch rows | under-specified | 3 explicit rows |
| 4C timing rows | late | 1 explicit row |
| expected profile effect | HBM/AI equipment relative strength can leak into Stage2 | relative strength must be backed by order/margin bridge |

## 20. Score-Return Alignment Matrix

|trigger_id|symbol|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|
|R2L126_C09_110990_20240417_4B|110990|68|Stage2|54|Stage4B-Watch|15.12|-51.25|bad_entry_or_false_positive|current_profile_false_positive|
|R2L126_C09_110990_20250114_S2A|110990|73|Stage2-Actionable|76|Stage2-Actionable|34.28|-20.34|return_aligned|current_profile_correct|
|R2L126_C09_140860_20240507_S2A|140860|76|Stage2-Actionable|80|Stage2-Actionable|27.85|-3.86|return_aligned|current_profile_correct|
|R2L126_C09_232140_20240816_S2|232140|68|Stage2|54|Stage4B-Watch|1.86|-50.45|bad_entry_or_false_positive|current_profile_false_positive|
|R2L126_C09_322310_20240327_4B|322310|72|Stage2|56|Stage4B-Watch|5|-53.43|bad_entry_or_false_positive|current_profile_false_positive|
|R2L126_C09_064290_20240221_4B|064290|68|Stage2|54|Stage4B-Watch|12.05|-42.47|bad_entry_or_false_positive|current_profile_false_positive|
|R2L126_C09_064290_20240716_4C|064290|47|Stage4B-Watch|34|Stage4C|1.39|-57.31|bad_entry_or_false_positive|current_profile_4C_too_late|

## 21. Coverage Matrix

| item | before | added by this MD | after if accepted |
|---|---:|---:|---:|
| C09 representative rows | 10 | 6 representative trigger groups / 7 trigger rows | about 16 representative rows if all accepted |
| C09 unique symbols | 10 | 5 | about 15 |
| C09 positives | 0 | 2 | 2 |
| C09 counterexamples | 10 | 4 | 14 |
| C09 4B rows | 3 | 3 | 6 |
| C09 4C rows | 0 | 1 | 1 |

## 22. Residual Contribution Summary

```text
new_independent_case_count = 6
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 7
calibration_usable_trigger_count = 7
positive_case_count = 2
counterexample_count = 4
stage4b_trigger_count = 3
stage4c_trigger_count = 1
current_profile_error_count = 5
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical OHLC path from stock-web tradable_raw shards, trigger-level 30/90/180D MFE/MAE, C09-specific residual profile stress, duplicate avoidance against visible No-Repeat Index top symbols.

Non-validation scope: no live stock discovery, no investment recommendation, no production code patch, no direct update to stock_agent scoring profile, no alternate price route discovery, no adjusted-price reconstruction.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C09_order_or_margin_bridge_required,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"Advanced equipment relative strength should not promote beyond Stage2 unless named order/revenue/margin bridge is present; otherwise Stage4B-Watch.","Cuts false positives in 110990_20240417,232140_20240816,322310_20240327,064290_20240221 while preserving 110990_20250114 and 140860_20240507 positives.","R2L126_C09_110990_20240417_4B|R2L126_C09_232140_20240816_S2|R2L126_C09_322310_20240327_4B|R2L126_C09_064290_20240221_4B|R2L126_C09_110990_20250114_S2A|R2L126_C09_140860_20240507_S2A",7,6,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C09_4c_loss_or_cb_reset_escalation,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"If pilot/order expectation is followed by operating loss persistence, demand weakness, or CB reset after price decline, escalate from 4B-watch to 4C.","Improves 064290 path; prevents stale HBM pilot narrative from remaining Stage2 watch.","R2L126_C09_064290_20240716_4C",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C09_110990_DIT_20240417_BLOWOFF","symbol":"110990","company_name":"디아이티","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LASER_ANNEALING_HBM_EXPECTATION_PRICE_BLOWOFF","case_type":"valuation_blowoff_false_positive","positive_or_counterexample":"counterexample","best_trigger":"R2L126_C09_110990_20240417_4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_if_blocked_misaligned_if_positive_stage","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Expectation about Nvidia B100/HBM laser annealing was technically plausible, but the entry sat near a narrative peak and 180D MAE exceeded -60%."}
{"row_type":"case","case_id":"C09_110990_DIT_20250114_ORDER_BACKED","symbol":"110990","company_name":"디아이티","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LASER_ANNEALING_SKHYNIX_ORDER_BACKED_EXCEPTION","case_type":"order_backed_exception","positive_or_counterexample":"positive","best_trigger":"R2L126_C09_110990_20250114_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Same equipment story became more usable when the named SK hynix contract and revenue-percentage bridge arrived; still volatile, so Stage2-Actionable not Green."}
{"row_type":"case","case_id":"C09_140860_PARKSYSTEMS_20240507_AFM_STRUCTURAL","symbol":"140860","company_name":"파크시스템스","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"AFM_METROLOGY_ORDER_GROWTH_BACKED_RERATING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L126_C09_140860_20240507_S2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"AFM/metrology was an advanced equipment rerating that did not behave like a pure blowoff: MFE180 high with shallow MAE."}
{"row_type":"case","case_id":"C09_232140_YC_20240816_HBM_TESTER_TOO_EARLY","symbol":"232140","company_name":"와이씨","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_WAFER_TESTER_DELIVERY_START_VALUATION_RISK","case_type":"stage2_too_early","positive_or_counterexample":"counterexample","best_trigger":"R2L126_C09_232140_20240816_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_if_blocked_misaligned_if_positive_stage","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"HBM tester delivery-start evidence came after a huge early move and before durable revenue conversion; 180D MAE remained large."}
{"row_type":"case","case_id":"C09_322310_AUROS_20240327_HIGH_VALUATION","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"OVERLAY_METROLOGY_HBM_WARPAGE_HIGH_VALUATION","case_type":"valuation_blowoff_false_positive","positive_or_counterexample":"counterexample","best_trigger":"R2L126_C09_322310_20240327_4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_if_blocked_misaligned_if_positive_stage","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Report itself acknowledged high valuation; price path confirms C09 should require valuation-to-order conversion before positive stage."}
{"row_type":"case","case_id":"C09_064290_INTEKPLUS_2024_HBM_PILOT_TO_LOSS","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_MODULE_INSPECTION_PILOT_NOT_PO_BLOWOFF","case_type":"pilot_to_loss_counterexample","positive_or_counterexample":"counterexample","best_trigger":"R2L126_C09_064290_20240221_4B|R2L126_C09_064290_20240716_4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_if_blocked_misaligned_if_positive_stage","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Pilot/possible PO narrative failed to convert quickly; later losses and CB reset made 4C protection relevant."}
{"row_type":"trigger","trigger_id":"R2L126_C09_110990_20240417_4B","case_id":"C09_110990_DIT_20240417_BLOWOFF","symbol":"110990","company_name":"디아이티","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LASER_ANNEALING_HBM_EXPECTATION_PRICE_BLOWOFF","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-04-17","entry_date":"2024-04-17","entry_price":28100.0,"evidence_available_at_that_date":"2024-04-17 05:11 KST / pre-market","evidence_source":"TheBigDataNews 2024-04-17: Nvidia B100/HBM3E laser annealing beneficiary narrative; order expectation exceeded confirmed revenue bridge. | https://www.thebigdata.co.kr/view.php?ud=202404170511366621cd1e7f0bdf_23","stage2_evidence_fields":["HBM3E laser annealing beneficiary narrative","SK hynix HBM3E line reference","AI GPU demand proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["expectation-led price blowoff","order/revenue bridge not yet confirmed at trigger","valuation/price extension before evidence conversion"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv","profile_path":"atlas/symbol_profiles/110/110990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.12,"MFE_90D_pct":15.12,"MFE_180D_pct":15.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.82,"MAE_90D_pct":-51.25,"MAE_180D_pct":-65.48,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-04-26","peak_price":32350.0,"drawdown_after_peak_pct":-70.02,"green_lateness_ratio":0.231,"four_b_local_peak_proximity":-13.14,"four_b_full_window_peak_proximity":-13.14,"trigger_outcome_label":"price_only_hbm_laser_anneal_blowoff_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_110990_DIT_20240417_BLOWOFF_2024-04-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L126_C09_110990_20250114_S2A","case_id":"C09_110990_DIT_20250114_ORDER_BACKED","symbol":"110990","company_name":"디아이티","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LASER_ANNEALING_SKHYNIX_ORDER_BACKED_EXCEPTION","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-14","entry_date":"2025-01-14","entry_price":14500.0,"evidence_available_at_that_date":"2025-01-14 14:41 KST / intraday","evidence_source":"TheElec 2025-01-14: SK hynix laser annealing equipment supply contract KRW 20.52bn, 19.17% of recent annual revenue; laser solution mix rising. | https://www.thelec.kr/news/articleView.html?idxno=32286","stage2_evidence_fields":["named customer contract","contract size vs annual revenue disclosed","laser solution revenue mix becoming semiconductor-led"],"stage3_evidence_fields":["order-backed visibility but only one tranche; not Green by itself"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2025.csv","profile_path":"atlas/symbol_profiles/110/110990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.28,"MFE_90D_pct":34.28,"MFE_180D_pct":34.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.9,"MAE_90D_pct":-20.34,"MAE_180D_pct":-23.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2025-01-22","peak_price":19470.0,"drawdown_after_peak_pct":-43.14,"green_lateness_ratio":1.449,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"order_backed_hbm_equipment_exception_positive_but_volatile","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_110990_DIT_20250114_ORDER_BACKED_2025-01-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L126_C09_140860_20240507_S2A","case_id":"C09_140860_PARKSYSTEMS_20240507_AFM_STRUCTURAL","symbol":"140860","company_name":"파크시스템스","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"AFM_METROLOGY_ORDER_GROWTH_BACKED_RERATING","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-07","entry_date":"2024-05-07","entry_price":155500.0,"evidence_available_at_that_date":"2024-05-07 / report date","evidence_source":"MiraeAsset 2024-05-07: global AFM leader, semiconductor miniaturization/HBM demand, order backlog and product demand visibility. | https://securities.miraeasset.com/bbs/download/2126453.pdf?attachmentId=2126453","stage2_evidence_fields":["AFM industrial demand visibility","semiconductor miniaturization/HBM process exposure","order trend highlighted"],"stage3_evidence_fields":["high margin equipment model","structural customer/region diversification"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv","profile_path":"atlas/symbol_profiles/140/140860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.67,"MFE_90D_pct":27.85,"MFE_180D_pct":60.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.74,"MAE_90D_pct":-3.86,"MAE_180D_pct":-3.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2025-01-22","peak_price":250000.0,"drawdown_after_peak_pct":-11.0,"green_lateness_ratio":15.744,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"advanced_metrology_order_quality_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_140860_PARKSYSTEMS_20240507_AFM_STRUCTURAL_2024-05-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L126_C09_232140_20240816_S2","case_id":"C09_232140_YC_20240816_HBM_TESTER_TOO_EARLY","symbol":"232140","company_name":"와이씨","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_WAFER_TESTER_DELIVERY_START_VALUATION_RISK","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-08-16","entry_date":"2024-08-16","entry_price":16690.0,"evidence_available_at_that_date":"2024-08-16 / report date","evidence_source":"YC-hosted Hyundai report 2024-08-16: 4Q HBM tester delivery start; 2Q24 sales down YoY but operating profit turned positive. | https://yccorp.com/bbs/bbs_download.php?download=1&idx=256","stage2_evidence_fields":["HBM tester shipment expectation","2Q24 operating profit turnaround","customer capex narrative"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["delivery-start narrative already priced","2024 annual sales later still declined YoY per KIRS 2025 report"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.86,"MFE_90D_pct":1.86,"MFE_180D_pct":1.86,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-35.11,"MAE_90D_pct":-50.45,"MAE_180D_pct":-50.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-08-16","peak_price":17000.0,"drawdown_after_peak_pct":-51.35,"green_lateness_ratio":0.037,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"hbm_tester_delivery_start_too_early_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window__profile_has_2017_corporate_action_outside_window","same_entry_group_id":"C09_232140_YC_20240816_HBM_TESTER_TOO_EARLY_2024-08-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L126_C09_322310_20240327_4B","case_id":"C09_322310_AUROS_20240327_HIGH_VALUATION","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"OVERLAY_METROLOGY_HBM_WARPAGE_HIGH_VALUATION","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":35000.0,"evidence_available_at_that_date":"2024-03-27 / report date","evidence_source":"eBEST 2024-03-27: HBM inspection/metrology localization beneficiary; 2024E sales/OP growth but 2024E PER around 34x high valuation. | https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%98%A4%EB%A1%9C%EC%8A%A4%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80.pdf","stage2_evidence_fields":["HBM TSV overlay and warpage inspection exposure","localization beneficiary narrative"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit high valuation disclosure","valuation advance before quarterly confirmation","short-term price proximity to peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","profile_path":"atlas/symbol_profiles/322/322310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.0,"MFE_90D_pct":5.0,"MFE_180D_pct":5.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.71,"MAE_90D_pct":-53.43,"MAE_180D_pct":-62.34,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-03-28","peak_price":36750.0,"drawdown_after_peak_pct":-64.14,"green_lateness_ratio":0.08,"four_b_local_peak_proximity":-4.76,"four_b_full_window_peak_proximity":-4.76,"trigger_outcome_label":"high_valuation_hbm_metrology_blowoff_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_322310_AUROS_20240327_HIGH_VALUATION_2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L126_C09_064290_20240221_4B","case_id":"C09_064290_INTEKPLUS_2024_HBM_PILOT_TO_LOSS","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_MODULE_INSPECTION_PILOT_NOT_PO_BLOWOFF","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":36500.0,"evidence_available_at_that_date":"2024-02-21 08:07 KST / free release; next tradable-date entry used","evidence_source":"TheBell 2024-02-20/21: SK hynix HBM module inspection pilot/supply negotiation, possible PO; company had 2023 revenue decline and operating loss. | https://www.thebell.co.kr/front/newsview.asp?key=202402201210212520106824","stage2_evidence_fields":["HBM module inspection pilot discussion","SK hynix contact/possible PO narrative","machine vision reference"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["pilot/negotiation rather than confirmed PO","prior-year operating loss","valuation advance before conversion"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.05,"MFE_90D_pct":12.05,"MFE_180D_pct":12.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.12,"MAE_90D_pct":-42.47,"MAE_180D_pct":-72.88,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-03-07","peak_price":40900.0,"drawdown_after_peak_pct":-75.79,"green_lateness_ratio":0.165,"four_b_local_peak_proximity":-10.76,"four_b_full_window_peak_proximity":-10.76,"trigger_outcome_label":"pilot_supply_discussion_price_blowoff_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_064290_INTEKPLUS_2024_HBM_PILOT_TO_LOSS_2024-02-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L126_C09_064290_20240716_4C","case_id":"C09_064290_INTEKPLUS_2024_HBM_PILOT_TO_LOSS","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_INSPECTION_REVENUE_BRIDGE_FAILS_AND_LOSS_CONFIRMS","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-07-16","entry_date":"2024-07-16","entry_price":21600.0,"evidence_available_at_that_date":"2024-07-16 / article date","evidence_source":"DailyInvest 2024-07-16: 1Q24 operating loss remained; 2023 revenue fell 37.1% and operating profit turned to KRW 11.09bn loss; some analysts still expected HBM/2.5D upside. | https://www.dailyinvest.kr/news/articleView.html?idxno=59633","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["prior 4B not resolved by confirmed order/margin"],"stage4c_evidence_fields":["operating loss persisted","front-end demand still weak","conversion bond reset after share-price decline"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.39,"MFE_90D_pct":1.39,"MFE_180D_pct":1.39,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-31.44,"MAE_90D_pct":-57.31,"MAE_180D_pct":-63.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-07-16","peak_price":21900.0,"drawdown_after_peak_pct":-63.56,"green_lateness_ratio":0.022,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"loss_confirmation_hard_4c_after_hbm_pilot_hype","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_064290_INTEKPLUS_2024_HBM_PILOT_TO_LOSS_2024-07-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4c_confirmation_after_initial_4b","independent_evidence_weight":0.8,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_110990_DIT_20240417_BLOWOFF","trigger_id":"R2L126_C09_110990_20240417_4B","symbol":"110990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage4B-Watch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score_quality_gate"],"component_delta_explanation":"C09 shadow gate discounts advanced-equipment relative strength unless named order/revenue/margin conversion is present; explicit high valuation and pilot-only evidence move to 4B watch or 4C.","MFE_90D_pct":15.12,"MAE_90D_pct":-51.25,"score_return_alignment_label":"bad_entry_or_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_110990_DIT_20250114_ORDER_BACKED","trigger_id":"R2L126_C09_110990_20250114_S2A","symbol":"110990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":18,"margin_bridge_score":16,"revision_score":14,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":18,"margin_bridge_score":16,"revision_score":14,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score_quality_gate"],"component_delta_explanation":"C09 shadow gate discounts advanced-equipment relative strength unless named order/revenue/margin conversion is present; explicit high valuation and pilot-only evidence move to 4B watch or 4C.","MFE_90D_pct":34.28,"MAE_90D_pct":-20.34,"score_return_alignment_label":"return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_140860_PARKSYSTEMS_20240507_AFM_STRUCTURAL","trigger_id":"R2L126_C09_140860_20240507_S2A","symbol":"140860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":18,"margin_bridge_score":16,"revision_score":14,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":18,"margin_bridge_score":16,"revision_score":14,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score_quality_gate"],"component_delta_explanation":"C09 shadow gate discounts advanced-equipment relative strength unless named order/revenue/margin conversion is present; explicit high valuation and pilot-only evidence move to 4B watch or 4C.","MFE_90D_pct":27.85,"MAE_90D_pct":-3.86,"score_return_alignment_label":"return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_232140_YC_20240816_HBM_TESTER_TOO_EARLY","trigger_id":"R2L126_C09_232140_20240816_S2","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage4B-Watch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score_quality_gate"],"component_delta_explanation":"C09 shadow gate discounts advanced-equipment relative strength unless named order/revenue/margin conversion is present; explicit high valuation and pilot-only evidence move to 4B watch or 4C.","MFE_90D_pct":1.86,"MAE_90D_pct":-50.45,"score_return_alignment_label":"bad_entry_or_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_322310_AUROS_20240327_HIGH_VALUATION","trigger_id":"R2L126_C09_322310_20240327_4B","symbol":"322310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"Stage4B-Watch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score_quality_gate"],"component_delta_explanation":"C09 shadow gate discounts advanced-equipment relative strength unless named order/revenue/margin conversion is present; explicit high valuation and pilot-only evidence move to 4B watch or 4C.","MFE_90D_pct":5.0,"MAE_90D_pct":-53.43,"score_return_alignment_label":"bad_entry_or_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_064290_INTEKPLUS_2024_HBM_PILOT_TO_LOSS","trigger_id":"R2L126_C09_064290_20240221_4B","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":8,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":19,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage4B-Watch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score_quality_gate"],"component_delta_explanation":"C09 shadow gate discounts advanced-equipment relative strength unless named order/revenue/margin conversion is present; explicit high valuation and pilot-only evidence move to 4B watch or 4C.","MFE_90D_pct":12.05,"MAE_90D_pct":-42.47,"score_return_alignment_label":"bad_entry_or_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_064290_INTEKPLUS_2024_HBM_PILOT_TO_LOSS","trigger_id":"R2L126_C09_064290_20240716_4C","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":10,"accounting_trust_risk_score":5},"weighted_score_before":47,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":16,"accounting_trust_risk_score":5},"weighted_score_after":34,"stage_label_after":"Stage4C","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score_quality_gate"],"component_delta_explanation":"C09 shadow gate discounts advanced-equipment relative strength unless named order/revenue/margin conversion is present; explicit high valuation and pilot-only evidence move to 4B watch or 4C.","MFE_90D_pct":1.39,"MAE_90D_pct":-57.31,"score_return_alignment_label":"bad_entry_or_false_positive","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R2","loop":"126","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus"],"residual_error_types_found":["advanced_equipment_theme_too_early","pilot_or_delivery_start_without_margin_bridge","explicit_high_valuation_not_discounted_enough","4c_loss_confirmation_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- Manifest max date used in this MD: 2026-02-20.

### Implementation task

1. Parse the JSONL rows under Machine-Readable Rows.
2. Validate required trigger fields: MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Treat shadow_weight rows as candidate calibration evidence only.
5. For C09, test whether an archetype-specific bridge gate improves false-positive control without deleting named-order positive exceptions.
6. Do not change production scoring without batch-level validation.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 126
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|C11_BATTERY_ORDERBOOK_RERATING|C01_ORDER_BACKLOG_MARGIN_BRIDGE|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- The main execution prompt required actual Songdaiki/stock-web 1D OHLC, standalone MD output, no stock_agent code patching, no live discovery, and complete 30/90/180D MFE/MAE trigger rows.
- The No-Repeat Index used for selection reported C09 as Priority 0 with 10 rows and top covered symbols 031980, 036810, 039030, 042700, 079370, 089030.
- Stock-web manifest used: source_name FinanceData/marcap, price_adjustment_status raw_unadjusted_marcap, max_date 2026-02-20, calibration_shard_root atlas/ohlcv_tradable_by_symbol_year.
- Evidence sources were used only to anchor historical trigger availability. They are not investment recommendations.
