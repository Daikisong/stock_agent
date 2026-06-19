# E2R v12 Residual Research — R1 / C01_ORDER_BACKLOG_MARGIN_BRIDGE / loop 130

## 0. Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 130
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C01 backlog-to-margin/FCF conversion, high-MAE residual and source-quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

No-Repeat Index is now past the simple row-fill phase: all C01~C32 representative row counts are above the old 80-row floor, so this loop prioritizes URL/proxy repair, complete entry/price fields, and residual 4B/4C taxonomy quality rather than raw volume. C05 was the immediate previous output, so this run returns to the other Priority-1 L1 backlog axis, **C01_ORDER_BACKLOG_MARGIN_BRIDGE**, while avoiding the earlier C01 loop's symbols.

C01 currently has a broad corpus, but it still has a recurring structural weakness: backlog/orderbook evidence is often recognized correctly, while the timing of margin, working-capital, and cash conversion remains too blunt. In lived trading terms, backlog is the ship parked outside the harbor; E2R should score the unloading only after the cargo shows up in margin, cash, or explicit delivery/revision evidence.

## 2. Stock-Web price validation protocol

- Atlas basis: `Songdaiki/stock-web`.
- Adjustment status: `raw_unadjusted_marcap`.
- Calibration shard: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv`.
- Entry rule: if disclosure timing is after close or unclear, use next Stock-Web tradable close.
- MFE/MAE definition: entry close versus max high / min low from entry date through the 30, 90, and 180 tradable-row windows.
- Manifest max date check: all selected rows have full 180-tradable-row forward windows within `2026-02-20`.
- Corporate-action check: checked symbol profiles where available; no 2024~2025 180D trigger-window contamination was used.

## 3. Evidence source ledger

| symbol | company | evidence focus | source quality | source URL |
|---|---|---|---|---|
|009540|HD한국조선해양|annual shipbuilding/offshore profit conversion and backlog-margin bridge|official/company financial page|https://www.hd-ksoe.com/en/investors/financial-info/financial-statements/contents|
|329180|HD현대중공업|official earnings-release trail and 2024 profit conversion|official/company IR|https://hd-hhi.com/en/investors/ir-data/earnings-release|
|010140|삼성중공업|Q3 2024 profit, high-end ship demand, order backlog visibility|high-quality news with company results|https://www.koreatimes.co.kr/business/companies/20241024/samsung-heavy-industries-q3-net-profit-doubles-on-strong-demand-for-high-end-ships|
|042660|한화오션|Q3 2024 profitability recovery and high-value backlog mix|high-quality news with company results|https://www.asiae.co.kr/en/article/2024102914003891749|
|010620|HD현대미포|Q4 2023 operating loss and cost gap, later recovery overblock test|high-quality news with company results|https://en.yna.co.kr/view/AEN20240206010000320|
|077970|STX엔진|annual sales and operating profit progression|official/company financial page|https://www.stxengine.co.kr/en/invest/financial-information/financial-status/|
|097230|HJ중공업|record 2024 order headline and later profit recovery context|high-quality news proxy|https://www.pulsenews.co.kr/view.php?year=2025&no=17967|

## 4. Trigger table

|symbol|company_name|trigger_date|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|case_role|current_profile_error|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|009540|HD한국조선해양|2025-02-06|Stage3-Yellow|2025-02-07|225500|12.42|-9.09|71.18|-17.65|119.29|-17.65|positive_high_MAE_green_delay|too_fast_green_if_backlog_profit_is_not_drawdown_confirmed|
|329180|HD현대중공업|2025-02-06|Stage3-Green|2025-02-07|311000|19.45|-8.36|47.27|-12.7|105.79|-12.7|positive|acceptable_green_but_requires_drawdown_aware_confirmation|
|010140|삼성중공업|2024-10-24|Stage3-Green|2024-10-25|9900|24.14|-5.76|57.78|-5.76|99.8|-5.76|positive_clean|low_error_current_profile_captures_backlog_to_margin|
|042660|한화오션|2024-10-29|Stage3-Yellow|2024-10-30|27550|49.0|-5.26|216.52|-5.26|247.73|-5.26|positive_turnaround|underweight_turnaround_if_yoy_profit_drop_overemphasized|
|010620|HD현대미포|2024-02-06|Stage4B|2024-02-07|67900|1.91|-12.22|22.39|-13.4|80.85|-13.4|counterexample_hard_4c_overblock|loss_only_hard_4c_would_miss_recovery|
|077970|STX엔진|2025-03-21|Stage4B|2025-03-24|24650|9.53|-25.72|9.53|-25.72|102.03|-25.72|counterexample_green_too_early_high_MAE|direct_profit_bridge_still_needs_drawdown_confirmation|
|097230|HJ중공업|2025-01-08|Stage4B|2025-01-09|7120|6.04|-18.68|39.04|-20.93|382.44|-20.93|counterexample_order_headline_green_delay|order_size_overcredits_before_margin_cash_conversion|


## 5. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","calibration_usable":true,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE","symbol":"009540","company_name":"HD한국조선해양","trigger_date":"2025-02-06","trigger_type":"Stage3-Yellow","trigger_family":"annual_shipbuilding_profit_turnaround_and_backlog_margin_bridge","evidence_family":"direct_financial_statement_profit_conversion","entry_rule":"after_close_or_time_unclear_next_tradable_close","entry_date":"2025-02-07","entry_price":225500,"MFE_30D_pct":12.42,"MAE_30D_pct":-9.09,"MFE_90D_pct":71.18,"MAE_90D_pct":-17.65,"MFE_180D_pct":119.29,"MAE_180D_pct":-17.65,"peak_30D_date":"2025-03-05","peak_30D_high":253500,"trough_30D_date":"2025-03-21","trough_30D_low":205000,"peak_90D_date":"2025-06-20","peak_90D_high":386000,"trough_90D_date":"2025-04-07","trough_90D_low":185700,"peak_180D_date":"2025-11-03","peak_180D_high":494500,"trough_180D_date":"2025-04-07","trough_180D_low":185700,"case_role":"positive_high_MAE_green_delay","current_profile_error":"too_fast_green_if_backlog_profit_is_not_drawdown_confirmed","residual_label":"C01_backlog_profit_positive_with_intermediate_drawdown","same_entry_group":"C01_009540_2025-02-07","forward_window_available":true,"corporate_action_window_180D_contaminated":false,"source_url":"https://www.hd-ksoe.com/en/investors/financial-info/financial-statements/contents","source_quality":"official_company_financial_page"}
{"row_type":"trigger","calibration_usable":true,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE","symbol":"329180","company_name":"HD현대중공업","trigger_date":"2025-02-06","trigger_type":"Stage3-Green","trigger_family":"large_shipbuilder_profit_conversion_and_high_value_order_mix","evidence_family":"direct_earnings_release_and_order_mix_bridge","entry_rule":"after_close_or_time_unclear_next_tradable_close","entry_date":"2025-02-07","entry_price":311000,"MFE_30D_pct":19.45,"MAE_30D_pct":-8.36,"MFE_90D_pct":47.27,"MAE_90D_pct":-12.7,"MFE_180D_pct":105.79,"MAE_180D_pct":-12.7,"peak_30D_date":"2025-02-13","peak_30D_high":371500,"trough_30D_date":"2025-02-28","trough_30D_low":285000,"peak_90D_date":"2025-06-17","peak_90D_high":458000,"trough_90D_date":"2025-03-31","trough_90D_low":271500,"peak_180D_date":"2025-10-27","peak_180D_high":640000,"trough_180D_date":"2025-03-31","trough_180D_low":271500,"case_role":"positive","current_profile_error":"acceptable_green_but_requires_drawdown_aware_confirmation","residual_label":"C01_direct_order_profit_winner","same_entry_group":"C01_329180_2025-02-07","forward_window_available":true,"corporate_action_window_180D_contaminated":false,"source_url":"https://hd-hhi.com/en/investors/ir-data/earnings-release","source_quality":"official_company_IR_release_list"}
{"row_type":"trigger","calibration_usable":true,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE","symbol":"010140","company_name":"삼성중공업","trigger_date":"2024-10-24","trigger_type":"Stage3-Green","trigger_family":"high_end_ship_backlog_and_margin_recovery","evidence_family":"quarterly_profit_order_backlog_three_year_visibility","entry_rule":"after_close_or_time_unclear_next_tradable_close","entry_date":"2024-10-25","entry_price":9900,"MFE_30D_pct":24.14,"MAE_30D_pct":-5.76,"MFE_90D_pct":57.78,"MAE_90D_pct":-5.76,"MFE_180D_pct":99.8,"MAE_180D_pct":-5.76,"peak_30D_date":"2024-11-25","peak_30D_high":12290,"trough_30D_date":"2024-11-01","trough_30D_low":9330,"peak_90D_date":"2025-02-26","peak_90D_high":15620,"trough_90D_date":"2024-11-01","trough_90D_low":9330,"peak_180D_date":"2025-07-22","peak_180D_high":19780,"trough_180D_date":"2024-11-01","trough_180D_low":9330,"case_role":"positive_clean","current_profile_error":"low_error_current_profile_captures_backlog_to_margin","residual_label":"C01_clean_backlog_margin_winner","same_entry_group":"C01_010140_2024-10-25","forward_window_available":true,"corporate_action_window_180D_contaminated":false,"source_url":"https://www.koreatimes.co.kr/business/companies/20241024/samsung-heavy-industries-q3-net-profit-doubles-on-strong-demand-for-high-end-ships","source_quality":"high_quality_news_with_company_results"}
{"row_type":"trigger","calibration_usable":true,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE","symbol":"042660","company_name":"한화오션","trigger_date":"2024-10-29","trigger_type":"Stage3-Yellow","trigger_family":"quarterly_profitability_recovery_with_backlog_mix","evidence_family":"profit_turnaround_qoq_LNG_backlog_quality","entry_rule":"after_close_or_time_unclear_next_tradable_close","entry_date":"2024-10-30","entry_price":27550,"MFE_30D_pct":49.0,"MAE_30D_pct":-5.26,"MFE_90D_pct":216.52,"MAE_90D_pct":-5.26,"MFE_180D_pct":247.73,"MAE_180D_pct":-5.26,"peak_30D_date":"2024-11-15","peak_30D_high":41050,"trough_30D_date":"2024-11-01","trough_30D_low":26100,"peak_90D_date":"2025-03-04","peak_90D_high":87200,"trough_90D_date":"2024-11-01","trough_90D_low":26100,"peak_180D_date":"2025-06-18","peak_180D_high":95800,"trough_180D_date":"2024-11-01","trough_180D_low":26100,"case_role":"positive_turnaround","current_profile_error":"underweight_turnaround_if_yoy_profit_drop_overemphasized","residual_label":"C01_turnaround_backlog_winner","same_entry_group":"C01_042660_2024-10-30","forward_window_available":true,"corporate_action_window_180D_contaminated":false,"source_url":"https://www.asiae.co.kr/en/article/2024102914003891749","source_quality":"high_quality_news_with_company_results"}
{"row_type":"trigger","calibration_usable":true,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE","symbol":"010620","company_name":"HD현대미포","trigger_date":"2024-02-06","trigger_type":"Stage4B","trigger_family":"loss_signal_vs_later_backlog_margin_recovery","evidence_family":"quarterly_loss_cost_gap_not_hard_thesis_break","entry_rule":"after_close_or_time_unclear_next_tradable_close","entry_date":"2024-02-07","entry_price":67900,"MFE_30D_pct":1.91,"MAE_30D_pct":-12.22,"MFE_90D_pct":22.39,"MAE_90D_pct":-13.4,"MFE_180D_pct":80.85,"MAE_180D_pct":-13.4,"peak_30D_date":"2024-03-15","peak_30D_high":69200,"trough_30D_date":"2024-02-27","trough_30D_low":59600,"peak_90D_date":"2024-06-21","peak_90D_high":83100,"trough_90D_date":"2024-04-16","trough_90D_low":58800,"peak_180D_date":"2024-07-31","peak_180D_high":122800,"trough_180D_date":"2024-04-16","trough_180D_low":58800,"case_role":"counterexample_hard_4c_overblock","current_profile_error":"loss_only_hard_4c_would_miss_recovery","residual_label":"C01_loss_watch_not_permanent_4C","same_entry_group":"C01_010620_2024-02-07","forward_window_available":true,"corporate_action_window_180D_contaminated":false,"source_url":"https://en.yna.co.kr/view/AEN20240206010000320","source_quality":"high_quality_news_with_company_results"}
{"row_type":"trigger","calibration_usable":true,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE","symbol":"077970","company_name":"STX엔진","trigger_date":"2025-03-21","trigger_type":"Stage4B","trigger_family":"profit_growth_confirmed_but_high_MAE_before_rerating","evidence_family":"annual_OP_growth_engine_component_backlog_to_margin","entry_rule":"after_close_or_time_unclear_next_tradable_close","entry_date":"2025-03-24","entry_price":24650,"MFE_30D_pct":9.53,"MAE_30D_pct":-25.72,"MFE_90D_pct":9.53,"MAE_90D_pct":-25.72,"MFE_180D_pct":102.03,"MAE_180D_pct":-25.72,"peak_30D_date":"2025-04-28","peak_30D_high":27000,"trough_30D_date":"2025-04-07","trough_30D_low":18310,"peak_90D_date":"2025-04-28","peak_90D_high":27000,"trough_90D_date":"2025-04-07","trough_90D_low":18310,"peak_180D_date":"2025-09-05","peak_180D_high":49800,"trough_180D_date":"2025-04-07","trough_180D_low":18310,"case_role":"counterexample_green_too_early_high_MAE","current_profile_error":"direct_profit_bridge_still_needs_drawdown_confirmation","residual_label":"C01_engine_component_high_MAE_winner","same_entry_group":"C01_077970_2025-03-24","forward_window_available":true,"corporate_action_window_180D_contaminated":false,"source_url":"https://www.stxengine.co.kr/en/invest/financial-information/financial-status/","source_quality":"official_company_financial_page"}
{"row_type":"trigger","calibration_usable":true,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE","symbol":"097230","company_name":"HJ중공업","trigger_date":"2025-01-08","trigger_type":"Stage4B","trigger_family":"record_order_headline_with_deep_initial_MAE","evidence_family":"orderbook_headline_requires_margin_cash_confirmation","entry_rule":"after_close_or_time_unclear_next_tradable_close","entry_date":"2025-01-09","entry_price":7120,"MFE_30D_pct":6.04,"MAE_30D_pct":-18.68,"MFE_90D_pct":39.04,"MAE_90D_pct":-20.93,"MFE_180D_pct":382.44,"MAE_180D_pct":-20.93,"peak_30D_date":"2025-01-14","peak_30D_high":7550,"trough_30D_date":"2025-01-24","trough_30D_low":5790,"peak_90D_date":"2025-03-06","peak_90D_high":9900,"trough_90D_date":"2025-04-07","trough_90D_low":5630,"peak_180D_date":"2025-09-10","peak_180D_high":34350,"trough_180D_date":"2025-04-07","trough_180D_low":5630,"case_role":"counterexample_order_headline_green_delay","current_profile_error":"order_size_overcredits_before_margin_cash_conversion","residual_label":"C01_record_order_high_MAE_eventual_winner","same_entry_group":"C01_097230_2025-01-09","forward_window_available":true,"corporate_action_window_180D_contaminated":false,"source_url":"https://www.pulsenews.co.kr/view.php?year=2025&no=17967","source_quality":"high_quality_news_proxy_company_results"}
```

## 6. Score simulation and residual interpretation

|symbol|current_stage|shadow_read|component_note|
|---|---|---|---|
|009540|Stage3-Yellow→too-fast-Green risk|keep Yellow until margin/cash bridge and drawdown confirmation|EPS/Visibility strong; capital/cash bridge not enough for immediate Green|
|329180|Stage3-Green|Green acceptable, but attach high-MAE monitor|direct OP conversion and order visibility support rerating|
|010140|Stage3-Green|clean C01 positive|order backlog + three-year visibility + OP bridge|
|042660|Stage3-Yellow|turnaround positive; avoid underweighting QoQ recovery|LNG/high-value backlog and profit recovery overcame YoY softness|
|010620|Stage4B|loss signal should not become permanent 4C without cancellation/cash break|initial MAE deep but 180D recovery large|
|077970|Stage4B|profit bridge is real but 30/90D high-MAE blocks Green|annual OP grew but entry was early relative to price validation|
|097230|Stage4B|record order headline needs margin/cash confirmation before Green|eventual huge MFE, but 30/90D drawdown shows timing hazard|


### Current calibrated profile stress

Current C01 baseline component weights from the active v12 ledger are treated as:

```text
EPS/Visibility/Bottleneck/Mispricing/Valuation/Capital/Info = 20/25/18/12/12/8/5
```

This loop does not argue that C01 backlog evidence is weak. It argues that **backlog without conversion timing is not enough for immediate Green**. The positive cases show why C01 deserves a high visibility score: Samsung Heavy Industries and Hanwha Ocean converted order/backlog quality into powerful price paths. The counterexamples show the missing guardrail: HD Hyundai Mipo, STX Engine, and HJ Shipbuilding all had valid industrial hooks, but early MAE was deep enough that a Green label at trigger time would have felt like stepping onto a gangplank before the ship was tied to the dock.

## 7. Aggregate metrics

```yaml
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 4
counterexample_count: 3
stage4b_case_count: 3
stage4c_case_count: 0
source_proxy_only_count: 1
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 5
diversity_score_summary: 7 symbols / 7 trigger families / 4 positives / 3 counterexamples / high-MAE and hard-4C-overblock repair
do_not_propose_new_weight_delta: false
```

## 8. Proposed residual axis

```yaml
new_axis_proposed: C01_BACKLOG_MARGIN_CASH_CONVERSION_AND_DRAWDOWN_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
  - information_confidence_gate
existing_axis_weakened: null
production_scoring_changed: false
shadow_weight_only: true
```

### Rule candidate

For C01, do not promote an order/backlog headline to Stage3-Green until at least **two** of the following are present:

1. named backlog/orderbook tied to delivery or revenue timing;
2. explicit margin/cost-rate/operating-profit conversion;
3. working-capital, cash, or receivable quality that confirms conversion is not merely accounting backlog;
4. revision/guidance evidence that the market has not already fully priced.

If only backlog size is present, cap at Stage2 or Stage2-Actionable. If a loss/cost gap is present without cancellation, cash break, or persistent cost-overrun proof, treat it as Stage4B watch rather than permanent Stage4C. Hard 4C should require backlog cancellation, project-margin collapse, visible working-capital stress, or repeated cash/earnings failure.

### Suggested shadow weight delta

```yaml
before:
  EPS_FCF_explosion: 20
  earnings_visibility: 25
  bottleneck_pricing: 18
  market_mispricing: 12
  valuation_rerating: 12
  capital_allocation: 8
  information_confidence: 5
after_shadow:
  EPS_FCF_explosion: 19
  earnings_visibility: 27
  bottleneck_pricing: 17
  market_mispricing: 10
  valuation_rerating: 10
  capital_allocation: 10
  information_confidence: 7
delta:
  EPS_FCF_explosion: -1
  earnings_visibility: +2
  bottleneck_pricing: -1
  market_mispricing: -2
  valuation_rerating: -2
  capital_allocation: +2
  information_confidence: +2
```

Interpretation: C01 should reward actual delivery/margin/cash visibility more than generic rerating vocabulary. Backlog is the warehouse label; margin and cash are the goods leaving the warehouse.

## 9. Batch ingest self-audit

```yaml
filename_regex_pass: true
filename_round_loop_match_metadata: true
round_sector_consistency: pass
canonical_archetype_id_valid: true
trigger_type_canonical_labels_only: true
required_MFE_MAE_30_90_180_present_for_all_trigger_rows: true
entry_date_and_entry_price_present_for_all_trigger_rows: true
forward_180D_window_available_for_all_rows: true
corporate_action_contamination_detected: false
same_entry_group_present: true
stock_agent_code_opened_or_patched: false
live_scan_or_current_candidate_discovery: false
production_scoring_changed: false
shadow_weight_only: true
evidence_url_pending_count: 0
source_proxy_only_count: 1
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research generation.

When batch-applying this MD later, parse the trigger JSONL rows and evaluate the shadow rule candidate:
C01_BACKLOG_MARGIN_CASH_CONVERSION_AND_DRAWDOWN_GATE.

Apply only to C01_ORDER_BACKLOG_MARGIN_BRIDGE candidates. Compare current profile behavior against shadow behavior:
- keep backlog/order-size evidence as Stage2/Stage2-Actionable unless at least two conversion bridges are present;
- require delivery/revenue timing + margin/cost-rate/OP conversion or cash/working-capital proof before Stage3-Green;
- route loss/cost-gap evidence to Stage4B watch unless there is cancellation, repeated cost-overrun, cash break, or working-capital thesis break;
- preserve winners with high MFE but delay Green where 30/90D MAE exceeds drawdown-aware thresholds.

Expected parser fields:
- canonical_archetype_id
- fine_archetype_id
- trigger_type
- entry_date / entry_price
- MFE_30D_pct / MFE_90D_pct / MFE_180D_pct
- MAE_30D_pct / MAE_90D_pct / MAE_180D_pct
- source_quality
- current_profile_error
- residual_label
```

## 11. Completed state

```yaml
completed_round: R1
completed_loop: 130
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C01 backlog-to-margin/FCF conversion, high-MAE residual and source-quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ORDER_BACKLOG_TO_MARGIN_CASH_CONVERSION_GATE
new_axis_proposed: C01_BACKLOG_MARGIN_CASH_CONVERSION_AND_DRAWDOWN_GATE
loop_contribution_label: canonical_archetype_rule_candidate
next_recommended_archetypes:
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```
