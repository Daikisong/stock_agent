# E2R Stock-Web v12 Residual Research — R5 / L5 / C19 Brand Retail Inventory Margin

```text
output_filename: e2r_stock_web_v12_residual_round_R5_loop_218_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
selected_round: R5
selected_loop: 218
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1
research_session: post_calibrated_sector_archetype_residual_research_v12
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection / No-Repeat check

`V12_Research_No_Repeat_Index.md` was used only as a duplicate-prevention and coverage ledger. The current corpus is no longer in raw-row shortage mode. For `C19_BRAND_RETAIL_INVENTORY_MARGIN`, the ledger state is:

```text
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
representative_rows: 217
symbol_count: 44
positive_counterexample_balance: 26 / 35
4B_4C_balance: 31 / 8
top_symbol_congestion: 383220, 020000, 081660, 036620, 111770, 298540
```

The previous immediate R5 output handled `C18_CONSUMER_EXPORT_CHANNEL_REORDER`. This run stays in L5 but changes the economic question from export-channel reorder to retail / fashion / brand inventory and gross-margin conversion. The selected cases avoid the hard duplicate key:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

## 2. Stock-Web price-source validation

```text
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_schema_columns: d,o,h,l,c,v,a,mc,s,m
zero_volume_zero_ohlc_rows: excluded by tradable shard
corporate_action_window_rule: if corporate_action_candidate_dates overlap entry~D+180 then calibration_usable=false
```

All seven usable trigger rows below have an available 180-trading-day forward window inside the Stock-Web manifest horizon. No row has a corporate-action candidate inside its entry~D+180 window.

## 3. Loop objective

```text
loop_objective:
C19에서 브랜드/리테일/패션 inventory normalization, price pass-through, cost removal, gross margin recovery, overseas/store expansion headline이
실제 inventory quality, gross-margin, operating-profit, cashflow bridge로 이어지는지 분리한다.

primary_residual_question:
브랜드 성장 또는 재고 정상화라는 단어 하나를 Stage2-Actionable/Yellow로 과승격하는가,
아니면 realized margin / inventory-assets decline / channel sell-through / working-capital bridge가 붙을 때만 Actionable을 허용하는가?
```

## 4. Selected trigger rows

| # | Symbol | Name | Trigger | Entry | Entry c | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Verdict |
|---:|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | `383220` | F&F | Stage4B | 2024-07-29 | 59,000 | 5.42 / -20.08 | 22.20 / -20.08 | 26.78 / -20.08 | current_profile_correct_4b_not_hard_4c |
| 2 | `081660` | Misto Holdings / FILA | Stage2-Actionable | 2024-05-16 | 40,350 | 2.48 / -5.70 | 11.40 / -7.31 | 11.40 / -9.79 | actionable_valid_but_green_blocked |
| 3 | `111770` | Youngone Corp | Stage2-Actionable | 2025-05-16 | 53,100 | 23.92 / -5.84 | 23.92 / -5.84 | 81.54 / -5.84 | missed_positive_repair_candidate |
| 4 | `036620` | Gamsung Corp | Stage2-Actionable | 2025-03-19 | 3,530 | 14.02 / -5.10 | 87.54 / -5.10 | 101.13 / -5.10 | profile_too_late_positive_control |
| 5 | `298540` | The Nature Holdings | Stage2 | 2024-02-21 | 15,890 | 0.76 / -11.96 | 1.32 / -27.88 | 1.32 / -43.99 | false_positive_if_promoted_above_stage2 |
| 6 | `009240` | Hanssem | Stage2 | 2024-05-13 | 66,300 | 4.07 / -21.57 | 4.07 / -23.23 | 4.07 / -32.65 | false_positive_if_actionable |
| 7 | `031430` | Shinsegae International | Stage4B | 2025-05-27 | 10,910 | 28.32 / -3.94 | 28.32 / -8.34 | 28.32 / -12.47 | 4b_watch_not_hard_4c |

Batch-level price summary:

```text
average_MFE_90D_pct: 25.54
average_MAE_90D_pct: -13.97
average_MFE_180D_pct: 36.37
average_MAE_180D_pct: -18.56
```

## 5. Case notes

### 5.1 F&F — Stage4B inventory / domestic-demand watch

F&F had direct evidence of domestic and duty-free weakness, MLB revenue decline, Discovery inventory clearing, and OP-margin pressure. This is not a clean hard-4C row because the 180D window still produced a meaningful rebound. It is a local Stage4B watch row: inventory and domestic-demand pressure existed, but the thesis had overseas / brand-offset paths.

```text
entry: 2024-07-29 close 59,000
180D_MFE_MAE: 26.78 / -20.08
classification: Stage4B, not hard 4C
```

### 5.2 Misto / FILA — inventory-assets decline and loss narrowing

FILA/Misto is a positive control for a real C19 second bridge. The evidence contains a U.S. revenue turn, FILA Group profit recovery, and inventory-assets reduction. The price path was positive but not explosive, so it protects Stage2-Actionable while keeping Yellow/Green blocked.

```text
entry: 2024-05-16 close 40,350
180D_MFE_MAE: 11.40 / -9.79
classification: Stage2-Actionable, Green blocked
```

### 5.3 Youngone — restocking and OEM margin reopen

Youngone is the strongest positive control in this batch. The evidence contains OEM restocking, the first OP growth in seven quarters, strong OEM margin, and inventory normalization at Scott. That is exactly the type of second bridge C19 needs.

```text
entry: 2025-05-16 close 53,100
180D_MFE_MAE: 81.54 / -5.84
classification: Stage2-Actionable; missed-positive repair candidate
```

### 5.4 Gamsung — brand growth with OP conversion

Gamsung is a direct brand-growth positive control. The Snowpeak apparel business showed revenue and operating-profit conversion rather than only store-count / brand-profile language. The forward price path confirms that a narrow profile-only cap would have missed a real C19 winner.

```text
entry: 2025-03-19 close 3,530
180D_MFE_MAE: 101.13 / -5.10
classification: Stage2-Actionable; Green still requires repeated inventory/cashflow evidence
```

### 5.5 The Nature Holdings — overseas expansion forecast without realized bridge

The Nature Holdings is a counterexample. Overseas expansion and portfolio diversification sounded C19-relevant, but the evidence was mostly forecast / plan language rather than realized margin or inventory-quality conversion. The 180D path was weak.

```text
entry: 2024-02-21 close 15,890
180D_MFE_MAE: 1.32 / -43.99
classification: Stage2 cap; false positive if promoted above Stage2
```

### 5.6 Hanssem — cost-cutting turnaround without durable channel demand

Hanssem had a black-turn and cost-removal evidence, but housing / moving demand remained delayed and the direct channel-demand bridge was weak. This is a classic C19 false-positive hazard: one-quarter cost removal looks like margin recovery but can still fail without end-demand durability.

```text
entry: 2024-05-13 close 66,300
180D_MFE_MAE: 4.07 / -32.65
classification: Stage2 cap; false positive if Actionable
```

### 5.7 Shinsegae International — seasonal inventory NRV watch

Shinsegae International's audit key matter highlights seasonal-fashion inventory valuation and net realizable value uncertainty. This is legitimate accounting-quality / inventory watch evidence, but the audit did not by itself confirm a hard thesis break. The forward path supports Stage4B/watch rather than sticky 4C.

```text
entry: 2025-05-27 close 10,910
180D_MFE_MAE: 28.32 / -12.47
classification: Stage4B watch, not hard 4C
```

## 6. Residual rule candidate

```text
canonical_rule_candidate:
C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1

sector_rule_candidate:
L5_BRAND_RETAIL_INVENTORY_GROSS_MARGIN_SECOND_BRIDGE_GATE_V1
```

Core residual:

```text
- C19에서 brand, overseas expansion, inventory normalization, store/channel, fashion-cycle headline만으로 Stage2-Actionable / Stage3-Yellow / Stage3-Green을 만들지 않는다.
- Stage2-Actionable에는 최소 하나의 직접 second bridge가 필요하다:
  inventory asset decline / clearance with loss narrowing,
  realized gross-margin or operating-margin conversion,
  repeat reorder or distributor sell-through,
  same-store / traffic / channel-demand recovery,
  working-capital or cashflow improvement,
  cost-ratio improvement tied to durable demand.
- forecast-only overseas expansion, licensed-brand profile, one-quarter cost cutting, product-line expansion은 Stage2 cap으로 둔다.
- seasonal-fashion inventory NRV / allowance / audit key matter는 우선 Stage4B watch로 처리한다.
  hard 4C는 repeated margin failure, accounting-trust break, inventory write-down cascade,
  weak offset quality, or liquidity stress가 같이 확인될 때만 허용한다.
- high MFE positive controls such as Youngone and Gamsung show that real second-bridge rows should reopen Stage2-Actionable.
- high MAE after forecast/profile rows should work as Yellow/Green brake and false-positive warning, not as a universal bearish label.
```

## 7. Current profile stress test

```text
current_default_profile_proxy: e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus_retested: no_global_repeat
stage3_green_not_loosened: true
price_only_blowoff_blocks_positive_stage: respected
hard_4c_thesis_break_routes_to_4c: respected
full_4b_requires_non_price_evidence: respected
```

| Profile | Interpretation | Eligible rows | Avg 90D MFE/MAE | Avg 180D MFE/MAE | Shadow result |
|---|---|---:|---:|---:|---|
| P0 current proxy | current calibrated profile | 7 | 25.54 / -13.97 | 36.37 / -18.56 | still over-promotes forecast/profile rows if second bridge not required |
| P0b no C19 second bridge | headline-sensitive | 7 | same | same | Nature/Hanssem false positives worsen |
| P1 require inventory/margin bridge for Actionable | proposed canonical gate | 7 | same | same | preserves FILA/Youngone/Gamsung, caps Nature/Hanssem |
| P2 audit inventory watch gate | proposed 4B guardrail | 7 | same | same | keeps Shinsegae as 4B, not 4C |
| P3 Green strictness unchanged | no global loosening | 7 | same | same | high-MFE winners still need repeated cashflow/inventory bridge |

## 8. Machine-readable JSONL trigger rows

```jsonl
{"schema_version":"stock_web_v12_trigger_row_v1","run_id":"R5_loop_218_C19_brand_retail_inventory_margin","row_id":"R5L218_C19_01_383220_2024-07-29_4B","selected_round":"R5","selected_loop":218,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","symbol":"383220","company_name":"F&F","trigger_type":"4B","display_stage":"Stage4B","entry_date":"2024-07-29","entry_price":59000,"evidence_family":"inventory_clearance_margin_watch","evidence_summary":"2Q24 revenue decline, OP decline, domestic/duty-free weakness, Discovery inventory clearing.","evidence_url":"https://securities.miraeasset.com/bbs/download/2130134.pdf?attachmentId=2130134","evidence_url_pending":false,"source_proxy_only":false,"source_quality":"direct_broker_pdf","price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","stock_web_manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","profile_path":"atlas/symbol_profiles/383/383220.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv","tradable_schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"entry_ohlcv":{"d":"2024-07-29","c":59000},"MFE_30D_pct":5.42,"MAE_30D_pct":-20.08,"peak_30D_date":"2024-09-03","trough_30D_date":"2024-08-05","MFE_90D_pct":22.2,"MAE_90D_pct":-20.08,"peak_90D_date":"2024-10-02","trough_90D_date":"2024-08-05","MFE_180D_pct":26.78,"MAE_180D_pct":-20.08,"peak_180D_date":"2025-02-20","trough_180D_date":"2024-08-05","forward_window_trading_days":180,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C19_383220_2024-07-29_4B","hard_duplicate_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|383220|4B|2024-07-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_verdict":"current_profile_correct_4b_not_hard_4c","score_simulation":{"profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after_shadow":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","raw_component_scores_before":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":3.0,"revision_score":3.0,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":3.0,"inventory_quality_score":3.0,"gross_margin_score":3.0},"raw_component_scores_after":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":2.5,"revision_score":2.0,"relative_strength_score":4.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":7.5,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":5.0,"channel_reorder_score":3.0,"inventory_quality_score":2.0,"gross_margin_score":2.0},"weighted_score_before":61.0,"weighted_score_after_shadow":59.0,"stage_before":"4B","stage_after_shadow":"4B","stage3_green_blocked_by_shadow_rule":true,"production_scoring_changed":false},"residual_contribution":{"rule_candidate":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","global_profile_repeated":false,"sector_specific_or_canonical_specific":true,"production_scoring_changed":false,"shadow_weight_only":true}}
{"schema_version":"stock_web_v12_trigger_row_v1","run_id":"R5_loop_218_C19_brand_retail_inventory_margin","row_id":"R5L218_C19_02_081660_2024-05-16_Stage2_Actionable","selected_round":"R5","selected_loop":218,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","symbol":"081660","company_name":"Misto Holdings / FILA","trigger_type":"Stage2-Actionable","display_stage":"Stage2-Actionable","entry_date":"2024-05-16","entry_price":40350,"evidence_family":"inventory_clearance_loss_narrowing_positive_control","evidence_summary":"FILA Group profit turn, U.S. revenue turn positive, loss narrowing, inventory-assets reduction.","evidence_url":"https://securities.miraeasset.com/bbs/download/2127021.pdf?attachmentId=2127021","evidence_url_pending":false,"source_proxy_only":false,"source_quality":"direct_broker_pdf","price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","stock_web_manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","profile_path":"atlas/symbol_profiles/081/081660.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv","tradable_schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"entry_ohlcv":{"d":"2024-05-16","c":40350},"MFE_30D_pct":2.48,"MAE_30D_pct":-5.7,"peak_30D_date":"2024-06-26","trough_30D_date":"2024-05-28","MFE_90D_pct":11.4,"MAE_90D_pct":-7.31,"peak_90D_date":"2024-09-25","trough_90D_date":"2024-08-06","MFE_180D_pct":11.4,"MAE_180D_pct":-9.79,"peak_180D_date":"2024-09-25","trough_180D_date":"2024-11-07","forward_window_trading_days":180,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C19_081660_2024-05-16_Stage2-Actionable","hard_duplicate_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|081660|Stage2-Actionable|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_verdict":"actionable_valid_but_green_blocked","score_simulation":{"profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after_shadow":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","raw_component_scores_before":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":3.0,"revision_score":3.0,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":3.0,"inventory_quality_score":3.0,"gross_margin_score":3.0},"raw_component_scores_after":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":7.0,"revision_score":6.0,"relative_strength_score":3.0,"customer_quality_score":6.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":3.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":6.0,"inventory_quality_score":7.0,"gross_margin_score":7.0},"weighted_score_before":71.0,"weighted_score_after_shadow":75.0,"stage_before":"Stage2-Actionable","stage_after_shadow":"Stage2-Actionable","stage3_green_blocked_by_shadow_rule":false,"production_scoring_changed":false},"residual_contribution":{"rule_candidate":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","global_profile_repeated":false,"sector_specific_or_canonical_specific":true,"production_scoring_changed":false,"shadow_weight_only":true}}
{"schema_version":"stock_web_v12_trigger_row_v1","run_id":"R5_loop_218_C19_brand_retail_inventory_margin","row_id":"R5L218_C19_03_111770_2025-05-16_Stage2_Actionable","selected_round":"R5","selected_loop":218,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","symbol":"111770","company_name":"Youngone Corp","trigger_type":"Stage2-Actionable","display_stage":"Stage2-Actionable","entry_date":"2025-05-16","entry_price":53100,"evidence_family":"restocking_operating_margin_reopen_positive_control","evidence_summary":"OEM restocking cycle, 1Q25 first OP growth in seven quarters, inventory normalization at Scott.","evidence_url":"https://securities.miraeasset.com/bbs/download/2136316.pdf?attachmentId=2136316","evidence_url_pending":false,"source_proxy_only":false,"source_quality":"direct_broker_pdf","price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","stock_web_manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","profile_path":"atlas/symbol_profiles/111/111770.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/111/111770/2025.csv","tradable_schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"entry_ohlcv":{"d":"2025-05-16","c":53100},"MFE_30D_pct":23.92,"MAE_30D_pct":-5.84,"peak_30D_date":"2025-06-30","trough_30D_date":"2025-05-16","MFE_90D_pct":23.92,"MAE_90D_pct":-5.84,"peak_90D_date":"2025-06-30","trough_90D_date":"2025-05-16","MFE_180D_pct":81.54,"MAE_180D_pct":-5.84,"peak_180D_date":"2025-11-27","trough_180D_date":"2025-05-16","forward_window_trading_days":180,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C19_111770_2025-05-16_Stage2-Actionable","hard_duplicate_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|111770|Stage2-Actionable|2025-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_verdict":"missed_positive_repair_candidate","score_simulation":{"profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after_shadow":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","raw_component_scores_before":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":3.0,"revision_score":3.0,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":3.0,"inventory_quality_score":3.0,"gross_margin_score":3.0},"raw_component_scores_after":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":7.0,"revision_score":6.0,"relative_strength_score":3.0,"customer_quality_score":6.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":3.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":6.0,"inventory_quality_score":7.0,"gross_margin_score":7.0},"weighted_score_before":71.0,"weighted_score_after_shadow":79.0,"stage_before":"Stage2-Actionable","stage_after_shadow":"Stage2-Actionable","stage3_green_blocked_by_shadow_rule":false,"production_scoring_changed":false},"residual_contribution":{"rule_candidate":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","global_profile_repeated":false,"sector_specific_or_canonical_specific":true,"production_scoring_changed":false,"shadow_weight_only":true}}
{"schema_version":"stock_web_v12_trigger_row_v1","run_id":"R5_loop_218_C19_brand_retail_inventory_margin","row_id":"R5L218_C19_04_036620_2025-03-19_Stage2_Actionable","selected_round":"R5","selected_loop":218,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","symbol":"036620","company_name":"Gamsung Corp","trigger_type":"Stage2-Actionable","display_stage":"Stage2-Actionable","entry_date":"2025-03-19","entry_price":3530,"evidence_family":"brand_growth_op_margin_positive_control","evidence_summary":"Snowpeak apparel sales growth and record 2024 revenue/OP with 2025 Jan-Feb continuation.","evidence_url":"https://www.mk.co.kr/en/business/11267765","evidence_url_pending":false,"source_proxy_only":false,"source_quality":"direct_news_url","price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","stock_web_manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","profile_path":"atlas/symbol_profiles/036/036620.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036620/2025.csv","tradable_schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"entry_ohlcv":{"d":"2025-03-19","c":3530},"MFE_30D_pct":14.02,"MAE_30D_pct":-5.1,"peak_30D_date":"2025-04-16","trough_30D_date":"2025-03-21","MFE_90D_pct":87.54,"MAE_90D_pct":-5.1,"peak_90D_date":"2025-07-10","trough_90D_date":"2025-03-21","MFE_180D_pct":101.13,"MAE_180D_pct":-5.1,"peak_180D_date":"2025-12-08","trough_180D_date":"2025-03-21","forward_window_trading_days":180,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C19_036620_2025-03-19_Stage2-Actionable","hard_duplicate_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|036620|Stage2-Actionable|2025-03-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_verdict":"profile_too_late_positive_control","score_simulation":{"profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after_shadow":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","raw_component_scores_before":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":3.0,"revision_score":3.0,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":3.0,"inventory_quality_score":3.0,"gross_margin_score":3.0},"raw_component_scores_after":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":7.0,"revision_score":6.0,"relative_strength_score":3.0,"customer_quality_score":6.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":3.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":6.0,"inventory_quality_score":7.0,"gross_margin_score":7.0},"weighted_score_before":71.0,"weighted_score_after_shadow":79.0,"stage_before":"Stage2-Actionable","stage_after_shadow":"Stage2-Actionable","stage3_green_blocked_by_shadow_rule":false,"production_scoring_changed":false},"residual_contribution":{"rule_candidate":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","global_profile_repeated":false,"sector_specific_or_canonical_specific":true,"production_scoring_changed":false,"shadow_weight_only":true}}
{"schema_version":"stock_web_v12_trigger_row_v1","run_id":"R5_loop_218_C19_brand_retail_inventory_margin","row_id":"R5L218_C19_05_298540_2024-02-21_Stage2","selected_round":"R5","selected_loop":218,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","symbol":"298540","company_name":"The Nature Holdings","trigger_type":"Stage2","display_stage":"Stage2","entry_date":"2024-02-21","entry_price":15890,"evidence_family":"overseas_plan_without_realized_margin_counterexample","evidence_summary":"Overseas expansion and portfolio-diversification forecast without realized inventory/margin bridge.","evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1708470258593.pdf","evidence_url_pending":false,"source_proxy_only":true,"source_quality":"broker_pdf_forecast","price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","stock_web_manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","profile_path":"atlas/symbol_profiles/298/298540.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv","tradable_schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"entry_ohlcv":{"d":"2024-02-21","c":15890},"MFE_30D_pct":0.76,"MAE_30D_pct":-11.96,"peak_30D_date":"2024-02-22","trough_30D_date":"2024-03-07","MFE_90D_pct":1.32,"MAE_90D_pct":-27.88,"peak_90D_date":"2024-06-03","trough_90D_date":"2024-07-03","MFE_180D_pct":1.32,"MAE_180D_pct":-43.99,"peak_180D_date":"2024-06-03","trough_180D_date":"2024-11-15","forward_window_trading_days":180,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C19_298540_2024-02-21_Stage2","hard_duplicate_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|298540|Stage2|2024-02-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_verdict":"false_positive_if_promoted_above_stage2","score_simulation":{"profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after_shadow":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","raw_component_scores_before":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":3.0,"revision_score":3.0,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":3.0,"inventory_quality_score":3.0,"gross_margin_score":3.0},"raw_component_scores_after":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":4.0,"revision_score":3.5,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.5,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":4.0,"inventory_quality_score":3.0,"gross_margin_score":4.0},"weighted_score_before":66.0,"weighted_score_after_shadow":66.0,"stage_before":"Stage2","stage_after_shadow":"Stage2","stage3_green_blocked_by_shadow_rule":true,"production_scoring_changed":false},"residual_contribution":{"rule_candidate":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","global_profile_repeated":false,"sector_specific_or_canonical_specific":true,"production_scoring_changed":false,"shadow_weight_only":true}}
{"schema_version":"stock_web_v12_trigger_row_v1","run_id":"R5_loop_218_C19_brand_retail_inventory_margin","row_id":"R5L218_C19_06_009240_2024-05-13_Stage2","selected_round":"R5","selected_loop":218,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","symbol":"009240","company_name":"Hanssem","trigger_type":"Stage2","display_stage":"Stage2","entry_date":"2024-05-13","entry_price":66300,"evidence_family":"cost_cut_turnaround_without_channel_demand_counterexample","evidence_summary":"1Q24 black-turn and cost removal but housing/moving demand recovery still delayed.","evidence_url":"https://securities.miraeasset.com/bbs/download/2126911.pdf?attachmentId=2126911","evidence_url_pending":false,"source_proxy_only":false,"source_quality":"direct_broker_pdf","price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","stock_web_manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","profile_path":"atlas/symbol_profiles/009/009240.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009240/2024.csv","tradable_schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"entry_ohlcv":{"d":"2024-05-13","c":66300},"MFE_30D_pct":4.07,"MAE_30D_pct":-21.57,"peak_30D_date":"2024-05-16","trough_30D_date":"2024-06-14","MFE_90D_pct":4.07,"MAE_90D_pct":-23.23,"peak_90D_date":"2024-05-16","trough_90D_date":"2024-08-12","MFE_180D_pct":4.07,"MAE_180D_pct":-32.65,"peak_180D_date":"2024-05-16","trough_180D_date":"2025-02-10","forward_window_trading_days":180,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C19_009240_2024-05-13_Stage2","hard_duplicate_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|009240|Stage2|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_verdict":"false_positive_if_actionable","score_simulation":{"profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after_shadow":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","raw_component_scores_before":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":3.0,"revision_score":3.0,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":3.0,"inventory_quality_score":3.0,"gross_margin_score":3.0},"raw_component_scores_after":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":4.0,"revision_score":3.5,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.5,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":4.0,"inventory_quality_score":3.0,"gross_margin_score":4.0},"weighted_score_before":66.0,"weighted_score_after_shadow":66.0,"stage_before":"Stage2","stage_after_shadow":"Stage2","stage3_green_blocked_by_shadow_rule":true,"production_scoring_changed":false},"residual_contribution":{"rule_candidate":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","global_profile_repeated":false,"sector_specific_or_canonical_specific":true,"production_scoring_changed":false,"shadow_weight_only":true}}
{"schema_version":"stock_web_v12_trigger_row_v1","run_id":"R5_loop_218_C19_brand_retail_inventory_margin","row_id":"R5L218_C19_07_031430_2025-05-27_4B","selected_round":"R5","selected_loop":218,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","symbol":"031430","company_name":"Shinsegae International","trigger_type":"4B","display_stage":"Stage4B","entry_date":"2025-05-27","entry_price":10910,"evidence_family":"inventory_nrv_accounting_quality_4b_watch","evidence_summary":"Audit key matter: seasonal-fashion inventory net realizable value uncertainty and allowance.","evidence_url":"https://img.sikorea.co.kr/files/upload2/noticePdf/202505/SI%202024%20Auditor_s%20Report%20%5BEN%5D_1748329084313.pdf","evidence_url_pending":false,"source_proxy_only":false,"source_quality":"issuer_audit_pdf","price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","stock_web_manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","profile_path":"atlas/symbol_profiles/031/031430.json","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031430/2025.csv","tradable_schema_columns":["d","o","h","l","c","v","a","mc","s","m"],"entry_ohlcv":{"d":"2025-05-27","c":10910},"MFE_30D_pct":28.32,"MAE_30D_pct":-3.94,"peak_30D_date":"2025-06-19","trough_30D_date":"2025-06-02","MFE_90D_pct":28.32,"MAE_90D_pct":-8.34,"peak_90D_date":"2025-06-19","trough_90D_date":"2025-09-03","MFE_180D_pct":28.32,"MAE_180D_pct":-12.47,"peak_180D_date":"2025-06-19","trough_180D_date":"2025-10-22","forward_window_trading_days":180,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C19_031430_2025-05-27_4B","hard_duplicate_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|031430|4B|2025-05-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"case_verdict":"4b_watch_not_hard_4c","score_simulation":{"profile_before":"e2r_2_1_stock_web_calibrated_proxy","profile_after_shadow":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","raw_component_scores_before":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":3.0,"revision_score":3.0,"relative_strength_score":3.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":4.0,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":1.0,"channel_reorder_score":3.0,"inventory_quality_score":3.0,"gross_margin_score":3.0},"raw_component_scores_after":{"contract_score":2.0,"backlog_visibility_score":2.0,"margin_bridge_score":2.5,"revision_score":2.0,"relative_strength_score":4.0,"customer_quality_score":3.0,"policy_or_regulatory_score":0.0,"valuation_repricing_score":3.0,"execution_risk_score":7.5,"legal_or_contract_risk_score":0.0,"dilution_cb_risk_score":0.0,"accounting_trust_risk_score":5.0,"channel_reorder_score":3.0,"inventory_quality_score":2.0,"gross_margin_score":2.0},"weighted_score_before":61.0,"weighted_score_after_shadow":59.0,"stage_before":"4B","stage_after_shadow":"4B","stage3_green_blocked_by_shadow_rule":true,"production_scoring_changed":false},"residual_contribution":{"rule_candidate":"C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1","global_profile_repeated":false,"sector_specific_or_canonical_specific":true,"production_scoring_changed":false,"shadow_weight_only":true}}
```

## 9. Aggregate / residual contribution rows

```json
{
  "schema_version": "stock_web_v12_aggregate_row_v1",
  "run_id": "R5_loop_218_C19_brand_retail_inventory_margin",
  "selected_round": "R5",
  "selected_loop": 218,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1",
  "new_independent_case_count": 7,
  "new_independent_trigger_count": 7,
  "unique_symbol_count": 7,
  "stage2_count": 2,
  "stage2_actionable_count": 3,
  "stage4b_count": 2,
  "stage4c_count": 0,
  "positive_case_count": 3,
  "counterexample_or_guardrail_count": 4,
  "source_proxy_only_count": 1,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "corporate_action_contaminated_180D_count": 0,
  "insufficient_forward_window_180D_count": 0,
  "average_MFE_90D_pct": 25.54,
  "average_MAE_90D_pct": -13.97,
  "average_MFE_180D_pct": 36.37,
  "average_MAE_180D_pct": -18.56,
  "rule_candidate": "C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1",
  "sector_rule_candidate": "L5_BRAND_RETAIL_INVENTORY_GROSS_MARGIN_SECOND_BRIDGE_GATE_V1",
  "loop_contribution_label": "C19_brand_retail_inventory_second_bridge_quality_repair",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "do_not_propose_new_weight_delta": false
}
```

## 10. Batch Ingest Self-Audit

```text
batch_ingest_self_audit:
  output_filename_pattern_valid: true
  selected_round_large_sector_pair_valid: true
  canonical_archetype_present_in_all_rows: true
  fine_archetype_bound_to_canonical: true
  hard_duplicate_key_present_in_all_rows: true
  jsonl_trigger_rows_present: true
  all_trigger_rows_have_entry_date: true
  all_trigger_rows_have_entry_price: true
  all_trigger_rows_have_30_90_180_mfe_mae: true
  all_trigger_rows_have_price_shard_path: true
  all_trigger_rows_have_profile_path: true
  all_trigger_rows_have_price_adjustment_status: true
  source_proxy_only_count: 1
  evidence_url_pending_count: 0
  missing_required_mfe_mae_count: 0
  missing_entry_price_count: 0
  missing_actual_entry_ohlcv_count: 0
  corporate_action_contaminated_180D_count: 0
  insufficient_forward_window_180D_count: 0
  production_scoring_changed: false
  shadow_weight_only: true
  ready_for_batch_ingest: true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.

When a later coding-agent session ingests this MD:
1. Parse the JSONL trigger rows and aggregate row.
2. Validate the hard duplicate key:
   C19_BRAND_RETAIL_INVENTORY_MARGIN + symbol + trigger_type + entry_date.
3. Confirm each Stock-Web price shard and profile path.
4. Add this run to v12 calibration only if the listed price fields remain schema-valid.
5. Treat C19_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1 as a shadow-rule candidate, not a production patch.
6. Compare it against existing L5 / C18 / C20 consumer rules before promotion.
7. Do not loosen Stage3-Green. Require repeated inventory, margin, channel, cashflow, or working-capital evidence before Green.
```

## 12. Next Research State

```text
completed_round: R5
completed_loop: 218
completed_large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
completed_canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
completed_fine_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN_SECOND_BRIDGE_GATE_V1
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C19_BRAND_RETAIL_INVENTORY_MARGIN_INVENTORY_NRV_DIRECT_URL_REPAIR
- C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_CHANNEL_REPEATABILITY_REPAIR
- C18_CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_REORDER_DIRECT_ROW_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_CONSUMER_EXPORT_HOLDOUT_REFRESH
```
