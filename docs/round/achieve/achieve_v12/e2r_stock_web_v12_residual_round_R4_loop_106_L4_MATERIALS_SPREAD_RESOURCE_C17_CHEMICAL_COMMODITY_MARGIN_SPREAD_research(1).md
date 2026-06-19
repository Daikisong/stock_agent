# E2R v12 Residual Research — R4 loop 106 — L4_MATERIALS_SPREAD_RESOURCE — C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

```text
completed_round = R4
completed_loop = 106
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C17 chemical commodity margin spread: source/proxy repair, 4B/4C split, and spread-to-margin conversion gate
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Research mode and hard gates

This standalone Markdown file follows the v12 post-calibrated historical trigger-level residual research mode. It does not perform live candidate discovery, stock_agent code inspection, production patching, auto-trading, brokerage/API work, or price-route discovery. The only output of this run is this research MD.

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
must_use_actual_stock_web_1D_OHLC = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
trigger_rows_missing_required_price_fields_are_forbidden = true
```

## 1. Selection rationale

The latest No-Repeat ledger shows that the corpus has moved past simple row-count filling and into quality repair: URL/proxy quality, complete MFE/MAE preservation, 4B/4C balance, and current-profile residual error mining. This run therefore does not pick C17 because it is underfilled; it picks C17 because chemical spread cycles still need a sharper split between:

1. real product-spread-to-margin conversion,
2. temporary spread headline overcredit,
3. true company-specific 4C margin/cash break,
4. false hard-4C overblocking from generic petrochemical downcycle commentary.

Recent current-session outputs were C05, C01, C13, C15, C10, C02, C16, and R13 high-MAE. This run avoids those exact canonical paths and uses C17 as the next R4/L4 residual quality repair.

```text
selected_round = R4
selected_loop = 106
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE
loop_objective = sector_specific_rule_discovery; canonical_archetype_rule_candidate; positive_case_balance; hard_4c_transition_timing_test; source_proxy_quality_repair; complete_30_90_180_MFE_MAE
```

## 2. Price source validation

Stock-Web manifest and schema assumptions used in this file:

```text
source_name = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
source_repo_url = https://github.com/Songdaiki/stock-web
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
stock_web_manifest_max_date = 2026-02-20
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

MFE/MAE definitions used for every trigger row:

```text
MFE_ND_pct = (max(high from entry_date through N tradable rows) / entry_close - 1) * 100
MAE_ND_pct = (min(low from entry_date through N tradable rows) / entry_close - 1) * 100
```

## 3. Novelty and no-repeat audit

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_key_reused = false
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 7
calibration_usable_case_count = 7
calibration_usable_trigger_count = 7
positive_case_count = 3
counterexample_count = 4
stage4b_case_count = 2
stage4c_case_count = 2
source_proxy_only_count = 3
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
current_profile_error_count = 4
```

Novelty is not claimed from the canonical ID itself. C17 is already populated. The novelty is in this run's fine-level split: named product spread vs company official margin conversion vs generic sector downcycle overblocking. The repeated large-cap chemical symbols are used only where they create new trigger-family separation or URL-quality repair.

## 4. Case table

|case_id|symbol|company|trigger|entry|role|MFE180|MAE180|source_proxy_only|
|---|---|---|---|---|---|---|---|---|
|C17_011780_20210323_NB_LATEX_SPREAD_RERATING_LOCAL_4B|011780|금호석유화학|Stage2-Actionable|2021-03-23|positive_with_local_4b|28.11|-34.12|true|
|C17_298020_20210504_SPANDEX_MARGIN_SUPERCYCLE_LOCAL_4B|298020|효성티앤씨|Stage3-Yellow|2021-05-04|positive_with_local_4b|33.38|-34.35|false|
|C17_011780_20240130_DEPRESSED_MARKET_FALSE_4C|011780|금호석유화학|Stage4B|2024-01-30|counterexample_false_hard_4c|29.56|-10.63|true|
|C17_011170_20240208_LOTTECHEM_2023_LOSS_TRUE_4C|011170|롯데케미칼|Stage4C|2024-02-08|counterexample_true_4c|3.41|-43.21|false|
|C17_011170_20241108_LOTTECHEM_Q3_LOSS_TRUE_4C|011170|롯데케미칼|Stage4C|2024-11-08|counterexample_true_4c|11.83|-41.07|false|
|C17_004000_20250514_LOTTEFINE_CHLORINE_PRICE_VOLUME_RECOVERY|004000|롯데정밀화학|Stage2-Actionable|2025-05-14|positive_structural|40.50|-3.17|false|
|C17_006650_20250508_SECTOR_DOWNCYCLE_FALSE_4C_OVERBLOCK|006650|대한유화|Stage4B|2025-05-08|counterexample_false_blanket_4c|93.45|-13.43|true|

## 5. Actual Stock-Web price-path table

|case_id|symbol|entry_date|entry_close|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|trough_date|trough_price|drawdown_after_peak_pct|outcome|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C17_011780_20210323_NB_LATEX_SPREAD_RERATING_LOCAL_4B|011780|2021-03-23|233000.00|25.54|-6.44|28.11|-13.09|28.11|-34.12|2021-05-06|298500.00|2021-11-29|153500.00|-48.58|positive_right_tail_then_4b_drawdown|
|C17_298020_20210504_SPANDEX_MARGIN_SUPERCYCLE_LOCAL_4B|298020|2021-05-04|722000.00|13.43|-4.29|33.38|-4.29|33.38|-34.35|2021-07-16|963000.00|2022-01-21|474000.00|-50.78|positive_90d_then_4b|
|C17_011780_20240130_DEPRESSED_MARKET_FALSE_4C|011780|2024-01-30|128900.00|27.15|-6.52|27.15|-10.63|29.56|-10.63|2024-07-15|167000.00|2024-04-19|115200.00|-27.72|false_4c_overblock_positive_mfe|
|C17_011170_20240208_LOTTECHEM_2023_LOSS_TRUE_4C|011170|2024-02-08|134700.00|3.41|-13.29|3.41|-28.66|3.41|-43.21|2024-02-19|139300.00|2024-09-09|76500.00|-45.08|true_negative_4c_deep_mae|
|C17_011170_20241108_LOTTECHEM_Q3_LOSS_TRUE_4C|011170|2024-11-08|87900.00|11.83|-35.84|11.83|-41.07|11.83|-41.07|2024-11-08|98300.00|2025-02-10|51800.00|-47.30|true_negative_4c_immediate_peak_deep_mae|
|C17_004000_20250514_LOTTEFINE_CHLORINE_PRICE_VOLUME_RECOVERY|004000|2025-05-14|36300.00|10.61|-3.17|38.57|-3.17|40.50|-3.17|2026-02-04|51000.00|2025-05-23|35150.00|-4.22|positive_clean_margin_conversion|
|C17_006650_20250508_SECTOR_DOWNCYCLE_FALSE_4C_OVERBLOCK|006650|2025-05-08|88600.00|2.71|-13.43|45.03|-13.43|93.45|-13.43|2026-01-26|171400.00|2025-05-26|76700.00|-9.98|false_4c_overblock_large_mfe|

## 6. Case notes and score-return alignment

### 6.1 금호석유화학 2021 — NB latex/SBR/BPA spread rerating but local 4B required

KB Securities' March 2021 report gave named product spread evidence: NB-latex, SBR, and BPA spread bands. Entry on 2021-03-23 produced 30D MFE +25.54% and 90D MFE +28.11%. However 180D MAE reached -34.12% and drawdown after the May 2021 peak was -48.58%. The correct C17 behavior is Stage2-Actionable / Stage3-Yellow entry, then local 4B once spread peak or price exhaustion appears. A Green state that ignores spread-cycle decay is too permissive.

### 6.2 효성티앤씨 2021 — spandex supercycle right-tail with post-peak protection failure

The Hyosung TNC 1Q 2021 presentation and eBest report supplied company/segment evidence around spandex ASP and margin. The price path produced 90D MFE +33.38% with only -4.29% MAE, but the 180D MAE expanded to -34.35% and drawdown after the July 2021 peak reached -50.78%. This is a winner at entry and an exit/4B problem later.

### 6.3 금호석유화학 2024 — earnings miss was 4B, not hard 4C

Mirae Asset's January 2024 report described weak synthetic resin and phenol derivatives, one-off expenses, and depressed conditions. The Stock-Web path still delivered 180D MFE +29.56% with MAE -10.63%. That means a single weak quarter can cap positive scoring, but it should not automatically route to hard 4C unless company-specific sustained margin/cash break is confirmed.

### 6.4 롯데케미칼 2024 full-year and Q3 — true 4C when company-level loss and spread break are explicit

Lotte Chemical's 2023 release disclosed consolidated operating loss and basic-materials spread weakness. Entry on 2024-02-08 produced only 180D MFE +3.41% and MAE -43.21%. The Q3 2024 release added delayed demand, lower product spreads, maintenance, and shipping costs; entry on 2024-11-08 produced 180D MFE +11.83% but MAE -41.07%. These are true C17 hard-4C rows because company-level loss and spread/cost damage were explicit.

### 6.5 롯데정밀화학 2025 — clean positive margin conversion

Lotte Chemical's Q1 2025 release provided a direct Lotte Fine Chemical segment bridge: sales, operating profit, price increases, higher sales volumes, and FX. Entry on 2025-05-14 produced 180D MFE +40.50% with MAE only -3.17%. This is the clean C17 positive: named product/segment improvement plus actual margin conversion.

### 6.6 대한유화 2025 — sector downcycle alone is not hard 4C

S&P Global Ratings' May 2025 sector note supported a Korean petrochemical downcycle stress view. But the row is intentionally source-proxy-only and not company-specific. Entry on 2025-05-08 produced 180D MFE +93.45% with MAE -13.43%. The lesson is not that the sector note was wrong; it is that C17 hard 4C should require symbol-level operating-loss/spread/cash break. Generic downcycle remains 4B/watch until company-specific evidence arrives.

## 7. Residual error family

```text
residual_error_family_1 = positive_stage_overcredit_from_product_spread_headline_without_company_margin_conversion
residual_error_family_2 = green_exit_late_after_spread_peak_in_spread_supercycle_winners
residual_error_family_3 = hard_4c_too_early_from_single_quarter_earnings_miss
residual_error_family_4 = hard_4c_too_early_from_generic_sector_downcycle_without_company_specific_loss_bridge
residual_error_family_5 = true_4c_when_company_level_operating_loss_and_product_spread_break_are_explicit
```

## 8. Shadow rule candidate

```text
new_axis_proposed = C17_CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE
shadow_weight_only = true
production_scoring_changed = false
```

### 8.1 Proposed C17 positive-stage gate

For C17, allow Stage2-Actionable only when at least two of the following are present as of trigger date:

```text
1. named product spread or ASP/cost spread evidence, not generic commodity optimism
2. company-level product/segment exposure to that spread
3. company official or high-quality source showing operating-profit/margin conversion
4. volume/demand/sales bridge supporting the spread
5. clean working-capital/balance-sheet quality, or no explicit deterioration
```

### 8.2 Proposed C17 4B/4C split

```text
4B/watch:
- single weak quarter
- sector downcycle commentary
- product spread deterioration without company-specific sustained loss
- price peak after verified spread winner

4C/hard break:
- company-level operating loss plus lower product spread / demand break
- sustained business-unit loss with financial soundness actions
- cash/working-capital damage directly tied to commodity spread collapse
- repeated quarter confirmation or explicit thesis break
```

## 9. Raw component score breakdown proxy

|row_type|case_id|symbol|trigger_type|baseline_total_proxy|post_shadow_total_proxy|revision_score_proxy|evidence_confidence_proxy|risk_penalty_proxy|guardrail_verdict|production_scoring_changed|shadow_weight_only|
|---|---|---|---|---|---|---|---|---|---|---|---|
|score_simulation|C17_011780_20210323_NB_LATEX_SPREAD_RERATING_LOCAL_4B|011780|Stage2-Actionable|78|79|55|45|12|pass_with_4b_local_watch|false|true|
|score_simulation|C17_298020_20210504_SPANDEX_MARGIN_SUPERCYCLE_LOCAL_4B|298020|Stage3-Yellow|78|82|55|70|12|pass_with_4b_local_watch|false|true|
|score_simulation|C17_011780_20240130_DEPRESSED_MARKET_FALSE_4C|011780|Stage4B|70|58|25|45|18|4b_watch_cap_until_company_specific_margin_bridge|false|true|
|score_simulation|C17_011170_20240208_LOTTECHEM_2023_LOSS_TRUE_4C|011170|Stage4C|61|38|25|70|18|hard_4c_blocks_positive_stage|false|true|
|score_simulation|C17_011170_20241108_LOTTECHEM_Q3_LOSS_TRUE_4C|011170|Stage4C|61|38|25|70|18|hard_4c_blocks_positive_stage|false|true|
|score_simulation|C17_004000_20250514_LOTTEFINE_CHLORINE_PRICE_VOLUME_RECOVERY|004000|Stage2-Actionable|78|82|55|70|5|pass|false|true|
|score_simulation|C17_006650_20250508_SECTOR_DOWNCYCLE_FALSE_4C_OVERBLOCK|006650|Stage4B|70|58|25|45|18|4b_watch_cap_until_company_specific_margin_bridge|false|true|

## 10. Machine-readable JSONL rows

```jsonl
{"row_type":"trigger","trigger_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|Stage2-Actionable|2021-03-23","case_id":"C17_011780_20210323_NB_LATEX_SPREAD_RERATING_LOCAL_4B","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":106,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage2-Actionable","trigger_date":"2021-03-23","evidence_available_at_that_date":true,"evidence_source":"KB Securities, Kumho Petrochemical report, 2021-03-22; NB-latex/SBR/BPA spread estimates and bull/bear spread bands.","evidence_url":"https://rdata.kbsec.com/pdf_data/20210322145204253E.pdf","source_proxy_only":true,"evidence_url_pending":false,"stage2_evidence_fields":["named_product_spread","visible_price_cost_spread","company_product_exposure"],"stage3_evidence_fields":["multi_product_spread_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["post_peak_spread_reversal_risk","full_window_drawdown_after_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-03-23","entry_price":233000.0,"entry_ohlc":{"d":"2021-03-23","o":242500.0,"h":247000.0,"l":231500.0,"c":233000.0,"v":430096,"mc":7098972003000.0,"m":"KOSPI"},"MFE_30D_pct":25.54,"MFE_90D_pct":28.11,"MFE_180D_pct":28.11,"MAE_30D_pct":-6.44,"MAE_90D_pct":-13.09,"MAE_180D_pct":-34.12,"peak_date":"2021-05-06","peak_price":298500.0,"peak_ohlc":{"d":"2021-05-06","o":272500.0,"h":298500.0,"l":269500.0,"c":296000.0,"v":2085191,"mc":9018436536000.0,"m":"KOSPI"},"trough_date":"2021-11-29","trough_price":153500.0,"trough_ohlc":{"d":"2021-11-29","o":153500.0,"h":164500.0,"l":153500.0,"c":157000.0,"v":247983,"mc":4783427487000.0,"m":"KOSPI"},"drawdown_after_peak_pct":-48.58,"below_entry_30D":true,"below_entry_90D":true,"below_entry_180D":true,"green_lateness_ratio":null,"four_b_local_vs_full_window_proximity":"local_peak_required_after_spread_peak","four_c_protection_label":"not_4c","trigger_outcome_label":"positive_right_tail_then_4b_drawdown","current_profile_verdict":"partial_error_green_duration_too_long_without_local_4b","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_profile_or_pre_2001_2010_2023_non_overlap","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|2021-03-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298020|Stage3-Yellow|2021-05-04","case_id":"C17_298020_20210504_SPANDEX_MARGIN_SUPERCYCLE_LOCAL_4B","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":106,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage3-Yellow","trigger_date":"2021-05-04","evidence_available_at_that_date":true,"evidence_source":"Hyosung TNC 1Q 2021 business performance presentation and eBest report; spandex OPM/ASP and tight-supply margin bridge.","evidence_url":"https://www.hyosungtnc.com/download/273 ; https://msg.ebestsec.co.kr/eum/20210503_31545_81.pdf","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":["segment_margin_visible","ASP_up","tight_supply"],"stage3_evidence_fields":["company_ir_performance","large_segment_opm","earnings_visibility"],"stage4b_evidence_fields":["commodity_margin_peak_risk","capacity_response_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv; atlas/ohlcv_tradable_by_symbol_year/298/298020/2022.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-04","entry_price":722000.0,"entry_ohlc":{"d":"2021-05-04","o":741000.0,"h":752000.0,"l":706000.0,"c":722000.0,"v":103501,"mc":3124586404000.0,"m":"KOSPI"},"MFE_30D_pct":13.43,"MFE_90D_pct":33.38,"MFE_180D_pct":33.38,"MAE_30D_pct":-4.29,"MAE_90D_pct":-4.29,"MAE_180D_pct":-34.35,"peak_date":"2021-07-16","peak_price":963000.0,"peak_ohlc":{"d":"2021-07-16","o":945000.0,"h":963000.0,"l":875000.0,"c":881000.0,"v":142525,"mc":3812687842000.0,"m":"KOSPI"},"trough_date":"2022-01-21","trough_price":474000.0,"trough_ohlc":{"d":"2022-01-21","o":490000.0,"h":492000.0,"l":474000.0,"c":475500.0,"v":57089,"mc":2057812791000.0,"m":"KOSPI"},"drawdown_after_peak_pct":-50.78,"below_entry_30D":true,"below_entry_90D":true,"below_entry_180D":true,"green_lateness_ratio":null,"four_b_local_vs_full_window_proximity":"local_peak_required_after_spread_peak","four_c_protection_label":"not_4c","trigger_outcome_label":"positive_90d_then_4b","current_profile_verdict":"partial_error_green_late_exit_without_spread_peak_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_profile_or_pre_2001_2010_2023_non_overlap","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298020|2021-05-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|Stage4B|2024-01-30","case_id":"C17_011780_20240130_DEPRESSED_MARKET_FALSE_4C","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":106,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage4B","trigger_date":"2024-01-30","evidence_available_at_that_date":true,"evidence_source":"Mirae Asset Securities, Kumho Petrochemical report, 2024-01-30; 4Q23 OP W36.6bn, -57% QoQ, weak resin/phenol and one-off expenses.","evidence_url":"https://securities.miraeasset.com/bbs/download/2121421.pdf?attachmentId=2121421","source_proxy_only":true,"evidence_url_pending":false,"stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["earnings_miss","depressed_market_commentary","weak_spread_segment"],"stage4c_evidence_fields":["not_confirmed_company_specific_thesis_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-30","entry_price":128900.0,"entry_ohlc":{"d":"2024-01-30","o":127900.0,"h":136500.0,"l":127800.0,"c":128900.0,"v":465355,"mc":3679795823100.0,"m":"KOSPI"},"MFE_30D_pct":27.15,"MFE_90D_pct":27.15,"MFE_180D_pct":29.56,"MAE_30D_pct":-6.52,"MAE_90D_pct":-10.63,"MAE_180D_pct":-10.63,"peak_date":"2024-07-15","peak_price":167000.0,"peak_ohlc":{"d":"2024-07-15","o":166100.0,"h":167000.0,"l":162200.0,"c":164300.0,"v":83690,"mc":4546621159700.0,"m":"KOSPI"},"trough_date":"2024-04-19","trough_price":115200.0,"trough_ohlc":{"d":"2024-04-19","o":117000.0,"h":118400.0,"l":115200.0,"c":117100.0,"v":68394,"mc":3240470710900.0,"m":"KOSPI"},"drawdown_after_peak_pct":-27.72,"below_entry_30D":true,"below_entry_90D":true,"below_entry_180D":true,"green_lateness_ratio":null,"four_b_local_vs_full_window_proximity":"not_applicable_or_4c","four_c_protection_label":"hard_4c_too_early","trigger_outcome_label":"false_4c_overblock_positive_mfe","current_profile_verdict":"error_if_routed_to_hard_4c_from_single_earnings_miss","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_profile_or_pre_2001_2010_2023_non_overlap","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|Stage4C|2024-02-08","case_id":"C17_011170_20240208_LOTTECHEM_2023_LOSS_TRUE_4C","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":106,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage4C","trigger_date":"2024-02-08","evidence_available_at_that_date":true,"evidence_source":"Lotte Chemical official 2023 business performance release; consolidated revenue KRW 19.9491tn, operating loss KRW 333.2bn, basic materials loss from reduced spread.","evidence_url":"https://www.lottechem.com/en/media/news/883/view.do","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["company_loss","weak_market_conditions","reduced_spread"],"stage4c_evidence_fields":["operating_loss","basic_materials_spread_break","demand_recovery_uncertainty"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":134700.0,"entry_ohlc":{"d":"2024-02-08","o":136800.0,"h":136800.0,"l":132800.0,"c":134700.0,"v":128897,"mc":5761848939300.0,"m":"KOSPI"},"MFE_30D_pct":3.41,"MFE_90D_pct":3.41,"MFE_180D_pct":3.41,"MAE_30D_pct":-13.29,"MAE_90D_pct":-28.66,"MAE_180D_pct":-43.21,"peak_date":"2024-02-19","peak_price":139300.0,"peak_ohlc":{"d":"2024-02-19","o":136900.0,"h":139300.0,"l":136500.0,"c":138400.0,"v":95273,"mc":5920117989600.0,"m":"KOSPI"},"trough_date":"2024-09-09","trough_price":76500.0,"trough_ohlc":{"d":"2024-09-09","o":78000.0,"h":79200.0,"l":76500.0,"c":79000.0,"v":89949,"mc":3379258101000.0,"m":"KOSPI"},"drawdown_after_peak_pct":-45.08,"below_entry_30D":true,"below_entry_90D":true,"below_entry_180D":true,"green_lateness_ratio":null,"four_b_local_vs_full_window_proximity":"not_applicable_or_4c","four_c_protection_label":"hard_4c_true","trigger_outcome_label":"true_negative_4c_deep_mae","current_profile_verdict":"correct_4c_or_stage2_block","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_profile_or_pre_2001_2010_2023_non_overlap","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|Stage4C|2024-11-08","case_id":"C17_011170_20241108_LOTTECHEM_Q3_LOSS_TRUE_4C","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":106,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage4C","trigger_date":"2024-11-08","evidence_available_at_that_date":true,"evidence_source":"Lotte Chemical official Q3 2024 release; operating loss KRW 413.6bn, lower product spreads, delayed demand, maintenance/shipping costs.","evidence_url":"https://www.lottechem.com/en/media/news/1014/view.do","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["lower_product_spreads","delayed_demand","shipping_costs"],"stage4c_evidence_fields":["large_quarterly_operating_loss","business_unit_loss","financial_soundness_actions"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv; atlas/ohlcv_tradable_by_symbol_year/011/011170/2025.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-08","entry_price":87900.0,"entry_ohlc":{"d":"2024-11-08","o":94900.0,"h":98300.0,"l":87600.0,"c":87900.0,"v":254679,"mc":3759959330100.0,"m":"KOSPI"},"MFE_30D_pct":11.83,"MFE_90D_pct":11.83,"MFE_180D_pct":11.83,"MAE_30D_pct":-35.84,"MAE_90D_pct":-41.07,"MAE_180D_pct":-41.07,"peak_date":"2024-11-08","peak_price":98300.0,"peak_ohlc":{"d":"2024-11-08","o":94900.0,"h":98300.0,"l":87600.0,"c":87900.0,"v":254679,"mc":3759959330100.0,"m":"KOSPI"},"trough_date":"2025-02-10","trough_price":51800.0,"trough_ohlc":{"d":"2025-02-10","o":54000.0,"h":54500.0,"l":51800.0,"c":53600.0,"v":169790,"mc":2292762458400.0,"m":"KOSPI"},"drawdown_after_peak_pct":-47.3,"below_entry_30D":true,"below_entry_90D":true,"below_entry_180D":true,"green_lateness_ratio":null,"four_b_local_vs_full_window_proximity":"not_applicable_or_4c","four_c_protection_label":"hard_4c_true","trigger_outcome_label":"true_negative_4c_immediate_peak_deep_mae","current_profile_verdict":"correct_4c_or_stage2_block","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_profile_or_pre_2001_2010_2023_non_overlap","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|2024-11-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|004000|Stage2-Actionable|2025-05-14","case_id":"C17_004000_20250514_LOTTEFINE_CHLORINE_PRICE_VOLUME_RECOVERY","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":106,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage2-Actionable","trigger_date":"2025-05-14","evidence_available_at_that_date":true,"evidence_source":"Lotte Chemical official Q1 2025 release; Lotte Fine Chemical sales KRW 445.6bn and operating profit KRW 18.8bn, improved from price increases, sales volume and FX.","evidence_url":"https://www.lottechem.com/en/media/news/1064/view.do","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":["price_increase","sales_volume_growth","segment_op_profit"],"stage3_evidence_fields":["company_official_segment_bridge","low_drawdown_confirmation","margin_recovery_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004000/2025.csv; atlas/ohlcv_tradable_by_symbol_year/004/004000/2026.csv","profile_path":"atlas/symbol_profiles/004/004000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-05-14","entry_price":36300.0,"entry_ohlc":{"d":"2025-05-14","o":36500.0,"h":37000.0,"l":36200.0,"c":36300.0,"v":32261,"mc":936540000000.0,"m":"KOSPI"},"MFE_30D_pct":10.61,"MFE_90D_pct":38.57,"MFE_180D_pct":40.5,"MAE_30D_pct":-3.17,"MAE_90D_pct":-3.17,"MAE_180D_pct":-3.17,"peak_date":"2026-02-04","peak_price":51000.0,"peak_ohlc":{"d":"2026-02-04","o":49100.0,"h":51000.0,"l":48850.0,"c":50500.0,"v":141051,"mc":1302900000000.0,"m":"KOSPI"},"trough_date":"2025-05-23","trough_price":35150.0,"trough_ohlc":{"d":"2025-05-23","o":35400.0,"h":35700.0,"l":35150.0,"c":35500.0,"v":21151,"mc":915900000000.0,"m":"KOSPI"},"drawdown_after_peak_pct":-4.22,"below_entry_30D":true,"below_entry_90D":true,"below_entry_180D":true,"green_lateness_ratio":null,"four_b_local_vs_full_window_proximity":"not_applicable_or_4c","four_c_protection_label":"not_4c","trigger_outcome_label":"positive_clean_margin_conversion","current_profile_verdict":"missed_or_delayed_stage2_if_generic_chemical_downcycle_penalty_dominates","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_profile_or_pre_2001_2010_2023_non_overlap","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|004000|2025-05-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|006650|Stage4B|2025-05-08","case_id":"C17_006650_20250508_SECTOR_DOWNCYCLE_FALSE_4C_OVERBLOCK","symbol":"006650","company_name":"대한유화","round":"R4","loop":106,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage4B","trigger_date":"2025-05-08","evidence_available_at_that_date":true,"evidence_source":"S&P Global Ratings sector note; Korean petrochemical companies face deeper downcycle and no meaningful recovery signal, but without symbol-level operating loss bridge for this ticker at trigger date.","evidence_url":"https://www.spglobal.com/ratings/en/regulatory/article/250508-korean-petrochemical-companies-face-a-deeper-downcycle-s101618287","source_proxy_only":true,"evidence_url_pending":false,"stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["sector_downcycle","spread_pressure","no_recovery_commentary"],"stage4c_evidence_fields":["company_specific_break_missing_at_trigger"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2025.csv; atlas/ohlcv_tradable_by_symbol_year/006/006650/2026.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-05-08","entry_price":88600.0,"entry_ohlc":{"d":"2025-05-08","o":88800.0,"h":89500.0,"l":87700.0,"c":88600.0,"v":15893,"mc":575900000000.0,"m":"KOSPI"},"MFE_30D_pct":2.71,"MFE_90D_pct":45.03,"MFE_180D_pct":93.45,"MAE_30D_pct":-13.43,"MAE_90D_pct":-13.43,"MAE_180D_pct":-13.43,"peak_date":"2026-01-26","peak_price":171400.0,"peak_ohlc":{"d":"2026-01-26","o":161700.0,"h":171400.0,"l":159800.0,"c":160100.0,"v":49719,"mc":1040650000000.0,"m":"KOSPI"},"trough_date":"2025-05-26","trough_price":76700.0,"trough_ohlc":{"d":"2025-05-26","o":77900.0,"h":80500.0,"l":76700.0,"c":80100.0,"v":9907,"mc":520650000000.0,"m":"KOSPI"},"drawdown_after_peak_pct":-9.98,"below_entry_30D":true,"below_entry_90D":true,"below_entry_180D":true,"green_lateness_ratio":null,"four_b_local_vs_full_window_proximity":"not_applicable_or_4c","four_c_protection_label":"hard_4c_too_early","trigger_outcome_label":"false_4c_overblock_large_mfe","current_profile_verdict":"error_if_sector_downcycle_blanket_hard_4c","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_profile_or_pre_2001_2010_2023_non_overlap","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|006650|2025-05-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","case_id":"C17_011780_20210323_NB_LATEX_SPREAD_RERATING_LOCAL_4B","symbol":"011780","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage2-Actionable","baseline_total_proxy":78,"post_shadow_total_proxy":79,"revision_score_proxy":55,"evidence_confidence_proxy":45,"risk_penalty_proxy":12,"guardrail_verdict":"pass_with_4b_local_watch","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","case_id":"C17_298020_20210504_SPANDEX_MARGIN_SUPERCYCLE_LOCAL_4B","symbol":"298020","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage3-Yellow","baseline_total_proxy":78,"post_shadow_total_proxy":82,"revision_score_proxy":55,"evidence_confidence_proxy":70,"risk_penalty_proxy":12,"guardrail_verdict":"pass_with_4b_local_watch","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","case_id":"C17_011780_20240130_DEPRESSED_MARKET_FALSE_4C","symbol":"011780","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage4B","baseline_total_proxy":70,"post_shadow_total_proxy":58,"revision_score_proxy":25,"evidence_confidence_proxy":45,"risk_penalty_proxy":18,"guardrail_verdict":"4b_watch_cap_until_company_specific_margin_bridge","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","case_id":"C17_011170_20240208_LOTTECHEM_2023_LOSS_TRUE_4C","symbol":"011170","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage4C","baseline_total_proxy":61,"post_shadow_total_proxy":38,"revision_score_proxy":25,"evidence_confidence_proxy":70,"risk_penalty_proxy":18,"guardrail_verdict":"hard_4c_blocks_positive_stage","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","case_id":"C17_011170_20241108_LOTTECHEM_Q3_LOSS_TRUE_4C","symbol":"011170","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage4C","baseline_total_proxy":61,"post_shadow_total_proxy":38,"revision_score_proxy":25,"evidence_confidence_proxy":70,"risk_penalty_proxy":18,"guardrail_verdict":"hard_4c_blocks_positive_stage","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","case_id":"C17_004000_20250514_LOTTEFINE_CHLORINE_PRICE_VOLUME_RECOVERY","symbol":"004000","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage2-Actionable","baseline_total_proxy":78,"post_shadow_total_proxy":82,"revision_score_proxy":55,"evidence_confidence_proxy":70,"risk_penalty_proxy":5,"guardrail_verdict":"pass","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","case_id":"C17_006650_20250508_SECTOR_DOWNCYCLE_FALSE_4C_OVERBLOCK","symbol":"006650","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_type":"Stage4B","baseline_total_proxy":70,"post_shadow_total_proxy":58,"revision_score_proxy":25,"evidence_confidence_proxy":45,"risk_penalty_proxy":18,"guardrail_verdict":"4b_watch_cap_until_company_specific_margin_bridge","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"aggregate","round":"R4","loop":106,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","trigger_count":7,"calibration_usable_trigger_count":7,"positive_case_count":3,"counterexample_count":4,"stage4b_case_count":2,"stage4c_case_count":2,"source_proxy_only_count":3,"evidence_url_pending_count":0,"rows_missing_required_mfe_mae":0,"current_profile_error_count":4,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_weight","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","new_axis_proposed":"C17_CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE","direction":"gate_positive_stage_and_strengthen_4b_4c_split","weight_delta_proposal":{"named_product_spread_bridge":"+1.0 shadow","company_official_margin_conversion":"+1.5 shadow","source_proxy_only_cap":"-1.0 shadow / watch cap","blanket_sector_downcycle_to_hard_4c":"blocked unless company_specific_loss_bridge","local_4b_after_spread_peak":"+1.0 guard strength"},"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","residual_error_family":["positive_stage_overcredit_from_spread_headline_without_company_conversion","green_exit_late_after_spread_peak","hard_4c_too_early_from_single_quarter_or_sector_blanket","true_4c_when_company_level_loss_and_spread_break_confirmed"],"recommended_rule":"C17 positive scoring requires at least two of named product spread, company official margin/OP conversion, volume/demand bridge, and clean working-capital/balance-sheet quality; hard 4C requires company-specific sustained operating-loss/spread/cash break, not generic sector downcycle alone.","production_scoring_changed":false,"shadow_weight_only":true}
```

## 11. Batch ingest self-audit

```text
standard_v12_filename = true
filename_round_matches_metadata = true
filename_loop_matches_metadata = true
canonical_archetype_id_valid = true
large_sector_id_valid = true
round_sector_consistency = pass
trigger_type_canonical_stage_label_only = true
all_trigger_rows_have_MFE_30D_pct = true
all_trigger_rows_have_MFE_90D_pct = true
all_trigger_rows_have_MFE_180D_pct = true
all_trigger_rows_have_MAE_30D_pct = true
all_trigger_rows_have_MAE_90D_pct = true
all_trigger_rows_have_MAE_180D_pct = true
same_entry_group_deduped_for_aggregate = true
calibration_usable_trigger_count = 7
production_scoring_changed = false
shadow_weight_only = true
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not treat this research MD as an instruction to change production scoring immediately. Parse the machine-readable JSONL rows only after running the standard v12 ingestion, validation, dedupe, and promotion-readiness checks. If rows are accepted, evaluate the shadow rule candidate named C17_CHEMICAL_SPREAD_TO_MARGIN_CONVERSION_GATE. The intended rule is not a global threshold change. It is a C17-specific split between product-spread-to-company-margin conversion and generic petrochemical downcycle overblocking.

Required validation:
1. Confirm all trigger rows have complete MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
2. Confirm source_proxy_only rows do not promote positive-stage scoring unless independently verified by company/direct sources.
3. Confirm hard 4C promotion is only from company-specific sustained loss/spread/cash break, not generic sector commentary.
4. Keep production_scoring_changed=false unless a separate approved promotion plan exists.
```

## 13. Next research state

```text
completed_round = R4
completed_loop = 106
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C17 chemical spread conversion / 4B-4C split / source-proxy repair
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY; C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH; C14_EV_DEMAND_SLOWDOWN_4B_4C; C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
