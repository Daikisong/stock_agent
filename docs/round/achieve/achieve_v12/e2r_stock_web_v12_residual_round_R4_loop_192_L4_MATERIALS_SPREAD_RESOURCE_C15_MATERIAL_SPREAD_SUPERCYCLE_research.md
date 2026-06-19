# E2R Stock-Web V12 Residual Research — R4 Loop 192 / C15 Material Spread Supercycle

## 0. Execution Metadata

| Field | Value |
|---|---|
| main_execution_prompt | `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` |
| no_repeat_index | `docs/core/V12_Research_No_Repeat_Index.md` |
| selected_round | `R4` |
| selected_loop | `192` |
| round_schedule_status | `coverage_index_selected` |
| large_sector_id | `L4_MATERIALS_SPREAD_RESOURCE` |
| canonical_archetype_id | `C15_MATERIAL_SPREAD_SUPERCYCLE` |
| fine_archetype_id | `STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE` |
| selection_basis | Priority 1 balance / quality reinforcement after Priority 0 URL-proxy and missing-MFE repair |
| prior_current_session_canonicals_avoided | `C05`, `C01`, `C13`, `C10`, `C14`, `C02`, `R13_*`; C15 reused only with fresh trigger keys |
| stock_agent_code_patch | `false` |
| production_scoring_changed | `false` |
| shadow_weight_only | `true` |
| generated_at_utc | `2026-06-15T14:47:18Z` |

## 1. Scheduler / No-Repeat Decision

The current index says all `C01`~`C32` buckets are now above 80 representative rows, so this run does not chase raw row count.  The index's next useful work is quality reinforcement: reduce URL/proxy and missing-MFE debt, then rebalance archetypes that still need cleaner positive/counterexample and 4B/4C separation.  The current-session outputs already covered `C05`, `C01`, and `C13`, so this file selects `C15_MATERIAL_SPREAD_SUPERCYCLE` under `R4 / L4`.

This batch avoids the hard duplicate key format:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Every case below has a fresh trigger date within this batch.  No row is marked promotion-eligible without actual stock-web OHLCV and 30/90/180D MFE/MAE.

## 2. Stock-Web Price Source Validation

| Field | Value |
|---|---|
| primary_price_source | `Songdaiki/stock-web` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| manifest_max_date | `2026-02-20` |
| MFE definition | max high from entry row through N tradable rows divided by entry close |
| MAE definition | min low from entry row through N tradable rows divided by entry close |
| corporate_action_rule | D~D+180 contamination blocks calibration use |

All entry rows below are actual 1D OHLCV rows from stock-web tradable shards.  Every selected row has at least 180 forward tradable rows inside the available manifest window and is marked `calibration_usable=true`.

## 3. Batch Ingest Self-Audit

```text
new_independent_case_count: 9
new_independent_trigger_count: 9
unique_symbol_count: 5

calibration_usable_case_count: 9
calibration_usable_trigger_count: 9

positive_case_count: 2
counterexample_or_guardrail_case_count: 7
Stage4B_case_count: 2
Stage4C_case_count: 2

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

new_independent_ratio: 1.00
production_scoring_changed: false
shadow_weight_only: true
```

## 4. Case Selection Table

|case_id|symbol|company|trigger_type|case_role|trigger_date|entry_date|MFE180|MAE180|DD_after_peak|evidence_url|
|---|---|---|---|---|---|---|---|---|---|---|
|C15_192_01_POSCO_2020_4Q_SPREAD_RECOVERY|005490|POSCO Holdings|Stage2-Actionable|positive|2021-01-28|2021-01-28|65.40|-3.00|-27.21|direct_url|
|C15_192_02_HYUNDAI_STEEL_1Q21_LATE_STEEL_CHASE|004020|Hyundai Steel|Stage2|counterexample_high_mae|2021-04-27|2021-04-27|11.11|-34.66|-41.19|direct_url|
|C15_192_03_POONGSAN_COPPER_PRICE_VOLUME_BRIDGE|103140|Poongsan|Stage2-Actionable|positive|2021-02-22|2021-02-22|36.48|-14.89|-37.64|direct_url|
|C15_192_04_POSCO_2021_RECORD_BUT_QOQ_MARGIN_ROLLOVER|005490|POSCO Holdings|Stage4B|guardrail|2022-01-28|2022-01-28|15.66|-20.38|-31.16|direct_url|
|C15_192_05_POONGSAN_2022_HIGH_BASE_COPPER_COUNTER|103140|Poongsan|Stage4B|counterexample|2022-03-18|2022-03-18|4.62|-28.20|-31.37|direct_url|
|C15_192_06_SOIL_Q2_2022_REFINING_MARGIN_LATE|010950|S-Oil|Stage2-Actionable|mixed_green_blocker|2022-07-28|2022-07-28|18.84|-17.63|-30.69|direct_url|
|C15_192_07_SKI_Q2_2022_INVENTORY_GAIN_WORKING_CAPITAL_OFFSET|096770|SK Innovation|Stage2-Actionable|mixed_green_blocker|2022-07-29|2022-07-29|13.87|-24.00|-33.26|direct_url|
|C15_192_08_SOIL_2023_WEAK_REFINING_MARGIN_4C|010950|S-Oil|Stage4C|correct_4c|2023-04-25|2023-04-25|5.06|-19.22|-20.02|direct_url|
|C15_192_09_SKI_Q4_2022_INVENTORY_LOSS_OFFSET_CHECK|096770|SK Innovation|Stage4C|overhard_4c_offset_check|2023-02-07|2023-02-07|41.14|-26.14|-47.67|direct_url|

## 5. Actual Stock-Web 1D Entry Rows and Forward Path

|symbol|entry_date|o|h|l|c|v|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|DD_after_peak|window_last|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|005490|2021-01-28|254000|255500|246000|250000|512201|33.60|-3.00|65.40|-3.00|65.40|-3.00|2021-05-10|-27.21|2021-10-22|
|004020|2021-04-27|52600|57000|52400|56700|5322376|11.11|-10.93|11.11|-20.19|11.11|-34.66|2021-05-11|-41.19|2022-01-17|
|103140|2021-02-22|33950|37400|33700|36600|2877677|8.47|-14.89|36.48|-14.89|36.48|-14.89|2021-05-12|-37.64|2021-11-12|
|005490|2022-01-28|260000|267000|256500|265000|333753|11.13|-3.21|15.66|-3.21|15.66|-20.38|2022-03-23|-31.16|2022-10-26|
|103140|2022-03-18|32400|32450|31900|32450|136535|4.62|-4.01|4.62|-28.20|4.62|-28.20|2022-03-24|-31.37|2022-12-07|
|010950|2022-07-28|93600|93800|90500|91300|538463|18.84|-7.12|18.84|-15.12|18.84|-17.63|2022-08-30|-30.69|2023-04-19|
|096770|2022-07-29|183000|191000|182500|187500|688623|13.87|-5.33|13.87|-24.00|13.87|-24.00|2022-08-17|-33.26|2023-04-20|
|010950|2023-04-25|77700|78300|76800|77000|272017|1.69|-8.31|4.29|-19.22|5.06|-19.22|2023-09-15|-20.02|2024-01-19|
|096770|2023-02-07|171200|175000|162600|162600|1554857|10.64|-7.75|28.54|-7.75|41.14|-26.14|2023-07-26|-47.67|2023-11-01|

## 6. Case Notes

### 6.1 `005490` POSCO Holdings — 2020 4Q spread recovery (`Stage2-Actionable`, positive)

Evidence: POSCO's 2020 release showed parent 4Q operating profit rising QoQ as WTP sales expanded and product prices increased; the consolidated steel segment also improved QoQ.  The stock-web path after the 2021-01-28 entry delivered 180D MFE of `65.40%` with MAE of only `-3.00%`.  This is the clean positive template for C15: product-price bridge + mix improvement + steel-sector OP recovery.

### 6.2 `004020` Hyundai Steel — Q1 2021 profit swing but late steel chase (`Stage2`, counterexample)

Evidence: Hyundai Steel swung to profit in Q1 2021 on strong sales amid the global recovery.  The entry row still produced only `11.11%` 180D MFE and `-34.66%` MAE, so the research label is not positive.  For C15, a profit-swing headline after a commodity spread run-up should be capped unless the next spread leg is visible.

### 6.3 `103140` Poongsan — copper price and volume bridge (`Stage2-Actionable`, positive)

Evidence: copper near US$9,000/t and OP growth forecasts created a true price-volume bridge.  The 180D MFE was `36.48%`, but the `-14.89%` MAE and post-peak drawdown mean this should remain Stage2-Actionable / Yellow-quality, not automatic Green.

### 6.4 `005490` POSCO Holdings — record annual profit but 4Q margin rollover (`Stage4B`, guardrail)

Evidence: POSCO's 2021 annual result was record-level, but the same release showed 4Q profit downturn and margin tightening due to coal/raw-material pressure.  The 180D MFE was only `15.66%` while MAE reached `-20.38%`.  The residual lesson is that record annual earnings can be a lagging commodity signal when QoQ spread has already rolled over.

### 6.5 `103140` Poongsan — 2022 high-base copper counterexample (`Stage4B`, counterexample)

Evidence: the 2022 report still expected record revenue from copper strength, but explicitly warned operating profit would contract due to high base.  The actual path delivered `4.62%` MFE and `-28.20%` MAE.  C15 should treat high-base language as a spread-persistence blocker.

### 6.6 `010950` S-Oil — Q2 2022 refining margin and inventory gain (`Stage2-Actionable`, mixed Green blocker)

Evidence: Q2 2022 profit surged on widened refining margins and higher oil prices.  The path had positive MFE (`18.84%`) but also `-17.63%` MAE and a `-30.69%` post-peak drawdown.  Refining margin/inventory-gain evidence is actionable but not Green without forward crack-spread persistence.

### 6.7 `096770` SK Innovation — Q2 2022 inventory gain with working-capital offset (`Stage2-Actionable`, mixed Green blocker)

Evidence: SK Innovation reported KRW2.33T operating profit from improved refining margins and inventory gains, while also noting working-capital/net-debt pressure and ongoing battery losses.  The actual path showed `13.87%` MFE and `-24.00%` MAE.  C15 should separate realized inventory gains from sustainable ex-inventory margin.

### 6.8 `010950` S-Oil — 2023 weak refining margin (`Stage4C`, correct 4C)

Evidence: weak refining margins later cut S-Oil's annual operating profit sharply.  The path had only `5.06%` 180D MFE and `-19.22%` MAE.  This is a good hard-4C example when margin deterioration is earnings-quality deterioration, not just daily commodity volatility.

### 6.9 `096770` SK Innovation — Q4 2022 inventory-loss hard-4C offset check (`Stage4C`, overhard 4C offset check)

Evidence: SK Innovation's Q4 loss widened due to inventory losses from lower oil prices and narrower margins, but battery revenue ramp offered a separate offset option.  The stock-web path delivered `41.14%` 180D MFE before a large drawdown.  The C15 residual is not to ignore the refining 4C signal; it is to require an issuer-level offset check before routing a multi-segment issuer into hard 4C.

## 7. Raw Component Score Breakdown

Component order follows the current E2R scoring vocabulary: `eps_fcf_explosion`, `earnings_visibility`, `bottleneck_pricing`, `market_mispricing`, `valuation_rerating`, `capital_allocation`, `information_confidence`.

- `C15_192_01_POSCO_2020_4Q_SPREAD_RECOVERY` `005490`: {"eps_fcf_explosion": 16, "earnings_visibility": 10, "bottleneck_pricing": 19, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 6, "information_confidence": 16, "total_proxy": 83}
- `C15_192_02_HYUNDAI_STEEL_1Q21_LATE_STEEL_CHASE` `004020`: {"eps_fcf_explosion": 15, "earnings_visibility": 10, "bottleneck_pricing": 17, "market_mispricing": 8, "valuation_rerating": 9, "capital_allocation": 4, "information_confidence": 11, "total_proxy": 74}
- `C15_192_03_POONGSAN_COPPER_PRICE_VOLUME_BRIDGE` `103140`: {"eps_fcf_explosion": 15, "earnings_visibility": 10, "bottleneck_pricing": 19, "market_mispricing": 9, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 12, "total_proxy": 77}
- `C15_192_04_POSCO_2021_RECORD_BUT_QOQ_MARGIN_ROLLOVER` `005490`: {"eps_fcf_explosion": 18, "earnings_visibility": 11, "bottleneck_pricing": 13, "market_mispricing": 7, "valuation_rerating": 7, "capital_allocation": 5, "information_confidence": 15, "total_proxy": 76}
- `C15_192_05_POONGSAN_2022_HIGH_BASE_COPPER_COUNTER` `103140`: {"eps_fcf_explosion": 11, "earnings_visibility": 9, "bottleneck_pricing": 18, "market_mispricing": 9, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 16, "total_proxy": 75}
- `C15_192_06_SOIL_Q2_2022_REFINING_MARGIN_LATE` `010950`: {"eps_fcf_explosion": 17, "earnings_visibility": 9, "bottleneck_pricing": 18, "market_mispricing": 7, "valuation_rerating": 8, "capital_allocation": 5, "information_confidence": 15, "total_proxy": 79}
- `C15_192_07_SKI_Q2_2022_INVENTORY_GAIN_WORKING_CAPITAL_OFFSET` `096770`: {"eps_fcf_explosion": 18, "earnings_visibility": 8, "bottleneck_pricing": 18, "market_mispricing": 7, "valuation_rerating": 7, "capital_allocation": 4, "information_confidence": 16, "total_proxy": 78}
- `C15_192_08_SOIL_2023_WEAK_REFINING_MARGIN_4C` `010950`: {"eps_fcf_explosion": 8, "earnings_visibility": 7, "bottleneck_pricing": 8, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 4, "information_confidence": 12, "total_proxy": 53}
- `C15_192_09_SKI_Q4_2022_INVENTORY_LOSS_OFFSET_CHECK` `096770`: {"eps_fcf_explosion": 6, "earnings_visibility": 7, "bottleneck_pricing": 6, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 5, "information_confidence": 14, "total_proxy": 54}

## 8. Current-vs-Shadow Stage Simulation

|case_id|symbol|current_stage|current_score|shadow_stage|shadow_score|delta|residual|
|---|---|---|---|---|---|---|---|
|C15_192_01_POSCO_2020_4Q_SPREAD_RECOVERY|005490|Stage2-Actionable|78|Stage2-Actionable|83|5|true spread bridge: product price + mix + steel-sector OP recovery all appear before the 180D rerating|
|C15_192_02_HYUNDAI_STEEL_1Q21_LATE_STEEL_CHASE|004020|Stage2|74|Stage4B|58|-16|late steel-spread chase: profit swing alone should not override peak-margin/late-cycle MAE guard|
|C15_192_03_POONGSAN_COPPER_PRICE_VOLUME_BRIDGE|103140|Stage2-Actionable|77|Stage2-Actionable|81|4|clean copper-price positive, but MAE still argues Yellow/Actionable rather than Green unless sell-through and hedge quality are verified|
|C15_192_04_POSCO_2021_RECORD_BUT_QOQ_MARGIN_ROLLOVER|005490|Stage2|76|Stage4B|60|-16|record annual earnings can be a lagging signal once QoQ steel margin has rolled over|
|C15_192_05_POONGSAN_2022_HIGH_BASE_COPPER_COUNTER|103140|Stage2|75|Stage4B|56|-19|high-base language must cap C15 Stage2 because spread persistence is no longer incremental|
|C15_192_06_SOIL_Q2_2022_REFINING_MARGIN_LATE|010950|Stage2-Actionable|79|Stage2|68|-11|refining margin and inventory gains are actionable but should be Green-blocked without forward crack-spread persistence|
|C15_192_07_SKI_Q2_2022_INVENTORY_GAIN_WORKING_CAPITAL_OFFSET|096770|Stage2-Actionable|78|Stage2|64|-14|inventory-gain positive needs working-capital/debt offset before Yellow or Green|
|C15_192_08_SOIL_2023_WEAK_REFINING_MARGIN_4C|010950|Stage4B|62|Stage4C|49|-13|when refining-margin weakness is not just local price volatility but earnings-quality deterioration, hard 4C is appropriate|
|C15_192_09_SKI_Q4_2022_INVENTORY_LOSS_OFFSET_CHECK|096770|Stage4C|54|Stage4B|59|5|hard 4C on refining/inventory loss needs offset-check where another segment has credible ramp optionality|

## 9. Residual Contribution

```text
residual_contribution_label:
C15_spread_persistence_inventory_gain_and_hard_4c_offset_repair

new_axis_proposed: false
existing_axis_strengthened:
- Stage2 required bridge
- earlier thesis-break watch
- full-window 4B vs hard 4C distinction

existing_axis_refined:
- spread-persistence gate
- inventory-gain / working-capital offset
- issuer-level hard-4C offset check

existing_axis_weakened:
- commodity-price-only rerating
- record-annual-earnings as standalone positive signal
```

### Proposed shadow rule candidate

```text
C15_SPREAD_PERSISTENCE_AND_INVENTORY_GAIN_GATE:
  If the C15 thesis is driven by commodity spread, crack spread, metal price,
  or inventory gain, cap the case at Stage2 unless at least one of the following
  is directly evidenced:
    1. forward spread persistence or price contract reset,
    2. ex-inventory margin bridge,
    3. volume / utilization / mix support independent of commodity price,
    4. working-capital and debt burden remain controlled.

C15_HARD_4C_OFFSET_CHECK:
  Route to hard 4C only when margin deterioration is issuer-level thesis break.
  For multi-segment issuers, check whether another segment has credible
  non-spread offset before applying hard 4C globally.
```

## 10. Shadow Weight Rows

```jsonl
{"row_type": "shadow_weight_delta", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "component": "bottleneck_pricing", "before": 20, "after_shadow": 18, "delta": -2, "reason": "Spread/commodity price alone had high late-cycle MAE in steel/copper/refining."}
{"row_type": "shadow_weight_delta", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "component": "information_confidence", "before": 20, "after_shadow": 22, "delta": 2, "reason": "Direct evidence must separate realized margin bridge, inventory gain, and forward spread persistence."}
{"row_type": "shadow_weight_delta", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "component": "earnings_visibility", "before": 12, "after_shadow": 14, "delta": 2, "reason": "Green/Yellow requires forward visibility, not lagging record earnings."}
{"row_type": "guardrail_delta", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "guardrail": "C15_SPREAD_PERSISTENCE_AND_INVENTORY_GAIN_GATE", "before": "implicit", "after_shadow": "explicit", "delta": "add", "reason": "Inventory-gain or peak-margin evidence should block Green unless forward crack/spread persistence or ex-inventory margin bridge is present."}
{"row_type": "guardrail_delta", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "guardrail": "C15_HARD_4C_OFFSET_CHECK", "before": "weak", "after_shadow": "strengthen", "delta": "refine", "reason": "Hard 4C should verify whether another segment has credible non-spread offset before routing entire issuer to 4C."}
```

## 11. Machine-Readable Trigger Rows

```jsonl
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_01_POSCO_2020_4Q_SPREAD_RECOVERY", "symbol": "005490", "company": "POSCO Holdings", "trigger_type": "Stage2-Actionable", "case_role": "positive", "trigger_date": "2021-01-28", "entry_date": "2021-01-28", "entry_price": 250000.0, "actual_1d_ohlcv": {"o": 254000.0, "h": 255500.0, "l": 246000.0, "c": 250000.0, "v": 512201}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "profile_note": "profile checked: 0 corporate-action candidates, 1995-05-02~2026-02-20 active-like", "forward_window": {"MFE_30D_pct": 33.6, "MAE_30D_pct": -3.0, "MFE_90D_pct": 65.4, "MAE_90D_pct": -3.0, "MFE_180D_pct": 65.4, "MAE_180D_pct": -3.0, "peak_date_180D": "2021-05-10", "peak_price_180D": 413500.0, "trough_after_peak_date_180D": "2021-10-22", "drawdown_after_peak_pct": -27.21, "window_last_date_180D": "2021-10-22", "forward_rows_available": 995}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "2020 earnings release showed 4Q steel profitability improving with product-price increases and WTP mix expansion after the COVID trough.", "evidence_url": "https://www.posco.co.kr/homepage/servlet/FileDownLoad?fileCategory=irDataFd&fileNum=372", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 16, "earnings_visibility": 10, "bottleneck_pricing": 19, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 6, "information_confidence": 16}, "score_simulation": {"current_profile_stage": "Stage2-Actionable", "current_profile_score": 78, "shadow_stage": "Stage2-Actionable", "shadow_score": 83}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|005490|Stage2-Actionable|2021-01-28", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "true spread bridge: product price + mix + steel-sector OP recovery all appear before the 180D rerating"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_02_HYUNDAI_STEEL_1Q21_LATE_STEEL_CHASE", "symbol": "004020", "company": "Hyundai Steel", "trigger_type": "Stage2", "case_role": "counterexample_high_mae", "trigger_date": "2021-04-27", "entry_date": "2021-04-27", "entry_price": 56700.0, "actual_1d_ohlcv": {"o": 52600.0, "h": 57000.0, "l": 52400.0, "c": 56700.0, "v": 5322376}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv", "profile_path": "atlas/symbol_profiles/004/004020.json", "profile_note": "profile checked: historical corporate-action candidates only through 2014; selected 2021 window not contaminated", "forward_window": {"MFE_30D_pct": 11.11, "MAE_30D_pct": -10.93, "MFE_90D_pct": 11.11, "MAE_90D_pct": -20.19, "MFE_180D_pct": 11.11, "MAE_180D_pct": -34.66, "peak_date_180D": "2021-05-11", "peak_price_180D": 63000.0, "trough_after_peak_date_180D": "2021-12-01", "drawdown_after_peak_pct": -41.19, "window_last_date_180D": "2022-01-17", "forward_rows_available": 660}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "Q1 2021 swing-to-profit headline reflected robust recovery and strong sales, but entry came after the steel cycle had already compressed most easy upside.", "evidence_url": "https://en.yna.co.kr/view/AEN20210427007052320", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 10, "bottleneck_pricing": 17, "market_mispricing": 8, "valuation_rerating": 9, "capital_allocation": 4, "information_confidence": 11}, "score_simulation": {"current_profile_stage": "Stage2", "current_profile_score": 74, "shadow_stage": "Stage4B", "shadow_score": 58}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|004020|Stage2|2021-04-27", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "late steel-spread chase: profit swing alone should not override peak-margin/late-cycle MAE guard"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_03_POONGSAN_COPPER_PRICE_VOLUME_BRIDGE", "symbol": "103140", "company": "Poongsan", "trigger_type": "Stage2-Actionable", "case_role": "positive", "trigger_date": "2021-02-22", "entry_date": "2021-02-22", "entry_price": 36600.0, "actual_1d_ohlcv": {"o": 33950.0, "h": 37400.0, "l": 33700.0, "c": 36600.0, "v": 2877677}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2021.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "profile_note": "profile checked: 0 corporate-action candidates, 2008-07-30~2026-02-20 active-like", "forward_window": {"MFE_30D_pct": 8.47, "MAE_30D_pct": -14.89, "MFE_90D_pct": 36.48, "MAE_90D_pct": -14.89, "MFE_180D_pct": 36.48, "MAE_180D_pct": -14.89, "peak_date_180D": "2021-05-12", "peak_price_180D": 49950.0, "trough_after_peak_date_180D": "2021-11-11", "drawdown_after_peak_pct": -37.64, "window_last_date_180D": "2021-11-12", "forward_rows_available": 1224}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "Copper near US$9,000/t and 2021 OP growth expectations provided a clean price-volume bridge before Poongsan rerated.", "evidence_url": "https://www.businesskorea.co.kr/news/articleView.html?idxno=60900", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 10, "bottleneck_pricing": 19, "market_mispricing": 9, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 12}, "score_simulation": {"current_profile_stage": "Stage2-Actionable", "current_profile_score": 77, "shadow_stage": "Stage2-Actionable", "shadow_score": 81}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|103140|Stage2-Actionable|2021-02-22", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "clean copper-price positive, but MAE still argues Yellow/Actionable rather than Green unless sell-through and hedge quality are verified"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_04_POSCO_2021_RECORD_BUT_QOQ_MARGIN_ROLLOVER", "symbol": "005490", "company": "POSCO Holdings", "trigger_type": "Stage4B", "case_role": "guardrail", "trigger_date": "2022-01-28", "entry_date": "2022-01-28", "entry_price": 265000.0, "actual_1d_ohlcv": {"o": 260000.0, "h": 267000.0, "l": 256500.0, "c": 265000.0, "v": 333753}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2022.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "profile_note": "profile checked: 0 corporate-action candidates, 1995-05-02~2026-02-20 active-like", "forward_window": {"MFE_30D_pct": 11.13, "MAE_30D_pct": -3.21, "MFE_90D_pct": 15.66, "MAE_90D_pct": -3.21, "MFE_180D_pct": 15.66, "MAE_180D_pct": -20.38, "peak_date_180D": "2022-03-23", "peak_price_180D": 306500.0, "trough_after_peak_date_180D": "2022-09-30", "drawdown_after_peak_pct": -31.16, "window_last_date_180D": "2022-10-26", "forward_rows_available": 746}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "2021 release showed record annual steel profit but also 4Q profit downturn / consolidated steel margin tightening from raw-material cost pressure.", "evidence_url": "https://www.posco.co.kr/homepage/servlet/FileDownLoad?fileCategory=irDataFd&fileNum=407", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 18, "earnings_visibility": 11, "bottleneck_pricing": 13, "market_mispricing": 7, "valuation_rerating": 7, "capital_allocation": 5, "information_confidence": 15}, "score_simulation": {"current_profile_stage": "Stage2", "current_profile_score": 76, "shadow_stage": "Stage4B", "shadow_score": 60}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|005490|Stage4B|2022-01-28", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "record annual earnings can be a lagging signal once QoQ steel margin has rolled over"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_05_POONGSAN_2022_HIGH_BASE_COPPER_COUNTER", "symbol": "103140", "company": "Poongsan", "trigger_type": "Stage4B", "case_role": "counterexample", "trigger_date": "2022-03-18", "entry_date": "2022-03-18", "entry_price": 32450.0, "actual_1d_ohlcv": {"o": 32400.0, "h": 32450.0, "l": 31900.0, "c": 32450.0, "v": 136535}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2022.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "profile_note": "profile checked: 0 corporate-action candidates, 2008-07-30~2026-02-20 active-like", "forward_window": {"MFE_30D_pct": 4.62, "MAE_30D_pct": -4.01, "MFE_90D_pct": 4.62, "MAE_90D_pct": -28.2, "MFE_180D_pct": 4.62, "MAE_180D_pct": -28.2, "peak_date_180D": "2022-03-24", "peak_price_180D": 33950.0, "trough_after_peak_date_180D": "2022-07-04", "drawdown_after_peak_pct": -31.37, "window_last_date_180D": "2022-12-07", "forward_rows_available": 960}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "Mirae Asset expected record 2022 revenue on copper strength, while explicitly warning operating profit would contract due to the high-base effect.", "evidence_url": "https://securities.miraeasset.com/bbs/download/2091868.pdf?attachmentId=2091868", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 11, "earnings_visibility": 9, "bottleneck_pricing": 18, "market_mispricing": 9, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 16}, "score_simulation": {"current_profile_stage": "Stage2", "current_profile_score": 75, "shadow_stage": "Stage4B", "shadow_score": 56}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|103140|Stage4B|2022-03-18", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "high-base language must cap C15 Stage2 because spread persistence is no longer incremental"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_06_SOIL_Q2_2022_REFINING_MARGIN_LATE", "symbol": "010950", "company": "S-Oil", "trigger_type": "Stage2-Actionable", "case_role": "mixed_green_blocker", "trigger_date": "2022-07-28", "entry_date": "2022-07-28", "entry_price": 91300.0, "actual_1d_ohlcv": {"o": 93600.0, "h": 93800.0, "l": 90500.0, "c": 91300.0, "v": 538463}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010950/2022.csv", "profile_path": "atlas/symbol_profiles/010/010950.json", "profile_note": "profile checked: corporate-action candidate 2001-12-03 only; selected 2022/2023 windows not contaminated", "forward_window": {"MFE_30D_pct": 18.84, "MAE_30D_pct": -7.12, "MFE_90D_pct": 18.84, "MAE_90D_pct": -15.12, "MFE_180D_pct": 18.84, "MAE_180D_pct": -17.63, "peak_date_180D": "2022-08-30", "peak_price_180D": 108500.0, "trough_after_peak_date_180D": "2023-03-27", "drawdown_after_peak_pct": -30.69, "window_last_date_180D": "2023-04-19", "forward_rows_available": 869}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "Q2 2022 net profit more than doubled on widened refining margins and higher oil prices, but the outcome path showed late-cycle drawdown risk.", "evidence_url": "https://en.yna.co.kr/view/AEN20220728002252320", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 17, "earnings_visibility": 9, "bottleneck_pricing": 18, "market_mispricing": 7, "valuation_rerating": 8, "capital_allocation": 5, "information_confidence": 15}, "score_simulation": {"current_profile_stage": "Stage2-Actionable", "current_profile_score": 79, "shadow_stage": "Stage2", "shadow_score": 68}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|010950|Stage2-Actionable|2022-07-28", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "refining margin and inventory gains are actionable but should be Green-blocked without forward crack-spread persistence"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_07_SKI_Q2_2022_INVENTORY_GAIN_WORKING_CAPITAL_OFFSET", "symbol": "096770", "company": "SK Innovation", "trigger_type": "Stage2-Actionable", "case_role": "mixed_green_blocker", "trigger_date": "2022-07-29", "entry_date": "2022-07-29", "entry_price": 187500.0, "actual_1d_ohlcv": {"o": 183000.0, "h": 191000.0, "l": 182500.0, "c": 187500.0, "v": 688623}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2022.csv", "profile_path": "atlas/symbol_profiles/096/096770.json", "profile_note": "profile checked: corporate-action candidate 2024-11-20; selected 2022/2023 D~D+180 windows end before that date", "forward_window": {"MFE_30D_pct": 13.87, "MAE_30D_pct": -5.33, "MFE_90D_pct": 13.87, "MAE_90D_pct": -24.0, "MFE_180D_pct": 13.87, "MAE_180D_pct": -24.0, "peak_date_180D": "2022-08-17", "peak_price_180D": 213500.0, "trough_after_peak_date_180D": "2022-09-30", "drawdown_after_peak_pct": -33.26, "window_last_date_180D": "2023-04-20", "forward_rows_available": 868}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "Q2 2022 results showed KRW2.33T operating profit from improved refining margins and inventory gains, while crude costs lifted net working capital and battery losses persisted.", "evidence_url": "https://askinno.com/global/archives/10897", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 18, "earnings_visibility": 8, "bottleneck_pricing": 18, "market_mispricing": 7, "valuation_rerating": 7, "capital_allocation": 4, "information_confidence": 16}, "score_simulation": {"current_profile_stage": "Stage2-Actionable", "current_profile_score": 78, "shadow_stage": "Stage2", "shadow_score": 64}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|096770|Stage2-Actionable|2022-07-29", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "inventory-gain positive needs working-capital/debt offset before Yellow or Green"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_08_SOIL_2023_WEAK_REFINING_MARGIN_4C", "symbol": "010950", "company": "S-Oil", "trigger_type": "Stage4C", "case_role": "correct_4c", "trigger_date": "2023-04-25", "entry_date": "2023-04-25", "entry_price": 77000.0, "actual_1d_ohlcv": {"o": 77700.0, "h": 78300.0, "l": 76800.0, "c": 77000.0, "v": 272017}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010950/2023.csv", "profile_path": "atlas/symbol_profiles/010/010950.json", "profile_note": "profile checked: corporate-action candidate 2001-12-03 only; selected 2022/2023 windows not contaminated", "forward_window": {"MFE_30D_pct": 1.69, "MAE_30D_pct": -8.31, "MFE_90D_pct": 4.29, "MAE_90D_pct": -19.22, "MFE_180D_pct": 5.06, "MAE_180D_pct": -19.22, "peak_date_180D": "2023-09-15", "peak_price_180D": 80900.0, "trough_after_peak_date_180D": "2024-01-17", "drawdown_after_peak_pct": -20.02, "window_last_date_180D": "2024-01-19", "forward_rows_available": 685}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "2023 S-Oil operating profit later more than halved as weak refining margins compressed the oil-refining business.", "evidence_url": "https://www.kedglobal.com/earnings/newsView/ked202402020003", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 7, "bottleneck_pricing": 8, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 4, "information_confidence": 12}, "score_simulation": {"current_profile_stage": "Stage4B", "current_profile_score": 62, "shadow_stage": "Stage4C", "shadow_score": 49}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|010950|Stage4C|2023-04-25", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "when refining-margin weakness is not just local price volatility but earnings-quality deterioration, hard 4C is appropriate"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "selected_round": "R4", "selected_loop": 192, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE", "case_id": "C15_192_09_SKI_Q4_2022_INVENTORY_LOSS_OFFSET_CHECK", "symbol": "096770", "company": "SK Innovation", "trigger_type": "Stage4C", "case_role": "overhard_4c_offset_check", "trigger_date": "2023-02-07", "entry_date": "2023-02-07", "entry_price": 162600.0, "actual_1d_ohlcv": {"o": 171200.0, "h": 175000.0, "l": 162600.0, "c": 162600.0, "v": 1554857}, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv", "profile_path": "atlas/symbol_profiles/096/096770.json", "profile_note": "profile checked: corporate-action candidate 2024-11-20; selected 2022/2023 D~D+180 windows end before that date", "forward_window": {"MFE_30D_pct": 10.64, "MAE_30D_pct": -7.75, "MFE_90D_pct": 28.54, "MAE_90D_pct": -7.75, "MFE_180D_pct": 41.14, "MAE_180D_pct": -26.14, "peak_date_180D": "2023-07-26", "peak_price_180D": 229500.0, "trough_after_peak_date_180D": "2023-11-01", "drawdown_after_peak_pct": -47.67, "window_last_date_180D": "2023-11-01", "forward_rows_available": 739}, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "evidence_summary": "Q4 2022 operating loss widened on inventory losses from lower oil prices and narrower margins, while battery revenue ramp provided a separate offset option.", "evidence_url": "https://en.yna.co.kr/view/AEN20230207002351320", "evidence_ref": "direct_evidence_url_checked", "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 7, "bottleneck_pricing": 6, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 5, "information_confidence": 14}, "score_simulation": {"current_profile_stage": "Stage4C", "current_profile_score": 54, "shadow_stage": "Stage4B", "shadow_score": 59}, "duplicate_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|096770|Stage4C|2023-02-07", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true, "residual_label": "hard 4C on refining/inventory loss needs offset-check where another segment has credible ramp optionality"}
```

## 12. Coverage Matrix Update

| Dimension | This batch contribution |
|---|---|
| broad commodity family | steel, copper, refining |
| positive templates | POSCO 2020 recovery, Poongsan copper bridge |
| counterexample templates | Hyundai late steel chase, Poongsan high-base copper, POSCO record-profit rollover |
| 4B/4C templates | POSCO local margin rollover, S-Oil weak refining margin, SKI hard-4C offset check |
| green-blocker templates | refining margin/inventory gain with forward-spread uncertainty, working-capital/debt offset |
| new duplicate keys | 9 |
| price validation | all rows include actual stock-web OHLCV and 30/90/180D MFE/MAE |

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not execute automatically.

Review the v12 C15 material-spread residual batch:
e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

Validate JSONL rows, confirm duplicate keys, and run the calibration parser.
If accepted, stage only shadow-profile changes for:
- C15_SPREAD_PERSISTENCE_AND_INVENTORY_GAIN_GATE
- C15_HARD_4C_OFFSET_CHECK
Do not change production scoring without promotion planner approval.
```

## 14. Next Research State

```text
completed_round: R4
completed_loop: 192
completed_large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
completed_canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
completed_fine_archetype_id: STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE

next_recommended_archetypes:
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- C02_POWER_GRID_DATACENTER_CAPEX
- C14_EV_DEMAND_SLOWDOWN_4B_4C
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP
- C15_STRATEGIC_RESOURCE_4C_OFFSET_REPAIR

next_research_note:
Continue quality reinforcement, not row-count filling.  Prefer direct evidence URL repair,
missing-MFE repair, and 4B/4C balance rows over more duplicate high-row symbols.
```
