---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 128
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_BACKEND_BONDER_REFLOW_TEST_EQUIPMENT_ORDER_CONVERSION_VS_RS_BLOWOFF
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C07 4C-empty, source/proxy repair, direct order-conversion vs relative-strength blowoff split
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
output_filename: e2r_stock_web_v12_residual_round_R2_loop_128_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
---

# E2R v12 Residual Research — R2/L2/C07 HBM Equipment Order Relative Strength

## 0. Execution mode and hard stops

This is a historical trigger-level residual calibration artifact. It is not a live stock recommendation, not a stock-agent code patch, not a brokerage/API task, and not a production scoring change. The only output is this standalone Markdown research file for later batch ingestion.

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
must_use_actual_stock_web_1D_OHLC = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
```

## 1. Coverage-index selection

The no-repeat ledger is now in quality-repair mode rather than simple row-count fill mode. It reports that all C01~C32 canonical archetypes exceed 80 representative rows, while C07 has 224 rows, 54 symbols, 56 positive / 60 counterexample rows, 42 4B rows and 0 4C rows. That makes C07 suitable for a quality loop focused on source/proxy repair and missing 4C conversion-failure paths.

```text
selected_round = R2
selected_loop = 128
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_BACKEND_BONDER_REFLOW_TEST_EQUIPMENT_ORDER_CONVERSION_VS_RS_BLOWOFF
```

## 2. Novelty and duplicate-avoidance check

Hard duplicate key used for this run:

```text
canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family
```

The selected cases avoid the immediately prior conversation outputs: C05, C01, C13, C15, C10, C02, C16, R13_HIGH_MAE, and C17. Inside C07, this loop uses a deliberately mixed HBM backend equipment basket: test/prober, fluxless reflow, TC bonder, laser dicing, and HBM tester localization.

```text
new_independent_case_count = 6
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
calibration_usable_case_count = 6
calibration_usable_trigger_count = 6
positive_case_count = 3
counterexample_count = 3
stage4b_case_count = 2
stage4c_case_count = 1
source_proxy_only_count = 3
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
current_profile_error_count = 5
```

## 3. Stock-Web source validation

Stock-Web manifest values used for this run:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
```

Schema rule used for every price row:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

All trigger windows have at least 180 forward tradable rows by the Stock-Web manifest max date. No selected entry window overlaps the profile-listed corporate-action candidate dates.

## 4. Case table with actual 1D OHLC row and MFE/MAE

|case_id|symbol|company|trigger_type|trigger_date|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak|trough|outcome|proxy|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C07_R2_L128_001|089030|테크윙|Stage2-Actionable|2024-03-14|2024-03-14|29000.00|34.83|-6.21|144.14|-6.21|144.14|-6.21|2024-07-11 / 70800.00|2024-03-14 / 27200.00|positive_structural_success|true|
|C07_R2_L128_002|039440|에스티아이|Stage2-Actionable|2023-08-04|2023-08-04|26050.00|32.82|-8.45|44.34|-8.45|66.03|-8.45|2024-03-13 / 43250.00|2023-08-28 / 23850.00|positive_order_conversion_success|false|
|C07_R2_L128_003|031980|피에스케이홀딩스|Stage2-Actionable|2024-05-31|2024-05-31|54900.00|55.37|-3.64|55.37|-34.24|55.37|-49.54|2024-06-19 / 85300.00|2024-12-09 / 27700.00|high_mfe_high_mae_success_requiring_4b_overlay|false|
|C07_R2_L128_004|042700|한미반도체|Stage4B|2024-06-07|2024-06-07|156800.00|25.13|-5.23|25.13|-41.77|25.13|-55.74|2024-06-14 / 196200.00|2024-12-11 / 69400.00|late_order_local_blowoff_counterexample|false|
|C07_R2_L128_005|039030|이오테크닉스|Stage4C|2024-04-26|2024-04-26|239500.00|6.89|-19.92|6.89|-45.97|6.89|-52.61|2024-04-29 / 256000.00|2024-11-29 / 113500.00|proxy_beneficiary_thesis_break_counterexample|true|
|C07_R2_L128_006|003160|디아이|Stage4B|2024-05-23|2024-05-23|19800.00|55.56|-17.17|55.56|-44.90|55.56|-50.20|2024-06-27 / 30800.00|2024-12-09 / 9860.00|local_blowoff_then_conversion_uncertainty_counterexample|true|


## 5. Evidence table

|case_id|symbol|evidence_family|as_of_evidence_summary|primary_url|proxy_only|
|---|---|---|---|---|---|
|C07_R2_L128_001|089030|HBM_test_equipment_new_business_customer_quality|Cube Prober/HBM package test narrative became specific enough to map to HBM test equipment but still lacked a disclosed customer order at trigger date.|https://www.asiae.co.kr/en/article/2024031315391648405|true|
|C07_R2_L128_002|039440|specific_global_customer_reflow_order|STI announced it had received an order for reflow equipment from a global semiconductor company for 4th-generation HBM3 production.|https://www.asiae.co.kr/en/article/2023080410125362539|false|
|C07_R2_L128_003|031980|specific_customer_supply_and_product_page|TheElec reported PSK Holdings had supplied reflow equipment to Micron for HBM, and PSK/PSK Group product pages map the company to reflow systems.|https://www.thelec.net/news/articleView.html?idxno=4859|false|
|C07_R2_L128_004|042700|specific_customer_order_but_after_large_price_run|A large SK hynix Dual TC Bonder Griffin order was real, but the entry occurred near a local exhaustion zone after a long rerating move.|https://www.kedglobal.com/korean-chipmakers/newsView/ked202406070008|false|
|C07_R2_L128_005|039030|product_exposure_but_missing_customer_order_conversion|Laser dicing was relevant to HBM packaging, but the trigger was a beneficiary narrative without a disclosed HBM customer order or revenue bridge.|https://www.digitaltoday.co.kr/news/articleView.html?idxno=515377|true|
|C07_R2_L128_006|003160|customer_supply_chain_proxy_without_HBM_order|DI/DF mapped to wafer test equipment and Samsung/SK hynix channels, but the trigger was a localization expectation rather than a formal HBM order.|https://alphabiz.co.kr/news/view/1065581016884096|true|


## 6. Case notes

### 6.1 C07_R2_L128_001 — Techwing / 테크윙 / 089030

Techwing is the constructive proxy-positive path. The as-of article mapped Cube Prober to HBM package test and argued that HBM yield inspection was becoming a bottleneck. It lacked a disclosed customer order at the trigger date, so this is not a clean direct-order row. But the price path shows a structural MFE profile: +34.83% within 30D and +144.14% within 90D/180D with only -6.21% MAE. This is the kind of C07 case where the current profile can be too slow if it requires a formal single-sales contract before acknowledging a new equipment node.

### 6.2 C07_R2_L128_002 — STI / 에스티아이 / 039440

STI is the clean order-conversion positive. The trigger was a 4th-generation HBM3 reflow equipment order from a global semiconductor company. The entry close was 26,050, and the 180D path reached +66.03% MFE with only -8.45% MAE. This is the archetypal C07 Stage2-Actionable row: named HBM process equipment plus order evidence plus forward price confirmation.

### 6.3 C07_R2_L128_003 — PSK Holdings / 피에스케이홀딩스 / 031980

PSK Holdings is a high-MFE but high-MAE success. The Micron HBM reflow supply evidence is real enough for Stage2-Actionable, and 30D MFE reached +55.37%. But the same 55.37% was also the 90D/180D maximum, followed by -34.24% 90D MAE and -49.54% 180D MAE. The right classification is not to erase the positive signal, but to require a local 4B watch once the order evidence becomes widely priced.

### 6.4 C07_R2_L128_004 — Hanmi Semiconductor / 한미반도체 / 042700

Hanmi's June 2024 SK hynix Dual TC Bonder Griffin order was real, but the signal arrived after a large rerating move. Entry at 156,800 produced +25.13% 30D MFE, yet the 90D/180D MAE reached -41.77%/-55.74%. This is not a bad company case; it is a late-entry classification case. C07 needs to separate real order evidence from fresh upside when the order lands at a local blowoff zone.

### 6.5 C07_R2_L128_005 — EO Technics / 이오테크닉스 / 039030

EO Technics is the proxy-beneficiary 4C path. HBM laser dicing is process-relevant, and EO's product map includes laser/dicing capabilities. The trigger, however, was a beneficiary narrative without named customer/order/revenue conversion. MFE was only +6.89%, while 90D/180D MAE reached -45.97%/-52.61%. For C07, this is a conversion-failure guardrail row: the equipment is plausible, but the bridge is not investable enough for Stage2-Actionable.

### 6.6 C07_R2_L128_006 — DI Corporation / 디아이 / 003160

DI is a local blowoff plus conversion-uncertainty row. The May 2024 article mapped DI/DF to wafer test equipment channels and HBM test-equipment localization. It produced +55.56% MFE, but then fell to -44.90% 90D MAE and -50.20% 180D MAE. Without a formal as-of HBM order/qualification row, this should stay 4B/watch rather than Green.

## 7. Price-path diagnostics

```text
avg_MFE_90D_pct_all = 55.24
avg_MAE_90D_pct_all = -30.26
avg_MFE_90D_pct_positive = 81.28
avg_MAE_90D_pct_positive = -16.3
avg_MFE_90D_pct_counter = 29.19
avg_MAE_90D_pct_counter = -44.21
```

The split is the main finding. Positive C07 cases still have strong 90D MFE, but a clean direct order is not enough if it arrives after a parabolic run. C07 behaves like a clean-room door: the HBM theme may point to the room, but Stage2 should open only when the equipment, customer, and conversion badge all scan.

## 8. Current calibrated profile stress test

Current global rules already block price-only blowoff and require non-price evidence for full 4B. The residual error here is narrower:

```text
residual_error_family = C07_order_conversion_vs_relative_strength_blowoff
current_profile_error_count = 5
false_positive_family = proxy_beneficiary_or_late_order_after_rerating
missed_structural_family = HBM_test_equipment_node_before_formal_contract
```

C07 needs a small archetype-specific gate, not a global threshold rewrite.

## 9. Profile comparison table

|profile|rule|selected_rows|avg_MFE90|avg_MAE90|diagnosis|
|---|---|---|---|---|---|
|P0 current calibrated proxy|Use C07 current weights 22/22/19/14/12/6/5; Stage2 bridge exists if HBM equipment evidence appears.|6|55.24|-30.26|Still overcredits late order/RS blowoff and under-separates direct order from proxy beneficiary articles.|
|P1 source-quality gate|Proxy-only HBM equipment articles cannot unlock Stage2-Actionable without customer/order/qualification or revenue bridge.|3 guardrail|29.19|-44.21|Cuts EO/DI-style false positive Green while preserving watch value.|
|P2 order-conversion gate|Named equipment + customer/order/qualification + conversion timing keeps positive rows eligible.|3 representative positive|81.28|-16.3|Keeps Techwing/STI/PSK as positive or watch-positive but forces drawdown-aware 4B after fast peaks.|
|P3 final shadow candidate|Stage2-Actionable requires 2+ bridge checks; late order after parabolic rerating routes to local 4B; proxy-only conversion failure routes to 4C/watch.|6|55.24|-30.26|Better split between structural HBM equipment and late-bubble beneficiary narratives.|


## 10. Score simulation rows

|case_id|symbol|before_score|after_score|before_stage|after_stage|alignment_note|
|---|---|---|---|---|---|---|
|C07_R2_L128_001|089030|74|81|Stage2|Stage3-Yellow|Cube prober source is proxy but product/process specificity and huge MFE indicate prior profile may underweight HBM test equipment conversion.|
|C07_R2_L128_002|039440|78|84|Stage2-Actionable|Stage3-Yellow|Specific HBM3 reflow order supports uplift, but Green remains blocked until revenue/margin bridge confirms.|
|C07_R2_L128_003|031980|82|76|Stage3-Yellow|Stage2-Actionable|Specific Micron HBM reflow supply is real, but fast peak and -34% 90D MAE require 4B watch discount.|
|C07_R2_L128_004|042700|86|63|Stage3-Yellow|Stage4B|Large order is real but late after parabolic rerating; fresh Stage2 credit should be capped by local 4B.|
|C07_R2_L128_005|039030|73|48|Stage2|Stage4C|HBM laser-dicing relevance without named customer/order conversion failed the bridge gate and suffered deep MAE.|
|C07_R2_L128_006|003160|79|57|Stage2-Actionable|Stage4B|HBM tester localization expectation created MFE but lacked formal as-of HBM order, so keep as 4B/watch rather than Green.|


## 11. Raw component score breakdown

The current C07 aggregate weight in the no-repeat ledger is approximately:

```text
C07 weights = EPS/Vis/Bott/Mis/Val/Cap/Info = 22/22/19/14/12/6/5
```

Shadow candidate:

```text
suggested_after_weights = 22/24/18/12/11/6/7
delta = 0/+2/-1/-2/-1/0/+2
```

Interpretation: do not make C07 more bullish. Shift a small amount from generalized bottleneck/mispricing/valuation beta into visibility and information confidence. HBM equipment rows should be rewarded when an order/qualification/revenue bridge appears, and capped when the evidence is only a beneficiary article or relative-strength chart.

## 12. Same-entry dedupe and aggregate roles

```text
representative_positive_rows = C07_R2_L128_001, C07_R2_L128_002, C07_R2_L128_003
4B_overlay_only_rows = C07_R2_L128_004, C07_R2_L128_006
4C_guardrail_only_rows = C07_R2_L128_005
same_entry_duplicate_count = 0
```

The 4B/4C rows are intentionally guardrail rows. They should not be used as positive promotion evidence.

## 13. 4B local vs full-window split

```text
local_4B_cases = 042700, 003160
full_window_4B_confirmation_cases = 031980, 042700, 003160
```

Hanmi and DI both gave enough early upside to tempt a naive Stage2/Green interpretation, but the drawdown after peak was larger than -60% in both cases. For C07, a real HBM term can be both true and stale. The local 4B question is therefore not “is HBM real?” but “has the order signal already become the exit liquidity candle?”

## 14. 4C thesis-break timing

EO Technics is the clean 4C timing row in this loop. The trigger evidence was process relevance, not order conversion. Once the 90D path showed only +6.89% MFE and -45.97% MAE, the proper residual classification is not late Green; it is bridge failure. C07 4C should fire when customer/order/qualification remains absent and the stock path confirms the market has stopped paying for the proxy.

## 15. Positive/counterexample balance

```text
positive_case_count = 3
counterexample_count = 3
balance_status = pass
```

The loop deliberately keeps both sides. Techwing and STI show why C07 cannot be too conservative. Hanmi, EO, and DI show why C07 cannot blindly follow every HBM equipment headline.

## 16. Sector-specific rule candidate

```text
L2_HBM_equipment_rule_candidate:
  Do not award Stage2-Actionable from relative strength, HBM capex beta, or beneficiary vocabulary alone.
  Require equipment-specific bridge evidence: named HBM equipment, explicit customer/order/qualification,
  deliverable timing, revenue/margin conversion, or repeat order pipeline.
  If the evidence appears after a large prior rerating and MAE risk is elevated, route to local 4B watch rather than fresh Stage2.
```

## 17. Canonical archetype rule candidate

```text
C07_HBM_EQUIPMENT_ORDER_CONVERSION_VS_RS_BLOWOFF_GATE:
  Stage2-Actionable requires at least two of:
    1. named HBM equipment node,
    2. customer/order/qualification evidence,
    3. deliverable or ramp timing,
    4. revenue/margin/revision conversion,
    5. repeat order pipeline or customer expansion.
  If only one condition is present and the price path has already rerated sharply, cap at Stage2-Watch or Stage4B.
  If proxy-only evidence is followed by MAE90 <= -35% and no order bridge appears, route to 4C/watch.
```

## 18. Residual contribution summary

```text
loop_contribution_label = C07_order_conversion_vs_RS_blowoff_quality_repair
new_axis_proposed = C07_HBM_EQUIPMENT_ORDER_CONVERSION_VS_RS_BLOWOFF_GATE
existing_axis_strengthened = stage2_required_bridge; local_4b_watch_guard; full_4b_requires_non_price_evidence; earlier_thesis_break_watch; hard_4c_confirmation
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

## 19. Machine-readable JSONL rows

```jsonl
{"row_type": "price_source_validation", "price_source": "Songdaiki/stock-web", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "schema_mfe_mae_definition": "MFE/MAE from entry_date through N tradable rows using max high/min low vs entry close", "source_basis": "FinanceData/marcap", "validation_status": "pass"}
{"row_type": "case", "case_id": "C07_R2_L128_001", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_CUBE_PROBER_TEST_EQUIPMENT_CONVERSION", "symbol": "089030", "company": "테크윙", "trigger_date": "2024-03-14", "entry_date": "2024-03-14", "case_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_too_late_or_underweight", "evidence_family": "HBM_test_equipment_new_business_customer_quality", "trigger_family": "HBM_cube_prober_test_equipment_revenue_path", "new_independent_case": true, "reused_case": false, "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": false, "novelty_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|Stage2-Actionable|2024-03-14|HBM_test_equipment_new_business_customer_quality"}
{"row_type": "case", "case_id": "C07_R2_L128_002", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_REFLOW_EQUIPMENT_ORDER_ROUTE", "symbol": "039440", "company": "에스티아이", "trigger_date": "2023-08-04", "entry_date": "2023-08-04", "case_outcome_label": "positive_order_conversion_success", "current_profile_verdict": "current_profile_correct_or_slightly_late", "evidence_family": "specific_global_customer_reflow_order", "trigger_family": "HBM3_fluxless_reflow_equipment_order", "new_independent_case": true, "reused_case": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "novelty_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039440|Stage2-Actionable|2023-08-04|specific_global_customer_reflow_order"}
{"row_type": "case", "case_id": "C07_R2_L128_003", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_REFLOW_EQUIPMENT_CUSTOMER_SUPPLY", "symbol": "031980", "company": "피에스케이홀딩스", "trigger_date": "2024-05-31", "entry_date": "2024-05-31", "case_outcome_label": "high_mfe_high_mae_success_requiring_4b_overlay", "current_profile_verdict": "current_profile_4B_too_late", "evidence_family": "specific_customer_supply_and_product_page", "trigger_family": "HBM_reflow_equipment_Micron_supply", "new_independent_case": true, "reused_case": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "novelty_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|Stage2-Actionable|2024-05-31|specific_customer_supply_and_product_page"}
{"row_type": "case", "case_id": "C07_R2_L128_004", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TC_BONDER_ORDER_ROUTE_LATE_ENTRY", "symbol": "042700", "company": "한미반도체", "trigger_date": "2024-06-07", "entry_date": "2024-06-07", "case_outcome_label": "late_order_local_blowoff_counterexample", "current_profile_verdict": "current_profile_4B_too_late", "evidence_family": "specific_customer_order_but_after_large_price_run", "trigger_family": "late_large_HBM_TC_bonder_order_after_rerating", "new_independent_case": true, "reused_case": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "novelty_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|Stage4B|2024-06-07|specific_customer_order_but_after_large_price_run"}
{"row_type": "case", "case_id": "C07_R2_L128_005", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_LASER_DICING_PROXY_BENEFICIARY", "symbol": "039030", "company": "이오테크닉스", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "case_outcome_label": "proxy_beneficiary_thesis_break_counterexample", "current_profile_verdict": "current_profile_false_positive", "evidence_family": "product_exposure_but_missing_customer_order_conversion", "trigger_family": "HBM_laser_dicing_beneficiary_narrative_without_order", "new_independent_case": true, "reused_case": false, "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": false, "novelty_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039030|Stage4C|2024-04-26|product_exposure_but_missing_customer_order_conversion"}
{"row_type": "case", "case_id": "C07_R2_L128_006", "selected_round": "R2", "selected_loop": 128, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_LOCALIZATION_PROXY", "symbol": "003160", "company": "디아이", "trigger_date": "2024-05-23", "entry_date": "2024-05-23", "case_outcome_label": "local_blowoff_then_conversion_uncertainty_counterexample", "current_profile_verdict": "current_profile_4B_too_late_or_false_positive", "evidence_family": "customer_supply_chain_proxy_without_HBM_order", "trigger_family": "HBM_test_equipment_localization_expectation", "new_independent_case": true, "reused_case": false, "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": false, "novelty_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|003160|Stage4B|2024-05-23|customer_supply_chain_proxy_without_HBM_order"}
{"row_type": "trigger", "case_id": "C07_R2_L128_001", "symbol": "089030", "company": "테크윙", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_CUBE_PROBER_TEST_EQUIPMENT_CONVERSION", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-14", "entry_date": "2024-03-14", "entry_price": 29000.0, "entry_open": 27600.0, "entry_high": 29500.0, "entry_low": 27200.0, "entry_close": 29000.0, "entry_volume": 924440, "MFE_30D_pct": 34.83, "MFE_90D_pct": 144.14, "MFE_180D_pct": 144.14, "MAE_30D_pct": -6.21, "MAE_90D_pct": -6.21, "MAE_180D_pct": -6.21, "peak_date": "2024-07-11", "peak_price": 70800.0, "trough_date": "2024-03-14", "trough_price": 27200.0, "drawdown_after_peak_pct": -57.63, "forward_window_trading_days": 180, "calibration_usable": true, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "corporate_action_window_status": "clean_180D_window", "profile_corporate_action_candidate_dates": "2011-12-13;2011-12-29;2022-08-01;2022-08-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_key": "089030|2024-03-14", "source_proxy_only": true, "evidence_url_pending": false, "primary_evidence_url": "https://www.asiae.co.kr/en/article/2024031315391648405", "secondary_evidence_url": "https://www.asiae.co.kr/en/article/2024031408180442980", "evidence_summary": "Cube Prober/HBM package test narrative became specific enough to map to HBM test equipment but still lacked a disclosed customer order at trigger date.", "audit_note": "positive path; source remains proxy because the public trigger was not a formal single-sales contract."}
{"row_type": "trigger", "case_id": "C07_R2_L128_002", "symbol": "039440", "company": "에스티아이", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_REFLOW_EQUIPMENT_ORDER_ROUTE", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-08-04", "entry_date": "2023-08-04", "entry_price": 26050.0, "entry_open": 24750.0, "entry_high": 27350.0, "entry_low": 24300.0, "entry_close": 26050.0, "entry_volume": 1634226, "MFE_30D_pct": 32.82, "MFE_90D_pct": 44.34, "MFE_180D_pct": 66.03, "MAE_30D_pct": -8.45, "MAE_90D_pct": -8.45, "MAE_180D_pct": -8.45, "peak_date": "2024-03-13", "peak_price": 43250.0, "trough_date": "2023-08-28", "trough_price": 23850.0, "drawdown_after_peak_pct": -28.09, "forward_window_trading_days": 180, "calibration_usable": true, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039440/2023.csv", "profile_path": "atlas/symbol_profiles/039/039440.json", "corporate_action_window_status": "clean_180D_window", "profile_corporate_action_candidate_dates": "2002-11-11;2006-01-24;2018-04-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_key": "039440|2023-08-04", "source_proxy_only": false, "evidence_url_pending": false, "primary_evidence_url": "https://www.asiae.co.kr/en/article/2023080410125362539", "secondary_evidence_url": "", "evidence_summary": "STI announced it had received an order for reflow equipment from a global semiconductor company for 4th-generation HBM3 production.", "audit_note": "clean positive: named equipment + customer/order + process relevance."}
{"row_type": "trigger", "case_id": "C07_R2_L128_003", "symbol": "031980", "company": "피에스케이홀딩스", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_REFLOW_EQUIPMENT_CUSTOMER_SUPPLY", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-31", "entry_date": "2024-05-31", "entry_price": 54900.0, "entry_open": 54700.0, "entry_high": 56000.0, "entry_low": 53000.0, "entry_close": 54900.0, "entry_volume": 257152, "MFE_30D_pct": 55.37, "MFE_90D_pct": 55.37, "MFE_180D_pct": 55.37, "MAE_30D_pct": -3.64, "MAE_90D_pct": -34.24, "MAE_180D_pct": -49.54, "peak_date": "2024-06-19", "peak_price": 85300.0, "trough_date": "2024-12-09", "trough_price": 27700.0, "drawdown_after_peak_pct": -67.53, "forward_window_trading_days": 180, "calibration_usable": true, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "profile_path": "atlas/symbol_profiles/031/031980.json", "corporate_action_window_status": "clean_180D_window", "profile_corporate_action_candidate_dates": "1998-07-28;2000-04-20;2007-03-16;2019-05-10;2020-02-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "same_entry_group_key": "031980|2024-05-31", "source_proxy_only": false, "evidence_url_pending": false, "primary_evidence_url": "https://www.thelec.net/news/articleView.html?idxno=4859", "secondary_evidence_url": "https://www.pskinc.com/aboutpsk/overview.php", "evidence_summary": "TheElec reported PSK Holdings had supplied reflow equipment to Micron for HBM, and PSK/PSK Group product pages map the company to reflow systems.", "audit_note": "positive but requires 4B watch after fast peak because 90/180D MAE erases the initial reward."}
{"row_type": "trigger", "case_id": "C07_R2_L128_004", "symbol": "042700", "company": "한미반도체", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TC_BONDER_ORDER_ROUTE_LATE_ENTRY", "trigger_type": "Stage4B", "trigger_date": "2024-06-07", "entry_date": "2024-06-07", "entry_price": 156800.0, "entry_open": 155800.0, "entry_high": 163000.0, "entry_low": 153500.0, "entry_close": 156800.0, "entry_volume": 2757638, "MFE_30D_pct": 25.13, "MFE_90D_pct": 25.13, "MFE_180D_pct": 25.13, "MAE_30D_pct": -5.23, "MAE_90D_pct": -41.77, "MAE_180D_pct": -55.74, "peak_date": "2024-06-14", "peak_price": 196200.0, "trough_date": "2024-12-11", "trough_price": 69400.0, "drawdown_after_peak_pct": -64.63, "forward_window_trading_days": 180, "calibration_usable": true, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "corporate_action_window_status": "clean_180D_window", "profile_corporate_action_candidate_dates": "2006-11-10;2017-05-11;2022-04-06", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "same_entry_group_key": "042700|2024-06-07", "source_proxy_only": false, "evidence_url_pending": false, "primary_evidence_url": "https://www.kedglobal.com/korean-chipmakers/newsView/ked202406070008", "secondary_evidence_url": "https://www.hanmisemi.com/index.php?CurrentPage=4&action=SiteBoardEn&iBrdContNo=243&iBrdNo=5&module=Board&sBrdContRe=0&sMode=VIEW_FORM&sSearchField=&sSearchValue=", "evidence_summary": "A large SK hynix Dual TC Bonder Griffin order was real, but the entry occurred near a local exhaustion zone after a long rerating move.", "audit_note": "true order evidence but better classified as local 4B/risk overlay than fresh Stage2-Actionable."}
{"row_type": "trigger", "case_id": "C07_R2_L128_005", "symbol": "039030", "company": "이오테크닉스", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_LASER_DICING_PROXY_BENEFICIARY", "trigger_type": "Stage4C", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 239500.0, "entry_open": 236500.0, "entry_high": 243000.0, "entry_low": 233000.0, "entry_close": 239500.0, "entry_volume": 142508, "MFE_30D_pct": 6.89, "MFE_90D_pct": 6.89, "MFE_180D_pct": 6.89, "MAE_30D_pct": -19.92, "MAE_90D_pct": -45.97, "MAE_180D_pct": -52.61, "peak_date": "2024-04-29", "peak_price": 256000.0, "trough_date": "2024-11-29", "trough_price": 113500.0, "drawdown_after_peak_pct": -55.66, "forward_window_trading_days": 180, "calibration_usable": true, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "corporate_action_window_status": "clean_180D_window", "profile_corporate_action_candidate_dates": "2003-02-03", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_guardrail_only", "same_entry_group_key": "039030|2024-04-26", "source_proxy_only": true, "evidence_url_pending": false, "primary_evidence_url": "https://www.digitaltoday.co.kr/news/articleView.html?idxno=515377", "secondary_evidence_url": "https://www.eotechnics.com/en/products/equipment3.php", "evidence_summary": "Laser dicing was relevant to HBM packaging, but the trigger was a beneficiary narrative without a disclosed HBM customer order or revenue bridge.", "audit_note": "hard 4C candidate: order-conversion bridge absent and 90/180D MAE dominated the path."}
{"row_type": "trigger", "case_id": "C07_R2_L128_006", "symbol": "003160", "company": "디아이", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_LOCALIZATION_PROXY", "trigger_type": "Stage4B", "trigger_date": "2024-05-23", "entry_date": "2024-05-23", "entry_price": 19800.0, "entry_open": 20800.0, "entry_high": 21200.0, "entry_low": 19350.0, "entry_close": 19800.0, "entry_volume": 2410649, "MFE_30D_pct": 55.56, "MFE_90D_pct": 55.56, "MFE_180D_pct": 55.56, "MAE_30D_pct": -17.17, "MAE_90D_pct": -44.9, "MAE_180D_pct": -50.2, "peak_date": "2024-06-27", "peak_price": 30800.0, "trough_date": "2024-12-09", "trough_price": 9860.0, "drawdown_after_peak_pct": -67.99, "forward_window_trading_days": 180, "calibration_usable": true, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "profile_path": "atlas/symbol_profiles/003/003160.json", "corporate_action_window_status": "clean_180D_window", "profile_corporate_action_candidate_dates": "1997-01-03;1998-07-03;1999-10-18", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "same_entry_group_key": "003160|2024-05-23", "source_proxy_only": true, "evidence_url_pending": false, "primary_evidence_url": "https://alphabiz.co.kr/news/view/1065581016884096", "secondary_evidence_url": "https://www.semi.org/en/resources/member-directory/di-corporation", "evidence_summary": "DI/DF mapped to wafer test equipment and Samsung/SK hynix channels, but the trigger was a localization expectation rather than a formal HBM order.", "audit_note": "4B overlay and 4C watch: large MFE exists, but no as-of formal HBM order conversion, so Green should be capped."}
{"row_type": "score_simulation", "case_id": "C07_R2_L128_001", "symbol": "089030", "profile_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_after": "C07_shadow_gate_candidate", "weighted_score_before": 74, "weighted_score_after": 81, "stage_before": "Stage2", "stage_after": "Stage3-Yellow", "component_scores_before": {"EPS": 20, "Vis": 22, "Bottleneck": 22, "Mispricing": 14, "Valuation": 12, "Capital": 5, "Info": 5}, "component_scores_after": {"EPS": 22, "Vis": 24, "Bottleneck": 20, "Mispricing": 12, "Valuation": 10, "Capital": 6, "Info": 6}, "rule_delta": "require order/qualification/revenue bridge; cap RS-only blowoff; route proxy-only conversion failure to 4B/4C", "score_return_alignment_note": "Cube prober source is proxy but product/process specificity and huge MFE indicate prior profile may underweight HBM test equipment conversion."}
{"row_type": "score_simulation", "case_id": "C07_R2_L128_002", "symbol": "039440", "profile_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_after": "C07_shadow_gate_candidate", "weighted_score_before": 78, "weighted_score_after": 84, "stage_before": "Stage2-Actionable", "stage_after": "Stage3-Yellow", "component_scores_before": {"EPS": 20, "Vis": 22, "Bottleneck": 22, "Mispricing": 14, "Valuation": 12, "Capital": 5, "Info": 5}, "component_scores_after": {"EPS": 22, "Vis": 24, "Bottleneck": 20, "Mispricing": 12, "Valuation": 10, "Capital": 6, "Info": 6}, "rule_delta": "require order/qualification/revenue bridge; cap RS-only blowoff; route proxy-only conversion failure to 4B/4C", "score_return_alignment_note": "Specific HBM3 reflow order supports uplift, but Green remains blocked until revenue/margin bridge confirms."}
{"row_type": "score_simulation", "case_id": "C07_R2_L128_003", "symbol": "031980", "profile_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_after": "C07_shadow_gate_candidate", "weighted_score_before": 82, "weighted_score_after": 76, "stage_before": "Stage3-Yellow", "stage_after": "Stage2-Actionable", "component_scores_before": {"EPS": 20, "Vis": 22, "Bottleneck": 22, "Mispricing": 14, "Valuation": 12, "Capital": 5, "Info": 5}, "component_scores_after": {"EPS": 22, "Vis": 24, "Bottleneck": 20, "Mispricing": 12, "Valuation": 10, "Capital": 6, "Info": 6}, "rule_delta": "require order/qualification/revenue bridge; cap RS-only blowoff; route proxy-only conversion failure to 4B/4C", "score_return_alignment_note": "Specific Micron HBM reflow supply is real, but fast peak and -34% 90D MAE require 4B watch discount."}
{"row_type": "score_simulation", "case_id": "C07_R2_L128_004", "symbol": "042700", "profile_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_after": "C07_shadow_gate_candidate", "weighted_score_before": 86, "weighted_score_after": 63, "stage_before": "Stage3-Yellow", "stage_after": "Stage4B", "component_scores_before": {"EPS": 20, "Vis": 22, "Bottleneck": 22, "Mispricing": 14, "Valuation": 12, "Capital": 5, "Info": 5}, "component_scores_after": {"EPS": 14, "Vis": 16, "Bottleneck": 12, "Mispricing": 12, "Valuation": 10, "Capital": 6, "Info": 16}, "rule_delta": "require order/qualification/revenue bridge; cap RS-only blowoff; route proxy-only conversion failure to 4B/4C", "score_return_alignment_note": "Large order is real but late after parabolic rerating; fresh Stage2 credit should be capped by local 4B."}
{"row_type": "score_simulation", "case_id": "C07_R2_L128_005", "symbol": "039030", "profile_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_after": "C07_shadow_gate_candidate", "weighted_score_before": 73, "weighted_score_after": 48, "stage_before": "Stage2", "stage_after": "Stage4C", "component_scores_before": {"EPS": 20, "Vis": 22, "Bottleneck": 22, "Mispricing": 14, "Valuation": 12, "Capital": 5, "Info": 5}, "component_scores_after": {"EPS": 14, "Vis": 16, "Bottleneck": 12, "Mispricing": 12, "Valuation": 10, "Capital": 6, "Info": 16}, "rule_delta": "require order/qualification/revenue bridge; cap RS-only blowoff; route proxy-only conversion failure to 4B/4C", "score_return_alignment_note": "HBM laser-dicing relevance without named customer/order conversion failed the bridge gate and suffered deep MAE."}
{"row_type": "score_simulation", "case_id": "C07_R2_L128_006", "symbol": "003160", "profile_before": "e2r_2_1_stock_web_calibrated_proxy", "profile_after": "C07_shadow_gate_candidate", "weighted_score_before": 79, "weighted_score_after": 57, "stage_before": "Stage2-Actionable", "stage_after": "Stage4B", "component_scores_before": {"EPS": 20, "Vis": 22, "Bottleneck": 22, "Mispricing": 14, "Valuation": 12, "Capital": 5, "Info": 5}, "component_scores_after": {"EPS": 14, "Vis": 16, "Bottleneck": 12, "Mispricing": 12, "Valuation": 10, "Capital": 6, "Info": 16}, "rule_delta": "require order/qualification/revenue bridge; cap RS-only blowoff; route proxy-only conversion failure to 4B/4C", "score_return_alignment_note": "HBM tester localization expectation created MFE but lacked formal as-of HBM order, so keep as 4B/watch rather than Green."}
{"row_type": "aggregate_summary", "selected_round": "R2", "selected_loop": 128, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "trigger_rows": 6, "representative_positive_rows": 3, "guardrail_overlay_rows": 3, "positive_case_count": 3, "counterexample_count": 3, "avg_MFE_90D_pct_all": 55.24, "avg_MAE_90D_pct_all": -30.26, "avg_MFE_90D_pct_positive": 81.28, "avg_MAE_90D_pct_positive": -16.3, "avg_MFE_90D_pct_counter": 29.19, "avg_MAE_90D_pct_counter": -44.21, "current_profile_error_count": 5}
{"row_type": "shadow_weight", "scope": "canonical_archetype", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "axis": "C07_HBM_EQUIPMENT_ORDER_CONVERSION_VS_RS_BLOWOFF_GATE", "production_scoring_changed": false, "shadow_weight_only": true, "before_weights": "22/22/19/14/12/6/5", "suggested_after_weights": "22/24/18/12/11/6/7", "delta": "0/+2/-1/-2/-1/0/+2", "explanation": "Shift a small amount from pure bottleneck/mispricing/valuation beta into visibility and information-confidence because C07 failures come from RS/beneficiary narratives without customer/order conversion."}
{"row_type": "residual_contribution", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "new_axis_proposed": "C07_HBM_EQUIPMENT_ORDER_CONVERSION_VS_RS_BLOWOFF_GATE", "sector_specific_rule_candidate": "L2 HBM equipment should not award Stage2-Actionable from relative strength or HBM capex beta alone; require equipment-specific order, customer qualification, or revenue/margin conversion bridge.", "canonical_archetype_rule_candidate": "C07 Stage2-Actionable requires at least two of named HBM equipment, explicit customer/order/qualification, deliverable timing, revenue/margin conversion, repeat order pipeline. A one-off beneficiary article stays Stage2 watch or 4B/4C depending price path.", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "earlier_thesis_break_watch", "hard_4c_confirmation"], "existing_axis_weakened": [], "do_not_propose_new_weight_delta": false}
```

## 20. Batch ingest self-audit

```text
required_filename_regex_pass = true
filename_round_matches_metadata_round = true
filename_loop_matches_metadata_loop = true
round_sector_consistency = pass
selected_round = R2
selected_loop = 128
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
trigger_type_canonical_stage_label_only = true
all_trigger_rows_have_MFE_30D_pct = true
all_trigger_rows_have_MFE_90D_pct = true
all_trigger_rows_have_MFE_180D_pct = true
all_trigger_rows_have_MAE_30D_pct = true
all_trigger_rows_have_MAE_90D_pct = true
all_trigger_rows_have_MAE_180D_pct = true
rows_missing_required_mfe_mae = 0
corporate_action_contaminated_180D_rows = 0
insufficient_forward_window_rows = 0
source_proxy_only_count = 3
evidence_url_pending_count = 0
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 21. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent for stock_agent. Do not execute this handoff during the research run that produced this file.

Task:
1. Ingest this MD as a standard v12 result file.
2. Parse row_type=trigger, score_simulation, shadow_weight, and residual_contribution JSONL rows.
3. Validate required MFE/MAE fields and canonical trigger_type labels.
4. Treat C07_R2_L128_001~003 as representative positive/order-conversion rows.
5. Treat C07_R2_L128_004 and C07_R2_L128_006 as 4B overlay guardrail rows.
6. Treat C07_R2_L128_005 as a 4C/order-conversion failure guardrail row.
7. Do not immediately change production scoring. Add the axis C07_HBM_EQUIPMENT_ORDER_CONVERSION_VS_RS_BLOWOFF_GATE to shadow evaluation only.
```

## 22. Next research state

```text
completed_round = R2
completed_loop = 128
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C07 4C-empty, source/proxy repair, direct order-conversion vs relative-strength blowoff split
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY; C14_EV_DEMAND_SLOWDOWN_4B_4C; C28_SOFTWARE_SECURITY_CONTRACT_RETENTION; C05_EPC_MEGA_CONTRACT_MARGIN_GAP
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
