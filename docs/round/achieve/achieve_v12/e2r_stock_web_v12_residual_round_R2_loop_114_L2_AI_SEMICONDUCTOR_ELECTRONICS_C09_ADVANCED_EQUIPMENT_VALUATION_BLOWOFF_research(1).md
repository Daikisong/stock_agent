# E2R Stock-Web V12 Residual Research — R2 loop 114 / L2 / C09

```yaml
research_id: R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS
output_file: e2r_stock_web_v12_residual_round_R2_loop_114_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
completed_round: R2
completed_loop: 114
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows / C09 rows 10 need_to_30 20
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: mixed_C09_advanced_metrology_inspection_optional_equipment_second_pass_set
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection / novelty check

V12 scheduler is coverage-index-first, not round-cycle-first. The No-Repeat ledger places `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` in Priority 0 with 10 rows and 20 rows still needed to reach 30. This second-pass C09 file uses five symbols not used in the prior C09 loop in this conversation.

Prior C09 loop in current session used: `322310`, `348210`, `240810`, `319660`, `101490`.

This file uses only new C09 symbols: `036930`, `140860`, `064290`, `036810`, `098460`.

Hard duplicate key check:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No hard duplicate was intentionally reused.

## 2. Research question

C09 is the archetype where semiconductor advanced-equipment narratives often look structurally correct while valuation, product-launch optionality, or order timing turns the actual path into high-MAE. The target question is:

> When should advanced-equipment evidence be allowed to become Stage3-Yellow, and when should it be capped as Stage2-Actionable / 4B watch because signed order, delivery timing, revenue recognition, or margin bridge is still missing?

The answer emerging from this pass is not simply “advanced equipment is dangerous.” The better rule is a split:

```text
allow_positive_path_if = named process demand + credible order trend + revenue/margin conversion visibility
cap_or_4B_if = product launch / optional customer qualification / theme-only valuation expansion without signed order or revenue bridge
```

## 3. Price atlas validation

Price data was read from `Songdaiki/stock-web` tradable symbol-year shards:

```text
atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv
atlas/ohlcv_tradable_by_symbol_year/036/036930/2025.csv
atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv
atlas/ohlcv_tradable_by_symbol_year/140/140860/2025.csv
atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv
atlas/ohlcv_tradable_by_symbol_year/064/064290/2025.csv
atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv
atlas/ohlcv_tradable_by_symbol_year/036/036810/2025.csv
atlas/ohlcv_tradable_by_symbol_year/098/098460/2024.csv
atlas/ohlcv_tradable_by_symbol_year/098/098460/2025.csv
```

`entry_date` is the next tradable day after the trigger date when report/publication timing is not guaranteed before the close. MFE/MAE is calculated from entry-date close against subsequent tradable-window highs/lows.

Corporate action screen:

```text
036930: CA candidate only 2000-06-22 -> clean 2024 180D window
140860: CA candidate count 0 -> clean
064290: CA candidate count 0 -> clean
036810: CA candidates 2000-05-02, 2004-06-17 -> clean 2024 180D window
098460: latest CA candidate 2021-04-13 -> clean 2024 180D window
```

## 4. Case table

| symbol | name | trigger_type | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | role |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 036930 | 주성엔지니어링 | Stage2-Actionable | 2024-04-03 | 35,300 | 17.42 | -10.34 | 17.42 | -37.25 | 17.42 | -37.54 | counterexample |
| 140860 | 파크시스템스 | Stage3-Yellow | 2024-04-01 | 167,700 | 3.40 | -17.05 | 18.43 | -17.05 | 33.57 | -17.05 | positive |
| 064290 | 인텍플러스 | 4B | 2024-03-13 | 36,500 | 6.58 | -19.73 | 6.58 | -47.97 | 6.58 | -76.00 | counterexample |
| 036810 | 에프에스티 | Stage2-Actionable | 2024-02-21 | 22,350 | 10.96 | -2.01 | 87.25 | -2.01 | 87.25 | -27.83 | positive_with_4B_watch |
| 098460 | 고영 | 4B | 2024-03-07 | 20,250 | 7.65 | -17.04 | 7.65 | -39.95 | 7.65 | -60.10 | counterexample |

## 5. Case notes


### Case 1. 036930 주성엔지니어링 — C09_ALD_TECH_MIGRATION_ORDER_BACKLOG_BLOWOFF

- trigger_date: `2024-04-02`
- entry_date / entry_price: `2024-04-03` / `35,300`
- trigger_type: `Stage2-Actionable`
- role: `counterexample`
- evidence_family: ALD tech migration + SK hynix/CXMT order backlog + within-leadtime revenue-recognition expectation
- source: https://ssl.pstatic.net/imgstock/upload/research/company/1712019166097.pdf

2024-04-02 report framed Jusung as a tech-migration ALD beneficiary with 2023 year-end semiconductor equipment backlog of KRW 230.2bn and 2024 semiconductor equipment revenue expectation of KRW 368bn, but the price path peaked within days and then suffered a large 90D/180D MAE. This is not a clean Stage3 evidence path without post-order margin/revenue validation.

Price path: 30D MFE/MAE `17.42% / -10.34%`, 90D `17.42% / -37.25%`, 180D `17.42% / -37.54%`. Peak inside 180D was `2024-04-08` at `41,450`, followed by drawdown_after_peak `-46.80%`.

Rule interpretation: cap_to_Stage2_Actionable_or_local_4B_watch_until quarterly revenue recognition and margin bridge are confirmed

### Case 2. 140860 파크시스템스 — C09_AFM_HBM_NANOMETROLOGY_ORDER_MOMENTUM

- trigger_date: `2024-03-29`
- entry_date / entry_price: `2024-04-01` / `167,700`
- trigger_type: `Stage3-Yellow`
- role: `positive`
- evidence_family: AFM global #1 + HBM/advanced process metrology + China/order growth expectations
- source: https://v.daum.net/v/ysn3GGva0J

The 2024-03-29 HBM/AFM thesis argued that Park Systems' industrial AFM is exposed to HBM and advanced-process metrology demand. The path had an early 30D drawdown but then reached +33.57% 180D MFE and +49.08% 1Y MFE, so C09 should not hard-cap every advanced-equipment valuation case; it needs an order/revenue-conversion gate and a 30D MAE buffer.

Price path: 30D MFE/MAE `3.40% / -17.05%`, 90D `18.43% / -17.05%`, 180D `33.57% / -17.05%`. Peak inside 180D was `2024-11-07` at `224,000`, followed by drawdown_after_peak `-25.45%`.

Rule interpretation: allow Stage3-Yellow when AFM/inspection demand is tied to named process demand and later order/revenue confirmation, but avoid Green until margin bridge appears

### Case 3. 064290 인텍플러스 — C09_ADVANCED_PACKAGING_INSPECTION_OPTIONAL_ORDER_DELAY

- trigger_date: `2024-03-12`
- entry_date / entry_price: `2024-03-13` / `36,500`
- trigger_type: `4B`
- role: `counterexample`
- evidence_family: advanced package inspection + 2.5D PKG setup + HBM4 hybrid-bonding R&D optionality
- source: https://files-scs.pstatic.net/2024/03/12/v2v0YGr2Ki/240312%28%ED%99%94%29%20%EC%A6%9D%EA%B6%8C%EC%82%AC%EB%A6%AC%ED%8F%AC%ED%8A%B8.pdf

The 2024-03-12 report gave a strong advanced-packaging inspection thesis with 2.5D PKG setup and next-generation inspection R&D, but the path produced only +6.58% MFE and -76.00% 180D MAE. This is a clean C09 false-positive where optional HBM inspection demand cannot substitute for confirmed high-margin order/revenue conversion.

Price path: 30D MFE/MAE `6.58% / -19.73%`, 90D `6.58% / -47.97%`, 180D `6.58% / -76.00%`. Peak inside 180D was `2024-03-13` at `38,900`, followed by drawdown_after_peak `-77.48%`.

Rule interpretation: route to 4B watch unless order is named, delivery timing is visible, and margin mix is not diluted by low-margin battery/display equipment

### Case 4. 036810 에프에스티 — C09_EUV_PELLICLE_OPTIONALITY_BLOWOFF_AND_DELAY_CAP

- trigger_date: `2024-02-20`
- entry_date / entry_price: `2024-02-21` / `22,350`
- trigger_type: `Stage2-Actionable`
- role: `positive_with_4B_watch`
- evidence_family: EUV pellicle pilot production expectation + chiller/pellicle semiconductor capex optionality
- source: https://ssl.pstatic.net/imgstock/upload/research/company/1708384069435.pdf

The 2024-02-20 KIRS report framed EUV pellicle market entry and 2024 H2 pilot production as a valuation unlock. The path delivered +87.25% 90D/180D MFE but then fell sharply after the June peak, so the rule should preserve Stage2-Actionable upside while forcing local 4B watch once revenue qualification remains optional and price outruns order evidence.

Price path: 30D MFE/MAE `10.96% / -2.01%`, 90D `87.25% / -2.01%`, 180D `87.25% / -27.83%`. Peak inside 180D was `2024-06-11` at `41,850`, followed by drawdown_after_peak `-61.46%`.

Rule interpretation: keep as Stage2-Actionable/Yellow candidate only while qualification or supply confirmation emerges; force local 4B after fast MFE with no revenue bridge

### Case 5. 098460 고영 — C09_WLP_INSPECTION_PRODUCT_LAUNCH_NO_ORDER_CONVERSION

- trigger_date: `2024-03-06`
- entry_date / entry_price: `2024-03-07` / `20,250`
- trigger_type: `4B`
- role: `counterexample`
- evidence_family: ZenStar WLP inspection launch + on-device AI/advanced-packaging thematic demand
- source: https://www.thebell.co.kr/front/newsview.asp?key=202403060813170400108350

The 2024-03-06 ZenStar launch linked WLP inspection to on-device AI and advanced packaging, but product launch evidence alone had no named customer order or revenue bridge. The path had +7.65% MFE and -60.10% 180D MAE, so C09 needs an explicit launch-to-order conversion gate.

Price path: 30D MFE/MAE `7.65% / -17.04%`, 90D `7.65% / -39.95%`, 180D `7.65% / -60.10%`. Peak inside 180D was `2024-03-07` at `21,800`, followed by drawdown_after_peak `-62.94%`.

Rule interpretation: block positive Stage2/3 unless product launch is followed by named customer order, revenue recognition, or repeat procurement evidence


## 6. Aggregate interpretation

```yaml
usable_trigger_count: 5
positive_case_count: 2
counterexample_count: 3
local_4B_watch_count: 4
hard_4C_count: 0
mean_MFE_180D_pct: 30.49
median_MFE_180D_pct: 17.42
mean_MAE_180D_pct: -43.7
median_MAE_180D_pct: -37.54
high_MAE_below_minus_30_count: 3
high_MAE_below_minus_50_count: 2
current_profile_error_count: 4
```

The mean MFE is inflated by one fast blowoff case, while the median 180D MAE is deeply negative. That is exactly the C09 danger pattern: the archetype can produce spectacular MFE, but the same evidence family also produces large capital impairment when price is moving faster than signed-order and revenue-recognition evidence.

## 7. Current calibrated profile stress test

Current profile guardrails already contain `price_only_blowoff_blocks_positive_stage` and `full_4b_requires_non_price_evidence`. This pass suggests those global guards are directionally correct but still too coarse for C09. The missing C09-specific distinction is:

```text
metrology / inspection / pellicle / ALD theme evidence must be separated into:
1. signed-or-named demand with delivery/revenue visibility
2. product launch or optional qualification without order conversion
3. fast-MFE blowoff where 4B should activate locally even if the full-window thesis remains alive
```

## 8. Proposed sector/canonical shadow rule

```text
C09_SIGNED_ORDER_REVENUE_BRIDGE_AND_OPTIONALITY_4B_CAP_SECOND_PASS
```

Rule body:

```text
For C09, do not allow Stage3-Yellow from advanced-equipment product launch, HBM adjacency, EUV optionality, or metrology TAM expansion alone.
Require at least one of:
- signed/named customer order,
- visible delivery or setup timing,
- within-12-month revenue recognition bridge,
- margin mix not diluted by low-margin non-core equipment,
- later quarter revenue/OP confirmation.

If 30~90D MFE exceeds +50% before this bridge appears, activate local 4B watch even if the 180D full thesis is not broken.
```

Shadow weight direction, not applied now:

```yaml
do_not_propose_new_weight_delta: false
production_scoring_patch_applied: false
suggested_delta_not_applied:
  earnings_visibility: +2.0
  information_confidence: +1.5
  bottleneck_pricing: -1.0
  valuation_rerating: -1.5
```

## 9. Machine-readable rows

```jsonl
{"row_type": "trigger", "research_id": "R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS", "selected_round": "R2", "selected_loop": 114, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "symbol": "036930", "company_name": "주성엔지니어링", "fine_archetype_id": "C09_ALD_TECH_MIGRATION_ORDER_BACKLOG_BLOWOFF", "case_role": "counterexample", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-02", "entry_date": "2024-04-03", "entry_price": 35300.0, "MFE_30D_pct": 17.42, "MAE_30D_pct": -10.34, "MFE_90D_pct": 17.42, "MAE_90D_pct": -37.25, "MFE_180D_pct": 17.42, "MAE_180D_pct": -37.54, "MFE_1Y_pct": 22.95, "MAE_1Y_pct": -37.54, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_date": "2024-04-08", "peak_price": 41450.0, "drawdown_after_peak_pct": -46.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "calibration_usable": true, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_status": "clean_180D_profile_CA_only_2000-06-22", "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1712019166097.pdf", "current_profile_error": "would_overpromote_if_order_backlog_and_ALD_theme_are_treated_as_stage3_without_order_to_margin_confirmation", "shadow_rule_effect": "cap_to_Stage2_Actionable_or_local_4B_watch_until quarterly revenue recognition and margin bridge are confirmed", "raw_component_score_breakdown": {"eps_fcf_explosion": 48, "earnings_visibility": 58, "bottleneck_pricing": 64, "market_mispricing": 45, "valuation_rerating": 50, "capital_allocation": 35, "information_confidence": 61}}
{"row_type": "trigger", "research_id": "R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS", "selected_round": "R2", "selected_loop": 114, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "symbol": "140860", "company_name": "파크시스템스", "fine_archetype_id": "C09_AFM_HBM_NANOMETROLOGY_ORDER_MOMENTUM", "case_role": "positive", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-03-29", "entry_date": "2024-04-01", "entry_price": 167700.0, "MFE_30D_pct": 3.4, "MAE_30D_pct": -17.05, "MFE_90D_pct": 18.43, "MAE_90D_pct": -17.05, "MFE_180D_pct": 33.57, "MAE_180D_pct": -17.05, "MFE_1Y_pct": 49.08, "MAE_1Y_pct": -17.05, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_date": "2024-11-07", "peak_price": 224000.0, "drawdown_after_peak_pct": -25.45, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "calibration_usable": true, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_status": "clean_180D_profile_CA_count_0", "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://v.daum.net/v/ysn3GGva0J", "current_profile_error": "too_strict_4B_if_initial_30D_drawdown_blocks_later_order_revenue_confirmation", "shadow_rule_effect": "allow Stage3-Yellow when AFM/inspection demand is tied to named process demand and later order/revenue confirmation, but avoid Green until margin bridge appears", "raw_component_score_breakdown": {"eps_fcf_explosion": 65, "earnings_visibility": 72, "bottleneck_pricing": 78, "market_mispricing": 61, "valuation_rerating": 66, "capital_allocation": 45, "information_confidence": 76}}
{"row_type": "trigger", "research_id": "R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS", "selected_round": "R2", "selected_loop": 114, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "symbol": "064290", "company_name": "인텍플러스", "fine_archetype_id": "C09_ADVANCED_PACKAGING_INSPECTION_OPTIONAL_ORDER_DELAY", "case_role": "counterexample", "trigger_type": "4B", "trigger_date": "2024-03-12", "entry_date": "2024-03-13", "entry_price": 36500.0, "MFE_30D_pct": 6.58, "MAE_30D_pct": -19.73, "MFE_90D_pct": 6.58, "MAE_90D_pct": -47.97, "MFE_180D_pct": 6.58, "MAE_180D_pct": -76.0, "MFE_1Y_pct": 6.58, "MAE_1Y_pct": -77.12, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_date": "2024-03-13", "peak_price": 38900.0, "drawdown_after_peak_pct": -77.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "calibration_usable": true, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_status": "clean_180D_profile_CA_count_0", "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://files-scs.pstatic.net/2024/03/12/v2v0YGr2Ki/240312%28%ED%99%94%29%20%EC%A6%9D%EA%B6%8C%EC%82%AC%EB%A6%AC%ED%8F%AC%ED%8A%B8.pdf", "current_profile_error": "Stage2_or_Stage3_false_positive_if_HBM_inspection_optionality_is_given_bottleneck_weight_without profit-quality decontamination", "shadow_rule_effect": "route to 4B watch unless order is named, delivery timing is visible, and margin mix is not diluted by low-margin battery/display equipment", "raw_component_score_breakdown": {"eps_fcf_explosion": 42, "earnings_visibility": 49, "bottleneck_pricing": 63, "market_mispricing": 38, "valuation_rerating": 37, "capital_allocation": 30, "information_confidence": 55}}
{"row_type": "trigger", "research_id": "R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS", "selected_round": "R2", "selected_loop": 114, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "symbol": "036810", "company_name": "에프에스티", "fine_archetype_id": "C09_EUV_PELLICLE_OPTIONALITY_BLOWOFF_AND_DELAY_CAP", "case_role": "positive_with_4B_watch", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 22350.0, "MFE_30D_pct": 10.96, "MAE_30D_pct": -2.01, "MFE_90D_pct": 87.25, "MAE_90D_pct": -2.01, "MFE_180D_pct": 87.25, "MAE_180D_pct": -27.83, "MFE_1Y_pct": 87.25, "MAE_1Y_pct": -36.51, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_date": "2024-06-11", "peak_price": 41850.0, "drawdown_after_peak_pct": -61.46, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "calibration_usable": true, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_status": "clean_180D_profile_CA_only_2000-05-02_and_2004-06-17", "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1708384069435.pdf", "current_profile_error": "price_momentum_may_mask_optional_revenue_delay_if_local_4B_is_not_triggered_after_fast_MFE", "shadow_rule_effect": "keep as Stage2-Actionable/Yellow candidate only while qualification or supply confirmation emerges; force local 4B after fast MFE with no revenue bridge", "raw_component_score_breakdown": {"eps_fcf_explosion": 59, "earnings_visibility": 55, "bottleneck_pricing": 75, "market_mispricing": 64, "valuation_rerating": 72, "capital_allocation": 35, "information_confidence": 62}}
{"row_type": "trigger", "research_id": "R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS", "selected_round": "R2", "selected_loop": 114, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "symbol": "098460", "company_name": "고영", "fine_archetype_id": "C09_WLP_INSPECTION_PRODUCT_LAUNCH_NO_ORDER_CONVERSION", "case_role": "counterexample", "trigger_type": "4B", "trigger_date": "2024-03-06", "entry_date": "2024-03-07", "entry_price": 20250.0, "MFE_30D_pct": 7.65, "MAE_30D_pct": -17.04, "MFE_90D_pct": 7.65, "MAE_90D_pct": -39.95, "MFE_180D_pct": 7.65, "MAE_180D_pct": -60.1, "MFE_1Y_pct": 9.88, "MAE_1Y_pct": -62.42, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "peak_date": "2024-03-07", "peak_price": 21800.0, "drawdown_after_peak_pct": -62.94, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "calibration_usable": true, "window_30D_corporate_action_contaminated": false, "window_90D_corporate_action_contaminated": false, "window_180D_corporate_action_contaminated": false, "corporate_action_window_status": "clean_180D_profile_CA_latest_2021-04-13", "source_proxy_only": false, "evidence_url_pending": false, "evidence_url": "https://www.thebell.co.kr/front/newsview.asp?key=202403060813170400108350", "current_profile_error": "AI_advanced_packaging_product_launch_can_be_misclassified_as_Stage2_without_named_order_or_margin_bridge", "shadow_rule_effect": "block positive Stage2/3 unless product launch is followed by named customer order, revenue recognition, or repeat procurement evidence", "raw_component_score_breakdown": {"eps_fcf_explosion": 35, "earnings_visibility": 42, "bottleneck_pricing": 52, "market_mispricing": 32, "valuation_rerating": 34, "capital_allocation": 30, "information_confidence": 58}}
{"row_type": "aggregate", "research_id": "R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS", "selected_round": "R2", "selected_loop": 114, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "usable_trigger_count": 5, "positive_case_count": 2, "counterexample_count": 3, "local_4B_watch_count": 4, "hard_4C_count": 0, "mean_MFE_180D_pct": 30.49, "median_MFE_180D_pct": 17.42, "mean_MAE_180D_pct": -43.7, "median_MAE_180D_pct": -37.54, "high_MAE_below_minus_30_count": 3, "high_MAE_below_minus_50_count": 2, "current_profile_error_count": 4, "rule_candidate": "C09_SIGNED_ORDER_REVENUE_BRIDGE_AND_OPTIONALITY_4B_CAP_SECOND_PASS"}
{"row_type": "shadow_weight_candidate", "research_id": "R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "rule_candidate": "C09_SIGNED_ORDER_REVENUE_BRIDGE_AND_OPTIONALITY_4B_CAP_SECOND_PASS", "direction": "increase penalty on product-launch/order-optionality; increase weight on signed order and revenue-recognition bridge; retain positive pathway for metrology/AFM with confirmed order trend", "suggested_delta_not_applied": {"earnings_visibility": 2.0, "information_confidence": 1.5, "bottleneck_pricing": -1.0, "valuation_rerating": -1.5}, "production_scoring_patch_applied": false, "handoff_prompt_executed_now": false}
{"row_type": "residual_contribution", "research_id": "R2_L114_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_SECOND_PASS", "contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": ["C09_SIGNED_ORDER_REVENUE_BRIDGE_AND_OPTIONALITY_4B_CAP_SECOND_PASS", "C09_PRODUCT_LAUNCH_NO_ORDER_CONVERSION_BLOCK", "C09_FAST_MFE_LOCAL_4B_AFTER_OPTIONAL_REVENUE_DELAY"], "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "stage2_required_bridge"], "existing_axis_weakened": [], "next_recommended_archetypes": ["C14_EV_DEMAND_SLOWDOWN_4B_4C", "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "C06_HBM_MEMORY_CUSTOMER_CAPACITY"]}
```

## 10. Source register

```yaml
main_execution_prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
stock_web_manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
stock_web_schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
profiles:
  036930: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/036/036930.json
  140860: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/140/140860.json
  064290: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/064/064290.json
  036810: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/036/036810.json
  098460: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/098/098460.json
evidence_sources:
  036930: https://ssl.pstatic.net/imgstock/upload/research/company/1712019166097.pdf
  140860: https://v.daum.net/v/ysn3GGva0J
  140860_validation: https://securities.miraeasset.com/bbs/download/2126453.pdf?attachmentId=2126453
  064290: https://files-scs.pstatic.net/2024/03/12/v2v0YGr2Ki/240312%28%ED%99%94%29%20%EC%A6%9D%EA%B6%8C%EC%82%AC%EB%A6%AC%ED%8F%AC%ED%8A%B8.pdf
  064290_validation: https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%9D%B8%ED%85%8D%ED%94%8C%EB%9F%AC%EC%8A%A4.pdf
  036810: https://ssl.pstatic.net/imgstock/upload/research/company/1708384069435.pdf
  036810_validation: https://securities.miraeasset.com/bbs/download/2129096.pdf?attachmentId=2129096
  098460: https://www.thebell.co.kr/front/newsview.asp?key=202403060813170400108350
  098460_backup: https://www.etnews.com/20240306000302
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session.

```text
You are a later coding agent working inside /home/eorb915/projects/stock_agent.
Ingest this standalone V12 Markdown as a candidate residual research file only.
Do not assume rule adoption from narrative text alone.
Parse the JSONL trigger rows, validate that all usable rows contain entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct, and corporate-action status.
Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
If accepted, attribute contribution to C09_SIGNED_ORDER_REVENUE_BRIDGE_AND_OPTIONALITY_4B_CAP_SECOND_PASS.
Generate shadow-only candidate changes first. Do not directly alter production scoring unless batch validation passes across the broader v12 corpus.
```

## 12. Next research state

```text
completed_round = R2
completed_loop = 114
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C09 rows 10 / need_to_30 20
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 13. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
